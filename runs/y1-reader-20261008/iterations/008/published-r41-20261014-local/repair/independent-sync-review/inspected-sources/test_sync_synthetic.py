"""Synthetic-only path/backup/rollback tests. Never invokes production CLI."""
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sync_under_test", ROOT / "sync_published_prof.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
FIXTURES = ROOT / "synthetic-fixtures" / STAMP
FIXTURES.mkdir(parents=True)
RESULTS = []
VERSION = "synthetic-r41"


def expect_failure(call):
    try:
        call()
    except Exception as exc:
        return sync.error_record(exc)
    raise AssertionError("Expected rejection did not occur")


def package(root, controls=5):
    root.mkdir()
    files = {
        "SKILL.md": b'\xef\xbb\xbf---\r\nmetadata:\r\n  version: "synthetic-r41"\r\n---\r\nSynthetic fixture only.\n',
        "references/sasis.md": b"synthetic protocol\r\n",
        "references/sasis/student-role.txt": b"synthetic role\n",
        "references/sasis/student-testing-contract.txt": b"synthetic contract\r\n",
        "references/sasis/rewrite-guide.md": b"synthetic guide\r\n",
    }
    for n in range(19):
        files[f"references/sasis/baseline/base-{n:02}.txt"] = b"\xef\xbb\xbf" + f"synthetic {n}\r\nline two\n".encode()
    for n in range(11):
        files[f"assets/payload-{n:02}.bin"] = bytes([0, 10, 13, 255, n])
    for p, raw in files.items():
        dest = root / p
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(raw)
    control_paths = ["student-role.txt", "student-testing-contract.txt", "rewrite-guide.md", "../sasis.md", "../../SKILL.md"][:controls]
    base = root / "references/sasis"
    manifest = {
        "protocol_revision": VERSION,
        "file_hashes_base_directory": "baseline",
        "file_hashes": {f"base-{n:02}.txt": sync.sha(files[f"references/sasis/baseline/base-{n:02}.txt"]) for n in range(19)},
        "control_file_hashes": {p: sync.sha((base / p).read_bytes()) for p in control_paths},
        "subject_files": [{"path": f"baseline/base-{n:02}.txt", "sha256": sync.sha(files[f"references/sasis/baseline/base-{n:02}.txt"])} for n in range(4)],
    }
    sync.save(root / "references/sasis/profile-manifest.json", manifest)
    assert len(sync.inventory(root)) == 36
    return {p: {"path": p, **e, "mode": "100644"} for p, e in sync.inventory(root).items()}


def case(name, extra=False):
    run = FIXTURES / name
    run.mkdir()
    staging = run / "staged-package"
    expected = package(staging)
    target = run / "installation"
    shutil.copytree(staging, target)
    for p in target.rglob("*"):
        if p.is_file():
            p.write_bytes(b"old synthetic bytes\r\n" + p.read_bytes())
    if extra:
        (target / "obsolete.txt").write_bytes(b"extra old fixture")
    return run, staging, target, run / "backups" / "dated-complete-backup", expected, sync.inventory(target)


def denied():
    exc = PermissionError(13, "Synthetic Windows directory rename refusal")
    exc.winerror = 5
    return exc


def record(name, **extra):
    RESULTS.append({"test": name, "pass": True, **extra})


# Dynamic profile cardinality and BOM/CRLF payload identity.
dynamic = FIXTURES / "dynamic-manifests"
dynamic.mkdir()
for controls, wanted in ((3, 26), (5, 28)):
    root = dynamic / str(wanted)
    package(root, controls=controls)
    manifest = sync.check_manifests(root, VERSION)
    assert manifest["operative_manifest_checks"] == wanted
    record(f"dynamic-manifest-{wanted}", actual=wanted, distinct_paths=manifest["distinct_checked_paths"])

# Whole directory replacement accepts old extras because no overlay occurs.
run, staging, target, backup, expected, before = case("whole-directory-with-obsolete-file", extra=True)
result = sync.install_transaction(staging, target, backup, run, expected, VERSION, lambda: None)
assert sync.inventory(target) == sync.byte_identities(expected)
assert sync.inventory(backup) == before and sync.inventory(run / "previous-installation") == before
assert not staging.exists() and not (target / "obsolete.txt").exists()
record("whole-directory-replaces-obsolete-file", backup_intact=True, payload_bom_and_newline_bytes_preserved=True)

# Windows rename-blocked equal-inventory fallback, preserving actual winerror.
run, staging, target, backup, expected, before = case("rename-blocked-fallback")
original_rename = Path.rename
def block_target(path, destination):
    if path == target:
        raise denied()
    return original_rename(path, destination)
with patch.object(Path, "rename", block_target):
    result = sync.install_transaction(staging, target, backup, run, expected, VERSION, lambda: None)
