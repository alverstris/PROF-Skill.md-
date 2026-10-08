D021 source technical review

Work, average value, probability

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/c9b0814986c30ee6aca81d0c9b3614d6_lec23.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec23/
SHA-256: 1463ecbf26380b9de000787155616be41e5c359102f4dae285d70c255131b182

Independently recomputed SHA-256 matches the audit. Read all 11 complete page text extractions and opened every original full-page render with view_image, including the cover. PDF page 1 is the unnumbered cover; PDF pages 2–11 are printed pages 1–10. The PDF skill was read and applied for read-only inspection. No unreadable portion. This preparation is source evidence only, not a teaching draft, PROF judgment, SASIS review, or lecture closure.

Page and figure coverage

PDF 1 / printed cover: MIT OCW course identity, Fall 2006 and terms/citation notice.
PDF 2 / printed 1: Discrete arithmetic means; Uniform subdivision and Riemann-sum derivation of average=(b−a)^−1 integral f.
Figure 1: Curve y=f(x) with equally spaced x ticks a to b; sample x4 and its height y4 located by dotted lines.
PDF 3 / printed 2: Average height of unit upper semicircle with respect to x isπ/4; Average of constant53; Arclength-weighted semicircle average setup.
Figure 2: Unit upper semicircle y=sqrt(1−x²), shaded-area labelπ/2 and coordinate axes.
Figure 3: Equal arc/angle segments project to unequal horizontal lengths; labels contrast equal weighting inθ with different weighting inx.
PDF 4 / printed 3: Arclength average 2/π from y=sinθ; Cauldron volumeπ/2 and profile100−30y; Volume weightw(y)=πy and weighted mean80°C; Height mean85°C and endpoint average.
Figure 4: Parabolic cauldron cross-section with rim diameter2m and height1m, matching meter-coordinate y=x².
PDF 5 / printed 4: Explanation of cooler upper-water volume weighting; Dart Gaussian areal model; Annular sector2r1<r<3r1 between3 and5 oclock; Probability as weighted part/whole.
Figure 5: Green board disk radiusr1; concentric radius2r1 and3r1 boundaries; red striped one-sixth annular sector. Caption prints lower radius2ri rather than2r1.
PDF 6 / printed 5: Ring weightce^(−r²)2πrdr and normalization ratio; One-sixth angular factor; Antiderivative ofre^(−r²); Improper denominator integral1/2; Probability reduces to [−e^(−r²)/6]_(2r1)^(3r1).
Figure 6: Concentric ring with radiusr, thicknessdr, circumference2πr and areal weightce^(−r²).
Figure 7: Unlabeled decreasing positive half-bell-shaped shaded graph captioned Normal Distribution; schematic only, not the radial density2re^(−r²).
PDF 7 / printed 6: Closed sector-probability formula; Calibration board-hit probability1/2 givese^(−r1²)=1/2; Powers1/512 and1/16, approximate1% per throw.
PDF 8 / printed 7: Gaussian improper integralQ over whole line; Rotational Gaussian solid withr=sqrt(x²+y²); Shell computation of finite-radius volumeπ(1−e^(−R²)) and limitπ.
Figure 8: Symmetric bell curvee^(−x²), shaded full areaQ and central vertical axis.
PDF 9 / printed 8: Annulus area diagram; Cross-sectionA(y) at fixedy and volume integral withdy.
Figure 9: Red annulus, radiusr, radial thicknessdr, x/y-plane axes.
Figure 10: Three-dimensional x,y,z axes and green sliceA(y) in a plane at fixedy, parallel to xz plane.
PDF 10 / printed 9: Top view of slice thicknessdy; Factorizatione^(−x²−y²)=e^(−x²)e^(−y²); A(y)=e^(−y²)Q withy held constant; Scaled Gaussian cross-section side view.
Figure 11: Top view: two horizontal green slice boundaries separated bydy at fixedy across x direction.
Figure 12: Side view of scaled Gaussiance^(−x²), c=e^(−y²), x→±∞ labels and shaded areaA(y).
PDF 11 / printed 10: IntegratingA(y) givesV=Q²; Dummy-variable invariance and positive square rootQ=sqrtπ; Normalized Gaussian and rescaling to normal density; Sigma>0 standard-deviation assertion.

