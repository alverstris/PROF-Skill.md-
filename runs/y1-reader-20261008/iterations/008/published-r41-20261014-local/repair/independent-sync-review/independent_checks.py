"""Independent bounded review; no network, production stage or installation."""
from pathlib import Path
import ast
import contextlib
import hashlib
import io
import json
import shutil
import types
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
OWNER = CASE / "local-sync-preparation"
EXPECTED_HELPER = "cb0c8b31a3d857edc3d8ed47f79afea61d7b3a752061c14f94f76a888b86b5f0"
PIN = "a" * 40


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": sha(raw)}


def write(name, value):
    (HERE / name).write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def rejected(call, contains):
    try:
        call()
    except Exception as exc:
        assert contains in str(exc), (contains, str(exc))
        return {"type": type(exc).__name__, "message": str(exc)}
    raise AssertionError("Expected rejection")


sources = {}
snapshots = HERE / "inspected-sources"
snapshots.mkdir(exist_ok=True)
for name in ("sync_published_prof.py", "test_sync_synthetic.py", "README.md", "verified-published-input.TEMPLATE.json", "synthetic-test-readback.json", "preparation-verification.json"):
    raw = (OWNER / name).read_bytes()
    sources[name] = {"bytes": len(raw), "sha256": sha(raw)}
    (snapshots / name).write_bytes(raw)
assert sources["sync_published_prof.py"]["sha256"] == EXPECTED_HELPER
prepared = json.loads((OWNER / "preparation-verification.json").read_bytes())
assert all(sources[p] == e for p, e in prepared["files"].items())
write("inspected-source-identities.json", sources)

sync = types.ModuleType("independently_reviewed_sync")
sync.__file__ = str(OWNER / "sync_published_prof.py")
exec(compile((OWNER / "sync_published_prof.py").read_bytes(), sync.__file__, "exec"), sync.__dict__)

# Read-only full real installed inventory, checked against earlier sealed r40 identities.
installed_before = sync.inventory(Path("C:/Users/alver/.codex/skills/prof"))
prior = json.loads((CASE / "independent-candidate-review/package-and-manifests/package-inventory-and-identities.json").read_bytes())
assert len(installed_before) == len(prior["files"]) == 36
assert set(installed_before) == {e["path"] for e in prior["files"]}
for e in prior["files"]:
    assert installed_before[e["path"]] == {"bytes": e["source_bytes"], "sha256": e["source_sha256"], "git_blob_sha": e["source_git_blob_sha"]}
installed_manifests = sync.check_manifests(Path("C:/Users/alver/.codex/skills/prof"), "2026-10-14-r40")
assert installed_manifests["operative_manifest_checks"] == 26
write("real-installed-readonly-check.json", {"files": installed_before, "manifests": installed_manifests, "production_mutation": False})

template = json.loads((OWNER / "verified-published-input.TEMPLATE.json").read_bytes())
assert len(template["package"]) == 36 and template["operative_manifest_checks"] == 28
proposed = {e["path"]: e for e in prior["files"]}
for e in template["package"]:
    p = proposed[e["path"]]
    assert (e["bytes"], e["sha256"], e["git_blob_sha"]) == (p["proposed_bytes"], p["proposed_sha256"], p["proposed_git_blob_sha"])
assert template["published_verification"]["verified"] is False and template["commit"] is None

tree = ast.parse((OWNER / "sync_published_prof.py").read_text(encoding="utf-8"))
arguments = sorted({n.args[0].value for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "add_argument" and n.args and isinstance(n.args[0], ast.Constant)})
assert arguments == ["--commit", "--inventory", "--run-id", "--version"]

