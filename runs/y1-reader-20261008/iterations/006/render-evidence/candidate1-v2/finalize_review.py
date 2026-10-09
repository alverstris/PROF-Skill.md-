#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,re,datetime
root=Path(__file__).parent
def save(n,v):(root/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
css=json.loads((root/'current-css-inventory.json').read_text())
dom=json.loads((root/'dom-structure.json').read_text())
rules=[]
for f in sorted((root/'current-css').glob('*.css')):
 for m in re.finditer(r'([^{}]+)\{([^{}]*)\}',f.read_text()):
  sel,decl=m[1].strip(),m[2]
  if sel in ['body','.markdown-body','.markdown-body p,.markdown-body blockquote,.markdown-body ul,.markdown-body ol,.markdown-body dl,.markdown-body table,.markdown-body pre,.markdown-body details'] or ('--base-text-weight-normal:400' in decl):
   rules.append({'file':str(f.relative_to(root)),'sha256':sha(f),'selector':sel,'declarations':decl,'offset':m.start()})
save('destination-typography-conclusion.json',{'T11_skill_commit':'a2389390c0709d65af4a3cf070a04e396e4a4792','T11_skill_local_file':'candidate1-SKILL.md','T11_skill_sha256':sha(root/'candidate1-SKILL.md'),'scope':'Static current destination DOM, ancestor chain, inline/page styles, and all 21 exact current href-linked CSS responses. No alternate renderer is used to certify destination typography.','current_stylesheet_count':len(css['fetches']),'all_stylesheets_current_status_200':all(r.get('status')==200 for r in css['fetches']),'prior_stylesheets_reused':False,'article_tag_inventory':{'article':1,'p':218,'a':59,'math-renderer':337,'ul':1,'li':2},'font_leaf_rules_scanned':590,'class_or_global_candidates_manually_inspected':22,'result':'No forced bold/italic prose found in the inspected current static destination representation. All actual prose is in plain p, a or li nodes; no headings, table headers, captions, strong/em, labels or other emphasizing structures occur. Of the candidate font rules, body applies with --base-text-weight-normal:400. Heading/th/dt/b/strong/dfn/label/kbd/input/optgroup/emoji/toc rules do not match the article or ancestor nodes. The default font-style remains normal; no relevant inline or ancestor emphasis declaration exists.','relevant_exact_rules':rules,'limits':['CSS declaration inspection is not a browser-computed style measurement.','Dynamic styling, user-agent differences, responsive layout, extensions and client execution are unobserved.','Conventional math italics are exempt under T11.']})
notes={
1:'Title, route, initial exponent laws and four display equations legible. Final derivative display fits above page number; no clipping or overlap.',
2:'Secant bullet list, chain-rule displays and Task A1 legible. Part 2 label is isolated at bottom before its explanation on page 3: a secondary-preview pagination limitation.',
3:'Inverse/logarithm displays, fractions and final general-base identity legible; all content within margins.',
4:'Constant-base rule, Task A2, Part 3 and logarithmic identities legible; no clipping or overlap.',
5:'Changing-power derivatives, Task A3 and start of sequence limit legible. Bottom paragraph stays inside the page; no missing exponent/fraction parts.',
6:'Derivative-quotient limit chain and Task A4 prompt legible. Task A4 links fall at top of page 7: a secondary-preview pagination limitation.',
7:'A4 links, relative-rate displays and worked model legible. Task A5 prompt continues onto page 8 without missing text.',
8:'Task A5 continuation, A6 and hints A1-A4 legible. Hint A5 label is isolated at bottom before its body on page 9: a secondary-preview pagination limitation.',
9:'Hints A5-A6 and complete solutions A1-A2 legible. Hints and complete solutions share this internal preview page; this is not a learner PDF. Solution A3 label is isolated at bottom.',
10:'Solutions A3-A4 and start of A5 legible; long derivative display fits. A5 absolute-rate explanation follows on page 11.',
11:'Personally opened first to test P179 width, then included in complete page review. Both P179 percentage expressions fit on one line within text margins with no clipping/overlap; P182 also fits. A6 and source-scope paragraph legible.',
12:'Complete final P194 source/corrections paragraph present and legible, ending with the distinction in Part 5. Sparse final page is a pagination artifact; no omitted ending.'}
pre=json.loads((root/'preview/preview-check.json').read_text())
save('complete-visual-inspection.json',{'pdf':'preview/preview.pdf','pdf_sha256':sha(root/'preview/preview.pdf'),'pages':12,'render_dpi':120,'image_dimensions':[1020,1320],'every_complete_final_page_opened_with_view_image':True,'opening_order':[11,1,2,3,4,5,6,7,8,9,10,12],'PIL_all_images_verified_and_fully_decoded':pre['PNG_complete'] and all(i['fully_decoded'] for i in pre['images']),'PNG_exports_failed':False,'failed_export_recovery_required':False,'unchanged_PDF_after_export':pre['PDF_unchanged_after_export'],'all_pages':[{'page':i,'path':f'preview/page-{i:02}.png','sha256':sha(root/f'preview/page-{i:02}.png'),'complete_page_opened':True,'finding':notes[i]} for i in range(1,13)],'typography':'Body text and visible titles are regular roman; conventional math italics only. All 11 listed PDF font resources are embedded subsets with Unicode maps. No bold font resource is present.','no_clipping_overlapping_or_missing_glyphs_observed':True,'preview_pagination_limitations':[2,6,7,8,9,12],'not_destination_certification':'Pandoc/TeX pixels do not certify GitHub MathJax, CSS, computed styles, navigation or viewport behavior. No PDF hyperlink parity or learner-PDF acceptance claimed.'})
pre['full_page_visual_review']='COMPLETE; every final full page personally opened; see ../complete-visual-inspection.json for findings and preview pagination limits.'
(root/'preview/preview-check.json').write_text(json.dumps(pre,indent=2)+'\n')
report=r'''# D006 candidate1 v2 immutable representation review

Result: destination representation has a confirmed math-payload defect. Four of 337 math payloads lose nine backslashes. No prose loss or forced bold/italic prose was found in the inspected static destination. All A1–A6 navigation relationships and grouping checks pass. The internal 12-page secondary PDF preserves all source math and has no clipping; it does not clear the GitHub payload defect.

## Frozen input and scope

- GitHub repository: `alverstris/PROF-Skill.md-`.
- Commit: `09e12f4fad9f3108ec62bd6918d239dc4f732490`.
- Path: `runs/y1-reader-20261008/iterations/006/regenerated-r13-candidate1/teaching-v2.md`.
- SHA256: `53a69398d757bfe20c062450aace5a405ad66664a7f749b8f1f1cbbe2703efc3`; 28,786 bytes.
- T11 was read from actual candidate skill commit `a2389390c0709d65af4a3cf070a04e396e4a4792` and preserved locally.

Read-only cloud HTTP retrieved the immutable GitHub page and raw source. Embedded layout/blob paths and OIDs match; rejoining embedded raw lines plus the source terminal newline matches every input byte. The raw endpoint matches independently. `richTextTruncated` is false. The complete server richText article and actual server DOM text agree. The immutable source has no external figure assets. This is a rendering, typography and navigation review; it is not SASIS, a scientific acceptance review, or evidence of human learning.

## Confirmed destination defect

The article was parsed once with ordinary `HTMLParser(convert_charrefs=True)`. No second entity decoding, stripping of escaped entities, or backslash repair was used. All 291 inline and 46 display payloads were compared in source order, including every display's internal newlines.

| Paragraph | Math kind | Exact mismatch | Lost backslashes |
| --- | --- | --- | ---: |
| P177 | Inline | `-2\,\text{percent}` becomes `-2,\text{percent}` | 1 |
| P179 | Display | Five `\,\text{percent}` sequences become `,\text{percent}` | 5 |
| P182 | Display | Two `\,\text{percent}` sequences become `,\text{percent}` | 2 |
| P183 | Inline | `-2\,\text{percent}` becomes `-2,\text{percent}` | 1 |

The other 333 payloads match exactly. Backslash-comma is a LaTeX thin-space command; the destination instead supplies an ordinary comma. This is a real payload alteration, not wrapper syntax or an invisible-marker defect. Every numeric token remains in the same order. Replacing each math span with the same placeholder establishes exact full prose order after only whitespace folding and removal of documented Markdown/comment wrappers. The combined prose/math stream correctly remains FAIL. Full exact mismatches are in `payload-and-prose-findings.json` and `scoped-markup-navigation-audit.json`.

## Destination typography

All 21 exact href-linked current stylesheets were fetched with HTTP 200 and independently hashed; no historical CSS was reused. The full article has only article/p/a/math-renderer/ul/li structures: 218 paragraphs, 59 anchors including 25 targets, 337 math elements, one list and two list items. Titles are plain paragraphs. No headings, table headers, captions, strong/em/b/i nodes or style-bearing prose nodes exist.

The review preserved all 590 font/font-weight/font-style leaf rules and inspected the 22 candidates involving present classes or global selectors, alongside all article/ancestor inline styles and the page style block. The relevant body rule uses `font-weight:var(--base-text-weight-normal,400)`; current primitives and brand CSS define the variable as 400. `.markdown-body` sets 16px sans-serif text and line-height 1.5 without adding weight/style. Emphasizing rules for headings, th, dt, b/strong, dfn, labels and the table of contents have no matching article structures. No forced bold/italic prose was found in this static current destination evidence. Conventional mathematical italics are exempt. Exact rules, files, offsets and hashes are recorded in `destination-typography-conclusion.json`.

This is a declaration/DOM inspection, not an observed browser-computed cascade. Live pixels, user-agent behavior, dynamic style injection, MathJax execution and responsive client layout remain unobserved; the PDF is not used to certify destination typography.

## Navigation and inventory

All 25 source anchor IDs occur once, in the same order, with GitHub's `user-content-` prefix. All 34 link labels/hrefs match source order: 33 internal links and one external link to the named MIT source PDF. Each task A1–A6 links to its own hint and solution; each hint returns to its task; each solution returns to its task and own hint. All tasks precede the grouped hints, and every hint precedes the grouped complete solutions. The first route reaches hints, solutions and A6. Target paragraphs have the correct visible names.

Fragment hrefs remain `#task-a1` etc while sanitized IDs are `user-content-task-a1` etc. Literal prefixed target existence/order is established; GitHub's client fragment translation and actual clicks/scrolling were not executed. The external URL was inventoried, not independently content-reviewed here. Details are in `task-section-navigation.json`.

## Complete internal secondary preview

The exact immutable source bytes were copied to the Pandoc input without source edits or math delimiter conversion. All 337 source-to-AST math payloads match exactly including display newlines. The only TeX header additions define `\gt` and `\lt` as the conventional greater-than/less-than symbols. Pandoc and two pdflatex passes completed. The final log has no overfull, underfull, warning, missing or undefined diagnostic. All 11 font resources are embedded subsets with Unicode maps; text fonts are regular roman, with conventional math italic fonts.

The final PDF is 12 US Letter pages at 11pt with 25mm margins. SHA256: `737fdac66eeefc3899b314a5b4a071536011c6b92ed8fdd714b7faa8da091e57`. All 12 PNG pages are 1020×1320 at 120dpi, verified and fully decoded with PIL. No export failed; the PDF hash remained unchanged. I personally opened every complete final page using `view_image` in the order 11, 1–10, 12.

P179's full two-part percentage display fits inside both text margins on page 11, with no clipping or overlap. All other equations and the final P194 paragraph are visible. No missing glyphs or clipped body content were observed. The preview has ordinary pagination limitations: isolated labels at the bottoms of pages 2, 8 and 9; A4 links continuing onto page 7; A5's prompt split across pages 7–8; a sparse final page. Hints and solutions share page 9. Those are recorded secondary-preview limitations, not claims about continuous GitHub layout; this file is not a learner PDF or a certified linked PDF. Every page's specific inspection is preserved in `complete-visual-inspection.json`.

## Evidence integrity and limitations

The reusable frozen helper was read and run unchanged in markup-only mode. Its original failed/null checks remain in `generic-markup/` and `generic-helper-run.txt`; its older protected-inline/fenced-math and visible-label/q-h-s assumptions are unsuitable for this file. The separate scoped checks preserve its failure evidence, handle the actual syntax narrowly, and still expose the genuine four payload mismatches. No source, skill, repository, helper, shared state, or Git mutation was made. No browser, CUA or user-computer interaction occurred. No repair was applied.

Artifact hashes are in `artifact-hashes.json`; scripts, source bytes, complete capture, current raw CSS, exact audits, AST, two-pass logs, PDF and every final page image are preserved under this directory. This review does not assert GitHub live rendering/click success, global teaching acceptance, or human understanding.
'''
(root/'report.md').write_text(report)
manifest={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(root.rglob('*')) if p.is_file() and p.name not in ['artifact-hashes.json']}
save('artifact-hashes.json',manifest)
print(json.dumps({'report_sha256':sha(root/'report.md'),'report_bytes':(root/'report.md').stat().st_size,'artifact_count':len(manifest),'manifest_sha256':sha(root/'artifact-hashes.json'),'source_still_matches':sha(root/'teaching-v2.md')=='53a69398d757bfe20c062450aace5a405ad66664a7f749b8f1f1cbbe2703efc3'}))
