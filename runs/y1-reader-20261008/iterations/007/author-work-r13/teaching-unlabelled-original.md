Lecture 7: hyperbolic functions and choosing differentiation methods

<a name="route"></a>
Reading route

Read the core in order and pause at Q1–Q6 if you want to practise the current connection. Each task links to its own hint and full solution. All hints are grouped after the core; the complete solutions are in a separate group after the hints. Q7 is a later review opportunity. You can bring a partial attempt to the help; there is no need to diagnose your own difficulty first.

The aim is to recognise how a function is built, choose a valid differentiation rule, and explain the important steps and restrictions. The route covers the content of MIT's Lecture 7, including its review material. It assumes the supplied school mathematics baseline, but no earlier lecture notes. In particular, ordinary algebra, exponent laws, trigonometric identities and the basic derivative rules are available. We restate the rules we use and reconstruct the lecture's consequential derivations.

All variables here are real, trigonometric angles are in radians, and $\ln$ means the natural logarithm. A prime means differentiation with respect to $x$, so $y'=dy/dx$. A square root is the nonnegative root. The symbols $\arcsin x$ and $\arctan x$ mean inverse functions, also written $\sin^{-1}x$ and $\tan^{-1}x$ in the source; they do not mean reciprocals. By contrast, $\sec x=1/\cos x$. Conditions beside a formula are part of that formula.

<a name="core"></a>
Hyperbolic sine and cosine from exponentials

Hyperbolic sine, $\sinh$ (read “sinsh”), and hyperbolic cosine, $\cosh$ (read “cosh”), package a difference and a sum of exponentials. For a real input $x$, their definitions are

$$
\sinh x=\frac{e^x-e^{-x}}2,
\qquad
\cosh x=\frac{e^x+e^{-x}}2.
$$

The entire numerator is divided by $2$, and the minus sign in $e^{-x}$ belongs to the exponent. These definitions let us build or unpack either function without a new differentiation rule. Using $(e^x)'=e^x$ and the chain rule, $(e^{-x})'=-e^{-x}$. Therefore

$$
(\sinh x)'=\frac{e^x-(-e^{-x})}{2}=\cosh x,
\qquad
(\cosh x)'=\frac{e^x+(-e^{-x})}{2}=\sinh x.
$$

In the first numerator, subtracting the derivative of $e^{-x}$ produces a plus. In the second, adding that derivative produces a minus. Unlike $(\cos x)'=-\sin x$, the derivative of $\cosh x$ has no leading minus sign. At $x=0$, $\sinh0=0$ and $\cosh0=1$, so these formulas give slopes $1$ and $0$, respectively.

The name “hyperbolic” comes from a coordinate relation. The notation $\cosh^2x$ means $(\cosh x)^2$, not composition. Substitution and difference of squares give

$$
\cosh^2x-\sinh^2x
=\frac{(e^x+e^{-x})^2-(e^x-e^{-x})^2}{4}
=\frac{4e^xe^{-x}}4=1.
$$

Here $(a+b)^2-(a-b)^2=4ab$ and $e^xe^{-x}=1$ explain the cancellation. If we construct a point with coordinates $u=\cosh x$ and $v=\sinh x$, it satisfies $u^2-v^2=1$, the equation of a hyperbola. The point lies on its right branch: $u>0$ from the exponential definition, and $u^2=1+v^2$ then gives $u\ge1$. By comparison, $u=\cos x$, $v=\sin x$ satisfies $u^2+v^2=1$, a circle. The parameter $x$ selects a point; it is not an extra coordinate in either equation. This comparison explains the names, not an assertion that every circular identity keeps the same signs for hyperbolic functions.

<a name="task-q1"></a>
Q1 — generated application

For every real $x$, let $H(x)=\cosh(2x)-\sinh(2x)$, with $\sinh t=(e^t-e^{-t})/2$ and $\cosh t=(e^t+e^{-t})/2$. Find $H'(x)$ in two ways: first simplify $H$ using these definitions, then differentiate the hyperbolic expression directly. Explain why the two derivatives agree. Your response should retain the derivative factor coming from $2x$ and identify whether $H$ is increasing or decreasing.

