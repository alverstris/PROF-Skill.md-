"""Prepare D016 closure from verified phase-A release; never publish."""
from pathlib import Path
import copy, hashlib, json, subprocess

root=Path(__file__).resolve().parent
repo='/workspace/scratch/f9c0b7fc7e76/prof-iteration'
release=json.loads((root/'phase-a-verification.json').read_text())
assert release['status']=='verified' and release['all_planned_paths_and_exact_bytes_match']
commit=release['commit']
run='runs/y1-reader-20261008'
base=run+'/iterations/016/published-r26-20261010/fresh-r26b/closure-20261011'
relbase=base.removeprefix(run+'/')
out=root/'phase-b';out.mkdir(exist_ok=True)
def get(path):
    return subprocess.check_output(['git','-C',repo,'show',commit+':'+path])
old=json.loads(get(run+'/queue.json'));queue=copy.deepcopy(old)
case=next(s for s in queue['sessions'] if s['material_id']=='D016')
assert case['status']=='pending'
case.setdefault('historical_acceptances',[]).append({
    'incoming_prof':case['incoming_prof'],'outgoing_prof':case['outgoing_prof'],
    'published_commit':case['published_commit'],'closure':'iterations/016/closure.md',
    'disposition':'Historical acceptance reopened on 2026-10-10; original record preserved. This is not the current accepted generation.'})
case['incoming_prof']='2026-10-10-r26'
case['outgoing_prof']='2026-10-11-r27'
case['published_commit']=commit
case['status']='closed'
case['source_access']='All six original source pages/texts/figures and the complete baseline were read; complete fresh r26b SASIS, source/PROF/math and affected-earlier audits pass. Actual GitHub preserves all 272 expressions, three embedded figures, normal prose styling and all 30 content links. Final topic/full checks pass mechanically; metadata-only r27 and all 144 release paths were independently read back byte-for-byte. Closure evidence preserves all original reports and frozen teaching.'
case['acceptance_revalidation']={
    'date':'2026-10-11','status':'resolved_by_complete_fresh_r26b_generation_and_full_current_checks',
    'generation':'fresh-r26b','frozen_commit':'51a78beccef858072b1da8d057ef3dff09878409',
    'operative_prof':'2026-10-10-r26','outgoing_prof':'2026-10-11-r27',
    'verified_release_commit':commit,'evidence':relbase+'/closure.md'}
case['current_iteration']={
    'incoming_prof':'2026-10-10-r26','outgoing_prof':'2026-10-11-r27',
    'verified_package_commit':'a5e86eac9e9805921473419c48b329bde7bd46ec',
    'verified_release_commit':commit,'frozen_commit':'51a78beccef858072b1da8d057ef3dff09878409',
    'state':'closed','evidence':relbase+'/closure.md','closure_status':relbase+'/closure-status.json',
    'next_action':'Verify this closure/progress checkpoint, then begin D017 from the actual current published r27 package in a fresh author context.',
    'previous_iteration':case['current_iteration']}
for name in ['closure.md','closure-status.json','phase-a-verification.json']:
    path=relbase+'/'+name
    if path not in case['evidence']:case['evidence'].append(path)
queue['active_readability_scope']['closed']=16
queue['active_readability_scope']['remaining']=60
assert len(queue['sessions'])==147
assert [s['id'] for s in queue['sessions']]==[s['id'] for s in old['sessions']]
assert [(s['material_id'],s['order'],s['readability']) for s in queue['sessions']]==[(s['material_id'],s['order'],s['readability']) for s in old['sessions']]
assert all(a==b for a,b in zip(old['sessions'],queue['sessions']) if a['material_id']!='D016')
counts={'total_ids':147,'eligible':76,'excluded':sum(s['status']=='excluded_by_user_readability_scope' for s in queue['sessions']),
        'accepted':sum(s['status']=='closed' for s in queue['sessions']),'remaining':sum(s['status']=='pending' for s in queue['sessions'])}