assert result["original_rename_failure"]["winerror"] == 5
assert sync.inventory(target) == sync.byte_identities(expected) and sync.inventory(backup) == before
record("blocked-rename-equal-inventory-fallback", preserved_winerror=5, backup_intact=True)

# Blocked rename with extras refuses file replacement and preserves original.
run, staging, target, backup, expected, before = case("rename-blocked-unequal-inventory", extra=True)
with patch.object(Path, "rename", block_target):
    rejection = expect_failure(lambda: sync.install_transaction(staging, target, backup, run, expected, VERSION, lambda: None))
assert sync.inventory(target) == before and sync.inventory(backup) == before
failure = sync.json_bytes((run / "installation-failure.json").read_bytes())
assert failure["generation_hold"] and not failure["destination_mutated"]
record("blocked-rename-unequal-inventory-refused", original_and_backup_intact=True, failure=rejection)

# One fallback write fails after prior writes: restore all original bytes.
run, staging, target, backup, expected, before = case("fallback-partial-write-rollback")
original_write = Path.write_bytes
write_count = [0]
def one_write_failure(path, raw):
    if path.is_relative_to(target):
        write_count[0] += 1
        if write_count[0] == 4:
            raise OSError("Synthetic fourth payload write failure")
    return original_write(path, raw)
with patch.object(Path, "rename", block_target), patch.object(Path, "write_bytes", one_write_failure):
    expect_failure(lambda: sync.install_transaction(staging, target, backup, run, expected, VERSION, lambda: None))
failure = sync.json_bytes((run / "installation-failure.json").read_bytes())
assert failure["generation_hold"] and failure["rollback"]["restored"]
assert sync.inventory(target) == before and sync.inventory(backup) == before
record("partial-fallback-write-rolls-back", original_and_backup_intact=True, generation_hold=True)

# Failed stage-to-target rename restores from preserved full backup.
run, staging, target, backup, expected, before = case("stage-promotion-failure")
def block_stage(path, destination):
    if path == staging:
        raise denied()
    return original_rename(path, destination)
with patch.object(Path, "rename", block_stage):
    expect_failure(lambda: sync.install_transaction(staging, target, backup, run, expected, VERSION, lambda: None))
failure = sync.json_bytes((run / "installation-failure.json").read_bytes())
assert failure["rollback"]["restored"] and failure["generation_hold"]
assert sync.inventory(target) == before and sync.inventory(backup) == before
record("failed-stage-directory-promotion-rolls-back", original_and_backup_intact=True)

# Any final publication/readback failure holds and restores after replacement.
run, staging, target, backup, expected, before = case("late-live-ref-failure")
live_checks = [0]
def fail_final_check():
    live_checks[0] += 1
    if live_checks[0] == 3:
        raise RuntimeError("Synthetic live main changed at final readback")
expect_failure(lambda: sync.install_transaction(staging, target, backup, run, expected, VERSION, fail_final_check))
failure = sync.json_bytes((run / "installation-failure.json").read_bytes())
assert failure["rollback"]["restored"] and failure["generation_hold"]
assert sync.inventory(target) == before and sync.inventory(backup) == before
assert sync.inventory(run / "failed-installation") == sync.byte_identities(expected)
record("late-live-ref-failure-restores-and-preserves-failed-installation", backup_intact=True, generation_hold=True)

# A final status-record write failure cannot bypass rollback or leave a valid pass.
run, staging, target, backup, expected, before = case("final-status-record-failure")
original_save = sync.save
def fail_success_hold(path, value):
    if path == run / "generation-hold.json" and value.get("generation_hold") is False:
        raise OSError("Synthetic final status-record write failure")
    return original_save(path, value)
with patch.object(sync, "save", fail_success_hold):
    expect_failure(lambda: sync.install_transaction(staging, target, backup, run, expected, VERSION, lambda: None))
failure = sync.json_bytes((run / "installation-failure.json").read_bytes())
verification = sync.json_bytes((run / "installation-verification.json").read_bytes())
assert failure["rollback"]["restored"] and failure["generation_hold"]
assert verification["generation_hold"] and verification["invalidated_after_installation_failure"]
assert sync.inventory(target) == before and sync.inventory(backup) == before
record("final-status-record-write-failure-restores-and-invalidates-pass", backup_intact=True, generation_hold=True)

# A persistent write failure prevents restoration; backup survives, never pass.
run, staging, target, backup, expected, before = case("rollback-itself-fails")
def persistent_write_failure(path, raw):
    if path.is_relative_to(target):
        raise OSError("Synthetic persistent payload write refusal")
    return original_write(path, raw)
with patch.object(Path, "rename", block_target), patch.object(Path, "write_bytes", persistent_write_failure):
    expect_failure(lambda: sync.install_transaction(staging, target, backup, run, expected, VERSION, lambda: None))
