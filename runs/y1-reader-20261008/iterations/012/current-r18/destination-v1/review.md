# D012 v1 destination review

Result: FAIL. The immutable destination recognizes all 309 expressions (281 inline, 28 display), but 20 inline comparison payloads contain literal entity text instead of their comparison operators. The 23 affected operators are required for bounds, positivity, feasibility and interval comparisons. Operands/grouping remain present; that does not restore the lost relation tokens. No missing math spans were found. 288 payloads are byte exact; one additional display mismatch is ordinary whitespace only.

The raw HTML uses double escaping (`&amp;lt;`/`&amp;gt;`); one standards-based HTML parse yields literal `&lt;`/`&gt;` in the math node. An additional unescape would conceal the observed failure and was not used to claim preservation. Client MathJax execution was not observed.

| Math ordinal | Paragraph | Source payload | Actual parsed payload |
|---|---|---|---|
| 51 | P010 | `x_1=2>r` | `x_1=2&gt;r` |
| 53 | P010 | `0<e_k<x_k` | `0&lt;e_k&lt;x_k` |
| 54 | P010 | `0<e_{k+1}<e_k/2` | `0&lt;e_{k+1}&lt;e_k/2` |
| 91 | P016 | `a>0` | `a&gt;0` |
| 95 | P016 | `m,g>0` | `m,g&gt;0` |
| 104 | P017 | `L>\sqrt{a^2+b^2}` | `L&gt;\sqrt{a^2+b^2}` |
| 152 | P023 | `b-2y=D>0` | `b-2y=D&gt;0` |
| 154 | P023 | `L^2>a^2+b^2` | `L^2&gt;a^2+b^2` |
| 155 | P023 | `D>|b|` | `D&gt;|b|` |
| 156 | P023 | `0<x<a` | `0&lt;x&lt;a` |
| 157 | P023 | `y<0` | `y&lt;0` |
| 158 | P023 | `y<b` | `y&lt;b` |
| 161 | P024 | `D\pm b>0` | `D\pm b&gt;0` |
| 176 | P026 | `\sqrt{73}\ \mathrm m<10\ \mathrm m` | `\sqrt{73}\ \mathrm m&lt;10\ \mathrm m` |
| 189 | P027 | `L<AB` | `L&lt;AB` |
| 193 | P027 | `L>AB` | `L&gt;AB` |
| 218 | P030 | `AB<L` | `AB&lt;L` |
| 272 | P043 | `10>\sqrt{40}` | `10&gt;\sqrt{40}` |
| 287 | P043 | `L=6\ \mathrm m<AB` | `L=6\ \mathrm m&lt;AB` |
| 299 | P044 | `L>AB=8\ \mathrm m` | `L&gt;AB=8\ \mathrm m` |

P024 display #159 removes the one ordinary leading space before `a-x=...` following `\qquad` and a newline. This fails strict payload byte equality but preserves mathematical operands, operators, grouping and explicit spacing: ordinary whitespace is ignored by TeX math. The complete exact source/destination and raw node evidence is in `complete-math-failure-map.json`.

All nonmath prose matches after whitespace folding with the 309 ordered math nodes replaced by identical position markers. Whole prose-plus-math equality correctly fails on the comparison changes. The 46 paragraph starts P001–P046 match exactly; 47 raw label-like matches include an internal P025 reference in P019.

Fresh immutable raw teaching bytes match the frozen/local document SHA256 `8a9845299b276ba13c3f2c18862bdde3ed9b0227451e89fb57f9fe2719e573f0`. Embedded identity is correct and untruncated (its rawLines representation omits the terminal newline). All five packet constituents match the manifest. The actual image URLs retain the immutable revision, all four freshly fetched PNGs match exactly, and every complete PNG was opened: Newton positive/negative iteration, two-cycle, lowest-ring geometry and arbitrary-point reflection agree with their prose and have no material visible defects.

All 17 named anchors, 28 ordered internal references and Q1–Q4 task/hint/solution/return mappings pass structural checks. Hints precede the complete solutions in a separate group. Browser navigation clicks and actual scroll locations were not tested. The actual official MIT source URL in P045 is exact; fresh official, immutable repository and local lecture PDFs are byte identical (7 pages; SHA256 `bf5673e95549bb93b6383c6be924baf315d4e0761d4f7e653744b1b87c8c8f65`).

All 21 referenced CSS assets were fetched. Applicable body default is weight400; article uses no strong/emphasis/headings/table/definition-term tags that trigger fetched bold/italic rules. Element/style/CSS records are preserved. This is data-level inspection, not live computed styles.

Root explicitly held the internal preview after this established parser failure. No PDF was built, no PDF digest exists, and no final-page/native-PDF-navigation/AST-equivalence pass is claimed. This failed original remains unchanged; a corrected revision requires a fresh complete destination audit and full preview.

Evidence: `final-audit.json`, `complete-math-failure-map.json`, original `github-page.html` and `github-article.html`, `source-math.json`, `destination-math.json`, `math-comparison.json`, `prose-comparison.json`, both placeholder prose streams, `navigation.json`, `asset-fetch.json`, `raw-source-fetch.json`, `source-PDF-link-check.json`, `css-font-rules.json`, `element-style-evidence.json`, and `visual-inspection.json`. No original audit result was rewritten. Live GitHub pixels, computed styles, client math rendering and browser clicks remain unobserved.
