from pathlib import Path
import hashlib,json,datetime,subprocess
P=Path(__file__).resolve().parents[1]; I=P.parents[1]; K=I/'candidate-r23-1'; S=I/'current-r22/source';ST=P/'.prof-state'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def record(path,scope,note):
 d=path.read_bytes();return {'path':str(path),'bytes':len(d),'sha256':sha(path),'read_scope':scope,'note':note}
controls={
'SKILL.md':'Full governing skill read before substantial authoring; ordinary duties applied under author role within the authorized self-iteration; no SASIS dispatch by author.',
'references/execution-protocol.md':'Full execution/recovery protocol reread alone after combined-output clipping. Source packets, conventions, gap resolutions, reconstruction and explicit pending gates applied. Attempted later sed 105–153 retrieved only the tail because file has 107 lines; no claim that this later command reread the execution loop.',
'references/domain-patterns.md':'Full file read separately after combined-output clipping; mathematics pattern used for representation, conditions, exact operation and changed application. Other domain patterns read but not activated.',
'references/state-tool.md':'Full file reread alone; helper initialized, topic activated and schema/dependency rules used.',
'references/sasis.md':'Full current protocol read for role boundaries, exact two-input fresh reader under root, instruction-only isolation and frozen outputs.',
'references/sasis/student-testing-contract.txt':'Full contract read, no reader role assumed by author.',
'references/sasis/student-role.txt':'Full operating instruction read as protocol control; root owns fresh dispatch.',
'references/sasis/profile-manifest.json':'Full manifest read to verify operational baseline identity and scope; linked individual subject research/corpus records not opened.',
'references/sasis/rewrite-guide.md':'Full rewrite guide read as linked SASIS control, not used to load prior reports or diagnoses.'}
access={'condition':'Instruction-confined author input whitelist; cloud tools technically capable of broader access. No technical isolation or erased pretraining claimed.','controls':[record(K/k,'whole file',v) for k,v in controls.items()],'baseline':record(K/'references/sasis/ocr-baseline-20261007/student-baseline.txt','LF-delimited lines 1–1377 inclusive','All Mathematics, Further Mathematics selected Core/Stats/Mechanics, Physics and Chemistry read. No subject skipped; no earlier lesson assumed.'),'source':[record(S/'lec18.pdf','PDF pages 1–6 via the whitelisted text/PNG artifacts','Hash independently matches expected original. Every text page and every visual opened; original visual information is not inferred from extracted text alone.')],'clipping_repairs':[
{'attempt':'Combined execution-protocol, domain-patterns and state-tool cat','result':'outer functions output clipped around middle','repair':'each file subsequently output alone with an adequate budget; complete read credited only to those calls'},
{'attempt':'baseline sed 1–850','result':'39733-token output clipped at 9500-token nested cap','repair':'complete replacement coverage by ten bounded ranges below; no read credit based on clipped centre'}],
'author_readback':{'notes':'1–155 then 156–308; final changed paragraphs reread 59–83 and 145–156','hints':'1–51 entire','solutions':'1–186 entire; final changed paragraphs reread 32–55 and 122–149','figures':'all three inspected at actual PNG output; sample rectangle corrected/reinspected'},'external_research':'evidence/research.md gives official URL, actual retrieved line scope and claim use; no third-party search hit used.','prohibited_access':'No earlier teaching, prior root/reviewer/SASIS diagnoses, previous answers, adjacent iteration artifact or installed Windows skill read; no branch/publish mutation.'}
d=(K/'references/sasis/ocr-baseline-20261007/student-baseline.txt').read_bytes();lines=d.splitlines(keepends=True)
# The file has CR bytes in its original payload: report byte positions using actual LF-delimited tool ranges.
lf=d.split(b'\n');starts=[0]
for line in lf[:-1]:starts.append(starts[-1]+len(line)+1)
ranges=[(1,150),(151,300),(301,450),(451,600),(601,730),(731,860),(861,990),(991,1120),(1121,1250),(1251,1377)]
access['baseline']['credited_read_ranges']=[{'lf_lines':[a,b],'byte_start_inclusive':starts[a-1],'byte_end_exclusive':starts[b] if b<len(starts) else len(d),'status':'complete untruncated tool output read'} for a,b in ranges]
for n in range(1,7):
 for ext in ['txt','png']:access['source'].append(record(S/f'page-{n:02}.{ext}','whole text page' if ext=='txt' else 'whole original page image visually inspected',f'PDF page {n}; '+('cover identity' if n==1 else f'printed lecture page {n-1}')+'; substantive correspondence in source-coverage.md.'))
