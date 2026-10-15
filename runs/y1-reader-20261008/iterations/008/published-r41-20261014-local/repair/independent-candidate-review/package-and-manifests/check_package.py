"""Read-only independent pinned-Git, candidate and installed package review."""
from pathlib import Path
import collections
import difflib
import hashlib
import json
import posixpath
import re
import subprocess

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[3]
CANDIDATE = PROJECT / '.prof-sasis/20261014-d008-r41/procedure-candidate'
REPO = PROJECT / '.prof-maintenance/20261014/repository'
INSTALLED = Path('C:/Users/alver/.codex/skills/prof')
COMMIT = '2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce'
EXPECTED_SEAL = '7679387d9640b65221c959ec314fdd145da419b72389393662933ddd167e65dc'
EXPECTED_CHANGED = {'SKILL.md', 'references/sasis.md', 'references/sasis/student-role.txt', 'references/sasis/student-testing-contract.txt', 'references/sasis/profile-manifest.json'}
errors = []


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def oid(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def check(ok, name, detail=None):
    if not ok:
        errors.append({'check': name, 'detail': detail})


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


seal_raw = (CANDIDATE / 'REVIEW-SEAL.json').read_bytes()
check(sha(seal_raw) == EXPECTED_SEAL, 'review_seal_expected_hash', sha(seal_raw))
seal = json.loads(seal_raw)
sealed_files = []
sealed_raw = {}
for name, identity in seal['files'].items():
    raw = (CANDIDATE / name).read_bytes()
    sealed_raw[name] = raw
    measured = {'bytes': len(raw), 'sha256': sha(raw)}
    check(identity == measured, 'review_sealed_file', name)
    sealed_files.append({'path': name, **measured, 'matches_seal': identity == measured})

tree = {}
for entry in filter(None, git('ls-tree', '-rz', COMMIT).split(b'\0')):
    meta, raw_name = entry.split(b'\t', 1)
    name = raw_name.decode('utf-8')
    mode, kind, blob = meta.decode('ascii').split()
    if name == 'SKILL.md' or name.split('/')[0] in {'agents', 'assets', 'references', 'scripts'}:
        check(kind == 'blob' and mode == '100644', 'package_regular_git_blob', {'path': name, 'kind': kind, 'mode': mode})
        tree[name] = {'git_blob_sha': blob, 'git_mode': mode}
check(len(tree) == 36, 'pinned_package_file_count', len(tree))
source = {name: git('cat-file', 'blob', item['git_blob_sha']) for name, item in tree.items()}
for name, raw in source.items():
    check(oid(raw) == tree[name]['git_blob_sha'], 'pinned_blob_identity_recomputed', name)

proposed_root = CANDIDATE / 'proposed-package'
proposed_paths = [p for p in proposed_root.rglob('*') if p.is_file()]
proposed = {p.relative_to(proposed_root).as_posix(): p.read_bytes() for p in proposed_paths}
check(set(proposed) == EXPECTED_CHANGED, 'actual_candidate_overlay_inventory', sorted(proposed))
check(not any(p.is_symlink() or p.is_junction() for p in proposed_root.rglob('*')), 'candidate_no_symlink_or_junction')
merged = {name: proposed.get(name, raw) for name, raw in source.items()}
check(set(merged) == set(tree) and len(merged) == 36, 'complete_merged_inventory')
changed = sorted(name for name in merged if merged[name] != source[name])
check(set(changed) == EXPECTED_CHANGED, 'actual_changed_files', changed)

installed_paths = [p for p in INSTALLED.rglob('*') if p.is_file()]
installed = {p.relative_to(INSTALLED).as_posix(): p.read_bytes() for p in installed_paths}
installed_extras = sorted(set(installed) - set(tree))
installed_missing = sorted(set(tree) - set(installed))
installed_changed = sorted(name for name in set(installed) & set(source) if installed[name] != source[name])
check(not installed_extras and not installed_missing and not installed_changed, 'installed_exact_pinned_inventory_and_bytes', {'extras': installed_extras, 'missing': installed_missing, 'changed': installed_changed})
check(not any(p.is_symlink() or p.is_junction() for p in INSTALLED.rglob('*')), 'installed_no_symlink_or_junction')
package_rows = []
for name in sorted(tree):
    before, after = source[name], merged[name]
    package_rows.append({'path': name, 'source_git_blob_sha': tree[name]['git_blob_sha'], 'source_bytes': len(before), 'source_sha256': sha(before), 'proposed_bytes': len(after), 'proposed_sha256': sha(after), 'proposed_git_blob_sha': oid(after), 'changed': before != after, 'installed_bytes': len(installed[name]) if name in installed else None, 'installed_sha256': sha(installed[name]) if name in installed else None, 'installed_equals_pinned': installed.get(name) == before})

independent_diff = ''.join(''.join(difflib.unified_diff(source[name].decode('utf-8').splitlines(keepends=True), merged[name].decode('utf-8').splitlines(keepends=True), fromfile='pinned-r40/' + name, tofile='candidate-r41/' + name, n=3)) for name in changed)
(OUT / 'actual-five-file.diff').write_bytes(independent_diff.encode('utf-8'))

profile_name = 'references/sasis/profile-manifest.json'
old = json.loads(source[profile_name])
new = json.loads(merged[profile_name])
allowed_fields = {'control_file_hashes', 'protocol_revision', 'protocol_update_notes'}
actual_field_changes = sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k))
check(set(actual_field_changes) == allowed_fields, 'actual_profile_changed_fields', actual_field_changes)
check(new['protocol_revision'] == '2026-10-14-r41', 'manifest_revision')
check(new['file_hashes'] == old['file_hashes'] and len(new['file_hashes']) == 19, 'frozen_baseline_manifest_identities_unchanged')
check(new['subject_files'] == old['subject_files'], 'subject_file_records_unchanged')
check(new['protocol_update_notes'][:-1] == old['protocol_update_notes'] and len(new['protocol_update_notes']) == len(old['protocol_update_notes']) + 1, 'exact_existing_notes_preserved_one_appended')
manifest_checks = []


