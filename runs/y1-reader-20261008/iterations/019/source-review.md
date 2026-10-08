D019 source technical review

Applications to logarithms and geometry

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/df90380a9805621e488cac35fe009764_lec21.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec21/
SHA-256: d73cb5e6e92b0a43661aa21a43f5b8cb991962e04eada5bdc292782b2aeb20d5

Independently recomputed SHA-256 matches the audit. Read all 7 complete page text extractions and opened every original full-page render with view_image, including the cover. PDF page 1 is the unnumbered cover; PDF pages 2–7 are printed pages 1–6. The PDF skill was read and applied for read-only inspection. No unreadable portion. This preparation is source evidence only, not a teaching draft, PROF judgment, SASIS review, or lecture closure.

Page and figure coverage

PDF 1 / printed cover: MIT OCW course identity, Fall 2006 and terms/citation notice.
PDF 2 / printed 1: Integral definition L(x) on x>0; Power antiderivative exception n=-1; FTC2 derivative, L(1)=0, signs, monotonicity and concavity; Multiplication-to-addition proof starts by additivity.
PDF 3 / printed 2: Substitution t=au completes L(ab)=L(a)+L(b); Limits at infinity via powers of two and at zero via reciprocals; Definitions ln x=L(x), e, inverse exponential and a^x; Graph of logarithm.
Figure 1: Increasing concave-down log curve on positive x through (1,0), arrows toward +∞ and −∞; vertical asymptote at x=0 implied.
PDF 4 / printed 3: Area between graphs f≥g; Example x=y² and y=x−2 setup and intersections diagram.
Figure 2: Blue region between upper f and lower g on [a,b], vertical strip dx.
Figure 3: Sideways parabola and diagonal line with labels (0,0), (0,−2), (1,−1), (4,2); an unlabeled horizontal baseline is drawn through (0,−2).
PDF 5 / printed 4: Intersection equation y²−y−2=0; Vertical slicing split at x=1, limits 0 to1 and 1 to4; Horizontal slicing and area calculation 9/2.
Figure 4: Repeated parabola/line plot with vertical red dx strip and dotted split at x=1; same baseline placement as Figure3.
PDF 6 / printed 5: Horizontal slice figure; Revolution around x-axis and disk dV=πy²dx.
Figure 5: Repeated plot with horizontal blue dy strip from parabola left to line right; curve labels and intersection coordinates checked.
Figure 6: Three-dimensional solid about x-axis, y and z axes, thin purple planar strips rotated, full rotation 2π annotation and caption angles π/4,π/2; slice thickness dx.
PDF 7 / printed 6: Ball radius a with upper semicircle sqrt(a²−x²); Disk integral over [−a,a]; Evenness reduction to twice integral over [0,a] and volume 4πa³/3.
Figure 7: Circle cross-section with upper solid and lower dashed semicircles, radii a, endpoints −a,+a, red vertical dx strip, x/y axes.

Findings and independent deductions

D019-E01 | confirmed_reversed_width_source_error | PDF 5 / printed 4 | Easy Way: Horizontal Slices prose and symbolic formula
The prose says subtract right from left and writes xleft−xright. Its actual integrand (y+2)−y² uses right minus left and gives positive 9/2.
Correct the rule to xright−xleft. Here right=y+2 and left=y² for −1≤y≤2.
(y+2)−y²=(2−y)(y+1)≥0 in the interval. The literal symbolic source order would yield −9/2.

D019-E02 | confirmed_differential_source_typo | PDF 5 / printed 4 | Horizontal area evaluated integral
The integral with limits y=−1 to y=2 and integrand (y+2)−y² is followed by dx.
Use dy.
The strip thickness in Figure5 is dy and the antiderivative y²/2+2y−y³/3 differentiates with respect to y.

D019-E03 | confirmed_missing_factor_source_error | PDF 7 / printed 6 | Both symmetry-method antiderivative displays
The first unsymmetrized ball computation correctly integrates −πx² to −πx³/3. Both later symmetry antiderivative displays print 2(πa²x−x³/3), omitting π in the cubic term.
Use 2(πa²x−πx³/3), or 2π(a²x−x³/3).
Differentiating the printed inner expression gives πa²−x², not π(a²−x²). The final numeric substitution and final 4πa³/3 are correct after restoring the factor.

