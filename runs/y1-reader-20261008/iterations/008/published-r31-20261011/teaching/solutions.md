<a id="d008-r31-solutions-start"></a>

Solutions for linear and quadratic approximations

These solutions explain the decisions as well as the results. For a smaller nudge first, use the separate [hints](hints.md#d008-r31-hints-start). The [main notes](README.md#d008-r31-main-start) contain the complete teaching route.

<a id="d008-r31-solution-p1"></a>

Solution P1

Let $`f(x)=\sqrt{x}`$ and choose $`a=4`$, so $`f(4)=2`$. Differentiating gives $`f'(x)=1/(2\sqrt{x})`$ and therefore $`f'(4)=1/4`$. The tangent formula is

```math
L(x)=2+\frac{x-4}{4}.
```

The displacement is $`h=4.08-4=0.08`$, giving

```math
\sqrt{4.08}\approx L(4.08)=2+\frac{0.08}{4}=2.02.
```

The tangent agrees with the curve in height and slope at 4; it need not agree at 4.08. Indeed, $`2.02^2=4.0804`$, so 2.02 is not exactly the requested root. This numerical check distinguishes an approximation from an identity. It also shows the estimate is slightly too high, since the positive square function increases with its input.

[Return to P1](README.md#d008-r31-main-p1) · [Hint P1](hints.md#d008-r31-hint-p1)

<a id="d008-r31-solution-p2"></a>

Solution P2

The original function is defined for every real input except $`x=1/2`$. For example, the neighborhood $`|x|\lt 1/4`$ avoids that point. For a useful approximation we take inputs sufficiently close to zero within that neighborhood; the domain condition alone is not an error guarantee.

The exponential input is $`3x`$, and the reciprocal power uses input $`-2x`$ with exponent −1. Both tend to zero as $`x\to0`$. Thus

```math
e^{3x}\approx1+3x,
\qquad (1-2x)^{-1}\approx1+2x.
```

The constant and linear terms in their product are

```math
g(x)\approx1+(3+2)x=1+5x.
```

Multiplying only those two polynomials gives $`1+5x+6x^2`$, but the square term 6 comes solely from the product of the linear terms. A square term from either original factor times the other's constant also contributes to the true quadratic coefficient. Those terms were omitted in constructing the linear factors, so 6 is not established as that coefficient.

Using the quadratic formulas now available in the notes confirms the distinction: the two additional contributions are $`9/2`$ from the exponential and 4 from the reciprocal, giving total quadratic coefficient $`9/2+6+4=29/2`$. The linear answer remains valid because the omitted terms have vanishing ratio to $`x`$ near zero.

[Return to P2](README.md#d008-r31-main-p2) · [Hint P2](hints.md#d008-r31-hint-p2)

<a id="d008-r31-solution-p3"></a>

Solution P3

For positive inputs the logarithm has derivatives $`1/x`$ and $`-1/x^2`$. At the chosen base point,

```math
f(2)=\ln2,\qquad f'(2)=\frac12,\qquad f''(2)=-\frac14.
```

Consequently

```math
L(x)=\ln2+\frac{x-2}{2},
\qquad
Q(x)=\ln2+\frac{x-2}{2}-\frac{(x-2)^2}{8}.
```

The square is the square of the displacement from 2. It vanishes at the base point and gives zero contribution to the first derivative there, while supplying the desired second derivative. Replacing it by $`x^2`$ would change the value and slope at the base point and defeat the matching construction.

At the requested input the displacement is 0.04, so, using the supplied rounded value of the logarithm at 2,

```math
L(2.04)\approx0.69314718+0.02=0.71314718,
```

```math
Q(2.04)\approx0.69314718+0.02-0.0002=0.71294718.
```

Against the supplied comparison 0.71294981, the absolute discrepancies at the shown precision are approximately 0.00019737 and 0.00000263, respectively. The linear estimate is high and the quadratic estimate low at this input. The quadratic estimate is closer here. Because both reference decimals are rounded, these are numerical comparisons at that precision, not exact error identities or a universal error bound.

[Return to P3](README.md#d008-r31-main-p3) · [Hint P3](hints.md#d008-r31-hint-p3)

<a id="d008-r31-solution-p4"></a>

Solution P4

The constant and linear terms cancel in the numerator. The quadratic expansion with its justified local error is

```math
e^x=1+x+\frac{x^2}{2}+R_2(x),
\qquad \frac{R_2(x)}{x^2}\longrightarrow0.
```

The exponential has a continuous second derivative near zero, so section 5 supplies this error condition. For nonzero inputs,

```math
\frac{e^x-1-x}{x^2}
=\frac12+\frac{R_2(x)}{x^2}\longrightarrow\frac12.
```

A linear expansion would give only a remainder whose ratio to $`x`$ tends to zero. That does not determine its ratio to $`x^2`$; for example, any constant multiple of $`x^2`$ satisfies the first condition while leaving that constant after division by the square. Declaring the linear numerator to be exactly zero would therefore lose the very information the limit is asking for.

[Return to P4](README.md#d008-r31-main-p4) · [Hint P4](hints.md#d008-r31-hint-p4)

<a id="d008-r31-solution-p5"></a>

Solution P5

The speed units cancel in the ratio:

```math
\frac vc=\frac{6}{3\times10^5}=2\times10^{-5},
\qquad q=4\times10^{-10}.
```

The term linear in the dimensionless quantity $`q`$ gives

```math
\frac{T'-T}{T}\approx\frac q2=2\times10^{-10}.
```

Multiplying by the onboard time converts this fraction into a time difference:

```math
T'-T\approx(86400\ \mathrm{s})(2\times10^{-10})
=1.728\times10^{-5}\ \mathrm{s}
=17.28\ \mathrm{microseconds}.
```

One microsecond is $`10^{-6}`$ seconds. The next fractional contribution is

```math
\frac{3q^2}{8}
=\frac38(4\times10^{-10})^2
=6\times10^{-20}.
```

Adding this term changes the fractional estimate by far less than $`10^{-12}`$. The first contribution is proportional to $`(v/c)^2`$, the next to $`(v/c)^4`$. Thus a linear approximation in the variable $`q`$ already has a quadratic speed dependence.

This calculation compares the displayed two corrections. It does not, by itself, bound the sum of every remaining term. A certified tolerance for the exact ratio would additionally require a bound on that remainder. The comparison nevertheless answers the stated question about the effect of adding this particular term. Both corrections are positive in the supplied model, consistent with a longer reference-frame interval than moving-clock interval.

[Return to P5](README.md#d008-r31-main-p5) · [Hint P5](hints.md#d008-r31-hint-p5)

<a id="d008-r31-solution-p6"></a>

Solution P6

The original function is defined on $`x\gt -1/2`$, so a two-sided interval about zero is available. Subtracting a linear term and dividing by $`x^2`$ suggests retaining the square term and checking an error small compared with the square. The two expansions are

```math
\ln(1+2x)\approx2x-\frac{(2x)^2}{2}=2x-2x^2,
\qquad e^{-x}\approx1-x+\frac{x^2}{2}.
```

The logarithm has no constant term. Its linear term times the exponential's constant gives $`2x`$. At degree two, the logarithm's square term times 1 gives $`-2x^2`$, and its linear term times the exponential's linear term gives another $`-2x^2`$. There is no contribution from an exponential square times a logarithm constant, because that constant is zero. Hence

```math
H(x)=2x-4x^2+R(x),
\qquad \frac{R(x)}{x^2}\longrightarrow0.
```

The error condition follows from section 7's product argument: each factor has the quadratic remainder property, both factors are bounded near zero, and discarded polynomial products of degree at least three vanish after division by $`x^2`$. The logarithm's required derivatives are continuous in the positive-input neighborhood, and the exponential's are continuous there too.

Therefore, for nonzero inputs,

```math
\frac{H(x)-2x}{x^2}
=-4+\frac{R(x)}{x^2}\longrightarrow-4.
```

The chosen expansion order supplies the coefficient left after cancellation. The same method of combining functions was used earlier, but the zero constant and the final division change which contributions must be tracked.

[Return to P6](README.md#d008-r31-main-p6) · [Hint P6](hints.md#d008-r31-hint-p6)

End of solutions. [Return to the reading route](README.md#d008-r31-main-start).
