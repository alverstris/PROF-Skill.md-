D132 source technical review

Current, Continuity Equation Resistance, Ohm’s Law

MIT 8.022 Fall 2004. Official indexed session 8; published PDF title Lecture 7; linked file lecture7.pdf. These identities are retained separately. One original PDF, 9 full sheets. Every complete text and original full-page render inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/fa6d8a67e9e53df0e2cbaed7b755b07a_lecture7.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture7/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D132/source.pdf
SHA256: 6d9dc979afd3cb0d057ffd03dd7a181c4619ae8cdfcca3a1200d07a74fa0578a
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 132, 'active_order': 61, 'queue_selection_evidence': 'Official index labels this row SES # 8: Current, Continuity Equation\n\n\nResistance, Ohm’s Law.'}

Page, slide and visual coverage

lecture7.pdf, PDF 1, printed sheet 1, slides 1,2: Printed Lecture 7 title; Current through a surface; units.
Slide 2 — moving charge cylinder: Parallel carrier velocities cross a wire section; current is signed charge flux.
lecture7.pdf, PDF 2, printed sheet 2, slides 3,4: Current density and oblique area; Multiple carriers, averaging and general surface flux.
Slide 3 — cylinder and oblique swept prism: Carrier motion uΔt, tilted area vector A and angle θ; volume A cosθ uΔt checked.
lecture7.pdf, PDF 3, printed sheet 3, slides 5,6: Ionic current example; Integral and differential continuity equation.
Slide 5 — electrolyte circuit: Left positive electrode, right negative electrode; drawn Cl− arrow right and Na+ arrow left are reversed for electric drift.
Slide 6 — closed control surface: Several J arrows enter and leave; outward area convention fixes minus sign in accumulation law.
lecture7.pdf, PDF 4, printed sheet 4, slides 7,8: Steady continuity; Local Ohm law; visible draft placeholder.
Slide 7 — control surface recap: Same inward/outward flux illustration; zero divergence means no local accumulation.
lecture7.pdf, PDF 5, printed sheet 5, slides 9,10: Uniform-wire resistance; Resistance dimensions and geometry.
Slide 9 — uniform wire: Area A, length L, current density J and field E parallel to axis.
lecture7.pdf, PDF 6, printed sheet 6, slides 11,12: Resistivity and material table; Temperature dependence and residual resistivity.
Slide 11 — eight-row numerical table: Silver, copper, gold, iron, seawater, polyethylene, glass and fused quartz: both SI and CGS values read, including enlarged original-PDF crop.
Slide 12 — schematic resistivity curve: Nonzero flat low-T residual plateau and rising high-T branch; no numerical axes or superconducting drop shown.
lecture7.pdf, PDF 7, printed sheet 7, slides 13,14: Radial conduction between concentric spheres; Interface charge in a two-material wire.
Slide 13 — spherical resistor: Inner radius a at V, outer b at zero; resistive annulus and ground symbol.
Slide 14 — two-section conductor: Equal-area cylinder with conductivities σ1 and σ2, axial current crosses material interface.
lecture7.pdf, PDF 8, printed sheet 8, slides 15,16: Drude drift interpretation; Momentum averaging and collision time.
Slide 15 — scattering path: Zigzag trajectory among fixed lattice sites in rightward E; schematic classical scattering, not literal full solid-state physics.
lecture7.pdf, PDF 9, printed sheet 9, slides 17: Single- and multiple-carrier conductivity; lower half blank.

Findings, conditions and independent derivations

D132-N01 | identity_and_draft_notation | lecture7.pdf, PDF 1,4,5,9, slides 1,8,10,17 | Numbering and minor editorial defects
Official session 8 links lecture7.pdf, printed Lecture 7. Slide 8 retains a draft note More stuff here please. Slide 10 calls R the proportionality constant between V and R, and slide 17 sums over i while its summand uses k.
Retain the identity offset. The proportionality is V=RI between voltage and current. Use one carrier index consistently in σ=Σ_k n_k q_k²τ_k/m_k. The draft note is visible source content, not an instruction to author missing material.
All nine sheets and 17 slides are present. The correctly displayed equations disambiguate both minor notation slips.

D132-S01 | current_density_and_units_verified | lecture7.pdf, PDF 1,2, slides 2,3,4 | Current and current density
The swept-volume derivation, species sum and general surface integral are correct. Charge density ρ here must not be confused with the later resistivity symbol ρ.
Use I=dQ_crossed/dt with a chosen surface normal; it is not automatically the time derivative of charge contained in a region. J=ρu applies to a single carrier population, while multiple populations need Σρ_k〈u_k〉.
In time Δt, the swept volume is A(u·n)Δt, so I=qn u·A. Summing species gives J=Σn_kq_k〈u_k〉. Opposite charges moving oppositely contribute the same conventional current direction. Thus a nearly neutral conductor can have nonzero J despite total ρ≈0. The source current conversion 1 A≈2.998×10^9 statC/s is correct.