def manifest_check(group, relative, expected):
    name = posixpath.normpath('references/sasis/' + relative)
    check(name in merged and not name.startswith('../'), 'manifest_path_within_package', name)
    actual = sha(merged[name]) if name in merged else None
    check(actual == expected, 'operative_manifest_hash', {'group': group, 'path': name, 'expected': expected, 'actual': actual})
    manifest_checks.append({'group': group, 'path': name, 'expected_sha256': expected, 'actual_sha256': actual, 'pass': actual == expected})


for name, digest in new['file_hashes'].items():
    manifest_check('frozen-baseline-and-provenance', new['file_hashes_base_directory'] + '/' + name, digest)
for name, digest in new['control_file_hashes'].items():
    manifest_check('control', name, digest)
for item in new['subject_files']:
    manifest_check('subject', item['path'], item['sha256'])
check(len(manifest_checks) == 28, 'operative_manifest_check_count', len(manifest_checks))
check(set(new['control_file_hashes']) == {'student-role.txt', 'student-testing-contract.txt', 'rewrite-guide.md', '../sasis.md', '../../SKILL.md'}, 'actual_control_manifest_key_set')
baseline_rows = []
for name, digest in new['file_hashes'].items():
    path = posixpath.normpath('references/sasis/' + new['file_hashes_base_directory'] + '/' + name)
    row = {'path': path, 'expected_sha256': digest, 'pinned_r40_sha256': sha(source[path]), 'candidate_sha256': sha(merged[path]), 'installed_sha256': sha(installed[path]), 'all_equal_exact_bytes': source[path] == merged[path] == installed[path]}
    check(row['all_equal_exact_bytes'] and row['candidate_sha256'] == digest, 'baseline_actual_identity_preserved', path)
    baseline_rows.append(row)

declared_manifest = json.loads(sealed_raw['manifest-validation.json'])
actual_comparable = [{k: c[k] for k in ('path', 'expected_sha256', 'actual_sha256', 'pass')} for c in manifest_checks]
check(declared_manifest['checks'] == actual_comparable, 'saved_manifest_check_records_exactly_reproduced')
candidate_identities = json.loads(sealed_raw['candidate-identities.json'])
proposed_identities = json.loads(sealed_raw['proposed-file-identities.json'])
measured_proposed = {name: {'bytes': len(raw), 'sha256': sha(raw), 'source_blob': tree[name]['git_blob_sha']} for name, raw in proposed.items()}
check(proposed_identities['files'] == measured_proposed, 'proposed_file_identity_record_reproduced')
check(candidate_identities['proposed_package_file_identities'] == measured_proposed, 'candidate_identity_record_reproduced')
check(candidate_identities['frozen_baseline_provenance_hashes_unchanged'] == new['file_hashes'], 'candidate_baseline_identity_record_reproduced')
check(candidate_identities['source_prof_commit'] == COMMIT and seal['source_package_commit'] == COMMIT, 'pinned_source_commit_records')