Findings and independent deductions

D021-E01 | confirmed_coefficient_source_typo | PDF 4 / printed 3 | Numerator of volume-weighted temperature
The source prints π(500y²−10y³)|_0^1=40π. The antiderivative of100y is50y², not500y².
Replace500 by50. The final40π numerator and80°C weighted average then agree.
d(50y²−10y³)/dy=100y−30y²; the printed500 would yield490π at1 rather than40π.

D021-E02 | minor_caption_subscript_typo | PDF 5 / printed 4 | Figure5 caption
The lower radius appears as2r_i, while the board radius and all calculations use r_1.
Read the annular sector as2r_1<r<3r_1, in agreement with the diagram and surrounding text.
There is only one board radius parameter in this example; no sequence indexed by i is introduced.

D021-C01 | averaging_measure_conditions | PDF 2, 3, 4, 5 / printed 1, 2, 3, 4 | Uniform and weighted averages
The derivation assumes equally spaced samples, b>a and an integrable function. Weighted means require a nonzero finite total nonnegative weight.
Use average_f=(1/(b−a))∫f for uniform x, and∫fw/∫w for the chosen nonnegative weightw with0<∫w<∞ and finite∫|f|w.
Equal horizontal spacing produces the source Riemann sum; nonuniform equal-count samples would represent a different measure. For the unit semicircle ds=dθ, so uniform arclength uses(1/π)∫_0^πsinθdθ=2/π, different fromπ/4.

D021-S01 | reviewer_supplementary_temperature_check | PDF 4, 5 / printed 3, 4 | 80°C versus85°C
The distinction between volume and height averages is valid; only the500 typo is erroneous.
Volume-weighted mean height is2/3m, while uniform-height mean is1/2m.
With normalized volume weight2y on[0,1], E[y]=∫2y²dy=2/3; hence E[T]=100−30(2/3)=80. Uniform-height average gives100−30/2=85. Both lie between70 and100, and the cooler-volume explanation is consistent.

D021-C02 | probability_model_and_density_condition | PDF 5, 6, 7 / printed 4, 5, 6 | Dart ce^(−r²), ring weighting and part/whole
The ratio assumes an isotropic planar Gaussian density on the whole plane, c>0, and the given annular-sector approximation of the target. ce^(−r²) by itself is not the one-dimensional radial probability density.
Interpret it as areal density; the radial factor after normalization is pR(r)=2re^(−r²) forr≥0, and angle is uniform. For probabilities, part/whole means integrals of this weight.
Whole-plane mass is2πc∫_0^∞re^(−r²)dr=πc, so normalized areal density isπ^−1e^(−r²). The angular interval is2/12=1/6 of a turn. A physical radius must be scaled: e^(−λr²), λ>0 with inverse-square-length units; the50% calibration suppliesλr1²=ln2.

D021-S02 | reviewer_exact_probability_check | PDF 6, 7 / printed 5, 6 | Sector probability and half-hit calibration
The final about1% probability per dart is correct for the specified model; the source neglects(1/2)^9.
The exact model probability is(1/6)(1/16−1/512)=31/3072≈0.0100911458=1.0091%.
The antiderivative yieldsP=(e^(−4r1²)−e^(−9r1²))/6. Board hit probability1−e^(−r1²)=1/2 gives the powers. Neglecting1/512 gives1/96≈1.0417%, still about1%. These are unconditional per-throw probabilities; conditioned on missing the board, divide by1/2, giving31/1536≈2.0182%. The source final sentence explicitly uses per dart.

