Complete solutions for D016

[Return to teaching and prompts](teaching.md) · [Grouped hints](hints.md)

P1

The width is $`\Delta x=2/4=1/2`$. The right endpoints are $`1/2,1,3/2,2`$:

```math
R_4=\frac12\left[\left(\frac12\right)^2+1^2+
\left(\frac32\right)^2+2^2\right]
=\frac12\left(\frac14+1+\frac94+4\right)
=\frac{15}{4}.
```

The left endpoints are $`0,1/2,1,3/2`$:

```math
L_4=\frac12\left[0^2+\left(\frac12\right)^2+1^2+
\left(\frac32\right)^2\right]
=\frac74.
```

Thus the area is in $`[7/4,15/4]`$. On each piece, increasing $`x^2`$ is at least its left value and at most its right value. Multiplying these height inequalities by the positive width and adding proves the bounds. The finite sums are bounds, not exact integrals.

P2

The volume of each slab is twice its square area, so $`V_n=2S_n`$. More geometrically, the vertical stretch doubles both comparison heights without changing either square base. The inner pyramid has base side $`n`$ and height $`2n`$; the outer has base side $`n+1`$ and height $`2(n+1)`$. Containment survives because the same vertical stretch is applied to all three solids.

```math
\frac13n^2(2n)\le V_n\le\frac13(n+1)^2\,2(n+1).
```

Divide by $`n^3\gt0`$:

```math
\frac23\le\frac{V_n}{n^3}
\le\frac23\left(1+\frac1n\right)^3.
```

Both bounds tend to $`2/3`$, so $`V_n/n^3\to2/3`$. Keeping the original pyramid heights while doubling the slabs would no longer give the same containment construction. The result is a limit; it need not be attained at any finite $`n`$.

P3

The width is $`(3-1)/n=2/n`$ and the right endpoints are $`1+2i/n`$. Constructing height times width gives

```math
R_n=\frac2n\sum_{i=1}^n
\left[2\left(1+\frac{2i}{n}\right)-3\right]
=\frac2n\left[-n+\frac4n\frac{n(n+1)}2\right]
=2+\frac4n.
```

The polynomial is continuous, so these sums have the definite integral as their limit. Consequently $`\int_1^3(2x-3)\,dx=2`$. As an independent algebraic check, $`[x^2-3x]_1^3=0-(-2)=2`$.

The crossing is $`x=3/2`$. From 1 to $`3/2`$, the triangle lies below the axis and has base $`1/2`$, height 1 and geometric area $`1/4`$. From $`3/2`$ to 3, the positive triangle has base $`3/2`$, height 3 and area $`9/4`$. The integral is $`-1/4+9/4=2`$; the geometric area is $`1/4+9/4=5/2`$. Adding magnitudes and adding signed contributions answer different questions.

P4

The fundamental theorem gives

```math
A(b)=[x^2+x]_1^b=b^2+b-2.
```

Then $`A(1)=1+1-2=0`$, as required by accumulating over zero interval length. Differentiating with respect to the variable upper endpoint gives $`A'(b)=2b+1`$, the original integrand evaluated there. The $`x`$ is a dummy integration variable; $`b`$ is the argument of the resulting function.

On $`[1,3]`$, the total is $`A(3)=9+3-2=10`$ and the width is 2. The average is therefore $`10/2=5`$. A constant height 5 over that width gives area 10, matching the area under $`2x+1`$. Dividing by 3 would confuse the endpoint with the interval length.

P5

The zero rate after half a year contributes nothing. The total borrowed is

```math
B(1)=\int_0^{1/2}24000\,dt=12000.
```

For the interest, each contribution is held until time 1:

```math
I=0.06\int_0^{1/2}24000(1-t)\,dt
=1440\left[t-\frac{t^2}{2}\right]_0^{1/2}
=1440\left(\frac12-\frac18\right)=540.
```

The final debt is $`12000+540=12540`$ dollars. Uniform borrowing over the whole year gives the worked case's 12,360 dollars, so front-loading raises the debt by 180 dollars despite identical 12,000-dollar principal totals.

During the first-half schedule, equal amounts are borrowed throughout $`[0,1/2]`$ and their average time outstanding is $`3/4`$ year. The interest check is $`12000(0.06)(3/4)=540`$. Uniform borrowing through the whole year has only $`1/2`$ year average time outstanding. The relevant difference is when the dollars are borrowed, not how much principal is borrowed.

P6

The principal contribution in a short interval is rate times duration. Summing without an interest multiplier gives

```math
B(2)=\int_0^2 6000(1+t)\,dt
=6000\left[t+\frac{t^2}{2}\right]_0^2
=24000.
```

This is 24,000 dollars. Divide by two years to obtain the average borrowing rate, 12,000 dollars per year.

A contribution borrowed at time $`t`$ has $`2-t`$ years left, so its simple-interest multiplier is $`1+0.10(2-t)`$. Hence

```math
D(2)=\int_0^2 6000(1+t)[1+0.10(2-t)]\,dt.
```

Separate principal from interest and expand the latter:

```math
I=600\int_0^2(1+t)(2-t)\,dt
=600\int_0^2(2+t-t^2)\,dt
=600\left[2t+\frac{t^2}{2}-\frac{t^3}{3}\right]_0^2
=600\left(4+2-\frac83\right)=2000.
```

Therefore $`D(2)=24000+2000=26000`$ dollars. Both principal and debt have units dollars; the average divides a dollar total by years. In the debt integrand the interest multiplier is dimensionless.

Multiplying the principal by $`1.20`$ gives 28,800 dollars and is too large. That multiplier assigns a full two years of interest to every dollar, whereas all amounts borrowed after time zero have less time outstanding. Here the borrowing rate rises, so more principal arrives later. The actual interest fraction is $`2000/24000=1/12`$, below 0.20, consistent with that timing.

[Return to teaching](teaching.md) · [Grouped hints](hints.md)
