"""Metadata/code-only identity proof. Never reads or executes subject files.

Run only after the fixed wrapper checks this file's SHA256. All paths are fixed
within this directory. This is instruction confinement, not a caller sandbox.
"""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = ROOT / "seal-core.json"
EXPECTED_NAMES = {
    "verify_reuse.py", "bootstrap_template.js", "short_call_template.js", "operating_instruction_template.md", "invoker_template.js",
    "operational_adapter.js", "fixed_launcher.py", "record_receipt.py", "__FIXED_ROUTE_FILENAME__",
}
ID = re.compile(r"[A-Za-z][A-Za-z0-9_-]{0,63}\Z")


def require(ok, why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def unique(raw):
    def pairs(items):
        d = {}
        for k, v in items:
            require(k not in d, "duplicate metadata key")
            d[k] = v
        return d
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs)


def render(template, core_hash, core):
    verifier = str(ROOT / "verify_reuse.py").replace("\\", "/")
    # Get-FileHash runs before Python executes the identity verifier.
    command = ("$v='" + verifier + "'; if ((Get-FileHash -LiteralPath $v -Algorithm SHA256).Hash.ToLowerInvariant() -ne '" + core["files"]["verify_reuse.py"]["sha256"] + "') { throw 'verifier identity mismatch' }; & '" + core["python"] + "' $v")
    for marker, value in {"__VERIFY_COMMAND__": command, "__CORE_SHA256__": core_hash, "__STORE_KEY__": core["store_key"]}.items():
        template = template.replace(marker, value)
    require("__" not in template, "unbound wrapper marker")
    return template


def proof(mode, core_hash, step_id=None):
    raw = CORE.read_bytes()
    require(len(raw) < 100000 and sha(raw) == core_hash, "sealed binding hash mismatch")
    core = unique(raw)
    require(type(core) is dict and set(core) == {"schema", "scope", "python", "store_key", "route_sha256", "route_path", "runtime_path", "files"}, "invalid core shape")
    require(core["schema"] == "prof-reader-reuse-core-v1" and core["scope"] == "__FIXED_SCOPE__", "wrong binding schema/scope")
    require(type(core["files"]) is dict and set(core["files"]) == EXPECTED_NAMES, "unpermitted operational path set")
    sources = {}
    for name, spec in core["files"].items():
        require(type(spec) is dict and set(spec) == {"sha256", "bytes"}, "invalid operational identity shape")
        require(type(spec["bytes"]) is int and 0 < spec["bytes"] < 1000000, "invalid operational extent")
        data = (ROOT / name).read_bytes()
        require(len(data) == spec["bytes"] and sha(data) == spec["sha256"], "operational identity mismatch: " + name)
        sources[name] = data.decode("utf-8")
    require(core["route_path"] == str(ROOT / "__FIXED_ROUTE_FILENAME__").replace("\\", "/"), "route path binding mismatch")
    require(core["runtime_path"] == str(ROOT / "__FIXED_RUNTIME_DIRNAME__").replace("\\", "/"), "runtime binding mismatch")
    require(core["route_sha256"] == core["files"]["__FIXED_ROUTE_FILENAME__"]["sha256"], "route hash binding mismatch")
    require(Path(core["python"]).is_absolute() and "'" not in core["python"] and "'" not in str(ROOT), "unsafe fixed command path")
    spec = importlib.util.spec_from_file_location("sealed_metadata_only_launcher", ROOT / "fixed_launcher.py")
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    require(str(runner.CONFIG_PATH).replace("\\", "/") == core["route_path"] and runner.EXPECTED_CONFIG_SHA256 == core["route_sha256"] and str(runner.RUNTIME_DIR).replace("\\", "/") == core["runtime_path"], "launcher route/runtime binding mismatch")
    config = runner.load_config()  # Bounded metadata read + pure metadata validation only.
    require(config["route_id"] == "__FIXED_ROUTE_ID__", "unpermitted fixture route")
    adapter = sources["operational_adapter.js"]
    require(adapter.count("await readerStep(STEP_ID);") == 1 and not re.search(r"const STEP_ID\s*=", adapter), "invalid parameterized adapter shape")
    require('const ROUTE_SHA256 = "' + core["route_sha256"] + '";' in adapter, "adapter route binding mismatch")
    invoker = render(sources["invoker_template.js"], core_hash, core)
    bootstrap = render(sources["bootstrap_template.js"], core_hash, core)
    short = render(sources["short_call_template.js"], core_hash, core)
    instruction = render(sources["operating_instruction_template.md"], core_hash, core)
    for name, text in {"invoker.js": invoker, "bootstrap.js": bootstrap, "short_call.js": short, "reader-operating.md": instruction}.items():
        require((ROOT / name).read_bytes() == text.encode("utf-8"), "derived bootstrap/wrapper/instruction identity mismatch: " + name)
    seal = {"schema": "prof-reader-invoker-store-v1", "binding_sha256": core_hash,
            "adapter_sha256": core["files"]["operational_adapter.js"]["sha256"],
            "route_sha256": core["route_sha256"], "bootstrap_sha256": sha(bootstrap.encode()),
            "short_call_sha256": sha(short.encode()), "runtime_path": core["runtime_path"], "invoker_sha256": sha(invoker.encode()), "invoker_source": invoker, "adapter_source": adapter}
    result = {"schema": "prof-reader-reuse-proof-v1", "mode": mode, "seal": seal}
    if mode == "bootstrap":
        result["instruction"] = instruction
    else:
        require(type(step_id) is str and ID.fullmatch(step_id), "exactly one plain STEP_ID is accepted")
        result["step_id"] = step_id
    return result


def main():
    try:
        require(len(sys.argv) in (3, 4), "invalid identity-verifier argument shape")
        mode, digest = sys.argv[1:3]
        require(mode in ("bootstrap", "step") and re.fullmatch(r"[a-f0-9]{64}", digest), "invalid verification mode/hash")
        require(len(sys.argv) == (3 if mode == "bootstrap" else 4), "mode argument shape mismatch")
        result = proof(mode, digest, sys.argv[3] if mode == "step" else None)
        sys.stdout.buffer.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")).encode("utf-8") + b"\n")
        return 0
    except Exception as exc:
        sys.stderr.write(json.dumps({"ok": False, "error": str(exc)}) + "\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