[Hint Q1](#hint-q1) · [Solution Q1](#solution-q1) · [Continue with differentiation rules](#rules)

<a name="rules"></a>
Reading a function before differentiating

For differentiable functions $u=u(x)$ and $v=v(x)$, and a constant $c$, the familiar rules are

$$
(u+v)'=u'+v',\qquad(cu)'=cu',\qquad(uv)'=u'v+uv',
$$

$$
\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}\quad(v\ne0),
\qquad
\frac d{dx}f(u(x))=f'(u(x))u'(x).
$$

The last formula says to differentiate the outer function $f$ with respect to its input, evaluate that derivative at the inner input $u(x)$, then multiply by the rate of change of $u$. Thus for $\sin(3x)$ the outside operation is sine and the inside input is $3x$: its derivative is $\cos(3x)\cdot3$. In a product, both factors vary, which is why both product-rule terms are needed. A constant has derivative zero.

To choose the first rule, identify the operation performed last when constructing the function. For $x\sin x$, that operation multiplies two quantities. For $\sin(x^2)$, it applies sine to one quantity. If the intended construction is “square $x$, then take its sine”, write $\sin(x^2)$; $[\sin x]^2$ would mean “take sine, then square”. Their derivatives, $2x\cos(x^2)$ and $2\sin x\cos x$, keep these different constructions visible.

The quotient rule can be recovered rather than memorised in isolation. On an interval where $v\ne0$, write $u/v=uv^{-1}$. Product and chain rules, with the power rule for $t^{-1}$, give

