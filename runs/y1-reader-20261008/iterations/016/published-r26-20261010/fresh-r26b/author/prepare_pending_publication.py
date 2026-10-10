"""Prepare an evidence-only checkpoint, preserving queue identities and counts."""
import hashlib,json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
pub=root/'publication';pub.mkdir(exist_ok=True)
prefix='runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b'
status={
 'material_id':'D016','generation':'fresh-r26b','status':'pending_destination_verification','accepted':False,
 'operative_prof':'2026-10-10-r26','package_commit':'a5e86eac9e9805921473419c48b329bde7bd46ec','incoming_main':'7e760fcc5bebd0a5017c470c7d593240d5f378da',
 'frozen_teaching_commit':'51a78beccef858072b1da8d057ef3dff09878409','freeze_manifest':prefix+'/freeze-manifest.json',
 'frozen_teaching_unchanged':True,'operative_package_unchanged':True,'verified_material_failure_established':False,'prof_repair_made':False,
 'completed':['Actual36-file published package admission','Complete baseline and original6-page source author admission','Whole fresh teaching generation and unchanged freeze','Prompt-first independent calculations','Fresh full-input SASIS original and access verification','Complete independent source/PROF and mathematics audits','Native figure/source-structure checks','Affected-earlier42-file identities,84 units hits and25 figure views'],
 'remaining':['Actual GitHub preservation of every inline/display expression in lesson and help','Actual destination prose styling','All3 embedded images, including the recorded annotation overlap at actual embedding size','Working task/hint/solution and return navigation','Final T11/T12 and global acceptance'],
 'blocker':'Two actual immutable-page browser attempts returned GitHub Unicorn error pages; no article was available. No HTTP status, auth/security challenge, global outage or document/PROF cause is inferred.',
 'gate_evidence':prefix+'/review/root-independent/live-destination-attempt.json','disposition':prefix+'/review/coordinator-disposition.md','root_disposition':prefix+'/review/root-independent/review-disposition.md',
 'state_checks':{'topic':'NOT_READY','full':'NOT_READY','reason':'Unresolved actual destination checks; no stale or manufactured pass.'},
 'queue':{'total_ids':147,'eligible':76,'excluded':71,'accepted':15,'remaining':61,'next':['D016','D017','D018']},
 'next_action':'Resume the same frozen immutable destination checks when available. Only close D016 after all applicable conditions pass; if a material defect is established, repair/publish/verify PROF first and generate anew in a fresh context.',
 'changes_excluded':['Frozen teaching edits','PROF package edits','Queue advancement','Installed skill edits','User computer operation','Automation changes'],
 'publication_note':'This file records the intended evidence-only checkpoint. Its own publication commit and readback are recorded in the subsequent verification checkpoint; no self-referential commit is invented.'
}
(root/'pending-status.json').write_text(json.dumps(status,indent=2)+'\n')
handover={
 'task':'Continue Jonathan\'s authorized PROF/SASIS corpus iteration; current work is D016 destination completion.',
 'repository':'alverstris/PROF-Skill.md-','operative_package_version':status['operative_prof'],'verified_package_commit':status['package_commit'],
 'frozen_generation_commit':status['frozen_teaching_commit'],'frozen_generation_prefix':prefix,'pending_status_path':prefix+'/pending-status.json',
 'baseline_sha256':'3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5','source_pdf_sha256':'3469042c0ca6aa75aa7e420b2bbf726228c31093aea11ddb2fc0044a4404fec0',
 'queue':status['queue'],'next_action':status['next_action'],'access_limit':status['blocker'],
 'publication_ownership':'Return sole publication ownership to root only after this checkpoint and its saved-byte verification are complete.',
 'constraints':'Canonical actual GitHub root PROF. Preserve all frozen teaching unchanged. No installed skill, user-computer or automation action. Fresh author and reader without inherited conversation after any verified PROF repair/publication. Repo-native Markdown, no bold/italic prose, separate hints/full solutions; complete sources and baseline. No generation should restart merely because a destination is temporarily unavailable.'
}
(root/'operational-handover.json').write_text(json.dumps(handover,indent=2)+'\n')
old=json.loads((root/'review/current-queue.json').read_text());q=json.loads(json.dumps(old))
case=next(s for s in q['sessions'] if s['material_id']=='D016')
case['source_access']='Fresh r26b author read all6 original source pages/texts/figures and the full baseline. Complete unchanged teaching, fresh SASIS and independent source/PROF/math audits are preserved; actual GitHub destination checks remain unverified after two error-page attempts.'
case['current_iteration']={
 'incoming_prof':'2026-10-10-r26','verified_package_commit':status['package_commit'],'frozen_commit':status['frozen_teaching_commit'],
 'state':status['status'],'evidence':prefix.removeprefix('runs/y1-reader-20261008/')+'/review/coordinator-disposition.md','pending_status':prefix.removeprefix('runs/y1-reader-20261008/')+'/pending-status.json','next_action':status['next_action'],
 'previous_iteration':case['current_iteration']}
