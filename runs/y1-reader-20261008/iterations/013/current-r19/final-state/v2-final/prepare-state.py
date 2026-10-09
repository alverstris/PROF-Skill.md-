from pathlib import Path
import json,hashlib,copy,subprocess,sys
root=Path(__file__).resolve().parents[2]
f=Path(__file__).resolve().parent
state=f/'.prof-state'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def ev(rel):
 p=root/rel
 return {'path':rel,'sha256':sha(p),'locator':{'kind':'lines','start':1,'end':len(p.read_text().splitlines())}}
m=json.loads((state/'manifest.json').read_text()); t=json.loads((state/'topics/mvt.json').read_text())
old=json.loads((root/'author/.prof-state/manifest.json').read_text()); ot=json.loads((root/'author/.prof-state/topics/mvt.json').read_text())
m['sources']=copy.deepcopy(old['sources'])
controls={'execution':'execution-protocol.md','sasis':'sasis.md','reader-role':'student-role.txt','reader-contract':'student-testing-contract.txt','profile':'profile-manifest.json','rewrite':'rewrite-guide.md','state-guide':'state-tool.md','domain-guide':'domain-patterns.md'}
for src in m['sources']:
 if src['id'] in controls:
  new=f/'frozen-inputs'/controls[src['id']]
  assert sha(new)==src['sha256']
  src['path']=str(new)
for ident,rel,why in [
 ('coverage-map','author/source-coverage.md','Every original portion S00–S08 mapped to actual route; unchanged line numbers in v2.'),
 ('reconstruction','author/reconstruction.md','Full original sequential reconstruction with v2 bridge below.'),
 ('requirements-v1','author/requirements.md','Original substantive witnesses, retained with version and pending-state limitations.'),
 ('author-technical','author/technical-check-results.json','43 actual original author checks; unchanged calculation and task content validated by inverse.'),
 ('v2-repair','author/v2-repair-note.md','Complete v2 repair, full readback and downstream reconstruction with explicit limits.'),
 ('v2-local','author/v2-local-check-results.json','Exact change count, complete inverse and preservation checks.'),
 ('v2-packet','author/packet-manifest-v2.json','Frozen seven constituent identities.'),
 ('root-source','root-source-review.md','Complete original source review; series wording correction in root-baseline source supersedes overbroad sentence.'),
 ('root-baseline','root-baseline-supplement.md','Precisely scoped positive baseline witnesses and correction to root-source review.'),
 ('root-technical','root-technical-review-v1.md','Complete independent root source, teaching, technical and all-figure audit.'),
 ('root-presolutions','root-independent-presolutions-v1.md','All six independent prompt-first solutions, saved before any author answer; author first read only after both teaching versions frozen.'),
 ('root-symbolic','root-source-symbolic-checks.json','Independent exact mathematical checks.'),
 ('root-v2-readback','root-v2-full-readback.md','Complete current v2 sequential readback and altered-use checks.'),
 ('root-v2-inverse','root-v2-local-inverse.json','Independent complete v2-to-v1 inverse and preservation audit.'),
 ('preparation','final-state/v2-final/preparation.md','Current author condition, substantive applicability bridge and exact pending-gate scope.')]:
 p=root/rel
 m['sources'].append({'id':ident,'path':str(p),'sha256':sha(p),'portions':[{'id':'full','locator':'whole file','disposition':'required','reason':why,'evidence':[]}]})
packet=json.loads((root/'author/packet-manifest-v2.json').read_text())
m['outputs']=[{'id':'learner' if i==0 else f'figure-{i}','path':'author/'+a['path'],'sha256':a['sha256']} for i,a in enumerate(packet['constituents'])]
for a in m['outputs']: assert sha(root/a['path'])==a['sha256']
m['required_topics']=[{'id':'mvt','title':'Mean value theorem, inequalities and derivative bounds: complete D013 v2','source_portions':[{'source_id':s['id'],'portion_id':p['id']} for s in m['sources'] for p in s['portions']],'outputs':[o['id']for o in m['outputs']]}]
t['source_reads']=[]
oldreads={r['source_id']:r for r in ot['source_reads']}
for src in m['sources']:
 for part in src['portions']:
  note=oldreads[src['id']]['note'] if src['id'] in oldreads else part['reason']
  t['source_reads'].append({'source_id':src['id'],'portion_id':part['id'],'status':'read','reviewed_sha256':src['sha256'],'note':note+' Current v2 preparation retains the actual read scope; frozen copies are byte-identical, not a claimed new whole-baseline reading.'})
