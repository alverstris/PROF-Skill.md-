<a name="start"></a>

P001. Newton’s method and a ring on a string — Lecture 13

These notes follow MIT 18.01 Single Variable Calculus, Fall 2006, Lecture 13. The two goals are to use a tangent to improve an equation-solving estimate, and to use a derivative to find and justify a lowest position under a fixed-length constraint. Familiar algebra, differentiation, right-triangle trigonometry and force balance are assumed. The different roles of their equations matter: finding a zero of a function and finding a zero of a derivative answer different questions.

P002. Reading route

Read the [core](#core) in order and pause at Q1–Q3 when they appear. Q4 is a [later mixed revisit](#q4). Each question has a direct link to its hint; [all hints](#hints) are grouped separately from [all complete solutions](#solutions). A partial attempt is useful: compare its first uncertain connection with the hint, then use the solution if needed. The figures and their captions belong to the core. The [source note](#source) explains corrections to the original lecture.

<a name="core"></a>

P003. From a curve to an equation-solving step

A root of $`f(x)=0`$ is an input whose graph point lies on the horizontal axis. For $`f(x)=x^2-3`$, there are two roots, $`-sqrt3`$ and $`+sqrt3`$. We first seek the positive one. An estimate $`x_0=1`$ gives the curve point $`(x_0,f(x_0))=(1,-2)`$. The subscript is a step number, not a power; $`x_0`$ is the starting input, $`x_1`$ the next input, and $`f(x_0)`$ is the current height.

P004. The tangent supplies a simpler equation

Near the current point, replace the curve by its tangent line. The tangent has the same value and slope there. With slope $`m=f'(x_0)`$, its equation is

$$
y-f(x_0)=f'(x_0)(x-x_0).
$$

To construct the next estimate, put $`y=0`$ because we want the line's horizontal-axis intercept, and call that intercept's input $`x_1`$:

$$
-f(x_0)=f'(x_0)(x_1-x_0),
\qquad x_1=x_0-\frac{f(x_0)}{f'(x_0)}.
$$

The division requires a defined, nonzero derivative. This exactly solves the tangent-line equation. It only approximately solves the curve equation; a tangent and a curve usually meet the horizontal axis at different inputs.

P005. A complete first step

For $`f(x)=x^2-3`$, $`f'(x)=2x`$. At $`x_0=1`$ the tangent is $`y+2=2(x-1)`$, or $`y=2x-4`$. Its intercept is $`x_1=2`$. Checking the original function gives $`f(2)=1`$, so the step has not found an exact root. It has moved from a point below the axis to an estimate on the other side of the positive root. To repeat, move vertically from $`(2,0)`$ to the curve point $`(2,1)`$, then use the new tangent there. Do not reuse the old slope.

<a name="q1"></a>

P006. Q1 — supported construction

For $`f(x)=x^2-5`$ and starting estimate $`x_0=2`$, write the tangent line at $`(2,f(2))`$, find its horizontal-axis intercept $`x_1`$, and explain why $`x_1`$ is a new estimate rather than the curve point's height. Give the exact fraction and check $`f(x_1)`$. Target: construct and interpret one Newton step. A complete response connects the tangent equation to the update and distinguishes an approximate root from an exact root. [Hint Q1](#h1) · [Solution Q1](#s1)

P007. Iterating the same construction

Newton’s method repeats P004 at the current input $`x_k`$:

$$
x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.
$$

Read the right side as “current input minus current value divided by current slope”; evaluate both function and derivative at the same input before updating. The left side is the newly produced input. For the square-root example this becomes

$$
x_{k+1}=x_k-\frac{x_k^2-3}{2x_k}
=\frac{x_k}{2}+\frac{3}{2x_k}.
$$

Thus $`x_2=2/2+3/4=7/4`$, and $`x_3=7/8+6/7=97/56`$. Each denominator uses the current estimate, and zero is excluded. This is a recurrence: the output of one step becomes the input of the next.

P008. Figure 1 — successive tangent intercepts

![Two Newton steps for the positive root and a negative starting point](figures/newton-steps.png)

The left panel plots the actual curve $`y=x^2-3`$. The red tangent at $`(1,-2)`$ meets the axis at $`x_1=2`$; the blue tangent at $`(2,1)`$ meets it at $`x_2=7/4`$. The dotted vertical segments merely locate the next curve point; they are not tangents. The right panel shows the same construction starting at $`x_0=-1`$: its first intercept is $`x_1=-2`$. Axis intercepts, current curve points and tangent slopes have the same roles in the general update, even for a differently shaped function.

P009. Accuracy in this example

Continuing without premature rounding gives $`x_4=18817/10864`$. The absolute errors, measured as distance from the positive root, are approximately

$$
\begin{aligned}
|x_0-\sqrt3|&=0.7320508076,\\
|x_1-\sqrt3|&=0.2679491924,\\
|x_2-\sqrt3|&=0.0179491924,\\
|x_3-\sqrt3|&=0.0000920496,\\
|x_4-\sqrt3|&=0.0000000024.
\end{aligned}
$$

These are errors in the input estimates, not the residual heights $`f(x_k)`$. The original lecture's rough values are consistent with these scales. Close agreement of consecutive displayed decimals alone does not certify accuracy: rounding or a failed iteration can mislead. Here, as an independent check, squaring the decimal endpoints gives

$$
1.73205080^2=2.99999997378064<3,
\qquad
1.73205081^2=3.0000000084216561>3.
$$

Since squaring is continuous and increasing for positive inputs, the positive root lies between those endpoints. This bracket certifies the root rounded to seven decimal places as $`1.7320508`$.

P010. Why the errors shrink so quickly

Let $`r=sqrt3`$ and let the signed error be $`e_k=x_k-r`$. Using $`r^2=3`$ in P007 gives the exact identity

$$
e_{k+1}=\frac{x_k^2+r^2-2rx_k}{2x_k}
=\frac{(x_k-r)^2}{2x_k}
=\frac{e_k^2}{2x_k}.
$$

Starting from $`x_1=2>r`$, this identity keeps every subsequent estimate above $`r`$. Also $`0<e_k<x_k`$, so $`0<e_{k+1}<e_k/2`$. Repeated halving bounds the errors by a geometric sequence tending to zero; hence these estimates really do converge to $`r`$. Once close to $`r`$, the factor $`1/(2x_k)`$ changes little and the next error is roughly a constant times the square of the current error. An error of order $`10^{-d}`$ then becomes roughly of order $`10^{-2d}`$. This explains the lecture's approximate doubling of correct digits here. It is not a promise for every function or starting value.

P011. What a limit calculation can establish

Write $`\bar x`$ for a proposed finite limit of the iterates. If the sequence converges and $`\bar x\ne0`$, continuity of addition and reciprocal away from zero lets us take limits in P007:

$$
\bar x=\frac{\bar x}{2}+\frac{3}{2\bar x}
\quad\Longrightarrow\quad
\frac{\bar x}{2}=\frac{3}{2\bar x}
\quad\Longrightarrow\quad
\bar x^2=3.
$$

This identifies possible nonzero limits; it does not by itself prove that a limit exists or select its sign. P010 supplies convergence for the positive start. For a negative start $`x_0=-1`$, write $`z_k=-x_k`$. Substitution into the recurrence shows $`z_{k+1}=z_k/2+3/(2z_k)`$, with $`z_0=1`$. Thus $`z_k\to\sqrt3`$ and $`x_k\to-\sqrt3`$. Newton’s method has solved the equation, but not the intended positive-root problem. At $`x_0=0`$, the derivative is zero and there is no Newton step at all.

P012. A step can exist without leading to convergence

A sequence can repeat two distinct estimates indefinitely. The lecture illustrates such a two-cycle schematically. Figure 2 supplies one concrete function, $`h(x)=-x^3+3x`$, and the two inputs $`a=-1/\sqrt5`$ and $`b=1/\sqrt5`$. At either of these inputs, $`h'(x)=3-3x^2=12/5`$ and $`h(x)=(14/5)x`$. Therefore its Newton intercept is $`x-(14x/5)/(12/5)=-x/6`$—which would not give the claimed cycle. That pair must not be used as a cycle example.
