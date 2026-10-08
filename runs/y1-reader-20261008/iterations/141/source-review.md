D141 source technical review

RL Circuits Undriven RLC Circuits Phasor Representation

MIT 8.022 Fall 2004. Official indexed session 18; published PDF title Lecture 16; linked file lecture16.pdf. Identities retained separately. One original PDF, 10 full sheets. Every complete page text and original full-page render personally inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied read-only.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/7b7348480e71d4b842dbc339543bd513_lecture16.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture16/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D141/source.pdf
SHA256: bb5247752f741d958b73554783364db1dff0b383c76aabbec85951ffd54f8ec1
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 141, 'active_order': 70, 'queue_selection_evidence': 'Official index labels this row SES # 18: RL Circuits\n\n\nUndriven RLC Circuits\n\n\nPhasor Representation.'}

Page, slide and visual coverage

lecture16.pdf, PDF 1, printed sheet 1, slides 1,2: Printed Lecture 16 title; Induction recap.
lecture16.pdf, PDF 2, printed sheet 2, slides 3,4: Switched RL intuition; RL rise equation and integration.
Slide 3 — two-switch RL circuit: S1 connects battery; S2 bypasses source to retain closed R-L discharge path; S1 closed/S2 open on energizing.
Slide 4 — repeated switch diagram: Same topology with voltage-drop equation.
lecture16.pdf, PDF 3, printed sheet 3, slides 5,6: RL decay after switching; Initial/open and final/short limits.
Slide 5 — piecewise current plot: Exponential rise followed by decay, continuous current at switch; decay annotation needs a reset time origin.
Slide 6 — repeated rise/decay plot: Qualitative inertia and endpoint interpretation.
lecture16.pdf, PDF 4, printed sheet 4, slides 7,8: Time constant and units; 75-Hz square-wave RL display.
Slide 7 — repeated transient plot: One rise/decay pair with L/R time scale.
Slide 8 — series RL circuit and four traces: Square-wave input, continuous current and resistor voltage, positive/negative inductor voltage pulses; all four traces inspected.
lecture16.pdf, PDF 5, printed sheet 5, slides 9,10: Undriven LC differential equation; LC initial conditions and phase.
Slide 9 — switched LC loop: Initially charged capacitor and ideal inductor; chosen discharge current I=−Qdot.
lecture16.pdf, PDF 6, printed sheet 6, slides 11,12: LC phase plot; Electric/magnetic energy exchange.
Slide 11 — current/voltage oscillations: Sinusoidal current and capacitor voltage in quadrature; unequal vertical scaling is schematic, not comparable physical units.
lecture16.pdf, PDF 7, printed sheet 7, slides 13,14: Series RLC equation; Damped sinusoid and complex exponential approaches.
Slide 13 — RLC loop: Capacitor top, resistor right, inductor bottom and initially open switch.
lecture16.pdf, PDF 8, printed sheet 8, slides 15,16: Complex plane, Euler identity and phasor notation; Characteristic equation and damped roots.
Slide 15 — complex plane: Point z=x+iy in first quadrant, real/imaginary coordinate projections; phase formula needs quadrant qualification.
lecture16.pdf, PDF 9, printed sheet 9, slides 17,18: Weak-damping derivative and approximation; Zero-initial-current approximation and L2 demonstration.
Slide 18 — damped current plot: Alternating red current lobes with decaying positive envelope; drawing represents underdamping only.
lecture16.pdf, PDF 10, printed sheet 10, slides 19: Summary and historical quiz notice; lower half blank.
Slide 19 — three miniature response sketches: Exponential, undamped sinusoid and damped sinusoid summarize the selected regimes.

Findings, conditions and independent derivations

