Differentials and antiderivatives

Reading route. Read L1–L8 in order and pause at the numbered attempts. P7 is a later return to the ideas. The hints H1–H7 are grouped after the lesson; complete solutions S1–S7 follow all the hints. Use the matching number to find help, and stop before the solutions if you want another attempt. Basic derivatives, algebra and elementary integration are assumed. The purpose here is to connect those familiar operations to differential notation, choose the correct reverse-chain factor, and preserve the interval on which an answer makes sense.

L1. Two different kinds of change

Suppose $`y=f(x)`$ is differentiable at a chosen base input $`a`$. Move the input from $`a`$ to $`a+h`$. The actual changes are

$$
\Delta x=h,\qquad \Delta y=f(a+h)-f(a).
$$

The derivative $`f'(a)`$ is the limiting value of $`\Delta y/h`$ as nonzero $`h`$ approaches zero. Thus, for small $`h`$, the slope at the base gives the linear estimate

$$
\Delta y\approx f'(a)h,\qquad f(a+h)\approx f(a)+f'(a)h.
$$

Here $`\approx`$ means an approximation, not equality. Smallness is relative to how the particular function changes near the base; this formula alone gives no guaranteed error for an arbitrary chosen step.

Differential notation names the input step and its corresponding tangent-line change:

$$
dx=h,\qquad dy=f'(a)\,dx.
$$

The second equality is the definition of $`dy`$ at this base. It is exact. The approximation is $`\Delta y\approx dy`$. The tangent passes through $`(a,f(a))`$ with slope $`f'(a)`$, so its value at input $`a+dx`$ is exactly $`f(a)+dy`$. Both changes can be negative. If input and output have units, $`f'(a)`$ has output units per input unit, and multiplying by $`dx`$ gives the output units of $`dy`$.

The lecture's compact form $`dy=f'(x)dx`$ uses $`x`$ for the base. Our $`a`$ makes explicit where the derivative is evaluated. For nonzero $`dx`$, the quotient of these defined differentials is exactly $`dy/dx=f'(a)`$, whereas the actual finite-change quotient $`\Delta y/\Delta x`$ generally only approximates that derivative. If $`dx=0`$, the definition still gives $`dy=0`$; do not divide these two zeros to find a derivative.

For example, let $`f(x)=x^2`$, $`a=2`$ and $`dx=0.1`$. Then $`dy=2(2)(0.1)=0.4`$, and the tangent estimate is $`4+0.4=4.4`$. Direct evaluation gives $`f(2.1)=4.41`$ and $`\Delta y=0.41`$. Expanding before inserting numbers explains the discrepancy:

$$
(2+h)^2-2^2=4h+h^2,\qquad dy=4h.
$$

The linear estimate omits $`h^2`$. Reducing a nonzero $`|h|`$ reduces this omitted term relative to the retained term: their magnitude ratio is $`|h|/4`$. This calculation supports the approximation here; it does not make finite changes identical to differentials.

P1. For $`y=x^2`$, take base $`x=3`$ and $`dx=-0.1`$. Find $`dy`$, the tangent estimate of the new $`y`$, and the exact $`\Delta y`$. State which equality is exact and why the two changes differ. A successful response preserves the signs and distinguishes a differential from the actual change. Help: H1; full solution: S1.

L2. Three descriptions of the same cube-root estimate

To estimate $`65^{1/3}`$, use $`f(x)=x^{1/3}`$ near the convenient base $`a=64`$. Here $`f(64)=4`$ and

$$
f'(x)=\frac13x^{-2/3},\qquad f'(64)=\frac{1}{3\cdot16}=\frac1{48}.
$$

The tangent-line description gives

$$
f(65)\approx f(64)+f'(64)(65-64)=4+\frac1{48}\approx4.02083.
$$

In differential notation the same calculation reads $`dx=1`$, $`dy=dx/48=1/48`$, and $`f(65)\approx4+dy`$. Notice that $`1/48`$ is the estimated change, not the whole new value. For $`64.1^{1/3}`$, the base and slope stay the same while $`dx=0.1`$, giving $`4+1/480\approx4.002083`$.

The binomial description first factors out the convenient base:

$$
(64+h)^{1/3}=4\left(1+\frac h{64}\right)^{1/3}.
$$

