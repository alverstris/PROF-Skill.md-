D016 · Complete solutions

Try the [tasks in the lesson](lesson.md) before reading their solutions. The [hints](hints.md) give intermediate help separately. These solutions explain the construction and interpretation as well as the arithmetic.

<a id="s1"></a>

Solution P1

Four equal pieces of $`[0,2]`$ each have width $`\Delta x=(2-0)/4=1/2`$. The left endpoints are $`0,1/2,1,3/2`$, with heights $`0,1/4,1,9/4`$. Thus

```math
L_4=\frac12\left(0+\frac14+1+\frac94\right)=\frac74.
```

On each subinterval, $`x^2`$ increases, so the left-endpoint height is no greater than any height of the curve over that piece. Every rectangle lies within the region under the curve. The result is an underestimate; no antiderivative is needed to establish its direction. A sum of heights alone would omit the width and would not be the requested area.

[Return to P1](lesson.md#p1)

<a id="s2"></a>

Solution P2

The right coordinate is $`ib/n`$ for $`i=1,\ldots,n`$. For the left sum the corresponding coordinates run from zero to $`(n-1)b/n`$. Hence

```math
R_n=\frac{b^3}{n^3}(1^2+2^2+\cdots+n^2),
\qquad
L_n=\frac{b^3}{n^3}(0^2+1^2+\cdots+(n-1)^2).
```

Subtracting these finite sums cancels every shared square. Therefore

```math
R_n-L_n=\frac{b^3}{n^3}(n^2-0^2)=\frac{b^3}{n}.
```

For fixed positive $`b`$, this tends to zero. Since the pyramid argument supplies $`R_n\to b^3/3`$, the identity $`L_n=R_n-b^3/n`$ gives $`L_n\to b^3/3`$ too.

For any permitted $`c_i\in[(i-1)b/n,ib/n]`$, monotonicity on the nonnegative interval gives

```math
\left(\frac{(i-1)b}{n}\right)^2
\le c_i^2\le
\left(\frac{ib}{n}\right)^2.
```

Multiply by the positive width $`b/n`$ and add over all subintervals:

```math
L_n\le S_n\le R_n.
```

Both bounds approach $`b^3/3`$, so $`S_n`$ must approach it as well. This supports every choice of one sample in each equal subinterval, including choices that change as $`n`$ changes. It does not say the finite totals are equal.

[Return to P2](lesson.md#p2)

<a id="s3"></a>

Solution P3

The displayed height is $`f(c_i)=2-c_i`$ with $`c_i=1+3i/n`$. Comparing with right endpoints $`a+i\Delta x`$ identifies $`a=1`$ and $`\Delta x=3/n`$. The last endpoint is $`1+3n/n=4`$, so the interval is $`[1,4]`$.

The function $`2-x`$ is continuous there: changing the input by $`h`$ changes the output by $`-h`$, which tends to zero. Thus the sum tends to its definite integral:

```math
\lim_{n\to\infty}S_n
=\int_1^4(2-x)\,dx
=\left[2x-\frac{x^2}{2}\right]_1^4
=0-\frac32=-\frac32.
```

An independent sum check is

```math
S_n=\frac3n\sum_{i=1}^{n}\left(1-\frac{3i}{n}\right)
=3-\frac9{n^2}\frac{n(n+1)}2
=-\frac32-\frac9{2n},
```

which has the same limit.

The zero at $`x=2`$ splits the geometric region. Above the axis, on $`[1,2]`$, the triangle has base 1 and height 1, hence area $`1/2`$. Below the axis, on $`[2,4]`$, the triangle has base 2 and height 2, hence area 2. Consequently

```math
\text{geometric area}=\frac12+2=\frac52,
\qquad
\text{signed integral}=\frac12-2=-\frac32.
```

The interval length is 3, so the average value is $`(-3/2)/3=-1/2`$. The integral gives net signed accumulation, the geometric area counts both regions positively, and the average divides the signed total by the interval length. The negative average says that a constant height of $`-1/2`$ over this interval would have the same signed total.

[Return to P3](lesson.md#p3)

<a id="s4"></a>

Solution P4

A short interval contributes approximately $`12000t\,\Delta t`$ dollars of principal. Adding and taking the limit gives

```math
B=\int_0^1 12000t\,dt
=12000\left[\frac{t^2}{2}\right]_0^1
=6000\text{ dollars}.
```

The portion borrowed at time $`t`$ remains outstanding for $`1-t`$ years. Simple interest makes its final multiplier $`1+0.06(1-t)`$. Thus

```math
D(1)=\int_0^1 12000t[1+0.06(1-t)]\,dt.
```

Here $`12000t`$ is the rate of borrowing, $`dt`$ supplies the limiting time width, and the bracket converts each principal contribution to what that contribution will cost at the common final time. Numerically,

```math
\begin{aligned}
D(1)&=12000\int_0^1(1.06t-0.06t^2)\,dt\\
&=12000\left[\frac{1.06t^2}{2}-\frac{0.06t^3}{3}\right]_0^1\\
&=12000(0.53-0.02)=6120\text{ dollars}.
\end{aligned}
```

Interest is therefore 120 dollars. Charging a full year on all 6000 dollars would give $`6000(1.06)=6360`$ dollars, 240 dollars too much. That expression assigns the start-of-year holding time to money that was actually borrowed throughout the year.

At a uniform borrowing rate of 6000 dollars per year, the principal is still 6000 dollars but the final debt is

```math
\int_0^1 6000[1+0.06(1-t)]\,dt
=6000(1+0.03)=6180\text{ dollars}.
```

This is 60 dollars more than for the increasing rate. Uniform borrowing puts half the total in each half-year; the increasing rate puts only $`\int_0^{1/2}12000t\,dt=1500`$ dollars in the first half and 4500 in the second. More of the same principal is therefore borrowed later and held for less time, which agrees with the smaller weighted interest integral. The calculation concerns the stated simple-interest model; no compounding has been introduced.

[Return to P4](lesson.md#p4)

<a id="s5"></a>

Solution P5

For a sample $`c_i`$ in an interval of duration $`\Delta t`$ minutes, the contribution to volume is approximately $`g(c_i)\Delta t=(3-c_i)\Delta t`$ litres. The sign tells whether that contribution enters or leaves. The limiting signed total gives the net change:

```math
\Delta V=\int_0^4(3-t)\,dt
=\left[3t-\frac{t^2}{2}\right]_0^4
=12-8=4\text{ litres}.
```

The tank already held 10 litres, so its final volume is $`10+4=14`$ litres. The integral is a change; it does not by itself include the initial amount.

The rate vanishes at $`t=3`$. Before that it is positive; after that it is negative. The amount entering in the first part is

```math
\int_0^3(3-t)\,dt=\frac92\text{ litres}.
```

The signed integral from 3 to 4 is $`-1/2`$ litre, so the amount leaving is $`1/2`$ litre. Because the specified signed flow is the only flow, total fluid crossing either way is

```math
\int_0^4|3-t|\,dt=\frac92+\frac12=5\text{ litres}.
```

The mean net flow is the signed total divided by the duration:

```math
\frac{1}{4}\int_0^4(3-t)\,dt
=1\text{ litre per minute}.
```

Thus the four questions require, respectively, a signed accumulation, that accumulation plus the initial volume, an accumulation of magnitudes, and a signed accumulation divided by elapsed time. Taking the absolute value of the final signed integral would give 4 litres and would still miss the extra half-litre that first entered and later left. The rate is continuous at its zero; a sign change is not itself a discontinuity.

[Return to P5](lesson.md#p5)
