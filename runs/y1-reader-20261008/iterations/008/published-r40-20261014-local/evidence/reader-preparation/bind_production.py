"""Root-owned preparation: route/copy frozen inputs, seal reviewed operational code.

Subject bytes are read only as data for identity/copy/chronological boundaries.
This is not SASIS and never invokes production retrieval or creates its runtime.
"""
import copy
import hashlib
import importlib.util
import json
import re
import shutil
import struct
import sys
from pathlib import Path

PREP = Path(__file__).resolve().parent
RUN = PREP.parent
PROJECT = RUN.parents[1]
AUTHOR = RUN / "fresh-author"
OLD = PROJECT / ".prof-sasis/20261014-d008-r39/reader-inputs"
OUT = RUN / "reader-inputs"
COMMIT = "2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce"
BASELINE = Path("C:/Users/alver/.codex/skills/prof/references/sasis/ocr-baseline-20261007/student-baseline.txt")
BASE_HASH = "3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5"
MAX = 6000


def sha(b): return hashlib.sha256(b).hexdigest()
def save(p, x): p.write_bytes((json.dumps(x, indent=2, ensure_ascii=False) + "\n").encode())
def mod(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def one(source, pattern, replacement):
    source, count = re.subn(pattern, lambda m: replacement, source, flags=re.M)
    assert count == 1, (pattern, count)
    return source


def chunks(raw, start, end):
    result = []
    while start < end:
        stop = min(start + MAX, end)
        if stop < end:
            breaks = list(re.finditer(rb"\r?\n\r?\n", raw[start:stop]))
            if breaks: stop = start + breaks[-1].end()
            else:
                line = raw.rfind(b"\n", start, stop)
                assert line > start, "No coherent bounded line/paragraph boundary"
                stop = line + 1
        raw[start:stop].decode("utf-8")
        assert stop > start
        result.append((start, stop)); start = stop
    return result


def seal(directory, route, instruction, key, scope, default_step):
    route_raw = (json.dumps(route, indent=2, ensure_ascii=False) + "\n").encode()
    (directory / "frozen-route.json").write_bytes(route_raw)
    route_hash = sha(route_raw)
    source = (OLD / "fixed_launcher.py").read_text(encoding="utf-8")
    bound = one(source, r'^CONFIG_PATH = Path\("[^"\n]+"\)$', 'CONFIG_PATH = Path("' + str(directory / "frozen-route.json").replace("\\", "/") + '")')
    bound = one(bound, r'^EXPECTED_CONFIG_SHA256 = "[a-f0-9]{64}"$', 'EXPECTED_CONFIG_SHA256 = "' + route_hash + '"')
    bound = one(bound, r'^RUNTIME_DIR = Path\("[^"\n]+"\)$', 'RUNTIME_DIR = Path("' + str(directory / "runtime").replace("\\", "/") + '")')
    (directory / "fixed_launcher.py").write_text(bound, encoding="utf-8", newline="\n")
    for name in ("record_receipt.py", "audit_bound_run.py"):
        shutil.copyfile(OLD / name, directory / name)
    original = (OLD / "fixed_adapter.js").read_text(encoding="utf-8")
    adapter = one(original, r'^const STEP_ID = "[A-Za-z][A-Za-z0-9_-]{0,63}";\n', "")
    for label, value in {"PYTHON": sys.executable.replace("\\", "/"), "LAUNCHER": str(directory / "fixed_launcher.py").replace("\\", "/"), "RECEIPT": str(directory / "record_receipt.py").replace("\\", "/"), "ROUTE_SHA256": route_hash}.items():
        adapter = one(adapter, '^const ' + label + r' = "[^"\n]+";$', 'const ' + label + ' = "' + value + '";')
    (directory / "operational_adapter.js").write_text(adapter, encoding="utf-8", newline="\n")
    for name in ("bootstrap_template.js", "short_call_template.js"):
        raw = (PREP / "templates" / name).read_text(encoding="utf-8")
        if name == "short_call_template.js":
            raw = one(raw, r'^const STEP_ID = "B001";$', 'const STEP_ID = "' + default_step + '";')
        (directory / name).write_text(raw, encoding="utf-8", newline="\n")
    verifier = (PREP / "templates/verify_reuse_template.py").read_text(encoding="utf-8")
    for marker, value in {"__FIXED_ROUTE_FILENAME__": "frozen-route.json", "__FIXED_RUNTIME_DIRNAME__": "runtime", "__FIXED_SCOPE__": scope, "__FIXED_ROUTE_ID__": route["route_id"]}.items():
        verifier = verifier.replace(marker, value)
    (directory / "verify_reuse.py").write_text(verifier, encoding="utf-8", newline="\n")
    assert "{{" not in instruction
    (directory / "operating_instruction_template.md").write_text(instruction, encoding="utf-8", newline="\n")
    names = ("verify_reuse.py", "bootstrap_template.js", "short_call_template.js", "operating_instruction_template.md", "operational_adapter.js", "fixed_launcher.py", "record_receipt.py", "frozen-route.json")
    core = {"schema": "prof-reader-reuse-core-v1", "scope": scope, "python": sys.executable.replace("\\", "/"), "store_key": key,
            "route_sha256": route_hash, "route_path": str(directory / "frozen-route.json").replace("\\", "/"), "runtime_path": str(directory / "runtime").replace("\\", "/"),
            "files": {n: {"sha256": sha((directory / n).read_bytes()), "bytes": (directory / n).stat().st_size} for n in names}}
    save(directory / "seal-core.json", core)
    digest = sha((directory / "seal-core.json").read_bytes())
    verify = mod("metadata_verify_" + directory.name.replace("-", "_"), directory / "verify_reuse.py")
    for src, dest in (("bootstrap_template.js", "bootstrap.js"), ("short_call_template.js", "short_call.js"), ("operating_instruction_template.md", "reader-operating.md")):
        text = verify.render((directory / src).read_text(encoding="utf-8"), digest, core)
        (directory / dest).write_text(text, encoding="utf-8", newline="\n")
    proof = verify.proof("bootstrap", digest)
    assert not (directory / "runtime").exists()
    def norm_launcher(s):
        return re.sub(r'^(CONFIG_PATH|EXPECTED_CONFIG_SHA256|RUNTIME_DIR) = .+$', r'\1 = <BOUND>', s, flags=re.M)
    def norm_adapter(s):
        s = re.sub(r'^const STEP_ID = "[^"\n]+";\n', "", s, flags=re.M)
        return re.sub(r'^const (PYTHON|LAUNCHER|RECEIPT|ROUTE_SHA256) = .+$', r'const \1 = <BOUND>', s, flags=re.M)
    assert norm_launcher(source) == norm_launcher(bound)
    assert norm_adapter(original) == norm_adapter(adapter)
    assert (directory / "record_receipt.py").read_bytes() == (OLD / "record_receipt.py").read_bytes()
    assert (directory / "audit_bound_run.py").read_bytes() == (OLD / "audit_bound_run.py").read_bytes()
    return core, digest, proof


def build():
    assert not OUT.exists(), "Preserve any pre-existing production binding"
    OUT.mkdir()
    freeze = json.loads((AUTHOR / "evidence/teaching-freeze.json").read_text(encoding="utf-8"))
    assert len(freeze["files"]) == 6 and freeze["frozen_before_review"] is True
    controls = json.loads((PREP / "control-identities.json").read_text())
    for c in controls["checked_controls"]:
        assert sha(Path(c["installed_path"]).read_bytes()) == c["sha256"], "Published control changed"
    raw_baseline = BASELINE.read_bytes()
    assert len(raw_baseline) == 247840 and sha(raw_baseline) == BASE_HASH
    baseline_dest = OUT / "subjects/baseline/student-baseline.txt"
    baseline_dest.parent.mkdir(parents=True)
    baseline_dest.write_bytes(raw_baseline)
    assert baseline_dest.read_bytes() == raw_baseline and sha(baseline_dest.read_bytes()) == BASE_HASH
    files = {"BASELINE": {"artifact_id": "OCR-A-4-subjects-r1", "revision": "frozen-operational-20261007", "kind": "baseline", "path": str(baseline_dest), "size": len(raw_baseline), "sha256": BASE_HASH, "encoding": "utf-8"}}
    data = {"BASELINE": raw_baseline}
    file_ids = {"teaching/main.md": "MAIN", "teaching/hints.md": "HINTS", "teaching/solutions.md": "SOLUTIONS", "teaching/figures/log-tangent.png": "FIG01", "teaching/figures/trig-linear.png": "FIG02", "teaching/figures/cos-quadratic.png": "FIG03"}
    copy_verification = []
    dimensions = {}
    for spec in freeze["files"]:
        assert spec["path"] in file_ids
        original = AUTHOR / spec["path"]
        raw = original.read_bytes()
        assert len(raw) == spec["bytes"] and sha(raw) == spec["sha256"], "Frozen teaching mismatch"
        dest = OUT / "subjects" / spec["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(raw)
        assert dest.read_bytes() == raw and sha(dest.read_bytes()) == spec["sha256"]
        file_id = file_ids[spec["path"]]
        figure = file_id.startswith("FIG")
        files[file_id] = {"artifact_id": "D008-r40-" + file_id, "revision": COMMIT, "kind": "teaching_figure" if figure else "teaching_text", "path": str(dest), "size": len(raw), "sha256": sha(raw), "encoding": "binary-image" if figure else "utf-8"}
        data[file_id] = raw
        if figure:
            assert raw[:8] == b"\x89PNG\r\n\x1a\n"
            dimensions[file_id] = list(struct.unpack(">II", raw[16:24]))
        copy_verification.append({"file_id": file_id, "source": str(original), "destination": str(dest), "bytes": len(raw), "sha256": sha(raw), "complete_byte_copy_verified": True})
    assert dimensions == {"FIG03": [1350,810], "FIG01": [1350,810], "FIG02": [1560,690]}
    steps = []; boundaries = []; revisits = {}
    def add(step_id, file_id, start, stop):
        raw = data[file_id][start:stop]
        steps.append({"id": step_id, "file_id": file_id, "start": start, "length": len(raw), "sha256": sha(raw), "kind": "figure" if file_id.startswith("FIG") else "text"})
    for i, (start, stop) in enumerate(chunks(raw_baseline, 0, len(raw_baseline)), 1):
        step = "B" + str(i).zfill(4); add(step, "BASELINE", start, stop); revisits["R" + step] = step
    baseline_count = len(steps)
    raw = data["MAIN"]
    cuts = {0, len(raw)}
    for m in re.finditer(rb'^<a id="main-d008-[^"]+"></a>\r?\n', raw, flags=re.M):
        cuts.add(m.start()); boundaries.append({"kind": "section_or_attempt_anchor", "file_id": "MAIN", "byte": m.start(), "line": raw[:m.start()].count(b"\n")+1})
    figures = {}
    for m in re.finditer(rb'^<img src="figures/([^"]+\.png)"[^\n]*\r?\n', raw, flags=re.M):
        rel = "teaching/figures/" + m.group(1).decode()
        fid = file_ids[rel]
        assert fid not in figures.values()
        cuts.add(m.end()); figures[m.end()] = fid
        boundaries.append({"kind": "complete_figure_first_use_after_image_tag", "file_id": "MAIN", "byte": m.end(), "line": raw[:m.start()].count(b"\n")+1, "figure_id": fid, "dimensions": dimensions[fid]})
    assert list(figures.values()) == ["FIG01", "FIG02", "FIG03"]
    index = 0
    ordered = sorted(cuts)
    for start, stop in zip(ordered, ordered[1:]):
        for a,b in chunks(raw,start,stop):
            index += 1; add("M"+str(index).zfill(4),"MAIN",a,b)
        if stop in figures:
            fid = figures[stop]; add("F"+fid[-2:],fid,0,len(data[fid]))
    for fid, prefix in (("HINTS","H"),("SOLUTIONS","S")):
        raw = data[fid]
        cuts = {0,len(raw)}
        for m in re.finditer(rb'^<a id="[^"\n]+"></a>\r?\n',raw,flags=re.M): cuts.add(m.start())
        index = 0; ordered = sorted(cuts)
        for start,stop in zip(ordered,ordered[1:]):
            for a,b in chunks(raw,start,stop): index+=1;add(prefix+str(index).zfill(4),fid,a,b)
    route = {"schema":"sasis-fixed-route-v1","route_id":"D008_R40_FROZEN_2102C1FC","revision":COMMIT,"range_convention":"zero-based-byte-start-length","files":files,"steps":steps,"baseline_revisits":revisits}
    route_hash = sha((json.dumps(route,indent=2,ensure_ascii=False)+"\n").encode())
    report = str(RUN / "reader-report-original.md").replace("\\","/")
    inst = (PREP / "operating_instruction_template.md").read_text(encoding="utf-8")
    for key,value in {"FROZEN_BASELINE_ID_AND_REVISION":"OCR-A-4-subjects-r1 / frozen-operational-20261007 / SHA256 "+BASE_HASH,"FROZEN_TEACHING_ID_AND_REVISION":"D008-r40-fresh-author-1 / "+COMMIT,"FROZEN_ROUTE_ID_AND_HASH":route["route_id"]+" / SHA256 "+route_hash,"READER_REPORT_DESTINATION":report,"READER_CONDITION_ID":"D008-r40-instruction-confined-fixed-reuse-1"}.items(): inst = inst.replace("{{"+key+"}}",value)
    inst += "\nNon-subject control identities (sealed with this instruction):\n" + "\n".join(c["path"]+" SHA256 "+c["sha256"] for c in controls["checked_controls"]) + "\n"
    core,digest,proof = seal(OUT,route,inst,"prof.reader.d008.r40.2102c1fc.condition1","production instruction-confined D008 r40",steps[0]["id"])
    runner = mod("production_metadata_only",OUT/"fixed_launcher.py")
    runner.validate_config(route)
    coverage=[]
    for fid,spec in files.items():
        spans=[s for s in steps if s["file_id"]==fid];position=0
        for s in spans:
            assert s["start"]==position and sha(data[fid][position:position+s["length"]])==s["sha256"]
            position+=s["length"]
        assert position==spec["size"]
        coverage.append({"file_id":fid,"exact_contiguous_bytes":position,"step_count":len(spans),"sha256":spec["sha256"],"complete":True})
    negatives=[]
    for name,mutate in (("duplicate_step",lambda c:c["steps"].insert(0,copy.deepcopy(c["steps"][0]))),("skip_first_span",lambda c:c["steps"].pop(0)),("reverse_order",lambda c:c["steps"].reverse()),("incomplete_figure",lambda c:next(s for s in c["steps"] if s["kind"]=="figure").update(length=1))):
        bad=copy.deepcopy(route);mutate(bad)
        try:runner.validate_config(bad)
        except runner.Denied as e:negatives.append({"name":name,"rejected":True,"reason":str(e),"subject_opens":0})
        else:raise AssertionError(name)
    message=(PREP/"dispatch_authorization_template.md").read_text(encoding="utf-8")
    values={"FROZEN_BASELINE_ID_AND_REVISION":"OCR-A-4-subjects-r1 / frozen-operational-20261007","FROZEN_TEACHING_ID_AND_REVISION":"D008-r40-fresh-author-1 / "+COMMIT,"BOUND_BOOTSTRAP_SHA256":proof["seal"]["bootstrap_sha256"],"EXACT_BOUND_BOOTSTRAP_BODY":(OUT/"bootstrap.js").read_text(),"BOUND_SHORT_CALL_SHA256":proof["seal"]["short_call_sha256"],"EXACT_BOUND_SHORT_CALL_BODY":(OUT/"short_call.js").read_text(),"SUBJECT_FREE_ROUTE_DELIVERY_OR_IMMUTABLE_LOCATOR":"Complete route metadata is inline below; do not issue a separate metadata-read command.\n\n```json\n"+(OUT/"frozen-route.json").read_text()+"```","READER_REPORT_DESTINATION":report}
    for key,value in values.items():message=message.replace("{{"+key+"}}",value)
    assert "{{" not in message and "__CORE" not in message
    (OUT/"reader-launch-message.txt").write_text(message,encoding="utf-8",newline="\n")
    save(OUT/"binding-validation.json",{"state":"bound_verified_pending_synthetic_preflight_root_review","subject_reads_scope":"Identity, copying and chronological structural routing only; no SASIS or diagnosis","published_commit":COMMIT,"baseline_bytes":len(raw_baseline),"baseline_sha256":BASE_HASH,"teaching_copies":copy_verification,"coverage":coverage,"baseline_step_count":baseline_count,"total_steps":len(steps),"baseline_revisit_count":len(revisits),"structural_boundaries":boundaries,"metadata_only_negative_validation":negatives,"core_sha256":digest,"seal":{k:v for k,v in proof["seal"].items() if k!="adapter_source"},"operational_logic_unchanged_except_allowed_bindings":True,"receipt_and_audit_byte_unchanged":True,"production_launcher_invoked":False,"production_runtime_exists":False,"reader_dispatched":False,"control_identities":controls})
    save(OUT/"binding-inventory.json",{"files":{str(p.relative_to(OUT)).replace("\\","/"):{"bytes":p.stat().st_size,"sha256":sha(p.read_bytes())} for p in OUT.rglob("*") if p.is_file() and "__pycache__" not in p.parts}})
    print(json.dumps({"steps":len(steps),"baseline_steps":baseline_count,"constituents":len(files),"core_sha256":digest,"route_sha256":route_hash,"bootstrap_sha256":proof["seal"]["bootstrap_sha256"],"short_call_sha256":proof["seal"]["short_call_sha256"],"launch_message_sha256":sha(message.encode()),"runtime_exists":(OUT/"runtime").exists()}))


if __name__ == "__main__":build()
