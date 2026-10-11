Solutions

These are complete reasoned solutions to E1–E7. For a partial cue first use [Hints](hints.md). The [Practice](practice.md) prompts state the criteria; valid alternative reasoning is welcome when it supplies the same warrants and respects the domains.

<a id="e1"></a>
E1

At $`x_0=4`$, $`f(4)=2`$. Differentiation gives $`f'(x)=1/(2\sqrt{x})`$ for positive $`x`$, so $`f'(4)=1/4`$. Use the displacement from 4:

```math
L(x)=2+\frac14(x-4),\qquad h=4.04-4=0.04,
\qquad \sqrt{4.04}\approx2+\frac14(0.04)=2.01.
```

At the basepoint, $`L(4)=2`$ as required. Replacing the displacement by $`x`$ would give $`2+x/4`$, which has value 3 at $`x=4`$. It would have the right slope but the wrong height, so it cannot be the required tangent there. The estimate is local; this calculation alone does not provide a rigorous decimal-place error bound.

[Return to E1](practice.md#e1)

<a id="e2"></a>
E2

Use $`g(x)=e^{3x}(1-2x)^{-1/2}`$. The exponential substitution is $`u=3x`$. For the power use $`u=-2x`$ and $`r=-1/2`$:

```math
e^{3x}\approx1+3x,\qquad
(1-2x)^{-1/2}\approx1+\left(-\frac12\right)(-2x)=1+x.
```

Their product is $`(1+3x)(1+x)=1+4x+3x^2`$, but only $`1+4x`$ is the complete first-order model. Thus $`g(0)=1`$ and $`g'(0)=4`$. A direct product-rule check gives slope $`3(1)+1(1)=4`$ at zero.

The original real function requires $`1-2x\gt 0`$, or $`x\lt 1/2`$; the denominator cannot be zero. For example, $`-1/4\lt x\lt 1/4`$ is an open domain around zero. The approximation needs both $`|3x|`$ and $`|2x|`$ small, a more restrictive practical question than mere domain membership. The isolated $`3x^2`$ omits the individual second-order contributions from the exponential and reciprocal power. E5 includes them.

[Return to E2](practice.md#e2)

<a id="e3"></a>
E3

For $`F(x)=\ln(1+3x)`$, the real domain is $`x\gt -1/3`$, which includes an interval around zero. Since $`F(0)=0`$, the given limit is exactly $`F'(0)`$. By the chain rule,

```math
F'(x)=\frac3{1+3x},\qquad F'(0)=3,
\qquad \lim_{x\to0}\frac{\ln(1+3x)}{x}=3.
```

Equivalently, the first-order expansion has exact form $`F(x)=3x+R_1(x)`$ with $`R_1(x)/x\to0`$. Dividing by nonzero $`x`$ gives $`3+R_1(x)/x\to3`$. The crucial warrant is the vanishing remainder ratio. A numerical approximation without that warrant could conceal an error that survives division by $`x`$.

[Return to E3](practice.md#e3)

<a id="e4"></a>
E4

For $`f(x)=\ln(1+x)`$, the value, first derivative and second derivative at zero are 0, 1 and $`-1`$ respectively, because $`f'(x)=(1+x)^{-1}`$ and $`f''(x)=-(1+x)^{-2}`$. Therefore

```math
L(x)=x,\qquad Q(x)=x-\frac{x^2}{2}.
```

Set $`x=-0.1`$ to obtain $`1+x=0.9`$. The linear estimate is $`-0.1`$; the quadratic estimate is

```math
-0.1-\frac{(-0.1)^2}{2}=-0.105.
```

Using the stated reference, their absolute errors are approximately

```math
|-0.1053605157-(-0.1)|=0.0053605157,
```

```math
|-0.1053605157-(-0.105)|=0.0003605157.
```

So the quadratic estimate is closer in this case. Its correction is negative on either side of zero because the square is nonnegative and the second derivative at the basepoint is negative. This captures downward curvature. A negative displacement does not turn that square negative.

For sine, $`f(0)=0`$, $`f'(0)=\cos0=1`$, and $`f''(0)=-\sin0=0`$. Its quadratic approximation is consequently $`Q(x)=x`$. Keeping terms through degree two does not require a nonzero degree-two coefficient.

[Return to E4](practice.md#e4)

<a id="e5"></a>
E5

Keep each factor through degree two:

```math
e^{3x}\approx1+3x+\frac92x^2,
```

```math
(1-2x)^{-1/2}\approx1+x+
\frac{(-1/2)(-3/2)}2(-2x)^2
=1+x+\frac32x^2.
```

The second-order coefficient in the product receives $`9/2`$ from the exponential's quadratic term times one, $`3/2`$ from one times the power's quadratic term, and 3 from the product of the two linear terms. Thus

```math
\frac92+\frac32+3=9,\qquad
Q(x)=1+4x+9x^2,\qquad g(x)\approx Q(x).
```

At zero the second derivative of this polynomial is 18, so $`g''(0)=18`$. Direct differentiation checks it: if $`a=e^{3x}`$ and $`b=(1-2x)^{-1/2}`$, their zero-point values are $`a=1`$, $`a'=3`$, $`a''=9`$, $`b=1`$, $`b'=1`$, $`b''=3`$. Then $`g''=a''b+2a'b'+ab''`$ gives $`9+6+3=18`$.

Cubic terms arise, for example, by multiplying a linear term by a quadratic one. They are beyond degree two, and the original factors' own cubic terms have not been included. Dropping the produced cubic terms is therefore consistent with the chosen order. The polynomial identity after collecting terms is exact for the retained polynomial; equality of $`g`$ to that polynomial for general $`x`$ is not asserted.

[Return to E5](practice.md#e5)

<a id="e6"></a>
E6

The small parameter is $`\epsilon=(0.02)^2=0.0004`$. The first-order ratio is $`1+0.0004/2=1.0002`$, so the time estimate is

```math
T'_{\mathrm{linear}}=1000(1.0002)\ \mathrm{s}=1000.2\ \mathrm{s}.
```

The second-order addition to the ratio is

```math
\frac38(0.0004)^2=0.00000006,
```

which adds $`0.00006\ \mathrm{s}`$ after multiplying by $`T=1000\ \mathrm{s}`$. Thus

```math
T'_{\mathrm{quadratic}}=1000.20006\ \mathrm{s}.
```

Against the supplied model reference, the errors are approximately $`0.000060020007\ \mathrm{s}`$ and $`0.000000020007\ \mathrm{s}`$. The first exceeds the required $`0.00001\ \mathrm{s}`$ tolerance; the second is below it. The reference's last displayed decimal uncertainty is far too small to change either decision. Both estimates are below the reference in this example.

The first correction contains $`\epsilon=(v/c)^2`$, so first degree in $`\epsilon`$ is second degree in $`v/c`$. The additional $`\epsilon^2`$ term is fourth degree in $`v/c`$. The approximation order always refers to a specified variable. Gravity is omitted here, whereas a full GPS clock calculation includes gravitational effects. The accuracy decision above concerns the supplied simplified model, not the accuracy of a complete satellite timing system.

[Return to E6](practice.md#e6)

<a id="e7"></a>
E7

Let $`h=x-x_0`$ and construct $`A+Bh+Ch^2`$. At $`h=0`$ its value is $`A`$, its slope is $`B`$, and its second derivative is $`2C`$. Matching these to the function gives

```math
L(x)=f(x_0)+f'(x_0)(x-x_0),
```

```math
Q(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}2(x-x_0)^2.
```

For the data at 2, the displacement is $`h=0.03`$. The linear formula predicts 5 because the slope is zero. The quadratic formula gives

```math
f(2.03)\approx5+0(0.03)+\frac{-6}{2}(0.03)^2
=5-0.0027=4.9973.
```

The correction supplies the downward bending missed by a horizontal tangent. A stationary point does not imply the function remains constant nearby.

The claim is false. A zero second derivative makes the squared coefficient zero, as in sine at zero; the two approximations can even coincide. Quadratic approximation is a local construction, not a guarantee of greater accuracy at every input. For a concrete global counterexample, at $`x=2\pi`$ the linear cosine estimate 1 is exact, whereas $`1-x^2/2`$ is not. This input is far from the basepoint and does not contradict local approximation.

Continuous second derivative near 2 licenses the local remainder statement in section D. The three derivative data alone do not bound the error at the particular displacement 0.03 tightly enough to certify a requested tolerance. For example, functions $`5-3(x-2)^2+K(x-2)^3`$ with different finite constants $`K`$ all have those same value and first two derivatives at 2, while their omitted term at 2.03 is $`0.000027K`$. A bound or more information about the function is needed for a numerical tolerance claim. This is an example of an acceptable reasoned correction; the cosine counterexample is not the only valid one.

[Return to E7](practice.md#e7)

[Back to lesson](lesson.md) · [Practice](practice.md) · [Hints](hints.md)
