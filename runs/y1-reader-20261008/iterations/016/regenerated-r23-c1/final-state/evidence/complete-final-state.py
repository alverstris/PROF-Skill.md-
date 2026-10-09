from pathlib import Path
import json,hashlib,subprocess,datetime
P=Path(__file__).resolve().parents[1];R=P.parent;ST=P/'.prof-state';V=R/'author-v2';O=R/'author';S=R.parent/'candidate-r23-1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
manifest=R/'destination-v2/evidence-manifest.json';pdf=R/'destination-v2/preview-attempt1/verified-build.pdf'
assert sha(manifest)=='7c56ebcdb67978d2b99f0473042a2b4f932a6f6b064ba09f6dd52fc55c5f7388';assert sha(pdf)=='dd4bf22a876dddc8627578285f876fbbf039153bf179bc2de66535e35d7eb2d3'
(P/'evidence/admitted/destination-evidence-manifest.json').write_bytes(manifest.read_bytes())
dump(P/'evidence/destination-identity-binding.json',{'manifest':{'path':str(manifest),'bytes':manifest.stat().st_size,'sha256':sha(manifest),'members':load(manifest)['file_count'],'self_exclusion':'175 listed members plus manifest =176 files'},'canonical_preview':{'path':str(pdf),'bytes':pdf.stat().st_size,'sha256':sha(pdf)},'author_scope':'Exact manifest parsed and identity bytes hashed; underlying complete176-file archive/roundtrip and full15-page visual/raster work attributed to root/reviewer accepted records, not repeated here.','root_acceptance':'evidence/admitted/root-v2-destination.md'})
m=load(ST/'manifest.json');t=load(ST/'topics/definite-integrals.json')
for sid,src,scope,note in [('destination-full-inventory',manifest,'whole structured file inventory and canonical identity','Complete JSON parsed, all bytes hashed and supplied expected hash verified. Inventory is not a new semantic review of every member; root full archive verification is separately admitted.'),('canonical-preview-identity',pdf,'exact whole-file byte identity of externally inspected canonical PDF','All bytes hashed, size and supplied expected identity verified. Complete visual reading/raster/navigation evidence is performed by root/reviewer and read in their admitted records; no claim of author personally viewing this PDF.')]:
 m['sources'].append({'id':sid,'path':str(src),'sha256':sha(src),'portions':[{'id':'identity','locator':scope,'disposition':'required','reason':'Bind accepted external evidence to its exact inspected artifact identity.','evidence':[]}]})
 m['required_topics'][0]['source_portions'].append({'source_id':sid,'portion_id':'identity'})
 t['source_reads'].append({'source_id':sid,'portion_id':'identity','status':'read','reviewed_sha256':sha(src),'note':note})
dump(ST/'manifest.json',m);dump(ST/'topics/definite-integrals.json',t)
for scope,args in [('topic',['--topic','definite-integrals']),('global',[])]:
 r=subprocess.run(['python',str(S/'scripts/prof_state.py'),'dependencies','--state',str(ST),*args],capture_output=True,text=True);assert r.returncode==0,r.stdout+r.stderr;(P/f'evidence/helper-{scope}-dependencies.json').write_text(r.stdout)
tdeps=load(P/'evidence/helper-topic-dependencies.json');gdeps=load(P/'evidence/helper-global-dependencies.json')
for c in t['requirements'].values():c['dependencies']=tdeps
for g in t['gaps']:g['dependencies']=tdeps
for c in m['output_checks']:c['dependencies']=gdeps
dump(ST/'manifest.json',m);dump(ST/'topics/definite-integrals.json',t)
ledger=load(V/'evidence/requirements-ledger-v2.json')
for row in ledger:
 row['artifact_revision']='d016-r23-c1-learner-v2-local-repair / separate final-state';row['check_method']='Retained performed original/v2 work plus admitted current root/reader/destination evidence, exact identity and final helper freshness checks. No repetition of external review claimed.'
 if row['id'].startswith('T'):
  row['status']='pass';row['evidence']=['evidence/final-reconciliation.md']+[x['path'] for x in t['requirements'][row['id']]['evidence']];row['acceptance']=t['requirements'][row['id']]['reason']
 if row['id']=='U10':
  row['status']='pass';row['acceptance']='Within author scope, actual destination and root final content acceptance verified; publication/readback/corpus closure explicitly retained as separate root operations.';row['evidence']='Root instruction supersedes pending author gate, final-content-acceptance.md and root-destination-v2-disposition.md admitted here; do not infer publication/closure.'
 if row['id']=='U11':row['acceptance']='Write only authorized final-state subtree; preserve every frozen author/author-v2 file, learner file and candidate skill.'
 if row['id']=='U12':row['evidence']='Current checkpoints, RUN and final-state-manifest.json bind final author evidence; root notified after freeze.'
 if row['id']=='R6':row['acceptance']='Retain gates pending until explicit root acceptance; then reconcile in separate final state, never mutate frozen pending packets.';row['evidence']='request.txt records both instructions; original frozen state preserved; current final-reconciliation.md records accepted scope.'
