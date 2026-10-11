D007 P1–P6 independent calculations, before teaching or answer access

Reading boundary and identity

Reviewer: /root/technical_d007_r29. This is a technical prompt review, not SASIS, a student performance record, or authoring. The only file read in the author directory is /workspace/scratch/f9c0b7fc7e76/d007-clean-r29-20261011/author/prompts-only.md. Its SHA256 was checked immediately before reading and is 6f1a42e831202d1fc386859bc96f2fa51dae82f5bf3f9c0070ad8210e7278c3d. All six prompts, including both parts of P6, were read in full.

No teaching, hints, proposed answers, author notes, old teaching, or old diagnoses were consulted. Other inputs were the original five-page MIT Lecture 7 source and the specifically recorded baseline passages and PROF requirements from source preparation. Baseline reading remains selected, not complete: original line ranges 1–28, 90–176, and 387–416, plus targeted search results. Full baseline reading by the author and SASIS reader remains a separate obligation. No outside web lookup was required for these elementary deductions.

Each answer below was completed before opening any supplied teaching or solution. The accompanying numeric checks are supplementary, not proofs. Sealing is by a recorded content hash and preserved files; it is not a claim of technical isolation from shared tools or erasure of pretraining. No answers or subject findings are to be sent to the author before the whole document is frozen.

P1

Given q(x)=cosh(2x)=[exp(2x)+exp(−2x)]/2, both exponentials start with plus signs. The two inner derivatives are d(2x)/dx=2 and d(−2x)/dx=−2. Therefore

q'(x)=[2 exp(2x)−2 exp(−2x)]/2
      =exp(2x)−exp(−2x)
      =2 sinh(2x).

The negative contribution arises from differentiating exp(−2x), whose inner derivative is −2. At zero, q'(0)=1−1=0. q and this derivative exist for every real x.

The ordinary identity (cos x)'=−sin x concerns a different function defined through circular trigonometry. It does not impose a negative sign on the derivative of cosh. Here the exponential definition directly gives cosh'=sinh, followed by the inner factor 2. A structural check is that q is even and its derivative is odd: q' is positive for positive x and negative for negative x. This also rules out the erroneous −2 sinh(2x) sign away from zero; checking zero alone would not distinguish the two signs.

P2

Use the quotient rule, with u=sin x, u'=cos x, v=1+cos x and v'=−sin x, all in radians. For v≠0,

F'(x)=[cos x(1+cos x)−sin x(−sin x)]/(1+cos x)²
     =[cos x+cos²x+sin²x]/(1+cos x)²
     =(1+cos x)/(1+cos x)²
     =1/(1+cos x).

The original function excludes 1+cos x=0, namely x=(2k+1)π for integer k. The cancellation is valid only at points where the cancelled factor is nonzero. It cannot assign a derivative to a function that was not defined at the excluded input. The simplified expression also retains the same zero denominator.

For an independent representation check, F(x)=tan(x/2) on the original domain, so F'(x)=(1/2)sec²(x/2)=1/(1+cos x). At x=0, F'(0)=1/2, consistent with sin x≈x and 1+cos x≈2. The derivative is positive everywhere it is defined. Near π, writing x=π+t gives F approximately −2/t and F' approximately 2/t², so the excluded point is not repaired by cancellation.

P3

The point is on the curve because 1²+1·2+2²=7. Treat y as a local differentiable function of x. The product xy has two contributions: (xy)'=1·y+x y'. Consequently,

2x+y+x y'+2y y'=0,
(x+2y)y'=−(2x+y),
y'=−(2x+y)/(x+2y), provided x+2y≠0.

At (1,2), the coefficient divided by is x+2y=1+4=5, which is nonzero. The numerator is −(2+2)=−4. Thus y' at (1,2) is −4/5. The tangent is

y−2=−(4/5)(x−1),

equivalently 4x+5y=14. It contains (1,2) and has the stated slope.

A check independent of the implicit derivative formula uses the local upper solution of the quadratic in y:

y(x)=[−x+sqrt(28−3x²)]/2.

At x=1 this gives y=2. Its derivative is [−1−3x/sqrt(28−3x²)]/2, which at x=1 is [−1−3/5]/2=−4/5. The radicand is 25 at the point, so this local branch is differentiable there. The implicit formula should not be presented as a finite slope where x+2y=0; that restriction is not encountered at the stated point.

P4

Fix a real x and take h→0 through nonzero values, with angles measured in radians. The given addition formula yields

