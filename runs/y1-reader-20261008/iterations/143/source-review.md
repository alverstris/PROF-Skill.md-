D143 source technical review

AC Circuits (Conclusion) Filters Quality Factor and Resonance

MIT 8.022 Fall 2004. Official indexed session 23; published PDF title Lecture 18; linked file lecture18.pdf. Identities retained separately. One original PDF, 10 full sheets. Every complete page text and original full-page render personally inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied read-only.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/19b92b261f2a29004c97cdbf189e103b_lecture18.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture18/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D143/source.pdf
SHA256: b59ea1d7b2b8c187d67534d2a8526c4d46518998cf68fae07bfbaf41ae59a355
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 143, 'active_order': 72, 'queue_selection_evidence': 'Official index labels this row SES # 23: AC Circuits (Conclusion)\n\n\nFilters\n\n\nQuality Factor and Resonance.'}

Page, slide and visual coverage

lecture18.pdf, PDF 1, printed sheet 1, slides 1,2: Title Lecture 18, footer Lecture 17; Complex impedance recap.
Slide 2 — driven RLC inset: Series AC source,C,R,L; correct R/C/L impedance list.
lecture18.pdf, PDF 2, printed sheet 2, slides 3,4: Series and parallel impedances; Reference voltage and current phase.
Slide 3 — two network diagrams: Two impedances in series versus parallel; branch-current equation checked.
Slide 4 — impedance/current diagrams: R horizontal, inductive reactance up, capacitive reactance down; reference V real and lagging I illustrated.
lecture18.pdf, PDF 3, printed sheet 3, slides 5,6: Impedance magnitude and phase; Current lead/lag from reciprocal impedance.
Slide 5 — complex-vector sum: Resultant Z has positive imaginary component and angle φZ.
Slide 6 — paired impedance and current phasors: Current phase opposite impedance phase for real reference voltage.
lecture18.pdf, PDF 4, printed sheet 4, slides 7,8: Instantaneous and period-average power; RMS and real-power formula.
Slide 7 — undriven circuit inset reused: Capacitor,R,L with open-switch-like gap, although equations explicitly assume a driven sinusoidal state; inset not used as proof of the drive.
lecture18.pdf, PDF 5, printed sheet 5, slides 9,10: Power resonance; Reactance cancellation.
Slide 9 — power peak graph: Frequency-dependent power with maximum at Ω=1/√LC.
Slide 10 — canceling reactance arrows: Inductive and capacitive vertical vectors cancel, leaving R.
lecture18.pdf, PDF 6, printed sheet 6, slides 11,12: Half-power width and Q; Antenna equivalent circuit.
Slide 11 — half-height construction: Power curve, Pmax/2 line and two positive crossing frequencies; quadratic roots inspected.
Slide 12 — antenna schematic: Aerial symbol feeds R,L,C series equivalent to ground; source EMF specified in prose.
lecture18.pdf, PDF 7, printed sheet 7, slides 13,14: Resonant current and capacitor voltage; Antenna bandwidth and Q changes.
Slide 13 — repeated antenna equivalent: R=75 ohm, L=8.22 microhenry, C=0.27 picofarad and 9.13 microvolt RMS input.
Slide 14 — repeated antenna equivalent: Same model for bandwidth/selectivity discussion.
lecture18.pdf, PDF 8, printed sheet 8, slides 15,16: RL low-pass across R; RL high-pass across L.
Slide 15 — RL circuit and gain curve: Output terminals across R; gain decreases from one to zero.
Slide 16 — RL output terminals: Output taken across L at the two bottom terminals; high-pass limits inspected.
lecture18.pdf, PDF 9, printed sheet 9, slides 17,18: RC low-pass across C; RC high-pass across R.
Slide 17 — RC capacitor output: Output terminal pair spans capacitor, despite asymptote text labelling VR.
Slide 18 — RC resistor output: Output terminal pair spans R; intermediate amplitude formula misses a numerator R.
lecture18.pdf, PDF 10, printed sheet 10, slides 19: Summary; lower half blank.

Findings, conditions and independent derivations

D143-N01 | identity_and_reused_notation | lecture18.pdf, PDF 1,2,3,10, slides 1,2,4,6,19 | Title/footer and symbols
Official indexed session 23 links lecture18.pdf. Title says Lecture 18, while slide footers throughout say Lecture 17. This is a source identity inconsistency, not grounds to remap the assigned asset.
Retain official session 23, title Lecture 18 and footer Lecture 17 explicitly. All 10 full sheets/19 slides were read. The ZC subscript in slides 4/6 is used where the context is total circuit impedance; define Ztot rather than confuse it with the capacitor impedance already defined on slide 2.
The packet’s formulas and diagrams establish the total impedance R+i(ωL−1/(ωC)); interpreting that repeated ZC as only a capacitor would contradict the R/L vectors and general magnitude formula. No new source file is inferred from the erroneous footer.

