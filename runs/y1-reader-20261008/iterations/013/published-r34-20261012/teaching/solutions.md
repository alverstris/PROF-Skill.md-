Solutions: mean value theorem and inequalities

Read these after attempting the corresponding exercise or using its [hint](hints.md). [Return to the lesson](main.md). These are reasoned solutions, not evidence that a reader has mastered the material.

<a id="d013-solutions-q1"></a>
Solution Q1

The polynomial $`t^3`$ is continuous on $`[-1,1]`$ and differentiable on $`(-1,1)`$, with derivative $`3t^2`$. Both MVT conditions hold. The secant slope is

```math
\frac{f(1)-f(-1)}{1-(-1)}=\frac{1-(-1)}{2}=1.
```

The matching equation is $`3c^2=1`$, giving $`c=1/\sqrt{3}`$ and $`c=-1/\sqrt{3}`$. Both lie strictly between $`-1`$ and $`1`$, because $`\sqrt{3}\gt 1`$. These are all solutions of the derivative equation. The theorem guaranteed at least one; the calculation finds two. Existence does not imply uniqueness, and neither point is the midpoint zero.

[Return to Q1](main.md#d013-main-q1) · [Hint Q1](hints.md#d013-hints-q1)

<a id="d013-solutions-q2"></a>
Solution Q2

The endpoint values are $`j(0)=0`$ and $`j(1)=2`$, so the secant slope is $`(2-0)/(1-0)=2`$. Every interior derivative equals $`1`$, because the interior function is $`j(t)=t`$. Thus no interior derivative has the secant slope.

At the right endpoint, $`\lim_{t\to1^-}j(t)=1`$ but $`j(1)=2`$. The endpoint value does not match the approach from inside the interval. Consequently $`j`$ is not continuous on $`[0,1]`$ and the MVT does not apply. Interior differentiability is present; endpoint continuity is the missing condition. There is no contradiction with the theorem.

[Return to Q2](main.md#d013-main-q2) · [Hint Q2](hints.md#d013-hints-q2)

<a id="d013-solutions-q3"></a>
Solution Q3

The anchor data are $`f(1)=1`$ and $`f'(1)=3`$. The tangent estimate at $`2`$ is $`1+3(2-1)=4`$. The exact value is $`f(2)=8`$, so the signed error is $`8-4=4`$; this tangent estimate is too small by four.

The polynomial satisfies the MVT conditions on $`[1,2]`$. The exact secant slope is $`(8-1)/(2-1)=7`$. Therefore a valid $`c`$ satisfies $`3c^2=7`$. The admissible root is $`c=\sqrt{7/3}`$: since $`1\lt 7/3\lt 4`$, it lies between $`1`$ and $`2`$. The negative root is outside the interval. Substitution gives $`f(2)=1+7(2-1)=8`$ exactly.

The midpoint is $`3/2`$, whose derivative is $`3(3/2)^2=27/4`$, not $`7`$. It is not the MVT point in this example. The square-function example's midpoint must not be made into a general rule. The approximation error can also be checked from the lesson's identity: $`[f'(c)-f'(1)](2-1)=(7-3)\cdot1=4`$.

[Return to Q3](main.md#d013-main-q3) · [Hint Q3](hints.md#d013-hints-q3)

<a id="d013-solutions-q4"></a>
Solution Q4

Take arbitrary $`a\lt b`$ in $`I`$. Because $`I`$ is an interval, it includes every input from $`a`$ to $`b`$. The assumed continuity supplies continuity on $`[a,b]`$, and each point strictly between them is an interior point of $`I`$, where the derivative exists. MVT therefore supplies $`a\lt c\lt b`$ with

```math
f(b)-f(a)=f'(c)(b-a).
```

Here $`f'(c)\lt 0`$ and $`b-a\gt 0`$, so $`f(b)-f(a)\lt 0`$. Hence $`f(a)\gt f(b)`$. The endpoints were arbitrary, which is precisely strict decrease throughout $`I`$.

For $`k`$, each nonzero input has a small neighborhood wholly on its own side of zero; the function is constant there, so its derivative is zero. However, $`k(-1)=0`$ and $`k(1)=1`$. The domain omits zero and is not one interval. MVT cannot be applied to $`[-1,1]`$, because the function is not even defined throughout that segment. The correct conclusion is that $`k`$ is constant on each separate interval $`(-\infty,0)`$ and $`(0,\infty)`$. The constants on those two intervals need not agree.

[Return to Q4](main.md#d013-main-q4) · [Hint Q4](hints.md#d013-hints-q4)

<a id="d013-solutions-q5"></a>
Solution Q5

Define the new difference

```math
r_5(t)=e^t-\left(1+t+\frac{t^2}{2}+\frac{t^3}{6}+\frac{t^4}{24}\right).
```

It is continuous and differentiable for real inputs, has $`r_5(0)=0`$, and

```math
r_5'(t)=e^t-\left(1+t+\frac{t^2}{2}+\frac{t^3}{6}\right)=r_4(t).
```

The preceding cubic inequality says $`r_4(t)\gt 0`$ for every $`t\gt 0`$. For any fixed $`x\gt 0`$, the derivative of $`r_5`$ is therefore positive throughout $`(0,x)`$. The increase result on $`[0,x]`$ gives $`r_5(x)\gt r_5(0)=0`$, which is exactly the requested strict bound. At $`x=0`$, both sides equal one, so the comparison is equality.

A finite lower bound says the remainder is positive. It supplies no reason that the remainder tends to zero as the number of terms grows. For example, the sequence $`1-1/n`$, for positive integer $`n`$, is below $`2`$ at every stage and increases, yet its limit is $`1`$, not $`2`$. Thus even increasing finite lower bounds need a separate argument about their limiting gap before equality with the target follows. The exponential-series equality is valid, but this positivity argument alone is not its proof.

[Return to Q5](main.md#d013-main-q5) · [Hint Q5](hints.md#d013-hints-q5)

<a id="d013-solutions-q6"></a>
Solution Q6

The logarithm requires $`1+t\gt 0`$, so use the domain $`t\gt -1`$. The denominator $`1+t`$ is also nonzero there. On this domain both proposed differences are continuous and differentiable, and their values at zero are zero because $`\ln1=0`$.

For the upper bound, choose $`A(t)=t-\ln(1+t)`$. The chain rule gives

```math
A'(t)=1-\frac{1}{1+t}=\frac{t}{1+t}.
```

For every positive $`t`$, numerator and denominator are positive. Given any $`x\gt 0`$, apply MVT on $`[0,x]`$: some $`0\lt c\lt x`$ gives $`A(x)-A(0)=A'(c)x\gt 0`$. Thus $`A(x)\gt 0`$, or $`\ln(1+x)\lt x`$.

For the lower bound, choose $`B(t)=\ln(1+t)-t/(1+t)`$. The quotient rule gives the derivative of $`t/(1+t)`$ as $`[(1+t)-t]/(1+t)^2=1/(1+t)^2`$. Hence

```math
B'(t)=\frac{1}{1+t}-\frac{1}{(1+t)^2}
=\frac{t}{(1+t)^2}.
```

This too is positive for $`t\gt 0`$. On $`[0,x]`$ the same finite-difference argument gives $`B(x)\gt B(0)=0`$, or $`x/(1+x)\lt \ln(1+x)`$. Combining the two inequalities gives the requested strict two-sided bound for every positive input.

For $`-1\lt x\lt 0`$, retain $`A`$ and use the interval $`[x,0]`$. Its interior inputs have negative numerator and positive denominator in $`A'(t)=t/(1+t)`$, so $`A'(t)\lt 0`$ there. MVT gives a $`c`$ between $`x`$ and zero such that

```math
A(0)-A(x)=A'(c)(0-x)\lt 0.
```

Since $`A(0)=0`$, this yields $`A(x)\gt 0`$ and hence $`\ln(1+x)\lt x`$ on the negative range as well. A negative derivative means the difference decreases as the input moves right toward the anchor zero; it does not mean its value to the left of the anchor is negative. At $`x=0`$ both comparisons become equalities, with all three quantities equal to zero. Inputs at or below $`-1`$ are outside the real logarithm's domain here.

[Return to Q6](main.md#d013-main-q6) · [Hint Q6](hints.md#d013-hints-q6)
