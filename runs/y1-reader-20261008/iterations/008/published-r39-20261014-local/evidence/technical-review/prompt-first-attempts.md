Independent prompt-first work, frozen teaching d008-r39-first-delivery

Timing/isolation record: main.md lines 1-532 and all four figure PNGs have been read/visually inspected. No authored hints.md or solutions.md has yet been opened or read. The independent preparation seal was verified unchanged before teaching access. These calculations were made from the retained prompts and main route, checked against the previously sealed source/baseline preparation, before authored help. This is reviewer work, not observed student performance. This file will be sealed before help access.

Attempt A (main 68-72)

Choose basepoint 1. h=0.96-1=-0.04. f(1)=0 and f'(1)=1 give L(x)=x-1 and estimate ln(0.96) approximately -0.04. Positive slope times negative displacement produces negative output change from 0; the logarithm is also negative for an input below 1 by its increasing graph. The identity belongs to L, not ln; an omitted nonlinear residual remains. Main 14-37, 41-65 explicitly supplies the required construction/interpretation. No new premise from help is needed.

Attempt B (main 142-152)

Rewrite g(x)=exp(3x)(1-2x)^(-1/2). Exponential input u=3x gives 1+3x; power input u=-2x and fixed r=-1/2 give 1+x. Their exact product is 1+4x+3x^2; retain 1+4x for the linear model. A real denominator domain containing zero is x<1/2, with |3x| and |2x| small for the model; 1-2x is positive and its square root is nonzero there. g'(0)=4 from the properly constructed derivative-based model. Independent derivative/product check: 3*1+1*1=4. Main 77-93 and 107-139 supply every consequential substitution, domain and coefficient step.

Attempt C (main 381-392)

Let F(x)=exp(-2x)/sqrt(1+x), x>-1. Main 362-375 supplies Q(x)=1-(5/2)x+(27/8)x^2. Write F(x)=Q(x)+E2(x), with E2(x)/x^2 ->0 from main 260-269 because F'' is continuous on an interval around 0 inside x>-1. Subtracting 1 and adding (5/2)x cancels constant and linear parts; for nonzero x division leaves 27/8+E2(x)/x^2 ->27/8. The first-order residual condition E1(x)/x ->0 does not imply E1(x)/x^2 ->0, so the linear model cannot establish this answer. The actual surviving quadratic coefficient would be lost by setting its error to zero.

Attempt D (main 424-436)

(a) Doubling v multiplies z=(v/c)^2 by 4, the leading z/2 by 4 and the added 3z^2/8 by 16. Expansion variable is z, not v. Fixed c and same model conditions matter.

(b) Original z=1.777777777...*10^-10, so original quadratic correction is 1.185185185...*10^-20, below 10^-19. Doubling gives 1.896296296...*10^-19, above 10^-19. This decides whether the term crosses the specified size threshold; it does not certify all uncomputed terms or model error.

(c) v=0.8c gives z=0.64. This is not a small input for the local low-z justification. L=1+0.32=1.32. Q=1.32+(3/8)*0.4096=1.4736. Exact ratio=1/0.6=5/3=1.666666666.... Absolute errors are about 0.3466667 and 0.1930667. Q improves this particular value but still misses substantially. Main 77, 199-230 and 397-421 license the comparison and its limits; no unstated lookup is needed because the exact square root is supplied.

Attempt E (main 477-491)

Let h=t-2 s, with h measured in seconds. L=3 V+(0.4 V/s)h. Q=3 V+(0.4 V/s)h-(0.1 V/s^2)h^2, since square-term coefficient is half F''(2). At t=2.1 s, h=0.1 s: L=3.04 V, Q=3.039 V. Each derivative coefficient times its matching displacement power has volts. The negative second derivative means slope initially decreases as t increases near the basepoint; the negative correction places Q below the tangent at nonzero h. Continuous F'' and its negative basepoint value guarantee negative curvature sufficiently near 2, but do not quantify a full 0.1 s interval. The three values do not guarantee error less than 0.001 V at 2.1 s. Independent counterexample family F(t)=Q(t)+K h^3, K=2 V/s^3, preserves all three specified basepoint values and has continuous second derivative; its error there is 0.002 V. This family is reviewer verification, not an extra required prompt step. Main 20, 235-269, 441-474 supplies model building and absence of a numerical bound.

Attempt F (main 499-523)

(a) L=f(x0)+f'(x0)(x-x0); Q=L+[f''(x0)/2](x-x0)^2. L matches value and first derivative at x0; Q additionally matches second derivative. These are polynomials of degree at most 1 and 2. Conditions for local error properties are differentiability for L and the taught sufficient continuous-second-derivative condition for Q.

(b) H=ln(1+2x)(1+x)^(-1). Log input u=2x gives 2x-2x^2. Reciprocal has u=x,r=-1, giving 1-x+x^2. Product through degree two: 2x +[-2-2]x^2=2x-4x^2. The complete product of these truncated polynomials is 2x-4x^2+4x^3-2x^4. Domain around 0: x>-1/2, which ensures log argument positive and also denominator 1+x>1/2. Local inputs |2x| and |x| are small. An independent exact derivative check gives H(0)=0,H'(0)=2,H''(0)=-8, agreeing with Q's square coefficient -4.

(c) H(x)=2x-4x^2+E2(x), E2(x)/x^2 ->0 on that smooth local domain. Thus [H(x)-2x]/x^2 ->-4. Constant is already zero, linear term cancels, quadratic survives. Main's product construction plus general second-order error statement supplies the bridge.

(d) Sine's square coefficient vanishes because sin''(0)=0; its cubic coefficient is -1/6 from the supplied baseline Maclaurin expansion and main 301. It is not an exact line. For f(x)=7-3x, f'' is zero and L=7-3x=Q exactly at every basepoint: substitution gives 7-3x0-3(x-x0)=7-3x. Here the whole original function is affine, not merely one local coefficient zero.

Prompt adequacy observations before help access

All six labels have identifiable response criteria in the prompt and are supported by earlier main-route/baseline premises. A appears immediately after the first usable result. B changes substituted input and admissible domain; C changes cancellation/order inference; D changes a physical scale/tolerance and leaves the small-parameter regime; E changes from known function formula to local dimensional data; F combines log/reciprocal/product/order/degenerate-case discrimination with later retrieval. No required incidental constant or lookup is missing. These are actual independent operations, not a heading-count pass. Complete-help adequacy and navigation are pending until help and destination are inspected.
