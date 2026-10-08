D006 source technical review

Exponential and log Logarithmic differentiation; hyperbolic functions

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/f9af0e98490296c99d330faf47389507_lec6.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec6/
SHA-256: e36b81f73c0e6265a814de8875c3898b1255d2e0aa656547a731b8274a00f66d

All eight complete text extractions and all eight original page renders were read/inspected, including three figures and both final remarks. Hash independently verified. PDF pages 2–8 are printed pages 1–7. PDF skill applied read-only.

Page and figure coverage

PDF page 1 (printed cover): MIT OCW course cover and citation/terms notice.
PDF page 2 (printed 1): Base a>1 assumption; Integer/rational exponent laws and continuous real extension; Difference quotient factorization; Definition of M(a) and analytic derivative-at-zero interpretation.
PDF page 3 (printed 2): M(a) tangent interpretation; Geometric estimates M(2)<1 and M(4)>1; Existence of a base with slope 1.
Figure 1: Increasing convex a^x with a tangent through its vertical-axis intercept; M(a) marks tangent slope at x=0.
PDF page 4 (printed 3): Secant/tangent comparisons for bases 2 and 4.
Figure 2: Black y=2^x, blue slope-1 secant through (0,1) and labeled (1,2), green tangent labeled M(2).
Figure 3: Black y=4^x, blue secant through labeled (-1/2,1/2) and incorrectly labeled (1,0) at the y-intercept; green tangent M(4).
PDF page 5 (printed 4): Definition/uniqueness of e via M(e)=1; Equivalent limit and derivative characterizations; Derivative of e^x; Natural-log inverse statements, signs, product law; Implicit derivation of derivative of ln(x).
PDF page 6 (printed 5): Base-e rewriting and derivative of a^x; Derivatives e^x and e^(3x); Identification M(a)=ln(a), base-10 example; General logarithmic differentiation identity.
PDF page 7 (printed 6): Logarithmic differentiation applied to a^x; Derivative of x^x and alternative base-e form; Limit (1+1/k)^k via logarithms and h=1/k substitution.
PDF page 8 (printed 7): Derivative of log at 1 as limit; Exponentiating limit to obtain e; k=10 approximation remark; Finite-change/market-scale motivation and instantaneous relative-rate identity.

Findings and independent deductions

D006-E01 | confirmed_source_coordinate_error | PDF page(s) 3, 4 | 4^x secant paragraph and Figure 3
The source gives the second secant point as (1,0), including the plotted label at the vertical-axis intercept. This is not a point of y=4^x and gives the wrong stated secant slope.
Replace (1,0) by (0,1) in both locations.
4^0=1 and 4^(-1/2)=1/2; the corrected secant slope is (1-1/2)/(0-(-1/2))=1. The two printed coordinates instead have slope -1/3. The intended inequality M(4)>1 is correct.

D006-E02 | confirmed_source_inverse_identity_error | PDF page(s) 5 | Second boxed natural-log definition
The box reads: if w=ln(x), then e^x=w.
The equivalent exponential statement is e^w=x (for x>0).
At x=1 the printed statement would assert e=0. The first definition box and the subsequent differentiation correctly use the inverse relationship, with e^w=x.

D006-G01 | foundational_proof_gap | PDF page(s) 2, 3, 4, 5 | Definition of M(a), secant comparisons, existence/uniqueness of e
The source assumes that the defining limit M(a) exists, reads convexity/strict slope comparisons from graphs, and infers existence and uniqueness of a base with M(a)=1 without proving the required dependence on a. Continuous real extension alone does not generally imply differentiability.
The argument is a geometric motivation, not a complete existence proof as written. These missing premises can be justified from the continuous exponential laws.
Continuous exponentials are strictly convex: midpoint convexity follows from the arithmetic-geometric mean inequality and continuity upgrades it to convexity. For fixed a>1, convexity bounds secant slopes near 0 and makes their right limit finite; the identity (a^(-h)-1)/(-h)=(a^h-1)/(h*a^h) equates the left limit, giving M(a)>0. For b=2, the strict secant comparisons on [-1,0] and [0,1] give 1/2<M(2)<1. Every a>0 is uniquely a=2^t, continuously in a. Substituting t*h gives M(a)=t*M(2). Thus the unique slope-1 base is e=2^(1/M(2)), lying strictly between 2 and 4. This independent deduction supplies existence, strict monotonicity, and continuity without assuming the later log derivative.

