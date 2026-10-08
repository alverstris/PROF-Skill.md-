D003 source technical review

Derivatives of products, quotients, sine, cosine

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/23c2c1b1ab31c9f10745b18e7b0bf131_lec3.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec3/
SHA-256: ccf25930cfad63d99e3fd5045e7931860051bbbb3eedd2bd8cd9318ebd32845a

The exact cached PDF hash was independently checked. All five complete text extractions and all five original page renders, including the cover, were read/inspected. PDF page 1 is the cover; PDF pages 2–5 are printed pages 1–4. No portion was unreadable. The PDF skill was applied read-only.

Page and figure coverage

PDF page 1 (printed cover): MIT OCW course identity, Fall 2006, terms/citation notice.
PDF page 2 (printed 1): Specific versus general derivative formulas; constant-multiple and sum rules; Function sum/product notation; Difference-quotient proof of sum rule; Review of sin(h)/h and (cos(h)-1)/h limits at zero; Sine/cosine derivatives at zero and setup at arbitrary x.
PDF page 3 (printed 2): Sine addition identity and sine derivative; Cosine derivative stated by analogous calculation; Product rule and full add-subtract proof; Differentiability implies continuity condition.
PDF page 4 (printed 3): Increment notation; Geometric product increment and discarded cross term.
Figure 1: Orange uv rectangle; red u Delta-v strip; yellow v Delta-u strip; white Delta-u Delta-v corner; horizontal u and Delta-u, vertical v and Delta-v.
PDF page 5 (printed 4): Quotient increment algebra; Quotient rule limit.

Findings and independent deductions

D003-E01 | confirmed_notational_source_error | PDF page(s) 2 | General Examples item 2 and sum-rule proof heading
The source prints (cu) = cu-prime in the item and (u+v) = u-prime+v-prime in the heading, omitting the derivative prime on the left.
Read these as (cu)-prime = c u-prime and (u+v)-prime = u-prime+v-prime. The displayed derivation and later constant-multiple sentence use the intended correct forms.
Without the missing primes the equalities fail, e.g. u(x)=x, c=1.

D003-C01 | required_condition | PDF page(s) 2, 3 | Sum, constant-multiple, and product rules
The rules require the component functions to be differentiable at the point; c is constant. Product proof states this explicitly.
Take finite two-sided derivatives on a neighborhood of the point (or formulate appropriate one-sided variants).
The limit sum/product operations use existence of the finite difference-quotient limits; differentiability gives continuity.

D003-C02 | implicit_convention | PDF page(s) 2, 3 | Trigonometric limits and derivative formulas
The displayed limits and derivatives use radian measure; this packet does not repeat that convention.
For radians, sin-prime(x)=cos(x), cos-prime(x)=-sin(x). For degree-valued input a factor pi/180 is needed.
Writing sin_degrees(x)=sin_radians(pi*x/180) accounts for the scaling.

D003-G01 | abbreviated_proof_not_false_result | PDF page(s) 4 | Figure 1 and instruction to divide by Delta-x
Smallness of Delta-u Delta-v alone is insufficient to justify its disappearance after division by Delta-x. The figure is explicitly called an intuitive justification.
Use (Delta-u Delta-v)/Delta-x = (Delta-u/Delta-x) Delta-v -> u-prime(x)*0=0.
Differentiability of u and continuity of v supply both factors; this completes the omitted limiting step. The figure assumes positive side lengths and positive increments, whereas the algebra holds for signed increments.

D003-C03 | omitted_domain_condition | PDF page(s) 5 | Quotient formula and its proof
The page does not explicitly require v(x) nonzero.
Require u and v differentiable at x and v(x) != 0. Continuity then makes v(x+h) nonzero for sufficiently small h.
The exact common-denominator identity and limit division are then legal, giving (u-prime*v-u*v-prime)/v^2.

D003-G02 | explicitly_deferred_calculation | PDF page(s) 3 | Cosine derivative
The cosine derivative is asserted after saying a similar calculation gives it; the derivation is not displayed.
cos(x+h)-cos(x) = cos(x)(cos(h)-1)-sin(x)sin(h); divide by h and use the two reviewed limits.
The result is -sin(x), with no further hypothesis beyond the radian convention.

Technical disposition

The principal derivative formulas and exact algebra are correct under the stated or recorded conditions. The two missing left-hand primes on PDF page 2 are actual typographical source errors. The geometric limit step, omitted cosine calculation, radian convention, and quotient nonvanishing requirement are recorded separately; no missing explanation is treated as an incorrect derivative result. No external search was needed, and this report makes no judgment about any PROF document or learner outcome.