D141-N01 | identity_and_packet_scope | lecture16.pdf, PDF 1,8,10, slides 1,15,19 | Source mapping and handout reference
Official session 18 links lecture16.pdf, printed Lecture 16. All 10 full sheets and 19 published slides were inspected. Slide 15 references a complex-number handout and later recitation.
The assigned indexed packet is the PDF; the audit explicitly excludes adding an unassigned separate handout. The PDF contains the needed complex-plane definition, Euler identity and phasor representation. The missing written proof is supplied below as a reviewer derivation, not represented as a recovered handout.
Queue, selection, audit and original SHA256 agree. Historical quiz and demonstration references do not expand the required packet or authorize an experiment.

D141-S01 | rl_rise_and_switching_time_origin | lecture16.pdf, PDF 2,3, slides 3,4,5 | RL equations and switch transition
L Idot+RI=V gives the displayed rise I=(V/R)(1−e^(−Rt/L)) for zero initial current. After switching at global time t′, the printed decay uses t as though reset to zero and assumes saturation.
With τ=L/R and I(0)=0, current just before switching is I′=(V/R)(1−e^(−t′/τ)). For t≥t′, I(t)=I′e^(−(t−t′)/τ). The source expression (V/R)e^(−t/τ) is valid if t is elapsed discharge time and the preceding energizing interval was much longer than τ.
Solving the first linear ODE with an integrating factor gives I=V/R+(Ii−V/R)e^(−t/τ). Removing the source while closing the discharge path gives Idot=−I/τ. Continuity of inductor current fixes the decay prefactor. The plotted continuous transition is physically consistent; the unshifted annotations alone are ambiguous on a shared global time axis. The ideal switching model never closes S1 and S2 together across the source.

D141-C01 | inductor_endpoint_and_quasistatic_conditions | lecture16.pdf, PDF 2,3,4, slides 3,6,7 | Current inertia and open/short language
An initially unenergized ideal inductor has I(0+)=0 under finite applied voltage, and at steady DC its ideal inductive voltage vanishes. These endpoint analogies depend on initial state and component model.
Require positive constant L,R, fixed geometry, linear response and a lumped quasistatic circuit with parasitic capacitance/inductance, radiation and core loss neglected. A pre-existing current is retained at switching, so the inductor is not generally an initial open circuit. Winding resistance remains at DC.
LΔI=∫vL dt establishes current continuity for finite voltages. The time constant L/R has units seconds: Gaussian (s²/cm)/(s/cm)=s and SI H/ohm=s. For rise the fraction of final-minus-initial change after τ is 1−1/e; for decay the remaining deviation is 1/e. Stored U=LI²/2 explains inertia without claiming an inductor can generate unlimited real voltage or energy.

D141-S02 | square_wave_rl_trace_check | lecture16.pdf, PDF 4, slides 8 | 75-Hz driven RL diagram
All four qualitative traces have the correct relationships: I and VR are continuous, while VL changes sign at falling input and can jump with the input. No component values or measured amplitudes are given.
For a constant input segment Vs beginning with Ia, I=Vs/R+(Ia−Vs/R)e^(−t/τ), VR=RI and VL=Vs−RI. Nearly complete rise/decay between pulses requires segment length large compared with τ.
At a finite input step, ΔI=0 and ΔVR=0, hence ΔVL=ΔVin. For 75 Hz, full period is 1/75≈13.333 ms; if duty cycle is 50%, each segment is 6.667 ms. No specified L/R establishes whether the shown near-settling actually occurs. Decay energy check: ∫0∞ RIa²e^(−2t/τ)dt=LIa²/2.

D141-E01 | lc_initial_current_derivative_sign_slip | lecture16.pdf, PDF 5, slides 9,10 | Initial-condition line on slide 10
The source consistently defines I=−dQ/dt, but its initial-current line uses −ω0 A sin(0)+ω0 B cos(0), the sign of Qdot instead of −Qdot.
For Q=A cosω0t+B sinω0t, I=ω0 A sinω0t−ω0 B cosω0t. Thus I(0)=−ω0B. The specific zero-current condition still gives B=0, so the displayed final solution is unaffected.
With Ω=1/√(LC), Q(0)=Q0 and I(0)=0 give Q=Q0cosΩt and I=ΩQ0sinΩt. More generally, Q=Q0cosΩt−(I0/Ω)sinΩt; a nonzero I0 would expose the source sign error.

