#!/usr/bin/env python3
"""PROPOSED ONLY. Root executes after its actual reviews; never edits Git or queue.

phase-a records completed reviews and leaves publication genuinely pending.
phase-b requires an independently obtained publication record and fetched Git objects.
All preserved author states and evidence files remain unchanged. No semantic judgment
is made by this script: exact substantive witness passages are supplied by the lead.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess

REPO = Path('/workspace/scratch/ac36b9c5ff31/PROF-repo')
P = REPO / 'runs/y1-reader-20261008/iterations/006'
PROJECT = P / 'regenerated-r13-candidate1'
ORIGINAL = P / 'author-state-candidate1-v3-original'
STATE = P / '.prof-state-final-v3'
MIRROR = PROJECT / 'parent-review-v3'
RECORDS = P / 'state-evidence-final-v3'
HELPER = REPO / 'scripts/prof_state.py'
TOPIC = 'exponential-log'
TEACHING_SHA = '311afdef083a4468f18bcdd11a68975d2e6622661e0be3405a5c9f58b3f3a813'
CANDIDATE_SHA = '3f7d903a399bdbaaeef397e7af7033dc0229cbb982371ea7c0679fe042c9cc8f'
PREVIOUS_MAIN = 'bd3453eac9cddd3fa96513aff204f44b8d8196eb'
INPUTS = {
    'acceptance': 'parent-acceptance-candidate1-v3.md',
    'reader': 'reader-report-candidate1-v3-original.md',
    'reader_access': 'reader-access-candidate1-v3-original.json',
    'render': 'render-evidence/candidate1-v3-recovery/report.md',
}

def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()

def read(p):
    return json.loads(p.read_text(encoding='utf-8'))

def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def immutable_copy(src, dst):
    b = src.read_bytes()
    if dst.exists():
        assert dst.read_bytes() == b, f'Existing preserved mirror differs: {dst}'
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(b)
    return {'original': str(src.relative_to(P)), 'mirror': str(dst.relative_to(PROJECT)),
            'bytes': len(b), 'sha256': sha_bytes(b)}

def witness(path, passage=None):
    b = path.read_bytes()
    text = b.decode('utf-8')
    if passage is None:
        loc = {'kind': 'lines', 'start': 1, 'end': len(text.splitlines())}
    else:
        assert passage.strip() and passage in text, f'Exact witness absent in {path}'
        loc = {'kind': 'text', 'value': passage}
    return {'path': str(path.relative_to(PROJECT)), 'sha256': sha_bytes(b), 'locator': loc}

def dependencies(topic=False):
    cmd = ['python3', str(HELPER), 'dependencies', '--state', str(STATE)]
    if topic:
        cmd += ['--topic', TOPIC]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    return json.loads(r.stdout)

def check(name, topic=False, expect_pending_publication=False):
    cmd = ['python3', str(HELPER), 'check', '--state', str(STATE), '--json']
    if topic:
        cmd += ['--topic', TOPIC]
    r = subprocess.run(cmd, capture_output=True, text=True)
    RECORDS.mkdir(parents=True, exist_ok=True)
    (RECORDS / (name + '.json')).write_text(r.stdout, encoding='utf-8')
    (RECORDS / (name + '.stderr.txt')).write_text(r.stderr, encoding='utf-8')
    obj = json.loads(r.stdout)
    expected = ['output_check.publication: not ready: pending'] if expect_pending_publication else []
    assert obj['defects'] == expected, obj
    assert r.returncode == (1 if expect_pending_publication else 0), obj
    print(name, obj['result'], obj['defects'])

def add_once(items, item):
    if item not in items:
        items.append(item)

def phase_a(args):
    assert not STATE.exists(), 'Refuse overwrite: inspect an existing state instead.'
    assert sha_bytes((PROJECT / 'teaching-v3.md').read_bytes()) == TEACHING_SHA
    assert sha_bytes((PROJECT / 'controls/SKILL.md').read_bytes()) == CANDIDATE_SHA
    # Validate all required files/passages before the first repository write.
    for key, rel in INPUTS.items():
        text = (P / rel).read_bytes().decode('utf-8')
        if key in ('acceptance', 'reader', 'render'):
            passage = getattr(args, key + '_witness')
            assert passage and passage.strip() and passage in text, key
    m, t = read(ORIGINAL / 'manifest.json'), read(ORIGINAL / 'topics' / (TOPIC + '.json'))
    assert m['project_root'] == str(PROJECT)
    assert m['outputs'] == [{'id': 'teaching', 'path': 'teaching-v3.md', 'sha256': TEACHING_SHA}]
    assert m['skill']['sha256'] == CANDIDATE_SHA
    original_inventory = [{ 'path': str(x.relative_to(ORIGINAL)), 'sha256': sha_bytes(x.read_bytes()) }
                          for x in sorted(ORIGINAL.rglob('*')) if x.is_file()]
    shutil.copytree(ORIGINAL, STATE)
    copies, ev = [], {}
    for key, rel in INPUTS.items():
        dst = MIRROR / Path(rel).name
        copies.append(immutable_copy(P / rel, dst))
        if key in ('acceptance', 'reader', 'render'):
            ev[key] = witness(dst, getattr(args, key + '_witness'))
    save(RECORDS / 'author-original-preservation.json', original_inventory)
    save(RECORDS / 'parent-review-mirrors-phase-a.json', copies)
    td = dependencies(topic=True)
    for key, condition in t['requirements'].items():
        add_once(condition['evidence'], ev['acceptance'])
        condition['dependencies'] = td
        if key in ('T11', 'T12'):
            condition.update(status='pass', reason=(
                'Lead completed the final teaching/source/technical/fresh-reader and '
                'representation review at frozen v3, with stated limits. '
                'Main publication is tracked separately and remains pending.'))
            add_once(condition['evidence'], ev['render'])
            add_once(condition['evidence'], ev['reader'])
        else:
            condition['reason'] += (' Lead independently reviewed the complete final v3 route; '
                'unchanged author witnesses are retained with the new parent acceptance witness.')
    save(STATE / 'topics' / (TOPIC + '.json'), t)
    # Snapshot project dependencies after the topic record is reconciled.
    # Topic-record reasoning is not part of inventory hashing; no acceptance claim is inferred.
    pd = dependencies()
    for c in m['output_checks']:
        if c['id'] == 'publication':
            c.update(status='pending', reason='Final r13 and D006 evidence have not yet been '
                'verified on main. Immutable teaching freeze alone is insufficient.',
                evidence=[], dependencies=[])
            continue
        c.update(status='pass', reason='Actual final-v3 review is recorded in lead acceptance; '
                 'publication remains a separate pending check.', evidence=[ev['acceptance']], dependencies=pd)
        if c['id'] in ('destination', 'final_review'):
            add_once(c['evidence'], ev['render'])
        if c['id'] in ('sasis', 'final_review'):
            add_once(c['evidence'], ev['reader'])
    save(STATE / 'manifest.json', m)
    (STATE / 'RUN.md').write_text('Parent-owned D006 final-v3 acceptance at immutable candidate controls. '
        'Teaching reviews complete; main publication remains pending. Publish phase A with D006 '
        'still open and counts 5/76; verify actual main and bytes before phase B. Original author '
        'states and evidence preserved.\n', encoding='utf-8')
    save(RECORDS / 'topic-dependencies-phase-a.json', td)
    save(RECORDS / 'project-dependencies-phase-a.json', pd)
    check('topic-check-phase-a', topic=True)
    check('full-check-phase-a', expect_pending_publication=True)
    save(RECORDS / 'manifest-phase-a-original.json', m)
    save(RECORDS / 'topic-phase-a-original.json', t)
    assert original_inventory == [{ 'path': str(x.relative_to(ORIGINAL)), 'sha256': sha_bytes(x.read_bytes()) }
                                  for x in sorted(ORIGINAL.rglob('*')) if x.is_file()]

def phase_b(args):
    m = read(STATE / 'manifest.json')
    publication = next(c for c in m['output_checks'] if c['id'] == 'publication')
    assert publication['status'] == 'pending', 'No repeated publication promotion.'
    record_path = P / args.publication_record
    assert record_path.resolve().is_relative_to(P.resolve())
    record = read(record_path)
    assert record['remote_main_verified'] is True and record['git_object_bytes_verified'] is True
    assert record['expected_previous_main'] == PREVIOUS_MAIN
    assert record['outgoing_prof'] == '2026-10-08-r13'
    assert record['teaching_sha256'] == TEACHING_SHA
    assert record['observed_at'].strip()
    commit, tree = record['verified_main_commit'], record['verified_main_tree']
    assert re.fullmatch('[0-9a-f]{40}', commit) and re.fullmatch('[0-9a-f]{40}', tree)
    def git(*args):
        return subprocess.check_output(['git', '-C', str(REPO), *args])
    assert git('rev-parse', 'refs/heads/main').decode().strip() == commit
    assert git('rev-parse', commit + '^{tree}').decode().strip() == tree
    teaching_path = 'runs/y1-reader-20261008/iterations/006/regenerated-r13-candidate1/teaching-v3.md'
    assert sha_bytes(git('show', commit + ':' + teaching_path)) == TEACHING_SHA
    skill = git('show', commit + ':SKILL.md')
    assert sha_bytes(skill) == record['outgoing_skill_sha256']
    assert skill.count(b'2026-10-08-r13"') == 1
    assert skill.replace(b'2026-10-08-r13"', b'2026-10-08-r13-candidate1"', 1) == (PROJECT / 'controls/SKILL.md').read_bytes()
    # Actual remote observation is supplied by the lead's authenticated readback record;
    # the read-only local Git checks above verify fetched bytes, not remote visibility.
    dst = MIRROR / 'publication-main-phase-a.json'
    provenance = immutable_copy(record_path, dst)
    save(RECORDS / 'parent-review-mirror-phase-b.json', provenance)
    pd = dependencies()
    publication.update(status='pass', reason='Phase-A main publication was independently observed '
        'and fetched Git tree/SKILL/teaching bytes were verified. Phase-B closure bookkeeping '
        'still must be published and checked before the next author starts.',
        evidence=[witness(dst)], dependencies=pd)
    save(STATE / 'manifest.json', m)
    (STATE / 'RUN.md').write_text('Parent-owned D006 final-v3 acceptance: completed teaching reviews '
        'and verified phase-A main publication. State stays bound to the actual candidate controls '
        'used by the author. Publish phase-B closure/counts, verify main, fully reload actual '
        'published PROF, then fresh D007.\n', encoding='utf-8')
    save(RECORDS / 'project-dependencies-phase-b.json', pd)
    check('topic-check-phase-b', topic=True)
    check('full-check-phase-b')
    # Queue/RUN/activation/closure/Git operations intentionally belong to the lead.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=('phase-a', 'phase-b'))
    parser.add_argument('--acceptance-witness')
    parser.add_argument('--reader-witness')
    parser.add_argument('--render-witness')
    parser.add_argument('--publication-record', default='publication-main-phase-a.json')
    args = parser.parse_args()
    if args.phase == 'phase-a':
        phase_a(args)
    else:
        phase_b(args)
