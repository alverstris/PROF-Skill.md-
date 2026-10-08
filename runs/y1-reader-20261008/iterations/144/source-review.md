D144 source technical review

Displacement Current, Maxwell’s Equations

MIT 8.022 Fall 2004. Official indexed session 24; published PDF title Lecture 19; linked file lecture19.pdf. Identities retained separately. One original PDF, 12 full sheets. Every complete page text and original full-page render personally inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied read-only.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/ece8a047519660f7128c2dea6fcec74d_lecture19.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture19/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D144/source.pdf
SHA256: fa5c60e6aa9e49500acb9ae2d4e54aa7f0db1975809715fbd84c629f1dfbc5ef
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 144, 'active_order': 73, 'queue_selection_evidence': 'Official index labels this row SES # 24: Displacement Current, Maxwell’s Equations.'}

Page, slide and visual coverage

lecture19.pdf, PDF 1, printed sheet 1, slides 1,2: Title Lecture 19; Incomplete Maxwell set and magnetic-divergence interpretation.
lecture19.pdf, PDF 2, printed sheet 2, slides 3,4: Continuity contradiction; Divergence of added term and its nonunique reconstruction.
lecture19.pdf, PDF 3, printed sheet 3, slides 5,6: Displacement-current density; Two spanning surfaces of a charging-capacitor contour.
Slide 6 — capacitor/surface diagram: Current to positive left plate; contour C, flat S through wire and bulged S-prime crossing gap; orientation and source-current content checked.
lecture19.pdf, PDF 4, printed sheet 4, slides 7,8: Flux form of displacement current; Uniform capacitor field and flux derivative.
Slide 7 — repeated capacitor diagram: Positive left plate and E to negative right plate; same contour and bulged gap surface.
lecture19.pdf, PDF 5, printed sheet 5, slides 9,10: RC circuit interpretation; Complete Gaussian/SI Maxwell equations and historical claim.
Slide 9 — RC schematic: Battery, switch, resistor and capacitor loop; no charge conduction across ideal insulating gap.
Slide 10 — two equation columns: Gaussian and SI coefficients, signs and source terms individually checked.
lecture19.pdf, PDF 6, printed sheet 6, slides 11,12: Integral equations and closed/open surfaces; Three historical classroom reasons.
lecture19.pdf, PDF 7, printed sheet 7, slides 13,14: Magnetic field inside charging circular capacitor; Source-free vacuum equations.
Slide 13 — RC schematic: Charging circuit as input to cylindrical gap-field calculation; radius and uniform-field assumptions checked.
lecture19.pdf, PDF 8, printed sheet 8, slides 15,16: Curl-curl derivation for E; Curl-curl derivation for B and one-dimensional wave ansatz.
lecture19.pdf, PDF 9, printed sheet 9, slides 17,18: Chain-rule check with derivative-label error; Right-moving profile.
Slide 18 — two pulse plots: Peak moves from x0 at t0 to x0+1 at t1 for v=1 cm/s; original sign agrees with f(x-vt).
lecture19.pdf, PDF 10, printed sheet 10, slides 19,20: Left-moving profile; Electromagnetic wave speed.
Slide 19 — two pulse plots: Peak moves from x0 to x0-1, agreeing with f(x+vt).
lecture19.pdf, PDF 11, printed sheet 11, slides 21,22: SI speed and numerical units; Demo A4 optical time of flight.
Slide 22 — optical path and scope traces: Beam splitter, nearby short channel2, distant-mirror channel1, two phase-shifted scope traces; long path trace shown later, contradicting prose description of delay.
lecture19.pdf, PDF 12, printed sheet 12, slides 23: Summary; lower half blank.

Findings, conditions and independent derivations

D144-E01 | divergence_free_does_not_imply_closed_field_lines | lecture19.pdf, PDF 1,6, slides 2,11 | Magnetic Gauss law interpretation
The slides equate div B=0 or zero closed-surface magnetic flux with magnetic field lines always being closed. That is too strong.
The equation forbids magnetic charge sources/sinks locally and gives zero net flux through a closed surface; integral curves can be unbounded or nonperiodic rather than closed loops.
A constant nonzero B=B0 z-hat has zero divergence everywhere and straight field lines extending to infinity. This explicit counterexample meets the equation without closed individual lines. Both integral Gauss laws require closed surfaces; an arbitrary open S need not have zero magnetic flux.

