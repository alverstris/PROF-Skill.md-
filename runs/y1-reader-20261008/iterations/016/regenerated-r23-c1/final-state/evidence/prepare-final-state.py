from pathlib import Path
import json,hashlib,subprocess,copy
P=Path(__file__).resolve().parents[1];R=P.parent;V=R/'author-v2';O=R/'author';S=R.parent/'candidate-r23-1';ST=P/'.prof-state';helper=S/'scripts/prof_state.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def run(*args):
 r=subprocess.run(['python',str(helper),*map(str,args)],text=True,capture_output=True);assert r.returncode==0,r.stdout+r.stderr;return r.stdout
assert sha(S/'SKILL.md')=='a01b9c28af398f9bdaa1d6b0e532553e2b3f69ece4666beb5e5cfc7f1d13456b'
for base,name,expected in [(O,'author-packet-manifest-v1.json','080e8984fdb39cec3cb8f89573c1a9a683dbf6d2b5fa1bf6a30a542f7157d546'),(V,'author-packet-manifest-v2.json','403beb58be50edf5134dbcfa33abbce999b9c113f2aa0e7a5ec37d9e0452647e')]:
 assert sha(base/name)==expected
 for f in load(base/name)['files']:
  x=base/f['path'];assert x.stat().st_size==f['bytes'] and sha(x)==f['sha256']
learn=load(V/'learner-manifest-v2.json');rows=[]
for f in learn['constituents']:
 src=V/f['relative_path'];dst=P/f['relative_path'];assert sha(src)==f['sha256'];dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(src.read_bytes());assert sha(dst)==f['sha256'];rows.append({'path':str(dst.relative_to(P)),'source':str(src),'bytes':dst.stat().st_size,'sha256':sha(dst)})
dump(P/'learner-bindings.json',{'revision':learn['revision'],'provenance':'Exact copies of frozen v2; no new learner revision','source_manifest':{'path':str(V/'learner-manifest-v2.json'),'sha256':sha(V/'learner-manifest-v2.json')},'read_order':learn['read_order'],'figure_insertions':learn['figure_insertions'],'constituents':rows})
retained=[]
for rel in ['route-audit-v2.md','exact-repair-proof.json','static-checks-v2.json','requirements-ledger-v2.json','access-log-v2.json','retained-evidence-v2.json','inherited-v1/source-coverage.md','inherited-v1/conventions-gaps.md','inherited-v1/reconstruction.md','inherited-v1/technical-checks.json','inherited-v1/static-checks.json','inherited-v1/access-log.json','inherited-v1/research.md','inherited-v1/requirements-ledger.json']:
 src=V/'evidence'/rel;dst=P/'evidence/retained-v2'/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(src.read_bytes());retained.append({'source':str(src),'copy':str(dst.relative_to(P)),'bytes':dst.stat().st_size,'sha256':sha(dst),'scope':'Exact retained historical record; current acceptance in final-reconciliation.md.'})
external=[('root-v2-content',R/'root-v2-content-review.md'),('root-v2-author',R/'root-author-v2-disposition.md'),('root-v2-parser',R/'root-parser-v2-verification.json'),('root-v2-preview',R/'root-v2-preview-review.json'),('root-v2-sasis',R/'root-sasis-v2-disposition.md'),('sasis-v2-admission',R/'sasis-v2-admission.json'),('sasis-v2-report',R/'sasis-v2/report-original.md'),('sasis-v2-access',R/'sasis-v2/access-log.md'),('root-v2-destination',R/'root-destination-v2-disposition.md'),('root-content-acceptance',R/'final-content-acceptance.md'),('root-issue-register',R/'issue-register-final.json'),('destination-v2-review',R/'destination-v2/review.md'),('destination-v2-audit',R/'destination-v2/final-audit.json'),('root-earlier-disposition',R.parent/'root-earlier-r23-disposition.md')]
copies={}
for sid,src in external:
 dst=P/'evidence/admitted'/f'{sid}{src.suffix}';dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(src.read_bytes());copies[sid]=str(dst.relative_to(P));retained.append({'source':str(src),'copy':str(dst.relative_to(P)),'bytes':dst.stat().st_size,'sha256':sha(dst),'scope':'Complete current original read; admitted by root. Author report-reader, not performer of the underlying external checks.'})
dump(P/'evidence/retained-and-admitted-bindings.json',retained)
run('init','--state',ST,'--skill',S/'SKILL.md','--request',P/'request.txt','--topic','definite-integrals')
m=load(ST/'manifest.json');t=load(ST/'topics/definite-integrals.json');vm=load(V/'.prof-state/manifest.json');vt=load(V/'.prof-state/topics/definite-integrals.json')
m['sources']=copy.deepcopy(vm['sources']);m['required_topics']=copy.deepcopy(vm['required_topics']);t['source_reads']=copy.deepcopy(vt['source_reads'])
for r in t['source_reads']:r['note']='Retained performed author/v2 read at its recorded phase, not a claim of new final-state retrieval. '+r['note']
m['outputs']=[{'id':f'learner-{i+1}','path':x['path'],'sha256':x['sha256']} for i,x in enumerate(rows)]
extras=external+[('original-exact-request',O/'request.txt'),('repair-exact-request',V/'request.txt'),('original-author-manifest',O/'author-packet-manifest-v1.json'),('v2-author-manifest',V/'author-packet-manifest-v2.json'),('v2-learner-manifest',V/'learner-manifest-v2.json'),('final-reconciliation',P/'evidence/final-reconciliation.md')]
for sid,src in extras:
 m['sources'].append({'id':sid,'path':str(src),'sha256':sha(src),'portions':[{'id':'whole','locator':'whole file','disposition':'required','reason':'Exact current or retained input needed for final accepted evidence binding.','evidence':[]}]})
 m['required_topics'][0]['source_portions'].append({'source_id':sid,'portion_id':'whole'})
 note='Complete current final-state read; underlying external work is attributed to its performer and root admission, not claimed repeated by author.' if (sid,src) in external else 'Exact retained original instruction/manifest bound and mechanically checked, or complete authored final reconciliation read. Does not claim repeated historical performance.'
 t['source_reads'].append({'source_id':sid,'portion_id':'whole','status':'read','reviewed_sha256':sha(src),'note':note})