# Separate synthetic fixture: exercise only readback/guard functions with all
# production routing and live-ref access replaced by explicit local fixtures.
fixture = HERE / "bounded-readback-fixture"
fixture.mkdir()
source_fixture = Path(json.loads((OWNER / "synthetic-test-readback.json").read_bytes())["fixture_root"]) / "whole-directory-with-obsolete-file"
target = fixture / "installation"
backup = fixture / "backups/retained"
shutil.copytree(source_fixture / "installation", target)
shutil.copytree(source_fixture / "backups/dated-complete-backup", backup)
expected = {p: {"path": p, **e, "mode": "100644"} for p, e in sync.inventory(target).items()}
before = sync.inventory(backup)
sync.save(fixture / "installation-verification.json", {"commit": PIN, "generation_hold": False, "backup": str(backup), "before": before})
record = {"version": "synthetic-r41"}
data = {"operative_manifest_checks": 28}
args = types.SimpleNamespace(run_id="synthetic-review", commit=PIN)
events = []
with patch.object(sync, "run_directory", return_value=fixture), patch.object(sync, "loaded_stage", return_value=(record, data, expected, fixture)), patch.object(sync, "authorized_target", return_value=target), patch.object(sync, "BACKUP_ROOT", backup.parent), patch.object(sync, "remote_main", return_value=PIN):
    with contextlib.redirect_stdout(io.StringIO()):
        sync.verify_installed(args)
    assert json.loads((fixture / "generation-hold.json").read_bytes())["generation_hold"] is False
    events.append({"test": "initial-complete-readback", "pass": True})
    with patch.object(sync, "remote_main", return_value="b" * 40):
        failure = rejected(lambda: sync.verify_installed(args), "Live main differs")
    assert json.loads((fixture / "generation-hold.json").read_bytes())["generation_hold"] is True
    assert sync.inventory(target) == sync.byte_identities(expected) and sync.inventory(backup) == before
    events.append({"test": "read-only-ref-failure-holds-and-preserves-bytes", "pass": True, "error": failure})
    with contextlib.redirect_stdout(io.StringIO()):
        sync.verify_installed(args)
    assert json.loads((fixture / "generation-hold.json").read_bytes())["generation_hold"] is False
    assert (fixture / "post-install-readback-failure.json").exists()
    events.append({"test": "fresh-success-clears-hold-with-historical-failure-retained", "pass": True})

# Actual loaded_stage checks: helper byte binding and raw root-input identity.
guard = HERE / "bounded-identity-fixture"
guard.mkdir()
(guard / "repository.git").mkdir()
published = dict(template)
published.update(commit=PIN, published_verification={"verified": True, "immutable_commit": PIN, "evidence": "Independent synthetic fixture only; not publication evidence"})
sync.save(guard / "root-verified-published-input.json", published)
raw_input = (guard / "root-verified-published-input.json").read_bytes()
expected_input = {e["path"]: e for e in template["package"]}
staged = {"schema": sync.RECORD_SCHEMA, "commit": PIN, "helper": sync.helper_identity(), "version": template["version"], "root_input_sha256": sha(raw_input), "package": expected_input, "git_repository": str(guard / "repository.git")}
sync.save(guard / "staging-verification.json", staged)
fake_tree = {p: {"mode": e["mode"], "git_blob_sha": e["git_blob_sha"]} for p, e in expected_input.items()}
with patch.object(sync, "package_tree", return_value=fake_tree):
    sync.loaded_stage(guard, PIN)
    with patch.object(sync, "helper_identity", return_value={"path": sync.__file__, "sha256": "0" * 64}):
        failure = rejected(lambda: sync.loaded_stage(guard, PIN), "Helper changed after staging")
    events.append({"test": "changed-helper-rejected-before-dependent-tree", "pass": True, "error": failure})
    (guard / "root-verified-published-input.json").write_bytes(raw_input.replace(b"\n", b"\r\n"))
    failure = rejected(lambda: sync.loaded_stage(guard, PIN), "Staged root input record changed")
    events.append({"test": "semantically-identical-raw-input-byte-change-rejected", "pass": True, "error": failure})

# Existing installation-attempt is terminal: no destination authorization reached.
sync.save(fixture / "installation-attempt.json", {"synthetic": True})
hold_before = (fixture / "generation-hold.json").read_bytes()
with patch.object(sync, "run_directory", return_value=fixture), patch.object(sync, "loaded_stage", return_value=(record, data, expected, fixture)), patch.object(sync, "authorized_target", side_effect=AssertionError("Destination must not be reached")):
    failure = rejected(lambda: sync.install(args), "Installation run already attempted")
assert (fixture / "generation-hold.json").read_bytes() == hold_before
events.append({"test": "repeat-install-refused-before-destination-with-original-record-retained", "pass": True, "error": failure, "interpretation": "A failed command is not permission to reuse an older pass; README requires successful exits and current full readback."})

assert sync.inventory(Path("C:/Users/alver/.codex/skills/prof")) == installed_before
assert all(identity(OWNER / name) == value for name, value in sources.items())
write("independent-check-results.json", {"helper_sha256": EXPECTED_HELPER, "source_records_match": True, "template_matches_all_36_reviewed_candidate_identities": True, "template_is_not_verified_publication_input": True, "only_cli_options": arguments, "real_installed_r40_files_unchanged": 36, "real_installed_dynamic_manifest_checks": 26, "candidate_template_manifest_checks": 28, "tests": events, "production_stage_or_install_invoked": False, "network_used": False, "owner_files_modified": False, "limits": ["Readback tests route only to synthetic copies inside this review tree.", "No production CLI staging, installation, GitHub fetch or publication was performed.", "Point-in-time checks do not prevent concurrent external mutation."]})
print(json.dumps({"helper": EXPECTED_HELPER, "independent_tests": len(events), "installed_files": 36, "actual_installed_r40_operative_checks": 26, "candidate_template_checks": 28, "errors": 0}))
