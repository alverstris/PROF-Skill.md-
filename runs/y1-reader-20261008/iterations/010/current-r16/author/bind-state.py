from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parents[6];p=Path(__file__).resolve().parent
# Resolve repository from its script, avoiding implicit current-directory assumptions.
while not (root/'scripts/prof_state.py').exists(): root=root.parent
helper=root/'scripts/prof_state.py';st=p/'.prof-state';mp=st/'manifest.json';m=json.loads(mp.read_text());tp=st/'topics/max-min.json';t=json.loads(tp.read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def evidence(file,text):return {'path':file,'sha256':sha(p/file),'locator':{'kind':'text','value':text}}
specs=[('execution',root/'references/execution-protocol.md','whole','Complete execution protocol: source packets, independent reconstruction, explicit convention choice, actual output checks.'),('domain',root/'references/domain-patterns.md','whole','Complete domain-patterns read; math portion requires model/representation warrants and discriminating checks.'),('state-guide',root/'references/state-tool.md','whole','Complete helper instructions read: actual activation, strict records and bindings, pending destination acceptance.'),('sasis',root/'references/sasis.md','whole','Complete current protocol: author/read separation and frozen two-input reader; no reader launched by author.'),('profile',root/'references/sasis/profile-manifest.json','whole','Complete manifest: frozen four subjects and exact baseline digest; no current-edition claim beyond freeze.'),('reader-contract',root/'references/sasis/student-testing-contract.txt','whole','Complete contract read for author-side role separation and pending reader.'),('reader-role',root/'references/sasis/student-role.txt','whole','Complete reader operating instructions read as author; not used to claim reader execution.'),('rewrite',root/'references/sasis/rewrite-guide.md','whole','Complete rewrite guide read; original draft retained for the local navigation correction.'),('baseline',root/'references/sasis/ocr-baseline-20261007/student-baseline.txt','all-lf1-1377','Complete baseline all1377 physical LF lines read in11 untruncated packets listed in access-record; H240 derivative/domain/mensuration and FM27 series are the actual premises used.'),('conventions',p/'contract-and-conventions.md','whole','Frozen teaching product, scope, baseline and source convention decisions; source errors independently corrected.')]
pdf=p.parent/'source/lec11.pdf';notes=['Cover identity MIT18.01 Fall2006 and terms pointer','Example1 log/x Fig1 values/location and Example2 candidate principle','Fig2 global/local candidates plus Example3 can geometry Fig3 and objective','Can elimination/sign/limits/recovered shape and Fig4, verified algebraic source errors','Unit wire Fig5, correctly differentiated quadratic and candidate values','Fig6 endpoint versus interior result and marker ambiguity']
for i,note in enumerate(notes,1):
 specs.extend([(f'page-{i}-text',p.parent/f'source/page-{i:02}.txt','whole',note+'; complete extracted text read'),(f'page-{i}-image',p.parent/f'source/page-{i:02}.png','whole',note+'; full original rendered page viewed')])
specs.append(('original-pdf',pdf,'pages1-6','All six pages read through complete text plus individually viewed original page renders; unchanged PDF digest verified.'))
m['sources']=[{'id':i,'path':str(f),'sha256':sha(f),'portions':[{'id':portion,'locator':('physical LF lines1–1377, whole file' if i=='baseline' else ('PDF pages1–6, all text/equations/six figures' if i=='original-pdf' else 'whole file')),'disposition':'required','reason':'','evidence':[]}]} for i,f,portion,note in specs]
t['source_reads']=[{'source_id':i,'portion_id':portion,'status':'read','reviewed_sha256':sha(f),'note':note} for i,f,portion,note in specs]
outputs=[('teaching','teaching-v1.md'),*[(f'figure-{i}',str(f.relative_to(p))) for i,f in enumerate(sorted((p/'figures').glob('*.png')),1)]]
m['outputs']=[{'id':i,'path':f,'sha256':sha(p/f)} for i,f in outputs]
m['required_topics']=[{'id':'max-min','title':'D010 all lecture max/min modelling, candidate conditions and boundary comparisons','source_portions':[{'source_id':i,'portion_id':portion} for i,f,portion,note in specs],'outputs':[i for i,f in outputs]}]
text=(p/'author-reconstruction.md').read_text();items={f'T{i}':next(l for l in text.splitlines() if l.startswith(f'T{i} —')) for i in range(1,13)}
for k,line in items.items():
 pending=k in ('T11','T12');t['requirements'][k]={'applicable':True,'status':'pending' if pending else 'pass','reason':line,'evidence':[evidence('author-reconstruction.md',line)],'dependencies':[]}
checks=[('coverage','Compare all source portions with full teaching','pass','Every source portion and figure is mapped in C01–C07, including corrected source formulas and open-domain conditions.','source-coverage.md','All requested subtopics are represented in the single coherent max-min topic.'),('technical','Independently calculate important formulas and full answers','pass','Symbolic derivatives, limits, objective substitution and independent numerical direct geometry agree.','author-reconstruction.md',items['T10']),('navigation-static','Check all task/help anchor matches','pass','Every local fragment link has a declared anchor; no duplicated labels or missing figure files. Actual destination behavior pending.','author-reconstruction.md','R08 — P037–P049 / all help.'),('figures-local','Inspect every final local scientific PNG','pass','All five PNGs directly viewed; source relationships preserved, one annotation moved and re-inspected.','author-reconstruction.md','Revision: teaching-v1.md and five figures exactly as freeze-v1.json.'),('destination','Verify actual GitHub math typography and navigation','pending','Actual GitHub renderer/visual inspection remains parent work.',None,None),('sasis-reader','Fresh separate two-input reader on frozen revision','pending','Author cannot act as SASIS; parent dispatches fresh reader.',None,None),('final_review','Final acceptance with current independent and destination evidence','pending','Author full reconstruction performed; global final acceptance not claimed.',None,None)]
m['output_checks']=[]
for i,desc,status,reason,file,ev in checks:
 # A short locator must actually occur; it points to a whole substantive paragraph in the record.
 m['output_checks'].append({'id':i,'description':desc,'applicable':True,'status':status,'reason':reason,'evidence':[] if file is None else [evidence(file,ev)],'dependencies':[]})
mp.write_text(json.dumps(m,indent=2)+'\n');tp.write_text(json.dumps(t,indent=2)+'\n')
r=subprocess.run([sys.executable,str(helper),'dependencies','--state',str(st)],capture_output=True,text=True);(p/'dependencies.json').write_text(r.stdout);print(r.stdout)
# Copy actual helper-generated snapshots only after the recorded audits.
deps=json.loads(r.stdout)
rt=subprocess.run([sys.executable,str(helper),'dependencies','--state',str(st),'--topic','max-min'],capture_output=True,text=True)
(p/'topic-dependencies.json').write_text(rt.stdout);td=json.loads(rt.stdout)
for rec in t['requirements'].values():
 if rec['status']=='pass':rec['dependencies']=td
issue=(p/'post-freeze-issue.md').read_text().splitlines()[2]
t['requirements']['T1']={'applicable':True,'status':'fail','reason':'Post-freeze independent review identified a too-narrow general definition of least upper bound at P011; correct example conclusions remain supported. Frozen original retained pending complete issue collection.','evidence':[evidence('post-freeze-issue.md',issue)],'dependencies':td}
for rec in m['output_checks']:
 if rec['status']=='pass':
  rec['dependencies']=deps
  # Use complete substantive witness paragraphs, never heading-only selectors.
  for e in rec['evidence']:
   e['locator']['value']=next(l for l in (p/e['path']).read_text().splitlines() if l.startswith(e['locator']['value']))
mp.write_text(json.dumps(m,indent=2)+'\n');tp.write_text(json.dumps(t,indent=2)+'\n')
(st/'RUN.md').write_text('D010 author recovery\n\nExact user constraints: '+str(root/'runs/y1-reader-20261008/requests.md')+'\nSkill r16: '+str(root/'SKILL.md')+'\nCurrent artifact: teaching-v1.md plus five PNGs, frozen by freeze-v1.json. Full controls/baseline/original source read recorded access-record.md. Capability/conventions: contract-and-conventions.md; source map: source-coverage.md; pre-report full reconstruction: author-reconstruction.md. All source and output dependencies declared.\n\nKnown post-freeze issue I01: too-narrow general least-upper-bound definition P011; see post-freeze-issue.md. No mutation of reader inputs. T1 fail; T11/T12 and destination/SASIS/final checks pending. One next action: parent collects full fresh reader/technical/destination issues, then makes one justified local revision and reruns current acceptance. No global queue or skill edit is owned here.\n')
for scope,args in [('topic',['--topic','max-min']),('full',[])]:
 q=subprocess.run([sys.executable,str(helper),'check','--state',str(st),*args,'--json'],capture_output=True,text=True)
 (p/f'{scope}-state-check.json').write_text(q.stdout or q.stderr);print(scope,q.returncode,q.stdout or q.stderr)
