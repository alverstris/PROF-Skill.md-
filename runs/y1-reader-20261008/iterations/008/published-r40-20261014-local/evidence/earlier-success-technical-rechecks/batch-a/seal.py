from pathlib import Path
import json,hashlib,subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
skill=Path('C:/Users/alver/.codex/skills/prof')
rules=[]
for rel in ['SKILL.md','references/execution-protocol.md','references/domain-patterns.md']:
 p=skill/rel
 rules.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read_scope':'complete SKILL.md; complete relevant execution content; mathematics/physics domain content, other domain text also retrieved'})
ids=json.loads((HERE/'identities.json').read_text(encoding='utf-8'))
ids['authoritative_main_binding']={'commit':'2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce','method':'parent independently verified all14 accepted Markdown blobs with ls-tree/cat-file at this commit; this worker independently verified accepted-copy hashes against r39 inventory','parent_evidence':'../current-main-identity-check.json','sparse_older_head':'f23c4a7e52743d48ff2bfef1892b44ed57575a54','sparse_older_head_status':'supplemental older comparison only'}
ids['rules_read']=rules
ids['new_independent_visual_scope']={'D003':[2,3,4,5],'D005':[2,3,4,5],'D006':[2,3,4,5,6,7,8],'cover_page_pixels':'not inspected; parsed for packet identities/counts'}
(HERE/'identities.json').write_text(json.dumps(ids,indent=2),encoding='utf-8')
queue=json.loads((ROOT/'.prof-sasis/20261014-d008-r40/run-state/queue.json').read_text(encoding='utf-8'))
assert ids['queue_sha256']==sha(ROOT/'.prof-sasis/20261014-d008-r40/run-state/queue.json')
for c in ids['cases']:
 assert c['actual_teaching_sha256']==sha(Path(c['accepted_copy']))
 assert c['original_sha256']==sha(Path(c['original_pdf']))
 for item in c['rendered_pages']+c['additional_rendered_pages']+c['crops']:
  assert item['sha256']==sha(Path(item['path']))
files=[]
for p in sorted(HERE.rglob('*')):
 if p.is_file() and p.name!='evidence-manifest.json':
  files.append({'path':str(p.relative_to(HERE)),'bytes':p.stat().st_size,'sha256':sha(p)})
(HERE/'evidence-manifest.json').write_text(json.dumps({'scope':'bounded technical rechecks D003,D005,D006; source attributions and final numerical validations','established_defects':[],'unverified_attributions':[],'rounded_values_checked':7,'rounded_values_passed':7,'files':files},indent=2),encoding='utf-8')
print(json.dumps({'report_sha256':sha(HERE/'REPORT.md'),'exact_witnesses_sha256':sha(HERE/'exact-validation-witnesses.md'),'numeric_sha256':sha(HERE/'numeric-final-value-witnesses.json'),'manifest_sha256':sha(HERE/'evidence-manifest.json'),'file_count':len(files),'line_counts':{c['material_id']:len(Path(c['accepted_copy']).read_text(encoding='utf-8').splitlines()) for c in ids['cases']}},indent=2))
