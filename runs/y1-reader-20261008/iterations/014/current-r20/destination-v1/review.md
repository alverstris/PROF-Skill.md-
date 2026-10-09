# D014 v1 actual destination audit

FAIL. Two material findings are established in the actual immutable GitHub output: MATH-1,12 display expressions lose13 TeX command backslashes; and NAV-1,all seven task/help triples lack native targets and links. The full audit continued through core, all hints and all solutions.

MATH-1 (T11/destination preservation): all346 expressions are recognized in order (310inline,36display). Every310 inline payload and24 display payloads match exactly. The remaining12 displays turn each affected `\,` thin-space command into a literal comma. This is not ordinary whitespace normalization: mathematical punctuation is inserted before dx/du, including between the coefficient and dx in the defining L1 equality. Operand strings and grouping survive, but the intended notation is altered. No missing math nodes or other payload mismatches were found.

| Ordinal | Label | Source line:column of lost backslash | Source payload | Actual parsed payload |
|---|---|---|---|---|
| 12 | L1 | 24:21 | `\ndx=h,\qquad dy=f'(a)\,dx.\n` | `\ndx=h,\qquad dy=f'(a),dx.\n` |
| 76 | L4 | 84:10 | `\n\int f(x)\,dx=F(x)+C\n` | `\n\int f(x),dx=F(x)+C\n` |
| 85 | L4 | 90:11 | `\n\int\sin x\,dx=-\cos x+C.\n` | `\n\int\sin x,dx=-\cos x+C.\n` |
| 88 | L4 | 98:9 | `\n\int x^n\,dx=\frac{x^{n+1}}{n+1}+C\quad(n\ne-1),\n` | `\n\int x^n,dx=\frac{x^{n+1}}{n+1}+C\quad(n\ne-1),\n` |
| 89 | L4 | 103:12 | `\n\int\frac{dx}{x}=\ln|x|+C,\qquad\n\int\sec^2x\,dx=\tan x+C,\n` | `\n\int\frac{dx}{x}=\ln|x|+C,\qquad\n\int\sec^2x,dx=\tan x+C,\n` |
| 142 | L6 | 166:18 | `\n\frac d{dx}A(g(x))=q(g(x))g'(x),\qquad\n\int q(g(x))g'(x)\,dx=A(g(x))+C.\n` | `\n\frac d{dx}A(g(x))=q(g(x))g'(x),\qquad\n\int q(g(x))g'(x),dx=A(g(x))+C.\n` |
| 145 | L6 | 174:18 | `\n\int x^3(x^4+2)^5\,dx,\n` | `\n\int x^3(x^4+2)^5,dx,\n` |
| 151 | L6 | 180:18,181:17 | `\n\int x^3(x^4+2)^5\,dx\n=\frac14\int u^5\,du\n=\frac{u^6}{24}+C\n=\frac{(x^4+2)^6}{24}+C.\n` | `\n\int x^3(x^4+2)^5,dx\n=\frac14\int u^5,du\n=\frac{u^6}{24}+C\n=\frac{(x^4+2)^6}{24}+C.\n` |
| 171 | L7 | 210:12 | `\n\int e^{6x}\,dx=\frac16e^{6x}+C.\n` | `\n\int e^{6x},dx=\frac16e^{6x}+C.\n` |
| 176 | L7 | 216:15 | `\n\int xe^{-x^2}\,dx=-\frac12e^{-x^2}+C.\n` | `\n\int xe^{-x^2},dx=-\frac12e^{-x^2}+C.\n` |
| 284 | S4 | 294:21 | `\nF(x)=\frac13\int u^5\,du\n=\frac{(x^3+2)^6}{18}+C.\n` | `\nF(x)=\frac13\int u^5,du\n=\frac{(x^3+2)^6}{18}+C.\n` |
| 297 | S5 | 318:17 | `\nF(x)=\int u^{-2}\,du=-u^{-1}+C=-\frac1{\ln x}+C.\n` | `\nF(x)=\int u^{-2},du=-u^{-1}+C=-\frac1{\ln x}+C.\n` |

`complete-math-failure-map.json` retains full raw HTML, source spans, source/actual payloads and per-character positions. `all13-lost-character-positions.json` gives zero-based Unicode-character and UTF8-byte offsets, plus one-based line/column locations. Raw source bytes are exact; loss occurs in actual server-parser output. No additional entity decoding or reconstructed math was used as acceptance. Repair must preserve the intended expression in destination-supported syntax; replacing the affected thin-space command with ordinary TeX whitespace would avoid this particular Markdown escape collision, but the complete new revision must be rechecked.

NAV-1 (T11): there are21 unique P/H/S labels but zero actual native targets and zero internal links. All seven positive required task-to-hint, task-to-solution, hint-to-task and solution-to-task checks fail. The only two actual links are external source citations. The reading route tells readers to match numbers and each task says “Help: Hn; full solution: Sn,” but neither text is a link; hint and solution paragraphs also lack return links. All hints are correctly grouped before solutions, and the label/content correspondence is retained; those successes do not satisfy native navigation on a supporting destination. `positive-navigation-audit.json` explicitly tests required nonempty relationships, with every task/hint/solution source line, rather than passing an empty set of links. Repair requires at least21 stable task/help targets and28 directed help/return links for seven tasks, plus an appropriate route/group navigation.

All nonmath prose matches after ordinary whitespace folding when the ordered math nodes are masked. Whole prose-plus-math equality correctly fails only on the13 lost backslashes. All29 paragraph-start L/P/H/S labels match in order, including every21 task/help label. In-paragraph references are excluded from this label count.

Frozen identity: `c222a4fbf9c51cb72141e352dfe909278febb37a`; teaching23136bytes, SHA256 `60f908bb588e6dea64725b321f6eb753a33f8293bd452105f9fd48cefe68adbb`. Fresh immutable raw bytes equal local frozen bytes. Embedded commit/path/untruncated source identity pass; its rawLines representation omits only the terminal newline. This packet has one constituent and no figure markup/files requiring visual asset inspection.

All21 referenced stylesheet assets were fetched. Actual body default is weight400; article has no bold/italic/heading/table-header/definition-term prose nodes and inline styles only specify mathematical display mode. Applicable fetched rules do not establish unintended prose emphasis. Live computed styles/pixels were not inspected, so no live-style pass is claimed.

Both external source hrefs are exact and successfully fetched. Official/immutable/local Lecture15 PDF bytes agree,130496bytes,five pages,SHA256 `10c3dc97fa877d3ed97c5561b5082dca3006c632d85e58e01d059484ae455323`. The official supplemental MVT PDF is472962bytes,SHA256 `9428a339cbc094840fdd85c58f4116d71fedbe29107d3d346d6a35fc7c1bba6f`; page1 text is retained as target-identity evidence. This destination review does not claim a complete source-PDF visual/technical audit.

Root explicitly held the full internal preview for the known-failing v1. No PDF build, faithful AST conversion, native-PDF-navigation or final-page pass is claimed. A separately rendered preview would not remove the actual parser/navigation failures. No learner/source/skill files were edited and nothing was published.

Primary evidence: `final-audit.json`, `complete-math-failure-map.json`, `all13-lost-character-positions.json`, `positive-navigation-audit.json`, `paragraph-label-check.json`, original GitHub page/article/raw source, complete math/prose/navigation/CSS records and source-PDF identity records. Live GitHub pixels, client MathJax, computed styles, responsive behavior and browser clicks remain unobserved. Originals remain unchanged for consolidated repair.
