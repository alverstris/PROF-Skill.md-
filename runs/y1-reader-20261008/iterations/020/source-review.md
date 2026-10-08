D020 source technical review

Volumes by disks and shells

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/dcd410f264f661f8ac1e53ea6df740cc_lec22.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec22/
SHA-256: 6a5a07e58c762c73543e6f9607bf128434d36fd441eacab54147a2f837d44077

Independently recomputed SHA-256 matches the audit. Read all 6 complete page text extractions and opened every original full-page render with view_image, including the cover. PDF page 1 is the unnumbered cover; PDF pages 2–6 are printed pages 1–5. The PDF skill was read and applied for read-only inspection. No unreadable portion. This preparation is source evidence only, not a teaching draft, PROF judgment, SASIS review, or lecture closure.

Page and figure coverage

PDF 1 / printed cover: MIT OCW course identity, Fall 2006 and terms/citation notice.
PDF 2 / printed 1: Cauldron formed by rotating y=x² about y-axis and cutting at y=a; Disk area πx², thickness dy, volume πa²/2.
Figure 1: Gray paraboloid vessel, x/y axes and circular rim.
Figure 2: Horizontal disk slice dy, total height a, paraboloid boundary and top opening.
PDF 3 / printed 2: Meter versus centimeter example and non-scale-invariance warning; Skinny cauldron height100cm, width20cm; Shell construction radius x and height a−x².
Figure 3: Tall narrow parabola section with height100cm and top diameter20cm.
Figure 4: Cylindrical shell inside paraboloid, radius x, vessel height a, outer radius sqrt(a).
PDF 4 / printed 3: Shell integral and agreement πa²/2; Heating profile T=100−30y on 0≤y≤1; Temperature-volume integral 40π degree·m³; Calorie conversion and approximately 500 candy bars.
Figure 5: Cauldron on fire; bottom100°C, top70°C, height a=1m. This is not uniform100°C.
PDF 5 / printed 4: Pipe velocity v=c(R²−r²); Annular flow element v2πr dr.
Figure 6: Pipe cross-section side view with radius R; axial arrows longest at center and shortest at walls.
Figure 7: Parabolic v-versus-r curve from cR² at r=0 to 0 at r=R.
PDF 6 / printed 5: Ring diagram; Flow integral πcR^4/2 and radius scaling; Dart-board Gaussian model and annular hit count.
Figure 8: Gray annulus labeled radius r and radial thickness dr.
Figure 9: Decreasing ce^(−r²) versus r, horizontal r tick2 and vertical intercept tick1. For general c the intercept is c; plot implicitly uses c=1.

Findings and independent deductions

D020-C01 | units_scale_condition | PDF 2, 3 / printed 1, 2 | Equation y=x² and volume πa²/2
The source correctly warns that using the same numerical equation in meters versus centimeters changes physical shape. Dimensional coefficient remains implicit.
Write physical lengths Y=κX² with κ of dimension inverse length. Then V=πA²/(2κ). The original numerical form selects κ from the length unit.
Meter coordinates imply κ=1/m; representing that same shape in centimeters gives κ=.01/cm, not 1/cm. With A=1m the volume πm³/2≈1571 liters. With A=100cm and κ=1/cm it is 5000πcm³≈15.71 liters. Top radii are 1m and10cm respectively, matching the source.

D020-C02 | slice_limit_and_geometric_condition | PDF 2, 3, 4, 5, 6 / printed 1, 2, 3, 4, 5 | Disks, shells and annulus differentials
a>0 and radial variables nonnegative are implicit; a thin shell is approximated by circumference times thickness.
Use a>0, 0≤y≤a and 0≤x≤sqrt(a) in the numerical coordinates; take a Riemann limit. For a ring, dA=2πr dr is the exact area differential.
A finite ring [r,r+Δr] has area π[(r+Δr)²−r²]=2πrΔr+πΔr². After summation on a bounded interval the omitted total is bounded by a constant times maxΔr→0. The same limiting argument applies to shell height variation.

D020-E01 | inconsistent_physical_target | PDF 4 / printed 3 | Boiling cauldron question and conclusion
The question equates the goal with raising water from0°C to100°C, while the imposed final profile ranges from100°C at bottom to70°C at top. The computed 40π integral matches that nonuniform profile, not all water at100°C.
Describe the calculation as heat stored in the specified profile relative to0°C under the model. Uniform100°C requires a different integral; phase-change energy is not included.
V=π/2 m³, so uniform100°C has temperature-volume integral100V=50π degree·m³. The prescribed profile gives π∫_0^1(100−30y)y dy=40π, with volume-weighted mean80°C. Thus the two targets differ by10π degree·m³.

