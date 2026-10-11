"""Prepare an exact additive release map after final gates pass; never publish."""
from pathlib import Path
import hashlib, json, subprocess

root = Path(__file__).resolve().parent
current = root/'current-main'
candidate = root/'candidate'
runpath = Path('runs/y1-reader-20261008')
remote_base = str(runpath/'iterations/016/published-r26-20261010/fresh-r26b/closure-20261011')
project = root/'final-project'
assert 'MECHANICALLY_READY' in (root/'final-topic-check.txt').read_text()
assert 'MECHANICALLY_READY' in (root/'final-full-check.txt').read_text()
assert (project/'review/root-final-disposition.md').is_file()
queue = json.loads((current/runpath/'queue.json').read_text())
case = next(s for s in queue['sessions'] if s['material_id']=='D016')
case['current_iteration'] = {
    'incoming_prof':'2026-10-10-r26',
    'verified_package_commit':'a5e86eac9e9805921473419c48b329bde7bd46ec',
    'frozen_commit':'51a78beccef858072b1da8d057ef3dff09878409',
    'state':'final_acceptance_checked_release_readback_pending',
    'outgoing_prof':'2026-10-11-r27',
    'outgoing_change':'metadata.version only; operative teaching instructions unchanged',
    'evidence':remote_base.removeprefix(str(runpath)+'/')+'/final-state/review/final-acceptance-20261011.md',
    'publication_verification':'pending subsequent immutable release readback',
    'next_action':'Verify release bytes, then publish and verify D016 closure/counts before D017 generation.',
    'previous_iteration':case['current_iteration']}
case['source_access']='Complete original six-page source, baseline, fresh r26b SASIS, source/PROF/math, affected-earlier and actual destination audits pass. All 272 expressions, three embedded figures, prose styling and 30 content links are verified. D016 closure awaits this release readback and the closure/count checkpoint.'
evidence = remote_base.removeprefix(str(runpath)+'/')+'/final-state/review/final-acceptance-20261011.md'
if evidence not in case['evidence']:
    case['evidence'].append(evidence)
assert case['status']=='pending'
assert sum(s['status']=='closed' for s in queue['sessions'])==15
assert sum(s['status']=='pending' for s in queue['sessions'])==61
out=candidate/runpath
(out/'queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
run=('D016 r26b final checks complete; r27 release readback pending, 2026-10-11\n\n'
     'The unchanged fresh-r26b teaching frozen at 51a78beccef858072b1da8d057ef3dff09878409 now has complete actual GitHub destination evidence. All 272 expressions, all three embedded figures, normal prose styling and all 30 content links pass within the recorded desktop-browser scope. Prior complete SASIS/source/PROF/mathematics and affected-earlier evidence remains valid. Final topic and full helper checks are MECHANICALLY_READY; they certify record mechanics only. See iterations/016/published-r26-20261010/fresh-r26b/closure-20261011/final-state/review/final-acceptance-20261011.md.\n\n'
     'PROF 2026-10-11-r27 changes version metadata only; its exact inverse restores the complete r26 SKILL bytes and the other 35 package files are unchanged. This release requires immutable byte readback before D016 closure. Published counters remain 15 accepted/61 remaining; all 147 IDs, 76 eligible and 71 excluded are preserved. Next: verify release, publish and verify 16/60 closure, then start D017 from the actual published package in a fresh context. Original pending/access-failure records and frozen teaching remain unchanged. No installed-skill, user-computer or automation change.\n\n'
     'Earlier dated records follow unchanged.\n\n')
(out/'RUN.md').write_text(run+(current/runpath/'RUN.md').read_text())
change=('## 2026-10-11 — PROF r27 metadata progression; D016 final checks complete\n\n'
        'Complete live destination checks resolve D016 r26b\'s last pending gate without changing teaching. Final semantic reconciliation and both helper checks pass within their recorded scopes. r27 changes metadata.version only under the rolling convention; the operative rules remain r26. Exact identity/inverse evidence and raw destination records are retained under iterations/016/published-r26-20261010/fresh-r26b/closure-20261011/. Release readback and closure remain separate: current counters are 15/76 accepted, 61 remaining until verified closure.\n\n'
        'Earlier dated entries retain their historical states.\n\n')
(out/'CHANGELOG.md').write_text(change+(current/runpath/'CHANGELOG.md').read_text())

mapping=[]
def add(local, remote):
    data=local.read_bytes()
    mapping.append({'local_path':str(local),'path':remote,'bytes':len(data),
                    'sha256':hashlib.sha256(data).hexdigest(),
                    'blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()})
add(candidate/'SKILL.md','SKILL.md')
for name in ['RUN.md','queue.json','CHANGELOG.md']:
    add(out/name,str(runpath/name))
for path in sorted(project.rglob('*')):
    if not path.is_file():
        continue
    rel=path.relative_to(project)
    if rel.parts[0]=='publication' or rel.as_posix() in ['review/current-RUN.md','review/current-queue.json','pending-status.json','operational-handover.json']:
        continue
    if rel.parts[0]=='author' and path.suffix=='.py':
        continue
    add(path,remote_base+'/final-state/'+rel.as_posix())
for name in ['check_identities.py','git-tree-identity-check.json','preclosure-identity-check.json','prepare_final_project.py','final-state-relocation.json','finalize_state.py','destination-evidence-identities.json','metadata-only-r27-proof.json','r27-basic-validation.json','final-topic-dependencies.json','final-global-dependencies.json','final-topic-check.txt','final-full-check.txt','final-readiness.json','prepare_phase_a.py','independent/closure-gate-crosscheck.md']:
    add(root/name,remote_base+'/'+name)
assert len({x['path'] for x in mapping})==len(mapping)
for item in mapping:
    assert item['path']=='SKILL.md' or item['path'].startswith(str(runpath)+'/')
plan={'phase':'A','expected_main':'54ebb635d842f1d65c2508b8f921fd32819f5f0c','expected_base_tree':'3999a55e098d6800ccf95434c201883efcc4647f',
      'purpose':'Publish metadata-only r27 and final additive evidence; counters intentionally remain 15/61 until verified phase-B closure.',
      'files':mapping,'self_record':'This map omits its own hash; the publisher adds this exact file as an additional planned blob.',
      'forbidden_mutations':['Existing frozen teaching paths','Original reports and pending records','Shared working-tree/index changes','Installed skill','User computer','Automations']}
(root/'publication-plan-phase-a.json').write_text(json.dumps(plan,indent=2)+'\n')
add(root/'publication-plan-phase-a.json',remote_base+'/publication-plan-phase-a.json')
(root/'publisher-map-phase-a.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps({'files':len(mapping),'bytes':sum(x['bytes'] for x in mapping),'path':'publisher-map-phase-a.json'},indent=2))