assert counts=={'total_ids':147,'eligible':76,'excluded':71,'accepted':16,'remaining':60}
(out/'queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
status={'material_id':'D016','status':'closed','accepted':True,'generation':'fresh-r26b',
        'operative_prof':'2026-10-10-r26','outgoing_prof':'2026-10-11-r27',
        'operative_package_publication':'a5e86eac9e9805921473419c48b329bde7bd46ec',
        'frozen_teaching_commit':'51a78beccef858072b1da8d057ef3dff09878409','verified_release_commit':commit,
        'release_verification':base+'/phase-a-verification.json','final_acceptance':base+'/final-state/review/final-acceptance-20261011.md',
        'state_checks':{'topic':'MECHANICALLY_READY','full':'MECHANICALLY_READY','semantic_limit':'Checks certify declared record mechanics; substantive audit evidence is separate.'},
        'frozen_teaching_unchanged':True,'material_defect_remaining':False,
        'change':'metadata.version only; no operative teaching-rule change',
        'queue':counts,'next':['D017','D018','D019'],
        'closure_publication':'This record is the closure/count candidate. Its own immutable commit and readback are recorded separately after publication; no self-referential identity is invented.',
        'preserved_history':['Original pending-status.json and .prof-state','Original reader/source/math reports','Earlier failed destination attempts','Historical D016 closure and acceptance reopening']}
(out/'closure-status.json').write_text(json.dumps(status,indent=2)+'\n')
closure=f'''D016 r26b closure — 2026-10-11

D016 is accepted after complete fresh generation under published PROF r26, the preserved full SASIS/source/PROF/mathematics audits, scoped affected-earlier checks, complete actual GitHub destination inspection and final topic/full state checks. The exact six teaching constituents remain frozen at 51a78beccef858072b1da8d057ef3dff09878409. The original pending records and earlier reopened closure remain historical evidence.

All 272 expressions preserve their operands, operators and grouping; authored prose uses normal weight/style; all three embedded figures are legible; all 30 content links have actual successful click/landing witnesses. The full review and raw observations are in final-state/review/final-acceptance-20261011.md and its destination-20261011 directory. Recorded nonmaterial punctuation and label overlap remain visible. Evidence is scoped to the inspected desktop Chrome destination; it makes no human-learning, mobile-browser or Overleaf claim.

Outgoing PROF 2026-10-11-r27 changes version metadata only. Exact inverse proof restores the complete r26 root skill bytes, and all other 35 package files are unchanged. Release {commit}, tree {release['tree']}, was fetched from actual origin/main: all 144 mapped files and exact bytes match. See phase-a-verification.json. The final helper remains bound to incoming r26, under which this document was authored, and its mechanical readiness does not substitute for semantic review.

The queue now contains 16 accepted, 60 remaining, 76 eligible and 71 excluded sessions, preserving all 147 original IDs and order. Only D016 changes status. Its prior r22/r23 release identities and acceptance-reopening record are preserved explicitly as history. D017 remains pending and is next, followed by D018 and D019.

This closure/count checkpoint must itself be published and read back before the next generation begins. Its actual commit is recorded in the subsequent verification receipt. No frozen teaching, original report, installed skill, user computer or automation was changed.
'''
(out/'closure.md').write_text(closure)
runtext=(f'D016 r26b accepted; 16 of 76 eligible sessions closed, 2026-10-11\n\n'
         f'Complete current D016 checks pass. The unchanged r26b teaching is frozen at 51a78beccef858072b1da8d057ef3dff09878409. Metadata-only PROF r27 and all 144 release paths were read back from actual publication {commit}; all planned bytes match, the other 35 package files and frozen teaching are unchanged. Full evidence and limits: iterations/016/published-r26-20261010/fresh-r26b/closure-20261011/closure.md.\n\n'
         'Current counts: 16 accepted, 60 remaining, 76 eligible, 71 excluded, all 147 IDs and original order preserved. D017 remains pending and is next; then D018 and D019. Verify this closure/progress checkpoint, reload the actual published r27 package and start D017 with a fresh author context carrying only original inputs and the operational handover. Prior audits do not become new author inputs. Root regains publication ownership only after this closing coordinator returns the verified final pin. No installed-skill, user-computer or automation change.\n\nEarlier dated records follow unchanged.\n\n')
(out/'RUN.md').write_text(runtext+get(run+'/RUN.md').decode())
change=(f'## 2026-10-11 — D016 reaccepted; PROF r27 metadata progression verified\n\n'
        f'The complete fresh r26b generation and all current audits pass, including actual destination preservation of 272 expressions, all three figures, normal prose style and all 30 content links. Release {commit} and all 144 planned bytes were fetched back and verified. r27 changes only metadata.version; no new material failure or teaching repair was invented. D016 restores the queue to 16/76 accepted and 60 remaining. All 147 IDs and 71 exclusions remain; historical acceptance/reopening/pending records are preserved. Next: verify this closure checkpoint and start D017 from published r27 in a fresh context.\n\nEarlier dated entries retain their historical states.\n\n')
(out/'CHANGELOG.md').write_text(change+get(run+'/CHANGELOG.md').decode())
reconciliation={'base':commit,'only_session_changed':'D016','all_other_sessions_equal':True,'all_ids_order_and_readability_equal':True,'counts':counts,
                'historical_release_identity_preserved':case['historical_acceptances'][-1],'next_pending':'D017'}
(out/'queue-reconciliation.json').write_text(json.dumps(reconciliation,indent=2)+'\n')
mapping=[]
def add(local,path):
    data=local.read_bytes();mapping.append({'local_path':str(local),'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()})
for name in ['RUN.md','queue.json','CHANGELOG.md']:add(out/name,run+'/'+name)
for name in ['closure.md','closure-status.json','queue-reconciliation.json']:add(out/name,base+'/'+name)
for name in ['phase-a-verification.json','verify_publication.py','prepare_phase_b.py']:add(root/name,base+'/'+name)
add(root.parent/'root-destination/r27-root-readback.json',base+'/root-r27-readback.json')
plan={'phase':'B','expected_main':commit,'files':mapping,'self_record':'Self hash omitted; publisher adds this exact map file as an additional planned blob.'}
(root/'publication-plan-phase-b.json').write_text(json.dumps(plan,indent=2)+'\n')
add(root/'publication-plan-phase-b.json',base+'/publication-plan-phase-b.json')
(root/'publisher-map-phase-b.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps({'files':len(mapping),'bytes':sum(p['bytes'] for p in mapping),'counts':counts},indent=2))
