D017 source technical review

First fundamental theorem of calculus

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/817a2c46ddc23e2efda247a79ddeed34_lec19.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec19/
SHA-256: f3bccf9b801aebb3266932eb8a549f700e5a38f26d377c85f6fd96ed9e7fb3b7

Independently recomputed SHA-256 matches the audit. Read all 5 complete page text extractions and opened every original full-page render with view_image, including the cover. PDF page 1 is the unnumbered cover; PDF pages 2–5 are printed pages 1–4. The PDF skill was read and applied for read-only inspection. No unreadable portion. This preparation is source evidence only, not a teaching draft, PROF judgment, SASIS review, or lecture closure.

Page and figure coverage

PDF 1 / printed cover: MIT OCW course identity, Fall 2006 and terms/citation notice.
PDF 2 / printed 1: FTC 1 statement with continuity and F-prime=f; Endpoint evaluation notation; Examples: integral x², sine on [0,π], x^5 on [0,1].
Figure 1: Positive sine hump from 0 to π, vertical height 1, horizontal endpoint π.
PDF 3 / printed 2: Position/velocity and odometer interpretation, Riemann sum approximation; Source qualification about sign changes and round trips; Integral sine from 0 to 2π and signed area.
Figure 2: Sine wave with positive first hump marked + and negative second hump marked −, height tick 1 and endpoint 2π.
PDF 4 / printed 3: Additivity across an intermediate endpoint; Reversed-limit sign convention and arbitrary endpoint ordering.
Figure 3: Positive curve partitioned by verticals at a<b<c, illustrating adjacent integral intervals.
PDF 5 / printed 4: Integral comparison for a<b; Bounds e≥2 and e≥5/2; Indefinite and definite substitution formulas; Example u=x³+2 with transformed limits 3,10.

Findings and independent deductions

D017-C01 | theorem_domain_clarification | PDF 2 / printed 1 | FTC 1 boxed statement
Continuity of f and F-prime=f are stated but the interval and endpoint regularity are implicit.
Take f continuous on [a,b], F continuous there and differentiable on its interior with F-prime=f; reverse limits as defined on PDF4 when needed.
Subdivide [a,b]. The mean value theorem gives F(xi)-F(xi-1)=f(ξi)Δxi; telescoping and the Riemann-sum limit yield F(b)-F(a). This is an independent proof; this packet states FTC 1 without proving it.

D017-E01 | terminology_requires_sign_qualification | PDF 3 / printed 2 | Opening intuitive interpretation
v=x-prime is called speed and x(b)-x(a) an odometer difference. The later paragraph correctly distinguishes cancellation when v changes sign, but constant negative velocity also invalidates the speed/odometer language.
Call v signed velocity, |v| speed, integral v displacement, and integral |v| total distance for a≤b. The odometer interpretation directly holds for v≥0.
For x(t)=-t on [0,1], v=-1 never changes sign yet displacement=-1 and distance=1. For v=sin t on [0,2π], displacement=0 and total distance=4.

D017-C02 | integral_property_conditions | PDF 4, 5 / printed 3, 4 | Additivity, reversed limits and comparison
Properties require the relevant functions to be integrable across the intervals. The comparison condition a<b is correctly emphasized.
Under Riemann integrability, additivity holds for any a,b,c in a common interval with oriented integrals; comparison holds for a≤b and reverses for a>b.
Integrate the nonnegative difference g-f on increasing limits. For a=b both integrals are zero; thus the parenthetical only if a<b is a useful directional caution rather than a literal exclusion of the equality case.

D017-C03 | substitution_regularity_condition | PDF 5 / printed 4 | Change of Variable
The substitution equalities omit sufficient regularity conditions and indefinite-integral constants.
A sufficient setting is continuous g on an interval containing u([x1,x2]) and continuously differentiable u; use endpoint values u1,u2 with orientation. Indefinite expressions represent antiderivative families up to constants.
If G-prime=g, then (G∘u)-prime=g(u)u-prime; FTC gives G(u2)-G(u1). Monotonicity or injectivity of u is not required for this composed-integrand form.

D017-S01 | reviewer_supplementary_checks | PDF 5 / printed 4 | Estimates and substitution example
The inequalities and transformed endpoints are correct.
Recompute all numerical expressions and the antiderivative independently.
For x≥0, e^x≥1 and e^x≥1+x: derivatives of e^x-1-x are e^x-1≥0 and its value at 0 is 0. Integrating yields e≥2 and ≥5/2. d[(x³+2)^5/15]/dx=(x³+2)^4 x², giving (10^5-3^5)/15=99757/15.

Independent mathematical coverage

- Checked x³/3 differentiation and endpoint subtraction.
- Checked integral_0^π sin x dx=2, integral_0^(2π) sin x dx=0, integral_0^1 x^5 dx=1/6.
- Checked sine diagrams against zero crossings, signs and unit maximum; radian convention implicit.
- Verified integral additivity and reversal through endpoint differences.
- Independently verified comparison estimates and the substitution factor 1/3, limits 3 and 10, and final denominator 15.

Technical disposition

Every displayed integral evaluation is correct. The motion interpretation needs the recorded velocity/speed qualification; the source does explicitly discuss signed cancellation. FTC, comparison and substitution conditions are documented separately, with independent mathematical checks and a supplementary FTC proof.
