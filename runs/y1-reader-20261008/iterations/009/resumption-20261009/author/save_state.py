from pathlib import Path
import json,hashlib,subprocess
A=Path(__file__).resolve().parent;R=A.parents[5];S=A/'.prof-state'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,obj):p.write_text(json.dumps(obj,indent=2)+'\n')
def ev(file,text):return {'path':file,'sha256':sha(A/file),'locator':{'kind':'text','value':text}}
m=json.loads((S/'manifest.json').read_text());t=json.loads((S/'topics/curve-sketching.json').read_text())
m['outputs']=[{'id':'teaching','path':'teaching-r15-recovery-v2.md','sha256':sha(A/'teaching-r15-recovery-v2.md')}]+[{'id':p.stem,'path':str(p.relative_to(A)),'sha256':sha(p)} for p in sorted((A/'figures').glob('*.png'))]
source_specs=[('lecture',A.parent/'source/lec10.pdf',[('p'+str(i),'PDF page '+str(i)) for i in range(1,9)]),('baseline',R/'references/sasis/ocr-baseline-20261007/student-baseline.txt',[('all','Complete lines 1–1377, all four subjects')]),('execution',R/'references/execution-protocol.md',[('all','Complete file')]),('domain',R/'references/domain-patterns.md',[('math','Physics and mathematics section')]),('sasis',R/'references/sasis.md',[('all','Complete file')]),('profile',R/'references/sasis/profile-manifest.json',[('all','Complete file')]),('state-guide',R/'references/state-tool.md',[('all','Complete file')]),('archive',A.parents[1]/'runtime-recovery/teaching-pending-write-recovery.md',[('all','Complete archived text, P001–P062')]),('continuation',A.parents[1]/'runtime-recovery/continuation-20261009.json',[('all','Complete file')]),('text-review',A.parents[1]/'runtime-recovery/independent-text-math-review-20261009.md',[('all','Complete file')])]
m['sources']=[];t['source_reads']=[]
for id,p,parts in source_specs:
 assert p.exists(),p
 m['sources'].append({'id':id,'path':str(p),'sha256':sha(p),'portions':[{'id':pid,'locator':loc,'disposition':'required','reason':'Input to recovery author audit','evidence':[]} for pid,loc in parts]})
 for pid,loc in parts:
  t['source_reads'].append({'source_id':id,'portion_id':pid,'status':'read','reviewed_sha256':sha(p),'note':('Actual PDF text/image inspected; substantive page map in source-coverage.md.' if id=='lecture' else 'Actual complete required input read; access ranges and substantive application in author-audit.md.')})
m['required_topics']=[{'id':'curve-sketching','title':'Construct and justify complete qualitative curve sketches','source_portions':[{'source_id':a['id'],'portion_id':p['id']} for a in m['sources'] for p in a['portions']],'outputs':[o['id'] for o in m['outputs']]}]
audit=(A/'author-audit.md').read_text()
for i in range(1,13):
 line=next(line for line in audit.splitlines() if line.startswith(f'T{i} applicable,'))
 t['requirements'][f'T{i}']={'applicable':True,'status':'pass' if i<=10 else ('unverified' if i==11 else 'pending'),'reason':line,'evidence':[ev('author-audit.md',line)],'dependencies':[]}
t['gaps']=[]
coverage='All ten source figures and the second-derivative table are covered.'
m['output_checks']=[{'id':'coverage','description':'All source pages/topics connected to current teaching','applicable':True,'status':'pass','reason':'Full actual PDF reading and full current teaching comparison, not a sample.','evidence':[ev('source-coverage.md',coverage)],'dependencies':[]},{'id':'final_review','description':'Whole final acceptance including destination and fresh reader','applicable':True,'status':'pending','reason':'Author audit complete; root destination verification, independent acceptance and fresh SASIS pending.','evidence':[],'dependencies':[]},{'id':'local_figures','description':'Inspect every current scientific PNG','applicable':True,'status':'pass','reason':'Four replacement plots directly viewed and checked against original-function values, signs and limits.','evidence':[ev('author-audit.md','Each new PNG was directly viewed full-size.')],'dependencies':[]},{'id':'destination','description':'Actual destination mathematics, styling and navigation','applicable':True,'status':'unverified','reason':'Root owns actual destination verification; local source checks do not establish it.','evidence':[],'dependencies':[]}]
write(S/'manifest.json',m);write(S/'topics/curve-sketching.json',t)
(S/'RUN.md').write_text('D009 author recovery only; current r15-recovery-v2 and four new figures frozen. Read author-audit.md, source-coverage.md and author-manifest.json. Historical pending-write outcome and old numerical evidence stay unknown. Author T1–T10 checks pass; T11 unverified and T12/final acceptance pending. Root must complete destination and fresh SASIS checks. No skill or corpus closure asserted.\n')
cmd=['python',str(R/'scripts/prof_state.py')]
subprocess.run(cmd+['begin-topic','--state',str(S),'--topic','curve-sketching'],check=True)
# Save exact helper-generated dependency snapshots after actual semantic checks.
for args,global_check in [(['--topic','curve-sketching'],False),([],True)]:
 result=json.loads(subprocess.check_output(cmd+['dependencies','--state',str(S)]+args,text=True))
 write(A/('global-dependencies.json' if global_check else 'topic-dependencies.json'),result)
 print('dependency_snapshot',global_check,type(result).__name__)
t=json.loads((S/'topics/curve-sketching.json').read_text());m=json.loads((S/'manifest.json').read_text())
for condition in t['requirements'].values():
 if condition['status']=='pass':condition['dependencies']=json.loads((A/'topic-dependencies.json').read_text())
for condition in m['output_checks']:
 if condition['status']=='pass':condition['dependencies']=json.loads((A/'global-dependencies.json').read_text())
write(S/'topics/curve-sketching.json',t);write(S/'manifest.json',m)
for args,name in [(['--topic','curve-sketching'],'topic-state-check.txt'),([],'full-state-check.txt')]:
 p=subprocess.run(cmd+['check','--state',str(S)]+args,text=True,capture_output=True)
 (A/name).write_text(p.stdout+p.stderr+'\nExit code: '+str(p.returncode)+'\n')
 print(name,p.returncode,p.stdout)