D141-S03 | lc_energy_phase_and_idealization | lecture16.pdf, PDF 5,6,7, slides 9,10,11,12,13 | LC solution and energy exchange
The differential equation Qddot+Q/(LC)=0, Ω=1/√(LC), final LC formulas and total energy Q0²/(2C) are correct for the specified initial state. The phrase R is never exactly zero is too universal as a material statement; superconducting DC resistance can vanish, although a physical oscillator still has other loss channels.
Distinguish ideal LC modeling from a claim about every material. For I=−Qdot, positive sinusoidal discharge current lags capacitor-charge cosine by a quarter period. With a passive capacitor-current convention the phase wording changes sign.
UC=(Q0²/2C)cos²Ωt and UL=(Q0²/2C)sin²Ωt; the sum is constant. Energy exchanges at twice the charge-oscillation frequency because the energies involve squares. At a capacitor-voltage zero all ideal energy is magnetic, and at current zero all is electric. Real losses may include resistance, dielectric/core loss and radiation; a zero DC resistance alone does not imply a perfectly loss-free oscillator.

D141-G01 | rlc_oscillatory_solution_requires_underdamping | lecture16.pdf, PDF 7,8, slides 13,14,16 | Must have an oscillatory term claim
The series RLC equation is correct, but a solution is not necessarily oscillatory for arbitrary positive R. The real damped-cosine form requires R<2√(L/C).
Let β=R/(2L) and Ω=1/√(LC). Roots for Q∝e^(st) are s=−β±√(β²−Ω²). Underdamped β<Ω: Q=e^(−βt)[Acosωt+Bsinωt], ω=√(Ω²−β²). Critical β=Ω: Q=(A+Bt)e^(−βt). Overdamped β>Ω: two real decaying exponentials.
Substitution into Qddot+2βQdot+Ω²Q=0 gives the characteristic polynomial. In the alternative source ansatz e^(iαt), α=iβ±√(Ω²−β²), so iα=−β±iω for underdamping. The signs on slide 16 are correct. Slide 14 uses e^(αt) while slide 16 uses e^(iαt), an implicit parameter change; the first trial’s ω0 should be an unknown damped frequency rather than fixed to the prior LC Ω when R≠0. At critical damping, a single cosine form misses the second independent t e^(−βt) solution.

D141-C02 | complex_phase_quadrant_and_real_solution_conditions | lecture16.pdf, PDF 8, slides 15,16 | Complex notation and real-part method
Euler’s identity and polar form are correct. θ=arctan(y/x) only directly gives the right quadrant for appropriate x,y; phase is undefined at z=0. Taking the real part of a complex solution is valid because the ODE has real coefficients.
Use r=√(x²+y²)≥0 and θ=atan2(y,x) modulo 2π for z≠0. A real number is also a complex number with zero imaginary part; both parts need not be nonzero. For a second-order ODE retain two real integration constants via amplitude/phase or two fundamental solutions.
Reviewer Maclaurin proof: e^(iθ)=Σ(iθ)^n/n!; grouping even powers yields cosθ and odd powers yields i sinθ. Absolute convergence justifies grouping. If Qtilde=u+iv solves a real linear ODE, its real and imaginary parts separately solve it by equating real/imaginary coefficients. Counterexample to principal arctan alone: z=−1 gives y/x=0 but phase π, not 0. A general decaying complex root is not a constant-amplitude steady-state sinusoidal phasor.

