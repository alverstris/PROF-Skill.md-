"""Additive raw-byte-preserving target mapping; writes only this owned subtree."""
import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

R = Path(__file__).resolve().parent
CASE = R.parent
PROJECT = CASE.parents[1]
OLD = CASE / "publication-preparation"
ORIGINAL_INDEX_SHA = "4b0ff7587f59528b8a84e91f253ea7b14909de7bb708c28728a1b673080b0987"
ORIGINAL_SEAL_SHA = "31d09b43e821f6c15608f3cd2e520979c2ca106a7a071723a1b623e388821aed"
SAFE = "_git_metadata_snapshot"
FAILURE = PROJECT / ".prof-maintenance/20261014/r41-initial-tree-rejection.json"
DIAGNOSTIC = PROJECT / ".prof-maintenance/20261014/r41-path-component-diagnostic.json"
EXPECTED_OVERLAYS = {"SKILL.md", "references/sasis.md", "references/sasis/profile-manifest.json", "references/sasis/student-role.txt", "references/sasis/student-testing-contract.txt"}
ARTIFACTS = ["target-path-mapping.json", "github-tree-rejection.json", "github-path-component-diagnostic.json", "validate_evidence_paths.py", "build_adaptation.py", "transport.py", "PROCEDURE.md", "README.md", "mapping-validation.json", "adaptation-record.json"]

def ident(p):
    b = p.read_bytes(); return {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(), "git_blob_sha": hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()}
