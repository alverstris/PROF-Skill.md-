from pathlib import Path
import difflib
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(r'C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae')
BASE = Path(r'C:/Users/alver/.codex/skills/prof')
STAGE = ROOT / '.prof-maintenance/20261014/prof-r40-candidate'
REVIEW = ROOT / '.prof-maintenance/20261014/prof-r40-review'
VALIDATOR = Path(r'C:/Users/alver/.codex/skills/.system/skill-creator/scripts/quick_validate.py')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inventory(root):
    return {p.relative_to(root).as_posix(): sha(p) for p in sorted(root.rglob('*')) if p.is_file()}

base = inventory(BASE)
candidate = inventory(STAGE)
assert set(base) == set(candidate)
assert len(candidate) == 36
changed = sorted(p for p in base if base[p] != candidate[p])
expected = sorted([
    'SKILL.md', 'references/execution-protocol.md', 'references/sasis.md',
    'references/sasis/profile-manifest.json', 'references/sasis/student-role.txt',
    'references/sasis/student-testing-contract.txt',
])
assert changed == expected, changed
assert (STAGE / 'SKILL.md').read_bytes() == (BASE / 'SKILL.md').read_bytes().replace(b'version: "2026-10-14-r39"', b'version: "2026-10-14-r40"', 1)
frozen = [p for p in base if p.startswith('references/sasis/ocr-baseline-20261007/')]
assert all(base[p] == candidate[p] for p in frozen)
assert len(frozen) == 19

for path in STAGE.rglob('*.json'):
    json.loads(path.read_text(encoding='utf-8'))

manifest_path = STAGE / 'references/sasis/profile-manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
base_manifest = json.loads((BASE / 'references/sasis/profile-manifest.json').read_text(encoding='utf-8'))
checks = []
def check(label, path, declared):
    actual = sha(path)
    assert actual == declared, (label, actual, declared)
    checks.append({'reference': label, 'path': path.relative_to(STAGE).as_posix(), 'sha256': actual, 'result': 'pass'})

for entry in manifest['subject_files']:
    check('profile.subject_files:' + entry['path'], manifest_path.parent / entry['path'], entry['sha256'])
for relative, declared in manifest['file_hashes'].items():
    check('profile.file_hashes:' + relative, manifest_path.parent / manifest['file_hashes_base_directory'] / relative, declared)
for relative, declared in manifest['control_file_hashes'].items():
    check('profile.control_file_hashes:' + relative, manifest_path.parent / relative, declared)
assert len(checks) == 26
assert manifest['file_hashes'] == base_manifest['file_hashes']
assert manifest['subject_files'] == base_manifest['subject_files']
assert manifest['baseline_revision'] == base_manifest['baseline_revision']
assert manifest['control_file_hashes']['rewrite-guide.md'] == base_manifest['control_file_hashes']['rewrite-guide.md']

baseline_root = manifest_path.parent / manifest['file_hashes_base_directory']
release = json.loads((baseline_root / 'release-manifest.json').read_text(encoding='utf-8'))
for entry in release['subjects']:
    check('release.subjects:' + entry['path'], baseline_root / entry['path'], entry['sha256'])
check('release.combined_baseline_sha256', baseline_root / 'student-baseline.txt', release['combined_baseline_sha256'])
chem_root = baseline_root / 'chemistry'
chem = json.loads((chem_root / 'freeze-manifest.json').read_text(encoding='utf-8'))
historical_unbundled = []
for entry in chem['files']:
    path = chem_root / entry['path']
    if path.is_file():
        check('chemistry.freeze.files:' + entry['path'], path, entry['sha256'])
        assert path.stat().st_size == entry['bytes']
    else:
        historical_unbundled.append({'manifest': 'chemistry/freeze-manifest.json', 'path': entry['path'], 'classification': 'unchanged historical authoring artifact, not an installed payload'})

environment = os.environ.copy()
environment['PYTHONPATH'] = str(ROOT / '.prof-maintenance/20261014/validation-deps')
validation = subprocess.run([sys.executable, str(VALIDATOR), str(STAGE)], env=environment, capture_output=True, text=True)
assert validation.returncode == 0, validation.stdout + validation.stderr

diff = []
for relative in changed:
    before = (BASE / relative).read_text(encoding='utf-8').splitlines(keepends=True)
    after = (STAGE / relative).read_text(encoding='utf-8').splitlines(keepends=True)
    diff.extend(difflib.unified_diff(before, after, fromfile='r39/' + relative, tofile='r40/' + relative))
(REVIEW / 'root-package.diff').write_text(''.join(diff), encoding='utf-8', newline='\n')

report = {
    'candidate_revision': '2026-10-14-r40', 'candidate_path': str(STAGE),
    'base_commit': '51abe635150f97baf5b5e84965a66588b208e37b',
    'package_file_count': 36, 'changed_files': changed, 'unchanged_files': 30,
    'frozen_baseline_payloads_byte_identical': len(frozen),
    'entrypoint_change_is_metadata_only': True,
    'all_package_json_parses': True,
    'operative_profile_manifest_checks': 26,
    'additional_local_frozen_manifest_checks': len(checks) - 26,
    'manifest_checks': checks,
    'historical_unbundled_references_preserved': historical_unbundled,
    'validator': {'path': str(VALIDATOR), 'returncode': validation.returncode, 'stdout': validation.stdout.strip(), 'stderr': validation.stderr.strip()},
    'control_hash_changes': {p: {'before': base_manifest['control_file_hashes'][p], 'after': manifest['control_file_hashes'][p]} for p in manifest['control_file_hashes'] if base_manifest['control_file_hashes'][p] != manifest['control_file_hashes'][p]},
    'candidate_sha256': candidate,
    'behavior_validation': 'pending: root must integrate actual sealed-adapter synthetic preflight evidence before release; fresh complete generation, complete SASIS reading, technical/destination checks and affected successes are not established by this validation',
    'publication_installation_generation_performed': False,
}
(REVIEW / 'validation-results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in report.items() if k not in {'manifest_checks', 'candidate_sha256'}}, indent=2))
