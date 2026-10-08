# D003 v1 frozen representation review

No product representation defect was found within the observed scope. The complete actual GitHub-delivered article passes the text, math, typography and destination-markup checks. All eight complete pages of the internal preview were visually opened and inspected, including the figure, every attempt, all hints and all complete solutions; no clipping, overlap, missing glyphs, unrendered mathematics or unreadable labels were observed.

This does not establish live GitHub client rendering. Live GitHub pixels, MathJax execution, responsive layout and click execution remain unobserved. The PDF is an internal secondary-renderer preview, not the requested product. This review concerns representation, not pedagogy or SASIS.

## Exact frozen inputs and original evidence

Canonical article: https://github.com/alverstris/PROF-Skill.md-/blob/4cbf83f2dc2859d5123fc01a0c311a268d580483/runs/y1-reader-20261008/iterations/003/teaching-v1.md

Frozen commit: `4cbf83f2dc2859d5123fc01a0c311a268d580483`.

| Input | Identity verified before and after review |
|---|---|
| `/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/iterations/003/teaching-v1.md` | 25,480 bytes; 25,408 decoded characters; SHA-256 `cd7426a9b70d0ac41aa3ca0418db8c89c391b67304016a7ad38f8379fe98b5a8` |
| Same-directory `product-increment-v1.png`, the sole constituent | 23,338 bytes; SHA-256 `61bc47e951267028b32ac0007370244d8d6489e8552639572a56bdf5cc2ad2b0` |

The reusable `frozen_render_review.py` fetched the actual immutable GitHub page and independently fetched the source and image from public raw URLs at that same commit. All three requests returned HTTP 200. The raw source and raw image match the supplied local frozen bytes exactly. The downloaded image, rather than a reconstructed figure, was used in the preview.

The actual GitHub HTML is preserved as `github-page.html`: 417,122 bytes, SHA-256 `d2eca9fd26bd54b0bafd8aa1328e5e643cfcd9d24aa116f6aba44140f8c70140`. Its extracted article is preserved as `github-article.html` with the complete parsed text in `github-article-text.txt`. Original machine checks are in `markup-audit.json`, `source-fetch.json` and `image-fetch.json`. The initial automatic preview state is retained as `preview-check.initial.json`; the completed page inspection is in `preview-check.json`. Exact evidence hashes are recorded there.

Neither the teaching source nor the figure was changed. No repository, skill or GitHub writes were made. No browser/CUA session or installation was attempted.

## Complete actual destination markup

The entire article was parsed. Its complete text stream matches the frozen source after documented Markdown syntax removal, math-delimiter conversion and whitespace normalization. Mathematical payloads were protected during prose normalization and separately compared exactly after HTML parsing; the check did not rely on excerpts.

| Check | Observed result |
|---|---|
| Paragraph labels | P01–P44, each once and in order |
| Paragraph anchors | All 44 unique `user-content-p01` through `user-content-p44` IDs map to their corresponding P labels |
| Inline mathematics | All 251 payloads match exactly |
| Display mathematics | All 25 payloads match exactly |
| Typography | No bold, italic-prose or heading elements in the article; no ATX headings in the source; conventional math italics are allowed |
| Article structure | One article, 108 paragraph elements, 276 math-renderer elements, one image |
| Internal navigation | All 49 hrefs match the source in order and have a unique corresponding target |
| All hrefs | 51 total: the 49 internal links, the frozen image blob wrapper, and the MIT source link; both remaining hrefs also match their intended source/frozen targets |
| Image markup | Same frozen-commit raw path, complete descriptive alt text and `max-width: 100%`; wrapper points to the same frozen image's blob page |
| Support groups | P33 introduces hints A–E at P34–P38; P39 introduces complete solutions A–E at P40–P44; all hints precede the solution group |

The image occurs after P19 and before P20 in the actual article. The external MIT href and label were checked as destination markup; this review did not undertake a new subject-source review or test that endpoint's availability.

GitHub's delivered HTML pairs hrefs such as `#p09` with sanitized IDs such as `user-content-p09`. Every such pair is present. This is a check of actual destination markup, not observed client-side fragment handling or clicks. No navigation inference was made from the preview PDF.

## Every attempt and support navigation route

D003 uses paragraph anchors rather than D002's q/h/s identifiers. The helper's q/h/s-specific fields are therefore not evidence for D003's A–E mapping. A separate check against the complete actual article, retained in `navigation-check.json`, carries paragraph identity across display-separated continuation paragraphs and verifies every matching route below.

