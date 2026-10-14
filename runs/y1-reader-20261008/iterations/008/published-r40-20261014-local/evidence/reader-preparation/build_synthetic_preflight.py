"""Bind only separate non-subject fixtures to the same reviewed operational code."""
import hashlib
import importlib.util
import json
import shutil
from pathlib import Path

PREP=Path(__file__).resolve().parent
PROJECT=PREP.parents[2]
OLD=PROJECT/".prof-sasis/20261014-d008-r39/reader-reuse-candidate"
INFRA=PROJECT/".prof-sasis/20261014-d008-r39/reader-infrastructure"
ROOT=PREP/"synthetic-preflight-r40"
KEY="prof.reader.d008.r40.synthetic.preflight1"
assert not ROOT.exists(), "Preserve previous synthetic preflight"
ROOT.mkdir()
for n in ("bind_synthetic.py","launcher_template.py","receipt_template.py","adapter_template.js"):
    shutil.copyfile(INFRA/n,ROOT/n)
spec=importlib.util.spec_from_file_location("fresh_synthetic_fixture",ROOT/"bind_synthetic.py")
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
route=builder.build();route["route_id"]="SYNTHETIC_R40"
spec=importlib.util.spec_from_file_location("production_binding_functions_only",PREP/"bind_production.py")
binder=importlib.util.module_from_spec(spec);spec.loader.exec_module(binder)
instruction="Synthetic r40 wrapper preflight only. This non-subject bootstrap is explicitly authorised once and retrieves no fixture bytes. Subsequent calls change STEP_ID only, never operational code. Preserve failures. No real reader or subject binding is exercised. Core __CORE_SHA256__; store __STORE_KEY__.\n"
core,digest,proof=binder.seal(ROOT,route,instruction,KEY,"synthetic non-subject r40 preflight","B001")
oldroot=str(OLD).replace("\\","/")
for n in ("preflight_support.py","actual_negative_preflight.js","actual_figure_preflight.js","actual_launcher_truncation_preflight.js","audit_verification_opens.py"):
    text=(OLD/n).read_text(encoding="utf-8").replace(oldroot,str(ROOT).replace("\\","/")).replace("prof.reader.reuse.synthetic.r40.candidate1",KEY).replace("synthetic-runtime","runtime").replace("synthetic-route.json","frozen-route.json")
    (ROOT/n).write_text(text,encoding="utf-8",newline="\n")
binder.save(ROOT/"synthetic-binding.json",{"core_sha256":digest,"key":KEY,"same_operational_logic_as_production":True,"production_runtime_exists":(binder.OUT/"runtime").exists(),"proof_seal":{k:v for k,v in proof["seal"].items() if k!="adapter_source"}})
print(json.dumps({"root":str(ROOT),"core_sha256":digest,"bootstrap_sha256":proof["seal"]["bootstrap_sha256"],"short_call_sha256":proof["seal"]["short_call_sha256"],"synthetic_only":True,"production_runtime_exists":(binder.OUT/"runtime").exists()}))
