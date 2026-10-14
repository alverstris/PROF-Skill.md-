from pathlib import Path
import sys,subprocess,json,hashlib,datetime
root=Path(r"C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/fresh-author")
state=root/"evidence/.prof-state"
helper=Path(r"C:/Users/alver/.codex/skills/prof/scripts/prof_state.py")
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dependencies(topic=False):
    args=[sys.executable,str(helper),"dependencies","--state",str(state)]
    if topic:args+=["--topic","d008"]
    result=subprocess.run(args,capture_output=True,text=True,encoding="utf8",check=True)
    data=json.loads(result.stdout)
    (root/"evidence"/("topic-dependencies.json" if topic else "global-dependencies.json")).write_text(json.dumps(data,indent=2),encoding="utf8")
    return data
td=dependencies(True);gd=dependencies(False)
def witness(name):
    p=root/name
    return {"path":name,"sha256":sh(p),"locator":{"kind":"lines","start":1,"end":len(p.read_text(encoding="utf-8-sig").splitlines())}}
audit=witness("evidence/author-audit.md");ledger=witness("evidence/requirements.md")
t=json.loads((state/"topics/d008.json").read_text())
for id,r in t["requirements"].items():
    r.update(applicable=True,status=("fail" if id in ("T10","T11") else "pass"),
      reason=f"Actual trigger, acceptance, check method and substantive witnesses for {id} are recorded in requirements.md and the full route reconstruction in author-audit.md; status is author judgment, not SASIS or learner mastery.",
      evidence=[audit,ledger],dependencies=td)
(state/"topics/d008.json").write_text(json.dumps(t,indent=2),encoding="utf8")
m=json.loads((state/"manifest.json").read_text())
info={
"coverage":("pass","Every assigned original source portion and capability is mapped to actual final teaching; source mathematical corrections preserved.","evidence/coverage.md"),
"final_review":("fail","Full final main/help/figures audited; unresolved numerical and source-format findings prevent release acceptance.","evidence/author-audit.md"),
"source_representation":("fail","Five comparison commands lack requested terminating spaces; frozen teaching remains unchanged.","evidence/mechanical-checks.json"),
"figure_visual":("pass","All four exact exported PNGs visually inspected with complete labels/canvas edges; actual destination embedding is separate and unverified.","evidence/author-audit.md"),
"destination_math":("unverified","No actual published GitHub artifact exists in author scope; 401 source expressions inventoried for root's full match.","evidence/math-inventory.json"),
"destination_navigation":("unverified","Local routes exist but actual forward/return and first-use layout clicks were not performed.","evidence/navigation-inventory.json"),
"write_scope":("fail","Matplotlib/dependencies installed outside allowed task directory; preserved scope finding, packages left at root instruction.","evidence/execution-scope-finding.json"),
"local_portability":("pass","All seven teaching files exist at frozen hashes; relative routes/assets and image intrinsic dimensions match source.","evidence/teaching-freeze.json")}
for c in m["output_checks"]:
    st,reason,path=info[c["id"]]
    c.update(status=st,reason=reason,evidence=[witness(path)],dependencies=gd)
(state/"manifest.json").write_text(json.dumps(m,indent=2),encoding="utf8")
results={}
for label,extra in [("topic",["--topic","d008"]),("full",[])]:
    p=subprocess.run([sys.executable,str(helper),"check","--state",str(state),*extra],capture_output=True,text=True,encoding="utf8")
    results[label]={"exit_code":p.returncode,"stdout":p.stdout,"stderr":p.stderr}
(root/"evidence/state-check-results.json").write_text(json.dumps(results,indent=2),encoding="utf8")
freeze=json.loads((root/"evidence/teaching-freeze.json").read_text())
for v in freeze["files"]:assert sh(root/v["path"])==v["sha256"]
files=[]
for p in sorted(root.rglob("*")):
    if p.is_file() and p.name!="first-delivery-inventory.json":
        files.append({"path":p.relative_to(root).as_posix(),"bytes":p.stat().st_size,"sha256":sh(p)})
out={"revision":"d008-r39-first-delivery","created_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"frozen_teaching_manifest":"evidence/teaching-freeze.json","all_teaching_hashes_unchanged":True,"inventory_excludes_only_itself":True,"files":files,"status":"Complete authored output and evidence, with preserved numerical/source-format/execution findings and pending destination checks; no global acceptance."}
(root/"evidence/first-delivery-inventory.json").write_text(json.dumps(out,indent=2),encoding="utf8")
print(json.dumps({"topic_check":results["topic"],"full_check":results["full"],"inventory_files":len(files),"teaching_unchanged":True},indent=2))
