# D013 v1 actual destination review

FAIL: all214 expressions are recognized (190 inline,24 display), but48 inline payloads contain58 literal `&lt;`/`&gt;` strings in place of comparison operators. All24 display expressions and the other142 inline expressions are byte exact. There are no missing math spans or other payload differences. Original raw HTML uses double escaping; one HTML parse yields the literal entity strings recorded below. No second unescape was used as acceptance. Operands/grouping remain intact, but required order relations do not. This affects endpoint order, theorem locations, derivative signs, monotonicity and inequality chains in the core and help.

| Math ordinal | Anchor section | Source line | Source payload | Actual parsed payload |
|---|---|---|---|---|
| 1 | a | 15 | `a<b` | `a&lt;b` |
| 26 | b | 53 | `h>0` | `h&gt;0` |
| 27 | b | 53 | `h<0` | `h&lt;0` |
| 44 | c | 77 | `0<c<3` | `0&lt;c&lt;3` |
| 50 | c | 89 | `x>a` | `x&gt;a` |
| 52 | c | 93 | `x<a` | `x&lt;a` |
| 54 | c | 93 | `x<c<a` | `x&lt;c&lt;a` |
| 70 | d | 117 | `a<b` | `a&lt;b` |
| 71 | d | 117 | `f(a)<f(b)` | `f(a)&lt;f(b)` |
| 72 | d | 117 | `f(a)>f(b)` | `f(a)&gt;f(b)` |
| 75 | d | 121 | `a<b` | `a&lt;b` |
| 77 | d | 125 | `f'>0` | `f'&gt;0` |
| 78 | d | 125 | `f(b)>f(a)` | `f(b)&gt;f(a)` |
| 79 | d | 125 | `f'<0` | `f'&lt;0` |
| 81 | d | 125 | `f(b)<f(a)` | `f(b)&lt;f(a)` |
| 85 | d | 127 | `v'(x)=3x^2+2>0` | `v'(x)=3x^2+2&gt;0` |
| 92 | d | 129 | `a<b` | `a&lt;b` |
| 95 | d | 133 | `a<b` | `a&lt;b` |
| 96 | e | 151 | `e^x>0` | `e^x&gt;0` |
| 101 | e | 153 | `R_0'(x)=e^x>0` | `R_0'(x)=e^x&gt;0` |
| 103 | e | 153 | `x>0` | `x&gt;0` |
| 109 | e | 161 | `R_1(x)>0` | `R_1(x)&gt;0` |
| 114 | e | 171 | `R_1(x)>0` | `R_1(x)&gt;0` |
| 115 | e | 171 | `x>0` | `x&gt;0` |
| 116 | e | 171 | `R_2(x)>0` | `R_2(x)&gt;0` |
| 124 | e | 177 | `e>1+1+1/2+1/6=8/3` | `e&gt;1+1+1/2+1/6=8/3` |
| 139 | e | 183 | `e^x>P_n(x)` | `e^x&gt;P_n(x)` |
| 143 | f | 203 | `L<f'(t)<U` | `L&lt;f'(t)&lt;U` |
| 144 | f | 203 | `a<t<b` | `a&lt;t&lt;b` |
| 146 | f | 203 | `b-a>0` | `b-a&gt;0` |
| 151 | f | 209 | `1<c<4` | `1&lt;c&lt;4` |
| 152 | f | 209 | `1<\sqrt c<2` | `1&lt;\sqrt c&lt;2` |
| 153 | f | 209 | `1/4<f'(c)<1/2` | `1/4&lt;f'(c)&lt;1/2` |
| 164 | h5 | 258 | `R_1'(x)<0` | `R_1'(x)&lt;0` |
| 169 | h6 | 263 | `1<c<1+h` | `1&lt;c&lt;1+h` |
| 175 | s1 | 273 | `\sqrt3>1` | `\sqrt3&gt;1` |
| 185 | s4 | 288 | `0<a<b` | `0&lt;a&lt;b` |
| 189 | s4 | 288 | `u'(c)=-1/c<0` | `u'(c)=-1/c&lt;0` |
| 190 | s4 | 288 | `b-a>0` | `b-a&gt;0` |
| 191 | s5 | 295 | `e^x<e^0=1` | `e^x&lt;e^0=1` |
| 192 | s5 | 295 | `R_1'(x)=e^x-1<0` | `R_1'(x)=e^x-1&lt;0` |
| 195 | s5 | 299 | `R_1(x)>0` | `R_1(x)&gt;0` |
| 196 | s5 | 299 | `e^x>1+x` | `e^x&gt;1+x` |
| 197 | s5 | 301 | `R_2'(x)=R_1(x)>0` | `R_2'(x)=R_1(x)&gt;0` |
| 198 | s5 | 301 | `R_2(0)-R_2(x)>0` | `R_2(0)-R_2(x)&gt;0` |
| 200 | s5 | 301 | `R_2(x)<0` | `R_2(x)&lt;0` |
| 202 | s6 | 310 | `a<b` | `a&lt;b` |
| 208 | s6 | 316 | `1/(1+h)<1/c<1` | `1/(1+h)&lt;1/c&lt;1` |

