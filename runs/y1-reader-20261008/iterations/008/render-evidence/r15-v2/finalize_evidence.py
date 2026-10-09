from pathlib import Path
import json,hashlib,re,datetime,fitz
p=Path(__file__).parent;old=p.parent/'r15-original';out=p/'preview-final';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(path,obj):
 with path.open('x') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
css=json.loads((p/'current-css-inventory.json').read_text());prior=json.loads((old/'current-css-inventory.json').read_text());review=json.loads((p/'css-scope-review.json').read_text());prevreview=json.loads((old/'css-scope-review.json').read_text())
assert all(x.get('status')==200 and sha(p/x['path'])==x['sha256'] for x in css['fetches'])
changes=json.loads((p/'fresh-CSS-changes.json').read_text());changed=[]
strip_map=lambda s:re.sub(r'/\*# sourceMappingURL=[^*]*\*/','',s)
for row in changes:
 a=(p/row['current']['path']).read_text();b=(old/row['prior']['path']).read_text();assert strip_map(a)==strip_map(b);changed.append({'stem':row['stem'],'old_sha256':row['prior']['sha256'],'new_sha256':row['current']['sha256'],'only_sourceMappingURL_comment_changed':True})
cleandom=lambda d:[{'tag':x['tag'],'attrs':{k:v for k,v in x['attrs'].items() if k!='initial-path'}} for x in d['ancestors']]
dom=json.loads((p/'dom-structure.json').read_text());olddom=json.loads((old/'dom-structure.json').read_text())
assert review['candidate_rules']==prevreview['candidate_rules'] and cleandom(dom)==cleandom(olddom)
for field in ['unique_inline_styles','present_classes','present_tags','present_ids','style_blocks']:assert review[field]==prevreview[field]
assert dom['article_attrs']==olddom['article_attrs']
manual=json.loads((old/'manual-style-review.json').read_text());manual['reviewed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();manual['fresh_revision_evidence']={'fresh_HTTP_CSS_fetches':len(css['fetches']),'all_bytes_hash_verified':True,'four_changed_assets':changed,'all_38_font_candidates_exactly_equal':True,'actual_ancestor_scopes_equal_except_route':True,'actual_article_tags_classes_ids_and_inline_styles_equal':True,'original_manual_review_path':str(old/'manual-style-review.json'),'original_manual_review_sha256':sha(old/'manual-style-review.json'),'claim':'Fresh CSS/DOM inspected. Four newly named assets differ only in sourceMappingURL comments, proved by full comparison after removing only those comments. No old fetch substituted. Initial shortcut expecting full URL/hash identity failed and is preserved.'};save(p/'manual-style-review.json',manual)
record=json.loads((out/'preview-check.json').read_text());findings=[
'P001–P008 complete. Title, prose, tangent display and two error displays legible; no clipping or overlap.',
'P009–P017 complete. Comparison signs, radicals and exponents legible. A1 navigation wraps within its paragraph. No clipping/overlap.',
'P018–P025 through quadratic formula complete. Product/limit displays legible. P025 explanation continues next page; no clipped formula.',
'Continuation of P025 through P032 introductory text. Proof inequalities and cosine models legible. P032 equation moves to page 5 after introductory “so”; preview-only pagination.',
'P032 display continuation through P038. Log/power models, A2, square-term collections and derivative notation clear; no clipping/overlap.',
'P039–P044 through first square-term display and “Consequently”. Time ratio, radical, units and scientific notation clear. P044 following equation continues on page 7; preview-only pagination.',
'P044 continuation through P052. A3 numeric reference and tolerance, A4 complete expression/task and limit legible. Plain P052 Sources and scope label ends page; associated P053 text begins page 8.',
'P053–P063 complete. End-core boundary, all four hints, end-hints boundary, solution heading, A1 solution and A2 initial solution visible/readable. Square roots and remainder terms legible; no overlap.',
'P064–P068 complete. A2 reasoning, A3 numeric errors, A4 product/coefficients and all ending return links visible. Final line has clear space below; no clipping/overlap.'
]
views=[]
for i,(im,finding) in enumerate(zip(record['images'],findings),1):
 assert sha(out/im['path'])==im['sha256'];views.append({'page':i,'path':str(out/im['path']),'sha256':im['sha256'],'complete_page_personally_opened':True,'method':'tools.view_image full saved page emitted with image; not inferred from text extraction','finding':finding})
assert len(views)==record['page_count']==9;assert sha(out/'preview.pdf')==record['pdf_sha256']
save(out/'visual-inspection.json',{'pdf_sha256':record['pdf_sha256'],'all_9_complete_final_pages_personally_opened':True,'pages':views,'conclusion':'Readable whole-document internal preview; no clipped/overlapping content or unreadable math found. Preview-only pagination artifacts listed page by page. No live GitHub pixels or PDF hyperlink pass.','limits':['Internal PDF conversion uses TeX/Pandoc, not GitHub CSS or MathJax.','18 missing PDF destinations remain; link click behavior not accepted.','Source labels and grouped help retained; no reflow repair or editing of frozen lesson.']})
compiler=[]
for passno in [1,2]:
 c=json.loads((out/f'compiler-pass{passno}-capture.json').read_text());assert sha(out/c['stdout_file'])==c['stdout_sha256'];assert sha(out/c['tex_log_snapshot'])==c['tex_log_sha256'];stdout=(out/c['stdout_file']).read_text();log=(out/c['tex_log_snapshot']).read_text();assert log
 compiler.append(c|{'case_insensitive_stdout_diagnostics':re.findall(r'^.*(?:warning|overfull|underfull|undefined|missing|^!).*$',stdout,re.I|re.M),'case_insensitive_log_diagnostics':re.findall(r'^.*(?:warning|overfull|underfull|undefined|missing|^!).*$',log,re.I|re.M),'unique_missing_destinations':sorted(set(re.findall(r'warning \(dest\): name\{([^}]+)\}',stdout,re.I))),'overfull_underfull_undefined_errors':re.findall(r'^.*(?:overfull|underfull|undefined control|^!).*$',stdout+'\n'+log,re.I|re.M)})
with fitz.open(out/'preview.pdf') as doc:linkcount=sum(len(page.get_links()) for page in doc)
save(out/'compiler-and-PDF-navigation-review.json',{'passes':compiler,'missing_destination_count_each_pass':[len(x['unique_missing_destinations']) for x in compiler],'log_package_line_not_a_warning':'Package: infwarerr ... Providing info/warning/error messages (HO) is package metadata caught by the broad scan.','PDF_link_annotation_count':linkcount,'PDF_navigation_status':'NOT PASSED: raw Markdown HTML id anchors do not become TeX destinations; compiler substitutes fixed destinations. Internal GitHub ids passed independently.','source_and_PDF_visible_labels_in_order':re.findall(r'P\d{3}\.',(out/'preview-text.txt').read_text())==[f'P{i:03}.' for i in range(1,69)]})
print(json.dumps({'pages_opened':len(views),'missingPDFdestinations':[len(x['unique_missing_destinations']) for x in compiler],'AST_prose_fidelity':record['AST']['complete_AST_prose_math_stream_exact_after_whitespace_folding'],'PDF_SHA':record['pdf_sha256'],'compiler_exits':[x['exit_code'] for x in compiler]},indent=2))
