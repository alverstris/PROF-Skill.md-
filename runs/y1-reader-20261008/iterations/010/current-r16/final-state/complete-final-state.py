from pathlib import Path
import copy, hashlib, json, shutil, subprocess, sys

p = Path(__file__).resolve().parent
case = p.parent
author = case / 'author'
root = p
while not (root / 'scripts/prof_state.py').exists():
    root = root.parent
st = p / '.prof-state'
helper = root / 'scripts/prof_state.py'
def sha(f): return hashlib.sha256(f.read_bytes()).hexdigest()
def rel(f): return str(f.relative_to(root))
def write(f, x): f.write_text(json.dumps(x, indent=2) + '\n')
def ev(f, prefix):
    text = next(s for s in f.read_text().splitlines() if s.startswith(prefix))
    return {'path': rel(f), 'sha256': sha(f), 'locator': {'kind': 'text', 'value': text}}

# Preserve the actual pending state before any promotion or activation write.
saved = p / 'pending-scaffold'
assert not saved.exists(), 'Pending scaffold must never be overwritten'
saved.mkdir()
shutil.copytree(st, saved / '.prof-state')
for name in ['dependencies.json', 'topic-dependencies.json', 'topic-check.json', 'full-check.json', 'path-index.json', 'activation.log', 'init.log']:
    shutil.copy2(p / name, saved / name)
write(saved / 'inventory.json', [{'path': str(f.relative_to(saved)), 'bytes': f.stat().st_size, 'sha256': sha(f)} for f in sorted(saved.rglob('*')) if f.is_file()])

m = json.loads((st / 'manifest.json').read_text())
t = json.loads((st / 'topics/max-min.json').read_text())
assert Path(m['skill']['path']) == p / 'inputs/SKILL-r16.md'
assert sha(Path(m['skill']['path'])) == m['skill']['sha256'] == 'd408ddd2ca6d377f484be84ca4c3213e7e8b06b69840984303beab46172bb557'
assert sha(Path(m['request']['path'])) == m['request']['sha256']
for s in m['sources']: assert sha(Path(s['path'])) == s['sha256'], s['id']
for out in m['outputs']: assert sha(root / out['path']) == out['sha256'], out['id']
for r in [*t['requirements'].values(), *m['output_checks']]:
    for e in r['evidence']:
        if e['path'] != '@request': assert sha(root / e['path']) == e['sha256'], e['path']
for item in json.loads((author / 'freeze-v2.json').read_text())['learner_constituents']:
    assert sha(root / item['path']) == item['sha256']
for item in json.loads((author / 'artifact-inventory.json').read_text()):
    assert sha(author / item['path']) == item['sha256']
for item in json.loads((author / 'artifact-inventory-v2.json').read_text())['files']:
    assert sha(author / item['path']) == item['sha256']

new = [('reader-v2', case / 'sasis-reader-v2-original.md'), ('admission-v2', case / 'sasis-admission-v2.json'), ('root-sasis-v2', case / 'root-sasis-disposition-v2.md'), ('root-final-v2', case / 'final-acceptance.md'), ('root-destination-v2', case / 'root-destination-v2-disposition.md'), ('root-repair-v2', case / 'root-v2-repair-verification.md'), ('final-reconciliation', p / 'final-evidence-disposition.md')]
assert sha(new[0][1]) == 'c680a76d043604e6b1eee4d2652d14911fd903df767e17953aa71b766ac18cf3'
for ident, f in new:
    m['sources'].append({'id': ident, 'path': str(f), 'sha256': sha(f), 'portions': [{'id': 'whole', 'locator': 'whole file', 'disposition': 'required', 'reason': '', 'evidence': []}]})
    t['source_reads'].append({'source_id': ident, 'portion_id': 'whole', 'status': 'read', 'reviewed_sha256': sha(f), 'note': 'Actually read in full; original reader ranges1–70,71–140,141–211. Current final-evidence-disposition.md records substantive admission, issue reconciliation and limitations. Dispatch and earlier pending language remain historical.'})
