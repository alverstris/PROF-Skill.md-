[P01] Implicit differentiation and inverses

Read [P02]–[P27] in order and try the questions where they occur. The [hints](#hints) are grouped after the core; the [complete solutions](#solutions) follow all hints. Each question has its own links and return route. Q5 is for a later revisit. Partial attempts are useful: compare the first step you cannot justify with the corresponding help.

[P02] The aim is to find a curve's slope without first solving explicitly for its vertical coordinate, and to find the slope of an inverse function without first finding its formula. We will also reconstruct the rational-power and arctangent derivatives. The starting toolkit is the derivative as a difference-quotient limit, ordinary algebra, the product and chain rules, real powers, inverse functions and radian trigonometry. These are available in the supplied school baseline; the new emphasis is on connecting the rules while keeping their conditions visible.

[P03] An equation such as $x^2+y^2=1$ describes pairs of coordinates. It does not assign just one $y$ to each $x$. To differentiate with respect to $x$, select a local branch: a part of the curve on which $y$ is a function $y(x)$. If that function is differentiable, the chain rule gives

$$
\frac{d}{dx}[y(x)^2]=2y(x)y'(x).
$$

Thus $2y$ differentiates the outer square, and $y'=dy/dx$ records the changing inner input. Implicit differentiation means applying this reasoning to the equation that relates the variables. It computes a derivative conditional on a differentiable branch; the act of differentiating an equation does not prove that such a branch exists.

[P04] The unit circle gives a first worked case. Solving $y^2=1-x^2$ produces the upper and lower branches $y=\pm\sqrt{1-x^2}$, defined for $-1\leq x\leq1$. On the upper branch and the open interval $-1\lt x\lt 1$, the familiar power and chain rules give

$$
y=(1-x^2)^{1/2},\qquad
y'=\frac12(1-x^2)^{-1/2}(-2x)
   =\frac{-x}{\sqrt{1-x^2}}=\frac{-x}{y}.
$$

Here the radicand is positive, so the known square-root derivative applies. The lower branch is the negative of the upper one and is also differentiable on this open interval. We therefore have actual differentiable branches for the next calculation.

[P05] Differentiating the original circle equation keeps both branches together:

$$
x^2+y^2=1
\quad\Longrightarrow\quad 2x+2yy'=0
\quad\Longrightarrow\quad 2yy'=-2x
\quad\Longrightarrow\quad y'=-\frac{x}{y}\quad(y\ne0).
$$

On the lower branch, putting a negative $y$ into this expression automatically gives the appropriate sign. At $(1,0)$ and $(-1,0)$, division by $y$ is unavailable. Indeed, a finite derivative there would make $2x+2yy'=0$ require $2x=0$, which is false. The circle has vertical tangents at those points: the radii are horizontal and a circle's tangent is perpendicular to its radius. A vertical tangent has no finite $dy/dx$.

<a id="q1"></a>

[P06] Q1. On $x^2+y^2=1$, use implicit differentiation to find the slope and tangent equation at $(3/5,-4/5)$. Explain why the negative $y$-coordinate is permitted even though the worked explicit example used the upper semicircle. State where the expression $-x/y$ cannot give a finite slope. Target: carry the chain-rule argument to another branch. A complete response has the differentiated equation, the slope, the tangent line, and the branch/division conditions. [Hint H1](#h1) · [Solution S1](#s1).

[P07] When solving for $y$ is awkward, keeping the equation is especially useful. The lecture's next curve is $y^3+xy^2+1=0$. Suppose we are on a differentiable local branch. The mixed term $xy^2$ is a product of two changing quantities; its derivative is

$$
\frac{d}{dx}(xy^2)=1\cdot y^2+x\cdot(2yy').
$$

Combining this with the derivative of $y^3$ gives a connected calculation:

$$
3y^2y'+y^2+2xyy'=0,
\qquad (3y^2+2xy)y'=-y^2,
\qquad y'=-\frac{y^2}{3y^2+2xy}\quad(3y^2+2xy\ne0).
$$

At $(0,-1)$, the original equation holds and the formula gives $y'=-1/3$; if the branch exists, its tangent is $y+1=-x/3$. Both chain-rule factors and both product-rule contributions are necessary. The constant $1$ contributes zero.

[P08] This algebra has a precise boundary. The curve never has $y=0$, since substitution would give $1=0$. If $3y^2+2xy=0$, the differentiated equation would demand $0=-y^2$, also impossible here. Hence no finite $dy/dx$ is compatible with a differentiable branch at such a point. We will justify the branches where this coefficient is nonzero using an inverse in [P18]; we have not inferred their existence merely by dividing.

<a id="q2"></a>

[P09] Q2. For $y^3+xy+1=0$, assume a differentiable local function $y(x)$ near $(0,-1)$. Find $dy/dx$ in terms of $x$ and $y$, then the tangent at that point. Identify the coefficient you must divide by and state what the calculation does and does not establish about existence of a differentiable branch. Target: reconstruct product/chain choices when the mixed term changes. A complete response shows both contributions from $xy$, the nonzero condition and the conditional nature of the argument. [Hint H2](#h2) · [Solution S2](#s2).

[P10] An inverse undoes a function on a chosen domain. Let $f$ assign each input in a set $I$ a unique output, and suppose different inputs give different outputs. Write $J=f(I)$ for its range. The inverse $g=f^{-1}$ takes each output in $J$ back to its unique input in $I$. The superscript $-1$ denotes this reverse assignment, not the reciprocal $1/f$. If $b=f(a)$, then $a=g(b)=f^{-1}(b)$.

[P11] For example, squaring on all real numbers has no inverse function, because $2$ and $-2$ both produce $4$. On $I=[0,\infty)$, squaring has range $J=[0,\infty)$ and inverse $g(z)=\sqrt z$. Choosing $I=(-\infty,0]$ instead gives the different inverse $g(z)=-\sqrt z$. The domain restriction is part of the function being inverted.

[P12] The two ways of undoing are

$$
g(f(x))=x\quad(x\in I),\qquad
f(g(z))=z\quad(z\in J).
$$

In composition notation these read $(g\circ f)(x)=x$ and $(f\circ g)(z)=z$: evaluate the inner function first. They have different input sets even though both return their inputs. In the lecture's graph, a point $(a,b)$ on $f$ has $b=f(a)$, and its reversed point $(b,a)$ lies on $g$, with $a=f^{-1}(b)$. Swapping the coordinates reflects the point across $y=x$. This explains the original figure's black forward curve, blue inverse curve and reflection line; the dashed horizontal and vertical guides connect corresponding input/output coordinates. The pictured shape illustrates the swap, rather than imposing a particular formula for $f$.

[P13] To put both graphs on the same axes, we conventionally call each graph's horizontal coordinate $x$. Thus the inverse graph can be written $y=g(x)$, equivalently $x=f(y)$. This is a renaming after reversing the assignment, not a claim that $f(x)=g(x)$. For the nonnegative squaring example, $(2,4)$ on $y=x^2$ becomes $(4,2)$ on $y=\sqrt x$.

[P14] The lecture obtains a reciprocal slope by differentiating an inverse identity. If both derivatives exist, $g(f(x))=x$ gives

$$
g'(f(x))f'(x)=1.
$$

At $a$ with $b=f(a)$ and $f'(a)\ne0$, this yields $g'(b)=1/f'(a)$. The inverse slope is evaluated at the forward output $b$, while the forward slope is evaluated at the original input $a$. In the lecture's notation $y=f(x)$, this is $dx/dy=1/(dy/dx)$ at the same paired values. The chain rule explains the reciprocal once the inverse is differentiable; it does not yet prove that differentiability.

[P15] Here is an existence justification we can reuse. Suppose $f$ is continuous and strictly monotone on an open interval $I$: it is either strictly increasing throughout or strictly decreasing throughout. Continuity means that nearby inputs have nearby outputs; strict monotonicity means the outputs preserve their order throughout or reverse it throughout. Hence $f$ is one-to-one there and has an inverse $g$ on its range. Choose an interior input $a$, write $b=f(a)$, and suppose $f'(a)$ exists and is nonzero.

[P16] First, the inverse is continuous at $b$. To see the connection, bracket $a$ by points $l\lt a\lt r$ as close to $a$ as desired. By strict monotonicity, $b$ lies strictly between $f(l)$ and $f(r)$. An output $z$ sufficiently close to $b$ stays between these endpoint outputs. Its inverse $g(z)$ must then lie between $l$ and $r$; otherwise monotonicity would put $z$ outside the bracket. Continuity of $f$ ensures every intermediate output is attained: apply the baseline's continuous sign-change root fact to $f(t)-z$ at the two bracket endpoints. This works for either ordering of the endpoint outputs. Since the input bracket can be arbitrarily narrow, $z\to b$ forces $g(z)\to a$.

[P17] Now set $u=g(z)$, so $z=f(u)$ and $g(b)=a$. For $z\ne b$, one-to-one correspondence ensures $u\ne a$. The inverse difference quotient becomes

$$
\frac{g(z)-g(b)}{z-b}
=\frac{u-a}{f(u)-f(a)}
=\frac{1}{\dfrac{f(u)-f(a)}{u-a}}
\ \longrightarrow\ \frac1{f'(a)}.
$$

The last limit uses $u\to a$ and the reciprocal limit rule: if $A\to L\ne0$, then $1/A\to1/L$. The reason is $1/A-1/L=(L-A)/(AL)$: sufficiently near $L$, $|A|\geq|L|/2$, so the denominator stays bounded away from zero while the numerator tends to zero. Here $A$ is the forward difference quotient and $L=f'(a)$. This proves the inverse derivative exists, not just what its value would be. Equivalently, for an inverse input $z$ satisfying these conditions,

$$
g'(z)=\frac{1}{f'(g(z))}.
$$

Read the denominator from inside out: recover the original input with $g$, then evaluate the forward derivative there. If the forward derivative is zero, this proof and the reciprocal formula are unavailable; a difference quotient or another argument is required.

[P18] Return to the source curve $y^3+xy^2+1=0$. Because $y\ne0$, it can be solved for the other coordinate:

$$
x=h(y)=-y-y^{-2},\qquad h'(y)=-1+2y^{-3}
       =-\frac{3y^2+2xy}{y^2}\quad\text{on the curve}.
$$

The last equality substitutes $x=-y-y^{-2}$. Where $3y^2+2xy\ne0$, this derivative is nonzero and continuous. It therefore keeps the same sign on a sufficiently small interval around that $y$, avoiding zero; the familiar derivative sign test makes $h$ strictly monotone there. The inverse argument [P15]–[P17] now justifies a differentiable local function $y(x)$ and gives the same $dy/dx$ as [P07]. In particular it justifies the branch and tangent used at $(0,-1)$. This route avoids solving a cubic for $y$.

[P19] The lecture also extends the integer power rule to rational exponents. For $m$ an integer, $n$ a positive integer and $x\gt 0$, define $y=x^{m/n}$ to be the positive $n$th root of $x^m$. Why may we differentiate this function? On positive inputs $p(t)=t^n$ is continuous and strictly increasing, with $p'(t)=nt^{n-1}\gt 0$. Its positive inverse root is differentiable by [P15]–[P17]. Composing that root with the differentiable integer power $x^m$ gives a differentiable $y(x)$. This supplies the existence premise before using the chain rule.

[P20] The integer power derivative is already known for positive, zero and negative integer powers on their proper domains. Raise $y=x^{m/n}$ to the $n$th power, differentiate, and solve:

$$
y^n=x^m,\qquad ny^{n-1}y'=mx^{m-1},\qquad
y'=\frac{m}{n}\frac{x^{m-1}}{y^{n-1}}
   =\frac{m}{n}\frac{x^{m-1}}{x^{m(n-1)/n}}.
$$

Here $y\gt 0$ makes the division valid. Dividing powers subtracts exponents, and

$$
(m-1)-\frac{m(n-1)}n
=\frac{n(m-1)-m(n-1)}n
=\frac{nm-n-mn+m}{n}
=\frac mn-1.
$$

Thus $(x^{m/n})'=(m/n)x^{m/n-1}$ for $x\gt 0$, reproducing every exponent step in the lecture's argument. For example, $y=x^{2/3}$ satisfies $y^3=x^2$, giving $3y^2y'=2x$ and $y'=(2/3)x^{-1/3}$ on this positive domain.

[P21] That calculation was deliberately on $x\gt 0$. Negative powers cannot include zero. For negative inputs, reduce the rational exponent first: an odd denominator permits the real odd-root convention, whereas an even denominator does not give a real root of a negative input. At zero, neither the preceding division nor the inverse proof at a zero forward derivative supplies a conclusion. A short example shows the right replacement. For $w(x)=x^{5/3}$ with the real cube-root convention, $w(0)=0$ and

$$
\frac{w(h)-w(0)}h
=\frac{(\sqrt[3]{h})^5}{(\sqrt[3]{h})^3}
=(\sqrt[3]{h})^2\longrightarrow0.
$$

So $w'(0)=0$ follows directly, although the earlier division proof did not cover zero. If an even-root domain ends at zero, only a one-sided endpoint quotient is available, not the ordinary two-sided derivative. A constant function defined as $w(x)=1$ has derivative zero wherever defined; this treats a zero exponent without evaluating $0\cdot x^{-1}$ at zero.

<a id="q3"></a>

[P22] Q3. Let $u(x)=x^{4/3}$ use the real cube-root convention for every real $x$, and let $v(x)=x^{1/3}$. Find their derivatives for $x\gt 0$. Then use difference quotients at $x=0$ to decide whether each has a finite derivative there. Target: separate a power formula valid away from zero from its endpoint/zero justification. A complete response gives both nonzero formulas and a justified zero-point conclusion for each; substitution into an undefined formula is not enough. [Hint H3](#h3) · [Solution S3](#s3).

[P23] For the inverse trigonometric example, use radians and the principal $y=\arctan x$, whose range is $-\pi/2\lt y\lt \pi/2$. This is the branch already specified in the baseline and used by the lecture's acute-angle triangle. Tangent on this interval is continuous, strictly increasing, has range all real numbers, and has nonzero derivative $\sec^2 y=1/\cos^2 y$. The inverse proof therefore justifies differentiability of arctangent for every real input. Differentiating the defining equation now gives

$$
\tan y=x,\qquad
\frac{1}{\cos^2 y}\,y'=1,\qquad
y'=\cos^2 y=\cos^2(\arctan x).
$$

[P24] The lecture's first figure turns this last composition into an expression in $x$. For $x\gt 0$, form a right triangle with angle $y$ at the top of a vertical side of length $1$. The horizontal side opposite $y$ has length $x$. Hence $\tan y=x/1=x$, so its acute angle is $y=\arctan x$. Pythagoras gives hypotenuse $\sqrt{1+x^2}$, and adjacent over hypotenuse gives

$$
\cos y=\frac{1}{\sqrt{1+x^2}},\qquad
\cos^2 y=\left(\frac{1}{\sqrt{1+x^2}}\right)^2
=\frac{1}{1+x^2}.
$$

The figure's vertical side is adjacent to the marked angle, although it is not the horizontal base. Side roles are relative to the angle, not the page orientation. This triangle describes positive $x$; a negative side length or the degenerate triangle at zero cannot justify the remaining inputs.

[P25] For all real $x$, use the identity $1+\tan^2 y=\sec^2 y$ instead. With $\tan y=x$ it gives $1+x^2=1/\cos^2 y$. Since $1+x^2\gt 0$, invert to obtain

$$
\frac{d}{dx}\arctan x=\frac1{1+x^2}\qquad(x\in\mathbb R).
$$

On the chosen branch $\cos y\gt 0$, so even the unsquared identity $\cos(\arctan x)=1/\sqrt{1+x^2}$ is consistent for negative $x$ and zero. The derivative is positive, equals $1$ at zero, and becomes small as $|x|$ grows, in agreement with an increasing inverse whose graph flattens toward its limiting angles.

<a id="q4"></a>

[P26] Q4. A continuous strictly decreasing function $f$ on an open interval $I$ has $f(2)=5$ and $f'(2)=-3$. Write $g=f^{-1}$ on the range $J=f(I)$. Find $g(5)$, $g'(5)$, and the corresponding points on the graphs of $f$ and $g$. State the domains of $g(f(x))=x$ and $f(g(z))=z$. Explain why the inverse derivative rule uses $f'(2)$ here, rather than requiring $f'(5)$. Target: match inverse inputs to forward evaluation points and interpret reflection. A complete response names the paired input/output values, the slope's evaluation point and both identity domains. [Hint H4](#h4) · [Solution S4](#s4).

<a id="q5"></a>

[P27] Q5. Revisit this after a break, first with the explanation closed; a later day is one adjustable option. (a) From memory, state what licenses differentiating an implicit relation and the hypotheses needed for a finite reciprocal inverse derivative. Then reopen the notes and repair omissions. (b) Let $F(t)=t+\arctan t$, with principal arctangent and radians. You may use that $F$ is continuous and strictly increasing on all real $t$ and has range all real numbers. If $G=F^{-1}$, find $G(1+\pi/4)$ and $G'(1+\pi/4)$, then give the tangent line to $G$ at that input. Target: (a) retrieve the conditions; (b) transfer them to a sum involving an inverse trigonometric function without solving explicitly for $G$. A complete response identifies the forward input, differentiates $F$, checks the nonzero condition and builds the tangent with the coordinates in the right order. All supplied facts in (b) are premises; the solution need not prove them. [Hint H5](#h5) · [Solution S5](#s5).

<a id="hints"></a>

[P28] Hints. Each hint supplies an intermediate step. The complete answers are in the next group.

<a id="h1"></a>

[P29] H1. Start with $2x+2yy'=0$ and substitute the signed coordinates into the coefficient of $y'$. Once the slope is $m$, construct the tangent as $y-y_0=m(x-x_0)$. The two explicit branches explain why the implicit equation can be used at either sign of $y$. [Return to Q1](#q1) · [Solution S1](#s1).

<a id="h2"></a>

[P30] H2. The product $xy$ gives $y+xy'$, whereas $y^3$ gives $3y^2y'$. Collect the two terms containing $y'$ before dividing. The question supplies branch differentiability as an assumption; keep it distinct from your algebraic conclusion. [Return to Q2](#q2) · [Solution S2](#s2).

<a id="h3"></a>

[P31] H3. Both functions vanish at zero. Put $r=\sqrt[3]{h}$, so $h=r^3$ and $h\to0$ means $r\to0$. Their zero-point quotients become $r^4/r^3$ and $r/r^3$. Compare their limits from either side. [Return to Q3](#q3) · [Solution S3](#s3).

<a id="h4"></a>

[P32] H4. Begin with the reversible pair $2\mapsto5$, so the inverse runs $5\mapsto2$. In $g'(z)=1/f'(g(z))$, evaluate the inner $g(z)$ first. A negative forward slope should give a negative inverse slope as well. [Return to Q4](#q4) · [Solution S4](#s4).

<a id="h5"></a>

[P33] H5. For (a), separate the assumed differentiability of an implicit branch from the monotonicity, continuity and nonzero derivative used to justify an inverse. For (b), $\arctan1=\pi/4$ identifies the forward input producing the requested inverse input. Compute $F'(t)$ before taking a reciprocal. [Return to Q5](#q5) · [Solution S5](#s5).

<a id="solutions"></a>

[P34] Complete solutions. These explain the choices as well as the resulting formulas. The potential mistakes mentioned below are anticipated routes, not reports of an observed attempt.

<a id="s1"></a>

[P35] S1. The point lies on the circle because $9/25+16/25=1$. Both upper and lower branches are differentiable where $-1\lt x\lt 1$. Differentiating gives $2x+2yy'=0$, and the nonzero $y=-4/5$ allows division:

$$
y'=-\frac{3/5}{-4/5}=\frac34,
\qquad y+\frac45=\frac34\left(x-\frac35\right).
$$

The sign change comes from the lower branch's actual negative coordinate. Replacing it by a positive square root would change the branch and produce the wrong slope. The expression is unavailable at the circle points $(\pm1,0)$, where the tangents are vertical and no finite derivative exists. [Return to Q1](#q1).

<a id="s2"></a>

[P36] S2. The supplied point satisfies $(-1)^3+0(-1)+1=0$. Using the assumed differentiable branch,

$$
3y^2y'+y+xy'=0,
\qquad (3y^2+x)y'=-y,
\qquad y'=-\frac{y}{3y^2+x}\quad(3y^2+x\ne0).
$$

At $(0,-1)$ the coefficient is $3$, the slope is $1/3$, and the tangent is $y+1=x/3$. The term $y$ comes from differentiating the factor $x$; the term $xy'$ comes from differentiating the factor $y$. Omitting either is a product-rule error, rather than a sign slip. The calculation establishes the derivative's value under the branch assumption and nonzero coefficient. It alone does not establish the existence of a differentiable branch. The problem explicitly supplies that assumption. [Return to Q2](#q2).

<a id="s3"></a>

[P37] S3. For positive inputs the rational-power derivation gives

$$
u'(x)=\frac43x^{1/3},\qquad
v'(x)=\frac13x^{-2/3}.
$$

At zero use the actual function values, both zero. For nonzero $h$, write $r=\sqrt[3]{h}$ so $h=r^3$. Then

$$
\frac{u(h)-u(0)}h=\frac{r^4}{r^3}=r\longrightarrow0,
\qquad
\frac{v(h)-v(0)}h=\frac{r}{r^3}=\frac1{r^2}\longrightarrow+\infty.
$$

The first quotient tends to zero from both sides, so $u'(0)=0$. The second grows without bound from both sides; it has no finite limit, so $v$ has no finite derivative at zero. Infinity is not a real derivative value. Even a plausible extension of a formula to zero needs this separate justification when its original proof divided by a quantity that vanishes there. [Return to Q3](#q3).

<a id="s4"></a>

[P38] S4. The pair $f(2)=5$ means $g(5)=2$. The continuous strictly decreasing restriction gives the inverse, and the nonzero forward derivative justifies its derivative:

$$
g'(5)=\frac1{f'(g(5))}=\frac1{f'(2)}=-\frac13.
$$

The graph points are $(2,5)$ on $f$ and $(5,2)$ on $g$, reflected across $y=x$. The identities are $g(f(x))=x$ for $x\in I$ and $f(g(z))=z$ for $z\in J$. The expression $1/f'(5)$ evaluates the forward derivative at the wrong input; $5$ need not even belong to $I$. The condition is about $f'(2)$, which is supplied. [Return to Q4](#q4).

<a id="s5"></a>

[P39] S5. An acceptable response to (a) says that implicit differentiation applies the usual rules to a differentiable local function satisfying the relation; collecting and dividing computes its derivative only where the divisor is nonzero. To justify an inverse derivative here, use a continuous strictly monotone function on an open interval, an interior input $a$ where $f'(a)$ exists and is nonzero, and the inverse on the corresponding range. At $b=f(a)$, the inverse derivative is $1/f'(a)$. Equivalent wording is acceptable if it preserves these assumptions and the paired evaluation points.

[P40] For (b), principal $\arctan1=\pi/4$, so $F(1)=1+\pi/4$ and $G(1+\pi/4)=1$. Differentiate the forward function:

$$
F'(t)=1+\frac1{1+t^2},\qquad F'(1)=\frac32\ne0,
\qquad G'\left(1+\frac\pi4\right)=\frac1{F'(1)}=\frac23.
$$

The problem supplies the continuous strictly increasing inverse setting. The computed nonzero derivative supplies the remaining local condition, so the reciprocal is justified. With $z$ denoting the horizontal input and $y=G(z)$ the vertical output, the tangent is

$$
y-1=\frac23\left(z-1-\frac\pi4\right).
$$

Solving $z=t+\arctan t$ explicitly for $t$ is unnecessary: the known pair identifies the correct evaluation point. Part (a) asks for retrieval of established conditions; part (b) asks for transfer to a new composition of ideas. Neither an immediate reading nor a worked solution by itself demonstrates delayed retention. [Return to Q5](#q5).

[P41] Source. This lesson reconstructs MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, Lecture 5, “Implicit Differentiation and Inverses”: [original five-page packet](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/18d6a86a30a4bc046c5f7034d47587f1_lec5.pdf). The course cover is followed by printed pages 1–4. The source's rational powers, circle, cubic, inverse derivative, arctangent triangle and inverse graph are all included above. The branch and existence arguments make explicit conditions left compressed in the lecture. Q1–Q5 are generated applications, not quoted MIT assessment questions. The original cover points to [MIT OCW's terms and citation information](https://ocw.mit.edu/terms/).