Set $`u=h/64`$. This is the relative, dimensionless change inside the brackets, not the original change $`h`$. The familiar first-order binomial approximation $`(1+u)^r\approx1+ru`$ gives

$$
4\left(1+\frac h{64}\right)^{1/3}
\approx4\left(1+\frac13\frac h{64}\right)
=4+\frac h{48}.
$$

For $`h=1`$ this is again $`4+1/48`$. All three methods use the same linear term; agreement between them is not three independent guarantees of accuracy. The original factorisation is exact; truncating the binomial expansion or replacing the curve by its tangent introduces the approximation. We retain $`\approx`$ where the lecture's worked lines sometimes print $`=`$.

P2. Estimate $`63.7^{1/3}`$ using base $`64`$. Write both the differential construction and the corresponding small-parameter binomial expression; show that the two estimates agree. Identify the step that introduces approximation. A successful response maps an absolute input change to a dimensionless relative one. Help: H2; full solution: S2.

L3. Reversing the question

A differential starts with a function and predicts its linear change. An antiderivative starts with a derivative and asks which function could have produced it. These are different questions: $`dy=f'(a)dx`$ does not turn an approximate finite change into an exact one, while checking $`F'(x)=f(x)`$ establishes an exact antiderivative relation at every input in the stated interval.

L4. Reading an indefinite integral

An antiderivative $`F`$ of $`f`$ on an interval is a differentiable function satisfying $`F'(x)=f(x)`$ there. The expression

$$
\int f(x)\,dx=F(x)+C
$$

asks for the family of such functions. The integral sign asks for antidifferentiation; $`f(x)`$ is the integrand; $`dx`$ specifies the variable; and $`C`$ is an arbitrary additive constant, fixed as $`x`$ varies. There are no endpoint bounds here. To construct this notation from $`F'=f`$, write the derivative on the integrand side and the original function plus $`C`$ on the other side. Equivalently, $`dF=f(x)dx`$ expresses the same derivative using differentials. For instance, $`(-\cos x)'=\sin x`$, so

$$
\int\sin x\,dx=-\cos x+C.
$$

The minus sign is essential because differentiating $`\cos x`$ gives $`-\sin x`$. Differentiating a proposed answer is our basic check.

The lecture's other standard forms are

$$
\int x^n\,dx=\frac{x^{n+1}}{n+1}+C\quad(n\ne-1),
$$

$$
\int\frac{dx}{x}=\ln|x|+C,\qquad
\int\sec^2x\,dx=\tan x+C,
$$

$$
\int\frac{dx}{\sqrt{1-x^2}}=\arcsin x+C,\qquad
\int\frac{dx}{1+x^2}=\arctan x+C.
$$

In a numerator, $`dx`$ without a preceding function means $`1\,dx`$. The power rule applies on real intervals where its terms are defined and differentiable; $`n=-1`$ is excluded because division by $`n+1`$ would divide by zero. Its answer instead comes from the logarithmic rule. For $`1/x`$, use an interval avoiding zero; for $`\sec^2x`$, avoid zeros of $`\cos x`$. The arcsine formula requires $`-1\lt x\lt1`$, and the arctangent formula holds on the whole real line. The source's $`\sin^{-1}x`$ and $`\tan^{-1}x`$ mean inverse functions, here written arcsine and arctangent, not reciprocals. The inverse-function derivatives check these last two formulas directly.

Absolute value in the logarithmic answer matters. For $`x\gt0`$, $`\ln|x|=\ln x`$ and its derivative is $`1/x`$. For $`x\lt0`$, $`|x|=-x\gt0`$, so the chain rule gives

$$
\frac d{dx}\ln|x|=\frac d{dx}\ln(-x)
=\frac1{-x}(-1)=\frac1x.
$$

The logarithm's input stays positive on both branches. Nothing here supplies a value at zero. This is the verification of the logarithmic formula, though the lecture calls it “Property 2” rather than its listed item 3.

L5. Why all answers differ only by a constant

Adding $`C`$ preserves a derivative because $`C'=0`$. Why does this describe every antiderivative? We need the interval condition as well as differentiation rules.

Continuity here means that function values approach the value at a point as the input approaches that point, using a one-sided approach at an endpoint. We use the mean value theorem as an established theorem: if $`H`$ is continuous on $`[a,b]`$ and differentiable on $`(a,b)`$, with $`a\lt b`$, some $`c`$ between them satisfies

