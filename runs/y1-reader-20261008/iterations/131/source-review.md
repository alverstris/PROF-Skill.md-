D131 source technical review

More on Capacitance

MIT 8.022 Fall 2004. Official indexed session 7; published PDF title Lecture 6; linked file lecture6.pdf. These identities are retained separately. One original PDF, 13 full sheets. Every complete text and original full-page render inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/07002b8b4ec36c93c70bfc4697be3789_lecture6.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture6/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D131/source.pdf
SHA256: 0cea3f0bd944685f8079b5ada3ddbbea54af51f56d2ba45ed58bf4cadfc9b571
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 131, 'active_order': 60, 'queue_selection_evidence': 'Official index labels this row SES # 7: More on Capacitance.'}

Page, slide and visual coverage

lecture6.pdf, PDF 1, printed sheet 1, slides 1,2: Printed Lecture 6 title; capacitance and energy recap.
Slide 2 — two conductors: Irregular separated bodies with opposite charges; material dependence is implicit in the recap.
lecture6.pdf, PDF 2, printed sheet 2, slides 3,4: Wimshurst/Leyden jar discussion; Dissectible jar and residual discharge.
Slide 3 — Leyden jar cross-section: Inner and outer conductors separated by an insulating cylindrical wall; labels read.
Slide 4 — disassembled jar: Inner conductor raised from insulating cup and outer conductor; energy explanation needs charge-transfer and work conditions.
lecture6.pdf, PDF 3, printed sheet 3, slides 5,6: Dielectric polarization and increased capacitance; Numerical capacitor energy demonstration.
Slide 5 — polarized molecules between plates: Positive plate left, negative right; dipoles aligned rightward and polarization field opposing applied plate field.
Slide 6 — oil capacitor and wire circuit: Charged oil-filled capacitor connected through a switch and wire; read as a documented demonstration, not performed.
lecture6.pdf, PDF 4, printed sheet 4, slides 7,8: Series and parallel capacitance.
Slide 7 — series network and intermediate node: Two capacitors in series, A/B/C nodes; isolated middle conductor initially neutral, correctly giving equal charge magnitudes.
Slide 8 — parallel network: Both capacitors share the same two terminals; common voltage and additive terminal charge.
lecture6.pdf, PDF 5, printed sheet 5, slides 9,10: Ways to increase capacitance; Twelve-capacitor bank and lamp discharge.
Slide 10 — bank circuit: Parallel capacitor branches, source/switch and lamp; twelve 80 μF units are represented by repeated branches and ellipsis.
lecture6.pdf, PDF 6, printed sheet 6, slides 11,12: Quiz review limitations; Coulomb force and directions.
Slide 12 — two-charge force geometry: Unit vector r̂21 goes from q1 to q2; opposite vector r̂12 is shown.
lecture6.pdf, PDF 7, printed sheet 7, slides 13,14: Discrete and continuous superposition; Charged body with three empty holes.
Slide 13 — point-charge cloud and source volume: Discrete charges around test Q; volume-source arrow appears aimed toward the source, so vector convention is specified algebraically.
Slide 14 — perforated charged body: Three empty circular regions in a charged disk-like drawing, test q outside; no dimensions or 2D/3D density specification is supplied.
lecture6.pdf, PDF 8, printed sheet 8, slides 15,16: Field and potential definitions; External work, path independence and energy.
Slide 16 — three paths: Three curves connect P1 and P2; equal line integrals apply to conservative electrostatic field.
lecture6.pdf, PDF 9, printed sheet 9, slides 17,18: Density-field-potential relationship; Coulomb integral and Gauss symmetry.
Slide 17 — three quantity diagram: ρ, E and φ as alternative data, with a density-to-field arrow.
Slide 18 — Gaussian boundaries: Point source, concentric sphere S1 and irregular enclosing S; radial arrows cross both.
lecture6.pdf, PDF 10, printed sheet 10, slides 19,20: Density to potential; Potential to field and density.
lecture6.pdf, PDF 11, printed sheet 11, slides 21,22: Potential/field continuity claims; Summary of integral and differential relations.
Slide 22 — six-direction relationship diagram: ρ/E/φ triangle: Coulomb potential integral, Gauss integral, line-integral potential difference, gradient, divergence and Poisson relation. All arrow directions and signs checked.
lecture6.pdf, PDF 12, printed sheet 12, slides 23,24: Conductor conditions and nested cylinders; Uniqueness and method of images.
Slide 23 — concentric conductor cross-section: Inner body charged +Q; neutral outer body develops negative inner-face and positive outer-face charge; dashed Gaussian circle lies in outer metal.
Slide 24 — mirror charges and plane: Real positive charge and negative image, with grounded-plane field geometry.
lecture6.pdf, PDF 13, printed sheet 13, slides 25,26: Capacitance/energy recap; Historical quiz scope and next topic.

