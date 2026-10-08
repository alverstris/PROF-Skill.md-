D005 source technical review

Implicit differentiation, inverses

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/18d6a86a30a4bc046c5f7034d47587f1_lec5.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec5/
SHA-256: d0ed3d4624b0a15cc5c65cff6aece48f70e185f5c417ba7d37a7c935b652848c

All five full text extractions and all five original page renders were read/inspected. Both figures, including all labels and guides, were inspected. Hash independently verified. PDF pages 2–5 are printed pages 1–4. PDF skill applied read-only.

Page and figure coverage

PDF page 1 (printed cover): MIT OCW cover, course/term identity and terms notice.
PDF page 2 (printed 1): Review of integer power rules; Rational-power derivative via y^n=x^m and exponent simplification; Circle equation and positive-square-root explicit differentiation.
PDF page 3 (printed 2): Circle implicit differentiation; Cubic implicit example y^3+xy^2+1=0; Inverse function notation and reciprocal derivative computation.
PDF page 4 (printed 3): Arctangent implicit derivative; Triangle/Pythagorean simplification of cos(arctan(x)).
Figure 1: Right triangle: adjacent vertical side 1, opposite horizontal side x, hypotenuse sqrt(1+x^2), angle y at upper left; labels and right-angle square inspected.
PDF page 5 (printed 4): Final arctangent derivative; Inverse graph variable exchange; Both inverse composition identities.
Figure 2: Black f(x), blue g(x), red line y=x, axes x and y, dashed guides, labels a=f^(-1)(b) and b=f(a); inspected as a qualitative schematic of reflection.

Findings and independent deductions

D005-C01 | omitted_domain_and_branch_conditions | PDF page(s) 2 | Rational-power calculation
The source says m and n are integers but does not state n != 0, real-power domain, or the nonzero denominator needed when dividing by n*y^(n-1).
Take n positive, reduce m/n when discussing negative inputs, and use x>0 as a sufficient common domain. Negative x is also possible for reduced odd n with the real odd-root convention. Negative powers exclude zero. The division argument is made at nonzero x (and hence nonzero y); x=0 requires a separate check.
Exponent simplification gives (m/n)*x^(m/n-1) correctly on this domain. On a two-sided real domain through zero, positive rational exponent a has derivative 0 at zero if a>1, derivative 1 if a=1, and no finite derivative there if 0<a<1. With even reduced denominator only a one-sided endpoint version is available. A defined constant x^0 has derivative 0 separately; the unsimplified formula involving x^(-1) cannot be evaluated at zero.

D005-G01 | existence_proof_gap | PDF page(s) 2 | Differentiate y^n=x^m
Knowing y=x^(m/n) is a function does not by itself establish that it is differentiable; the chain-rule step presupposes this.
The displayed work correctly computes the derivative conditional on its existence. Away from y=0 the real nth-root inverse is differentiable and supplies the missing existence justification.
For p(y)=y^n, p-prime(y)=n*y^(n-1) is nonzero on the chosen nonzero branch. The inverse difference quotient tends to 1/p-prime(y), which justifies differentiability before composing with x^m.

D005-C02 | omitted_domain_condition | PDF page(s) 2, 3 | Circle examples
The explicit upper branch sqrt(1-x^2) is defined for -1<=x<=1 but its displayed finite derivative applies only for -1<x<1. The implicit formula divides by y.
Use y-prime=-x/y at circle points with y != 0, for either local branch. Points (+/-1,0) have vertical tangents and no finite dy/dx.
2x+2y*y-prime=0 gives the formula when y != 0. At (+/-1,0), the equation would require nonzero 2x=0 if a finite derivative existed.

D005-C03 | omitted_division_condition_and_exception | PDF page(s) 3 | Cubic implicit example
The displayed y-prime=-y^2/(3y^2+2xy) requires 3y^2+2xy != 0 on the curve.
The curve never has y=0. Its unique real point with zero displayed denominator is y=cuberoot(2), x=-(3/2)*cuberoot(2). At this point there is no finite dy/dx and the regular curve has a vertical tangent.
Since y != 0, a vanishing denominator gives x=-3y/2. Substitution into y^3+xy^2+1=0 gives y^3=2. F_x=y^2 is nonzero there. Independently x=-y-y^(-2) has dx/dy=-1+2/y^3=0 there, agreeing with the vertical tangent.

D005-C04 | inverse_hypotheses_and_proof_gap | PDF page(s) 3, 5 | Inverse definition, inverse derivative, and graphing
An inverse function requires a one-to-one restriction and its appropriate range; writing g(f(x))=x for a single pair does not define an inverse globally. The chain-rule computation also assumes inverse differentiability and divides by f-prime(x).
Treat f as a bijection from its chosen domain to its range. For the local derivative, sufficient assumptions are continuous strict monotonicity on an interval and differentiability at x0 with f-prime(x0) != 0. Then g-prime(y0)=1/f-prime(g(y0)), y0=f(x0).
As y->y0, inverse continuity gives g(y)->x0. The inverse difference quotient equals 1/((f(g(y))-f(x0))/(g(y)-x0)), tending to 1/f-prime(x0). A zero forward derivative is not covered. The two composition identities live respectively on the original domain and its range; graph reflection swaps (a,b) to (b,a).

D005-C05 | branch_convention_and_geometric_coverage_gap | PDF page(s) 4, 5 | Arctangent and Figure 1
The source does not state the principal arctan range. A side labeled x in an ordinary triangle only depicts positive x, so the diagram alone does not justify negative inputs or the degenerate x=0 case.
Use the radian principal inverse of tan on (-pi/2,pi/2), with real input x. Its cosine is positive and its derivative 1/(1+x^2) holds for all real x.
sec^2(y)=1+tan^2(y)=1+x^2 implies cos^2(y)=1/(1+x^2) without a sign restriction on x. Positivity of cos(y) on the branch gives cos(y)=1/sqrt(1+x^2). tan-prime(y)=sec^2(y)>0 supplies the nonzero forward derivative. The triangle is consistent for x>0.

Technical disposition

All displayed derivative formulas and exponent/algebra steps are correct where their assumptions and denominators permit them. The source omits important domain, branch, and differentiability conditions, and its chain-rule derivations do not independently prove the existence of the derivatives being computed. These gaps are separated from a false formula claim. No external research was required, and no PROF or learner evaluation is included.
