D002 source review: MIT 18.01 Fall 2006, Lecture 2

Technical source preparation only. This review does not author a teaching document, establish a learner baseline, design the next document, run SASIS, or change PROF or GitHub.

Access and actual inspection

The packet is the lecture-specific 12-page PDF, including its cover. PDF page 1 is unnumbered; PDF pages 2–12 correspond to printed pages 1–11. All 12 extracted page texts were read, and all 12 original page renders were individually opened and visually inspected at 1224 × 1584 pixels. No page was accepted solely from the earlier audit. All prose, formulas, figure labels and endpoint markers were readable. There are no missing pages or unresolved symbol readings.

Official index: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/lecture-notes/

Resource page: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec2/

Exact PDF asset: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/acebd5cc8fe0315270d486685739d08f_lec2.pdf

Local source: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L02/lec2.pdf

Recomputed SHA-256: 55bc48e3f4b4f1652984ed5e5f59ab2ef366fe897aa46f38b70ea8c4f89437e3

Size: 2,718,760 bytes. Hash and page count match the supplied audit. URLs and original acquisition provenance were read from the supplied audit and acquisition records; this review did not download the source again. No external browsing was needed to resolve a consequential uncertain claim. A separate reader independently checked the mathematics and original images on PDF pages 8–12 and agreed with the findings below.

Source coverage

| PDF / printed page | Required source content | Figures |
|---|---|---|
| 1 / none | MIT OCW identity, course, term and terms/citation link | None |
| 2 / 1 | Finite rate of change and derivative; current, speed and spatial temperature gradient | 1: generic curve with Δx and Δy |
| 3 / 2 | Measurement sensitivity ΔL/Δh; GPS illustration and simplified geometry | 2: curved Earth; 3: flat right triangle |
| 4 / 3 | Rational limit by substitution; punctured derivative quotient; continuity; piecewise discontinuity | 4: left filled origin and right open intercept |
| 5 / 4 | Continuation of piecewise example; one-sided limits; removable discontinuity; sin(x)/x at zero | 5: curve with one hole |
| 6 / 5 | Jump discontinuity; infinite discontinuity; one-sided reciprocal limits | 6: unequal finite levels; 7: reciprocal hyperbola |
| 7 / 6 | Persistent oscillation and failure of a limit | 8: right-side oscillatory schematic |
| 8 / 7 | Function graph versus derivative graph; reciprocal derivative; parity | 9: 1/x and −1/x² with corresponding tangent/derivative samples |
| 9 / 8 | Pumpkin height 400−16t² on [−5,5] and derivative graph | 10: flight/building scene; 11: height and derivative |
| 10 / 9 | Both trigonometric limits; radians; sine-limit geometry | 12: unit-circle sector; 13: small-angle view |
| 11 / 10 | Cosine-limit geometry and relative horizontal gap | 14: cosθ projection; 15: small-angle gap |
| 12 / 11 | Differentiability implies continuity; proof and nonzero-denominator explanation | None |

Confirmed source errors

1. F01, PDF 4 / printed 3, piecewise formula beneath Figure 4: the second branch is printed −x for x≥0. It must be −x for x≤0. The printed conditions assign two incompatible values for every x>0 and no value for x<0. Figure 4 and the continuation on PDF 5 instead establish the corrected function: −x on x≤0 and x+1 on x>0. Consequently f(0)=0, the left limit is 0, the right limit is 1, and the two-sided limit does not exist.

2. F02, PDF 6 / printed 5, sentence beneath Figure 6: the x<x0 clause is paired with x→x0+ and the x>x0 clause with x→x0−. Both superscripts are reversed. The correct pairings are x<x0 with x→x0− and x>x0 with x→x0+. The definitions on PDF 5 are correctly printed. The intended criterion of unequal finite side limits and Figure 6 are sound.

3. F03, PDF 11 / printed 10, paragraph between Figures 14 and 15: the phrase “vertical distance θ along the arc” misidentifies the geometry. For the pictured unit circle and positive radian angle, θ is arc length. Vertical displacement is sinθ. The horizontal gap is correctly labelled 1−cosθ.

Proof gaps, ambiguities and conditions

