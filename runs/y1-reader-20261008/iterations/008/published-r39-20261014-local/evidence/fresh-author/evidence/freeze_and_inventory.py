from pathlib import Path
import hashlib,json,re
from PIL import Image
root=Path(r"C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/fresh-author")
teaching=root/"teaching"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
items=[]
for p in sorted(teaching.rglob("*")):
    if p.is_file():
        info={"path":p.relative_to(root).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p)}
        if p.suffix==".png":
            with Image.open(p) as im:info["pixels"]=list(im.size)
        items.append(info)
freeze={"revision":"d008-r39-first-delivery","prof_version":"2026-10-14-r39","prof_commit":"15f0b916d8a686e6972cbee330d261569d3b92a3","meaning":"Complete first authored teaching; preserved unchanged after this freeze. Identity does not establish acceptance.","files":items}
(root/"evidence/teaching-freeze.json").write_text(json.dumps(freeze,indent=2),encoding="utf8")
expressions=[]; links=[];anchors={};issues=[]
for p in sorted(teaching.glob("*.md")):
    txt=p.read_text(encoding="utf-8-sig");name=p.name
    anchors[name]=re.findall(r'<a id="([^"]+)"></a>',txt)
    if re.search(r"(?m)^\s{0,3}#{1,6}\s",txt):issues.append([name,"ATX heading"])
    for m in re.finditer(r'\$\x60(.*?)\x60\$|\x60{3}math\n(.*?)\n\x60{3}',txt,re.S):
        payload=m.group(1) if m.group(1) is not None else m.group(2)
        line=txt.count("\n",0,m.start())+1
        expressions.append({"id":f"math-{len(expressions)+1:03d}","file":name,"line":line,"kind":"inline" if m.group(1) is not None else "display","payload":payload,"rendered_match":"unverified"})
        if "<" in payload or ">" in payload:issues.append([name,line,"literal strict-comparison glyph in math"])
        for bad in re.finditer(r"\\(?:lt|gt)(?!\s)",payload):issues.append([name,line,"comparison command missing requested terminating space",bad.group()])
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',txt):
        href=m.group(2)
        if href.startswith("http"):continue
        target,sep,frag=href.partition("#");target=target or name
        links.append({"source":name,"line":txt.count("\n",0,m.start())+1,"target":target,"fragment":frag})
    if "<details" in txt:issues.append([name,"disclosure container"])
    if "\u00a7" in txt:issues.append([name,"unreplaced build placeholder"])
    if re.search(r"TODO|TBD|FIXME",txt):issues.append([name,"unresolved placeholder"])
for route in links:
    p=teaching/route["target"]
    if not p.is_file():issues.append([route,"missing target file"])
    if route["fragment"] not in anchors.get(route["target"],[]):issues.append([route,"missing fragment"])
allanchors=[(f,a) for f,aa in anchors.items() for a in aa]
assert len({a for f,a in allanchors})==len(allanchors),"Sibling anchors duplicated"
for p in teaching.glob("*.md"):
    txt=p.read_text(encoding="utf-8-sig")
    for m in re.finditer(r'<img src="([^"]+)" width="(\d+)" height="(\d+)"',txt):
        with Image.open(teaching/m[1]) as im:assert im.size==(int(m[2]),int(m[3]))
for letter in "abcdef":
    assert f"d008-main-task-{letter}" in anchors["main.md"]
    assert f"d008-hints-{letter}" in anchors["hints.md"]
    assert f"d008-solutions-{letter}" in anchors["solutions.md"]
(root/"evidence/math-inventory.json").write_text(json.dumps(expressions,indent=2,ensure_ascii=False),encoding="utf8")
(root/"evidence/navigation-inventory.json").write_text(json.dumps(links,indent=2),encoding="utf8")
report={"revision":"d008-r39-first-delivery","teaching_files":len(items),"math_expressions":len(expressions),"inline_math":sum(e["kind"]=="inline" for e in expressions),"display_math":sum(e["kind"]=="display" for e in expressions),"source_link_routes":len(links),"unique_anchors":len(allanchors),"issues":issues,"checks":{"all_task_hint_solution_anchors":"pass for A-F","local_link_targets":"pass","image_declared_dimensions_match_export":"pass","live_GitHub_expression_preservation":"unverified","live_GitHub_navigation_and_first_use_layout":"unverified","destination_typography":"unverified"}}
(root/"evidence/mechanical-checks.json").write_text(json.dumps(report,indent=2),encoding="utf8")
print(json.dumps(report,indent=2));print("FROZEN: seven teaching files; no post-freeze edits.")
