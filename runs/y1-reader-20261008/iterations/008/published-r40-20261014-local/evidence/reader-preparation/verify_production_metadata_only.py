"""Prove bound identities/route metadata without subject access or runtime change."""
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path

PREP=Path(__file__).resolve().parent
ROOT=PREP.parent/"reader-inputs"
route=json.loads((ROOT/"frozen-route.json").read_text())
subjects={os.path.normcase(os.path.abspath(s["path"])) for s in route["files"].values()}
events=[]
def hook(event,args):
    if event=="open" and isinstance(args[0],(str,bytes,os.PathLike)):
        path=os.path.normcase(os.path.abspath(os.fsdecode(args[0])))
        events.append({"event":"open","path":path,"mode":str(args[1]),"subject_path":path in subjects})
        if path in subjects:raise AssertionError("Metadata proof attempted subject access")
sys.addaudithook(hook)
before=(ROOT/"runtime").exists()
spec=importlib.util.spec_from_file_location("production_verified_metadata",ROOT/"verify_reuse.py")
verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)
digest=hashlib.sha256((ROOT/"seal-core.json").read_bytes()).hexdigest()
p=verify.proof("bootstrap",digest)
after=(ROOT/"runtime").exists()
assert not before and not after and not any(e["subject_path"] for e in events)
result={"metadata_only_binding_verification_passed":True,"exact_bootstrap_short_call_instruction_code_and_route_identity":True,"subject_file_opens":0,"production_launcher_main_invoked":False,"production_runtime_before":before,"production_runtime_after":after,"reader_dispatched":False,"core_sha256":digest,"bootstrap_sha256":p["seal"]["bootstrap_sha256"],"short_call_sha256":p["seal"]["short_call_sha256"],"open_events":events,"audit_scope":"Python opens during metadata verifier import/proof only; subject opens explicitly blocked; not OS-wide isolation"}
(PREP/"production-metadata-verification.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="open_events"}))
