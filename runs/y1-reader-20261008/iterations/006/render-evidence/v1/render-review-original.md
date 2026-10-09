# D006 v1 original independent representation review

Current verdict: PASS for actual frozen server-delivered representation after an explicitly documented table-aware source normalization, and complete local-preview visual coverage (8/8 pages). No source-to-GitHub math payload mismatch, missing table cell, label, anchor or required A-E route was found. The original helper failure is preserved, not overwritten or relabeled. Live GitHub client pixels, MathJax behavior and clicking remain unobserved; this includes table-header weight and full T11 client-pixel compliance.

This is a representation review only. It makes no teaching-sufficiency, reader-performance or SASIS verdict. The generated PDF is internal QA evidence, not a user PDF deliverable. No browser or computer operation, subagent work, teaching edit, repository helper edit, skill edit or run-state edit was performed.

## Immutable source identity

The input was fetched directly from the immutable raw GitHub object, then saved as `frozen-teaching-v1.md` under this evidence directory. The changing worktree was not used as preview input.

- Commit: `e17c6ae521b5f8ff70e9f6e1ffa2ff66881b8663`.
- Repository path: `runs/y1-reader-20261008/iterations/006/teaching-v1.md`.
- Frozen source: 24,386 bytes; SHA-256 `d2946240bb9d5442919d1fb22f1f93b2f7626b69ad2e5a04178c283005f5bfdf`.
- Direct raw fetch returned HTTP 200 and matched the expected byte count and hash. The helper separately refetched that same frozen object and recorded exact local equality. The saved source hash remained unchanged through the final review.
- The immutable rendered GitHub page and extracted article are preserved under `capture-initial/`. Reextracting the article from that saved page equals the saved article exactly; the full-page bytes match the capture's recorded hash.

## Actual markup and the preserved helper failure

The existing helper reports all 320 inline and all 24 display math payloads exact after ordinary HTML parsing. Its paragraph labels, anchor sequence, internal href sequence and unique targets also pass. Its complete-text check fails because `prose_stream` retains Markdown pipe-table syntax at P17, source lines 67-70, while GitHub has serialized the same content as a semantic HTML table. The helper stops there, before PDF creation. Its original failed audit and no-preview record remain under `capture-initial/`.

The separate `independent_audit.py` does not edit the helper and does not add entity decoding. It parses the actual article with lxml once, independently checks every math-renderer payload in order, and compares the table structurally. All four header cells and eight body cells match exactly after the helper's existing math-wrapper conversion and whitespace normalization. The table has four columns, one header row and two body rows, in the expected order.

Only after verifying all 12 cells, the independent source normalization removes that table's outer/inter-cell pipe syntax and its Markdown alignment separator row. It retains every cell's content and order. Applying the helper's existing Markdown and whitespace normalization to this source representation gives an exact complete-article text match. Thus the initial failure is a source-normalization limitation, not a demonstrated GitHub content discrepancy. No broad character stripping, extra HTML unescape or inferred client normalization was used.

Additional exact checks: P01-P63 appear once and in source order; all 17 custom anchors appear once under GitHub's `user-content-` prefix and in order; all 24 link text/href pairs match source in order (23 internal, one external MIT source PDF link); every internal target resolves to exactly one corresponding prefixed ID. No image constituents are present.

## P17 typography scope and T11 boundary

The actual captured article uses one semantic table with four bare `<th>` header cells: “Curve”, “Secant endpoints”, “Secant slope and line”, and “Tangent at zero”. These header elements have no attributes. Across the entire article there are zero `<strong>`, `<b>`, `<em>` or `<i>` elements. The helper's no-emphasis tag check therefore passes at that explicitly limited markup layer; it does not examine computed CSS or default `<th>` font weight.

In the full page-3 internal preview actually viewed, all four header labels are upright and normal weight, with no visibly bold or italic prose. The PDF spans independently identify all four as `LMRoman10-Regular`, approximately 10.9091 pt, and the generated table TeX has no bold/italic emphasis commands. Mathematical variables use normal mathematical typography; this observation concerns table prose and header labels.

