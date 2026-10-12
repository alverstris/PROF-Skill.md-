<a id="d016-solutions-start"></a>

Complete solutions for Definite integrals

These solutions follow the prompt IDs on the [main page](main.md#d016-main-start). The separate [hints page](hints.md#d016-hints-start) gives smaller steps before full answers. An equivalent valid construction or justified geometric route is acceptable.

<a id="d016-solutions-p1"></a>

Solution P1

The interval length is 2, so four strips have width $`1/2`$. The right samples are $`1/2,1,3/2,2`$ and the heights are $`5/2,2,3/2,1`$. Multiplying each height by the common width and adding gives

```math
R_4=\frac12\left(\frac52+2+\frac32+1\right)=\frac72.
```

The function decreases. Its right-endpoint height is the minimum on each strip, so these rectangles lie below the graph. The region is a trapezium with parallel vertical sides 3 and 1, separated by horizontal distance 2; its area is $`(3+1)2/2=4`$. Therefore $`\int_0^2(3-x)\,dx=4`$, and $`7/2\lt 4`$ confirms an underestimate. The heights alone sum to 7; omitting the width would count heights rather than rectangle contributions.

[Return to P1](main.md#d016-main-p1) · [Hint P1](hints.md#d016-hints-p1)

<a id="d016-solutions-p2"></a>

Solution P2

Here $`\Delta x=2/n`$ and the right sample is $`c_i=1+2i/n`$. The starting 1 belongs inside the square:

```math
R_n=\frac2n\sum_{i=1}^n\left(1+\frac{2i}{n}\right)^2
   =\frac2n\sum_{i=1}^n\left(1+\frac{4i}{n}+\frac{4i^2}{n^2}\right).
```

There are $`n`$ constant terms. Applying the two given finite-sum identities yields

```math
R_n=2+\frac8{n^2}\frac{n(n+1)}2
       +\frac8{n^3}\frac{n(n+1)(2n+1)}6
   =\frac{26}{3}+\frac8n+\frac{4}{3n^2}
   \longrightarrow\frac{26}{3}.
```

Both endpoint sums use the same width. Their interior boundary heights cancel on subtraction, leaving the final height 9 minus initial height 1:

```math
R_n-L_n=\frac2n(3^2-1^2)=\frac{16}{n}\longrightarrow0.
```

Consequently $`L_n=R_n-16/n`$ has the same limit. On $`[1,3]`$ the square function increases, so any chosen sample in each strip gives a height between the endpoint heights. Summing these inequalities traps any sampled sum between $`L_n`$ and $`R_n`$. The squeeze principle therefore establishes the same limit $`26/3`$ for every permitted choice. As an independent value check, the antiderivative gives $`(3^3-1^3)/3=26/3`$. This last check alone would not demonstrate sample independence.

[Return to P2](main.md#d016-main-p2) · [Hint P2](hints.md#d016-hints-p2)

<a id="d016-solutions-p3"></a>

Solution P3

For the proposed pyramid, base side is $`n+1`$ and height is $`n`$. Its remaining-height fraction at $`z`$ is $`(n-z)/n`$, so similar triangles give square side

```math
s(z)=(n+1)\left(1-\frac zn\right).
```

Choose $`z=n-1/4`$. For every positive integer $`n`$ this lies strictly within the top layer, whose side remains 1. The proposed pyramid there has side

```math
s(n-1/4)=\frac{n+1}{4n}\le\frac12\lt 1.
```

It therefore fails to contain the stack. The larger base alone did not guarantee containment: the apex is too low. Other heights sufficiently close to $`n`$ give equally valid counterexamples.

A working outer pyramid has base side $`n+1`$ and height $`n+1`$, on the same base plane and axis. Its side at height $`z`$ is $`n+1-z`$. In layer $`j`$, $`j-1\lt z\lt j`$, this side exceeds $`n-j+1`$, the stack side. Its cross-sections contain every layer, and its extra tip extends above the stack. These side comparisons establish containment; comparing total volumes alone could not exclude a local part protruding outside.

[Return to P3](main.md#d016-main-p3) · [Hint P3](hints.md#d016-hints-p3)

<a id="d016-solutions-p4"></a>

Solution P4

An antiderivative of $`2x-1`$ is $`x^2-x`$. Evaluating at the bounds gives

```math
A(b)=b^2-b,\qquad A'(b)=2b-1\quad(0\lt b\lt 2).
```

This agrees with the height at the moving upper bound. The signed integral over $`[0,2]`$ is $`A(2)=2`$.

The line crosses the axis at $`x=1/2`$. The below-axis triangle on $`[0,1/2]`$ has area $`(1/2)\cdot1/2=1/4`$. The above-axis triangle on $`[1/2,2]`$ has base $`3/2`$ and height 3, giving area $`(3/2)\cdot3/2=9/4`$. Hence signed area is $`9/4-1/4=2`$, while total geometric area is $`9/4+1/4=5/2`$. The sign convention, not an arithmetic discrepancy, accounts for the difference.

The average value is the signed integral divided by width 2, so it is 1. Finally, $`A'(b)\lt 0`$ for $`0\lt b\lt 1/2`$, so $`A`$ decreases there. Extending the interval through negative heights adds negative contributions; an increasing interval length need not give an increasing signed total.

[Return to P4](main.md#d016-main-p4) · [Hint P4](hints.md#d016-hints-p4)

<a id="d016-solutions-p5"></a>

Solution P5

A short interval sampled at $`c`$ contributes approximately $`(6000+6000c)\Delta t`$ dollars of principal. This amount is outstanding for $`1-c`$ years, so its final-debt contribution is approximately

```math
(6000+6000c)\Delta t\,[1+0.08(1-c)].
```

Summing and taking the limit gives the debt integral. Separate principal and interest to keep their meanings visible:

```math
B=\int_0^1(6000+6000t)\,dt
 =6000\left(1+\frac12\right)=9000,
```

```math
I=0.08\int_0^1(6000+6000t)(1-t)\,dt
 =480\int_0^1(1-t^2)\,dt
 =480\left(1-\frac13\right)=320,
```

```math
D=\int_0^1(6000+6000t)[1+0.08(1-t)]\,dt
 =B+I=9320.
```

Each final number is in dollars. Rate times duration produces dollars; the simple-interest factor is dimensionless because $`0.08`$ per year multiplies an age in years. Charging the entire 9000 dollars for a full year would give $`9000(1.08)=9720`$ dollars, treating every contribution as if borrowed at the start. Here later contributions have shorter ages; their correct total interest is 320 dollars, not 720 dollars. The distinction follows from the model's timing, not from compound interest, which is absent.

[Return to P5](main.md#d016-main-p5) · [Hint P5](hints.md#d016-hints-p5)

<a id="d016-solutions-p6"></a>

Solution P6

Both plans have the same one-year principal:

```math
B_U=\int_0^1 9000\,dt=9000,
\qquad
B_V=\int_0^{1/2}6000\,dt+\int_{1/2}^{1}12000\,dt
   =3000+6000=9000.
```

The continuous-borrowing contribution at time $`t`$ has age $`1-t`$ years when repaid. Plan U therefore gives

```math
D_U=\int_0^1 9000[1+0.06(1-t)]\,dt
   =9000+540\int_0^1(1-t)\,dt
   =9000+270=9270.
```

Plan V has one finite jump, so split at its change time:

```math
D_V=\int_0^{1/2}6000[1+0.06(1-t)]\,dt
    +\int_{1/2}^{1}12000[1+0.06(1-t)]\,dt.
```

Since $`\int(1-t)\,dt=t-t^2/2`$, the two age integrals are $`3/8`$ and $`1/8`$. Thus

```math
D_V=9000+0.06\left(6000\frac38+12000\frac18\right)
   =9000+225=9225.
```

Principal, interest and debt are dollar amounts. Plan V costs 45 dollars less interest. Compared with U, it shifts borrowing from the first half-year to the second while retaining the same principal, so less of that principal remains outstanding for a long time. Equal totals borrowed do not imply equal interest when timing differs.

Finally, let $`K`$ be the change in rate at exactly $`t=1/2`$, with $`K`$ fixed and finite. In a finite sum only rectangles sampling that exact point can change. At most two adjacent strips can include it as a permitted sample, so the principal sums differ in magnitude by at most $`2|K|\Delta t`$. For debt, the weight $`1+0.06(1-t)`$ lies between 1 and 1.06 on the interval, so the corresponding bound is $`2.12|K|\Delta t`$. Both bounds tend to zero. The finite sums may differ, but their limiting integrals and the final principal/debt do not. The bounded finite-piece existence condition still holds after changing one finite value.

[Return to P6](main.md#d016-main-p6) · [Hint P6](hints.md#d016-hints-p6)

[Return to the reading route](main.md#d016-main-start)
