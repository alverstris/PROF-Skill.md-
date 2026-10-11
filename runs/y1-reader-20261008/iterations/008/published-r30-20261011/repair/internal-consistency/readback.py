import pathlib,json,subprocess,hashlib,sys
w=pathlib.Path('/workspace/scratch/f9c0b7fc7e76/d008-clean-r30-20261011');repo=w.parent/'prof-iteration';pin=sys.argv[1];d=w/'repair/internal-consistency';files=json.loads((d/'publication-files.json').read_bytes())
subprocess.run(['git','fetch','origin','--stdin'],cwd=repo,input=('\n'.join(sorted(set(f['git_blob'] for f in files)))+'\n').encode(),check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out=subprocess.run(['git','cat-file','--batch'],cwd=repo,input=('\n'.join(pin+':'+f['path'] for f in files)+'\n').encode(),check=True,stdout=subprocess.PIPE).stdout
pos=0;rec=[];fetchroot=w/'corrected-prof-r31-published'
for f in files:
 end=out.index(b'\n',pos);head=out[pos:end].decode().split();size=int(head[2]);b=out[end+1:end+1+size];pos=end+2+size
 assert head[1]=='blob' and head[0]==f['git_blob'] and len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'] and b==(w/f['local']).read_bytes(),f['path']
 rec.append(dict(path=f['path'],bytes=size,sha256=f['sha256'],git_blob=head[0],match=True))
 if not f['path'].startswith('runs/'):
  target=fetchroot/f['path'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(b)
assert pos==len(out)
subprocess.run([sys.executable,str(d/'validate_internal.py'),str(fetchroot),str(d/'all-internal-checks-published.json')],check=True)
(d/'correction-publication-readback.json').write_text(json.dumps(dict(commit=pin,all_pass=True,files=rec,package_files=36,bundled_internal_references=34,internal_reference_check='all-internal-checks-published.json',status='corrected complete published package bytes and internal declarations verified; fresh generation permitted; D008 still pending'),indent=2)+'\n')
print('PASS all',len(rec),'published paths, 36 package files, 34 internal declarations')