m['required_topics'][0]['source_portions'] = [{'source_id': s['id'], 'portion_id': v['id']} for s in m['sources'] for v in s['portions']]
d = p / 'final-evidence-disposition.md'
common = [ev(d, 'Current acceptance.'), ev(d, 'Destination limits.'), ev(d, 'Frozen generation and remaining action.')]
t['requirements']['T12'] = {'applicable': True, 'status': 'pass', 'reason': 'Complete current-v2 source, teaching, independent technical, fresh-reader and observed destination evidence reconciled; no supported material issue remains. Scope and unobserved runtime/human-outcome boundaries are explicit. Publication is separate.', 'evidence': copy.deepcopy(common), 'dependencies': []}
t['requirements']['T1']['reason'] = t['requirements']['T1']['reason'].replace('Fresh reader acceptance remains separate and pending.', 'Fresh v2 reader acceptance is now separately established by the original complete report and root disposition; the original author audit remains preserved.')
for rec in m['output_checks']:
    if rec['id'] == 'sasis-reader':
        rec.update(status='pass', reason='Fresh two-input v2 reader admission and full-document original report independently dispositioned; all P001–P049, five actual figures and complete help covered. No supported material mathematical/accessibility defect remains. Instruction-only isolation and source-history remit limits preserved.', evidence=[ev(d, 'Reader acceptance.'), ev(d, 'Issue disposition.'), ev(case / 'root-sasis-disposition-v2.md', 'Accepted:')], dependencies=[])
    if rec['id'] == 'final_review':
        rec.update(status='pass', reason='Root accepted full exact-v2 content after complete source/technical/teaching/reader/destination reconciliation. Current author independently read actual final evidence and verified unchanged prior witnesses; no learner outcome or publication is inferred.', evidence=copy.deepcopy(common) + [ev(case / 'final-acceptance.md', 'Teaching duties pass')], dependencies=[])
write(st / 'manifest.json', m)
write(st / 'topics/max-min.json', t)
r = subprocess.run([sys.executable, str(helper), 'begin-topic', '--state', str(st), '--topic', 'max-min'], capture_output=True, text=True)
(p / 'final-activation.log').write_text(r.stdout + r.stderr)
assert r.returncode == 0
t = json.loads((st / 'topics/max-min.json').read_text())
def snapshot(args, name):
    r = subprocess.run([sys.executable, str(helper), 'dependencies', '--state', str(st), *args], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    (p / name).write_text(r.stdout)
    return json.loads(r.stdout)
g = snapshot([], 'dependencies.json')
local = snapshot(['--topic', 'max-min'], 'topic-dependencies.json')
for rec in t['requirements'].values():
    assert rec['status'] == 'pass'
    rec['dependencies'] = local
for rec in m['output_checks']:
    assert rec['status'] == 'pass'
    rec['dependencies'] = g
write(st / 'manifest.json', m)
write(st / 'topics/max-min.json', t)
(st / 'RUN.md').write_text('D010 final accepted content state\n\nFrozen r16 skill: ' + rel(p / 'inputs/SKILL-r16.md') + '\nExact request: ' + rel(p / 'inputs/requests.md') + '\nFrozen teaching: ' + rel(author / 'teaching-v2.md') + ' and five figures in freeze-v2.json.\nT1–T12 and all declared output checks pass for the precise evidence scope in final-evidence-disposition.md. Original author states and pending-scaffold are preserved.\nNo live-browser rendering, human learning outcome, publication or corpus closure is inferred. Next action: root publishes accepted metadata/evidence with expected-head protection, verifies canonical blobs/head, then separately records closure.\nAll output/evidence paths and path-index.json recovery locators are repo-relative. Helper-required absolute inputs bind the frozen r16 snapshot, not the changing top-level SKILL.md.\n')
idx = {'repository_root_at_check': str(root), 'skill': rel(Path(m['skill']['path'])), 'request': rel(Path(m['request']['path'])), 'sources': {s['id']: rel(Path(s['path'])) for s in m['sources']}, 'outputs': {o['id']: o['path'] for o in m['outputs']}, 'state_path': rel(st), 'schema_note': 'Helper schema requires absolute project/skill/request/source paths. Rebase their checkout prefix on recovery and verify exact recorded hashes; output/evidence paths already repository-relative.'}
write(p / 'path-index.json', idx)
results = {}
for name, args in [('topic', ['--topic', 'max-min']), ('full', [])]:
    r = subprocess.run([sys.executable, str(helper), 'check', '--state', str(st), *args, '--json'], capture_output=True, text=True)
    (p / f'{name}-check.json').write_text(r.stdout or r.stderr)
    results[name] = {'exit_code': r.returncode, 'result': json.loads(r.stdout)}
    print(name, r.returncode, r.stdout)
    assert r.returncode == 0
write(p / 'completion-check-results.json', {'checks': results, 'all_six_frozen_constituents_match': True, 'historical_author_v1_and_v2_inventories_unchanged': True, 'pending_scaffold_preserved': True, 'skill_binding': m['skill'], 'publication_performed': False})
write(p / 'artifact-inventory.json', [{'path': rel(f), 'bytes': f.stat().st_size, 'sha256': sha(f)} for f in sorted(p.rglob('*')) if f.is_file() and f != p / 'artifact-inventory.json'])