D143-E01 | parallel_branch_currents_incorrectly_equated | lecture18.pdf, PDF 2, slides 3 | Parallel impedance calculation
The source writes V1/Z1=V2/Z2=V/Zeq for parallel branches, incorrectly equating each branch current to the total. Its final reciprocal-impedance result is correct.
Use V1=V2=V and V/Zeq=V1/Z1+V2/Z2. In series, I1=I2=I and V=I(Z1+Z2), as the source correctly states.
KCL gives I=I1+I2, so Yeq=Y1+Y2. Counterexample Z1=Z2=R: each branch carries V/R and total is 2V/R, hence Zeq=R/2, not R. The sum formulas require a common sinusoidal frequency and linear uncoupled lumped elements; mutually coupled inductors need their coupling terms rather than simple independent impedances.

D143-C01 | phasor_reference_and_complex_ordering | lecture18.pdf, PDF 1,2,3, slides 2,4,5,6 | Choosing V real and comparing impedances
The magnitude and phase formulas are correct, but ZL>ZC is not an ordering of complex numbers. Choosing a real voltage means choosing its constant phasor reference, not making the full V0e^(iωt) real at every time.
For R>0, X=ωL−1/(ωC), Z=R+iX and φZ=atan2(X,R). Compare positive reactance magnitudes ωL and 1/(ωC), then current phase relative to voltage is −φZ.
With voltage phasor V0 real, I=V0/Z=(V0/|Z|)e^(−iφZ), |Z|=√(R²+X²). X>0 gives lag, X<0 gives lead. The time-domain signal is Re[Ie^(iωt)]. This algebra addresses sinusoidal steady state; arbitrary initial transients/nonlinear or time-varying components are not captured by the instruction to analyze like DC resistors.

D143-E02 | period_average_integral_limits_inverted | lecture18.pdf, PDF 4, slides 7,8 | Expanded integrals and trigonometric averages
Both original slides print upper integration limit ω/(2π) with integration variable t. That is a frequency, not one period. Direct original-PDF enlargements confirm this is visible source notation, not extraction noise.
Replace every such time limit by T=2π/ω. Keep the outside averaging prefactor 1/T=ω/(2π). The final power expression is correct after this repair.
For corrected limits, (ω/2π)∫0^(2π/ω) cos²ωt dt=1/2 and (ω/2π)∫0^(2π/ω) cosωt sinωt dt=0. With u=ωt, limits become 0 and 2π and prefactor 1/(2π). The printed frequency upper bound fails dimensional consistency and does not produce those identities generally.

D143-S01 | real_power_rms_and_reactive_exchange | lecture18.pdf, PDF 4, slides 7,8 | Power result and no-work wording
The corrected derivation yields Pavg=(V0I0/2)cosφ=Vrms Irms cosφ=R Irms². RMS equals peak/√2 here because the signals are sinusoidal. No-work wording for cosφ=0 must mean zero net work over a full cycle, not zero instantaneous exchange.
For an ideal pure reactive element, p(t)=v(t)i(t) oscillates positive and negative; stored field energy rises and falls while its period-average change vanishes. For general waveforms, compute RMS by sqrt of the mean square and average power directly, not automatically by peak/√2.
Use cos a cos(a−φ)=[cosφ+cos(2a−φ)]/2; the second term averages to zero. In peak phasors Pavg=Re[V I*]/2, not generally the real part of an unconjugated product. The source’s given 120-V RMS sinusoidal example has peak 120√2≈169.706 V, consistent with its 170-V rounding; this is a calculation from stated input, not a current supply-specification audit.

D143-S02 | power_resonance_and_exact_bandwidth | lecture18.pdf, PDF 5,6, slides 9,10,11 | Power peak and half-power quadratics
The power peak, positive-frequency half-power roots, Δω=R/L and Q=Ω/Δω=ΩL/R are correct for a series ideal RLC with constant positive R and frequency-independent input RMS amplitude. One intermediate line writes |X|=±R; the absolute value should equal only +R, or remove the bars for the ± branches.
Let Ω=1/√LC. P=Vrms²R/[R²+(ωL−1/(ωC))²], with Pmax=Vrms²/R at Ω. Half-power points obey X=−R and X=+R, respectively. The bandwidth formula is exact for this model, not limited to weak damping.
Positive roots: ω1=[sqrt(R²+4L/C)−R]/(2L), ω2=[sqrt(R²+4L/C)+R]/(2L). Subtraction gives R/L; multiplication gives ω1ω2=1/(LC)=Ω², so Ω is their geometric mean, not exactly arithmetic midpoint. Other quadratic roots are negative-frequency partners and the source explicitly discards them. R→0 is singular at resonance: its divergent steady-current formula does not establish finite lossless steady power.

D143-S03 | antenna_equivalent_model_numerics | lecture18.pdf, PDF 6,7, slides 12,13,14 | Given L,C,R and induced EMF
The source uses a lumped series RLC representation of a receiving system. Its displayed values are coarse approximations; recalculating the stated inputs gives more precise numbers below.
For L=8.22 microhenry,C=0.27 picofarad,R=75 ohm,Vrms=9.13 microvolt: Ω=6.712467704×10^8 rad/s, f0=106.8322415 MHz, Irms=0.121733333 microampere, capacitor RMS magnitude 0.671681738 mV, Δω=9.124087591×10^6 rad/s, Δf=1.452143641 MHz and Q=73.568646.
Use Ω=1/√LC, I=V/R, |Vc|=I/(ΩC)=QV, Δω=R/L. The source 106 MHz/0.66 mV/1.4 MHz/73 values are approximate or truncated, not precise rounding of all given digits. Voltage magnification does not create power: reactive capacitor/inductor voltages are opposite in phase and cancel at resonance, while their individual magnitudes can exceed source voltage. Source real power for these ideal inputs is Vrms²/R≈1.111425333×10^−12 W. The voltage across C should use |ZC| for an RMS magnitude, or retain its complex phase if using ZC.

