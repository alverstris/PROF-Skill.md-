"""Read-only post-failure verification, then seal only this supplemental evidence."""
import hashlib
import importlib.util
import json
from pathlib import Path

R = Path(__file__).resolve().parent
C = R.parent / "procedure-candidate"

def sha(b): return hashlib.sha256(b).hexdigest()
def identity(p):
    b = p.read_bytes(); return {"bytes": len(b), "sha256": sha(b)}
def load(p): return json.loads(p.read_text(encoding="utf-8-sig"))
def save(p, x): p.write_text(json.dumps(x, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

before = load(R / "reviewed-candidate-before.json")["files"]
after = {p.relative_to(C).as_posix(): identity(p) for p in sorted(C.rglob("*")) if p.is_file()}
assert before == after, "Reviewed candidate changed"
save(R / "reviewed-candidate-unchanged.json", {"passed": True, "file_count": len(before), "inventory_and_all_bytes_unchanged": True, "differences": [], "review_seal_identity": after["REVIEW-SEAL.json"], "scope": str(C).replace("\\", "/")})

runtime = R / "runtime"
runtime_before = {p.relative_to(runtime).as_posix(): identity(p) for p in sorted(runtime.rglob("*")) if p.is_file()}
assert set(runtime_before) == {"access.jsonl"}, runtime_before
events = [json.loads(x) for x in (runtime / "access.jsonl").read_text(encoding="utf-8").splitlines()]
assert len(events) == 1
assert events[0]["event"] == "launcher_rejected" and events[0]["requested_step"] == "RB002"
assert events[0]["reason"] == "baseline revisit target not yet read" and events[0]["argument_count"] == 1
assert not (runtime / "state.json").exists()
call = (R / "unread-revisit-call.js").read_text(encoding="utf-8")
template_call = (R / "short_call.js").read_text(encoding="utf-8")
assert call == template_call.replace('const STEP_ID = "B001";', 'const STEP_ID = "RB002";')
assert len(call.splitlines()) == 2 and not any(x in call for x in ("schema", "JSON", "proof", "receipt", "exec_command"))
bootstrap_before = load(R / "after-bootstrap-before-call.json")
assert not any(bootstrap_before[k] for k in ("runtime_exists", "state_exists", "access_ledger_exists"))
assert bootstrap_before["effective_cursor"] == 0 and bootstrap_before["baseline_read"] == []
spec = importlib.util.spec_from_file_location("supplement_final_metadata_proof", R / "verify_reuse.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
digest = sha((R / "seal-core.json").read_bytes())
proof = m.proof("bootstrap", digest)
retained = load(R / "bootstrap-retained-envelope.json")
assert retained == proof["seal"]
assert load(R / "identity-normalized-comparison.json")["pass"]
error = (R / "actual-functions-exec-return.txt").read_text(encoding="utf-8")
assert 'baseline revisit target not yet read' in error and 'at async exec_main.mjs:2:1' in error
assert runtime_before == {p.relative_to(runtime).as_posix(): identity(p) for p in sorted(runtime.rglob("*")) if p.is_file()}

subject_events = {name: sum(x["event"] == name for x in events) for name in ("subject_open_attempt", "python_subject_open_audit", "subject_open_succeeded", "bounded_bytes_read", "verified_access_receipt", "launcher_output_prepared", "delivery_receipt", "figure_view_receipt")}
assert all(x == 0 for x in subject_events.values())
result = {"passed": True, "scope": "Supplemental exact two-line unread-baseline revisit on fresh non-subject fixture only", "actual_functions_exec_bootstrap": True, "bootstrap_executions": 1, "actual_functions_exec_minimal_call": True, "retrieval_invocations": 1, "exact_call": call, "requested_step": "RB002", "target_step": "B002", "target_unread_at_invocation": True, "failure": "launcher rejected/failed: {\"error\":\"baseline revisit target not yet read\",\"ok\":false}", "launcher_rejection_count": 1, "effective_cursor_before": 0, "effective_cursor_after": 0, "baseline_read_before": [], "baseline_read_after": [], "state_file_before": False, "state_file_after": False, "reader_access_event_counts": subject_events, "bootstrap_retained_envelope_matches_independent_canonical_proof": True, "reviewed_candidate_files_unchanged": len(before), "identity_normalized_code_comparison_passed": True, "failed_fixture_preserved_without_reset_or_retry": True, "post_failure_runtime_identity_unchanged": runtime_before, "core_sha256": digest, "bootstrap_sha256": sha((R / "bootstrap.js").read_bytes()), "invoker_sha256": sha((R / "invoker.js").read_bytes()), "exact_unread_call_sha256": sha(call.encode()), "no_operational_code_change": True, "production_subject_or_runtime_access": False, "reader_dispatch_teaching_generation_publication_installation": False, "limits": "The invoker expression evaluates before its current canonical check; this supplements instruction-confined execution evidence, not pre-evaluation authentication or technical confinement."}
save(R / "verification.json", result)

entries = []
for p in sorted(R.rglob("*")):
    if not p.is_file() or p.name in {"INVENTORY.json", "SUPPLEMENT-SEAL.json"}: continue
    raw = p.read_bytes()
    try: raw.decode("utf-8"); kind = "UTF-8"
    except UnicodeDecodeError: kind = "binary"
    entries.append({"path": p.relative_to(R).as_posix(), **identity(p), "type": kind})
save(R / "INVENTORY.json", {"files": entries, "file_count": len(entries), "excluded_self_referential_records": ["INVENTORY.json", "SUPPLEMENT-SEAL.json"]})
names = ("README.md", "verification.json", "identity-normalized-comparison.json", "reviewed-candidate-before.json", "reviewed-candidate-unchanged.json", "bound-identities.json", "bootstrap.js", "unread-revisit-call.js", "actual-functions-exec-return.txt", "bootstrap-retained-envelope.json", "after-bootstrap-before-call.json", "runtime/access.jsonl", "INVENTORY.json")
save(R / "SUPPLEMENT-SEAL.json", {"state": "supplemental_same_surface_unread_revisit_passed_pending_root_and_independent_review", "files": {name: identity(R / name) for name in names}, "reviewed_candidate_not_modified": True, "no_new_code_proposal": True, "failed_fixture_not_reset_or_retried": True, "production_actions": False})
print(json.dumps({"passed": True, "reviewed_candidate_files_unchanged": len(before), "reader_subject_opens": 0, "cursor_before": 0, "cursor_after": 0, "retrieval_invocations": 1, "supplement_seal": identity(R / "SUPPLEMENT-SEAL.json"), "verification": identity(R / "verification.json"), "inventory_files": len(entries)}, indent=2))
