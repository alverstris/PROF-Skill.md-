Solutions for Lecture 18

These solutions show the reasoning and interpretation expected, not just final values. If you want a smaller next step first, use [Hints](hints.md). Different valid methods are accepted when they justify the requested conclusions. Any error routes discussed below are anticipated possibilities, not observations of your work.

<a name="q1"></a>

Q1 solution

The width is $`2/4=1/2`$. Right samples are $`1/2,1,3/2,2`$, so the corresponding heights are $`1/4,1,9/4,4`$. The right sum is

$$
R_4=\frac12\left(\frac14+1+\frac94+4\right)=\frac{15}{4}.
$$

Left samples are $`0,1/2,1,3/2`$, with heights $`0,1/4,1,9/4`$, giving

$$
L_4=\frac12\left(0+\frac14+1+\frac94\right)=\frac74.
$$

The function increases on this interval: the right height is at least every height to its left in the same interval, while the left height is at most every height to its right. Thus the true area lies between $`7/4`$ and $`15/4`$. Neither sum is exact here; each misses or adds a region of positive area. Their difference is 2, agreeing with $`b^3/n=8/4`$.

If you added sample coordinates rather than their squares, the first issue is the chosen heights. If the heights are right but the width is missing, the issue is converting heights into area, not endpoint choice. A numerical slip after forming the correct products is a different, local arithmetic issue.

