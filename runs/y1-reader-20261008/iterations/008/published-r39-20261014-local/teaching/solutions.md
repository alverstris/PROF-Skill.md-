<a id="d008-solutions-start"></a>
Complete solutions for Linear and quadratic approximations

These solutions explain the consequential choices and the result for every generated attempt. They also identify some anticipated wrong routes; these are possible errors to check, not claims about any learner's observed work. Try a problem or use its separate hint before opening the corresponding solution.

<a id="d008-solutions-a"></a>
Solution A

Choose $`x_0=1`$. The displacement is $`h=0.96-1=-0.04`$. For $`f(x)=\ln x`$, $`f(1)=0`$ and $`f'(1)=1`$, so the tangent is

```math
L(x)=0+1(x-1)=x-1.
```

Its estimate is $`\ln(0.96)\approx-0.04`$. A positive slope multiplied by a negative displacement gives a negative output change from $`\ln1=0`$. This agrees with the increasing logarithm having a negative value below 1.

It is a local approximation: $`f'(x)=1/x`$ varies with $`x`$, whereas $`L'(x)=1`$ is constant. The two functions share value and slope at 1; they do not share all values near it. Direct evaluation, if desired, gives $`\ln(0.96)\approx-0.040822`$. The tangent is about $`0.000822`$ above that value.

An anticipated error is using $`+0.04`$ as the displacement. The displacement is target minus basepoint; its sign matters.

