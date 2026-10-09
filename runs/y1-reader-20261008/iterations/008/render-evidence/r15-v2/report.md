# D008 revised r15 v2 — bounded destination and whole-preview review

Status: PASS for actual immutable GitHub markup/content/navigation preservation, static typography scope, and readable whole-document internal preview within the limits below. This is not SASIS, scientific-content acceptance, live GitHub pixel validation, or a PDF hyperlink pass.

## Immutable identity and independent revision check

Commit `a6b7aaaf2ded04bb6b0c2da2528234d36ca2f6d4`; parent-supplied tree `1ab89016b14388d34f0d024308a1208b228f7eb0`. Path `runs/y1-reader-20261008/iterations/008/revised-r15-v2/teaching-r15-v2.md`. Fresh raw HTTP 200: 27,868 bytes, 27,819 UTF-8 characters, SHA256 `b6e93b986e2a77763c556a4b5fc5cb42f43269742d0af9bd06021d7aa3ad7668`. Fresh immutable HTML HTTP 200 SHA256 `96e8707ff5dd373fd7e8d04c5a836ce9b9e17de755ae631868871f92ccfd12b4`. Actual page OIDs/paths match the request; richText is untruncated. RawLines recover the exact source with its terminal newline. Full fetch URLs/times are recorded.

The r15 original was personally read completely. This review independently verified all source bytes by reversing exactly nine inline `\gt ` / `\lt ` substitutions, recovering original SHA256 `86b6338315866e711ddfcefd52e4a84b2bb99093c321ff6b7a8124c66c739718`. All nine changed payloads were inspected. No r14 source-equivalence assumption is made. Original failure evidence remains separately preserved under sibling `r15-original`.

## Actual destination

All 305 mathematical expressions (276 protected inline, 29 ordinary `$$` displays) retain exact payload, type and order after one ordinary HTML parse. No extra unescape, fuzzy equivalence or payload whitespace normalization is used. Complete prose/math stream and numeric tokens match after folding prose-stream whitespace. All 68 visible P001–P068 blocks and labels match, including the four complete task prompts. All source dollars/backticks are accounted for.

All 37 labeled links match exactly in order: 34 internal and three external. All 18 explicit id targets occur once in source order as GitHub `user-content-*` targets. Four task-to-own-hint/solution and return mappings pass. Fifteen explicit paragraph checks verify group entrances, all task links, end-core choices, hint returns, end-hints choices, solution returns and continuation/start links. Core ends at P054; hint heading P055; hints P056–P059; end hints P060; solution heading P061; solutions P062–P068. This is a check of document representation and help placement, not a test of the student or the reasoning supplied by the lesson.

## Fresh static style evidence

All 21 unique actual href CSS assets were fetched fresh and hash-verified. Four asset URLs and hashes changed from the immediately preceding original review; full comparison proves their only content differences are sourceMappingURL comments. The remaining assets are unchanged. All 590 font declarations were inventoried, and all 38 conservatively selected candidates exactly match the just-inspected original candidates. Actual article tags/classes/ids, ancestor scopes except the route, inline styles and style blocks were separately checked.

The applicable body normal weight is 400. The `.markdown-body` rule declares sans-serif, 16px, line-height 1.5, with ordinary paragraph margins. No matching forced bold/italic prose rule or inline override was found. Link underline and math-wrapper layout declarations were inspected. Inactive data-href themes are inventoried separately; no alternate-theme activation is claimed. This is manual static scope inspection, not a browser CSS/cascade engine. Whole stylesheet bytes and DOM evidence remain available.

## Faithful internal preview

The PDF skill was read before this read-only rendering derivative. Only protected inline delimiters were adapted for Pandoc; the exact inverse recovers all frozen bytes. Ordinary display syntax, prose, links, anchors and visible P labels were unchanged. The final Pandoc AST has **all 305 source math payloads byte-exact**, including boundary/internal newlines, and the complete prose/math stream is exact after whitespace folding. There were zero initial math boundary-normalization differences for this source. The final TeX conversion used that verified AST.

Final internal PDF SHA256: `7ff1f1b16a451d5a1f2b46897b0269bd6318a81b3e5c5c33226f81a0b2a5540d`. Nine complete final pages were rasterized, individually decoded, personally opened, and re-hash-verified. Page-specific observations and actual image hashes are in `preview-final/visual-inspection.json`.

| Page | Full extent inspected | Findings |
|---|---|---|
| 1 | P001–P008 | Title, tangent and error displays clear. |
| 2 | P009–P017 | A1, comparison signs, radicals and exponents clear; navigation wraps within paragraph. |
| 3 | P018–P025 formula | Product and limit displays complete; P025 explanation continues next page. |
| 4 | P025 continuation–P032 introduction | Proof and cosine displays readable; P032 equation follows on page 5. |
| 5 | P032 equation–P038 | A2, quadratic products and derivatives clear. |
| 6 | P039–P044 first display | Time ratio, units and scientific notation clear; equation follows “Consequently” on page 7. |
| 7 | P044 continuation–P052 | A3/A4 and their math complete; P052 label is at page bottom, P053 text follows next page. |
| 8 | P053–P063 | End-core boundary, all hints, end-hints boundary, solution heading, A1 and first A2 solution readable. |
| 9 | P064–P068 and ending | Remaining solutions, coefficients, accuracy values and final return links complete. |

No clipped or overlapping content, unreadable math, black squares or missing endings were observed. Listed page breaks are preview-only pagination artifacts; this derivative is not a polished learner PDF or evidence of GitHub pagination.

Both compiler passes exited 0. Stdout and full TeX logs were captured immediately for each pass and their hashes verified. Case-insensitive review found **18 missing PDF destination warnings per pass**, corresponding to raw Markdown HTML id anchors that do not become TeX destinations. The PDF links are therefore NOT accepted; the independent GitHub target check remains separate. No overfull/underfull boxes or undefined-control errors were found. A package metadata line mentioning warning/error is retained but is not a warning. The preview preserves all 68 visible P labels in order.

## Preserved failures and limits

The first preview attempt stopped before compilation when a complete prose-stream assertion failed: Pandoc smart punctuation converted straight apostrophes and the simple AST text extractor omitted quote delimiters represented as Quoted nodes. The exact mismatch evidence and initial files remain under `preview/`; no PDF was produced from that attempt. A separate final build disabled smart punctuation, preserved literal quotes/apostrophes, and passed the complete stream and all math checks. No frozen teaching was changed. The first finalization shortcut also failed because it assumed fresh CSS URL/hash identity; this failure is recorded, with the four actual changes resolved by full comparison rather than ignored.

No browser/CUA, live MathJax execution, computed styles, responsive pixel inspection, click/scroll landing, external source-content validation, learner-response assessment, SASIS, scientific-content acceptance, final global approval, repo edit or GitHub write occurred. This review only checks the teaching artifact’s representation and internal preview. All final PDF/PNG binaries are internal scratch artifacts; file paths/hashes are in the manifest. Parent owns final acceptance and publication.

`evidence-manifest.json` records every evidence file except itself, including failed attempts, current CSS, compiler output, final PDF and all nine actually viewed images.
