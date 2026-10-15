"""Orchestrator-only synthetic metadata inspection, mutation preservation, audits."""
import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNTIME = ROOT / "runtime"
ALLOWED = {"operational_adapter.js", "fixed_launcher.py", "record_receipt.py", "verify_reuse.py", "frozen-route.json", "bootstrap.js", "short_call.js", "reader-operating.md", "seal-core.json", "invoker_template.js", "invoker.js"}


def snapshot():
    state = json.loads((RUNTIME / "state.json").read_text(encoding="utf-8")) if (RUNTIME / "state.json").exists() else None
    events = [json.loads(s) for s in (RUNTIME / "access.jsonl").read_text(encoding="utf-8").splitlines()] if (RUNTIME / "access.jsonl").exists() else []
    return {"state": state, "subject_open_audit_count": sum(e["event"] == "python_subject_open_audit" for e in events),
            "verified_access_count": sum(e["event"] == "verified_access_receipt" for e in events), "event_count": len(events), "events": events}


def main():
    mode = sys.argv[1]
    if mode == "snapshot":
        assert len(sys.argv) == 2
        print(json.dumps(snapshot(), separators=(",", ":")))
    elif mode in ("mutate", "restore"):
        assert len(sys.argv) == 3 and sys.argv[2] in ALLOWED
        name = sys.argv[2]
        folder = ROOT / "failure-records" / ("disk-" + name.replace(".", "-"))
        folder.mkdir(parents=True, exist_ok=True)
        target = ROOT / name
        original = folder / "original.bytes"
        corrupted = folder / "corrupted.bytes"
        if mode == "mutate":
            assert not original.exists(), "Preserve prior probe; do not rerun under same name"
            data = target.read_bytes()
            original.write_bytes(data)
            bad = data + b"\n "
            if name == "operational_adapter.js":
                needle = b"0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee"
                replacement = b"0x2748774c,0x34b0bcb5,0x682e6ff3,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x748f82ee"
                assert data.count(needle) == 1
                bad = data.replace(needle, replacement, 1)
            corrupted.write_bytes(bad)
            target.write_bytes(bad)
            (folder / "mutation.json").write_text(json.dumps({"file": name, "original_sha256": hashlib.sha256(data).hexdigest(), "corrupted_sha256": hashlib.sha256(bad).hexdigest(), "condition": "independent synthetic mutation, not original departed reader call"}, indent=2), encoding="utf-8")
        else:
            assert original.exists() and corrupted.exists()
            target.write_bytes(original.read_bytes())
        print(json.dumps({"mode": mode, "name": name, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}))
    elif mode == "archive-runtime":
        assert len(sys.argv) == 3 and sys.argv[2] in ("successful-runtime", "launcher-truncation-runtime")
        dest = ROOT / sys.argv[2]
        assert RUNTIME.resolve().parent == ROOT.resolve() and dest.resolve().parent == ROOT.resolve() and not dest.exists()
        RUNTIME.rename(dest)
        print(json.dumps({"preserved": str(dest)}))
    elif mode == "restore-success-runtime":
        assert len(sys.argv) == 2 and not RUNTIME.exists()
        src = ROOT / "successful-runtime"
        assert src.resolve().parent == ROOT.resolve()
        src.rename(RUNTIME)
        print(json.dumps({"restored_synthetic_success_runtime": True}))
    else:
        raise ValueError("unpermitted support command")


if __name__ == "__main__":
    main()
