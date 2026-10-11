"""Bind root-approved complete destination evidence without altering old state."""
from pathlib import Path
import argparse, hashlib, json, shutil, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--help-report', required=True)
parser.add_argument('--root-disposition', required=True)
args = parser.parse_args()
base = Path(__file__).resolve().parent
resume = base.parent
project = base/'final-project'
state = project/'.prof-state'
tool = Path('/workspace/scratch/f9c0b7fc7e76/d016-r26b/inputs/prof/scripts/prof_state.py')
help_report = Path(args.help_report).resolve()
root_disposition = Path(args.root_disposition).resolve()
assert help_report.is_file() and root_disposition.is_file()
assert help_report.parent == resume/'help-destination'
assert root_disposition.read_text().strip()

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

records = []
for folder in ['root-destination', 'help-destination']:
    source = resume/folder
    destination = project/'review/destination-20261011'/folder
    destination.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.rglob('*')):
        if path.is_file():
            target = destination/path.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                assert target.read_bytes() == path.read_bytes(), target
            else:
                shutil.copy2(path, target)
            records.append({'source': str(path), 'path': str(target.relative_to(project)),
                            'sha256': sha(target), 'bytes': target.stat().st_size})
shutil.copy2(root_disposition, project/'review/root-final-disposition.md')
(base/'destination-evidence-identities.json').write_text(json.dumps(records, indent=2)+'\n')

lesson = 'review/destination-20261011/root-destination/lesson-live-review.md'
help_path = 'review/destination-20261011/help-destination/'+help_report.name
acceptance = f'''D016 r26b final acceptance reconciliation — 2026-10-11

This additive review resolves the destination limitation for the unchanged six-constituent fresh-r26b generation frozen at 51a78beccef858072b1da8d057ef3dff09878409, generated under the actual published PROF 2026-10-10-r26 package a5e86eac9e9805921473419c48b329bde7bd46ec. Original teaching, reader reports, pending states and failed access observations remain unchanged. Outgoing metadata publication and queue closure are separate later steps.

Identity and retained evidence: all six teaching files match both the immutable freeze and current main 54ebb635d842f1d65c2508b8f921fd32819f5f0c; all 36 operative package files and 35 preserved review/state files match their published identities. The complete fresh SASIS admission/reading, full source/PROF review, root's prompt-first mathematics and complete frozen answer review, source/native-figure checks and scoped affected-earlier checks retain their valid original scopes. No content or dependency change has invalidated them. Their full substantive reconciliation remains in review/coordinator-disposition.md and review/earlier/coordinator-disposition.md.

Actual destination: root's complete lesson audit and the separate complete help/navigation audit cover all 272 expressions (196 lesson and 76 help), preserving operands, operators and grouping in actual live GitHub MathML. Actual teaching prose is normal-weight and normal-style. All three exact embedded figures are readable at the inspected GitHub sizes, and all declared task, hint, solution and return routes are usable. Full visual traversal and matched source/MathML evidence are retained in {lesson} and {help_path}; the raw DOM, MathML, route observations and saved screenshots accompany those reports.

Scope and limits: the lesson's full-page overview contains a sticky overlay, so root's complete overlapping viewport inspection establishes coverage through that region. The curve touches portions of two Figure 3 labels, but their complete characters are readable at the narrower inspected 929-pixel width and map consistently to the caption. Orphan source backticks remain nonmaterial punctuation. Those observations do not establish a material reading failure. No local preview substitutes for these actual-destination checks, and no human learning, retention or mastery result is claimed.

Integrated disposition: the valid full content/source/mathematics/SASIS/earlier-case evidence plus the new complete destination evidence satisfy the applicable T1–T12 duties and all ten declared output checks for this frozen generation. The former destination-access gap is resolved. No verified material failure remains; no substantive PROF change or teaching patch is justified. Root's final gate disposition is preserved in review/root-final-disposition.md. Mechanical helper readiness is recorded separately and does not itself prove these semantic findings.

Publication boundary: this is acceptance of the frozen teaching and its checked outputs, pending verified r27 metadata/evidence publication and a separately verified closure/count checkpoint. Current published counts remain 15 accepted and 61 remaining until that closure; then D016 restores the accepted count to 16 and leaves 60 remaining. All 147 IDs, 76 eligible sessions and 71 exclusions stay fixed; D017 is next. The r27 candidate changes only version metadata under the recorded rolling convention and preserves all r26 operative instructions.
'''
acceptance_path = project/'review/final-acceptance-20261011.md'
acceptance_path.write_text(acceptance)

