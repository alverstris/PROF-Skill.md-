# D001–D007 affected-earlier-evidence review

This targeted review maps the accepted earlier documents to the markup-preservation paragraph now frozen in PROF r15. It reviews historical final-revision destination and preview evidence, verifies local byte/Git identities, and adds a separately attributed D001 final-preview supplement. It does not claim that these seven documents were regenerated under r15, that a fresh SASIS review occurred, that a student learned from them, or that the candidate or run is ready for closure. Parent review owns that decision.

The reviewed candidate is `7ea4148ed1eda90436c0f6f23fde479de3452079:SKILL.md`, SHA-256 `24b8c2e2d1898384f85eca608f34074d91a78268efcec69d7ceb81052a87659e`, 37,867 bytes. Its local Git blob contains this exact new paragraph:

> For mathematics delivered through markup, check that the actual destination preserves every intended expression’s operands, operators and grouping, including inline mathematics and help. Use destination-supported syntax to prevent parser collisions; correct source, protected delimiters or another renderer’s preview alone cannot establish preservation. Distinguish parsed-content checks from live visual inspection.

The candidate identity and paragraph are recorded in [candidate-paragraph-binding.json](candidate-paragraph-binding.json). The review uses published reference `e35a59a64ed1b01f7ae43e4ef46042f23cc7e2d6` for the accepted earlier files; this is a local immutable-reference check, not a new GitHub poll or claim about a later main head.

## Exact accepted artifacts

Paths are relative to `/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/iterations/`.

| Case | Final teaching path | Teaching freeze | SHA-256 |
|---|---|---|---|
| D001 | `001/teaching-v4.md` | `0716ea92991d7f9fe2814e137bcc830d91a27511` | `402485baa2767af9625146721e356f92bad76e4cfb738e5729c6c8b94ea79401` |
| D002 | `002/teaching-v1.md` | `f1c0e91c24e9140049d50c7ca965f41e36f3e1a2` | `8139080278edb96287576629e7d80933b380c1b82af60d3ede888d500cb68a3a` |
| D003 | `003/teaching-v1.md` | `4cbf83f2dc2859d5123fc01a0c311a268d580483` | `cd7426a9b70d0ac41aa3ca0418db8c89c391b67304016a7ad38f8379fe98b5a8` |
| D004 | `004/teaching-v1.md` | `197b57555834d36952e948d4100d2f835c86b20c` | `5adb3e95c2fa47c94b4c665d85dc2fe669e2c0086dbc2ebc194cd59720d5d8ad` |
| D005 | `005/teaching-v2.md` | `32c553f279ac1e5771ff05b78a9951cbff3fee38` | `4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6` |
| D006 | `006/regenerated-r13-candidate1/teaching-v3.md` | `28825d27b93baef43a5751eacecac81fa46841bc` | `311afdef083a4468f18bcdd11a68975d2e6622661e0be3405a5c9f58b3f3a813` |
| D007 | `007/revised-v3/teaching-v3.md` | `2c0a49dff10d407296675a9d52a2d664be1bb0f0` | `6dc2823d9f931c1baaa6eb4ce5076ed2aef1859ba29255d5503eed627824ae54` |

All seven current local teaching files equal their recorded hashes, local frozen Git blobs, and corresponding blobs at published reference e35a59a. The same frozen/published identity checks cover the two constituent figures: D002 `figures/unit-circle-proof-v1.png`, SHA-256 `95616719d3035e9f174367b55c48ccb3e04a8cbf5105434115e4bddff0b3c75d`; D003 `product-increment-v1.png`, SHA-256 `61bc47e951267028b32ac0007370244d8d6489e8552639572a56bdf5cc2ad2b0`. A further 37 final closure/report/audit/preview-record files equal the explicit published-reference blobs. The complete file paths, sizes, hashes and checks are in [exact-bindings.json](exact-bindings.json); [verify_bindings.py](verify_bindings.py) performs only local `git show`, reads and scratch output.

## Substantive preservation and coverage witnesses

