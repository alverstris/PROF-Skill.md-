from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent
rows=[]
for p in sorted(root.rglob('*')):
 if not p.is_file() or p==root/'review-freeze.json' or 'runtime' in p.relative_to(root).parts:continue
 b=p.read_bytes();rows.append({'file':p.relative_to(root).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
q=root.parents[2]/'.prof-sasis/20261014-d008-r40/run-state/queue.json'
queue=json.loads(q.read_text(encoding='utf-8-sig'))
source_hash=hashlib.sha256(q.read_bytes()).hexdigest()
stats={s:sum(x['status']==s for x in queue['sessions']) for s in set(x['status'] for x in queue['sessions'])}
d008=root.parent/'technical-review/review-freeze.json'
previous=json.loads(d008.read_text(encoding='utf-8'))
for item in previous['files']:
 b=(d008.parent/item['file']).read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256']
result={'scope':'Targeted source-attribution and final-value rechecks only: D003,D005,D006,D007,D009,D012,D013,D015','prof_version':'2026-10-14-r40','authoritative_current_main':'2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce','all14_accepted_markdown_constituents_match':True,'queue_sha256':source_hash,'actual_queue_status_counts':stats,'established_material_defects':[],'unresolved_original_access_limits':[],'sealed_d008_evidence_all_unchanged':True,'remaining_checks':'Root-owned actual GitHub rendering/styling/click/first-use checks and acceptance; no new SASIS, full earlier-teaching T1-T12 route audit, portability or human outcome claimed','manifest_exclusion':'Task-local runtime packages, pip cache and installation temporary files are excluded from the evidence file census; their confinement/module origin and version are recorded separately','files':rows}
(root/'review-freeze.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('Evidence files sealed',len(rows),'queue status counts',stats,'D008 unchanged')
print('Report SHA256',hashlib.sha256((root/'REPORT.md').read_bytes()).hexdigest())
print('Freeze SHA256',hashlib.sha256((root/'review-freeze.json').read_bytes()).hexdigest())
