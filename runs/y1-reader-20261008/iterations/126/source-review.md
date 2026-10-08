D126 source technical review

Introduction Coulomb’s Law, Superposition Energy of Charge Distributions

MIT 8.022 Fall 2004, lecture 1. One original PDF, 17 full sheet pages, usually two slides per sheet. Every complete extracted text and original full-page image inspected; raster-only text recovered visually where noted. SHA256 independently recomputed and matches audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only; no teaching authoring, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/f59496323e413301a73107db95e40a7e_lecture1.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture1/
Local original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D126/source.pdf
SHA256: df40b1901b5adbabb3199162490d15c22d4af1215fe188f7a2e18e0b5584af7e
Mapping: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 126, 'active_order': 55}

Page, slide and visual coverage

PDF 1/printed sheet 1/slides 1,2: Title, lecturer Gabriella Sciolla and course goals; Gaussian-unit differential Maxwell equations preview.
Slide 2 equation panel: All four vacuum microscopic Maxwell equations in Gaussian units, with4pi rho,4pi j/c and time-derivative1/c factors; inspected directly because panel is not in extracted text.
PDF 2/printed sheet 2/slides 3,4: Raster-only course webpage and staff/meeting information; Lecture Tue/Thu9:30–11; recitations Mon/Wed10–11,11–12 and Tue/Thu2–3,3–4.
Slide 3 homepage screenshot: Course URL and page headings legible; illustrative tiny webpage body is intrinsically blurred. No physics data are encoded there.
Slide 4 staff and meeting tables: Gabriella Sciolla lecturer; Erik Katsavounidis recitations. Table recovered by enlarged original render; historical2004 information.
PDF 3/printed sheet 3/slides 5,6: Purcell volume2 second edition and cgs units; Problem-set schedule, exceptions and collaboration directions.
PDF 4/printed sheet 4/slides 7,8: Grading25% homework/recitations,20% each quiz,35% final; lab requirement; Historical quiz/final dates and invitation for help.
PDF 5/printed sheet 5/slides 10: Blank upper slide slot where9 would be; Mathematics prerequisites and Griffiths chapter1 reference.
PDF 6/printed sheet 6/slides 11,12: Derivative and total differential; Cartesian gradient and displacement; df=grad f dot dl.
PDF 7/printed sheet 7/slides 13,14: Del differential operator and scalar/vector operations; Cartesian divergence definition and interpretation.
PDF 8/printed sheet 8/slides 15,16: Divergence examples+3,0,−3; Point-charge field/source analogy.
Slide 15 three vector plots: Outward linear field(x,y,z), uniform z-hat field and inward linear field(−x,−y,−z).
Slide 16 two charge-field plots: Radial outward/inward arrows at positive/negative charges; local divergence assertion needs source-region qualification.
PDF 9/printed sheet 9/slides 17,18: Curl determinant definition; v=(−y,x,0) and curl=2z-hat.
Slide 18 vector plot: Counterclockwise rotation: right-side arrows upward, top arrows left, lower arrows right; matches positive z curl.
PDF 10/printed sheet 10/slides 19,20: Magnetic wire analogy and nonzero-curl assertion; Section-transition slide.
Slide 19 wire/current/field diagram: Straight wire with current right and circular magnetic-field arrows; curved lines alone do not establish nonzero local curl outside wire.
PDF 11/printed sheet 11/slides 21,22: Historical electricity/magnetism overview and inverse-square precision assertion; Oersted/Ampere, Faraday, Maxwell, Hertz and Einstein chronology.
PDF 12/printed sheet 12/slides 23,24: Fermion overview and force table; Signs of charge, quantization, electron/proton values and conservation.
Slide 23 particle chart: Six quark flavours and six leptons; all labels read.
Slide 23 interaction table: Strong/gluon/10^37/10^−13cm; EM/photon/10^35/infinite; weak/W±,Z0/10^24/10^−15cm; gravity/graviton?/1/infinite. Numerical comparison has no specified energy or particle scale.
Slide 24 demonstration reference: D1,D2,D4 markers denote incidental demonstrations, not additional assigned packet assets.
PDF 13/printed sheet 13/slides 25,26: Coulomb vector force and action–reaction; cgs/SI base and derived quantities, esu dimensional definition and vacuum constants.
Slide 25 two-charge diagram: r-hat21 points fromq1toq2; opposite r-hat12 and force signs consistent.
Slide 26 unit table: cm/g/s/esu/esu per second versus m/kg/s/C/A.
PDF 14/printed sheet 14/slides 27,28: Full cgs–SI conversion table; Discrete superposition.
Slide 27 conversion table: All ten rows read: energy, force, charge, current, potential, E,B,capacitance,resistance,inductance; factors derived below.
Slide 28 charge configuration: Test chargeQ surrounded byN source charges; summed separation vectors directed source-to-test.
PDF 15/printed sheet 15/slides 29,30: Continuous volume/surface/line charge integrals; rho,sigma,lambda definitions.
Slide 29 source-volume diagram: Infinitesimal source cube and externalQ; drawn r arrow appears to point toward source while integral needs source-to-field direction; scalar distance is unaffected.
PDF 16/printed sheet 16/slides 31,32: Uniform rod force on perpendicular bisector; Symmetry, theta substitution and integral.
Slide 31 rod geometry: LengthL horizontal; q distancea above midpoint.
Slide 32 integration geometry: Elementdq=lambda dx, separationr, central normal distancea and angle theta; all labels inspected.
PDF 17/printed sheet 17/slides 33,34: Infinite-rod expansion and limiting force; Binomial formulas and exponential/log/geometric/sin/cos series reminder.
Slide 34 series reference panel: All five series, factorials, start indices and domains read directly; log/geometric |x|<1 and entire exp/sin/cos are correct.

