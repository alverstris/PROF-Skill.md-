"""Read-only verification of prepared source packets; outputs stay beside this script."""
import datetime
import hashlib
import html
import json
import pathlib
import re
import sys
from urllib.parse import urljoin, urlparse

from PIL import Image
from pypdf import PdfReader

sys.stdout.reconfigure(encoding="utf-8")
OUT = pathlib.Path(__file__).resolve().parent
ROOT = OUT.parents[2]
CACHE = ROOT / ".prof-sasis/original-source-cache/20261014"
CASES = ["D001", "D002", "D004", "D010", "D011", "D014", "D017"]
EXPECTED = {"D001": 1, "D002": 2, "D004": 4, "D010": 11, "D011": 12, "D014": 15, "D017": 19}
QUEUE_PATH = ROOT / ".prof-sasis/20261014-d008-r40/run-state/queue.json"
QUEUE = json.loads(QUEUE_PATH.read_text("utf-8-sig"))
QUEUE_SESSIONS = {x["material_id"]:x for x in QUEUE["sessions"]}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def identity(p):
    return {"path": str(p), "bytes": p.stat().st_size, "sha256": sha(p)}

def clean(s):
    s = re.sub(r"<script\b[^>]*>.*?</script>", " ", s, flags=re.I | re.S)
    s = re.sub(r"<style\b[^>]*>.*?</style>", " ", s, flags=re.I | re.S)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())

def links(s, base):
    return [urljoin(base, html.unescape(x)) for x in re.findall(r'href=["\']([^"\']+)', s, flags=re.I)]

def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