| Attempt | Prompt | Hint | Complete solution | Continue/resume destination |
|---|---|---|---|---|
| A | P09 | P34 | P40 | P10 |
| B | P21 | P35 | P41 | P22 |
| C | P26 | P36 | P42 | P27 |
| D | P30 | P37 | P43 | P31, transfer attempt E |
| E | P31 | P38 | P44 | P03, reading route |

For each A–E entry, the prompt's hint and solution links, the hint's return and solution links, the solution's return and resume/transfer/reading-route links, and both group-index links were verified. A–C also have the correct prompt continuation links. The P03 group links, P33 link to the complete-solutions start, and P32 return to the reading route were checked. All 49 internal hrefs and their target labels are recorded, including links after display equations within P41–P44.

## Internal preview and full-page visual coverage

The PDF skill's existing workflow was applied. The converted copy changes only protected inline math delimiters to ordinary dollar delimiters and fenced math blocks to display-dollar blocks. The Pandoc AST retains all 251 inline payloads exactly and all 25 display payloads exactly after removing the one added wrapper newline on each side. Prose, image reference and mathematical payloads were not edited. The header supplies only the existing LaTeX-compatible `\gt` and `\lt` definitions.

Pandoc/pdflatex compiled the internal preview at 11 pt with 25 mm margins, using two LaTeX passes. The final preview has eight US Letter pages. Page 1 was successfully opened as its full 120 dpi PNG. The page 2 PNG encountered an image-viewer decode error, so the same final PDF was also rendered to full 150 dpi JPEG pages; pages 2–8 were each successfully opened in that form. The original constituent figure was also opened separately. Inspection was of complete pages, not thumbnails, crops or text extraction alone.

| Complete PDF page opened | Inspected content | Display formula indices |
|---|---|---|
| 1 | P01–P07, including all derivative, sum and constant-multiple displays | 1–4 |
| 2 | P08–P13 and P14 opening; Attempt A, units, standard limits, full sine/cosine chains, degree conversion | 5–7 |
| 3 | P14 display and continuation, complete P15–P18; product split, product rule, example and exact increment expansion | 8–13 |
| 4 | Complete P19, complete figure, complete P20, P21 opening | 14 |
| 5 | P21 continuation, P22–P25, P26 opening; complete quotient derivation and worked derivative | 15–18 |
| 6 | P26 continuation, P27–P34 and most P35; complete Attempts C–E, attribution, hint introduction, Hint A and most Hint B | — |
| 7 | P35 final solution-link label, complete P36–P42; remaining hints, solution introduction and complete Solutions A–C | 19–20 |
| 8 | Complete P43–P44 and every continuation paragraph; full Solutions D–E and final navigation labels | 21–25 |

All 25 display expressions were visually covered. The long sine/cosine derivations, exact product split, product difference quotient, quotient chains and both final Solution E chains fit without clipping or collision. Fractions, prime marks, radicals, subscripts, superscripts, minus signs and units were legible. The figure on page 4 follows P19, with all four regions, side arrows and `u`, `v`, `Delta u`, `Delta v` area/length labels separated and readable. The entire hints group and complete-solutions group were inspected through the end of P44.

No clipping, overlapping text, black boxes, missing glyphs, raw TeX, truncated mathematical content or unreadable figure labels were observed. The final LaTeX log contains no overfull/underfull, missing-glyph or other warning diagnostics. PDF text extraction independently confirms all P01–P44 labels in order, but was not substituted for visual inspection.

## Bounded differences and limitations

The following are local preview effects, not observed GitHub failures:

- Pandoc turns the figure's descriptive alt text into a Figure 1 caption. Actual GitHub markup retains it as alt text. The figure itself remains after P19 in both observed representations.
- P14's opening and display cross pages 2/3; Attempt B crosses pages 4/5; Attempt C crosses pages 5/6. Every continuation was inspected.
- Hint B's final “Solution B” link label appears at the top of page 7 after its remaining text on page 6. It is present and legible, with the actual GitHub href independently verified.
- Hints and solutions retain their separate source groups but share preview page 7. No extra PDF page-segregation requirement was imposed.

The preview uses local fonts, pdflatex, fixed pages and PDF layout rather than GitHub client math/CSS. Its visual success is supporting evidence, not proof of live GitHub rendering. Live GitHub pixels, MathJax execution, responsive behavior and clicking are explicitly unobserved. No PDF hyperlink parity is claimed.

Compact structured result: `review-summary.json`. Detailed full-page inspection and provenance: `preview-check.json`. Actual A–E navigation evidence: `navigation-check.json`. The PDF remains internal QA and is not proposed as a new deliverable.
