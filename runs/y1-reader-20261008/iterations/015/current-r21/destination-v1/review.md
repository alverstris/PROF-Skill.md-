# D015 v1 actual destination review

FAIL: MATH-1, an actual parser-preservation defect affects 20 inline expressions across all three learner files. There are 398 recognized math nodes in the correct order and with the correct types: 373 inline and 25 fenced displays. Exactly 378 payloads match, including all 25 displays. In the other 20 payloads, 21 source comparison symbols become literal `&lt;` or `&gt;` strings after one ordinary HTML parse. Original raw HTML contains `&amp;lt;`/`&amp;gt;`. No second entity decoding was applied to declare preservation.

This is a comparison-operator preservation failure, not whitespace normalization. Operands and surrounding grouping remain, but the actual parsed math payload no longer contains the intended comparison token. The affected conditions control positive exponentials, derivative-sign descriptions, interval/domain choices, ellipse existence, branch endpoints and solution restrictions. In the chained ellipse interval, both less-than operators are affected. No missing math nodes or other payload differences were found. Client MathJax/pixels were not observed, so this report does not invent the resulting live visual appearance.

| Source file | Math ordinal within file | Source line:column of comparison | Intended payload | Actual singly parsed payload |
|---|---|---|---|---|
| teaching.md | 52 | 59:260 | `e^c>0` | `e^c&gt;0` |
| teaching.md | 75 | 74:196 | `x<0` | `x&lt;0` |
| teaching.md | 76 | 74:221 | `x>0` | `x&gt;0` |
| teaching.md | 172 | 168:214 | `x>0` | `x&gt;0` |
| teaching.md | 173 | 168:226 | `x<0` | `x&lt;0` |
| teaching.md | 176 | 171:184 | `x>0` | `x&gt;0` |
| teaching.md | 195 | 195:8 | `c>0` | `c&gt;0` |
| teaching.md | 207 | 201:519 | `c<0` | `c&lt;0` |
| teaching.md | 213 | 214:8 | `c>0` | `c&gt;0` |
| teaching.md | 215 | 214:162, 214:164 | `-2\sqrt c<x<2\sqrt c` | `-2\sqrt c&lt;x&lt;2\sqrt c` |
| teaching.md | 250 | 244:80 | `x<0` | `x&lt;0` |
| hints.md | 28 | 36:179 | `x<0` | `x&lt;0` |
| solutions.md | 24 | 21:90 | `g(y)>0` | `g(y)&gt;0` |
| solutions.md | 34 | 34:63 | `x^2<\pi` | `x^2&lt;\pi` |
| solutions.md | 42 | 36:217 | `1+b^2>0` | `1+b^2&gt;0` |
| solutions.md | 46 | 43:108 | `x>0` | `x&gt;0` |
| solutions.md | 54 | 51:232 | `x>0` | `x&gt;0` |
| solutions.md | 60 | 55:232 | `x>0` | `x&gt;0` |
| solutions.md | 99 | 93:237 | `x<0` | `x&lt;0` |
| solutions.md | 104 | 93:417 | `x<0` | `x&lt;0` |

Exact original full raw HTML, source spans, payloads and element locations are in complete-math-failure-map.json and each document's math records. all21-comparison-character-positions.json records one-based line/column, zero-based character and UTF8-byte offsets for every affected symbol. Nearest preceding printed labels in the original failure map are location aids, not replacements for these exact source lines.

Frozen packet: immutable commit `6066e554fa4874a2a057da772236050482135f68`. All nine constituents were freshly fetched and agree with the frozen manifest and local bytes: teaching.md, hints.md, solutions.md, three linked SVGs and their three PNG companions. Full asset URLs, sizes and SHA256 values are in asset-manifest.json. Each actual GitHub page's embedded immutable commit/path and untruncated source identity match; rawLines omits only the source's terminal newline. Original response pages and actual articles are retained.