Findings, conditions and independent derivations

D126-E01 | confirmed_scalar_vector_word_error | lecture1.pdf PDF 7/slides 13 | Del operator final bullet
Curl is described as acting on a scalar function, although the displayed symbol is a vector f and later definition is correct.
Replace scalar by vector in this bullet.
In three dimensions curl maps a differentiable vector fieldv to(∂y vz−∂z vy,∂z vx−∂x vz,∂x vy−∂y vx). An ordinary scalar is not an operand for this cross product.

D126-C01 | differentiability_and_coordinate_conditions | lecture1.pdf PDF 1,6,7,8,9/slides 2,11,12,13,14,15,17,18 | Vector-calculus recap
The Cartesian differential, gradient, divergence and curl formulas are correct. Their smoothness/coordinate conditions and finite-change versus differential distinction are implicit.
Assume differentiability for df and sufficient continuous partials for the usual local interpretations. These component expressions use Cartesian orthonormal axes; other coordinates require metric factors. Maxwell preview is in Gaussian units.
Differentiability gives f(r+h)−f(r)=grad f(r) dot h+o(|h|), not an exact proportional finite difference in general. Divergence of(x,y,z) is3, of z-hat is0, of(−x,−y,−z) is−3. Curl(−y,x,0)=(0,0,1−(−1))=2z-hat. The Maxwell panel implies continuity: divergence of curl B=0 gives ∂t rho+div j=0, under commuting derivatives.

D126-E02 | overbroad_local_divergence_claim | lecture1.pdf PDF 8/slides 16 | Electric field around a charge has nonzero divergence
For an isolated point charge the claimed positive/negative divergence is false at ordinary points around the charge. It applies to charge density at the source, not throughout the radial field.
In Gaussian units E=q r/r³ has div E=0 for r>0; at the point charge E is singular and div E=4pi q delta³(r) distributionally. For a smooth density, div E=4pi rho.
For r>0, sum_i ∂i(x_i/r³)=3/r³−3r²/r⁵=0. Flux through a sphere is(q/R²)4piR²=4piq, which identifies the source delta. By contrast the linear outward field on slide15 has div3 everywhere and corresponds to uniform density3/(4pi), not an isolated point charge.

D126-E03 | overbroad_local_curl_claim | lecture1.pdf PDF 10/slides 19 | Magnetic field around a wire: curl B not0
Circular magnetic-field lines around a steady ideal straight wire do not imply nonzero local curl outside the current.
For a long steady wire alongz, B=(2I/c)(−y,x,0)/(x²+y²), and curl B=0 away from the axis; inside a finite wire curl B=4pi j/c. A line current gives a distribution supported on its axis.
Let s²=x²+y². ∂x(x/s²)−∂y(−y/s²)=[s²−2x²+s²−2y²]/s⁴=0. Yet circulation around the wire is4piI/c. A spanning disk meets the singular/current region; this does not contradict Stokes. The slide18 solid-rotation field instead grows with radius and has nonzero curl everywhere.

