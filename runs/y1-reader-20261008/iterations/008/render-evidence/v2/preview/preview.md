<!-- P001 -->
Linear and quadratic approximations

<!-- P002 -->
<a name="route"></a>

<!-- P003 -->
Reading route

<!-- P004 -->
Read from “A tangent as a local model” through the clock application, trying A1 and A2 where they occur and A3 at the end of the application. The later revisit A4 combines recall with method choice. All [hints](#hints) are together, followed by all [solutions](#solutions); use the task links to return. You may stop at a partial attempt and use its hint. The aim is to construct a local approximation, keep a consistent order, and decide what that approximation can justify.

<!-- P005 -->
This route uses familiar differentiation, limits, elementary algebra, radians and integration. It assumes no earlier university lecture. A basepoint is an input where the function and its derivatives are known or easy to calculate. We will approximate nearby values by a polynomial in the displacement from that point. The approximating polynomial has exact coefficients; using it in place of the function generally gives an estimate.

<!-- P006 -->
A tangent as a local model

<!-- P007 -->
Choose a fixed basepoint $x_0$ and put $h=x-x_0$. Thus $x=x_0+h$; the small quantity is $h$, even if $x_0$ is large. If $f$ is differentiable at $x_0$, its tangent polynomial is

<!-- P008 -->

$$L(x)=f(x_0)+f'(x_0)(x-x_0).$$


<!-- P009 -->
Here $f(x_0)$ is the height at contact, and $f'(x_0)$ is the slope there. Starting at the contact point, a horizontal displacement $h$ changes the line's height by $f'(x_0)h$. Conversely, a line through that point with that slope must have this equation. This is the meaning of the lecture's figure $y=b+a(x-x_0)$: $b=f(x_0)$ and $a=f'(x_0)$. The curve and line share height and slope at contact; they need not coincide elsewhere.

<!-- P010 -->
The derivative supplies a precise reason to approximate. Define the error $R_1(h)=f(x_0+h)-f(x_0)-f'(x_0)h$. For nonzero $h$,

<!-- P011 -->

$$\frac{R_1(h)}h=\frac{f(x_0+h)-f(x_0)}h-f'(x_0)\longrightarrow0\quad(h\to0).$$


<!-- P012 -->
So the error becomes small compared with the displacement. We abbreviate this property as $R_1(h)=o(h)$: the symbol $o(h)$ denotes an unspecified remainder whose ratio to $h$ tends to zero. It need not be zero, and it is not a stated error bound at a particular nonzero input. Writing $f(x)\approx L(x)$ means using that local model. The guarantee concerns approach to $x_0$; it does not say the error must increase monotonically at every step away from $x_0$.

<!-- P013 -->
For $f(x)=\ln x$ on $x\gt 0$, choose $x_0=1$. Since $f(1)=0$ and $f'(1)=1$, the exact tangent polynomial is $L(x)=x-1$. Therefore $\ln x\approx x-1$ near $1$; for example, $\ln(1.03)\approx0.03$. To describe the same calculation with a zero basepoint, set $u=x-1$. Then $x=1+u$, $u$ is near zero, and $\ln(1+u)\approx u$, with $u\gt -1$. The small input to this last formula is the change $u$, not the original input $x$ near $1$.

<!-- P014 -->
<a name="a1"></a>

<!-- P015 -->
A1. First use

<!-- P016 -->
For f(x)=sqrt(x), use the tangent at basepoint x0=4 to estimate sqrt(4.08). Give the whole tangent polynomial L(x), substitute the target input, and explain what is exact and what is approximate. Use the real square root on x>0. A sufficient response names the basepoint and displacement and keeps the exact tangent equation distinct from the estimate of f.

<!-- P017 -->
[Hint A1](#h1) · [Solution A1](#s1) · [Reading route](#route)

<!-- P018 -->
<a name="basics"></a>

<!-- P019 -->
Five basic local models

<!-- P020 -->
For the next formulas the basepoint is zero and $x$ itself is the displacement. Trigonometric inputs are in radians. The exponential and logarithm inputs are dimensionless. The exponent $r$ in the last formula is fixed; for general real $r$ we work near zero with $1+x\gt 0$.

<!-- P021 -->
For sine, $f(0)=0$ and $f'(0)=\cos0=1$, giving $\sin x\approx x$. For cosine, $f(0)=1$ and $f'(0)=-\sin0=0$, giving $\cos x\approx1$. The two tangent pictures mean different things: sine has a sloping tangent through the origin, while cosine has a horizontal tangent through height $1$. A “linear approximation” includes a constant polynomial when the slope is zero.

<!-- P022 -->
For $e^x$, value and slope at zero are both $1$, so $e^x\approx1+x$. For $\ln(1+x)$, value zero and derivative $1/(1+x)$ give $\ln(1+x)\approx x$. For $(1+x)^r$, value $1$ and derivative $r(1+x)^{r-1}$ give $(1+x)^r\approx1+rx$. All five are approximations near zero, not identities. The derivative argument above gives an $o(x)$ remainder in each case.

<!-- P023 -->
Substitution means replacing the entire small input. For instance, $e^u\approx1+u$ with $u=-2x$ gives $e^{-2x}\approx1-2x$, requiring $|-2x|$ small. Similarly $(1+x)^{-1/2}\approx1-x/2$. The identity $1/\sqrt{1+x}=(1+x)^{-1/2}$ requires $x\gt -1$ and gives the lecture's reciprocal-square-root shortcut directly. Alternatively, first approximate $\sqrt{1+x}$ by $1+x/2$, then use $(1+u)^{-1}\approx1-u$ with $u=x/2$ for its reciprocal. Neither step is an exact equality to the original function.

<!-- P024 -->
Combining approximations without inventing extra accuracy

<!-- P025 -->
The lecture's example is $f(x)=e^{-2x}/\sqrt{1+x}$ for $x\gt -1$. Write it exactly as $e^{-2x}(1+x)^{-1/2}$ and use the two linear models:

<!-- P026 -->

$$f(x)\approx(1-2x)(1-x/2)=1-\frac52x+x^2.$$


<!-- P027 -->
The displayed multiplication is exact for the two polynomials, but its $x^2$ coefficient need not be the function's quadratic coefficient: the factors' own quadratic contributions have not yet been included. Keeping only constant and linear terms gives

<!-- P028 -->

$$L(x)=1-\frac52x,\qquad f(x)=1-\frac52x+o(x).$$


<!-- P029 -->
To justify combining the remainders, write the factors as $1-2x+r(x)$ and $1-x/2+s(x)$, where $r(x)/x\to0$ and $s(x)/x\to0$. On multiplying, the additional pieces are $x^2$, $(1-2x)s(x)$, $(1-x/2)r(x)$ and $r(x)s(x)$. After division by $x$ each tends to zero: for example $x^2/x=x\to0$ and $r(x)s(x)/x=(r(x)/x)s(x)\to0$. This licenses the stated first-order remainder. It also recovers the exact facts $f(0)=1$ and $f'(0)=-5/2$ by continuity and the derivative definition. A merely rough numerical fit would not justify reading off an exact derivative this way.

<!-- P030 -->
Limits: cancellation makes the error matter

<!-- P031 -->
For the lecture's $F(x)=(1+2x)^{10}$, the derivative definition immediately gives

<!-- P032 -->

$$\lim_{x\to0}\frac{(1+2x)^{10}-1}{x}=F'(0)=20.$$


<!-- P033 -->
Indeed $F(0)=1$ and $F'(x)=20(1+2x)^9$. The approximation route reaches the same answer: put $u=2x$, $r=10$ into the power model, obtaining $F(x)=1+20x+o(x)$. Subtracting $1$ and dividing by nonzero $x$ leaves $20+o(x)/x\to20$. This shows why an error statement matters. Cancelling the constant does not turn $\approx$ into an equality; the remaining error must still vanish after the division used in the limit.

<!-- P034 -->
<a name="quadratic"></a>

<!-- P035 -->
Matching bending as well as slope

<!-- P036 -->
A linear model misses bending. Write a candidate polynomial in the same displacement $h=x-x_0$ as $A+Bh+Ch^2$. Its value, first derivative and second derivative at $h=0$ are $A,B,2C$. Matching these to $f(x_0),f'(x_0),f''(x_0)$ therefore gives

<!-- P037 -->

$$Q(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}2(x-x_0)^2.$$


<!-- P038 -->
The coefficient is $f''(x_0)/2$, because differentiating $Ch^2$ twice gives $2C$. The whole displacement is squared. In particular, if $f(x)=a+bx+cx^2$ and $x_0=0$, this construction gives $a+bx+cx^2$ exactly. At any basepoint it reproduces a polynomial of degree at most two exactly, because that polynomial is already of the candidate form when expressed in $h$.

<!-- P039 -->
For a function whose first two derivatives are continuous near $x_0$, the error $R_2(h)=f(x_0+h)-Q(x_0+h)$ satisfies $R_2(h)/h^2\to0$. We write this as $R_2(h)=o(h^2)$. Here is why this stronger error claim follows, beyond merely matching three numbers. The fundamental theorem of calculus gives

<!-- P040 -->

$$f(x_0+h)-f(x_0)=\int_0^h f'(x_0+t)\,dt,$$


<!-- P041 -->

$$f'(x_0+t)=f'(x_0)+f''(x_0)t+\int_0^t\bigl[f''(x_0+s)-f''(x_0)\bigr]\,ds.$$


<!-- P042 -->
Insert the second equation into the first. Integrating the first two terms gives $f'(x_0)h+f''(x_0)h^2/2$, exactly the nonconstant terms of $Q$. The remainder is the double integral of the bracketed difference. By continuity, for sufficiently small $|h|$ the absolute value of that difference is below any chosen positive number $\varepsilon$ throughout the interval between $0$ and $h$. The inner integral then has magnitude at most $\varepsilon|t|$, and the outer one at most $\varepsilon h^2/2$, for either sign of $h$. Thus $|R_2(h)/h^2|\le\varepsilon/2$ as near zero as required, which proves the claim. This establishes local accuracy without asserting a particular numerical tolerance at a chosen input.

<!-- P043 -->
For cosine at zero, $f(0)=1$, $f'(0)=0$ and $f''(0)=-1$. Hence $Q(x)=1-x^2/2$ and $\cos x\approx1-x^2/2$. The constant tangent has no bending; the negative quadratic term bends downward symmetrically to either side, as cosine does near its maximum. This is the relation shown by the source's parabola-and-cosine figure. “Best fit” here means matching value, slope and second derivative at the basepoint; it does not mean minimising errors over an arbitrary interval. A quadratic model is useful when bending or a cancellation makes the second-order term consequential, as well as when a closer local value is wanted.

<!-- P044 -->
The five quadratic models

<!-- P045 -->
At zero, sine has second derivative $-\sin0=0$, cosine has second derivative $-\cos0=-1$, and the exponential has second derivative $e^0=1$. The resulting formulas are

<!-- P046 -->

$$\sin x\approx x,\qquad \cos x\approx1-\frac{x^2}{2},\qquad e^x\approx1+x+\frac{x^2}{2}.$$


<!-- P047 -->
A quadratic approximation means retaining terms through degree two; its quadratic coefficient is allowed to be zero. For $\ln(1+x)$, differentiating $f'(x)=(1+x)^{-1}$ gives $f''(x)=-(1+x)^{-2}$, so $(f(0),f'(0),f''(0))=(0,1,-1)$ and

<!-- P048 -->

$$\ln(1+x)\approx x-\frac{x^2}{2}.$$


<!-- P049 -->
For fixed $r$, differentiating $r(1+x)^{r-1}$ gives $r(r-1)(1+x)^{r-2}$. Therefore

<!-- P050 -->

$$(1+x)^r\approx1+rx+\frac{r(r-1)}2x^2.$$


<!-- P051 -->
These formulas have the same local domains and radian convention as the linear models, and each has an $o(x^2)$ remainder. The interval where an infinite series converges and the interval where a short truncation meets a desired tolerance are different questions. Even when $|x|\lt 1$ permits a nonterminating binomial series, that condition alone does not certify an accurate two-term numerical estimate. Coefficients and the required tolerance matter as well as smallness of the input.

<!-- P052 -->
Returning to the combined function

<!-- P053 -->
To improve $f(x)=e^{-2x}(1+x)^{-1/2}$, expand each factor through degree two before multiplying. Substitution into the exponential and power formulas gives

<!-- P054 -->

$$e^{-2x}=1-2x+2x^2+o(x^2),$$


<!-- P055 -->

$$(1+x)^{-1/2}=1-\frac{x}{2}+\frac38x^2+o(x^2).$$


<!-- P056 -->
The quadratic coefficient $3/8$ comes from $(-1/2)(-3/2)/2$. To build the product through degree two, a constant times a quadratic contributes, and a linear times a linear contributes too. Thus

<!-- P057 -->

$$Q(x)=1+\left(-2-\frac12\right)x+\left(2+(-2)(-1/2)+\frac38\right)x^2
=1-\frac52x+\frac{27}{8}x^2.$$


<!-- P058 -->
Terms of degree three and above, divided by $x^2$, tend to zero. A factor remainder $o(x^2)$ multiplied by a polynomial that stays bounded near zero still has ratio to $x^2$ tending to zero. The product of the two remainders has that property too. Consequently $f(x)=Q(x)+o(x^2)$, and the coefficient $27/8$ is justified. The earlier isolated $x^2$ term supplied only the mixed contribution $1$; it omitted $2+3/8$ from the factors themselves.

<!-- P059 -->
<a name="a2"></a>

<!-- P060 -->
A2. Combining and cancelling

<!-- P061 -->
Let g(x)=e^(3x)/sqrt(1-2x), on the real domain x<1/2. Construct its linear and quadratic polynomials about x=0. Show which products contribute to the coefficient of x^2. Then evaluate lim_(x->0) [g(x)-g(0)-g'(0)x]/x^2, and explain why a first-order approximation alone does not determine this limit. A sufficient response gives the two polynomials, the cross-term calculation, and a remainder-based warrant for the limit, with the substitutions' smallness conditions.

<!-- P062 -->
[Hint A2](#h2) · [Solution A2](#s2) · [Reading route](#route)

<!-- P063 -->
<a name="clock"></a>

<!-- P064 -->
A small parameter inside a physical model

<!-- P065 -->
The lecture's “Planet Quirk” satellite picture shows motion relative to an observer; the direction arrow identifies relative motion, not an additional term in the calculation. To give the clock comparison a precise scope, use a constant-speed model without gravity or acceleration. The laboratory is an inertial frame: a system of positions and synchronised clocks in which an unforced body moves uniformly along a straight line. Let $T\gt 0$ be the time between two ticks recorded by the travelling clock itself, and let $T'$ be the interval assigned to those same events by the laboratory. This is a comparison of event times in the frame, not the arrival-time spacing of light signals at a wristwatch. The special-relativistic law supplied for this example is

<!-- P066 -->

$$T'=\frac{T}{\sqrt{1-v^2/c^2}},\qquad c>0,\quad0\le v<c.$$


<!-- P067 -->
Here $v$ is speed relative to the laboratory and $c$ is light speed. This physical law is an introduced premise, not a consequence of differentiation. The inertial, moving-clock interpretation is consistent with [Markus Pössel's explanation of time dilation](https://www.einstein-online.info/en/spotlight/light-clocks-time-dilation/). The mathematical work below approximates that law. It is not a complete model of an orbiting clock on a gravitating planet.

<!-- P068 -->
Define $z=v^2/c^2$. Since both speeds use the same units, $z$ and $T'/T$ are dimensionless. For $v\ll c$, $z\ll1$ and the small input in the power formula is $u=-z$, with exponent $r=-1/2$. Keeping through degree two in $z$ gives

<!-- P069 -->

$$\frac{T'}T=(1-z)^{-1/2}\approx1+\frac z2+\frac38z^2,$$


<!-- P070 -->

$$T'-T\approx T\left(\frac{v^2}{2c^2}+\frac{3v^4}{8c^4}\right).$$


<!-- P071 -->
The sign of the leading change is positive: the laboratory assigns a longer interval to those two ticks than the moving clock records. At $v=0$ the difference vanishes. “Linear” in $z$ here already means quadratic in $v/c$; “quadratic” in $z$ means quartic in $v/c$. This distinction prevents dropping the leading effect by looking for a term proportional to $v$.

<!-- P072 -->
With the lecture's rounded values $v=4\ \mathrm{km/s}$ and $c=3\times10^5\ \mathrm{km/s}$,

<!-- P073 -->

$$z=\left(\frac4{300000}\right)^2\approx1.78\times10^{-10},\qquad \frac z2\approx8.89\times10^{-11},\qquad \frac38z^2\approx1.19\times10^{-20}.$$


<!-- P074 -->
The last two numbers are contributions to the ratio $T'/T$. Multiplying by the actual interval $T$ gives time contributions; for example the leading contribution for $T=1\ \mathrm{s}$ is about $8.89\times10^{-11}\ \mathrm{s}$. Its smallness relative to $1$ does not by itself say whether a clock application needs it. Similarly, the next term's size suggests the scale of the truncation error but does not itself bound the sum of everything omitted. A required accuracy must be compared with an actual error bound or a sufficiently justified error estimate, in matching units.

<!-- P075 -->
Real GPS timing requires motion and gravitational effects. [NIST's account](https://www.nist.gov/atomic-clocks/a-powerful-tool-for-science/putting-einstein-test) explains that they act in opposite directions for GPS satellites and that the system corrects relativistic timing effects. That supports the lecture's practical motivation while limiting what the single displayed speed formula can establish. The lecture's 2006 comment about the best atomic clocks is historical context, not a present-day measurement limit used here. We need no such performance claim to compare terms in the model.

<!-- P076 -->
<a name="a3"></a>

<!-- P077 -->
A3. A changed clock comparison

<!-- P078 -->
Use the declared constant-speed, gravity-free model T'=T/sqrt(1-(v/c)^2), where T is the interval recorded by a clock travelling with the object, T' is the interval assigned to the same two ticks by the inertial laboratory, c>0, and 0<=v<c. Set v/c=0.02 and T=1000 s. Estimate T'-T retaining terms through (v/c)^4. Find the size, in seconds, of the quartic correction that is lost if only the leading nonzero correction is kept. Compare it with an allowable absolute error of 10^(-4) s. Does the size of that one correction alone prove that the total error is below the allowance? Explain. A sufficient response distinguishes the dimensionless expansion variable, the clock-time difference, the order in that variable versus the order in v/c, and an estimate of error from a proved bound. No gravitational model or current clock-performance fact is needed.

<!-- P079 -->
[Hint A3](#h3) · [Solution A3](#s3) · [Reading route](#route)

<!-- P080 -->
<a name="revisit"></a>

<!-- P081 -->
Returning after a break

<!-- P082 -->
Try A4 at a later sitting, perhaps the next day; that timing is an adjustable study suggestion. Reconstructing a formula checks retrieval of what you studied. Selecting enough terms after a cancellation checks transfer to the expression in front of you. If you need help, use the hint, then return to the original task and complete the part you can justify.

<!-- P083 -->
<a name="a4"></a>

<!-- P084 -->
A4. Later retrieval and method choice

<!-- P085 -->
At a later sitting, first try without rereading: reconstruct the linear and quadratic approximation formulas about a general basepoint a for a function whose first two derivatives are continuous near a. Explain the factor 1/2 by differentiating a quadratic polynomial. Then evaluate lim_(x->0) [cos(x)-1]/x^2 and explain why the constant-plus-linear approximation alone cannot settle it. Finally state whether going from linear to quadratic approximation changes the polynomial for sin(x) about zero, and justify your answer with derivatives at zero. Angles are in radians. A sufficient response supplies the formulas, the coefficient-matching reason, the limit with its remainder warrant, and the sine comparison. Partial attempts are useful; mark the last step you can justify before opening help.

<!-- P086 -->
[Hint A4](#h4) · [Solution A4](#s4) · [Reading route](#route)

<!-- P087 -->
<a name="provenance"></a>

<!-- P088 -->
Source and task provenance

<!-- P089 -->
This is an independently written teaching route based on the complete seven-page [MIT OpenCourseWare 18.01, Fall 2006, Lecture 9: Linear and Quadratic Approximations](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/40cb41807e6d67373f3299ce87c4d9b3_lec9.pdf), including its attribution page, four figures and footnote. The logarithm, exponential/reciprocal-root product, power limit, and Planet Quirk examples come from that source. Its attribution and use information is at [MIT OCW Terms](https://ocw.mit.edu/terms/). A1–A4 are generated practice, not quoted exam questions; the clock task deliberately uses a changed speed and duration. The remainder explanations and intermediate reasoning are supplied here to justify approximation algebra and limits.

<!-- P090 -->
Two source formulas need care: some of its derivations print an equality where only approximation is meant, and its first clock expansion drops the multiplier $T$. Here equality is reserved for exact expressions (including expressions with remainders), and the dimensionless clock expansion is explicitly for $T'/T$. The source's printed exponent $4$ in the bracket explaining the clock binomial substitution is also a typo; the stated exponent for that calculation is $r=-1/2$. These corrections preserve the mathematical operation without adopting the printing errors.

<!-- P091 -->
<a name="hints"></a>

<!-- P092 -->
Hints — all tasks

<!-- P093 -->
Each hint advances one useful construction. Complete solutions are in the separate group below.

<!-- P094 -->
<a name="h1"></a>

<!-- P095 -->
Hint A1

<!-- P096 -->
Start with $h=4.08-4$ and the values $f(4)=2$, $f'(4)=1/(2\sqrt4)$. The line starts at height $2$ and changes by its slope times $h$. The line's value is exact for that line; identify which replacement makes the answer an approximation.

<!-- P097 -->
[Return to A1](#a1) · [Solution A1](#s1)

<!-- P098 -->
<a name="h2"></a>

<!-- P099 -->
Hint A2

<!-- P100 -->
Rewrite the denominator factor as $(1-2x)^{-1/2}$. Its power-formula input is $u=-2x$, while the exponential's input is $u=3x$. For the quadratic product, collect constant-times-quadratic, linear-times-linear and quadratic-times-constant separately. Only after collecting those terms subtract the value and slope terms in the limit. [The remainder explanation](#quadratic) tells you what survives division by $x^2$.

<!-- P101 -->
[Return to A2](#a2) · [Solution A2](#s2)

<!-- P102 -->
<a name="h3"></a>

<!-- P103 -->
Hint A3

<!-- P104 -->
First compute $z=(0.02)^2$. The excess ratio is $T'/T-1\approx z/2+3z^2/8$; multiply each contribution by $1000\ \mathrm{s}$ before comparing with a tolerance in seconds. Keep “the next term” distinct from “the whole error”.

<!-- P105 -->
[Return to A3](#a3) · [Solution A3](#s3)

<!-- P106 -->
<a name="h4"></a>

<!-- P107 -->
Hint A4

<!-- P108 -->
Use $h=x-a$ and start from $A+Bh+Ch^2$. Match its first two derivatives and value at $h=0$. In the cosine limit, subtraction removes the value at zero, so the first surviving term matters. For sine, inspect the second derivative at zero before deciding whether there is a degree-two term.

<!-- P109 -->
[Return to A4](#a4) · [Solution A4](#s4)

<!-- P110 -->
<a name="solutions"></a>

<!-- P111 -->
Complete reasoned solutions — all tasks

<!-- P112 -->
These are model solutions to the generated tasks, not reports of anyone's performance.

<!-- P113 -->
<a name="s1"></a>

<!-- P114 -->
Solution A1

<!-- P115 -->
At $x_0=4$, $f(4)=2$ and $f'(4)=1/4$, from $f'(x)=1/(2\sqrt{x})$ on $x\gt 0$. Therefore the exact tangent polynomial is

<!-- P116 -->

$$L(x)=2+\frac14(x-4).$$


<!-- P117 -->
The displacement for the requested input is $h=0.08$. Thus $L(4.08)=2+0.08/4=2.02$ exactly, and $\sqrt{4.08}\approx2.02$ by the local tangent approximation. The basepoint lies in the differentiable domain and the displacement is small. Equality to the square root would be false: $2.02^2=4.0804$, rather than $4.08$. This check distinguishes exact line arithmetic from approximate use of the line.

<!-- P118 -->
[Return to A1](#a1) · [Hint A1](#h1) · [Reading route](#route)

<!-- P119 -->
<a name="s2"></a>

<!-- P120 -->
Solution A2

<!-- P121 -->
On $x\lt 1/2$ the real denominator is positive, so $g(x)=e^{3x}(1-2x)^{-1/2}$. Near zero, both $|3x|$ and $|-2x|$ are small. The substitutions into the established quadratic formulas give

<!-- P122 -->

$$e^{3x}=1+3x+\frac92x^2+o(x^2),$$


<!-- P123 -->

$$(1-2x)^{-1/2}=1+x+\frac32x^2+o(x^2).$$


<!-- P124 -->
For the second factor, the linear coefficient is $(-1/2)(-2)=1$ and the quadratic coefficient is $[(-1/2)(-3/2)/2](-2)^2=3/2$. On multiplication, the linear terms contribute $3+1=4$, and the quadratic terms contribute

<!-- P125 -->

$$\frac92+(3)(1)+\frac32=9.$$


<!-- P126 -->
Consequently $L(x)=1+4x$ and $Q(x)=1+4x+9x^2$. The established product remainder rule gives $g(x)=1+4x+9x^2+o(x^2)$. In particular $g(0)=1$ and $g'(0)=4$: the first is direct substitution, and the second follows by subtracting $g(0)$, dividing by $x$ and taking the derivative limit. The requested limit is therefore

<!-- P127 -->

$$\lim_{x\to0}\frac{g(x)-g(0)-g'(0)x}{x^2}
=\lim_{x\to0}\left(9+\frac{o(x^2)}{x^2}\right)=9.$$


<!-- P128 -->
A first-order statement gives only $g(x)=1+4x+o(x)$. Dividing its unspecified error by $x^2$ need not give zero or any particular finite value; for example any term $kx^2$ is $o(x)$ but becomes $k$ after division by $x^2$. The quadratic information is what determines this limit. Differentiating the original product gives the independent check $g''(0)=18$, consistent with coefficient $18/2=9$.

<!-- P129 -->
[Return to A2](#a2) · [Hint A2](#h2) · [Reading route](#route)

<!-- P130 -->
<a name="s3"></a>

<!-- P131 -->
Solution A3

<!-- P132 -->
The dimensionless small parameter is $z=(v/c)^2=(0.02)^2=0.0004$. Through degree two in $z$, or degree four in $v/c$,

<!-- P133 -->

$$T'-T\approx1000\left(\frac{0.0004}{2}+\frac38(0.0004)^2\right)\mathrm{s}
=0.20006000\ \mathrm{s}.$$


<!-- P134 -->
The leading term is $0.2000\ \mathrm{s}$. The quartic correction discarded by keeping only that term is $0.00006000\ \mathrm{s}=6.0\times10^{-5}\ \mathrm{s}$, which is smaller than the allowance $10^{-4}\ \mathrm{s}$. This comparison suggests that keeping only the leading term may be adequate here, but that single correction does not prove a bound on the total omitted contribution. The local $o(z^2)$ statement says how the remainder behaves as $z\to0$, not a numerical bound at $z=0.0004$. Certification would need a bound on the remaining terms or a controlled comparison with the exact model. The requested estimate and the logical limitation are both part of the answer; no claim about real clock capabilities follows.

<!-- P135 -->
[Return to A3](#a3) · [Hint A3](#h3) · [Reading route](#route)

<!-- P136 -->
<a name="s4"></a>

<!-- P137 -->
Solution A4

<!-- P138 -->
With $h=x-a$, the required polynomials are

<!-- P139 -->

$$L(x)=f(a)+f'(a)(x-a),$$


<!-- P140 -->

$$Q(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}2(x-a)^2.$$


<!-- P141 -->
For $A+Bh+Ch^2$, derivatives are $B+2Ch$ and $2C$. At $h=0$, matching the function, slope and second derivative sets $A=f(a)$, $B=f'(a)$ and $2C=f''(a)$. This explains the factor $1/2$. Under the stated continuity conditions the earlier integration argument supplies the $o(h^2)$ remainder.

<!-- P142 -->
For cosine at zero, the value and first two derivatives are $1,0,-1$. Thus $\cos x=1-x^2/2+o(x^2)$. Subtract $1$ and divide by $x^2$ to obtain

<!-- P143 -->

$$\lim_{x\to0}\frac{\cos x-1}{x^2}=-\frac12.$$


<!-- P144 -->
The linear model is the constant $1$; it supplies no coefficient for the first surviving term after the subtraction. Its error is known to be $o(x)$, which alone is insufficient after division by $x^2$, for the same reason demonstrated in Solution A2. For sine the value, slope and second derivative at zero are $0,1,0$. Therefore both its linear and quadratic polynomials are $x$. This says the degree-two coefficient vanishes, not that $\sin x=x$ identically or that there is no higher-order error.

<!-- P145 -->
[Return to A4](#a4) · [Hint A4](#h4) · [Reading route](#route)
