D146 source technical review

Radiation (cont.) Polarization, Poynting Vector: Energy, Power and Momentum of Radiation

MIT 8.022 Fall 2004. Official indexed session 26; published PDF title Lecture 21; linked file lecture21.pdf. Identities retained separately. One original PDF, 11 full sheets. Every complete page text and original full-page render personally inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied read-only.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/2f5efba0b9926c9ce8e9ab0d04bfc7b3_lecture21.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture21/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D146/source.pdf
SHA256: 2a9f4078384b3643c87bd32f0e9caa95e5384651b71a17444b87679d261a60b9
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 146, 'active_order': 75, 'queue_selection_evidence': 'Official index labels this row SES # 26: Radiation (cont.)\n\n\nPolarization, Poynting Vector: Energy, Power and Momentum of Radiation.'}

Page, slide and visual coverage

lecture21.pdf, PDF 1, printed sheet 1, slides 1,2: TitleLecture21; Plane-wave/polarization recap.
lecture21.pdf, PDF 2, printed sheet 2, slides 3,4: Vacuum field energy; Poynting derivation.
Slide 3 — closed-volume sketch: Arbitrary V bounded by A containing E/B; outward-surface convention checked.
lecture21.pdf, PDF 3, printed sheet 3, slides 5,6: Energy flux interpretation; Dimensions and intensity.
lecture21.pdf, PDF 4, printed sheet 4, slides 7,8: Plane-wave flux; Oscillating electric-dipole far field.
Slide 8 — dipole axis drawing: Positive/negative charge pair along z with angular radiation formulas.
lecture21.pdf, PDF 5, printed sheet 5, slides 9,10: Integrated dipole power; Charging-capacitor inflow.
Slide 9 — spherical surface/dipole: Sphere centered on z-directed dipole; radius and angular integration checked.
Slide 10 — charged plates and current: Upper positive plate, lower negative plate, charging current downward through gap in generalized-current sense; right-handed cylindrical signs checked.
lecture21.pdf, PDF 6, printed sheet 6, slides 11,12: Radiation momentum/pressure; Flux-density summary table.
Slide 12 — energy/momentum table: Every scalar/vector density and flux entry checked; plane-wave scope versus general fields recorded.
lecture21.pdf, PDF 7, printed sheet 7, slides 13,14: Distributed LC ladder and match; Coax impedance and speed.
Slide 13 — two LC ladder diagrams: Single series inductor/shunt capacitor terminatedR, then repeated infinitesimal sections; frequency-order approximation checked.
Slide 14 — coax section: Nested cylindrical conductors with a,b radii; unit convention and dielectric assumptions checked.
lecture21.pdf, PDF 8, printed sheet 8, slides 15,16: Transmission-line demo; Atmospheric scattering geometry.
Slide 15 — scope/pulse/spool wiring: Ch1/Ch2, split trigger/pulse source, cable reel and terminal location; total path and reflection limitations recorded.
Slide 16 — sun/atmosphere/observer: Incident z direction and observed x direction in orthogonal triad; ideal90degree single-scattering geometry.
lecture21.pdf, PDF 9, printed sheet 9, slides 17,18: Scattered polarization; Rayleigh frequency scaling.
lecture21.pdf, PDF 10, printed sheet 10, slides 19,20: Summary; Sunset experiment.
Slide 20 — tank/screen illumination: Light enters from right toward screen left; blue side scattering and transmitted red beam illustrated; chemical description checked.
lecture21.pdf, PDF 11, printed sheet 11, slides 21: Optical activity of sugar; lower half blank.
Slide 21 — polarizer/tank/analyzer diagram: First polarizer right, sugar cell, analyzer left, then wall; propagation and wavelength-dependent rotation inspected.

Findings, conditions and independent derivations