The complete per-instance record, including raw HTML, source spans and actual element indexes, is `complete-math-failure-map.json`. `math-comparison.json` retains the original aligned differences. The whole prose/math stream fails only at those58 comparison substitutions; with all ordered math nodes replaced by identical position markers, all nonmath prose matches after whitespace folding. Plain mathematical wording in tasks and Unicode symbols outside math markup are included in that complete prose check.

All28 standalone route/section/task/help/source labels match as full paragraphs, including A–F and six each of Task/Hint/Solution P1–P6. This document has no P001 paragraph labels; the inherited generic extraction in prose-comparison.json returns empty lists and is not an acceptance claim. `paragraph-label-check.json` supplies the correct actual-document label audit. All27 named anchors and37 ordered internal links are preserved with unique targets. Every P1–P6 task/hint/solution/return mapping and solution-to-hint link is correct; hints form a separate group before solutions. Browser clicks remain unobserved.

Frozen identity: commit `7671c6708cfee4805c08837c955ebd164495420c`; learner Markdown SHA256 `4af6ed4369de2cc322f2d1022fdc05071a5355d05f4cf8df52d3fc343baf7364`,31506 bytes. Fresh raw bytes equal local/manifest source. Embedded commit/path/untruncated source are correct; GitHub rawLines omits only its terminal newline. All7 constituents (Markdown,3PNGs,3SVGs) were freshly fetched at that commit and match their manifest/local hashes and sizes.

All3 complete PNGs were opened. All3 fresh immutable SVG companions were parsed and independently rendered as full frames by Inkscape at150dpi; every complete rendered frame was opened. SVGs contain no external href dependencies. Plots, slopes, contact locations, parallel-line shift arrows and the tangent-error segment agree with their captions and worked examples. No material visual asset defect found. Inkscape exits0 for all3, with preserved GtkRecentManager initialization warnings that did not affect the inspected frames. SVG companions are not directly linked in the learner Markdown; their identity and renders were still audited.

All21 referenced CSS assets were fetched. Actual body defaults to weight400; this article has no strong/emphasis/headings/table-header/definition-term prose nodes matching the fetched forced-emphasis rules. Inline styles are limited to math display mode and image width. This is actual CSS/parser evidence, not live computed-style or pixel observation.

The two MIT source links exactly preserve the official URL. Fresh official, immutable-repository and local lecture PDF bytes match SHA256 `67d74be87119ab367516c8a80cc710664e48059bc1184c7042846556b3c0a609`,five pages. All4 external hrefs remain in source order; the two OpenStax targets are exact, but their page contents/live navigation were not reaudited here.

Root explicitly held the internal PDF preview after the actual parser defect. No PDF build, AST conversion, PDF digest, final-page or native-PDF navigation pass is claimed for v1. A repaired immutable packet needs fresh complete checks and full preview. No original audit evidence was rewritten; no learner/source/skill file was changed.

Evidence: `final-audit.json`, `review.md`, raw HTML/article/source, complete math/prose/label/navigation records, `asset-fetch.json`, `raw-source-SVG-fetch.json`, `SVG-companion-check.json`, `svg-render.json`, `visual-inspection.json`, actual images/full-frame renders, CSS files/rule evidence and source-PDF identity records. Live GitHub pixels, client MathJax, computed styles, responsive behavior and clicks remain unobserved. These limits do not erase the established parser preservation failure.
