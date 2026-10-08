# D004 v1 frozen representation review

No product representation defect was found within the observed scope. The initial failure was a paragraph-counting error in the review helper, not a change or defect in the teaching. After a narrow helper correction, the complete actual GitHub-delivered article passes text, math, typography, anchor and href checks. Explicit A–D navigation checks also pass.

All nine complete final preview pages were opened and visually inspected. All 30 display expressions, four tasks, all hints and complete solutions are present and legible. No clipping, overlap, missing glyphs, raw TeX or truncated content was observed. The preview has several page-break effects documented below; these are not asserted GitHub defects.

Live GitHub pixels, MathJax execution, responsive layout and click execution remain unobserved. The PDF is supporting internal QA, not the requested product. This is a representation review, not pedagogy or SASIS.

## Frozen input and preserved evidence

Canonical article: https://github.com/alverstris/PROF-Skill.md-/blob/197b57555834d36952e948d4100d2f835c86b20c/runs/y1-reader-20261008/iterations/004/teaching-v1.md

Frozen commit: `197b57555834d36952e948d4100d2f835c86b20c`.

Source: `/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/iterations/004/teaching-v1.md`; 22,691 bytes, 22,645 decoded characters; SHA-256 `5adb3e95c2fa47c94b4c665d85dc2fe669e2c0086dbc2ebc194cd59720d5d8ad`. The source was verified against that identity before and after review. There are no constituent images, image references or actual image elements.

The parent's first helper run had already fetched the actual immutable GitHub page and the raw source with HTTP 200, recording exact agreement with the frozen source. That initial evidence remains untouched in `../v1/`. This review reused the same immutable HTML bytes, independently extracted and parsed the complete article, rechecked the local source identity, and saved the corrected evidence in this new directory. No refetch or silently replaced original record was used.

The actual page SHA-256 remains `ec8718015dbe2f244f847497c0715563eb10e05e64dda3d3808d1d0f831435fe`. `github-page.html`, `github-article.html`, `github-article-text.txt`, `source-fetch.json` and `image-fetch.json` in this directory are byte-identical copies of their initial counterparts. `preserved-originals.json` records hashes for all 82 pre-existing files across the original D002, D003 and failed D004 review directories; all were verified unchanged after this review.

No teaching, figure, skill or global changes were made. The only repository edits are the specifically authorized helper and its README under `runs/y1-reader-20261008/tooling/frozen-render-review/`. No GitHub write, browser/CUA session or installation was attempted.

## Initial failure and narrow correction

The old helper counted actual labels with an unrestricted search across the entire rendered text. D004 contains 36 leading P labels and 31 additional bracketed P cross-references in prose, so that search returned 67 occurrences. Its source-side comparison counted only the 36 leading labels. This mismatch falsely failed `paragraph_labels_match_source_in_order` and `paragraph_labels_unique`. The original full-text, math, anchor, href/target and typography checks already passed.

The correction addresses the identified problems without changing teaching:

- Actual leading labels now come from actual HTML paragraph starts. All label/reference occurrences remain available separately.
- The latest P label carries across following body paragraphs and display-separated continuations when associating a link with its source paragraph. D004 places labels/titles in separate ordinary paragraphs, so dropping that label produced null source associations.
- The PDF extraction check compares all label/reference occurrences against all corresponding source occurrences. It no longer compares all PDF occurrences with only source-leading labels. A PDF line start is not treated as proof of a paragraph start.
- Absent q/h/s-specific checks are now explicitly null/not applicable, with a custom-navigation flag. Empty generic collections are not evidence for D004's named task/hint/solution scheme.

The exact patch is preserved as `helper-patch.diff`; the pre-patch Python file is `helper-before.py`. The README documents the corrected count semantics, custom-navigation requirement and use of the versioned helper copy rather than the older scratch prototype.

`regression-d002-d003-d004.json` records exact checks against cached actual D002, D003 and initial D004 HTML, without refetching or changing earlier reports:

| Artifact | Actual leading P labels | All P occurrences | Inline/display payloads | Internal hrefs / anchors | Result |
|---|---:|---:|---:|---:|---|
| D002 | 72 | 72 | 330 / 24 | 41 / 22 | Existing exact checks and converted Markdown retained |
| D003 | 44 | 44 | 251 / 25 | 49 / 44 | Existing exact checks retained; carried link labels equal the earlier explicit navigation supplement |
| D004 | 36 | 67 | 275 / 30 | 22 / 14 | Corrected leading-label check and every other applicable markup check pass |

All three Pandoc AST comparisons retain every mathematical payload. D002 and D003 converted Markdown is identical to the earlier validated preview copies. The regression does not replace their prior visual reviews.

## Complete actual GitHub markup

The complete article text matches the frozen source after documented Markdown syntax removal, math-delimiter conversion and whitespace normalization. Math was protected while normalizing prose and separately compared exactly after HTML parsing. This check covers the entire article, including every cross-reference and the final source paragraph.

| Check | Observed result |
|---|---|
| Leading paragraph labels | P01–P36, once each and in order, derived from actual HTML paragraph starts |
| Label and prose-reference occurrences | All 67 are retained in order |
| Inline mathematics | All 275 payloads match exactly |
| Display mathematics | All 30 payloads match exactly |
| Typography | No bold, italic-prose or heading elements; no ATX headings; math italics are conventional notation |
| Article structure | One article, 114 paragraph elements, 305 math-renderer elements, 38 anchor elements, zero images |
| Internal anchor IDs | All 14 expected unique sanitized IDs are present at the correct P labels |
| Internal hrefs | All 22 match the frozen source in order and have unique corresponding targets |
| Remaining hrefs | Both external MIT source/terms hrefs match the source; endpoint availability and subject content were not re-reviewed |
| Groups | Hints P26–P30; separate complete solutions P31–P35; P36 is source/scope |

