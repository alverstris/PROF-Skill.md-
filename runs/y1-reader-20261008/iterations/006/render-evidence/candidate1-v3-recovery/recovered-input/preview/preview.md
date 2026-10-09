<!-- P001 -->
Exponential and logarithmic differentiation

<!-- P002 -->
MIT 18.01, Fall 2006, Lecture 6

<!-- P003 -->
This lesson develops one useful connection: taking a logarithm turns a changing power into a product, and its derivative measures relative change. You will derive the exponential and logarithm derivative rules, use them when both a base and an exponent vary, and evaluate a limit by recognising a derivative.

<!-- P004 -->
Reading route: read Parts 1–5 in order and try A1–A5 where they occur. Keep any partial working; the [hints](#hints) give a next step and the [solutions](#solutions) give complete reasoning in a separate group. Use [A6](#task-a6) on a later return. The source and its corrections are recorded at the end.

<!-- P005 -->
Starting tools: the derivative is a tangent slope or instantaneous rate, defined by a difference quotient; the product rule is $(uv)'=u'v+uv'$; and the chain rule is $(F(u(x)))'=F'(u(x))u'(x)$. We use ordinary algebra, limits, continuous functions, exponent laws, and the meaning of an inverse function. The needed connections to logarithms are developed below. All quantities in powers and logarithms are real, and logarithm inputs must be positive.

<a id="part-1"></a>

<!-- P006 -->
Part 1: why an exponential's derivative is proportional to itself

<!-- P007 -->
Start with a fixed base $a\gt 1$, as in the lecture. In $a^x$, $a$ stays fixed while $x$ changes. The exponent laws give

<!-- P008 -->
$$
a^0=1,\qquad a^1=a,\qquad a^2=a\cdot a,
$$

<!-- P009 -->
$$
a^{x_1+x_2}=a^{x_1}a^{x_2},\qquad (a^{x_1})^{x_2}=a^{x_1x_2}.
$$

<!-- P010 -->
For integers $p$ and positive integers $q$, $a^{p/q}=\sqrt[q]{a^p}$. Extending from rational exponents to real ones by continuity gives the real exponential family. We use its usual differentiability; constructing that family rigorously is not this lesson's task.

<!-- P011 -->
Write $h$ for a small nonzero change in $x$. The lecture writes $\Delta x$ for the same change. At a fixed $x$, the difference quotient is

<!-- P012 -->
$$
\frac{a^{x+h}-a^x}{h}
=a^x\frac{a^h-1}{h}.
$$

<!-- P013 -->
The exponent law factors $a^{x+h}$ as $a^xa^h$. While $h$ tends to zero, $a^x$ is constant, so it can be taken outside the limit. Define

<!-- P014 -->
$$
M(a)=\lim_{h\to0}\frac{a^h-1}{h}.
$$

<!-- P015 -->
$M$ is a function of the base: it assigns each base its slope at $x=0$. It is a constant with respect to $x$ when that base is fixed. The definition now gives

<!-- P016 -->
$$
\frac{d}{dx}a^x=M(a)a^x.
$$

<!-- P017 -->
To read this formula, multiply the current height $a^x$ by the base's fixed factor $M(a)$ to get the slope there. To construct it from the graph, first take the tangent slope at $(0,1)$; that number is $M(a)$, because $a^0=1$. Then the slope at any other $x$ is that number times the height. This is the relationship shown by the lecture's first figure.

<!-- P018 -->
The special base $e$

<!-- P019 -->
The natural exponential uses the unique base $e$ for which $M(e)=1$, equivalently

<!-- P020 -->
$$
\lim_{h\to0}\frac{e^h-1}{h}=1.
$$

<!-- P021 -->
We take the existence of this special base as a foundational property of the real exponential family. The lecture's following geometric comparisons motivate where it lies; pictures alone do not prove existence or uniqueness.

<!-- P022 -->
- For $y=2^x$, the secant through $(0,1)$ and $(1,2)$ has slope $(2-1)/(1-0)=1$. The upward-curving graph has a smaller tangent slope at the left endpoint, so $M(2)\lt 1$.
- For $y=4^x$, the secant through $(-1/2,1/2)$ and $(0,1)$ has slope $(1-1/2)/(0-(-1/2))=1$. At the right endpoint the tangent is steeper, so $M(4)\gt 1$.

<!-- P023 -->
These are the comparisons in Figures 2 and 3: a secant measures an average slope between its two points, while a tangent measures the slope at one point. For these strictly upward-curving exponentials, tangent slopes increase along the curve, placing the secant slope between the endpoint tangent slopes. The comparisons locate the slope-one base between 2 and 4 once continuity and increase of $M(a)$ are established. We will identify $M(a)$ explicitly in Part 2, which also verifies those properties. The printed source labels the second secant's right endpoint $(1,0)$; the correct coordinates are $(0,1)$.

<!-- P024 -->
Substituting $M(e)=1$ into the derivative formula yields

<!-- P025 -->
$$
\frac{d}{dx}e^x=e^x.
$$

<!-- P026 -->
The chain rule extends this to a differentiable input $u(x)$:

<!-- P027 -->
$$
\frac{d}{dx}e^{u(x)}=e^{u(x)}u'(x).
$$

<!-- P028 -->
For example, to differentiate $e^{3x}$, the outer function is $e^u$ and the inner input is $u=3x$. The outer derivative is evaluated at that same input, giving $e^{3x}$, and the inner derivative is 3. Thus $(e^{3x})'=3e^{3x}$. Changing how quickly the exponent changes changes how quickly the whole expression changes.

<a id="task-a1"></a>

<!-- P029 -->
Task A1 (generated)

<!-- P030 -->
Let $y=e^{2x-1}$. Find $dy/dx$ and the tangent slope at $x=1/2$. Explain where the factor from the inner expression enters. A complete response connects the chain rule to the factor and evaluates the derivative at the stated point.

<!-- P031 -->
[Hint A1](#hint-a1) · [Solution A1](#solution-a1)

<a id="part-2"></a>

<!-- P032 -->
Part 2: logarithms reverse exponentials

<!-- P033 -->
The natural logarithm answers an inverse question: which exponent of $e$ gives a specified positive number? Thus

<!-- P034 -->
$$
y=e^x\quad\Longleftrightarrow\quad\ln y=x,
$$

<!-- P035 -->
and, with different variable names,

<!-- P036 -->
$$
w=\ln x\quad\Longleftrightarrow\quad e^w=x\qquad(x\gt 0).
$$

<!-- P037 -->
For instance, $\ln(e^3)=3$ and $e^{\ln 5}=5$. The notation $\ln x$ is a function value, not a product of symbols. Since $e^0=1$ and the exponential is increasing, $\ln1=0$, $\ln x\lt 0$ for $0\lt x\lt 1$, and $\ln x\gt 0$ for $x\gt 1$. The logarithm has no real value at zero or at a negative input.

<!-- P038 -->
For positive $u,v$, the exponent law gives the logarithm law

<!-- P039 -->
$$
\ln(uv)=\ln u+\ln v.
$$

<!-- P040 -->
Indeed, put $u=e^r$ and $v=e^s$. Then $uv=e^{r+s}$, so its logarithm is $r+s$. Similarly, for $u\gt 0$ and real $r$, $\ln(u^r)=r\ln u$. Moving an exponent outside the logarithm will be our main simplifying step.

<!-- P041 -->
To obtain the logarithm's derivative, set $w(x)=\ln x$, so $e^{w(x)}=x$. The positive exponential derivative means the inverse has a finite local derivative here. Differentiate this identity with respect to $x$ using the chain rule:

<!-- P042 -->
$$
e^{w(x)}w'(x)=1.
$$

<!-- P043 -->
Since $e^{w(x)}=x\gt 0$, division is permitted, giving

<!-- P044 -->
$$
\frac{d}{dx}\ln x=\frac1x\qquad(x\gt 0).
$$

<!-- P045 -->
The derivative is positive, confirming that $\ln x$ is increasing; differentiability also gives continuity on the positive inputs. For a positive differentiable function $u(x)$, the same chain rule gives

<!-- P046 -->
$$
\frac{d}{dx}\ln(u(x))=\frac{u'(x)}{u(x)}.
$$

<!-- P047 -->
The numerator is the derivative of the entire inner input; the denominator is that input itself. For example, $\ln(1+x^2)$ is defined for every real $x$, and its derivative is $2x/(1+x^2)$. A check at $x=0$ gives zero slope, consistent with the expression being unchanged when $x$ is replaced by $-x$ and with the displayed derivative.

<!-- P048 -->
Returning to a general constant base

<!-- P049 -->
For fixed $a\gt 0$, write $a=e^{\ln a}$. The exponent laws then give

<!-- P050 -->
$$
a^x=(e^{\ln a})^x=e^{x\ln a}.
$$

<!-- P051 -->
This rewrites the same quantity in base $e$; it does not change its value or interchange the base and exponent. Since $\ln a$ is constant with respect to $x$, the chain rule gives

<!-- P052 -->
$$
\frac{d}{dx}a^x=(\ln a)e^{x\ln a}=(\ln a)a^x.
$$

<!-- P053 -->
Comparison with Part 1 identifies $M(a)=\ln a$. In particular $M$ is continuous and strictly increasing for $a\gt 0$, and $M(a)=1$ has the unique solution $a=e$. The previous geometric bracket $2\lt e\lt 4$ is consistent with this identification. This is a check of the slope-based characterisation, not a new construction of $e$ from the pictures.

<!-- P054 -->
Even base 10 brings in the natural logarithm: $(10^x)'=(\ln10)10^x$. The same argument extends the lecture's initial $a\gt 1$ convention to $0\lt a\lt 1$: there $\ln a\lt 0$, so $a^x$ decreases. At $a=1$ the function is constant and the derivative is zero. No corresponding general real-variable rule with a negative base is being claimed.

<a id="task-a2"></a>

<!-- P055 -->
Task A2 (generated)

<!-- P056 -->
Find the derivatives of $f(x)=(1/2)^{3x}$ and $g(x)=\ln(5-2x)$. State the real domain of each function and explain why each derivative is negative throughout its domain. A complete response includes the inner derivative, the domain inequality for the logarithm, and a sign justification.

<!-- P057 -->
[Hint A2](#hint-a2) · [Solution A2](#solution-a2)

<a id="part-3"></a>

<!-- P058 -->
Part 3: logarithmic differentiation when a power changes

<!-- P059 -->
Let $f(x)\gt 0$ be differentiable. The previous chain-rule result says

<!-- P060 -->
$$
(\ln f(x))'=\frac{f'(x)}{f(x)},\qquad
f'(x)=f(x)(\ln f(x))'.
$$

<!-- P061 -->
A prime means differentiation with respect to the current variable, here $x$. In particular $(\ln f)'$ is the derivative of the composite function $x\mapsto\ln(f(x))$. It is not $\ln(f')$. The first formula divides absolute change rate by the current value; the second recovers the absolute rate by multiplying back by that value.

<!-- P062 -->
This gives a procedure: take the logarithm of a positive expression, simplify using logarithm laws, differentiate the simplified expression, and multiply by the original function. Positivity is a condition for taking the real logarithm in this procedure, not a claim that every differentiable function is positive.

<!-- P063 -->
Applied to $f(x)=a^x$, it provides the lecture's second method:

<!-- P064 -->
$$
\ln f=x\ln a,\qquad (\ln f)'=\ln a,
$$

<!-- P065 -->
$$
f'=f\ln a=(\ln a)a^x.
$$

<!-- P066 -->
Here $\ln a$ is fixed. For this short expression, rewriting in base $e$ is equally effective.

<!-- P067 -->
Now consider the lecture's worked example $f(x)=x^x$ on $x\gt 0$. Both the base and exponent change. The ordinary power rule $(x^n)'=nx^{n-1}$ treats $n$ as constant, while the exponential rule $(a^x)'=(\ln a)a^x$ treats $a$ as constant. Neither rule alone applies to the two changing occurrences of $x$.

<!-- P068 -->
Taking the logarithm exposes those two changes as a product:

<!-- P069 -->
$$
\ln f=x\ln x.
$$

<!-- P070 -->
The product rule now gives

<!-- P071 -->
$$
(\ln f)'=1\cdot\ln x+x\cdot\frac1x=\ln x+1.
$$

<!-- P072 -->
Multiplying by the original function recovers

<!-- P073 -->
$$
f'(x)=x^x(\ln x+1)\qquad(x\gt 0).
$$

<!-- P074 -->
For example, at $x=2$ the slope is $4(\ln2+1)$, not 4 from treating the exponent as fixed at 2. Alternatively, $x^x=e^{x\ln x}$, and the chain rule gives precisely the same result. These two methods use the same simplification of the changing power.

<!-- P075 -->
More generally, if $u(x)\gt 0$ and both $u,v$ are differentiable, construct the real power $y=u(x)^{v(x)}$ as $e^{v(x)\ln u(x)}$. Then

<!-- P076 -->
$$
\ln y=v\ln u,\qquad
\frac{y'}{y}=v'\ln u+v\frac{u'}u.
$$

<!-- P077 -->
The first term records the changing exponent; the second records the changing base. Setting $v$ constant removes the first term and recovers the ordinary power rule with the inner derivative. Setting $u$ constant removes the second and recovers the constant-base exponential rule. This connects the methods rather than creating an unrelated formula to memorise.

<a id="task-a3"></a>

<!-- P078 -->
Task A3 (generated)

<!-- P079 -->
For $y=(1+x)^{x^2}$, $x\gt -1$, find $y'$ and the tangent slope at $x=0$. Explain why treating the exponent $x^2$ as constant throughout differentiation would miss a term. A complete response differentiates both changing parts after a justified rewrite and preserves the given domain.

<!-- P080 -->
[Hint A3](#hint-a3) · [Solution A3](#solution-a3)

<a id="part-4"></a>

<!-- P081 -->
Part 4: a limit hidden inside a logarithm

<!-- P082 -->
The lecture asks for the limit of

<!-- P083 -->
$$
b_k=\left(1+\frac1k\right)^k\qquad(k=1,2,3,\ldots).
$$

<!-- P084 -->
The subscript labels the term of a sequence; $k\to\infty$ means considering larger and larger positive integers. Although the base tends to 1, the exponent grows. Replacing the base by its limit too early loses the effect of many repeated factors. Nor can the competing factors $k$ and $\ln(1+1/k)$ be evaluated separately as an ordinary product of finite limits.

<!-- P085 -->
Each $b_k$ is positive, so define $a_k=\ln b_k$. These subscripted letters label sequences; they are not the fixed base $a$ from Part 1. The logarithm law gives

<!-- P086 -->
$$
a_k=k\ln\left(1+\frac1k\right)
=\frac{\ln(1+1/k)}{1/k}.
$$

<!-- P087 -->
The change of variable $h=1/k$ makes $h\to0$ from the positive side. Using $\ln1=0$ gives the exact equality

<!-- P088 -->
$$
a_k=\frac{\ln(1+h)-\ln1}{h}.
$$

<!-- P089 -->
Compare this with the derivative definition $[F(x_0+h)-F(x_0)]/h$: here $F=\ln$ and $x_0=1$. Thus Part 2 supplies the limit

<!-- P090 -->
$$
a_k\longrightarrow (\ln x)'\big|_{x=1}=\frac11=1.
$$

<!-- P091 -->
The vertical bar means evaluate the derivative at the stated input. We have found the logarithm's limit. To recover the original sequence, use the exact inverse relation $b_k=e^{a_k}$ and continuity of the exponential:

<!-- P092 -->
$$
b_k=e^{a_k}\longrightarrow e^1=e.
$$

<!-- P093 -->
Consequently,

<!-- P094 -->
$$
\lim_{k\to\infty}\left(1+\frac1k\right)^k=e.
$$

<!-- P095 -->
We did not assume that $b_k$ already converges in order to take the logarithm of its proposed limit. Instead, we found a convergent sequence $a_k$ and then applied a continuous function to it.

<!-- P096 -->
The lecture's first closing remark uses this formula to approximate $e$. With $k=10$, it gives $(1.1)^{10}\approx2.59374$, whereas $e\approx2.71828$: the estimate is about 4.58% low. It is useful as a rough approximation, and the limit guarantees convergence as $k$ increases; $k=10$ does not give several correct decimal places.

<!-- P097 -->
The same route works with a small negative increment as long as the logarithm's input stays positive: the derivative of $\ln$ at 1 has the same limit from either side. More broadly, if logarithms tend to a finite $L$, exponentiating yields a limit $e^L$. If logarithms instead tend to $+\infty$, the original positive quantities grow without bound because the exponential is increasing and unbounded. If they tend to $-\infty$, the original quantities tend to zero.

<a id="task-a4"></a>

<!-- P098 -->
Task A4 (generated)

<!-- P099 -->
For positive integers $k\gt 2$, let $b_k=(1-2/k)^{3k}$. Find the limit of $\ln(b_k)$, then the limit of $b_k$. Show how $h=-2/k$ converts $\ln(b_k)$ into a multiple of the derivative quotient for $\ln$ at 1, and state the side from which $h$ approaches zero. A complete response distinguishes the logarithm's limit from the original sequence's limit and justifies returning by the exponential.

<!-- P100 -->
[Hint A4](#hint-a4) · [Solution A4](#solution-a4)

<a id="part-5"></a>

<!-- P101 -->
Part 5: relative change explains the usefulness of logarithms

<!-- P102 -->
A fall of 50 points has different significance from a starting level of 300 than from 10000. For positive initial and final levels $F_0,F_1$, the exact finite fractional change is

<!-- P103 -->
$$
\frac{F_1-F_0}{F_0},
$$

<!-- P104 -->
and multiplying by 100 expresses it as a percentage. The denominator is the starting level, not the final level. This is the distinction behind the lecture's final market example; no actual market observation is needed.

<!-- P105 -->
For a positive differentiable level $F(t)$, its instantaneous relative rate is

<!-- P106 -->
$$
\frac{F'(t)}{F(t)}=\frac{d}{dt}\ln(F(t)).
$$

<!-- P107 -->
The prime now denotes differentiation with respect to time $t$. If $F$ is measured in points and time in days, $F'$ has units points per day and $F'/F$ has units per day. Multiplying by 100 gives an instantaneous percentage rate per day. For a physical measurement, read the logarithm as $\ln(F/F_{\rm ref})$ with a fixed positive reference in the same units; its derivative is still $F'/F$, because the reference is constant. This avoids taking a logarithm of a dimensional quantity.

<!-- P108 -->
Why is that an instantaneous percentage rate? The derivative definition gives, for small time increments $\Delta t$,

<!-- P109 -->
$$
F(t+\Delta t)-F(t)\approx F'(t)\Delta t,
$$

<!-- P110 -->
and division by $F(t)\gt 0$ yields

<!-- P111 -->
$$
\frac{F(t+\Delta t)-F(t)}{F(t)}
\approx\frac{F'(t)}{F(t)}\Delta t.
$$

<!-- P112 -->
This is a local approximation, not an exact finite-change rule. The exact finite logarithmic change is $\ln(F_1/F_0)$, which also generally differs from $(F_1-F_0)/F_0$; the two are close for a small fractional change because $(\ln x)'$ at 1 is 1.

<!-- P113 -->
For a worked model, let $F(t)=80e^{0.03t}$, where $t$ is the numerical time in days and $F$ is in points. Its absolute rate is $F'=2.4e^{0.03t}$ points per day. Dividing by its current level gives $F'/F=0.03$ per day, or 3% per day instantaneously. After one day, however, the exact percentage increase is $100(e^{0.03}-1)$, about 3.045%. The level on which growth acts changes during the day. Calling both numbers exactly 3% would confuse a local rate with a finite change.

<a id="task-a5"></a>

<!-- P114 -->
Task A5 (generated mathematical models, not market data)

<!-- P115 -->
Two positive index levels are modelled by $F(t)=300e^{-0.02t}$ and $G(t)=10000e^{-0.02t}$, where $t$ is the numerical time in days. At $t=0$, find each absolute rate in points per day and each instantaneous percentage rate per day. Separately compare the exact finite percentage changes caused by a fall of 50 points from 300 and from 10000. For the model $F$, express its exact percentage change from day 0 to day 1 and explain why it differs from the instantaneous percentage rate multiplied by one day. A complete response states which quantities agree, carries signs and units, and separates exact finite change from local approximation; a symbolic expression in $e$ is sufficient.

<!-- P116 -->
[Hint A5](#hint-a5) · [Solution A5](#solution-a5)

<a id="task-a6"></a>

<!-- P117 -->
Later return: Task A6 (generated)

<!-- P118 -->
Return after a gap, perhaps the next day; adjust the gap to your needs. The first request below retrieves the main relationships. The later requests test using them to choose methods and handle a changed limit. Needing to reopen the lesson identifies a useful place to revisit; it is not evidence about your overall ability.

<!-- P119 -->
First, with the lesson closed, write what $M(a)$ means geometrically and give the relationship between $(\ln f)'$ and $f'$ for positive differentiable $f$. Then reopen the lesson if needed and differentiate $p(x)=x^3$, $q(x)=3^x$ and $r(x)=x^x$ on $x\gt 0$, giving a reason for the method chosen in each case. Finally decide whether $c_k=(1+1/k)^{k^2}$, for positive integers $k$, has a finite limit, and justify the conclusion through its logarithm rather than the misleading substitution 1 raised to an increasing power. A complete response separates recall from transfer, identifies what is constant in each derivative, and controls the growing factor in $\ln(c_k)$.

<!-- P120 -->
[Hint A6](#hint-a6) · [Solution A6](#solution-a6)

<a id="hints"></a>

<!-- P121 -->
Hints

<!-- P122 -->
These hints are grouped separately from the complete solutions. Stop at whichever hint lets you resume your working.

<a id="hint-a1"></a>

<!-- P123 -->
Hint A1

<!-- P124 -->
Put $u=2x-1$. Write the outer derivative as $e^u$, find $u'$, and only then substitute $x=1/2$ into their product.

<!-- P125 -->
[Return to A1](#task-a1)

<a id="hint-a2"></a>

<!-- P126 -->
Hint A2

<!-- P127 -->
Write the first function as $e^{3x\ln(1/2)}$. For the second, solve $5-2x\gt 0$ before differentiating. Its derivative has the inner derivative in the numerator and the positive input in the denominator.

<!-- P128 -->
[Return to A2](#task-a2)

<a id="hint-a3"></a>

<!-- P129 -->
Hint A3

<!-- P130 -->
The given interval makes $1+x$ positive. Begin with $\ln y=x^2\ln(1+x)$. In the product rule, keep one contribution from $(x^2)'$ and another from $(\ln(1+x))'$, then multiply by $y$.

<!-- P131 -->
[Return to A3](#task-a3)

<a id="hint-a4"></a>

<!-- P132 -->
Hint A4

<!-- P133 -->
After taking the logarithm, the expression is $3k\ln(1-2/k)$. Since $h=-2/k$, solve for $k$ as $-2/h$. This exposes a constant multiplying $[\ln(1+h)-\ln1]/h$.

<!-- P134 -->
[Return to A4](#task-a4)

<a id="hint-a5"></a>

<!-- P135 -->
Hint A5

<!-- P136 -->
For either exponential model, first compute its derivative and then divide by the same model's current value. For the separate 50-point falls, use $\Delta F/F_0$ with $\Delta F=-50$. For the one-day model change, find $F(1)/F(0)$ before subtracting 1.

<!-- P137 -->
[Return to A5](#task-a5)

<a id="hint-a6"></a>

<!-- P138 -->
Hint A6

<!-- P139 -->
The point used to define $M(a)$ is $(0,1)$. For the three derivatives, identify whether the base, exponent, or both change. For the last part write $\ln c_k=k[k\ln(1+1/k)]$; Part 4 already establishes the limit of the bracketed factor. A factor tending to 1 is eventually greater than $1/2$.

<!-- P140 -->
[Return to A6](#task-a6)

<a id="solutions"></a>

<!-- P141 -->
Complete solutions

<!-- P142 -->
Compare the first step where your working differs. A missing chain-rule factor, an invalid logarithm input, and confusing a logarithm's limit with the original limit are different problems. The explanations below describe possible errors, not errors you have been observed making.

<a id="solution-a1"></a>

<!-- P143 -->
Solution A1

<!-- P144 -->
The outer function $e^u$ has derivative $e^u$, evaluated at $u=2x-1$. The inner derivative is 2, so

<!-- P145 -->
$$
\frac{dy}{dx}=2e^{2x-1}.
$$

<!-- P146 -->
At $x=1/2$ the exponent is zero and $e^0=1$, giving slope 2. The extra factor records that a change in $x$ changes the exponent at twice that rate. Substituting the point before differentiating would erase the varying function and leave only a number; differentiate first.

<!-- P147 -->
[Return to A1](#task-a1) · [Hint A1](#hint-a1)

<a id="solution-a2"></a>

<!-- P148 -->
Solution A2

<!-- P149 -->
The positive fixed base $1/2$ permits every real $x$. Rewriting $f=e^{3x\ln(1/2)}$ and applying the chain rule gives

<!-- P150 -->
$$
f'(x)=3\ln(1/2)(1/2)^{3x}.
$$

<!-- P151 -->
Here $\ln(1/2)\lt 0$, while 3 and the exponential are positive. Hence $f'\lt 0$ for all real $x$.

<!-- P152 -->
The second function requires $5-2x\gt 0$, or $x\lt 5/2$. On that interval,

<!-- P153 -->
$$
g'(x)=\frac{-2}{5-2x}\lt 0.
$$

<!-- P154 -->
Its numerator is negative and its denominator positive. Merely writing $1/(5-2x)$ would omit the changing input's derivative and predict the wrong sign. The logarithm itself is undefined at $x=5/2$ and beyond, so the derivative formula supplies no real-function derivative there.

<!-- P155 -->
[Return to A2](#task-a2) · [Hint A2](#hint-a2)

<a id="solution-a3"></a>

<!-- P156 -->
Solution A3

<!-- P157 -->
For $x\gt -1$, the base is positive and so is $y=e^{x^2\ln(1+x)}$. Taking its logarithm is valid:

<!-- P158 -->
$$
\ln y=x^2\ln(1+x).
$$

<!-- P159 -->
Use the product and chain rules:

<!-- P160 -->
$$
\frac{y'}y=2x\ln(1+x)+\frac{x^2}{1+x}.
$$

<!-- P161 -->
Thus

<!-- P162 -->
$$
y'=(1+x)^{x^2}\left(2x\ln(1+x)+\frac{x^2}{1+x}\right),\qquad x\gt -1.
$$

<!-- P163 -->
At $x=0$, $y=1$ and both terms in parentheses vanish, giving slope 0. The term $2x\ln(1+x)$ comes from the changing exponent. Treating $x^2$ as constant would lose that term. Evaluating only at zero would hide that particular mistake because the missing term happens to vanish there; the full derivative must still include it.

<!-- P164 -->
[Return to A3](#task-a3) · [Hint A3](#hint-a3)

<a id="solution-a4"></a>

<!-- P165 -->
Solution A4

<!-- P166 -->
For $k\gt 2$, $1-2/k\gt 0$, so the real logarithm is allowed. Taking it gives

<!-- P167 -->
$$
\ln b_k=3k\ln(1-2/k).
$$

<!-- P168 -->
With $h=-2/k$, $h\to0$ from below and $k=-2/h$. Consequently

<!-- P169 -->
$$
\ln b_k=-6\frac{\ln(1+h)-\ln1}{h}\longrightarrow-6.
$$

<!-- P170 -->
The quotient tends to $(\ln x)'$ at 1, which is 1, just as in Part 4; approaching from below is permitted. Finally $b_k=e^{\ln b_k}$, so continuity yields

<!-- P171 -->
$$
b_k\longrightarrow e^{-6}.
$$

<!-- P172 -->
A result of $-6$ for the original limit would miss this last inverse operation and would also conflict with positivity of every $b_k$.

<!-- P173 -->
[Return to A4](#task-a4) · [Hint A4](#hint-a4)

<a id="solution-a5"></a>

<!-- P174 -->
Solution A5

<!-- P175 -->
By the chain rule,

<!-- P176 -->
$$
F'(t)=-0.02F(t),\qquad G'(t)=-0.02G(t).
$$

<!-- P177 -->
At zero, the absolute rates are $-0.02(300)=-6$ points per day and $-0.02(10000)=-200$ points per day. They differ because the starting levels differ. Dividing by the respective levels gives the same relative rate $-0.02$ per day, or $-2\text{ percent}$ per day instantaneously.

<!-- P178 -->
For the separate finite falls, the exact percentages are

<!-- P179 -->
$$
\frac{-50}{300}\times100\text{ percent}=-\frac{50}{3}\text{ percent}\approx-16.67\text{ percent},\qquad
\frac{-50}{10000}\times100\text{ percent}=-0.5\text{ percent}.
$$

<!-- P180 -->
These are changes, not rates, because no elapsed time is specified for those falls. They are comparisons separate from the two exponential models.

<!-- P181 -->
For $F$ over one day, $F(1)/F(0)=e^{-0.02}$, so its exact percentage change is

<!-- P182 -->
$$
100(e^{-0.02}-1)\text{ percent}\approx-1.9801\text{ percent}.
$$

<!-- P183 -->
The initial relative rate times one day gives $-2\text{ percent}$, a local approximation. As the level falls, its absolute loss rate also becomes smaller in magnitude. The exact one-day fall is therefore slightly smaller than 2% of its starting level. Equal instantaneous percentage rates do not make finite percentages exactly equal to the rate times elapsed time.

<!-- P184 -->
[Return to A5](#task-a5) · [Hint A5](#hint-a5)

<a id="solution-a6"></a>

<!-- P185 -->
Solution A6

<!-- P186 -->
The recall targets are the tangent slope of $y=a^x$ at $(0,1)$, called $M(a)$, and $(\ln f)'=f'/f$ for positive differentiable $f$. Equivalently $f'=f(\ln f)'$. Also $M(a)=\ln a$.

<!-- P187 -->
For $p=x^3$, the exponent is the fixed number 3, so the power rule gives $p'=3x^2$. For $q=3^x$, the base is fixed, so $q'=(\ln3)3^x$. For $r=x^x$, both parts change; logarithmic differentiation or rewriting as $e^{x\ln x}$ gives $r'=x^x(\ln x+1)$. Alternative correct methods are acceptable if they account for every changing part and preserve the domain $x\gt 0$.

<!-- P188 -->
For the sequence, take a logarithm:

<!-- P189 -->
$$
\ln c_k=k^2\ln(1+1/k)
=k\left[k\ln(1+1/k)\right].
$$

<!-- P190 -->
The bracketed factor tends to 1 by Part 4. To make the conclusion precise, it is greater than $1/2$ for all sufficiently large $k$, so $\ln c_k\gt k/2$ eventually. Thus $\ln c_k\to+\infty$, and $c_k\to+\infty$ by the exponential's increase without bound. There is no finite limit. The additional factor $k$ in the exponent changes the conclusion from the lecture's $e$ limit; the base approaching 1 does not determine the answer by itself.

<!-- P191 -->
[Return to A6](#task-a6) · [Hint A6](#hint-a6)

<!-- P192 -->
Source and scope

<!-- P193 -->
This lesson covers the complete supplied [MIT OpenCourseWare 18.01 Fall 2006 Lecture 6 PDF](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/f9af0e98490296c99d330faf47389507_lec6.pdf), comprising a cover and printed pages 1–7. The printed title is “Exponential and Log, Logarithmic Differentiation, Hyperbolic Functions.” Hyperbolic functions appear in that title but are not developed anywhere in this PDF; no missing continuation is assumed here.

<!-- P194 -->
The source's worked $x^x$ derivative, exponential limit, three geometric figures and both final remarks are developed above. Tasks A1–A6 are generated applications, not quoted MIT assessment questions. Two source typos are corrected: the point labelled $(1,0)$ in the discussion of $4^x$ and Figure 3 is $(0,1)$, and the inverse box on printed page 4 must read $w=\ln x\Rightarrow e^w=x$. The approximation at $k=10$ is quantified in Part 4, and finite percentage change is distinguished from instantaneous relative rate in Part 5.