D126-C02 | empirical_overview_requires_scope | lecture1.pdf PDF 11,12/slides 21,22,23,24 | Historical precision and modern-particle overview
The overview includes a vague inverse-square precision statement, a five-boson count, universal-looking relative strengths/ranges, and an integer-e quantization claim. These require qualifications beyond elementary calculus.
The precision statement is a loose lower benchmark, not a false bound: a1971primary experiment already constrained an exponent deviation near10^−16. The Standard Model covers three interactions, not gravity; a graviton is hypothetical. The five-boson phrase is not a reliable count without species conventions. Integer-e charge applies to ordinary isolated charges; quarks carry fractional charges.
For force strength, Coulomb/Newton ratio is k_e|q1q2|/(Gm1m2), so it changes with particle masses/charges and is not one universal10^35. Quark charges+2e/3and−e/3 give protonuud chargee and neutronudd charge0. The fermion chart itself correctly lists six flavours of each type. The force table can serve as qualitative scale orientation, not a precise universal law; no energy scale is specified. All historical dates were read but no independent history-of-discovery investigation is claimed.

D126-E04 | unit_terminology_error | lecture1.pdf PDF 13/slides 26 | Ampere called a fundamental constant
An ampere is a unit of electric current, not a physical constant. The numerical Coulomb constant and elementary-charge values are rounded and otherwise compatible with the historical units.
Use SI base unit for ampere. The2004definition differs from the present fixed-elementary-charge definition; do not silently interpret old exactness conventions as current ones.
Charge has dimensions force^(1/2)*length in electrostatic cgs:1esu=1cm*sqrt(1dyne). BIPM history records the force-based ampere used in2004; the current definition fixes e=1.602176634e−19C exactly. Rounded e≈1.602e−19C,≈4.803e−10esu and epsilon0≈8.8e−12 are adequate to their stated precision.

D126-S01 | independent_conversion_and_unit_check | lecture1.pdf PDF 13,14/slides 26,27 | All cgs/SI conversion rows
The listed numerical conversions are consistent to their displayed precision under the electrostatic electrical-unit definitions. The note equating the mantissa2.9979... directly with c is shorthand requiring a scale/unit.
Interpret quoted3as2.99792458 and quoted9as its square≈8.98755179 in the historical conventions. Distinguish electrostatic circuit units from Gaussian magnetic units; cgs alone is not a unique electromagnetic convention.
1N=10^5dyn and1J=10^7erg follow from cm=10^−2m,g=10^−3kg. Taking1C≈2.99792458e9esu gives1statV=1erg/esu≈299.792458V;1statV/cm≈2.99792458e4V/m.1F≈8.98755179e11cm.1statohm=statV/(esu/s)≈8.98755179e11ohm has dimension s/cm, and statH=statohm*s has s²/cm.1T=10^4gauss is the conventional magnetic conversion. Here c=2.99792458e10cm/s, not dimensionless2.9979.

D126-C03 | electrostatic_model_and_integral_conditions | lecture1.pdf PDF 13,14,15/slides 25,28,29,30 | Coulomb and superposition formulas
Discrete and continuous formulas are correct in Gaussian electrostatic units(k=1), for prescribed source charges. The general unit vector and singular-source conventions must be fixed.
Use R=r_field−r_source,R-hat=R/|R|; require distinct point sources and a field point away from ideal line/surface singularities unless one-sided limits are specified. Volume integrals need integrable density and convergence. Newton action–reaction here concerns electrostatic pairs, not arbitrary retarded electromagnetic particle forces.
The general expression is F(r)=Q integral rho(r′)(r−r′)/|r−r′|³ d³r′, with analogous surface/line measures. The arrow in slide29 appears opposite to the required source-to-test direction; define R algebraically rather than following that ambiguous graphic. Pair forces negate becauseR_12=−R_21. SI versions restore k_e=1/(4pi epsilon0). A source charge distribution responding to the test charge would need a further model.

D126-E05 | theta_substitution_and_bound_errors | lecture1.pdf PDF 16/slides 32 | Charged-rod solution prose and final integral
The prose writes dx=dtheta/cos²theta, missinga. The displayed final integral integrates dtheta but retains bounds±L/2, which are x bounds. The detailed intermediate algebra and finite-rod final answer are correct.
Use dx=a sec²theta dtheta and angular bounds±alpha with alpha=arctan(L/(2a)). The phrase infinitesimal charge dF should mean force.
For a>0,lambda=Q/L and theta=arctan(x/a), dF_y=lambda q a dx/(a²+x²)^(3/2)=(lambda q/a)cos theta dtheta. Integration gives(2lambda q/a)sin alpha=Qq/[a sqrt(a²+(L/2)²)], directed alongy-hat. Odd x contributions cancel. The result is valid for signedQq with force direction encoded by its sign.

