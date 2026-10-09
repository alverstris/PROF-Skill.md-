from pathlib import Path
import json,hashlib,subprocess,shutil
out=Path(__file__).resolve().parent;base=out.parent;repo=out.parents[5];prep=out/'v2-preparation';st=out/'v2-final';script=out/'inputs/scripts/prof_state.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2)+'\n')
def info(p):return {'path':str(p.relative_to(repo)),'bytes':p.stat().st_size,'sha256':sha(p)}
def ev(path,text):return {'path':path,'sha256':sha(base/path),'locator':{'kind':'text','value':text}}
def run(*args):return subprocess.run(['python',str(script),*args],capture_output=True,text=True)
assert not st.exists(),'Do not overwrite final evidence; preserve before retry.'
preserve_paths=[p for p in (base/'author/.prof-state').rglob('*') if p.is_file()]+[base/'author/helper-checks-v1.json']+[p for p in prep.rglob('*') if p.is_file()]+[out/'helper-checks-v2-preparation.json',out/'v2-preparation-inventory.json']
before=[info(p) for p in sorted(preserve_paths)]
m=json.loads((prep/'manifest.json').read_text());assert m['skill']['path']==str(out/'inputs/SKILL.md');assert sha(Path(m['skill']['path']))=='ffc6366348e1a9aa97f85adb0a6402b43c2a2c9532e994b3c947e086e0039394'
extras={
 'final-reconciliation':'author/final-reconciliation-v2.md','fresh-reader-original':'sasis-reader-v2-original.md','fresh-reader-disposition':'root-sasis-disposition-v2.md','final-destination-disposition':'root-destination-v2-disposition.md','final-issues':'issue-register.md','root-final-acceptance':'final-acceptance.md','final-destination-review':'destination-v2/review.md','final-destination-audit':'destination-v2/final-audit.json','final-visual-review':'destination-v2/visual-inspection.json','final-style-review':'destination-v2/style-supplement.json','final-native-navigation':'destination-v2/navigation.json','final-preview-ast':'destination-v2/preview-final/AST-content-check.json','final-preview-navigation':'destination-v2/preview-final/navigation-fonts.json','root-parser-verification':'root-destination-v2-independent-check.json','full-destination-inventory':'final-state/destination-v2-evidence-inventory.json'}
for sid,name in extras.items():
 m['sources'].append({'id':sid,'path':str(base/name),'sha256':sha(base/name),'portions':[{'id':'full','locator':'Complete textual evidence record read during final reconciliation; complete inventory generated and every file identity verified. Actual source/visual scopes preserved in author/final-reconciliation-v2.md.','disposition':'required','reason':'Final current reader, parser, style, navigation, full-preview or complete-issue evidence.','evidence':[]}]})
m['outputs'].append({'id':'internal-preview','path':'destination-v2/preview-final/main.pdf','sha256':sha(base/'destination-v2/preview-final/main.pdf')})
for td in m['required_topics']:
 td['source_portions'] += [{'source_id':sid,'portion_id':'full'} for sid in extras];td['outputs'].append('internal-preview')
parts=(base/'author/final-reconciliation-v2.md').read_text().split('\n\n');get=lambda start:next(x for x in parts if x.startswith(start))
finalpath='author/final-reconciliation-v2.md'
check_witness={
 'coverage':'Source, teaching and mathematical acceptance.', 'author_reconstruction':'Actual author access.', 'technical':'Source, teaching and mathematical acceptance.', 'figure_visual':'Destination repair acceptance and T11.', 'source_navigation':'Destination repair acceptance and T11.', 'independent_review':'Source, teaching and mathematical acceptance.', 'sasis':'Fresh SASIS acceptance.', 'destination':'Destination repair acceptance and T11.', 'full_preview':'Internal full preview acceptance.', 'final_review':'Limits and honest acceptance, T12.'}
for c in m['output_checks']:
 witness=get(check_witness[c['id']]);c.update(status='pass',reason=witness,evidence=[ev(finalpath,witness)],dependencies=[])
write(st/'manifest.json',m)
(st/'RUN.md').write_text('D012 v2 final content/helper state, frozen incoming r18. Exact learner packet author/packet-v2.json plus separately bound internal PDF evidence. Full source, author, independent math, fresh SASIS, destination and preview reconciled in author/final-reconciliation-v2.md; actual scopes/limits preserved. Original author and v2-preparation states remain unchanged. Next run full/topic helper checks, then root publishes evidence/metadata and verifies canonical readback before iteration closure.\n')
for tid in ['newton','ring']:
 t=json.loads((prep/f'topics/{tid}.json').read_text())
 for sid,name in extras.items():t['source_reads'].append({'source_id':sid,'portion_id':'full','status':'read','reviewed_sha256':sha(base/name),'note':'Complete actual textual report read, or complete inventory generated with each artifact identity checked; page visual access remains attributed precisely to original reviewer/root. No live-client observation claimed.'})
 for key,r in t['requirements'].items():
  r['status']='pass';r['dependencies']=[]
  if key=='T11':w=get('Destination repair acceptance and T11.');r['reason']=w;r['evidence']=[ev(finalpath,w),ev(finalpath,get('Internal full preview acceptance.')),ev(finalpath,get('Limits and honest acceptance, T12.'))]
  elif key=='T12':w=get('Limits and honest acceptance, T12.');r['reason']=w;r['evidence']=[ev(finalpath,w),ev(finalpath,get('Fresh SASIS acceptance.')),ev(finalpath,get('Source, teaching and mathematical acceptance.'))]
  else:
   r['reason']=r['reason'].replace('Root independent v2 inverse/full reading is complete; fresh SASIS/destination/final remain pending.','Root independent v2 inverse/full reading and fresh complete reader/destination/final content reviews are reconciled in final-reconciliation-v2.md.')
   r['evidence'].append(ev(finalpath,get('Source, teaching and mathematical acceptance.')))
 for g in t['gaps']:
  assert g['id']=='destination-recheck';g['status']='resolved';g['reason']=get('Destination repair acceptance and T11.');g['next_action']='No further content repair indicated; retain exact evidence and disclosed live-client/secondary-preview limits. Root publication/readback remains a separate iteration closure action.';g['evidence']=[ev(finalpath,g['reason']),ev(finalpath,get('Internal full preview acceptance.'))];g['dependencies']=[]
 write(st/f'topics/{tid}.json',t)
 r=run('begin-topic','--state',str(st),'--topic',tid);assert r.returncode==0,r.stdout+r.stderr
for tid in ['newton','ring']:
 r=run('dependencies','--state',str(st),'--topic',tid);assert r.returncode==0,r.stdout+r.stderr;deps=json.loads(r.stdout);t=json.loads((st/f'topics/{tid}.json').read_text())
 for v in t['requirements'].values():v['dependencies']=deps
 for g in t['gaps']:g['dependencies']=deps
 write(st/f'topics/{tid}.json',t)
r=run('dependencies','--state',str(st));assert r.returncode==0,r.stdout+r.stderr;deps=json.loads(r.stdout)
for c in m['output_checks']:c['dependencies']=deps
write(st/'manifest.json',m)
results={}
for tid in ['newton','ring',None]:
 args=['check','--state',str(st)]+(['--topic',tid] if tid else []);r=run(*args);results[tid or 'full']={'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
write(out/'helper-checks-v2-final.json',results)
after=[info(p) for p in sorted(preserve_paths)];assert before==after
write(out/'final-original-state-preservation.json',{'before':before,'after':after,'original_author_and_v2_preparation_unchanged':True})
print(json.dumps(results,indent=2))
