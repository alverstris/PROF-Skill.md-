"""Read-only metadata proof with synthetic fixture opens explicitly denied."""
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path

R = Path(__file__).resolve().parent
S = R / "synthetic-preflight"
route = json.loads((S / "frozen-route.json").read_text(encoding="utf-8"))
forbidden = {os.path.normcase(os.path.abspath(x["path"])) for x in route["files"].values()}
digest = hashlib.sha256((S / "seal-core.json").read_bytes()).hexdigest()
state_path = S / "runtime/state.json"
state_before = hashlib.sha256(state_path.read_bytes()).hexdigest()
opens = []
blocked = []

def audit(event, args):
    if event != "open" or not isinstance(args[0], (str, bytes, os.PathLike)):
        return
    path = os.path.normcase(os.path.abspath(os.fsdecode(args[0])))
    if path in forbidden:
        blocked.append(path)
        raise RuntimeError("Fixture subject open forbidden during metadata proof")
    if path.startswith(os.path.normcase(str(S)) + os.sep):
        opens.append({"path": path, "mode": str(args[1])})

sys.addaudithook(audit)
spec = importlib.util.spec_from_file_location("subject_free_proof", S / "verify_reuse.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
proof = module.proof("bootstrap", digest)
assert proof["schema"] == "prof-reader-reuse-proof-v1"
assert len(forbidden) == 3 and not blocked
state_after = hashlib.sha256(state_path.read_bytes()).hexdigest()
assert state_before == state_after
record = {
    "scope": "Synthetic metadata/bootstrap proof only; no production input or runtime access",
    "passed": True,
    "fixture_subject_paths_denied": sorted(forbidden),
    "fixture_subject_open_attempts": blocked,
    "fixture_subject_opens": 0,
    "metadata_or_operational_file_opens": opens,
    "synthetic_runtime_state_sha256_before": state_before,
    "synthetic_runtime_state_sha256_after": state_after,
    "canonical_invoker_sha256": proof["seal"]["invoker_sha256"],
    "limits": "This audit verifies metadata proof file access in this run. It is not process isolation or a reader security boundary."
}
(R / "metadata-subject-free-verification.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "fixture_subject_opens": 0, "runtime_state_unchanged": True, "operational_metadata_open_events": len(opens)}))
