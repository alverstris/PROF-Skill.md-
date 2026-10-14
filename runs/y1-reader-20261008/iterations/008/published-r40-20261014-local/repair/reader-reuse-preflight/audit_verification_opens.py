"""External Python-open instrumentation of exact sealed verifier, no fixture read.

Separate corroboration of metadata-only verifier behavior. Actual runtime calls
are in functions.exec transcript; this hook is not OS-wide monitoring.
"""
import json
import os
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
target = ROOT / "verification-open-audit.jsonl"
assert not target.exists(), "Preserve prior evidence"
handle = target.open("wb")


def hook(event, args):
    if event == "open" and isinstance(args[0], (str, bytes, os.PathLike)):
        path = os.path.normcase(os.path.abspath(os.fsdecode(args[0])))
        handle.write((json.dumps({"event": event, "path": path, "mode": str(args[1]), "flags": args[2]}) + "\n").encode())
        handle.flush()


sys.addaudithook(hook)
digest = __import__("hashlib").sha256((ROOT / "seal-core.json").read_bytes()).hexdigest()
sys.argv = [str(ROOT / "verify_reuse.py"), "bootstrap", digest]
try:
    runpy.run_path(str(ROOT / "verify_reuse.py"), run_name="__main__")
finally:
    handle.flush()
    handle.close()
