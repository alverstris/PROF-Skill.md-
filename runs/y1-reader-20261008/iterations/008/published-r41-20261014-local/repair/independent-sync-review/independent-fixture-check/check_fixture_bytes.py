"""Read-only independent reconstruction/rehash of the named synthetic fixture."""
from pathlib import Path
import hashlib
import json
import posixpath
import re
import subprocess

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[3]
OWNER = PROJECT / '.prof-sasis/20261014-d008-r41/local-sync-preparation'
FIXTURE = OWNER / 'synthetic-fixtures/20261014T212433699002Z'
EXPECTED_HELPER = 'cb0c8b31a3d857edc3d8ed47f79afea61d7b3a752061c14f94f76a888b86b5f0'
VERSION = 'synthetic-r41'
errors = []


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob_sha(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def identity(raw):
    return {'bytes': len(raw), 'sha256': sha(raw), 'git_blob_sha': blob_sha(raw)}


def check(ok, name, detail=None):
    if not ok:
        errors.append({'check': name, 'detail': detail})


def pairs(items):
    value = {}
    for key, item in items:
        if key in value:
            raise ValueError('Duplicate JSON key: ' + key)
        value[key] = item
    return value


def read_json(path):
    return json.loads(path.read_bytes().decode('utf-8-sig'), object_pairs_hook=pairs)


def write(name, value):
    (OUT / name).write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))


inputs = {name: (OWNER / name).read_bytes() for name in ('sync_published_prof.py', 'test_sync_synthetic.py', 'synthetic-test-readback.json')}
check(sha(inputs['sync_published_prof.py']) == EXPECTED_HELPER, 'expected_helper_hash')
readback = read_json(OWNER / 'synthetic-test-readback.json')
check(readback['helper']['sha256'] == EXPECTED_HELPER and Path(readback['helper']['path']) == OWNER / 'sync_published_prof.py', 'readback_helper_identity')
check(Path(readback['fixture_root']) == FIXTURE, 'readback_is_named_latest_fixture')
snapshot = {p.relative_to(FIXTURE).as_posix(): p.read_bytes() for p in FIXTURE.rglob('*') if p.is_file()}
check(not any(p.is_symlink() or p.is_junction() for p in FIXTURE.rglob('*')), 'no_actual_fixture_symlink_or_junction')
all_file_rows = [{'path': name, **identity(raw)} for name, raw in sorted(snapshot.items())]


