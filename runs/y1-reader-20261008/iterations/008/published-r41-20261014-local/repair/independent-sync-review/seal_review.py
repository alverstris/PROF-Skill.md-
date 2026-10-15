"""Seal finalized bounded-review outputs; no owner evidence is mutated."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
owner = root.parent / "local-sync-preparation"
expected = "cb0c8b31a3d857edc3d8ed47f79afea61d7b3a752061c14f94f76a888b86b5f0"
assert hashlib.sha256((owner / "sync_published_prof.py").read_bytes()).hexdigest() == expected
assert (root / "independent-fixture-check/REPORT.md").is_file()
assert not (root / "review-freeze.json").exists()
identities = []
for path in sorted(root.rglob("*")):
    if path.is_file():
        raw = path.read_bytes()
        identities.append({"path": path.relative_to(root).as_posix(), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
record = {"schema": "prof-independent-sync-review-freeze-v1", "helper": {"path": str(owner / "sync_published_prof.py"), "bytes": 30691, "sha256": expected}, "report": "REPORT.md", "disposition": "No material defect established in the bounded final helper review; actual publication/stage/install/readback remain root obligations", "production_stage_install_or_network_invoked": False, "candidate_or_owner_evidence_modified": False, "files": identities}
raw = (json.dumps(record, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
(root / "review-freeze.json").write_bytes(raw)
print(json.dumps({"review_files": len(identities), "review_bytes": sum(e["bytes"] for e in identities), "freeze_bytes": len(raw), "freeze_sha256": hashlib.sha256(raw).hexdigest(), "report": next(e for e in identities if e["path"] == "REPORT.md")}))