D144-C01 | necessary_condition_not_sufficient_for_old_ampere_law | lecture19.pdf, PDF 2, slides 3 | div curl B and continuity
The unamended equation implies div J=0 and hence rho-dot=0. Its wording only when is a necessary condition, but stationary rho alone does not guarantee the displacement term vanishes.
Retain the necessary-condition direction; use full Maxwell equation for time-varying fields, including source-free vacuum with rho=J=0. Smoothness or the distributional versions of the identities are assumed.
Taking divergence gives 0=(4pi/c)div J=-(4pi/c)rho-dot. A transverse source-free wave has rho-dot=0 but E-dot nonzero, so dropping displacement current still fails.

D144-E02 | wrong_divergence_referent | lecture19.pdf, PDF 2, slides 4 | What is F? its divergence must be zero
The prose attributes zero divergence to the new F term; its following algebra correctly requires zero divergence of the entire right side.
For curl B=4pi J/c+F, div F=(4pi/c)rho-dot, generally nonzero. It is div(4pi J/c+F) that vanishes.
Use div J=-rho-dot. Then div F=-(4pi/c)div J=(4pi/c)rho-dot. This agrees with the displayed div(cF)=4pi rho-dot and exposes the local prose error.

D144-G01 | equal_divergence_not_vector_uniqueness | lecture19.pdf, PDF 2, slides 4 | Arrow from div(cF)=div(E-dot) to F=E-dot/c
The inference does not uniquely determine the vector correction. Continuity and Gauss law constrain its divergence only.
F=E-dot/c is the Maxwell choice consistent with this constraint, not a consequence uniquely proved by that algebra. An arbitrary divergence-free G may be added at this stage; physical field equations supply additional content.
div(F-E-dot/c)=0 allows F=E-dot/c+curl A locally (and other solenoidal fields under domain/global conditions). Even a nonzero constant G is a direct counterexample to uniqueness. No boundary condition or extra dynamical law that eliminates G is given.

D144-C02 | displacement_current_and_material_scope | lecture19.pdf, PDF 3,5, slides 5,9 | Not a real current and Kirchhoff wording
Jd=E-dot/(4pi) correctly supplies the Gaussian vacuum/microscopic displacement contribution. No mobile charge crosses an ideal capacitor vacuum gap, but the term is not physically ineffective. The blanket claim that it ensures Kirchhoff laws needs lumped-circuit conditions.
In material macroscopic equations the useful split uses D-dot/(4pi) with free conduction current; in the E/B formulation J includes the appropriate material charges/currents. Charge continuity already explains I=Q-dot at a plate. Changing magnetic flux must still be included in a circuit voltage balance.
For an ideal capacitor, Q=CV implies I=C V-dot without conduction through the gap. Maxwell-Ampere gives surface-independent generalized current; Faraday gives sum of electric line integrals=-PhiB-dot/c, so an unqualified electrostatic zero-EMF loop rule is not restored solely by displacement current. Currents in the metal plates exist while they charge; no current through the plates is shorthand for no conduction across the dielectric gap.

D144-E03 | displacement_flux_alone_not_surface_independent | lecture19.pdf, PDF 4, slides 7,8 | Last equation on slide8
The original image visibly writes integral over S-prime of Jd equal to integral over S of Jd equal to I. The second integrand should be conduction J for the depicted ideal wire surface, or the expression should use total current consistently on both surfaces.
The correct surface-independent flux is integral_S (J+Jd) dot da. In the idealized gap surface J=0 and Id=I; in the wire-cutting surface the leading contribution is conduction current I. Separate Jd fluxes need not agree.
div(J+Jd)=-rho-dot+(1/4pi)div E-dot=0. The divergence theorem proves equal generalized fluxes through equally oriented surfaces with common boundary. Since div Jd=rho-dot, its isolated flux difference equals changing charge enclosed between the surfaces, not generally zero. Uniform ideal-gap E=4pi Q/A gives PhiE=4pi Q and Id=Q-dot=I, as preceding lines correctly state.

