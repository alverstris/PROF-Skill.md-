# D017 destination math and prose preservation

**PASS — no preservation defect found in the supplied live-GitHub DOM capture.** This is a source-to-destination preservation finding only, not a scientific or SASIS verdict.

Source: `/workspace/scratch/f9c0b7fc7e76/d017-clean-r27/output/teaching.md`  
Verified SHA-256: `0317f26777f5285616be96713d79e1731818fea76d40954f3e21be2c6dbcb7b5`

Actual destination: https://github.com/alverstris/PROF-Skill.md-/blob/a7b7de5e040882fa605716e3a954ee067d3ce9a6/runs/y1-reader-20261008/iterations/017/published-r27-20261011/output/teaching.md  
Capture timestamp: `2026-10-11T21:20:45.969Z`  
Capture SHA-256: `c85626b11852e59640df6431d2f9d67aef472a3183263cf16591657e30de4a67`

| Check | Source | Actual destination | Result |
|---|---:|---:|---|
| All mathematical expressions, in order | 248 | 248 | 248 structural matches |
| Inline expressions | 208 | 208 | Exact type match |
| Display expressions | 40 | 40 | Exact type match |
| Fractions | 39 | 39 | Numerators and denominators preserved |
| Script structures | 212 | 212 | Bases and every sub/sup operand preserved |
| Integral symbols | 70 | 70 | 67 bounded; all bounds preserved |
| Sum with bounds | 1 | 1 | Index, lower bound and upper bound preserved |
| Aligned display | 1 | 1 | Both rows and both cells in each row preserved |
| Nonmath prose, with positional math markers | 20,511 normalized characters | 20,511 | Exact entire-body match |
| Textual links | 35 | 35 | Every label and href preserved |
| Figure alt texts | 2 | 2 | Both exact matches |

The 248 MathML strings embedded in `articleHTML` are byte-for-byte identical to the capture's corresponding `math` array entries. GitHub also adds two image-wrapper anchors; they are separately recorded and are not missing or extra textual links.

The independent restricted-TeX parser compares every expression with the actual MathML tree. It preserves operands, operators, visible grouping delimiters, fractions, script bases and contents, integral/sum bounds, derivative primes, and aligned rows/cells. Normalization is limited to equivalent TeX/MathML symbol spellings, layout wrappers and spacing, the invisible function-application marker, and empty alignment cells. Contiguous numerals retain whole-number script attachment. It does not simplify equations or substitute algebraically equivalent expressions.

Prose comparison removes Markdown/HTML markup, restores ordered-list markers from HTML list starts, collapses whitespace, and replaces each mathematical expression with its matching ordinal marker. Case, wording, punctuation, typographic quotes, order and math positions remain unchanged. Image alt text is checked separately. Both normalized full strings have SHA-256 `ee450f0762914cffd233d2ae7087b812496ba2eb546d1deff77abeba4624fc9a`.

Witness records in `math-preservation.json`: 10 (limit subscript), 19 (bracket and evaluation-bar bounds), 38 (sum and sample-time sub/superscripts), 126 (two aligned rows and nested endpoint subscripts), 145 (10⁵ numerator and changed bounds), 245 (negative starting bound and fractions). Every one of the 248 records includes source line/type/LaTeX, complete actual MathML, independent canonical trees, hashes and pass flags; the full normalized prose and all link-label comparisons are also included.

Review inputs only: no frozen-file changes, browser operation or GitHub writes. The root reviewer owns visual geometry, clipping and link-navigation verification; this review uses the supplied actual-live capture and does not independently repeat navigation.
