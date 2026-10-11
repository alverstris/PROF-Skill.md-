"""Read-only identity reconciliation of unchanged frozen material."""
from pathlib import Path
import json, subprocess, hashlib

repo = '/workspace/scratch/f9c0b7fc7e76/prof-iteration'
local = Path('/workspace/scratch/f9c0b7fc7e76/d016-r26b')
output = Path(__file__).resolve().parent
current = '54ebb635d842f1d65c2508b8f921fd32819f5f0c'
frozen = '51a78beccef858072b1da8d057ef3dff09878409'
base = 'runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b'

def tree(commit, root=None):
    args = ['git', '-C', repo, 'ls-tree', '-r', commit]
    if root:
        args.append(root)
    lines = subprocess.check_output(args, text=True).splitlines()
    return {x.split('\t')[1]: x.split('\t')[0].split()[2] for x in lines}

def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def sha(data):
    return hashlib.sha256(data).hexdigest()

current_tree = tree(current)
frozen_tree = tree(frozen, base)
manifest = json.loads((local/'freeze-manifest.json').read_text())
files = []
for item in manifest['files']:
    p = item['path']
    data = (local/p).read_bytes()
    files.append({'path': p, 'sha256': sha(data), 'current_main_blob': current_tree[base+'/'+p],
                  'frozen_commit_blob': frozen_tree[base+'/'+p], 'local_blob': blob(data),
                  'match': blob(data) == current_tree[base+'/'+p] == frozen_tree[base+'/'+p]
                           and sha(data) == item['sha256']})
reviews = []
for p, oid in current_tree.items():
    if not p.startswith(base+'/'):
        continue
    relative = p[len(base)+1:]
    if relative.startswith('review/') or relative in ['pending-status.json', '.prof-state/manifest.json', '.prof-state/topics/definite-integrals.json']:
        data = (local/relative).read_bytes()
        reviews.append({'path': relative, 'sha256': sha(data), 'git_blob': oid,
                        'local_blob': blob(data), 'match': oid == blob(data)})
package = []
for item in json.loads((local/'package-verification.json').read_text())['files']:
    p = item['path']
    data = (local/'inputs/prof'/p).read_bytes()
    package.append({'path': p, 'sha256': sha(data), 'git_blob': current_tree[p],
                    'local_blob': blob(data), 'match': blob(data) == current_tree[p] and sha(data) == item['sha256']})
result = {'current_main': current, 'frozen_commit': frozen,
          'method': 'Compare exact local byte Git object identities against the fetched immutable Git trees; independently compare SHA256 with preserved manifests. No semantic audit repeated.',
          'frozen_files': files, 'review_state_files': reviews, 'package_files': package,
          'all_match': all(item['match'] for item in files+reviews+package)}
(output/'git-tree-identity-check.json').write_text(json.dumps(result, indent=2)+'\n')
print('all_match', result['all_match'], 'frozen', len(files), 'review_state', len(reviews), 'package', len(package))
