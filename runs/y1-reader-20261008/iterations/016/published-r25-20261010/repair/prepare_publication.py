from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,copy

p=Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25')
repo=Path('/workspace/scratch/f9c0b7fc7e76/prof-iteration')
bare=p/'current-verification.git'
expected='18ad505b72fd034589271d70b15d3cae5c50e730'
base_tree='3ed994d5855da0e725f8df801e352abff99fd919'
prefix=Path('runs/y1-reader-20261008/iterations/016/published-r25-20261010')
runprefix=Path('runs/y1-reader-20261008')
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def save(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def old(path):return subprocess.check_output(['git','--git-dir='+str(bare),'show',expected+':'+str(path)])

# Preserve reports and their evidence exactly, including final root supplements.
shutil.copytree(Path('/workspace/scratch/f9c0b7fc7e76/root-review-d016-r25'),p/'reviews/root-independent',dirs_exist_ok=True)
paths=[]
def copyto(src,rel):
    dest=repo/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest);paths.append(str(rel))
for item in json.loads((p/'repair/candidate-package-manifest.json').read_text())['files']:
    if item['changed']:
        assert (repo/item['path']).read_bytes()==(p/'inputs/prof'/item['path']).read_bytes()
        copyto(p/'repair/candidate/prof'/item['path'],Path(item['path']))
for name in ('reviews',):
    for f in sorted((p/name).rglob('*')):
        if f.is_file():copyto(f,prefix/f.relative_to(p))
for f in sorted((p/'.prof-state').rglob('*')):
    if f.is_file():copyto(f,prefix/'author-state'/f.relative_to(p/'.prof-state'))
repair_files=['prepare_candidate.py','create_probe.py','quick_validate.py','finalize_evidence.py','prepare_publication.py','validation.json','probe-original.md','probe-input-identities.json','candidate-package-manifest.json']
for name in repair_files:copyto(p/'repair'/name,prefix/'repair'/name)
for f in sorted((p/'repair/probe-input').iterdir()):copyto(f,prefix/'repair/probe-input'/f.name)

# These readback files describe the already verified frozen r25 publication.
for name in ('frozen-publication-plan.json','frozen-publication-readback.json'):
    if (p/name).exists():copyto(p/name,prefix/name)
status='D016 r25 is frozen and not accepted. Full original SASIS and technical reports, additive technical supplement, root independent work, complete coordinator disposition and failed/unverified state checks are preserved. Two verified local failures motivate r26; no frozen teaching is edited. This commit publishes the focused r26 root package with 34 other package files unchanged. Fetched-byte verification and a fresh-context D016 generation are still required. Counts remain 15 accepted, 61 remaining, 76 eligible, 71 excluded and 147 stable IDs.\n'
(repo/prefix/'STATUS.txt').write_text(status);paths.append(str(prefix/'STATUS.txt'))

before=json.loads((p/'repair/queue-before.json').read_text());after=copy.deepcopy(before)
row=next(r for r in after['sessions'] if r['material_id']=='D016')
row['source_access']='All six original source pages and figures fully re-read under actual r25. Complete frozen r25 teaching/source/reader audits are preserved; D016 remains pending fresh generation under the published repair.'
row['evidence'] += [str(Path('iterations/016/published-r25-20261010')/n) for n in ['freeze.json','reviews/coordinator-disposition.md','repair/validation.json'] if str(Path('iterations/016/published-r25-20261010')/n) not in row['evidence']]
row['current_iteration']={'incoming_prof':'2026-10-10-r25','frozen_commit':expected,'outgoing_prof':'2026-10-10-r26','state':'repair_publication_readback_and_fresh_generation_required','evidence':'iterations/016/published-r25-20261010/reviews/coordinator-disposition.md','next_action':'Verify published r26 bytes, then fresh-context whole D016 generation from original inputs and full baseline; no old teaching or diagnoses before freeze.'}
assert len(after['sessions'])==147
assert len({r['id'] for r in after['sessions']})==147
assert [r['id'] for r in before['sessions']]==[r['id'] for r in after['sessions']]
assert [r['material_id'] for r in before['sessions']]==[r['material_id'] for r in after['sessions']]
assert before['active_readability_scope']==after['active_readability_scope']
assert sum(r['status']=='closed' for r in after['sessions'])==15
assert sum(r['readability']['eligible'] for r in after['sessions'])==76
assert all(a==b for a,b in zip(before['sessions'],after['sessions']) if a['material_id']!='D016')
save(repo/runprefix/'queue.json',after);paths.append(str(runprefix/'queue.json'))
save(p/'repair/queue-reconciliation.json',{'before_sha256':sha((p/'repair/queue-before.json').read_bytes()),'after_sha256':sha((repo/runprefix/'queue.json').read_bytes()),'only_session_changed':'D016; source_access, appended evidence and current_iteration only','all_147_ids_and_order_preserved':True,'other_146_rows_byte_semantically_identical':True,'active_readability_scope_unchanged':True,'closed':15,'remaining':61,'eligible':76,'excluded':71,'historical_reopening_and_closure_records_preserved':True})
copyto(p/'repair/queue-reconciliation.json',prefix/'repair/queue-reconciliation.json')

run=old(runprefix/'RUN.md')
lead=('D016 r25 audited; focused r26 PROF repair publication, 2026-10-10\n\n'
      'The fresh complete D016 r25 generation and original reader/technical reports remain unchanged. Full review confirms a local units overgeneralization and exported title/tick clipping; the six practice answers and source constructions remain correct. The r26 root package strengthens qualitative formula-scope checks and saved-figure inspection. Original reports, additive findings, targeted forward-probe evidence and all earlier-case scope checks are in iterations/016/published-r25-20261010/. No affected earlier accepted case was found.\n\n'
      'D016 remains pending. Actual GitHub article/live checks were unavailable after recorded server errors; no rendering cause is inferred. The author-state checks truthfully remain NOT_READY. This commit publishes the repair; next verify all published bytes and launch D016 from the actual published package in a fresh context carrying only the original inputs and task necessities. D017 follows D016. Counts remain 15/76 accepted, 61 remaining, 71 excluded and all 147 IDs preserved. No installed-skill, user-computer or automation change.\n\n'
      'Earlier records preserved below.\n\n').encode()
(repo/runprefix/'RUN.md').write_bytes(lead+run);paths.append(str(runprefix/'RUN.md'))

records=[]
for rel in sorted(set(paths)):
    f=repo/rel;b=f.read_bytes()
    check=subprocess.run(['git','--git-dir='+str(bare),'show',expected+':'+rel],capture_output=True)
    if check.returncode==0 and check.stdout==b:continue
    records.append({'path':rel,'local_path':str(f),'bytes':len(b),'sha256':sha(b),'git_blob':blob(b)})
plan={'repository':'alverstris/PROF-Skill.md-','branch':'main','expected_head':expected,'base_tree':base_tree,'version':'2026-10-10-r26','files':records,'all_36_package_expected':json.loads((p/'repair/candidate-package-manifest.json').read_text())['files'],'message':'Repair PROF formula-scope and saved-figure checks; preserve full D016 r25 audit'}
save(p/'repair/publication-plan.json',plan)
print(json.dumps({'files_to_publish':len(records),'total_bytes':sum(r['bytes'] for r in records),'expected_head':expected,'package_changed':['SKILL.md','references/execution-protocol.md'],'counts':after['active_readability_scope']['closed']}))