D006-C01 | scope_and_domain_conditions | PDF page(s) 2, 5, 6, 7 | Exponential laws, logs, log product law, logarithmic differentiation
The source explicitly restricts its starting base to a>1, but omits the nonzero rational denominator and several positivity conditions beside log identities.
Take q a positive integer in a^(p/q), ln(x) only for x>0, ln(x1*x2)=ln(x1)+ln(x2) for x1,x2>0, and (ln f)-prime=f-prime/f where f is differentiable and positive on the interval in question.
For a differentiable nonzero function, the corresponding extension is (ln|f|)-prime=f-prime/f locally; plain ln(f) is not real for negative f. The formula (a^x)-prime=ln(a)*a^x also extends to all a>0 (including a=1), though that extension is outside the stated a>1 starting scope.

D006-G02 | implicit_inverse_differentiability_premise | PDF page(s) 5 | Implicit differentiation of ln
The calculation uses differentiability of the inverse function before explicitly justifying it.
Once e^x is differentiable, strictly increasing, and has derivative e^x>0, its inverse ln on (0,infinity) is differentiable.
The inverse difference quotient tends to the reciprocal derivative, yielding (ln x)-prime=1/e^(ln x)=1/x. This supplies an existence premise and does not change the correct final formula.

D006-C02 | example_domain_and_limit_conditions | PDF page(s) 7, 8 | x^x and (1+1/k)^k
The logarithmic x^x derivation is a real-variable calculation on x>0. The limit is taken with k eventually positive.
Use x^x=exp(x ln x) for x>0; its derivative is x^x(ln x+1). For the sequence k in the positive integers, h=1/k approaches 0 from the right.
The two-sided log derivative at 1 supplies the needed right limit. Logarithms of the positive bases are defined, and continuity of exp justifies returning from log-limit 1 to original limit e. The same proof works for real k->+infinity.

D006-A01 | unquantified_approximation_language | PDF page(s) 8 | Remark 1, k=10 gives a pretty good approximation
The qualitative accuracy claim has no numerical tolerance.
The stated k=10 value is 1.1^10=2.5937424601, approximately 0.1245393684 below e, or about 4.58155 percent relative error.
Direct independent numerical evaluation quantifies the remark; the limit formula itself is correct. This is not classified as a false mathematical assertion.

D006-C03 | rate_interpretation_condition | PDF page(s) 8 | Remark 2 and f-prime(t)/f(t)=d/dt ln(f(t))
The prose motivates logs with a finite market drop, whereas the displayed identity is an instantaneous fractional rate.
Assume f(t)>0 and differentiability for the displayed identity. The instantaneous percent rate is 100*f-prime/f; a finite relative change Delta-f/f and finite log change ln(f_new/f_old) are generally different.
For small changes, ln(1+Delta-f/f) is approximately Delta-f/f. The finite examples compare the scale of a 50-point change, not an exact finite-change identity.

D006-S01 | title_body_scope_discrepancy | PDF page(s) 2, 3, 4, 5, 6, 7, 8 | Title versus complete body
Hyperbolic Functions occurs in the lecture title, but no hyperbolic definitions, identities, graphs, or derivatives appear in the seven content pages.
Record body coverage as exponentials, natural logarithms, logarithmic differentiation, and the exponential limit.
This is an observed scope discrepancy, not a missing-page assertion and not grounds to invent supplemental source content.

Technical disposition

Two actual source errors are confirmed: the swapped coordinate in the 4^x secant (prose and Figure 3) and the reversed variables/exponent in the second logarithm-definition box. The intended derivative and limit results are correct. Foundational existence arguments, positivity conditions, approximation language, and the unused hyperbolic title phrase are separately classified. No external research or PROF/learner verdict is included.
