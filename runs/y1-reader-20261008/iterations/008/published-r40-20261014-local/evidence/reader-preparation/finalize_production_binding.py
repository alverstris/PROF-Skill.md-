"""Finalize identities, routing evidence and synthetic results; no production launch."""
import hashlib
import json
import re
import shutil
from pathlib import Path

PREP=Path(__file__).resolve().parent
OUT=PREP.parent/"reader-inputs"
SYNTH=PREP/"synthetic-preflight-r40"
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text(encoding="utf-8-sig"))
def save(p,x):p.write_text(json.dumps(x,indent=2)+"\n",encoding="utf-8")
route=read(OUT/"frozen-route.json")
binding=read(OUT/"binding-validation.json")
metadata=read(PREP/"production-metadata-verification.json")
negative=read(SYNTH/"negative-preflight-evidence.json")
figure=read(SYNTH/"figure-preflight-evidence.json")
trunc=read(SYNTH/"launcher-truncation-evidence.json")
supplement=read(SYNTH/"rejection-supplement.json")
audit=read(SYNTH/"whole-route-audit.json")
assert metadata["subject_file_opens"]==0 and not metadata["production_runtime_after"]
assert negative["negative_checks_passed"] and figure["figure_checks_passed"] and trunc["passed"] and audit["operational_route_audit_passed"]
assert all(x["passed"] for x in supplement["checks"]) and read(SYNTH/"undefined-store-evidence.json")["passed"]
def norm(s,kind):
    if kind=="launcher":return re.sub(r'^(CONFIG_PATH|EXPECTED_CONFIG_SHA256|RUNTIME_DIR) = .+$',r'\1 = <BOUND>',s,flags=re.M)
    if kind=="adapter":return re.sub(r'^const (PYTHON|LAUNCHER|RECEIPT|ROUTE_SHA256) = .+$',r'const \1 = <BOUND>',s,flags=re.M)
    if kind=="call":return re.sub(r'^const STEP_ID = "[^"\n]+";$','const STEP_ID = "<ID>";',s,flags=re.M)
    if kind=="verifier":
        for value in ("production instruction-confined D008 r40","synthetic non-subject r40 preflight"):s=s.replace(value,"<SCOPE>")
        for value in ("D008_R40_FROZEN_2102C1FC","SYNTHETIC_R40"):s=s.replace(value,"<ROUTE>")
        return s
    return s
equivalence=[]
for name,kind in (("fixed_launcher.py","launcher"),("operational_adapter.js","adapter"),("record_receipt.py","exact"),("audit_bound_run.py","exact"),("bootstrap_template.js","exact"),("short_call_template.js","call"),("verify_reuse.py","verifier")):
    a=(OUT/name).read_text(encoding="utf-8");b=(SYNTH/name).read_text(encoding="utf-8")
    assert norm(a,kind)==norm(b,kind),name
    equivalence.append({"file":name,"production_sha256":sha((OUT/name).read_bytes()),"synthetic_sha256":sha((SYNTH/name).read_bytes()),"logic_equal":True,"allowed_difference":kind})
main=(OUT/"subjects/teaching/main.md").read_bytes()
spans=[s for s in route["steps"] if s["file_id"]=="MAIN"]
anchors=list(re.finditer(rb'^<a id="main-d008-[^"]+"></a>\r?\n',main,re.M))
exercise=[]
for m in re.finditer(rb'^(?:Attempt A[1-4]:[^\r\n]*|Revisit R1)\r?\n',main,re.M):
    anchor=max(a.start() for a in anchors if a.start()<m.start())
    assert any(s["start"]==anchor for s in spans)
    assert not any(s["start"]<anchor<s["start"]+s["length"] for s in spans)
    exercise.append({"heading_line":main[:m.start()].count(b"\n")+1,"boundary_byte":anchor,"no_text_chunk_crosses_start":True})
assert len(exercise)==5
total=0
for fid,spec in route["files"].items():
    raw=Path(spec["path"]).read_bytes()
    assert len(raw)==spec["size"] and sha(raw)==spec["sha256"]
    total+=len(raw)
