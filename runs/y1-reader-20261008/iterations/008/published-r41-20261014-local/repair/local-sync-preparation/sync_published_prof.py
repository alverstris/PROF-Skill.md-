"""Stage/verify a root-supplied published PROF pin; install only by explicit command.

No dependency installation. Package payloads always move as binary bytes. The CLI
has no destination override: production installation is confined to AUTHORIZED.
Synthetic tests call the transaction core with separate, confined fixture paths.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
REMOTE = "https://github.com/alverstris/PROF-Skill.md-.git"
REPOSITORY = "alverstris/PROF-Skill.md-"
AUTHORIZED = Path("C:/Users/alver/.codex/skills/prof")
BACKUP_ROOT = Path("C:/Users/alver/.codex/skill-backups/prof")
BOUNDARIES = {"agents", "assets", "references", "scripts"}
INPUT_SCHEMA = "prof-verified-published-package-v1"
RECORD_SCHEMA = "prof-staged-published-package-v1"
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}\Z")
RESERVED = {"CON", "PRN", "AUX", "NUL", *("COM" + str(n) for n in range(1, 10)), *("LPT" + str(n) for n in range(1, 10))}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def strict_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON object key")
        result[key] = value
    return result


def json_bytes(raw):
    return json.loads(raw.decode("utf-8-sig"), object_pairs_hook=strict_pairs)


def save(path, value):
    # Records contain no command output, credentials, or environment dumps.
    path.write_bytes((json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def error_record(exc):
    # Do not disclose subprocess stderr/stdout (which can contain credential URLs).
    if isinstance(exc, subprocess.SubprocessError):
        return {"type": type(exc).__name__, "message": "Git command failed; command output suppressed", "returncode": getattr(exc, "returncode", None)}
    result = {"type": type(exc).__name__, "message": str(exc), "errno": getattr(exc, "errno", None), "winerror": getattr(exc, "winerror", None)}
    if getattr(exc, "__notes__", None):
        result["notes"] = list(exc.__notes__)
    return result


def reject_link(path):
    info = path.lstat()
    require(not stat.S_ISLNK(info.st_mode), "Linked path forbidden: " + str(path))
    require(not (getattr(info, "st_file_attributes", 0) & 0x400), "Windows reparse point forbidden: " + str(path))


def checked_path(path, *, exists=False):
    path = Path(os.path.abspath(path))
    # Check all existing ancestors as well as the final component.
    chain = [path, *path.parents]
    for part in reversed(chain):
        if os.path.lexists(part):
            reject_link(part)
    require(os.path.normcase(str(path.resolve(strict=exists))) == os.path.normcase(str(path)), "Resolved path differs: " + str(path))
    return path


def child(root, relative, *, exists=False):
    root = checked_path(root, exists=True)
    path = checked_path(root / relative, exists=exists)
    require(path != root and path.is_relative_to(root), "Path is outside confined root")
    return path


def relative_path(value, *, package=False):
    require(isinstance(value, str) and value, "Relative path must be a nonempty string")
    require("\\" not in value and ":" not in value and not any(ord(c) < 32 for c in value), "Unsafe path syntax")
    p = PurePosixPath(value)
    require(not p.is_absolute() and p.as_posix() == value, "Noncanonical relative path")
    require(all(part not in {"", ".", ".."} and part.rstrip(" .") == part and part.split(".")[0].upper() not in RESERVED for part in p.parts), "Unsafe Windows path component")
    if package:
        require(value == "SKILL.md" or (len(p.parts) > 1 and p.parts[0] in BOUNDARIES), "Path outside the root skill package")
    return value


def manifest_path(root, manifest_parent, fragment):
    # Control maps legitimately contain ../sasis.md and ../../SKILL.md.
    require(isinstance(fragment, str) and fragment and "\\" not in fragment and ":" not in fragment and not fragment.startswith("/"), "Unsafe manifest path")
    require(not any(ord(c) < 32 for c in fragment), "Unsafe manifest path characters")
    resolved = checked_path(manifest_parent / fragment, exists=True)
    require(resolved.is_file() and resolved.is_relative_to(checked_path(root, exists=True)), "Manifest path outside the package")
    relative_path(resolved.relative_to(root).as_posix(), package=True)
    return resolved


def inventory(root):
    root = checked_path(root, exists=True)
    require(root.is_dir(), "Inventory root is not a directory")
    result = {}
    folded = set()
    for directory, directories, files in os.walk(root, followlinks=False):
        for name in directories + files:
            path = checked_path(Path(directory) / name, exists=True)
            rel = relative_path(path.relative_to(root).as_posix())
            require(rel.casefold() not in folded, "Case-insensitive path collision")
            folded.add(rel.casefold())
            require(path.is_dir() or path.is_file(), "Nonordinary filesystem entry")
        for name in files:
            path = child(root, (Path(directory) / name).relative_to(root), exists=True)
            raw = path.read_bytes()
            result[path.relative_to(root).as_posix()] = {"bytes": len(raw), "sha256": sha(raw), "git_blob_sha": blob_sha(raw)}
    return dict(sorted(result.items()))


def byte_identities(package):
    return {p: {k: e[k] for k in ("bytes", "sha256", "git_blob_sha")} for p, e in sorted(package.items())}


def version_of(root):
    raw = child(root, "SKILL.md", exists=True).read_bytes()
    matches = re.findall(r'^  version: "([^"\r\n]+)"\s*$', raw.decode("utf-8-sig"), re.MULTILINE)
    require(len(matches) == 1, "SKILL.md version is absent or ambiguous")
    return matches[0]


def check_manifests(root, expected_version):
    # The operative profile is explicit. Historical frozen-release/download
    # manifests also contain unavailable archive paths and are provenance, not
    # replacement package dependencies. Parse every JSON without rewriting it.
    parsed = {}
    for p in sorted(root.rglob("*.json")):
        checked_path(p, exists=True)
        parsed[p.relative_to(root).as_posix()] = json_bytes(p.read_bytes())
    key = "references/sasis/profile-manifest.json"
    require(key in parsed, "Missing operative profile manifest")
    m = parsed[key]
    require(isinstance(m, dict) and m.get("protocol_revision") == expected_version, "Profile revision differs from requested PROF version")
    require(isinstance(m.get("file_hashes"), dict) and m["file_hashes"], "Missing baseline hash map")
    require(isinstance(m.get("control_file_hashes"), dict) and m["control_file_hashes"], "Missing control hash map")
    require(isinstance(m.get("subject_files"), list) and m["subject_files"], "Missing subject hash records")
    base = root / "references/sasis"
    baseline_base = manifest_path_directory(root, base, m.get("file_hashes_base_directory"))
    checks = [("file_hashes", p, baseline_base, h) for p, h in m["file_hashes"].items()]
    checks += [("control_file_hashes", p, base, h) for p, h in m["control_file_hashes"].items()]
    for e in m["subject_files"]:
        require(isinstance(e, dict) and isinstance(e.get("path"), str), "Invalid subject manifest record")
        checks.append(("subject_files", e["path"], base, e.get("sha256")))
    results = []
    for field, fragment, parent, expected in checks:
        require(isinstance(expected, str) and HEX64.fullmatch(expected), "Invalid declared manifest digest")
        path = manifest_path(root, parent, fragment)
        actual = sha(path.read_bytes())
        require(actual == expected, "Operative manifest hash mismatch: " + path.relative_to(root).as_posix())
        results.append({"manifest": key, "field": field, "declared_path": fragment, "package_path": path.relative_to(root).as_posix(), "expected_sha256": expected, "actual_sha256": actual, "pass": True})
    require(version_of(root) == expected_version, "Installed/staged SKILL version mismatch")
    return {"checks": results, "operative_manifest_checks": len(results), "distinct_checked_paths": len({e["package_path"] for e in results}), "json_files_parsed": len(parsed), "historical_provenance_hashes_rewritten": False}


def manifest_path_directory(root, base, fragment):
    require(isinstance(fragment, str), "Missing file_hashes_base_directory")
    relative_path(fragment)
    result = checked_path(base / fragment, exists=True)
    require(result.is_dir() and result.is_relative_to(checked_path(root, exists=True)), "Manifest base escapes package")
    return result


def request_input(path, commit, version):
    raw = Path(path).read_bytes()
    data = json_bytes(raw)
    require(data.get("schema") == INPUT_SCHEMA, "Input must be a verified-published package record")
    require(data.get("repository") == REPOSITORY and data.get("remote") == REMOTE and data.get("branch") == "main", "Incorrect repository identity")
    require(data.get("commit") == commit and data.get("version") == version, "Root-supplied pin/version differ from input")
    verification = data.get("published_verification", {})
    require(verification.get("verified") is True and verification.get("immutable_commit") == commit and isinstance(verification.get("evidence"), str) and verification["evidence"].strip(), "Root must supply actual immutable-publication verification evidence")
    entries = data.get("package")
    require(isinstance(entries, list) and entries, "Complete package inventory is required")
    package = {}
    folded = set()
    for e in entries:
        require(isinstance(e, dict), "Invalid inventory entry")
        p = relative_path(e.get("path"), package=True)
        require(p.casefold() not in folded, "Duplicate/colliding inventory path")
        folded.add(p.casefold())
        require(type(e.get("bytes")) is int and e["bytes"] >= 0, "Invalid byte length")
        require(isinstance(e.get("sha256"), str) and HEX64.fullmatch(e["sha256"]), "Invalid SHA256")
        require(isinstance(e.get("git_blob_sha"), str) and HEX40.fullmatch(e["git_blob_sha"]), "Invalid Git blob SHA")
        require(e.get("mode") in {"100644", "100755"}, "Linked/non-file Git mode forbidden")
        package[p] = dict(e)
    require("SKILL.md" in package, "Missing root SKILL.md")
    count = data.get("operative_manifest_checks")
    require(type(count) is int and count > 0, "Root must supply the independently verified operative-manifest count")
    return raw, data, dict(sorted(package.items()))


def git(repo, *args):
    proc = subprocess.run(["git", "-c", "credential.helper=", "-C", str(repo), *args], capture_output=True, check=True)
    return proc.stdout


def remote_main(repo):
    require(git(repo, "remote", "get-url", "origin").decode().strip() == REMOTE, "Git origin identity differs")
    lines = git(repo, "ls-remote", "origin", "refs/heads/main").decode("ascii").splitlines()
    require(len(lines) == 1 and lines[0].split()[1] == "refs/heads/main", "Main ref response invalid")
    commit = lines[0].split()[0]
    require(HEX40.fullmatch(commit), "Main ref is not a SHA1 commit")
    return commit


def package_tree(repo, commit):
    require(git(repo, "rev-parse", commit + "^{commit}").decode().strip() == commit, "Downloaded object is not requested commit")
    result = {}
    folded = set()
    for entry in filter(None, git(repo, "ls-tree", "-rz", "--full-tree", commit).split(b"\0")):
        meta, name = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        p = name.decode("utf-8")
        if p == "SKILL.md" or p.split("/")[0] in BOUNDARIES:
            relative_path(p, package=True)
            require(p.casefold() not in folded, "Git tree case-insensitive path collision")
            folded.add(p.casefold())
            require(mode in {"100644", "100755"} and kind == "blob", "Nonordinary package Git entry")
            result[p] = {"mode": mode, "git_blob_sha": oid}
    return dict(sorted(result.items()))


def run_directory(run_id, *, new=False):
    require(RUN_ID.fullmatch(run_id), "Unsafe run ID")
    base = checked_path(ROOT, exists=True)
    runs = checked_path(base / "runs")
    if new:
        runs.mkdir(exist_ok=True)
    require(runs.is_dir(), "Missing preparation runs directory")
    run = child(runs, run_id, exists=not new)
    if new:
        require(not run.exists(), "Run already exists; use a new run ID")
        run.mkdir()
    return run


def helper_identity():
    return {"path": str(Path(__file__).resolve()), "sha256": sha(Path(__file__).read_bytes())}


def stage(args):
    require(HEX40.fullmatch(args.commit), "A full immutable 40-character commit is required")
    require(re.fullmatch(r"[A-Za-z0-9_.-]+", args.version), "Unsafe version string")
    run = run_directory(args.run_id, new=True)
    save(run / "generation-hold.json", {"generation_hold": True, "reason": "Staging/install/readback not yet complete", "at": utc()})
    try:
        raw, input_data, expected = request_input(args.inventory, args.commit, args.version)
        (run / "root-verified-published-input.json").write_bytes(raw)
        repo = run / "repository.git"
        git(run, "init", "--bare", str(repo))
        git(repo, "remote", "add", "origin", REMOTE)
        require(remote_main(repo) == args.commit, "Live main differs from root-supplied published pin")
        git(repo, "fetch", "--no-tags", "--depth=1", "origin", args.commit)
        require(remote_main(repo) == args.commit, "Live main changed while downloading")
        tree = package_tree(repo, args.commit)
        require(set(tree) == set(expected), "Root-supplied inventory is not the complete package at the published commit")
        require(all(tree[p] == {"mode": e["mode"], "git_blob_sha": e["git_blob_sha"]} for p, e in expected.items()), "Published Git tree differs from independently verified inventory")
        staging = run / "staged-package"
        staging.mkdir()
        for p, e in expected.items():
            raw_blob = git(repo, "cat-file", "blob", e["git_blob_sha"])
            require(len(raw_blob) == e["bytes"] and sha(raw_blob) == e["sha256"] and blob_sha(raw_blob) == e["git_blob_sha"], "Downloaded Git blob bytes differ: " + p)
            destination = child(staging, p)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw_blob)
        require(inventory(staging) == byte_identities(expected), "Staged inventory/bytes differ")
        manifest = check_manifests(staging, args.version)
        require(manifest["operative_manifest_checks"] == input_data["operative_manifest_checks"], "Actual manifest count differs from verified publication record")
        require(remote_main(repo) == args.commit, "Live main changed during staging verification")
        save(run / "staged-manifest-checks.json", manifest)
        record = {"schema": RECORD_SCHEMA, "repository": REPOSITORY, "remote": REMOTE, "branch": "main", "commit": args.commit, "version": args.version, "verified_at": utc(), "helper": helper_identity(), "root_input_sha256": sha(raw), "git_tree_sha": git(repo, "rev-parse", args.commit + "^{tree}").decode().strip(), "live_main_equals_pin": True, "stage": str(staging), "git_repository": str(repo), "package_files": len(expected), "operative_manifest_checks": manifest["operative_manifest_checks"], "package": expected, "generation_hold": True, "new_lecture_acceptance_claimed": False}
        save(run / "staging-verification.json", record)
        print(json.dumps({"result": "staged-and-verified", "record": str(run / "staging-verification.json"), "commit": args.commit, "package_files": len(expected), "operative_manifest_checks": manifest["operative_manifest_checks"], "generation_hold": True}))
    except BaseException as exc:
        save(run / "staging-failure.json", {"at": utc(), "error": error_record(exc), "generation_hold": True, "destination_mutated": False})
        raise


def loaded_stage(run, commit):
    record = json_bytes((run / "staging-verification.json").read_bytes())
    require(record.get("schema") == RECORD_SCHEMA and record.get("commit") == commit, "Staging record pin differs")
    require(record.get("helper") == helper_identity(), "Helper changed after staging; create and verify a new run")
    raw, data, expected = request_input(run / "root-verified-published-input.json", commit, record["version"])
    require(sha(raw) == record["root_input_sha256"] and expected == record["package"], "Staged root input record changed")
    repo = child(run, "repository.git", exists=True)
    require(str(repo) == record["git_repository"], "Staged repository path changed")
    tree = package_tree(repo, commit)
    require(set(tree) == set(expected) and all(tree[p] == {"mode": e["mode"], "git_blob_sha": e["git_blob_sha"]} for p, e in expected.items()), "Stored immutable Git package changed")
    return record, data, expected, repo


def authorized_target():
    require(os.name == "nt", "Production install is only available on the authorized Windows computer")
    target = checked_path(AUTHORIZED, exists=True)
    require(target == Path(os.path.abspath("C:/Users/alver/.codex/skills/prof")) and target.is_dir(), "Destination is not the exact authorized PROF directory")
    return target


def write_complete_equal_inventory(source, destination, expected_destination_paths):
    require(set(inventory(destination)) == set(expected_destination_paths), "Every-file replacement forbidden for unequal inventory")
    for p in sorted(expected_destination_paths):
        src = child(source, p, exists=True)
        dest = child(destination, p, exists=True)
        require(src.is_file() and dest.is_file(), "Replacement path is not a confined ordinary file")
        dest.write_bytes(src.read_bytes())


def restore_backup(target, backup, before, run):
    require(inventory(backup) == before, "Backup is not intact; preserve it and hold generation")
    failed = child(run, "failed-installation")
    require(not failed.exists(), "Failed-installation evidence path already exists")
    if target.exists():
        checked_path(target, exists=True)
        try:
            target.rename(failed)
        except OSError as exc:
            failure = error_record(exc)
            write_complete_equal_inventory(backup, target, before)
            require(inventory(target) == before, "Rollback file-content readback failed")
            return {"restored": True, "method": "equal-inventory complete byte restoration from preserved verified backup", "rollback_rename_failure": failure, "backup_preserved": True}
    shutil.copytree(backup, target)
    require(inventory(target) == before and inventory(backup) == before, "Whole-directory backup restoration readback failed")
    return {"restored": True, "method": "complete copy from preserved verified backup into absent destination", "failed_installation_preserved": str(failed) if failed.exists() else None, "backup_preserved": True}


def install_transaction(stage_root, target, backup, run, expected, version, check_live_main, *, record_name="installation-verification.json", context=None):
    """Core transaction; CLI supplies only the fixed authorized production target."""
    expected_bytes = byte_identities(expected)
    require(inventory(stage_root) == expected_bytes, "Stage inventory/bytes changed before installation")
    manifest_before = check_manifests(stage_root, version)
    checked_path(target, exists=True)
    checked_path(backup)
    require(not backup.exists() and not backup.is_relative_to(target) and not target.is_relative_to(backup), "Backup is not a new external directory")
    before = inventory(target)
    displaced = child(run, "previous-installation")
    require(not displaced.exists(), "Previous-installation evidence path already exists")
    check_live_main()
    attempt = {**(context or {}), "at": utc(), "destination": str(target), "backup": str(backup), "stage": str(stage_root), "before": before, "generation_hold": True, "original_rename_failure": None, "backup_complete_inventory_and_bytes_match": False, "new_lecture_acceptance_claimed": False}
    save(run / "installation-attempt.json", attempt)
    mutated = False
    try:
        backup.parent.mkdir(parents=True, exist_ok=True)
        checked_path(backup.parent, exists=True)
        shutil.copytree(target, backup)
        require(inventory(backup) == before and inventory(target) == before, "Complete backup readback failed or installation changed during backup")
        attempt["backup_complete_inventory_and_bytes_match"] = True
        save(run / "installation-attempt.json", attempt)
        check_live_main()
        try:
            target.rename(displaced)
        except OSError as exc:
            attempt["original_rename_failure"] = error_record(exc)
            save(run / "installation-attempt.json", attempt)
            require(target.is_dir() and not displaced.exists() and inventory(target) == before, "Blocked rename left unexpected filesystem state")
            require(set(before) == set(expected_bytes), "Fallback forbidden: existing and staged relative file inventories differ")
            require(inventory(backup) == before, "Fallback forbidden: full backup verification failed")
            mutated = True
            write_complete_equal_inventory(stage_root, target, expected_bytes)
            method = "equal-inventory complete file-content replacement after full verified backup; actual directory-rename failure retained"
        else:
            mutated = True
            require(inventory(displaced) == before and not target.exists(), "Renamed old installation failed readback")
            stage_root.rename(target)
            method = "whole-directory replacement from verified stage after full verified dated backup"
        require(inventory(target) == expected_bytes, "Complete installed inventory/byte readback failed")
        manifests = check_manifests(target, version)
        require(manifests == manifest_before, "Installed operative-manifest readback differs from staged check")
        require(inventory(backup) == before, "Backup changed during installation")
        check_live_main()
        result = {**attempt, "verified_at": utc(), "method": method, "installed_files_overwritten_and_verified": len(expected_bytes), "package": expected, "manifest_checks": manifests["operative_manifest_checks"], "complete_installed_inventory_and_bytes_equal_pin": True, "backup_complete_inventory_and_bytes_match": True, "generation_hold": False, "previous_installation_directory": str(displaced) if displaced.exists() else None}
        save(run / "installed-manifest-checks.json", manifests)
        save(run / record_name, result)
        save(run / "generation-hold.json", {"generation_hold": False, "reason": "Complete local installation and pinned published package verified; root must reread installed controls before generation", "at": utc()})
        return result
    except BaseException as exc:
        failure = {**attempt, "failed_at": utc(), "error": error_record(exc), "generation_hold": True, "destination_mutated": mutated, "rollback": {"attempted": False, "backup_preserved": backup.exists()}}
        # Restoration must run even when the initiating failure is a record-write
        # error (disk full, permissions). Persist failure evidence afterwards.
        if mutated:
            try:
                failure["rollback"] = {"attempted": True, **restore_backup(target, backup, before, run)}
            except BaseException as rollback_exc:
                failure["rollback"] = {"attempted": True, "restored": False, "error": error_record(rollback_exc), "backup_preserved": backup.exists(), "manual_recovery_required": True}
        persistence_errors = []
        def persist(path, value):
            try:
                save(path, value)
            except BaseException as write_exc:
                persistence_errors.append({"path": str(path), "error": error_record(write_exc)})
        verification_path = run / record_name
        if verification_path.exists():
            try:
                previous_verification = json_bytes(verification_path.read_bytes())
            except BaseException:
                previous_verification = {"original_verification_record_unreadable": True}
            persist(run / "installation-verification-before-failure.json", previous_verification)
            persist(verification_path, {"generation_hold": True, "invalidated_after_installation_failure": True, "failure_record": str(run / "installation-failure.json"), "new_lecture_acceptance_claimed": False})
        persist(run / "generation-hold.json", {"generation_hold": True, "reason": "Installation/readback failed; do not generate from this installation", "at": utc()})
        failure["record_persistence_errors"] = persistence_errors
        persist(run / "installation-failure.json", failure)
        if persistence_errors and hasattr(exc, "add_note"):
            exc.add_note("Failure records could not all be saved; generation remains held. Preserve the complete backup and inspect the installation before recovery.")
        raise


def install(args):
    run = run_directory(args.run_id)
    require(HEX40.fullmatch(args.commit), "A full immutable commit is required")
    record, data, expected, repo = loaded_stage(run, args.commit)
    require(not (run / "installation-attempt.json").exists(), "Installation run already attempted; preserve it and stage a new run")
    target = authorized_target()
    stage_root = child(run, "staged-package", exists=True)
    require(str(stage_root) == record["stage"], "Stage path changed")
    require(check_manifests(stage_root, record["version"])["operative_manifest_checks"] == data["operative_manifest_checks"], "Manifest count changed")
    backup_root = checked_path(BACKUP_ROOT)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    backup = checked_path(backup_root / (stamp + "-before-" + record["version"] + "-" + args.commit[:12]))
    def live_check():
        require(remote_main(repo) == args.commit, "Live main differs from the verified immutable pin; hold generation")
    context = {"repository": REPOSITORY, "commit": args.commit, "prof_revision": record["version"], "helper": helper_identity(), "staging_record_sha256": sha((run / "staging-verification.json").read_bytes())}
    result = install_transaction(stage_root, target, backup, run, expected, record["version"], live_check, context=context)
    print(json.dumps({"result": "installed-and-verified", "record": str(run / "installation-verification.json"), "commit": args.commit, "backup": str(backup), "method": result["method"], "original_rename_failure": result["original_rename_failure"], "generation_hold": False}))


def verify_installed(args):
    run = run_directory(args.run_id)
    try:
        record, data, expected, repo = loaded_stage(run, args.commit)
        target = authorized_target()
        installation = json_bytes((run / "installation-verification.json").read_bytes())
        require(installation.get("commit") == args.commit and installation.get("generation_hold") is False, "No successful installation bound to this pin")
        require(remote_main(repo) == args.commit, "Live main differs from installed pin")
        require(inventory(target) == byte_identities(expected), "Installed inventory/byte readback differs from pin")
        manifests = check_manifests(target, record["version"])
        require(manifests["operative_manifest_checks"] == data["operative_manifest_checks"], "Installed manifest count differs")
        backup = checked_path(Path(installation["backup"]), exists=True)
        require(backup.parent == checked_path(BACKUP_ROOT, exists=True) and inventory(backup) == installation["before"], "Recorded backup identity differs")
        require(remote_main(repo) == args.commit, "Live main changed during final readback")
        result = {"at": utc(), "repository": REPOSITORY, "commit": args.commit, "version": record["version"], "destination": str(target), "backup": str(backup), "package_files": len(expected), "operative_manifest_checks": manifests["operative_manifest_checks"], "installed_inventory_bytes_and_manifests_match": True, "backup_intact": True, "generation_hold": False, "new_lecture_acceptance_claimed": False}
        save(run / "post-install-readback.json", result)
        save(run / "generation-hold.json", {"generation_hold": False, "reason": "Fresh complete installed readback passed; root must reread the installed controls before generation", "at": utc()})
        print(json.dumps(result))
    except BaseException as exc:
        save(run / "generation-hold.json", {"generation_hold": True, "reason": "Final installed readback failed; preserve backup and hold generation", "at": utc()})
        save(run / "post-install-readback-failure.json", {"at": utc(), "error": error_record(exc), "generation_hold": True, "action": "Read-only check made no installation mutation; preserve the verified backup and resolve before generation"})
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    stage_parser = sub.add_parser("stage", help="Download current verified published pin to isolated binary staging; never install")
    stage_parser.add_argument("--commit", required=True)
    stage_parser.add_argument("--version", required=True)
    stage_parser.add_argument("--inventory", required=True)
    stage_parser.add_argument("--run-id", required=True)
    for name in ("install", "verify-installed"):
        command = sub.add_parser(name)
        command.add_argument("--run-id", required=True)
        command.add_argument("--commit", required=True)
    args = parser.parse_args()
    try:
        {"stage": stage, "install": install, "verify-installed": verify_installed}[args.command](args)
    except BaseException as exc:
        print(json.dumps({"result": "failed", "error": error_record(exc), "generation_hold": True}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