D146-E01 | poynting_cross_product_reversed | lecture21.pdf, PDF 2,3,6, slides 4,5,12 | Initial definition, divergence line and summary table
The source defines S=c(B cross E)/(4pi) in slides4,5 and12, reversing the correct order. Its detailed vector identity and later slides6-10 use E cross B. The red divergence term on slide4 also reverses E/B.
Use S=c(E cross B)/(4pi) throughout and dU/dt=-integral_closedA S dot da in a fixed source-free volume.
With u=(E^2+B^2)/(8pi), u_t=(c/4pi)[E dot curl B-B dot curl E]=-div[c(E cross B)/(4pi)]. For E=x-hat F(z-ct), B=y-hat F(z-ct), energy propagates+z; B cross E would point-z. This direct counterexample fixes the sign independently of labels.

D146-C01 | energy_theorem_sources_and_surface_theorem | lecture21.pdf, PDF 2,3, slides 3,4,5,6 | Vacuum derivation and Stokes label
The no-source energy balance is correct after cross-product repair. Vacuum alone does not exclude current; if charges/currents are present, field energy can be transferred to matter. The volume-divergence to closed-surface-flux step is labeled Stokes but is specifically the divergence/Gauss theorem.
General vacuum/microscopic balance is u_t+div S=-J dot E. For a fixed volume, dUfield/dt=-outward flux-integral J dot E. Intensity is normally the time-averaged normal energy flux for a beam, not energy density.
Substitute E_t=c curl B-4pi J and B_t=-c curl E into u_t. Units ofS are erg/(s cm^2), equivalently power/area. Oblique flux is S dot n, so a bare magnitude is not every surface-normal irradiance. Material effective energies and fluxes require constitutive/dispersion assumptions not given here.

D146-E02 | plane_wave_cosine_squared_replaced_by_sine_squared | lecture21.pdf, PDF 4, slides 7 | Instantaneous plane-wave S and u
The input fields are both cos(kz-omega t), but their product and squared energy are printed sin^2. This is an inconsistent phase substitution within the same example; its averaged formulas are unaffected. The prose also calls averageS an average energy density.
For the displayed fields use S=cE0^2 cos^2 psi z-hat/(4pi), u=E0^2 cos^2 psi/(4pi); then S=cu z-hat. Their averages are cE0^2/(8pi) and E0^2/(8pi), respectively.
At psi0 the source fields are maximal, so a sin^2 energy would incorrectly vanish. Averaging either squared sinusoid gives1/2, explaining why final mean intensity is correct. S is flux, u is energy per volume. The relationS=cu n requires a single traveling vacuum wave, not arbitrary fields.

D146-S01 | dipole_radiation_field_and_power | lecture21.pdf, PDF 4,5, slides 8,9 | Given far fields and angular integration
The displayed radiation fields and mean total power p0^2 omega^4/(3c^3) are consistent for an electrically small nonrelativistic harmonic electric dipole in vacuum, with p0 the peak dipole moment. The source states far-zone r much greater thanlambda, but the next slide merelyR much greater thand does not replace that requirement.
Retain source size d much smaller thanlambda and observation r much greater thanlambda andd. Fields are the transverse1/r terms, not the complete near field. Call positive outward flux Prad; do not confuse it with the time derivative of stored field energy inside the sphere.
For p(t)=p0 z-hat sin omega t, E_rad=n cross(n cross p-double-dot(t-r/c))/(c^2r)=theta-hat p0 omega^2 sin theta sin(kr-omega t)/(c^2r), B=n cross E. Thus meanS=p0^2 omega^4 sin^2 theta n/(8pi c^3r^2). Angular integral2pi integral0^pi sin^3 theta dtheta=8pi/3 yieldsPrad. Instantaneous dipole result2|p-double-dot|^2/(3c^3) cycle-averages to that value. Radius independence is the averaged far-zone outgoing power; source work and retarded timing still matter in a full energy balance.

