from pathlib import Path
import subprocess,json,hashlib
out=Path(__file__).resolve().parent
base=out.parents[2]
repo=base/'.prof-maintenance/20261014/repository'
pin='2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce'
prior=json.loads((out/'input-identity-record.json').read_text(encoding='utf-8'))
tree={}
for row in subprocess.check_output(['git','-C',str(repo),'ls-tree','-rz',pin]).split(b'\0'):
 if row:
  meta,path=row.split(b'\t',1);tree[path.decode()]=meta.decode().split()[2]
inv=json.loads((base/'.prof-sasis/20261014-d008-r39/earlier-success-review/accepted-teaching-exposure-inventory.json').read_text(encoding='utf-8'))
rows=[]
for rec in prior['accepted_teaching']:
 art=next(a for c in inv['cases'] if c['material_id']==rec['case'] for a in c['artifacts'] if a['sha256']==rec['sha256'])
 blob=tree[art['path']]
 b=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',blob]);local=Path(rec['copy']).read_bytes()
 assert b==local and hashlib.sha256(b).hexdigest()==rec['sha256']
 rows.append({'case':rec['case'],'git_path':art['path'],'blob':blob,'bytes':len(b),'sha256':rec['sha256'],'matches_current_main':True,'matches_exact_accepted_identity':True,'frozen_commit':rec['frozen_commit']})
source_rows=[]
for src in prior['source_files']:
 blob=tree[src['git_path']]
 b=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',blob])
 assert b==Path(src['path']).read_bytes() and hashlib.sha256(b).hexdigest()==src['sha256']
 source_rows.append({'case':src['case'],'git_path':src['git_path'],'blob':blob,'sha256':src['sha256'],'matches_current_main':True})
result={'authoritative_current_main':pin,'root_supplied_current_main_identity':True,'read_only_local_object_comparison':True,'prior_sparse_checkout_head':prior['read_only_repository_head'],'prior_comparison_role':'Supplemental older sparse-checkout comparison, not current GitHub main','queue_sha256':prior['queue_sha256'],'accepted_markdown_count':len(rows),'accepted_markdown':rows,'all_match':True,'existing_original_source_constituents':source_rows}
(out/'current-main-identity-check.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
