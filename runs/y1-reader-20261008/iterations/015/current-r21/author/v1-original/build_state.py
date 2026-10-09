from pathlib import Path
import hashlib,json,subprocess
A=Path(__file__).resolve().parent; R=A.parents[5]; S=A/'.prof-state'; TOOL=R/'scripts/prof_state.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
def ev(file,text):return {'path':file,'sha256':sha(A/file),'locator':{'kind':'text','value':text}}
def source(id,p,portions,note):
 return {'id':id,'path':str(p),'sha256':sha(p),'portions':[{'id':q,'locator':l,'disposition':'required','reason':note,'evidence':[]} for q,l in portions]}
m=json.loads((S/'manifest.json').read_text());m['skill']={'path':str(A/'controls/SKILL.md'),'sha256':sha(A/'controls/SKILL.md')}
access=json.loads((A/'input-access.json').read_text()); sources=[]; notes={}
def add(id,p,portions,note):sources.append(source(id,p,portions,note));notes[id]=note
add('lecture',A.parent/'source/lec16.pdf',[(f'p{i}',f'PDF page{i}, printed'+(' cover' if i==1 else str(i-1))+', entire original including figures') for i in range(1,6)],'All five source pages read as text and original images; input-access.json details source-by-source contribution.')
for i in range(1,6):
 for ext in ['txt','png']:
  add(f'page{i}-{ext}',A.parent/f'source/page-{i:02}.{ext}',[('whole','Entire extracted page text' if ext=='txt' else 'Entire original rendered page image')],access['source_pages'][i-1]['note'])
add('baseline',R/'references/sasis/ocr-baseline-20261007/student-baseline.txt',[(f'packet{i+1}',f"1-based LF line range {p['start']}–{p['end']}, internal CR preserved") for i,p in enumerate(access['baseline']['packets'])],'Complete frozen operational baseline read in ten packets; no prior lesson or reader substitutes.')
for id,path in [('execution','references/execution-protocol.md'),('sasis','references/sasis.md'),('profile','references/sasis/profile-manifest.json'),('reader-role','references/sasis/student-role.txt'),('reader-contract','references/sasis/student-testing-contract.txt'),('rewrite','references/sasis/rewrite-guide.md'),('domain','references/domain-patterns.md'),('state-guide','references/state-tool.md'),('user-requests','runs/y1-reader-20261008/requests.md')]:
 add(id,A/'controls'/path,[('whole','Complete frozen control file')],'Read actual control; skill mode, author/reader separation, source accounting, mathematics representation checks, state and exact user constraints applied.')
add('qm',A.parent/'primary-qm/MIT22_51F12_Ch9.pdf',[('operator','PDF pages2–3, printed80–81, sections9.1.2–9.1.3, including operators and position representation')],'Actual extracted text and original page images read; only narrow scaled-operator/zero-output context adopted, see research-record.md.')
for i in [2,3]:
 for ext in ['txt','png']:add(f'qm{i}-{ext}',A.parent/f'primary-qm/page-{i:02}.{ext}',[('whole','Full original page image' if ext=='png' else 'Full extracted text')],'Read complete page, focusing operator scaling and lowest-state Gaussian equation; additional content not imported into learner prerequisites.')
