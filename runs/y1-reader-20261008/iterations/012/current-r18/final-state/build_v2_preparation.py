from pathlib import Path
import json,hashlib,subprocess
out=Path(__file__).resolve().parent;base=out.parent;repo=out.parents[5];author=base/'author';st=out/'v2-preparation';script=out/'inputs/scripts/prof_state.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+'\n')
def evidence(path,text):return {'path':path,'sha256':sha(base/path),'locator':{'kind':'text','value':text}}
def run(*args):
 r=subprocess.run(['python',str(script),*args],text=True,capture_output=True)
 return r
assert not st.exists(),'Preserve existing preparation; use a new revision for subsequent evidence.'
for r in json.loads((out/'incoming-inputs-inventory.json').read_text())['files']:
 assert sha(repo/r['frozen']['path'])==r['original']['sha256']
m=json.loads((author/'.prof-state/manifest.json').read_text());m['project_root']=str(base)
for name in ['skill','request']:
 original=Path(m[name]['path']); frozen=out/'inputs'/original.relative_to(repo); assert sha(original)==sha(frozen);m[name]['path']=str(frozen)
for s in m['sources']:
 original=Path(s['path']);frozen=out/'inputs'/original.relative_to(repo)
 if frozen.exists():s['path']=str(frozen)
for o in m['outputs']:
 o['path']='author/'+('teaching-v2.md' if o['id']=='teaching' else o['path']);o['sha256']=sha(base/o['path'])
extras={
 'current-audit':'author/author-audit-v2.md','current-math':'author/technical-checks-v2.json','current-math-code':'author/technical_checks_v2.py','repair-proof':'author/v2-repair-equivalence.json','repair-code':'author/repair_v2.py','repair-diff':'author/v1-to-v2.diff','packet':'author/packet-v2.json',
 'root-math-review':'root-technical-review-v1.md','root-original-source':'root-source-review.md','root-source-math':'root-source-calculations.json','root-final-math':'root-v1-extra-calculations.json','root-optics':'root-ellipse-optics-verification.md','root-presolution':'root-presolution-record.json','root-presolution-review':'root-presolution-review.md','root-current-review':'root-v2-repair-verification.json',
 'original-destination-review':'destination-v1/review.md','original-destination-result':'destination-v1/final-audit.json','original-destination-map':'destination-v1/complete-math-failure-map.json','root-destination-disposition':'root-destination-v1-disposition.md'}
for sid,name in extras.items():
 f=base/name;m['sources'].append({'id':sid,'path':str(f),'sha256':sha(f),'portions':[{'id':'full','locator':'Complete file; actual scope and chronology in author-audit-v2.md and final-state/v2-preparation/RUN.md','disposition':'required','reason':'Current content review, independent verification, exact representation repair or preserved defect evidence; not a substitute for pending fresh external gates.','evidence':[]}]})
for td in m['required_topics']:
 td['source_portions'] += [{'source_id':sid,'portion_id':'full'} for sid in extras]
current=(author/'author-audit-v2.md').read_text().split('\n\n')
get=lambda start:next(x for x in current if x.startswith(start))
common=get('Current T witnesses.')
checks={
 'coverage':('pass',get('Coverage and preservation.')),
 'author_reconstruction':('pass',get('Full current reconstruction, Newton route.')+'\n\n'+get('Full current reconstruction, ring route.')),
 'technical':('pass',common),
 'figure_visual':('pass',get('Scope and actual access.')),
 'source_navigation':('pass',get('Exact repair map and proof.')),
 'independent_review':('pass','Representation-only equivalence is independently verified in root-v2-repair-verification.json; root full current read and original source/math/presolution review corroborate unchanged semantics. This is not fresh reader/destination/final acceptance.'),
 'sasis':('pending','Fresh separate whole-baseline/full-v2 reader is active; completed original report and lead admission/disposition not yet supplied.'),
 'destination':('pending','V1 actual parser failed; v2 source repair has no fresh actual destination preservation/style/navigation result yet.'),
 'full_preview':('pending','Fresh complete final preview, every page and help destination audit pending; v1 preview was explicitly held.'),
 'final_review':('pending','Final integration and acceptance await fresh SASIS, actual destination/full preview and complete current evidence reconciliation.')}
