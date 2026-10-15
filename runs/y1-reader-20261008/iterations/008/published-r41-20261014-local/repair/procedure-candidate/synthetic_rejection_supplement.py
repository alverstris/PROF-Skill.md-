"""Separate synthetic fresh-runtime rejection probes; preserve success and failures."""
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent/"synthetic-preflight"
RUNTIME=ROOT/"runtime"
success=ROOT/"success-before-rejection-supplement"
failed=ROOT/"unread-and-shape-rejection-runtime"
assert RUNTIME.resolve().parent==ROOT.resolve() and not success.exists() and not failed.exists()
RUNTIME.rename(success)
results=[]
try:
    for name,args in (("unread_baseline_revisit",["RB002"]),("extra_subject_path_argument",["B001","C:/synthetic-unpermitted.txt"]),("premature_teaching",["T001"]),("skipped_initial_baseline",["B002"]),("missing_argument",[])):
        proc=subprocess.run([sys.executable,str(ROOT/"fixed_launcher.py"),*args],capture_output=True)
        events=[json.loads(x) for x in (RUNTIME/"access.jsonl").read_text().splitlines()] if (RUNTIME/"access.jsonl").exists() else []
        opens=sum(e["event"]=="python_subject_open_audit" for e in events)
        assert proc.returncode!=0 and not proc.stdout and opens==0 and not (RUNTIME/"state.json").exists()
        results.append({"name":name,"passed":True,"arguments":args,"exit_code":proc.returncode,"stderr":proc.stderr.decode(),"fixture_opens":0,"state_created":False})
finally:
    assert RUNTIME.resolve().parent==ROOT.resolve()
    if RUNTIME.exists():RUNTIME.rename(failed)
    assert not RUNTIME.exists()
    success.rename(RUNTIME)
(ROOT/"rejection-supplement.json").write_text(json.dumps({"synthetic_only":True,"checks":results,"failed_runtime_preserved":str(failed),"production_access":False},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"supplemental_checks":len(results),"all_passed":all(x["passed"] for x in results),"production_access":False}))