def witness(path, starts):
    p = project/path
    line = next(s for s in p.read_text().splitlines() if s.startswith(starts))
    return {'path': path, 'sha256': sha(p), 'locator': {'kind': 'text', 'value': line}}

def deps(topic=False):
    command = ['python', str(tool), 'dependencies', '--state', str(state)]
    if topic:
        command += ['--topic', 'definite-integrals']
    return json.loads(subprocess.check_output(command, text=True))

td, gd = deps(True), deps()
topic = json.loads((state/'topics/definite-integrals.json').read_text())
manifest = json.loads((state/'manifest.json').read_text())
destination_witness = witness('review/final-acceptance-20261011.md', 'Actual destination:')
final_witness = witness('review/final-acceptance-20261011.md', 'Integrated disposition:')
limit_witness = witness('review/final-acceptance-20261011.md', 'Scope and limits:')
for key, evidence in [('T11', [destination_witness, limit_witness]), ('T12', [final_witness, limit_witness])]:
    check = topic['requirements'][key]
    assert check['status'] == 'unverified'
    check.update(status='pass', reason='Complete actual destination evidence resolves the previously unverified gate; full retained content evidence and explicit limits are reconciled in the final acceptance record.', evidence=evidence, dependencies=td)
gap = next(x for x in topic['gaps'] if x['id'] == 'destination-access')
assert gap['status'] == 'unverified'
gap.update(status='resolved', reason='The same immutable actual GitHub lesson/help now load, and complete expression, prose style, embedded-figure and navigation checks pass.', next_action='No further destination action for unchanged teaching; proceed to verified publication and closure.', evidence=[destination_witness, limit_witness], dependencies=td)
for check in manifest['output_checks']:
    if check['id'] in ['destination', 'final_review']:
        assert check['status'] == 'unverified'
        check.update(status='pass', reason='The complete current audit and actual-destination evidence are reconciled without editing frozen teaching; semantic scope and limits remain explicit.', evidence=[destination_witness if check['id']=='destination' else final_witness, limit_witness], dependencies=gd)
(state/'topics/definite-integrals.json').write_text(json.dumps(topic, indent=2)+'\n')
(state/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
(state/'RUN.md').write_text('D016 r26b final state, 2026-10-11\n\nFrozen teaching remains at 51a78beccef858072b1da8d057ef3dff09878409 under incoming PROF r26. The complete actual lesson/help destination audit resolves the last gate; see review/final-acceptance-20261011.md and review/destination-20261011/. Original pending state remains preserved in the source project and published history. All semantic acceptance conditions pass within their recorded scope.\n\nNext: verify the r27 metadata-only/evidence release, then publish and verify D016 closure with 16 accepted/60 remaining. Until verified closure, published counts remain 15/61. D017 is next. No teaching, installed-skill, user-computer or automation change.\n')
(base/'final-topic-dependencies.json').write_text(json.dumps(td, indent=2)+'\n')
(base/'final-global-dependencies.json').write_text(json.dumps(gd, indent=2)+'\n')
for name, arguments in [('topic', ['--topic', 'definite-integrals']), ('full', [])]:
    result = subprocess.run(['python', str(tool), 'check', '--state', str(state), *arguments], text=True, capture_output=True)
    (base/f'final-{name}-check.txt').write_text(result.stdout+result.stderr)
    print(name, result.returncode, result.stdout.strip())
    assert result.returncode == 0
result = subprocess.run(['python', str(tool), 'status', '--state', str(state), '--json'], text=True, capture_output=True)
(base/'final-readiness.json').write_text(result.stdout)
assert result.returncode == 0