D146-E03 | charging_capacitor_magnetic_sign | lecture21.pdf, PDF 5, slides 10 | Bphi and E cross B calculation
For the depicted upper+Q, lower-Q capacitor and positive charging I=dQ/dt, E=-4Q z-hat/a^2. The source prints B=+2Ir phi-hat/(ca^2), which has the wrong sign in standard right-handed cylindrical coordinates. It then drops E minus sign in the product to obtain the physically correct inwardS.
Correct B=-2Ir phi-hat/(ca^2). Then both negative signs cancel and z-hat cross phi-hat=-r-hat, giving S=-2IQr r-hat/(pi a^4). The final inward direction and magnitude are right after the intermediate signs are repaired.
E-dot is down, so generalized current is down and right-hand-rule B is-phi. For gapd and r=a, inward power=-integralS dot da=(2IQ/(pi a^3))(2pi ad)=4IQd/a^2=I Vcap, sinceVcap=4Qd/a^2. Stored electrostatic energyU=2Q^2d/a^2 has derivative4IQd/a^2. Uniform small-gap/quasistatic approximation and r<a apply; higher-order changing magnetic-energy/induced-E terms are omitted.

D146-C02 | momentum_and_pressure_require_direction_and_boundary | lecture21.pdf, PDF 6, slides 11,12 | Massless relation and momentum-flux table
p=U/c applies to collinear unidirectional radiation or each photon, not arbitrary total radiation. Dimensional analysis suggests pressure units but does not establish a universal pressureS/c for every boundary. The summary table conflates a directed beam with general fields.
For a single vacuum traveling beam, momentum densityg=S/c^2=u n/c and momentum transport tensorPi_ij=u n_i n_j. Normal-incidence perfect absorption gives pressureI/c; perfect reflection gives2I/c. Net pressure depends on incident and outgoing momentum.
Two equal counterpropagating beams have positive totalU but zero total momentum, directly disproving unconditionalp=U/c for their aggregate. General vacuum fieldg=S/c^2 is valid, while u is(E^2+B^2)/(8pi), not generally|S|/c: 2|E cross B|<=E^2+B^2, with equality requiring perpendicular equal-magnitude fields. Momentum flux generally needs tensorPi_ij=u delta_ij-(EiEj+BiBj)/(4pi), not merely vectorS/c. No specific pressure demonstration is supplied or certified.

D146-S02 | distributed_lc_matching_and_omitted_factors | lecture21.pdf, PDF 7, slides 13 | Ladder recursion
The final R=sqrt(L-prime/C-prime) is correct for an ideal lossless uniform transmission line in the continuum limit. The first displayed impedance term is just i, missing omegaL, although the next equality restores it. Dropping theLC term needs explicit infinitesimal-section scaling.
For a sectiondelta x, useL=L-prime delta x,C=C-prime delta x. ThenZeq=i omega L+(1/R+i omega C)^(-1). RequiringZeq=R gives i omegaL-omega^2LCR=i omegaCR^2; discardO(delta x^2), not a potentially large arbitrary finiteLC product.
At first order L-prime=C-prime R^2, henceZ0=sqrt(L-prime/C-prime)>0. Telegraph equationsV_x=-L-prime I_t andI_x=-C-prime V_t implyv=1/sqrt(L-prime C-prime). Distributed resistive/conductive losses or dispersion give frequency-dependent complex characteristic impedance; a single real match then is not guaranteed.

D146-S03 | coax_formula_units_and_scope | lecture21.pdf, PDF 7, slides 14 | Coax homework result
Z0=2ln(b/a)/c andv=c are Gaussian-unit vacuum, ideal-conductor TEM results, not a generic dielectric-filled coax speed or a number directly in ohms. The50ohm note uses SI resistance.
For vacuum coax, C-prime=1/[2ln(b/a)], L-prime=2ln(b/a)/c^2 in this Gaussian inductance convention. In SI, C-prime=2pi epsilon/ln(b/a), L-prime=mu ln(b/a)/(2pi), Z0=sqrt(mu/epsilon)ln(b/a)/(2pi), v=1/sqrt(mu epsilon).
Gauss givesE_r=2lambda/r in Gaussian units; V=2lambda ln(b/a). Ampere givesB_phi=2I/(cr); magnetic energy per length=(1/8pi)integral_a^b B^2 2pi r dr=I^2 ln(b/a)/c^2=(1/2)L-prime I^2. ProductL-prime C-prime=1/c^2. In vacuum SI Z0 is approximately60ln(b/a)ohm, so50ohm corresponds to b/a approximately2.30; that conditional example does not identify the actual demo cable geometry or dielectric.