t['gaps']=[]
for i in range(1,13):
 key=f'T{i}'
 if i<=10:
  t['requirements'][key]={'applicable':True,'status':'pass','reason':ot['requirements'][key]['reason']+' Rechecked for v2 using the entire actual author and root readbacks, precise altered-use reconstruction, and exact inverse preservation proof. The original witness remains historically scoped; external pending gates are not promoted here.','evidence':[ev('author/requirements.md'),ev('author/v2-repair-note.md'),ev('root-v2-full-readback.md'),ev('final-state/v2-final/preparation.md')],'dependencies':[]}
 else:
  t['requirements'][key]={'applicable':True,'status':'pending','reason':'Await actual fresh v2 SASIS, complete destination/full-preview findings and independent final acceptance. Live GitHub clicks and computed styles are unobserved and will not be passed from static or PDF evidence.','evidence':[],'dependencies':[]}
checks=[('coverage','Every source portion and all requested teaching covered in current v2.',True,['author/source-coverage.md','author/v2-repair-note.md','root-v2-full-readback.md']),('independent_technical','Exact prompt-first calculations and complete source/teaching/figure mathematical review.',True,['root-independent-presolutions-v1.md','root-technical-review-v1.md','root-baseline-supplement.md','root-v2-full-readback.md']),('sasis','Fresh two-input reader admission, complete sequential packet reading and finding dispositions.',False,[]),('destination_math','Every expression in actual immutable destination preserves operands, operators, grouping and meaning.',False,[]),('destination_visual','Actual server-parsed prose/asset structure and complete native faithful preview inspected; no live browser pixels or computed-style claim.',False,[]),('navigation_targets','Actual server-parsed anchors and task/hint/solution/return relationships plus native internal PDF destinations match intended targets. Live GitHub clicks remain unobserved.',False,[]),('final_review','Independent final complete route/help/limit review and all current evidence dispositions.',False,[])]
m['output_checks']=[]
for ident,description,passed,w in checks:
 m['output_checks'].append({'id':ident,'description':description,'applicable':True,'status':'pass' if passed else 'pending','reason':('Actual complete records reviewed and rechecked against current frozen v2; see witnesses and preparation limits.' if passed else 'Await actual final v2 reports and root acceptance; no forecast result recorded.'),'evidence':[ev(x)for x in w],'dependencies':[]})
save(state/'manifest.json',m);save(state/'topics/mvt.json',t)
helper=Path('/workspace/scratch/6a5c7131498d/prof-r19/scripts/prof_state.py')
for label,args in [('topic',['--topic','mvt']),('global',[])]:
 r=subprocess.run([sys.executable,str(helper),'dependencies','--state',str(state),*args],capture_output=True,text=True)
 (f/f'prepared-{label}-dependencies.json').write_text(r.stdout)
 if r.returncode: raise RuntimeError(r.stderr+r.stdout)
 deps=json.loads(r.stdout)
 if isinstance(deps,dict): print('dependency keys',list(deps)); deps=deps.get('dependencies',deps)
 if label=='topic':
  for v in t['requirements'].values():
   if v['status']=='pass':v['dependencies']=deps
 else:
  for v in m['output_checks']:
   if v['status']=='pass':v['dependencies']=deps
save(state/'manifest.json',m);save(state/'topics/mvt.json',t)
print('Prepared',len(m['sources']),'source dependencies and',len(m['outputs']),'outputs.')
