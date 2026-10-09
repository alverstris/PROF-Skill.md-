Solutions for definite integrals

Read these after attempting the matching task or using its [hint](hints.md). These are reasoned model responses; equivalent justified methods are acceptable where the prompt leaves the method open.

<a name="s1"></a>
Solution P1

The width is $`1/2`$. The right inputs are $`1/2,1,3/2,2`$, giving heights $`1/4,1,9/4,4`$. The left inputs are $`0,1/2,1,3/2`$, giving heights $`0,1/4,1,9/4`$. Thus

```math
R_4=\frac12\left(\frac14+1+\frac94+4\right)=\frac{15}{4},
\qquad
L_4=\frac12\left(0+\frac14+1+\frac94\right)=\frac74.
```

Because $`x^2`$ increases on this interval, a left height is no larger than any height in its strip, while a right height is no smaller. Multiplying by a positive width and adding preserves the inequalities. Therefore the area lies in $`[7/4,15/4]`$, an interval of width 2. This also follows from $`R_4-L_4=(1/2)(4-0)=2`$. The exact area $`8/3`$ from C2 lies inside, but that check does not replace the bound argument. Forgetting the width would sum heights rather than rectangle areas; this is an anticipated mistake, not an observed learner error.

[Return to P1](teaching.md#p1).

<a name="s2"></a>
Solution P2

Here $`\Delta x=2/n`$, right inputs are $`2i/n`$, and left inputs are $`2(i-1)/n`$. Consequently

```math
R_n=\frac2n\sum_{i=1}^n\left(2-\frac{2i}{n}\right)
=\frac2n\left(2n-\frac2n\frac{n(n+1)}2\right)
=2-\frac2n.
```

The left sum uses the integers $`0,1,\ldots,n-1`$, whose sum is $`n(n-1)/2`$, obtained by subtracting $`n`$ from $`n(n+1)/2`$. Hence

```math
L_n=\frac2n\sum_{i=1}^n\left(2-\frac{2(i-1)}n\right)
=\frac2n\left(2n-(n-1)\right)=2+\frac2n.
```

For arbitrary $`c_i\in[2(i-1)/n,2i/n]`$, construct

```math
S_n=\frac2n\sum_{i=1}^n(2-c_i).
```

The function decreases, so each right height is no greater than $`2-c_i`$, and each left height is no smaller. The positive common width permits summing these comparisons:

```math
2-\frac2n=R_n\le S_n\le L_n=2+\frac2n.
```

Both ends tend to 2; the enclosing gap is $`4/n`$ and tends to zero. This applies to every permissible tag selection, even if it changes with $`n`$, so the integral is 2 independently of tags. An antiderivative or the triangle of base 2 and height 2 confirms the value. A right-endpoint sum is a lower bound here, unlike P1; the monotonicity condition determines that reversal.

[Return to P2](teaching.md#p2).

<a name="s3"></a>
Solution P3

Over a short interval near time $`t`$, the amount borrowed is approximately $`6000t\Delta t`$ dollars. It remains outstanding for $`1-t`$ years, so the year-end contribution is approximately $`6000t[1+0.06(1-t)]\Delta t`$ dollars. The continuous rates allow the Riemann limits, using numerical times in years:

```math
B=\int_0^1 6000t\,dt
=3000[t^2]_0^1=3000\text{ dollars},
```

```math
D=\int_0^1 6000t(1.06-0.06t)\,dt
=6000\left[\frac{1.06t^2}{2}-\frac{0.06t^3}{3}\right]_0^1
=6000(0.53-0.02)=3060\text{ dollars}.
```

The interest is 60 dollars. It also follows directly from $`0.06\int_0^1 6000t(1-t)\,dt=60`$, which isolates the interest contribution. The rate has units dollars per year, its weight is dimensionless, and integration over years leaves dollars, not dollars per year.

Uniform borrowing of the same 3000 dollars over one year uses rate 3000 dollars per year. Its debt is

```math
D_{\rm uniform}=3000\int_0^1[1+0.06(1-t)]\,dt
=3000(1.03)=3090\text{ dollars}.
```

The increasing borrowing rate puts more of the principal later in the year, leaving less time to earn interest. Quantitatively the interest-weighted duration integral is $`\int_0^1 6000t(1-t)\,dt=1000`$ dollar-years; dividing by the principal gives average duration $`1/3`$ year, compared with $`1/2`$ year for uniform borrowing. This agrees with the 30-dollar smaller debt. That division is a weighted mean: each duration is weighted by its borrowed contribution.

[Return to P3](teaching.md#p3).

<a name="s4"></a>
Solution P4

(a) Assume $`a<b`$ and $`f`$ continuous on $`[a,b]`$. For a positive integer $`n`$, set $`\Delta x=(b-a)/n`$ and boundaries $`x_i=a+i\Delta x`$, for $`i=0,\ldots,n`$. Choose one tag $`c_i\in[x_{i-1},x_i]`$ in each strip. Then

```math
\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^n f(c_i)\Delta x.
```

Each term is sampled value times strip width; the sum is finite before taking the limit. Continuity supplies existence and independence of all permissible tags. The limits $`a,b`$ locate the interval and $`dx`$ names the integration variable. A correct recalled formula without the per-strip restriction or the tag-independence condition is incomplete for this question.

(b) The graph crosses the axis at $`x=3/2`$. It has positive height to the left and negative height to the right. An antiderivative is $`F(x)=3x-x^2`$, since $`F'(x)=3-2x`$. The signed integral is

```math
\int_0^2(3-2x)\,dx=[3x-x^2]_0^2=2.
```

For the geometric area, retain both pieces with positive signs:

```math
\int_0^{3/2}(3-2x)\,dx=\frac94,
\qquad
\int_{3/2}^{2}(3-2x)\,dx=-\frac14.
```

Thus the area is $`9/4+1/4=5/2`$. Alternatively the two triangles have bases $`3/2`$ and $`1/2`$ and heights 3 and 1, giving those same positive areas directly. The signed integral subtracts the second triangle; the geometric area adds it. These methods are both efficient because the graph is linear and its crossing is easy to locate.

(c) The fundamental theorem gives $`A'(b)=3-2b`$; equivalently $`A(b)=3b-b^2`$ and direct differentiation agrees. At $`b=2`$, $`A'(2)=-1`$, so the signed accumulation decreases locally when its endpoint moves right. This does not make the geometric area negative. The curve is below the axis near 2, so an added strip decreases signed accumulation while increasing the nonnegative area between graph and axis.

[Return to P4](teaching.md#p4).
