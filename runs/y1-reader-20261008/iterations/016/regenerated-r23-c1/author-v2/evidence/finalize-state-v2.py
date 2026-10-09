from pathlib import Path
import json,subprocess,hashlib,datetime
P=Path(__file__).resolve().parents[1];O=P.parent/'author';S=P.parent.parent/'candidate-r23-1';state=P/'.prof-state'
def load(p):return json.loads(p.read_text())
def dump(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
t=load(state/'topics/definite-integrals.json');m=load(state/'manifest.json')
for c in t['requirements'].values():
 if c['status']=='pass':c['dependencies']=load(P/'evidence/helper-topic-dependencies-v2.json')
for c in m['output_checks']:
 if c['status']=='pass':c['dependencies']=load(P/'evidence/helper-global-dependencies-v2.json')
dump(state/'topics/definite-integrals.json',t);dump(state/'manifest.json',m)
oldledger=load(O/'evidence/requirements-ledger.json');ledger=[]
for row in oldledger:
 row=dict(row);row['artifact_revision']='d016-r23-c1-learner-v2-local-repair';row['check_method']='Current whole-route reconstruction, exact raw-byte inverse, current static check and explicitly retained immutable v1 scientific/source evidence. External gates pending.'
 if row['id'].startswith('T'):
  row['status']=t['requirements'][row['id']]['status'];row['evidence']=['evidence/route-audit-v2.md','evidence/static-checks-v2.json','evidence/inherited-v1/'+('technical-checks.json' if row['id']=='T10' else 'reconstruction.md')]
  if row['id']=='T11':row['acceptance']='Actual v2 destination must preserve every expression and usable styling/navigation; v1 failure remains historical evidence.'
  if row['id']=='T12':row['acceptance']='Current whole-route author audit complete; final acceptance awaits root external checks. No global completion claim.'
 else:
  row['evidence']='Retained exact original evidence in inherited-v1/ plus current route-audit-v2.md, static-checks-v2.json, retained-evidence-v2.json and this v2 state.'
  if row['id']=='U10':row['status']='pending';row['evidence']='Root reports v2 publication/readback at 80c86f6d11c0cbec403dad2da04ee887ca52ce6f; repaired destination and final acceptance remain pending.'
  if row['id']=='U11':row['acceptance']='Write only newly owned author-v2 subtree; preserve original author; cloud exec only.'
  if row['id']=='U12':row['evidence']='Current checkpoints.md, RUN.md, parent freeze notice and final author-packet-manifest-v2.json; all learner files frozen.'
 ledger.append(row)
for i,(acceptance,evidence,status) in enumerate([
 ('Exactly 14 named displays changed, only delimiter tokens','exact-repair-proof.json and static-checks-v2.json: 14 displays, 28 changed lines, all 316 inline and 46 display payloads unchanged','pass'),
 ('Preserve full TeX and all other learner bytes, accounting for boundary LF','exact-repair-proof.json retains LF after opener and before closer; exact inverse reconstructs every original byte','pass'),
 ('Original packet and v1 evidence immutable','static-checks-v2.json verifies all original 32 packet members plus original manifest read without edits','pass'),
 ('Freeze six current learner files and immediately notify root','learner-manifest-v2.json frozen and sent before subsequent whole-route audit; six hashes verified','pass'),
 ('Read complete current route and affected help/figures','route-audit-v2.md V1–V6 and actual full bounded reads, all 3 PNG views','pass'),
 ('Retain external gates pending, no fresh-generation or release claim','T11/T12, destination/SASIS/final pending; root owns external checks','pass'),
 ('No skill, content, figure, other representation changes','Exact inverse/source byte equality; unchanged r23-candidate1 binding','pass')],1):ledger.append({'id':f'R{i}','trigger':'Explicit consolidated repair request','acceptance':acceptance,'status':status,'evidence':evidence,'artifact_revision':'d016-r23-c1-learner-v2-local-repair','check_method':'Actual current read, raw-byte proof, freeze records and instruction comparison'})
dump(P/'evidence/requirements-ledger-v2.json',ledger)
(state/'RUN.md').write_text('''Local v2 repair recovery index

Exact authority: ../../author-v2/request.txt (within this state root use ../request.txt). Original frozen author packet: ../../author/author-packet-manifest-v1.json. Skill: candidate-r23-1/SKILL.md, version 2026-10-09-r23-candidate1; full path and hash in manifest.json.

Current topic: definite-integrals, complete C0–C7. New learner-v2 is a 14-display delimiter repair after original fresh candidate generation, not another generation. All six files are frozen in learner-manifest-v2.json. Do not rerun repair.py: it is a historical exclusive-create script. Do not edit either v1 or v2 learner files.

Current evidence: evidence/route-audit-v2.md (V1–V6 whole route, complete help, images and actual read/clipping scopes); exact-repair-proof.json (14 blocks, boundary LF and inverse); static-checks-v2.json (all 362 payloads, prompts, local targets, original-packet preservation); inherited-v1 and retained-evidence-v2.json (unchanged earlier source/baseline/scientific evidence, not new performances); requirements-ledger-v2.json. Full original baseline read ranges and source corrections remain in inherited records. New helper dependencies bind all current outputs and relevant original inputs.

State: T1–T10 author pass; T11/T12 pending current destination and final gates. Original v1 failure remains in preserved evidence. No unresolved mathematical/convention question established. Root reports freeze publication/readback; author does not infer actual rendering or student understanding from it. Subject boundaries remain instruction-only, not technical isolation.

Next action: wait for root accepted current destination and fresh v2 reader evidence, then only under root authorization create a separate final state. This packet ends before those gates; retain it frozen. No publication or branch mutation by author.
''')
for scope,args in [('topic',['--topic','definite-integrals']),('full',[])]:
 r=subprocess.run(['python',str(S/'scripts/prof_state.py'),'check','--state',str(state),*args],text=True,capture_output=True)
 (P/f'evidence/helper-{scope}-check-v2.txt').write_text(r.stdout+r.stderr)
 print(scope,r.returncode,r.stdout+r.stderr)
 assert r.returncode==1
 assert 'stale' not in (r.stdout+r.stderr).lower()
