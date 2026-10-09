from pathlib import Path
import json,hashlib,subprocess
w=Path(__file__).resolve().parent;state=w/'.prof-state';m=json.loads((state/'manifest.json').read_text());t=json.loads((state/'topics/l07-review.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def witness(path,text):return {'path':path,'sha256':sha(w/path),'locator':{'kind':'text','value':text}}
author=(w/'author-evidence.md').read_text()
def reqtext(i):
 start=author.index(f'T{i} ')
 end=author.find('\nT',start+2)
 return author[start:end if end>=0 else len(author)].strip()
def condition(status,reason,evidence):return {'applicable':True,'status':status,'reason':reason,'evidence':evidence,'dependencies':[]}
sources=[];reads=[];assignments=[]
def add(sid,path,loc,note,portion='whole',url=None):
 path=Path(path).resolve();obj={'id':sid,'path':str(path),'sha256':sha(path),'portions':[{'id':portion,'locator':loc,'disposition':'required','reason':'Assigned teaching, control or prerequisite input; not an exclusion.','evidence':[]}]}
 if url:obj['url']=url
 sources.append(obj);assignments.append({'source_id':sid,'portion_id':portion});reads.append({'source_id':sid,'portion_id':portion,'status':'read','reviewed_sha256':sha(path),'note':note})
ctrl=w/'controls'
control_notes={
'references/execution-protocol.md':'Read whole: source-portion inventory, prerequisite-before-use reconstruction, conditional convention questions, revision-bound evidence, checkpoint and truthful final acceptance applied.',
'references/domain-patterns.md':'Read whole reference; mathematical route applies: descriptions mapped to grouped expressions, inference conditions, branch/sign checks and meaningful changed applications. Other domains are not lesson scope.',
'references/state-tool.md':'Read whole: strict manifest/topic schema, current dependency snapshots, source scope binding, separate topic/global readiness and semantic limits applied.',
'references/sasis.md':'Read whole: author uses complete baseline and original source; parent owns separate fresh reader with two inputs and corpus publication; no author masquerading as SASIS.',
'references/sasis/profile-manifest.json':'Read whole: frozen OCR-A-4-subjects-r1 identities, full four-subject content and selected FM Pure/Statistics/Mechanics; hashes and actual isolation limits respected.',
'references/sasis/student-testing-contract.txt':'Read whole: full-document fresh-reader contract, source/author/reader role separation, complete baseline admission and parent closure obligations; not run by this author.',
'references/sasis/student-role.txt':'Read whole: reader instruction prohibits outside subject inputs and requires sequential reconstruction; this author does not claim that reader role.',
'references/sasis/rewrite-guide.md':'Read whole: preserve original evidence, locate earliest supported gap, audit rest, distinguish source/baseline/reader/process errors and avoid unjustified skill rules.'}
for i,(path,note) in enumerate(control_notes.items(),1):add(f'control-{i:02}',ctrl/path,'Whole exact file from pinned commit 905f6443a0e0198c1472c5e671e355b656d4f3bd',note)
add('baseline',ctrl/'references/sasis/ocr-baseline-20261007/student-baseline.txt','Raw UTF-8 characters [0,246945), all 1377 LF; exact ranges in access-record.json','Personally read all four subjects in 17 contiguous chunks, preserving CRCRLF. Relevant math supplied derivative and algebra/trig premises; then reloaded raw ranges [15243,23787), [62829,65894).')
add('delegation',w/'delegated-task.txt','Whole received author assignment','Read entire received task: author-only role, exact source/controls, disjoint ownership, prompt-before-answer sequencing, Markdown product and parent-owned gates.')
add('prerequisites',w/'prerequisite-conventions.md','PK1–PK4, C1–C8 and complete record','Created and inspected complete prerequisite/convention decisions from actual source/baseline reads: real/radian domain, inverse branch and notation, h mapping, positive x for real powers; no prior-lecture assumption.')
src=Path('/workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L07')
notes={1:'Cover identifies MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006 and terms/citation pointer; no individual author is named.',2:'Full hyperbolic definitions/pronunciations, both derivatives, difference-of-squares identity and u,v hyperbola/circle comparison; signs checked against original image.',3:'Full general rules, quotient reconstruction, implicit cubic relation and arcsine derivation; y primes and product grouping confirmed visually.',4:'All nine derivative families, secant calculation, two trig limits/derivative definition, and both arbitrary-real-power derivations; positive x restriction follows ln usage.',5:'Full final exp(x tan^-1 x) calculation; image confirms whole product is exponent and final parenthesised factor includes arctan x+x/(1+x^2).'}
p=src/'lec7.pdf'
obj={'id':'lecture-pdf','path':str(p),'sha256':sha(p),'url':'https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/a30756fe9d577184f205b09bc6d6d005_lec7.pdf','portions':[]}
for i in range(1,6):
 pid=f'p{i:02}';obj['portions'].append({'id':pid,'locator':f'Complete physical PDF page {i}; '+('cover' if i==1 else f'printed page {i-1}'),'disposition':'required','reason':'Entire original five-page lecture assigned.','evidence':[]});assignments.append({'source_id':'lecture-pdf','portion_id':pid});reads.append({'source_id':'lecture-pdf','portion_id':pid,'status':'read','reviewed_sha256':sha(p),'note':'Personally read full extraction and opened full corresponding PNG. '+notes[i]})
sources.append(obj)
for i in range(1,6):
 add(f'lecture-text-{i:02}',src/f'lec7-p{i:02}.txt','Whole page extraction, raw ranges in access-record.json',notes[i]+' Extraction artefacts resolved with original full page image.')
 add(f'lecture-image-{i:02}',src/f'lec7-p{i:02}.png','Complete uncropped rendered original physical page '+str(i),'Personally opened full individual PNG with view_image. '+notes[i])
m['sources']=sources
m['required_topics']=[{'id':'l07-review','title':'Complete Lecture 7: hyperbolic continuation and differentiation review','source_portions':assignments,'outputs':['teaching']}]
m['outputs']=[{'id':'teaching','path':'teaching.md','sha256':sha(w/'teaching.md')}]
coverage_text='All five physical pages and all consequential equations are accounted for; no required portion is excluded or inaccessible.'
fullread_text='After correction the entire current teaching.md was opened with cat in one untruncated tool result (7524 output tokens) and personally read from P001 through P165, including all equations, task prompts, hints, complete solutions and final links.'
m['output_checks']=[
 {'id':'coverage','description':'Author full source/required capability accounting',**condition('pass','All five original pages and eleven source coverage items mapped to actual teaching and task/help locations. Parent final source audit remains a separate gate.',[witness('source-coverage.md',coverage_text)])},
 {'id':'author_full_read','description':'Actual complete author read and prerequisite reconstruction',**condition('pass','Read full current labelled teaching P001–P165 after correction; R01–R08 records core/help/ending reconstruction.',[witness('author-evidence.md',fullread_text)])},
 {'id':'author_math','description':'Author exact mathematical and numerical corroboration',**condition('pass','M01–M08 exact independent checks plus 71 derivative/3 identity numerical corroborations; no SymPy claim.',[witness('math-review.md','An independent check of Q7 uses logarithmic differentiation rather than its displayed quotient route: J>0, ln J=x arctan x-ln(1+x^2).')])},
 {'id':'source_mechanics','description':'Current source-level structure and navigation matching',**condition('pass','165 sequential locators, 32 unique anchors, all 53 internal link occurrences resolve; all task/hint/solution IDs matched and groups separated. Actual destination not certified.',[witness('mechanical-checks.json','"source_level_checks_pass": true')])},
 {'id':'parent_technical','description':'Independent parent final mathematical/source audit',**condition('pending','Parent-owned final review has not been completed by this author; no inference from author checks.',[])},
 {'id':'destination','description':'Actual ordinary GitHub file-view styling/math/navigation',**condition('pending','Parent-owned actual destination inspection and freeze pending; no substitute renderer can pass it.',[])},
 {'id':'fresh_sasis','description':'Separate fresh two-input whole-document SASIS',**condition('pending','Parent must dispatch a new reader with complete frozen baseline and current full document after admission/freeze. Author did not run SASIS.',[])},
 {'id':'final_review','description':'Parent final integrated acceptance across all gates',**condition('pending','Author audit complete; parent final technical/source, destination and fresh SASIS must be resolved at current revision before acceptance.',[])},
 {'id':'publication','description':'Canonical GitHub publication and subsequent verification',**condition('pending','Parent owns publication; this author neither committed nor pushed nor claims closure.',[])}
]
t['source_reads']=reads
for i in range(1,13):
 status='pass' if i<=10 else 'pending'
 reason=reqtext(i)
 t['requirements'][f'T{i}']=condition(status,reason,[witness('author-evidence.md',reason)])
t['gaps']=[{'id':'reciprocal-wording','question':'Which reciprocal operation exactly maps the generated F to G in solution Q2?','consequential':False,'status':'resolved','reason':'First full labelled author read found an under-specified verbal operation; replaced it with replacing factor x^2+1 by its reciprocal. Formulas/prompts unchanged; original draft preserved and whole corrected document reread.','next_action':'No author-side repair remains; parent review pending.','evidence':[witness('check-history.md','Replacing a factor by its reciprocal states exactly how F becomes G.')],'dependencies':[]}]
(state/'manifest.json').write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n');(state/'topics/l07-review.json').write_text(json.dumps(t,indent=2,ensure_ascii=False)+'\n')
(state/'RUN.md').write_text('D007 author recovery index\n\nCanonical incoming PROF: 905f6443a0e0198c1472c5e671e355b656d4f3bd, r13; controls/SKILL.md exact byte copy. Exact user request: controls/runs/y1-reader-20261008/requests.md. Exact author delegation: delegated-task.txt.\n\nCurrent topic: complete l07-review. Source pages 1–5 and full baseline read; see access-record.json and source-coverage.md. Prerequisites/conventions: prerequisite-conventions.md. Current teaching.md SHA256 '+sha(w/'teaching.md')+'. Author evidence: author-evidence.md R01–R08 and T1–T12; math-review.md; mechanical-checks.json.\n\nFirst unlabelled and labelled originals preserved. Only teaching correction is precise reciprocal wording P135. Prompt packet unchanged. Initial mechanical false positive on literal URL underscores is preserved and resolved in check-history.md. No course question or author-side technical gap remains.\n\nPending: parent final technical/source audit, actual GitHub destination styling/navigation/freeze, new fresh SASIS, final acceptance and publication. T11/T12 intentionally pending.\n\nNext action: hand off current frozen teaching/evidence so parent can complete its independent final gates. Do not mark them pass from this author return. On recovery reread exact skill, execution protocol, exact constraints, this index and current artifacts before changes.\n')
for arg,out in [(['--topic','l07-review'],'dependencies-topic.json'),([], 'dependencies-full.json')]:
 r=subprocess.run(['python',str(ctrl/'scripts/prof_state.py'),'dependencies','--state',str(state),*arg],capture_output=True,text=True);(w/out).write_text(r.stdout);assert r.returncode==0,(r.returncode,r.stdout,r.stderr)
tdeps=json.loads((w/'dependencies-topic.json').read_text());fdeps=json.loads((w/'dependencies-full.json').read_text())
for v in t['requirements'].values():
 if v['status']=='pass':v['dependencies']=tdeps
for v in t['gaps']:
 if v['status']=='resolved':v['dependencies']=tdeps
for v in m['output_checks']:
 if v['status']=='pass':v['dependencies']=fdeps
(state/'manifest.json').write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n');(state/'topics/l07-review.json').write_text(json.dumps(t,indent=2,ensure_ascii=False)+'\n')
print('sources',len(sources),'assigned portions',len(assignments),'topic dependency bindings',len(tdeps),'full bindings',len(fdeps))
