import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--manifest', required=True)
parser.add_argument('--commit', required=True)
parser.add_argument('--receipt', required=True)
args = parser.parse_args()
repo = '/workspace/scratch/f9c0b7fc7e76/prof-iteration'
items = json.loads(Path(args.manifest).read_text())
if isinstance(items, dict):
    items = items['files']
shas = list(dict.fromkeys(x['git_blob'] for x in items))
fetch = subprocess.run(['git', 'fetch', 'origin', '--stdin'], cwd=repo,
                       input=('\n'.join(shas) + '\n').encode(), stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=True)
subprocess.run(['git', 'fetch', 'origin', args.commit], cwd=repo,
               stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
requests = ''.join(f"{args.commit}:{x['path']}\n" for x in items).encode()
raw = subprocess.run(['git', 'cat-file', '--batch'], cwd=repo,
                     input=requests, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     check=True).stdout
pos = 0
results = []
for item in items:
    end = raw.index(b'\n', pos)
    header = raw[pos:end].decode().split()
    assert len(header) == 3 and header[1] == 'blob', (item['path'], header)
    size = int(header[2])
    body = raw[end + 1:end + 1 + size]
    assert raw[end + 1 + size:end + 2 + size] == b'\n'
    pos = end + 2 + size
    digest = hashlib.sha256(body).hexdigest()
    blob = hashlib.sha1(b'blob ' + str(size).encode() + b'\0' + body).hexdigest()
    assert size == item['bytes'] and digest == item['sha256'] and blob == item['git_blob'] == header[0], item['path']
    if item.get('local_path'):
        assert Path(item['local_path']).read_bytes() == body, item['path']
    results.append({'path': item['path'], 'bytes': size, 'sha256': digest,
                    'git_blob': blob, 'full_byte_match': True})
assert pos == len(raw)
tree = subprocess.run(['git', 'rev-parse', f'{args.commit}^{{tree}}'], cwd=repo,
                      stdout=subprocess.PIPE, check=True).stdout.decode().strip()
receipt = {'utc': datetime.now(timezone.utc).isoformat(), 'commit': args.commit,
           'tree': tree, 'method': 'Read-only exact blob prefetch followed by complete binary cat-file --batch resolution of every explicit published path; actual byte/hash/blob comparisons.',
           'files': results, 'count': len(results), 'all_match': True}
Path(args.receipt).write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'commit': args.commit, 'tree': tree, 'count': len(results), 'all_match': True}))
