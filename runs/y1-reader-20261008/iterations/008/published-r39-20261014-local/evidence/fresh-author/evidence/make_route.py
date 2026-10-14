from pathlib import Path
import json,hashlib
root=Path(r"C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/fresh-author")
teaching=root/"teaching"; steps=[]
def digest(b):return hashlib.sha256(b).hexdigest()
def textstep(id,file,a,b):
    raw=(teaching/file).read_bytes();ls=raw.splitlines(keepends=True)
    st=sum(map(len,ls[:a-1]));en=sum(map(len,ls[:b]))
    steps.append({"step_id":id,"kind":"text","path":"teaching/"+file,"lines_1_based_inclusive":[a,b],"byte_start_0_based":st,"byte_end_exclusive":en,"bytes":en-st,"sha256":digest(raw[st:en])})
def figstep(id,name):
    p=teaching/"figures"/name
    steps.append({"step_id":id,"kind":"figure","path":"teaching/figures/"+name,"bytes":p.stat().st_size,"sha256":digest(p.read_bytes()),"require_actual_view_before_advance":True})
textstep("main-01","main.md",1,55);figstep("figure-01","tangent-log.png")
textstep("main-02","main.md",56,72)
textstep("main-03","main.md",73,89);figstep("figure-02","sine-cosine-linear.png")
textstep("main-04","main.md",90,152)
textstep("main-05","main.md",153,188);figstep("figure-03","clock-intervals.png")
textstep("main-06","main.md",189,286);figstep("figure-04","cosine-quadratic.png")
for i,(a,b) in enumerate([(287,392),(393,436),(437,491),(492,523),(524,532)],7):textstep(f"main-{i:02d}","main.md",a,b)
for id,a,b in [("hints-intro",1,5),("hint-a",6,12),("hint-b",13,25),("hint-c",26,32),("hint-d",33,43),("hint-e",44,50),("hint-f",51,64)]:textstep(id,"hints.md",a,b)
for id,a,b in [("solutions-intro",1,5),("solution-a",6,22),("solution-b",23,61),("solution-c",62,91),("solution-d",92,125),("solution-e",126,163),("solution-f",164,221)]:textstep(id,"solutions.md",a,b)
for file in ["main.md","hints.md","solutions.md"]:
    chunks=[s for s in steps if s.get("path")=="teaching/"+file]
    raw=(teaching/file).read_bytes()
    assert chunks[0]["byte_start_0_based"]==0 and chunks[-1]["byte_end_exclusive"]==len(raw)
    assert all(x["byte_end_exclusive"]==y["byte_start_0_based"] for x,y in zip(chunks,chunks[1:]))
out={"teaching_revision":"d008-r39-first-delivery","metadata_only":True,"reading_order":"complete baseline first, then these teaching steps strictly in order; main with each figure at first use, all hints, all complete solutions","line_convention":"1-based inclusive, byte offsets zero-based and end-exclusive; text slices preserve BOM and all newline bytes","steps":steps}
(root/"evidence/complete-reading-route.json").write_text(json.dumps(out,indent=2),encoding="utf8")
print("Route saved: 29 ordered steps; all text bytes and all 4 figures covered, no text gap or overlap.")
