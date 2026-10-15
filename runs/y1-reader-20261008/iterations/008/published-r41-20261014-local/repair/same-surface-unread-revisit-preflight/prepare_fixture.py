"""Bind a fresh subject-free fixture; never mutate the sealed reviewed candidate."""
import hashlib
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

R = Path(__file__).resolve().parent
C = R.parent / "procedure-candidate"
S = C / "synthetic-preflight"
KEY = "prof.reader.r41.unread_revisit.supplement1"

def sha(b): return hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p, x): p.write_text(json.dumps(x, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
def identity(p):
    b = p.read_bytes()
    return {"bytes": len(b), "sha256": sha(b)}
def slash(p): return str(p).replace("\\", "/")

assert not (R / "seal-core.json").exists(), "Fresh fixture only; preserve any existing run"
before = {p.relative_to(C).as_posix(): identity(p) for p in sorted(C.rglob("*")) if p.is_file()}
save(R / "reviewed-candidate-before.json", {"scope": slash(C), "files": before})
for name in ("baseline.txt", "teaching.txt", "figure.png", "verify_reuse.py", "record_receipt.py", "audit_bound_run.py", "bootstrap_template.js", "short_call_template.js", "invoker_template.js", "operating_instruction_template.md"):
    shutil.copyfile(S / name, R / name)

route = load(S / "frozen-route.json")
for spec in route["files"].values():
    spec["path"] = slash(R / Path(spec["path"]).name)
save(R / "frozen-route.json", route)
route_hash = sha((R / "frozen-route.json").read_bytes())
launcher = (S / "fixed_launcher.py").read_text(encoding="utf-8")
for label, value in {"CONFIG_PATH": 'Path("' + slash(R / "frozen-route.json") + '")', "EXPECTED_CONFIG_SHA256": '"' + route_hash + '"', "RUNTIME_DIR": 'Path("' + slash(R / "runtime") + '")'}.items():
    launcher, count = re.subn(r'^' + label + r' = .+$', label + " = " + value, launcher, flags=re.M)
    assert count == 1
(R / "fixed_launcher.py").write_text(launcher, encoding="utf-8", newline="\n")
adapter = (S / "operational_adapter.js").read_text(encoding="utf-8")
for label, value in {"PYTHON": slash(sys.executable), "LAUNCHER": slash(R / "fixed_launcher.py"), "RECEIPT": slash(R / "record_receipt.py"), "ROUTE_SHA256": route_hash}.items():
    adapter, count = re.subn(r'^const ' + label + r' = "[^"\n]+";$', 'const ' + label + ' = "' + value + '";', adapter, flags=re.M)
    assert count == 1
(R / "operational_adapter.js").write_text(adapter, encoding="utf-8", newline="\n")

core = load(S / "seal-core.json")
core.update({"python": slash(sys.executable), "store_key": KEY, "route_sha256": route_hash, "route_path": slash(R / "frozen-route.json"), "runtime_path": slash(R / "runtime")})
for name in core["files"]: core["files"][name] = identity(R / name)
save(R / "seal-core.json", core)
digest = sha((R / "seal-core.json").read_bytes())
spec = importlib.util.spec_from_file_location("supplement_metadata_verifier", R / "verify_reuse.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for source, target in (("invoker_template.js", "invoker.js"), ("bootstrap_template.js", "bootstrap.js"), ("short_call_template.js", "short_call.js"), ("operating_instruction_template.md", "reader-operating.md")):
    (R / target).write_text(m.render((R / source).read_text(encoding="utf-8"), digest, core), encoding="utf-8", newline="\n")
call = (R / "short_call.js").read_text(encoding="utf-8")
assert call.count('const STEP_ID = "B001";') == 1 and len(call.splitlines()) == 2
(R / "unread-revisit-call.js").write_text(call.replace('const STEP_ID = "B001";', 'const STEP_ID = "RB002";'), encoding="utf-8", newline="\n")
assert not (R / "runtime").exists()
proof = m.proof("bootstrap", digest)
save(R / "before-bootstrap.json", {"runtime_exists": False, "state": None, "effective_cursor": 0, "baseline_read": [], "subject_open_events": 0, "verified_accesses": 0})

def norm(text, kind):
    if kind == "launcher": return re.sub(r'^(CONFIG_PATH|EXPECTED_CONFIG_SHA256|RUNTIME_DIR) = .+$', r'\1 = <BOUND>', text, flags=re.M)
    if kind == "adapter": return re.sub(r'^const (PYTHON|LAUNCHER|RECEIPT|ROUTE_SHA256) = .+$', r'const \1 = <BOUND>', text, flags=re.M)
    return text
checks = []
for name, kind in (("fixed_launcher.py", "launcher"), ("operational_adapter.js", "adapter")):
    a = norm((S / name).read_text(encoding="utf-8"), kind); b = norm((R / name).read_text(encoding="utf-8"), kind)
    assert a == b
    checks.append({"file": name, "comparison": "identical after only enumerated fixed constants normalized", "normalized_sha256": sha(a.encode()), "pass": True})
for name in ("verify_reuse.py", "record_receipt.py", "audit_bound_run.py", "bootstrap_template.js", "short_call_template.js", "invoker_template.js", "operating_instruction_template.md", "baseline.txt", "teaching.txt", "figure.png"):
    assert (S / name).read_bytes() == (R / name).read_bytes()
    checks.append({"file": name, "comparison": "exact bytes identical", **identity(R / name), "pass": True})
oldcore = load(S / "seal-core.json"); olddigest = sha((S / "seal-core.json").read_bytes())
for name in ("invoker.js", "bootstrap.js", "short_call.js", "reader-operating.md"):
    a = (S / name).read_text(encoding="utf-8").replace(slash(S), "<FIXTURE_ROOT>").replace(oldcore["store_key"], "<STORE_KEY>").replace(olddigest, "<CORE_SHA256>")
    b = (R / name).read_text(encoding="utf-8").replace(slash(R), "<FIXTURE_ROOT>").replace(KEY, "<STORE_KEY>").replace(digest, "<CORE_SHA256>")
    assert a == b, name
    checks.append({"file": name, "comparison": "identical after only fixed fixture root, store key and sealed core digest normalized", "normalized_sha256": sha(a.encode()), "pass": True})
oldroute = load(S / "frozen-route.json")
for x in (route, oldroute):
    for f in x["files"].values(): f["path"] = "<FIXTURE_ROOT>/" + Path(f["path"]).name
assert route == oldroute
save(R / "identity-normalized-comparison.json", {"pass": True, "reviewed_source": slash(S), "checks": checks, "route_only_absolute_fixture_paths_changed": True, "unread_revisit_id": "RB002", "unread_target": "B002", "new_unique_store_key": KEY, "no_operational_logic_change": True, "no_new_dependency": True})
save(R / "bound-identities.json", {"scope": "Fresh non-subject same-surface unread-baseline-revisit preflight only", "core_sha256": digest, "route_sha256": route_hash, "store_key": KEY, "files": {name: identity(R / name) for name in ("seal-core.json", "frozen-route.json", "invoker.js", "bootstrap.js", "short_call.js", "unread-revisit-call.js", "verify_reuse.py", "operational_adapter.js", "fixed_launcher.py")}, "bootstrap_explicitly_authorized_once": True, "production_subject_or_runtime_access": False})
print(json.dumps({"prepared": True, "runtime_exists": False, "core_sha256": digest, "invoker_sha256": proof["seal"]["invoker_sha256"], "bootstrap_sha256": proof["seal"]["bootstrap_sha256"], "unread_call_sha256": sha((R / "unread-revisit-call.js").read_bytes()), "bootstrap": (R / "bootstrap.js").read_text(encoding="utf-8"), "call": (R / "unread-revisit-call.js").read_text(encoding="utf-8")}, indent=2))
