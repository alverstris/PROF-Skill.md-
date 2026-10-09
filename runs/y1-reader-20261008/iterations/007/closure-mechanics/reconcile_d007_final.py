#!/usr/bin/env python3
"""PROPOSAL ONLY: D007 v3 parent state. No Git/skill/queue mutation.
Root supplies actual reviewed evidence paths, hashes and exact substantive witnesses.
This bookkeeping script does not perform reader, rendering or semantic acceptance.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, re, shutil, subprocess, tempfile, os

REPO = Path('/workspace/scratch/ac36b9c5ff31/PROF-repo')
P = REPO / 'runs/y1-reader-20261008/iterations/007'
AUTHOR = P / 'author-work-r13'
ORIGINAL = AUTHOR / '.prof-state'
HELPER = REPO / 'scripts/prof_state.py'
TOPIC = 'l07-review'
V1_SHA = 'c57e0ce849af6865e8422a3a62672d337053a40a66c3eee8904e251f989990f7'
V2_SHA = '66493aa3d30f53467ee997d9ab372b605cd73e1c84daf21f1737c83761774d3b'
V3_SHA = '6dc2823d9f931c1baaa6eb4ce5076ed2aef1859ba29255d5503eed627824ae54'
R13_SHA = '44610963ed675e6df95529e5a3e985669c9ce0077e6e885511cfd2fdfb9feff6'
V3_COMMIT = '2c0a49dff10d407296675a9d52a2d664be1bb0f0'
READ_ROLES = ('acceptance', 'parent_technical', 'destination', 'fresh_sasis',
              'reader_access', 'reader_admission', 'revision_review')
DECISIONS = ('complete_final_document_read', 'all_report_originals_read',
             'reader_admitted_complete_two_inputs', 'final_destination_review_complete',
             'whole_preview_inspected', 'all_supported_issues_resolved',
             'source_and_math_review_complete', 'revision_carry_review_complete')


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(b):
    return hashlib.sha256(b).hexdigest()


def read(p):
    return json.loads(p.read_text(encoding='utf-8'))


def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def within(rel):
    p = P / rel
    need(not Path(rel).is_absolute() and '..' not in Path(rel).parts, 'Path must be relative within 007: ' + rel)
    need(p.resolve().is_relative_to(P.resolve()), 'Path escape: ' + rel)
    return p


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])


def inventory(root):
    return [{'path': str(p.relative_to(root)), 'bytes': p.stat().st_size,
             'sha256': digest(p.read_bytes())} for p in sorted(root.rglob('*')) if p.is_file()]


def helper(state, command, topic=False):
    cmd = ['python3', str(HELPER), command, '--state', str(state)]
    if command == 'check':
        cmd += ['--json']
    if topic:
        cmd += ['--topic', TOPIC]
    r = subprocess.run(cmd, capture_output=True, text=True)
    need(r.returncode in (0, 1) and r.stdout.strip(), r.stdout + r.stderr)
    return r.returncode, json.loads(r.stdout), r.stderr


def dependencies(state, topic=False):
    code, obj, err = helper(state, 'dependencies', topic)
    need(code == 0 and isinstance(obj, list), str(obj) + err)
    return obj


def check(state, records, name, topic=False, pending=False):
    code, obj, err = helper(state, 'check', topic)
    save(records / (name + '.json'), obj)
    (records / (name + '.stderr.txt')).write_text(err, encoding='utf-8')
    wanted = ['output_check.publication: not ready: pending'] if pending else []
    need(obj['defects'] == wanted and code == int(pending), str(obj))
    print(name, obj['result'], obj['defects'])


def witness(spec):
    p = within(spec['path'])
    b = p.read_bytes()
    need(re.fullmatch('[0-9a-f]{64}', spec['sha256']) is not None, 'Real evidence hash required')
    need(digest(b) == spec['sha256'], 'Evidence bytes changed: ' + str(p))
    text = b.decode('utf-8')
    passage = spec['exact_text']
    need(isinstance(passage, str) and passage.strip() and passage in text,
         'Exact substantive witness missing: ' + str(p))
    return {'path': spec['path'], 'sha256': spec['sha256'],
            'locator': {'kind': 'text', 'value': passage}}


def append_once(items, value):
    if value not in items:
        items.append(value)


def prefix_original_evidence(node):
    if isinstance(node, dict):
        for key, val in node.items():
            if key == 'evidence':
                for item in val:
                    if item['path'] != '@request':
                        item['path'] = 'author-work-r13/' + item['path']
            else:
                prefix_original_evidence(val)
    elif isinstance(node, list):
        for val in node:
            prefix_original_evidence(val)


def equivalence(config):
    b1 = (AUTHOR / 'teaching.md').read_bytes()
    b2 = (P / 'revised-v2/teaching-v2.md').read_bytes()
    b3 = within(config['final_path']).read_bytes()
    need(digest(b1) == V1_SHA and digest(b2) == V2_SHA and digest(b3) == V3_SHA,
         'This narrowly scoped proposal accepts only the inspected v1/v2/v3 identities; revise it for another repair.')
    need(config['final_sha256'] == V3_SHA and config['final_commit'] == V3_COMMIT,
         'Unexpected final freeze identity')
    restored2, n_inline3 = re.subn(rb'\$`([^`\n]+)`\$',
        lambda m: b'$`' + m[1].replace(b'\\lt ', b'<').replace(b'\\gt ', b'>') + b'`$', b3)
    restored1, n_inline2 = re.subn(rb'\$`([^`\n]+)`\$', lambda m: b'$' + m[1] + b'$', b2)
    restored1, n_display = re.subn(rb'(?m)^```math\n([\s\S]*?)\n```$',
        lambda m: b'$$\n' + m[1] + b'\n$$', restored1)
    need(restored2 == b2 and restored1 == b1, 'Composed byte-exact inverse failed')
    need((n_inline3, n_inline2, n_display) == (338, 338, 33), 'Unexpected expression inventory')
    repo_path = str(within(config['final_path']).relative_to(REPO))
    need(git('show', V3_COMMIT + ':' + repo_path) == b3, 'Fetched frozen output differs')
    return {'checked_at': datetime.now(timezone.utc).isoformat(),
            'v1_sha256': V1_SHA, 'v2_sha256': V2_SHA, 'v3_sha256': V3_SHA,
            'v3_inverse_exact_v2': True, 'v2_inverse_exact_v1': True,
            'inline': 338, 'display': 33, 'final_commit': V3_COMMIT,
            'scope': 'Exact delimiter/operator-spelling inverse only. Independent parent semantic, '
                     'actual output and fresh-reader reviews remain separate required evidence.'}


def phase_a(config, state, records):
    need(not state.exists() and not records.exists(), 'Refuse overwrite of existing parent state/evidence directory')
    need(config['outgoing_change'] == 'metadata_only', 'Substantive skill change requires its own regeneration workflow')
    need(config['incoming_version'] == '2026-10-08-r13' and config['outgoing_version'] == '2026-10-08-r14',
         'Unexpected version transition')
    for k in DECISIONS:
        need(config['lead_decisions'].get(k) is True, 'Actual lead review required: ' + k)
    ev = {role: witness(config['evidence'][role]) for role in READ_ROLES}
    eq = equivalence(config)
    m = read(ORIGINAL / 'manifest.json')
    t = read(ORIGINAL / 'topics' / (TOPIC + '.json'))
    need(m['project_root'] == str(AUTHOR) and m['skill']['sha256'] == R13_SHA, 'Author controls differ')
    need(digest(Path(m['skill']['path']).read_bytes()) == R13_SHA, 'Original skill bytes changed')
    need(m['outputs'] == [{'id': 'teaching', 'path': 'teaching.md', 'sha256': V1_SHA}], 'Original output binding differs')
    expected_pending = ['l07-review.T11: not ready: pending', 'l07-review.T12: not ready: pending',
        'output_check.parent_technical: not ready: pending', 'output_check.destination: not ready: pending',
        'output_check.fresh_sasis: not ready: pending', 'output_check.final_review: not ready: pending',
        'output_check.publication: not ready: pending']
    code, original_check, _ = helper(ORIGINAL, 'check')
    need(code == 1 and original_check['defects'] == expected_pending, 'Unexpected original author state; inspect before carry')
    need([(g['id'], g['status']) for g in t['gaps']] == [('reciprocal-wording', 'resolved')],
         'Original gap set changed; inspect before carry')
    before = inventory(AUTHOR)
    # First mutations occur only after required actual files, hashes, lead decisions,
    # fetched frozen bytes and original-state checks have all passed.
    shutil.copytree(ORIGINAL, state)
    records.mkdir(parents=True)
    save(records / 'original-author-inventory.json', before)
    save(records / 'original-state-check.json', original_check)
    save(records / 'lead-config-phase-a.json', config)
    save(records / 'revision-equivalence-mechanical.json', eq)
    prefix_original_evidence(m)
    prefix_original_evidence(t)
    m['project_root'] = str(P)
    m['outputs'] = [{'id': 'teaching', 'path': config['final_path'], 'sha256': V3_SHA}]
    for c in t['requirements'].values():
        c['dependencies'] = []
    for g in t['gaps']:
        g['dependencies'] = []
    for c in m['output_checks']:
        c['dependencies'] = []
    save(state / 'manifest.json', m)
    save(state / 'topics' / (TOPIC + '.json'), t)
    td = dependencies(state, topic=True)
    for key, c in t['requirements'].items():
        append_once(c['evidence'], ev['acceptance'])
        append_once(c['evidence'], ev['revision_review'])
        c['dependencies'] = td
        if key in ('T11', 'T12'):
            c.update(status='pass', reason='Lead verified complete final v3 teaching and all current '
                'technical/source, actual destination and admitted fresh-reader evidence. Main publication '
                'remains the separate pending gate; no human-learning or live-client inference is made.')
            for role in ('destination', 'fresh_sasis', 'reader_admission'):
                append_once(c['evidence'], ev[role])
        else:
            c['reason'] += (' Original author v1 evidence retained; lead reviewed the complete final v3 '
                'route and exact composed byte inverse. Representation-specific final evidence is separate; '
                'this does not assert that the original author read v3.')
    for g in t['gaps']:
        need(g['status'] in ('resolved', 'waived_by_user'), 'Unresolved gap cannot be carried as accepted')
        # In this case reciprocal-wording is resolved in v1 and survives both inverse-verified repairs.
        append_once(g['evidence'], ev['revision_review'])
        append_once(g['evidence'], ev['acceptance'])
        g['reason'] += ' Lead verified that the corrected reciprocal wording and its dependent route survive in final v3.'
        g['dependencies'] = td
    save(state / 'topics' / (TOPIC + '.json'), t)
    pd = dependencies(state)
    for c in m['output_checks']:
        if c['id'] == 'publication':
            c.update(status='pending', reason='Final r14/main publication and readback have not yet occurred.',
                     evidence=[], dependencies=[])
            continue
        append_once(c['evidence'], ev['acceptance'])
        append_once(c['evidence'], ev['revision_review'])
        if c['id'] in ev:
            append_once(c['evidence'], ev[c['id']])
        if c['id'] in ('fresh_sasis', 'final_review'):
            for role in ('fresh_sasis', 'reader_access', 'reader_admission'):
                append_once(c['evidence'], ev[role])
        if c['id'] in ('source_mechanics', 'final_review'):
            append_once(c['evidence'], ev['destination'])
        c.update(status='pass', dependencies=pd)
        c['reason'] += (' Lead final-v3 review and equivalent-revision carry completed with the cited '
                       'current evidence; original author ownership/scope remains as reported. '
                       'Publication is separately pending.')
    save(state / 'manifest.json', m)
    (state / 'RUN.md').write_text('D007 parent final-v3 state: original author evidence/activation '
        'preserved at incoming r13; final v3 separately read and reviewed. Phase A publication pending. '
        'Keep D007 open and counts 6/76; publish/verify r14 and this evidence, then phase B.\n', encoding='utf-8')
    save(records / 'topic-dependencies-phase-a.json', td)
    save(records / 'project-dependencies-phase-a.json', pd)
    check(state, records, 'topic-check-phase-a', topic=True)
    check(state, records, 'full-check-phase-a', pending=True)
    save(records / 'manifest-phase-a-original.json', m)
    save(records / 'topic-phase-a-original.json', t)
    need(inventory(AUTHOR) == before, 'Original author files changed during reconciliation')
    # Freeze the phase-A publication inventory after the final pending-state checks.
    # The inventory's own bytes are checked separately at phase B, avoiding self-hashing.
    publish_files = set()
    for root in (AUTHOR, state, records):
        publish_files.update(f for f in root.rglob('*') if f.is_file())
    publish_files.update(within(config['evidence'][r]['path']) for r in READ_ROLES)
    publish_files.update([within(config['final_path']), P / 'revised-v2/teaching-v2.md',
        P / 'revised-v2/revision-equivalence.json', P / 'revised-v3/revision-equivalence.json'])
    publication_inventory = [{'path': str(f.relative_to(REPO)), 'bytes': f.stat().st_size,
                             'sha256': digest(f.read_bytes())} for f in sorted(publish_files)]
    save(records / 'phase-a-publication-inventory.json', publication_inventory)


def phase_b(config, state, records, publication_spec):
    need(config == read(records / 'lead-config-phase-a.json'), 'Phase-A config changed; preserve and review differences')
    need(inventory(AUTHOR) == read(records / 'original-author-inventory.json'), 'Original author files changed')
    for role in READ_ROLES:
        witness(config['evidence'][role])
    equivalence(config)
    pub_ev = witness(publication_spec)
    pub = read(within(publication_spec['path']))
    need(pub['remote_main_verified'] is True and pub['git_object_bytes_verified'] is True, 'Actual remote readback needed')
    need(pub['expected_previous_main'] == config['phase_a_expected_previous_main'], 'Unexpected main parent observation')
    need(pub['outgoing_prof'] == config['outgoing_version'] and pub['teaching_sha256'] == V3_SHA,
         'Published revision differs')
    need(isinstance(pub['observed_at'], str) and pub['observed_at'].strip(), 'Observation timestamp needed')
    commit, tree = pub['verified_main_commit'], pub['verified_main_tree']
    need(re.fullmatch('[0-9a-f]{40}', commit) is not None and re.fullmatch('[0-9a-f]{40}', tree) is not None,
         'Real published commit/tree required')
    need(git('rev-parse', 'refs/heads/main').decode().strip() == commit, 'Local main not synchronized to observed phase-A commit')
    need(git('rev-parse', commit + '^{tree}').decode().strip() == tree, 'Fetched tree differs')
    # Frozen teaching commits can sit between previous main and phase-A commit.
    # Require actual ancestry, not a fabricated direct-parent claim.
    git('merge-base', '--is-ancestor', config['phase_a_expected_previous_main'], commit)
    pub_index = records / 'phase-a-publication-inventory.json'
    need(git('show', commit + ':' + str(pub_index.relative_to(REPO))) == pub_index.read_bytes(),
         'Published phase-A inventory missing or different')
    for item in read(pub_index):
        f = REPO / item['path']
        need(f.resolve().is_relative_to(REPO.resolve()), 'Publication inventory path escape')
        local_bytes, published_bytes = f.read_bytes(), git('show', commit + ':' + item['path'])
        need(digest(local_bytes) == item['sha256'] and len(local_bytes) == item['bytes'],
             'Local phase-A artifact changed: ' + item['path'])
        need(published_bytes == local_bytes, 'Phase-A publication omitted/changed artifact: ' + item['path'])
    repo_path = str(within(config['final_path']).relative_to(REPO))
    need(digest(git('show', commit + ':' + repo_path)) == V3_SHA, 'Published teaching bytes differ')
    skill = git('show', commit + ':SKILL.md')
    need(digest(skill) == pub['outgoing_skill_sha256'], 'Published skill hash differs')
    final_label, original_label = (config['outgoing_version'] + '"').encode(), (config['incoming_version'] + '"').encode()
    need(skill.count(final_label) == 1 and skill.replace(final_label, original_label, 1) == (AUTHOR / 'controls/SKILL.md').read_bytes(),
         'Outgoing skill is not precisely metadata-only; use appropriate substantive-change workflow')
    # The lead's readback record supplies remote observation. git show checks actual
    # fetched content and does not itself prove remote main visibility.
    m = read(state / 'manifest.json')
    gate = next(c for c in m['output_checks'] if c['id'] == 'publication')
    need(gate['status'] == 'pending', 'Refuse repeated publication promotion')
    pd = dependencies(state)
    gate.update(status='pass', reason='Actual phase-A main publication and fetched tree/SKILL/teaching '
        'bytes verified. Phase-B closure publication still must be verified before the next author.',
        evidence=[pub_ev], dependencies=pd)
    new_run = ('D007 final v3 reviews and phase-A main publication verified. '
        'Publish phase-B closure and counts 7/76; verify latest main and fully reload published '
        'PROF before a fresh next author. Original author remains bound to incoming r13.\n')
    # Validate a staged candidate first; a failed staged check never promotes live publication.
    with tempfile.TemporaryDirectory(prefix='d007-phase-b-state-') as scratch:
        staged_state, staged_records = Path(scratch) / 'state', Path(scratch) / 'checks'
        shutil.copytree(state, staged_state)
        staged_records.mkdir()
        save(staged_state / 'manifest.json', m)
        (staged_state / 'RUN.md').write_text(new_run, encoding='utf-8')
        check(staged_state, staged_records, 'topic-check-phase-b-staged', topic=True)
        check(staged_state, staged_records, 'full-check-phase-b-staged')
        for f in staged_records.iterdir():
            shutil.copyfile(f, records / f.name)
    old_manifest = (state / 'manifest.json').read_bytes()
    old_run = (state / 'RUN.md').read_bytes()
    def atomic_bytes(path, value):
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=path.name + '.', delete=False) as f:
            temporary = Path(f.name)
            f.write(value)
            f.flush()
            os.fsync(f.fileno())
        try:
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)
    try:
        atomic_bytes(state / 'RUN.md', new_run.encode('utf-8'))
        atomic_bytes(state / 'manifest.json', (json.dumps(m, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))
        check(state, records, 'topic-check-phase-b', topic=True)
        check(state, records, 'full-check-phase-b')
        need(inventory(AUTHOR) == read(records / 'original-author-inventory.json'), 'Original author files changed')
    except BaseException:
        atomic_bytes(state / 'manifest.json', old_manifest)
        atomic_bytes(state / 'RUN.md', old_run)
        raise
    save(records / 'publication-evidence-binding.json', publication_spec)
    save(records / 'project-dependencies-phase-b.json', pd)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=('phase-a', 'phase-b'))
    p.add_argument('--config', required=True, type=Path)
    p.add_argument('--publication-spec', type=Path,
                   help='JSON with path, actual sha256 and exact_text for the verified publication record')
    a = p.parse_args()
    cfg = read(a.config)
    need(isinstance(cfg['phase_a_expected_previous_main'], str) and
         re.fullmatch('[0-9a-f]{40}', cfg['phase_a_expected_previous_main']) is not None,
         'Expected previous main must be a frozen full commit hash, not a mutable Git ref')
    need(git('cat-file', '-t', cfg['phase_a_expected_previous_main']).strip() == b'commit',
         'Expected previous main does not identify a fetched commit')
    state, records = within(cfg['state_dir']), within(cfg['state_evidence_dir'])
    need(state.resolve() != P.resolve() and records.resolve() != P.resolve() and
         not state.resolve().is_relative_to(records.resolve()) and not records.resolve().is_relative_to(state.resolve()),
         'Parent state and record directories must be distinct and disjoint')
    need(not state.resolve().is_relative_to(AUTHOR.resolve()) and not records.resolve().is_relative_to(AUTHOR.resolve()),
         'Parent state/evidence must not be inside the original author directory')
    if a.phase == 'phase-a':
        phase_a(cfg, state, records)
    else:
        need(a.publication_spec is not None, 'Actual publication specification is required')
        phase_b(cfg, state, records, read(a.publication_spec))
