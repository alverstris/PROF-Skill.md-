Lecture 16 — Complete solutions

These are reasoned solutions to the five generated tasks. [Hints](hints.md) are separate. [Return to the reading route](teaching.md).

<a name="a1"></a>
Solution Q1

The input function is $`u(x)=x^2`$. Its derivative is $`2x`$ and multiplying it by $`x`$ gives $`x^3`$. Thus $`L[x^2]=2x+x^3`$, a new function of $`x`$. The operator is not being applied to the number 2 or multiplied by a constant labelled $`x^2`$.

The solution family of $`L[y]=0`$ is $`y=ae^{-x^2/2}`$. At zero this gives $`y(0)=a`$, so the first initial value selects $`y=-2e^{-x^2/2}`$. Its derivative is $`2xe^{-x^2/2}`$, while $`xy=-2xe^{-x^2/2}`$. Their sum is zero at every real $`x`$, and its value at zero is $`-2`$.

The second initial value selects $`y=0`$. Its derivative and $`xy`$ are both zero, so it satisfies the original equation and $`y(0)=0`$. Dividing by $`y`$ would exclude this function before the integration starts; it must be recovered from the original equation. The product-rule completeness check in section 2 shows that the same family covers all solutions, including this one, without that division.

Anticipated error: treating $`e^c`$ as possibly zero would not repair the division. An exponential of a finite real constant is positive; testing the excluded function is what justifies adding it.

