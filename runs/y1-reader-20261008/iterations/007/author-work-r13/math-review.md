D007 author mathematical review

This is an author audit, independent corroboration of the presentation, not the parent's independent technical review or SASIS. The frozen prompts were sent first; no parent solution was consulted. Exact source page images were used to distinguish primes, grouping, and signs from damaged extraction. Standard-library numerical checks are reproducible with author-math-check.py and reported in math-numerical-checks.json; SymPy was neither used nor claimed available.

M01 Hyperbolic definitions and identity, P008–P014

Let a=e^x and b=e^-x, so ab=1. Then ((a+b)/2)^2-((a-b)/2)^2=ab=1. Differentiating b gives -b; the two linear combinations therefore exchange as stated. Since a,b>0, cosh>0, and the identity implies cosh^2>=1, hence cosh>=1. This verifies the right-branch qualification rather than claiming the full two-branch hyperbola is traced. At x=0, derivatives are 1 and 0. Q1 independent exponential reduction gives H=e^-2x and H'=-2H<0. Direct hyperbolic chain differentiation agrees, including factor 2.

M02 General rules and representation examples, P020–P028

Product/chain rules are baseline premises. For quotient u/v, differentiating v^-1 gives -v'/v^2, so u'/v-uv'/v^2=(u'v-uv')/v^2. Nonzero v is essential. The worked R=x/(1+x^2) has numerator 1+x^2-2x^2=1-x^2 and positive squared denominator. Derivative signs agree with stated intervals and at x=0. Composition checks: sin(x^2) gives cos(x^2)*2x; (sin x)^2 gives 2sin x*cos x. Their distinct outputs confirm the parentheses matter.

Q2 alternate check: F=A B, G=B/A. F'=A'B+AB' with A'=2x, B'=3cos3x. For G, the logarithm-free product form B*A^-1 yields 3cos3x/A-2x sin3x/A^2; bringing to one denominator matches P134. A>0 on R. The author found and repaired only an imprecise verbal description of changing F into G; replacing factor A by 1/A is the exact construction. No mathematical prompt changed.

M03 Source implicit curve, P033–P038

Differentiate y^3+3xy^2=8: 3y^2 y'+3y^2+6xy y'=0. Thus y'=-3y^2/(3y^2+6xy) where denominator is nonzero. Independent route solves for x as a function of nonzero y: x=8/(3y^2)-y/3, hence dx/dy=-16/(3y^3)-1/3. At y=2, x=0 and dx/dy=-1; reciprocal local slope is -1, matching the displayed y-derivative and tangent. On this curve y cannot be zero because it would make 0=8. Denominator failure therefore requires y=-2x, giving x^3=2. The lesson does not claim its quotient works at that point. The condition on local differentiability is explicit rather than importing a general implicit-function theorem.

Q3 independent check uses explicit branches y=+sqrt(5-x^2) and y=-sqrt(5-x^2) on (-sqrt5,sqrt5). Their derivatives are -x/sqrt(5-x^2) and +x/sqrt(5-x^2), giving -1/2 and +1/2 at x=1. At y=0, x=±sqrt5; a hypothetical finite derivative would force 2x=0 in the undivided equation, a contradiction. Circle radius geometry gives a vertical tangent at either point. This is not an inference from division failure alone.

M04 Inverse derivatives and branch signs, P043–P050 and Q4

For y=arcsin x, sin y=x with y in the principal interval. Differentiation gives cos y*y'=1. On the interior cos y>0 and cos^2 y=1-x^2; hence y'=1/sqrt(1-x^2). For arctan, sec^2 y*y'=1 and sec^2y=1+x^2>0. For Q4 arccos, -sin y*y'=1 with 0<y<pi and sin y>0, so derivative is negative reciprocal square root. An independent identity check uses arccos x=pi/2-arcsin x on these branches, yielding the same negative derivative. Domain [-1,1] of the inverse is distinguished from (-1,1) for the finite derivative formula. Q7(a) repeats this derivation as retrieval, not novel transfer.

