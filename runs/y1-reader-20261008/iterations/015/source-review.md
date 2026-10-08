D015 source technical review

Differential equations, separation of variables

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/991e10d17c527483d3d41d83a7313536_lec16.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec16/
SHA-256: cdf0e899a0f0dd5a57ca1069a5c039c08b9efb84ef6d416f3dce038939564d23

Independently recomputed SHA-256 matches the audit. Read all 5 complete page text extractions and opened every original full-page render with view_image, including the cover. PDF page 1 is the unnumbered cover; PDF pages 2–5 are printed pages 1–4. The PDF skill was read and applied for read-only inspection. No unreadable portion. This preparation is source evidence only, not a teaching draft, PROF judgment, SASIS review, or lecture closure.

Page and figure coverage

PDF 1 / printed cover: MIT OCW course identity, Fall 2006 and terms/citation notice.
PDF 2 / printed 1: ODE notation and antiderivative solution of y-prime=f(x); Operator form (d/dx+x)y=0; Separation and solution y=a exp(-x²/2); restoration of zero solution; initial value y(0)=a.
PDF 3 / printed 2: General separable equation y-prime=f(x)g(y); Reciprocal h=1/g, implicit H(y)=F(x)+c and inverse notation; Identification of f, F, g and H for preceding example.
Figure 1: Gaussian y=exp(-x²/2), peak (0,1), symmetric tails on x=-6 to 6; labels X,Y and caption checked.
PDF 4 / printed 3: Geometric slope condition y-prime=2y/x; Logarithmic separation and family y=ax²; Six parameter examples including zero.
Figure 2: Parabola in first quadrant, point (x,y), dashed ray from origin, red tangent with twice ray slope. Axes and caption checked.
PDF 5 / printed 4: Orthogonal trajectories y-prime=-x/(2y); Integration to x²/4+y²/2=c; ellipse aspect ratio sqrt(2); Explicit branches ±sqrt(2(c-x²/4)); Exam 2 topic list and external review-sheet pointer.
Figure 3: Two horizontal blue ellipses crossing black upward/downward parabolas orthogonally; horizontal and vertical axes. Crossings are schematic; no numeric scale.

Findings and independent deductions

D015-E01 | confirmed_sign_source_error | PDF 3 / printed 2 | Bottom identification of f(x) in previous example
The source prints f(x)=x while F(x)=-x²/2 and the preceding ODE is y-prime=-xy.
Correct f(x) to -x with g(y)=y.
F-prime=-x; differentiating a exp(-x²/2) gives -xy. The displayed positive f would instead yield a exp(x²/2).

D015-E02 | confirmed_variable_source_typo | PDF 4 / printed 3 | Example 3 parameter list at a=-2
The source prints y=-2y².
The intended member is y=-2x².
Substitute a=-2 into y=ax². The printed algebraic relation is not that parabola.

D015-C01 | division_condition_and_missing_equilibria | PDF 2, 3, 4 / printed 1, 2, 3 | Separation dy/g(y)=f(x) dx
Division requires g(y) nonzero. Examples explicitly restore y=0; the general formula does not list all equilibrium solutions.
Apply separation on a solution interval where g(y) is nonzero; also test every root g(y0)=0 as the constant solution y=y0.
The chain rule gives dH(y(x))/dx=y-prime/g(y)=f(x). If g(y0)=0 then y-prime=0=f(x)g(y0). Without regularity/uniqueness, piecewise solutions reaching or leaving roots can require separate study.

D015-C02 | inverse_domain_condition | PDF 3 / printed 2 | y=H^{-1}(F(x)+c)
H^{-1} is written without specifying branch, interval or range. H=ln|y| is not one-to-one on all nonzero reals.
Choose a connected y-interval with continuous nonzero g, so H-prime=1/g keeps one sign and H is strictly monotone; restrict x so F(x)+c is in its range.
For ln|y| the branches give y=+exp(F+c) or -exp(F+c); the initial value selects sign. This supplies the conditions for the source inverse expression.

D015-C03 | singular_domain_condition | PDF 4 / printed 3 | Example 3 y-prime=2y/x
The ODE and ray slope are undefined at x=0 although the plotted parabolas pass through the origin.
The ODE solutions y=ax² are defined on intervals avoiding x=0; they admit smooth extensions through 0 as curves, but do not satisfy the displayed ODE there.
(y/x²)-prime=(xy-prime-2y)/x³=0 for x nonzero, proving completeness separately on either half-line. Constants on the two sides need not agree absent an extension requirement.

D015-C04 | geometric_and_branch_conditions | PDF 5 / printed 4 | Example 4 ellipses, reciprocal slope and explicit branches
A genuine ellipse requires c>0. The displayed graph ODE divides by y and the negative-reciprocal argument uses finite nonzero parabola slope.
For c>0 use smooth implicit ellipses; graph branches have |x|<2sqrt(c) when differentiating. At y=0 use vertical tangent geometry. c=0 is a point and c<0 has no real locus.
Differentiate x²/4+y²/2=c to get x/2+yy-prime=0; semi-axes 2sqrt(c) and sqrt(2c) have ratio sqrt(2). Where x,y are nonzero, (2y/x)(-x/(2y))=-1. The x-axis member a=0 intersects at y=0 with horizontal/vertical tangents. Ellipse points at x=0,y≠0 do not belong to any finite-a parabola.

D015-S01 | reviewer_supplementary_completeness_check | PDF 2 / printed 1 | Gaussian family
The source obtains the correct one-parameter family and separately includes a=0.
An integrating-factor check proves every differentiable solution is captured, including zeros.
d[exp(x²/2)y]/dx=exp(x²/2)(y-prime+xy)=0, so y=a exp(-x²/2) on each connected interval. This is an independent supplement, not a source-displayed proof.

Independent mathematical coverage

- Antiderivative notation in Example 1 denotes a family; y=F(x)+C when F-prime=f.
- Recomputed logarithmic antiderivatives, exponentiation and y(0)=a for Gaussian family; operator application (d/dx+x)exp(-x²/2)=0.
- General separation verified by chain rule on intervals with g nonzero; inverse branch and equilibrium limitations recorded.
- For y=ax², y-prime=2ax=2y/x when x≠0; tangent/ray slopes in Figure 2 agree.
- Orthogonal trajectory integration gives y²/2=-x²/4+c; explicit branches and sqrt(2) aspect ratio recomputed.
- Exam list fully read; the referenced separate Exam 2 review sheet is not in this assigned lecture-specific packet.

Technical disposition

Two confirmed source typos (sign of f and variable in a=-2 example). Main Gaussian, parabola and ellipse calculations are correct with the recorded separation, domain, branch and nondegeneracy conditions. Figures are legible and consistent as schematic geometry.

Limits

- Quantum-mechanics annihilation-operator naming is an incidental contextual aside; the algebraic null-function relation was checked, but normalization conventions and physical interpretation were not investigated.
- No lecture video or separately referenced exam review sheet was included in this lecture-specific packet.
