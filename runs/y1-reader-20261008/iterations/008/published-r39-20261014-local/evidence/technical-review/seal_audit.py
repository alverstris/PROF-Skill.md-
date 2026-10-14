from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

r=Path(__file__).resolve().parent
names=['full-audit.md','audit-RECOVERY.txt','audit-access-log.jsonl','audit-final-check-record.txt','audit_checks.py','audit-check-results.json','source-math-inventory.json','source-slope-crop.png','prompt-first-attempts.md','prompt-first-seal.json']
files=[{'path':n,'bytes':(r/n).stat().st_size,'sha256':hashlib.sha256((r/n).read_bytes()).hexdigest()} for n in names]
result={'stage':'complete original independent technical/source audit',
        'frozen_utc':datetime.now(timezone.utc).isoformat(),
        'teaching_revision':'d008-r39-first-delivery',
        'read_scope':'main1-532; hints1-64; solutions1-221; four full figure PNGs; prompt-first A-F sealed before help',
        'findings':['I01','I02','C01'],
        'destination_verification':'root-owned, not performed by this reviewer','files':files}
(r/'audit-manifest.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'manifest':str(r/'audit-manifest.json'),'report':str(r/'full-audit.md'),'frozen_utc':result['frozen_utc'],'files':len(files)}))