m['output_checks']=[]
for cid,(status,reason) in checks.items():
 ev=[]
 if status=='pass':
  if cid=='independent_review':
   text=(base/'root-v2-repair-verification.json').read_text();ev=[evidence('root-v2-repair-verification.json',text)]
  else:ev=[evidence('author/author-audit-v2.md',reason)]
 m['output_checks'].append({'id':cid,'description':reason,'applicable':True,'status':status,'reason':reason,'evidence':ev,'dependencies':[]})
write(st/'manifest.json',m)
(st/'RUN.md').write_text('D012 v2 helper preparation in progress; all fresh external gates pending. Next finish current dependency binding and checks.\n')
for tid in ['newton','ring']:
 t=json.loads((author/f'.prof-state/topics/{tid}.json').read_text())
 for sid,name in extras.items():t['source_reads'].append({'source_id':sid,'portion_id':'full','status':'read','reviewed_sha256':sha(base/name),'note':'Complete actual evidence read/generated/checked at v2 preparation; original source/math evidence remains unchanged and current equivalence independently checked. Fresh external gates are not represented by these historical records.'})
 t['gaps']=[{'id':'destination-recheck','question':'Does the actual v2 destination preserve all 309 expressions, prose/style/help links and complete usable preview?','consequential':True,'status':'unverified','reason':'V1 parser failed at23comparison signs/20inline payloads plus1insignificant leading-space mismatch. Local v2 is inverse-equivalent but source alone cannot prove destination preservation.','next_action':'Read the fresh full v2 destination report and final preview evidence, reconcile every finding, then bind current evidence.','evidence':[evidence('author/author-audit-v2.md',get('Supported defect and repair.'))],'dependencies':[]}]
 for key,r in t['requirements'].items():
  r['dependencies']=[]
  if int(key[1:])<=10:
   r['status']='pass';r['reason']=r['reason'].replace('technical-checks-v1.json','technical-checks-v2.json').replace('Independent root/SASIS remain separate pending gates.','Root independent v2 inverse/full reading is complete; fresh SASIS/destination/final remain pending.')
   r['evidence']=[evidence('author/author-audit-v2.md',get('Full current reconstruction, Newton route.' if tid=='newton' else 'Full current reconstruction, ring route.')),evidence('author/author-audit-v2.md',common),evidence('author/author-audit-v2.md',get('Full current help/seam reconstruction.'))]
  else:
   r['status']='pending';r['reason']=checks['destination' if key=='T11' else 'final_review'][1];r['evidence']=[]
 write(st/f'topics/{tid}.json',t)
 r=run('begin-topic','--state',str(st),'--topic',tid);assert r.returncode==0,r.stdout+r.stderr
for tid in ['newton','ring']:
 r=run('dependencies','--state',str(st),'--topic',tid);assert r.returncode==0,r.stdout+r.stderr;deps=json.loads(r.stdout)
 t=json.loads((st/f'topics/{tid}.json').read_text())
 for v in t['requirements'].values():
  if v['status']=='pass':v['dependencies']=deps
 write(st/f'topics/{tid}.json',t)
r=run('dependencies','--state',str(st));assert r.returncode==0,r.stdout+r.stderr;deps=json.loads(r.stdout)
for c in m['output_checks']:
 if c['status']=='pass':c['dependencies']=deps
write(st/'manifest.json',m)
(st/'RUN.md').write_text('D012 v2 preparation, NOT final acceptance. Current outputs: author/packet-v2.json, teaching SHA04355b5ac132bfdaecf6a165cf332d0e04a0ff29bd59b53e03d6c801c9838d59, four unchanged PNGs. Frozen incoming r18 and exact controls/request bound from final-state/inputs. Author fully reread SKILL/stateguide/execution/exactrequests and current records; execution packet clipping recovered at lines61–90. Full v2 read and all four complete PNGs reinspected in author-audit-v2.md. All original source/baseline full reads remain recorded, not reattributed to this bookkeeping step.\n\nT1–T10 and performed source/math/author/independent content review bind current bytes; T11/T12, fresh SASIS, actual destination, full preview and final review pending. Historical destination defect remains an unverified consequential recheck gap until actual fresh destination evidence. Original author/.prof-state, helper-checks-v1.json and prior preparation untouched. Next: receive/read complete fresh reader and destination reports, disposition all supported issues, then create separate final state with current bindings and full checks.\n')
results={}
for tid in ['newton','ring',None]:
 args=['check','--state',str(st)]+(['--topic',tid] if tid else []);r=run(*args);results[tid or 'full']={'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
write(out/'helper-checks-v2-preparation.json',results)
print(json.dumps(results,indent=2))
