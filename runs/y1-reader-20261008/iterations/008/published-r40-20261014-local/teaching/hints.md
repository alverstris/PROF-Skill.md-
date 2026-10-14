<a id="hints-d008-start"></a>

Hints for linear and quadratic approximations

These give an intermediate step without the complete answer. Select the hint matching your attempt, then return to the question. Complete reasoning is in the separate [solutions file](solutions.md#solutions-d008-start).

[A1](#hints-d008-a1) · [A2](#hints-d008-a2) · [A3](#hints-d008-a3) · [A4](#hints-d008-a4) · [R1](#hints-d008-r1)

<a id="hints-d008-a1"></a>

Hint A1

The nearby input is $`2.04`$ but the derivative is evaluated at $`2`$. Start with

```math
L(2.04)=\ln2+\frac12(2.04-2).
```

The base value is supplied; only the tangent's change is left to add. Rounding describes the estimate's displayed precision.

[Return to A1](main.md#main-d008-a1) · [Complete solution A1](solutions.md#solutions-d008-a1)

<a id="hints-d008-a2"></a>

Hint A2

Build the two factors using $`\sin u\approx u`$ with $`u=3x`$, and the power rule with exponent $`-1/2`$. The sine factor has zero constant term. Write the product $`(3x)(1-x/2)`$ and label the degrees of its two terms before selecting the line. For the limit, observe that its numerator can be written as $`k(x)-k(0)`$.

[Return to A2](main.md#main-d008-a2) · [Complete solution A2](solutions.md#solutions-d008-a2)

<a id="hints-d008-a3"></a>

Hint A3

First square the speed ratio: $`q=(0.6)^2`$. The two candidate factors are $`1+q/2`$ and $`1+q/2+3q^2/8`$. Compute each absolute difference from $`1.25`$, and compare each difference with $`0.001`$. A correction being smaller than another correction does not by itself meet the stated tolerance.

[Return to A3](main.md#main-d008-a3) · [Complete solution A3](solutions.md#solutions-d008-a3)

<a id="hints-d008-a4"></a>

Hint A4

Multiply $`1+ax`$ by the complete quadratic model already obtained for $`f`$. The coefficient of $`x`$ becomes $`a-5/2`$. Set that coefficient to zero, then combine the original quadratic term with the product of the two linear terms. A horizontal tangent fixes only the first derivative; inspect the remaining quadratic coefficient before deciding whether the function is constant.

[Return to A4](main.md#main-d008-a4) · [Complete solution A4](solutions.md#solutions-d008-a4)

<a id="hints-d008-r1"></a>

Hint R1

Construct $`A+Bx+Cx^2`$ by matching $`A=f(0)`$, $`B=f'(0)`$ and $`2C=f''(0)`$. For cosine at zero, the three values are $`1,0,-1`$. Substitute $`x=0.2`$ into the line and quadratic, then compare with the supplied reference. For sine, evaluate $`-\sin0`$ to decide what happens to $`C`$.

[Return to R1](main.md#main-d008-revisit) · [Complete solution R1](solutions.md#solutions-d008-r1)

[Return to the main reading route](main.md#main-d008-start)
