from pathlib import Path
import json,hashlib,subprocess
A=Path(__file__).resolve().parent; state=A/'.prof-state';M=state/'manifest.json';T=state/'topics/definite-integrals.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def evidence(fn,prefix):
 p=A/fn; para=next(x for x in p.read_text().split('\n\n') if x.startswith(prefix));return {'path':fn,'sha256':sha(p),'locator':{'kind':'text','value':para}}
def condition(status,reason,ev=[]):return {'applicable':True,'status':status,'reason':reason,'evidence':ev,'dependencies':[]}
m=json.loads(M.read_text());t=json.loads(T.read_text());m['sources']=[];t['source_reads']=[];assign=[]
paths=[p for p in sorted((A/'inputs').rglob('*')) if p.is_file() and p.name!='prof_state.py' and p != Path(m['skill']['path']) and p != Path(m['request']['path'])]
paths.append(A/'prerequisites-and-conventions.md')
notes={
 'execution-protocol.md':'Full current execution protocol read with clipped late stress section repaired; requires full source coverage and actual reconstruction before acceptance.',
 'sasis.md':'Full current author/reader separation and full-baseline/complete-learner-input conditions read; root owns fresh reader and publication.',
 'state-tool.md':'Full helper schema and truthfulness limits read; pending external gates retained.',
 'domain-patterns.md':'Mathematics/physics pattern read: meaningful representations, conditions and changed application control this topic.',
 'profile-manifest.json':'Full frozen profile identity and four-subject baseline hashes verified; no live-edition claim.',
 'student-testing-contract.txt':'Full reader input boundary and sequential audit contract read; not supplied as subject input.',
 'student-role.txt':'Full short fresh-reader role read for accurate author handoff.',
 'rewrite-guide.md':'Full issue classification and evidence-backed repair guidance read; no skill change by author.',
 'student-baseline.txt':'All1378 LF slots read in15 bounded complete outputs preserving internal CR; prerequisite locators and non-reliance on other lectures in prerequisite record.',
 'continuation-status-reconciliation.json':'Full later scheduling cancellation reconciliation read; disabled schedules preserved, no mutation.',
 'prerequisites-and-conventions.md':'Full current capability/prerequisite/convention decision record: local new geometry and theorem premises, baseline exact sums, signed integrals and simple-interest timing.',
 'lec18.pdf':'All6 pages text and images inspected; source identity and figures1–5, square geometry, line pattern, tags and borrowing fully mapped in author-audit S01–S10.'}
for idx,p in enumerate(paths,1):
 sid=f'input-{idx:02}';note=notes.get(p.name)
 if note is None and p.name.startswith('page-'):
  pg=int(p.stem[-2:]); scopes={1:'cover/course/year',2:'rectangle procedure and square sum',3:'right squares and staircase/pyramids',4:'squeeze, line triangle and derivative pattern',5:'arbitrary tag and simple-interest borrowing',6:'principal/debt integrals and dimensional mistake'}
  note=f'Full page{pg} '+('render visually inspected: ' if p.suffix=='.png' else 'text read and checked against rendered original: ')+scopes[pg]
 if note is None:note='Full supplied source snapshot read; see read-log and source coverage audit.'
 m['sources'].append({'id':sid,'path':str(p),'sha256':sha(p),'portions':[{'id':'whole','locator':'whole file','disposition':'required','reason':'Current author dependency','evidence':[]}]})
 assign.append({'source_id':sid,'portion_id':'whole'});t['source_reads'].append({'source_id':sid,'portion_id':'whole','status':'read','reviewed_sha256':sha(p),'note':note})