dump(P/'evidence/access-log.json',access)
reqs={
'T1':('pass','New constructions have meaning and conditions before dependent use: width/height, staircase volume, common sample-choice limit, moving endpoint, per-loan age and simple-interest premise.','R1 — notes introduction'),
'T2':('pass','Every consequential unfamiliar form is built and read: b³/n³Σi², scaled cross sections, general c_i sum, definite integral/dummy variable, A(b), growth-weighted integral and endpoint brackets.','R4 — section 3 endpoints'),
'T3':('pass','Pivotal transitions have warrants: geometry and similarity, positive division, squeeze gap, continuity strip bound, declared simple interest and dimensional conversion.','R2 — section 2 construction'),
'T4':('pass','Connected cases run width→sample→sum→limit; geometry→bound→area; moving-edge difference→derivative; per-loan principal→growth→total.','R9 — section 5 interest weighting'),
'T5':('pass','Applicable to all C1–C7 teaching capabilities. Early Q1 follows the first usable result; Q2 changes thickness, Q3 changes origin and monotonicity, Q4 lower boundary, Q5 borrowing timing, Q6 signed rate and total/average distinction.','R10 — section 5 connected calculations'),
'T6':('pass','All six generated tasks identify requested outputs and discriminating explanations; no retained task depends on undisclosed incidental facts. Q3 and Q6 require actual choices rather than headings giving a method.','R11 — ending Q6'),
'T7':('pass','Six matched intermediate hints and six complete reasoned solutions, separated files and specific return links; hypothetical wrong routes are not claimed observations.','R12 — complete hints route'),
'T8':('pass','Durable-study trigger applies to all taught capabilities; Q6 later recall of sum construction is explicitly distinguished from signed-rate transfer. Spacing is an adjustable suggestion.','R11 — ending Q6'),
'T9':('pass','Full baseline used: algebra/calculus/series compressed; geometric sum/volume, arbitrary sample membership, moving endpoint and per-loan timing bridged locally. Figures explain relationships, not decoration.','Starting premises are the baseline'),
'T10':('pass','32 symbolic/rational/containment/unit checks plus actual primary source/visual comparison; source mistakes independently investigated. Root independent review is a separate pending gate.','Audit result and limits.'),
'T11':('pending','Requested Markdown and separated help are complete; local figures inspected and all local targets verified. Actual GitHub math preservation, typography and click navigation remain pending root.','Audit result and limits.'),
'T12':('pending','Whole author route/help/source audit is recorded honestly; global acceptance awaits actual destination, fresh SASIS and root final review. No mastery or final-release claim.','Audit result and limits.')}
# Detailed ledger separate from helper's strict schema.
ledger=[]
for id,(status,reason,marker) in reqs.items():ledger.append({'id':id,'trigger':'Applies to this complete study lesson and all retained teaching/help; T5–T8 capability triggers recorded in source-coverage.md and reconstruction.md.','acceptance':reason,'status':status,'evidence':['evidence/reconstruction.md', 'evidence/technical-checks.json' if id=='T10' else 'evidence/static-checks.json' if id=='T11' else 'evidence/source-coverage.md'],'artifact_revision':'d016-r23-c1-learner-v1','check_method':'Actual full readback and reconstruction, exact calculations and original-source comparison as appropriate; pending checks explicitly not performed.'})
users=[
('U1','Complete current frozen skill and linked required controls','pass','access-log.json lists full actual reads and clipping repairs; helper activation hash matches frozen skill.'),
('U2','Complete four-subject baseline; no prior corpus prerequisites','pass','Ten bounded LF line ranges cover all 1377 lines and full 247840 bytes; relevant baseline operations named in conventions-gaps.md.'),
('U3','Read all original source portions and consequential visuals','pass','Six text pages and six whole PNGs inspected; every source/figure mapped in source-coverage.md; PDF hash checked.'),
('U4','Subject input whitelist and instruction-only isolation','pass','No prior teaching/reports/answers accessed; only specified controls/baseline/source plus narrowly needed official OpenStax read. Shared tooling is not represented as isolated.'),
('U5','Repo-native Markdown instead of PDF/workbook','pass','notes/hints/solutions plus three PNG constituents; no PDF/workbook or unrequested deck.'),
('U6','All proposed prompts frozen before solutions','pass','prompts-only-v1 SHA 6824364976209f1e873c14c4bbaea5048843b8070e45e242eea47e9cd63c9cde sent root; root acknowledged presolutions saved before solution drafting. Root presolutions never accessed.'),
('U7','Freeze complete learner constituents and do not mutate','pass','learner-manifest-v1 contains exact bytes/SHA/read order/figure insertions; final hash comparison required again at packet freeze.'),
('U8','Author evidence, coverage, full route, ledgers and helper','pass','This ledger, source map, reconstruction, access log, scientific/static checks and bound helper records constitute the requested evidence; mechanical partial check must truthfully retain pending output gates.'),
('U9','No SASIS by author or branch publishing','pass','No agent spawned and no branch/remote operation; root owns dispatch/publication.'),
('U10','Actual GitHub destination and final release verification','pending','Explicitly assigned to root; author has not claimed actual destination or final release passed.'),
('U11','Write only owned author subtree; cloud exec; no Windows skill','pass','All authored paths are below exact author root; no user computer/native app operation performed.'),
('U12','Progress checkpoints and full final author-packet manifest','pass','checkpoints.md and RUN.md record progress; root received prompt/learner freezes; final packet manifest lists every owned deliverable/evidence file.')]
for id,condition,status,witness in users:ledger.append({'id':id,'trigger':'Explicit request.txt instruction','acceptance':condition,'status':status,'evidence':witness,'artifact_revision':'d016-r23-c1-author-v1','check_method':'Compare actual records/artifacts and performed tools with literal task instruction.'})
dump(P/'evidence/requirements-ledger.json',ledger)
# Make helper input inventory explicit, including support references and frozen baseline.
m=json.loads((ST/'manifest.json').read_text());sources=[];assign=[];reads=[]
def add_source(id,path,parts,notes,url=None):
 dec={'id':id,'path':str(path),'sha256':sha(path),'portions':[]}
 if url:dec['url']=url
 for pid,loc in parts:
  dec['portions'].append({'id':pid,'locator':loc,'disposition':'required','reason':'Required author input within assigned scope.','evidence':[]});assign.append({'source_id':id,'portion_id':pid});reads.append({'source_id':id,'portion_id':pid,'status':'read','reviewed_sha256':sha(path),'note':notes.get(pid,notes.get('all','Read and applied as recorded in evidence.'))})
 sources.append(dec)