def ev(rel):
 x=P/rel;return {'path':rel,'sha256':sha(x),'locator':{'kind':'lines','start':1,'end':len(x.read_text().splitlines())}}
def cond(reason,rels):return {'applicable':True,'status':'pass','reason':reason,'evidence':[ev(x) for x in rels],'dependencies':[]}
recon='evidence/final-reconciliation.md'; route='evidence/retained-v2/route-audit-v2.md'; orig='evidence/retained-v2/inherited-v1/'
for k,old in vt['requirements'].items():
 reason=old['reason'] if k not in ['T11','T12'] else ('All current destination math/prose/CSS/assets/navigation and complete faithful internal preview accepted by root with explicit unobserved-method limits.' if k=='T11' else 'Full author/source/technical/reader/destination evidence reconciled at exact current bytes; final content acceptance recorded. Root publication and corpus closure remain separate downstream operations.')
 rels=[recon,route]
 if k=='T10':rels +=[orig+'technical-checks.json',orig+'source-coverage.md',copies['root-v2-content']]
 if k=='T11':rels +=[copies['root-v2-destination'],copies['destination-v2-audit'],copies['root-v2-parser'],copies['root-v2-preview']]
 if k=='T12':rels +=[copies['root-content-acceptance'],copies['root-v2-author'],copies['root-v2-sasis']]
 t['requirements'][k]=cond(reason,rels)
t['gaps']=[{'id':'v2-destination-verification','question':'Does actual current destination preserve every expression and adequate styling/navigation?','consequential':True,'status':'resolved','reason':'Root accepted the complete current parser/CSS/asset/navigation and faithful full-preview evidence. All 362 actual types/payloads exact; all 16 thin-space backslashes preserved. Observed scope excludes live browser/client MathJax/Overleaf, as disclosed.','next_action':'No content repair. Root publication/readback and closure remain external bookkeeping.','evidence':[ev(recon),ev(copies['root-v2-destination'])],'dependencies':[]}]
checks=[('coverage','All required original six-page source portions and C0–C7 capabilities accounted for; no exclusion.',[orig+'source-coverage.md',route]),('technical','32 retained independent mathematical/unit checks, unchanged substantive content and independent root current review.',[orig+'technical-checks.json',copies['root-v2-content'],recon]),('local-static','Current v2 exact inverse, all362 source payloads, all6 prompts,18 anchors and relative targets; exact output copies.', ['evidence/retained-v2/static-checks-v2.json','learner-bindings.json']),('local-figures','All three current figures visually inspected by author/root/reviewer and exact bytes retained.',[route,copies['root-v2-content'],copies['destination-v2-audit']]),('destination-rendering','Actual full362 server payloads/types exact, whole prose/labels/assets and retrieved CSS adequate; no live pixel/client/computed-style claim.',[copies['root-v2-parser'],copies['destination-v2-audit'],copies['root-v2-destination']]),('destination-navigation','All18 named targets and40 positive cross-file chains resolve under official anchor-prefix contract; not live clicks.',[copies['destination-v2-audit'],copies['root-v2-destination']]),('internal-preview','Full faithful canonical AST/native navigation and all15 pages accepted; independent root raster identity. Internal derivative only.',[copies['root-v2-preview'],copies['destination-v2-audit'],copies['root-v2-destination']]),('sasis','Fresh whole-baseline/complete-six-constituent reader admitted; no consequential gap; instruction-only isolation.',[copies['sasis-v2-admission'],copies['sasis-v2-report'],copies['sasis-v2-access'],copies['root-v2-sasis']]),('affected-earlier','Root accepted all15 affected earlier sessions/4448 payloads without claiming old regeneration or new unrelated review.',[copies['root-earlier-disposition'],copies['root-content-acceptance']]),('final_review','Root final content/output acceptance supported; helper reconciliation is ready for root binding verification/publication/closure. Does not claim those downstream actions performed.',[recon,copies['root-content-acceptance'],copies['root-v2-destination']])]
m['output_checks']=[dict(id=id,description=reason,**cond(reason,rels)) for id,reason,rels in checks]
dump(ST/'manifest.json',m);dump(ST/'topics/definite-integrals.json',t);run('begin-topic','--state',ST,'--topic','definite-integrals')
for scope,args in [('topic',['--topic','definite-integrals']),('global',[])]:
 out=run('dependencies','--state',ST,*args);(P/f'evidence/helper-{scope}-dependencies.json').write_text(out)
print(json.dumps({'learner_copies':len(rows),'sources':len(m['sources']),'admitted_current_originals':len(external),'retained_and_admitted_copies':len(retained),'phase':'prepared final accepted bindings, not yet ready-state checked/frozen'},indent=2))
