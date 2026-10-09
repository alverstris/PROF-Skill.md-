D013 independent prompt-only calculations, root

These calculations were completed after reading only the six exact prompts, before seeing or receiving authored hints/solutions or a solved learner document. They are technical reviewer work, not SASIS or evidence of student performance.

P1. A polynomial is continuous on [0,2] and differentiable on (0,2). The secant slope is (8-0)/2=4. Derivative 3c²=4 gives c=±2/√3; only 2/√3 is in (0,2). The tangent there is parallel to the endpoint secant. c≈1.1547 is not the midpoint 1. The negative root is excluded by the required interval.

P2. q(0)=0,q(1)=2, so the secant slope is 2. Every c in (0,1) has q′(c)=1. No required c exists. The left limit at 1 is 1, different from q(1)=2; endpoint continuity on [0,1] fails. Interior differentiability does not control a separately assigned endpoint value, so it does not restore the theorem.

P3. L(x)=1+2(x-1)=2x-1. At x=1.4=7/5, L=9/5=1.8 while f=49/25=1.96, signed error=4/25=0.16. The exact identity requires (49/25-1)/(2/5)=12/5=2c, hence c=6/5=1.2. Using c gives the exact secant slope; using a=1 fixes tangent slope 2, giving a local approximation, and the computed nonzero error distinguishes the claims. Both statements are true under their different meanings.

P4(a). For arbitrary 0<a<b, -ln x is continuous on [a,b], differentiable on (a,b), derivative -1/x. MVT yields u(b)-u(a)=-(b-a)/c<0 with a<c<b and c>0. Thus strictly decreasing on the whole positive interval. (b) k(-1)=0≠1=k(1): not constant on its disconnected domain. k is not defined at 0, so it is not a continuous function on [-1,1], nor differentiable throughout (-1,1). Every interval wholly within either component does meet the hypotheses, proving it constant separately on (-∞,0) and (0,∞).

P5. Exponential positivity implies eˣ is strictly increasing, so eˣ<1 for x<0. R₁′=eˣ-1<0 on (-∞,0), R₁(0)=0. MVT on [x,0] gives R₁(0)-R₁(x)=R₁′(c)(0-x)<0, so R₁(x)>0. Thus eˣ>1+x also for negative x. R₂′=R₁>0 for negative x; similarly R₂(0)-R₂(x)>0, hence R₂(x)<0: eˣ<1+x+x²/2 on x<0. Both bounds become equality at zero. These are derivative-sign proofs for all negative x, not sampled numerical guesses.

P6(a). For a<b, continuous f:[a,b]→R and differentiable f on (a,b), some c∈(a,b) satisfies f′(c)=(f(b)-f(a))/(b-a). It need not be unique (an affine function supplies every interior c) and is not generally known beforehand. (b) ln t on [1,1+h] is continuous/differentiable because h>0 keeps the interval positive. MVT yields ln(1+h)=h/c with 1<c<1+h. Reciprocals reverse the strict positive order: 1/(1+h)<1/c<1. Multiply by h>0 to obtain h/(1+h)<ln(1+h)<h. (c) Let G(x)=F(x)-2x. G′=0 on R, a connected interval, and differentiability ensures continuity on every finite closed subinterval. MVT between 0 and any x (reverse order when x<0) gives G(x)=G(0)=3. Thus unique F=2x+3; its derivative is 2 and F(0)=3.