D143-C02 | selectivity_and_improving_q_constraints | lecture18.pdf, PDF 7, slides 14 | Antenna quality discussion
Using the source’s stated 0.2-MHz channel-separation benchmark, its approximately 1.45-MHz bandwidth is broad. This toy calculation alone does not establish complete receiver/antenna performance. Saying decreasing R is the only solution tacitly fixes C and prohibits coordinated retuning.
At fixed L,C, reducing R narrows the modeled bandwidth without changing Ω. At fixed desired Ω but adjustable L and C, L′=kL,C′=C/k keeps LC constant and increases Q by k at unchanged R. Real parasitics, loss, matching, occupied signal bandwidth and receiver design are outside the supplied model.
From Q=ΩL/R and Δf=R/(2πL), either mathematical change follows directly. If a 0.2-MHz full half-power bandwidth were adopted solely as this model’s target, Q=f0/Δf≈534.16 and at original L it would correspond to R≈10.33 ohm. This is a conditional algebraic comparison, not an operational radio design recommendation or a newly verified allocation/channel-spacing claim.

D143-S04 | rl_filter_transfer_functions | lecture18.pdf, PDF 8, slides 15,16 | Low/high-pass RL circuits
The two output terminal pairs and all RL amplitude formulas/limits are correct for unloaded ideal voltage measurements. A frequency-dependent voltage divider attenuates continuously; select only certain frequencies is qualitative language.
Across R: HR=R/(R+iωL), |HR|=R/√(R²+ω²L²), low pass. Across L: HL=iωL/(R+iωL), |HL|=ωL/√(R²+ω²L²), high pass.
At cutoff ωc=R/L both magnitudes are 1/√2 (−3.0103 dB amplitude ratio). HR phase is −arctan(ωL/R); HL phase is π/2−arctan(ωL/R). Complex gains satisfy HR+HL=1, while magnitudes generally do not sum to one. Input source impedance, winding resistance, finite load and high-frequency parasitics change these ideal formulas.

D143-E03 | rc_filter_label_and_missing_r_factor | lecture18.pdf, PDF 9, slides 17,18 | Low-pass asymptotes and high-pass intermediate equality
Slide 17 correctly computes capacitor voltage and draws capacitor output terminals, but labels its asymptotic voltage VR; it should be VC. Slide 18 writes VR=R|I|=V0/√(R²+1/(ω²C²)), omitting R in that intermediate numerator, although the final expression includes it correctly.
Correct low-pass limits to VC→V0 as ω→0 and VC→0 as ω→∞. Correct the high-pass intermediate amplitude to R V0/√(R²+1/(ω²C²)), giving ωCRV0/√(1+ω²C²R²).
Derive HC=ZC/(R+ZC)=1/(1+iωRC) and HR=R/(R+ZC)=iωRC/(1+iωRC). Their magnitudes are 1/√(1+ω²R²C²) and ωRC/√(1+ω²R²C²); limits match the actual output nodes. The incorrect intermediate V0/impedance has current units rather than voltage. Cutoff is ωc=1/(RC), with low/high phases −arctan(ωRC) and π/2−arctan(ωRC). Loading and source-resistance assumptions are the same as for the RL examples.

Independent coverage

- Read all 10 complete texts, all 19 slides and every original full sheet; title/footer conflict explicitly retained.
- Inspected all impedance and current phasors, series/parallel topologies, power/half-height plots, antenna equivalent and all four filter output-node pairs.
- Independently derived correct averaging integrals and inspected two direct-PDF enlargements of their erroneous original upper bounds.
- Solved the bandwidth quadratics exactly, recalculated all antenna numbers, and derived all RL/RC complex transfer functions, cutoffs and phases.

Technical disposition

Source review complete. Confirmed errors are equated parallel branch currents, inverted period-integration limits, an absolute-value ± notation slip, incorrect RC output label and a missing R factor in one intermediate amplitude. Final power, bandwidth and filter formulas are otherwise consistent under their linear steady-state/unloaded assumptions. Antenna values and improvement claims are retained as a qualified lumped example.

Limits

- The antenna model does not specify physical geometry, matching, distributed effects, radiation/loss partition or receiver architecture; no empirical performance is certified.
- The stated 0.2-MHz separation is used only as the source’s benchmark, not asserted as a newly checked universal/current broadcasting rule.
- No filter demonstration or radio observation was performed; graphical scales without model parameters are illustrative.
- Source title Lecture18 and repeated Lecture17 footers are both recorded; official session23 mapping remains determined by audit/queue/selection.
