<a id="d013-hints-start"></a>

Hints — Mean value theorem and inequalities

Use the hint for the task you are attempting, then return to it. Complete answers are in a [separate solutions file](solutions.md#d013-solutions-start). [Return to the lesson](main.md#d013-main-start).

<a id="d013-hint-p1"></a>

Hint P1

The polynomial has no breaks and its derivative exists throughout the interval. The endpoints give a secant slope of 1. Set $`3c^2=1`$, then compare both algebraic candidates with the required open interval. To assess uniqueness as a theorem claim, consider a straight-line function, whose derivative equals its secant slope everywhere.

[Return to P1](main.md#d013-main-p1) · [Solution P1](solutions.md#d013-solution-p1)

<a id="d013-hint-p2"></a>

Hint P2

For (a), evaluate $`g(0)`$ and $`g(3)`$, then write the two linear formulas on either side of the corner at 1. Their slopes give every possible derivative value away from the corner. For (b), compare the actual values at −1 and 1. The closed interval joining those inputs contains zero; check whether the function is even defined at that input before applying a theorem to the interval.

[Return to P2](main.md#d013-main-p2) · [Solution P2](solutions.md#d013-solution-p2)

<a id="d013-hint-p3"></a>

Hint P3

Differentiate using the power rule to get $`f'(t)=1/(2\sqrt{t})`$. The tangent approximation uses $`f'(4)`$, while the exact identity uses $`f'(c)`$ with $`4\lt c\lt 4.04`$. Increasing the positive denominator decreases its reciprocal, so

```math
\frac1{2\sqrt{4.04}}\lt f'(c)\lt \frac14.
```

Multiply this comparison by the positive step 0.04, then add the starting output 2.

[Return to P3](main.md#d013-main-p3) · [Solution P3](solutions.md#d013-solution-p3)

<a id="d013-hint-p4"></a>

Hint P4

Use $`d(x)=x-\ln(1+x)`$, whose value at zero is zero. The chain rule and a common denominator give

```math
d'(x)=1-\frac1{1+x}=\frac{x}{1+x}.
```

The denominator is positive throughout the logarithm's domain. Compare the sign on each side of zero. For the negative side, move from the input $`x`$ to the larger input 0 and use what decreasing means.

[Return to P4](main.md#d013-main-p4) · [Solution P4](solutions.md#d013-solution-p4)

<a id="d013-hint-p5"></a>

Hint P5

For the induction, use the difference $`R_n(x)=e^x-P_n(x)`$. The base case compares the exponential with 1. For $`n\ge1`$, differentiating the finite polynomial gives $`P_n'(x)=P_{n-1}(x)`$: each power drops by one, and $`k/k!=1/(k-1)!`$. Use the previous difference to determine the sign of $`R_n'`$, and check $`R_n(0)`$. For the last part, a sequence can stay below a given ceiling and converge to a value strictly below that ceiling. What additional assertion about $`R_n(x)`$ would identify the ceiling as its limiting sum?

[Return to P5](main.md#d013-main-p5) · [Solution P5](solutions.md#d013-solution-p5)

[Return to the lesson](main.md#d013-main-start) · [Complete solutions](solutions.md#d013-solutions-start)