Counts below describe all final source formal math payloads, compared in order with the actual immutable destination's served article after ordinary HTML parsing. They are not sample sizes or readiness flags. Exact payload equality preserves every source operand, operator, grouping character, sign and factor within those expressions at that parser layer. It does not independently prove that the source expresses the intended mathematics correctly or that a later client renderer displays it correctly.

| Case | Complete inline / display witness | Included help | Final secondary-preview evidence |
|---|---:|---|---|
| D001 v4 | 249 / 39 | Hints P32–P35; complete solutions P37–P40 | Original final pages 2/6; supplemental final pages 1/3/4/5/7/8 |
| D002 v1 | 330 / 24 | All six hints P52–P58 and complete solutions P59–P72 | All 11 complete final pages in original review |
| D003 v1 | 251 / 25 | Hints A–E P33–P38 and complete solutions P39–P44 | All 8 complete final pages in original review |
| D004 v1 | 275 / 30 | All four hints and complete solutions P26–P35 | All 9 complete final pages in original review |
| D005 v2 | 280 / 23 | All five hints P28–P33 and complete solutions P34–P40 | All 8 complete final pages, including recovered pages 1/7 |
| D006 candidate1-v3 | 291 / 46 | All A1–A6 hints and complete solutions | Root's complete final 12-page review after interrupted renderer |
| D007 v3 | 338 / 33 | All Q1–Q7 hints and complete solutions | Original renderer's complete final 10-page review |

D001's final `001/render-review-v4-original.md:17` specifies comparison of every expression, ordinary HTML parsing, and no extra entity-decoding or payload-whitespace normalization. Its table at line 21 gives 249/249 inline and 39/39 display equality; line 30 specifically records both aligned row separators and the P26 comparator. The final source audit and retained article have also been independently compared locally during this preparation: all 288 expressions agree without a second unescape. Earlier failed destination versions do not supply this final-v4 result. The original final-preview report only personally inspected pages 2 and 6 and carried unchanged content from an earlier complete preview; the new six-page supplement below addresses that precise limitation.

D002's `002/render-review-v1-original.md:16` states whole-article comparison, with math protected from prose normalization and compared exactly; lines 21–22 give the full 330/24 comparison. Line 27 maps all help, and lines 49–65 describe opening every complete final page, recovering pages 2/8 as complete JPEGs, and checking long derivations, inline degree-angle notation and both support groups. The retained actual article, source and complete audit arrays have now also been compared with one ordinary parse, with no unequal expression or unexpected nested math markup.

D003's `003/render-review-v1-original.md:26` states the complete article/math comparison; lines 32–33 give 251/25 exact payloads, including all complete solutions through P44. Lines 63–76 describe all eight full pages, the figure and all display expressions. The original report explicitly rejects vacuous question/hint/solution helper fields for its paragraph-anchor scheme and uses the separate real A–E navigation check. The retained actual article, source and audit arrays also agree under the supplemental ordinary single parse.

D004's `004/render-review-v1-original.md:46` onward separates complete normalized article equality from exact mathematical payload comparison; lines 54–55 establish all 275/30 expressions. Help is explicitly mapped at lines 67–78 and is included in the same whole-source comparison: 19 hint inline payloads and 44 inline/6 display solution payloads. Lines 80–100 and `render-preview-v1.json` cover every final page and all 30 displays. The current retained article comparison reproduces exact equality without nested HTML in math; all recorded final page/PDF hashes still match.

D005's `005/render-evidence/v2/render-review-original.md:15` onward explicitly excludes additional entity unescaping and compares all 280/23 final payloads. The 13 repaired inline spans retain their 17 named comparison-sign spellings; failed v1 serialization remains separate. Its help contributes 22 hint inline payloads and 45 inline/7 display solution payloads, all included in the whole comparison. Lines 30–53 document every complete final page, including recovered pages 1/7 from the unchanged PDF. The retained article comparison and all recorded final page/PDF identities agree.