- F04, PDF 5 / printed 4, opening limit: the displayed x→0 limit is 1 only under the prose restriction x>0. Its unambiguous notation is x→0+. It is not the two-sided limit of the corrected example.
- F05, PDF 5 / printed 4, removable-discontinuity definition: both one-sided limits must exist and equal the same finite real number L. The point value must be absent or different from L. An undefined point value alone does not establish removability; neither does agreement at an infinite limit.
- F06, PDF 4 / printed 3, derivative quotient: the printed subscript x→x0 is coherent if Δx=x−x0 is understood. With the displayed increment notation alone, Δx→0 is clearer. This is implicit notation rather than an incorrect derivative calculation.
- F07–F08, PDF 10–11 / printed 9–10: the trigonometric limit values are correct, but the explanations are visual intuition rather than complete proofs. The sine argument supplies no bound on sinθ/θ. The cosine argument says the horizontal gap is much smaller than the arc, which is the ratio conclusion requiring justification. All four sector figures depict positive acute angles; the negative-angle extension of each two-sided limit is unstated. Geometric lengths are nonnegative, so they cannot simply be labelled by a negative θ.
- F09, PDF 8 / printed 7: the parity rule assumes a symmetric domain and differentiability at paired points. “And vice versa” has the valid intended reading that the derivative of an even function is odd. It must not be read as saying that an even derivative forces the original function to be odd: x+1 is a counterexample.
- F10, PDF 9 / printed 8: the usual two-sided derivative of a function restricted to [−5,5] is taken on (−5,5). Closed endpoint dots on the derivative graph require a polynomial-extension or one-sided convention. Negative times put the time origin at the apex; that convention is not explained. The page gives no units or building height.

Independent mathematical checks

| Source locator | Checked deduction and conditions |
|---|---|
| PDF 2 / printed 1 | Δy/Δx approaches a derivative only where that derivative exists, with a fixed base point and nonzero increment. ds/dt is speed when s means distance traveled; for signed position it is velocity. |
| PDF 3 / printed 2, Fig. 3 | For the flat model with fixed s, h²=s²+L². Taking L≥0 gives L=√(h²−s²), h≥s, and local sensitivity dL/dh=h/√(h²−s²) for h>s. The derivative becomes unbounded as h approaches s from above when s>0. These equations are deductions from the figure, not printed equations. The curved model and referenced Problem Set 1 have no supplied numerical data. |
| PDF 4 / printed 3 | At x=3 the denominator x+1 equals 4, so direct substitution gives 12/4=3. Cancellation also gives x on x≠−1. Continuity requires a defined point value and matching finite limit. |
| PDF 5–7 / printed 4–6 | sin(x)/x can be continuously extended at zero by the value 1. Figure 6 has no specified value at x0, and no value can reconcile its unequal side limits. For 1/x, right divergence is +∞ and left divergence is −∞; the two-sided limit does not exist. Figure 8 depicts a nonvanishing oscillation amplitude. No analytic formula is supplied, and merely oscillating does not by itself preclude a limit. |
| PDF 8 / printed 7 | For x≠0, the reciprocal difference quotient simplifies to −1/[x(x+h)] and tends to −1/x². Both reciprocal branches decrease; the derivative is negative and even. Neither function is defined at zero. |
| PDF 9 / printed 8 | y′(t)=−32t. Heights at t=−5,0,5 are 0,400,0. Under polynomial extension, derivative values there are 160,0,−160. The derivative represents signed vertical velocity; it is positive before the apex and negative after it. |
| PDF 10 / printed 9 | For 0<θ<π/2 in radians, sector/triangle comparison gives sinθ≤θ≤tanθ, hence cosθ≤sinθ/θ≤1. Together with cosθ→1, this proves the positive-side limit. The ratio sinθ/θ is even, establishing the negative-side limit. These quantitative steps are not printed. |
| PDF 10–11 / printed 9–10 | The geometric inequality \|sin u\|≤\|u\| gives 0≤1−cosθ=2sin²(θ/2)≤θ²/2. Thus \|(1−cosθ)/θ\|≤\|θ\|/2→0 for nonzero real radian θ, proving both sides. The same bound gives cosθ→1 without appealing to trigonometric differentiation. |
| PDF 12 / printed 11 | The proof is valid for a finite derivative: for x≠x0, f(x)−f(x0)=[(f(x)−f(x0))/(x−x0)](x−x0). The factors tend to f′(x0) and 0, so the difference tends to 0 and f is continuous at x0. An infinite “derivative” would not justify the finite product-limit step. |

Figure fidelity and packet boundaries

All 15 figures were inspected. Figures 1, 4, 6, 7, 9 and 11 support the stated qualitative rate, endpoint, sign and limiting behavior, subject to the corrections above. Figure 5 shows a hole but no numerical location. Figure 8 supplies no formula and only pictures approach from the right. Figures 10–11 are schematic rather than labelled quantitative axes. Figures 12–15 label unit-radius geometry consistently for positive acute angles, apart from the arc-length wording in the prose.

The packet references Problem Set 1, but that problem set was not inspected. No lecture video, transcript, textbook chapter or other lecture packet was inspected. No exact spherical GPS equation, units, numerical data, or analytic formula for an unlabeled schematic has been invented. The JSON companion records each inspected page, all 15 figures, 20 claims with conditions, and the 10 findings. Source statements and reviewer deductions are distinguished throughout.