add_source('lecture-pdf',S/'lec18.pdf',[(f'p{i}',f'PDF page {i}; cover' if i==1 else f'PDF page {i}, printed page {i-1}') for i in range(1,7)],{'p1':'Cover title/course/year inspected.','p2':'Rectangle area, x² right sum, original Figure 1 inspected.','p3':'x² rectangles and staircase Figures 2–3, slab sums and pyramid bounds inspected; prism mislabel investigated.','p4':'Squeeze, line triangle Figure 4 and moving-endpoint derivative pattern inspected.','p5':'General rectangle Figure 5, sample sum/integral definition and borrowing rate model inspected.','p6':'Borrowing total, mistaken rate units, per-loan simple interest and settlement integral inspected.'},'https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/d1b3d809b6505825b5cde0cee823fa0f_lec18.pdf')
for i in range(1,7):
 for ext in ['txt','png']:add_source(f'page-{i:02}-{ext}',S/f'page-{i:02}.{ext}',[('whole','whole extracted page' if ext=='txt' else 'whole rendered original page')],{'all':f'Page {i} '+('text read fully' if ext=='txt' else 'image personally inspected')+'; consequential correspondence in source-coverage.md.'})
add_source('baseline',K/'references/sasis/ocr-baseline-20261007/student-baseline.txt',[(f'lines-{a}-{b}',f'LF-delimited lines {a}–{b}') for a,b in ranges],{'all':'Complete four-subject baseline read in bounded ranges; Mathematics calculus/series, FM23/FM30 and physics rate-area rules used; chemistry also read without importing absent university premises.'})
for i,(path,note) in enumerate(controls.items()):
 if path=='SKILL.md':continue
 add_source(f'control-{i}',K/path,[('whole','whole file')],{'all':note})
