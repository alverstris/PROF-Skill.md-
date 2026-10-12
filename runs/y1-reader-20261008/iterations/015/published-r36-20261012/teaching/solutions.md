<a id="d015-r36-solution-start"></a>

Complete solutions for Differential equations: from a slope rule to a curve

These solutions explain the consequential decisions as well as the answers. Use the separate hints first if you want an intermediate step without the full route.

[Q1](#d015-r36-solution-q1) · [Q2](#d015-r36-solution-q2) · [Q3](#d015-r36-solution-q3) · [Q4](#d015-r36-solution-q4) · [Q5](#d015-r36-solution-q5)

<a id="d015-r36-solution-q1"></a>

Solution Q1

The proposed conclusion is invalid. Dividing by y assumed y was nonzero; it cannot settle the excluded case. The function $`y(x)=0`$ has $`y'=0=-x\cdot0`$ and $`y(0)=0`$, so it satisfies both requirements on all real x.

For the second initial condition, the family $`y=ae^{-x^2/2}`$ gives $`a=-2`$. Thus

```math
y=-2e^{-x^2/2},\qquad y'=2xe^{-x^2/2}=-xy,\qquad y(0)=-2.
```

The derivative check holds for every real x. Exponentiation correctly gave a nonzero a within the divided calculation. The mistake was applying that restriction to every solution of the original equation. A negative a is allowed: the absolute value in the logarithm had not specified that y must be positive.

[Return to Q1](main.md#d015-r36-main-q1) · [Hint Q1](hints.md#d015-r36-hint-q1)

<a id="d015-r36-solution-q2"></a>

Solution Q2

The factor $`1-y`$ is zero when y=1. A constant y=1 has derivative zero and right side $`x(1-1)=0`$, so it is a solution. It meets the second initial condition.

For the initial value y(0)=2 we seek the branch with $`y\ne1`$. Separate and integrate:

```math
\frac{dy}{1-y}=x\,dx,\qquad
-\ln|1-y|=\frac{x^2}{2}+C.
```

Multiplying by −1 and renaming the arbitrary constant gives $`\ln|1-y|=-x^2/2+K`$. Exponentiating and restoring the sign gives

```math
1-y=Ae^{-x^2/2}.
```

At x=0, $`1-2=A`$, so A=−1 and

```math
y=1+e^{-x^2/2}.
```

Its derivative is $`-xe^{-x^2/2}`$; the original right side is $`x(1-y)=-xe^{-x^2/2}`$, and its initial value is 2. For any finite real x the exponential is positive, so this solution stays strictly above y=1. It approaches 1 as the magnitude of x grows, without reaching it at any finite x. Both solutions are defined on all real x. Division would have discarded y=1 if we had not checked it separately.

[Return to Q2](main.md#d015-r36-main-q2) · [Hint Q2](hints.md#d015-r36-hint-q2)

<a id="d015-r36-solution-q3"></a>

Solution Q3

The origin-to-point slope is $`y/x`$, so the required equation is $`y'=3y/x`$ on $`x\lt 0`$. On the nonzero branch through the given point,

```math
\frac{dy}{y}=3\frac{dx}{x},\qquad
\ln|y|=3\ln|x|+C,\qquad
|y|=e^C|x|^3.
```

The positive initial y-coordinate selects the positive sign on this connected nonzero branch. At x=−1 the absolute-value factor is 1 and y=2, so $`y=2|x|^3`$. Since $`|x|=-x`$ for $`x\lt 0`$, the formula is

```math
y=-2x^3,\qquad x\lt 0.
```

Its derivative is $`-6x^2`$, while $`3y/x=-6x^2`$ on that interval. At $`(-1,2)`$, the origin-to-point slope is $`2/(-1)=-2`$ and the tangent slope is −6, exactly three times it. This also checks the sign that could be lost by replacing $`|x|`$ with x too early.

The polynomial can be evaluated and differentiated at zero, but $`3y/x`$ cannot be evaluated there. Extending the formula as a smooth curve does not remove the denominator from the original equation. The constant zero solution would solve the equation on negative x, but it cannot pass through the given point.

[Return to Q3](main.md#d015-r36-main-q3) · [Hint Q3](hints.md#d015-r36-hint-q3)

<a id="d015-r36-solution-q4"></a>

Solution Q4

The parabola-family slope at a point with $`x\ne0`$ is $`2y/x`$, so the perpendicular slope is $`-x/(2y)`$ where y is also nonzero. Its integrated family is $`x^2/4+y^2/2=C`$. Using P gives

```math
C=\frac{2^2}{4}+\frac{(-1)^2}{2}=\frac32.
```

The required implicit curve and its unit-right-side form are

```math
\frac{x^2}{4}+\frac{y^2}{2}=\frac32,\qquad
\frac{x^2}{6}+\frac{y^2}{3}=1.
```

Thus the horizontal semiaxis is $`\sqrt6`$ and the vertical semiaxis is $`\sqrt3`$. The implicit curve includes upper and lower y values. The branch through the negative y-coordinate of P is

```math
y=-\sqrt{3-\frac{x^2}{2}}.
```

Strictly negative y requires $`3-x^2/2\gt 0`$, or $`-\sqrt6\lt x\lt \sqrt6`$. Combining this with positive x gives the maximal open interval requested:

```math
0\lt x\lt \sqrt6.
```

It contains x=2 because $`4\lt 6`$. At its left boundary x=0 the original parabola slope expression is undefined; at its right boundary y=0 the reciprocal slope expression is undefined. Those are the relevant restrictions even though the ellipse exists geometrically at the boundary points.

At P the parabola slope is $`2(-1)/2=-1`$ and the perpendicular slope is $`-2/(2(-1))=1`$. Their product is −1. As a further branch check, differentiation gives

```math
y'=\frac{x}{2\sqrt{3-x^2/2}}=-\frac{x}{2y},
```

and substituting x=2 gives y=−1. A single negative square-root branch contains no upper half of the ellipse. The full loop fails the one-y-per-x condition for a function, so its implicit description conveys more of the geometric curve than this solution branch.

[Return to Q4](main.md#d015-r36-main-q4) · [Hint Q4](hints.md#d015-r36-hint-q4)

<a id="d015-r36-solution-q5"></a>

Solution Q5

(a) The derivative's right side depends only on x, so direct antidifferentiation gives $`y=x^2+C`$. The condition $`3=1+C`$ fixes C=2. The result $`y=x^2+2`$ has derivative 2x and takes the value 3 at x=1. It is defined on all real x. No division by y was needed.

(b) First keep a fixed while differentiating each member of the given family:

```math
y'=-\frac{a}{x^2}.
```

At a point on the family, $`a=xy`$. Its slope therefore becomes $`-y/x`$. For nonzero y and positive x, the perpendicular slope is the negative reciprocal:

```math
\frac{dy}{dx}=-\frac{1}{-y/x}=\frac{x}{y}.
```

Separation and integration give

```math
y\,dy=x\,dx,\qquad
\frac{y^2}{2}=\frac{x^2}{2}+C,\qquad
y^2-x^2=K,
```

where $`K=2C`$ is still an arbitrary constant. At $`(1,2)`$, K=3. An implicit equation is therefore $`y^2-x^2=3`$, and the branch through the point is

```math
y=\sqrt{x^2+3},\qquad x\gt 0.
```

The radicand is positive and the selected y remains positive on this entire interval, so both slope expressions stay nonzero and finite. Its derivative is $`x/\sqrt{x^2+3}=x/y`$. At the given point the original family's slope is −2 and the new curve's slope is $`1/2`$, whose product is −1; the new formula also gives y=2 at x=1.

The changed family matters: differentiating a reciprocal curve produced $`-y/x`$ rather than the parabola family's $`2y/x`$. Copying the earlier ellipse equation would miss this change. The reusable operation is to derive the family slope, eliminate its fixed parameter, and only then take the negative reciprocal.

[Return to Q5](main.md#d015-r36-main-q5) · [Hint Q5](hints.md#d015-r36-hint-q5)

[Return to the reading route](main.md#d015-r36-main-start) · [Grouped hints](hints.md#d015-r36-hint-start)