D144-H01 | historical_claim_overstates_symmetry_origin | lecture19.pdf, PDF 5, slides 10 | Purely on symmetry claim
The statement that Maxwell introduced displacement current based purely on symmetry is not supported by his own original account. Primary checking found explicit dielectric-polarization and dynamical arguments, as well as a total-current definition.
Qualify this as a modern pedagogical symmetry/consistency motivation, not a literal exclusive historical account. Maxwell 1865 Part I sections11-12 discusses dielectric displacement and changing displacement as current; Part III section55/equationA adds displacement variation to conduction.
Primary reading directly contradicts the exclusivity of purely. This review does not reconstruct the complete chronology or assign priority from this limited check; the later statement that Maxwell was first is not independently established here.

D144-S01 | complete_equations_and_integral_orientation | lecture19.pdf, PDF 5,6,7, slides 10,11,14 | Gaussian/SI and integral systems
All four displayed complete differential equations have consistent signs and coefficients. The integral forms need closed surfaces for Gauss laws and a shared oriented boundary C=boundary S for curl laws.
Gaussian: div E=4pi rho, div B=0, curl E=-B-dot/c, curl B=4pi J/c+E-dot/c. SI replaces electric Gauss coefficient by1/epsilon0, Faraday by-B-dot, Ampere bymu0 J+mu0 epsilon0 E-dot. Flux time derivatives as written assume fixed integration surfaces.
Divergence theorem yields electric/magnetic flux laws; Stokes yields line integrals with orientation fixed by right-hand rule. For moving material circuits the motional u cross B term and changing-surface flux formula must be used. I and Id are scalar oriented fluxes, despite occasional vector-arrow typesetting. Vacuum with rho=J=0 here means source-free vacuum, a stronger condition than merely absence of a material dielectric.

D144-S02 | charging_capacitor_field_and_quasistatic_conditions | lecture19.pdf, PDF 7, slides 13 | B inside circular capacitor
The final B(r,t)=2r Vb exp(-t/RC)/(c a^2 R) follows correctly in the ideal uniform-gap model for r<a. The range, negligible fringe fields and quasistatic approximation are essential.
For circular plates radius a and uniform axial E, Jd=I/(pi a^2). Then Bphi=2I r/(c a^2), with I=(Vb/R)e^(-t/RC) for initially uncharged capacitor switched to a constant battery. The azimuthal sign is the right-hand rule around positive axial generalized current.
2pi r B=(4pi/c)Jd pi r^2. At r=a it joins 2I/(ca); under the same abrupt-uniform-flux idealization, outside r>a gives 2I/(cr). A uniform axial E(t) has zero curl while time-varying B requires a small induced curl of E, so this is a leading quasistatic result, not an exact full-wave solution for arbitrary rapid transients. A characteristic timescale RC large compared with a/c is a sufficient scale separation for that approximation.

D144-S03 | wave_equations_are_necessary_not_complete_maxwell_solution | lecture19.pdf, PDF 8,10, slides 15,16,20 | Uncoupling the equations
Both curl-curl derivations correctly give Laplacian E=E-double-dot/c^2 and the same for B in source-free vacuum. Independently chosen component solutions of those second-order equations need not satisfy Maxwell constraints.
Preserve div E=div B=0 and the paired curl equations/compatible initial data. In one dimension the general scalar homogeneous solution is F(x-ct)+G(x+ct); the source gives individual traveling branches rather than the full superposition.
curl curl E=grad div E-Laplacian E and curl B=E-dot/c give the result. Counterexample E=x-hat F(x-ct), B=0 solves each component wave equation but violates div E=0 for nonconstant F and the curl equations. A valid right-moving pair is E=y-hat F(x-ct), B=z-hat F(x-ct) in Gaussian units; a left-moving branch requires the opposite B sign. This is reviewer supplementary closure, not a derivation supplied on the source slide.

D144-E04 | spatial_second_derivative_mislabeled | lecture19.pdf, PDF 9, slides 17 | Second chain-rule line
The original slide prints d^2 f(x plus/minus vt)/dt^2=f-double-prime(u) in the spatial-derivative row. It should be the second x derivative.
For u=x plus/minus vt, f_t=plus/minus v f-prime, f_tt=v^2 f-double-prime; f_x=f-prime, f_xx=f-double-prime. The final wave-equation identity is correct with that denominator repaired.
The printed t denominator would contradict the preceding correct temporal row for general v and is dimensionally inconsistent. In the profile diagrams x-vt=x0 implies x=x0+vt, while x+vt=x0 implies x=x0-vt; both illustrated translations and 1-cm displacements are correct.