Findings, conditions and independent derivations

D131-N01 | packet_identity_and_demonstration_wiring_ambiguity | lecture6.pdf, PDF 1,2, slides 1,3 | Numbering and Leyden-jar question
Official session 7 links lecture6.pdf, which prints Lecture 6. Slide 3 refers to two jars but shows one jar and asks about connecting outer and outer surfaces.
Keep official and printed identities separate. The text does not fully specify the two-jar circuit; do not silently replace the words with an inner-to-outer short or infer a unique demonstration outcome.
The complete packet has 13 sheets and 26 slides. The source labels jar conductors and dielectric clearly, but gives neither the full two-jar wiring nor a written answer to the question.

D131-E01 | capacitance_geometry_only_overstatement | lecture6.pdf, PDF 1,3,5,13, slides 2,5,9,25 | Capacitance depends only on geometry
The unqualified claim is false when the medium changes, as the same lecture demonstrates by adding a dielectric.
At fixed geometry, fixed linear dielectric distribution and electrostatic boundary model, C is independent of Q and V. It depends on material permittivity as well as geometry.
A parallel-plate gap completely filled with uniform linear dielectric ε_r has C=ε_r A/(4πd) in Gaussian units or ε0ε_r A/d in SI, versus the vacuum value. Under fixed Q, V and U=Q²/(2C) decrease as C grows; under fixed V, Q and U=CV²/2 increase. These different constraints must be retained.

D131-G01 | dissectible_jar_energy_argument_incomplete | lecture6.pdf, PDF 2, slides 4 | Explanation of residual charge after disassembly
The source invokes the energy increase at fixed Q when C decreases as a reason charge must stay on the dielectric. Energy conservation alone does not force that conclusion: mechanical work during separation can increase field energy.
Distinguish ordinary polarization from actual transfer of charge onto insulating surfaces during high-voltage disassembly. The source provides no measured transfer data or complete mechanism for its apparatus.
At fixed Q, dU=−Q²dC/(2C²); pulling capacitor parts apart can supply positive external work when dC<0. UCSB’s primary demonstration record explicitly describes charge transfer to the dielectric during high-voltage disassembly and warns against interpreting the disassembled state as proof that an ordinary assembled capacitor stores its free charge solely there. This corroborates a possible mechanism, not an inspection of the MIT classroom event.

D131-E02 | dielectric_molecular_symmetry_overstatement | lecture6.pdf, PDF 3, slides 5 | Polarization explanation
Dielectric molecules are not spherically symmetric is not a necessary or universal condition for polarization. Charges are not free to travel through an ideal dielectric, but their bound distributions can deform.
Include induced dipoles in atoms or nonpolar molecules and reorientation of permanent dipoles where applicable. Use the net internal field, not the plate-only 4πσ field, after polarization.
An isotropic bound-charge model with restoring force −kx gives displacement x=qE/k and induced dipole p=q²E/k even if the unperturbed charge cloud is spherical. For a linear medium P=χE, D=E+4πP=ε_rE and D_n=4πσ_free in an ideal filled plate gap, giving E=4πσ_free/ε_r. MIT Haus–Melcher section 6.0 confirms induced dipoles without permanent moments.

D131-S01 | numerical_energy_and_discharge_model | lecture6.pdf, PDF 3,5, slides 6,9,10 | Stored-energy demonstrations
The stated 800 J for 100 μF at 4000 V is correct. The capacitor-bank total and 1:4:9 energy ratio are also correct. Exact energy deposition and visible damage are not determined by capacitance and voltage alone.
The statement that all energy goes into the wire assumes its resistance dominates the other dissipative elements and the circuit transient permits that allocation. Demonstration outcomes need apparatus, resistance/inductance and thermal data absent here.
U=(1/2)(100×10^(-6))(4000)²=800 J. Twelve 80 μF capacitors in parallel give 960 μF, with stored energies 4.8, 19.2 and 43.2 J at 100, 200 and 300 V. In a simple fixed-resistance series model, energy dissipated in one resistor is its fraction R_i/ΣR_j of initial stored energy; this makes the dominance assumption explicit without claiming the actual wire history.