$$
(uv^{-1})'=u'v^{-1}+u(-v^{-2}v')
=\frac{u'}v-\frac{uv'}{v^2}
=\frac{u'v-uv'}{v^2}.
$$

This derivation explains the order of the subtraction and the squared denominator. It also shows that product plus chain rules are a valid alternative to a separately recalled quotient rule. As a worked case, if $R(x)=x/(1+x^2)$, the denominator is always positive and

$$
R'(x)=\frac{1(1+x^2)-x(2x)}{(1+x^2)^2}
=\frac{1-x^2}{(1+x^2)^2}.
$$

At $x=0$ the slope is $1$. More generally, the numerator determines the sign because the denominator is positive: this derivative is positive when $|x|<1$ and negative when $|x|>1$.

<a name="task-q2"></a>
Q2 — generated application

For real $x$, let $F(x)=(x^2+1)\sin(3x)$ and $G(x)=\sin(3x)/(x^2+1)$. Differentiate both. Before calculating, state the outermost operation in each expression and the corresponding first differentiation rule. State their real domains and identify where the inner factor $3$ enters each derivative. A correct final formula without these decisions is not a complete response.

[Hint Q2](#hint-q2) · [Solution Q2](#solution-q2) · [Continue with implicit relations](#implicit)

<a name="implicit"></a>
Differentiating a relation without solving it first

An equation linking $x$ and $y$ may describe a curve without specifying one global function $y(x)$. Implicit differentiation finds a slope on a part of the curve where $y$ can be treated locally as a differentiable function of $x$. Every occurrence of $y$ then changes with $x$. For example, $(y^3)'=3y^2y'$, whereas $(x^3)'=3x^2$ because $x'=1$.

The source's worked relation is $y^3+3xy^2=8$. Differentiate both sides with respect to $x$. The second term is a product, so its derivative is $3y^2+6xyy'$. Collecting the terms containing $y'$ gives

$$
3y^2y'+3y^2+6xyy'=0,
\qquad
(3y^2+6xy)y'=-3y^2,
$$

$$
y'=\frac{-3y^2}{3y^2+6xy}
\quad\text{where }3y^2+6xy\ne0.
$$

The slope can depend on both coordinates because different points can share an $x$-coordinate. For a concrete interpretation, $(0,2)$ is on this curve because $2^3+0=8$. Substitution into the slope formula gives $y'=-12/12=-1$, and the tangent there is $y-2=-x$. This point and tangent are an added illustration of the source calculation.

If the coefficient of $y'$ vanishes, do not divide by it. Return to the undivided equation and the curve. A failed division does not by itself prove that no tangent exists; a curve can have a vertical tangent, which has no finite $dy/dx$. It may also require a different local analysis. Keeping this condition prevents a formula from being used beyond the step that justified it.

<a name="task-q3"></a>
Q3 — generated application

The real curve $x^2+y^2=5$ contains $(1,2)$ and $(1,-2)$. Regard $y$ as a differentiable function of $x$ locally near each of those points. Obtain one implicit expression for $y'$ and use it to find both slopes. Explain why the two points need not have the same slope despite their common $x$-coordinate. Identify the points on this curve where your division for $y'$ fails, and say what that failure alone allows you to conclude.

[Hint Q3](#hint-q3) · [Solution Q3](#solution-q3) · [Continue with inverse functions](#inverses)

<a name="inverses"></a>
Inverse functions: the branch supplies the sign

An inverse function reverses an input-output relation on a chosen one-to-one branch. The principal arcsine has $y=\arcsin x$ in $[-\pi/2,\pi/2]$, with $x\in[-1,1]$, and therefore $\sin y=x$. On the interior $-1<x<1$, implicit differentiation gives

$$
(\cos y)y'=1,\qquad y'=\frac1{\cos y}.
$$

To express the answer in $x$, use $\cos^2y=1-\sin^2y=1-x^2$. Squaring alone would allow either sign for $\cos y$. The selected interval has $\cos y>0$ in its interior, so the appropriate root is positive:

$$
(\arcsin x)'=\frac1{\sqrt{1-x^2}},\qquad -1<x<1.
$$

The function is defined at $x=\pm1$, but this finite-derivative formula applies only inside that interval. The square-root sign comes from the inverse branch, not from a rule that a cosine is always positive.

For the principal arctangent, $y=\arctan x$ lies in $(-\pi/2,\pi/2)$ and $\tan y=x$. Using $(\tan y)'$ with the chain rule and $\sec^2y=1+\tan^2y$ gives

$$
\sec^2y\,y'=1,
\qquad
(\arctan x)'=\frac1{1+x^2},\qquad x\in\mathbb R.
$$

There is no zero denominator for real $x$. In both examples the procedure is to write the original-function equation, differentiate with $y$ depending on $x$, then use the equation and the chosen branch to remove $y$.

<a name="task-q4"></a>
Q4 — generated application

Define $y=\arccos x$ by $\cos y=x$ with $y\in[0,\pi]$. For $-1<x<1$, derive $y'$ by implicit differentiation and express it solely in $x$. Justify the square-root sign using the specified interval for $y$. State the interval on which your derivative formula is finite and explain why its sign differs from that of the principal arcsine derivative.

[Hint Q4](#hint-q4) · [Solution Q4](#solution-q4) · [Continue with formula reconstruction](#reconstruct)

<a name="reconstruct"></a>
Reconstructing the specific formulas in the review

The source asks for the derivatives of $x^n$, $\sin^{-1}x$, $\tan^{-1}x$, $\sin x$, $\cos x$, $\tan x$, $\sec x$, $e^x$ and $\ln x$, together with ways to deduce them from previous information. The inverse formulas have just been reconstructed. The remaining connections below explain what information each calculation uses; they are not a claim that every foundational limit is proved here.

For sine and cosine, the source supplies these two limits in radians:

$$
\lim_{h\to0}\frac{\sin h}{h}=1,
\qquad
\lim_{h\to0}\frac{\cos h-1}{h}=0.
$$

The derivative is the limit of slopes of chords as their horizontal separation $h$ tends to zero:

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h.
$$

Here $x$ is fixed while taking the limit; $h$ is the varying increment and is nonzero in the quotient. The source also writes this increment as $\Delta x$. It is the same role under a different symbol. To obtain the sine derivative, use the addition identity $\sin(x+h)=\sin x\cos h+\cos x\sin h$:

$$
\frac{\sin(x+h)-\sin x}{h}
=\sin x\frac{\cos h-1}{h}+\cos x\frac{\sin h}{h}.
$$

Taking the two supplied limits gives $\sin x\cdot0+\cos x\cdot1=\cos x$. This is an exact derivative calculation. A small-angle approximation at a finite $h$ would not by itself be the same justification.

<a name="task-q5"></a>
Q5 — source review request with an explicit response criterion

Starting from the derivative definition, derive $d(\cos x)/dx$ for real $x$ without invoking the cosine derivative as a known rule. Use radians and the supplied facts $\cos(x+h)=\cos x\cos h-\sin x\sin h$, $\lim_{h\to0}(\sin h)/h=1$, and $\lim_{h\to0}(\cos h-1)/h=0$. Your response should display the difference quotient reorganised into those two limits and explain which factors stay fixed as $h$ tends to zero.

[Hint Q5](#hint-q5) · [Solution Q5](#solution-q5) · [Continue with the other formulas](#other-formulas)

<a name="other-formulas"></a>
The other formulas and their dependencies

Using the established rules $(\sin x)'=\cos x$ and $(\cos x)'=-\sin x$, quotient and reciprocal differentiation give

$$
(\tan x)'=\left(\frac{\sin x}{\cos x}\right)'
=\frac{\cos^2x+\sin^2x}{\cos^2x}=\sec^2x,
$$

$$
(\sec x)'=((\cos x)^{-1})'
=-(\cos x)^{-2}(-\sin x)
=\frac{\sin x}{\cos^2x}=\tan x\sec x.
$$

Both require $\cos x\ne0$. The last equality for secant uses $\tan x=\sin x/\cos x$ and $\sec x=1/\cos x$, so the factored answer represents the same quotient. This is the secant calculation shown in the source, with the two minus signs exposed.

For the exponential, a foundational fact associated with the base $e$ is $\lim_{h\to0}(e^h-1)/h=1$. Taking that fact as given, the exponent law $e^{x+h}=e^xe^h$ shows why the derivative equals the original function:

$$
\frac{e^{x+h}-e^x}{h}=e^x\frac{e^h-1}{h}
\quad\Longrightarrow\quad
(e^x)'=e^x,\qquad x\in\mathbb R.
$$

The limit is stated as a premise here; this is not a construction or existence proof of the number $e$. It is equivalent to the familiar exponential's slope $1$ at input $0$, and recovers the derivative rule already used above. For the logarithm, take $y=\ln x$ with $x>0$. The inverse relation $e^y=x$ gives $e^yy'=1$, and hence

$$
(\ln x)'=\frac1{e^y}=\frac1x,\qquad x>0.
$$

For positive integers $n$, the power rule follows by applying the product rule to the $n$ factors in $x^n$: each term is $x^{n-1}$, giving $nx^{n-1}$. For $n=0$, $x^0=1$ on $x\ne0$ has derivative zero. Negative integer powers follow by the reciprocal rule away from $0$. Rational powers can be justified by implicit differentiation: if $r=p/q$, with integers $p$, $q>0$, then on $x>0$ the positive function $y=x^{p/q}$ satisfies $y^q=x^p$. Thus

$$
qy^{q-1}y'=px^{p-1},
\qquad
y'=\frac pq\frac{x^{p-1}}{x^{p(q-1)/q}}
=\frac pqx^{p/q-1}.
$$

The positive domain makes the powers and the division unambiguous. For particular integer or rational powers the real domain may extend to negative inputs, and individual cases at $0$ may also be differentiable. That extension is a separate domain check; it is not supplied by a derivation using $\ln x$.

<a name="real-powers"></a>
A fixed real exponent: two routes to the same power rule

The lecture's remaining issue is a fixed real exponent $r$, which need not be rational. Work on $x>0$. Real powers on this domain have the exponential representation $x^r=e^{r\ln x}$. Reading this representation means “take the logarithm of the input, multiply by the fixed number $r$, then exponentiate”. Conversely, that sequence constructs $e^{r\ln x}$ and gives the original positive-base power $x^r$.

The first route is to differentiate that composition directly:

$$
\frac d{dx}x^r
=\frac d{dx}e^{r\ln x}
=e^{r\ln x}\frac r x
=x^r\frac r x
=rx^{r-1},\qquad x>0.
$$

The second route is logarithmic differentiation: take the logarithm of a positive function to make a power easier to handle, differentiate, then recover the derivative of the original function. The chain rule gives $(\ln f)'=f'/f$ when $f>0$. For $f=x^r>0$,

$$
\ln f=r\ln x,
\qquad
\frac{f'}f=\frac r x,
\qquad
f'=f\frac r x=x^r\frac r x=rx^{r-1}.
$$

The intermediate $f'/f$ is a ratio of the derivative to the function, not the derivative itself. Multiplying by $f$ is necessary to finish. Both methods use the same exponential-logarithm relationship; either is sufficient. For example, $f=x^\pi$ on $x>0$ gives $f'=\pi x^{\pi-1}$. The fixed exponent $\pi$ is allowed even though it is irrational. If the exponent varies with $x$, differentiating it creates an additional term; the fixed-$r$ step cannot simply be reused.

<a name="task-q6"></a>
Q6 — generated application

On $x>0$, compare $f(x)=x^{\sqrt2}$ and $g(x)=(\sqrt2)^x$, where $\sqrt2$ is the positive square root of $2$ and is a constant. Differentiate both, using an exponential or logarithmic rewriting to justify each answer. State what stays fixed and what varies in each function. A response that applies the same power-rule template to both without a justification is incomplete.

[Hint Q6](#hint-q6) · [Solution Q6](#solution-q6) · [Continue with the final source example](#integration)

<a name="integration"></a>
Putting the decisions together

The source ends with $E(x)=e^{x\tan^{-1}x}$. In our notation this is $E(x)=\exp(x\arctan x)$, where $\exp(t)=e^t$ and the whole product $x\arctan x$ is the exponent. To construct it, first obtain $x$ and its arctangent, multiply them, then use that product as the exponential's input. It is not the product $e^x\arctan x$.

The outermost operation selects the chain rule. Set $w(x)=x\arctan x$, so $E'=e^ww'$. The inner operation is a product, so

$$
w'=1\cdot\arctan x+x\frac1{1+x^2}.
$$

Substitute the original exponent back into the derivative:

$$
E'(x)=e^{x\arctan x}
\left(\arctan x+\frac{x}{1+x^2}\right),
\qquad x\in\mathbb R.
$$

This is the source's final result, with its inverse notation translated. At $x=0$, the bracket is zero and $E(0)=1$, so the tangent is horizontal there. Every component is defined and differentiable for real $x$, which licenses the rule combination on that whole domain. The source's promise of differentiating “anything” is motivational: differentiation still requires the function and relevant derivatives to exist.

<a name="task-q7"></a>
Q7 — later retrieval and a changed combination

After leaving the main explanation for a while, try this with the core closed initially. A later session or the next day is one adjustable option, not a universal best interval. Part (a) revisits a previously taught derivation; part (b) applies the methods to a changed expression. Use the help after recording whatever you can reconstruct.

(a) Reconstruct the derivative of $y=\arcsin x$ from $\sin y=x$, giving its finite-derivative domain and the reason for the square-root sign. (b) For real $x$, differentiate $J(x)=\exp(x\arctan x)/(1+x^2)$. In (b), explain your choice of outermost rule and show the needed derivative of the exponent. An unsimplified but correct expression with justified decisions is acceptable.

[Hint Q7](#hint-q7) · [Solution Q7](#solution-q7) · [Return to reading route](#route)

Source and task provenance

The assigned source is MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, “Lecture 7: Continuation and Exam Review”, [original lecture PDF](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/a30756fe9d577184f205b09bc6d6d005_lec7.pdf). Its four numbered teaching pages follow one cover page. Hyperbolic definitions and identity come from printed page 1; the general rules, implicit curve and arcsine from page 2; specific derivative review and both real-power methods from page 3; the exponential of $x\arctan x$ from page 4. Q5 restates a request on printed page 3 with a more explicit response criterion. Q1–Q4 and Q6–Q7 are generated applications, not historical exam questions. Added domains, branch explanations and worked interpretations make the route explicit. The source's “Exam 1 Review” label describes that course document; it does not establish anyone's current assessed syllabus.

<a name="hints"></a>
Hints — intermediate steps only

Choose the named hint for the task you are working on. The full solutions start in a separate group after all seven hints. [Return to core](#core) · [Go to full solutions](#solutions)

<a name="hint-q1"></a>
Hint Q1

Write both fractions for input $2x$ over the same denominator before subtracting. In the direct route, use $(\cosh u)'=\sinh u\,u'$ and $(\sinh u)'=\cosh u\,u'$ with $u=2x$. Compare what is left with the original difference $H$; the sign of an exponential will decide monotonicity.

[Return to Q1](#task-q1) · [Solution Q1](#solution-q1)

<a name="hint-q2"></a>
Hint Q2

Use $A=x^2+1$ and $B=\sin(3x)$. The two requested functions are $AB$ and $B/A$, so the numerator and denominator roles in the second formula differ from the first product. Compute $A'$ and $B'$ separately, then place them into the selected rule before simplifying.

[Return to Q2](#task-q2) · [Solution Q2](#solution-q2)

<a name="hint-q3"></a>
Hint Q3

Differentiate the relation into $2x+2yy'=0$. The coefficient by which you would divide is $2y$. Evaluate the resulting slope at both full points, not just at $x=1$. To find where division fails, combine $y=0$ with the original circle equation.

[Return to Q3](#task-q3) · [Solution Q3](#solution-q3)

<a name="hint-q4"></a>
Hint Q4

Differentiate $\cos y=x$ to obtain an equation involving $-\sin y$ and $y'$. Express $\sin^2y$ using $\cos y=x$. In the interior of the specified branch, $0<y<\pi$; check the sign of sine there before taking a root.

[Return to Q4](#task-q4) · [Solution Q4](#solution-q4)

<a name="hint-q5"></a>
Hint Q5

After substituting the addition identity into $[\cos(x+h)-\cos x]/h$, collect the two terms containing $\cos x$. One part will contain $(\cos h-1)/h$; the other will contain $\sin h/h$. The factors depending only on $x$ can stay outside the respective limits.

[Return to Q5](#task-q5) · [Solution Q5](#solution-q5)

<a name="hint-q6"></a>
Hint Q6

For $f$, write $e^{\sqrt2\ln x}$. For $g$, write $e^{x\ln\sqrt2}$. The quantities inside these two exponentials have different derivatives because $\sqrt2$ and $\ln\sqrt2$ are constants but $x$ and $\ln x$ vary.

[Return to Q6](#task-q6) · [Solution Q6](#solution-q6)

<a name="hint-q7"></a>
Hint Q7

For (a), the first differentiated relation is $\cos y\,y'=1$; the inverse branch determines the sign when eliminating $y$. For (b), name the numerator $N=e^w$ with $w=x\arctan x$ and the denominator $D=1+x^2$. Obtain $w'$ first, then $N'$, and finally assemble $(N'D-ND')/D^2$.

[Return to Q7](#task-q7) · [Solution Q7](#solution-q7)

<a name="solutions"></a>
Full solutions — complete reasoning

These solutions follow the task numbers. If you want another attempt first, use [the hint group](#hints) or the return link beside the relevant solution.

<a name="solution-q1"></a>
Solution Q1

Subtracting the defining fractions cancels $e^{2x}$ and doubles $e^{-2x}$:

$$
H(x)=\frac{e^{2x}+e^{-2x}-(e^{2x}-e^{-2x})}{2}=e^{-2x}.
$$

The chain rule gives $H'=-2e^{-2x}$. Directly from the hyperbolic functions, $H'=2\sinh(2x)-2\cosh(2x)=-2H(x)$. Since $H=e^{-2x}$, the two answers are identical. The derivative is strictly negative for every real $x$, so $H$ is decreasing everywhere. Omitting either inner factor $2$ would change the rate; a sign error in subtracting the second numerator would change the function itself.

[Return to Q1](#task-q1) · [Hint Q1](#hint-q1)

<a name="solution-q2"></a>
Solution Q2

The last operation in $F$ is multiplication, so use the product rule. For $G$ it is division, so use the quotient rule, or its product-with-reciprocal equivalent. Set $A=x^2+1$, $B=\sin(3x)$; then $A'=2x$ and $B'=3\cos(3x)$. Thus

$$
F'=2x\sin(3x)+3(x^2+1)\cos(3x),
$$

$$
G'=\frac{3(x^2+1)\cos(3x)-2x\sin(3x)}{(x^2+1)^2}.
$$

Both functions have all real numbers as their domains because sine is defined everywhere and $x^2+1>0$. The factor $3$ belongs to the derivative of the inner input $3x$; it appears in the terms where $B$ is differentiated. Multiplying $F$ by a reciprocal to construct $G$ changes the differentiation structure as well as the value.

[Return to Q2](#task-q2) · [Hint Q2](#hint-q2)

<a name="solution-q3"></a>
Solution Q3

The differentiated relation is $2x+2yy'=0$. For $y\ne0$, it gives $y'=-x/y$. Hence the slope at $(1,2)$ is $-1/2$, whereas at $(1,-2)$ it is $1/2$. These are different local branches of the circle; an $x$-coordinate alone does not identify a point or slope.

Division fails when $y=0$. The original relation then gives $x=\pm\sqrt5$, so the points are $(\sqrt5,0)$ and $(-\sqrt5,0)$. Failure of division alone tells us the displayed quotient cannot be evaluated there; it does not establish absence of a tangent. In this case the undivided equation would require $2x=0$ if a finite $y'$ existed, which is impossible at either point. The circle has vertical tangents there: its radius is horizontal and the tangent is perpendicular to the radius. Thus the missing finite slope has a geometric explanation.

[Return to Q3](#task-q3) · [Hint Q3](#hint-q3)

<a name="solution-q4"></a>
Solution Q4

Differentiate the defining relation to obtain $-\sin y\,y'=1$. For $-1<x<1$, the branch gives $0<y<\pi$, so $\sin y>0$. From $\sin^2y=1-\cos^2y=1-x^2$ we therefore get $\sin y=\sqrt{1-x^2}$ and

$$
y'=-\frac1{\sqrt{1-x^2}},\qquad -1<x<1.
$$

This is finite throughout that open interval. Although arccosine is defined at both endpoints, the denominator vanishes there. The negative sign comes from differentiating cosine in $\cos y=x$; the principal branch makes the sine factor positive. For arcsine, differentiating $\sin y=x$ gives a positive cosine factor on its principal branch, hence a positive derivative instead.

[Return to Q4](#task-q4) · [Hint Q4](#hint-q4)

<a name="solution-q5"></a>
Solution Q5

Substitute the supplied addition identity and group terms:

$$
\frac{\cos(x+h)-\cos x}{h}
=\cos x\frac{\cos h-1}{h}-\sin x\frac{\sin h}{h}.
$$

With $x$ fixed, $\cos x$ and $\sin x$ are constants in this limit. The given limits yield $\cos x\cdot0-\sin x\cdot1=-\sin x$. Thus $(\cos x)'=-\sin x$ for every real $x$, in radians. The subtraction in the addition formula is what produces the minus sign; no cosine derivative was needed as a premise for this calculation.

[Return to Q5](#task-q5) · [Hint Q5](#hint-q5)

<a name="solution-q6"></a>
Solution Q6

For $f$, the exponent $\sqrt2$ is fixed and the base $x$ varies. On $x>0$, $f=e^{\sqrt2\ln x}$, so the chain rule gives

$$
f'=e^{\sqrt2\ln x}\frac{\sqrt2}{x}=\sqrt2\,x^{\sqrt2-1}.
$$

For $g$, the base $\sqrt2$ is fixed and the exponent $x$ varies. Rewriting $g=e^{x\ln\sqrt2}$ gives

$$
g'=e^{x\ln\sqrt2}\ln\sqrt2=(\sqrt2)^x\ln\sqrt2.
$$

The logarithm of the fixed base is a constant. These formulas hold on the requested positive domain; the second also extends to all real $x$. The power-rule exponent factor in $f'$ and the logarithm factor in $g'$ come from different inner derivatives. Confusing the roles of base and exponent would be a conceptual error, distinct from an arithmetic slip after the correct rewriting.

[Return to Q6](#task-q6) · [Hint Q6](#hint-q6)

<a name="solution-q7"></a>
Solution Q7

(a) On the principal branch $y\in[-\pi/2,\pi/2]$, differentiating $\sin y=x$ gives $\cos y\,y'=1$. For $-1<x<1$, $\cos y>0$ and $\cos^2y=1-x^2$, so $y'=1/\sqrt{1-x^2}$. Its finite-derivative domain is $(-1,1)$. The branch supplies the positive cosine, which is the reason for the positive root.

(b) The outermost operation in $J$ is division. Let $N=e^w$, $w=x\arctan x$, and $D=1+x^2$. Product and chain rules give

$$
w'=\arctan x+\frac{x}{1+x^2},
\qquad N'=e^ww',\qquad D'=2x.
$$

The denominator is positive for every real $x$, so the quotient rule is valid everywhere:

$$
J'=\frac{e^w\left(\arctan x+\frac{x}{1+x^2}\right)(1+x^2)-e^w(2x)}{(1+x^2)^2}
=\frac{e^{x\arctan x}\big((1+x^2)\arctan x-x\big)}{(1+x^2)^2}.
$$

The first expression already answers the task; the second merely collects terms. A product-rule solution using $(1+x^2)^{-1}$ is equally valid. At $x=0$, either expression gives zero. If an attempt used the derivative of the numerator alone, the first missing step would be accounting for the varying denominator; repair that rule choice before simplifying.

[Return to Q7](#task-q7) · [Hint Q7](#hint-q7) · [Return to reading route](#route)
