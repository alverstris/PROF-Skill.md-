from pathlib import Path
import json,subprocess
root=Path.cwd();state=root/'.prof-state-v3'
manifest=json.loads((state/'manifest.json').read_text());topic=json.loads((state/'topics/exponential-log.json').read_text())
results=[]
for scope,extra in [('topic',['--topic','exponential-log']),('full',[])]:
 r=subprocess.run(['python','controls/scripts/prof_state.py','dependencies','--state','.prof-state-v3',*extra],text=True,capture_output=True)
 (root/f'dependencies-v3-{scope}.json').write_text(r.stdout);(root/f'dependencies-v3-{scope}.stderr.txt').write_text(r.stderr)
 if r.returncode:raise RuntimeError(f'{scope} dependency snapshot failed: {r.stderr} {r.stdout}')
 deps=json.loads(r.stdout)
 if scope=='topic':
  for c in topic['requirements'].values():
   if c['status']=='pass':c['dependencies']=deps
 else:
  for c in manifest['output_checks']:
   if c['status']=='pass':c['dependencies']=deps
(state/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(state/'topics/exponential-log.json').write_text(json.dumps(topic,indent=2)+'\n')
for scope,extra in [('topic',['--topic','exponential-log']),('full',[])]:
 r=subprocess.run(['python','controls/scripts/prof_state.py','check','--state','.prof-state-v3',*extra],text=True,capture_output=True)
 (root/f'helper-check-v3-{scope}.txt').write_text(r.stdout+r.stderr)
 results.append({'scope':scope,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 print(scope,r.returncode,r.stdout)
(root/'helper-check-results-v3.json').write_text(json.dumps(results,indent=2)+'\n')
