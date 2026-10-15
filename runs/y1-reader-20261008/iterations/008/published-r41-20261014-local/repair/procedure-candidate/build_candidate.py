"""Build only an unpublished r41 procedure proposal and non-subject fixture binding."""
import difflib
import hashlib
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parents[2]
INSTALLED=Path("C:/Users/alver/.codex/skills/prof")
R40=PROJECT/".prof-sasis/20261014-d008-r40"
PACKAGE=ROOT/"proposed-package"
TEMPLATES=ROOT/"templates"
SYNTH=ROOT/"synthetic-preflight"
R41_NOTE="2026-10-14-r41 repairs the verified r40 reader failure at B0024: a recopied proof-schema guard used prof-reader-reuse-store-v1 instead of prof-reader-reuse-proof-v1 and stopped before teaching. One independently verified bootstrap now retains the non-subject invoker and all per-step guards; later fixed two-line calls change only STEP_ID. The expression evaluates before the current canonical comparison, which precedes subject access. Frozen baseline/provenance identities are unchanged. Publication, fresh generation, complete fresh reading and affected-success evidence remain pending."


def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+"\n",encoding="utf-8")
def once(s,a,b):
    assert s.count(a)==1,(a[:100],s.count(a))
    return s.replace(a,b,1)
def module(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def main():
    assert not PACKAGE.exists() and not SYNTH.exists(),"Preserve prior candidate"
    TEMPLATES.mkdir(parents=True)
    failure=ROOT/"failure-evidence";failure.mkdir()
    report=(R40/"reader-report-original.md").read_bytes()
    (failure/"reader-report-original.md").write_bytes(report)
    source=report.decode().split("**Exact stopping call**",1)[1]
    call=re.search(r'```javascript\r?\n(.*?)\r?\n```',source,re.S).group(1)+"\n"
    (failure/"exact-failed-call.js").write_text(call,encoding="utf-8",newline="\n")
    save(failure/"identities.json",{"report_sha256":sha(report),"report_bytes":len(report),"exact_call_sha256":sha(call.encode()),"observed_failure":"At B0024 the reader changed proof.schema comparison to prof-reader-reuse-store-v1; stopped before adapter/subject access. Baseline incomplete; teaching never read.","read_scope":"Saved original execution report only; no original subject or live runtime access."})
    old=R40/"reader-preparation/templates"
    short=(old/"short_call_template.js").read_text(encoding="utf-8")
    body=once(short,'const STEP_ID = "B001";\n',"")
    body=once(body,'cached.schema !== "prof-reader-reuse-store-v1"','cached.schema !== "prof-reader-invoker-store-v1"')
    invoker='(async function retainedReaderInvoker(STEP_ID) {\nif (arguments.length !== 1) throw new Error("exactly one STEP_ID datum is accepted");\n'+body+'\n})\n'
    (TEMPLATES/"invoker_template.js").write_text(invoker,encoding="utf-8",newline="\n")
    (TEMPLATES/"short_call_template.js").write_text('const STEP_ID = "B001";\nawait eval(load("__STORE_KEY__").invoker_source)(STEP_ID);\n',encoding="utf-8",newline="\n")
    bootstrap=(old/"bootstrap_template.js").read_text(encoding="utf-8")
    bootstrap=bootstrap.replace('"prof-reader-reuse-store-v1"','"prof-reader-invoker-store-v1"')
    bootstrap=once(bootstrap,'typeof p.seal.adapter_source !== "string"','typeof p.seal.adapter_source !== "string" || typeof p.seal.invoker_source !== "string"')
    bootstrap=once(bootstrap,'short_call_sha256: p.seal.short_call_sha256,','short_call_sha256: p.seal.short_call_sha256, invoker_sha256: p.seal.invoker_sha256,')
    (TEMPLATES/"bootstrap_template.js").write_text(bootstrap,encoding="utf-8",newline="\n")
    verify=(old/"verify_reuse_template.py").read_text(encoding="utf-8")
    verify=once(verify,'"verify_reuse.py", "bootstrap_template.js", "short_call_template.js", "operating_instruction_template.md",','"verify_reuse.py", "bootstrap_template.js", "short_call_template.js", "operating_instruction_template.md", "invoker_template.js",')
    verify=once(verify,'    bootstrap = render(sources["bootstrap_template.js"], core_hash, core)','    invoker = render(sources["invoker_template.js"], core_hash, core)\n    bootstrap = render(sources["bootstrap_template.js"], core_hash, core)')
    verify=once(verify,'{"bootstrap.js": bootstrap, "short_call.js": short, "reader-operating.md": instruction}','{"invoker.js": invoker, "bootstrap.js": bootstrap, "short_call.js": short, "reader-operating.md": instruction}')
    verify=once(verify,'"schema": "prof-reader-reuse-store-v1"','"schema": "prof-reader-invoker-store-v1"')
    verify=once(verify,'"short_call_sha256": sha(short.encode()), "runtime_path": core["runtime_path"], "adapter_source": adapter','"short_call_sha256": sha(short.encode()), "runtime_path": core["runtime_path"], "invoker_sha256": sha(invoker.encode()), "invoker_source": invoker, "adapter_source": adapter')
    (TEMPLATES/"verify_reuse_template.py").write_text(verify,encoding="utf-8",newline="\n")
    changes={}
    for n in ("SKILL.md","references/sasis.md","references/sasis/student-role.txt","references/sasis/student-testing-contract.txt","references/sasis/profile-manifest.json"):
        changes[n]=(INSTALLED/n).read_text(encoding="utf-8")
    changes["SKILL.md"]=once(changes["SKILL.md"],'version: "2026-10-14-r40"','version: "2026-10-14-r41"')
    s=changes["references/sasis.md"]
    s=once(s,"Protocol revision: 2026-10-14-r40.","Protocol revision: 2026-10-14-r41.")
    oldparagraph=next(p for p in s.split("\n\n") if p.startswith("When the reader tool interface needs an operational wrapper"))
    newparagraph="When the reader tool interface needs an operational wrapper around that launcher, seal one fixed non-subject invoker containing all per-step schema, identity, retrieval, receipt and view checks. An exact explicitly authorised bootstrap independently verifies and retains that invoker without subject access. Subsequent calls use only a fixed invocation surface and the permitted STEP_ID datum; the reader must not reproduce or edit any guard, proof parser, hash, receipt or retrieval logic. On serializable-store interfaces such as functions.exec, the fixed two-line call may evaluate the retained invoker expression and pass STEP_ID; all guards stay inside the reused program. The expression evaluates before its current retained-source/envelope comparison. That comparison must use independently verified canonical metadata and reject changes before subject launcher or view access; do not claim authentication before evaluation, a persistent callable, or technical confinement. Only the bootstrap-verified designated non-subject program belongs in this position; subject bytes never may. Preserve all existing argument, order, range, hash, delivery and figure-view checks and stop/preserve without retry on failure. If this narrow reuse surface is unavailable, hold dependent dispatch and state the exact capability limit. Extract the four named [sealed invoker templates](#sealed-reader-invoker-templates) programmatically from this published reference and verify their exact bytes before binding; do not manually recreate their logic."
    changes["references/sasis.md"]=once(s,oldparagraph,newparagraph)
    oldsentence="Where a wrapper is needed, preflight that same sealed adapter, exact bootstrap and short call surface too: bootstrap retrieves no subject, successive valid step IDs reuse the same program, and an altered adapter identity fails before subject access."
    newsentence="Where a wrapper is needed, preflight that same sealed invoker, exact bootstrap and minimal invocation surface too: bootstrap retrieves no subject; successive step data reuse the same program without caller-authored guards; an altered retained source/envelope, missing/stale store, invalid/extra/out-of-order step, unread baseline revisit and truncated output stop before dependent access; and the observed proof/store schema-copy mistake is reproduced synthetically and absent from the repeated invocation surface. Check the actual evaluation order and preserve failures; source/envelope comparison occurs after invoker-expression evaluation and before subject launcher/view access."
    changes["references/sasis.md"]=once(changes["references/sasis.md"],oldsentence,newsentence)
    oldsentence="If a retrieval wrapper is supplied, use only its exact explicitly authorised verified non-subject bootstrap once, then reuse that same sealed adapter through its short step-ID-only call; change only the ID, without recopying or editing operational logic. Only that verified operational code may execute; subject bytes never may."
    newsentence="If a retrieval wrapper is supplied, use only its exact explicitly authorised verified non-subject bootstrap once, then the supplied fixed invocation changing only STEP_ID. All schema, identity, retrieval, receipt and view guards belong inside the same retained invoker; never reproduce or edit them in a later call. On the supplied two-line evaluation surface the designated invoker expression evaluates first, then its independent canonical source/envelope comparison must pass before subject launcher/view access; this is not pre-evaluation authentication or a persistent callable. Only the bootstrap-verified designated non-subject program may occupy that executable position; subject bytes never may."
    changes["references/sasis/student-role.txt"]=once(changes["references/sasis/student-role.txt"],oldsentence,newsentence)
    changes["references/sasis/student-testing-contract.txt"]=once(changes["references/sasis/student-testing-contract.txt"],"revision 2026-10-14-r40","revision 2026-10-14-r41")
    oldsentence="When a tool wrapper is needed, also seal and preflight one non-subject operational adapter and its exact explicitly authorised verified bootstrap, then reuse that same program through a short step-ID-only call; do not recopy hash or receipt logic per step, and never execute subject bytes."
    newsentence="When a tool wrapper is needed, seal and preflight one non-subject invoker containing every per-step schema/identity/retrieval/receipt/view guard and its exact explicitly authorised verified bootstrap. Later calls must contain only the supplied fixed invocation and permitted STEP_ID datum, with no reproduced guards or parsers. On serializable-store evaluation interfaces, independently verify the designated invoker at bootstrap; its expression evaluates before a current canonical source/envelope comparison that must reject changes before subject launcher/view access. Do not claim a persistent callable or pre-evaluation authentication. Never execute subject bytes. Include concrete same-surface checks for the observed proof/store schema-copy failure, retained identity changes, missing/stale store, bad/extra/out-of-order steps, baseline revisits, figure delivery and truncation."
    changes["references/sasis/student-testing-contract.txt"]=once(changes["references/sasis/student-testing-contract.txt"],oldsentence,newsentence)
    profile=json.loads(changes["references/sasis/profile-manifest.json"])
    profile["protocol_revision"]="2026-10-14-r41"
    profile["protocol_update_notes"].append(R41_NOTE)
    for key in ("student-role.txt","student-testing-contract.txt"):
        profile["control_file_hashes"][key]=sha(changes["references/sasis/"+key].encode())
    changes["references/sasis.md"] += "\n## Sealed reader invoker templates\n\nThese four named blocks are operational source templates, not subject content or reader role text. The orchestrator extracts their exact UTF-8 payload bytes programmatically between the named markers, including the final newline, then binds and seals them before dispatch. Keep them in this existing reference so the complete installed package inventory remains unchanged. The reader receives only the exact authorised bootstrap and two-line invocation, not PROF or these template instructions. The function expression evaluates before the reused program's current identity comparison; no pre-evaluation authentication or persistent-callable claim is made.\n"
    for name in ("invoker_template.js","bootstrap_template.js","short_call_template.js","verify_reuse_template.py"):
        language="python" if name.endswith(".py") else "javascript"
        changes["references/sasis.md"] += "\n<!-- PROF-READER-TEMPLATE-BEGIN: "+name+" -->\n```"+language+"\n"+(TEMPLATES/name).read_text(encoding="utf-8")+"```\n<!-- PROF-READER-TEMPLATE-END: "+name+" -->\n"
    profile["control_file_hashes"]["../sasis.md"]=sha(changes["references/sasis.md"].encode())
    profile["control_file_hashes"]["../../SKILL.md"]=sha(changes["SKILL.md"].encode())
    changes["references/sasis/profile-manifest.json"]=json.dumps(profile,indent=2,ensure_ascii=False)+"\n"
    diffs=[]
    for name,new in changes.items():
        p=PACKAGE/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(new,encoding="utf-8",newline="\n")
        oldtext=(INSTALLED/name).read_text(encoding="utf-8")
        diffs.extend(difflib.unified_diff(oldtext.splitlines(True),new.splitlines(True),fromfile="r40/"+name,tofile="r41/"+name))
    (ROOT/"proposed-controls.diff").write_text("".join(diffs),encoding="utf-8",newline="\n")
    # A new isolated synthetic fixture, with reviewed operational launcher/receipt/audit/adapter logic.
    SYNTH.mkdir()
    previous=R40/"reader-preparation/synthetic-preflight-r40"
    shutil.copyfile(previous/"synthetic-fixtures/four-quadrants.png",SYNTH/"figure.png")
    b=[b"Synthetic baseline alpha.\n",b"Synthetic baseline beta.\n"]
    t=[b"Synthetic teaching start.\n",b"Synthetic teaching end.\n"]
    (SYNTH/"baseline.txt").write_bytes(b"".join(b));(SYNTH/"teaching.txt").write_bytes(b"".join(t))
    blobs={"BFILE":b"".join(b),"TFILE":b"".join(t),"FIMAGE":(SYNTH/"figure.png").read_bytes()}
    filenames={"BFILE":"baseline.txt","TFILE":"teaching.txt","FIMAGE":"figure.png"}
    kinds={"BFILE":"baseline","TFILE":"teaching_text","FIMAGE":"teaching_figure"}
    files={fid:{"artifact_id":"synthetic-"+fid,"revision":"r41-fixture-1","kind":kinds[fid],"path":str(SYNTH/filenames[fid]),"size":len(raw),"sha256":sha(raw),"encoding":"binary-image" if fid=="FIMAGE" else "utf-8"} for fid,raw in blobs.items()}
    def step(i,f,a,raw):return {"id":i,"file_id":f,"start":a,"length":len(raw),"sha256":sha(raw),"kind":"figure" if f=="FIMAGE" else "text"}
    route={"schema":"sasis-fixed-route-v1","route_id":"SYNTHETIC_R41","revision":"non-subject-r41","range_convention":"zero-based-byte-start-length","files":files,"steps":[step("B001","BFILE",0,b[0]),step("B002","BFILE",len(b[0]),b[1]),step("T001","TFILE",0,t[0]),step("F001","FIMAGE",0,blobs["FIMAGE"]),step("T002","TFILE",len(t[0]),t[1])],"baseline_revisits":{"RB001":"B001","RB002":"B002"}}
    save(SYNTH/"frozen-route.json",route);rh=sha((SYNTH/"frozen-route.json").read_bytes())
    source=(R40/"reader-inputs/fixed_launcher.py").read_text(encoding="utf-8")
    source=re.sub(r'^CONFIG_PATH = .+$','CONFIG_PATH = Path("'+str(SYNTH/"frozen-route.json").replace("\\","/")+'")',source,flags=re.M)
    source=re.sub(r'^EXPECTED_CONFIG_SHA256 = .+$','EXPECTED_CONFIG_SHA256 = "'+rh+'"',source,flags=re.M)
    source=re.sub(r'^RUNTIME_DIR = .+$','RUNTIME_DIR = Path("'+str(SYNTH/"runtime").replace("\\","/")+'")',source,flags=re.M)
    (SYNTH/"fixed_launcher.py").write_text(source,encoding="utf-8",newline="\n")
    for n in ("record_receipt.py","audit_bound_run.py"):shutil.copyfile(R40/"reader-inputs"/n,SYNTH/n)
    adapter=(R40/"reader-inputs/operational_adapter.js").read_text(encoding="utf-8")
    for label,value in {"PYTHON":sys.executable.replace("\\","/"),"LAUNCHER":str(SYNTH/"fixed_launcher.py").replace("\\","/"),"RECEIPT":str(SYNTH/"record_receipt.py").replace("\\","/"),"ROUTE_SHA256":rh}.items():
        adapter=re.sub('^const '+label+r' = "[^"\n]+";$','const '+label+' = "'+value+'";',adapter,flags=re.M)
    (SYNTH/"operational_adapter.js").write_text(adapter,encoding="utf-8",newline="\n")
    for n in ("invoker_template.js","bootstrap_template.js","short_call_template.js"):shutil.copyfile(TEMPLATES/n,SYNTH/n)
    verify=(TEMPLATES/"verify_reuse_template.py").read_text(encoding="utf-8")
    for marker,value in {"__FIXED_ROUTE_FILENAME__":"frozen-route.json","__FIXED_RUNTIME_DIRNAME__":"runtime","__FIXED_SCOPE__":"synthetic r41 retained invoker","__FIXED_ROUTE_ID__":"SYNTHETIC_R41"}.items():verify=verify.replace(marker,value)
    (SYNTH/"verify_reuse.py").write_text(verify,encoding="utf-8",newline="\n")
    instruction="Synthetic r41 retained-invoker preflight. This exact non-subject bootstrap is authorised once and retrieves no fixture content. Later calls use only the fixed two-line surface and STEP_ID data. The invoker expression evaluates first; current canonical identity checks run inside it before subject launcher/view access. Preserve failures. Core __CORE_SHA256__; key __STORE_KEY__.\n"
    (SYNTH/"operating_instruction_template.md").write_text(instruction,encoding="utf-8",newline="\n")
    names=("verify_reuse.py","bootstrap_template.js","short_call_template.js","operating_instruction_template.md","invoker_template.js","operational_adapter.js","fixed_launcher.py","record_receipt.py","frozen-route.json")
    core={"schema":"prof-reader-reuse-core-v1","scope":"synthetic r41 retained invoker","python":sys.executable.replace("\\","/"),"store_key":"prof.reader.r41.synthetic.invoker1","route_sha256":rh,"route_path":str(SYNTH/"frozen-route.json").replace("\\","/"),"runtime_path":str(SYNTH/"runtime").replace("\\","/"),"files":{n:{"sha256":sha((SYNTH/n).read_bytes()),"bytes":(SYNTH/n).stat().st_size} for n in names}}
    save(SYNTH/"seal-core.json",core);digest=sha((SYNTH/"seal-core.json").read_bytes())
    verifier=module("r41_metadata_verifier",SYNTH/"verify_reuse.py")
    for a,z in (("invoker_template.js","invoker.js"),("bootstrap_template.js","bootstrap.js"),("short_call_template.js","short_call.js"),("operating_instruction_template.md","reader-operating.md")):
        (SYNTH/z).write_text(verifier.render((SYNTH/a).read_text(encoding="utf-8"),digest,core),encoding="utf-8",newline="\n")
    proof=verifier.proof("bootstrap",digest)
    assert not (SYNTH/"runtime").exists()
    assert len((SYNTH/"short_call.js").read_text(encoding="utf-8").splitlines())==2
    assert all(x not in (SYNTH/"short_call.js").read_text(encoding="utf-8") for x in ("schema","JSON","proof","receipt","exec_command"))
    save(ROOT/"candidate-identities.json",{"source_prof_commit":"2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce","source_prof_version":"2026-10-14-r40","proposed_version":"2026-10-14-r41","changed_existing_files":list(changes),"template_carrier":"references/sasis.md#sealed-reader-invoker-templates","extracted_template_files":[p.relative_to(ROOT).as_posix() for p in TEMPLATES.iterdir()],"complete_package_file_count_after_integration":36,"operative_manifest_checks_after_integration":28,"synthetic_core_sha256":digest,"synthetic_seal":{k:v for k,v in proof["seal"].items() if k not in ("adapter_source","invoker_source")},"installed_or_repository_mutated":False,"subject_or_production_runtime_access":False})
    print(json.dumps({"core_sha256":digest,"bootstrap_sha256":proof["seal"]["bootstrap_sha256"],"call_sha256":proof["seal"]["short_call_sha256"],"invoker_sha256":proof["seal"]["invoker_sha256"],"repeated_call_lines":2,"proposed_files":len(list(PACKAGE.rglob('*'))),"runtime_exists":(SYNTH/"runtime").exists()}))


if __name__=="__main__":main()
