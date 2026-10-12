Solutions for Mean value theorem and inequalities

These are complete reasoned solutions to the generated practice. Use [the hints](hints.md) for a smaller next step, or [return to the lesson](main.md). Equivalent correct reasoning is acceptable; the response criteria in each prompt identify what must be justified.

<a name="d013-solutions-p1"></a>

Solution P1. The polynomial $`f(x)=x^2`$ is continuous on $`[1,4]`$ and differentiable on $`(1,4)`$, so the MVT applies. Its average slope is

```math
\frac{f(4)-f(1)}{4-1}=\frac{16-1}{3}=5.
```

The derivative condition is $`2c=5`$, so $`c=5/2`$. It lies strictly between 1 and 4, and it is the only solution of that linear equation. The tangent slope at that point equals the slope of the line joining the two endpoint points. Thus the tangent and secant are parallel. The equality concerns their slopes, not their heights.

[Return to P1](main.md#d013-main-p1) · [Hint P1](hints.md#d013-hints-p1)

<a name="d013-solutions-p2"></a>

Solution P2. In (a), the absolute-value function is continuous on $`[-1,2]`$ but fails to be differentiable at the interior point zero. The endpoint values are 1 and 2, giving secant slope $`(2-1)/(2-(-1))=1/3`$. At negative interior inputs the derivative is $`-1`$; at positive inputs it is $`1`$; at zero it is undefined. None equals $`1/3`$. Thus the theorem is unavailable, and the conclusion also fails in this case.

In (b), the limit of $`g(x)=x`$ as $`x`$ approaches 1 from below is 1, but the assigned endpoint value is 2. Hence continuity on the closed interval fails. The derivative is nevertheless 1 at every interior input. The secant slope is $`(g(1)-g(0))/(1-0)=2`$, so no interior derivative equals it. Here too the conclusion fails by direct calculation.

The logic matters: missing a sufficient hypothesis removes a guarantee. It does not prove that the conclusion always fails whenever the hypothesis is absent. The derivative computations, beyond merely naming the failed hypotheses, established failure for these two particular functions. A response that stops at “MVT does not apply” has not yet checked the question's second demand.

[Return to P2](main.md#d013-main-p2) · [Hint P2](hints.md#d013-hints-p2)

<a name="d013-solutions-p3"></a>

Solution P3. At $`a=2`$, the value is 4 and the derivative is 4. The input change is 0.2, so the tangent estimate is $`4+4(0.2)=4.8`$. The exact value is $`2.2^2=4.84`$, giving signed error $`4.84-4.8=0.04`$. The MVT hypotheses hold because the function is a polynomial. Its secant slope is

```math
\frac{4.84-4}{2.2-2}=4.2.
```

Therefore $`2c=4.2`$, giving $`c=2.1`$, an interior point. The exact MVT identity uses $`f'(c)=4.2`$ and gives $`4+4.2(0.2)=4.84`$. Replacing that slope by $`f'(a)=4`$ gives the tangent estimate 4.8. The input interval has finite width, so the two slopes differ; closeness of inputs supports an approximation, not their equality. The error identity also gives $`(4.2-4)(0.2)=0.04`$, confirming the sign and amount of the error.

[Return to P3](main.md#d013-main-p3) · [Hint P3](hints.md#d013-hints-p3)

<a name="d013-solutions-p4"></a>

Solution P4. Differentiability on the real line supplies continuity on each closed comparison interval. Since the derivative is negative everywhere, the MVT sign argument shows that $`p`$ is strictly decreasing. Consequently $`p(5)\lt p(2)=7`$, while $`p(-1)\gt p(2)=7`$. The data do not specify their exact values.

The proposed converse is false. For $`q(x)=x^3`$, $`q'(x)=3x^2`$ and $`q'(0)=0`$, so its derivative is not strictly positive everywhere. Nevertheless, take any real $`a\lt b`$. Then

```math
q(b)-q(a)=(b-a)(b^2+ab+a^2),\qquad
b^2+ab+a^2=(a+b/2)^2+3b^2/4.
```

The first factor is positive. The second is a sum of nonnegative squares and can be zero only when $`b=0`$ and $`a=0`$, which contradicts $`a\lt b`$. It is therefore positive for the chosen distinct inputs. The difference is positive, proving strict increase. The positive-derivative rule is a sufficient route to strict increase; this example shows it is not a necessary condition. An isolated zero of a derivative is different from a derivative that is zero throughout an interval.

[Return to P4](main.md#d013-main-p4) · [Hint P4](hints.md#d013-hints-p4)

<a name="d013-solutions-p5"></a>

Solution P5. Define the difference

```math
D(x)=e^x-\left(1+x+\frac{x^2}{2}+\frac{x^3}{6}\right).
```

It has $`D(0)=0`$. Differentiating gives

```math
D'(x)=e^x-\left(1+x+\frac{x^2}{2}\right)\gt 0\qquad(x\gt 0),
```

where the inequality is the preceding result supplied in the prompt. For any fixed $`x\gt 0`$, $`D`$ is continuous on $`[0,x]`$ and differentiable on $`(0,x)`$. By the MVT there is an interior $`c`$ such that $`D(x)-D(0)=D'(c)x`$. Both factors on the right are positive, so $`D(x)\gt 0`$. Rearranging proves the requested strict inequality. At zero the two sides are both 1, so equality holds there.

For the series, let the gap after a finite partial sum be $`R_n(x)`$, as defined in Section 6. Proving that it is positive for every finite $`n`$ does not prove that it tends to zero. One needs the additional limiting assertion $`R_n(x)\to0`$ for each fixed $`x`$. For comparison, a sequence of positive gaps such as $`1+1/n`$ for positive integers $`n`$ decreases while tending to 1. This is a logical counterexample to the inference “positive and decreasing implies limit zero”; it is not a formula for the exponential's actual remainder. The infinite-series equality requires its own convergence argument, as the lecture's preview acknowledges.

[Return to P5](main.md#d013-main-p5) · [Hint P5](hints.md#d013-hints-p5)

<a name="d013-solutions-p6"></a>

Solution P6. For $`a\lt b`$, continuity of $`f`$ on $`[a,b]`$ and differentiability on $`(a,b)`$ imply that some interior $`c`$ satisfies $`f'(c)=(f(b)-f(a))/(b-a)`$. It says that a local tangent slope equals the average slope across that interval, without identifying or ensuring uniqueness of the point.

To study the equation, define $`u(x)=e^x+x-2`$. A solution of the equation is exactly a zero of $`u`$. The function is continuous on $`[0,1]`$, since exponential and polynomial terms are continuous. Its endpoint values satisfy

```math
u(0)=-1\lt 0,\qquad u(1)=e-1\gt 0.
```

For the second sign one may use Section 6's $`e^1\gt 1`$. Alternatively, using only the prompt's positive-exponential premise, note that $`u'(x)=e^x+1\gt 1`$ and apply the MVT on $`[0,1]`$: $`u(1)-u(0)=u'(c)\gt 1`$, hence $`u(1)\gt 0`$. Both routes are supported. The opposite endpoint signs and continuity imply at least one zero strictly inside the interval.

For uniqueness, $`u'(x)=e^x+1\gt 0`$ everywhere, so the MVT makes $`u`$ strictly increasing on $`[0,1]`$. If two distinct inputs there both had output zero, strict increase would require the later output to be larger, a contradiction. There is at most one zero, and existence already gives at least one. Thus there is exactly one solution in $`(0,1)`$. The continuity argument establishes existence; the derivative argument establishes uniqueness. Neither requires a numerical root estimate.

[Return to P6](main.md#d013-main-p6) · [Hint P6](hints.md#d013-hints-p6)
