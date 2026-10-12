"""Read exact published Git blobs; verify package, declarations and queue identity."""
from pathlib import Path
import collections
import hashlib
import json
import subprocess
import sys

BASE = Path(__file__).resolve().parent.parent
REPO = BASE / 'prof-iteration'
PIN = sys.argv[1]
EXPECTED_CLOSED = int(sys.argv[2]) if len(sys.argv) > 2 else 15
OUT = Path(__file__).resolve().parent / PIN
OUT.mkdir(exist_ok=True)
PREV = sys.argv[4]
CANDIDATE = BASE / 'd008-clean-r35-20261012/release-prof'
INCOMING = json.loads((BASE / 'd008-clean-r35-20261012/inputs/prof-package-manifest.json').read_text())
PACKAGE_PATHS = [x['path'] for x in INCOMING['files']]
RAW_PUBLICATION = json.loads((BASE / sys.argv[3]).read_text())
PUBLICATION_MAP = [dict(x, local_path=x.get('local', x.get('local_path')), git_blob=x.get('sha', x.get('git_blob'))) for x in (RAW_PUBLICATION if isinstance(RAW_PUBLICATION,list) else RAW_PUBLICATION.get('entries', RAW_PUBLICATION.get('files', [])))]
assert PUBLICATION_MAP
QUEUE = 'runs/y1-reader-20261008/queue.json'

def git(*args):
    return subprocess.run(['git', '-C', str(REPO), *args], check=True, stdout=subprocess.PIPE).stdout

def sha(data):
    return hashlib.sha256(data).hexdigest()

changes = [line.split('\t') for line in git('diff', '--name-status', PREV, PIN).decode().splitlines()]
changed_paths = [row[-1] for row in changes]
requests = list(dict.fromkeys([f'{PIN}:{p}' for p in PACKAGE_PATHS + changed_paths + [x['path'] for x in PUBLICATION_MAP] + [QUEUE]] + [f'{PREV}:{QUEUE}']))
result = subprocess.run(['git', '-C', str(REPO), 'cat-file', '--batch'], input=('\n'.join(requests)+'\n').encode(), check=True, stdout=subprocess.PIPE)
raw = result.stdout
pos = 0
data = {}
blobs = {}
for request in requests:
    end = raw.index(b'\n', pos)
    header = raw[pos:end].decode().split()
    assert len(header) == 3 and header[1] == 'blob', (request, header)
    size = int(header[2])
    content = raw[end+1:end+1+size]
    assert len(content) == size and raw[end+1+size:end+2+size] == b'\n'
    blob = hashlib.sha1(b'blob '+str(size).encode()+b'\0'+content).hexdigest()
    assert blob == header[0], request
    data[request] = content
    blobs[request] = blob
    pos = end+2+size
assert pos == len(raw)

records = []
for path in PACKAGE_PATHS:
    content = data[f'{PIN}:{path}']
    local = (CANDIDATE/path).read_bytes()
    assert content == local, path
    target = OUT/'fetched-prof'/path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    records.append({'path': path, 'bytes': len(content), 'sha256': sha(content), 'git_blob': blobs[f'{PIN}:{path}'], 'candidate_byte_equal': True})
assert len(records) == 36
publication_map_checks = []
for item in PUBLICATION_MAP:
    content = data[f"{PIN}:{item['path']}"]
    local = Path(item['local_path']).read_bytes()
    assert content == local, item['path']
    assert len(content) == item['bytes'] and sha(content) == item['sha256'], item['path']
    assert blobs[f"{PIN}:{item['path']}"] == item['git_blob'], item['path']
    publication_map_checks.append({'path': item['path'], 'bytes': len(content), 'sha256': sha(content), 'git_blob': item['git_blob'], 'actual_published_equals_local': True})

mapping = json.loads((BASE/'root-review-d008-r31-publication/corrected-release-readback.json').read_text())['all34_internal_bundled_hash_references_checked_on_fetched_bytes']
declarations = []
for item in mapping:
    obj = json.loads(data[f"{PIN}:{item['declaring_file']}"])
    entry = item['entry']
    if entry.startswith('/file_hashes/'):
        declared = obj['file_hashes'][entry[len('/file_hashes/'):]]
    elif entry.startswith('/control_file_hashes/'):
        declared = obj['control_file_hashes'][entry[len('/control_file_hashes/'):]]
    else:
        declared = obj
        for part in entry.strip('/').split('/'):
            declared = declared[int(part)] if isinstance(declared, list) else declared[part]
    actual = sha(data[f"{PIN}:{item['target']}"])
    assert declared == actual, item
    declarations.append({'declaring_file': item['declaring_file'], 'entry': entry, 'target': item['target'], 'declared': declared, 'actual_sha256': actual, 'match': True})
assert len(declarations) == 34

before = json.loads(data[f'{PREV}:{QUEUE}'])
after = json.loads(data[f'{PIN}:{QUEUE}'])
identity = lambda q: [(x['material_id'],x['id'],x['order'],bool(x.get('readability',{}).get('eligible'))) for x in q['sessions']]
assert identity(before) == identity(after)
assert len(after['sessions']) == 147
status_changes = [{'material_id': a['material_id'], 'before': b['status'], 'after': a['status']} for b,a in zip(before['sessions'],after['sessions']) if b['status'] != a['status']]
assert all(x['material_id']=='D008' and x['after']=='closed' for x in status_changes), status_changes
counts = collections.Counter(x['status'] for x in after['sessions'])
assert counts['closed'] == EXPECTED_CLOSED and counts['excluded_by_user_readability_scope'] == 71, counts
assert sum(counts.values()) == 147

published_records = []
for path in changed_paths:
    content = data[f'{PIN}:{path}']
    target = OUT/'published-files'/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(content)
    published_records.append({'path': path, 'bytes': len(content), 'sha256': sha(content), 'git_blob': blobs[f'{PIN}:{path}']})

report = {'pin': PIN, 'predecessor': PREV, 'complete_package_count': len(records), 'complete_package_bytes': sum(x['bytes'] for x in records), 'full_actual_blob_reads': len(requests), 'package': records, 'all34_internal_declarations': declarations, 'changes': changes, 'published_changed_files': published_records, 'all_publication_map_entries': publication_map_checks, 'queue_identity147_order_and_eligibility_unchanged': True, 'queue_status_changes': status_changes, 'queue_status_counts': dict(counts), 'queue_sha256': sha(data[f'{PIN}:{QUEUE}']), 'limits': 'Mechanical full-blob identity verification; semantic adjudication and archive reassembly checks are recorded separately.'}
(OUT/'release-readback.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['pin','predecessor','complete_package_count','complete_package_bytes','full_actual_blob_reads','queue_status_changes','queue_status_counts','queue_identity147_order_and_eligibility_unchanged']},indent=2))
