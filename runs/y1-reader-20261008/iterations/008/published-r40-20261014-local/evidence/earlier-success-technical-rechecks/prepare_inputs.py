from pathlib import Path
import subprocess,json,hashlib,sys,zipfile,io
sys.stdout.reconfigure(encoding='utf-8')
out=Path(__file__).resolve().parent
base=out.parents[2]
repo=base/'.prof-maintenance/20261014/repository'
old=base/'.prof-sasis/20261014-d008-r39/earlier-success-review'
queue=base/'.prof-sasis/20261014-d008-r40/run-state/queue.json'
ids=['D003','D005','D006','D007','D009','D012','D013','D015']
q=json.loads(queue.read_text(encoding='utf-8-sig'))
pin=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD']).decode().strip()
tree={}
for row in subprocess.check_output(['git','-C',str(repo),'ls-tree','-rz','HEAD']).split(b'\0'):
 if not row: continue
 meta,path=row.split(b'\t',1); tree[path.decode()]=meta.decode().split()[2]
inv=json.loads((old/'accepted-teaching-exposure-inventory.json').read_text(encoding='utf-8'))
result={'read_only_repository_head':pin,'queue_sha256':hashlib.sha256(queue.read_bytes()).hexdigest(),'queue_cases':[], 'accepted_teaching':[], 'source_files':[]}
for case in ids:
 s=next(s for s in q['sessions'] if s['material_id']==case)
 assert s['status']=='closed'
 result['queue_cases'].append(s)
 record=next(c for c in inv['cases'] if c['material_id']==case)
 for art in record['artifacts']:
  if not art['path'].endswith('.md'): continue
  rel=art['path'].split('/iterations/')[1].split('/',1)[1]
  copy=old/case/('teaching__'+rel.replace('/','__'))
  data=copy.read_bytes(); sha=hashlib.sha256(data).hexdigest()
  assert sha==art['sha256'] and len(data)==art['bytes']
  head_data=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',tree[art['path']]])
  assert head_data==data
  result['accepted_teaching'].append({'case':case,'copy':str(copy),'current_git_blob':tree[art['path']],'frozen_commit':record['commit'],'sha256':sha,'bytes':len(data),'current_head_matches':True})
sources={
 'D009':'runs/y1-reader-20261008/iterations/009/resumption-20261009/source/',
 'D012':'runs/y1-reader-20261008/iterations/012/current-r18/source/',
 'D013':'runs/y1-reader-20261008/iterations/013/current-r19/source/',
 'D015':'runs/y1-reader-20261008/iterations/015/current-r21/source/'}
for case,pref in sources.items():
 dest=out/case/'originals'; dest.mkdir(parents=True,exist_ok=True)
 for path,blob in tree.items():
  if not path.startswith(pref) or not (path.endswith('.pdf') or path.endswith('.png')): continue
  data=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',blob])
  target=dest/Path(path).name; target.write_bytes(data)
  result['source_files'].append({'case':case,'git_path':path,'blob':blob,'path':str(target),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
archive='runs/y1-reader-20261008/iterations/007/published-r29-20261011/review/root/archives/d007-r29-root-review-20261011.zip'
blob=tree[archive]; data=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',blob])
z=zipfile.ZipFile(io.BytesIO(data))
result['d007_archive']={'path':archive,'blob':blob,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'source_candidates':[n for n in z.namelist() if any(w in n.lower() for w in ['source','input','lec7']) and n.endswith(('.pdf','.png','.json'))]}
(out/'d007-archive-members.txt').write_text('\n'.join(z.namelist()),encoding='utf-8')
(out/'input-identity-record.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('Current HEAD',pin,'queue SHA256',result['queue_sha256'])
print('Accepted Markdown identities',len(result['accepted_teaching']),'all match current HEAD and frozen identities')
print('Source files retrieved',len(result['source_files']))
print(json.dumps(result['d007_archive'],indent=2))
