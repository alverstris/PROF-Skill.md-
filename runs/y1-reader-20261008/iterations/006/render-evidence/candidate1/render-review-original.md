# D006 regenerated candidate1 original representation review

Current verdict: FAIL for actual GitHub math-payload fidelity. There are 36 changed payloads: 34 inline and two display. The visible non-math prose, all A1-A6 navigation routes/returns, grouping and inspected destination prose typography pass their separate checks. All 12 full pages of the unchanged source-faithful secondary preview were opened. This is not global teaching acceptance or a SASIS verdict.

## Frozen inputs and scope

Teaching commit: `4bf1c6df54d26f3b44806a0f1955f17fb33a3e7f`, path `runs/y1-reader-20261008/iterations/006/regenerated-r13-candidate1/teaching.md`. The immutable raw GitHub object was fetched directly into `frozen-teaching.md`, not read from a changing worktree. It is 28,540 bytes with SHA-256 `7030eca0fddab9a27c720a9ac4f7c3ae2d7e2e9716fc5d798cbaea5769c54986`. The helper's independent raw fetch also reports exact equality. Final source identity is unchanged.

Candidate T11 was read from the actual `SKILL.md` git object at `a2389390c0709d65af4a3cf070a04e396e4a4792`, preserved as `candidate-controls-SKILL.md`, SHA-256 `3f7d903a399bdbaaeef397e7af7033dc0229cbb982371ea7c0679fe042c9cc8f`. It forbids bold/italic prose, requires destination-style checks for implicit emphasis, and requires correctly matched, separately grouped help for these non-PDF notes.

All evidence is under this candidate1 review directory. No teaching, controls, repository helper or run-state edits were made; no subagents, browser or CUA were used. There are no external figure constituents. The internal PDF is QA evidence, not a learner PDF deliverable.

## Method and helper limitation

The unchanged existing helper was first run against the actual immutable rendered GitHub page. Its original failed capture and audit remain under `capture-initial/`. That helper recognizes protected-backtick inline math and fenced display math; this candidate instead uses ordinary dollar inline math and double-dollar display math. Its zero source-math counts cannot serve as this source's actual inventory. It also does not handle the invisible comment locators or unordered-list markers in its complete-prose comparison. Its generic numeric Q/H/S checks do not test these A1-A6 routes.

The separate `independent_audit.py` extracts ordinary dollar math and performs one ordinary HTML parse of the actual captured article. It compares all renderer payloads in document order with type, locator, source line and exact characters. For double-dollar source, newlines inside the source delimiters are part of the compared payload and are retained on both sides; they are not falsely classified as differences. No extra HTML unescape is applied.

P001-P194 are invisible `<!-- Pnnn -->` comments. Their source sequence is exact, but they are not required to be visible in GitHub or the PDF. All location references below use these diagnostic comments. The independent text comparison removes only those comments, source anchor tags, Markdown link destinations and the two unordered-list markers, then normalizes whitespace. Masking math on both sides proves all other visible prose matches exactly. Full text remains unequal because of the actual math changes below.

## Actual math-payload failures

The source and actual article each contain 291 inline and 46 display mathematical payloads. Of these, 257 inline and 44 display payloads match exactly. There are two failure classes:

1. In 32 inline payloads, 35 literal angle comparison characters are delivered as entity text after the ordinary HTML parse. The saved renderer HTML has `&amp;lt;`/`&amp;gt;`; its parsed text therefore retains `&lt;`/`&gt;`. An extra unescape would conceal the mismatch and was not used.
2. In four payloads (two inline and two display), nine source percent-escape backslashes are removed. The source uses the standard TeX `\%` convention correctly. The destination payload changes that to `%`. This is an actual changed TeX payload, not a mistake in the source convention. Its live MathJax outcome was not observed, and it is not normalized away.

Every changed inline payload is listed here. Ordinals are 1-based among inline math.