carrier = merged['references/sasis.md'].decode('utf-8')
template_names = ['bootstrap_template.js', 'invoker_template.js', 'short_call_template.js', 'verify_reuse_template.py']
template_checks = []
for name in template_names:
    pattern = r'<!-- PROF-READER-TEMPLATE-BEGIN: ' + re.escape(name) + r' -->\n```(?:javascript|python)\n(.*?)```\n<!-- PROF-READER-TEMPLATE-END: ' + re.escape(name) + r' -->'
    matches = re.findall(pattern, carrier, re.S)
    check(len(matches) == 1, 'exact_unique_named_template', name)
    raw = matches[0].encode('utf-8')
    actual_template = (CANDIDATE / 'templates' / name).read_bytes()
    extracted = (CANDIDATE / 'verified-extracted-templates' / name).read_bytes()
    check(raw == actual_template == extracted, 'embedded_template_exact_candidate_and_readback', name)
    preflight = (CANDIDATE / 'synthetic-preflight' / ('verify_reuse.py' if name == 'verify_reuse_template.py' else name)).read_bytes()
    if name == 'verify_reuse_template.py':
        bound = raw.decode('utf-8')
        for marker, value in {'__FIXED_ROUTE_FILENAME__': 'frozen-route.json', '__FIXED_RUNTIME_DIRNAME__': 'runtime', '__FIXED_SCOPE__': 'synthetic r41 retained invoker', '__FIXED_ROUTE_ID__': 'SYNTHETIC_R41'}.items():
            bound = bound.replace(marker, value)
        check(bound.encode('utf-8') == preflight, 'verifier_bound_only_four_fixed_substitutions')
    else:
        check(raw == preflight, 'template_actual_preflight_bytes', name)
    template_checks.append({'name': name, 'bytes': len(raw), 'sha256': sha(raw), 'exact_candidate_template_and_extraction': raw == actual_template == extracted})
check(set(p.name for p in (CANDIDATE / 'templates').iterdir() if p.is_file()) == set(template_names), 'template_directory_inventory')

# Recheck the reviewed snapshot and every proposed/installed byte after the inspection.
check((CANDIDATE / 'REVIEW-SEAL.json').read_bytes() == seal_raw, 'seal_stable_during_review')
for name, raw in sealed_raw.items():
    check((CANDIDATE / name).read_bytes() == raw, 'sealed_file_stable_during_review', name)
for name, raw in proposed.items():
    check((proposed_root / name).read_bytes() == raw, 'candidate_file_stable_during_review', name)
for name, raw in installed.items():
    check((INSTALLED / name).read_bytes() == raw, 'installed_file_stable_during_review', name)

summary = {'status': 'pass' if not errors else 'fail', 'scope': 'Read-only package and manifest review, no production execution, generation, reader, publication or synchronization performed.', 'expected_and_measured_review_seal_sha256': sha(seal_raw), 'pinned_r40_commit': COMMIT,
           'pinned_package_files': len(source), 'proposed_overlay_files': len(proposed), 'merged_package_files': len(merged), 'actual_changed_files': changed, 'unchanged_package_files': len(merged) - len(changed),
           'installed_file_count': len(installed), 'installed_missing': installed_missing, 'installed_extras': installed_extras, 'installed_changed_from_pinned_r40': installed_changed,
           'operative_manifest_check_records': len(manifest_checks), 'operative_manifest_distinct_paths': len({c['path'] for c in manifest_checks}), 'manifest_groups': dict(collections.Counter(c['group'] for c in manifest_checks)), 'unchanged_frozen_baseline_provenance_identities': len(baseline_rows),
           'actual_profile_changed_fields': actual_field_changes, 'new_protocol_note_count': len(new['protocol_update_notes']) - len(old['protocol_update_notes']), 'review_seal_named_files_checked': len(sealed_files), 'template_payloads_checked': len(template_checks),
           'errors': errors, 'limitations': ['The complete proposed package is a virtual merge of five candidate replacements with 31 immutable pinned r40 Git blobs; no staging, installation or publication was performed.', 'The 28 operative records cover 24 distinct paths, since four subject records repeat baseline hashes. Whole-package identity is established separately by the complete inventory.', 'Candidate validation code was inspected but not run because it writes inside the candidate and invokes synthetic proof logic. Saved synthetic pass flags alone are not adopted as execution proof in this package review.', 'The candidate validator checks every expected installed path but does not enumerate extras; this independent recursive inventory check closes that local review gap and found no extras.', 'No production binding, runtime, fresh reader, generation, scientific teaching quality or future synchronization result is established. Root retains those actions.', 'The repository root prof.zip is a distribution artifact, and runs/ is historical evidence; neither is part of the operative root-package inventory SKILL.md, agents/, assets/, references/, scripts/.']}
write('package-inventory-and-identities.json', {'files': package_rows})
write('operative-manifest-checks.json', {'checks': manifest_checks, 'distinct_paths': len({c['path'] for c in manifest_checks}), 'baseline_preservation': baseline_rows})
write('review-seal-checks.json', {'review_seal_bytes': len(seal_raw), 'review_seal_sha256': sha(seal_raw), 'sealed_files': sealed_files, 'proposed_file_identities': measured_proposed, 'template_checks': template_checks})
write('validation-summary.json', summary)
print(json.dumps(summary, ensure_ascii=True, indent=2))
raise SystemExit(0 if not errors else 1)
