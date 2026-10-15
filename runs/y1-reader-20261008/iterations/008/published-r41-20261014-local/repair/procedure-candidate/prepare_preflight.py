"""Reuse prior synthetic-only harnesses; add checks for the observed r40 failure."""
from pathlib import Path
R=Path(__file__).resolve().parent
PROJECT=R.parents[2]
OLD=PROJECT/".prof-sasis/20261014-d008-r40/reader-preparation/synthetic-preflight-r40"
S=R/"synthetic-preflight"
oldroot=str(OLD).replace("\\","/");newroot=str(S).replace("\\","/")
for name in ("preflight_support.py","actual_negative_preflight.js","actual_figure_preflight.js","actual_launcher_truncation_preflight.js"):
    text=(OLD/name).read_text(encoding="utf-8").replace(oldroot,newroot).replace("prof.reader.d008.r40.synthetic.preflight1","prof.reader.r41.synthetic.invoker1")
    if name=="preflight_support.py":
        text=text.replace('"seal-core.json"}', '"seal-core.json", "invoker_template.js", "invoker.js"}')
    if name=="actual_negative_preflight.js":
        needle='await test("truncated_identity_proof", "F001", null, {truncateVerifier:true});'
        extra='''await test("corrupted_retained_invoker_schema_guard", "F001", async()=>store(KEY,{...original,invoker_source:original.invoker_source.replace('p.schema !== "prof-reader-reuse-proof-v1"','p.schema !== "prof-reader-reuse-store-v1"')}));
await test("mutated_retained_invoker_digest", "F001", async()=>store(KEY,{...original,invoker_sha256:"0".repeat(64)}));
await test("mutated_retained_invoker_source_identity", "F001", async()=>store(KEY,{...original,invoker_source:original.invoker_source.replace("// Only the exact verified operational source", "// Changed retained operational source")}));
'''
        assert needle in text;text=text.replace(needle,extra+needle)
        text=text.replace('"seal-core.json"])','"seal-core.json","invoker_template.js","invoker.js"])')
    (S/name).write_text(text,encoding="utf-8",newline="\n")
