# D013 source review

Mapping: D013 = MIT 18.01 Fall 2006, Lecture 14, Mean Value Theorem and Inequalities. SOURCE preparation only. All five cached text pages were read; all five 1224 by 1584 page renders and all three figures were individually inspected. PDF page 1 is the cover; PDF pages 2-5 are printed pages 1-4.

PDF: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L14/lec14.pdf
Official asset: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/1a211af8e4860b63b801aa3d6e7a2e95_lec14.pdf
SHA-256 recomputed: 67d74be87119ab367516c8a80cc710664e48059bc1184c7042846556b3c0a609. Exact audit.json match; 634,448 bytes, five pages.

## Page coverage

| PDF page | Printed page | Content and visual inspection |
| --- | --- | --- |
| 1 | cover | MIT OCW course, term and terms notice. |
| 2 | 1 | Full MVT statement with endpoint conditions, secant/tangent slopes, Figure 1, geometric proof and absolute-value warning. |
| 3 | 2 | Figure 2 absolute-value secant, travel example, equivalent MVT formulas and linear approximation. |
| 4 | 3 | Figure 3 approximation error, derivative-sign consequences, definitions, proofs of increasing and constant cases. |
| 5 | 4 | Exponential inequalities, derivative induction through cubic polynomial, infinite-series preview. |

## Resolved mathematical witnesses

The theorem is correct for a<b, f continuous on [a,b] and differentiable on (a,b): some c in (a,b) satisfies f'(c)=(f(b)-f(a))/(b-a). It neither requires endpoint derivatives nor a continuous derivative, and does not assert uniqueness of c. The displayed alternative formulas follow by multiplication and rearrangement. The x-version explicitly takes x>a; for x<a, c is instead between x and a. At x=a the equality is trivial and there need not be any point strictly between the identical endpoints.

A complete version of the source's moving-line proof is to set m=(f(b)-f(a))/(b-a) and g(t)=f(t)-f(a)-m(t-a). Then g(a)=g(b)=0. If g is identically zero, any interior c works. Otherwise a negative minimum or positive maximum occurs at an interior point by continuity and compactness; differentiability and Fermat's theorem give g'(c)=0. Thus f'(c)=m. Figure 1 correctly shows a parallel tangent with a<c<b; the drawing need not contain the only such tangent. Sliding lines must be considered on [a,b], not on an unspecified full graph.

For |t| with a<0<b, the secant slope is (a+b)/(b-a), strictly between -1 and 1. Every existing derivative is -1 or 1, so no derivative equals that secant slope. The parallel supporting line from below meets the cusp at 0, where the derivative is undefined. Figure 2 correctly depicts this failure of the differentiability hypothesis. If both endpoints lie on one side of zero, the theorem does apply there. Slopes ±1 can contact an entire ray/segment; slopes outside [-1,1] do not have the asserted first-contact behavior. Thus the prose's 'no matter what its slope is' requires the secant-straddling-zero context.

For derivative-sign consequences, apply the MVT to any a<b in the same interval. The sign of f(b)-f(a)=f'(c)(b-a) is positive, negative, or zero as claimed. This proves strict monotonicity when the derivative is strictly signed, and constancy when it vanishes everywhere on the interval. The missing decreasing proof follows by the same equation, with a negative factor f'(c).

For exponentials, f1=e^x-1 satisfies f1(0)=0 and f1'=e^x>0. Hence f1>0 for x>0. With f2=e^x-1-x, f2(0)=0 and f2'=f1>0 for x>0, so f2>0 there. Generally R_n(x)=e^x-sum_(k=0)^n x^k/k! has R_n(0)=0 and R_n'=R_(n-1); induction proves R_n>0 for x>0. This verifies the displayed linear, quadratic and cubic truncation inequalities on that domain. At x=0 every displayed strict comparison with a Taylor polynomial becomes equality. The linear inequality is also strict for x<0: f2'=e^x-1<0 there and f2(0)=0. The quadratic strict lower bound fails for negative x, for example e^(-1)<1-1+1/2=1/2. Taylor's remainder e^ξ x^(n+1)/(n+1)! tends to zero for each fixed real x, establishing the previewed infinite sum for all real x; that convergence proof is deferred by the source.

The travel arithmetic is correct: (1000-0)/(3-0)=1000/3 mph. For this derivative to be actual speed, f should be accumulated distance along a differentiable route of total length 1000 miles, or the trip should be monotone along the single scalar direction used for position. Differentiating literal radial distance from Boston on an arbitrary curved route gives radial speed, not total speed.

## Confirmed source errors

1. PDF p4, printed p3: the definition of decreasing incorrectly repeats f(a)<f(b) for a<b. It must be f(a)>f(b). For example, f(x)=-x has negative derivative and f(0)=0>f(1)=-1.
2. PDF p5, printed p4: in the proof for f1=e^x-1, one intermediate comparison switches to undefined f(x)>f(0). It should retain f1(x)>f1(0); the surrounding argument and final inequality are correct.

## Missing conditions and pedagogical omissions

- The geometric proof needs the compact interval, existence of an extremum, interior-contact argument, and affine special case made explicit. These complete an otherwise correct geometric idea.
- The absolute-value statement's unrestricted slope wording needs a<0<b and the associated secant slope in (-1,1). The figure supplies that intended setting; it is not a universal supporting-line claim.
- The three derivative-sign conclusions require a common interval of differentiability and appropriate endpoint continuity when endpoints are included. On disconnected domains they need not compare values across components: -1/x has positive derivative on R without zero but f(-1)=1>f(1)=-1; 1/x provides the reversed example for negative derivative. A function equal to 0 for x<0 and 1 for x>0 has derivative zero throughout its domain but no single global constant.
- Figure 3 shows a convex case with the graph above its tangent. It does not establish a universal sign or numerical bound for linearization error. The general differentiability statement is f(x)=f(a)+f'(a)(x-a)+o(|x-a|).
- Item 3 in the initial exponential list omits the domain; e^x>1+x fails at x=0. The proof establishes x>0, and the stronger correct global version is e^x≥1+x, with equality exactly at zero. The quadratic inequality also needs x>0 as supplied by the surrounding progression, not all real x. These are omitted domain/equality qualifications rather than incorrect calculations.
- The travel story relies on differentiability and on a scalar distance whose derivative is the desired speed, as detailed above. The scalar MVT does not identify total speed from an arbitrary radial coordinate.
- The infinite-sum equality is an announced later result, not proved by the finite inequalities alone. Remainder convergence closes the logical gap when a proof is needed.

Open technical uncertainties: none. No teaching audit, external record, or repository was edited.