M05 Difference quotients, P056–P062 and Q5

With x fixed and h nonzero, sine addition transforms the difference quotient into sin x*(cos h-1)/h+cos x*sin h/h. Supplied limits yield cos x. Cosine addition similarly gives cos x*(cos h-1)/h-sin x*sin h/h, yielding -sin x. These are exact algebraic identities before the limit. Units are radians; applying them unchanged to degree-valued trigonometric inputs would miss pi/180. The added review needs no new theorem beyond linear combinations of the supplied limits. It does not substitute a finite small-angle approximation for a limit argument.

M06 Specific derivative families, P067–P077

For tan=sin/cos, numerator is cos^2+sin^2=1 and denominator cos^2. For sec=cos^-1, the outer negative and inner -sin cancel, leaving sin/cos^2=tan sec. Both need cos nonzero. Exponential differentiation takes normalisation limit (e^h-1)/h->1 as an explicitly stated premise and factors e^x out of the difference quotient; no existence proof of e is claimed. This premise is also obtained from baseline e'(0)=1, so it is not an unprovided empirical fact. For ln, e^y=x gives y'=1/e^y=1/x at positive x.

Integer positive power differentiation yields n terms x^(n-1); negative powers use a reciprocal and x nonzero. Rational p/q on x>0: qy^(q-1)y'=p x^(p-1), division is valid because y>0 and q>0, and exponent subtraction p-1-p(q-1)/q=p/q-1 checks the final power. At exponent 0 the derivative vanishes. Domain extension to negative x and zero is not assumed from the positive-x derivation.

M07 Real powers and Q6, P079–P086/P152–P156

For fixed real r and positive x, define/represent x^r as exp(r ln x). Its derivative is exp(r ln x)*r/x=r x^(r-1). Alternate log differentiation: f>0 permits ln f=r ln x; f'/f=r/x; multiply by f. Independent sign/limit probes r=0 and r=-2 give derivative 0 and -2/x^3, respectively; r=2/3 matches the implicit rational calculation. Q6: f=x^sqrt2 yields sqrt2*x^(sqrt2-1), while g=(sqrt2)^x yields g*ln(sqrt2). Since ln(sqrt2)=ln2/2>0, both are increasing on the requested domain, but the factors differ. For x^pi the same constant-exponent rule gives pi*x^(pi-1).

M08 Source final expression and Q7(b), P089–P094/P160–P164

The full source image confirms the exponent is x times tan^-1 x. Writing w=x arctan x gives w'=arctan x+x/(1+x^2), then E'=Ew'. At x=0 the bracket vanishes. An independent check of Q7 uses logarithmic differentiation rather than its displayed quotient route: J>0, ln J=x arctan x-ln(1+x^2). Thus J'/J=arctan x+x/(1+x^2)-2x/(1+x^2)=arctan x-x/(1+x^2). Multiplying by J gives exp(x arctan x)*[(1+x^2)arctan x-x]/(1+x^2)^2, exactly the final expression. The denominator never vanishes. This check discriminates the omitted-denominator-derivative error. At zero J'=0; nonzero asymmetrical numerical samples also agree, so a zero-only check did not conceal a missing sign or term.

Numerical corroboration actually performed

The Python 3 standard-library script used central differences with h=1e-6 at non-symmetric real interior values, avoiding singular endpoints. It checked 71 derivative comparisons across every task's calculational component and important worked formula, plus three hyperbolic identities. All comparisons passed their recorded relative/absolute tolerance; maximum absolute derivative discrepancy was 3.112052837650481e-09. These comparisons corroborate, but do not replace, the exact proofs/domain reasoning above. No human performance or reader understanding follows from them.

Author result and remaining gates

No unresolved author-side mathematical discrepancy was found against the inspected source and stated premises. The source omits useful domain/branch conditions and uses motivational 'anything' language; the lesson supplies conditions and qualifies that language without changing the source formulas. Parent final technical/source review and the separate fresh SASIS remain pending; this record does not pre-approve them.