D019-C01 | positive_domain_and_orientation_condition | PDF 2, 3 / printed 1, 2 | Log product proof and definitions
The source explicitly defines L on x>0, so a,b in the product law and base a in a^x must be positive. The printed inequalities a<t<ab and 1<u<b only depict b>1.
Keep a,b>0 and use oriented endpoints t=a→ab, u=1→b, valid also when 0<b<1.
Because a>0, dt/t=du/u under t=au; the definite substitution handles reversed bounds. The product law and reciprocal identity are valid for every positive a,b, not only the pictured ordering.

D019-S01 | reviewer_supplementary_inverse_justification | PDF 3 / printed 2 | Definition of e and exponential
The source has already established strict increase, continuity and endpoint limits; it then defines the inverse and e.
The intermediate value theorem and strict monotonicity provide existence and uniqueness of the e with L(e)=1 and a bijection L:(0,∞)→R.
If E=L^{-1}, inverse differentiation gives E-prime(t)=1/L-prime(E(t))=E(t). L(E(s)E(t))=s+t proves E(s+t)=E(s)E(t). This makes precise the source construction without circular use of a prior logarithm.

D019-C02 | area_order_condition | PDF 4, 5 / printed 3, 4 | A=integral_a^b(f−g)
The figure encodes a≤b and f≥g; these conditions are needed for ordinary positive area.
For curves that exchange order, split at crossings or integrate |f−g|; for horizontal slices integrate right minus left.
Every thin slice contributes nonnegative width times nonnegative thickness. In this example the vertical lower boundary changes from −sqrt(x) to x−2 at x=1.

D019-S02 | reviewer_supplementary_area_check | PDF 5 / printed 4 | Vertical and horizontal area computations
The final area 9/2 is correct despite horizontal-label errors; the vertical setup is not evaluated in source.
Both methods agree when evaluated.
Vertical first part integral_0^1 2sqrt(x)dx=4/3. Second part [2x^(3/2)/3−x²/2+2x]_1^4=19/6. Total=27/6=9/2. Horizontal [y²/2+2y−y³/3]_-1^2=10/3−(−7/6)=9/2.

D019-C03 | solid_region_and_slice_condition | PDF 6, 7 / printed 5, 6 | Rotate f or upper part of curve to get solid
Rotating a curve alone produces the boundary surface; the volume formula concerns the filled region between the curve and the axis.
Use the region 0≤y≤f(x) with nonnegative f, or more generally disk radius |f(x)| where appropriate. For a ball take a>0 and −a≤x≤a.
Cross-sectional disks have area πf(x)² and volume is their area integral. A finite varying-radius slice is only approximated by a cylinder; the Riemann limit makes V=integral πf² exact.

D019-V01 | figure_axis_ambiguity | PDF 4, 5, 6 / printed 3, 4, 5 | Figures3–5 horizontal baseline
The horizontal baseline is drawn through the label (0,−2), while the vertex labeled (0,0) sits above it. The baseline has no x label.
Do not interpret that line as the actual y=0 coordinate axis; if it is intended as the x-axis, its placement is erroneous. Use the explicit point coordinates and equations to determine the geometry.
The true x-axis must pass through (0,0), and y=x−2 intersects it at (2,0). The labeled intersections and slicing logic otherwise match the equations.

Independent mathematical coverage

- Recomputed L-prime=1/x, L-double-prime=−1/x² and the signs from oriented integrals.
- Checked the product substitution, L(2^n)=nL(2)>0 divergence and reciprocal relation.
- Checked the inverse/exponential construction under positive-domain conditions.
- Solved intersections (y−2)(y+1)=0 and confirmed coordinates (1,−1),(4,2).
- Independently evaluated both slice directions to 9/2 and inspected all graph labels and widths.
- Recomputed ball disk volume both on [−a,a] and using evenness, exposing the missing π in two intermediate expressions.

Technical disposition

The integral logarithm construction is sound with positive-domain and oriented-bound qualifications. The geometric examples have correct final values but source errors in the horizontal-width rule, horizontal differential, and two sphere antiderivatives; these are recorded exactly. The repeated area-figure baseline remains explicitly ambiguous, not assumed a valid x-axis.
