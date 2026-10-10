"""Replay the scoped audit identities using a checkout with complete history."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

evidence = Path(__file__).resolve().parent
repo = Path(sys.argv[1])
records = []
for ledger in ("earlier-figure-scope.json", "earlier-figure-identities.json"):
    for entry in json.loads((evidence / ledger).read_text()):
        locator = entry["accepted_commit"] + ":" + entry["path"]
        blob = subprocess.check_output(
            ["git", "rev-parse", locator], cwd=repo, text=True
        ).strip()
        raw = subprocess.check_output(["git", "show", locator], cwd=repo)
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == entry["sha256"], locator
        records.append({
            "ledger": ledger,
            "locator": locator,
            "git_blob_sha": blob,
            "bytes": len(raw),
            "sha256": digest,
            "matches": True,
        })
json.dump({"method": "git show FULL_COMMIT:EXACT_PATH; no path mapping",
           "records": records, "verified": len(records)}, sys.stdout, indent=2)
print()
