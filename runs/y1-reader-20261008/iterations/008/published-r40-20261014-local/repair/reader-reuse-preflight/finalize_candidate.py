"""Finalize evidence/portable operational templates. Reads no actual subjects."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(name, obj):
    target = ROOT / name
    assert not target.exists(), "Preserve existing evidence: " + name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def main():
    core_raw = (ROOT / "seal-core.json").read_bytes()
    core_hash = sha(core_raw)
    core = json.loads(core_raw)
    import verify_reuse
    proof = verify_reuse.proof("bootstrap", core_hash)
    audit = json.loads((ROOT / "whole-route-audit.json").read_text(encoding="utf-8-sig"))
    negative = json.loads((ROOT / "negative-preflight-evidence.json").read_text(encoding="utf-8"))
    figure = json.loads((ROOT / "figure-preflight-evidence.json").read_text(encoding="utf-8"))
    truncation = json.loads((ROOT / "launcher-truncation-evidence.json").read_text(encoding="utf-8"))
    assert audit["operational_route_audit_passed"] and len(audit["verified_accesses"]) == 7
    assert negative["negative_checks_passed"] and len(negative["negative_checks"]) == 27
    assert figure["figure_checks_passed"] and len(figure["actual_tool_events"]) == 2 and truncation["passed"]
    opens = [json.loads(s) for s in (ROOT / "verification-open-audit.jsonl").read_text(encoding="utf-8").splitlines()]
    fixture_dir = str(ROOT / "synthetic-fixtures").lower().replace("\\", "/") + "/"
    fixture_opens = [e for e in opens if e["path"].lower().replace("\\", "/").startswith(fixture_dir)]
    assert fixture_opens == []
    write("verification-open-audit-summary.json", {"separate_external_python_audit": True, "actual_bootstrap_transcript_is_separate": True,
          "exact_verifier_instrumented": True, "python_open_events": len(opens), "synthetic_fixture_opens": len(fixture_opens),
          "all_paths": sorted({e["path"] for e in opens}), "os_wide_monitoring": False})
    tested = ROOT / "tested-calls"
    tested.mkdir(exist_ok=True)
    bootstrap = (ROOT / "bootstrap.js").read_bytes()
    (tested / "00-bootstrap.js").write_bytes(bootstrap)
    source = (ROOT / "short_call.js").read_text(encoding="utf-8")
    calls = [{"file": "00-bootstrap.js", "sha256": sha(bootstrap), "mechanism": "exact body submitted directly to actual functions.exec", "subject_retrieval": False}]
    for index, step in enumerate(("B001", "B002", "RB001", "T001", "F001", "RB002", "T002"), 1):
        call = source.replace('const STEP_ID = "B001";', 'const STEP_ID = "' + step + '";', 1)
        assert call.replace('const STEP_ID = "' + step + '";', 'const STEP_ID = "B001";', 1) == source
        name = str(index).zfill(2) + "-" + step + ".js"
        (tested / name).write_text(call, encoding="utf-8", newline="\n")
        calls.append({"file": name, "step_id": step, "sha256": sha(call.encode()),
                      "only_edited_datum": "STEP_ID", "mechanism": "exact sealed body in actual functions.exec with tool instrumentation" if step == "F001" else "exact body submitted directly to a fresh actual functions.exec cell"})
    write("tested-calls/manifest.json", {"code_identity_source": "Saved exact submitted bootstrap/short bodies; compare with actual functions.exec transcript. The running wrapper cannot introspect the submitted cell source.", "calls": calls})
    portable = ROOT / "portable-templates"
    portable.mkdir(exist_ok=True)
    for name in ("bootstrap_template.js", "short_call_template.js"):
        (portable / name).write_bytes((ROOT / name).read_bytes())
    verifier = (ROOT / "verify_reuse.py").read_text(encoding="utf-8")
    substitutions = {"__FIXED_ROUTE_FILENAME__": "synthetic-route.json", "__FIXED_RUNTIME_DIRNAME__": "synthetic-runtime", "__FIXED_SCOPE__": "synthetic non-subject only", "__FIXED_ROUTE_ID__": "SYNTHETIC_R39"}
    template = verifier
    for token, value in substitutions.items():
        assert value in template
        template = template.replace(value, token)
    assert "C:/" not in template and "D008" not in template and "d008" not in template
    (portable / "verify_reuse_template.py").write_text(template, encoding="utf-8", newline="\n")
    rendered = template
    for token, value in substitutions.items():
        rendered = rendered.replace(token, value)
    assert rendered.encode() == (ROOT / "verify_reuse.py").read_bytes()
    template_hashes = {p.name: sha(p.read_bytes()) for p in portable.iterdir() if p.is_file()}
    write("portable-template-roundtrip.json", {"passed": True, "same_tested_logic": True, "substitutions": substitutions,
          "rendered_verifier_sha256": sha(rendered.encode()), "actual_tested_verifier_sha256": core["files"]["verify_reuse.py"]["sha256"],
          "template_hashes": template_hashes, "production_binding_or_reader_dispatch_tested": False,
          "minimal_bundle_files": list(template_hashes), "new_dependencies": [], "additional_runner_framework": False})
    origins = {}
    for name in ("launcher_template.py", "receipt_template.py", "adapter_template.js", "audit_template.py", "bind_synthetic.py", "inspect_synthetic_runtime.py"):
        original = ROOT.parent / "reader-infrastructure" / name
        assert original.read_bytes() == (ROOT / name).read_bytes()
        origins[str(original)] = sha(original.read_bytes())
    for name in ("fixed_adapter.js", "fixed_launcher.py", "record_receipt.py"):
        path = ROOT.parent / "reader-inputs" / name
        origins[str(path)] = sha(path.read_bytes())
    write("original-code-identities.json", {"allowed_original_code_files_only": True, "source_template_copies_still_byte_identical": True, "hashes": origins,
          "no_write_outside_candidate_by_this_agent": True, "complete_old_evidence_inventory_rehash": False})
    summary = {"status": "synthetic_reuse_preflight_passed_pending_root_review", "scope": "synthetic infrastructure only", "real_reader_dispatched": False,
       "actual_subject_files_read": False, "installed_prof_modified_or_published": False, "current_reader_inputs_mutated": False,
       "core_sha256": core_hash, "adapter_sha256": proof["seal"]["adapter_sha256"], "route_sha256": core["route_sha256"],
       "bootstrap_sha256": proof["seal"]["bootstrap_sha256"], "short_call_sha256": proof["seal"]["short_call_sha256"],
       "negative_checks_passed": len(negative["negative_checks"]), "figure_checks_passed": len(figure["figure_checks"]),
       "launcher_output_truncation_preserved": True, "verified_accesses": len(audit["verified_accesses"]), "scheduled_steps": audit["scheduled_steps"],
       "baseline_revisits": 2, "complete_route_audit_passed": True, "external_verifier_fixture_opens": len(fixture_opens),
       "instruction_confinement_only": True, "technical_sandbox_or_memory_erasure_claim": False, "semantic_admission_claim": False,
       "production_r40_binding_required_after_publication": True, "portable_template_hashes": template_hashes}
    write("summary.json", summary)
    inventory = {str(p.relative_to(ROOT)).replace("\\", "/"): {"sha256": sha(p.read_bytes()), "bytes": p.stat().st_size}
                 for p in ROOT.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.name != "INVENTORY.json"}
    write("INVENTORY.json", {"files": inventory, "scope": "all candidate code, fixtures and evidence; no outside subject content"})
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
