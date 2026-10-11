"""Preserve the pending state and create an additive relocated final-check project.

This preparation does not promote any pending/unverified record.
"""
from pathlib import Path
import hashlib, json, shutil, subprocess

base = Path(__file__).resolve().parent
source = Path('/workspace/scratch/f9c0b7fc7e76/d016-r26b')
target = base/'final-project'
if target.exists():
    raise SystemExit('Refusing to overwrite existing final-check project')
shutil.copytree(source, target, ignore=shutil.ignore_patterns('__pycache__'))

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

copies = []
for p in sorted(target.rglob('*')):
    if p.is_file():
        rel = p.relative_to(target)
        copies.append({'path': str(rel), 'sha256': sha(p), 'source_sha256': sha(source/rel),
                       'match': p.read_bytes() == (source/rel).read_bytes()})
assert all(x['match'] for x in copies)
state = target/'.prof-state'
manifest = json.loads((state/'manifest.json').read_text())
old_root = manifest['project_root']
manifest['project_root'] = str(target)
(state/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
tool = source/'inputs/prof/scripts/prof_state.py'
dependencies = json.loads(subprocess.check_output(['python', str(tool), 'dependencies', '--state', str(state)], text=True))
for check in manifest['output_checks']:
    if check['status'] == 'pass':
        old = {(x['kind'], x['id']): x['sha256'] for x in check['dependencies']}
        new = {(x['kind'], x['id']): x['sha256'] for x in dependencies}
        changed = [key for key in old.keys() | new.keys() if old.get(key) != new.get(key)]
        assert changed == [('inventory', '')], changed
        check['dependencies'] = dependencies
(state/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
record = {'purpose': 'Identity-only local relocation for additive final evidence; no status promoted.',
          'original_project_root': old_root, 'final_project_root': str(target),
          'copies_verified_before_state_relocation': copies,
          'dependency_delta': 'Only global inventory digest changes, because project_root changes. All topic and subject-content dependencies are identical.'}
(base/'final-state-relocation.json').write_text(json.dumps(record, indent=2)+'\n')
for name, args in [('topic', ['--topic', 'definite-integrals']), ('full', [])]:
    result = subprocess.run(['python', str(tool), 'check', '--state', str(state), *args], text=True, capture_output=True)
    (base/f'prepared-{name}-check.txt').write_text(result.stdout+result.stderr)
    print(name, result.returncode, result.stdout.strip())
