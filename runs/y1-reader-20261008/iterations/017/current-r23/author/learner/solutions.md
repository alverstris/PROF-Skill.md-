Complete solutions for Lecture 19

Use these after an attempt or a hint. The solutions explain the decisions as well as the results. They describe anticipated error routes, not mistakes observed in any learner. [Main route](lesson.md) · [Hints only](hints.md)

<a id="s1"></a>
Solution P1

Differentiation gives $(x^6/6)'=x^5$, and $x^5$ is continuous on $[1,2]$. FTC 1 therefore gives

$$
\int_1^2x^5\,dx=\frac{2^6}{6}-\frac{1^6}{6}
=\frac{63}{6}=\frac{21}{2}.
$$

Adding 7 to $F$ adds 7 to both endpoint values: $(F(2)+7)-(F(1)+7)=F(2)-F(1)$. It cannot change the answer. Leaving a free constant in the definite result would confuse a number with a family of antiderivative functions.

[Return to P1](lesson.md#p1) · [Hint P1](hints.md#h1)

<a id="s2"></a>
Solution P2

Velocity vanishes at $t=1$, is negative on $0\le t\lt1$ and positive on $1\lt t\le3$. With antiderivative $V(t)=t^2-2t$, the values at 0, 1, 3 are 0, $-1$, 3. Hence displacement is

$$
\int_0^3v(t)\,dt=V(3)-V(0)=3\text{ metres}.
$$

The early displacement is $-1$ metre and the later displacement is $3-(-1)=4$ metres. Taking both travel amounts positively gives

$$
\int_0^3|v(t)|\,dt
=-\int_0^1v(t)\,dt+\int_1^3v(t)\,dt
=1+4=5\text{ metres}.
$$

The odometer increment is 5 metres. The reversed integral is $\int_3^0v(t)\,dt=-3$ metres by definition, or by $V(0)-V(3)$. It reverses the orientation of the same mathematical interval. It is not an additional trip; the stated physical motion still runs forward from time 0 to time 3. Taking only the absolute value of the net displacement would give 3 metres and miss the backtracking.

[Return to P2](lesson.md#p2) · [Hint P2](hints.md#h2)

<a id="s3"></a>
Solution P3

The given pointwise inequality applies on a forward interval. Integral comparison and FTC 1 give

$$
4=\left[t+\frac{t^2}{2}\right]_0^2
\le[e^t]_0^2=e^2-1.
$$

Thus $e^2\ge5$. This is a lower bound, not an equality determination. Reversing both integrals negates them, so

$$
\int_2^0(1+t)\,dt=-4
\ge\int_2^0e^t\,dt=1-e^2.
$$

The direction is $\ge$ because multiplication of $4\le e^2-1$ by a negative number reverses an inequality. The pointwise ordering of the functions itself has not changed.

[Return to P3](lesson.md#p3) · [Hint P3](hints.md#h3)

<a id="s4"></a>
Solution P4

Choose $u=2-x^2$. Then $du=-2x\,dx$ and $x\,dx=-du/2$. The start $x=0$ maps to $u=2$, and the end $x=1$ maps to $u=1$. Therefore

$$
\int_0^1x(2-x^2)^4\,dx
=-\frac12\int_2^1u^4\,du
=\frac12\int_1^2u^4\,du
=\left[\frac{u^5}{10}\right]_1^2
=\frac{31}{10}.
$$

The negative differential factor and reversed endpoint order cancel. The original integrand is nonnegative on $[0,1]$ and positive except at 0, consistent with a positive answer. A direct antiderivative check gives $-(2-x^2)^5/10$: its derivative is $-5(2-x^2)^4(-2x)/10=x(2-x^2)^4$. Evaluating it at 1 and 0 also yields $(-1/10)-(-32/10)=31/10$. Sorting the new endpoints without accounting for a minus sign would be an incorrect change to the original integral.

[Return to P4](lesson.md#p4) · [Hint P4](hints.md#h4)

<a id="s5"></a>
Solution P5

(a) A complete recalled FTC 1 rule is $\int_a^b f(x)\,dx=F(b)-F(a)$, assuming $f$ continuous on the interval between the endpoints and $F'=f$ there. For substitution, with $u$ continuously differentiable and $g$ continuous on an interval containing its range,

$$
\int_{x_1}^{x_2}g(u(x))u'(x)\,dx
=\int_{u(x_1)}^{u(x_2)}g(u)\,du.
$$

Equivalent names for the variables are fine; preserving the derivative factor, endpoint mapping and conditions matters.

(b) For $0\lt t\lt1$, $2t\gt0$ and $t^2-1\lt0$, so velocity is negative. For $1\lt t\le\sqrt2$ it is positive. Velocity is zero at 0 and 1; only 1 splits the interior of the travel interval into opposite directions.

Choose $u=t^2-1$ because $du=2t\,dt$ matches the other factor. The full interval maps from $u=-1$ to $u=1$, giving displacement

$$
\int_0^{\sqrt2}2t(t^2-1)\,dt
=\int_{-1}^1u\,du
=\left[\frac{u^2}{2}\right]_{-1}^1=0\text{ metres}.
$$

For distance, keep the sign split at $t=1$, which maps to $u=0$:

$$
-\int_0^1 2t(t^2-1)\,dt
+\int_1^{\sqrt2}2t(t^2-1)\,dt
=-\int_{-1}^0u\,du+\int_0^1u\,du
=\frac12+\frac12=1\text{ metre}.
$$

The particle returns to its initial position after travelling half a metre in each direction. Zero displacement therefore does not mean it stayed still. Expanding to $2t^3-2t$ and using antiderivative $t^4/2-t^2$ is equally valid: its values at 0, 1, $\sqrt2$ are 0, $-1/2$, 0, confirming the two signed contributions. Substitution was convenient, not mandatory.

[Return to P5](lesson.md#p5) · [Hint P5](hints.md#h5)
