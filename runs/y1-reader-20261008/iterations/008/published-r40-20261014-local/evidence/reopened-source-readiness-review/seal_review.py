"""Seal the bounded review and verify the read-only source census once more."""
import datetime
import hashlib
import json
import pathlib

OUT=pathlib.Path(__file__).resolve().parent
def ident(p):
    p=pathlib.Path(p)
    return {"path":str(p),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
e=json.loads((OUT/'identity-readiness-evidence.json').read_text('utf-8'))
h=json.loads((OUT/'original-only-handoff.json').read_text('utf-8'))
post=[]
for c in e['cases']:
    for old in c['full_packet_file_census']:
        new=ident(old['path'])
        assert all(new[k]==old[k] for k in ['path','bytes','sha256']),old['path']
        post.append(new)
queue=ident(e['current_queue_identity']['path'])
assert queue==e['current_queue_identity']
manual={
 'completed_records':'All seven complete visual-inspection records were read, including all 45 observations and figure/table entries. Completed prepared records were parsed in full, their identity/association/page/readability fields checked against current files and selected current queue fields; scope, official URL/download metadata, required-asset statement, and completion flags inspected.',
 'operational_content':'Both D001 preparation scripts were read completely without executing them; only original official-source acquisition/rendering and readability-record finalisation are present. Batch summary was read completely. All seven historical preparation manifests have exactly identical common fields to their completed prepared records, except the earlier visual-status marker. No old teaching, author reasoning, proposed correction, or diagnosis is present in these records. They remain coordinator-only operational files in the strict author whitelist.',
 'original_aids':'All 45 extraction files match exact independent pypdf re-extraction of their identified original PDF pages, including covers. All 45 PNGs match completed-record hashes and are valid 1700x2200 pixel images at the declared 200 dpi page geometry. This verifies unchanged prepared images, not a repeated visual or mathematical audit.',
 'association':'For each case the cached official index row has the correct university lecture number, title and unique session-resource link; the cached official resource title agrees and links the declared original official PDF. First content-page original PDF text identifies the same lecture; the cover identifies MIT 18.01 Fall 2006. Current queue ID, lecture number, title, index/session URLs and readability provenance agree.',
 'old_marker':'The pending individual visual inspection value in preparation-manifest.json is an earlier historical state. prepared-source-record.json and visual-inspection.json are the completed authoritative records for this audit; no readiness failure is inferred from the old marker.',
 'scope_limits':'No live re-download, repeated full pixel audit, source mathematics correctness review, teaching generation, SASIS, destination inspection, publication, or acceptance decision was performed. Existing completed visual records attest the preparer’s visual work; this reviewer claims only independent current identity/readiness checks. Technical access to other files is not a confinement boundary; fresh authors must use explicit original-only input instructions.'
}
(OUT/'manual-content-review.json').write_text(json.dumps(manual,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=[
 '# Seven reopened original-source packets: bounded identity and readiness review',
 '',
 'Result: no identity, official-session association, page-coverage, or source-packet contamination discrepancy was established in D001, D002, D004, D010, D011, D014, or D017. The exact completed records and all current source constituents are bound below and in identity-readiness-evidence.json. This is preparation readiness, not acceptance of teaching or of the seven sessions.',
 '',
 'The authoritative completed records are each preparation/prepared-source-record.json and preparation/visual-inspection.json. The earlier preparation-manifest.json files still say “pending individual visual inspection”; those historical markers were not used to decide readiness. Their common source fields equal the completed records exactly. No cache file was changed.',
 '',
 'The seven original PDFs and seven verified copies were hashed, byte-compared and parsed for page counts. Every one of 45 declared PNGs was hashed and decoded, with exact declared file-set coverage and 1700 × 2200 geometry. Every one of 45 extraction aids exactly matches a fresh extraction from its original PDF page. All 45 page positions occur once, in order, in both completed records. Seven covers plus 38 content pages, 35 numbered figure groups and two unnumbered tables are accounted for by the completed visual records. No missing/unread portion is recorded. The present review did not repeat the full pixel audit.',
 '',
 'Official association was checked through the actual saved index row → session resource → original PDF link. Source-page lecture headers, cached resource titles, completed-record lecture numbers, and current queue identifying fields agree. Material IDs are queue identifiers: D010 maps to Lecture 11, D011 to Lecture 12, D014 to Lecture 15, and D017 to Lecture 19.',
 '',
 '| Material | University lecture | Original PDF bytes | PDF pages (cover + content) | Figure groups / tables | Original and verified-copy SHA256 |',
 '| --- | --- | ---: | --- | --- | --- |'
]
for c in e['cases']:
 v=c['visual_complete_record']
 lines.append(f"| {c['material_id']} | {c['lecture']} — {c['title']} | {c['original']['bytes']} | {c['pdf_pages']} ({v['cover_count']} + {v['content_page_count']}) | {v['figure_count']} / {v['table_count']} | `{c['original']['sha256']}` |")
lines += ['', 'Completed-record identities:', '', '| Material | prepared-source-record.json bytes / SHA256 | visual-inspection.json bytes / SHA256 |', '| --- | --- | --- |']
for c in e['cases']:
 a,b=c['authoritative_completed_records']
 lines.append(f"| {c['material_id']} | {a['bytes']} / `{a['sha256']}` | {b['bytes']} / `{b['sha256']}` |")
lines += [
 '',
 'Safe original-only author handoff: use original-only-handoff.json as an exact file whitelist, not a recursive folder handoff. It contains only subject-free identities/locators for each original PDF, its identical verified copy, every exact rendered page, every exact extraction aid, and the two cached official web provenance pages. The originals remain the authority for mathematics and visuals. The whitelist covers 118 source/provenance files. Its file census excludes 24 coordinator-only operational files: the seven earlier manifests, fourteen completed preparation/visual records, and D001’s two scripts and batch summary. Those records contain preparation/readability observations rather than teaching or diagnoses; excluding them keeps the fresh author’s subject inputs explicit. Do not pass this audit report, the identity/readiness evidence, queue history, old teaching, or diagnosis files as author subject content.',
 '',
 'Exact safe original locators:',
 ''
]
for c in h['cases']:
 p=pathlib.Path(c['original_pdf']['path'])
 lines.append(f"- {c['material_id']}: `{p}`; `{p.parent / 'render-200dpi'}` contains the exact {c['page_count']} per-page files listed individually in original-only-handoff.json. Extraction aids are listed there individually; D002’s PNG filenames use two-digit page numbers, the other cases use unpadded numbers.")
lines += [
 '',
 'All 142 files present in the seven preparation directories were inventoried and hashed. The source-only PDF/PNG/extraction/HTML classes plus the complete operational-record inspection revealed no old author/teaching/diagnosis artifact. Both preparation scripts were inspected without execution. The final readback rehashed the complete 142-file source census and found no change during this review.',
 '',
 f"Current queue association snapshot: `{queue['path']}`, {queue['bytes']} bytes, SHA256 `{queue['sha256']}`. Only its identifying fields were compared for this task; its teaching/diagnosis history is excluded from the author whitelist. The queue was unchanged at final readback.",
 '',
 'Disproved mechanical concerns: the generic MIT cover has no lecture number; the lecture number is printed on the first content page and agrees in all seven cases. Six selected queue provenance snapshots omit a source_url field; the completed record and official resource supply the exact original URL, so absence of that optional duplicate field is not a missing-source failure. The historical pending-visual marker is superseded by the complete per-page records. None of these is an original-source defect.',
 '',
 'Limits and remaining checks: this bounded review establishes current packet identity and readiness using the completed visual records. It does not re-establish pixel readability, validate the lecture mathematics, judge new teaching, run SASIS, inspect the actual destination, publish, or close any queue item. There is no unresolved original-access or packet-readiness discrepancy within the delegated scope. The next fresh author still must independently read the complete original source, under the verified published skill and the parent’s authorised input boundary. Root retains publishing and acceptance decisions.',
 '',
 'The earlier sealed D008 audit and eight-case technical recheck audit were preserved; all writes for this task are within reopened-source-readiness-review/.',
 ''
]
(OUT/'REPORT.md').write_text('\n'.join(lines),encoding='utf-8')
freeze={
 'sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'bounded seven-source readiness audit only',
 'source_files_final_readback_count':len(post),
 'source_files_final_readback_all_unchanged':True,
 'queue_final_readback_unchanged':True,
 'independent_machine_comparisons':sum(len(c['checks']) for c in e['cases']),
 'comparison_discrepancies':sum(len(c['issues']) for c in e['cases']),
 'strict_author_whitelist_count':sum(len(c['strict_author_whitelist']) for c in h['cases']),
 'coordinator_only_exclusion_count':sum(len(c['excluded_coordinator_only_files']) for c in h['cases']),
 'evidence_files':[ident(p) for p in sorted(OUT.glob('*')) if p.is_file() and p.name!='review-freeze.json']
}
(OUT/'review-freeze.json').write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({"report":ident(OUT/'REPORT.md'),"handoff":ident(OUT/'original-only-handoff.json'),"freeze":ident(OUT/'review-freeze.json'),"source_files":len(post),"whitelist":freeze['strict_author_whitelist_count'],"excluded":freeze['coordinator_only_exclusion_count']},indent=2))