D146-C03 | termination_reflection_and_demo_path_ambiguity | lecture21.pdf, PDF 7,8, slides 14,15 | Mismatch claim, open/short and timing
A matched lossless line has inputZ0 independent of length/frequency; mismatch can cause reflections and frequency-dependent input impedance. Distortion is not unavoidable for every monochromatic signal. The timing prose says back and forth while computingv=L/T fromL=127.4m andT=656ns.
The given quotient is1.942073171e8m/s, about0.648c, reasonably described as roughly2c/3. It requires127.4m to be the total relevant propagation path. If it instead means a one-way length with a complete round trip, the formula needs2L/T, inconsistent with the stated result. The simplified wiring does not settle that ambiguity.
For realZ0, voltage reflectionGamma=(ZL-Z0)/(ZL+Z0): open+1, short-1, match0. Current reflection has opposite sign. Zin=Z0(ZL+iZ0 tan beta l)/(Z0+iZL tan beta l), reducing toZ0 on match. A matched load does not send a reflected pulse back; return-conductor current is part of a traveling transmission mode, not by itself a reflected signal. The source descriptions of other/return cables lack enough topology/calibration to infer exact scope traces. No invented wiring correction or empirical speed claim is made.

D146-S04 | single_scattering_polarization | lecture21.pdf, PDF 8,9, slides 16,17 | Incidentz, observedx geometry
The predicted y polarization is correct for ideal single Rayleigh scattering by isotropic induced electric dipoles at90degrees. It is not implied merely by requiring both incoming and outgoing waves transverse; the source needs the dipole-response/projection link.
Let incidentE=Ex x-hat+Ey y-hat, inducedp=alpha E. Radiation observed alongx projects out thex component and preservesy, giving the stated direction. Rotating an incident linear polarizer varies that Ey amplitude and can extinguish the idealx-directed scattered field.
Radiation amplitude is proportional to n cross(n cross p); for n=x-hat the incidentx component giveszero andy gives a y-directed field up to an overall sign. Multiple scattering, anisotropic polarizability, finite angles and other particles reduce the ideal polarization. The source itself notes multiple scattering, and no unconditional real-sky100percent polarization is asserted.

D146-C04 | rayleigh_scaling_and_color_ratio | lecture21.pdf, PDF 9, slides 18 | Frequency-to-the-fourth argument
The omega^4 orlambda^-4 intensity scaling assumes induced-dipole amplitude is approximately frequency-independent for equal incident intensity and fixed geometry. Molecular polarizability is generallyalpha(omega); resonances, finite particle size and multiple scattering lie outside this simple rule.
More fullyIscat is proportional toomega^4|alpha(omega)|^2Iincident times angular/distance factors, in the electrically small Rayleigh regime. If two chosen wavelengths have ratio2, the ideal scattering ratio is16. The packet does not specify actual red/blue wavelengths, so16 is a conditional illustration, not a universal measured color ratio.
Two time derivatives giveomega^2 p0; squaring givesomega^4|p0|^2. Withp0=alpha E0 the omitted dependence is explicit. A longer atmospheric path suppresses more short-wavelength direct light, while short wavelengths contribute strongly to side-scattered light. Source spectrum, wavelength definitions, human response and aerosols are not computed here; no newly invented empirical color correction is supplied.

D146-C05 | sunset_chemistry_incomplete_and_particle_description | lecture21.pdf, PDF 10, slides 20 | Water/salt and sodium-thiosulfate account
The source attributes the evolving scattering to bigger molecules after adding sodium thiosulfate to unspecified water/salt. It gives no acid/reactant details, and its printed hydrate string Na2S2O335H2O is malformed. The depicted effect alone cannot establish what was actually mixed in this2004 demonstration.
Primary UCSB documentation of the analogous standard demonstration identifies acid-induced colloidal sulfur precipitation and subsequent particle growth, not merely enlarged dissolved molecules. This is corroboration of the physical explanation and an omitted-condition warning, not evidence of the exact historical MIT recipe.
The documented net reactionS2O3^2-+2H+ -> S(s)+SO2+H2O conserves atoms/charge. Growing sulfur particles first preferentially scatter shorter wavelengths; the eventual optically thick/multiple-scattering state is not the same simple single-Rayleigh regime. No recipe/procedure or experimental claim is authored, and generic salt is not assumed to mean an acid. The light is polarized note requires viewing direction and scattering conditions, not all emergent light100percent polarized.