D141-C03 | weak_damping_and_initial_condition_accuracy | lecture16.pdf, PDF 9, slides 17,18 | Approximate current and initial phase
The source explicitly labels its final weak-damping formulas approximate. Dropping the βcos term in I and setting phase zero are leading-order approximations, not an exact initial-value solution for finite R. The general derivative should use the amplitude A; calling it Q0 before the phase is fixed conflates amplitude with initial charge.
Require β/Ω≪1, equivalently R≪2√(L/C). Exact zero-initial-current underdamped solution is Q=Q0 e^(−βt)[cosωt+(β/ω)sinωt] and I=Q0(Ω²/ω)e^(−βt)sinωt, with ω=√(Ω²−β²).
Differentiate the exact Q: cosine terms cancel, leaving Qdot=−Q0(ω+β²/ω)e^(−βt)sinωt=−Q0Ω²/ω e^(−βt)sinωt. In A e^(−βt)cos(ωt+φ), exact I(0)=0 requires tanφ=−β/ω and A=Q0Ω/ω for Q0>0. The source approximate pair Q≈Q0e^(−βt)cosΩt, I≈ΩQ0e^(−βt)sinΩt is leading order, but differentiating its approximate Q gives an additional βQ0e^(−βt)cosΩt and nonzero I(0)=βQ0. Thus it should not be advertised as exactly satisfying both derivative relation and initial conditions. The omitted term may dominate relative error near current zeros even when its absolute amplitude is small.

D141-S04 | damping_energy_and_envelope_interpretation | lecture16.pdf, PDF 7,8,9, slides 13,16,17,18 | Meaning of damping and plotted envelope
For positive R, circuit energy decreases. Charge/current envelope time constant 2L/R differs from the earlier RL current time constant L/R; the source exponent R/(2L) is correct.
Use U=Q²/(2C)+LI²/2 and dU/dt=−RI² for the exact source-free model. A pure energy exponential e^(−Rt/L) is generally an averaged weak-damping approximation, not an exact instantaneous identity for arbitrary initial phase.
Multiply Qddot+(R/L)Qdot+Q/(LC)=0 by LQdot and use I=−Qdot to obtain dU/dt=−R Qdot². For weak damping, averaging sin² and cos² over a cycle gives Ubar proportional to e^(−2βt), hence energy-decay time L/R, while amplitudes decay on 1/β=2L/R. The red-envelope sketch illustrates this regime; exact successive maxima are affected by the phase and frequency. No L2 measured trace was supplied or observed.

Independent coverage

- Read all 10 complete page texts and personally viewed every original full sheet, 19 slides and final blank lower half.
- Checked both switch configurations, RL integration, current continuity, time-origin shift, SI/CGS units and all four square-wave traces.
- Verified LC frequency, current sign, initial conditions and energy transfer; localized a derivative-sign slip that cancels only for zero initial current.
- Derived all three RLC damping regimes, checked the complex-root signs, supplied Euler proof and quadrant conditions, and compared exact versus weak-damping initial-value solutions.

Technical disposition

Source review complete. Main issues are the LC initial-current sign slip, unqualified oscillation claim, RL decay time-origin/prefactor assumptions, and weak-damping/phase conditions. The displayed RL and final ideal-LC solutions are correct in their stated zero-initial-current settings; RLC roots and decay exponent are correct below the stated critical-damping boundary.

Limits

- The separate complex-number handout/recitation is referenced but not an indexed assigned asset. No unprovided handout is claimed read.
- The 75-Hz demonstration lacks component values and scope calibration; no quantitative settling or measured amplitude is certified.
- Weak-damping expressions have controlled leading-order scope; exact equality near current zeros or exact initial phase is not asserted.
- No demonstration or historical quiz material was executed, observed or invented.

Primary corroboration

CERN, Superconductivity | https://home.cern/science/physics/superconductivity/ | Opening explanation of vanishing electrical resistance below critical temperature, with critical-field conditions | retrieved 2026-10-08
Primary institution page successfully opened earlier in this source-preparation conversation. Used only to qualify the universal material statement R is never exactly zero; it does not establish zero total loss in a real AC resonator.

