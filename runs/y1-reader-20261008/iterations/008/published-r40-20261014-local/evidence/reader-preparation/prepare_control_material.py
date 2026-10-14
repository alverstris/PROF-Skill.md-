"""Prepare only verified non-subject r40 reader controls/templates; no binding."""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[2]
INSTALLED = Path("C:/Users/alver/.codex/skills/prof")
REPO = PROJECT / ".prof-maintenance/20261014/repository"
PUBLISHED = "0c0031cf996d7f47d4db878709f31676594aa08f"
OLD = PROJECT / ".prof-sasis/20261014-d008-r39/reader-reuse-candidate"
CONTROLS = ("SKILL.md", "references/sasis.md", "references/sasis/student-role.txt", "references/sasis/student-testing-contract.txt")
TEMPLATES = ("bootstrap_template.js", "short_call_template.js", "verify_reuse_template.py")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args):
    result = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, check=True)
    return result.stdout


def write(name, value):
    target = ROOT / name
    assert not target.exists(), "Preserve prepared evidence: " + name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def main():
    assert ROOT.name == "reader-preparation" and ROOT.parent.name == "20261014-d008-r40"
    assert git("rev-parse", "--verify", PUBLISHED + "^{commit}").decode().strip() == PUBLISHED
    controls = []
    for path in CONTROLS:
        published = git("show", PUBLISHED + ":" + path)
        installed = (INSTALLED / path).read_bytes()
        assert installed == published, "Installed/published control mismatch: " + path
        controls.append({"path": path, "installed_path": str(INSTALLED / path).replace("\\", "/"), "published_commit": PUBLISHED,
                         "git_blob": git("rev-parse", PUBLISHED + ":" + path).decode().strip(), "sha256": sha(installed), "bytes": len(installed), "installed_equals_published": True})
        if path.endswith("student-role.txt") or path.endswith("student-testing-contract.txt"):
            name = Path(path).stem + ".r40.txt"
            target = ROOT / "controls" / name
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(installed)
    write("control-identities.json", {"published_commit": PUBLISHED, "revision": "2026-10-14-r40", "checked_controls": controls,
          "verification_scope": "These four installed operational files compared byte for byte to exact local Git objects at the published commit; root separately verified full installation/publication.",
          "baseline_teaching_original_subject_content_read": False})
    previous = json.loads((OLD / "portable-template-roundtrip.json").read_text(encoding="utf-8"))
    assert previous["passed"] and previous["same_tested_logic"]
    identities = []
    target_dir = ROOT / "templates"
    target_dir.mkdir(exist_ok=True)
    for name in TEMPLATES:
        source = OLD / "portable-templates" / name
        raw = source.read_bytes()
        assert sha(raw) == previous["template_hashes"][name], "Old tested template identity mismatch: " + name
        target = target_dir / name
        target.write_bytes(raw)
        assert target.read_bytes() == raw
        identities.append({"file": "templates/" + name, "sha256": sha(raw), "bytes": len(raw), "source": str(source).replace("\\", "/"), "byte_identical_to_tested_template": True})
    write("template-identities.json", {"templates": identities, "previous_synthetic_verifier_roundtrip_passed": True,
          "old_test_evidence_changed": False, "new_runtime_code_or_dependencies": False, "production_binding_and_preflight": "pending"})
    write("binding-state.json", {"state": "operational_controls_prepared_route_unbound_dispatch_held", "published_prof_commit": PUBLISHED,
          "reader_role_revision": "2026-10-14-r40", "reader_agent": None, "fork_turns_required": "none", "root_is_publisher_and_acceptance_owner": True,
          "frozen_baseline_identity": None, "frozen_teaching_identity": None, "frozen_route_identity": None, "route_step_ids": None,
          "bound_input_directory": None, "fixed_python": None, "fixed_launcher_identity": None, "fixed_receipt_identity": None,
          "operational_adapter_identity": None, "bound_verifier_identity": None, "store_key": None, "seal_core_identity": None,
          "bootstrap_identity": None, "short_call_identity": None, "runtime_identity": None, "reader_report_destination": None,
          "production_bound_preflight": "pending", "admission": "not_dispatched_not_admitted", "actual_subject_input_access": "none",
          "next_owner_action": "Root freezes newly authored teaching and exact baseline/constituent route, then binds/seals/preflights before any fresh reader dispatch."})
    print(json.dumps({"verified_published_controls": len(controls), "copied_exact_tested_templates": len(identities), "route_binding": "pending", "reader_dispatched": False}))


if __name__ == "__main__":
    main()
