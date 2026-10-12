Complete solutions for Lecture 9

These solutions include the reasoning as well as the results. [Return to the lesson](lesson.md) or [open the grouped hints](hints.md). Each exercise allows equivalent correct reasoning under its stated conditions.

<a id="d008-solution-e1"></a>

Solution D008-E1

The displacement is $`h=4.08-4=0.08`$. For $`f(x)=\sqrt{x}=x^{1/2}`$, the derivative is $`f'(x)=1/(2\sqrt{x})`$ for positive $`x`$. Thus $`f(4)=2`$ and $`f'(4)=1/4`$. The constructed tangent and estimate are

```math
L(x)=2+\frac{x-4}{4},\qquad
\sqrt{4.08}\approx L(4.08)=2+\frac{0.08}{4}=2.02.
```

The derivative gives a local slope at the easy base point; multiplying it by the displacement estimates the output change. The original square-root curve is not this line: for example, $`2.02^2=4.0804`$, not 4.08. The tangent error is controlled only locally by differentiability unless a quantitative bound is also supplied. This answer therefore does not assert exact equality or a particular number of guaranteed decimal places.

[Return to E1](lesson.md#d008-main-e1) · [Hint E1](hints.md#d008-hint-e1)

<a id="d008-solution-e2"></a>

Solution D008-E2

Use $`e^{3x}\approx1+3x`$ near zero. Multiplication gives

```math
(1+3x)(1-2x)=1+x-6x^2,
\qquad g(x)\approx1+x.
```

The displayed $`-6x^2`$ is not a justified quadratic coefficient for $`g`$ because the exponential's own quadratic contribution was discarded. For the requested limit, $`g(0)=1`$ and the product rule independently gives

```math
g'(x)=3e^{3x}(1-2x)-2e^{3x},\qquad g'(0)=3-2=1.
```

The expression in the prompt is exactly $`[g(x)-g(0)]/x`$ for nonzero $`x`$. Its limit is therefore $`g'(0)=1`$ by the derivative definition. This supplies the warrant that an approximate equality alone would lack. Equivalently, the controlled linear remainder is $`x\varepsilon(x)`$ with $`\varepsilon(x)\to0`$, leaving $`1+\varepsilon(x)`$ after division.

[Return to E2](lesson.md#d008-main-e2) · [Hint E2](hints.md#d008-hint-e2)

<a id="d008-solution-e3"></a>

Solution D008-E3

For positive $`x`$, $`f'(x)=1/x`$ and $`f''(x)=-1/x^2`$. At 2 the three matching data are $`\ln2`$, $`1/2`$ and $`-1/4`$. With $`h=x-2`$,

```math
Q(x)=\ln2+\frac{x-2}{2}-\frac{(x-2)^2}{8}.
```

Indeed, the square coefficient must obey $`2C=f''(2)=-1/4`$, so $`C=-1/8`$. At $`x=2.1`$ the displacement is 0.1, giving

```math
\ln(2.1)-\ln2
\approx\frac{0.1}{2}-\frac{0.1^2}{8}
=0.05-0.00125=0.04875.
```

The constant cancels. As another check of the change of variable, the exact logarithmic difference is $`\ln(2.1/2)=\ln(1.05)`$. The zero-based logarithm formula at input 0.05 gives $`0.05-0.05^2/2=0.04875`$, the same estimate. Confusing $`x`$ with $`x-2`$ would not match the value and derivatives at the requested base point.

[Return to E3](lesson.md#d008-main-e3) · [Hint E3](hints.md#d008-hint-e3)

<a id="d008-solution-e4"></a>

Solution D008-E4

Both factors are well-defined near zero with $`x\gt -1/2`$. Use the exponential formula and substitute $`2x`$ in the power formula:

```math
e^x\approx1+x+\frac{x^2}{2},\qquad
(1+2x)^{-1/2}\approx1-x+\frac32x^2.
```

The constant is 1. The linear coefficient is $`1-1=0`$. The quadratic coefficient combines all three relevant products:

```math
\frac12+(1)(-1)+\frac32=1.
```

Thus the linear approximation is $`H(x)\approx1`$ and the quadratic approximation is $`H(x)\approx1+x^2`$. The line misses the leading variation because the individual first-order changes cancel. The quadratic predicts an increase above 1 for small nonzero positive and negative inputs, since $`x^2`$ is positive on both sides. Its remainder divided by $`x^2`$ tends to zero, so sufficiently close to zero the positive quadratic contribution controls that sign. This is a local statement, not the identity $`H(x)=1+x^2`$ on the entire domain. The function is a product of smooth elementary functions there, satisfying the section 5 condition for the quadratic remainder.

[Return to E4](lesson.md#d008-main-e4) · [Hint E4](hints.md#d008-hint-e4)

<a id="d008-solution-e5"></a>

Solution D008-E5

The factor is approximated by $`1+z/2`$ or $`1+z/2+3z^2/8`$. Subtracting $`T`$ after multiplying gives

```math
(T'-T)_{\mathrm{linear}}\approx
1000\,\mathrm{s}\times\frac{10^{-4}}2=0.05\,\mathrm{s},
```

```math
(T'-T)_{\mathrm{quadratic}}\approx
1000\,\mathrm{s}\left(\frac{10^{-4}}2+\frac38\,10^{-8}\right)
=0.05000375\,\mathrm{s}.
```

These are linear and quadratic in the dimensionless variable $`z=v^2/c^2`$. The corresponding speed terms have powers two and four. The extra quadratic contribution is $`3.75\times10^{-6}\,\mathrm{s}`$.

For the required guarantee, use the supplied bound on the entire linear error:

```math
|T'-T(1+z/2)|\le T\frac{z^2}{2}
=1000\,\mathrm{s}\times\frac{10^{-8}}2
=5\times10^{-6}\,\mathrm{s}
\lt 10^{-5}\,\mathrm{s}.
```

So the linear calculation alone already meets this stated absolute-error requirement in the given model. The quadratic correction is also smaller than that requirement, but that observation alone would not bound every remaining term. The derivative bound over the interval is what supplies the guarantee. Subtracting the exact fixed $`T`$ changes neither the approximation error nor its bound. Nothing here accounts for gravity or uncertainties in the model inputs; the result concerns the stipulated model and exact supplied values.

[Return to E5](lesson.md#d008-main-e5) · [Hint E5](hints.md#d008-hint-e5)

<a id="d008-solution-e6"></a>

Solution D008-E6

The two formulas to recall are

```math
L(x)=f(x_0)+f'(x_0)(x-x_0),
```

```math
Q(x)=f(x_0)+f'(x_0)(x-x_0)
+\frac{f''(x_0)}{2}(x-x_0)^2.
```

Recall is checked by the correct base-point values, displacement and factor one-half; it does not establish successful method choice in the following cases.

For sine at zero, the second derivative is zero. Both approximations are $`x`$, so changing the label from linear to quadratic does not improve this polynomial. The first nonzero correction in the stated expansion is $`-x^3/6`$; retaining it would be a cubic approximation.

For the exponential, the effective input is $`u=50x`$. At $`x=0.02`$ it equals 1, not a number small compared with 1. The smallness of $`x`$ alone does not justify the truncation. The linear polynomial gives 2, whereas the supplied exponential series at input 1 already begins $`1+1+1/2+\cdots`$ with further positive terms. Thus even the next contribution is substantial; an accuracy claim needs an appropriate evaluation or bound, not the bare small-input slogan.

For the square root at zero, only the right side lies in the real domain. Its right-hand difference quotient is

```math
\frac{\sqrt{h}-0}{h}=\frac1{\sqrt{h}},\qquad h\gt 0.
```

It increases without a finite limit as $`h\to0^+`$. There is no finite slope to insert into the usual tangent approximation, even one-sided. A vertical geometric tangent is not a function of the form $`L(x)=f(0)+mx`$ with finite $`m`$. This does not prevent approximating the square root by other methods or using a positive base point; it rules out this particular construction at zero.

[Return to E6](lesson.md#d008-main-e6) · [Hint E6](hints.md#d008-hint-e6)
