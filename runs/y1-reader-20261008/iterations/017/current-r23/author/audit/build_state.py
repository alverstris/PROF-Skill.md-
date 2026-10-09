from pathlib import Path
import json,hashlib,subprocess
root=Path(__file__).resolve().parents[1]; run=root.parent;state=root/'.prof-state'; manifest=json.loads((state/'manifest.json').read_text());topic=json.loads((state/'topics/ftc1.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ev(path,start=None,end=None,text=None):
 p=root/path;return {'path':path,'sha256':sha(p),'locator':({'kind':'text','value':text} if text is not None else {'kind':'lines','start':start,'end':end})}
sources=[];reads=[];assigned=[]
def source(sid,p,portions,note,url=None):
 r={'id':sid,'path':str(p.resolve()),'sha256':sha(p),'portions':[]}
 if url:r['url']=url
 for pid,loc in portions:
  r['portions'].append({'id':pid,'locator':loc,'disposition':'required','reason':'Required author input/dependency; not an additional SASIS subject-content input.','evidence':[]})
  assigned.append({'source_id':sid,'portion_id':pid});reads.append({'source_id':sid,'portion_id':pid,'status':'read','reviewed_sha256':sha(p),'note':note+' Actual portion: '+loc})
 sources.append(r)
refs=[('execution','references/execution-protocol.md','Bounded source reading, reconstruction, conventions and dependency workflow applied.'),('state-tool','references/state-tool.md','Strict state schema, dependency binding and honest readiness limits applied.'),('domain','references/domain-patterns.md','Physics/mathematics route: representation meaning, governing conditions, explicit deductions and discriminating signs applied.'),('sasis','references/sasis.md','Fresh original author and separate fresh full-reader condition, complete baseline and immutable evidence required; external closure left pending.'),('profile','references/sasis/profile-manifest.json','Baseline scope and exact frozen revision verified.'),('reader-contract','references/sasis/student-testing-contract.txt','Two-input reader boundary and author role separation read, not passed as learner subject content.'),('reader-role','references/sasis/student-role.txt','Short instruction read to understand separate external reader role; author does not self-certify SASIS.'),('rewrite-guide','references/sasis/rewrite-guide.md','Preserve original, collect entire audit and repair causes; no original learner repair made.'),('governing-requests','runs/y1-reader-20261008/requests.md','Exact user scope/repository/Linux constraints read and copied to current request.')]
for sid,rel,note in refs:source(sid,run/'controls'/rel,[('whole','whole file')],note)
baseline=run/'controls/references/sasis/ocr-baseline-20261007/student-baseline.txt'; ranges=json.loads((root/'audit/baseline-ranges.json').read_text())['ranges']
source('baseline',baseline,[(f'chunk-{i}',f'UTF-8 byte range [{s},{e}) of247840; complete contiguous operational baseline') for i,(s,e) in enumerate(ranges,1)],'Actually printed and read all nine ranges; baseline-access.jsonl records chunk identity. Maths supplies calculus, signs and units; all other sections read without silently granting unlisted facts.')
source('original-pdf',run/'source/lec19.pdf',[(f'page-{i}',f'PDF physical page{i}: '+('OCW cover' if i==1 else f'printed lecture page{i-1}, all text/equations/figures')) for i in range(1,6)],'All extracted text read then rendered page viewed; source-review.md and author-audit.md map every example/figure and correction.',url='https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/817a2c46ddc23e2efda247a79ddeed34_lec19.pdf')
for i in range(1,6):
 for ext in ['txt','png']:source(f'page-{i}-{ext}',run/f'source/page-{i:02d}.{ext}',[('whole',f'whole source physical page{i} {ext}')],('Extracted text read; layout/notation checked against image.' if ext=='txt' else 'Entire image actually viewed; consequential equations and diagrams inspected, not merely extracted.'))
source('conventions-research',root/'audit/source-review.md',[('whole','whole frozen author source/prerequisite/convention and independent research record')],'FTC1 is MIT endpoint-evaluation convention; v is signed velocity, |v| speed; no new convention selected by guess. Independent MIT metadata and OpenStax passages read at recorded URLs.')
manifest['sources']=sources
outs=[]
for oid,rel in [('core','learner/lesson.md'),('hints','learner/hints.md'),('solutions','learner/solutions.md'),('sine','learner/figures/sine.png'),('additivity','learner/figures/additivity.png')]:outs.append({'id':oid,'path':rel,'sha256':sha(root/rel)})
manifest['outputs']=outs
manifest['required_topics']=[{'id':'ftc1','title':'D017 full Lecture19: FTC1 evaluation, signed net change, orientation/additivity, comparison and substitution','source_portions':assigned,'outputs':[o['id'] for o in outs]}]
topic['source_reads']=reads
# Put declared inventory into state before requesting exact dependency snapshots.
(state/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(state/'topics/ftc1.json').write_text(json.dumps(topic,indent=2)+'\n')
helper=run/'controls/scripts/prof_state.py'
for args,name in [(['--topic','ftc1'],'topic-dependencies.json'),([], 'global-dependencies.json')]:
 cmd=['python',str(helper),'dependencies','--state',str(state),*args];r=subprocess.run(cmd,text=True,capture_output=True);(root/'audit'/name).write_text(r.stdout);print(name,r.returncode,r.stdout[:600]);assert r.returncode==0,r.stderr
