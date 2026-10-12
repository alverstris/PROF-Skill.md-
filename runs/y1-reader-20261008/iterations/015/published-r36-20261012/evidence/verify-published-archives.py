from pathlib import Path
import subprocess,json,hashlib,zipfile,io,sys,datetime
B=Path(__file__).resolve().parents[1];plan=json.loads((B/'work/release-plan.json').read_text());receipt=json.loads((B/'work/release-readback.json').read_text());pin=receipt['pin'];repo=B.parent/'prof-iteration'
assert receipt['all_actual_bytes_match']
def sha(b):return hashlib.sha256(b).hexdigest()
def actual(rel):
 f=next(f for f in plan['files'] if f['local']==str(B/rel));b=subprocess.check_output(['git','cat-file','blob',f['git_blob']],cwd=repo);assert sha(b)==f['sha256'] and len(b)==f['bytes'];return b
rows=[]
for archive,manifest in [('reader-and-preflight.zip','reader-and-preflight-manifest.json'),('technical-original.zip','technical-original-manifest.json'),('independent-mechanics.zip','independent-mechanics-manifest.json'),('author-original-inputs-and-state.zip','author-original-inputs-and-state-manifest.json'),('d015-r36-root-review-20261012.zip','d015-r36-root-review-20261012.manifest.json')]:
 b=actual('evidence/'+archive);m=json.loads(actual('evidence/'+manifest));members=m['files'] if 'files' in m else m['members'];expected_sha=m.get('sha256',m.get('archive_sha256'));assert sha(b)==expected_sha
 with zipfile.ZipFile(io.BytesIO(b)) as z:
  assert len(z.namelist())==len(members)
  for f in members:
   data=z.read(f['path']);assert len(data)==f['bytes'] and sha(data)==f['sha256']
 rows.append({'archive':archive,'actual_git_bytes':len(b),'sha256':sha(b),'all_members_verified':len(members)})
for v in ['v10','v11']:
 stem=v+'-d015-r36-20261012';b=actual('evidence/'+stem+'.zip');mb=actual('evidence/'+stem+'-manifest.json');m=json.loads(mb)
 with zipfile.ZipFile(io.BytesIO(b)) as z:
  assert z.read(stem+'/MANIFEST.json')==mb and len(z.namelist())==len(m['files'])+1
  for f in m['files']:
   data=z.read(stem+'/'+f['path']);assert len(data)==f['bytes'] and sha(data)==f['sha256']
 rows.append({'archive':stem+'.zip','actual_git_bytes':len(b),'sha256':sha(b),'all_members_verified':len(m['files'])+1})
opaque=json.loads(actual('evidence/preserved-archives.json'))
for f in opaque['files']:
 b=actual(f['path']);assert len(b)==f['bytes'] and sha(b)==f['sha256']
out={'pin':pin,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_git_archive_member_checks':rows,'opaque_archive_and_manifest_files':len(opaque['files']),'opaque_semantics_unpacked':False,'all_pass':True}
(B/'work/published-archive-readback.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