failure = sync.json_bytes((run / "installation-failure.json").read_bytes())
assert failure["generation_hold"] and not failure["rollback"]["restored"] and failure["rollback"]["manual_recovery_required"]
assert sync.inventory(backup) == before
record("rollback-failure-preserves-backup-and-holds", backup_intact=True, manual_recovery_required=True)

# Path guards: no traversal, alternate root, Windows ADS/name ambiguity or collision.
bad_paths = ["../outside", "/absolute", "C:/outside", "assets\\outside", "assets/a/../outside", "assets//file", "assets/NUL.txt", "assets/file. ", "assets/file:stream"]
for path in bad_paths:
    expect_failure(lambda path=path: sync.relative_path(path, package=True))
record("unsafe-paths-rejected", cases=len(bad_paths))
fixture_target = FIXTURES / "whole-directory-with-obsolete-file/installation"
with patch.object(sync, "AUTHORIZED", fixture_target):
    expect_failure(sync.authorized_target)
record("alternate-production-destination-rejected")

# A simulated reparse-point attribute is rejected before payload opening.
fake_reparse = FIXTURES / "fake-reparse"
fake_reparse.write_bytes(b"synthetic reparse fixture")
original_lstat = Path.lstat
def simulated_reparse_lstat(path, *args, **kwargs):
    if path == fake_reparse:
        class Info:
            st_mode = 0o100644
            st_file_attributes = 0x400
        return Info()
    return original_lstat(path, *args, **kwargs)
with patch.object(Path, "lstat", simulated_reparse_lstat):
    expect_failure(lambda: sync.checked_path(fake_reparse, exists=True))
record("windows-reparse-attribute-rejected", simulated=True)

# Complete Git package tree filtering uses local synthetic Git objects only.
repo = FIXTURES / "synthetic-git"
repo.mkdir()
expected = package(repo / "package")
for p in sorted(expected):
    dest = repo / p
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes((repo / "package" / p).read_bytes())
(repo / "prof.zip").write_bytes(b"excluded historical fixture")
(repo / "runs").mkdir()
(repo / "runs/evidence.json").write_bytes(b"{}")
subprocess.run(["git", "init", str(repo)], check=True, capture_output=True)
# Only existing package roots are added; absent agents/scripts are intentional fixtures.
subprocess.run(["git", "-C", str(repo), "-c", "core.autocrlf=false", "add", "SKILL.md", "assets", "references", "prof.zip", "runs"], check=True, capture_output=True)
subprocess.run(["git", "-C", str(repo), "-c", "user.name=PROF Synthetic Test", "-c", "user.email=synthetic@example.invalid", "-c", "core.hooksPath=NUL", "commit", "-m", "Synthetic package fixture"], check=True, capture_output=True)
commit = sync.git(repo, "rev-parse", "HEAD").decode().strip()
tree = sync.package_tree(repo, commit)
assert set(tree) == set(expected) and len(tree) == 36
for p, e in expected.items():
    raw = sync.git(repo, "cat-file", "blob", tree[p]["git_blob_sha"])
    assert raw == (repo / p).read_bytes() and sync.blob_sha(raw) == e["git_blob_sha"]
record("complete-immutable-git-package-filter-and-binary-identities", package_files=36, excluded=["prof.zip", "runs/evidence.json"], network_used=False)

input_data = {"schema": sync.INPUT_SCHEMA, "repository": sync.REPOSITORY, "remote": sync.REMOTE, "branch": "main", "commit": commit, "version": VERSION, "published_verification": {"verified": True, "immutable_commit": commit, "evidence": "Synthetic local object fixture only; never production"}, "operative_manifest_checks": 28, "package": list(expected.values())}
input_path = FIXTURES / "synthetic-inventory.json"
sync.save(input_path, input_data)
sync.request_input(input_path, commit, VERSION)
input_data["published_verification"]["verified"] = False
sync.save(input_path, input_data)
expect_failure(lambda: sync.request_input(input_path, commit, VERSION))
record("unverified-publication-input-rejected")

readback = {"at": sync.utc(), "helper": sync.helper_identity(), "fixture_root": str(FIXTURES), "synthetic_tests": RESULTS, "passed": len(RESULTS), "failed": 0, "production_cli_invoked": False, "actual_installed_prof_read_or_written_by_tests": False, "network_used": False, "dependency_installation_performed": False, "limitations": ["Synthetic mocked rename/write failures establish exercised control paths, not all Windows locking/filesystem failure modes.", "Reparse guard is tested using a simulated Windows attribute, not an actual junction.", "No production staging, installation, GitHub publication or post-installation readback was invoked."]}
sync.save(ROOT / "synthetic-test-readback.json", readback)
print(json.dumps({"passed": len(RESULTS), "failed": 0, "record": str(ROOT / "synthetic-test-readback.json"), "fixture_root": str(FIXTURES), "production_cli_invoked": False}))