def save(p, value): p.write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")
def load(p): return json.loads(p.read_bytes())
def snapshot(folder): return {p.relative_to(folder).as_posix(): ident(p) for p in sorted(folder.rglob("*")) if p.is_file()}
def describe(p, path):
    raw = p.read_bytes()
    try: text = raw.decode("utf-8"); encoding = "utf-8"; assert text.encode("utf-8") == raw
    except UnicodeDecodeError: text = None; encoding = "base64"
    return {"source": str(p.resolve()).replace("\\", "/"), "path": path, "group": "publication-path-adaptation", **ident(p), "encoding": encoding, "characters": len(text) if text is not None else None, "text_chars": len(text) if text is not None else None, "encoded_chars": len(text) if text is not None else 4 * ((len(raw) + 2) // 3), "utf16_length": len(text.encode("utf-16-le")) // 2 if text is not None else None, "utf8_bom": raw.startswith(b"\xef\xbb\xbf"), "crlf_count": raw.count(b"\r\n") if text is not None else None}

if (R / "publication-inputs.json").exists():
    assert sys.argv[1:] == ["--refresh-root-diagnostic"], "Preserve completed adaptation; no automatic rerun"
    checkpoint = R / "before-root-diagnostic"
    assert ident(checkpoint / "ADAPTATION-SEAL.json")["sha256"] == "832234ef430d49c2917e5a84c8ae957229f9c9051ccc684a9a0d2b61eada9254"
    assert ident(R / "publication-inputs.json") == ident(checkpoint / "publication-inputs.json")
before = snapshot(OLD)
assert ident(OLD / "publication-inputs.json")["sha256"] == ORIGINAL_INDEX_SHA
assert ident(OLD / "PREPARATION-SEAL.json")["sha256"] == ORIGINAL_SEAL_SHA
original = load(OLD / "publication-inputs.json")
assert original["status"] == "ready_for_root_readback_not_published" and not original["pending"]
assert len(original["items"]) == 3797 and len(original["unique_blobs"]) == 398 and len(original["package"]) == 36
assert original["summary"]["operative_manifest_checks"] == 28 and original["summary"]["frozen_provenance_identities"] == 19
failure_before = ident(FAILURE)
failure = load(FAILURE)
assert failure["base_commit"] == original["base_commit"] and failure["base_tree"] == original["base_tree"]
assert failure["requested_entries"] == 3797 and failure["uploaded_raw_blobs"] == 398
shutil.copyfile(FAILURE, R / "github-tree-rejection.json")
assert ident(R / "github-tree-rejection.json") == failure_before
diagnostic_before = ident(DIAGNOSTIC)
diagnostic = load(DIAGNOSTIC)
assert diagnostic["base_tree"] == original["base_tree"]
assert diagnostic["reserved_component_rejected"] is True and diagnostic["mapped_component_accepted"] is True
assert diagnostic["results"][1]["value"]["result"]["structuredContent"]["sha"] == "69de497b6d0162394442381c0d84477c07657eb4"
shutil.copyfile(DIAGNOSTIC, R / "github-path-component-diagnostic.json")
assert ident(R / "github-path-component-diagnostic.json") == diagnostic_before
shutil.copyfile(OLD / "transport.py", R / "transport.py")
assert ident(R / "transport.py") == ident(OLD / "transport.py")
spec = importlib.util.spec_from_file_location("evidence_path_validator", R / "validate_evidence_paths.py")
validator = importlib.util.module_from_spec(spec); spec.loader.exec_module(validator)
original_paths = [e["path"] for e in original["items"]]
assert not any(SAFE in p.split("/") for p in original_paths), "Replacement component already exists"
items = []; changes = []
for entry in original["items"]:
    current = ident(Path(entry["source"]))
    assert current == {k: entry[k] for k in current}
    path = "/".join(SAFE if p == ".git" else p for p in entry["path"].split("/"))
    assert "/".join(".git" if p == SAFE else p for p in path.split("/")) == entry["path"]
    mapped = {**entry, "original_path": entry["path"], "path": path}
    items.append(mapped)
    if path != entry["path"]:
        changes.append({"original_path": entry["path"], "published_path": path, "source": entry["source"], **current})
assert len(changes) == 204
assert {e["original_path"]: e["git_blob_sha"] for e in changes} == {e["path"]: e["git_blob_sha"] for e in failure["affected_paths"]}
path_checks = validator.validate_target_set([e["path"] for e in items])
overlays = [e for e in items if e["group"] == "root_package_overlay"]
assert len(overlays) == 5 and {e["path"] for e in overlays} == EXPECTED_OVERLAYS
assert all(e["original_path"] == e["path"] for e in overlays)
assert [{k: v for k, v in e.items() if k != "original_path"} for e in overlays] == [e for e in original["items"] if e["group"] == "root_package_overlay"]
for e in original["package"]: assert ident(Path(e["source"])) == {k: e[k] for k in ("bytes", "sha256", "git_blob_sha")}
save(R / "target-path-mapping.json", {"schema": "prof-evidence-path-mapping-v1", "original_index": {"source": str(OLD / "publication-inputs.json").replace("\\", "/"), **ident(OLD / "publication-inputs.json")}, "rule": {"exact_component": ".git", "published_component": SAFE, "other_components_unchanged": True, "replacement_component_absent_from_original_targets": True}, "original_items": 3797, "changed_targets": 204, "unchanged_targets": 3593, "bijective": True, "mapping": changes})
negative = []
for path in ("a/.git/config", "a/.GIT/config", "/absolute", "a//b", "a/../b", "a/./b", "a\\b", "a/", "a/\u0000b"):
    try: validator.validate_path(path)
    except (ValueError, UnicodeError) as exc: negative.append({"path": path, "rejected": True, "error": str(exc)})
    else: raise AssertionError("Invalid path accepted: " + repr(path))
for paths in (["a", "a"], ["a", "a/b"], ["A", "a"]):
    try: validator.validate_target_set(paths)
    except ValueError as exc: negative.append({"paths": paths, "rejected": True, "error": str(exc)})
    else: raise AssertionError("Collision accepted")
assert validator.validate_path("a/.github/archive.git/" + SAFE + "/config")
save(R / "mapping-validation.json", {"passed": True, "original_items_preserved": 3797, "original_source_byte_checks": 3797, "package_source_byte_checks": 36, "original_unique_blob_ids_reusable": 398, "changed_targets": 204, "mapping_exactly_matches_root_failure_paths_and_blobs": True, "exact_component_only": True, "reverse_mapping_matches_all_original_targets": True, "path_checks": path_checks, "all_five_root_overlays_unchanged": True, "complete_36_package_inventory_unchanged": True, "operative_manifest_checks_carried_forward": 28, "frozen_provenance_identities_carried_forward": 19, "validator_rejections": negative, "similar_nonreserved_names_accepted": True, "no_source_renamed_or_rewritten": True, "no_publication_installation_or_reader_action": True})
save(R / "adaptation-record.json", {"schema": "prof-evidence-publication-path-adaptation-v1", "state": "prepared_for_independent_root_review_not_published", "base_commit": original["base_commit"], "base_tree": original["base_tree"], "original_index_identity": ident(OLD / "publication-inputs.json"), "original_preparation_seal_identity": ident(OLD / "PREPARATION-SEAL.json"), "exact_root_failure_source": str(FAILURE).replace("\\", "/"), "exact_failure_identity": failure_before, "mapping_identity": ident(R / "target-path-mapping.json"), "original_entries_retained": 3797, "mapped_entries": 204, "publishable_adaptation_records": ARTIFACTS, "raw_content_or_package_changes": False, "root_publisher_and_acceptance_owner": True})
adaptation_record = load(R / "adaptation-record.json")
adaptation_record.update({"exact_root_diagnostic_source": str(DIAGNOSTIC).replace("\\", "/"), "exact_diagnostic_identity": diagnostic_before, "root_controlled_component_probe": {"reserved_component_rejected": True, "mapped_component_accepted": True, "accepted_immutable_probe_tree": "69de497b6d0162394442381c0d84477c07657eb4", "full_adapted_tree_accepted_or_published": False}})
save(R / "adaptation-record.json", adaptation_record)
prefix = original["evidence_prefix"] + "publication-path-adaptation/"
for name in ARTIFACTS: items.append(describe(R / name, prefix + name))
complete_paths = validator.validate_target_set([e["path"] for e in items])
unique = {}
for entry in items:
    if entry["git_blob_sha"] not in unique: unique[entry["git_blob_sha"]] = {**entry, "target_paths": []}
    unique[entry["git_blob_sha"]]["target_paths"].append(entry["path"])
assert [e["git_blob_sha"] for e in list(unique.values())[:398]] == [e["git_blob_sha"] for e in original["unique_blobs"]]
summary = {**original["summary"], "original_source_items_preserved": 3797, "mapped_original_targets": 204, "new_adaptation_records": len(ARTIFACTS), "upload_files": len(items), "evidence_files": len(items) - 5, "upload_bytes": sum(e["bytes"] for e in items), "unique_upload_blobs": len(unique), "unique_upload_blob_bytes": sum(e["bytes"] for e in unique.values()), "previously_uploaded_unique_blobs_reusable": 398, "new_unique_blob_bodies": len(unique) - 398, "groups": {**original["summary"]["groups"], "publication-path-adaptation": {"files": len(ARTIFACTS), "bytes": sum(e["bytes"] for e in items if e["group"] == "publication-path-adaptation")}}}
record = {**original, "status": "mapped_inputs_ready_for_independent_root_review_not_published", "path_adaptation": {"exact_component": ".git", "published_component": SAFE, "mapped_targets": 204, "source_bytes_unchanged": True}, "summary": summary, "items": items, "unique_blobs": list(unique.values()), "pending": ["Root and independent review of additive publication path adaptation; no tree/commit/ref or install action authorized by this preparation."]}
assert record["package"] == original["package"]
save(R / "publication-inputs.json", record)
assert snapshot(OLD) == before and ident(FAILURE) == failure_before and ident(DIAGNOSTIC) == diagnostic_before
save(R / "original-publication-preparation-unchanged.json", {"passed": True, "file_count": len(before), "all_original_inventory_paths_and_bytes_unchanged": True, "files": before, "root_failure_record_unchanged": failure_before})
local = {p.name: ident(p) for p in sorted(R.iterdir()) if p.is_file() and p.name != "ADAPTATION-SEAL.json"}
save(R / "ADAPTATION-SEAL.json", {"state": "additive_path_adaptation_ready_for_independent_root_review", "files": local, "original_items": 3797, "mapped_targets": 204, "new_records": len(ARTIFACTS), "complete_items": len(items), "complete_package_files": 36, "unchanged_original_blob_ids": 398, "path_validation": complete_paths, "no_source_content_change_publication_installation_or_reader_action": True})
print(json.dumps({"status": record["status"], "index_identity": ident(R / "publication-inputs.json"), "seal_identity": ident(R / "ADAPTATION-SEAL.json"), "mapping_identity": ident(R / "target-path-mapping.json"), "summary": summary}, indent=2))
