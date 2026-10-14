"""Check only non-subject production preparation and record its exact identities."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save(name, value):
    p = ROOT / name
    assert not p.exists(), "Preserve prior preparation evidence: " + name
    p.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def main():
    controls = json.loads((ROOT / "control-identities.json").read_text())
    templates = json.loads((ROOT / "template-identities.json").read_text())
    state = json.loads((ROOT / "binding-state.json").read_text())
    assert all(c["installed_equals_published"] and sha(Path(c["installed_path"]).read_bytes()) == c["sha256"] for c in controls["checked_controls"])
    assert all(sha((ROOT / t["file"]).read_bytes()) == t["sha256"] and (ROOT / t["file"]).read_bytes() == Path(t["source"]).read_bytes() for t in templates["templates"])
    substitutions = {
      "verifier_template": [
        {"marker": "__FIXED_ROUTE_FILENAME__", "value": None, "source_after_freeze": "Exact frozen route metadata basename", "constraint": "safe ASCII basename; no quotes, slashes, backslashes or newline"},
        {"marker": "__FIXED_RUNTIME_DIRNAME__", "value": None, "source_after_freeze": "Fresh isolated runtime basename", "constraint": "safe ASCII basename; no quotes, slashes, backslashes or newline"},
        {"marker": "__FIXED_SCOPE__", "value": None, "source_after_freeze": "Explicit instruction-confined condition label", "constraint": "safe ASCII label; no quotes, backslashes or newline"},
        {"marker": "__FIXED_ROUTE_ID__", "value": None, "source_after_freeze": "Exact frozen route ID", "constraint": "[A-Za-z][A-Za-z0-9_-]{0,63}"}],
      "wrapper_render": [
        {"marker": "__VERIFY_COMMAND__", "value": None, "source_after_freeze": "Existing deterministic render of fixed bound verifier path/hash and Python path"},
        {"marker": "__CORE_SHA256__", "value": None, "source_after_freeze": "SHA256 of exact saved sealed core bytes"},
        {"marker": "__STORE_KEY__", "value": None, "source_after_freeze": "Fresh simple safe operational store key, fixed by root"}],
      "short_call_seed": {"exact_template_datum": 'const STEP_ID = "B001";', "synthetic_test_seed_only": True, "production_value": None,
                          "source_after_freeze": "Actual first scheduled ID from frozen route, JSON string literal; substitute this one datum before sealing", "remainder_of_template": "byte unchanged"},
      "operating_instruction": {}, "dispatch_authorization": {},
      "production_binding": "pending; no replacement values selected"}
    for filename, key, expected in [
        ("operating_instruction_template.md", "operating_instruction", {"FROZEN_BASELINE_ID_AND_REVISION", "FROZEN_TEACHING_ID_AND_REVISION", "FROZEN_ROUTE_ID_AND_HASH", "READER_REPORT_DESTINATION", "READER_CONDITION_ID"}),
        ("dispatch_authorization_template.md", "dispatch_authorization", {"FROZEN_BASELINE_ID_AND_REVISION", "FROZEN_TEACHING_ID_AND_REVISION", "BOUND_BOOTSTRAP_SHA256", "EXACT_BOUND_BOOTSTRAP_BODY", "BOUND_SHORT_CALL_SHA256", "EXACT_BOUND_SHORT_CALL_BODY", "SUBJECT_FREE_ROUTE_DELIVERY_OR_IMMUTABLE_LOCATOR", "READER_REPORT_DESTINATION"})]:
        text = (ROOT / filename).read_text(encoding="utf-8")
        markers = set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", text))
        assert markers == expected, (filename, markers ^ expected)
        assert "synthetic" not in text.lower(), "Synthetic operating role must not be imported"
        substitutions[key] = {"file": filename, "preseal_markers": sorted(markers), "replacement_values": {m: None for m in sorted(markers)}}
    assert set(re.findall(r"__[A-Z0-9_]+__", (ROOT / "operating_instruction_template.md").read_text())) == {"__CORE_SHA256__", "__STORE_KEY__"}
    assert state["route_step_ids"] is None and state["frozen_route_identity"] is None and state["frozen_teaching_identity"] is None
    assert state["admission"] == "not_dispatched_not_admitted"
    assert not any((ROOT / name).exists() for name in ("bootstrap.js", "short_call.js", "verify_reuse.py", "seal-core.json", "fixed_launcher.py", "operational_adapter.js"))
    save("binding-substitutions.json", substitutions)
    verifier = (ROOT / "templates/verify_reuse_template.py").read_text(encoding="utf-8")
    fixture = {"__FIXED_ROUTE_FILENAME__": "synthetic-route.json", "__FIXED_RUNTIME_DIRNAME__": "synthetic-runtime", "__FIXED_SCOPE__": "synthetic non-subject only", "__FIXED_ROUTE_ID__": "SYNTHETIC_R39"}
    for marker, value in fixture.items():
        verifier = verifier.replace(marker, value)
    expected_verifier = "cc727c2b2b0fee7e1f5cb8ca71f6eff18fc2006cdc4654bd023f94de8cac209f"
    assert sha(verifier.encode()) == expected_verifier
    save("requirements-map.json", {"derived_from": ["student-role.r40.txt", "student-testing-contract.r40.txt"], "published_commit": controls["published_commit"],
      "reader_instruction_paragraphs": [
        {"paragraph": 1, "preserves": "Dedicated reader; one frozen revision; whole teaching route; document evaluation, no task battery/score"},
        {"paragraph": 2, "preserves": "Exactly two subject inputs; actual complete four-subject operational baseline; baseline before teaching"},
        {"paragraph": 3, "preserves": "Permitted premise recall/deduction; no external or author/history/source inputs; no browsing/messaging/searches"},
        {"paragraph": 4, "preserves": "Explicit one-time non-subject bootstrap; exact sealed short call; only STEP_ID edited; no subject execution"},
        {"paragraph": 5, "preserves": "Exact bounded sequential route; already-read baseline revisits; complete first-use actual figures and display receipts"},
        {"paragraph": 6, "preserves": "Execution/input failure stop/preserve/no retry; input-procedure failure distinct from teaching judgement; root recovery"},
        {"paragraph": 7, "preserves": "Meaning, availability/locators, concise reconstruction, accessibility, ambiguity; no redundant baseline reteaching; legitimate introductions and preview distinction"},
        {"paragraph": 8, "preserves": "Teaching gaps continue whole reading; supported state; dependencies blocked/conditional; all issues and uncertainty"},
        {"paragraph": 9, "preserves": "Original final-response report preserved by root; access/full coverage; witnesses/alternatives/dependencies; honest claims and admission audit"},
        {"paragraph": 10, "preserves": "Published r40 provenance; one condition; instruction confinement limits; separate fresh reader after change/repair"}],
      "root_only_sealing_doc": "BINDING-PENDING.md preserves frozen identity, preflight, access audit, provisional admission and publication/acceptance ownership requirements.",
      "independent_control_requirements_review": "A fresh infrastructure-only subagent read installed r40 role/contract and relevant protocol clauses and returned the mandatory requirement list; root retains final acceptance. Follow-up review could not run because agent thread limit was reached."})
    save("verification.json", {"status": "non_subject_preparation_verified_route_binding_pending", "published_control_byte_comparisons": 4,
      "exact_tested_template_copies": 3, "verifier_template_roundtrip_sha256": expected_verifier, "verifier_template_roundtrip_equal_to_tested_program": True,
      "operating_instruction_preseal_fields": 5, "operating_instruction_render_fields": 2, "dispatch_authorization_fields": 8,
      "production_bound_code_created": False, "production_preflight_claimed": False, "reader_dispatched": False, "baseline_teaching_source_or_author_content_read": False,
      "no_writes_outside_reader_preparation_by_this_task": True, "installed_prof_old_r39_and_test_evidence_changed": False,
      "reader_route_binding_and_admission": "pending", "publisher_and_acceptance_owner": "root"})
    inventory = {str(p.relative_to(ROOT)).replace("\\", "/"): {"sha256": sha(p.read_bytes()), "bytes": p.stat().st_size}
                 for p in ROOT.rglob("*") if p.is_file() and p.name != "INVENTORY.json" and "__pycache__" not in p.parts}
    save("INVENTORY.json", {"scope": "Only r40 non-subject reader preparation; not frozen input/route admission", "files": inventory})
    print(json.dumps({"preparation_files": len(inventory), "verified_controls": 4, "exact_tested_templates": 3, "production_route_and_dispatch": "pending", "sha256": {n: inventory[n]["sha256"] for n in ("operating_instruction_template.md", "dispatch_authorization_template.md", "BINDING-PENDING.md")}}, indent=2))


if __name__ == "__main__":
    main()