[Return to Q1](notes.md#q1) · [Q1 hint](hints.md#q1)

<a name="q2"></a>

Q2 solution

Write $`j=0,\ldots,n-1`$ for the layer number from the bottom. Layer $`j`$ occupies heights $`2j\le z\le2j+2`$ and has square side $`n-j`$. Similarity gives inner side $`n-z/2`$ and outer side $`n+1-z/2`$. Since $`j\le z/2\le j+1`$,

$$
n-\frac z2\le n-j\le n+1-\frac z2.
$$

As in the original construction, all squares share their centre and have corresponding sides parallel, so comparing side lengths establishes containment at each height. The outer pyramid continues above the staircase to its own apex. The inequalities yield strict volume bounds because the solids differ through regions of positive volume.

Each slab now has volume $`2k^2`$, so

$$
W_n=2(1^2+\cdots+n^2).
$$

The inner volume is $`n^2(2n)/3=2n^3/3`$ and the outer volume is $`(n+1)^2[2(n+1)]/3=2(n+1)^3/3`$. Divide by positive $`n^3`$:

$$
\frac23\lt \frac{W_n}{n^3}\lt \frac23\left(1+\frac1n\right)^3.
$$

Both bounds tend to $`2/3`$, hence $`W_n/n^3\to2/3`$. But the requested sum of squares is $`W_n/2`$, so

$$
\frac{1^2+\cdots+n^2}{n^3}=\frac{W_n}{2n^3}\longrightarrow\frac13.
$$

Doubling thickness doubles the auxiliary volume, not the numerical sum of squares. Using triangle area in place of square-pyramid volume would lose the three-dimensional construction. An equivalent argument stretching the entire original construction vertically by a factor of 2 is valid if it states that every contained solid's volume doubles and then divides out that factor.

[Return to Q2](notes.md#q2) · [Q2 hint](hints.md#q2)

<a name="q3"></a>

Q3 solution

The width is $`\Delta x=(3-1)/n=2/n`$. The $`i`$th interval is $`[1+2(i-1)/n,1+2i/n]`$, so its right sample is $`c_i=1+2i/n`$. Its height is

$$
f(c_i)=4-\left(1+\frac{2i}{n}\right)=3-\frac{2i}{n}.
$$

Therefore the required sum is

$$
R_n=\sum_{i=1}^n\left(3-\frac{2i}{n}\right)\frac2n.
$$

For $`n=2`$, the intervals are $`[1,2]`$ and $`[2,3]`$, giving

$$
R_2=(4-2)\times1+(4-3)\times1=3.
$$

Because $`4-x`$ decreases, the right rectangle in each interval lies below the graph. This is an underestimate, reversing the right-endpoint conclusion for the increasing $`x^2`$ example.

An antiderivative is $`4x-x^2/2`$, giving

```math
\int_1^3(4-x)\,dx
=\left(12-\frac92\right)-\left(4-\frac12\right)=4.
```

Alternatively, the endpoint heights are 3 and 1, with separation 2, so the trapezium area is $`(3+1)2/2=4`$. The exact integral exceeds the two-rectangle sum by 1. An additional check is $`R_n=6-4[n(n+1)/2]/n^2=4-2/n`$, approaching 4 from below. This last check is optional reasoning in the solution, not an additional task.

A sample $`2i/n`$ would start the construction at the wrong boundary. Repair that coordinate before doing the height substitution or summation.

[Return to Q3](notes.md#q3) · [Q3 hint](hints.md#q3)

<a name="q4"></a>

Q4 solution

An antiderivative of $`2x+1`$ is $`x^2+x`$. Evaluating at both ends gives

$$
A(b)=(b^2+b)-(1^2+1)=b^2+b-2,
\qquad A(1)=0.
$$

For $`b\gt 1`$, differentiation gives $`A'(b)=2b+1`$. For the strip explanation, the interval $`[1,b]`$ is present in both $`A(b+h)`$ and $`A(b)`$ and cancels. Only the region near the moving edge remains. As its width $`h`$ shrinks to zero, its height approaches $`2b+1`$, so area change divided by width approaches $`2b+1`$.

Here the algebra makes that geometric statement exact before the limit:

$$
\frac{A(b+h)-A(b)}h
=\frac{2bh+h^2+h}{h}=2b+1+h\longrightarrow2b+1.
$$

The fixed lower edge at 1 contributes a constant subtraction of 2; its derivative is zero. Giving $`A'(b)=3`$ would use the fixed lower height instead of the height of the strip that changes. At $`b=1`$ the stated domain permits a right-hand derivative, but the requested two-sided interior derivative concerns $`b\gt 1`$.

[Return to Q4](notes.md#q4) · [Q4 hint](hints.md#q4)

<a name="q5"></a>

Q5 solution

At numerical year-time $`t`$, a short interval of width $`\Delta t`$ years contributes approximately $`24000t\Delta t`$ dollars of principal. Each such loan earns interest for $`1-t`$ years, giving multiplier $`1+0.06(1-t)`$. Below, square brackets with endpoint labels mean evaluate the enclosed antiderivative at the upper endpoint and subtract its value at the lower endpoint. Thus

```math
B=\int_0^1 24000t\,dt
=24000\left[\frac{t^2}{2}\right]_0^1
=12000\text{ dollars}.
```

The debt is principal plus interest:

```math
D=\int_0^1 24000t\bigl(1+0.06(1-t)\bigr)\,dt
=B+1440\int_0^1(t-t^2)\,dt.
```

Expanding the interest contribution gives a polynomial already covered by the power rule:

```math
\int_0^1(t-t^2)\,dt=\frac12-\frac13=\frac16.
```

Consequently $`D=12000+1440/6=12240`$ dollars. The constant rate also borrows 12000 dollars, but gives a debt of 12360 dollars, so the increasing-rate plan owes 120 dollars less.

The increasing rate shifts borrowing later: below half a year its rate is below 12000, and after half a year it is above 12000. The amounts removed early and added late balance in principal, while the later loans have shorter interest-bearing durations. Equal principal therefore need not imply equal debt. Dividing interest by principal times annual rate gives an amount-weighted mean duration of $`240/(12000\times0.06)=1/3`$ year, compared with half a year for constant borrowing.

The borrowing rate has dollars/year units; multiplying by $`dt`$ in years gives dollars. The growth multiplier is dimensionless because annual rate times duration has no remaining unit. Both $`B`$ and $`D`$ are dollar totals. Charging every loan for a full year would give the wrong model even if its integral arithmetic were correct; using $`t`$ instead of $`1-t`$ would give early loans less time to grow and reverse the intended timing.

[Return to Q5](notes.md#q5) · [Q5 hint](hints.md#q5)

<a name="q6"></a>

Q6 solution

The velocity is zero at $`t=2`$, positive before that and negative afterward. Its integral therefore gives net displacement, allowing motion in opposite directions to cancel:

```math
\text{displacement}=\int_0^3(2-t)\,dt
=\left[2t-\frac{t^2}{2}\right]_0^3
=6-\frac92=\frac32\text{ m}.
```

Here the brackets mean the upper-endpoint value minus the lower-endpoint value. The speed is $`|2-t|`$: it equals $`2-t`$ on $`[0,2]`$ and $`t-2`$ on $`[2,3]`$. Hence

```math
\text{distance}=\int_0^2(2-t)\,dt+\int_2^3(t-2)\,dt
=2+\frac12=\frac52\text{ m}.
```

The same values follow from two triangles on the velocity-time graph: the positive one has base 2 and height 2, and the negative one has base 1 and height 1. Add their areas for distance and subtract the second from the first for displacement. Distance is at least the magnitude of displacement, as these values satisfy.

Dividing each total by the three seconds gives average velocity $`(3/2)/3=1/2`$ m/s and average speed $`(5/2)/3=5/6`$ m/s. The negative contribution after two seconds decreases displacement but increases total distance; that is why a single signed-velocity integral cannot supply both totals.

The right-endpoint intervals have width $`\Delta t=3/n`$ seconds, samples $`t_i=3i/n`$, and sampled velocities $`2-3i/n`$. The requested sum is

$$
\sum_{i=1}^n\left(2-\frac{3i}{n}\right)\frac3n.
$$

Its limit is the displacement integral because the continuous velocity is sampled over the whole three-second interval with widths tending to zero. Negative late summands belong in this sum. Taking their magnitudes instead would construct the distance integral. Building this sum checks recall of the representation; deciding where to split and what signs to use checks transfer to the new rate.

[Return to Q6](notes.md#q6) · [Q6 hint](hints.md#q6)