D131-S02 | series_parallel_derivations_verified | lecture6.pdf, PDF 4, slides 7,8 | Capacitor networks
Both equivalent-capacitance formulas and circuit topologies are correct for ideal independent capacitors. The source explicitly states the essential initial neutrality of the isolated middle conductor in series.
Ignore stray/mutual capacitances and leakage. Series equal charge magnitudes require no pre-existing net charge on internal nodes; parallel elements share the same two terminal potentials.
Series: Q=C1V1=C2V2, V=V1+V2, hence 1/C=1/C1+1/C2. A middle-node net charge qB would instead impose Q2−Q1=qB. Parallel: Q=C1V+C2V, so C=C1+C2. The general finite-N formulas follow inductively. For positive C_i, series C is smaller than each member and parallel C exceeds each, a consistency check.

D131-C01 | lamp_fixed_resistance_approximation | lecture6.pdf, PDF 5, slides 10 | Voltage-independent discharge time and power ratio
The claims about unchanged discharge time and ninefold power follow only for a fixed R. A filament lamp changes resistance with temperature, so the same component does not ensure the same resistance throughout different transients.
Treat the claims as an ideal resistor model, not an exact prediction for the real lamp. Time of discharge must also specify a fractional level, since exponential decay never reaches zero at finite time.
With constant R, V(t)=V0 exp(−t/RC), P(t)=V0² exp(−2t/RC)/R, and time to a fixed fraction f is −RC ln f, independent of V0. Time to a fixed absolute threshold depends on V0. A temperature-dependent R(T) couples this electrical ODE to heating; MIT current/resistance notes verify material temperature dependence. No lamp-failure or exact light-duration result is inferred.

D131-C02 | superposition_kernel_and_hole_exercise_conditions | lecture6.pdf, PDF 6,7, slides 12,13,14 | Coulomb law, superposition and perforated body
The Coulomb and superposition formulas are correct for prescribed electrostatic sources. The volume diagram’s separation arrow is ambiguous/opposite to the source-to-test direction. The hole exercise lacks quantitative geometry and density data.
Define R=r_field−r_source and use Q∫ρ(r′)R/|R|³ d³r′. Subtraction of filled holes works for a prescribed charge density, not automatically for an equipotential conductor whose remaining charge redistributes.
For uniform density and disjoint holes H_i inside body B, ρ_actual=ρ0[1_B−Σ1_Hi], so E_actual=E_B−ΣE_Hi exactly. If B and holes are spheres and the test point lies outside each, each field reduces to its center point charge. If the drawing means a planar disk instead, the required kernels/geometries differ. No unsupported numerical force is supplied.

D131-C03 | potential_energy_and_transform_domain_conditions | lecture6.pdf, PDF 8,9,10,11, slides 15,16,17,18,19,20,22 | Field, potential, energy and conversion diagram
All six displayed integral/differential transformations have the correct Gaussian signs. Their domains, reference, boundary conditions and singularities are implicit. The energy identity is the vacuum electrostatic identity; the earlier dielectric discussion requires a material-energy extension.
Use a nonperturbing test charge, quasistatic external work, a conservative field and a convergent infinity reference. An assigned charge density alone needs boundary data to determine φ or E in a region. With a linear dielectric, macroscopic total reversible electrostatic energy is (1/8π)∫E·D, not only ∫E²/(8π).
φ=∫ρ(r′)/|r−r′| d³r′, E=−∇φ, ∇·E=4πρ and Δφ=−4πρ agree for suitable total charge in vacuum. Adding a harmonic potential preserves interior ρ, showing the boundary-data need. In vacuum, ∇·(φE)=−E²+4πρφ gives the energy identity only after the boundary term vanishes. Point-charge self energies diverge; a distinct-pair interaction energy can be negative. Work W_ext=−∫F_C·ds may have either sign.

D131-C04 | gauss_symmetry_scope | lecture6.pdf, PDF 9, slides 18 | Gauss law shortcuts
Gauss law is always true in its domain but not useful without symmetry is too categorical. Constant magnitude on an entire closed surface is sufficient in some cases, but not necessary for standard Gaussian methods.
Symmetry plus boundary conditions lets one extract E from flux. Other surfaces use zero normal flux on some faces and constant normal component on selected faces. Gauss law still supplies constraints without symmetry.
For an infinite charged sheet, a pillbox has nonzero cap flux and zero side flux; the field is not parallel to every outward normal. For a point charge, E=q r̂/r² has zero divergence away from its location yet closed flux 4πq if enclosed. This checks the irregular-surface graphic without confusing local divergence with radial line appearance.

