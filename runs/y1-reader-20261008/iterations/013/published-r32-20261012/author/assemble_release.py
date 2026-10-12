from pathlib import Path
import json,hashlib,base64,zipfile
w=Path('/workspace/scratch/f9c0b7fc7e76/d013-clean-r32-20261012'); prefix='runs/y1-reader-20261008/iterations/013/published-r32-20261012/'
def ident(local,path,reuse=False):
 b=local.read_bytes();return dict(path=path,local_path=str(local),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),reuse=reuse)
rm=json.loads((w/'evidence/root-complete-archive-manifest.json').read_text())
with zipfile.ZipFile(w/'evidence/root-complete-original.zip') as z:
 for row in rm['members']:
  b=z.read(row['path']);assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
items=[]
for row in json.loads((w/'evidence/repair-package-manifest.json').read_text())['files']:
 items.append(ident(w/'candidate-prof-r33-repair'/row['path'],row['path'],True))
for sub in ['evidence','author','.prof-state']:
 for p in sorted((w/sub).rglob('*')):
  if p.is_file() and p.name != 'root-complete-original.zip':items.append(ident(p,prefix+str(p.relative_to(w))))
for row in json.loads((w/'publication-opaque.json').read_text()):items.append(ident(Path(row['local_path']),row['path'], row['git_blob'] in ['304e17719cd733f1d9bc3704303988607d205e23','42ccbc29ad4c3a4920ef211ceedd96b94db36f57','cc2c88963733d6826b11c15b158bcfdadeb5637b']))
for name,sha in [('d033-d034-technical-original-preparation-20261012.zip','f6e3887d2ffaaef2ae40ba08d57356661c246b96a30731edd7a1afc1c0d1730b'),('d033-d034-technical-original-preparation-20261012-manifest.json','4143f13ca682eeaf76d52ff5a1af836fc85e9c0ef5b132fde40fe9b735334e9d')]:
 row=ident(w.parent/'source-audit-archives'/name,prefix+'evidence/opaque/'+name);assert row['sha256']==sha;items.append(row)
assert len(set(r['path'] for r in items))==len(items)
(w/'release-items.json').write_text(json.dumps(items,indent=2)+'\n')
full=items[:]
for row in json.loads((w/'evidence/whole-freeze-manifest.json').read_text())['files']:
 full.append(ident(Path(row['local_path']),prefix+'teaching/'+row['path'],True))
(w/'release-verification-manifest.json').write_text(json.dumps(full,indent=2)+'\n')
small=[{**r,'content':base64.b64encode(Path(r['local_path']).read_bytes()).decode()} for r in items if not r['reuse'] and r['bytes']<1000000]
large=[r for r in items if not r['reuse'] and r['bytes']>=1000000]
(w/'release-small-upload.json').write_text(json.dumps(small,separators=(',',':')))
for r in large:
 (w/('upload-'+r['git_blob']+'.b64')).write_bytes(base64.b64encode(Path(r['local_path']).read_bytes()))
print(json.dumps({'items':len(items),'small':len(small),'small_json_bytes':(w/'release-small-upload.json').stat().st_size,'large':large}))