T11 forbids bold/italic prose including tables. No explicit emphasis markup or local-preview header-prose violation was observed. GitHub may apply destination CSS/default styling to semantic `<th>` headers; its live header pixels and computed style were not observed. Therefore this review does not declare full client-pixel T11 compliance, nor infer GitHub's visible header weight from the local preview or absence of `<strong>/<em>`. The exact evidence and boundary are preserved in `typography-scope.json`. No source or helper change was made.

## Explicit A-E navigation

The helper's numeric Q/H/S detector matches none and records null for its route/group checks. That is not treated as navigation success. The independent audit verifies all of these actual links, locations and destinations:

| Task | Task anchor paragraph | Outgoing hint/solution links | Hint destination | Solution destination | Hint return / solution return | Result |
|---|---|---|---|---|---|---|
| A | [P09] | [P09] | [P45] | [P51] | [P45] / [P51] | PASS |
| B | [P26] | [P26] | [P46] | [P52] | [P46] / [P54] | PASS |
| C | [P33] | [P34] | [P47] | [P55] | [P47] / [P56] | PASS |
| D | [P40] | [P40] | [P48] | [P57] | [P48] / [P59] | PASS |
| E | [P41] | [P42] | [P49] | [P60] | [P49] / [P63] | PASS |

Each outgoing hint and solution href appears once at the indicated prompt paragraph. Each hint has its one correctly named return link; each solution has its one correctly named return link, totaling two returns per task and ten returns overall. Task C starts at P33 and puts its links at continuation P34; Task E starts at P41 and puts its links at continuation P42. These are intentional multi-paragraph task spans, not missing routes. Longer solution returns similarly occur at their closing paragraphs.

The source and actual article both order all five `hint-a` through `hint-e` entries before the `solutions` group and all five `solution-a` through `solution-e` entries. `hints` leads to P44 and `solutions` to P50. The P02 routes to Task E, Hints and complete solutions are preserved. This establishes server markup destinations and routing intent; actual clicks and GitHub's JavaScript fragment handling were not performed.

## Faithful internal preview

After the independent representation checks passed, the unmodified helper's `prepare_preview` function was called on the saved immutable source in a separate new `preview-initial/` directory. This avoided changing or suppressing the original failed audit. The PDF skill was read in full and its creation marker ran successfully exactly once immediately before preview creation. The existing Pandoc/pdflatex pipeline was retained for consistent secondary rendering.

Only the protected-inline and fenced-display delimiters were converted for Pandoc. Every one of the 320 inline and 24 display mathematical payloads survives in its AST, including the table math. The local preamble supplies `\lt`/`\gt` aliases. Two LaTeX passes completed; there are no recorded overfull/underfull, warning, missing-glyph or undefined-command diagnostics. PDF text extraction preserves the full paragraph-label/reference sequence. These automated checks supplement the full visual inspection below.

The internal PDF has eight US Letter pages, 11-point type and 25 mm margins. Its SHA-256 is `b4ab3d405216521beed9ce90554ec0f27f13e3f9da0be1ed5ddf28470f49eed1` and remained unchanged through recovery and inspection.

## Actual full-page visual coverage

All eight complete pages were opened at 1020 x 1320 pixels from 120 dpi Poppler PNGs. No crop, excerpt or contact-sheet thumbnail substituted for a full page.

