from pathlib import Path
import json,hashlib,subprocess
root=Path('/workspace/scratch/6a5c7131498d/prof-r18');p=Path(__file__).parent;st=p/'.prof-state';script=root/'scripts/prof_state.py'
def sha(q):return hashlib.sha256(q.read_bytes()).hexdigest()
def deps(t=None):
 cmd=['python',str(script),'dependencies','--state',str(st)]+(['--topic',t] if t else []);r=subprocess.run(cmd,text=True,capture_output=True);assert r.returncode==0,r.stdout+r.stderr;return json.loads(r.stdout)
for tid in ['newton','ring']:
 q=st/'topics'/f'{tid}.json';t=json.loads(q.read_text());d=deps(tid)
 for v in t['requirements'].values():
  if v['status']=='pass':v['dependencies']=d
 q.write_text(json.dumps(t,indent=2))
m=json.loads((st/'manifest.json').read_text());d=deps();audit=(p/'author-audit-v1.md').read_text();first=audit.splitlines()[2];mapping=audit.split('Final source mapping\n\n')[1].split('\n')[0]
for c in m['output_checks']:
 if c['status']=='pass':
  c['dependencies']=d;c['evidence']=[{'path':'author-audit-v1.md','sha256':sha(p/'author-audit-v1.md'),'locator':{'kind':'text','value':mapping if c['id']=='coverage' else first}}]
(st/'manifest.json').write_text(json.dumps(m,indent=2))
(st/'RUN.md').write_text('D012 author current frozen v1: teaching-v1.md and fourPNG, exactpacket-v1.json. r18; originalrequests path bound. Two capabilities newton/ring split into two helper topics after one connected pre-draft scope grouping; skill was actually reread before ring. Fullbaseline and all7originalpages read. T1–T10 author scope pass; T11/T12 and actualdestination/SASIS/independentreview/finalacceptance pending. See author-audit-v1.md, technical-checks-v1.json, source-coverage-v1.md and baseline-access.json. Next root completes independent and freshreader/destination gates; preserve v1 unchanged.\n')
results={}
for tid in ['newton','ring',None]:
 cmd=['python',str(script),'check','--state',str(st)]+(['--topic',tid] if tid else []);r=subprocess.run(cmd,capture_output=True,text=True);results[tid or 'full']={'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
(p/'helper-checks-v1.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