all_cases = []
handoff = []
for case in CASES:
    p = (CACHE / case / "preparation").resolve()
    rp, vp = p / "prepared-source-record.json", p / "visual-inspection.json"
    r, v = json.loads(rp.read_text("utf-8")), json.loads(vp.read_text("utf-8"))
    issues = []
    checks = []
    def ck(name, actual, expected):
        ok = actual == expected
        checks.append({"check": name, "actual": actual, "expected": expected, "pass": ok})
        if not ok:
            issues.append(name)
        return ok
    original = pathlib.Path(r["local_original"])
    copy = pathlib.Path(r["verified_local_copy"]["path"])
    n = r["page_count"]
    lecture = EXPECTED[case]
    reader = PdfReader(original)
    ck("material ID", r["material_id"], case)
    ck("visual material ID", v["material_id"], case)
    ck("lecture number", r["university_lecture_number"], lecture)
    ck("PDF basename", original.name, f"lec{lecture}.pdf")
    ck("original contained in this packet", original.resolve().parent, p)
    ck("verified copy contained in this packet", copy.resolve().parent, p)
    ck("original SHA256", sha(original), r["original_pdf"]["sha256"])
    ck("original byte count", original.stat().st_size, r["original_pdf"]["bytes"])
    ck("copy SHA256", sha(copy), r["verified_local_copy"]["sha256"])
    ck("copy equals original", copy.read_bytes(), original.read_bytes())
    # Remove byte values from the record; only the actual comparison result belongs here.
    checks[-1] = {"check": "copy equals original byte for byte", "pass": checks[-1]["pass"]}
    ck("repeat official download SHA256", r["repeat_official_download"]["sha256"], sha(original))
    ck("repeat official download byte count", r["repeat_official_download"]["bytes"], original.stat().st_size)
    ck("actual original PDF page count", len(reader.pages), n)
    ck("verified copy actual PDF page count", len(PdfReader(copy).pages), n)
    ck("prepared page sequence", [x["pdf_page"] for x in r["pages"]], list(range(1,n+1)))
    ck("visual page sequence", [x["pdf_page"] for x in v["pages"]], list(range(1,n+1)))
    ck("visual page count", v["page_count"], n)
    ck("visual covers plus content pages", v["cover_count"] + v["content_page_count"], n)
    ck("visual complete status", r["visual_inspection_status"], "complete_individual_page_reading")
    ck("visual record locator", pathlib.Path(r["visual_inspection_record"]).resolve(), vp.resolve())
    ck("all required assets recorded verified", r["all_required_session_specific_assets_verified"], True)
    ck("required asset count", r["required_session_specific_asset_count"], 1)
    ck("missing/unread portions", r["missing_or_unread_required_portions"], [])
    for field in ["unread_pages", "inaccessible_required_portions", "readability_limits"]:
        ck("visual " + field, v[field], [])
    ck("visual figure count", v["numbered_figure_count"], r["numbered_figure_count"])
    ck("observed figure group total", sum(len(x.get("figures", [])) for x in v["pages"]), v["numbered_figure_count"])
    ck("observed table total", sum(len(x.get("tables", [])) for x in v["pages"]), v["unnumbered_table_count"])
    for field in ["queue_changed", "teaching_generation_launched", "acceptance_or_queue_closure_claimed"]:
        ck(field, r[field], False)
    records = [identity(rp), identity(vp)]
    pages = []
    for pr, vr, actual_page in zip(r["pages"], v["pages"], reader.pages):
        i = pr["pdf_page"]
        pp = pathlib.Path(pr["render"])
        ck(f"p{i} render contained in packet", pp.resolve().parent, p / "render-200dpi")
        ck(f"p{i} render SHA256", sha(pp), pr["render_sha256"])
        with Image.open(pp) as im:
            dims = list(im.size)
            im.verify()
        expect_dims = [round(float(pr["width_points"]) * r["render_dpi"] / 72), round(float(pr["height_points"]) * r["render_dpi"] / 72)]
        # Poppler rounds up pixel boundaries when a page does not fit exact pixels.
        ok_dims = all(abs(a-b) <= 1 for a,b in zip(dims,expect_dims))
        checks.append({"check":f"p{i} decoded PNG expected DPI geometry", "actual":dims,"expected_with_one_pixel_rounding":expect_dims,"pass":ok_dims})
        if not ok_dims: issues.append(f"p{i} geometry")
        ck(f"p{i} visual readable status", vr["status"], "readable")
        ck(f"p{i} visual unreadable regions", vr["unreadable_regions"], [])
        ep = p / f"page-{i:02}-extraction.txt"
        extracted = actual_page.extract_text() or ""
        saved = ep.read_text("utf-8")
        ck(f"p{i} extraction exact re-extraction", saved, extracted)
        # Source text can be long; retain hashes and counts rather than text in machine checks.
        checks[-1] = {"check":f"p{i} extraction exact re-extraction", "pass":checks[-1]["pass"], "saved_chars":len(saved), "reextracted_chars":len(extracted),"reextracted_utf8_sha256":hashlib.sha256(extracted.encode("utf-8")).hexdigest()}
        ck(f"p{i} extraction recorded char count", len(saved), pr["extractable_chars"])
        ck(f"p{i} actual page width", float(actual_page.mediabox.width), float(pr["width_points"]))
        ck(f"p{i} actual page height", float(actual_page.mediabox.height), float(pr["height_points"]))
        pages.append({"pdf_page":i,"printed_page":vr.get("printed_page"),"render":identity(pp),"decoded_pixels":dims,"extraction_aid":identity(ep),"visual_record_observation":vr.get("observation"),"figures":vr.get("figures",[]),"tables":vr.get("tables",[])})
    declared_pngs = sorted(str(pathlib.Path(x["render"]).resolve()) for x in r["pages"])
    ck("actual PNG set equals complete declared set", sorted(str(x.resolve()) for x in p.rglob("*.png")), declared_pngs)
    ck("actual extraction set complete", sorted(x.name for x in p.glob("*-extraction.txt")),[f"page-{i:02}-extraction.txt" for i in range(1,n+1)])
    index_path, resource_path = p / "lecture-notes-index.html", p / f"lec{lecture}-resource.html"
    ih, rh = index_path.read_text("utf-8"), resource_path.read_text("utf-8")
    ck("saved index SHA256", sha(index_path), r["index"]["sha256"])
    ck("saved index byte count", index_path.stat().st_size, r["index"]["bytes"])
    ck("saved resource SHA256", sha(resource_path), r["resource"]["sha256"])
    ck("saved resource byte count", resource_path.stat().st_size, r["resource"]["bytes"])
    expected_resource = f"https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec{lecture}/"
    expected_index = "https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/lecture-notes/"
    ck("resource requested URL", r["resource"]["requested_url"], expected_resource)
    ck("resource final URL", r["resource"]["final_url"], expected_resource)
    ck("index requested URL", r["index"]["requested_url"], expected_index)
    ck("index final URL", r["index"]["final_url"], expected_index)
    row_matches = [tr for tr in re.findall(r"<tr\b[^>]*>.*?</tr>",ih,re.I|re.S) if expected_resource in links(tr,expected_index)]
    ck("index rows assigning resource",len(row_matches),1)
    row = row_matches[0] if row_matches else ""
    ck("exact index row text",clean(row),r["verified_official_index_row"]["row_text"])
    ck("index row lecture prefix", clean(row).split(" ",1)[0],str(lecture))
    ck("index row resource link set", links(row,expected_index),[urljoin(expected_index,x) for x in r["verified_official_index_row"]["resource_links"]])
    rl = links(rh,expected_resource)
    pdf_url = r["original_pdf"]["requested_url"]
    ck("actual resource links original PDF", pdf_url in rl, True)
    ck("official original final URL",r["original_pdf"]["final_url"],pdf_url)
    ck("official PDF host",urlparse(pdf_url).netloc,"ocw.mit.edu")
    ck("official PDF lecture basename",urlparse(pdf_url).path.split("_")[-1],f"lec{lecture}.pdf")
    for field in ["index","resource","original_pdf","repeat_official_download"]:
        ck(field+" recorded HTTP status",r[field]["status"],200)
    provenance=r["original_queue_identifying_fields_and_readability_provenance"]
    for field,expect in [("material_id",case),("number",lecture),("title",r["title"]),("index_url",expected_index),("session_url",expected_index)]:
        ck("queue identifying provenance "+field,provenance[field],expect)
    if "source_url" in provenance:
        ck("optional queue identifying provenance source_url",provenance["source_url"],pdf_url)
    current_queue=QUEUE_SESSIONS[case]
    for field in ["material_id","number","title","index_url","session_url","readability"]:
        ck("actual current queue association "+field,current_queue[field],provenance[field])
    if "source_url" in current_queue:
        ck("actual current queue source URL",current_queue["source_url"],pdf_url)
    q=provenance["readability"]
    for field,expect in [("material_id",case),("number",lecture),("title",r["title"]),("id",f"mit-18-01-fall-2006-L{lecture:02}")]:
        ck("readability provenance "+field,q[field],expect)
    cover_text=(reader.pages[0].extract_text() or "")
    first_content_text=(reader.pages[v["cover_count"]].extract_text() or "")
    ck("first original content page lecture number",bool(re.search(r"Lecture\s+"+str(lecture)+r"\b",first_content_text,re.I)),True)
    ck("original cover course code", "18.01" in cover_text,True)
    # Every entry is listed and hashed; whitelist is deliberately narrower than preparation directory.
    whitelist=[original,copy,index_path,resource_path]+[pathlib.Path(x["render"]) for x in r["pages"]]+[p/f"page-{i:02}-extraction.txt" for i in range(1,n+1)]
    safe_set={x.resolve() for x in whitelist}
    census=[]
    for x in sorted(p.rglob("*")):
        if x.is_file():
            census.append({**identity(x),"relative_path":str(x.relative_to(p)),"author_packet_role":"original_or_exact_source_aid" if x.resolve() in safe_set else "coordinator_only_operational_record"})
    all_cases.append({"material_id":case,"lecture":lecture,"title":r["title"],"packet":str(p),"authoritative_completed_records":records,"original":identity(original),"verified_copy":identity(copy),"pdf_pages":n,"cover_text":cover_text,"index_association":{"row_text":clean(row),"resource_links":links(row,expected_index)},"resource_association":{"requested_url":expected_resource,"original_pdf_url":pdf_url,"linked_pdf_present":pdf_url in rl,"resource_title":re.findall(r"<title[^>]*>(.*?)</title>",rh,re.I|re.S),"pdf_links":[u for u in rl if urlparse(u).path.endswith(".pdf")]},"visual_complete_record":{"cover_count":v["cover_count"],"content_page_count":v["content_page_count"],"figure_count":v["numbered_figure_count"],"table_count":v["unnumbered_table_count"],"inspection_method_values":sorted({x.get("inspection_method","") for x in v["pages"]})},"pages":pages,"checks":checks,"issues":issues,"full_packet_file_census":census,"operational_texts_requiring_manual_review":[str(x) for x in sorted(p.glob("*.json"))]+[str(x) for x in sorted(p.glob("*.py"))]})
    handoff.append({"material_id":case,"university_lecture_number":lecture,"title":r["title"],"official_index_url":expected_index,"official_resource_url":expected_resource,"official_pdf_url":pdf_url,"original_pdf":identity(original),"verified_pdf_copy":identity(copy),"page_count":n,"render_dpi":r["render_dpi"],"pages":[{"pdf_page":x["pdf_page"],"render":x["render"],"extraction_aid":x["extraction_aid"]} for x in pages],"saved_official_web_evidence":[identity(index_path),identity(resource_path)],"strict_author_whitelist":[identity(x) for x in whitelist],"excluded_coordinator_only_files":[x["path"] for x in census if x["author_packet_role"]=="coordinator_only_operational_record"]})
    print(case,"L"+str(lecture),n,"pages",len(checks),"checks; issues:",issues,"PDF",original.stat().st_size,sha(original))

write("identity-readiness-evidence.json",{"checked_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"authority":"prepared-source-record.json and visual-inspection.json; older preparation-manifest.json is not readiness authority","current_queue_identity":identity(QUEUE_PATH),"method_limits":"Independent current byte, parser-page-count, source association and packet-content verification; no repeated full pixel audit and no live re-download. Existing completed visual records retained as evidence of the prior pixel inspection, not reviewer pixel claims.","cases":all_cases})
write("original-only-handoff.json",{"scope":"Source files and exact extraction aids only; this manifest contains no old teaching, author reasoning, diagnoses or proposed corrections. Pass exact whitelisted files, not entire preparation folders or this audit report. Original images/PDF are authority; extraction aids may omit mathematical glyphs.","cases":handoff})
print("TOTAL",sum(x["pdf_pages"] for x in all_cases),"pages",sum(len(x["checks"]) for x in all_cases),"checks",sum(len(x["issues"]) for x in all_cases),"issues")
