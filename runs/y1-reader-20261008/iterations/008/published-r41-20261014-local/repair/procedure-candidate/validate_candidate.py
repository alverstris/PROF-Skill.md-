"""Validate merged package hashes/template extraction and same-interface synthetic evidence."""
import ast
import hashlib
import importlib.util
import json
import posixpath
import re
import subprocess
from pathlib import Path

R=Path(__file__).resolve().parent
PROJECT=R.parents[2]
REPO=PROJECT/".prof-maintenance/20261014/repository"
P=R/"proposed-package"
T=R/"templates"
S=R/"synthetic-preflight"
COMMIT="2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce"
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(["git","-C",str(REPO),*a])
def read(p):return json.loads(p.read_text(encoding="utf-8-sig"))
def save(p,x):p.write_text(json.dumps(x,indent=2)+"\n",encoding="utf-8")

tree={}
for entry in filter(None,git("ls-tree","-rz",COMMIT).split(b"\0")):
    meta,path=entry.split(b"\t",1);path=path.decode();oid=meta.decode().split()[2]
    if path=="SKILL.md" or path.split("/")[0] in {"agents","assets","references","scripts"}:tree[path]=oid
assert len(tree)==36
proposed={p.relative_to(P).as_posix():p.read_bytes() for p in P.rglob("*") if p.is_file()}
assert set(proposed)<=set(tree) and len(proposed)==5
merged={path:proposed.get(path,git("cat-file","blob",oid)) for path,oid in tree.items()}
source_profile=json.loads(git("show",COMMIT+":references/sasis/profile-manifest.json"))
profile=json.loads(merged["references/sasis/profile-manifest.json"])
revision_fields={"control_file_hashes","protocol_revision","protocol_update_notes"}
assert {k:v for k,v in profile.items() if k not in revision_fields}=={k:v for k,v in source_profile.items() if k not in revision_fields}
assert profile["protocol_revision"]=="2026-10-14-r41"
assert profile["protocol_update_notes"][:-1]==source_profile["protocol_update_notes"]
assert len(profile["protocol_update_notes"])==len(source_profile["protocol_update_notes"])+1
assert profile["protocol_update_notes"][-1].startswith("2026-10-14-r41 repairs the verified r40 reader failure at B0024:")
assert profile["file_hashes"]==source_profile["file_hashes"] and len(profile["file_hashes"])==19
assert profile["subject_files"]==source_profile["subject_files"]
checks=[]
base="references/sasis"
for name,h in profile["file_hashes"].items():checks.append((posixpath.normpath(base+"/"+profile["file_hashes_base_directory"]+"/"+name),h))
for name,h in profile["control_file_hashes"].items():checks.append((posixpath.normpath(base+"/"+name),h))
for e in profile["subject_files"]:checks.append((posixpath.normpath(base+"/"+e["path"]),e["sha256"]))
for name,h in checks:assert sha(merged[name])==h,name
assert len(checks)==28
carrier=merged["references/sasis.md"].decode()
assert "Protocol revision: 2026-10-14-r41." in carrier
extracted=R/"verified-extracted-templates";extracted.mkdir(exist_ok=True)
template_checks=[]
for p in T.iterdir():
    pattern=r'<!-- PROF-READER-TEMPLATE-BEGIN: '+re.escape(p.name)+r' -->\n```(?:javascript|python)\n(.*?)```\n<!-- PROF-READER-TEMPLATE-END: '+re.escape(p.name)+r' -->'
    matches=re.findall(pattern,carrier,re.S);assert len(matches)==1
    raw=matches[0].encode();assert raw==p.read_bytes()
    if p.name=="verify_reuse_template.py":
        bound=raw.decode()
        for marker,value in {"__FIXED_ROUTE_FILENAME__":"frozen-route.json","__FIXED_RUNTIME_DIRNAME__":"runtime","__FIXED_SCOPE__":"synthetic r41 retained invoker","__FIXED_ROUTE_ID__":"SYNTHETIC_R41"}.items():bound=bound.replace(marker,value)
        assert bound.encode()==(S/"verify_reuse.py").read_bytes()
    else:assert raw==(S/p.name).read_bytes()
    (extracted/p.name).write_bytes(raw)
    template_checks.append({"name":p.name,"bytes":len(raw),"sha256":sha(raw),"exact_named_block_extraction":True,"same_template_used_in_actual_preflight":True})
