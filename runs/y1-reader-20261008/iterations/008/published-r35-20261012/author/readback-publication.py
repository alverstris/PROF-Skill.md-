from pathlib import Path
import json,hashlib,subprocess,sys,io,zipfile,datetime
w=Path(__file__).resolve().parents[1];repo=w.parent/'prof-iteration';pin,manifest,output=sys.argv[1:];files=json.loads((w/manifest).read_text());H=lambda b:hashlib.sha256(b).hexdigest()
def git(args,inp=None):
 p=subprocess.run(['git','-C',str(repo)]+args,input=inp,stdout=subprocess.PIPE,stderr=subprocess.PIPE);assert p.returncode==0,p.stderr.decode(errors='replace');return p.stdout
requested=list(dict.fromkeys([pin]+[x['git_blob'] for x in files]));fetch=git(['fetch','--no-tags','origin','--stdin'],('\n'.join(requested)+'\n').encode())
raw=git(['cat-file','--batch'],''.join(pin+':'+x['path']+'\n' for x in files).encode());pos=0;checks=[];actual={};extracted=w/'publication'/(pin+'-readback');extracted.mkdir(exist_ok=True)
for f in files:
 end=raw.index(b'\n',pos);head=raw[pos:end].decode().split();assert len(head)==3 and head[1]=='blob',head;n=int(head[2]);b=raw[end+1:end+1+n];assert raw[end+1+n:end+2+n]==b'\n';pos=end+2+n
 assert n==f['bytes'] and H(b)==f['sha256'] and head[0]==f['git_blob'] and b==Path(f['local']).read_bytes(),f['path']
 actual[f['path']]=b;checks.append({k:f[k] for k in ['path','bytes','sha256','git_blob']}|{'whole_actual_bytes_match_local':True});p=extracted/f['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
assert pos==len(raw)
head=git(['ls-remote','origin','refs/heads/main']).decode().split()[0];assert head==pin,(head,pin);tree=git(['rev-parse',pin+'^{tree}']).decode().strip();prefix='runs/y1-reader-20261008/iterations/008/published-r35-20261012/'
package=json.loads((w/'evidence/outgoing-package-manifest.json').read_text());assert len(package['files'])==36
for f in package['files']:assert H(actual[f['path']])==f['sha256']
# Verify every outgoing bundled declaration against actual published package bytes.
declarations=[]
def dec(target,sha):assert H(actual[target])==sha;declarations.append({'target':target,'sha256':sha,'pass':True})
pre='references/sasis/';profile=json.loads(actual[pre+'profile-manifest.json'])
for x in profile['subject_files']:dec(pre+x['path'],x['sha256'])
for path,sha in profile['file_hashes'].items():dec(pre+profile['file_hashes_base_directory']+'/'+path,sha)
for path,sha in profile['control_file_hashes'].items():dec(pre+path,sha)
base=pre+'ocr-baseline-20261007/';rel=json.loads(actual[base+'release-manifest.json'])
for x in rel['subjects']:dec(base+x.get('path',x.get('baseline_path')),x['sha256'])
dec(base+'student-baseline.txt',rel['combined_baseline_sha256']);chem=json.loads(actual[base+'chemistry/freeze-manifest.json'])
for x in chem['files']:
 target=base+'chemistry/'+x.get('path',x.get('name'))
 if target in actual:dec(target,x['sha256'])
assert len(declarations)==34
archives=[]
rp=prefix+'evidence/archives/evidence-archive-reassembly.json'
if rp in actual:
 r=json.loads(actual[rp]);b=b''.join(actual[x['path']] for x in r['parts']);assert len(b)==r['original_bytes'] and H(b)==r['original_sha256'];assert b==(w/'publication/d008-complete-original-evidence.zip').read_bytes();m=json.loads(actual[prefix+'evidence/archives/evidence-archive-manifest.json'])
 with zipfile.ZipFile(io.BytesIO(b)) as z:
  assert len(z.namelist())==m['member_count']
  for f in m['members']:v=z.read(f['path']);assert len(v)==f['bytes'] and H(v)==f['sha256']
 archives.append({'name':r['original_name'],'actual_reassembled_bytes':len(b),'sha256':H(b),'verified_member_count':m['member_count'],'all_actual_member_identities_match':True})
future=prefix+'evidence/future-preparation/'
for name in ['d116-d118-prepared-20261012','d119-d121-prepared-20261012']:
 p=future+name+'.zip'
 if p in actual:b=actual[p]
 elif future+name+'-parts/'+name+'.zip.part001' in actual:b=actual[future+name+'-parts/'+name+'.zip.part001']+actual[future+name+'-parts/'+name+'.zip.part002']
 else:continue
 original=w.parent/'source-audit-archives'/(name+'.zip');assert b==original.read_bytes();archives.append({'name':name+'.zip','actual_reassembled_bytes':len(b),'sha256':H(b),'whole_original_bytes_match':True,'semantic_content_not_read':True})
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pin':pin,'tree':tree,'main_equals_pin':head==pin,'all_bytes_match':True,'paths':len(checks),'total_bytes':sum(x['bytes'] for x in checks),'checks':checks,'package_files':36,'package_bytes':907146,'internal_declaration_count':len(declarations),'internal_declarations':declarations,'archives':archives,'actual_readback_directory':str(extracted),'method':'Exact intended blob SHAs and commit fetched in one readonly git fetch origin --stdin; binary cat-file --batch returned every complete path payload, byte-compared with intended local originals. No checkout/index/history mutation.'}
(w/output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['pin','tree','all_bytes_match','paths','total_bytes','package_files','internal_declaration_count','archives']}))