| Locator | Source line | Inline ordinal | Source payload | Ordinary-parsed GitHub payload |
|---|---:|---:|---|---|
| P007 | 22 | 3 | `a>1` | `a&gt;1` |
| P022 | 80 | 34 | `M(2)<1` | `M(2)&lt;1` |
| P022 | 81 | 39 | `M(4)>1` | `M(4)&gt;1` |
| P037 | 138 | 60 | `\ln x<0` | `\ln x&lt;0` |
| P037 | 138 | 61 | `0<x<1` | `0&lt;x&lt;1` |
| P037 | 138 | 62 | `\ln x>0` | `\ln x&gt;0` |
| P037 | 138 | 63 | `x>1` | `x&gt;1` |
| P040 | 149 | 69 | `u>0` | `u&gt;0` |
| P043 | 160 | 75 | `e^{w(x)}=x>0` | `e^{w(x)}=x&gt;0` |
| P049 | 182 | 84 | `a>0` | `a&gt;0` |
| P053 | 198 | 91 | `a>0` | `a&gt;0` |
| P053 | 198 | 94 | `2<e<4` | `2&lt;e&lt;4` |
| P054 | 201 | 97 | `a>1` | `a&gt;1` |
| P054 | 201 | 98 | `0<a<1` | `0&lt;a&lt;1` |
| P054 | 201 | 99 | `\ln a<0` | `\ln a&lt;0` |
| P059 | 220 | 104 | `f(x)>0` | `f(x)&gt;0` |
| P067 | 251 | 113 | `x>0` | `x&gt;0` |
| P075 | 281 | 122 | `u(x)>0` | `u(x)&gt;0` |
| P079 | 298 | 129 | `x>-1` | `x&gt;-1` |
| P099 | 375 | 159 | `k>2` | `k&gt;2` |
| P110 | 416 | 176 | `F(t)>0` | `F(t)&gt;0` |
| P119 | 450 | 199 | `x>0` | `x&gt;0` |
| P127 | 480 | 208 | `5-2x>0` | `5-2x&gt;0` |
| P151 | 570 | 235 | `\ln(1/2)<0` | `\ln(1/2)&lt;0` |
| P151 | 570 | 236 | `f'<0` | `f'&lt;0` |
| P152 | 573 | 238 | `5-2x>0` | `5-2x&gt;0` |
| P152 | 573 | 239 | `x<5/2` | `x&lt;5/2` |
| P157 | 592 | 242 | `x>-1` | `x&gt;-1` |
| P166 | 627 | 248 | `k>2` | `k&gt;2` |
| P166 | 627 | 249 | `1-2/k>0` | `1-2/k&gt;0` |
| P177 | 670 | 260 | `-2\%` | `-2%` |
| P183 | 693 | 263 | `-2\%` | `-2%` |
| P187 | 707 | 278 | `x>0` | `x&gt;0` |
| P190 | 719 | 281 | `\ln c_k>k/2` | `\ln c_k&gt;k/2` |

The two changed displays are:

P179, source line 676, display 44: source payload (the source delimiter-interior leading/trailing newlines are retained in the JSON comparison):

```tex
\frac{-50}{300}\times100\%=-\frac{50}{3}\%\approx-16.67\%,\qquad
\frac{-50}{10000}\times100\%=-0.5\%.
```

Actual ordinary-parsed payload:

```tex
\frac{-50}{300}\times100%=-\frac{50}{3}%\approx-16.67%,\qquad
\frac{-50}{10000}\times100%=-0.5%.
```

P182, source line 688, display 45: source payload (the source delimiter-interior leading/trailing newlines are retained in the JSON comparison):

```tex
100(e^{-0.02}-1)\%\approx-1.9801\%.
```

Actual ordinary-parsed payload:

```tex
100(e^{-0.02}-1)%\approx-1.9801%.
```


`independent-audit.json` preserves the full source/actual payloads, raw renderer HTML and all 337 comparisons. These changes are already in the saved GitHub article after ordinary parsing. They are not caused by the existing helper's unsupported-source-syntax inventory. Display angle signs otherwise remain exact. All non-math visible prose is exact, so there is no independent prose loss concealed by this diagnosis.

## A1-A6 routing, returns and grouping

All 25 source anchor IDs match unique GitHub `user-content-` IDs in source order. All 34 link text/href pairs match exactly: 33 internal and one external source link. Every internal target exists once. Each task has one route to its corresponding hint and solution; each hint has one return to its task; each solution has one return to its task and one route to its matching hint. All 30 of these task/help-specific routes pass. The reading-route links to Hints, Solutions and A6 also match.

| Task | Task start locator | Hint start locator | Solution start locator | Routes and returns |
|---|---|---|---|---|
| A1 | P029 | P123 | P143 | PASS |
| A2 | P055 | P126 | P148 | PASS |
| A3 | P078 | P129 | P156 | PASS |
| A4 | P098 | P132 | P165 | PASS |
| A5 | P114 | P135 | P174 | PASS |
| A6 | P117 | P138 | P185 | PASS |

The complete source and actual article place all six hints before the distinct complete-solutions group and all six solutions. No hint is interleaved with its complete answer. These are markup destination checks, not live clicking or JavaScript fragment behavior. Exact outgoing-link and return locators are in the navigation records.

## Candidate T11 destination typography

The actual prose structures are plain paragraphs and one two-item unordered list. Titles, part labels, task labels, hint/solution labels and source labels are paragraphs. There are no heading elements, tables/table headers, definition lists/terms, strong/bold elements, or emphasis/italic elements. Conventional mathematical notation is kept separate from prose typography.

All 21 active stylesheet URLs linked by this candidate's actual captured GitHub page were freshly fetched successfully; raw bytes, HTTP provenance and SHA-256 hashes are saved under `css-evidence/`. No prior CSS snapshot was substituted. The actual linked Primer stylesheet still contains the forced-emphasis rules for `.markdown-body h1` through `h6`, `.markdown-body dl dt`, `.markdown-body table th`, and `.markdown-body .csv-data th`. None of these target structures exists in this candidate. The present plain paragraph/list rules do not assign that forced weight or italic style. The previous P17 table-header conflict is absent here.

The typography inspection therefore passes for the actual structures and linked Markdown CSS inspected, independently of the math-payload failure. The source-faithful preview also shows normal upright prose titles and labels. Neither fact is represented as a live computed-style or pixel observation; those layers remain unobserved. `typography-audit.json` records selectors, exact declarations, source URLs, asset hashes and limits.