D006's `006/render-evidence/candidate1-v3-recovery/report.md:11` specifies all 337 final mathematical payloads, types, order and internal display newlines after one ordinary parse, with no extra decoding. Numeric-token order and the percentage signs/factors/units at P177/P179/P182/P183 are explicitly checked. Line 13 maps all help and navigation; a separate frozen-source inventory gives 23 inline hint payloads and 66 inline/13 display solution-and-ending payloads. The preserved full source/destination arrays were compared locally again with zero unequal type/payload positions. Line 21 and `root-preview/inspection.json` document all 12 complete pages from the exact final PDF; the final report is explicitly root-completed, not a verdict invented for the interrupted renderer. Original truncated exports, 20 PDF-target warnings and page seams remain disclosed.

D007's `007/render-evidence/v3/report.md:5` establishes all 371 ordered typed payloads after one ordinary parse, complete prose/math and independent numeric-token checks. Line 7 maps all help; the frozen-source partition includes 42 inline hint payloads and 76 inline/9 display solution-and-ending payloads. Its preserved full type/payload arrays were also recomputed locally with zero unequal positions. Line 11 binds all 371 preview AST payloads to source/destination expectations and records personally opening all 10 complete final pages, reopening 2/9. Named comparisons and retained thin spaces are visibly valid in that separate renderer. The 31 PDF-target warnings, page seams and disclosed log anomaly remain part of the evidence.

The detailed prior-report passages, retained capture identities, preview PDF/page identities and preparation methods are in [D001–D003 mapping](d001-d003/mapping.md), [D001–D003 retained-capture comparison](d001-d003/retained-capture-recheck.json), [D004–D005 mapping](d004-d005/d004-d005-preparation.md), [D004–D005 local comparison](d004-d005/local-evidence-verification.json), and [D006–D007 mapping](d006-d007/mapping.json). Those early mapping documents retain their original preparation scope; the D001 supplement is additional evidence and does not rewrite them.

## Supplemental D001 final-preview review

The missing final-v4 whole-page coverage was the only concrete historical preview gap identified. The unchanged eight-page final PDF is `/workspace/scratch/ac36b9c5ff31/prof-readability/d001-render-review/v4/preview.pdf`, SHA-256 `62aa9ea95c941630f8da512bcabb08857a94f636b03ecbceb17d534dd8fc51d9`. At the parent's request, the historical reviewer generated and personally opened complete final pages 1, 3, 4, 5, 7 and 8, compared their visible notation/text to the final source, and recorded page-specific findings. Page 5's PNG produced a viewer decode failure; the failed file was preserved and the same full page was successfully opened as a JPEG generated from the same unchanged PDF.

The separate [supplemental report](d001-final-v4-visual-recheck/report.md) and [inspection record](d001-final-v4-visual-recheck/inspection.json) give exact source/PDF/page-image identities and observed page boundaries. Their six directly inspected final pages combine with the original final-v4 pages 2/6 inspection; this closes the identified coverage gap without asserting that the original reviewer had previously opened all final-v4 pages. This is secondary-preview evidence, not live GitHub viewing.

## Disposition and remaining limits

The exact r15 paragraph is supported by explicit earlier final-version preservation evidence for every D001–D007 formal inline/display expression, including every help group. There is no remaining named parser-preservation or complete-secondary-preview coverage gap after the D001 supplement. No further source research, repolling of unchanged GitHub pages, author regeneration, or repeat visual review of D002–D007 is indicated solely by this paragraph. This is the scoped evidence disposition for parent review, not a substitute for the active D008 fresh-generation and fresh-reader loop.

Every case retains the same important boundary: the actual destination evidence is the captured served/parsed representation. Live GitHub pixels, MathJax execution, computed CSS, responsive layout and actual clicking remain unobserved. The new paragraph expressly distinguishes those layers; the secondary previews cannot establish actual-host parsing and the parsed-content comparisons cannot establish client pixels. A stronger future requirement for live-client correctness would require a separate check rather than relabelling the existing evidence.

No original closure, report, teaching file, skill, queue, count or Git object was changed during this review. New files are only this scratch preparation and the explicitly requested D001 visual supplement. The local capture comparisons are consistency checks of retained evidence, not fresh server observations. Source truth, explanatory sufficiency and the correctness of students' available conclusions remain separate semantic/SASIS responsibilities; this review does not infer them from string equality.