| Page | Actual full image opened | Findings |
|---:|---|---|
| 1 | `preview-initial/page-1.png` | Complete page viewed. P01-P09, positive-domain comparators, powers and the three difference-quotient/M(a) displays are legible. Task A begins near the bottom and continues on page 2. No clipped formula, missing glyph or footer collision observed. |
| 2 | `preview-recovery/page-2.png` | Complete recovered page viewed. Task A continuation and Hint A/Solution A labels are visible. P10-P17 inverse-log, base-change and secant-integral displays are legible. All comparison signs appear correctly. P17 table introduction ends this page and the full table follows on page 3. |
| 3 | `preview-initial/page-3.png` | Complete page viewed. The P17 table has all four headers and both complete rows; cell math, endpoints, slope-one lines and tangent inequalities are readable and remain within their columns. P18-P24, evaluation bar at zero and logarithmic derivative displays are legible. P24 introduction ends this page; its x^x calculation begins page 4. |
| 4 | `preview-initial/page-4.png` | Complete page viewed. P24 x^x display is readable at the top. P25-P32, Task B and its help labels, logarithmic sequence transformation and limit displays are clear. Parentheses, fractions, limits and evaluation bar are intact. P32 numerical comparison continues on page 5. |
| 5 | `preview-initial/page-5.png` | Complete page viewed. P32 continuation and P33-P40 are legible. Task C limit and direction notation, rate/log-rate display, percentages, units, and Task D help labels are visible. No clipped text, overlapping math or missing glyph observed. |
| 6 | `preview-initial/page-6.png` | Complete page viewed. P41-P51 includes the Task E display and continuation, source label, all five hints with their return labels, the separate solutions group label, and Solution A opening. Help groups are in the required order and are visually distinct by their labels/paragraph spacing. Solution A continues page 7. |
| 7 | `preview-initial/page-7.png` | Complete page viewed. Solution A continuation and return label, P52-P59, logarithmic product derivation, evaluated derivative, negative-sign sequence limit and fractional-rate display are legible. Return labels for B and C are visible; Solution D continuation/return is on page 8. No clipping or missing glyph observed. |
| 8 | `preview-initial/page-8.png` | Complete page viewed. P59 continuation and Return to Task D appear above P60-P63. Solution E logarithm, quotient-rule derivative, positive-domain condition and limit/continuity displays are readable. Return to Task E is present. The remaining page is normal end-of-document whitespace; footer is clear. |

## Recovery and minor preview findings

The initial page-2 PNG was truncated (73,728 bytes), confirmed by a full Pillow load, even though the exporter returned success. That file remains untouched under `preview-initial/`. The complete page was re-rendered separately from the unchanged PDF into `preview-recovery/page-2.png`, fully loaded, and opened for the inspection recorded above. The PDF and source were unchanged. The initial raster failure's cause is not established; it is not evidence of a source or PDF content defect. All seven other original page PNGs fully loaded and were viewed.

No clipping, overlap, missing glyph, missing label, table-cell overflow or unreadable equation was observed. Minor local pagination seams remain: Task A spans pages 1-2; P17's introduction and its complete table split across pages 2-3; P24's introduction and display split across pages 3-4; P32 continues pages 4-5; Solution A continues pages 6-7; and P59/Solution D continues pages 7-8. The P17 table itself stays together and all source content remains readable. These are preview-layout observations, not GitHub defects. No source or preview reformatting was required for representation fidelity.

The preview's link labels are readable, including the A-E hint/solution labels and all return labels. The hints and solutions occupy separate labeled groups on page 6 but need not occupy separate PDF pages. PDF hyperlink parity with GitHub is not claimed.

## Limits and evidence inventory

Actual server HTML is checked; live client pixels, custom-element/MathJax execution, GitHub CSS and responsive layout are unobserved. Hrefs and expected prefixed destination IDs are checked; clicking and fragment handling are unobserved. The local PDF is a separate renderer and cannot certify GitHub's live appearance.

- `frozen-source-fetch.json` and `frozen-teaching-v1.md`: direct immutable input and identity.
- `capture-initial/`: untouched helper capture, failed audit and initial no-preview record.
- `initial-helper-outcome.json`: original exit and classified normalization limitation.
- `independent_audit.py` and `independent-audit.json`: reproducible ordinary-parse payload, cell, text and A-E navigation audit.
- `preview-initial/`: unchanged PDF, initial page images, AST, LaTeX logs and original PENDING visual record.
- `preview-recovery/page-2.png`: separate recovered full raster.
- `typography-scope.json`: actual table/emphasis tags, observed preview header font, and the T11 client-pixel boundary.
- `preview-check.json`: current verdict, every actual full-page view, image hashes, recovery and exact limits.
- `artifact-hashes.json`: exact hashes for the source, original report and key evidence.