add_source('conventions',P/'evidence/conventions-gaps.md',[('whole','whole project convention and prerequisite record')],{'all':'Actual local convention and dependency decisions reread and applied; all resolved gaps name taught passage and independent warrant.'})
add_source('research',P/'evidence/research.md',[('whole','whole precise primary-source access/research record')],{'all':'Official OpenStax theorem and finite-jump paragraph checked; source-read limits preserved.'},'https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral')
m['sources']=sources
lm=json.loads((P/'learner-manifest-v1.json').read_text());m['outputs']=[{'id':f'learner-{i}','path':q['relative_path'],'sha256':q['sha256']} for i,q in enumerate(lm['constituents'],1)]
m['required_topics']=[{'id':'definite-integrals','title':'Lecture 18 definite integrals: full C0–C7 source coverage','source_portions':assign,'outputs':[x['id'] for x in m['outputs']]}]
def condition(status,reason,evidence=[]):return {'applicable':True,'status':status,'reason':reason,'evidence':evidence,'dependencies':[]}
def ev(path,needle):
 f=P/path;assert needle in f.read_text();return {'path':path,'sha256':sha(f),'locator':{'kind':'text','value':needle}}
# Use substantive actual paragraphs rather than headings as witnesses.
recon=(P/'evidence/reconstruction.md').read_text().split('\n\n')
evs={id:ev('evidence/reconstruction.md',next(p for p in recon if marker in p)) for id,(_,_,marker) in reqs.items()}
topic=json.loads((ST/'topics/definite-integrals.json').read_text());topic['source_reads']=reads;topic['gaps']=[]
topic['requirements']={id:condition(status,reason,[evs[id]]) for id,(status,reason,_) in reqs.items()}
m['output_checks']=[
 {'id':'coverage','description':'Every original source portion and required subcapability accounted for.',**condition('pass','All six pages and five original figures mapped to substantive teaching; no exclusion.',[ev('evidence/source-coverage.md',next(x for x in (P/'evidence/source-coverage.md').read_text().split('\n\n') if x.startswith('C6 —')))])},
 {'id':'technical','description':'Independent mathematical and unit checks.',**condition('pass','32 actual symbolic/rational/boundary checks passed.',[ev('evidence/technical-checks.json','"Q5_debt"')])},
 {'id':'local-static','description':'Local task matching, syntax and reference checks.',**condition('pass','Six exact prompt matches, 18 unique anchors, all relative targets, paired math delimiters and strict-comparison syntax checked.',[ev('evidence/static-checks.json','"prompt_verbatim_match": true')])},
 {'id':'local-figures','description':'All local constituent images inspected.',**condition('pass','All three figures inspected; Figure 3 label repositioned and inspected again before freeze.',[ev('evidence/reconstruction.md',recon[1])])},
 {'id':'destination-rendering','description':'Actual GitHub operand/operator/grouping preservation and normal prose styling.',**condition('pending','Root owns actual destination rendering and typography verification; local syntax/images cannot pass this gate.')},
 {'id':'destination-navigation','description':'Actual GitHub help/return-link navigation.',**condition('pending','Root owns actual destination navigation; local target checks are insufficient.')},
 {'id':'sasis','description':'Fresh two-input full-document reader after freeze.',**condition('pending','Root dispatches separate fresh reader; author has not run SASIS or seen prior reports.')},
 {'id':'final_review','description':'Root full final acceptance and release.',**condition('pending','Author route/readback evidence complete; actual destination, fresh reader and root final acceptance still pending. No global completion claim.')}
]
dump(ST/'manifest.json',m);dump(ST/'topics/definite-integrals.json',topic)
print('Detailed evidence and pending helper inventory written.')
