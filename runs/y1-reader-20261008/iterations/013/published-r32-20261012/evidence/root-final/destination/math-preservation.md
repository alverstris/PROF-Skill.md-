# D013 r32 destination preservation

**PASS.** All 314 frozen-source expressions preserve mathematical structure and inline/display type in the three actual immutable GitHub captures. Whole prose and all requested textual structure match. No differences or unsupported forms remain.

| Source | Expressions | Inline / display | Prose characters | Text links | Explicit anchors | Alts |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| main.md | 233/233 | 212 / 21 | 21733 | 16 | 6 | 3 |
| hints.md | 10/10 | 10 / 0 | 2422 | 14 | 6 | 0 |
| solutions.md | 71/71 | 65 / 6 | 5969 | 14 | 6 | 0 |
| **Total** | **314/314** | **287 / 27** | **30,124** | **44** | **18** | **3** |

The 44 text links comprise 42 local and two external links. Every label and resolved href matches, all 18 explicit `name` anchors retain their attribute family and match their actual GitHub-prefixed names, and all three image alts and image-wrapper hrefs match. No click or fragment-navigation behavior is inferred.

Every expression was extracted from the complete source and independently compared against its ordered article slot and actual MathML tree. Operands, operators, grouping, fractions, powers, subscripts, sum bounds, text style and explicit delimiter sizing remain preserved. All article MathML matches the ordered capture arrays; no error or raw-math slots occur. Entire nonmath prose matches after only markup/whitespace normalization and positional math markers. The initial source inventory matches every compared expression, prose string, link, explicit anchor and alt.

Unchanged v4 explicitly rejected new hbox syntax. Separate v5 adds only observed actual forms: hbox as a distinct text-style node; bigl/bigr parentheses as distinct OPEN/CLOSE nodes with exact 1.2em size; literal factorial punctuation; centered cdots. This was a parser extension, not a source defect. Unknown constructs remain explicit failures. One isolated unknown-command check returned exit 2 and wrote no report.

All six frozen teaching files and all original DOM captures retain their exact hashes. Exact full DOM copies are saved in each page subdirectory. V4 and its archive are unchanged; v5 and its provenance are separately archived.

- [Combined coverage, hashes and complete-record index](math-preservation.json)
- [Independent complete source inventory](source-inventory.json)
- [Main per-expression and whole-prose records](main/math-preservation.json)
- [Hints per-expression and whole-prose records](hints/math-preservation.json)
- [Solutions per-expression and whole-prose records](solutions/math-preservation.json)
- [Actual witnesses for new parser forms](v5-observed-extension-witnesses.json)
- [All named-anchor attribute families and explicit math-style witnesses](anchor-style-preservation.json)

Immutable commit: `36e3d042ba459f3048e1489fd12045029f61abbb`. Manifest SHA256: `a32397e7903eb2e4b09827a51175dce760743fb728e4363cf0f82dfb5c4f3749`. V5 SHA256: `7b77d3704d7358802608892569e8e14225f745dceb1bec1fe402e159ec1bff7e`.

This review is strictly destination preservation. Root owns visual/navigation review. No source-science/SASIS, image geometry/semantics, click-success or fragment-landing verdict is made.