assert total==512898 and len(route["steps"])==77 and not (OUT/"runtime").exists()
summary={"state":"bound_synthetic_preflight_passed_root_review_pending","published_teaching_commit":route["revision"],"root_is_sole_publisher_and_acceptance_owner":True,
 "production_metadata_binding_passed":True,"metadata_proof_subject_opens":0,"production_launcher_invoked":False,"production_runtime_exists":False,"reader_dispatched":False,"substantive_admission":"not_admitted",
 "constituents":7,"total_exact_covered_bytes":total,"baseline_steps":45,"main_text_steps":17,"figure_steps":3,"hint_steps":6,"solution_steps":6,"total_scheduled_steps":77,"bounded_baseline_revisit_ids":45,"max_text_slice_bytes":max(s["length"] for s in route["steps"] if s["kind"]=="text"),
 "exercise_boundaries":exercise,"figures_at_first_use":[x for x in binding["structural_boundaries"] if x["kind"].startswith("complete_figure")],
 "synthetic_negative_checks":len(negative["negative_checks"]),"synthetic_supplemental_rejection_checks":len(supplement["checks"]),"synthetic_undefined_store_check":True,"synthetic_figure_stage_checks":len(figure["figure_checks"]),"synthetic_actual_launcher_truncation_failure_preserved":True,"synthetic_whole_route_audit":True,"synthetic_verified_accesses":len(audit["verified_accesses"]),
 "same_program_equivalence":equivalence,"core_sha256":binding["core_sha256"],"route_sha256":sha((OUT/"frozen-route.json").read_bytes()),"bootstrap_sha256":sha((OUT/"bootstrap.js").read_bytes()),"short_call_sha256":sha((OUT/"short_call.js").read_bytes()),"operating_instruction_sha256":sha((OUT/"reader-operating.md").read_bytes()),"launch_message_sha256":sha((OUT/"reader-launch-message.txt").read_bytes()),"launch_message_bytes":(OUT/"reader-launch-message.txt").stat().st_size,
 "subject_free_route_delivery":"complete inline JSON in exact launch message; no arbitrary metadata-read command", "preparation_read_scope":"Frozen subject data for identity/copy/chronological routing only; no SASIS report or teaching diagnosis", "limits":"Instruction confinement only; no technical sandbox, semantic admission or memory-erasure claim. Synthetic fixture views do not establish actual production figure access."}
save(PREP/"production-binding-summary.json",summary)
shutil.copyfile(OUT/"binding-validation.json",OUT/"binding-validation-before-synthetic-preflight.json")
binding["state"]=summary["state"];binding["synthetic_preflight_summary"]={k:summary[k] for k in summary if k.startswith("synthetic_")};binding["exercise_boundary_validation"]=exercise
save(OUT/"binding-validation.json",binding)
shutil.copyfile(PREP/"binding-state.json",PREP/"binding-state-before-freeze.json")
state=read(PREP/"binding-state.json")
state.update({"state":summary["state"],"frozen_baseline_identity":route["files"]["BASELINE"],"frozen_teaching_identity":{"revision":route["revision"],"constituents":6},"frozen_route_identity":{"id":route["route_id"],"sha256":summary["route_sha256"]},"route_step_ids":[s["id"] for s in route["steps"]],"bound_input_directory":str(OUT),"fixed_python":read(OUT/"seal-core.json")["python"],"store_key":read(OUT/"seal-core.json")["store_key"],"seal_core_identity":summary["core_sha256"],"bootstrap_identity":summary["bootstrap_sha256"],"short_call_identity":summary["short_call_sha256"],"runtime_identity":{"path":str(OUT/"runtime"),"exists":False},"production_bound_preflight":"passed separate synthetic same-program binding; production metadata-only proof passed","next_owner_action":"Root reviews exact bound launch message/route/identities and decides fresh reader dispatch; full access/admission audit remains pending."})
save(PREP/"binding-state.json",state)
shutil.copyfile(PREP/"INVENTORY.json",PREP/"INVENTORY-before-production-binding.json")
for folder,filename in ((OUT,"binding-inventory.json"),(PREP,"INVENTORY.json")):
    save(folder/filename,{"files":{str(p.relative_to(folder)).replace("\\","/"):{"bytes":p.stat().st_size,"sha256":sha(p.read_bytes())} for p in folder.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.name!=filename},"scope":"Production metadata and preserved separate synthetic evidence; no actual reader admission"})
print(json.dumps({k:summary[k] for k in ("state","total_exact_covered_bytes","total_scheduled_steps","core_sha256","route_sha256","bootstrap_sha256","short_call_sha256","launch_message_sha256","production_runtime_exists")},indent=2))