D020-C03 | thermal_model_assumptions | PDF 4 / printed 3 | Calorie conversion and candy-bar comparison
The source uses1cal/(cm³·degree), effectively a constant volumetric heat capacity, and assumes full energy delivery to water. The displayed H before conversion has temperature×volume units, not energy.
Apply Q=∫ρcp(T−Tinitial)dV with the chosen constantρcp≈1cal/(cm³·°C), initial0°C, ignoring vessel heating and heat losses; 250kcal/bar is the example input.
40π×10^6cal=40000πkcal≈125664kcal; dividing by250 gives160π≈502.65 bars. The source500-bar rounded value is correct for that specified idealized profile. The line labeled number of calories but expressed in candy bars has a label/units mismatch.

D020-C04 | specialized_flow_model_conditions | PDF 5, 6 / printed 4, 5 | Parabolic pipe profile
The source presents v=c(R²−r²) as a pipe-flow profile without stating its physical regime.
Interpret as steady, fully developed laminar axial flow of a constant-viscosity Newtonian fluid in a straight stationary circular pipe with no-slip walls; standard pressure-driven model gives c=ΔP/(4μL). MIT fluid-mechanics sources confirm the profile and coefficient.
The calculus integral is independently valid for any given nonnegative profile c(R²−r²), c≥0,R≥0. Its physical applicability is conditional; it is not a general turbulent, entrance-region or pulsatile blood-flow law.

D020-C05 | held_parameter_condition | PDF 6 / printed 5 | Flow proportional to R^4
The stated proportionality requires c fixed while R varies.
Hold pressure drop, pipe length and viscosity fixed in the Poiseuille model; then Q=πΔP R^4/(8μL).
Direct integration yields2πc[R²r²/2−r^4/4]_0^R=πcR^4/2. If maximum speed cR² instead is held fixed, Q=(π/2)vmaxR², not an R^4 scaling. Flow units are volume/time, not speed.

D020-E02 | density_count_terminology_error | PDF 6 / printed 5 | Dart-board N=ce^(−r²), prose and Figure9
N is called the number of hits at radius r, but the subsequent ring integral multiplies it by area. Therefore N must be an areal expected-hit density, not a count at an exact radius or a radial probability density.
Use ρ(r)=ce^(−r²) hits per unit area, with c≥0 and a specified length scale; expected hits in [r1,r2] are∫ρ(r)2πr dr. If used as probability density, normalize it over the chosen board/domain.
The radial density is2πrce^(−r²), which vanishes at r=0 and has maximum at1/sqrt2 when the domain includes it. Areal density is highest at the center. The source Gaussian graph cannot serve as the radial distribution.

D020-V01 | unstated_plot_normalization | PDF 6 / printed 5 | Figure9 vertical intercept1
The graph is labeled ce^(−r²) but marks its intercept as1.
Interpret the schematic as c=1, or replace the intercept label by c for arbitrary c.
At r=0, ce^0=c. This is a figure-parameter qualification separate from the density terminology issue.

D020-S01 | reviewer_supplementary_annular_integral | PDF 6 / printed 5 | Dart ring formula
The displayed ring integral is correct after interpreting c as density normalization.
For0≤r1<r2, evaluate it as πc(e^(−r1²)−e^(−r2²)).
Substitution u=−r² gives∫2πcr e^(−r²)dr=−πce^(−r²). On the whole plane total expected hits areπc; a probability model on the plane would choose c=1/π. A finite board radiusB instead has c=1/[π(1−e^(−B²))]. These normalizations are independent supplements, not assertions from this page.

Independent mathematical coverage

- Recomputed disk and shell volumes and all radius/height bounds.
- Checked both meter and centimeter numerical examples with an explicit dimensioned curvature coefficient.
- Recomputed heating integral, caloric conversion, mean profile temperature and candy-bar count; distinguished target mismatch from arithmetic.
- Recomputed annulus area limit and pipe-flow integral, units and fixed-c scaling.
- Checked flow figures at center and wall, and Gaussian figure versus areal/radial interpretations.

Technical disposition

Volume and annular integration arithmetic is correct. The temperature profile does not represent the stated uniform100°C goal; the candy-bar result instead fits the imposed profile. Flow assumptions, fixed parameters and units are necessary. The dart example conflates areal density with count/radial likelihood; its ring formula remains correct under the density interpretation.

Limits

- Historical priority claim that Poiseuille was the first person to study pipe flow was read but not independently resolved; no historical certification is claimed.
- No real cauldron energy-efficiency, water-property variation, dietary calibration or empirical dart-distribution validation is asserted.

Primary references consulted

- https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/1a114d602956fa0dd328155f9b45f93d_MIT2_25F13_Couet_and_Pois.pdf | PDF2/printed2, c) Tube Pressure Driven Flow | u(r)=(-dP/dx)(R²−r²)/(4μ) and Q=(-dP/dx)πR^4/(8μ) | retrieved 2026-10-08
- https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter28.pdf | PDF14/printed28-13, §§28.6.1–28.6.2 | Laminar fully developed pipe flow, no-slip wall and Newtonian viscosity assumption | retrieved 2026-10-08
