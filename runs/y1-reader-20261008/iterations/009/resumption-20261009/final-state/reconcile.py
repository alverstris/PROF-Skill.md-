"""Rebuild D009 final bookkeeping from retained evidence; never performs acceptance review."""
from pathlib import Path
import argparse,copy,hashlib,json,re,subprocess
S=Path(__file__).resolve().parent;B=S.parent;R=B.parents[4];A=B/'author'
V2='7b8be9795369dd3dd69300954ac9a2dcd37177d27ec92d18279768ccb5d4de6d'
V3='5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244'
R15='24b8c2e2d1898384f85eca608f34074d91a78268efcec69d7ceb81052a87659e'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p):return str(p.resolve().relative_to(R))
def write(p,obj):p.write_text(json.dumps(obj,indent=2)+'\n')
def evidence(p,text):
 assert text and text in p.read_text(),f'Missing exact witness in {p}'
 return {'path':rel(p),'sha256':sha(p),'locator':{'kind':'text','value':text}}
def whole(p):
 lines=p.read_text().splitlines();assert lines
 return {'path':rel(p),'sha256':sha(p),'locator':{'kind':'lines','start':1,'end':len(lines)}}
def condition(status,reason,witnesses):return {'applicable':True,'status':status,'reason':reason,'evidence':witnesses,'dependencies':[]}
p=argparse.ArgumentParser();p.add_argument('--root-accepted',action='store_true');p.add_argument('--acceptance-evidence');p.add_argument('--acceptance-text');p.add_argument('--reader-report');args=p.parse_args()
if args.root_accepted:
 assert all([args.acceptance_evidence,args.acceptance_text,args.reader_report]),'Final acceptance requires all three evidence/report arguments.'
else:
 assert not any([args.acceptance_evidence,args.acceptance_text,args.reader_report]),'Acceptance arguments require explicit --root-accepted.'
 existing=json.loads((S/'manifest.json').read_text())
 assert not any(c['id']=='final_review' and c['status']=='pass' for c in existing['output_checks']),'Already accepted: use read-only checks or rerun with explicit acceptance evidence; no silent demotion.'
assert sha(B/'frozen-prof-r15.md')==R15
assert sha(A/'teaching-r15-recovery-v2.md')==V2 and sha(A/'teaching-r15-recovery-v3.md')==V3
v2=(A/'teaching-r15-recovery-v2.md').read_text();v3=(A/'teaching-r15-recovery-v3.md').read_text()
reverse=v3.replace('\\lt ','<').replace('\\gt ','>')
reverse=re.sub(r'^```math\n','$$\n',reverse,flags=re.M)
reverse=re.sub(r'^```$',r'$$',reverse,flags=re.M)
assert reverse==v2,'Content equivalence changed: do not refresh old semantic passes.'
oldm=json.loads((A/'.prof-state/manifest.json').read_text());oldt=json.loads((A/'.prof-state/topics/curve-sketching.json').read_text())
oldrepo=Path(oldm['project_root']).parents[5]
assert oldm['skill']['sha256']==R15
inherited=S/'inherited-author-state.json'
snapshot={'attribution':'Original recovery-author v2 state, preserved without promotion; v3 carryforward is separately justified.','manifest':oldm,'topic':oldt}
if inherited.exists():assert json.loads(inherited.read_text())==snapshot,'Original author state changed; investigate.'
else:write(inherited,snapshot)
def relocate(s):return R/Path(s).relative_to(oldrepo)
request=relocate(oldm['request']['path']);assert sha(request)==oldm['request']['sha256'],'Requests changed: inspect them before accepting inherited applicability.'
m={'schema_version':1,'project_root':str(R),'skill':{'path':str(B/'frozen-prof-r15.md'),'sha256':R15},'request':{'path':str(request),'sha256':sha(request)},'sources':copy.deepcopy(oldm['sources']),'outputs':[],'required_topics':[],'output_checks':[]}
t=copy.deepcopy(oldt)
for src in m['sources']:
 path=relocate(src['path']);assert sha(path)==src['sha256'],f'Changed original source {path}'
 src['path']=str(path)
 for portion in src['portions']:
  for ev in portion['evidence']:
   if ev['path']!='@request':ev['path']=rel(A/ev['path'])
for read in t['source_reads']:
 read['note']='Original recovery-author reading attribution retained from author/.prof-state and author-audit.md; not a new reread by this reconciliation. '+read['note']
for out in oldm['outputs']:
 path=A/out['path']
 if out['id']=='teaching':path=A/'teaching-r15-recovery-v3.md'
 else:assert sha(path)==out['sha256'],'Figure changed: visual carryforward invalid.'
 m['outputs'].append({'id':out['id'],'path':rel(path),'sha256':sha(path)})