ledger.append({'id':'F1','trigger':'Root final-state delegation','acceptance':'Bind actual candidate/used controls, complete original source/baseline, exact current six outputs and admitted independent evidence, not prospective release','status':'pass','evidence':'manifest.json sources and outputs, learner-bindings.json, final-reconciliation.md','artifact_revision':'final-state','check_method':'Exact hashes and source/portion bindings; performed read scopes retained.'})
ledger.append({'id':'F2','trigger':'Root owns downstream operations','acceptance':'No author learner/skill/publishing changes or corpus closure claim','status':'pass','evidence':'request.txt, final-reconciliation.md and preserved original packet identity','artifact_revision':'final-state','check_method':'Compare actual author operations against exact delegation.'})
dump(P/'evidence/requirements-ledger-final.json',ledger)
(P/'release-provenance.md').write_text('''Release versus authoring provenance

The teaching was generated using the actual immutable candidate r23-candidate1 SKILL hash a01b9c28af398f9bdaa1d6b0e532553e2b3f69ece4666beb5e5cfc7f1d13456b. Local v2 then repaired fourteen display delimiters under that same candidate. This final-state helper remains bound to that candidate and its actual used control files.

Root reports the outgoing r23 release was prepared and structurally validated, differing only by removal of the metadata -candidate1 suffix, and remained unpublished at that message. This is a root report about subsequent release preparation, not the generation dependency and not author verification of outgoing release bytes. Root owns final release publication/readback and corpus closure. Those operations are not inferred from content acceptance or MECHANICALLY_READY.
''')
(ST/'RUN.md').write_text('''Final accepted author/content state recovery index

Authority: ../request.txt preserves exact preparation and subsequent acceptance instructions. Current authoritative reconciliation: ../evidence/final-reconciliation.md. Earlier reconciliation-pending.md is explicitly historical preparatory state. All prior author/author-v2 packets remain frozen.

Actual authoring dependency: candidate-r23-1/SKILL.md, hash a01b9c28af398f9bdaa1d6b0e532553e2b3f69ece4666beb5e5cfc7f1d13456b; exact absolute path in manifest.json. Do not substitute prospective released r23. Generation and later local14-display repair remain distinct; final-state copies are byte-identical current learner-v2, not a new learner revision.

Current topic: definite-integrals, full C0–C7, all six tasks/help and three figures. Source/baseline/control read evidence is retained at its actual performed phase. New complete root/reviewer/SASIS reports read and admitted, exact current payloads and final derivative identity bound. Current sources include the complete original source/baseline and used controls, all accepted independent witnesses, destination inventory and canonical PDF identity. See retained/admitted records, requirements-ledger-final.json and learner-bindings.json.

T1–T12 and declared scoped author/content gates pass. The earlier v1 display failure and v2 pending packet remain historical evidence; no record was overwritten. Explicitly unobserved: live client MathJax/GitHub pixels/computed styles/responsive layout/browser/PDF clicks/Overleaf. Internal PDF is an inspection derivative only. SASIS is instruction-confined document review, not human-learning evidence or technical isolation.

Next action: root independently verifies final bindings, publishes/readbacks final evidence and outgoing release, then closes D016/counts. Author performs no publication or closure. After final-state-manifest.json freeze, create another separately authorized state for any later update; do not mutate this packet or rerun its preparation scripts.
''')
for scope,args in [('topic',['--topic','definite-integrals']),('full',[])]:
 r=subprocess.run(['python',str(S/'scripts/prof_state.py'),'check','--state',str(ST),*args],capture_output=True,text=True)
 (P/f'evidence/helper-{scope}-check-final.txt').write_text(r.stdout+r.stderr)
 print(scope,r.returncode,r.stdout+r.stderr);assert r.returncode==0