## Complete internal preview

The PDF skill was read in full and its creation marker succeeded exactly once for this candidate preview. The original source bytes were copied unchanged to `preview-initial/preview.md`; comments remain invisible through normal rendering. Pandoc AST extraction verifies every one of the 291 inline and 46 display payloads and their types in document order exactly. The existing helper's unsupported-source math checker was not modified or bypassed by changing its expected results; a separate explicit AST comparison was used.

Two pdflatex passes completed with no logged overfull/underfull, warning, missing-glyph or undefined-command diagnostics. The PDF has 12 US Letter pages, 11-point type and 25 mm margins. Its SHA-256 is `ceef50b2261ad7dde0bee4842f3cc3bc0f3c6f45bd17609a0d849f64b08e7f69` and remained unchanged throughout review.

Every complete 1020 x 1320 page image was opened at 120 dpi; no crop or contact-sheet thumbnail substituted for a full page.

| Page | Actual full-page finding |
|---:|---|
| 1 | Complete page viewed. Title, course line, reading route and Part 1 label use ordinary upright prose. Power laws, difference quotient, M(a) definition and exponential derivative fit within margins. Invisible Pnnn comments are not printed. |
| 2 | Complete page viewed. The two-item secant list replaces the prior table and is ordinary prose with mathematical notation. Exponential/chain-rule displays and Task A1/help labels are legible. Part 2 label is alone at the bottom, with its body beginning page 3. |
| 3 | Complete page viewed. Logarithm inverse pairs, domain inequalities, product law and inverse/chain-rule displays are readable. Lower-page base-change display and footer do not collide. No missing mathematical glyphs observed. |
| 4 | Complete page viewed. Base derivative, comparison inequalities, Task A2/help, Part 3 and logarithmic differentiation displays are clear. Title/part/task prose remains normal weight. |
| 5 | Complete page viewed. x^x and varying-base/exponent calculations, domain condition, Task A3/help and opening sequence definition are readable. Fractions, superscripts and parentheses are distinct. |
| 6 | Complete page viewed. Logarithmic sequence transformations, evaluation bar, exponential continuity step and limiting value are legible. Task A4 ends near bottom; its help links appear at the start of page 7. |
| 7 | Complete page viewed. Task A4 help labels, Part 5, relative/log-rate displays, units and percentages in the example are readable. Task A5 prompt continues page 8. |
| 8 | Complete page viewed. Task A5 continuation/help, later-return Task A6/help and the Hints group are readable. Hints A1-A4 and returns are visible; Hint A5 label is at the bottom and its body begins page 9. |
| 9 | Complete page viewed. Hints A5/A6 and returns precede the distinct Complete solutions group. Solutions A1/A2 and returns are legible. Solution A3 label is at the bottom and its body begins page 10. Hints and solutions share this internal-preview page; source grouping is preserved. |
| 10 | Complete page viewed. Solutions A3/A4 and returns show readable logarithmic derivatives, domain conditions and signed limit. Solution A5 begins with its derivative display near the bottom. No clipping or overlap observed. |
| 11 | Complete recovered page viewed. Source-faithful percentage signs are visibly retained in the two inline -2% expressions and both percentage displays (the locations whose GitHub payloads lose escapes). Solution A6 limit calculation, return/help labels and source/scope opening are readable. No missing percent glyph or clipping observed. |
| 12 | Complete page viewed. Source/scope continuation and correction summary are readable, with normal trailing document whitespace. No printed Pnnn locators, clipping or missing prose observed. |

The initial page-11 PNG was truncated, confirmed by full image loading. It remains preserved. Page 11 was re-rendered separately from the unchanged PDF as `preview-recovery/page-11.png`, fully loaded and opened. All other original page images loaded and were viewed. This recovered export defect is not a source/PDF-content change.

The source-faithful preview visibly retains the percent glyphs at P177, P179, P182 and P183. That corroborates the validity of the original TeX percent spelling in this renderer; it does not repair or certify the changed GitHub payloads.

Minor preview pagination issues are recorded rather than hidden: orphaned Part 2, Hint A5 and Solution A3 labels; Task A4 help separated from its prompt; a Task A5 continuation; and source/scope continuation. No clipping, overlap or missing glyph was observed. Hints and solutions share page 9 in separate ordered groups. This is an internal secondary preview of non-PDF Markdown notes, not a static learner PDF presented as meeting T11's different-page help rule.

## Remaining limits and evidence

Live GitHub pixels, computed CSS cascade, custom-element/MathJax execution, responsive layout and clicking were not observed. Server payload equality, source-comment locators and href/ID mappings are precisely distinguished from those unobserved layers. The faithful local preview cannot overturn the actual serialization FAIL. No global teaching acceptance is made.

The original helper capture/failure, independent audit and all raw payloads, candidate controls, fresh CSS responses, AST comparisons, untouched preview PDF, initial and recovered raster evidence, final per-page inspection record and key hashes are preserved under this directory. `preview-check.json` gives the current combined scope; `artifact-hashes.json` gives exact key evidence hashes.
