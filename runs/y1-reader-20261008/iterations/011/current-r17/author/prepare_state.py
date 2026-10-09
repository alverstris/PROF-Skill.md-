from pathlib import Path
import hashlib,json,subprocess
repo=Path.cwd();a=repo/'runs/y1-reader-20261008/iterations/011/current-r17/author';state=a/'.prof-state'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,o):p.write_text(json.dumps(o,indent=2)+'\n')
m=json.loads((state/'manifest.json').read_text());t=json.loads((state/'topics/related-rates.json').read_text())
readnotes={}
def source(sid,path,portions,note):
 p=repo/path
 m['sources'].append({'id':sid,'path':str(p),'sha256':sha(p),'portions':[{'id':i,'locator':l,'disposition':'required','reason':'Assigned or actually used prerequisite/control input.','evidence':[]} for i,l in portions]})
 for i,l in portions:t['source_reads'].append({'source_id':sid,'portion_id':i,'status':'read','reviewed_sha256':sha(p),'note':note+' '+l})
source('lecture','runs/y1-reader-20261008/iterations/011/current-r17/source/lec12.pdf',[(f'page-{i}',f'Physical PDF page{i}, complete, with figures') for i in range(1,6)],'Personally inspected all complete original pages; source-access.md records page-specific content.')
for i in range(1,6):
 for ext in ('txt','png'):source(f'page{i}-{ext}',f'runs/y1-reader-20261008/iterations/011/current-r17/source/page-{i:02d}.{ext}',[('all','Whole text/page image')],f'Physical original page{i}; extraction checked against rendered original. See source-access.md and author-audit.md.')
source('baseline','references/sasis/ocr-baseline-20261007/student-baseline.txt',[(f'packet{i+1}',f'Physical LF lines{lo}–{hi}') for i,(lo,hi) in enumerate([(1,100),(101,210),(211,330),(331,445),(446,560),(561,700),(701,830),(831,960),(961,1100),(1101,1230),(1231,1377)])],'Complete frozen four-subject baseline read in bounded untruncated packets, logged baseline-access.jsonl. Relevant mathematics LF28–34,138–174; units/sign LF297–312,473,533–543.')
for sid,path in [('execution','references/execution-protocol.md'),('state-tool','references/state-tool.md'),('sasis','references/sasis.md'),('profile','references/sasis/profile-manifest.json'),('reader-role','references/sasis/student-role.txt'),('reader-contract','references/sasis/student-testing-contract.txt'),('rewrite','references/sasis/rewrite-guide.md')]:source(sid,path,[('all','Whole control file')],'Actually read current file; governs author execution, input separation, truthful pending gates and evidence scope.')
source('domain','references/domain-patterns.md',[('math','Physics and mathematics domain section')],'Relevant domain read; descriptive-to-symbolic mapping, course notation and discriminating units/sign checks applied.')
files=[a/'teaching-v1.md',*sorted((a/'figures').glob('*.png'))]
m['outputs']=[{'id':('teaching' if p.suffix=='.md' else p.stem),'path':str(p.relative_to(a)),'sha256':sha(p)} for p in files]
m['required_topics']=[{'id':'related-rates','title':'Construct and interpret geometry-based related rates and local measurement sensitivity','source_portions':[{'source_id':s['id'],'portion_id':p['id']} for s in m['sources'] for p in s['portions']],'outputs':[x['id'] for x in m['outputs']]}]
checks=[('coverage','Complete source-to-teaching coverage and full author reconstruction','pass'),('technical','Independent mathematics, units, signs and limits','pass'),('source_structure','Source labels, task matching, links and figure availability','pass'),('destination_math','Actual destination preserves mathematical operands/operators/grouping','pending'),('destination_typography','Actual destination plain prose styling','pending'),('destination_visual','Actual complete destination visual review/assets/navigation','pending'),('sasis','Fresh full two-input reader admission and report disposition','pending'),('final_review','Final integrated independent acceptance','pending')]
m['output_checks']=[{'id':i,'description':d,'applicable':True,'status':s,'reason':d+'; performed author evidence only where pass, pending gates not claimed.','evidence':[],'dependencies':[]} for i,d,s in checks]
save(state/'manifest.json',m);save(state/'topics/related-rates.json',t)