D144-E05 | speed_units_acceleration_typo | lecture19.pdf, PDF 11, slides 21 | Numerical SI wave speed
The slide prints v=2.998 times10^8 m/s^2; the numerical value is a speed and requires m/s. The formula v=1/sqrt(mu0 epsilon0) is correct.
Change only the unit to m/s. The displayed 2004 numerical constants are historical supplied inputs, not a claim about current SI exactness or an independent metrology update.
[mu0 epsilon0]=s^2/m^2, so its inverse square root is m/s. Substitution of epsilon0=8.85418e-12 and mu0=4pi e-7 yields approximately2.997925e8 m/s. Maxwell equations predict wave propagation; identifying observed light as electromagnetic additionally involves empirical comparison, not the scalar differential equation alone.

D144-E06 | time_of_flight_delay_label_reversed | lecture19.pdf, PDF 11, slides 22 | Demo A4 prose versus drawn channels
The diagram and labels designate channel1 as the longer path and channel2 as the shorter. The prose instead calls the116ns delay that of channel2 relative to channel1. The plotted long-path trace is later, consistent with the channel1 label.
With otherwise matched/equal-latency channels, long-path channel1 must lag short-path channel2. The measured delay magnitude, not the reversed verbal ordering, gives the stated positive speed.
DeltaL=2 times17.15m=34.3m; DeltaL/116ns=2.956896552e8m/s, which rounds to2.96e8. This is about1.37percent below nominal2.998e8; no uncertainty budget, detector/electronics calibration or modulation details are supplied, so no further empirical correction or accuracy judgment is justified. This is a reported historical demonstration, not a measurement performed by the reviewer.

Independent coverage

- Complete12-page text and every full original page visually inspected;23slides with lower blank half on final sheet.
- Inspected all Gaussian/SI coefficients, surface/contour drawings, RC circuits, both moving-profile pairs, optical paths and scope timing traces.
- Independently checked continuity divergence, nonuniqueness of vector reconstruction, generalized-current surface invariance and gap magnetic-field approximation.
- Derived both wave equations and corrected chain-rule entries, supplied explicit counterexamples to stronger claims, recomputed speed units and demonstration ratio.
- Targeted primary historical reading performed for the consequential purely-on-symmetry claim; no broader historical or empirical certification.

Technical disposition

Source review complete. Main technical gaps are nonunique divergence reconstruction and confusing displacement-only with total-current surface invariance. Local errors include closed-field-line generalization, zero-divergence referent, a spatial derivative label, speed units and reversed channel-delay wording. Final Maxwell and wave equations are consistent under the recorded assumptions.

Limits

- The alleged Purcell chapter9 equation15 typo lacks edition/page evidence in this packet and was not independently checked; no correction to an unassigned book is asserted.
- Historical priority, complete development chronology and live demonstration accuracy remain outside the inspected packet.
- The original optical demonstration omits electronics timing calibration and measurement uncertainties; source values are verified arithmetically only.
- Source-free plane waves and quasistatic capacitor fields have different approximation requirements; packet alone does not give a complete exact time-dependent capacitor boundary-value solution.

Primary corroboration

James Clerk Maxwell, A Dynamical Theory of the Electromagnetic Field (1865), Part I | https://en.wikisource.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field/Part_I | Sections11-12, with sections9-10 and18 for context; primary paper transcription | retrieved 2026-10-08
Original author describes dielectric polarization, varying displacement and dynamical analogy; used only to qualify the exclusive purely-on-symmetry historical claim.

James Clerk Maxwell, A Dynamical Theory of the Electromagnetic Field (1865), Part III | https://en.wikisource.org/wiki/A_Dynamical_Theory_of_the_Electromagnetic_Field/Part_III | Section55, equation(A), total current; sections69 and73 continuity and limits of mechanical analogy | retrieved 2026-10-08
Primary definition adds time variation of displacement to conduction; original explanatory scope does not amount to a purely symmetric derivation.