add('topic-record',A/'topic-record.md',[('whole','Complete source coverage/prerequisite/convention/gap record')],'Current explicit starting-knowledge and course convention decisions, complete source map C01–C10.')
add('research-record',A/'research-record.md',[('whole','Complete targeted source and syntax research record')],'Primary operator aside, official supported GitHub syntax, explicit deduction boundaries.')
add('prompt-freeze',A/'prompts-only-v1.md',[('whole','Complete frozen five-task prompt-only revision before authored solutions')],'Preserved unchanged for independent root prompt-first check; current learner prompts retain those mathematical demands.')
m['sources']=sources
f=json.loads((A/'freeze-manifest-v1.json').read_text());m['outputs']=[{'id':'file'+str(i+1),'path':x['path'],'sha256':x['sha256']} for i,x in enumerate(f['constituents'])]
m['required_topics']=[{'id':'d015','title':'Lecture16 Differential equations and separation of variables','source_portions':[{'source_id':src['id'],'portion_id':p['id']} for src in sources for p in src['portions']],'outputs':[x['id'] for x in m['outputs']]}]
def cond(status,reason,evidence=[]):return {'applicable':True,'status':status,'reason':reason,'evidence':evidence,'dependencies':[]}
m['output_checks']=[{'id':'coverage','description':'Entire assigned lecture including all figures, aside and ending',**cond('pass','C01–C09 map every source portion; generated Q1–Q5 add handover without narrowing source scope.',[ev('topic-record.md','No source page is excluded.')])}, {'id':'author_reconstruction','description':'Substantive complete route and help author audit',**cond('pass','A01–A20 reconstruct all substantive steps and help from supplied premises.',[ev('author-audit.md','A20. Q5 and retention: a suggested adjustable gap distinguishes later retrieval from application.')])}, {'id':'technical_execution','description':'Symbolic and manual scientific checks',**cond('pass','Eighteen correct residual checks and two rejected counterexample checks, with manual domains/geometry documented.',[ev('author-audit.md','Two deliberately incorrect candidate residuals are nonzero(-2 equation,-4 initial), demonstrating the checks distinguish an incorrect answer.')])}, {'id':'source_structure','description':'Source-level task/help/anchor and typography checks',**cond('pass','Every local link resolves and task/hint/solution IDs match; all expressions inventoried. Does not substitute for GitHub destination.',[ev('structural-checks.json','Source-level links/typography/counts only; actual GitHub parsing, styling and clicked navigation remain pending.')])}]
for id,desc in [('destination_math','Actual GitHub parsed operand/operator/group preservation'),('destination_visual','Actual GitHub complete visual and computed styling inspection'),('native_navigation','Actual clicked task/hint/solution return destinations'),('external_review','Independent authored-answer/source technical review'),('sasis','Fresh complete-document SASIS and root disposition'),('final_review','Final acceptance of current artifacts after all necessary checks')]:m['output_checks'].append({'id':id,'description':desc,**cond('pending','Root-owned stage pending; no destination/external/SASIS/final result claimed by author.')})
write(S/'manifest.json',m)
subprocess.run(['python',str(TOOL),'begin-topic','--state',str(S),'--topic','d015'],check=True,capture_output=True,text=True)
t=json.loads((S/'topics/d015.json').read_text());t['source_reads']=[{'source_id':src['id'],'portion_id':p['id'],'status':'read','reviewed_sha256':src['sha256'],'note':notes[src['id']] if src['id']!='baseline' else access['baseline']['packets'][int(p['id'][6:])-1]['note']} for src in sources for p in src['portions']]
audit=(A/'author-audit.md').read_text()
for i in range(1,13):
 line=next(l for l in audit.splitlines() if l.startswith('T'+str(i)+' '))
 t['requirements']['T'+str(i)]=cond('pass' if i<=10 else 'pending',line,[ev('author-audit.md',line)])
t['gaps']=[]
tr=(A/'topic-record.md').read_text()
for i in range(1,9):
 line=next(l for l in tr.splitlines() if l.startswith('G'+str(i).zfill(2)+':'))
 t['gaps'].append({'id':'g'+str(i).zfill(2),'question':line.split('. ')[0],'consequential':True,'status':'resolved' if i<8 else 'open','reason':line,'next_action':'None for author mathematical route; retain source correction and explanation.' if i<8 else 'Root perform actual destination parser/visual/native navigation checks against frozen manifest.','evidence':[ev('topic-record.md',line)],'dependencies':[]})
write(S/'topics/d015.json',t)
(S/'RUN.md').write_text('D015 r21 author recovery\n\nFrozen teaching v1: ../freeze-manifest-v1.json. Exact assignment ../assignment.txt; user instructions in frozen controls. Complete baseline/source access ../input-access.json. Source/prereq/convention map ../topic-record.md; targeted research ../research-record.md; substantive route audit ../author-audit.md. Skill snapshot controls/SKILL.md SHA3e5d1f2c9f43c8a5ebe9df73d18711a649e5716f88cd6011239d3ca449327bf9.\n\nAll author content and technical checks complete. T11/T12 and root-owned destination, native navigation, external review, SASIS and final acceptance pending. No revision to frozen teaching without preserving v1 and fresh reader dispatch.\n\nNext action: provide root this state/evidence packet and await root-owned checks; do not claim whole-project acceptance.\n')
print('STATE DECLARED',len(sources),'sources',len(m['outputs']),'outputs')
