from pathlib import Path
import hashlib,json,subprocess,sys,copy
p=Path(__file__).resolve().parent;case=p.parent;author=case/'author';root=p
while not(root/'scripts/prof_state.py').exists():root=root.parent
st=p/'.prof-state';helper=root/'scripts/prof_state.py'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def rel(f):return str(f.relative_to(root))
def ev(f,txt):return {'path':rel(f),'sha256':sha(f),'locator':{'kind':'text','value':txt}}
def para(f,prefix):return next(l for l in f.read_text().splitlines() if l.startswith(prefix))
m=json.loads((st/'manifest.json').read_text());t=json.loads((st/'topics/max-min.json').read_text())
om=json.loads((author/'.prof-state-v2/manifest.json').read_text());ot=json.loads((author/'.prof-state-v2/topics/max-min.json').read_text())
assert sha(Path(om['skill']['path']))==m['skill']['sha256']==om['skill']['sha256']
assert sha(Path(om['request']['path']))==m['request']['sha256']==om['request']['sha256']
for s in om['sources']:assert sha(Path(s['path']))==s['sha256'],s['id']
for out in om['outputs']:assert sha(author/out['path'])==out['sha256'],out['id']
m['sources']=copy.deepcopy(om['sources']);m['outputs']=copy.deepcopy(om['outputs']);m['required_topics']=copy.deepcopy(om['required_topics']);m['output_checks']=copy.deepcopy(om['output_checks'])
t['source_reads']=copy.deepcopy(ot['source_reads']);t['requirements']=copy.deepcopy(ot['requirements']);t['gaps']=copy.deepcopy(ot['gaps'])
for out in m['outputs']:out['path']=rel(author/out['path'])
# Relocate actual witness paths from author-root to repository-root, preserving identities.
for rec in [*t['requirements'].values(),*m['output_checks']]:
 rec['dependencies']=[]
 for e in rec['evidence']:
  if e['path']!='@request':
   f=author/e['path'];assert sha(f)==e['sha256'];e['path']=rel(f)
new=[('dest-review',case/'destination-v2/review.md'),('dest-audit',case/'destination-v2/final-audit.json'),('dest-math',case/'destination-v2/math-comparison.json'),('dest-prose',case/'destination-v2/prose-comparison.json'),('dest-css',case/'destination-v2/css-font-rules.json'),('dest-visual',case/'destination-v2/visual-inspection.json'),('dest-navigation',case/'destination-v2/navigation.json'),('dest-preview',case/'destination-v2/preview-final/preview-check.json'),('dest-source-link',case/'destination-v2/source-PDF-link-check.json'),('dest-disposition',p/'destination-evidence-disposition.md')]
for ident,f in new:
 m['sources'].append({'id':ident,'path':str(f),'sha256':sha(f),'portions':[{'id':'whole','locator':'whole file','disposition':'required','reason':'','evidence':[]}]})
 t['source_reads'].append({'source_id':ident,'portion_id':'whole','status':'read','reviewed_sha256':sha(f),'note':'Complete current-v2 destination evidence actually read. Scope and runtime limitations retained in destination-evidence-disposition.md; not a claim of a new personal browser/page inspection.'})
m['required_topics'][0]['source_portions']=[{'source_id':s['id'],'portion_id':v['id']} for s in m['sources'] for v in s['portions']]
d=p/'destination-evidence-disposition.md';evidence=[ev(d,para(d,'Observed destination pass.')),ev(d,para(d,'Visual scope.')),ev(d,para(d,'Limits retained in the T11/destination pass.'))]
reason='PASS only for observed actual server parser/CSS/navigation/image identity and complete source-faithful internal preview evidence. All156 math payloads exact and correct separated task/help navigation; no material issue in inspected scope. Live GitHub pixels, computed styles, browser clicks, responsive layout and client MathJax execution unobserved; this is not a live-browser pass.'
t['requirements']['T11']={'applicable':True,'status':'pass','reason':reason,'evidence':evidence,'dependencies':[]}
for rec in m['output_checks']:
 if rec['id']=='destination':rec.update(status='pass',reason=reason,evidence=copy.deepcopy(evidence),dependencies=[])
 if rec['id'] in ('sasis-reader','final_review'):rec.update(status='pending',reason='Await completed fresh-v2 reader report and independently verified root disposition; no final acceptance.',dependencies=[])
t['requirements']['T12'].update(status='pending',reason='Whole-v2 author review and destination observed-scope review exist; completed fresh reader and root final disposition pending. No final acceptance.',dependencies=[])
(st/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');(st/'topics/max-min.json').write_text(json.dumps(t,indent=2)+'\n')
def snapshot(args,name):
 r=subprocess.run([sys.executable,str(helper),'dependencies','--state',str(st),*args],capture_output=True,text=True);assert r.returncode==0,r.stderr
 (p/name).write_text(r.stdout);return json.loads(r.stdout)
g=snapshot([],'dependencies.json');local=snapshot(['--topic','max-min'],'topic-dependencies.json')
for rec in t['requirements'].values():
 if rec['status']=='pass':rec['dependencies']=local
for rec in m['output_checks']:
 if rec['status']=='pass':rec['dependencies']=g
(st/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');(st/'topics/max-min.json').write_text(json.dumps(t,indent=2)+'\n')
(st/'RUN.md').write_text('D010 separate final-state scaffold\n\nRepository-relative case: '+rel(case)+'\nFrozen skill: '+rel(p/'inputs/SKILL-r16.md')+' (r16 unchanged bytes). Exact request: '+rel(p/'inputs/requests.md')+'\nTeaching: '+rel(author/'teaching-v2.md')+' plus five unchanged PNGs, freeze-v2.json.\nDefinition repairs and full reread: '+rel(author/'v2-repair-and-audit.md')+'\nDestination observed-scope disposition: '+rel(d)+'\nT1–T11 pass for exact stated scopes; T12,new-v2SASIS,final_review pending. Runtime browser boundaries remain unobserved. Next action: read completed fresh-v2 report and root issue/acceptance disposition, then bind their actual evidence and run full check without altering historical states. path-index.json records repo-relative recovery paths for helper-required absolute fields.\n')
idx={'repository_root_at_check':str(root),'skill':rel(Path(m['skill']['path'])),'request':rel(Path(m['request']['path'])),'sources':{s['id']:rel(Path(s['path'])) for s in m['sources']},'outputs':{o['id']:o['path'] for o in m['outputs']},'state_path':rel(st),'schema_note':'Absolute source/request/skill/project paths required by helper schema. All destinations and witness paths are repo-relative; rebase absolute prefixes to new checkout then verify exact hashes when recovering.'}
(p/'path-index.json').write_text(json.dumps(idx,indent=2)+'\n')
for name,args in [('topic',['--topic','max-min']),('full',[])]:
 r=subprocess.run([sys.executable,str(helper),'check','--state',str(st),*args,'--json'],capture_output=True,text=True);(p/f'{name}-check.json').write_text(r.stdout or r.stderr);print(name,r.returncode,r.stdout or r.stderr)
# Preserve both complete original states, not merely their learner outputs.
for item in json.loads((author/'artifact-inventory.json').read_text()):assert sha(author/item['path'])==item['sha256']
for item in json.loads((author/'artifact-inventory-v2.json').read_text())['files']:assert sha(author/item['path'])==item['sha256']
print('Both historical state/artifact inventories unchanged')
