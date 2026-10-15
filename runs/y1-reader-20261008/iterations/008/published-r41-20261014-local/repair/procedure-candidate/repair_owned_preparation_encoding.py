"""Repair only owned, unpublished candidate preparation's Windows UTF-8 reads."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
p=R/"adopt_existing_reference_carrier.py"
s=p.read_text(encoding="utf-8")
s=s.replace("assert not T.exists();T.mkdir()","T.mkdir(exist_ok=True)")
s=s.replace("for p in old.iterdir():","for p in list(old.iterdir()) if old.exists() else []:")
s=s.replace("old.rmdir()","if old.exists():old.rmdir()")
s=s.replace(".read_text()",'.read_text(encoding="utf-8")')
p.write_text(s,encoding="utf-8")
p=R/"build_candidate.py"
p.write_text(p.read_text(encoding="utf-8").replace(".read_text()",'.read_text(encoding="utf-8")'),encoding="utf-8")
record={"scope":"Owned unpublished candidate preparation only","failures":["UnicodeDecodeError from Windows default cp1252 reading UTF-8 sasis.md","Attempted shell-quoted repair command rejected by Python parser before running; no file changes","Repeated adoption refused because templates had already moved"],"before_control_changes":True,"templates_moved_with_byte_identity_verified":True,"repair":"Explicit UTF-8 reads and resumable owned template move","old_source_or_installed_mutation":False}
(R/"failure-evidence/carrier-preparation-encoding-failure.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
