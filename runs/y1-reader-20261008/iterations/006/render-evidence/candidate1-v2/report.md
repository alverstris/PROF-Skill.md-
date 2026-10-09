# D006 candidate1 v2 immutable representation review

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