for name in ['pending-status.json','review/sasis-original.md','review/sasis-access.json','review/source-prof-original.md','review/source-prof-access.json','review/coordinator-disposition.md','review/root-independent/review-disposition.md','review/root-independent/live-destination-attempt.json','review/earlier/coordinator-disposition.md']:
    p=prefix.removeprefix('runs/y1-reader-20261008/')+'/'+name
    if p not in case['evidence']:case['evidence'].append(p)
assert len(q['sessions'])==147
assert [(s['material_id'],s['id'],s['order'],s['status']) for s in old['sessions']]==[(s['material_id'],s['id'],s['order'],s['status']) for s in q['sessions']]
assert len({s['id'] for s in q['sessions']})==147
assert sum(s['status']=='closed' for s in q['sessions'])==15
assert sum(s['status']=='pending' for s in q['sessions'])==61
assert sum(s['status']=='excluded_by_user_readability_scope' for s in q['sessions'])==71
assert q['active_readability_scope']==old['active_readability_scope']
(pub/'queue.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
oldrun=(root/'review/current-RUN.md').read_text()
newrun='D016 r26b complete content audit; destination pending, 2026-10-10\n\nFresh teaching is frozen unchanged at51a78beccef858072b1da8d057ef3dff09878409. Complete fresh SASIS, source/PROF and independent mathematical reviews establish no material content failure. Native figure and source-structure checks and affected-earlier review are preserved under iterations/016/published-r26-20261010/fresh-r26b/. Actual GitHub expression/style/image/navigation checks remain unverified after two Unicorn error-page observations; no document/PROF cause is inferred. See pending-status.json and review/coordinator-disposition.md there. Both topic/full helper checks truthfully remain NOT_READY.\n\nPROF remains actual published r26, package publicationa5e86eac9e9805921473419c48b329bde7bd46ec; all36 package files and all6 frozen teaching constituents are unchanged. D016 remains pending, with15 accepted/61remaining,76eligible/71excluded,all147IDs retained. Do not advance toD017 until D016 is accepted. Next: finish the same immutable destination audit when access is available; no speculative PROF revision or regeneration. No installed-skill, user-computer or automation change. Root regains sole publication ownership after this evidence checkpoint is published and read back.\n\nEarlier dated records follow unchanged.\n\n'
(pub/'RUN.md').write_text(newrun+oldrun)
paths=[]
for folder in ['review','.prof-state']:
    for p in sorted((root/folder).rglob('*')):
        if p.is_file() and p.name not in ['current-queue.json','current-RUN.md']:paths.append((p,prefix+'/'+str(p.relative_to(root))))
for name in ['generation-publication-verification.json','pending-status.json','operational-handover.json','author/declare_state.py','author/finalize_state.py','author/prepare_pending_publication.py']:paths.append((root/name,prefix+'/'+name))
paths += [(pub/'queue.json','runs/y1-reader-20261008/queue.json'),(pub/'RUN.md','runs/y1-reader-20261008/RUN.md')]
plan=[]
for local,remote in paths:
    b=local.read_bytes();plan.append({'local_path':str(local),'path':remote,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()})
(pub/'plan.json').write_text(json.dumps(plan,indent=2)+'\n')
(pub/'queue-reconciliation.json').write_text(json.dumps({'all147_ids_and_order_retained':True,'all_statuses_unchanged':True,'active_readability_scope_unchanged':True,'counts':status['queue'],'changed_case_metadata_only':'D016'},indent=2)+'\n')
print(json.dumps({'planned_files':len(plan),'planned_bytes':sum(p['bytes'] for p in plan),'queue':status['queue']}))