[Return to Q1](teaching.md#q1) · [Hint Q1](hints.md#h1)

<a name="a2"></a>
Solution Q2

The right-hand side is a product of $`f(x)=x`$ and $`g(y)=1+y^2`$. For real $`y`$, $`g(y)>0`$, so division discards no zero of this factor. The reciprocal is $`h(y)=1/(1+y^2)`$. Choose $`H(y)=\arctan y`$ and $`F(x)=x^2/2`$, whose derivatives are the required functions. Separation yields

```math
\arctan y=\frac{x^2}{2}+c.
```

Using $`y(0)=0`$ and $`\arctan0=0`$ gives $`c=0`$. Arctangent takes real inputs to $`(-\pi/2,\pi/2)`$, on which tangent is its inverse. Therefore

```math
y=\tan\left(\frac{x^2}{2}\right),
\qquad -\frac{\pi}{2}<\frac{x^2}{2}<\frac{\pi}{2}.
```

The left inequality holds automatically; the right gives $`x^2<\pi`$. The largest open interval containing zero before the solution becomes infinite is $`(-\sqrt\pi,\sqrt\pi)`$. At each endpoint the tangent argument approaches $`\pi/2`$, and the solution grows without bound. Other intervals where tangent happens to be finite do not extend this solution continuously through those infinities or satisfy the same implicit arctangent relation.

The derivative is $`x\sec^2(x^2/2)`$. Using $`\sec^2 u=1+\tan^2u`$, it equals $`x(1+y^2)`$; the value at zero is zero. A constant $`y=b`$ would require $`0=x(1+b^2)`$ at every point of an open interval. Since $`1+b^2>0`$, this cannot hold on such an interval. Thus there is no omitted constant solution, even though the right-hand side vanishes at the individual input $`x=0`$.

[Return to Q2](teaching.md#q2) · [Hint Q2](hints.md#h2)

<a name="a3"></a>
Solution Q3

The ray's rise over run is $`y/x`$. A tangent slope twice this is $`y'=2y/x`$, defined on the requested $`x>0`$. For a nonzero branch,

```math
\frac{dy}{y}=2\frac{dx}{x},\qquad
\ln\lvert y\rvert=2\ln x+c,
\qquad y=ax^2.
```

The separately restored zero solution belongs to the general family but cannot pass through $`(2,-4)`$. Inserting that point gives $`-4=4a`$, so $`a=-1`$ and $`y=-x^2`$. It has derivative $`-2x`$, which equals $`2(-x^2)/x`$ for $`x>0`$, and $`y(2)=-4`$.

At the given point the ray slope is $`-4/2=-2`$, and the tangent slope is $`-2(2)=-4`$, twice the ray slope. Both are signed slopes; “twice” does not mean an absolute-value comparison only.

The formula $`-x^2`$ can be evaluated and differentiated at zero. The original ODE cannot: $`2y/x`$ becomes an undefined quotient there, and the ray from the origin to itself has no slope. The requested solution is therefore on $`x>0`$; a polynomial extension does not turn zero into an allowed ODE input.

[Return to Q3](teaching.md#q3) · [Hint Q3](hints.md#h3)

<a name="a4"></a>
Solution Q4

For the parabola through an intersection with $`x\ne0`$, $`a=y/x^2`$; substituting in $`2ax`$ gives slope $`2y/x`$. At points with $`y\ne0`$ as well, a perpendicular slope is $`-x/(2y)`$. Separating and integrating gives

```math
y\,dy=-\frac{x}{2}\,dx,
\qquad \frac{x^2}{4}+\frac{y^2}{2}=c.
```

Substitute $`(2,1)`$: $`c=4/4+1/2=3/2`$. Thus the implicit answer can be written in either form

```math
\frac{x^2}{4}+\frac{y^2}{2}=\frac32,
\qquad \frac{x^2}{6}+\frac{y^2}{3}=1.
```

The squared semiaxes are 6 and 3, so their lengths are $`\sqrt6`$ horizontally and $`\sqrt3`$ vertically. Their ratio is $`\sqrt2`$, agreeing with the family. Since the given point has positive $`y`$, the branch through it is

```math
y=\sqrt{3-\frac{x^2}{2}},\qquad -\sqrt6<x<\sqrt6.
```

The strict inequalities make the radicand positive, hence $`y\ne0`$ and a finite derivative is available. Differentiating gives $`y'=-x/(2\sqrt{3-x^2/2})=-x/(2y)`$, and at $`x=2`$ the value is 1. At that point the parabola parameter is $`a=1/4`$, so its slope is $`2ax=1`$. The ellipse slope is $`-2/(2\cdot1)=-1`$. The product $`-1`$ checks perpendicularity.

The full ellipse includes both signs of the square root and the endpoints $`(\pm\sqrt6,0)`$, so it is not one single-valued graph $`y(x)`$. The upper branch can be extended continuously to those endpoints, but its derivative is not finite there and $`-x/(2y)`$ is undefined. The full ellipse has vertical tangents there, perpendicular to the horizontal $`a=0`$ member. This geometrical fact does not remove the ODE's division restriction. At its two vertical-axis points it does not intersect any finite-parameter parabola of the family, as section 5 explains.

[Return to Q4](teaching.md#q4) · [Hint Q4](hints.md#h4)

<a name="a5"></a>
Solution Q5

For (i), the derivative is already a known function of $`x`$, so direct integration gives $`y=x^3+c`$. The initial condition is $`2=1+c`$, hence $`y=x^3+1`$, defined for all real $`x`$. Its derivative is $`3x^2`$ and its value at 1 is 2. Separating with a trivial factor $`g(y)=1`$ would also work, but is unnecessary.

For (ii), the slope contains a product of an $`x`$-factor and $`y`$. Separation gives $`dy/y=2\,dx/x`$ on a nonzero branch. The result is $`\ln\lvert y\rvert=2\ln\lvert x\rvert+c`$, hence $`y=ax^2`$. Retaining the modulus matters on $`x<0`$; $`\ln x`$ would not be real there. The zero solution also belongs to the family but does not satisfy this initial value. Using $`y(-1)=2`$ gives $`a=2`$, so $`y=2x^2`$ on $`x<0`$. Its derivative $`4x`$ equals $`2(2x^2)/x`$, and its value at $`-1`$ is 2.

For the proposed $`y=2x`$, checking the equation first already finds a failure: its derivative is 2, but $`2y/x=4`$ for every allowed $`x`$. It also fails the initial condition because $`y(-1)=-2`$, not 2. Either check disproves it; there is no unique chronological “first” unless a check order is chosen. More generally, satisfying an initial value alone would still not establish an ODE solution.

Before separating $`y'=f(x)g(y)`$, keep to the original domain (in this example $`x\ne0`$) and require $`g(y)\ne0`$ for the division. Test the zeros of $`g`$ separately in the original equation. After integration, respect logarithm/inverse domains and selected branches and check any further divisions or square roots used when isolating $`y`$. Separation is a conditional equivalence, not a rule for cancelling zero.

[Return to Q5](teaching.md#q5) · [Hint Q5](hints.md#h5)