def original_package(controls=5):
    # Reconstructed from the inspected literal test specification, not imported.
    raw = {
        'SKILL.md': b'\xef\xbb\xbf---\r\nmetadata:\r\n  version: "synthetic-r41"\r\n---\r\nSynthetic fixture only.\n',
        'references/sasis.md': b'synthetic protocol\r\n',
        'references/sasis/student-role.txt': b'synthetic role\n',
        'references/sasis/student-testing-contract.txt': b'synthetic contract\r\n',
        'references/sasis/rewrite-guide.md': b'synthetic guide\r\n',
    }
    for number in range(19):
        raw[f'references/sasis/baseline/base-{number:02}.txt'] = b'\xef\xbb\xbf' + f'synthetic {number}\r\nline two\n'.encode()
    for number in range(11):
        raw[f'assets/payload-{number:02}.bin'] = bytes([0, 10, 13, 255, number])
    controls_map = ['student-role.txt', 'student-testing-contract.txt', 'rewrite-guide.md', '../sasis.md', '../../SKILL.md'][:controls]
    manifest = {
        'protocol_revision': VERSION,
        'file_hashes_base_directory': 'baseline',
        'file_hashes': {f'base-{number:02}.txt': sha(raw[f'references/sasis/baseline/base-{number:02}.txt']) for number in range(19)},
        'control_file_hashes': {name: sha(raw[posixpath.normpath('references/sasis/' + name)]) for name in controls_map},
        'subject_files': [{'path': f'baseline/base-{number:02}.txt', 'sha256': sha(raw[f'references/sasis/baseline/base-{number:02}.txt'])} for number in range(4)],
    }
    raw['references/sasis/profile-manifest.json'] = (json.dumps(manifest, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
    return dict(sorted(raw.items()))


expected_new = original_package()
expected_identities = {name: identity(raw) for name, raw in expected_new.items()}
expected_package = {name: {'path': name, **item, 'mode': '100644'} for name, item in expected_identities.items()}


def old_package(extra=False):
    old = {name: b'old synthetic bytes\r\n' + raw for name, raw in expected_new.items()}
    if extra:
        old['obsolete.txt'] = b'extra old fixture'
    return dict(sorted(old.items()))


def actual_subtree(relative):
    path = FIXTURE / relative
    if not path.exists():
        return None
    prefix = relative + '/'
    return {name[len(prefix):]: raw for name, raw in snapshot.items() if name.startswith(prefix)}


state_rows = []
manifest_rows = []


def check_state(case, role, expected):
    rel = case + '/' + role if case else role
    actual = actual_subtree(rel)
    check(actual == expected, 'actual_fixture_package_state', {'case': case, 'role': role, 'present': actual is not None, 'expected_present': expected is not None})
    rows = [] if actual is None else [{'path': name, **identity(raw)} for name, raw in sorted(actual.items())]
    state_rows.append({'case': case, 'role': role, 'present': actual is not None, 'files': len(rows), 'matches_independently_reconstructed_exact_bytes': actual == expected, 'identities': rows})
    return actual


def independent_manifest(raw_package, label):
    manifest = json.loads(raw_package['references/sasis/profile-manifest.json'].decode('utf-8-sig'), object_pairs_hook=pairs)
    items = [('file_hashes', name, 'references/sasis/' + manifest['file_hashes_base_directory'], digest) for name, digest in manifest['file_hashes'].items()]
    items += [('control_file_hashes', name, 'references/sasis', digest) for name, digest in manifest['control_file_hashes'].items()]
    items += [('subject_files', item['path'], 'references/sasis', item['sha256']) for item in manifest['subject_files']]
    checks = []
    for field, fragment, parent, digest in items:
        package_path = posixpath.normpath(parent + '/' + fragment)
        measured = sha(raw_package[package_path])
        check(measured == digest, 'independent_fixture_manifest_hash', {'label': label, 'path': package_path})
        checks.append({'manifest': 'references/sasis/profile-manifest.json', 'field': field, 'declared_path': fragment, 'package_path': package_path, 'expected_sha256': digest, 'actual_sha256': measured, 'pass': measured == digest})
    check(manifest['protocol_revision'] == VERSION, 'fixture_manifest_revision', label)
    match = re.findall(r'^  version: "([^"\r\n]+)"\s*$', raw_package['SKILL.md'].decode('utf-8-sig'), re.M)
    check(match == [VERSION], 'fixture_SKILL_version', label)
    result = {'checks': checks, 'operative_manifest_checks': len(checks), 'distinct_checked_paths': len({item['package_path'] for item in checks}), 'json_files_parsed': sum(name.endswith('.json') for name in raw_package), 'historical_provenance_hashes_rewritten': False}
    manifest_rows.append({'label': label, **result})
    return result


claims = []
for count, controls in ((26, 3), (28, 5)):
    current = check_state('', f'dynamic-manifests/{count}', original_package(controls))
    manifest = independent_manifest(current, f'dynamic-manifests/{count}')
    check(manifest['operative_manifest_checks'] == count and manifest['distinct_checked_paths'] == count - 4, 'dynamic_count', count)
    claims.append({'test': f'dynamic-manifest-{count}', 'basis': 'Actual complete 36-file bytes and all manifest hashes independently reconstructed', 'corroborated': True})

cases = {
    'whole-directory-with-obsolete-file': {'extra': True, 'installation': 'new', 'backup': 'old', 'previous': 'old', 'stage': None, 'failed': None, 'test': 'whole-directory-replaces-obsolete-file', 'success': True},
    'rename-blocked-fallback': {'extra': False, 'installation': 'new', 'backup': 'old', 'previous': None, 'stage': 'new', 'failed': None, 'test': 'blocked-rename-equal-inventory-fallback', 'success': True},
    'rename-blocked-unequal-inventory': {'extra': True, 'installation': 'old', 'backup': 'old', 'previous': None, 'stage': 'new', 'failed': None, 'test': 'blocked-rename-unequal-inventory-refused', 'error': 'Fallback forbidden: existing and staged relative file inventories differ', 'mutated': False, 'restored': None},
    'fallback-partial-write-rollback': {'extra': False, 'installation': 'old', 'backup': 'old', 'previous': None, 'stage': 'new', 'failed': None, 'test': 'partial-fallback-write-rolls-back', 'error': 'Synthetic fourth payload write failure', 'mutated': True, 'restored': True},
    'stage-promotion-failure': {'extra': False, 'installation': 'old', 'backup': 'old', 'previous': 'old', 'stage': 'new', 'failed': None, 'test': 'failed-stage-directory-promotion-rolls-back', 'error': '[WinError 5] Synthetic Windows directory rename refusal', 'mutated': True, 'restored': True},
    'late-live-ref-failure': {'extra': False, 'installation': 'old', 'backup': 'old', 'previous': 'old', 'stage': None, 'failed': 'new', 'test': 'late-live-ref-failure-restores-and-preserves-failed-installation', 'error': 'Synthetic live main changed at final readback', 'mutated': True, 'restored': True},
    'final-status-record-failure': {'extra': False, 'installation': 'old', 'backup': 'old', 'previous': 'old', 'stage': None, 'failed': 'new', 'test': 'final-status-record-write-failure-restores-and-invalidates-pass', 'error': 'Synthetic final status-record write failure', 'mutated': True, 'restored': True},
    'rollback-itself-fails': {'extra': False, 'installation': 'old', 'backup': 'old', 'previous': None, 'stage': 'new', 'failed': None, 'test': 'rollback-failure-preserves-backup-and-holds', 'error': 'Synthetic persistent payload write refusal', 'mutated': True, 'restored': False},
}
failure_records = []
for name, expected in cases.items():
    old = old_package(expected['extra'])
    before = {path: identity(raw) for path, raw in old.items()}
    actual_states = {}
    for role, folder in (('installation', 'installation'), ('backup', 'backups/dated-complete-backup'), ('previous', 'previous-installation'), ('stage', 'staged-package'), ('failed', 'failed-installation')):
        kind = expected[role]
        target = expected_new if kind == 'new' else old if kind == 'old' else None
        actual_states[role] = check_state(name, folder, target)
    run = FIXTURE / name
    attempt = read_json(run / 'installation-attempt.json')
    check(attempt['before'] == before, 'record_before_equals_reconstructed_old_and_actual_backup', name)
    check(attempt['destination'] == str(run / 'installation') and attempt['backup'] == str(run / 'backups/dated-complete-backup') and attempt['stage'] == str(run / 'staged-package'), 'record_confined_fixture_paths', name)
    check(attempt['backup_complete_inventory_and_bytes_match'] is True, 'attempt_backup_verified', name)
    hold = read_json(run / 'generation-hold.json')
    if expected.get('success'):
        verification = read_json(run / 'installation-verification.json')
        check(verification['before'] == before and verification['package'] == expected_package, 'success_record_full_before_and_expected_package', name)
        check(verification['generation_hold'] is False and hold['generation_hold'] is False and verification['installed_files_overwritten_and_verified'] == 36, 'success_record_current_hold_and_count', name)
        manifests = independent_manifest(actual_states['installation'], name + '/installation')
        check(read_json(run / 'installed-manifest-checks.json') == manifests, 'saved_installed_manifest_rows_match_actual_hashes', name)
        if name == 'rename-blocked-fallback':
            check(verification['original_rename_failure']['winerror'] == 5 and verification['original_rename_failure']['errno'] == 13, 'mocked_Windows_rename_error_preserved', name)
    else:
        failure = read_json(run / 'installation-failure.json')
        check(failure['before'] == before and failure['generation_hold'] is True and hold['generation_hold'] is True, 'failure_old_inventory_and_generation_hold', name)
        check(failure['error']['message'] == expected['error'] and failure['destination_mutated'] == expected['mutated'], 'substantive_failure_record', name)
        check(failure['record_persistence_errors'] == [], 'failure_record_persistence', name)
        if expected['restored'] is None:
            check(failure['rollback']['attempted'] is False, 'unequal_inventory_no_payload_mutation_or_rollback', name)
        else:
            check(failure['rollback']['attempted'] is True and failure['rollback']['restored'] == expected['restored'] and failure['rollback']['backup_preserved'] is True, 'rollback_state_record', name)
        if name in ('rename-blocked-unequal-inventory', 'fallback-partial-write-rollback', 'rollback-itself-fails'):
            check(failure['original_rename_failure']['winerror'] == 5 and failure['original_rename_failure']['errno'] == 13, 'failure_mocked_rename_winerror', name)
        if name == 'rollback-itself-fails':
            check(failure['rollback']['manual_recovery_required'] is True and failure['rollback']['error']['message'] == 'Synthetic persistent payload write refusal', 'rollback_failure_manual_hold')
        if name == 'final-status-record-failure':
            invalid = read_json(run / 'installation-verification.json')
            prior = read_json(run / 'installation-verification-before-failure.json')
            check(invalid['generation_hold'] is True and invalid['invalidated_after_installation_failure'] is True and prior['generation_hold'] is False, 'pass_record_preserved_and_invalidated')
            check(prior['before'] == before and prior['package'] == expected_package, 'pre_failure_pass_full_inventory_identity')
            manifests = independent_manifest(actual_states['failed'], name + '/failed-installation')
            check(read_json(run / 'installed-manifest-checks.json') == manifests, 'pre_failure_manifest_rows_bind_preserved_failed_installation')
        failure_records.append({'case': name, 'path': str(run / 'installation-failure.json'), 'bytes': (run / 'installation-failure.json').stat().st_size, 'sha256': sha((run / 'installation-failure.json').read_bytes()), 'error': failure['error'], 'original_rename_failure': failure['original_rename_failure'], 'generation_hold': failure['generation_hold'], 'destination_mutated': failure['destination_mutated'], 'rollback': failure['rollback'], 'before_inventory_matches_actual_backup': failure['before'] == before})
    claims.append({'test': expected['test'], 'basis': 'Actual before identities, complete backup/current/displaced/failed/staged byte states and substantive transaction records', 'corroborated': True, 'historical_exception_execution_independently_observed': False})

# Local Git reads only. Do not invoke helper, tests or any network command.
repo = FIXTURE / 'synthetic-git'


def git(*args):
    return subprocess.check_output(['git', '-c', 'credential.helper=', '-C', str(repo), *args])


commit = git('rev-parse', 'HEAD').decode('ascii').strip()
tree = {}
excluded = {}
for entry in filter(None, git('ls-tree', '-rz', '--full-tree', commit).split(b'\0')):
    meta, path = entry.split(b'\t', 1)
    mode, kind, blob = meta.decode('ascii').split()
    name = path.decode('utf-8')
    if name == 'SKILL.md' or name.split('/')[0] in {'agents', 'assets', 'references', 'scripts'}:
        tree[name] = {'mode': mode, 'kind': kind, 'git_blob_sha': blob}
    else:
        excluded[name] = {'mode': mode, 'kind': kind, 'git_blob_sha': blob}
check(set(tree) == set(expected_new) and len(tree) == 36, 'actual_immutable_local_git_package_inventory')
check(set(excluded) == {'prof.zip', 'runs/evidence.json'}, 'actual_excluded_Git_paths')
git_rows = []
for name, item in sorted(tree.items()):
    raw = git('cat-file', 'blob', item['git_blob_sha'])
    check(raw == expected_new[name] and item['git_blob_sha'] == blob_sha(raw) and item['mode'] == '100644', 'actual_local_Git_blob_and_fixture_bytes', name)
    check((repo / name).read_bytes() == raw and (repo / 'package' / name).read_bytes() == raw, 'actual_Git_worktree_and_package_fixture', name)
    git_rows.append({'path': name, **item, **identity(raw)})
config = (repo / '.git/config').read_text(encoding='utf-8')
check('[remote ' not in config, 'synthetic_Git_has_no_configured_remote')
input_record = read_json(FIXTURE / 'synthetic-inventory.json')
check(input_record['commit'] == commit and input_record['version'] == VERSION and input_record['operative_manifest_checks'] == 28, 'synthetic_inventory_pin_and_version')
check({e['path']: e for e in input_record['package']} == expected_package, 'synthetic_input_all_36_actual_byte_identities')
check(input_record['published_verification']['verified'] is False and input_record['published_verification']['immutable_commit'] == commit, 'saved_unverified_input_is_actual_rejection_witness')
claims.append({'test': 'complete-immutable-git-package-filter-and-binary-identities', 'basis': 'Actual 36 immutable local Git blob identities and root/package fixture bytes, with exact two excluded paths and no configured remote', 'corroborated': True})
check(snapshot['fake-reparse'] == b'synthetic reparse fixture', 'actual_fake_reparse_bytes')
for name, basis in (
    ('unsafe-paths-rejected', 'Static inspection accounts for all nine unsafe paths and their rejecting guards; individual exception results are not saved.'),
    ('alternate-production-destination-rejected', 'Static patched AUTHORIZED fixture differs from hard-coded production destination; no dedicated rejection record.'),
    ('windows-reparse-attribute-rejected', 'Static mock supplies st_file_attributes=0x400; actual fake-reparse is an ordinary file. No actual junction or independent exception record.'),
    ('unverified-publication-input-rejected', 'Actual final input has verified=false and helper guard requires true; no independent saved exception trace.')):
    claims.append({'test': name, 'basis': basis, 'corroboration': 'Static code and saved fixture consistency; dynamic rejection is reported by test readback, not independently witnessed'})
check(len(readback['synthetic_tests']) == 15 and readback['passed'] == 15 and readback['failed'] == 0, 'readback_15_claim_cardinality')
check({c['test'] for c in claims} == {c['test'] for c in readback['synthetic_tests']}, 'all_15_claims_accounted_for')
for count in (26, 28):
    claim = next(c for c in readback['synthetic_tests'] if c['test'] == f'dynamic-manifest-{count}')
    check(claim['actual'] == count and claim['distinct_paths'] == count-4, 'readback_dynamic_count_matches_actual_manifest', count)
check(readback['network_used'] is False and readback['production_cli_invoked'] is False and readback['actual_installed_prof_read_or_written_by_tests'] is False, 'readback_static_scope_flags_consistent')

# Stable readback is limited to this exact latest fixture; stale trees are untouched.
for name, raw in snapshot.items():
    check((FIXTURE / name).read_bytes() == raw, 'latest_fixture_file_unchanged_during_review', name)
for name, raw in inputs.items():
    check((OWNER / name).read_bytes() == raw, 'owner_record_unchanged_during_review', name)
check({p.relative_to(FIXTURE).as_posix() for p in FIXTURE.rglob('*') if p.is_file()} == set(snapshot), 'latest_fixture_inventory_stable')

summary = {'status': 'corroborated' if not errors else 'discrepancy', 'fixture_root': str(FIXTURE), 'helper_sha256': sha(inputs['sync_published_prof.py']), 'test_script_sha256': sha(inputs['test_sync_synthetic.py']), 'readback_sha256': sha(inputs['synthetic-test-readback.json']),
           'fixture_files_rehashed': len(snapshot), 'fixture_total_bytes': sum(len(raw) for raw in snapshot.values()), 'transaction_cases': len(cases), 'package_state_comparisons_including_absence': len(state_rows), 'present_package_trees': sum(r['present'] for r in state_rows), 'substantive_failure_records': len(failure_records), 'manifest_check_groups': len(manifest_rows), 'local_immutable_git_package_blobs_checked': len(git_rows), 'synthetic_git_commit': commit, 'test_claims_accounted_for': len(claims), 'test_claims_with_direct_package_or_Git_byte_corroboration': 11, 'test_claims_with_static_guard_and_readback_corroboration_only': 4, 'errors': errors,
           'limits': ['No owner helper/test was imported or executed, and no production stage/install or network command was invoked. Only read-only local Git object commands were used.', 'Saved files corroborate byte states and substantive failure records, not an independent historical exception transcript or actual test execution trace.', 'Rename/write errors and late-live-ref/final-status failures are deliberate mocks; winerror5 is assigned to the synthetic PermissionError.', 'Reparse test uses a simulated lstat Windows attribute on an ordinary file, not an actual junction.', 'Rollback-itself-fails refuses the first attempted payload write. Current installation remains exact old bytes; destination_mutated=true marks an attempted replacement path, not observed surviving corruption. This test proves hold/backup policy, not recovery of a partly damaged target when restoration also fails.', 'Unsafe-path, alternate-destination, reparse and unverified-input test exceptions are not separately saved; static guard/input consistency and readback claims are distinguished.', 'Synthetic local Git has no configured remote. Test source uses local Git and stubbed live checks; no actual GitHub/live-main check or production synchronization result is established.', 'No stale fixture tree was read or altered; all writes stay in the independent-fixture-check output directory.']}
write('fixture-file-identities.json', {'fixture_root': str(FIXTURE), 'files': all_file_rows})
write('actual-package-state-checks.json', {'states': state_rows})
write('manifest-and-Git-checks.json', {'manifest_groups': manifest_rows, 'synthetic_git_commit': commit, 'package_blobs': git_rows, 'excluded': excluded})
write('substantive-failure-record-checks.json', {'failures': failure_records})
write('claim-corroboration.json', {'claims': claims})
write('validation-summary.json', summary)
print(json.dumps(summary, ensure_ascii=True, indent=2))
raise SystemExit(0 if not errors else 1)