$$
H(b)-H(a)=H'(c)(b-a).
$$

It connects the net change to a derivative at some intermediate input. The point need not be known. The conditions and statement are supplied here, so no previous lecture is required. [MIT's introduction to the theorem](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/e880603ec136cc8ebaa68c7d72c22024_MIT18_01SCF10_Ses34a.pdf), page 1, gives this result.

If $`H'=0`$ throughout an interval, apply the theorem between any two of its points. Differentiability implies continuity there: a finite limiting difference quotient, multiplied by an input change tending to zero, gives an output change tending to zero. Thus $`H(b)-H(a)=0`$. Every two values agree, so $`H`$ is constant.

Now let $`F'=f`$ and $`G'=f`$ on the same interval. Then

$$
(G-F)'=f-f=0.
$$

The result just established makes $`G-F=C`$ on that interval; equivalently, $`G=F+C`$. This is an additive constant, not a multiplicative factor. On separated intervals the constants may be chosen independently: a derivative condition does not connect points across a hole in the domain.

For a concrete comparison, two answers to the same source example are

$$
A(x)=\frac12\sin^2x,\qquad B(x)=-\frac12\cos^2x.
$$

The chain rule gives $`A'=\sin x\cos x`$ and $`B'=\sin x\cos x`$. Also

$$
A(x)-B(x)=\frac12(\sin^2x+\cos^2x)=\frac12.
$$

Thus $`A=B+1/2`$. The two families $`A+C_A`$ and $`B+C_B`$ coincide, but they represent the same particular function when $`C_B=C_A+1/2`$, not when their constants are forced to have the same value. A supplied function value selects that particular function.

P3. A function $`H`$ is $`0`$ for $`x\lt0`$ and $`5`$ for $`x\gt0`$; it is not defined at $`0`$. Its derivative is $`0`$ everywhere in its domain. Does this contradict the claim that a function with zero derivative on an interval is constant? Explain by identifying the domain condition. A successful response says why a single constant need not span two disconnected intervals. Help: H3; full solution: S3.

L6. Substitution expresses a reversed chain rule

If $`u=g(x)`$, then $`du=g'(x)dx`$. The useful object to replace in an integral is the entire product $`g'(x)dx`$. This rule is justified by the chain rule: whenever $`A'(u)=q(u)`$,

$$
\frac d{dx}A(g(x))=q(g(x))g'(x),\qquad
\int q(g(x))g'(x)\,dx=A(g(x))+C.
$$

Reading from left to right, identify an inner expression and look for its derivative as a factor. Building an answer in the other direction, find an antiderivative in $`u`$, restore $`u=g(x)`$, and differentiate the resulting whole function to check all factors and signs. Differential notation helps organise this replacement; it is not permission to discard unmatched factors.

For the lecture's integral

$$
\int x^3(x^4+2)^5\,dx,
$$

choose $`u=x^4+2`$ because its derivative is $`4x^3`$, matching the outside factor up to the constant $`4`$. Hence $`du=4x^3dx`$, or $`x^3dx=du/4`$. Replace both the inner power and that whole factor:

$$
\int x^3(x^4+2)^5\,dx
=\frac14\int u^5\,du
=\frac{u^6}{24}+C
=\frac{(x^4+2)^6}{24}+C.
$$

The check differentiates the outer sixth power and then the inner expression:

$$
\frac d{dx}\left(\frac{(x^4+2)^6}{24}\right)
=\frac6{24}(x^4+2)^5(4x^3)=x^3(x^4+2)^5.
$$

The factor $`1/24`$ accounts for both the outer power and the inner derivative. Expanding the polynomial and integrating term by term would also work, but substitution keeps the repeated expression together.

L7. Guess, differentiate, adjust

“Advanced guessing” in the lecture means recognising a possible outer function and checking it by differentiation. A constant mismatch can be repaired by a constant multiplier. A mismatch depending on $`x`$ cannot be repaired that way.

For $`\int x/\sqrt{1+x^2}\,dx`$, write the integrand as $`x(1+x^2)^{-1/2}`$. The power suggests $`(1+x^2)^{1/2}`$. Its derivative is

$$
\frac12(1+x^2)^{-1/2}(2x)=\frac{x}{\sqrt{1+x^2}},
$$

so the answer is $`\sqrt{1+x^2}+C`$ for real $`x`$. Equivalently, $`u=1+x^2`$ replaces $`x\,dx`$ by $`du/2`$. The $`1/2`$ cancels the $`2`$ from integrating $`u^{-1/2}`$.

For $`\int e^{6x}\,dx`$, the guess $`e^{6x}`$ differentiates to $`6e^{6x}`$. Divide the guess by $`6`$:

$$
\int e^{6x}\,dx=\frac16e^{6x}+C.
$$

For $`\int xe^{-x^2}\,dx`$, the guess $`e^{-x^2}`$ differentiates to $`-2xe^{-x^2}`$. Multiplying by $`-1/2`$ repairs that factor:

$$
\int xe^{-x^2}\,dx=-\frac12e^{-x^2}+C.
$$

This answer applies to the integrand with the outside $`x`$. Removing that $`x`$ changes the pattern. The earlier sine-cosine example likewise admits two choices of inner function: $`u=\sin x`$ gives $`du=\cos x\,dx`$, while $`u=\cos x`$ gives $`du=-\sin x\,dx`$. Integrating $`u`$ or $`-u`$ produces exactly the two forms compared in L5.

P4. Find an antiderivative $`F`$ of $`x^2(x^3+2)^5`$ with $`F(0)=0`$. Then assess the separate proposal that $`-e^{-x^2}/2`$ is an antiderivative of $`e^{-x^2}`$. Differentiate the proposal and say exactly what integrand it does match. A successful response chooses or adjusts the inner derivative and uses a condition without treating every exponential as the same pattern. Help: H4; full solution: S4.

L8. A logarithm inside a logarithm

Consider the final source example

$$
\int\frac{dx}{x\ln x}.
$$

For a real integrand, $`\ln x`$ requires $`x\gt0`$, and its position in the denominator further requires $`\ln x\ne0`$, hence $`x\ne1`$. We work on either $`(0,1)`$ or $`(1,\infty)`$.

Choose $`u=\ln x`$, because $`du=dx/x`$. Reading the original integrand as $`(1/\ln x)(dx/x)`$ displays the two substitutions:

$$
\int\frac{dx}{x\ln x}
=\int\frac{du}{u}
=\ln|u|+C
=\ln|\ln x|+C.
$$

The inner $`\ln x`$ is evaluated first; absolute value then makes it positive; the outer logarithm is taken last. If $`x\gt1`$, this simplifies to $`\ln(\ln x)`$. If $`0\lt x\lt1`$, it becomes $`\ln(-\ln x)`$, and its derivative is

$$
\frac1{-\ln x}\left(-\frac1x\right)=\frac1{x\ln x}.
$$

For $`x\gt1`$, differentiation gives $`(1/\ln x)(1/x)`$ directly. Thus $`\ln|\ln x|`$ works on both intervals, with an independent constant allowed on each. The source assumes only $`x\gt0`$ but prints $`\ln(\ln x)`$: that expression actually requires $`x\gt1`$. Keeping the absolute value and excluding $`1`$ repairs the stated range.

P5. Find $`F`$ on $`0\lt x\lt1`$ such that $`F'(x)=1/[x(\ln x)^2]`$ and $`F(e^{-1})=0`$. State the domain of your formula and verify its derivative. A successful response lets the changed power of $`\ln x`$ determine the primitive, without treating a negative $`\ln x`$ as automatically invalid. Help: H5; full solution: S5.

P6. Write the function with derivative $`\sin x\cos x`$ and value $`0`$ at $`x=\pi/2`$ in each form $`A(x)=\sin^2x/2+C_A`$ and $`B(x)=-\cos^2x/2+C_B`$. Determine both constants, show the expressions agree, and explain why their constants differ. A successful response distinguishes the same family from identical constants in two representations. Help: H6; full solution: S6.

P7. Later, with the explanations covered: (a) for $`y=\ln x`$ estimate $`y`$ at $`x=1.04`$ from $`x=1`$ and state why your result is approximate; (b) find a function $`J`$ with $`J'(x)=\cos(3x)`$, $`J(0)=2`$ and check it exactly; (c) a classmate claims $`\ln(\ln x)`$ is an antiderivative of $`1/(x\ln x)`$ on every $`x\gt0`$. Give the real intervals on which the integrand is defined, repair the formula and explain the role of absolute value. A successful response discriminates finite-change approximation from exact recovery of a function and retains domain conditions. Help: H7; full solution: S7.

Returning tomorrow, or after another study session, is one adjustable way to use P7; it is not an optimal schedule guaranteed for everyone. Recalling the differential/antiderivative distinction and domain rule is retrieval. Applying them to the changed logarithmic and trigonometric cases checks transfer. If a step stalls, keep the part you can establish and use the matching hint.

Source note. This lesson covers the cover and all four printed pages of MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, [Lecture 15: Differentials and Antiderivatives](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/c07ab6e13cf8684dd98b2650b64672fb_lec15.pdf). The cube-root and integral examples retain its mathematical content, with the approximation and domain corrections identified above. P1–P7 are generated practice, not quoted exam questions. The supplemental mean value theorem statement is linked at L5.

Hints. Stop here if you want to attempt the questions without help. All hints come before any complete solution.

H1. Expand $`(3+h)^2-9`$ before setting $`h=-0.1`$. Compare its term proportional to $`h`$ with the derivative-based change.

H2. The actual input change is $`63.7-64`$, while the change inside $`(1+u)^{1/3}`$ is that number divided by $`64`$. Use the same signed change in both representations.

H3. Try choosing one negative and one positive endpoint. Does the closed interval between them stay within the domain of $`H`$?

H4. Set $`u=x^3+2`$ and replace $`x^2dx`$ as a whole. After returning to $`x`$, use $`F(0)=0`$ to find the constant. For the separate proposal, retain the derivative of $`-x^2`$ when differentiating the exponential.

H5. With $`u=\ln x`$, the integrand becomes $`u^{-2}du`$, not $`u^{-1}du`$. Negative nonzero $`u`$ is permitted for a reciprocal power. At the given input, $`u=-1`$.

H6. At $`\pi/2`$, sine is $`1`$ and cosine is $`0`$. Determine each constant independently, then use $`\sin^2x+\cos^2x=1`$ to compare the full expressions.

H7. For (a), start from $`f(1)`$, $`f'(1)`$ and $`dx`$. For (b), differentiating $`\sin(3x)`$ produces an extra constant factor. For (c), check both the input to the inner logarithm and the denominator before checking the input to the outer logarithm.

Complete solutions. These follow all the hints. Match the solution number to the original prompt; after reading a repair, return to that prompt and reproduce the decision that was missing.

S1. The base derivative is $`f'(3)=6`$, so by definition $`dy=6(-0.1)=-0.6`$. The tangent estimate of the new value is $`9-0.6=8.4`$. Direct evaluation gives $`(2.9)^2=8.41`$, so the exact change is $`\Delta y=8.41-9=-0.59`$. In general, $`(3+h)^2-9=6h+h^2`$: the omitted $`h^2=0.01`$ accounts for the discrepancy. The differential equality $`dy=f'(3)dx`$ is exact, while $`\Delta y\approx dy`$ is approximate. Both changes are negative; the true decrease is slightly smaller in magnitude. Returning to P1, check that you added the differential to the old value rather than reporting it as the new value.

S2. Set $`dx=63.7-64=-0.3`$. At base $`64`$, $`dy=dx/48=-0.00625`$, giving $`63.7^{1/3}\approx4-0.00625=3.99375`$. The matching binomial form is

$$
63.7^{1/3}=4\left(1-\frac{0.3}{64}\right)^{1/3}
\approx4\left(1-\frac{0.3}{3\cdot64}\right)=3.99375.
$$

Factoring out $`64`$ is exact. Replacing the bracketed power by its first two binomial terms introduces the approximation, just as replacing the curve by its tangent does in the differential approach. Using $`-0.3`$ directly as the binomial parameter would lose the division by the base.

S3. There is no contradiction. On $`(-\infty,0)`$, the function is the constant $`0`$; on $`(0,\infty)`$, it is the constant $`5`$. Its complete domain is the union of these intervals, not one interval. A closed interval joining a negative point to a positive point contains $`0`$, where $`H`$ is undefined, so the mean value theorem's conditions fail there. Zero derivative fixes a constant on each connected interval, without requiring the two constants to agree.

S4. Choose $`u=x^3+2`$ and $`du=3x^2dx`$. Therefore

$$
F(x)=\frac13\int u^5\,du
=\frac{(x^3+2)^6}{18}+C.
$$

At $`x=0`$, $`F(0)=64/18+C=32/9+C`$, so $`C=-32/9`$. Thus

$$
F(x)=\frac{(x^3+2)^6}{18}-\frac{32}{9}.
$$

The derivative is $`(6/18)(x^3+2)^5(3x^2)=x^2(x^3+2)^5`$, and substitution at zero verifies the value condition. This polynomial answer holds on the real line.

The separate proposal differentiates to

$$
\frac d{dx}\left(-\frac12e^{-x^2}\right)
=-\frac12e^{-x^2}(-2x)=xe^{-x^2}.
$$

It matches the integrand with the outside $`x`$, not $`e^{-x^2}`$ on an interval. Equality at one isolated input would not establish an antiderivative relation throughout an interval. No constant multiplier of $`e^{-x^2}`$ can remove a varying factor $`x`$. This check rejects the proposed answer; it does not by itself establish whether another form of antiderivative exists.

S5. Substituting $`u=\ln x`$, $`du=dx/x`$, gives

$$
F(x)=\int u^{-2}\,du=-u^{-1}+C=-\frac1{\ln x}+C.
$$

The exponent is $`-2`$, so the power rule applies; the exceptional logarithmic case would have exponent $`-1`$. At $`x=e^{-1}`$, $`\ln x=-1`$, so $`0=1+C`$ and $`C=-1`$. The required answer is

$$
F(x)=-\frac1{\ln x}-1,\qquad 0\lt x\lt1.
$$

Checking by the chain rule gives

$$
F'(x)=-(-1)(\ln x)^{-2}\frac1x=\frac1{x(\ln x)^2}.
$$

The formula is also real and differentiable for $`x\gt1`$, but cannot include $`x=1`$ or nonpositive $`x`$. The given condition selects the constant on $`(0,1)`$ only; an extension to the other interval could have its own constant. A negative $`\ln x`$ is valid inside a nonzero denominator and its square. We have not taken the logarithm of that negative number.

S6. In the first representation, $`0=1/2+C_A`$, so $`C_A=-1/2`$. In the second, $`0=0+C_B`$, so $`C_B=0`$. Consequently

$$
A(x)=\frac12\sin^2x-\frac12
=\frac12(\sin^2x-1)
=-\frac12\cos^2x=B(x).
$$

Both derivatives are $`\sin x\cos x`$, and both full expressions vanish at $`\pi/2`$. Their unadjusted primitives differed by $`1/2`$, so their constants must differ by that amount in the opposite adjustment: $`C_B=C_A+1/2`$. The additive constant labels a function within a chosen representation, not a representation-independent number.

S7. (a) For $`f(x)=\ln x`$, $`f(1)=0`$ and $`f'(1)=1`$. With $`dx=0.04`$, $`dy=0.04`$, so $`\ln(1.04)\approx0.04`$. The equality defining $`dy`$ is exact, but the curved function's actual change need not equal its tangent-line change.

(b) Differentiating $`\sin(3x)`$ gives $`3\cos(3x)`$, so $`J(x)=\sin(3x)/3+C`$. At zero the sine term vanishes, hence $`C=2`$. The answer $`J(x)=\sin(3x)/3+2`$ has derivative exactly $`\cos(3x)`$ and value exactly $`2`$ at zero. Unlike (a), this is an exact function recovery checked by differentiation, not an estimate for a finite step.

(c) The real integrand requires $`x\gt0`$ and $`x\ne1`$, giving the intervals $`(0,1)`$ and $`(1,\infty)`$. The expression $`\ln(\ln x)`$ works only on the latter. An answer valid on either interval is $`\ln|\ln x|+C`$, with constants chosen independently if both intervals are considered. Absolute value makes the outer logarithm's input positive when the inner logarithm is negative. It does not make $`x\le0`$ acceptable to the inner logarithm or remove the singularity at $`x=1`$. For $`0\lt x\lt1`$, the derivative of $`\ln(-\ln x)`$ is $`(-1/x)/(-\ln x)=1/(x\ln x)`$; for $`x\gt1`$, the same result follows directly from differentiating $`\ln(\ln x)`$.
