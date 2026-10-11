import json,hashlib,sys,pathlib
root=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]); records=[]
def check(decl,path,wanted,size=None):
 b=(root/path).read_bytes(); actual=hashlib.sha256(b).hexdigest(); ok=actual==wanted and (size is None or len(b)==size)
 records.append(dict(declaration=decl,path=path,declared_sha256=wanted,actual_sha256=actual,bytes=len(b),match=ok)); assert ok,path
prefix='references/sasis/'; base=prefix+'ocr-baseline-20261007/'
p=json.loads((root/prefix/'profile-manifest.json').read_bytes())
for k,v in p['file_hashes'].items(): check('profile.file_hashes',base+k,v)
for k,v in p['control_file_hashes'].items():check('profile.control_file_hashes',prefix+k,v)
for item in p['subject_files']: check('profile.subject_files',prefix+item['path'],item['sha256'])
r=json.loads((root/base/'release-manifest.json').read_bytes())
for item in r['subjects']:check('release.subjects',base+item['path'],item['sha256'],item['bytes'])
check('release.combined_baseline',base+'student-baseline.txt',r['combined_baseline_sha256'])
f=json.loads((root/base/'chemistry/freeze-manifest.json').read_bytes())
for item in f['files']:
 path=base+'chemistry/'+item['path']
 if (root/path).exists():check('chemistry.freeze',path,item['sha256'],item['bytes'])
assert len(records)==34
out.write_text(json.dumps(dict(scope='All 34 bundled SHA256 declarations in the complete 36-file package; 31 historical/external declarations retain provenance and are outside bundled-byte validation.',package_root=str(root),checks=records,all_pass=True),indent=2)+'\n')
print('PASS: 34 bundled hash declarations')