D132-E01 | ionic_drift_arrows_reversed | lecture7.pdf, PDF 3, slides 5 | NaCl-solution diagram
The left electrode is labeled positive and the right negative, giving rightward applied E, but Na+ is drawn moving left and Cl− right.
For electric drift in the illustrated field, Na+ should move right toward the negative electrode and Cl− left toward the positive electrode.
F=qE gives the two opposite directions immediately. Under positive mobilities, both species contribute conventional current rightward because q and velocity both reverse for the anion. The figure cannot be reconciled with the stated simple field-driven drift model by merely switching the conventional-current sign.

D132-C01 | continuity_regular_control_volume_conditions | lecture7.pdf, PDF 3,4, slides 6,7 | Charge conservation
The outward-flux minus sign and final continuity equation are correct. The volume integral is printed with a closed-contour integral glyph; it means an ordinary volume integral.
Use a fixed spatial control volume and sufficiently regular densities/current for the classical pointwise derivation; distributional conservation covers surface accumulations. Steady state means ∂tρ_charge=0, not ρ_charge=0.
Q_V=∫_Vρ_charge dV and dQ_V/dt=−∮J·n dA. Divergence theorem and arbitrariness of V give ∂tρ_charge+∇·J=0. For a moving boundary with velocity v_b, the transported flux is J−ρ_charge v_b; that is outside the displayed fixed-volume argument.

D132-C02 | ohmic_material_model_and_resistance | lecture7.pdf, PDF 4,5,6, slides 8,9,10,11 | Ohm law and resistivity meaning
J=σE and R=L/(σA) are valid for the stated uniform scalar Ohmic model, not every conductor at every field, temperature or frequency. Resistivity does not by itself specify electron speed.
Assume isotropic linear response at fixed material state, uniform cross-section and negligible contact/end effects. Define V as the positive drop along conventional current. Anisotropic media need a tensor conductivity; nonlinear response and heating can invalidate constant R.
For uniform axial field, V=EL and I=JA=σEA, yielding V=IR. Units are Ω in SI and s/cm in electrostatic CGS; resistivity is Ω·m or s. In a single-carrier model drift speed is J/(n|q|), whereas thermal/Fermi motion is a different quantity. Conductivity depends on both carrier density and mobility.

D132-E02 | confirmed_factor_ten_cgs_resistivity_table_error | lecture7.pdf, PDF 6, slides 11 | Complete SI/CGS material table
Every CGS-second entry is approximately ten times too large relative to the corresponding SI Ω·m entry under the lecture’s stated esu units. The enlarged original render confirms the printed powers.
For the displayed SI values, corrected CGS values are: silver 1.78×10^(-18) s; copper 1.89×10^(-18); gold 2.67×10^(-18); iron 1.11×10^(-17); seawater 2.23×10^(-11); polyethylene 22.3; glass approximately 1.11×10²; fused quartz 8.34×10^7. Source rounding can then be applied.
One statV/cm = 2.99792458×10^4 V/m; one statA/cm² = 3.33564095×10^(-6) A/m². Thus one CGS resistivity second = 8.98755179×10^9 Ω·m, so ρ_cgs[s]=ρ_SI[Ω·m]/(8.98755179×10^9). The printed column reads 1.8e−17, 1.9e−17, 2.6e−17, 1.1e−16, 2.2e−10, 220, ~1e3, 8.3e8. This conversion check does not claim the underlying material values are universal without temperature/composition data.

D132-C03 | temperature_superconductivity_and_scattering_scope | lecture7.pdf, PDF 6,8, slides 12,15 | Temperature graph and microscopic explanation
The plateau/rising curve is a qualitative normal-metal picture. Some metals become superconducting is true, but sufficient purity alone is not a general criterion or an explanation. Electrons bump into nuclei is a classical cartoon, not a literal complete transport mechanism.
Normal-metal resistance can include temperature-dependent lattice-vibration scattering and residual defect/impurity scattering. Superconductivity is a distinct phase subject to material and critical temperature/field/current conditions. Do not infer all purer metals superconduct or all conductors have the drawn T dependence.
The TU Delft primary course explicitly separates phonon and defect scattering in a crystal and gives the relaxation-time model. CERN documents superconducting critical conditions and superconducting Nb–Ti alloy, demonstrating why purity is not a universal condition. The source schematic has no quantitative T law and does not show a superconducting transition; none is fitted or invented.

D132-S02 | spherical_resistor_derivation_verified | lecture7.pdf, PDF 7, slides 13 | Concentric spherical conduction
The printed potential, radial field, current and resistance are correct. Spherical symmetry alone does not establish φ=A+B/r; steady current and constant conductivity supply the needed Laplace equation.
Assume a<b, homogeneous isotropic σ>0, steady conduction, equipotential spherical electrodes at V and zero, and no additional sources in the shell.
∇·J=0 and J=−σ∇φ give Δφ=0. Radially, (r²φ′)′=0, so φ=A+B/r. Boundary data give φ=V[ab/((b−a)r)−a/(b−a)], E=Vab/[(b−a)r²]r̂ and I=4πσVab/(b−a). Hence R=(b−a)/(4πσab)=ρ_res(1/a−1/b)/(4π). Equivalently integrate dR=ρ_res dr/(4πr²). This also gives R≈ρ_res d/(4πa²) for a thin shell.

