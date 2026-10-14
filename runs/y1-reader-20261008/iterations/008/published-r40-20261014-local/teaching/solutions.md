<a id="solutions-d008-start"></a>

Complete solutions for linear and quadratic approximations

Use these after an attempt or when a hint is insufficient. Each solution shows the consequential decisions and a check. These are model answers to generated tasks, not diagnoses of any observed student work.

[A1](#solutions-d008-a1) · [A2](#solutions-d008-a2) · [A3](#solutions-d008-a3) · [A4](#solutions-d008-a4) · [R1](#solutions-d008-r1)

<a id="solutions-d008-a1"></a>

Solution A1

The displacement is $`h=2.04-2=0.04`$. The derivative of $`\ln x`$ is $`1/x`$, so the slope at the fixed base point is $`1/2`$. The base value must also remain in the line:

```math
L(2.04)=0.69314718056+\frac12(0.04)
=0.71314718056\approx0.713147.
```

An equivalent construction factors $`2.04=2(1.02)`$ and uses $`\ln(2.04)=\ln2+\ln(1.02)\approx\ln2+0.02`$. The estimate is rounded to six decimal places, as requested. Direct evaluation gives about $`0.7129498079`$, so its error is about $`0.0001973727`$; the six-place display is not a six-place accuracy claim. A possible mistake would be carrying the zero base value from the centre-one example into this centre-two calculation; the added $`\ln2`$ is essential.

[Return to A1](main.md#main-d008-a1) · [Hint A1](hints.md#hints-d008-a1)

<a id="solutions-d008-a2"></a>

Solution A2

The standard forms give $`\sin(3x)\approx3x`$ and $`(1+x)^{-1/2}\approx1-x/2`$. Their product is

```math
(3x)\left(1-\frac12x\right)=3x-\frac32x^2.
```

At linear degree the model is $`L_k(x)=3x`$. The denominator factor's linear term multiplies a numerator linear term and therefore contributes only at degree two. There is no numerator constant for it to multiply into a linear term.

For the exact limit, $`k(0)=0`$, and $`k`$ is differentiable near zero in its domain $`x\gt -1`$. The product and chain rules give

```math
k'(0)=3\cos0\cdot1+\sin0\cdot\left(-\frac12\right)=3.
```

The requested quotient equals $`[k(x)-k(0)]/x`$ for nonzero $`x`$. Its limit is therefore $`k'(0)=3`$. Equivalently, the residual formulation gives $`k(x)=3x+R_1(x)`$ with $`R_1(x)/x\to0`$; dividing yields $`3+R_1(x)/x\to3`$. The derivative definition supplies the exact-limit warrant that an approximate value alone would lack.

[Return to A2](main.md#main-d008-a2) · [Hint A2](hints.md#hints-d008-a2)

<a id="solutions-d008-a3"></a>

Solution A3

The expansion variable is $`q=0.6^2=0.36`$, giving

```math
1+\frac q2=1.18,
\qquad
1+\frac q2+\frac38q^2=1.18+0.0486=1.2286.
```

Compared with the supplied exact factor $`1.25`$, their absolute errors are

```math
|1.25-1.18|=0.07,
\qquad |1.25-1.2286|=0.0214.
```

Both exceed $`0.001`$, so neither meets the requested accuracy. The quadratic improves this estimate but does not improve it enough. Here $`q=0.36`$ is far larger than the lecture's approximately $`1.78\times10^{-10}`$; the same low-degree truncation cannot be accepted without checking its error. The exact factor is available directly from the supplied model, $`1/\sqrt{1-0.36}=1/0.8=1.25`$, so there is no need to insist on an approximation in this case.

[Return to A3](main.md#main-d008-a3) · [Hint A3](hints.md#hints-d008-a3)

<a id="solutions-d008-a4"></a>

Solution A4

Use the complete quadratic of $`f`$ and multiply by the new factor. Retaining degrees through two gives

```math
g(x)\approx(1+ax)\left(1-\frac52x+\frac{27}{8}x^2\right)
\approx1+\left(a-\frac52\right)x
+\left(\frac{27}{8}-\frac52a\right)x^2.
```

The derivative-matching linear coefficient is $`g'(0)`$. Setting it to zero requires $`a=5/2`$. Substitution into the quadratic coefficient gives

```math
\frac{27}{8}-\frac52\cdot\frac52
=\frac{27}{8}-\frac{50}{8}=-\frac{23}{8},
\qquad g(x)\approx1-\frac{23}{8}x^2.
```

The first nonzero correction is quadratic and negative. A horizontal tangent does not make the function constant: the model has nonzero second derivative $`-23/4`$. An independent product-rule check uses $`g=(1+ax)f`$, yielding $`g'(0)=a+f'(0)=a-5/2`$ and $`g''(0)=2af'(0)+f''(0)`$. At the chosen $`a`$, this is $`-25/2+27/4=-23/4`$, which verifies both coefficients. All these constructions use the original domain $`x\gt -1`$ locally around zero.

[Return to A4](main.md#main-d008-a4) · [Hint A4](hints.md#hints-d008-a4)

<a id="solutions-d008-r1"></a>

Solution R1

The line matches value and first derivative; the second-order model also matches the second derivative, so its quadratic coefficient is half that derivative. For cosine at zero, the three data are $`1,0,-1`$. Thus

```math
L(x)=1,
\qquad Q(x)=1-\frac{x^2}{2}.
```

At $`x=0.2`$, these give $`L(0.2)=1`$ and $`Q(0.2)=0.98`$. Using the supplied reference, their absolute errors are approximately

```math
|0.98006657784-1|=0.01993342216,
\qquad
|0.98006657784-0.98|=0.00006657784.
```

The line fails the tolerance $`0.0001`$; the quadratic meets it at this input. Its negative second derivative captures cosine's downward bending near zero. For sine, the second derivative is $`-\sin x`$, which vanishes at zero. Its second-order polynomial is still $`x`$; the next nonzero term is cubic, $`-x^3/6`$. Thus a second-order construction need not add a nonzero quadratic term. Recalling the formula and successfully choosing a model from a numerical tolerance are separate achievements.

[Return to R1](main.md#main-d008-revisit) · [Hint R1](hints.md#hints-d008-r1)

[Return to the main reading route](main.md#main-d008-start)
