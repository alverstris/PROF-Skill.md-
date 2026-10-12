from pathlib import Path
import subprocess,json,hashlib,zipfile,io
w=Path('/workspace/scratch/f9c0b7fc7e76/d013-clean-r32-20261012');repo=w.parent/'prof-iteration';commit='ea2fba9253430a45f7c4287684c064d86a74af64';prefix='runs/y1-reader-20261008/iterations/013/published-r32-20261012/'
def get(path):return subprocess.run(['git','cat-file','blob',commit+':'+path],cwd=repo,stdout=subprocess.PIPE,check=True).stdout
package=json.loads((w/'evidence/repair-package-manifest.json').read_text())['files'];out=w/'published-prof-r33';out.mkdir(exist_ok=True);bodies={}
for r in package:
 b=get(r['path']);assert hashlib.sha256(b).hexdigest()==r['sha256'];bodies[r['path']]=b;p=out/r['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
checks=[]
for r in json.loads((w/'evidence/internal-hashes.json').read_text())['internal_declarations']:
 value=json.loads(bodies[r['source']])
 for k in r['declaration'].split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');value=value[int(k)] if isinstance(value,list) else value[k]
 actual=hashlib.sha256(bodies[r['target']]).hexdigest();assert value==actual
 checks.append({'source':r['source'],'declaration':r['declaration'],'target':r['target'],'declared':value,'actual':actual,'match':True})
assert len(checks)==34
(w/'evidence/published-package-internal-check.json').write_text(json.dumps({'commit':commit,'package_count':36,'actual_full_bytes':True,'declarations':checks,'all_match':True},indent=2)+'\n')
re=json.loads(get(prefix+'evidence/root-complete-original-reassembly.json'));parts=[get(prefix+'evidence/'+r['path']) for r in re['parts']];archive=b''.join(parts);assert len(archive)==re['bytes'] and hashlib.sha256(archive).hexdigest()==re['sha256'];assert archive==(w/'evidence/root-complete-original.zip').read_bytes()
man=json.loads(get(prefix+'evidence/root-complete-archive-manifest.json'))
with zipfile.ZipFile(io.BytesIO(archive)) as z:
 assert z.testzip() is None
 for r in man['members']:
  b=z.read(r['path']);assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
(w/'evidence/published-root-archive-check.json').write_text(json.dumps({'commit':commit,'method':'Actual published raw part bytes concatenated, original ZIP byte equality, SHA256 and all87 uncompressed member byte identities verified.','bytes':len(archive),'sha256':hashlib.sha256(archive).hexdigest(),'members':len(man['members']),'all_match':True},indent=2)+'\n')
print('36 published package bytes extracted; 34 declarations verified; exact original 87-member ZIP reconstructed from published bytes.')