[cos(x+h)−cos x]/h
= [cos x cos h−sin x sin h−cos x]/h
= cos x·[(cos h−1)/h]−sin x·[sin h/h].

The limit variable is h. The chosen evaluation point x remains fixed, so sin x and cos x are finite constants with respect to that limit. The two displayed h-dependent quotients have the supplied finite limits 0 and 1. Applying constant-multiple and sum rules for limits gives

d(cos x)/dx=cos x·0−sin x·1=−sin x.

The minus sign is inherited from the cosine addition formula. This deduction applies to every real x. At x=0 the derivative is zero, and at x=π/2 it is −1; the latter check discriminates the sign. The supplied limits are radian limits, so replacing radians with degree input would change the scaling and would not preserve this calculation unchanged.

P5

On x>0, write y=x^x=exp(x ln x). This representation keeps both appearances of the varying x visible. The inner derivative uses the product rule:

d(x ln x)/dx=1·ln x+x·(1/x)=ln x+1.

The outer exponential derivative therefore gives

y'=exp(x ln x)(ln x+1)=x^x(ln x+1), for x>0.

The same result follows from ln y=x ln x: y'/y=ln x+1 and y=x^x>0. The constant-power rule differentiates x^r while holding r fixed. Substituting r=x only after that differentiation changes the function without accounting for the derivative of its exponent. In the more general positive-base representation exp(r(x) ln x), the inner derivative is r'(x)ln x+r(x)/x. Taking r(x)=x adds the missing ln x term. This is why the naive result x·x^(x−1)=x^x is generally incorrect.

At x=1 both results happen to agree, so that is not a discriminating check. At x=e, the correct derivative is 2e^e, whereas the naive substitution gives e^e. Since x^x>0, the correct derivative changes sign at x=exp(−1): negative below, zero there, positive above. This sign check is consistent with the positive-base domain and is not a claim about a value or derivative at x=0.

P6: rules available before lesson/solution inspection

From the inspected permitted baseline, the relevant rules are the chain and product rules, (arcsin u)' with respect to u equal to 1/sqrt(1−u²) for |u|<1, (arctan x)'=1/(1+x²), (exp u)' with respect to u equal to exp u, and (x²)'=2x. These are available formula premises. The scaled inverse input in (a) and the product nested inside the exponential in (b) require new combinations of those premises. This review records those combinations; it does not claim observed successful recall, later retention, or human transfer.

P6(a)

The outer operation is arcsine and the inner expression is 2x, whose derivative is 2. The real function domain is −1≤2x≤1, or −1/2≤x≤1/2. For the finite derivative use the open interval −1/2<x<1/2.

Let θ=A(x)=arcsin(2x). Its principal range is [−π/2,π/2], and sin θ=2x. Differentiation at interior inputs gives

cos θ·θ'=2.

The identity cos²θ=1−sin²θ=1−4x² supplies the magnitude of cosine. For interior inputs θ lies in (−π/2,π/2), where cos θ>0, so cos θ=+sqrt(1−4x²). Thus

A'(x)=2/sqrt(1−4x²), for −1/2<x<1/2.

At the function-domain endpoints A is defined, but the denominator tends to zero from above and this formula gives no finite derivative there. A'(0)=2, checking the inner scale factor. The derivative is positive throughout the open interval, consistent with the increasing principal arcsine branch. Using a negative square root would contradict that branch.

P6(b)

The outer operation is the exponential and the inner expression is g(x)=x² arctan x. The exponent itself is a product. Its two derivative contributions are

g'(x)=(2x)arctan x+x²[1/(1+x²)].

Therefore

B'(x)=exp(x² arctan x)[2x arctan x+x²/(1+x²)].

Every expression is defined for every real x. At x=1, the exponent is π/4 and the bracket is 2(π/4)+1/2=(π+1)/2. Hence

B'(1)=((π+1)/2) exp(π/4).

The two terms cannot be replaced with the derivative of only one factor. An additional check is that g' is even, since x arctan x is even and x²/(1+x²) is even; it is positive for x≠0 and zero at zero. Consequently B'(0)=0 and B'(x)>0 for x≠0, because the exponential is positive. Evaluating at a negative input is useful for detecting an incorrect sign in the first product term.

Completion boundary

All six prompts and both P6 parts have complete independent answers, including the requested response criteria. The calculations are sealed before any whole-document, hint, or proposed-answer access. No conclusion about the yet-unread teaching's coverage, correctness, usability, SASIS result, or rendering is made here. Next: wait for root to provide the frozen whole teaching and figures, then compare them against this preserved work.
