[P01] Derivatives: slope, velocity and rate of change

[P02] Read P03–P30 in order, pausing for attempts A, B and C. Hints are collected at P32–P35; complete solutions follow separately at P37–P40. Attempt D at P31 is for a later visit. This lesson assumes familiarity with algebra, straight-line gradients, elementary differentiation and the binomial expansion. Its purpose is to connect those tools: construct a derivative from changing quantities, justify the reciprocal and positive-integer power rules, and use the result in geometry and motion.

[P03] A derivative measures a local rate of change. A secant slope compares two distinct points; a derivative asks what those slopes approach as the second point approaches the first. The same construction can describe a graph's slope, an object's velocity or the rate of a measured quantity in another subject. This lecture develops that meaning and some basic calculations. Later differentiation rules can handle more elaborate expressions involving exponentials and inverse trigonometric functions; those are a preview, not a prerequisite here.

[P04] From two points to a quotient. Fix an input $x_0$ for a function $f$. Write $h=\Delta x$ for a nonzero change in input. Both $x_0$ and $x_0+h$ must lie in the function's domain. The two graph points and their changes are
$$
P=(x_0,f(x_0)),\qquad Q=(x_0+h,f(x_0+h)),
$$
$$
\Delta x=h,\qquad \Delta f=f(x_0+h)-f(x_0).
$$
Thus the line through $P$ and $Q$, called a secant, has slope
$$
m_{\mathrm{sec}}=\frac{\Delta f}{\Delta x}
=\frac{f(x_0+h)-f(x_0)}{h}.
$$
To construct the expression, subtract the old output from the new output, and divide by the corresponding input change. To read it, the numerator is the vertical change and the denominator the horizontal change; the result is output units per input unit.

[P05] A coordinate description of the geometry. Introduce $R=(x_0+h,f(x_0))$. Moving from $P$ to $R$ changes the horizontal coordinate by $h$; moving from $R$ to $Q$ changes the vertical coordinate by $\Delta f$. These are signed changes, so either can be negative. Keep $P$ fixed while moving $Q$ towards it along the graph. If the secant slopes approach one finite value from both sides of $x_0$, that value is the derivative:
$$
f'(x_0)=\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}h.
$$
The prime is read “prime”; $f'(x_0)$ is one number at the chosen input. The limit varies $h$, while $x_0$ stays fixed. At an interior point, agreement for positive and negative $h$ is essential. The tangent line is the line through $P$ with this limiting slope. A vertical tangent does not have a finite slope under this definition.

[P06] Tangency is a local slope condition, not an intersection count. For example, $f(x)=x^3$ at $x_0=0$ has quotient $h^3/h=h^2$ for $h\ne0$, which approaches zero. Its tangent is therefore $y=0$, although the curve crosses that line at the origin. Conversely, the line $y=-x$ meets $y=x^3$ only at the origin: $x^3=-x$ gives $x(x^2+1)=0$, whose only real solution is zero. Its slope is $-1$, rather than the tangent slope 0. Even a unique intersection does not establish tangency.

[P07] The reciprocal function. Take $f(x)=1/x$, with $x\ne0$, and choose $x_0\ne0$. We require $h\ne0$ and $x_0+h\ne0$. Directly setting $h=0$ in the difference quotient would give $0/0$, which has no value. Instead, simplify while $h$ is nonzero:
$$
\begin{aligned}
\frac{f(x_0+h)-f(x_0)}h
&=\frac{1/(x_0+h)-1/x_0}{h}\\
&=\frac{x_0-(x_0+h)}{h\,x_0(x_0+h)}\\
&=\frac{-h}{h\,x_0(x_0+h)}
=-\frac1{x_0(x_0+h)}.
\end{aligned}
$$
The common denominator combines the two reciprocal terms; cancellation is valid because $h\ne0$. It preserves the quotient for the nearby inputs used in the limit. It does not give the original quotient a value at $h=0$.

