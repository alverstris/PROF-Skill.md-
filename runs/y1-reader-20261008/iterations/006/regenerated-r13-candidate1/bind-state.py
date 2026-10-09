from pathlib import Path
import json,hashlib,subprocess
root=Path.cwd();state=root/'.prof-state';manifest=json.loads((state/'manifest.json').read_text());topic=json.loads((state/'topics/exponential-log.json').read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def witness(path,text):return {'path':path,'sha256':sha(root/path),'locator':{'kind':'text','value':text}}
source=[];reads=[];assign=[]
def add(sid,path,parts,note,url=None):
 p=Path(path).resolve();h=sha(p);decl={'id':sid,'path':str(p),'sha256':h,'portions':[]}
 if url:decl['url']=url
 for pid,locator in parts:
  decl['portions'].append({'id':pid,'locator':locator,'disposition':'required','reason':'Assigned original content or applied control/prerequisite dependency.','evidence':[]})
  reads.append({'source_id':sid,'portion_id':pid,'status':'read','reviewed_sha256':h,'note':note+' Locator: '+locator})
  assign.append({'source_id':sid,'portion_id':pid})
 source.append(decl)
orig=Path('/workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L06')
add('lecture-pdf',orig/'lec6.pdf',[(f'p{i:02}',f'PDF page {i}: '+('cover' if i==1 else f'printed page {i-1}')) for i in range(1,9)],'Read every page text and full image; C01-C09 in author-evidence.md identify claims, figures, source typos and final remarks.', 'https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/f9af0e98490296c99d330faf47389507_lec6.pdf')
for i in range(1,9):
 add(f'original-image-{i}',orig/f'lec6-p{i:02}.png',[('complete',f'Complete uncropped original page image {i}')],'Inspected full original image, equations, signs, labels and footer; matched to source text. Image groups p01-p04 then p05-p08.')
 add(f'original-text-{i}',orig/f'lec6-p{i:02}.txt',[('complete',f'Complete extracted original page text {i}')],'Read complete text; extraction artefacts resolved against the actual original full image. No source-preparation report read.')
ctrls=[('execution','controls/references/execution-protocol.md'),('domain','controls/references/domain-patterns.md'),('state-tool','controls/references/state-tool.md'),('run-requests','controls/runs/y1-reader-20261008/requests.md'),('sasis-protocol','controls/references/sasis.md'),('reader-contract','controls/references/sasis/student-testing-contract.txt'),('reader-role','controls/references/sasis/student-role.txt'),('profile','controls/references/sasis/profile-manifest.json'),('rewrite','controls/references/sasis/rewrite-guide.md'),('pdf-skill','controls/pdf-SKILL.md')]
for sid,path in ctrls:add(sid,root/path,[('complete','Whole applied control file')],'Actual full control read; pinned GitHub git show snapshots except authorised local PDF skill. Author role only; reader and publication gates delegated to parent.')
add('baseline',root/'controls/references/sasis/ocr-baseline-20261007/student-baseline.txt',[('complete','Complete cover plus all four operational subjects, LF lines1-1377')],'Read full247840 bytes/246945 raw UTF8 characters in bounded coherent chunks. Actual successful ranges and recovered clipping in access-record.json. Relevant premises recorded in prerequisites-conventions.md.')
add('conventions',root/'prerequisites-conventions.md',[('complete','Whole prerequisite, foundational-status, notation and convention record')],'Current record written and inspected from actual baseline/source. Course a>1 preserved at start; extension to0<a<1 explicitly labelled; source typos independently corrected.')
manifest['required_topics']=[{'id':'exponential-log','title':'Lecture6 exponential and logarithmic differentiation, sequence limits and relative change','source_portions':assign,'outputs':['teaching']}]
manifest['sources']=source;manifest['outputs']=[{'id':'teaching','path':'teaching.md','sha256':sha(root/'teaching.md')}]
def pending(cid,desc,reason):return {'id':cid,'description':desc,'applicable':True,'status':'pending','reason':reason,'evidence':[],'dependencies':[]}
manifest['output_checks']=[pending('coverage','Compare every required original portion to actual teaching.','Author coverage reconciliation completed; bindings pending.'),pending('final_review','Final integrated review at immutable revision.','Full sequential author read completed, including final help/ending; final acceptance awaits parent independent review, actual destination check and fresh SASIS.'),pending('destination','Inspect ordinary GitHub Markdown file view.','Parent owns actual destination typography, math and navigation review. Byte checks alone cannot establish this.'),pending('independent_review','Independent mathematical and scientific review.','Parent owns independent review; author derivations/numerical checks are supplied separately.'),pending('sasis','Fresh independent whole-document reader.','Parent owns fresh SASIS against the final frozen teaching and complete baseline.'),pending('publication','Immutable freeze and publication.','Parent owns immutable GitHub freeze and publication; no author Git mutations.')]
topic['source_reads']=reads;topic['gaps']=[]
author=(root/'author-evidence.md').read_text()
for i in range(1,13):
 para=next(line for line in author.splitlines() if line.startswith(f'- T{i} '))
 topic['requirements'][f'T{i}']={'applicable':True,'status':'pass' if i<=10 else 'pending','reason':para[2:],'evidence':[witness('author-evidence.md',para)],'dependencies':[]}
(state/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(state/'topics/exponential-log.json').write_text(json.dumps(topic,indent=2)+'\n')
for scope,extra in [('topic',['--topic','exponential-log']),('full',[])]:
 r=subprocess.run(['python','controls/scripts/prof_state.py','dependencies','--state','.prof-state',*extra],text=True,capture_output=True)
 (root/f'dependencies-{scope}.json').write_text(r.stdout);(root/f'dependencies-{scope}.stderr.txt').write_text(r.stderr)
 print(scope,'dependency_snapshot_exit',r.returncode,'output_start',r.stdout[:150])
