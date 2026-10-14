from pathlib import Path
import json,hashlib
root=Path(r"C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/fresh-author")
state=root/"evidence/.prof-state";skill=Path(r"C:/Users/alver/.codex/skills/prof")
orig=root.parent/"original-inputs"
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((state/"manifest.json").read_text(encoding="utf-8-sig"))
sources=[]
def source(id,p,parts,note,url=None):
    d={"id":id,"path":str(p.resolve()),"sha256":sh(p),"portions":[{"id":pi,"locator":loc,"disposition":"required","reason":note,"evidence":[]} for pi,loc in parts]}
    if url:d["url"]=url
    sources.append(d)
source("baseline",skill/"references/sasis/ocr-baseline-20261007/student-baseline.txt",[("maths","lines1–666"),("further-maths","lines667–826"),("physics","lines827–1389"),("chemistry","lines1390–2561")],"Complete actual baseline read in bounded ranges; access.md records exact recovery and consequential premises.")
source("lecture",orig/"mit-18.01-fall-2006-lec9.pdf",[(f"p{i}",f"PDF page{i}, complete") for i in range(1,8)],"All original pages visually inspected; page-specific actual content and corrections in access.md/coverage.md.")
for i in range(1,8):source(f"original-png-{i}",orig/f"page-{i}.png",[("whole","whole page image including edges")],"Actual view_image result inspected; corresponding PDF page recorded.")
for id,name in [("provenance","provenance.json"),("extracted-aid","complete-extracted-text.txt")]:source(id,orig/name,[("whole","whole file")],"Read completely; extraction aid cross-checked against all original page images.")
source("official-resource",orig/"official-resource-page.html",[("identity","lines33,52,65,491,829,1199,1241,1328")],"Actual targeted identity passages inspected, title/course/instructor agree.")
refs=["execution-protocol.md","domain-patterns.md","state-tool.md","sasis.md","sasis/profile-manifest.json","sasis/student-testing-contract.txt","sasis/student-role.txt","sasis/rewrite-guide.md"]
for i,r in enumerate(refs):source(f"skill-reference-{i+1}",skill/"references"/r,[("whole","whole file; domain guide math/physics pattern applied")],"Complete actual read; source tracking, teaching duties, state and role limits applied.")
source("pdf-skill",Path(r"C:/Users/alver/.codex/plugins/cache/openai-primary-runtime/pdf/26.1013.11914/skills/pdf/SKILL.md"),[("whole","whole skill; source-reading branch")],"Complete actual read; rendered original pages inspected; no PDF create/edit.")
source("conventions",root/"evidence/coverage.md",[("whole","whole capability/source/convention record")],"Current coverage/convention record used in audit.")
source("research",root/"evidence/research.md",[("whole","R1–R3 complete targeted research/access record")],"Actual official web passages inspected with recorded scopes; no publication of unsupported clock/GPS claim.")
frozen=json.loads((root/"evidence/teaching-freeze.json").read_text())
m["sources"]=sources
m["outputs"]=[{"id":"output-"+str(i+1),"path":v["path"],"sha256":v["sha256"]} for i,v in enumerate(frozen["files"])]
m["required_topics"]=[{"id":"d008","title":"Complete MIT18.01 Lecture9 Linear and Quadratic Approximations","source_portions":[{"source_id":s["id"],"portion_id":p["id"]} for s in sources for p in s["portions"]],"outputs":[o["id"] for o in m["outputs"]]}]
m["output_checks"]=[{"id":id,"description":desc,"applicable":True,"status":"pending","reason":"","evidence":[],"dependencies":[]} for id,desc in [
("coverage","Full source/assigned capability coverage"),
("final_review","Whole final teaching/help readback with no unresolved release defect"),
("source_representation","Markdown mathematics and typography contract"),
("figure_visual","Every exact saved figure inspected"),
("destination_math","All401 source expressions preserved in actual GitHub result"),
("destination_navigation","Actual forward/return and first-use layout checks"),
("write_scope","Respect task-only write constraint"),
("local_portability","Local relative asset targets, complete file inventory and unchanged hashes")]]
(state/"manifest.json").write_text(json.dumps(m,indent=2),encoding="utf8")
t=json.loads((state/"topics/d008.json").read_text())
t["source_reads"]=[{"source_id":s["id"],"portion_id":p["id"],"status":"read","reviewed_sha256":s["sha256"],"note":p["reason"]+" See evidence/access.md, coverage.md, research.md and author-audit.md."} for s in sources for p in s["portions"]]
t["gaps"]=[]
(state/"topics/d008.json").write_text(json.dumps(t,indent=2),encoding="utf8")
a=root/"evidence/author-audit.md";x=a.read_text(encoding="utf-8-sig")
x=x.replace("Other checked worked values: ln1.1, cos.2, composite.05 and sqrt4.04 are recomputed in final-numerical-readback.json.","Other worked values were recomputed in final-numerical-readback.json. The composite at x=.05 FAILED its printed-value check: actual 0.883030902... differs from main378's 0.8830328. Correct seven-decimal rounding is 0.8830309. The frozen text is unchanged; its linear and quadratic estimates and improvement conclusion are correct. Original failed assertion is preserved in final_readback.py and preserved-numerical-failure.txt. Other numerical readbacks passed their stated rounding checks.")
a.write_text(x,encoding="utf8")
print("State inventory declares all source portions, outputs and relevant checks; teaching remains frozen.")
