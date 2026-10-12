# D008 r31 destination preservation

**PASS.** All 252 source expressions preserve their mathematical structure and inline/display type in the three actual immutable GitHub captures. No differences or unsupported forms were found.

| Source | Expressions | Inline / display | Whole prose characters | Text links | Explicit anchors | Image alts |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| README.md | 187/187 | 156 / 31 | 21304 | 20 | 7 | 4 |
| hints.md | 14/14 | 14 / 0 | 2268 | 16 | 7 | 0 |
| solutions.md | 51/51 | 34 / 17 | 5921 | 15 | 7 | 0 |
| **Total** | **252/252** | **204 / 48** | **29,493** | **51** | **21** | **4** |

The 51 textual links comprise 48 local links and 3 external links. Every label and resolved href matches. All 21 explicit IDs match GitHub’s corresponding `user-content-` IDs. All four image alt texts and image wrapper hrefs match. Href and ID preservation does not establish navigation or fragment landing behavior.

Every expression was independently extracted from the complete frozen source, then compared in order with its actual article slot and MathML structure. All embedded MathML strings agree with the capture arrays; no raw-math or error slots occur. Coverage includes 67 fractions, 191 attached script structures (174 upper/power operands and 17 lower operands), 6 square roots and 13 distinct upright runs. No algebraic equivalence was substituted for preserved structure.

The entire ordered nonmath prose matches after only the documented markup/whitespace normalization and positional math markers. Wording, punctuation, case and order remain exact. The pre-capture source inventory agrees with every expression, full prose string, textual link, anchor and alt used in this comparison.

Existing v4 was used unchanged; no parser extension was needed. Unknown constructs remain explicit failures. Source, capture and comparator hashes were rechecked after comparison: all seven frozen files and all three exact captures remain unchanged.

- [Combined machine-readable coverage and hash record](math-preservation.json)
- [Independent source inventory](source-inventory.json)
- [README complete per-expression and full-prose comparison](readme/math-preservation.json)
- [Hints complete per-expression and full-prose comparison](hints/math-preservation.json)
- [Solutions complete per-expression and full-prose comparison](solutions/math-preservation.json)

Immutable commit: `81076b4c593fc1d685648c72892769c7a025f390`. Manifest SHA256: `7bc78597ea26b3fd56ea7ab39e37f7385407215117efa6436ff54dcb9e1da060`. Comparator v4 SHA256: `7466be19fe2073d2b8de4f8bc9e1a20209245741a466cb048ab7295eb303d6df`.

This is destination preservation only. Root supplied the actual DOM captures and owns visual/navigation checks. This report makes no source-science/SASIS, visual geometry, image pixel/diagram semantics, click-success or fragment-landing verdict.