ast.parse((T/"verify_reuse_template.py").read_text(encoding="utf-8"))
negative=read(S/"negative-preflight-evidence.json");figure=read(S/"figure-preflight-evidence.json")
audit=read(S/"whole-route-audit.json");trunc=read(S/"launcher-truncation-evidence.json")
supplement=read(S/"rejection-supplement.json");minimal=read(S/"minimal-surface-supplement.json")
cause=read(R/"failure-evidence/schema-copy-synthetic-reproduction.json")
metadata=read(R/"metadata-subject-free-verification.json")
assert metadata["passed"] and metadata["fixture_subject_opens"]==0 and not metadata["fixture_subject_open_attempts"]
assert metadata["synthetic_runtime_state_sha256_before"]==metadata["synthetic_runtime_state_sha256_after"]
assert negative["negative_checks_passed"] and len(negative["negative_checks"])==32
assert figure["figure_checks_passed"] and len(figure["figure_checks"])==4
assert audit["operational_route_audit_passed"] and len(audit["verified_accesses"])==7
assert trunc["passed"] and cause["passed"] and all(x["passed"] for x in supplement["checks"]+minimal["cases"])
core=read(S/"seal-core.json");digest=sha((S/"seal-core.json").read_bytes())
spec=importlib.util.spec_from_file_location("validated_retained_invoker",S/"verify_reuse.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
proof=m.proof("bootstrap",digest)
call=(S/"short_call.js").read_text(encoding="utf-8")
assert len(call.splitlines())==2 and not any(x in call for x in ("schema","JSON","proof","receipt","exec_command"))
state=read(S/"runtime/state.json");assert state["cursor"]==5 and state["pending_figure"] is None
old=PROJECT/".prof-sasis/20261014-d008-r40/reader-inputs"
def norm(s,kind):
    if kind=="launcher":return re.sub(r'^(CONFIG_PATH|EXPECTED_CONFIG_SHA256|RUNTIME_DIR) = .+$',r'\1 = <BOUND>',s,flags=re.M)
    if kind=="adapter":return re.sub(r'^const (PYTHON|LAUNCHER|RECEIPT|ROUTE_SHA256) = .+$',r'const \1 = <BOUND>',s,flags=re.M)
    return s
logic=[]
for name,kind in (("fixed_launcher.py","launcher"),("operational_adapter.js","adapter"),("record_receipt.py","exact"),("audit_bound_run.py","exact")):
    assert norm((S/name).read_text(encoding="utf-8"),kind)==norm((old/name).read_text(encoding="utf-8"),kind)
    logic.append({"file":name,"unchanged_except_fixed_bindings":True})
installed=Path("C:/Users/alver/.codex/skills/prof")
for name,oid in tree.items():assert (installed/name).read_bytes()==git("cat-file","blob",oid),"Installed source changed: "+name
result={"state":"r41_candidate_preflight_passed_unpublished_pending_root_review","source_commit":COMMIT,"proposed_version":"2026-10-14-r41","changed_existing_package_files":list(proposed),"package_inventory_unchanged":True,"complete_package_files_after_integration":36,"operative_manifest_checks":28,"frozen_baseline_profile_and_hashes_unchanged":True,"named_template_checks":template_checks,"same_interface_actual_functions_exec":True,"repeated_call_lines":2,"caller_contains_schema_or_identity_guard_logic":False,"synthetic_negative_checks":32,"synthetic_additional_shape_or_missing_store_checks":len(minimal["cases"]),"synthetic_unread_revisit_and_launcher_shape_checks":len(supplement["checks"]),"synthetic_figure_stage_checks":4,"synthetic_actual_view_events":len(figure["actual_tool_events"]),"synthetic_whole_route_verified_accesses":7,"synthetic_actual_truncation_failure_preserved":True,"exact_saved_r40_failure_reproduced_without_actual_tools":True,"launcher_adapter_receipt_audit_logic":logic,"core_sha256":digest,"invoker_sha256":proof["seal"]["invoker_sha256"],"bootstrap_sha256":proof["seal"]["bootstrap_sha256"],"call_sha256":proof["seal"]["short_call_sha256"],"evaluation_order":"Bootstrap independently verifies designated invoker source. Later minimal call evaluates that retained function expression, invokes it with one STEP_ID, then its fixed metadata helper proof/canonical retained source-envelope comparison precede subject launcher/view access. Nested adapter source executes only after current proof match.","limits":"No persistent callable exists. Current retained source is not authenticated before its expression evaluates. Tested accidental source/envelope mutations stop before subject access; deliberately hostile replacement expression is outside the instruction whitelist and is not technically confined.","installed_repository_old_reading_or_subjects_mutated":False,"production_runtime_access":False,"reader_dispatched":False,"teaching_generated":False,"publication_installation_or_acceptance_claimed":False,"mechanical_skill_validator":"Skill is valid!; existing quick_validate.py run with -B and existing validation-deps; no dependencies installed."}
save(R/"validation.json",result)
save(R/"proposed-file-identities.json",{"files":{n:{"bytes":len(b),"sha256":sha(b),"source_blob":tree[n]} for n,b in proposed.items()},"template_carrier":"references/sasis.md","template_checks":template_checks})
save(R/"manifest-validation.json",{"checks":[{"path":n,"expected_sha256":h,"actual_sha256":sha(merged[n]),"pass":True} for n,h in checks],"all_passed":True,"count":28,"merged_complete_package_files":36,"frozen_baseline_provenance_hash_count":19,"frozen_baseline_provenance_identities_unchanged":True,"subject_files_unchanged":True,"other_profile_fields_unchanged_except":["control_file_hashes","protocol_revision","protocol_update_notes"],"existing_protocol_notes_preserved":True,"new_r41_protocol_note_count":1})
print(json.dumps({k:result[k] for k in ("state","complete_package_files_after_integration","operative_manifest_checks","synthetic_negative_checks","synthetic_figure_stage_checks","invoker_sha256","bootstrap_sha256","call_sha256")},indent=2))
