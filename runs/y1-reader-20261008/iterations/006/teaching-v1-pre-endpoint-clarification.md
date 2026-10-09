[P01] Exponentials, logarithms and relative change

[P02] This lesson connects the exponential derivative, the slope that characterises the base $`e`$, logarithmic differentiation and the limit $`(1+1/k)^k\to e`$. It follows the complete body of MIT 18.01, Fall 2006, Lecture 6. “Hyperbolic Functions” appears in the source title, but the eight-page PDF contains no teaching of that topic. Read the core through [Task E](#task-e); try the embedded tasks when you reach them. [Hints](#hints) are grouped after the core, followed separately by [complete solutions](#solutions). Each help item links back to its task.

[P03] The starting toolkit is the familiar algebra of positive powers and logarithms, the derivative as a limit and tangent slope, and the product, quotient, chain and inverse-function differentiation rules. We take the already established function $`e^x`$, with derivative $`e^x`$, and its inverse $`\ln x`$ as starting facts. Here $`e^x`$ is positive for every real $`x`$, and $`\ln x`$ is real only for $`x\gt0`$. This route reconstructs connections among familiar calculus facts; it does not claim to construct the real exponential or the number $`e`$ from nothing. In particular, the lecture's sketches will illustrate slope comparisons that we justify below.

[P04] First fix a base $`a\gt1`$, as the lecture does. Integer powers begin with $`a^0=1`$, $`a^1=a`$ and $`a^2=a\cdot a`$. For an integer $`p`$ and a positive integer $`q`$, $`a^{p/q}=\sqrt[q]{a^p}`$, taking the positive root. The familiar laws are

```math
a^{u+v}=a^u a^v,\qquad (a^u)^v=a^{uv}.
```

[P05] For a real exponent, the value is the continuous extension of these rational powers: rational inputs approaching $`x`$ have outputs approaching $`a^x`$. The identity $`a^x=e^{x\ln a}`$ gives the same positive real power and shows, using the chain rule, that it is differentiable. We will work out that derivative explicitly shortly. Thus the derivative limits used next exist; continuity alone would not have proved differentiability.

[P06] Write $`E(x)=a^x`$. A small input change $`h`$ multiplies its height by $`a^h`$. This turns the difference quotient into a particularly useful form:

```math
E'(x)=\lim_{h\to0}\frac{a^{x+h}-a^x}{h}
=a^x\lim_{h\to0}\frac{a^h-1}{h}.
```

[P07] The factor $`a^x`$ can come outside the limit because $`x`$ is fixed while $`h`$ tends to zero. Name the remaining number $`M(a)`$:

```math
M(a)=\lim_{h\to0}\frac{a^h-1}{h}=E'(0),
\qquad E'(x)=M(a)E(x).
```

[P08] The notation $`M(a)`$ means that the slope at zero depends on the chosen base. It is constant as $`x`$ varies. Since $`E(0)=1`$, the tangent there passes through $`(0,1)`$ and has equation $`y=1+M(a)x`$. This is the meaning of the lecture's Figure 1: $`M(a)`$ labels a slope, not the height of the curve. For example, when $`E(x)=2^x`$, the height at $`x=3`$ is $`8`$ and its slope is $`8M(2)`$. Dividing slope by height gives $`E'(x)/E(x)=M(a)`$ at every input: the absolute slope grows with the height, while this fractional rate stays constant.

<a id="task-a"></a>

[P09] Task A: connect height, tangent slope and fractional rate. For $`E(x)=3^x`$, compare the tangent slopes at $`x=2`$ and $`x=0`$, then compare slope divided by height at those two points. Give the tangent line at $`x=0`$ in terms of $`M(3)`$. Explain why the slope comparison and fractional-rate comparison differ. Answers in terms of $`M(3)`$ are sufficient; no numerical logarithm is required. [Hint A](#hint-a) · [Solution A](#solution-a)

[P10] To identify $`M(a)`$, first make the inverse relationship precise. The statements $`y=e^x`$ and $`\ln y=x`$ describe the same input-output pair. Equivalently, if $`w=\ln x`$, then $`e^w=x`$, with $`x\gt0`$. Applying the exponential undoes the logarithm; it does not swap the exponent and the output. The source's second boxed inverse statement has that swap as a typographical error. Its subsequent calculation uses the correct equation $`e^w=x`$.

[P11] The inverse has $`\ln1=0`$. Because $`e^w`$ increases, $`0\lt x\lt1`$ corresponds to $`w\lt0`$, and $`x\gt1`$ corresponds to $`w\gt0`$. The positive-input product law also matches the exponential law: if $`x_1=e^u`$ and $`x_2=e^v`$, then $`x_1x_2=e^{u+v}`$, so $`\ln(x_1x_2)=\ln x_1+\ln x_2`$. Both $`x_1`$ and $`x_2`$ must be positive for these real logarithms.

[P12] Here is the inverse differentiation calculation, with its condition visible. The exponential is differentiable, strictly increasing, and has nonzero derivative $`e^w`$, so the inverse-function rule applies to its inverse $`w=\ln x`$. Differentiating $`e^{w(x)}=x`$ with respect to $`x`$ gives

```math
e^w\frac{dw}{dx}=1,
\qquad \frac{dw}{dx}=\frac1{e^w}=\frac1x\quad(x\gt0).
```

[P13] The factor $`dw/dx`$ is essential: the input of the exponential is $`w(x)`$, not simply $`x`$. This recovers $`(\ln x)'=1/x`$. As a direct chain-rule use, $`\ln(1+x^2)`$ has derivative $`2x/(1+x^2)`$ for all real $`x`$; its argument is always positive, even though its derivative can be negative. Positivity of a function and positivity of its derivative are different conditions.

[P14] Now use $`a=e^{\ln a}`$ to build a base-$`e`$ expression for the original exponential:

```math
a^x=(e^{\ln a})^x=e^{x\ln a},
\qquad \frac{d}{dx}a^x=e^{x\ln a}\frac{d}{dx}(x\ln a)
=(\ln a)a^x.
```

[P15] The base is fixed, so $`\ln a`$ is a number, and $`(x\ln a)'=\ln a`$. It plays the same role as $`3`$ in $`(e^{3x})'=3e^{3x}`$; $`(e^x)'=e^x`$ is the case with coefficient $`1`$. At $`x=0`$, the displayed derivative is $`\ln a`$, hence $`M(a)=\ln a`$. Even a base-ten exponential has derivative $`(10^x)'=(\ln10)10^x`$. Natural logarithms enter because they convert a base into its slope-per-unit-height factor. The same rewriting also extends this formula to every fixed $`a\gt0`$: $`a=1`$ gives the constant function, while $`0\lt a\lt1`$ gives a negative derivative because $`\ln a\lt0`$.

[P16] We can now justify the three geometric pictures without treating a drawing as a proof. For $`a\gt1`$, both $`a^x`$ and its slope $`(\ln a)a^x`$ strictly increase with $`x`$. The slope of a secant from $`u`$ to $`v`$, where $`u\lt v`$, is the average of these tangent slopes:

```math
\frac{E(v)-E(u)}{v-u}
=\frac1{v-u}\int_u^v E'(s)\,ds.
```

[P17] This is the fundamental theorem of calculus applied to $`E'`$. Since the slope strictly increases across the interval, its average is strictly between its endpoint values. A secant to the right of $`0`$ therefore has greater slope than the tangent at $`0`$; a secant ending at $`0`$ from the left has smaller slope. Here are the exact objects represented in the lecture's Figures 2 and 3:

| Curve | Secant endpoints | Secant slope and line | Tangent at zero |
| --- | --- | --- | --- |
| $`y=2^x`$ | $`(0,1)`$ and $`(1,2)`$ | $`(2-1)/(1-0)=1`$; $`y=1+x`$ | $`y=1+M(2)x`$, with $`M(2)\lt1`$ |
| $`y=4^x`$ | $`(-1/2,1/2)`$ and $`(0,1)`$ | $`(1-1/2)/(0+1/2)=1`$; $`y=1+x`$ | $`y=1+M(4)x`$, with $`M(4)\gt1`$ |

[P18] Thus the same slope-one line is compared with the tangent from opposite sides. In the second row $`4^{-1/2}=1/2`$ and $`4^0=1`$. The original text and Figure 3 incorrectly label the second point $`(1,0)`$; that point is not on $`y=4^x`$. The increasing-slope argument concerns one fixed base at a time. When comparing different bases, $`M(a)=\ln a`$ strictly increases with $`a`$, so a larger base has a steeper tangent at $`x=0`$. No claim about the relative slopes of different bases at every negative input is needed.

[P19] The special base is characterised by $`M(e)=\ln e=1`$. There is exactly one positive base with that slope, since $`\ln a=1`$ is equivalent to $`a=e`$. The two secant comparisons give $`M(2)\lt1\lt M(4)`$, and the strict increase of $`\ln a`$ then gives $`2\lt e\lt4`$. The lecture uses this picture to motivate the choice of base. With our established exponential and inverse, it is a verified characterisation, not an independent existence proof. These three statements express the same property:

```math
M(e)=1,\qquad
\lim_{h\to0}\frac{e^h-1}{h}=1,\qquad
\left.\frac{d}{dx}e^x\right|_{x=0}=1.
```

[P20] Substitution into $`E'(x)=M(a)E(x)`$ gives $`(e^x)'=e^x`$ again. The vertical bar means “evaluate the derivative at the indicated input”; it does not introduce a new differentiation operation. This explains why the base $`e`$ makes the exponential derivative especially simple.

[P21] Logarithmic differentiation uses the same chain rule in the other direction. Suppose $`f`$ is differentiable and positive on the interval being considered. Writing $`u=f(x)`$ gives

```math
\frac{d}{dx}\ln(f(x))=\frac1{f(x)}f'(x),
\qquad f'(x)=f(x)\frac{d}{dx}\ln(f(x)).
```

[P22] The expression $`\ln(f(x))`$ means take the output of $`f`$ and then its logarithm. Its derivative is the derivative of $`f`$ divided by the current output of $`f`$. Multiplying back by $`f`$ recovers the desired ordinary derivative. Taking a logarithm can turn a varying exponent into a multiplier where the product rule works. For example, for $`f(x)=a^x`$ with fixed positive $`a`$,

```math
\ln f=x\ln a,\qquad
\frac{f'}f=\ln a,\qquad f'=(\ln a)a^x.
```

[P23] This is the lecture's second route to the same derivative. It requires $`f\gt0`$, which holds for a positive-base exponential. The plain expression $`\ln f`$ would not be a real-valued route for a negative $`f`$. When direct differentiation is simpler, there is no need to take logs: the ordinary power rule already handles $`x^3`$ on the real line.

[P24] In $`x^x`$ both the base and the exponent vary. On $`x\gt0`$, define this real-valued function by $`x^x=e^{x\ln x}`$. Its positivity permits logarithmic differentiation:

```math
f(x)=x^x,\qquad \ln f=x\ln x,
\qquad \frac{f'}f=1\cdot\ln x+x\frac1x=\ln x+1,
\qquad f'=x^x(\ln x+1).
```

[P25] The product rule contributes both terms because both $`x`$ and $`\ln x`$ vary. Treating the exponent as a fixed power would miss this dependence. Treating the base as a fixed exponential base would miss a different contribution. Rewriting first as $`e^{x\ln x}`$ gives the same result directly by the chain rule: the outer exponential stays, and the inner derivative is $`\ln x+1`$. At $`x=1`$, the height is $`1`$ and slope is $`1`$; this check also distinguishes the answer from $`x^x\ln x`$, which would incorrectly give zero there.

<a id="task-b"></a>

[P26] Task B: choose and carry out a derivative method. For $`G(x)=(1+x)^{x-1}`$ on $`x\gt-1`$, find $`G'(x)`$ and $`G'(1)`$. Explain which factors vary and why treating either the base or the exponent as a constant throughout gives an invalid method. Show a line that justifies the derivative, not only a final formula. [Hint B](#hint-b) · [Solution B](#solution-b)

[P27] A logarithm can also expose a limit hidden by a changing exponent. Let $`k`$ run through positive integers and put

```math
b_k=\left(1+\frac1k\right)^k,\qquad L_k=\ln b_k.
```

[P28] A subscript $`k`$ labels the terms of a sequence. The base approaches $`1`$ while the exponent increases without bound, so simply replacing the base by $`1`$ throws away the competition between them. All bases are positive, so the power law for logarithms applies:

```math
L_k=k\ln\left(1+\frac1k\right)
=\frac{\ln(1+h)-\ln1}{h},\qquad h=\frac1k.
```

[P29] The equality uses $`k=1/h`$ and $`\ln1=0`$. As $`k\to\infty`$, $`h\to0`$ from the positive side. The right-hand expression is the derivative difference quotient of $`\ln x`$ at $`x=1`$. We already obtained that derivative as $`1/x`$, so

```math
L_k\longrightarrow \left.\frac{d}{dx}\ln x\right|_{x=1}=1.
```

[P30] The derivative is a two-sided limit at $`1`$, and therefore supplies this particular right-hand approach too. To return from logarithms, use the identity $`b_k=e^{L_k}`$. The exponential is continuous, so $`L_k\to1`$ gives $`e^{L_k}\to e^1`$. Continuity here also follows from its known differentiability: a small change of output is $`h`$ times a difference quotient with a finite limit, and hence tends to zero. Consequently

```math
\lim_{k\to\infty}\left(1+\frac1k\right)^k=e.
```

[P31] This argument does not assume in advance that $`b_k`$ has a limit. It proves convergence of the logarithms, then uses continuity to establish convergence of the original positive sequence. The same reasoning works if $`k`$ is a positive real variable tending to infinity.

[P32] The lecture's first final remark proposes $`k=10`$ as an approximation to $`e`$. Its value is $`1.1^{10}=2.5937424601`$. For scale, the independently evaluated numerical value $`e\approx2.7182818285`$ makes that approximation about $`0.12454`$ too small, or about $`4.58\%`$ low relative to $`e`$. Thus it is a rough numerical estimate; the proved limit does not make a small finite $`k`$ exact or specify an accuracy tolerance.

<a id="task-c"></a>

[P33] Task C: retain the sign and scale of a changing exponent. For positive integers $`n\ge3`$, evaluate

```math
\lim_{n\to\infty}\left(1-\frac2n\right)^{3n}.
```

[P34] State why the logarithm is real; exhibit the small increment used in a log difference quotient and its direction of approach; justify returning to the original sequence. [Hint C](#hint-c) · [Solution C](#solution-c)

[P35] The lecture's second final remark explains why relative change matters in science and finance. A fall of $`50`$ points from $`300`$ is a fractional change $`-50/300=-1/6`$, or about $`-16.67\%`$. The same fall from $`10000`$ is $`-50/10000=-0.005`$, or $`-0.5\%`$. Equal absolute changes can have very different importance relative to the starting level.

[P36] Now let $`f(t)\gt0`$ be a differentiable numerical level measured in one fixed unit, with $`t`$ measured in a fixed time unit. Its instantaneous fractional rate is $`f'(t)/f(t)`$, with units of inverse time. Indeed, divide the finite fractional change by elapsed time and take the limit:

```math
\lim_{h\to0}\frac{f(t+h)-f(t)}{h\,f(t)}
=\frac{f'(t)}{f(t)}
=\frac{d}{dt}\ln(f(t)).
```

[P37] Multiplying by $`100`$ expresses this as an instantaneous percent rate per time unit. If $`f`$ denotes a physical quantity with units rather than its numerical value, take $`\ln(f/f_{\rm ref})`$ for a fixed positive reference quantity in the same unit; the ratio is dimensionless and its log derivative is still $`f'/f`$. Changing a fixed reference adds a constant to the logarithm and leaves its derivative unchanged.

[P38] For example, take $`f(t)=300e^{-0.02t}`$ with $`t`$ the numerical time in days. The chain rule gives $`f'(t)=-0.02f(t)`$, so the fractional rate is $`-0.02`$ per day, or $`-2\%`$ per day instantaneously. At the start the absolute rate is $`-6`$ points per day. For $`10000e^{-0.02t}`$ the same fractional rate accompanies an initial absolute rate of $`-200`$ points per day. This is the rate version of comparing a change with the size of the quantity.

[P39] Three related measurements must remain distinct. Over a finite interval from level $`f_0\gt0`$ to $`f_1\gt0`$, the exact fractional change is $`r=(f_1-f_0)/f_0`$, while the exact log change is $`\ln(f_1/f_0)=\ln(1+r)`$. These are generally unequal. Since $`(\ln(1+r)-\ln1)/r\to1`$ as $`r\to0`$, $`\ln(1+r)\approx r`$ for a small fractional change. In the previous example the exact one-day fractional change is $`e^{-0.02}-1`$, whereas the one-day log change is $`-0.02`$. The instantaneous derivative is not an exact finite percentage-change formula.

<a id="task-d"></a>

[P40] Task D: interpret rate and finite change. A numerical index level is $`f(t)=100(1+t)^2`$ for $`t\ge0`$, with $`t`$ the numerical elapsed time in days. Find its instantaneous fractional rate at time $`t`$ and compare that rate at $`t=0`$ and $`t=1`$. Calculate the exact fractional change and exact log change from day $`0`$ to day $`1`$. Explain how the level can rise while its instantaneous fractional rate falls. Units are needed for rates, and factors of $`100`$ for percent interpretations must be explicit. [Hint D](#hint-d) · [Solution D](#solution-d)

<a id="task-e"></a>

[P41] Task E: return to the ideas after a gap. On a later study occasion, close the core and help first, then attempt this connected problem. Choosing your next study session is a practical starting point, not a prescribed optimal interval. Recalling the log-rate rule checks recall; using it for the new expression checks transfer. For

```math
P(x)=(1+x)^{1/x},\qquad x\gt0,
```

[P42] find $`P'(x)`$ and $`\lim_{x\to0^+}P(x)`$. For the derivative, show which operation follows taking logs and why. For the limit, identify the derivative difference quotient and the continuity step. Keep the derivative at a positive input distinct from the limit as the input tends to zero. Reopen the relevant core passage or use [Hint E](#hint-e) if needed; the [complete solution](#solution-e) supplies a route to compare with your own.

[P43] Source: MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, Lecture 6, [original lecture PDF](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/f9af0e98490296c99d330faf47389507_lec6.pdf). PDF pages 2–8 are printed pages 1–7; PDF page 1 is the course cover. The two corrected misprints are identified at their uses above. All tasks here are generated applications, not attributed MIT assessment questions.

<a id="hints"></a>

[P44] Hints. Choose your task's hint, then return to the prompt before looking at its solution. Full solutions begin only after all five hints.

<a id="hint-a"></a>

[P45] Hint A. Make a two-row table of height and slope, using $`E(0)=1`$ and $`E(2)=9`$. In the slope column multiply each height by $`M(3)`$. Divide each row's slope by its own height before comparing fractional rates. A tangent line through $`(x_0,y_0)`$ with slope $`m`$ satisfies $`y-y_0=m(x-x_0)`$. [Return to Task A](#task-a)

<a id="hint-b"></a>

[P46] Hint B. The starting transformation is $`\ln G=(x-1)\ln(1+x)`$. Differentiate the product on the right, retaining the contribution from each factor. The derivative of the left is $`G'/G`$. Recover $`G'`$ before substituting $`x=1`$; substituting first would erase the varying function you need to differentiate. [Return to Task B](#task-b)

<a id="hint-c"></a>

[P47] Hint C. Choose $`h=-2/n`$ so that the logarithm's argument becomes $`1+h`$. Solve for $`n`$ in terms of $`h`$ before replacing the factor $`3n`$. The resulting expression is a constant times $`\ln(1+h)/h`$. Think about which side of zero $`h`$ occupies. [Return to Task C](#task-c)

<a id="hint-d"></a>

[P48] Hint D. Find $`f'`$, then divide by $`f`$ at the same time. For the finite interval, make a separate pair of endpoint values $`f(0)`$ and $`f(1)`$. Build a difference-over-starting-value expression and a logarithm-of-ratio expression from that pair; neither requires replacing the rate by a constant. [Return to Task D](#task-d)

<a id="hint-e"></a>

[P49] Hint E. Taking logs produces $`\ln P=\ln(1+x)/x`$. For the derivative, this is a quotient of two varying functions; its derivative equals $`P'/P`$. For the limit, keep that quotient intact and insert the zero $`\ln1`$ into its numerator to expose a derivative at input $`1`$. These are two different uses of the same transformed expression. [Return to Task E](#task-e)

<a id="solutions"></a>

[P50] Complete solutions. These give the connecting steps as well as the results. Compare the first step at which your reasoning differs; a different valid method, such as rewriting in base $`e`$, is also acceptable. The possible errors discussed below are anticipated routes, not reports of your performance.

<a id="solution-a"></a>

[P51] Solution A. The two heights are $`E(0)=1`$ and $`E(2)=9`$. Since $`E'=M(3)E`$, their slopes are $`M(3)`$ and $`9M(3)`$, respectively. The slope at $`2`$ is nine times the slope at $`0`$. Their slope-to-height ratios are $`M(3)/1=M(3)`$ and $`9M(3)/9=M(3)`$, so the fractional rates are equal. The tangent at zero passes through $`(0,1)`$ and has slope $`M(3)`$, giving $`y=1+M(3)x`$. The slope comparison retains the change of scale; dividing by the current height removes it. An equal fractional rate does not mean an equal absolute slope. [Return to Task A](#task-a)

<a id="solution-b"></a>

[P52] Solution B. On $`x\gt-1`$, $`1+x\gt0`$ and $`G=e^{(x-1)\ln(1+x)}\gt0`$. Both the base $`1+x`$ and exponent $`x-1`$ vary. Taking logarithms and then applying the product and chain rules gives

```math
\ln G=(x-1)\ln(1+x),
\qquad \frac{G'}G=\ln(1+x)+\frac{x-1}{1+x}.
```

[P53] Multiplying by the positive original function and then evaluating gives

```math
G'(x)=(1+x)^{x-1}\left(\ln(1+x)+\frac{x-1}{1+x}\right),
\qquad G'(1)=2^0(\ln2+0)=\ln2.
```

[P54] The logarithm term comes from differentiating the exponent factor $`x-1`$. The fraction comes from differentiating $`\ln(1+x)`$, which carries the changing base. Treating either as constant throughout drops one of those contributions. The fact that the second contribution is zero at $`x=1`$ does not make the base constant as a function of $`x`$. Direct differentiation of the displayed base-$`e`$ form gives the same two contributions and is equally valid. [Return to Task B](#task-b)

<a id="solution-c"></a>

[P55] Solution C. For $`n\ge3`$, $`1-2/n\gt0`$, so the original sequence $`c_n=(1-2/n)^{3n}`$ is positive and its logarithm is real. Set $`h=-2/n`$. Then $`n=-2/h`$, and $`h\to0^-`$ as $`n\to\infty`$. Therefore

```math
\ln c_n=3n\ln(1-2/n)
=-6\frac{\ln(1+h)-\ln1}{h}\longrightarrow-6.
```

[P56] The quotient tends to the derivative of $`\ln x`$ at $`1`$, which is $`1`$. Its two-sided derivative permits this left-hand approach as well. Since $`c_n=e^{\ln c_n}`$ and the exponential is continuous, $`c_n\to e^{-6}`$. The negative sign is essential: all the bases lie below $`1`$ and the exponents are positive, so all $`c_n\lt1`$; the answer $`e^6`$ would conflict with that check. Replacing the base by its limiting value before dealing with the exponent would lose the limiting effect. [Return to Task C](#task-c)

<a id="solution-d"></a>

[P57] Solution D. The ordinary derivative is $`f'(t)=200(1+t)`$ points per day. Dividing by the level at the same time gives

```math
\frac{f'(t)}{f(t)}=\frac{200(1+t)}{100(1+t)^2}
=\frac2{1+t}\quad\text{per day}.
```

[P58] This is $`2`$ per day at $`t=0`$ and $`1`$ per day at $`t=1`$, or instantaneous percent rates $`200\%`$ and $`100\%`$ per day. The level grows because $`f'(t)\gt0`$ for $`t\ge0`$. The fractional rate falls because its positive denominator $`1+t`$ grows. In fact the absolute rate grows too, but the level against which it is compared grows faster in this ratio.

[P59] The endpoint levels are $`f(0)=100`$ and $`f(1)=400`$. Hence the exact finite fractional change is $`(400-100)/100=3`$, or $`300\%`$, while the exact log change is $`\ln(400/100)=\ln4`$. These finite changes are dimensionless. No constant instantaneous rate was specified: using the initial rate $`2`$ per day for the whole day would be a different model. The change is not small, so replacing $`\ln4=\ln(1+3)`$ by $`3`$ would also be unjustified. [Return to Task D](#task-d)

<a id="solution-e"></a>

[P60] Solution E. For $`x\gt0`$, the base and the function are positive, so logarithmic differentiation is available. First

```math
\ln P=\frac{\ln(1+x)}x.
```

[P61] The numerator and denominator both vary. Apply the quotient rule to that expression and the chain rule to its left side:

```math
\frac{P'}P=
\frac{x/(1+x)-\ln(1+x)}{x^2},
\qquad
P'(x)=(1+x)^{1/x}\frac{x/(1+x)-\ln(1+x)}{x^2}quad(x\gt0).
```

[P62] For the limit, instead recognise

```math
\ln P(x)=\frac{\ln(1+x)-\ln1}{x}\longrightarrow1
\quad\text{as }x\to0^+.
```

[P63] This quotient computes the derivative of the logarithm at input $`1`$, even though the increment is now called $`x`$. Since $`P(x)=e^{\ln P(x)}`$, continuity of the exponential gives $`P(x)\to e`$. The derivative formula describes variation at each positive input; the limit describes the value approached near the excluded input $`0`$. A limit of function values is not a derivative, so the two answers have different roles. [Return to Task E](#task-e)
