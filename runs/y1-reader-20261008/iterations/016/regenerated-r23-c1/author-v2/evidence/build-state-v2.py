from pathlib import Path
import json,hashlib,subprocess,datetime,copy
P=Path(__file__).resolve().parents[1]; O=P.parent/'author';S=P.parent.parent/'candidate-r23-1';state=P/'.prof-state'; helper=S/'scripts/prof_state.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def call(*a):
 r=subprocess.run(['python',str(helper),*map(str,a)],text=True,capture_output=True);assert r.returncode==0,r.stdout+r.stderr;return r.stdout
oldm=load(O/'.prof-state/manifest.json');oldt=load(O/'.prof-state/topics/definite-integrals.json')
(P/'evidence/inherited-v1').mkdir(exist_ok=True)
retained=['source-coverage.md','conventions-gaps.md','reconstruction.md','technical-checks.json','static-checks.json','access-log.json','research.md','requirements-ledger.json']
retained_rows=[]
for name in retained:
 old=O/'evidence'/name;dest=P/'evidence/inherited-v1'/name;dest.write_bytes(old.read_bytes());retained_rows.append({'source':str(old),'copy':str(dest.relative_to(P)),'bytes':old.stat().st_size,'sha256':sha(old),'scope':'Exact historical v1 evidence; not a new performance of its checks. Current relevance established by exact inverse and v2 full-route audit.'})
dump(P/'evidence/retained-evidence-v2.json',retained_rows)
call('init','--state',state,'--skill',S/'SKILL.md','--request',P/'request.txt','--topic','definite-integrals')
m=load(state/'manifest.json');m['sources']=copy.deepcopy(oldm['sources']);m['required_topics']=copy.deepcopy(oldm['required_topics'])
m['outputs']=[{'id':f'learner-{i+1}','path':x['relative_path'],'sha256':x['sha256']} for i,x in enumerate(load(P/'learner-manifest-v2.json')['constituents'])]
t=load(state/'topics/definite-integrals.json');t['source_reads']=copy.deepcopy(oldt['source_reads'])
for r in t['source_reads']:r['note']='Retained unchanged v1 read evidence for this local repair; not reread anew unless stated in route-audit-v2.md. '+r['note']
extras=[('original-reconstruction',O/'evidence/reconstruction.md'),('original-coverage',O/'evidence/source-coverage.md'),('original-technical',O/'evidence/technical-checks.json'),('original-access',O/'evidence/access-log.json'),('original-ledger',O/'evidence/requirements-ledger.json'),('root-v1-disposition',P.parent/'root-destination-v1-disposition.md'),('root-v1-audit',P.parent/'root-author-v1-audit.md'),('repair-proof',P/'evidence/exact-repair-proof.json'),('current-route',P/'evidence/route-audit-v2.md')]
for sid,path in extras:
 m['sources'].append({'id':sid,'path':str(path),'sha256':sha(path),'portions':[{'id':'whole','locator':'whole file','disposition':'required','reason':'Retained evidence or authorized current local-repair audit input.','evidence':[]}]})
 m['required_topics'][0]['source_portions'].append({'source_id':sid,'portion_id':'whole'})
 t['source_reads'].append({'source_id':sid,'portion_id':'whole','status':'read','reviewed_sha256':sha(path),'note':'Read complete current audit/proof or retained original record. Source-access baseline ranges remain the original author pass; current route is independently reread. See route-audit-v2.md.'})
def ev(path):return {'path':path,'sha256':sha(P/path),'locator':{'kind':'lines','start':1,'end':len((P/path).read_text().splitlines())}}
audit=[ev('evidence/route-audit-v2.md')]
for k,c in oldt['requirements'].items():
 t['requirements'][k]={'applicable':True,'status':'pass' if int(k[1:])<=10 else 'pending','reason':c['reason'] if int(k[1:])<=10 else 'V2 external destination/fresh reader/final gates pending root; original v1 destination failure preserved.','evidence':audit+([ev('evidence/inherited-v1/technical-checks.json')] if k=='T10' else []),'dependencies':[]}
 for_case=t['requirements'][k]
 if int(k[1:])<=10:for_case['reason']='Re-established for v2 by complete current-route audit and exact mathematical/prose identity; original scientific evidence retained. '+for_case['reason']
t['gaps']=[{'id':'v2-destination-verification','question':'Does actual GitHub preserve every current expression and usable styling/navigation after the fence repair?','consequential':True,'status':'open','reason':'V1 failed 14 displays; source repair and inverse proof do not establish actual destination behavior.','next_action':'Await root current destination evidence, fresh v2 reader and acceptance; no learner mutations.','evidence':audit,'dependencies':[]}]
checks=[('coverage','All original C0–C7 source portions retained and current route read.','pass','evidence/route-audit-v2.md'),('technical','Mathematics unchanged; original 32 checks retained, entire current route inspected.','pass','evidence/inherited-v1/technical-checks.json'),('local-static','Exact inverse, all ordered math payloads, six prompts, 18 anchors, 43 local targets checked.','pass','evidence/static-checks-v2.json'),('local-figures','All three current images read and original bytes retained.','pass','evidence/route-audit-v2.md'),('destination-rendering','Actual v2 expression preservation and destination styling pending root.','pending',None),('destination-navigation','Actual v2 destination navigation pending root.','pending',None),('sasis','Fresh v2 two-input reader pending root.','pending',None),('final_review','Root final acceptance pending all current external checks.','pending',None)]
m['output_checks']=[{'id':id,'description':desc,'applicable':True,'status':status,'reason':desc,'evidence':[ev(path)] if path else [],'dependencies':[]} for id,desc,status,path in checks]
dump(state/'manifest.json',m);dump(state/'topics/definite-integrals.json',t)
call('begin-topic','--state',state,'--topic','definite-integrals')
for scope,args in [('topic',['--topic','definite-integrals']),('global',[])]:
 out=call('dependencies','--state',state,*args);(P/f'evidence/helper-{scope}-dependencies-v2.json').write_text(out)
 print(scope+' dependency snapshot captured')