D131-E03 | potential_always_continuous_overstatement | lecture6.pdf, PDF 11, slides 21 | Continuity claim
Potential is always continuous is false without excluding singular sources and ideal dipole layers. It is correct across an ordinary finite surface-charge sheet under the usual electrostatic model.
For a finite single charge sheet, φ is continuous while E_n jumps by 4πσ and tangential E is continuous. At an ideal point charge, φ=q/r diverges and has no finite continuous extension at the source.
Across a vanishing thickness h with bounded one-sided E, Δφ=−∫E_n dn tends to zero even though E_n has a finite jump. By contrast, two oppositely charged sheets separated by h with σh fixed form an ideal dipole layer: a finite potential jump survives as h→0. These are explicit limits of the source assertion, not failures of the ordinary-sheet rule.

D131-E04 | wrong_cylinder_surface_named | lecture6.pdf, PDF 12, slides 23 | Induced −Q location in nested conductors
The bullet says −Q is induced on the inner surface of the inner cylinder. It must be the inner surface of the outer cylinder. The diagram depicts the correct arrangement.
With +Q on the inner conductor, no charge in its empty cavity, and an initially neutral isolated outer conductor, the outer conductor acquires −Q on its inner face and +Q on its outer face.
A Gaussian surface in the outer metal has E=0 and encloses Q+Q_outer,inner=0. Neutrality gives Q_outer,outer=+Q. In the long coaxial model, the gap field is 2(Q/L)r̂/r; outside the entire system the total enclosed charge is +Q, so the exterior field is not zero. Empty interior cavity field is zero. End effects remain excluded.

D131-C05 | uniqueness_and_image_scope | lecture6.pdf, PDF 12, slides 23,24 | Conductor recap and image method
The equilibrium conductor conditions and mirror construction are correct with proper boundary data. A candidate satisfying boundary values alone is not enough; it must solve the same source equation in the domain.
Require zero interior E in electrostatic equilibrium, a signed exterior normal field E_n=4πσ, and a grounded infinite plane with decay at infinity for the displayed image solution.
For Q at y=h, φ=Q/√(s²+(y−h)²)−Q/√(s²+(y+h)²) vanishes at y=0 and has the correct source only in y>0. The image lies outside that domain. The difference from any second admissible solution is harmonic with zero boundary/infinity data and hence zero by uniqueness.

Independent coverage

- Read every complete extracted page and viewed all 13 original full-page renders; covered 26 slides, every circuit, dielectric drawing, arrow and review formula.
- Checked capacitor scaling, all numerical energies and circuit equivalents; separated ideal-resistor mathematics from lamp and wire observations.
- Verified source-to-field kernels, hole subtraction, potential/energy conditions, all six conversion-diagram arrows, continuity limits and induced conductor-surface charge.

Technical disposition

Source review complete. Confirmed overstatements concern geometry-only capacitance, molecular asymmetry and universal potential continuity; the nested-cylinder text names the wrong surface. Demonstration explanations require charge-transfer, work and temperature-dependent material conditions. The core network and electrostatic formulas are correct under the recorded assumptions.

Limits

- No classroom demonstrations E1/E2/E6/E7 were performed or viewed; the packet’s reported outcomes are not independently reproduced.
- The two-jar wiring and perforated-body geometry remain insufficient for a unique numerical prediction. Their published text and diagrams were fully read.
- External primary sources corroborate limited mechanisms; they do not certify the specific historical MIT apparatus or its quantitative transients.

Primary corroboration

UCSB Physics Lecture Demonstration 60.18, Leyden jar | https://web.physics.ucsb.edu/~lecturedemonstrations/Composer/Pages/60.18.html | Explanatory paragraphs on disassembly, HTML lines 14–20 | retrieved 2026-10-08
Primary university apparatus record, opened. Distinguishes charge transfer during sufficiently high-voltage disassembly from ordinary assembled-capacitor charge location. Referenced journal articles were not read.

Haus and Melcher, Electromagnetic Fields and Energy, section 6.0 | https://web.mit.edu/6.013_book/www/chapter6/6.0.html | Induced atomic dipoles, HTML lines 13–20 | retrieved 2026-10-08
Primary MIT textbook, opened. Charges within an initially nonpolar atom can shift relatively and create an induced dipole.

MIT 8.02T Current and Resistance notes | https://web.mit.edu/8.02t/www/802TEAL3D/visualizations/coursenotes/modules/guide06.pdf | PDF page 6, printed 6-6, temperature-dependent resistivity equation 6.2.11; PDF page 7 tungsten row | retrieved 2026-10-08
Primary MIT course text, relevant extracted passage read. Confirms metal resistivity depends on temperature; not used to assert a quantitative thermal model for the lecture lamp.

