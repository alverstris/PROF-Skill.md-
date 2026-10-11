# Additive actual-destination comparison of the 25 flagged expressions

This preserves the earlier static inventory and supplements it with the root browser owner’s actual client-hydrated captures. Nine target expressions fail structural preservation, across D007, D008, D013 and D015. Sixteen targets preserve the complete expression. D012 has no demonstrated damage in these two targets. These are current accepted artifacts, not historical failed candidates.

The accepted canonical paths and SHA-256 values are those in `math-feature-inventory.json` and `live-targets.json`, pinned to repository object `f8f76d0775051896326fb400ec5782bf1d954971`. Each live capture URL exactly matches its immutable published target URL. Root captured the DOM; this reviewer independently parsed the complete supplied article and ordered MathML array. This is a structural/content verdict, not an independent pixel-legibility verdict.

## Alignment and method

Source and actual counts agree for all five pages (371, 305, 309, 214, 116). Every inline/display classification agrees at every ordinal. The actual article renderer count agrees with each ordered array, and all ordinals run consecutively from 1. At every target I compared both immediate neighboring expressions against the source and inspected the full target MathML tree, including fractions, roots, powers, subscripts, derivative marks, grouping, comparisons, operands and domain clauses. Thus target identity does not rely on counts or an assumed ordinal alone. The machine record preserves each complete target tree and neighboring source/MathML witnesses.

All five captures report zero renderer error elements. This does not detect the nine content losses: those expressions rendered successfully after being truncated.

| Case | Actual/source math count | Failed target ordinals | Preserved target ordinals |
|---|---:|---|---|
| D007 | 371 / 371 | 122, 331 | 184, 209 |
| D008 | 305 / 305 | 195 | 73, 153 |
| D012 | 309 / 309 | none | 45, 269 |
| D013 | 214 / 214 | 51, 76, 147, 206, 209 | 93, 104, 107, 110, 121, 122, 154, 193, 201 |
| D015 | 116 / 116 | 75 | 33 |

## Exact failed clauses

| Case / source line / actual ordinal | Original clause or expression | Actual remaining clause | Lost text |
|---|---|---|---|
| D007 / 179 / 122 | `(\arcsin x)'=\frac1{\sqrt{1-x^2}},\qquad -1<x<1.` | `−1` | `<x<1.` |
| D007 / 548 / 331 | `y'=-\frac1{\sqrt{1-x^2}},\qquad -1<x<1.` | `−1` | `<x<1.` |
| D008 / 196 / 195 | `T'=\frac{T}{\sqrt{1-v^2/c^2}},\qquad 0\le v<c.` | `0≤v` | `<c.` |
| D013 / 91 / 51 | `f(x)=f(a)+f'(c)(x-a),\qquad a<c<x.` | `a` | `<c<x.` |
| D013 / 123 / 76 | `f(b)-f(a)=f'(c)(b-a),\qquad a<c<b.` | `a` | `<c<b.` |
| D013 / 205 / 147 | `L(b-a)<f(b)-f(a)<U(b-a).` | `L(b−a)` | `<f(b)-f(a)<U(b-a).` |
| D013 / 314 / 206 | `\ln(1+h)-\ln1=\frac{1}{c}h,\qquad 1<c<1+h.` | `1` | `<c<1+h.` |
| D013 / 318 / 209 | `\frac{h}{1+h}<\ln(1+h)<h.` | `h/(1+h)<ln(1+h)` | `<h.` |
| D015 / 78 / 75 | `y=\sqrt{3-\frac{x^2}{2}},\qquad -\sqrt6<x<\sqrt6.` | `−√6` | `<x<\sqrt6.` |

## Preserved structures

D007 ordinals 184 and 209 preserve all derivative equalities, fractions, powers and the complete x>0 condition. D008 ordinals 73 and 153 preserve both function/approximation expressions and x>−1. D012 ordinals 45 and 269 preserve the full decimal-square bracket and signed polynomial evaluation, including every comparison.

D013 ordinals 93, 104, 107, 110, 121, 122, 154, 193 and 201 preserve all operands and comparisons, including both strict bounds in ordinal 154, both negative-input comparisons in ordinal 201, and the powers/factorial/fractions in ordinals 121–122. D015 solutions ordinal 33 preserves the full tangent formula and both sides of −π/2<x²/2<π/2. These are positive preservation findings for the specified expressions only.

The failures occur when a literal less-than is followed by a letter within the source payload. The preserved comparison targets include greater-than signs, less-than before numerals, and less-than before a TeX backslash command. This pattern explains these observations but is not a universal parser guarantee; the recorded exact structures, not a heuristic rule, support the dispositions.

## Dependency disposition and limits

The current accepted D007, D008, D013 and D015 have demonstrated learner-facing content loss and must be reopened for the affected destination preservation dependency. Earlier static wrappers preserved these TeX payloads but did not establish live client rendering. D012’s two flagged targets are structurally preserved in the current capture. The other twelve accepted cases lacked all three specific source features in the complete earlier inventory; no blanket re-review or regeneration claim follows.

This reviewer did not operate a browser and does not independently certify pixel placement or visual readability. Root separately owns visual inspection. No GitHub object, frozen teaching document, queue status or acceptance record was changed by this audit.