D146-S05 | optical_activity_phase_derivation | lecture21.pdf, PDF 11, slides 21 | Sugar solution/circular decomposition
The stated circular-birefringence mechanism is consistent for an optically active medium where right/left circular modes propagate with different phase constants and comparable amplitudes. The optical train matches the MITT8 primary apparatus description.
Equal circular components with kR,kL acquire phase differenceDelta=(kR-kL)ell; the linear-polarization axis rotates byDelta/2 up to handedness convention. Wavelength-dependent index difference gives wavelength-dependent rotation, and the second polarizer analyzes the result.
Writing eR=(x-hat+i y-hat)/sqrt2,eL=(x-hat-i y-hat)/sqrt2, equal fields sum afterlength ell to exp(i kbar ell)[x-hat cos(Delta/2)-y-hat sin(Delta/2)] times a common oscillatory factor. Unequal attenuation of the two modes produces ellipticity, not purely linear rotation. The rotation is with propagation distance for fixed monochromatic light, not a slow time rotation at a stationary point. The source provides no concentration/length/index data for a numerical angle. The consulted MIT apparatus page corroborates only the setup and wavelength-dependent rotation; unrelated explanatory assertions there were not adopted.

Independent coverage

- Read all11complete text pages and personally viewed all11full original renders/21slides.
- Inspected energy-flux signs, complete table, dipole field/area geometry, capacitor orientation, ladder/coax circuits, scope wiring and all scattering/optical diagrams.
- Derived Poynting theorem including J dotE, corrected instantaneous phase and capacitor signs, integrated dipole power and derived beam momentum boundaries/general tensor limits.
- Derived continuum line impedance/velocity, coax per-length constants, reflection coefficients and timing quotient; retained unresolved path topology honestly.
- Derived Rayleigh polarization/scaling and circular-birefringence rotation; targeted primary apparatus research resolved mechanism uncertainty without claiming a live or historical measurement.

Technical disposition

Source review complete. Confirmed errors are repeated reversed initial Poynting products, a cosine/sine-square mismatch, capacitor intermediate magnetic/product signs and a missing impedance factor. Final dipole power, corrected capacitor inflow and ideal transmission-line match are consistent. Momentum tables, radiation pressure, Rayleigh scaling and demonstrations require the recorded model/geometry conditions.

Limits

- The historical transmission-line demo does not specify whether127.4m is a total travel path or one-way path despite back-and-forth wording; exact wiring and timing calibration remain unresolved.
- The original sunset mixture is not fully specified. Analogous primary apparatus evidence supports an acid/colloidal-sulfur mechanism but cannot reconstruct the actual2004 mixture or particle distribution.
- No radiation-pressure, transmission-line, sunset or sugar demonstration was performed; source empirical descriptions are not independently measured.
- Source polarization/energy recap assumes traveling vacuum plane waves; no general arbitrary-field transversality or|S|/c energy identity is certified.

Primary corroboration

UCSB Physics Lecture Demonstrations,84.45 Sunset | https://web.physics.ucsb.edu/~lecturedemonstrations/Composer/Pages/84.45.html | Opening apparatus description, acid decomposition equation, sulfur-particle growth and side-scattered polarization | retrieved 2026-10-08
Primary operator documentation of an analogous sunset demonstration; establishes colloidal-sulfur mechanism and missing reaction condition, without identifying the historical MIT mixture.

MIT Physics Instructional Resources Lab, Polarization in a Sugar Solution(T8) | https://pirl.mit.edu/demo/T_8.html | Description; Materials; optical alignment instruction, first23lines | retrieved 2026-10-08
Primary MIT apparatus record corroborates source polarizer-sugar-analyzer arrangement and wavelength/path/concentration-dependent rotation only.