D021-G01 | improper_integral_justification_gap | PDF 8, 9, 10, 11 / printed 7, 8, 9, 10 | Gaussian solid computed by two unbounded slicing methods
The source calculates the shell limit correctly but passes between unbounded solid slices and Q² without explicitly proving convergence or justifying the passage. The result is correct.
A bounded-domain squeeze supplies a direct justification without assuming Q is finite first.
Let QR=∫_-R^R e^(−x²)dx. Over the square[−R,R]² the finite product integral equals QR². The disk of radiusR lies inside that square, which lies inside the disk of radius sqrt2 R. Nonnegative integrand givesπ(1−e^(−R²))≤QR²≤π(1−e^(−2R²)). Both bounds tendπ, so QR→sqrtπ. Positivity/evenness then establish the ordinary whole-line improper integral and both tail limits. This is reviewer-derived supplementation, not a proof displayed in the packet.

D021-C03 | positive_root_and_scale_conditions | PDF 11 / printed 10 | Q=sqrtπ and normal-density rescaling
Q²=π alone has two algebraic roots; positivity of the integral selects the positive root. Sigma>0 is explicitly stated.
Use t=x/(sqrt2 σ), dx=sqrt2 σdt, withσ>0; the density is[σsqrt(2π)]^−1 exp(−x²/(2σ²)).
The enlarged original-source render confirmsσ is outside the radical in the denominator; this normalization is correct, not a source typo. Substitution gives integral1 directly fromQ=sqrtπ.

D021-S03 | reviewer_supplementary_standard_deviation_check | PDF 11 / printed 10 | Sigma is its standard deviation
The source asserts the statistical meaning ofσ without computing moments.
For this centered normal density, symmetry gives mean0 and the second moment isσ².
Forσ=1, integrate x²e^(−x²/2): integration by parts gives integral x²e^(−x²/2)dx=integral e^(−x²/2)dx over the whole line since x e^(−x²/2)→0 at both ends. Normalization gives variance1. Scalingx=σt gives varianceσ²; positiveσ is the standard deviation. This is an independent supplement.

D021-V01 | figure_interpretation_limit | PDF 6 / printed 5 | Figure7 Normal Distribution
The picture shows a decreasing positive profile with no axes values. It cannot be the radial density2re^(−r²), which starts at0 and initially increases.
Treat it as a schematic right half of a Gaussian areal/profile function, not as a plot of the radial integrand in the adjacent denominator.
Derivative of2re^(−r²) is2e^(−r²)(1−2r²), so its peak is atr=1/sqrt2. The actual ring integration in the text includes the requiredr factor and remains correct.

D021-L01 | packet_scope_observation | PDF 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 / printed 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | Lecture title versus body
Work appears in the title but there is no work integral or work example in the ten content pages.
Record this as packet coverage, without inventing a missing source section or importing later lecture content.
All content pages were inspected. The body consists of averages, weighted temperature, dart probability, Gaussian integral and normal normalization.

Independent mathematical coverage

- Re-derived continuous average from equally spaced Riemann sums; checked the constant53 example.
- Checked unit-semicircle areaπ/2 and averagesπ/4 inx versus2/π inarclength.
- Recomputed cauldron volume, temperature numerator and both average temperatures.
- Read every dart figure and formula, recomputed angular fraction, radial integral, normalization, calibration and exact sector probability.
- Checked finite shell volumeπ(1−e^(−R²)), slice factorizationA(y)=e^(−y²)Q and dummy-variable equality.
- Independently supplied bounded square/disk squeeze for Gaussian convergence and normalization.
- Re-rendered a high-resolution detail of PDF11 to confirmσ outside the square root; checked rescaling and moments.

Technical disposition

The substantive averages, probability answer, Gaussian integral and final normal-density formula are correct under the recorded measure/model conditions. Confirmed source defects are500 for50 in the temperature antiderivative and the minor radius subscript in Figure5. The Gaussian proof needs an improper-limit justification, supplied separately. No work section exists in this packet despite the title.

Limits

- The dart model is an assumed idealized spatial distribution and annular-sector target. The source anecdote about children and actual hit frequencies is not empirical evidence validated here.
- No work topic, lecture-video material, homework solution or physically measured aiming distribution was supplied by this packet.

Additional visual evidence: normalization-detail.png is a 4x direct rendering of the formula region on PDF11/printed10; inspected to confirm sigma is outside the radical.
