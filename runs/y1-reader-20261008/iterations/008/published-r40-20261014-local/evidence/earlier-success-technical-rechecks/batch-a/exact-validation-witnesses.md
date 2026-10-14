# Independent exact-value validation witnesses

This is a bounded technical recheck of the exact accepted Markdown identities in `identities.json`. The complete three Markdown files were read to inventory direct/independent validation claims. Exact fractions and derivative limits are checked exactly; no new rounded-decimal requirement is imposed on a symbolic check. This is not a blinded task attempt, a SASIS reading, or evidence of learner understanding.

## D003 v1

- L55–58, origin derivatives: the learner-facing sine quotient is `sin(h)/h`, with limit 1. For cosine, `(cos(h)-1)/h = -sin(h/2)*(sin(h/2)/(h/2))`, whose factors tend to 0 and 1. Thus the stated values 1 and 0 follow using the explicitly supplied radian sine limit. Neither quotient requires a value at h=0. L69–79's general formulas give the same two values on substitution; the values at pi/3 are respectively 1/2 and -sqrt(3)/2.
- L127, counterexample to the product-of-derivatives rule: for u=v=x, the actual product x^2 has difference quotient h at x=0, hence derivative 0; u'v'=1. The exact disagreement is real and is labelled an anticipated wrong rule. The separate x*sin(x) example gives sin(pi)+pi*cos(pi)=-pi, despite a zero function value.
- L191–197, division check of q=(x^2+1)/(x+1): multiplication verifies `(x-1)(x+1)+2=x^2+1`. On x!=-1, q=x-1+2/(x+1), giving q'=1-2/(x+1)^2. A common denominator gives `(x^2+2x-1)/(x+1)^2`, identical to the printed quotient-rule result. At x=1 this is 1-2/4=1/2, matching the printed 2/4=1/2. This check preserves the excluded input -1.
- L271–275, direct extension derivative: q=(x^2-1)/(x-1) equals x+1 only on x!=1. Q additionally has Q(1)=2, so it is x+1 everywhere. Its quotient at 1 is `(Q(1+h)-Q(1))/h=((2+h)-2)/h=1` for every nonzero h. Q'(1)=1 follows exactly; the original q'(1) remains undefined because q(1) is missing.
- L303–315, alternate F derivative: on F's domain, `cos(x)*(1+cos(x))+sin(x)^2=1+cos(x)`, so F'=1/(1+cos(x)). At pi/3 this is 2/3, and at zero 1/2. Independently, F(0)=0 and F(h)/h=`(sin(h)/h)/(1+cos(h))` tends to 1/2. The denominator tends to 2, so division is legal. G(0) is undefined; replacing it by an invented value would be invalid. For sufficiently small nonzero h, G(h)=F(h), which does allow `[G(h)-F(0)]/h` with the same limit. The text expressly makes this distinction.

Ordinary exact decimal arithmetic was also recomputed: L47 gives 3(0.2)-0.5=0.1 V/s; L257 gives 2(0.30)-0.40=0.20 V/s; L264 gives (-0.2)(4)+3(0.5)=0.7 m^2/s. These are worked answers, not newly classified independent-decimal checks.

## D005 v2

- L137–144, direct zero derivative for w=x^(5/3): using the real cube root, put r=cuberoot(h), so h=r^3 and w(h)=r^5. For nonzero h the actual derivative quotient is r^5/r^3=r^2, tending to 0 from either side. w(0)=0 is defined. Thus the printed w'(0)=0 follows without applying the earlier positive-input division argument at zero.
- The related changed zero checks at L239–247 retain the different conclusions: for u=x^(4/3), the quotient is r^4/r^3=r -> 0; for v=x^(1/3), it is r/r^3=1/r^2 -> +infinity. Hence u'(0)=0 and v has no finite derivative there. Infinity is not assigned as a real derivative value.
- L170's arctangent derivative at zero is 1/(1+0^2)=1. The inverse proof has a nonzero tan derivative at the corresponding angle 0. The ordinary paired-input examples also agree exactly: circle slope at (3/5,-4/5) is 3/4; source cubic slope at (0,-1) is -1/3; Q2's different curve gives +1/3; Q4 gives g(5)=2 and g'(5)=-1/3; Q5 gives G(1+pi/4)=1 and G'=2/3 because F'(1)=3/2. These are supplementary exact checks, not decimal validation claims.

No rounded decimal is presented as a direct/independent numerical validation in this accepted file.

## D006 r13-candidate1-v3

- L176, derivative check for ln(1+x^2) at zero: the stated derivative is 2x/(1+x^2), which evaluates to 0. An independent defining-quotient route is `ln(1+h^2)/h = h*[ln(1+h^2)/h^2]`; the bracket tends to the derivative of ln at 1, namely 1, and h tends to zero. This proves zero using the already established log derivative. Symmetry is only a consistency observation, as in the text.
- L198, slope-characterisation consistency: for a>0, `a^x=exp(x*ln(a))`, so the derivative at x=0 is ln(a). Therefore M(a)=ln(a), continuous and strictly increasing, and M(a)=1 only at a=e. This is symbolic and consistent with the explicitly adopted existence premise; no numerical construction of e is attributed to the pictures.
- L551's A1 slope is exactly 2 exp(2*(1/2)-1)=2. L616's A3 slope is exactly 0 at x=0 because both derivative terms vanish. The document itself states that this zero-input evaluation does not discriminate omission of the changing-exponent term. Independently rewriting y as exp(x^2 ln(1+x)) yields the whole printed derivative, including `2x ln(1+x)` and `x^2/(1+x)` on x>-1. A zero-only check is not credited with validating that full formula.
- L639–647 gives log limit -6 and original positive limit exp(-6), with h=-2/k -> 0 from below. No decimal for exp(-6) is printed or required.

The seven actual final numerals in the requested ordinary approximation blocks are mapped individually to formulas, inputs, units, 70-digit computations and their exact printed lines in `numeric-final-value-witnesses.json`. All seven match nearest rounding at the displayed precision. No finite-difference calculation is substituted for the exact-limit checks above.
