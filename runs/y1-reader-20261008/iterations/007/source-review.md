D007 source technical review

Exam 1 review
Source display title: Lecture 7: Continuation and Exam Review

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/a30756fe9d577184f205b09bc6d6d005_lec7.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec7/
SHA-256: 47316203594d35c47220c7049238045ff0a2ac73ba3292d17107f13d575f3602

All five complete text extractions and original page renders were read/inspected. This includes the hyperbolic continuation, every review formula/condition, and closing examples. There are no figures or diagrams. Hash independently verified. PDF pages 2–5 are printed pages 1–4. PDF skill applied read-only.

Page and figure coverage

PDF page 1 (printed cover): MIT OCW cover, course/term, citation/terms notice.
PDF page 2 (printed 1): Hyperbolic sine/cosine exponential definitions; Both hyperbolic derivatives and comparison with circular cosine derivative; Expanded proof of cosh^2-sinh^2=1; Hyperbola relation in u,v and circle relation for cosine/sine.
PDF page 3 (printed 2): Exam 1 review: sum, constant-multiple, product, quotient, chain rules; Quotient-rule derivation reminder using reciprocal power; Implicit cubic y^3+3xy^2=8; Inverse sine derivative via implicit differentiation.
PDF page 4 (printed 3): Exam-specific derivative list: x^n, inverse sine, inverse tangent, sine, cosine, tangent, secant, exponential, logarithm; Secant derivative derivation; Sine/cosine limit prerequisites and derivative definition; Power rule for real constant r via base e and logarithmic differentiation.
PDF page 5 (printed 4): Closing derivative of exp(x arctan(x)); General exp(uv) chain/product calculation and substitution.

Findings and independent deductions

D007-C01 | parametrization_scope | PDF page(s) 2 | Hyperbolic naming explanation
u=cosh(x), v=sinh(x) satisfies u^2-v^2=1, but it covers only the right branch of that hyperbola. No figure is present.
For real x, u>=1 and v ranges over all real numbers; the other branch has u<=-1. The stated hyperbola equation is correct.
cosh(x)=(e^x+e^(-x))/2>=1. sinh is strictly increasing, has limits +/-infinity, and cosh^2-sinh^2=1. Hence the parameterization covers exactly u=sqrt(1+v^2). The circular parameterization covers the full unit circle.

D007-C02 | review_rule_hypotheses | PDF page(s) 3 | General differentiation formulas and reciprocal rewrite
The compressed review omits local hypotheses beside the formulas.
Use differentiable u and v; c must be constant. The quotient rule and v^(-1) rewrite require v(x) != 0. For the chain rule, u is differentiable at x, f is differentiable at u(x), and the composition is locally defined.
Continuity of v ensures local nonvanishing at a point where v(x) != 0. Applying product and chain rules to u*v^(-1) yields u-prime/v-u*v-prime/v^2, equal to the printed quotient rule.

D007-C03 | implicit_derivative_domain_and_exception | PDF page(s) 3 | y^3+3xy^2=8
The final expression divides by 3y^2+6xy without stating its nonzero condition or the local-function assumption.
The source formula applies on differentiable local y(x) branches where 3y^2+6xy != 0. The only real exceptional curve point is (x,y)=(cuberoot(2),-2*cuberoot(2)), where the regular curve has a vertical tangent and no finite dy/dx.
The equation excludes y=0. A zero denominator forces y+2x=0; substitution gives y^3=-16 and x=-y/2=cuberoot(2). Since F_x=3y^2 != 0, x is locally a differentiable function of y. Independently x=8/(3y^2)-y/3 has dx/dy=-16/(3y^3)-1/3=0 at this point. Away from it, the printed derivative simplifies to -y/(y+2x).

D007-C04 | inverse_branch_and_endpoint_conditions | PDF page(s) 3, 4 | Inverse-sine calculation and inverse-tangent review notation
The inverse-sine derivation replaces cos(y) with the positive square root, which requires the principal branch; sin^(-1) is inverse notation here, not the reciprocal.
Use arcsin range [-pi/2,pi/2], with derivative 1/sqrt(1-x^2) only for -1<x<1. At x=+/-1 there is no finite derivative. Use arctan range (-pi/2,pi/2), whose derivative 1/(1+x^2) holds for every real x.
For arcsin interior values, cos(y)>0 and cos^2(y)=1-x^2. For arctan, sec^2(y)=1+x^2>0. Both inverse derivatives require existence on these branches, justified by the nonzero forward derivatives there.

D007-C05 | review_domains_and_angular_convention | PDF page(s) 4 | Specific derivative checklist, sec derivative, and trigonometric limits
The review list and displayed secant derivative do not repeat domain restrictions or the radian convention.
The sine/cosine limits and derivative formulas use radians. tan and sec require cos(x) != 0; ln requires x>0. Sine, cosine, and e^x are defined and differentiable for all real x. Integer power domains depend on whether the exponent is negative; the real-power discussion has x>0.
Differentiating 1/cos(x) gives sin(x)/cos^2(x)=tan(x)sec(x) wherever cos(x) != 0. tan-prime(x)=sec^2(x), sine-prime=cosine, cosine-prime=-sine, exp-prime=exp, and log-prime=1/x agree with their corresponding reviewed rules and domains. A derivative-definition limit is an existence requirement, not automatic for every function.

D007-C06 | real_power_and_logarithmic_domain | PDF page(s) 4 | Both derivations of d(x^r)/dx
Both proofs use ln(x) and require positive x; r must be a constant real number. Neither proof establishes a uniform real-valued formula for arbitrary negative x or behavior at x=0.
For x>0 define x^r=exp(r ln x); then the displayed derivative r*x^(r-1) follows. Treat integer/rational extensions and endpoints separately where defined. Logarithmic differentiation with ln(f) requires f>0.
exp(r ln x) is differentiable and its derivative is exp(r ln x)*r/x. Thus this route also supplies existence, while the log-differentiation route computes the same derivative under its assumptions. If r varied with x an additional r-prime(x)*ln(x) term would be needed.

D007-C07 | closing_example_conventions | PDF page(s) 5 | exp(x tan^(-1)(x))
tan^(-1) denotes arctan on its usual branch in this calculation. The composition and final derivative have no real domain singularity.
For all real x, the derivative is exp(x arctan(x))*(arctan(x)+x/(1+x^2)).
The product derivative of x*arctan(x) is arctan(x)+x/(1+x^2); multiplying by the outer exponential gives the displayed result. The source rhetoric about differentiating anything is not a theorem asserting every function has a derivative.

D007-S01 | actual_packet_scope | PDF page(s) 2, 3, 4, 5 | Queue label versus complete source body
The queue label is Exam 1 review; the PDF itself begins with a continuation on hyperbolic sine/cosine and later adds the real-power derivation and closing composite example.
All these portions belong to this original source packet and were included in this audit, not just the section headed Exam 1 Review.
The four content pages are complete and consecutively numbered 1–4; there are no figures or diagrams in this packet.

Technical disposition

No incorrect displayed derivative or algebraic identity was found. The source compresses several hypotheses and domain/branch restrictions; these are recorded separately from source formula errors. The hyperbola parameterization covers the right branch, and the implicit cubic has one exceptional vertical-tangent point. No external research was needed. This is a source-only report without a PROF or learner verdict.