P headings are plain paragraph text, as required. Plain bracketed cross-references such as `[P03]` are not additional paragraph labels or hyperlinks in this source and were not silently converted into links.

The actual HTML uses hrefs such as `#task-a` with GitHub-sanitized IDs such as `user-content-task-a`. The corresponding target markup is present. This does not claim observed client fragment handling or click behavior. No PDF hyperlink parity is claimed.

## Explicit A–D navigation

The actual delivered task, hint and solution destinations were checked independently of the inapplicable generic q/h/s scheme. `navigation-check.json` records each link and its carried source P label.

| Task | Task anchor / P label | Hint anchor / P label | Solution anchor / P label |
|---|---|---|---|
| A | task-a / P06 | hint-a / P27 | solution-a / P32 |
| B | task-b / P09 | hint-b / P28 | solution-b / P33 |
| C | task-c / P19 | hint-c / P29 | solution-c / P34 |
| D | task-d / P23 | hint-d / P30 | solution-d / P35 |

For every task, its hint and solution links match; its hint returns to the matching task and links to the matching complete solution; its solution returns to the matching task. These are 20 verified links. The two additional links from P02 point to `hints`/P26 and `solutions`/P31, completing all 22 internal hrefs. The complete hints group precedes the solution group in the actual article. All 14 IDs map to the intended paragraph labels.

## Internal preview and every complete page

The already-read PDF skill was applied, reusing the parent's successful pre-authoring marker for this same intended PDF operation. No additional marker was run. The corrected helper's preview function uses the same transparent conversion: protected inline math becomes ordinary dollar-delimited math, and fenced math becomes display-dollar blocks. All 275 inline payloads and all 30 display payloads are retained; the Pandoc AST confirms exact payloads after removal of the single conversion-wrapper newline on each side of a display. The header only supplies the existing `\gt` and `\lt` compatibility definitions.

The preview was compiled twice by pdflatex at 11 pt with 25 mm margins on US Letter pages. The final PDF has nine pages. Every complete page was rendered and successfully opened as a 150 dpi JPEG from that same final PDF. These were full-page inspections, not crops, contact sheets or text extraction alone. There is no figure to inspect in this artifact.

| Complete page opened | Inspected content | Display formula indices |
|---|---|---|
| 1 | Complete P01–P04 and the P05 label/title | 1–3 |
| 2 | P05 body, complete P06–P09, Tasks A and B | 4–6 |
| 3 | Complete P10–P11 and P12 through its final display | 7–12 |
| 4 | P12 conclusion, complete P13–P16, P17 label/title | 13–15 |
| 5 | P17 body, complete P18–P19 including Task C, P20 through the third-power display | 16–21 |
| 6 | P20 continuation, complete P21–P24 including Task D, P25 label/title | 22–24 |
| 7 | P25 body, complete P26–P32: every hint, separate solution introduction and complete Solution A | 25 |
| 8 | Complete P33–P35: full Solutions B–D, then P36 beginning | 26–30 |
| 9 | Complete remaining P36 source/scope prose and final sentence | — |

All 30 displays were visually inspected. The increment-definition line, remainder expression, composition difference quotient, both negative-power chains, derivative-order displays, long induction chain, second-derivative chains and final cube comparison fit and are legible. Fractions, evaluation bars, superscripts, primes, inequalities, minus signs and parentheses render without collisions or truncation. Every hint and every complete solution, including their return-label text, was inspected.

No clipping, overlap, black boxes, missing glyphs, unrendered TeX or missing content was observed. The final LaTeX log contains no overfull/underfull or other warning diagnostics. Text extraction additionally confirms all 67 label/reference occurrences in source order; it does not substitute for the full-page visual inspection.

## Actual local pagination findings and limits

The local PDF has these bounded layout effects:

- P05's label/title appears at the bottom of page 1 and its body begins on page 2.
- P17's label/title appears at the bottom of page 4 and its body begins on page 5.
- P25's label/title appears at the bottom of page 6 and its body begins on page 7.
- P12's conclusion follows on page 4 after its page 3 display; P20's displays span pages 5–6; P36 spans pages 8–9. Every continuation was opened and inspected.
- The hints and complete-solutions groups share preview page 7 while retaining their separate source groups. No PDF help-page-segregation requirement was imposed.

These are concrete properties of the internal fixed-page preview. They are not evidence that the scrolling GitHub article has the same breaks, and they do not justify silently changing the frozen Markdown. The preview was not re-laid out to hide them.

The PDF uses local fonts and pdflatex rather than GitHub client CSS/MathJax. Actual delivered HTML has been inspected; live GitHub pixels, MathJax execution, responsive behavior and clicking remain explicitly unobserved. The conclusions are limited to the actual markup and the supporting full local-preview inspection.

Compact result: `review-summary.json`. Complete page record and provenance: `preview-check.json`. Custom navigation: `navigation-check.json`. Original failure evidence remains in `../v1/`; its files and all earlier D002/D003 reports are unchanged.
