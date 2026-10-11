# D016 r26b live lesson destination review

Date: 2026-10-11. Reviewer: root, post-freeze destination audit only.

Exact publication: `51a78beccef858072b1da8d057ef3dff09878409`.
URL: https://github.com/alverstris/PROF-Skill.md-/blob/51a78beccef858072b1da8d057ef3dff09878409/runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b/teaching/lesson.md

The actual GitHub Preview article now loads. This is new successful evidence; the previous two Unicorn error observations remain valid historical records and are not overwritten. Inspection used the dedicated cloud Chrome tab 1. It did not use a local renderer as a substitute for GitHub.

## Equations and prose

All 196 lesson expressions were read from the hydrated article's live MathML, in order, preserving fractions, powers, subscripts, limits, sums, integral bounds, grouping and operators in compact DOM records. Each was manually compared with its corresponding inline or fenced expression from the frozen local lesson. Bounded comparisons covered 1–70, 71–105, 106–140, 141–175 and 176–196. All operands, operators and grouping are preserved. This is a complete manual semantic comparison, not a claim of byte equality between TeX and MathML.

The unhydrated initial accessibility snapshot briefly exposed TeX; the later live article renders mathematics. No MathML error or KaTeX error nodes were present. Actual screenshots show the rendered equations, including the long midpoint sum, squeezed bounds and interest underbraces, without lost content or clipping.

All article p, a and li computed styles were checked: font-weight 400 and font-style normal. Mathematical variable italics are part of math typography. Repository navigation and browser chrome are outside the teaching. The stray source backtick previously noted does not remove any equation, operator, help link or prose in the rendered lesson; it is nonmaterial punctuation.

## Full visual traversal

Overlapping viewport screenshots traversed the article from the opening through Sources and scope at its bottom. The inspected sequence included rectangle construction; Figure 1; P1 and pyramid construction; full Figure 2 and containment; squeeze and straight-line comparison; full Figure 3; general construction and continuity; midpoint example/P2; signed total/average/P3; rate units/monthly borrowing; interest multiplier; numerical comparison; P4/P5; sources.

The article is 929 CSS pixels wide. All three embedded images loaded completely with the immutable publication URL. Natural sizes are 1700×799, 1768×884 and 1700×816; displayed sizes are approximately 929×437, 929×465 and 929×446.

Figure 1 passes at embedded reading size: both axes, curve label, all four rectangles and endpoint dots are visible; no clipping or ambiguous relation. Figure 2 passes: all four centred square layers, complete side-length annotation, inner/outer pyramid legend and apex, heights and aligned sectional stack are visible. Figure 3 passes: full triangle/base label and sample rectangle, width, point and arrows are visible. The curve intersects portions of the coloured c_3=1.2 and f(c_3)=1.44 labels, but the complete characters remain readily readable at the actual 929-pixel embedded size; the caption independently gives both values and the same mapping. This is a nonmaterial overlap, not an unresolved reading failure.

No new material failure was demonstrated. The frozen teaching was not edited. Lesson-expression, prose-style and all-three-figure destination gates pass. Cross-file help and return routes are covered by the separate help-destination report; this report alone does not certify those routes.

Saved raw live evidence: `lesson-mathml.json` contains all 196 ordered compact MathML records; `lesson-full.jpg` is the actual GitHub full-page capture. The full-page image includes a sticky navigation overlay around the middle, so the complete overlapping viewport inspection described above, not that overview image alone, establishes visual coverage there.

`lesson-dom.json` preserves a subsequent live DOM observation: 196 math nodes, zero error nodes and zero prose style exceptions. The browser's full-page capture left a wider article layout (993-pixel images in that later observation); the earlier viewport traversal and Figure 3 legibility decision used the narrower 929-pixel layout documented above.