[Return to Attempt A](main.md#d008-main-task-a) · [Hint A](hints.md#d008-hints-a)

<a id="d008-solutions-b"></a>
Solution B

The exact rewrite is

```math
g(x)=e^{3x}(1-2x)^{-1/2}.
```

For the exponential, $`u=3x`$ gives $`e^{3x}\approx1+3x`$. For the power, use $`u=-2x`$ and $`r=-1/2`$:

```math
(1-2x)^{-1/2}\approx
1+\left(-\frac12\right)(-2x)=1+x.
```

The local approximations need both $`3x`$ and $`-2x`$ near zero. The real original function requires $`1-2x\gt 0`$, or $`x\lt 1/2`$; this includes an interval around zero.

Multiply the polynomials:

```math
(1+3x)(1+x)=1+4x+3x^2.
```

At linear order keep $`L_g(x)=1+4x`$. The square term is discarded because the factors' quadratic terms have not been included. Since these were derivative-based local models, their linear coefficient gives $`g'(0)=4`$.

A direct derivative provides an independent check:

```math
g'(x)=3e^{3x}(1-2x)^{-1/2}
+e^{3x}(1-2x)^{-3/2}.
```

The second term includes the chain-rule factor $`(-1/2)(-2)=1`$. Substituting zero gives $`3+1=4`$.

An anticipated sign error is replacing $`(1-2x)^{-1/2}`$ by $`1-x`$. The two negative factors in $`ru`$ produce a positive linear term. Another is keeping $`3x^2`$ as the true quadratic coefficient; a degree-two calculation would also need both factors' own square terms.

[Return to Attempt B](main.md#d008-main-task-b) · [Hint B](hints.md#d008-hints-b)

<a id="d008-solutions-c"></a>
Solution C

The main route constructs the degree-two model of $`f(x)=e^{-2x}/\sqrt{1+x}`$ as

```math
f(x)=1-\frac52x+\frac{27}{8}x^2+E_2(x),
\qquad \frac{E_2(x)}{x^2}\longrightarrow0.
```

The function has a continuous second derivative on an interval around zero within $`x\gt -1`$, so the stated error condition applies. Substitute into the exact numerator:

```math
f(x)-1+\frac52x=\frac{27}{8}x^2+E_2(x).
```

For $`x\ne0`$, division gives

```math
\frac{f(x)-1+(5/2)x}{x^2}
=\frac{27}{8}+\frac{E_2(x)}{x^2}
\longrightarrow\frac{27}{8}.
```

The constant and linear terms cancel, leaving the quadratic coefficient as the limit. A linear model alone gives an error whose ratio to $`x`$ tends to zero; it does not say that its ratio to $`x^2`$ tends to zero. Indeed its omitted $`(27/8)x^2`$ becomes the entire nonzero answer after this division.

An anticipated wrong answer is 0 from substituting only the linear polynomial. This does not fail in the cancellation algebra; it fails at treating discarded terms as negligible after division by a smaller quantity.

[Return to Attempt C](main.md#d008-main-task-c) · [Hint C](hints.md#d008-hints-c)

<a id="d008-solutions-d"></a>
Solution D

(a) Since $`z=(v/c)^2`$, replacing $`v`$ by $`2v`$ multiplies $`z`$ by 4. It also multiplies $`z/2`$ by 4. The added term is proportional to $`z^2`$, so it is multiplied by $`4^2=16`$. Equivalently it is proportional to $`v^4`$.

(b) At the original speed, $`3z^2/8\approx1.19\times10^{-20}`$, which is less than $`10^{-19}`$. It does not exceed the stated threshold. At double speed it is

```math
16(1.185185\ldots\times10^{-20})
\approx1.90\times10^{-19},
```

which exceeds the threshold. The threshold and both terms are dimensionless contributions to $`T'/T`$, so the comparison is consistent. These calculations decide whether this extra term crosses the threshold. A certified bound on the total error would also require controlling all remaining terms and the model assumptions.

(c) At $`v=0.8c`$,

```math
z=0.8^2=0.64.
```

This is not small compared with one, so a truncation justified by a small input is unreliable without further checking. The two estimates are

```math
1+\frac z2=1.32,\qquad
1+\frac z2+\frac38z^2
=1.32+\frac38(0.4096)=1.4736.
```

The exact law gives $`T'/T=1/0.6=5/3\approx1.666667`$. Both polynomials underestimate it. Their absolute errors in the dimensionless factor are about $`0.346667`$ and $`0.193067`$. Adding the square term improved this particular estimate, but neither is close enough to justify a high-precision claim. For this supplied input, evaluating the simple exact square root is also easier than using a poorly controlled truncation.

An anticipated error is describing the first model as linear in speed. It is linear in $`z`$; the power of speed in its first correction is two.

[Return to Attempt D](main.md#d008-main-task-d) · [Hint D](hints.md#d008-hints-d)

<a id="d008-solutions-e"></a>
Solution E

Use the signed time displacement $`h=t-2\ \mathrm{s}`$. The models are

```math
L_F(t)=3\ \mathrm{V}+
(0.4\ \mathrm{V/s})h,
```

```math
Q_F(t)=3\ \mathrm{V}+
(0.4\ \mathrm{V/s})h-
(0.1\ \mathrm{V/s^2})h^2.
```

The square-term coefficient is $`F''(2)/2=-0.1\ \mathrm{V/s^2}`$, not $`-0.2\ \mathrm{V/s^2}`$. For $`t=2.1\ \mathrm{s}`$, $`h=0.1\ \mathrm{s}`$. Thus

```math
L_F(2.1\ \mathrm{s})=3.04\ \mathrm{V},\qquad
Q_F(2.1\ \mathrm{s})=3.04\ \mathrm{V}-0.001\ \mathrm{V}
=3.039\ \mathrm{V}.
```

Every term has volts: $`(\mathrm{V/s})\mathrm{s}=\mathrm{V}`$ and $`(\mathrm{V/s^2})\mathrm{s^2}=\mathrm{V}`$. The negative second derivative means the slope is decreasing at the basepoint. In this quadratic model the slope at displacement $`h`$ is $`0.4\ \mathrm{V/s}-(0.2\ \mathrm{V/s^2})h`$. For the positive displacement, the model accumulates less output rise than a slope held fixed at $`0.4\ \mathrm{V/s}`$. The negative square correction represents that difference.

The three given values do not guarantee an error below $`0.001\ \mathrm{V}`$ at 2.1 s. They control derivatives at one point, not how much the second derivative varies across that whole interval. For a concrete counterexample consistent with the assumptions, let

```math
F(t)=Q_F(t)+(2\ \mathrm{V/s^3})h^3.
```

The cubic term and its first two derivatives vanish at $`h=0`$, so all three supplied local values are unchanged. This polynomial has a continuous second derivative. At $`h=0.1\ \mathrm{s}`$, however, its difference from $`Q_F`$ is $`0.002\ \mathrm{V}`$, larger than the claimed bound. Additional information about variation of derivatives, or a direct reliable evaluation, is needed to certify such a finite-interval error.

Other sufficiently large cubic coefficients give acceptable counterexamples. The purpose is to exhibit the freedom left by the data, not to identify the actual sensor's behaviour.

[Return to Attempt E](main.md#d008-main-task-e) · [Hint E](hints.md#d008-hints-e)

<a id="d008-solutions-f"></a>
Solution F

(a) With $`h=x-x_0`$, the models are

```math
L(x)=f(x_0)+f'(x_0)h,\qquad
Q(x)=f(x_0)+f'(x_0)h+\frac{f''(x_0)}2h^2.
```

The linear model matches the value and first derivative at the basepoint. The quadratic model also matches the second derivative. A zero slope or second derivative can lower the polynomial's actual degree.

(b) Rewrite $`H(x)=\ln(1+2x)(1+x)^{-1}`$. The logarithm uses $`u=2x`$:

```math
\ln(1+2x)\approx2x-\frac{(2x)^2}{2}
=2x-2x^2.
```

The reciprocal uses $`r=-1`$, $`u=x`$:

```math
(1+x)^{-1}\approx1-x+x^2.
```

Through degree two, multiplication gives

```math
Q_H(x)=2x(1)+2x(-x)+(-2x^2)(1)
=2x-4x^2.
```

The reciprocal's square term times $`2x`$ has degree three and does not contribute at this order. The two distinct quadratic contributions must both be retained.

The real logarithm requires $`1+2x\gt 0`$, or $`x\gt-1/2`$. The denominator also requires $`x\ne-1`$, which is automatically satisfied on $`x\gt-1/2`$. Hence that interval is a real domain containing zero; the approximation itself is local, requiring the substituted inputs to be small.

A derivative check gives $`H(0)=0`$, $`H'(0)=2`$. For the product's second derivative, the logarithm contributes $`-4`$ times the reciprocal's value 1, twice the first-derivative product contributes $`2(2)(-1)=-4`$, and the logarithm's value 0 kills the remaining term. Thus $`H''(0)=-8`$ and its square coefficient is $`-8/2=-4`$, agreeing with the product calculation.

(c) Write $`H(x)=2x-4x^2+E_2(x)`$. Its second derivative is continuous near zero within the domain, so $`E_2(x)/x^2\to0`$. For nonzero $`x`$,

```math
\frac{H(x)-2x}{x^2}
=-4+\frac{E_2(x)}{x^2}\longrightarrow-4.
```

(d) For sine at zero, $`\sin0=0`$, $`(\sin x)'_{x=0}=1`$ and $`(\sin x)''_{x=0}=0`$. The linear and degree-two models therefore both equal $`x`$. This removes the quadratic coefficient, not the higher-order error; the Maclaurin expansion has a nonzero cubic term $`-x^3/6`$.

For $`f(x)=7-3x`$, the function is itself affine: its derivative is $`-3`$ and its second derivative is zero everywhere. At any basepoint,

```math
L(x)=Q(x)=(7-3x_0)-3(x-x_0)=7-3x.
```

Here both models equal the original function exactly. The reasons differ: sine has a vanishing second derivative at the chosen point, whereas the affine function has no nonlinear part anywhere.

[Return to Attempt F](main.md#d008-main-task-f) · [Hint F](hints.md#d008-hints-f)

[Return to the reading route](main.md#d008-main-linear) · [All hints](hints.md#d008-hints-start)