new_inputs=[('author-audit',A/'author-audit.md','Original complete author audit and reconstruction for semantically equivalent v2; previously read by this recovery author.'),('coverage-record',A/'source-coverage.md','Original complete source-to-teaching map for unchanged substantive content; previously read.'),('equivalence',B/'v2-v3-semantic-equivalence.json','Complete equivalence report read; exact inverse transform independently rechecked in this script.'),('root-review',B/'root-technical-and-source-review.md','Complete independent root review read; its source/image observations remain attributed to root.'),('destination-review',B/'destination-v3/review.md','Complete destination review read; image/page/CSS observations attributed to its reviewer; no live client claim.'),('destination-audit',B/'destination-v3/final-audit.json','Complete final audit summary read; individual result scope preserved.'),('reader-admission',B/'sasis-admission-v3.json','Complete original provisional dispatch/admission record read by recovery author; root final acceptance separately admits actual full reader access.'),('reconciliation',S/'reconciliation.md','Complete current carryforward and scope record written/read by recovery author.')]
if args.root_accepted:
 acc=(R/args.acceptance_evidence).resolve();reader=(R/args.reader_report).resolve();rel(acc);rel(reader)
 assert V3 in acc.read_text(),'Acceptance must identify exact current teaching hash.'
 assert V3 in reader.read_text(),'Reader report must identify exact current teaching hash.'
 acc_ev=evidence(acc,args.acceptance_text)
 new_inputs += [('root-acceptance',acc,'Root explicitly asserts this full acceptance evidence has been reviewed; exact witness attached.'),('reader-v3',reader,'Root explicitly asserts fresh v3 reader report has been fully read, admitted and adjudicated; not an author-generated reader verdict.')]
for id,path,note in new_inputs:
 assert path.is_file()
 m['sources'].append({'id':id,'path':str(path),'sha256':sha(path),'portions':[{'id':'all','locator':'Complete evidence record','disposition':'required','reason':'Revision-bound acceptance dependency','evidence':[]}]})
 t['source_reads'].append({'source_id':id,'portion_id':'all','status':'read','reviewed_sha256':sha(path),'note':note})
m['required_topics']=[{'id':'curve-sketching','title':'D009 complete qualitative sketches, r15 generation with v3 markup repair','source_portions':[{'source_id':z['id'],'portion_id':q['id']} for z in m['sources'] for q in z['portions']],'outputs':[o['id'] for o in m['outputs']]}]
carry=evidence(S/'reconciliation.md','Thus T1–T10 source, mathematical and teaching-route evidence carries forward for identical content, with explicit v3 output bindings; this is not claimed as regeneration or a fresh full author read.')
for i in range(1,11):
 old=oldt['requirements'][f'T{i}'];assert old['status']=='pass'
 evs=copy.deepcopy(old['evidence'])
 for ev in evs:
  if ev['path']!='@request':ev['path']=rel(A/ev['path'])
 t['requirements'][f'T{i}']=condition('pass','Original recovery-author evidence retained for identical v3 semantic content, with current equivalence and output bindings. '+old['reason'],evs+[carry])
t11reason='Current v3 server-parsed math/prose, immutable figures, link mapping, observed CSS/markup and complete local preview pass in reported scope. Live pixels, computed styles, client MathJax, responsive behavior and browser clicks remain unobserved.'
t['requirements']['T11']=condition('pass',t11reason,[whole(B/'destination-v3/review.md'),whole(B/'destination-v3/final-audit.json'),whole(S/'reconciliation.md')])
t12reason='Root final acceptance awaits full fresh v3 SASIS admission/adjudication and whole-evidence reconciliation.'
t['requirements']['T12']=condition('pass' if args.root_accepted else 'pending',('Root final acceptance explicitly recorded for exact v3 teaching and complete evidence; limits remain as documented.' if args.root_accepted else t12reason),[acc_ev] if args.root_accepted else [])
t['gaps']=[]
for id,description,reason,evs in [('coverage','Complete source correspondence','Original full source mapping remains applicable by exact semantic equivalence.',[whole(A/'source-coverage.md'),carry]),('technical','Full mathematical and source audit','Original independent-method author and root checks cover identical mathematical content; not a new blind calculation claim.',[whole(B/'root-technical-and-source-review.md'),carry]),('destination','Actual v3 destination and preview',t11reason,[whole(B/'destination-v3/review.md'),whole(B/'destination-v3/final-audit.json')])]:
 m['output_checks'].append({'id':id,'description':description,**condition('pass',reason,evs)})
m['output_checks'].append({'id':'final_review','description':'Root final whole-document acceptance',**condition('pass' if args.root_accepted else 'pending',t['requirements']['T12']['reason'],[acc_ev] if args.root_accepted else [])})
write(S/'manifest.json',m);write(S/'topics/curve-sketching.json',t)
(S/'RUN.md').write_text('D009 separate parent final state. Generation binds exact frozen r15; current learner output is v3. Original author/.prof-state unchanged. See reconciliation.md and README.md. '+('Root acceptance recorded; run helper checks and preserve actual scope.' if args.root_accepted else 'T12/final_review pending: root must read/admit/adjudicate fresh v3 SASIS and record final acceptance.')+' No global queue/skill/publication action is performed here.\n')
cmd=['python',str(R/'scripts/prof_state.py')]
subprocess.run(cmd+['begin-topic','--state',str(S),'--topic','curve-sketching'],check=True)
t=json.loads((S/'topics/curve-sketching.json').read_text())
for extra,target in [(['--topic','curve-sketching'],t['requirements'].values()),([],m['output_checks'])]:
 deps=json.loads(subprocess.check_output(cmd+['dependencies','--state',str(S)]+extra,text=True))
 for c in target:
  if c['status']=='pass':c['dependencies']=deps
write(S/'manifest.json',m);write(S/'topics/curve-sketching.json',t)
for extra,name in [(['--topic','curve-sketching'],'topic-check.txt'),([],'full-check.txt')]:
 result=subprocess.run(cmd+['check','--state',str(S)]+extra,text=True,capture_output=True)
 (S/name).write_text(result.stdout+result.stderr+'\nExit code: '+str(result.returncode)+'\n')
 print(name,result.returncode,result.stdout)