D132-C04 | conductivity_interface_charge_conditions | lecture7.pdf, PDF 7, slides 14 | Two-material interface
The steady equal-current relation and jump formula are correct for the stated equal-area geometry and Gaussian total-charge convention. Conductivity change makes charge accumulation possible, but nonzero current and a discontinuity of the normal E are what produce the shown sheet charge.
Take n from material 1 to 2, equal cross-sectional area A, steady state with no interface charging rate, scalar Ohmic materials. Distinguish total surface charge from free surface charge when dielectric permittivities differ.
J_n=I/A implies E1=I/(Aσ1), E2=I/(Aσ2). Thus σ_surface,total=(E2−E1)/(4π)=I(ρ_res,2−ρ_res,1)/(4πA). If σ2<σ1 and I>0, positive sheet charge supports the larger downstream field. For free charge with material polarization, use n·(D2−D1)=4πσ_free. For smooth σ, ∇·(σE)=0 gives ρ_charge=−E·∇lnσ/(4π), showing distributed accumulation in the analogous model.

D132-G01 | drude_collision_time_sampling_gap | lecture7.pdf, PDF 8,9, slides 15,16,17 | Momentum averaging and definition of τ
The final σ=nq²τ/m is the standard relaxation-time result. The derivation identifies the average time elapsed since the last collision with the mean time between collisions without specifying collision statistics. This equality is not automatic.
Use independent Poisson scattering with momentum randomized to zero mean after each collision, or define τ as a phenomenological momentum-relaxation time. Require constant weak field and steady state for the displayed DC formula.
For intervals T sampled over a long stationary trajectory, mean age since last collision is E[T²]/(2E[T]). Exponential intervals of mean τ give E[T²]=2τ² and mean age τ, while deterministic intervals τ give mean age τ/2. Independently, m dv_d/dt=qE−mv_d/τ yields v_d→qτE/m and σ=nq²τ/m. This establishes the result without the unstated sampling assumption.

D132-S03 | carrier_sign_and_multicomponent_conductivity | lecture7.pdf, PDF 9, slides 17 | Conductivity formula
The charge-squared expression and additive species contributions are correct within independent scalar relaxation-time response.
For electron carriers q<0 the drift is opposite E but conventional current is along E. Species parameters may depend on temperature and material; τ is not a universal constant.
With v_k=q_kτ_k E/m_k, J=Σn_kq_kv_k=[Σn_kq_k²τ_k/m_k]E. Each term is nonnegative for n_k,τ_k,m_k>0. Units verify σ_SI in S/m and σ_CGS in s^(-1). The source’s scalar sum omits magnetic-field Hall terms, tensor response and carrier coupling, which are outside its approximation.

Independent coverage

- Read all nine complete page texts and personally viewed all original full pages, 17 slides and the final blank lower half.
- Read all eight numerical-table rows in the full page and a direct-PDF enlargement; independently recomputed every unit conversion.
- Verified current geometry, signed species current, continuity, local/macroscopic Ohm law, spherical resistor, conductivity-interface charge and DC Drude formulas.
- Primary checks localized the physical limits of the scattering cartoon and superconductivity/purity language.

Technical disposition

Source review complete. Main confirmed defects are reversed ion-drift arrows and a factor-ten error across the CGS resistivity table. Minor wording/index slips are localized. The conservation and resistor mathematics is correct under steady, scalar-Ohmic and boundary assumptions; collision-time averaging and material physics need the recorded qualifications.

Limits

- The printed material resistivities lack temperature/composition specifications. Their SI-to-CGS consistency is checked; exact empirical values under unspecified conditions are not certified.
- Demonstrations F1/F4/F5 and the visible draft placeholder are not missing assigned assets or instructions to invent content.
- No microscopic or superconducting quantitative model beyond the clearly identified primary corroboration and explicit relaxation-time derivation is claimed.

Primary corroboration

TU Delft Open Solid State Notes, Drude model | https://solidstate.quantumtinkerer.tudelft.nl/3_drude_model/ | Drude assumptions, equation of motion and On what do the electrons scatter? | retrieved 2026-10-08
Primary university course, successfully opened on retry. Confirms uncorrelated scattering, randomized momentum, relaxation-time conductivity and phonon/defect mechanisms. Independent sampling derivation in this record is reviewer supplied.

CERN, Superconductivity | https://home.cern/science/physics/superconductivity/ | Critical-temperature and Type-I/Type-II discussion | retrieved 2026-10-08
Primary institution, opened. Supports phase-transition and critical-field conditions; not used as a comprehensive microscopic transport theory.

CERN, Less hungry magnets for the experiments of the future | https://home.cern/less-hungry-magnets-experiments-future/ | Paragraph identifying superconducting niobium–titanium alloy | retrieved 2026-10-08
Official primary search extract establishes an alloy example. A separate CERN Document Server artifact returned a bot wall and is not claimed read.