learner=json.loads((A/'learner-manifest-v1.json').read_text());m['outputs']=[{'id':f'learner-{idx+1}','path':v['path'],'sha256':v['sha256']} for idx,v in enumerate(learner['files'])];m['required_topics'][0].update({'title':'Definite integral construction, geometric justification and timed borrowing','source_portions':assign,'outputs':[x['id'] for x in m['outputs']]})
records={
'T1':('pass','New local concepts defined and exemplified before dependence; familiar baseline operations compressed.',['W1 —','W5 —']),
'T2':('pass','Rectangle/sum/index geometry, tags and time weights are read and constructed, with matching visuals.',['W1 —','W2 —','W3 —','W5 —']),
'T3':('pass','Containment, division and limiting warrants, introduced theorem/model premises and conditions explicit.',['W2 —','W4 —','W5 —']),
'T4':('pass','Connected square, line, tagged sum and borrowing examples reconstruct from supplied premises.',['W1 —','W2 —','W4 —','W5 —']),
'T5':('pass','Understanding/justification/use triggers application: P1 early supported, P2 reverses monotonicity, P3 changes timing, P4 signs/endpoint.',['Prerequisite decisions from actual baseline','W3 —','W5 —','W6 —']),
'T6':('pass','Every P1–P4 prompt states capability and response criterion; P4 leaves method choice, reasons discriminate lucky outputs.',['W3 —','W6 —']),
'T7':('pass','All four prompts have separate useful hint and full reasoned solution; no learner attempt or error fabricated.',['W6 —']),
'T8':('pass','Durable study applies; P4 separates later recall from changed signed-area transfer and timing suggestion is adjustable.',['W6 —']),
'T9':('pass','Complete actual baseline used; no unrelated course expansion; figures explain containment and time/endpoint mappings locally.',['C1 compresses','W2 —']),
'T10':('pass','Author independently checked technical claims, source defects and every complete answer; external reviewer comparison remains separate.',['D01 established','D02 established','check_author.py independently']),
'T11':('unverified','Source typography/links and actual PNGs checked; actual GitHub parsed math, styling and live navigation pending.',[]),
'T12':('pending','Final acceptance pending root review, fresh SASIS and actual destination evidence; no global completion claim.',[])}
for rid,(status,reason,prefs) in records.items():
 ev=[evidence('author-audit.md',pre) for pre in prefs if pre!='Prerequisite decisions from actual baseline']
 if rid in ['T6','T8']:
  ev.append(evidence('teaching.md','On a later study occasion' if rid=='T8' else 'For $`f(x)=x^2`$ on $`[0,2]`$'))
 t['requirements'][rid]=condition(status,reason,ev)
m['output_checks']=[
 dict(id='coverage',description='Complete source/topic coverage',**condition('pass','All source portions and required representations mapped and inspected; author-side coverage only.',[evidence('author-audit.md','S01.'),evidence('author-audit.md','S05.'),evidence('author-audit.md','S10.') ])),
 dict(id='author_technical',description='Independent author calculations and source defects',**condition('pass','22 mathematical checks and explicit source corrections inspected.',[evidence('author-audit.md','check_author.py independently')])),
 dict(id='local_navigation',description='Local links and help matching',**condition('pass','21 link/anchor checks, all task/help pairs and image files found; not live destination evidence.',[evidence('author-audit.md','Mechanical checks found21')])),
 dict(id='figure_visual',description='All authored PNG content visual inspection',**condition('pass','All4 images inspected; pyramid legend repaired and reread before freeze.',[evidence('author-audit.md','Author full learner reread')])),
 dict(id='github_destination',description='Actual destination math, prose style and navigation',**condition('pending','Root destination review pending.')),
 dict(id='sasis',description='Fresh full-document reader',**condition('pending','Root fresh reader pending.')),
 dict(id='independent_review',description='Independent root technical comparison',**condition('pending','Root solved prompt-only packet before answers; final comparison pending.')),
 dict(id='final_review',description='Full integrated external/final acceptance',**condition('pending','Root owns final acceptance/publication; original author checkpoint remains pending.'))]
M.write_text(json.dumps(m,indent=2)+'\n');T.write_text(json.dumps(t,indent=2)+'\n')
helper=A/'inputs/scripts/prof_state.py'
for scope in ['topic','project']:
 cmd=['python',str(helper),'dependencies','--state',str(state)]+(['--topic','definite-integrals'] if scope=='topic' else [])
 r=subprocess.run(cmd,capture_output=True,text=True);(A/f'{scope}-dependencies.json').write_text(r.stdout);assert r.returncode==0,r.stderr
 print(scope,r.stdout[:140])
