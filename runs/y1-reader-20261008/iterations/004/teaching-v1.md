[P01] Chain rule and higher derivatives

These notes develop MIT 18.01 Lecture 4, dated September 14, 2006: how to differentiate a function of another function, then how to differentiate the result again. The goal is to keep the order of operations, evaluation points and derivative order straight, and to justify the two general rules used below. School differentiation, algebra and induction are available; the necessary connections are included here.

[P02] Reading route

Read [P03]–[P25] in order. Tasks A, B and C appear after the reasoning they use; Task D is a later revisit. Each task links to its own hint and full solution. All [hints](#hints) are grouped after the core, and all [solutions](#solutions) are grouped after the hints, so you can stop at the help you need. The source and the distinction between its proof sketch and the proof here are recorded at [P36].

[P03] One input passes through two functions

In a composition, one function's output becomes the next function's input. Write $`x=g(t)`$ and $`y=f(x)`$: first use $`g`$ on $`t`$, then use $`f`$ on the result. Thus

```math
(f\circ g)(t)=f(g(t)).
```

The symbol $`\circ`$ records this order; it is not multiplication. Starting from the instruction “square the input, then take its sine”, choose $`g(t)=t^2`$ and $`f(x)=\sin x`$, giving $`f(g(t))=\sin(t^2)`$. Conversely, reading $`\sin(t^2)`$ from its inner parentheses identifies exactly those two operations. The composition is defined only for inputs $`t`$ in the domain of $`g`$ whose output $`g(t)`$ belongs to the domain of $`f`$. All trigonometric arguments in these notes are in radians, as required by the sine and cosine derivative formulae used here.

[P04] The rate through the composition

At an input $`t_0`$, assume $`g`$ is differentiable at $`t_0`$, $`f`$ is differentiable at $`g(t_0)`$, and $`f(g(t))`$ is defined for $`t`$ in an open interval about $`t_0`$. The chain rule states

```math
\left.\frac{d}{dt}f(g(t))\right|_{t=t_0}=f'(g(t_0))g'(t_0).
```

A prime means the derivative with respect to that function's own input. The vertical bar means “evaluate at the stated value”. The outer rate $`f'(g(t_0))`$ must be evaluated at the input actually reaching $`f`$, namely $`g(t_0)`$. The inner rate $`g'(t_0)`$ measures how that input changes with $`t`$. Multiplying the rates gives the overall rate. When the hypotheses hold at each input in an interval, the same statement is written

```math
\frac{d}{dt}f(g(t))=f'(g(t))g'(t).
```

In the intermediate-variable notation of [P03], this is $`dy/dt=(dy/dx)(dx/dt)`$, with $`dy/dx`$ evaluated at $`x=g(t)`$. The notation suggests cancellation, but the proof in [P10]–[P13] explains why the rule works even when an intermediate change is zero.

[P05] Worked composition: the lecture's first example

For $`y=\sin(t^2)`$, the outer function is sine and its input is $`x=t^2`$. The familiar derivatives give $`dy/dx=\cos x`$ and $`dx/dt=2t`$. Substitute the actual input into the first factor and multiply:

```math
\frac{dy}{dt}=\left.\cos x\right|_{x=t^2}(2t)=2t\cos(t^2).
```

For example, at $`t=1`$ the intermediate input is $`1`$, the two rates are $`\cos 1`$ and $`2`$, and the overall rate is $`2\cos 1`$. The cosine factor alone would describe change per unit of $`x`$, not per unit of $`t`$. This is why the inner derivative is necessary.

<a id="task-a"></a>

[P06] Task A: use the two rates

Let $`y=\cos(t^2)`$. Find $`dy/dt`$ and its value at $`t=0`$. State the inner input, the derivative of the outer function with respect to that input, and why the final derivative is not just $`-\sin(t^2)`$. A complete response identifies both factors and their evaluation, with a reason for the inner factor. [Hint A](#hint-a) · [Solution A](#solution-a)

[P07] Reversing the order changes the question

For $`f(x)=\sin x`$ and $`g(x)=x^2`$, the two orders give

```math
(f\circ g)(x)=\sin(x^2),\qquad (g\circ f)(x)=(\sin x)^2.
```

The right-hand expression, also written $`\sin^2 x`$, means square the sine value. The left-hand expression squares the input before taking sine. The lecture's composition diagram shows input $`x`$ entering $`g`$, then $`g(x)`$ entering $`f`$, to produce $`f(g(x))`$; it is the first order above. Differentiation preserves the distinction:

```math
\frac{d}{dx}\sin(x^2)=2x\cos(x^2),\qquad \frac{d}{dx}(\sin x)^2=2\sin x\cos x.
```

For the right-hand calculation in this display, the outer function is $`u^2`$ and the inner input is $`u=\sin x`$. Its two factors are therefore $`2u`$ evaluated at $`\sin x`$, and $`\cos x`$.

[P08] What “not commutative” means

Composition is not commutative in general: there is no rule allowing its order to be exchanged without checking. The lecture's sine and square functions really do differ: at $`x=\sqrt{\pi}`$, the first composition is $`\sin\pi=0`$, whereas the second is $`(\sin\sqrt{\pi})^2\gt0`$. Here $`0\lt\sqrt{\pi}\lt\pi`$ and sine is positive between $`0`$ and $`\pi`$. This does not say that every pair has different compositions. For example, $`f(x)=2x`$ and $`g(x)=3x`$ give $`f(g(x))=g(f(x))=6x`$. Check the actual functions and their domains rather than assuming either outcome.

<a id="task-b"></a>

[P09] Task B: use information at the right input

Let $`f`$ and $`g`$ be differentiable at the needed inputs, with the compositions defined nearby. You are given $`f(4)=7`$, $`f'(4)=-2`$, $`g(1)=4`$ and $`g'(1)=3`$. Find the derivative of $`H(t)=f(g(t))`$ at $`t=1`$, identifying exactly which data it uses. Do these data determine the derivative of $`J(t)=g(f(t))`$ at $`t=1`$? Explain what information is missing rather than assuming the orders are interchangeable. A complete response uses the correct evaluation points and justifies its sufficient-or-insufficient decision. [Hint B](#hint-b) · [Solution B](#solution-b)

[P10] Why the rate product is valid

Fix the point $`t_0`$ and set $`x_0=g(t_0)`$ and $`y_0=f(x_0)`$. A nonzero change $`h`$ in the initial input produces an intermediate change $`k`$ and an output change $`\Delta y`$:

```math
h=\Delta t,\qquad k=\Delta x=g(t_0+h)-g(t_0),\qquad \Delta y=f(x_0+k)-f(x_0).
```

Thus the new values are $`t_0+h`$, $`x_0+k`$ and $`y_0+\Delta y`$. The lecture factors the average rate as

```math
\frac{\Delta y}{h}=\frac{\Delta y}{k}\frac{k}{h}.
```

This equality requires $`k\ne0`$. A change in $`t`$ need not change $`g(t)`$: for a constant $`g`$, every $`k`$ is zero. The theorem in [P04] does not exclude constant inner functions, so cancellation alone is not a complete proof. We will keep the rate idea while avoiding division by $`k`$ when it is zero.

[P11] Turn the outer derivative into an exact change formula

The derivative definition says that for nonzero $`k`$ tending to zero,

```math
\frac{f(x_0+k)-f(x_0)}{k}\longrightarrow f'(x_0).
```

Define the difference between this quotient and its limiting value as $`r(k)`$:

```math
r(k)=\frac{f(x_0+k)-f(x_0)}{k}-f'(x_0)\quad(k\ne0),\qquad r(0)=0.
```

By the derivative definition, $`r(k)\to0`$ as $`k\to0`$. Multiplying the nonzero-$`k`$ definition by $`k`$ gives the exact identity

```math
f(x_0+k)-f(x_0)=\bigl(f'(x_0)+r(k)\bigr)k.
```

At $`k=0`$, both sides of this last identity are zero, so it remains true there without division. The function $`r`$ records the error in using the limiting slope for a finite change. No approximation has replaced the actual change: the error term is still included.

[P12] Pass to the limit without an excluded inner increment

We use the elementary limit law that a product of quantities with finite limits tends to the product of those limits. Differentiability of $`g`$ gives $`k/h\to g'(t_0)`$ as nonzero $`h\to0`$. It also gives $`k\to0`$: write $`k=h(k/h)`$ and take the product limit, with the first factor tending to zero and the second to the finite number $`g'(t_0)`$. This is the continuity fact used in the lecture. Consequently $`r(k)\to0`$ along these intermediate inputs: nonzero values of $`k`$ approach zero through the defining derivative limit, and at any zero values we set $`r(0)=0`$.

Substitute $`k=g(t_0+h)-g(t_0)`$ into the exact identity in [P11] and divide only by the nonzero $`h`$:

```math
\frac{f(g(t_0+h))-f(g(t_0))}{h}=\bigl(f'(x_0)+r(k)\bigr)\frac{k}{h}.
```

The factors on the right tend to $`f'(x_0)`$ and $`g'(t_0)`$. Their product therefore tends to $`f'(g(t_0))g'(t_0)`$. The left-hand limit is the derivative of the composition by definition. This proves [P04] with zero intermediate increments included.

[P13] Check the boundary case

If $`g(t)=5`$ for every $`t`$, and $`f`$ is differentiable at $`5`$, then $`f(g(t))=f(5)`$ is constant, so its derivative is zero. The chain rule also gives $`f'(5)\cdot0=0`$. In [P12], $`k=0`$ and the right side is zero for every nonzero $`h`$. The quotient $`\Delta y/k`$ in [P10] would instead be $`0/0`$, which is undefined. This confirms why the repaired proof needs its exact-change form.

[P14] A reciprocal input: the lecture's second example

Consider $`y=\cos(1/x)`$, defined for real $`x\ne0`$. The intermediate input is $`u=1/x`$ and the outer derivative is $`dy/du=-\sin u`$. The reciprocal derivative is $`du/dx=-1/x^2`$; it follows directly from the quotient rule on $`1/x`$: the numerator is $`0\cdot x-1\cdot1=-1`$ and the denominator is $`x^2`$. Hence

```math
\frac{d}{dx}\cos(1/x)=\bigl(-\sin(1/x)\bigr)\left(-\frac1{x^2}\right)=\frac{\sin(1/x)}{x^2},\qquad x\ne0.
```

The two negative factors give the positive sign. The sine input stays $`1/x`$ after taking the outer derivative. No derivative at $`x=0`$ is claimed, because the original function is not defined there.

[P15] One negative power, two valid compositions

Let $`n`$ be a fixed positive integer and $`x\ne0`$. Then $`x^{-n}=(1/x)^n=1/(x^n)`$. These two equal expressions expose different intermediate inputs. First take $`u=1/x`$, followed by the positive-integer power $`u^n`$:

```math
\frac{d}{dx}x^{-n}=n\left(\frac1x\right)^{n-1}\left(-\frac1{x^2}\right)=-n x^{-(n-1)}x^{-2}=-n x^{-n-1}.
```

Alternatively take $`u=x^n`$, followed by the reciprocal $`1/u`$:

```math
\frac{d}{dx}x^{-n}=\left(-\frac1{(x^n)^2}\right)(nx^{n-1})=-n x^{n-1-2n}=-n x^{-n-1}.
```

The reciprocal derivative was established independently in [P14], so neither route assumes the negative-power result it is obtaining. Both use the known positive-integer power rule and the chain rule. Once the power rule is already known for negative integers, applying it directly is shorter; these decompositions explain why it agrees. This argument establishes the result for the stated integer exponents and does not settle real noninteger powers with their additional real-domain restrictions.

[P16] A derivative can itself be differentiated

The first derivative assigns a slope to each input where that derivative exists. Differentiating this slope function gives the second derivative: the rate at which slope changes. For example, if $`p(x)=x^3`$, then $`p'(x)=3x^2`$ and $`p''(x)=6x`$. At $`x=1`$ the original slope is $`3`$ and the slope changes locally at rate $`6`$ per unit of $`x`$.

[P17] Reading and constructing the notation

Write $`D=d/dx`$ for the operation “differentiate with respect to $`x`$”. Applying it twice means $`D^2p=D(Dp)`$. Three times means $`D^3p=D(D(Dp))`$. The notation in the lecture can therefore be read as

```math
p'(x)=(Dp)(x)=\frac{dp}{dx}(x),\qquad p''(x)=(D^2p)(x)=\frac{d^2p}{dx^2}(x).
```

```math
p'''(x)=(D^3p)(x)=\frac{d^3p}{dx^3}(x),\qquad p^{(n)}(x)=(D^np)(x)=\frac{d^np}{dx^n}(x).
```

Here $`n`$ is a positive integer counting differentiations. To express “differentiate $`p`$ three times, then evaluate at $`2`$”, write $`p'''(2)`$ or $`(D^3p)(2)`$. For $`p(x)=x^3`$, this gives $`6`$. In contrast, $`[p'(x)]^2=9x^4`$ squares a derivative value; it does not differentiate again. The superscripts in $`D^2`$, $`p^{(n)}`$ and $`d^np/dx^n`$ record an order of operations, not ordinary powers of the function or algebraic fractions to cancel. Each next derivative is defined only where the derivative function being differentiated has a derivative. Polynomials have all these orders everywhere; existence for an arbitrary function must be checked.

[P18] Repeated differentiation can require more than one rule

Let $`p(x)=\cos(x^2)`$. First use the chain rule:

```math
p'(x)=-2x\sin(x^2).
```

To differentiate again, the expression now has a product: $`-2x`$ times $`\sin(x^2)`$. The product rule says to differentiate each factor in turn while retaining the other. The second factor itself requires the chain rule from [P05]. Thus

```math
p''(x)=(-2)\sin(x^2)+(-2x)\bigl(2x\cos(x^2)\bigr)=-2\sin(x^2)-4x^2\cos(x^2).
```

At $`x=0`$, both terms vanish. This is a rate of change of the first derivative, obtained by two differentiations, not by squaring $`-2x\sin(x^2)`$. Each differentiation starts by inspecting the structure of the current expression.

<a id="task-c"></a>

[P19] Task C: connect the two differentiations

Let $`q(t)=\sin(t^2)`$. Find $`q''(t)`$ and $`q''(0)`$. Label the derivative rule needed when differentiating $`q'(t)`$, and explain why $`q''`$ is not $`[q']^2`$. A complete response gives a connected two-derivative calculation with both product terms and the correct input factors. [Hint C](#hint-c) · [Solution C](#solution-c)

[P20] A pattern worth proving

For $`D=d/dx`$, the lecture computes small cases of differentiating a power exactly as many times as its exponent:

```math
Dx=1,\qquad D^2(x^2)=D(2x)=2.
```

```math
D^3(x^3)=D^2(3x^2)=D(6x)=6.
```

```math
D^4(x^4)=D^3(4x^3)=D^2(12x^2)=D(24x)=24.
```

The coefficients accumulate as products: $`1`$, $`2\cdot1`$, $`3\cdot2\cdot1`$, and $`4\cdot3\cdot2\cdot1`$. For a positive integer $`n`$, their general form is called $`n`$ factorial:

```math
n!=n(n-1)\cdots2\cdot1.
```

In particular, $`1!=1`$ and $`(n+1)!=(n+1)n!`$. The cases suggest $`D^n(x^n)=n!`$, but a finite list alone does not prove a statement for every positive integer.

[P21] Induction connects every case to the next

The claim is: for every positive integer $`n`$, differentiating the function $`x^n`$ exactly $`n`$ times gives the constant $`n!`$. The base case $`n=1`$ is $`Dx=1=1!`$. For the induction step, assume the claim holds for an arbitrary positive integer $`n`$, and consider the next polynomial $`x^{n+1}`$. Take one derivative first; the positive-integer power rule gives $`D(x^{n+1})=(n+1)x^n`$. There are now $`n`$ further derivatives to take:

```math
D^{n+1}(x^{n+1})=D^n\bigl((n+1)x^n\bigr)=(n+1)D^n(x^n)=(n+1)n!=(n+1)!.
```

The factor $`n+1`$ is constant with respect to $`x`$, so it stays outside each of those $`n`$ differentiations. The next equality uses exactly the induction assumption $`D^n(x^n)=n!`$; the last is the factorial definition. The verified first case and this implication establish every positive-integer case by induction. All required derivatives exist because the functions are polynomials.

[P22] What the indices do and do not say

In $`D^n(x^n)=n!`$, the same $`n`$ occurs twice: once as the number of derivatives and once as the original exponent. For example, $`D^3(x^3)=6`$, but $`D^2(x^3)=6x`$ and $`D^4(x^3)=0`$. After the third derivative the result is constant, so another derivative is zero. These examples also explain why derivative order must be specified separately from the function. We have proved the identity for positive integers; no convention about a zeroth derivative is needed here.

<a id="task-d"></a>

[P23] Task D: a later revisit

On a later study occasion, first recall what $`D^3p`$ means and the rule for differentiating $`x^n`$ exactly $`n`$ times for a positive integer $`n`$, without looking at [P17] or [P20]–[P21]. Then let $`p(x)=(2x-1)^3`$. Find $`D^3p`$ and $`(Dp)^3`$, and decide whether the latter could be substituted for the former as an identity in $`x`$. Use either repeated differentiation or polynomial expansion, explaining how your method handles the inner $`2x-1`$. A complete response distinguishes order from power, accounts for the inner slope and justifies the identity decision. [Hint D](#hint-d) · [Solution D](#solution-d)

[P24] Using the revisit

The first part of Task D asks for recall; the transformed polynomial and comparison ask you to transfer the rules to a different expression. Trying it after a break, perhaps the next day, is an adjustable study suggestion, not an optimum schedule. If a step is uncertain, use the matched hint, then compare with the reasoned solution. A wrong expression is most useful when traced to its first changed operation: using the wrong intermediate input, omitting an inner derivative, or replacing repeated differentiation by a power.

[P25] Return points

To rebuild a composition use [P03] and [P07]; to evaluate its derivative use [P04]–[P05]. For the proof and zero-increment issue use [P10]–[P13]. Reciprocal inputs and the two negative-power decompositions are in [P14]–[P15]. For repeated differentiation use [P16]–[P19], and for the all-integer argument use [P20]–[P22]. The tasks are generated applications; the sine-square, reciprocal-cosine, two negative-power routes and factorial proof follow the lecture's topics.

<a id="hints"></a>

[P26] Hints only

This group gives intermediate steps. The complete answers begin at [P31]. Choose the matching task letter; you need not read the next hint to use one.

<a id="hint-a"></a>

[P27] Hint A

Set $`u=t^2`$ so $`y=\cos u`$. Keep the two questions separate: what is $`dy/du`$, and what is $`du/dt`$? In the first answer replace $`u`$ by $`t^2`$, multiply the two factors, and only then set $`t=0`$. [Return to Task A](#task-a) · [Solution A](#solution-a)

<a id="hint-b"></a>

[P28] Hint B

Before substituting numbers, write $`H'(1)=f'(g(1))g'(1)`$. This reveals which input to $`f'`$ is needed. For the reverse order write $`J'(1)=g'(f(1))f'(1)`$ and compare each required input/value with the data. A function value at $`4`$ is not automatically a value or derivative at $`1`$. [Return to Task B](#task-b) · [Solution B](#solution-b)

<a id="hint-c"></a>

[P29] Hint C

Your first derivative should have the product $`2t\cos(t^2)`$. In differentiating it, one product-rule term comes from differentiating $`2t`$; the other comes from differentiating $`\cos(t^2)`$. In that second calculation retain its own inner derivative. Evaluate only after these terms have been formed. [Return to Task C](#task-c) · [Solution C](#solution-c)

<a id="hint-d"></a>

[P30] Hint D

The first derivative is $`Dp=6(2x-1)^2`$. For $`D^3p`$, differentiate that expression twice more; each power of $`2x-1`$ still has an inner derivative. For $`(Dp)^3`$, cube the whole first-derivative expression instead. To disprove an identity between the results, one input at which they disagree is enough. [Return to Task D](#task-d) · [Solution D](#solution-d)

<a id="solutions"></a>

[P31] Complete solutions

These answers include the reasons for the decisive operations. If you wanted only a hint, return to the relevant task before continuing.

<a id="solution-a"></a>

[P32] Solution A

The inner input is $`u=t^2`$, with $`du/dt=2t`$. The outer function is cosine, with $`dy/du=-\sin u`$. Evaluate the outer derivative at the actual intermediate input, then multiply:

```math
\frac{dy}{dt}=(-\sin(t^2))(2t)=-2t\sin(t^2).
```

At $`t=0`$, this is $`0`$. The expression $`-\sin(t^2)`$ gives the outer rate per unit of $`u`$; multiplying by $`2t`$ converts it to the rate per unit of $`t`$. Without that factor the proposed formula is not the derivative as a function of $`t`$, even though both expressions happen to be zero at $`t=0`$. [Return to Task A](#task-a)

<a id="solution-b"></a>

[P33] Solution B

For the first order, the inner output at $`1`$ is $`g(1)=4`$, so the needed outer derivative is $`f'(4)=-2`$. Thus

```math
H'(1)=f'(g(1))g'(1)=f'(4)\cdot3=-6.
```

The value $`f(4)=7`$ gives $`H(1)=7`$ but is not needed for this derivative. For the reversed order the rule gives

```math
J'(1)=g'(f(1))f'(1).
```

The data do not provide $`f(1)`$, $`f'(1)`$ or $`g'`$ at the required input $`f(1)`$. Differentiability does not determine these missing values. The supplied values and slopes therefore suffice for $`H'(1)`$ but do not determine $`J'(1)`$. Exchanging order changes where each rate must be evaluated. [Return to Task B](#task-b)

<a id="solution-c"></a>

[P34] Solution C

The chain rule first gives $`q'(t)=2t\cos(t^2)`$. Apply the product rule to this derivative. Its first factor differentiates to $`2`$; its second differentiates by the chain rule to $`-2t\sin(t^2)`$. Hence

```math
q''(t)=2\cos(t^2)+(2t)(-2t\sin(t^2))=2\cos(t^2)-4t^2\sin(t^2).
```

Since $`\cos0=1`$ and $`\sin0=0`$, $`q''(0)=2`$. The square $`[q'(t)]^2`$ would instead be $`4t^2\cos^2(t^2)`$, obtained by multiplication, not another derivative. It equals $`0`$ at $`t=0`$, so even at that input it disagrees with the second derivative. [Return to Task C](#task-c)

<a id="solution-d"></a>

[P35] Solution D

The notation $`D^3p`$ means three successive differentiations with respect to $`x`$. The recalled identity is $`D^n(x^n)=n!`$ for positive integers $`n`$. For this transformed polynomial, the inner input has derivative $`2`$ at each use of the chain rule:

```math
Dp=6(2x-1)^2,\qquad D^2p=24(2x-1),\qquad D^3p=48.
```

Alternatively expand $`p(x)=8x^3-12x^2+6x-1`$. Three derivatives of its cubic term give $`8\cdot3!=48`$; each lower-degree term reaches zero by the third derivative. This independently explains the same answer. In contrast,

```math
(Dp)^3=\bigl(6(2x-1)^2\bigr)^3=216(2x-1)^6.
```

It cannot replace $`D^3p`$ as an identity: at $`x=1/2`$ this cube is $`0`$, while $`D^3p`$ remains $`48`$. Repeated differentiation and ordinary exponentiation perform different operations. [Return to Task D](#task-d)

[P36] Source and scope

Source: MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, [Lecture 4: Chain Rule and Higher Derivatives](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/b8051c7c7a28e2cd03667de9dd4865fb_lec4.pdf), September 14, 2006. The PDF has a cover and three numbered lecture pages. Its cover directs readers to [MIT OCW terms and citation information](https://ocw.mit.edu/terms/). The composition order, all worked source examples, derivative notation, four small power cases and induction argument are represented above. The exact remainder argument in [P10]–[P13] completes the source's informal quotient proof when an intermediate increment is zero. The stated hypotheses, radian convention and reciprocal-domain restrictions make the conditions of its correct formulae explicit.
