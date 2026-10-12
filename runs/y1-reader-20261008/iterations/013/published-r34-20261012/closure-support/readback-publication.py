from pathlib import Path
import subprocess,json,hashlib,sys,zipfile,io
W=Path(__file__).resolve().parents[1]; clone=W.parent/'prof-iteration'; pin=sys.argv[1]; mp=Path(sys.argv[2]); out=Path(sys.argv[3]); rows=json.loads(mp.read_bytes());h=lambda b:hashlib.sha256(b).hexdigest();blob=lambda b:hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def git(args,data=None):return subprocess.run(['git','-C',str(clone),*args],input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout
extra=[]
for p in sorted((W/'teaching').rglob('*')):
 if p.is_file():extra.append({'local':str(p),'path':'runs/y1-reader-20261008/iterations/013/published-r34-20261012/teaching/'+p.relative_to(W/'teaching').as_posix()})
if 'release/' in str(mp):
 for n in ['queue.json','RUN.md','CHANGELOG.md']:extra.append({'local':str(W/'canonical-before'/n),'path':'runs/y1-reader-20261008/'+n})
for e in extra:
 b=Path(e['local']).read_bytes();e.update(bytes=len(b),sha256=h(b),git_blob=blob(b))
allrows=rows+extra
fetch='\n'.join(dict.fromkeys([pin]+[e['git_blob'] for e in allrows]))+'\n';git(['fetch','origin','--stdin'],fetch.encode())
raw=git(['cat-file','--batch'],''.join(pin+':'+e['path']+'\n' for e in allrows).encode());cursor=0;actual={};verified=[]
for e in allrows:
 end=raw.index(b'\n',cursor);head=raw[cursor:end].decode().split();assert len(head)==3 and head[1]=='blob',(e,head);n=int(head[2]);cursor=end+1;b=raw[cursor:cursor+n];cursor+=n;assert raw[cursor:cursor+1]==b'\n';cursor+=1
 assert head[0]==e['git_blob'] and n==e['bytes'] and h(b)==e['sha256'] and blob(b)==e['git_blob'] and b==Path(e['local']).read_bytes(),e['path'];actual[e['path']]=b;verified.append({k:e[k] for k in ['path','bytes','sha256','git_blob']})
assert cursor==len(raw)
archives=[]
for path,b in actual.items():
 if path.endswith('-members.json'):
  m=json.loads(b);prefix=path.rsplit('/',1)[0]+'/';key=prefix+m['archive'];z=actual.get(key)
  if z is None:
   reassembly=json.loads(actual[prefix+m['archive'].replace('.zip','-reassembly.json')]);parts=[]
   for p in sorted(reassembly['parts'],key=lambda r:r['ordinal']):
    data=actual[prefix+p['filename']];assert len(data)==p['bytes'] and h(data)==p['sha256'];parts.append(data)
   z=b''.join(parts)
  assert len(z)==m['archive_bytes'] and h(z)==m['archive_sha256']
  with zipfile.ZipFile(io.BytesIO(z)) as ar:
   assert ar.testzip() is None and len(ar.namelist())==m['member_count']
   for member in m['members']:
    data=ar.read(member['path']);assert len(data)==member['bytes'] and h(data)==member['sha256']
  archives.append({'archive':m['archive'],'bytes':len(z),'sha256':h(z),'members_verified':m['member_count']})
opaque=None
for path,b in actual.items():
 if path.endswith('d108-d112-prepared-20261012-parts/reassembly-manifest.json'):
  m=json.loads(b);prefix=path.rsplit('/',1)[0]+'/';parts=[]
  for part in sorted(m['parts'],key=lambda r:r['ordinal']):
   data=actual[prefix+part['filename']];assert len(data)==part['bytes'] and h(data)==part['sha256'];parts.append(data)
  joined=b''.join(parts);assert len(joined)==m['archive_bytes'] and h(joined)==m['archive_sha256'] and joined==(W.parent/'source-audit-archives'/m['archive_filename']).read_bytes()
  with zipfile.ZipFile(io.BytesIO(joined)) as z:assert z.testzip() is None;member_count=len(z.namelist())
  opaque={'actual_remote_raw_parts':len(parts),'reconstructed_original_bytes':len(joined),'sha256':h(joined),'byte_equal_local_original':True,'zip_crc':True,'members':member_count,'semantic_contents_read':False}
package=json.loads((W/'release-package-manifest.json').read_bytes());pkg=[]
for e in package['files']:
 b=actual.get(e['path'])
 if b is None:b=git(['cat-file','blob',pin+':'+e['path']])
 assert len(b)==e['bytes'] and h(b)==e['sha256'] and blob(b)==e['git_blob'];p=W/'published-prof'/e['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);pkg.append(e)
p=W/'published-prof/references/sasis';prof=json.loads((p/'profile-manifest.json').read_bytes());decl=0
for s in prof['subject_files']:assert s['sha256']==h((p/s['path']).read_bytes());decl+=1
for name,sha in prof['file_hashes'].items():assert sha==h((p/prof['file_hashes_base_directory']/name).read_bytes());decl+=1
for name,sha in prof['control_file_hashes'].items():assert sha==h((p/name).read_bytes());decl+=1
for d in json.loads((W/'internal-hash-verification.json').read_bytes())['verified_declarations']:
 if d['declaration']!='references/sasis/profile-manifest.json':
  assert (W/'published-prof'/d['declaration']).read_bytes()==(W/'verified-prof'/d['declaration']).read_bytes();assert (W/'published-prof'/d['path']).read_bytes()==(W/'verified-prof'/d['path']).read_bytes();decl+=1
assert decl==34
receipt={'pin':pin,'tree':git(['rev-parse',pin+'^{tree}']).decode().strip(),'files':verified,'file_count':len(verified),'actual_bytes':sum(x['bytes'] for x in verified),'complete_package_files':len(pkg),'package_bytes':sum(x['bytes'] for x in pkg),'internal_hash_declarations':decl,'archives':archives,'actual_full_byte_comparison':True,'teaching_unchanged':True,'canonical_unchanged_at_release':bool('release/' in str(mp))}
receipt['opaque_future_original_reassembly']=opaque
out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k!='files'},indent=2))