The full nonmath prose of all three documents matches after ordinary whitespace folding and ordered math-node masking. Whole prose-plus-math equality correctly fails on the 21 entity expansions only. All 25 paragraph-start labels match: seven section labels, three figure labels, five task labels, five hint labels and five solution labels. Cross-references inside paragraphs are not counted. All six closing exam-list items and their order are preserved as one ordered list starting at one.

Navigation passes its positive server-markup/contract checks. There are 21 unique authored named targets and 31 cross-file references. Every source href is rewritten to the intended exact immutable teaching/hints/solutions blob path and fragment. All five Q→H, Q→A, H→Q, A→Q and A→H chains have the correct unique target. Hints also provide a global solutions-file link, satisfying the allowed hints-to-solutions route. Hints and complete solutions are separate actual files, each fetched and audited; entry-file return links are retained.

Actual target names carry GitHub's `user-content-` prefix while cross-file fragments retain their authored names. The check explicitly compares that prefix mapping, not raw literal href/name equality. Root's current official GitHub Docs relative-links/custom-anchors evidence was read and preserved in root-navigation-contract-copy.md. It supplies the supported syntax contract, not an observed click, client implementation or scroll landing. No PDF preview is used to establish browser navigation.

All three fresh remote PNGs and all three independently rendered fresh SVG full frames were actually opened. Figure 1 has the expected symmetric Gaussian peak and tails; figure 2 distinguishes the parabola, ray and tangent at (1,1); figure 3 preserves the four parabolas, two horizontal ellipses, equal coordinate scales and √2 semiaxis ratio. Their geometry, labels and captions agree. Figure styles are readable and upright. All SVG local glyph references remain internal; no external rendering dependencies were found. All Inkscape exports succeeded; original GtkRecentManager initialization warnings are retained. Raw asset identity and local full-frame views do not establish live GitHub embedded-image pixels.

All 21 referenced external CSS assets were freshly fetched. The body default is normal weight400. Actual learner articles have no heading, bold/italic emphasis, table-header or definition-term prose nodes; the corresponding fetched semibold/italic rules do not apply. Inline styles only set mathematical display modes and image width. The outer GitHub page has a stylesheet entry without href; there is no external URL to fetch for it. That entry exposed an initial adapter KeyError before content parsing. Original script/stdout and a precise failure record remain; audit2.py records the missing URL and correctly parses all documents. No live computed-style pass is claimed.

The primary lecture and supplemental source identities were freshly checked. Official, immutable and local Lecture16 bytes agree: 645,960 bytes, five pages, SHA256 `cdf0e899a0f0dd5a57ca1069a5c039c08b9efb84ef6d416f3dce038939564d23`. Official, immutable and local MIT22.51 chapter9 bytes also agree: 294,693 bytes, 15 pages, SHA256 `9373189eb619b5e524194cf8616ed1f959016fdf3b41c5bbcfcb976f50ce1e30`. First-page course/title text was inspected and retained. Both actual learner source hrefs match. A full visual/technical source-PDF review is outside this destination role and is not claimed.

Root explicitly held the original v1 internal PDF cycle because actual parser preservation fails. Thus internal PDF compilation, faithful final AST, page inspection, native PDF links and hint/solution page separation are unverified/not performed for v1. A corrected immutable packet requires a fresh complete actual destination audit and full source-faithful preview; a separate successful renderer cannot erase this original destination mismatch.

The audit continued through the complete teaching, all hints, all solutions, all assets, navigation, styling and source identities. No additional supported material issue was found. Primary evidence is final-audit.json, complete-math-failure-map.json, all21-comparison-character-positions.json, positive-navigation-audit.json, full-prose-check.json, paragraph-label-check.json, exam-list-check.json, asset-manifest.json, asset-visual-inspection.json, source-PDF-identity.json and all original response/CSS/render records. Nothing in the frozen learner/source/skill packet or prior D014 evidence was changed; nothing was published.

Limits: live GitHub pixels, client MathJax, computed styles, responsive behavior, browser fragment processing/clicks/scroll positions and PDF rendering remain unobserved as specified above. This report is original failure evidence for root's consolidated repair decision, not acceptance of v1.
