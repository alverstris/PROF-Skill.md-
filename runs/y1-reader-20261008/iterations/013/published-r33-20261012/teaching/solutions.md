<a id="d013-solutions-start"></a>

Solutions — Mean value theorem and inequalities

These solutions explain the requested reasoning. If you want to continue an attempt with less help, use the [separate hints](hints.md#d013-hints-start). [Return to the lesson](main.md#d013-main-start).

<a id="d013-solution-p1"></a>

Solution P1

The function $`f(x)=x^3`$ is a polynomial, continuous on $`[0,1]`$ and differentiable on $`(0,1)`$, with $`f'(x)=3x^2`$. Thus the hypotheses hold. Its secant slope is

```math
\frac{f(1)-f(0)}{1-0}=\frac{1-0}{1}=1.
```

The matching derivative condition is $`3c^2=1`$, giving candidates $`c=1/\sqrt3`$ and $`c=-1/\sqrt3`$. Since $`\sqrt3\gt 1`$, the positive candidate lies strictly between zero and one. The negative candidate lies outside that interval and must be discarded. Therefore the only matching point here is

```math
c=\frac1{\sqrt3}.
```

At that input the tangent has the same slope as the endpoint secant. The equation and interval check show uniqueness for this particular function and interval. The theorem itself guarantees only existence. For example, $`f(x)=x`$ on $`[0,1]`$ has secant slope 1 and derivative 1 at every interior input, so there are infinitely many matching points.

[Return to P1](main.md#d013-main-p1) · [Hint P1](hints.md#d013-hint-p1)

<a id="d013-solution-p2"></a>

Solution P2

(a) The endpoint values are $`g(0)=1`$ and $`g(3)=2`$, so the secant slope is

```math
\frac{2-1}{3-0}=\frac13.
```

For $`x\lt 1`$, the modulus gives $`g(x)=1-x`$ and derivative −1. For $`x\gt 1`$, it gives $`g(x)=x-1`$ and derivative +1. At 1 the two one-sided slopes disagree, so the derivative does not exist. The function is continuous throughout the interval, but no interior derivative is $`1/3`$. This is an actual failure of the theorem's conclusion when differentiability at the corner is missing, not a contradiction of the theorem.

(b) On the negative half-line the function is identically zero, and on the positive half-line it is identically one. A small change of input that stays within either half-line changes no output, giving derivative zero there. Nevertheless $`r(-1)=0`$ differs from $`r(1)=1`$, so it is not constant on its whole domain.

The domain omits zero and is therefore not an interval. In particular, $`r`$ is not defined on all of $`[-1,1]`$, so it cannot satisfy the theorem's continuity and differentiability hypotheses on that connecting interval. The constant-function conclusion holds separately on each half-line, with possibly different constants. “Derivative zero everywhere in its domain” needs the interval condition before it can assert one common value across that domain.

[Return to P2](main.md#d013-main-p2) · [Hint P2](hints.md#d013-hint-p2)

<a id="d013-solution-p3"></a>

Solution P3

The square root is continuous on $`[4,4.04]`$ and differentiable in its interior, since all these inputs are positive. The power rule gives $`f'(t)=1/(2\sqrt{t})`$. At the starting point the output is 2 and the derivative is $`1/4`$. Thus

```math
L(4.04)=f(4)+f'(4)(4.04-4)
=2+\frac14(0.04)=2.01.
```

The exact mean-value identity is

```math
\sqrt{4.04}=2+\frac{0.04}{2\sqrt{c}},\qquad 4\lt c\lt 4.04.
```

As positive inputs increase, their square roots increase and their positive reciprocals decrease. Therefore

```math
\frac1{2\sqrt{4.04}}\lt \frac1{2\sqrt c}\lt \frac1{2\sqrt4}=\frac14.
```

Multiplication by 0.04 preserves the inequality direction because it is positive. Adding 2 to all three terms, and using the exact identity in the middle, gives

```math
2+\frac{0.04}{2\sqrt{4.04}}\lt \sqrt{4.04}\lt 2.01.
```

The tangent approximation overestimates: its slope at 4 is strictly larger than the intermediate slope at $`c`$. Equivalently, the signed error $`f(4.04)-L(4.04)`$ is negative. No numerical evaluation of the radical or explicit solution for $`c`$ was needed. Using $`c=4`$ would wrongly turn the approximation into an equality and would violate the open-interval requirement.

[Return to P3](main.md#d013-main-p3) · [Hint P3](hints.md#d013-hint-p3)

<a id="d013-solution-p4"></a>

Solution P4

The logarithm is real when $`1+x\gt 0`$, so the domain is $`x\gt -1`$. Choose the difference between the proposed upper and lower expressions:

```math
d(x)=x-\ln(1+x),\qquad d(0)=0.
```

By the chain rule,

```math
d'(x)=1-\frac1{1+x}=\frac{x}{1+x}.
```

On the whole domain the denominator is positive. If $`x\gt 0`$, the derivative is positive at every input between 0 and $`x`$. The difference is continuous on the corresponding closed interval and differentiable inside, so the mean value theorem gives $`d(x)\gt d(0)=0`$.

If instead $`-1\lt x\lt 0`$, the derivative is negative at every input between $`x`$ and 0. Thus $`d`$ decreases as the input moves right from $`x`$ to 0, and $`d(x)\gt d(0)=0`$. Written directly with an intermediate point,

```math
d(0)-d(x)=d'(c)(0-x)\lt 0,\qquad x\lt c\lt 0,
```

because the derivative factor is negative and the interval length is positive. This is the ordering connection: negative derivative describes direction of change, not the sign of the output.

In both ranges the positive difference means $`x-\ln(1+x)\gt 0`$, so

```math
\ln(1+x)\lt x\quad\text{for }x\gt -1,\ x\ne0.
```

At zero there is equality. At or below −1 this real logarithmic expression is not defined, so the asserted real inequality has no such cases. An argument that differentiated a comparison without checking its value at zero would omit the step fixing the vertical difference.

[Return to P4](main.md#d013-main-p4) · [Hint P4](hints.md#d013-hint-p4)

<a id="d013-solution-p5"></a>

Solution P5

The mean value theorem says: if $`a\lt b`$ and $`f`$ is continuous on $`[a,b]`$ and differentiable on $`(a,b)`$, then some $`c`$ in that open interval satisfies

```math
f(b)-f(a)=f'(c)(b-a).
```

Knowing the exact point is unnecessary if a useful derivative sign or bound holds at every possible point in the interval. For example, a positive derivative everywhere inside and a positive interval length imply a positive output difference.

For the induction define $`R_n(x)=e^x-P_n(x)`$. The claim is that for each nonnegative integer $`n`$, this difference is positive for every $`x\gt 0`$.

At $`n=0`$, $`P_0(x)=1`$, so $`R_0(0)=0`$ and $`R_0'(x)=e^x\gt 0`$. For any fixed $`x\gt 0`$, apply the theorem on $`[0,x]`$ to obtain $`R_0(x)\gt R_0(0)=0`$. This establishes the base case without assuming a finite exponential lower bound in advance.

For the induction step, let $`n\ge1`$ and assume $`R_{n-1}(t)\gt 0`$ for every positive $`t`$. Differentiate the finite sum, with the constant term disappearing:

```math
P_n'(x)=\sum_{k=1}^{n}\frac{kx^{k-1}}{k!}
=\sum_{k=1}^{n}\frac{x^{k-1}}{(k-1)!}
=\sum_{j=0}^{n-1}\frac{x^j}{j!}
=P_{n-1}(x).
```

The middle equality uses $`k!=k(k-1)!`$. In the next sum $`j=k-1`$ merely renames the index: as $`k`$ runs from 1 to $`n`$, $`j`$ runs from 0 to $`n-1`$. No infinite series has been differentiated.

Consequently

```math
R_n'(x)=e^x-P_{n-1}(x)=R_{n-1}(x).
```

Also $`P_n(0)=1`$ because its constant term is 1 and all positive powers vanish; hence $`R_n(0)=e^0-1=0`$. The exponential and the finite polynomial are continuous and differentiable on the required intervals. For a fixed positive target $`x`$, apply the theorem to $`R_n`$ on $`[0,x]`$:

```math
R_n(x)-R_n(0)=R_n'(c)x=R_{n-1}(c)x\gt 0,
\qquad 0\lt c\lt x.
```

The induction hypothesis applies at $`c`$ because $`c`$ is positive. Both factors on the right are positive. Thus $`R_n(x)\gt 0`$, proving the next case and therefore all finite cases:

```math
e^x\gt P_n(x)\qquad(x\gt 0,\ n=0,1,2,\ldots).
```

The comparison at zero and the derivative relation play different roles: the former fixes the initial difference, while the latter controls how it changes on the connecting interval.

For a fixed positive $`x`$, this establishes a positive gap for every finite $`n`$. It does not show that the gaps tend to zero. Even an increasing sequence of lower values can approach a value strictly below its ceiling: $`1-1/(n+1)`$ is always below 2 and increases to 1. Thus an upper bound alone does not identify a limit as that bound. To obtain the exponential series identity by this route, one would additionally need to establish $`R_n(x)\to0`$. The baseline supplies that identity as established knowledge, but the finite-inequality proof here does not prove its convergence assertion.

[Return to P5](main.md#d013-main-p5) · [Hint P5](hints.md#d013-hint-p5)

[Return to the reading route](main.md#d013-main-start) · [Hints](hints.md#d013-hints-start)
