D001 source visual review, 2026-10-08

The earlier source-image access block is resolved. The cloud execution environment downloaded the original eight-page MIT PDF and rendered it with Poppler. The lead actually viewed every page at a 1500-pixel long edge, including all five figures and the opening expression. The independent notes audit also viewed all eight pages. This is actual image inspection, not a text-only screenshot placeholder or a claim inferred from successful rendering.

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/c6a2d4081848972d197c41332e604d49_lec1.pdf

PDF SHA-256: d361861e8804a206ef8ef7f75c7e6db62ba0a4a893f3d5818a859895ce565a0e. Length: 1,096,602 bytes. Eight file pages; cover followed by printed pages 1–7. The audit records reproduce acquisition, page locators and image paths.

Comparison against teaching-v2.md, SHA-256 5a892606c9064d56bb6dea693ed5b3dfbb823608da9a4b1926c408aed00aca5b:

| File page | Inspected source content | Current teaching and consequence |
| --- | --- | --- |
| 1 | MIT 18.01 Fall 2006 cover and terms reference | P41 identifies the course and source. |
| 2 / printed 1 | Preview is the derivative of exp(x arctan x). Figure 1 distinguishes the fixed point, moving point, secant and tangent. | P03 keeps the elaborate expression as a preview; no inference depends on its evaluation. P04–P06 supply the meaningful point/slope relationships. |
| 3 / printed 2 | Figure 2 shows horizontal input change and vertical output change; secant quotient and reciprocal algebra are legible. | P04–P08 give the coordinates, signed changes, domain and cancellation conditions. No missing graphic premise found. |
| 4 / printed 3 | Figure 3 shows the decreasing positive reciprocal branch and its negative-slope tangent; the tangent equation is legible. | P08 and P10 preserve the derivative sign and equation. |
| 5 / printed 4 | Figure 4 shades the triangle bounded by tangent and axes; the source derives one intercept and uses symmetry for the other. | P11–P13 supply both intercepts, perpendicular lengths, area and the reflection argument. Negative-branch treatment is a derived extension with explicit absolute lengths. |
| 6 / printed 5 | Figure 5 labels x0, 2x0, y0, 2y0. Derivative notation is clear; the prime-notation historical label is incorrect in the source. | P11–P15 preserve the geometric relations and explain the notation; the existing independently sourced attribution correction remains. |
| 7 / printed 6 | Positive-integer power proof, binomial remainder, polynomial derivative and falling-height model. The displayed average-speed definition equates it with a signed height quotient and distance/time. | P16–P26 explain the finite remainder and model conditions and distinguish velocity from speed. This page is the precise locator for the source's signed-quotient wording problem. |
| 8 / printed 7 | The source calculates positive average speed 400/5 = 80 ft/s, and a negative height derivative -160 ft/s at impact, approximately 110 mph downward. | P25–P28 preserve the correct positive speed while explaining signed velocity and the pre-impact limit. The source does not calculate -80 ft/s as its average speed. |

No newly observed source detail requires a teaching-content repair. All consequential diagrams and typography are recoverable and represented in the current coordinate descriptions and equations. This closes EXT01; it does not replace the required fresh SASIS reading or final-format check.

Evidence correction: the original issue ledger located SRC01 at printed page 7/file page 8. Its defining ambiguity is actually on printed page 6/file page 7. The later positive 80 ft/s calculation is correct. The current ledger is corrected; historical author and reviewer reports are preserved unchanged. P25's existing description remains accurate.
