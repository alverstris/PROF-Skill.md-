"""Synthetic preflight metadata snapshot, no content-file access."""
import json
import sys
from pathlib import Path

if len(sys.argv) != 1:
    raise SystemExit("no arguments accepted")
ROOT = Path(__file__).resolve().parent
runtime = ROOT / "synthetic-runtime"
state = json.loads((runtime / "state.json").read_text(encoding="utf-8")) if (runtime / "state.json").exists() else None
events = [json.loads(line) for line in (runtime / "access.jsonl").read_text(encoding="utf-8").splitlines()] if (runtime / "access.jsonl").exists() else []
print(json.dumps({"state": state, "subject_open_audit_count": sum(e["event"] == "python_subject_open_audit" for e in events),
                  "verified_access_count": sum(e["event"] == "verified_access_receipt" for e in events),
                  "event_count": len(events), "events": [e["event"] for e in events]}))