[P08] As $h\to0$, the denominator in the simplified expression approaches the nonzero number $x_0^2$. Consequently,
$$
f'(x_0)=-\frac1{x_0^2}\qquad(x_0\ne0).
$$
This is negative on each branch of the reciprocal graph: as $x$ increases within either branch, the graph falls. The conclusion concerns each interval on which the function is defined; it does not bridge the gap at zero. Cancellation was useful in this calculation. The general requirement is to establish the limit, not to find a cancellation in every derivative problem. An already established differentiation rule may be the simpler method when a first-principles derivation is not requested.

[P09] Attempt A — compare a finite change with the local rate. For $f(x)=1/x$, fix $x_0=2$. Find the secant slopes for $h=0.1$ and $h=-0.1$, then the tangent slope at $x_0=2$. Explain why the secant slopes need not equal the tangent slope, and why the same construction cannot start at $x_0=0$. Your answer should distinguish a nonzero interval from a limit and identify the domain restriction, rather than treating $0/0$ as zero. Hint A: P32. Solution A: P37.

[P10] From a derivative to a tangent equation. A line of slope $m$ through $(x_0,y_0)$ satisfies $y-y_0=m(x-x_0)$: its output change equals its slope times its input change. For a tangent, use $y_0=f(x_0)$ and $m=f'(x_0)$. Here this gives
$$
y-\frac1{x_0}=-\frac1{x_0^2}(x-x_0),
\qquad\text{or}\qquad
y=\frac2{x_0}-\frac{x}{x_0^2}.
$$
In this equation $x_0$ selects one tangent and remains fixed; $x$ and $y$ describe points along that line. Substitution of $x=x_0$ recovers $y=1/x_0$, as required.

[P11] The intercept triangle. The $x$-axis has $y=0$, so the tangent's $x$-intercept satisfies
$$
0=\frac2{x_0}-\frac{x}{x_0^2},
\qquad x=2x_0.
$$
The $y$-axis has $x=0$, so its $y$-intercept is $2/x_0$. Writing $y_0=1/x_0$, this is $2y_0$. Thus the triangle has vertices
$$
(0,0),\qquad (2x_0,0),\qquad (0,2/x_0).
$$
The axes are perpendicular, and their segment lengths are $|2x_0|$ and $|2/x_0|$. Its geometric area is
$$
A=\frac12|2x_0|\,\left|\frac2{x_0}\right|=2
$$
in coordinate square units, for every $x_0\ne0$. For positive $x_0$ the triangle lies in the first quadrant; for negative $x_0$ it lies in the third. Absolute values keep lengths positive in both cases.

[P12] For a concrete picture, $x_0=2$ gives contact point $(2,1/2)$, tangent $y=1-x/4$, and intercepts $(4,0)$, $(0,1)$. The triangle has base 4 and height 1, hence area 2. Changing $x_0$ changes its shape while preserving the product of its perpendicular side lengths. The contact point is the midpoint of the segment between the intercepts, because the coordinate averages are $x_0$ and $1/x_0$.

[P13] The reciprocal graph also has a useful symmetry: $y=1/x$ is equivalent to $xy=1$, which is unchanged when $x$ and $y$ are exchanged. Reflection in the line $y=x$ therefore takes the graph to itself. It sends the contact point $(x_0,y_0)$ to $(y_0,x_0)$, its tangent to the tangent there, and the old $y$-intercept to the new $x$-intercept. Applying the already established $x$-intercept rule at the reflected contact point gives $2y_0$. This explains the symmetry shortcut for the original $y$-intercept; setting $x=0$ in P11 gives the same result directly.

[P14] Reading derivative notation. For $y=f(x)$, with the second input written $x=x_0+\Delta x$,
$$
\Delta y=\Delta f=f(x)-f(x_0)
=f(x_0+\Delta x)-f(x_0).
$$
Here $\Delta f$ means a change in the output of $f$, not a new function. The two quotients $\Delta y/\Delta x$ and $\Delta f/\Delta x$ are the same finite-change slope. Their limit at $x_0$, when it exists, can be written
$$
f'(x_0)=\left.\frac{dy}{dx}\right|_{x=x_0}.
$$
The vertical bar means “evaluate at the stated input”. The fraction-shaped notation $dy/dx$, called Leibniz notation, denotes a derivative; it is not obtained by putting $\Delta x=0$ in the finite-change fraction. In particular, its letter $d$ is not an algebraic factor to cancel.