D126-E06 | confirmed_factor_four_error | lecture1.pdf PDF 17/slides 33 | Factoring L/2 out of the rod denominator
After the correct initial fraction, the source replaces the prefactor by lambda q/(2a), and ends with that limit. The correct prefactor is2lambda q/a, four times larger.
For a long rod at fixed linear densitylambda, F≈(2lambda q/a)y-hat. Preserve the earlier exact finite formula; repair every subsequent prefactor on this slide.
Q=lambdaL, so lambdaLq/[a(L/2)sqrt(1+(2a/L)²)]=(2lambda q/a)(1+(2a/L)²)^(−1/2). Expansion yields(2lambda q/a)[1−2a²/L²+6a⁴/L⁴+O(a⁶/L⁶)]. The source first algebraic factoring, not the binomial coefficient−1/2, causes the error.

D126-C04 | limiting_process_and_remainder_conditions | lecture1.pdf PDF 16,17/slides 31,32,33,34 | Infinite-rod limit and Taylor reminders
An infinite rod is taken without saying what is held fixed. Binomial-series domains and the five reminder series are otherwise correct.
Holdlambda fixed asL→infinity. Holding totalQ fixed instead makes this force tend to0. Long-rod accuracy is controlled by2a/L, while the binomial variable is(2a/L)².
With epsilon=(2a/L)²≥0, relative deficit from the infinite-line value is1−1/sqrt(1+epsilon)≤epsilon/2, proving an explicit long-rod error estimate. At a≫L, the finite formula becomesQq/a²[1−L²/(8a²)+...], the point-charge limit. Exponential,sine,cosine expansions are entire in realx; geometric and log series are valid for|x|<1. Binomial identities need|x|<1 unless terminating; source writesx²<1, which is equivalent for realx.

D126-L01 | source_packet_boundary_and_readability_limit | lecture1.pdf PDF 1,2,5,17/slides 1,3,4,10,34 | Original packet identity, raster slide and numbering
The indexed title mentions energy of charge distributions, but this PDF ends with rod forces and Taylor reminders; energy is not developed here. Slide9is a blank slot, and slide3contains an intrinsically blurred illustrative browser screenshot.
Do not invent missing energy content or a slide9lesson. Required mathematics and logistics are recoverable from the published packet. Tiny screenshot body text is not certified as read verbatim; the complete image and enlarged original were inspected.
Lecture1identity is independently aligned across queue,selection,audit and PDFtitle. The four basic Maxwell equations are present visually on slide2 despite text extraction omitting them. Printed sheet pages1–17 and slide numbers1–8,10–34 provide the locators used in this record.

Independent mathematical coverage

- Every original page and every formula/visual/table inspected, including raster page2and the mathematically substantive image panels on slides2and34.
- Derived divergence/curl examples and their singular-source corrections explicitly.
- Re-derived Coulomb vector superposition and the rod force by Cartesian and angular integration, including both limits and error bounds.
- Checked all conversion-table rows dimensionally and numerically to the source precision.
- All four packet PDF hashes were recomputed at intake; this packet hash is recomputed again when saving.

Technical disposition

Source review complete. Consequential confirmed defects include the scalar/vector curl wording, overbroad point-source divergence and wire-curl assertions, rod substitution/bounds, and a factor-four long-rod error. Particle/unit overview qualifications and finite-domain assumptions are distinguished from source errors.

Limits

- Tiny body text of the historical homepage preview on slide3remains intrinsically blurred and is not claimed verbatim recovered; it is incidental, not required technical content.
- Historical dates and force-strength table lack detailed sourcing/scale; no comprehensive history audit or exact universal strength validation is claimed.
- CERN Open Data quark glossary was retrieved as a primary search result; the ATLAS alternative returned403 and is not treated as read.

Primary corroboration

CERN Standard Model | https://home.cern/science/physics/standard-model/ | Matter particles; Forces and carrier particles | retrieved 2026-10-08
Corroborates six quark/lepton flavours, three Standard Model interactions and hypothetical graviton.

CERN Open Data Quark glossary | https://opendata.cern.ch/glossary/Quark | Quark definition | retrieved 2026-10-08
Primary institutional corroboration of fractional quark charges.

BIPM ampere and historical perspective | https://www.bipm.org/en/si-base-units/ampere | SI base unit ampere; historical companion https://www.bipm.org/en/history-si/ampere | retrieved 2026-10-08
Distinguishes unit from constant and current fixed-e definition from historical force-based unit.

Williams,Faller,Hill1971 Coulomb-law test | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.26.721 | Abstract, Physical Review Letters26,721 | retrieved 2026-10-08
Published exponent deviation(2.7±3.1)e−16 corroborates that better than2e−9 is a loose benchmark; full subscription article not inspected.

