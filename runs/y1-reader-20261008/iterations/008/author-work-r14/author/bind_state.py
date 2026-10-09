from pathlib import Path
import json,hashlib,subprocess
p=Path(__file__).resolve().parents[1];state=p/'.prof-state'
h=lambda x:hashlib.sha256(Path(x).read_bytes()).hexdigest()
manifest=json.loads((state/'manifest.json').read_text());topic=json.loads((state/'topics/local-approximations.json').read_text())
def ev(path):
 q=p/path;return {'path':path,'sha256':h(q),'locator':{'kind':'lines','start':1,'end':len(q.read_text().splitlines())}}
sources=[];assignments=[];reads=[]
def source(sid,rel,parts,note,url=None):
 q=p/rel
 src={'id':sid,'path':str(q),'sha256':h(q),'portions':[]}
 if url:src['url']=url
 for pid,loc in parts:
  src['portions'].append({'id':pid,'locator':loc,'disposition':'required','reason':'Required exact input or necessary support for this author condition.','evidence':[]})
  assignments.append({'source_id':sid,'portion_id':pid})
  reads.append({'source_id':sid,'portion_id':pid,'status':'read','reviewed_sha256':h(q),'note':note})
 sources.append(src)
source('lecture-pdf','inputs/original-source/lec9.pdf',[(f'p{n:02}',f'physical PDF page {n}; '+('attribution cover' if n==1 else f'printed lecture page {n-1}')) for n in range(1,8)],'All seven pages actually read as complete extraction and opened full PNGs. Substantive per-page findings and learner locations: author/source-coverage.md S1–S7. Original PDF identity independently verified.', 'https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/40cb41807e6d67373f3299ce87c4d9b3_lec9.pdf')
for n in range(1,8):
 for ext in ['txt','png']:
  source(f'page{n}-{ext}',f'inputs/original-source/lec9-p{n:02}.{ext}', [('whole',f'full page{n} {ext} including all labels/footnotes/ending')], 'Full original-derived page actually '+('read without clipping.' if ext=='txt' else 'opened with view_image and inspected; not inferred from text.')+' Details in source-coverage.md.')
controls=['references/execution-protocol.md','references/domain-patterns.md','references/state-tool.md','references/sasis.md','references/sasis/profile-manifest.json','references/sasis/student-testing-contract.txt','references/sasis/student-role.txt','references/sasis/rewrite-guide.md','runs/y1-reader-20261008/requests.md']
for n,rel in enumerate(controls,1):source(f'control-{n}',f'inputs/{rel}',[('whole','whole exact git object at e35a59a64ed1b01f7ae43e4ef46042f23cc7e2d6')],'Actually read complete control; access-record.md records bounded read/recovery. Governs execution, scope, author-only role, baseline or pending reader/release gates.')
source('baseline','inputs/references/sasis/ocr-baseline-20261007/student-baseline.txt',[('whole','all four subjects, raw UTF-8 character range [0,246945), CRCRLF preserved')],'Read all fourteen overlapping ranges in order without clipping; exact ranges in access-record.md. Immediate derivative/integral/FM27 passages reopened. Prerequisite grants and limits in conventions-prerequisites.md.')
source('conventions','author/conventions-prerequisites.md',[('whole','complete B1–B6, C1–C5 and consequential gap decisions')],'Authored and applied from actual source/baseline: fixed basepoint, displacement, radian/real domains, little-o rules and time-interval/model scope precede uses.')
source('research','author/research.md',[('whole','R1/R2 actual opened text scope and limitations')],'Read official R1 full returned text and R2 full returned text as recorded; only specified inertial-clock interpretation and GPS motivation used. No uninspected image or future/current-performance claim imported.')
source('prompt-freeze','task-prompts-original.md',[('whole','all four complete stable generated prompts before solutions')],'Prompt bodies frozen before full solutions and independently calculated by root before acknowledgement; author did not read root calculations. Current teaching prompt bodies remain verbatim.')
manifest['sources']=sources
manifest['outputs']=[{'id':'teaching','path':'teaching.md','sha256':h(p/'teaching.md')}]
manifest['required_topics']=[{'id':'local-approximations','title':'Linear and quadratic local approximation: shifts, products, cancellation and clock model','source_portions':assignments,'outputs':['teaching']}]
checks=[('coverage','Compare complete original source portions against actual final teaching.','pass','All physical pages1–7 including four figures, footnote, examples and ending accounted for; no exclusions.','author/source-coverage.md'),('final_review','Author complete final reading and whole-route reconstruction, bounded to author scope.','pass','Actual P001–P145 read with complete help/ending after final content; independent parent acceptance remains separately pending.','author/reconstruction.md'),('technical_author','Author exact mathematical and targeted numerical checks.','pass','Independent product-rule differentiation, exact rational arithmetic, dimensional/sign/domain and high-precision clock checks before solutions.','author/pre-solution-checks.txt'),('markdown_source','Source-level task matching, links, plain labels and frozen prompts.','pass','All source-level checks true; actual destination styling/math/navigation not established.','author/mechanical-checks.json'),('destination','Actual ordinary GitHub rendered styling, math conversion and help/navigation.','unverified','Parent-owned; author did not inspect actual destination. Source-only checks cannot pass this.','author/requirements.md'),('fresh_sasis','Separate fresh reader with complete frozen baseline and current document.','pending','Parent-owned; no SASIS agent dispatched by author.','author/requirements.md'),('parent_technical_review','Independent parent inspection and comparison with pre-solution calculations.','pending','Parent-owned; author has not read or incorporated parent calculations/reports.','author/requirements.md'),('final_acceptance','Parent disposition of full reader, technical and destination evidence.','pending','No global closure or final acceptance claim.','author/requirements.md'),('publication','Accepted iteration evidence/skill publication and verification.','pending','Parent-owned; author made no GitHub, branch, skill or queue mutation.','author/requirements.md')]
manifest['output_checks']=[{'id':cid,'description':desc,'applicable':True,'status':status,'reason':reason,'evidence':[ev(path)],'dependencies':[]} for cid,desc,status,reason,path in checks]
topic['source_reads']=reads
topic['gaps']=[]
requirements=(p/'author/requirements.md').read_text()
for n in range(1,13):
 key=f'T{n}';line=next(x for x in requirements.splitlines() if x.startswith(key+' '))
 topic['requirements'][key]={'applicable':True,'status':'unverified' if n==11 else 'pass','reason':line,'evidence':[ev('author/requirements.md'),ev('author/reconstruction.md')]+([ev('author/pre-solution-checks.txt')] if n==10 else []),'dependencies':[]}
(state/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(state/'topics/local-approximations.json').write_text(json.dumps(topic,indent=2)+'\n')
helper=p/'inputs/scripts/prof_state.py'
for suffix,args in [('topic',['--topic','local-approximations']),('full',[])]:
 r=subprocess.run(['python',str(helper),'dependencies','--state',str(state)]+args,capture_output=True,text=True)
 (p/f'author/dependencies-{suffix}.json').write_text(r.stdout)
 if r.returncode:raise RuntimeError(r.stdout+r.stderr)
 print(suffix,'dependency snapshot',len(r.stdout),'characters',r.stdout[:130])
