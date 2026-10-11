Lecture 7 — complete solutions

These solutions explain the decisions as well as the algebra. If you want a smaller step first, use the separate [hints](hints.md). The anticipated mistakes mentioned here are possible wrong routes, not claims about your work.

<a id="s1"></a>

Solution P1

From the exponential definition,

```math
q(x)=\frac{e^{2x}+e^{-2x}}2,
\qquad
q'(x)=\frac{2e^{2x}-2e^{-2x}}2
=e^{2x}-e^{-2x}=2\sinh(2x).
```

Each exponential retains its own exponent and is multiplied by that exponent's derivative. The contribution from $`e^{-2x}`$ is negative because $`(-2x)'=-2`$. At zero, $`q'(0)=1-1=0`$. This agrees with the horizontal tangent at the minimum of this even hyperbolic cosine function.

The ordinary cosine formula applies to $`\cos`$, a different function. It would incorrectly insert an additional negative sign if copied for $`\cosh`$. The exponential definition establishes the sign directly. [Return to P1](lesson.md#p1) · [Hint P1](hints.md#h1)

<a id="s2"></a>

Solution P2

The outer operation is division. The quotient rule, with the functions identified in the hint, gives

```math
F'(x)=\frac{\cos x(1+\cos x)-\sin x(-\sin x)}{(1+\cos x)^2}
=\frac{\cos x+\cos^2x+\sin^2x}{(1+\cos x)^2}
=\frac{1+\cos x}{(1+\cos x)^2}
=\frac1{1+\cos x}.
```

The original denominator must be nonzero, so exclude $`x=(2k+1)\pi`$ for every integer $`k`$: these are exactly the real inputs with $`\cos x=-1`$. The cancellation is valid only where the cancelled factor is nonzero; it cannot add points to the domain of the original function. The simplified derivative is also undefined at those points. As a local check, $`F'(0)=1/2`$.

A product-rule route using $`\sin x(1+\cos x)^{-1}`$ is equally valid when it preserves the same exclusions. The important numerator sign is positive in front of $`\sin^2x`$, since subtraction multiplies the negative derivative of cosine. [Return to P2](lesson.md#p2) · [Hint P2](hints.md#h2)

<a id="s3"></a>

Solution P3

First check the point: $`1^2+1\cdot2+2^2=7`$. On the local branch, implicit differentiation gives

```math
2x+(y+xy')+2yy'=0,
\qquad
(x+2y)y'=-(2x+y).
```

The term $`y+xy'`$ differentiates both factors of $`xy`$. At $`(1,2)`$, the coefficient $`x+2y`$ is $`5`$, so division is permitted:

```math
y'=-\frac{2x+y}{x+2y},
\qquad
y'(1,2)=-\frac45.
```

The tangent is therefore

```math
y-2=-\frac45(x-1).
```

This line passes through the given point and has the required gradient. Treating $`y`$ as constant in $`xy`$ would omit $`xy'`$ and give the wrong denominator. [Return to P3](lesson.md#p3) · [Hint P3](hints.md#h3)

<a id="s4"></a>

Solution P4

Fix $`x`$ and use a nonzero increment $`h`$. The cosine addition identity gives

```math
\frac{\cos(x+h)-\cos x}{h}
=\frac{\cos x\cos h-\sin x\sin h-\cos x}{h}
=\cos x\frac{\cos h-1}{h}
-\sin x\frac{\sin h}{h}.
```

The two ratios have the stated limits 0 and 1. Since $`\cos x`$ and $`\sin x`$ do not change as $`h`$ tends to zero, they are constant multipliers in this limit. The limit laws for a sum and constant multiples therefore give

```math
\frac d{dx}\cos x
=\cos x\,(0)-\sin x\,(1)
=-\sin x.
```

The negative sign is inherited from the cosine addition identity. It is not supplied by memorising the derivative. The limit requires radians for the two starting facts used here. [Return to P4](lesson.md#p4) · [Hint P4](hints.md#h4)

<a id="s5"></a>

Solution P5

For $`x\gt 0`$, the value $`y=x^x`$ is positive, so its real logarithm is defined. Taking logarithms keeps the varying exponent visible:

```math
\ln y=x\ln x,
\qquad
\frac{y'}y=1\cdot\ln x+x\frac1x=\ln x+1.
```

The left side uses the chain rule; the right side uses the product rule because both $`x`$ and $`\ln x`$ vary. Multiplying by $`y=x^x`$ gives

```math
y'=x^x(\ln x+1)\quad(x\gt 0).
```

Equivalently, differentiating $`e^{x\ln x}`$ by the chain and product rules gives the same expression. The constant-power rule assumed the exponent's derivative was zero. Here the exponent is $`x`$, whose derivative is 1, and its variation creates the $`\ln x`$ term. Substituting $`r=x`$ into a rule derived for fixed $`r`$ changes that assumption. A check only at $`x=1`$ would miss this mistake because $`\ln1=0`$; at $`x=e`$ the correct derivative is $`2e^e`$, which distinguishes it from the incorrectly substituted constant-power result $`e^e`$. [Return to P5](lesson.md#p5) · [Hint P5](hints.md#h5)

<a id="s6"></a>

Solution P6

(a) The outer function is arcsine and its inner input is $`2x`$. The original function is real when $`-1\le2x\le1`$, or $`-1/2\le x\le1/2`$. For an interior point, set $`y=\arcsin(2x)`$ and differentiate its defining relation:

```math
\sin y=2x,
\qquad
(\cos y)y'=2.
```

The principal range makes $`-\pi/2\lt y\lt \pi/2`$ in the interior, so cosine is positive. With $`\cos^2y=1-4x^2`$, this selects $`\cos y=\sqrt{1-4x^2}`$ rather than the negative root. Thus

```math
A'(x)=\frac2{\sqrt{1-4x^2}}
\quad\left(-\frac12\lt x\lt \frac12\right).
```

The endpoints belong to the function's domain but make this denominator zero; the inverse curve has no finite derivative there. A chain-rule derivation gives the same factor 2 from differentiating the inner input. Omitting it would confuse the outer derivative with the derivative of the whole composite.

(b) The outer operation is the exponential. Its exponent is a product, not a constant multiple. Set $`w=x^2\arctan x`$; then

```math
w'=2x\arctan x+\frac{x^2}{1+x^2},
\qquad
B'(x)=e^{x^2\arctan x}
\left(2x\arctan x+\frac{x^2}{1+x^2}\right).
```

The first term in $`w'`$ differentiates $`x^2`$ and retains $`\arctan x`$; the second retains $`x^2`$ and differentiates $`\arctan x`$. Both are required. All real $`x`$ are admissible here. Now substitute $`x=1`$ and $`\arctan1=\pi/4`$:

```math
B'(1)=e^{\pi/4}\left(\frac\pi2+\frac12\right)
=\frac{\pi+1}{2}e^{\pi/4}.
```

Recalling the derivative formulas and their conditions is retrieval. Constructing the nested differentiation and distinguishing the two domains in (a) applies those facts to changed expressions. A successful calculation shows that this particular route worked; it does not by itself establish long-term retention. [Return to P6](lesson.md#p6) · [Hint P6](hints.md#h6)

[Return to the lesson](lesson.md) · [Open the hints](hints.md)
