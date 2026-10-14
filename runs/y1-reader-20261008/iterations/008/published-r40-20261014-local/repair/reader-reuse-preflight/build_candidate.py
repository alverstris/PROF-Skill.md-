"""Create a separate synthetic reuse candidate, never touch real reader inputs."""
import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INFRA = ROOT.parent / "reader-infrastructure"


def main():
    if (ROOT / "seal-core.json").exists():
        raise SystemExit("Candidate already sealed: preserve it and use a new candidate directory.")
    for name in ("launcher_template.py", "receipt_template.py", "adapter_template.js", "audit_template.py", "bind_synthetic.py", "inspect_synthetic_runtime.py"):
        shutil.copyfile(INFRA / name, ROOT / name)
    spec = importlib.util.spec_from_file_location("candidate_fixture_builder", ROOT / "bind_synthetic.py")
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    builder.build()
    original = (ROOT / "fixed_adapter.js").read_text(encoding="utf-8")
    needle = 'const STEP_ID = "B001";\n'
    assert original.count(needle) == 1
    adapter = original.replace(needle, "", 1)
    (ROOT / "operational_adapter.js").write_text(adapter, encoding="utf-8", newline="\n")
    shutil.copyfile(ROOT / "audit_template.py", ROOT / "audit_bound_run.py")
    names = ("verify_reuse.py", "bootstrap_template.js", "short_call_template.js", "operating_instruction_template.md", "operational_adapter.js", "fixed_launcher.py", "record_receipt.py", "synthetic-route.json")
    files = {name: {"sha256": hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), "bytes": (ROOT / name).stat().st_size} for name in names}
    core = {"schema": "prof-reader-reuse-core-v1", "scope": "synthetic non-subject only", "python": sys.executable.replace("\\", "/"),
            "store_key": "prof.reader.reuse.synthetic.r40.candidate1", "route_sha256": files["synthetic-route.json"]["sha256"],
            "route_path": str(ROOT / "synthetic-route.json").replace("\\", "/"), "runtime_path": str(ROOT / "synthetic-runtime").replace("\\", "/"), "files": files}
    raw = (json.dumps(core, indent=2) + "\n").encode("utf-8")
    (ROOT / "seal-core.json").write_bytes(raw)
    digest = hashlib.sha256(raw).hexdigest()
    import verify_reuse
    for source, target in (("bootstrap_template.js", "bootstrap.js"), ("short_call_template.js", "short_call.js"), ("operating_instruction_template.md", "reader-operating.md")):
        (ROOT / target).write_text(verify_reuse.render((ROOT / source).read_text(encoding="utf-8"), digest, core), encoding="utf-8", newline="\n")
    verify_reuse.proof("bootstrap", digest)
    identity = {"core_sha256": digest, "file_hashes": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in (*names, "bootstrap.js", "short_call.js", "reader-operating.md")},
                "operational_transformation": "Exact bound adapter_template.js with exactly one const STEP_ID = B001 declaration removed; terminal readerStep(STEP_ID) unchanged.",
                "scope": "synthetic candidate only; original r39 evidence and current reader-inputs untouched"}
    (ROOT / "tested-identities.json").write_text(json.dumps(identity, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"sealed": True, "core_sha256": digest, "verifier_sha256": files["verify_reuse.py"]["sha256"], "bootstrap": str(ROOT / "bootstrap.js"), "short_call": str(ROOT / "short_call.js")}))


if __name__ == "__main__":
    main()
