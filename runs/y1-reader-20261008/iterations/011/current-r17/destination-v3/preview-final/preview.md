P001. Related rates: from geometry to a changing measurement

P002. The aim is to infer an unknown instantaneous rate from a relation between quantities that change together. Read P003–P035 in order and try RR1 and RR2 where they appear. RR3 is a later return task. [Hints](#hints) are grouped after the teaching; [complete solutions](#solutions) come after all hints. Links return to each prompt. These notes develop MIT 18.01 Fall 2006 Lecture 12, including its measurement-sensitivity sketches; the three practice tasks are generated applications.

P003. In a related-rates problem, two quantities depend on the same time $t$. For example, a car's distance along a road and its distance from a roadside radar change together, but not at the same rate. Write $x(t)$ for the first distance and $D(t)$ for the second. The notation $x'=dx/dt$ means the instantaneous change in $x$ per unit time; the prime in this lesson means differentiation with respect to time unless a different derivative is explicitly written. A negative distance rate means that distance is shrinking. Speed along a straight road is the magnitude of the signed road-coordinate rate.

P004. The chain rule connects geometry to motion. If $D$ is determined by $x$, then $dD/dt=(dD/dx)(dx/dt)$. The first factor says how much the radar distance changes per change in road distance; the second says how quickly road distance changes. Their product has distance-per-time units. More generally, differentiating an equation that holds throughout the motion relates the instantaneous rates at the same instant. This is why we first write a relation valid for nearby times, then differentiate, then insert instantaneous values. Fixed constants, such as a permanent road offset, may be inserted before differentiating; an instantaneous value of a changing quantity may not replace that quantity throughout the relation.

P005. A radar beside a straight road

P006. The lecture's radar is fixed 30 ft perpendicular to the road. Let $x$ be the positive distance along the pictured side of the road from its nearest point to the radar, and let $D$ be the sloping distance from radar to car. Consider the approach before the car reaches that nearest point, so $x\gt0$. The instantaneous radar reading is $D=50\,\mathrm{ft}$ and $D'=-80\,\mathrm{ft/s}$. The negative sign comes from the measured sloping distance decreasing; the car's road speed is still to be found. The radar is treated as measuring this distance rate directly.

![Radar geometry: perpendicular fixed offset30ft, variable horizontal distance x, and slant distance D.](figures/radar-v2.png)

P007. Figure 1. The perpendicular offset and road segment are the two legs of a right triangle; $D$ is its hypotenuse. The arrow indicates the approach direction. Thus Pythagoras supplies a relation valid as the car moves. In equations using feet as the length unit, the fixed offset is 30:

$$
30^2+x^2=D^2.
$$

P008. Differentiate both sides with respect to $t$. The derivative of $30^2$ is zero because the radar does not move. The chain rule gives $d(x(t)^2)/dt=2x(t)x'(t)$ and similarly for $D$. Suppressing the repeated $(t)$ yields

$$
2xx'=2DD',\qquad x'=\frac{D}{x}D'\quad(x\ne0).
$$

P009. Now use the geometry at the specified instant: $x=\sqrt{50^2-30^2}=40\,\mathrm{ft}$, choosing the positive distance. Substituting all values at that same instant gives

$$
x'=\frac{50}{40}(-80)=-100\,\mathrm{ft/s}.
$$

P010. The negative sign means motion toward the nearest point on the road; the car's speed is $100\,\mathrm{ft/s}$. For comparison, $1\,\mathrm{mile}=5280\,\mathrm{ft}$ and $1\,\mathrm{hour}=3600\,\mathrm{s}$ give

$$
65\,\mathrm{mile/hour}=65\frac{5280}{3600}\,\mathrm{ft/s}
=95\frac13\,\mathrm{ft/s}.
$$

P011. Therefore the car exceeds the 65 mph limit in this model. The source rounds the limit to $95\,\mathrm{ft/s}$; using the exact conversion leaves the conclusion unchanged. The factor $D/x=50/40\gt1$ explains why a radar distance rate of magnitude 80 is compatible with road speed 100: part of the motion is across the line from radar to car, rather than directly along it. Algebraically, $D'=(x/D)x'$ with $0\lt x/D\lt1$ at this instant. At the closest point, extend $x$ as a signed road coordinate through zero. The divided formula for $x'$ is unavailable at $x=0$: the undivided equation with finite $x'$ and $D=30$ instead gives $D'=0$. A zero distance rate at the closest point does not by itself establish zero road speed.

<a id="rr1"></a>

P012. RR1 — early supported application. A radar is fixed 30 ft perpendicular to a straight road. Let $x$ be the car's positive distance along the road from the nearest point to the radar, and $D$ its distance from the radar. On the same side of that point as in the worked approach example, the car is now travelling away. At $D=50\,\mathrm{ft}$, the measured distance is increasing at $80\,\mathrm{ft/s}$. Determine $dx/dt$ and the car's speed. Explain the sign and whether reversing direction changes the speed inferred from these data. Criterion: use the geometry to relate the two instantaneous rates; distinguish signed rate from speed. [Hint RR1](#hint-rr1). [Solution RR1](#solution-rr1).

P013. The source gives two equivalent alternatives. Solving the geometry first gives $D=(30^2+x^2)^{1/2}$, so the chain rule gives

$$
D'=\frac12(30^2+x^2)^{-1/2}(2xx')
=\frac{x}{\sqrt{30^2+x^2}}x'=\frac{x}{D}x'.
$$

P014. This is the same relation as P008 because $D$ is positive. Returning to the worked approaching-car example, at its specified instant the relation is $-80=(40/50)x'$, again giving $x'=-100\,\mathrm{ft/s}$. Or solve for $x=\sqrt{D^2-30^2}$ on the positive branch and obtain $x'=DD'/\sqrt{D^2-30^2}$. Implicit differentiation of the squared equation is shorter because it avoids these roots. The general choice is to use the simplest relation that retains every changing quantity. Replacing $D$ by 50 before differentiating would falsely describe a permanently fixed radar distance.

P015. A rising water level in a conical tank

P016. The lecture's tank is an inverted circular cone, point downward, 10 ft high with top radius 4 ft. Water enters at $2\,\mathrm{ft^3/min}$. For this worked example assume no water leaves and the level stays horizontal. Let $h(t)$ be water depth measured upward from the point, $r(t)$ the radius of the water surface, and $V(t)$ the water volume. They all change. The fixed tank dimensions are 10 and 4; $r$ is not the tank's fixed top radius except when full. We seek $h'$ when $h=5\,\mathrm{ft}$, using minutes for $t$ in this example.

![Conical tank and half-section: water depth h and surface radius r form a smaller triangle similar to the full height10ft and radius4ft triangle.](figures/cone.png)

P017. Figure 2. The left view shows the water as a smaller cone; the right view takes half of the central vertical section. Horizontal radii correspond, as do vertical heights. The two right triangles share the angle at the point, so similarity gives $r/h=4/10$, hence $r=(2/5)h$ for $0\lt h\le10$. The marked radii run from the centre to an edge, not across the full diameter. This makes explicit the radius intended in the source's cone formula and its similar-triangle figure.

P018. The cone volume formula applies to the water's dimensions: $V=\pi r^2h/3$. Substitute the relation that holds throughout filling, not just at the requested instant:

$$
V=\frac13\pi\left(\frac25h\right)^2h
=\frac{4\pi}{75}h^3.
$$

P019. This elimination of $r$ leaves one changing input, $h$. By the chain rule,

$$
V'=\frac{4\pi}{25}h^2h'.
$$

P020. At $h=5\,\mathrm{ft}$ and $V'=2\,\mathrm{ft^3/min}$, the coefficient of $h'$ is $4\pi\,\mathrm{ft^2}$. Thus

$$
2=\frac{4\pi}{25}(5)^2h',\qquad
h'=\frac1{2\pi}\,\mathrm{ft/min}\approx0.159\,\mathrm{ft/min}.
$$

P021. The answer is positive, as filling requires. Its units follow from volume-per-time divided by area. Indeed $4\pi h^2/25=\pi r^2$ is the area of the current water surface. For a small rise, the added volume is approximately that area times the rise; the derivative gives the limiting ratio exactly. As the cone widens, the same inflow produces a smaller height rate. The rate formula is used for $h\gt0$; division by $h^2$ does not give a finite initial height rate at the ideal sharp point.

P022. If instead we differentiated $V=\pi r^2h/3$ directly, both $r$ and $h$ would require differentiation: $V'=(\pi/3)(2rr'h+r^2h')$. The missing connection would then be supplied by $r'=(2/5)h'$, obtained from similarity. Substitution reproduces P019. Holding $r$ fixed while water rises in this cone would describe a different shape. A cylinder of fixed radius would allow that shortcut; a cone does not.

P023. A related-rates calculation also needs the correct input rate. If water enters and leaves, the change of stored volume is inflow minus outflow, assuming no other volume changes. Denote those nonnegative volume rates by $Q_{\mathrm{in}}$ and $Q_{\mathrm{out}}$: then $V'=Q_{\mathrm{in}}-Q_{\mathrm{out}}$. This balance is the model premise for the next task. It changes the supplied $V'$ while leaving the cone's geometry intact.

<a id="rr2"></a>

P024. RR2 — changed application. An inverted conical tank has total height 10 ft and top radius 4 ft. The water depth $h$ is measured up from its point. Water enters at $2\,\mathrm{ft^3/min}$ and leaves through a leak at the supplied rate $(h/5)\,\mathrm{ft^3/min}$ when $h$ is the numerical depth in feet. Equivalently the outflow is $kh$ with $k=(1/5)\,\mathrm{ft^2/min}$. Volume changes at inflow minus outflow. Find the water-level rate when $h=5\,\mathrm{ft}$. Decide whether the level is rising or falling at each interior depth $0\lt h\lt10$, and whether it can be stationary at an interior depth. Explain why setting $dV/dt=2$ would be incorrect. Criterion: construct the net volume rate, use the tank geometry, and distinguish a volume rate from a height rate. [Hint RR2](#hint-rr2). [Solution RR2](#solution-rr2).

P025. From rates to measurement sensitivity

P026. The source ends with two pointers to Problem Set 3: a satellite margin-of-error calculation and a parabolic-mirror sensitivity sketch. Sensitivity here means how much one inferred quantity changes when an input changes slightly. The same differentiation used for time rates can compare small measurement changes, even when no object is moving.

![Satellite triangle with vertical c, horizontal L and slant distance h.](figures/satellite.png)

P027. Figure 3. Preserve the source's labels: $c$ is the vertical separation, $L$ the horizontal separation, and $h$ the slant distance. Here $h$ is not the vertical water depth from the previous example. For fixed $c\gt0$, Pythagoras gives $L^2+c^2=h^2$. With $L\gt0$, the slant distance satisfies $h\gt c$, and $L=\sqrt{h^2-c^2}$. Differentiating with respect to the measured input $h$ gives

$$
2L\frac{dL}{dh}=2h,\qquad \frac{dL}{dh}=\frac hL.
$$

P028. The derivative has units of length divided by length. A small positive change in the measured $h$ produces a positive inferred change in $L$. To connect this local rate to an actual finite change, let $\Delta h$ be the new measured input minus the original input, and $\Delta L=L(h+\Delta h)-L(h)$. The derivative definition says that $\Delta L/\Delta h$ approaches $dL/dh$ as a nonzero $\Delta h$ tends to zero. Therefore for a sufficiently small change at a fixed point with $L\gt0$,

$$
\frac{\Delta L}{\Delta h}\approx\frac hL,
\qquad \Delta L\approx\frac hL\,\Delta h.
$$

P029. This is a local approximation, not an equality for arbitrary errors. It becomes particularly sensitive near $L=0$, where $h/L$ grows large; the linear estimate then needs correspondingly small input changes and must stay in $h\gt c$. If the triangle actually changes with time while $c$ remains fixed, differentiating gives $2LL'=2hh'$. When $h'\ne0$, division gives $L'/h'=h/L$, the source's time-rate form. The derivative $dL/dh$ remains the clearer way to discuss measurement error because it does not require any motion or division by a possibly zero time rate.

P030. For a concrete sensitivity reading, if $c=3$ length units and $h=5$, then $L=4$ and $dL/dh=5/4$. This means that small slant-distance errors are magnified by about 1.25 in the inferred horizontal distance when the same length unit is used for both. It does not mean that the horizontal distance itself is $1.25h$. If $c$ also changes, differentiating the full equation instead gives $2LL'+2cc'=2hh'$; the zero derivative of $c^2$ in P029 depended on fixed $c$.

P031. The mirror sketch makes the same kind of question visible. Nearby ray directions and nearby positions on the mirror give an angular separation $\Delta\theta$ and a position separation $\Delta a$. The following redraw shows those two separations; it is a schematic, not a supplied calibration curve.

![Parabolic-mirror schematic showing two nearby ray directions separated by delta theta and positions separated horizontally by delta a.](figures/mirror.png)

P032. Figure 4. The curved profile and two ray paths reproduce the source's comparison between positional and angular changes. The angular gap is marked between the two sloping paths; the position gap is marked between their vertical continuations. The source supplies neither a quantitative mirror equation nor complete definitions of the absolute $a$ and $\theta$ coordinates. Consequently this lecture alone does not determine a numerical mirror sensitivity; those details belong to the referenced problem, not to a guessed convention here.

P033. Once a particular setup supplies a differentiable relation $a=f(\theta)$, the local position sensitivity is $da/d\theta$, approximating $\Delta a/\Delta\theta$ for small changes. The reverse sensitivity is $d\theta/da$, approximating $\Delta\theta/\Delta a$. Where a differentiable local inverse exists and $da/d\theta\ne0$, the chain rule gives $(d\theta/da)(da/d\theta)=1$, so the two local sensitivities are reciprocals. This is conditional on the setup and the nonzero derivative; the sketch alone supplies neither value. The source mentions asteroid-impact prediction as another motivation for understanding how measurement errors affect inferred outcomes. No orbital prediction model is being asserted by this geometric example.

P034. A reusable route is now available: identify the changing quantities and fixed constraints in a diagram; write a relation valid beyond one instant; differentiate using the same independent variable throughout; insert simultaneous values; then interpret sign, units, domain and the model's conditions. For measurement sensitivity, replace a time-rate question by a derivative with respect to the uncertain input, and distinguish the derivative from a finite-error approximation. Eliminating a variable before differentiating is useful when a fixed geometric relation permits it, as in the cone.

<a id="rr3"></a>

P035. RR3 — later retrieval and transfer. After a break, first reconstruct the governing relations without looking back. A right triangle has horizontal leg $L\gt0$, vertical leg $c\gt0$ and sloping side $h$. In part (a), $c=3\,\mathrm{km}$ is fixed, $h=5\,\mathrm{km}$ and $h$ is overestimated by $0.01\,\mathrm{km}$. Estimate the resulting change in $L$ using a derivative, calculate the exact change from the two triangles, and explain why these need not be identical. In part (b), the physical vertical separation is now changing: at the same $L,c,h$ values, $dh/dt=0.2\,\mathrm{km/s}$ and $dc/dt=-0.1\,\mathrm{km/s}$. Determine $dL/dt$ and explain which term would be lost if the fixed-$c$ shortcut were reused. Criterion: distinguish finite-error approximation from exact geometry and recognise when differentiating a previously constant quantity is required. A calculator may be used for the square root in (a). This revisits the relation from memory, then tests its use under a changed condition; these are distinct aims. A next-day return is one adjustable study suggestion, not a required interval. [Hint RR3](#hint-rr3). [Solution RR3](#solution-rr3).

P036. Source and scope. Adapted and independently checked from [MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, Lecture 12: Related Rates](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/ba3498155dbaa90b2a82c88174a18ee1_lec12.pdf), all five PDF pages (cover plus printed pages 1–4). The two numerical worked examples and satellite relation are the lecture's; figures here are new explanatory redraws. Practice and its supplied leak law are generated, not MIT assessment questions. The original rounds the speed conversion, calls $V$ tank volume before switching to changing water dimensions, and leaves the final problem-set sketches abbreviated. These notes make the relevant meanings and limits explicit; they do not reconstruct missing problem-set data.

<a id="hints"></a>

P037. Hints. Use the hint matched to your task, then return to the prompt before opening the separate complete solution.

<a id="hint-rr1"></a>

P038. Hint RR1. Draw the unchanged right triangle and determine its road leg from $D=50$. Increasing radar distance supplies a positive $D'$ now. In $2xx'=2DD'$, which factors stay positive on the stated side of the road? [Return to RR1](#rr1).

<a id="hint-rr2"></a>

P039. Hint RR2. First calculate $Q_{\mathrm{out}}$ at the specified depth and subtract it from inflow. This supplies $V'$, not $h'$. For the sign question, keep $h$ variable in $V'=2-h/5$ using feet and minutes; compare its sign with that of the coefficient $4\pi h^2/25$ multiplying $h'$. [Return to RR2](#rr2).

<a id="hint-rr3"></a>

P040. Hint RR3. In (a), calculate the original horizontal leg, then compare a tangent-based change with $\sqrt{(5.01)^2-3^2}-\sqrt{5^2-3^2}$. In (b), write Pythagoras with all three time-dependent lengths before differentiating. The vertical-leg term now has derivative $2cc'$, which cannot be dropped. [Return to RR3](#rr3).

<a id="solutions"></a>

P041. Complete solutions. These are separated from the hint group so an intermediate suggestion can be used without immediately seeing its full answer.

<a id="solution-rr1"></a>

P042. Solution RR1. Pythagoras gives $x=\sqrt{50^2-30^2}=40\,\mathrm{ft}$ on the stated side. Differentiate the unchanged relation $30^2+x^2=D^2$ before inserting the instantaneous values: $2xx'=2DD'$. Now $D'=+80\,\mathrm{ft/s}$, so

$$
x'=\frac{50}{40}(80)=100\,\mathrm{ft/s}.
$$

P043. The positive rate means increasing road distance from the nearest point, as required for departure. Speed is its magnitude, also $100\,\mathrm{ft/s}$. Reversing direction while keeping the same geometry and radar-rate magnitude reverses the signed rate but leaves the inferred speed unchanged. The signs come from the stated direction, not from a rule that every radar reading must be negative. [Return to RR1](#rr1).

<a id="solution-rr2"></a>

P044. Solution RR2. At $h=5\,\mathrm{ft}$, the leak removes $(1/5)(5)=1\,\mathrm{ft^3/min}$, leaving net volume rate $V'=2-1=1\,\mathrm{ft^3/min}$. The fixed tank shape still gives $r=(2/5)h$ and $V=4\pi h^3/75$. Therefore

$$
1=\frac{4\pi}{25}(5)^2h',\qquad
h'=\frac1{4\pi}\,\mathrm{ft/min}\approx0.0796\,\mathrm{ft/min}.
$$

P045. To decide the direction at every interior depth, keep the depth variable. Using numerical lengths in feet and time in minutes,

$$
\frac{4\pi}{25}h^2h'=2-\frac h5,
\qquad h'=\frac{25}{4\pi h^2}\left(2-\frac h5\right).
$$

P046. For $0\lt h\lt10$, the denominator and $2-h/5$ are positive, so the level is rising. A stationary level would need $2-h/5=0$, which gives $h=10$, outside the open interior interval. Hence there is no stationary interior depth and no falling interior depth in this model. The limiting zero net rate at the brim is not an interior solution. Setting $V'=2$ would ignore the outgoing water and overestimate the rise. [Return to RR2](#rr2).

<a id="solution-rr3"></a>

P047. Solution RR3(a). The original leg is $L=\sqrt{5^2-3^2}=4\,\mathrm{km}$. With $c$ fixed, $dL/dh=h/L=5/4$, so the derivative estimate is

$$
\Delta L\approx\frac54(0.01)=0.0125\,\mathrm{km}.
$$

P048. The exact new geometry gives

$$
\Delta L=\sqrt{5.01^2-3^2}-4
=\sqrt{16.1001}-4
\approx0.01249299\,\mathrm{km}.
$$

P049. Both changes are positive. The estimate uses the slope at the original point as constant over the small input interval; the exact calculation uses the curved relation at its new input. They therefore need not agree exactly. Here the difference is about $0.00000701\,\mathrm{km}$, or $0.00701\,\mathrm m$, since $1\,\mathrm{km}=1000\,\mathrm m$. The estimate slightly overstates the true change. The input change is small enough in this particular geometry for their numerical agreement to be close; this calculation does not supply a universal error bound.

P050. Solution RR3(b). With $c$ now changing, differentiate $L^2+c^2=h^2$ with respect to time, retaining all three terms:

$$
2LL'+2cc'=2hh',\qquad
L'=\frac{hh'-cc'}{L}
=\frac{5(0.2)-3(-0.1)}4
=0.325\,\mathrm{km/s}.
$$

P051. The horizontal separation increases. Increasing slant distance contributes positively through $hh'$; decreasing vertical separation contributes positively through $-cc'$, because less of the slant length is required vertically. Reusing the fixed-$c$ shortcut would omit $2cc'$ and give $0.25\,\mathrm{km/s}$, losing the effect of the shrinking vertical leg. The difference is a changed model condition, not a rounding slip. [Return to RR3](#rr3).
