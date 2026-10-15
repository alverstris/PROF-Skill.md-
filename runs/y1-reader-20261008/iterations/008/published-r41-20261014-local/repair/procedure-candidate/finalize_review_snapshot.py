"""Refresh only this owned unpublished review snapshot; no source/runtime mutation."""
import difflib
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parent
P = R / "proposed-package"
INSTALLED = Path("C:/Users/alver/.codex/skills/prof")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

profile = json.loads((P / "references/sasis/profile-manifest.json").read_text(encoding="utf-8"))
assert profile["protocol_revision"] == "2026-10-14-r41"
assert len(profile["file_hashes"]) == 19
assert profile["control_file_hashes"]["../sasis.md"] == sha((P / "references/sasis.md").read_bytes())
assert profile["control_file_hashes"]["../../SKILL.md"] == sha((P / "SKILL.md").read_bytes())
diff = []
for file in sorted(p for p in P.rglob("*") if p.is_file()):
    name = file.relative_to(P).as_posix()
    old = (INSTALLED / name).read_text(encoding="utf-8")
    new = file.read_text(encoding="utf-8")
    diff.extend(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile="r40/" + name, tofile="r41/" + name))
(R / "proposed-controls.diff").write_text("".join(diff), encoding="utf-8", newline="\n")

identity_path = R / "candidate-identities.json"
identity = json.loads(identity_path.read_text(encoding="utf-8"))
identity["state"] = "unpublished_candidate_pending_root_review_not_accepted"
identity["proposed_visible_and_manifest_protocol_revision"] = profile["protocol_revision"]
identity["protocol_update_note_appended"] = profile["protocol_update_notes"][-1]
identity["frozen_baseline_provenance_hashes_unchanged"] = profile["file_hashes"]
identity["proposed_package_file_identities"] = json.loads((R / "proposed-file-identities.json").read_text(encoding="utf-8"))["files"]
identity["source_control_readback"] = {name: {"bytes": (INSTALLED / name).stat().st_size, "sha256": sha((INSTALLED / name).read_bytes())} for name in identity["changed_existing_files"]}
save(identity_path, identity)

excluded = {"INVENTORY.json", "REVIEW-SEAL.json"}
entries = []
for file in sorted(p for p in R.rglob("*") if p.is_file()):
    relative = file.relative_to(R).as_posix()
    if relative in excluded:
        continue
    raw = file.read_bytes()
    try:
        raw.decode("utf-8")
        kind = "UTF-8"
    except UnicodeDecodeError:
        kind = "binary"
    entries.append({"path": relative, "bytes": len(raw), "sha256": sha(raw), "type": kind})
save(R / "INVENTORY.json", {"scope": "Owned r41 procedure-candidate subtree only", "excluded_self_referential_records": sorted(excluded), "files": entries, "file_count": len(entries), "total_bytes": sum(x["bytes"] for x in entries)})

authoritative = ["README.md", "SEALING.md", "proposed-controls.diff", "candidate-identities.json", "proposed-file-identities.json", "manifest-validation.json", "validation.json", "metadata-subject-free-verification.json", "interface-probes.json", "failure-evidence/identities.json", "failure-evidence/schema-copy-synthetic-reproduction.json", "synthetic-preflight/negative-preflight-evidence.json", "synthetic-preflight/figure-preflight-evidence.json", "synthetic-preflight/whole-route-audit.json", "synthetic-preflight/launcher-truncation-evidence.json", "synthetic-preflight/minimal-surface-supplement.json", "synthetic-preflight/rejection-supplement.json", "INVENTORY.json"]
seal = {"status": "unpublished_r41_candidate_pending_root_review", "proposed_version": "2026-10-14-r41", "source_package_commit": "2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce", "complete_package_files_after_integration": 36, "proposed_changed_existing_package_files": 5, "operative_manifest_checks": 28, "unchanged_frozen_baseline_provenance_identities": 19, "files": {name: {"bytes": (R / name).stat().st_size, "sha256": sha((R / name).read_bytes())} for name in authoritative}, "synthetic_preflight_passed": True, "templates_unchanged_by_root_metadata_review": True, "production_binding_dispatch_generation_publication_installation_or_acceptance": False, "limitations": "Retained expression evaluates before its current identity check. No pre-evaluation authentication, persistent callable or technical confinement. Fresh generation/complete reading/affected-success evidence remain pending after root review, full package publication/readback/sync."}
save(R / "REVIEW-SEAL.json", seal)
print(json.dumps({"review_seal_sha256": sha((R / "REVIEW-SEAL.json").read_bytes()), "diff_sha256": sha((R / "proposed-controls.diff").read_bytes()), "inventory_sha256": sha((R / "INVENTORY.json").read_bytes()), "inventory_files": len(entries), "proposed_files": identity["proposed_package_file_identities"]}, indent=2))
