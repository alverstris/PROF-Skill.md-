# D008 r15 original — failed destination representation

Status: FAIL for exact GitHub mathematical payload preservation. This is a diagnostic for the independent r15 original, not a final acceptance or SASIS review. No teaching was edited and no PDF was built for this failed destination.

## Immutable identity

Commit `2d144338ec647166e6fd2a6527fbc96b766e7d5e`; parent-supplied tree `de158c9084bb9ae17e3dc4f715ae788dd3bfb60e`. Path `runs/y1-reader-20261008/iterations/008/author-work-r15/teaching-original.md`. Fresh actual raw HTTP 200 bytes: 27,841 bytes, 27,792 UTF-8 characters, SHA256 `86b6338315866e711ddfcefd52e4a84b2bb99093c321ff6b7a8124c66c739718`. Actual immutable page HTTP 200 SHA256 `4eadf0e5abe96636ad7c645e4459f4bc7a86ecb38f0c8c2e497170d28af03c0f`. Fetch timestamps and URLs are in `fetch-records.json`.

Actual page layout/blob current OIDs and paths equal the requested freeze, richText is not truncated, and embedded rawLines recover exact raw source with its single terminal newline. The source was read completely. No content equivalence to earlier r14 teaching is assumed.

## Exact failures

The source has 305 expressions: 276 protected inline and 29 ordinary `$$` displays. All 305 wrappers and their type/order remain. 296 exact mathematical payloads pass, including all 29 displays. Nine inline payloads fail after **one ordinary HTML parse**. Literal article HTML contains `&amp;gt;` or `&amp;lt;`; the parsed wrapper therefore contains entity text, not the source comparison character. No second unescape was used to hide this difference.

| 1-based math index | Visible block | Source payload | Once-parsed actual payload |
|---|---|---|---|
| 33 | P010 | `x>0` | `x&gt;0` |
| 63 | P014 | `x>-1` | `x&gt;-1` |
| 66 | P015 | `1+x>0` | `1+x&gt;0` |
| 128 | P026 | `\eta>0` | `\eta&gt;0` |
| 162 | P033 | `1+x>0` | `1+x&gt;0` |
| 170 | P034 | `x>-1/2` | `x&gt;-1/2` |
| 197 | P040 | `T>0` | `T&gt;0` |
| 233 | P051 | `x<1` | `x&lt;1` |
| 257 | P062 | `x>0` | `x&gt;0` |

`literal-destination-defects.json` preserves every original wrapper, source span, label and parsed payload. `math-comparison.json` preserves exact sequence/alignment evidence. This is a confirmed serialization defect under the required payload-equality check; actual MathJax response or final glyph appearance was not observed.

## Whole document and navigation

Outside-math prose and all numeric tokens preserve order/content after prose whitespace folding. All source dollars/backticks are accounted for by the supported source math forms. All 68 **visible** P001–P068 labels occur once and in order. Independent per-block comparison identifies exactly the same nine failed blocks; the other 59 complete blocks match. All four entire task prompts were checked: A1/P011 and A3/P045 match fully; A2/P034 and A4/P051 contain only the corresponding reported math mismatch. Their wording and numeric tokens are retained.

All 37 intended labeled links match in order: 34 internal, three external. All 18 explicit source id targets appear once, in order, as GitHub `user-content-*` ids. All four mappings are exact: task a1/a2/a3/a4 to own h1/h2/h3/h4 and s1/s2/s3/s4; each hint and solution returns to its own task. Fifteen explicit paragraph navigation checks cover the group-entry links, tasks, end-of-core choices, every hint return, end-of-hints choices, solution returns, continuation anchors and final start link. The source does not include hint-to-solution or solution-to-hint links; their absence is recorded without inventing a requirement.

The core ends P054, hints heading P055, hint blocks P056–P059, end-hints P060, solutions heading P061 and solution blocks P062–P068. Separation/order and all linked destinations are preserved. This verifies representation and structure, not whether the explanations enable valid reasoning. Link landing offsets and actual clicks are unobserved. External URL serialization was checked, not present external source contents/availability.

## Fresh static styles

All 21 unique actual href CSS URLs from this page were fetched afresh (HTTP 200, 2,490,700 bytes total) and hash-verified. No old CSS was substituted. The inventory retains inactive data-href theme links separately. Complete article, ancestor attributes and inline styles are retained. All 590 font declaration rules were inventoried and the 38 conservatively selected font candidates were manually inspected against actual scope.

Body normal weight resolves statically to 400; `.markdown-body` declares sans-serif, 16px, line-height 1.5. Paragraphs use the normal block margin. No matching bold/italic override was found on actual prose or ancestors. Actual article tags are 141 p, 55 a (18 target anchors plus 37 links), and 305 math-renderer; no headings, tables, bold/italic markup or constituent images. Current link underline and math-wrapper layout declarations were inspected. `manual-style-review.json` records applicable scopes and limitations. Static declarations do not prove final computed cascade, MathJax pixels or responsive rendering.

## Tooling and limits

The source uses protected inline math plus ordinary `$$` displays; the parser supports these directly and retains exact display boundary newlines. Visible P labels and id anchors were deliberately handled, rather than inheriting the old invisible-label/name-anchor assumptions. Source math is protected before Markdown link extraction. The generic helper is used only for embedded JSON extraction; helper snapshots and hashes are retained. No audit runtime failure or CSS fetch failure occurred. The destination failures above are preserved unchanged.

No source-equivalence assumption, repair, repository/GitHub write, learner assessment, SASIS, scientific validity decision or global teaching acceptance is claimed. No browser/CUA, live client MathJax, screenshots, click/scroll, live computed styles or PDF preview was used. Because the destination already fails, the conditional full internal-preview stage was not entered: there are no compiler diagnostics or page-view claims for this original. A repaired/new freeze must receive its own fresh destination witness and whole-preview review.

All files under this owned evidence directory are listed with byte counts and SHA256 in `evidence-manifest.json` (manifest excludes itself).
