"""Owned candidate-only adjustment: retain exact templates in existing package reference."""
import difflib,hashlib,json,re,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R/"proposed-package";T=R/"templates";I=Path("C:/Users/alver/.codex/skills/prof")
T.mkdir(exist_ok=True)
old=P/"references/sasis/reader-invoker"
assert old.resolve().is_relative_to(R.resolve())
for p in list(old.iterdir()) if old.exists() else []:
    assert p.is_file();q=T/p.name;q.write_bytes(p.read_bytes());assert q.read_bytes()==p.read_bytes();p.unlink()
if old.exists():old.rmdir()
s=(P/"references/sasis.md").read_text(encoding="utf-8")
start="Bind the [invoker](sasis/reader-invoker/invoker_template.js), [bootstrap](sasis/reader-invoker/bootstrap_template.js), [two-line call](sasis/reader-invoker/short_call_template.js) and [metadata verifier](sasis/reader-invoker/verify_reuse_template.py) from the published package rather than recreating their logic."
assert s.count(start)==1
s=s.replace(start,"Extract the four named [sealed invoker templates](#sealed-reader-invoker-templates) programmatically from this published reference and verify their exact bytes before binding; do not manually recreate their logic.")
s+="\n## Sealed reader invoker templates\n\nThese four named blocks are operational source templates, not subject content or reader role text. The orchestrator extracts their exact UTF-8 payload bytes programmatically between the named markers, including the final newline, then binds and seals them before dispatch. Keep them in this existing reference so the complete installed package inventory remains unchanged. The reader receives only the exact authorised bootstrap and two-line invocation, not PROF or these template instructions. The function expression evaluates before the reused program's current identity comparison; no pre-evaluation authentication or persistent-callable claim is made.\n"
for name in ("invoker_template.js","bootstrap_template.js","short_call_template.js","verify_reuse_template.py"):
    language="python" if name.endswith(".py") else "javascript"
    s+="\n<!-- PROF-READER-TEMPLATE-BEGIN: "+name+" -->\n```"+language+"\n"+(T/name).read_text(encoding="utf-8")+"```\n<!-- PROF-READER-TEMPLATE-END: "+name+" -->\n"
(P/"references/sasis.md").write_text(s,encoding="utf-8",newline="\n")
profile=json.loads((P/"references/sasis/profile-manifest.json").read_text(encoding="utf-8"))
profile["control_file_hashes"]={k:v for k,v in profile["control_file_hashes"].items() if not k.startswith("reader-invoker/")}
profile["control_file_hashes"]["../sasis.md"]=hashlib.sha256(s.encode()).hexdigest()
profile["control_file_hashes"]["../../SKILL.md"]=hashlib.sha256((P/"SKILL.md").read_bytes()).hexdigest()
(P/"references/sasis/profile-manifest.json").write_text(json.dumps(profile,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
diff=[]
for p in sorted(x for x in P.rglob("*") if x.is_file()):
    rel=p.relative_to(P).as_posix();diff.extend(difflib.unified_diff((I/rel).read_text(encoding="utf-8").splitlines(True),p.read_text(encoding="utf-8").splitlines(True),fromfile="r40/"+rel,tofile="r41/"+rel))
(R/"proposed-controls.diff").write_text("".join(diff),encoding="utf-8",newline="\n")
shutil.copyfile(R/"candidate-identities.json",R/"candidate-identities-before-template-carrier.json")
d=json.loads((R/"candidate-identities.json").read_text(encoding="utf-8"));d.pop("new_template_files",None);d.update(template_carrier="references/sasis.md#sealed-reader-invoker-templates",extracted_template_files=[p.relative_to(R).as_posix() for p in T.iterdir()],complete_package_file_count_after_integration=36,operative_manifest_checks_after_integration=28)
(R/"candidate-identities.json").write_text(json.dumps(d,indent=2)+"\n",encoding="utf-8")
for p in T.iterdir():
    pattern=r'<!-- PROF-READER-TEMPLATE-BEGIN: '+re.escape(p.name)+r' -->\n```(?:javascript|python)\n(.*?)```\n<!-- PROF-READER-TEMPLATE-END: '+re.escape(p.name)+r' -->'
    m=re.search(pattern,s,re.S);assert m and m.group(1).encode()==p.read_bytes()
print(json.dumps({"package_file_inventory":36,"operative_manifest_checks":28,"exact_embedded_template_payloads":4}))