[P15] Allow the evaluation input to vary and the derivative becomes a function:
$$
f'(x)=\frac{df}{dx}(x)=(Df)(x).
$$
The symbols $f'$, $df/dx$ and $Df$ all name the derivative function in this one-variable setting. The operator $d/dx$ means “differentiate the following expression with respect to $x$”; parentheses identify the whole expression on which it acts. For example,
$$
\frac d{dx}\left(\frac1x\right)=-\frac1{x^2},
\qquad
\left.\frac d{dx}\left(\frac1x\right)\right|_{x=2}=-\frac14.
$$
The first is a function rule, while the second is its value at one input. Prime notation is also called Lagrange notation; this corrects the historical label in the source notes. See [the Open University's notation explanation](https://www.open.edu/openlearn/science-maths-technology/introduction-differentiation/content-section-3.4.2).

[P16] Why the positive-integer power rule works. Let $f(x)=x^n$, where $n$ is a fixed positive integer. We now write the evaluation input as $x$ rather than $x_0$; during each limit, this $x$ is still fixed and only $h$ varies. We must examine
$$
\frac{(x+h)^n-x^n}{h}.
$$
When $n=1$, it equals $h/h=1$ for $h\ne0$, so the derivative of $x$ is 1 at every real input. For $n\ge2$, expand the product of $n$ factors $x+h$.

[P17] Selecting $x$ from every factor gives $x^n$. Selecting $h$ from exactly one factor gives $hx^{n-1}$, and there are $n$ choices of that factor, giving $nx^{n-1}h$. Selecting $h$ from two or more factors gives the remaining terms. The full binomial expansion is
$$
(x+h)^n=x^n+nx^{n-1}h+R_n(x,h),
\qquad
R_n(x,h)=\sum_{k=2}^{n}\binom nk x^{n-k}h^k.
$$
The index $k$ counts factors supplying $h$; $\binom nk=n!/[k!(n-k)!]$ counts their possible selections. The summation adds one term for each $k=2,\ldots,n$. A zero exponent on $x$ here denotes the constant polynomial 1, including at $x=0$: selecting no $x$ factors leaves that factor 1. Thus $R_n$ is an exact name for the terms left over, not an approximation or an extra unspecified term.

[P18] The source compresses this remainder as $O(h^2)$. Here the notation means that, for this fixed $x$ and $n$, the magnitude of the remainder is at most $C|h|^2$ for sufficiently small $|h|$, for some finite constant $C$ independent of $h$. To see why, factor $h^2$ from every remaining term:
$$
R_n(x,h)=h^2\sum_{k=2}^{n}\binom nk x^{n-k}h^{k-2}.
$$
The absolute value of a sum is no greater than the sum of its terms’ absolute values. Thus, for $|h|\le1$, the absolute value of the finite sum is no larger than
$$
C=\sum_{k=2}^{n}\binom nk |x|^{n-k}.
$$
All its coefficients are fixed, and $|h|^{k-2}\le1$. Consequently $|R_n(x,h)|\le C|h|^2$. This is the concrete content of the $O(h^2)$ shorthand in this calculation.

[P19] Subtract $x^n$, divide by nonzero $h$, and then take the limit:
$$
\frac{(x+h)^n-x^n}{h}
=nx^{n-1}+\frac{R_n(x,h)}h.
$$
The remainder now obeys
$$
\left|\frac{R_n(x,h)}h\right|\le C|h|\longrightarrow0,
$$
so
$$
\frac d{dx}x^n=nx^{n-1}\qquad(n=1,2,3,\ldots).
$$
For $n=1$, interpret the result as the constant 1, as directly checked in P16. The argument proves this rule for positive integers. Other exponents require their own justification and domain conditions; they do not follow just by replacing the integer $n$ in this finite-product proof.

[P20] For example, when $n=3$,
$$
(x+h)^3=x^3+3x^2h+3xh^2+h^3,
$$
$$
\frac{(x+h)^3-x^3}{h}=3x^2+3xh+h^2\longrightarrow3x^2.
$$
The exact remainder $3xh^2+h^3$ is $O(h^2)$ for fixed $x$, and after division it is $3xh+h^2=O(h)$, meaning bounded in magnitude by a constant times $|h|$ near zero. The bound matters: knowing merely that a remainder tends to zero would not suffice, since the remainder $h$ tends to zero but $h/h=1$. We need the remainder after division by $h$ to disappear. At $x=0$, the cubic quotient is $h^2$, agreeing with P06.

[P21] Polynomials follow by combining derivatives. For differentiable functions $u,v$ and a constant $c$, the quotient for $u+cv$ splits into the quotient for $u$ plus $c$ times the quotient for $v$. Taking their finite limits gives
$$
(u+cv)'=u'+cv'.
$$
A constant function has zero numerator in its quotient and hence derivative zero. Applying these rules to the source's example,
$$
\frac d{dx}(x^2+3x^{10})
=2x+3(10x^9)
=2x+30x^9.
$$
The factor 3 multiplies the derivative, while the power 10 contributes the factor 10 and changes its power to 9.

[P22] Attempt B — connect calculation to geometry. Let $q(x)=x^3-3x$. Construct and simplify $[q(1+h)-q(1)]/h$ for $h\ne0$, then find the tangent at $x=1$. Does this tangent and the two coordinate axes enclose a bounded triangle? Justify the answer from the resulting line, rather than carrying over the reciprocal graph's area result. Your work should show which terms survive the limit and how the slope determines the geometry. Hint B: P33. Solution B: P38.

[P23] From a graph to a falling object. Consider the lecture's idealised pumpkin released from rest 400 feet above the ground. Take upward height $y$ as positive, set $t=0$ at release, ignore air resistance, and use constant downward acceleration of magnitude $32\,\mathrm{ft/s^2}$. The constant-acceleration position rule gives
$$
y(t)=400\,\mathrm{ft}-\left(16\,\mathrm{ft/s^2}\right)t^2.
$$
Equivalently, with numerical height measured in feet and numerical time in seconds, $y=400-16t^2$. These are model assumptions, not a prediction that the same formula describes the collision or the later motion. The factor 16 is half the acceleration magnitude, and its units make the quadratic term a length.

[P24] The ground is at $y=0$, so the model reaches it when $400-16t^2=0$, giving $t^2=25$. We select $t=5$ seconds because elapsed time after release is nonnegative. The negative algebraic root is outside this physical interval. The model is used from release up to first contact at 5 seconds.

[P25] An average velocity is displacement divided by elapsed time. An average speed is total distance travelled divided by elapsed time. For the entire downward fall,
$$
\overline v=\frac{0-400}{5-0}=-80\,\mathrm{ft/s},
\qquad
\text{average speed}=\frac{400}{5}=80\,\mathrm{ft/s}.
$$
The displacement is negative because height decreases; the distance is positive. They have the same magnitude here because there is no reversal. With a reversal, distance accumulates on both parts while signed displacements can cancel. This distinction corrects the source's use of “average speed” for the signed height quotient; see [MIT's one-dimensional velocity definition, section 4.3.1](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter4.pdf) and [MIT's velocity and speed notes](https://www.mit.edu/~hlb/1802/pdf/MIT18_02SC_notes_12.pdf).

[P26] Instantaneous velocity is the derivative of height with respect to time, so the power and constant-multiple rules give
$$
v(t)=\frac{dy}{dt}
=-\left(32\,\mathrm{ft/s^2}\right)t.
$$
Its negative sign indicates downward motion for $t>0$. Its magnitude is the instantaneous speed. The result is also visible directly in the quotient. Using numerical $t,\Delta t$ in seconds and $y$ in feet,
$$
\frac{y(t+\Delta t)-y(t)}{\Delta t}
=\frac{-16[(t+\Delta t)^2-t^2]}{\Delta t}
=-32t-16\Delta t
\quad\mathrm{ft/s}.
$$
The interval must remain within the falling phase and $\Delta t\ne0$. As $\Delta t\to0$, its final term disappears, leaving the same instantaneous velocity. The graph has time on the horizontal axis and height on the vertical axis; its secant and tangent slopes now carry velocity units.

[P27] Just before impact, the model therefore gives
$$
v(5^-)=-160\,\mathrm{ft/s},
\qquad \text{speed}=160\,\mathrm{ft/s}.
$$
The notation $5^-$ means approaching time 5 from earlier times. We can take the limit of $v(t)$ as $t$ rises to 5, or use the quotient at $t=5$ with negative $\Delta t$. Both use only the pre-impact motion. A two-sided derivative of the real motion at the collision is not supplied by this falling model. The impact speed exceeds the average speed because the object accelerates throughout the fall.

[P28] To express that speed in miles per hour, use $1\,\mathrm{mile}=5280\,\mathrm{ft}$ and $1\,\mathrm{hour}=3600\,\mathrm{s}$:
$$
160\,\frac{\mathrm{ft}}{\mathrm{s}}
\left(\frac{1\,\mathrm{mile}}{5280\,\mathrm{ft}}\right)
\left(\frac{3600\,\mathrm{s}}{1\,\mathrm{hour}}\right)
=\frac{1200}{11}\,\mathrm{mph}\approx109.1\,\mathrm{mph},
$$
or about 110 mph. Each conversion factor equals one, and the unwanted feet and seconds cancel. The [NIST length conversion table](https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors) and [NIST time-unit table](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-5-units-outside-si) give these unit relations.

[P29] Attempt C — choose the rate that answers the question. A different object has prescribed upward position $z(t)=(t-1)^2$ metres, with the numerical time $t$ in seconds on $0\le t\le2$. This is a specified motion, not the preceding gravity model. It moves down to $z=0$ at $t=1$, then up again. Find its average velocity and average speed over the whole interval, and its velocity and speed at $t=1.5$. Explain why the first two answers can differ even though they use the same total time. A complete response must identify the distance on each leg, the signed displacement, and whether an interval quotient or a derivative is needed. Hint C: P34. Solution C: P39.

[P30] The same distinction applies beyond motion: a finite output change divided by a finite input change is an average rate, whereas its local limit is a derivative when that limit exists. Always retain the quantity being differentiated, the input with respect to which it changes, the evaluation point or interval, and the domain or physical phase in which the calculation applies.

[P31] Attempt D — later recall and transfer. On your next study visit, perhaps tomorrow or after a few days, first close the main lesson and write the derivative definition at a fixed $x_0$, including the restrictions on the quotient and the limit. Adjust that revisit interval to your study needs. Then apply the ideas to $g(x)=-2/x$, $x\ne0$: find the tangent at an arbitrary $x_0\ne0$, its two axis intercepts, and the enclosed triangle's area. Decide whether the area depends on $x_0$, and explain how a positive tangent slope can coexist with a positive area. The first part checks recall of the construction; the changed curve checks transfer of the derivative, line and geometric-length reasoning. Reopen the lesson when needed and distinguish that supported attempt from what you recalled unaided. Hint D: P35. Solution D: P40.

[P32] Hint A. Substitute $x_0=2$ into the simplified quotient in P07, giving $-1/[2(2+h)]$. Keep the chosen nonzero $h$ when finding each secant slope. For the tangent, let $h$ tend to zero instead. At the proposed input 0, check whether the fixed point $P$ can be formed at all.

[P33] Hint B. First obtain $q(1)=-2$. Expand
$$
q(1+h)=(1+h)^3-3(1+h)
$$
before subtracting $q(1)$. After finding the slope, put it and the point $(1,-2)$ into the line equation. Check whether that line meets the $x$-axis.

[P34] Hint C. The three positions at times 0, 1 and 2 are $1,0,1$ metres. Add the lengths of the two separate legs for distance, but subtract final minus initial position for displacement. For the instant $t=1.5$, differentiating $z=t^2-2t+1$ supplies a rate at one time.

[P35] Hint D. Use the constant-multiple rule with the reciprocal derivative; keep the two minus signs. For the line, the contact point has height $-2/x_0$. Set $y=0$ and $x=0$ separately for its intercepts. Geometric side lengths are the absolute values of intercept coordinates, even when the coordinates have opposite signs.

[P36] Complete solutions. The following answers correspond to A–D in order. The preceding hint group is separate so that you can use a hint before reading a full answer.

[P37] Solution A. With $h=0.1$, the secant slope is $-1/4.2=-5/21\approx-0.2381$. With $h=-0.1$, it is $-1/3.8=-5/19\approx-0.2632$. The tangent slope is $f'(2)=-1/4=-0.25$. Both secants compare two distinct points, while the tangent uses the limiting slopes at the fixed point. Nonzero interval slopes therefore need not equal their limit. At $x_0=0$, $f(0)$ is undefined, so neither the starting graph point nor a derivative there exists for this function. This is a domain failure, not a rule that every undefined quotient should be assigned zero. Return to P10.

[P38] Solution B. Since $q(1)=-2$ and
$$
q(1+h)=1+3h+3h^2+h^3-3-3h=-2+3h^2+h^3,
$$
the quotient is
$$
\frac{q(1+h)-q(1)}h=3h+h^2\longrightarrow0.
$$
Thus $q'(1)=0$, agreeing with $q'(x)=3x^2-3$. The tangent through $(1,-2)$ is $y+2=0(x-1)$, or $y=-2$. It meets the $y$-axis at $(0,-2)$ and is parallel to, and distinct from, the $x$-axis. There is no $x$-intercept and no bounded triangle formed by these three lines. The reciprocal area calculation depended on having both nonzero finite intercepts. Return to P23.

[P39] Solution C. The net displacement is $z(2)-z(0)=1-1=0$ metres, so average velocity is $0/2=0\,\mathrm{m/s}$. The object travels 1 metre down and 1 metre up, for total distance 2 metres and average speed $2/2=1\,\mathrm{m/s}$. At a single instant use
$$
z'(t)=2t-2,\qquad z'(1.5)=1\,\mathrm{m/s}.
$$
The velocity is upward and its magnitude, the speed, is $1\,\mathrm{m/s}$. Oppositely signed displacements cancel in the whole-interval velocity; positive leg lengths add in distance. This is why taking the magnitude of average velocity would fail to give average speed for this journey. Return to P30.

[P40] Solution D. The recalled definition is
$$
f'(x_0)=\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}h.
$$
The quotient uses nonzero $h$ and requires both function values to be defined. At an interior point it must approach the same finite value from positive and negative $h$. For the changed function,
$$
g'(x)=(-2)\left(-\frac1{x^2}\right)=\frac2{x^2}.
$$
The tangent is
$$
y+\frac2{x_0}=\frac2{x_0^2}(x-x_0),
\qquad
y=\frac{2x}{x_0^2}-\frac4{x_0}.
$$
Its intercepts are $(2x_0,0)$ and $(0,-4/x_0)$. Their coordinates have opposite signs, but their distances from the origin are positive:
$$
A=\frac12|2x_0|\,|-4/x_0|=4.
$$
The area is independent of nonzero $x_0$. The slope measures signed vertical change per horizontal change along a line; area uses the product of positive perpendicular lengths. A positive slope imposes no negative-area requirement.

[P41] Source and licence. Adapted from MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, taught by David Jerison, [Lecture 1: Derivatives, Slope, Velocity, and Rate of Change](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/c6a2d4081848972d197c41332e604d49_lec1.pdf). MIT's [course page](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/) identifies the course and instructor. This adaptation is distributed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/), following [MIT OCW's terms](https://ocw.mit.edu/pages/privacy-and-terms-of-use/). MIT and the instructor do not endorse this adaptation.

[P42] Changes from the source. The explanations and coordinate descriptions have been rewritten, domain and limit conditions made explicit, the binomial remainder justified, and original practice with separate hints and solutions added. The prime-notation attribution and the distinction between signed velocity and speed have been corrected. The falling-motion prediction is limited to first contact, and geometric area uses positive lengths on either reciprocal branch. The coordinate constructions supply the mathematical information needed here without requiring the source's figure artwork.
