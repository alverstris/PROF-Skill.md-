# D005 v2 original render review

Result: the actual frozen GitHub server markup passes exact-payload and structural checks. All eight pages of the separate local PDF preview were opened in full. No clipped or overlapping content, unreadable equations, missing glyphs, or lost paragraph/help labels was observed. Minor preview pagination seams and a recovered PNG export defect are recorded below. Live GitHub client rendering, MathJax behavior, and clicking remain unobserved.

## Identity and scope

- Immutable source commit: `32c553f279ac1e5771ff05b78a9951cbff3fee38`.
- Source path: `runs/y1-reader-20261008/iterations/005/teaching-v2.md`.
- Source: 24,261 bytes; SHA-256 `4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6`.
- The GitHub raw source fetched during this review returned HTTP 200 and exactly matched those local bytes. Source hash was checked again after visual inspection and is unchanged.
- PDF: `preview.pdf`, eight US Letter pages, 11-point type and 25 mm margins; SHA-256 `26f6aae873b2c75330c65fd143af0ce11fd486b417141d1a9594978e22afc533`.
- Helper: the existing frozen-render-review script. Neither helper nor teaching source was edited. The parent had already performed the PDF operation marker once for this D005 preview operation; no additional marker was run.
- This report assesses actual captured markup plus secondary preview presentation. It is not a teaching-content review, empirical reader result, or a live GitHub visual sign-off.

## Actual frozen GitHub markup

Every recorded markup check passes after ordinary HTML parsing, without an extra entity-unescape pass:

- 280/280 inline and 23/23 display mathematical payloads exactly match the frozen v2 source, including order and whitespace.
- The 13 changed comparator spans retain their source `\lt`/`\gt` spellings exactly. The raw captured article has no `&amp;lt;` or `&amp;gt;` form. This directly verifies the intended serialization repair for this new version.
- The complete article text matches source after the helper's documented Markdown/whitespace normalization.
- P01-P41 paragraph labels are present once and in source order; cross-references are separately preserved.
- All 17 source anchor IDs appear uniquely and in order under GitHub's `user-content-` prefix.
- The independent parser review found all 29 source link text/href pairs exact: 27 internal and two external. Every internal href has exactly one expected GitHub-prefixed target. Each Q1-Q5 has its matching hint and solution routes and the two returns.
- The hints precede the complete solutions. The specified bold, italic and heading markup is absent.
- There are no source image constituents or GitHub image elements in this version.

The independent audit used standard HTMLParser conversion, source math extraction and wrapper removal. It found no further mismatch. Presence of hrefs and destination IDs is the observed layer; actual navigation actions were not executed.

## Local preview preparation and page evidence

The helper changed only the protected-inline and fenced-display delimiters for Pandoc. Pandoc AST checks retain every source mathematical payload. The local LaTeX preamble supplies `\lt`/`\gt` aliases for this preview. Both LaTeX passes completed, the final log diagnostic list is empty, and extracted PDF paragraph-label/reference occurrences match source. Those automated results supplement, and do not substitute for, the following full-page views.

| Page | Full page actually opened | Visual finding |
|---:|---|---|
| 1 | `page-recovery-1.png` | Viewed complete recovered page. P01-P06 and all three display derivations are readable. The repaired P04 -1 < x < 1 relation renders as comparison signs. The long circle derivative chain stays within margins. Q1 begins near the bottom and its target/completeness prose continues on page 2; no text is clipped. |
| 2 | `page-2.png` | Viewed complete page. Q1 continuation and links remain readable. P07 product/implicit derivative displays fit, including the wide final derivative/condition. P08-P12 prose and Q2 help labels are clear; inverse identity display fits. P12 reflection prose continues on page 3. |
| 3 | `page-3.png` | Viewed complete page. P12 continuation, P13-P17 and inverse identity/reciprocal quotient displays are readable. Repaired P16 l < a < r appears correctly. Nested fractions in the difference quotient remain distinct. The final inverse formula is above the page number without collision; its explanatory continuation starts page 4. |
| 4 | `page-4.png` | Viewed complete page. P17 continuation and P18-P21 are clear. Cubic inverse, rational-power and exponent-simplification displays fit within margins. P19 and P20 repaired positive-domain relations render as > signs. The zero quotient remains readable; P21 endpoint/constant-function prose continues page 5. |
| 5 | `page-5.png` | Viewed complete page. P21 continuation and P22-P27 are readable. Repaired x > 0, arctangent -pi/2 < y < pi/2, 1+x^2 > 0 and cos y > 0 appear as intended comparison signs. Arctangent and triangle displays are legible. Q3/Q4 hint and solution labels remain visible. Q5 starts at the bottom and continues page 6. |
| 6 | `page-6.png` | Viewed complete page. Q5 continuation has its matching help labels. All five hints P29-P33 and the P28/P34 group labels are readable in order. P35 solution and repaired -1 < x < 1 interval are clear. S1 tangent display and S2 implicit derivative display fit; S2 explanation continues page 7. Hints and solutions share this preview page without overlap. |
| 7 | `page-recovery-7.png` | Viewed complete recovered page. P36 continuation, P37-P40 and all rational-power, zero-quotient, inverse-slope and F/G derivative displays are readable. Fractions, cube-root indices, infinity and nonzero symbols are clear. P40 tangent lead-in finishes at the bottom while its display starts page 8; this is a preview-only pagination discontinuity, with content preserved. |
| 8 | `page-8.png` | Viewed complete page. P40 tangent display at the top is legible and its following explanation/return label are present. P41 source and terms link labels are readable. The remaining page is intentionally blank from normal document end; footer is clear. No clipped content, overlap or missing glyph was observed. |

All full pages were opened at 1020 x 1320 pixels from a 120 dpi Poppler rendering. No crop, excerpt or contact-sheet thumbnail was used as a substitute for a full final page.

## Defects and limitations observed

The initial PNG exports for pages 1 and 7 were truncated: the image viewer rejected them and a full Pillow load confirmed truncation, despite the helper's successful pdftoppm return code. The original files remain preserved. Each page was re-rendered individually from the unchanged PDF as `page-recovery-1.png` and `page-recovery-7.png`; both complete replacement images loaded and were visually inspected. The PDF SHA-256 remained unchanged. This was an export-artifact failure, not evidence of a damaged source or PDF; its cause was not established. `preview-check.json` points those page records to the actual recovered images viewed.

The local PDF has several readable cross-page paragraph continuations. The clearest minor layout issue is P40: the tangent lead-in ends page 7 and its display starts page 8. Q1 and Q5 also span page boundaries. No content is lost or clipped. These are secondary preview pagination observations, not GitHub layout findings, and no source change was made to address them. Page 8 has normal trailing whitespace after the final source paragraph. Hints and solutions share page 6 in separate labeled groups; this does not imply a navigation or ordering failure.

The preview presents source link labels as readable text; GitHub link styling, clicking, JavaScript fragment handling, responsive layout and hyperlink parity were not tested. GitHub's live custom-element behavior and MathJax output remain unobserved. The local visible comparator success and the actual server-payload equality are separate findings.

## Evidence records

`preview-check-generated.json` preserves the helper's initial PENDING visual record. `preview-check.json` contains the final per-page actual view status, image hashes, export recovery, pagination observations and identity checks. `markup-audit.json`, `github-page.html`, `github-article.html`, `source-fetch.json`, the Pandoc AST and LaTeX logs remain the original generated evidence. `artifact-hashes.json` records key final evidence hashes. The failed v1 capture and its diagnosis remain in their separate directories.
