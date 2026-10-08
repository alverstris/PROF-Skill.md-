D134 source technical review

Variable Currents, RC Circuits Thévenin Equivalence

MIT 8.022 Fall 2004. Official indexed session 11; published PDF title Lecture 9; linked file lecture9.pdf. These identities are retained separately. One original PDF, 12 full sheets. Every complete text and original full-page render inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/46de97e4978fc003565f683871741451_lecture9.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture9/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D134/source.pdf
SHA256: 072bc2998b5448a93dbe75a8e0833eb069763b75f26ed40c7b674e88b1959e56
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 134, 'active_order': 63, 'queue_selection_evidence': 'Official index labels this row SES # 11: Variable Currents, RC Circuits\n\n\nThévenin Equivalence.'}

Page, slide and visual coverage

lecture9.pdf, PDF 1, printed sheet 1, slides 1,2: Printed Lecture 9 title; EMF, Kirchhoff and power recap.
lecture9.pdf, PDF 2, printed sheet 2, slides 3,4: Initially charged capacitor and open switch; Discharge after closing switch.
Slide 3 — open RC loop: Upper capacitor plate positive, switch open, R on right; Q0 is one plate charge magnitude.
Slide 4 — closed discharge loop: Clockwise conventional current leaves the positive capacitor plate.
lecture9.pdf, PDF 3, printed sheet 3, slides 5,6: Discharge ODE; Separated integral and exponential solution.
lecture9.pdf, PDF 4, printed sheet 4, slides 7,8: Time constant, units and discharge current; Charging an initially uncharged capacitor.
Slide 8 — charging loop: Battery bottom with left positive terminal; lower capacitor plate becomes positive and clockwise current is consistent with increasing lower-plate Q.
lecture9.pdf, PDF 5, printed sheet 5, slides 9,10: Charging ODE; Shifted-variable integral.
Slide 9 — charging loop: Same polarity, switch and current diagram as slide 8; source, capacitor and resistor voltages inspected.
lecture9.pdf, PDF 6, printed sheet 6, slides 11,12: Charge/voltage/current plots; Substitution into loop rule and initial/final limits.
Slide 11 — three time plots: Q and Vc rise from zero, I steps to V/R then decays; Q asymptote is labelled Q0 even though preceding initial Q0 was zero.
lecture9.pdf, PDF 7, printed sheet 7, slides 13,14: E9 time-constant numbers; E8 square-wave circuit and scope plots.
Slide 13 — RC loop and voltage plot: 3 V, 1.3 F, 11.7 ohm; Vc reaches 1.9 V at about 15.2 s.
Slide 14 — three-terminal E8 schematic: As published, R2 joins upper V_EMF node to lower A node, C joins upper node to ground G, R1 joins G to A; no generator or transformer secondary is drawn in left branch.
Slide 14 — square-wave/response plots: 5 V pulses; continuous rise/fall capacitor voltage and alternating current transients labelled 10 mA positive peak.
lecture9.pdf, PDF 8, printed sheet 8, slides 15,16: Doubling C or resistance; Switched shunt RC circuit.
Slide 15 — repeated E8 circuit: Same missing generator/secondary and displayed R1=100, R2=400 ohm; R2 replacement 900 ohm checked.
Slide 16 — non-series RC topology: Source V through R1 to a node shunted by R2, with switch connecting capacitor across R2.
lecture9.pdf, PDF 9, printed sheet 9, slides 17,18: Thevenin port equivalence; Argument from open/short capacitor limits.
Slide 17 — equivalent-circuit pair: Original network port A above B replaced by positive Voc and series RT; capacitor external to the two-terminal network.
Slide 18 — open network and loaded equivalent: Open-circuit A/B on original network and zero-initial-charge capacitor on equivalent used in the claimed demonstration.
lecture9.pdf, PDF 10, printed sheet 10, slides 19,20: Actual Thevenin solution; General two-terminal box.
Slide 19 — worked equivalent circuits: Source-divider network compared with series Voc,RT; all formula coefficients and exponent checked.
Slide 20 — black-box equivalence: Unspecified resistor/source network and voltage-source series-resistor replacement; terminal behavior rather than internal currents is equivalent.
lecture9.pdf, PDF 11, printed sheet 11, slides 21,22: E13 lamp relaxation oscillator; Different on/off charging time constants.
Slide 21 — lamp parallel to capacitor: 1 kV source through 2.5 megohm resistor feeds capacitor 0.1 microfarad and fluorescent lamp in parallel.
Slide 22 — repeated oscillator circuit: Same topology; finite on-state lamp resistance gives parallel resistance and a nonzero driven final voltage.
lecture9.pdf, PDF 12, printed sheet 12, slides 23,24: Norton equivalence; Summary and historical logistics.
Slide 23 — Norton equivalent pair: Original source-divider network replaced by current generator and RT in parallel with capacitor; generator circle is labelled IN but lacks a visible direction arrow.

Findings, conditions and independent derivations

D134-N01 | source_identity_and_coverage | lecture9.pdf, PDF 1,12, slides 1,24 | Title and source mapping
Official indexed session 11 links lecture9.pdf, whose title is Lecture 9.
Preserve official session 11 and printed lecture 9 separately. One verified PDF contains 12 sheets and all 24 slides; complete extracted text and every original full-page render were personally inspected.
The index/queue/selection mapping and original SHA256 were independently checked. Source E8/E9/E13 references name demonstrations, not additional assigned lecture-packet assets. Scoped E8 primary diagrams were separately inspected as corroboration, not silently added to the original packet.

D134-C01 | lumped_rc_model_and_current_signs | lecture9.pdf, PDF 1,2,3,4,5, slides 2,3,4,5,8,9 | Kirchhoff recap and capacitor models
The source uses time-dependent Kirchhoff equations and Q=CV. A charged capacitor is called an EMF, but it supplies stored electrostatic energy rather than a chemical non-electrical EMF. Having capacitors does not by itself imply varying current in every possible state.
Assume ideal linear constant C>0, positive constant R, ideal wires and source/switch, negligible inductance and propagation delay, and no unmodelled changing linked magnetic flux. The models are quasistatic lumped approximations. Q is charge on the chosen plate, not the 2Q difference between plate charges.
During discharge with Q on the initially positive upper plate, clockwise I=−dQ/dt; during charging the lower plate is positive and clockwise I=dQ/dt. The two drawn polarities and signs are consistent. A capacitor at DC equilibrium has zero current and can retain nonzero voltage. KCL includes capacitor branch current; it does not deny charge accumulation on capacitor plates. Finite current implies continuous Vc because ΔQ=∫I dt and Vc=Q/C.

D134-S01 | discharge_solution_integrals_and_dimensions | lecture9.pdf, PDF 2,3,4, slides 3,4,5,6,7 | Discharge derivation
Q/C−IR=0 and I=−Qdot give RQdot+Q/C=0. Both the displayed exponential and its positive clockwise discharge current are correct.
For Q(0)=Q0, Q=Q0 exp(−t/RC), Vc=Q/C, I=Q0/(RC) exp(−t/RC). The logarithmic separation requires Q0≠0 and a fixed nonzero sign; Q0=0 is the separate identically zero solution.
Integrating dQ/Q=−dt/(RC) gives ln|Q/Q0|=−t/(RC). SI [R][C]=(V/A)(coulomb/V)=s; Gaussian [R][C]=(statvolt·s/statcoulomb)(statcoulomb/statvolt)=s. At t=RC the charge is Q0/e; the lost fraction is 1−1/e. Thus decreased by 1/e should be understood as reduced to 1/e, not lost 1/e. τ=RC is a time constant; exponential decay rate is 1/τ, irrespective of the source’s decay-constant naming.

D134-S02 | charging_solution_initial_condition_and_plot_notation | lecture9.pdf, PDF 4,5,6, slides 8,9,10,11 | Charging integral and plotted Q scale
For the explicitly uncharged initial capacitor, the charging equations and all three formulas beside the plots are correct. The Q-plot asymptote is labelled Q0, reusing the earlier initial-charge symbol misleadingly.
Use Q∞=CV for the plotted asymptote, with Q(0)=0 here. In the integration, shifted Q′=Q−CV starts at −CV; a lower bound labelled Q=0 is an original-variable endpoint, not Q′=0. Current becomes exactly zero only asymptotically for finite positive R,C and a nonzero step.
RQdot+Q/C=V yields Q=CV+(Qi−CV)e^(−t/RC), I=(V−Qi/C)/R e^(−t/RC). At Qi=0 this reduces to Q=CV(1−e^(−t/RC)), Vc=V(1−e^(−t/RC)), I=(V/R)e^(−t/RC). With Q′<0 for positive V, ln[(Q−CV)/(−CV)]=−t/RC has a positive dimensionless argument. The pre-switch zero-current and post-switch V/R step are idealized finite current jumps, not capacitor-voltage jumps.

D134-C02 | initial_short_final_open_and_single_exponential_scope | lecture9.pdf, PDF 6, slides 12 | No need to solve the differential equation conclusion
The asymptotic shortcut works for a first-order linear circuit with known time constant. Initially acting as a short requires zero initial capacitor voltage; it is not a general property of every capacitor.
For arbitrary initial voltage v0, use v(t)=v∞+(v0−v∞)e^(−t/τ), with τ=R_seen C for one independent capacitor state. A precharged capacitor at t=0 acts as its initial voltage constraint. At steady DC it is an open current branch.
Substitution gives V−V(1−e^(−t/RC))−(V/R)e^(−t/RC)R=0 as shown. Initial and final values alone do not determine an unknown multiexponential or nonlinear transient. A network with two independent capacitor states can have two decay rates; the source shortcut presupposes the first-order model already established.

D134-S03 | energy_consistency_supplement | lecture9.pdf, PDF 3,4,5,6, slides 5,7,9,11 | Independent energy check of both transient solutions
The source does not develop the energy partition in this packet. The following checks are reviewer-derived corroboration of its current/charge formulas.
For discharge, the resistor receives the initially stored energy Q0²/(2C). For a step charging from zero through positive R, battery work is CV², final stored energy is CV²/2 and resistor heat CV²/2 within the ideal model.
Integrate R[Q0/(RC)]²e^(−2t/RC) dt over t≥0 to obtain Q0²/(2C). During charging, ∫VI dt=V∫dQ=CV² and ∫RI²dt=(V²/R)(RC/2)=CV²/2. The R→0 limit is singular and is not a loss-free charging conclusion from these lumped equations.

D134-S04 | e9_numerical_time_constant | lecture9.pdf, PDF 7, slides 13 | E9 stated values
The source’s RC=15.2 s and Vc≈1.9 V at one time constant are correctly rounded.
For R=11.7 ohm, C=1.3 F, V=3 V and initially zero charge: τ=15.21 s, Q∞=3.9 coulomb and I0≈0.256410 A.
At τ, Vc=3(1−e^−1)=1.896361676 V and I=(3/11.7)e^−1=0.094328062 A. These are predictions of the specified model, not measured demonstration outcomes. The plotted 3 V limit and concave-down growth agree with the formula.

D134-G01 | e8_published_schematic_omits_drive_element | lecture9.pdf, PDF 7,8, slides 14,15 | E8 circuit wiring
The full pages and direct original-PDF enlargement show a closed R2–C–R1 loop with no source/transformer secondary in its left branch. The upper terminal marked V_EMF is directly the capacitor upper node; G is its lower node. Taken literally, that three-terminal drawing does not establish the stated driven series-RC model.
A separately inspected MIT E8 primary apparatus diagram includes an isolation-transformer secondary in series with 400 ohm, C=0.3 microfarad and 100 ohm, supporting the intended total 500 ohm series model. The lecture schematic omits that drive element and ambiguously labels its capacitor-monitor node. This corroboration is not a claim that the historical 2004 setup is completely known.
In the literal lecture graph, an ideal source between the upper node and G would clamp Vc directly; an ideal source between upper node and A would drive C in series with R1 while R2 lies across the source, giving τ=R1 C=30 microseconds, not 150 microseconds. In the externally corroborated series loop, killing the ideal drive leaves R_seen=R1+R2=500 ohm and τ=150 microseconds. These distinct outcomes prove that the missing drive connection matters. External diagrams use varying resistor names/earlier 450+50 versions, so identification is by positions and values, not blindly matched labels.

D134-C03 | e8_square_wave_and_measurement_conditions | lecture9.pdf, PDF 7, slides 14 | Voltage/current response plots
The 10 mA peak and τ=150 microseconds follow from the intended 5 V, 500 ohm series model and a initially uncharged capacitor. The plotted nearly full charge/discharge implicitly requires pulse intervals long enough compared with τ.
For each constant input segment Vs, vC(t)=Vs+(v_start−Vs)e^(−t/τ) and I=(Vs−v_start)/(R1+R2)e^(−t/τ). At downward steps the current reverses but capacitor voltage is continuous. A resistor-voltage scope reading requires division by its resistance and a stated polarity to represent current.
For equal high/low durations h and a=e^(−h/τ), the periodic 0-to-V square-wave extrema are v_max=V/(1+a), v_min=aV/(1+a), so peaks do not equal ±V/R unless near-complete settling or an isolated initial step is assumed. The primary E8 diagrams show two scope channels and a common node; their polarity/inversion notes reinforce that the source I_AG label alone does not fully specify measurement sign. Actual generator impedance and waveform frequency are unspecified in the lecture.

D134-E01 | doubling_time_constant_reverses_speed_claim | lecture9.pdf, PDF 8, slides 15 | Doubling C and R2 replacement line
After correctly writing τ1=2τ0 for doubled C, the source says voltage/current rises/falls twice as fast. It also prints R′=2R=2(R1+R2′), an inconsistent placement of the prime.
The normalized transient is twice as slow: reaching the same fractional endpoint takes twice as long. For the intended series model, R′=R1+R2′=2(R1+R2), so R2′=2R2+R1=900 ohm. The displayed final 900-ohm choice is correct despite the preceding equation.
For any fraction 0<f<1, t_f=−τ ln(1−f) during charging, so τ→2τ gives t_f→2t_f; initial voltage slope V/τ halves. Doubling C leaves initial current V/R unchanged, while doubling total R halves that current from 10 to 5 mA. Thus changing C and R to equalize τ does not make every voltage/current amplitude identical. Under the source’s incorrect primed equality, R′=1000 would equal 2(100+900)=2000, directly exposing the algebraic slip.

D134-G02 | thevenin_demonstration_is_not_general_proof | lecture9.pdf, PDF 9, slides 17,18 | Claimed Thevenin demonstration
The argument starts with the already-assumed single-exponential equivalent RC solution and identifies its open/short limits. This checks parameter identification after equivalence, but does not prove that an arbitrary original network has that terminal relation for every load.
A proof needs linearity of the well-posed resistive network’s terminal equations. The voltage/current relation is affine with independent sources: v=Voc−RT i for current i delivered to the load.
Reviewer derivation: linear nodal equations for internal voltages x have Mx=b+c i, with invertible M after a reference is fixed; port voltage is a linear expression in x and i. Eliminating x gives v=α+βi. At i=0, α=Voc; with independent sources suppressed b=0, β=−RT by the passive input-resistance convention. Therefore all admissible loads see exactly the Thevenin relation, not merely matching two asymptotic points. Degenerate or inconsistent ideal-source networks require separate treatment.

D134-C04 | thevenin_norton_scope_and_source_suppression | lecture9.pdf, PDF 9,10,12, slides 17,18,20,23 | Theorem statements and RT determination
For the stated independent voltage sources and linear resistors, suppressing EMFs means replacing ideal independent voltage sources by shorts. The source Voc/Ishort rule and phrase all elements follow Ohm law need qualifications.
Voc/Ishort is usable when those measurements are defined and nonzero as required; a zero-source resistor network gives 0/0 despite a finite resistance. A test-source slope gives RT generally. Independent current sources are opened, as slide 23 says; dependent sources, if a theorem is extended to them, remain active. Linearity of terminal behavior is the essential requirement, not literal V=RI for every element—an ideal EMF itself is an affine source.
For finite RT≠0, i=(Voc−v)/RT=IN−v/RT with IN=Voc/RT, proving Norton equivalence. A pure ideal voltage source RT=0 has no ordinary finite Norton current; a pure ideal current source has no finite Thevenin open-circuit voltage. Positive passive resistor networks give nonnegative driving-point resistance, but controlled-source extensions can have negative or degenerate resistance and unstable attached-C response. The source’s steady stable RC formulas assume RT>0.

D134-S05 | shunt_rc_thevenin_norton_solution_verified | lecture9.pdf, PDF 8,9,10,12, slides 16,17,18,19,23 | Worked R1–R2 circuit
All displayed Voc, Ishort, RT, Q(t), I(t) and Norton algebra match the circuit, with initially uncharged capacitor and capacitor-branch current. The source’s single I(t) must not be misidentified as the entire battery current.
Voc=VR2/(R1+R2), Ishort=V/R1, RT=R1R2/(R1+R2), τ=CRT. Thus vC=Voc(1−e^(−t/τ)), Q=CvC, IC=(V/R1)e^(−t/τ). Norton current V/R1 must inject upward into the positive capacitor node; the drawn generator lacks a direction arrow.
Direct KCL yields (V−vC)/R1=vC/R2+C dvC/dt, equivalent to C dvC/dt+vC/RT=V/R1. Battery current is V/(R1+R2)+[VR2/(R1(R1+R2))]e^(−t/τ), and shunt current is V/(R1+R2)(1−e^(−t/τ)); their difference equals IC. Checks: at t=0, IC=V/R1 and shunt current zero; at infinity IC=0 but battery current remains V/(R1+R2). R2→∞ recovers the ordinary R1C step; RT arises by shorting the source and seeing R1 parallel R2.

D134-G03 | relaxation_oscillator_frequency_and_threshold_gap | lecture9.pdf, PDF 11, slides 21,22 | E13 flashing estimate and restart condition
R=2.5 megohm and C=0.1 microfarad give RC=0.25 s and 1/RC=4 Hz, correctly calculated. This does not quantitatively establish the stated roughly 1 Hz flashing: threshold and extinction values are not supplied. A threshold equal to or above the 1 kV ideal supply is never crossed in finite passive charging time.
Need hysteresis or equivalent lamp switching dynamics with turn-on Von below supply Vs and turn-off Voff below Von. In the simple on-state-resistor model, its driven equilibrium Von_state=Vs RFL/(R+RFL) must be below Voff so extinction can occur. The source’s RFL much smaller than R is an approximation, not a full nonlinear lamp law.
Starting at Voff, charge time is tc=RC ln[(Vs−Voff)/(Vs−Von)]. Let Rp=R parallel RFL and veq=Vs RFL/(R+RFL). On-state discharge time is td=Rp C ln[(Von−veq)/(Voff−veq)], provided veq<Voff<Von<Vs. Period is tc+td. If td negligible and Voff≈0, a 1 s period with τ=0.25 s corresponds to Von/Vs=1−e^−4≈0.981684, compatible with a loosely stated near-1-kV threshold but not fixed by it. The source 1/RC is only a characteristic scale. τ_dis≈RFL C≪RC is correct when RFL≪R, while the nonzero on-state equilibrium and switching thresholds determine whether repeated flashes occur at all. These formulas are reviewer supplements; no observed lamp properties are invented.

Independent coverage

- Read all 12 complete original page texts, all 24 slides and every original full-page image. Inspected every loop diagram, source polarity, integral endpoint, exponential formula and response plot.
- Verified discharge/charge ODEs by substitution, initial/final limits, current signs, SI/CGS dimensions and an independent energy balance.
- Recomputed E9 values, E8 intended time constant/current and both doubling effects; directly enlarged the original E8 circuit to establish its actual connectivity.
- Resolved the intended E8 series loop through three inspected primary MIT apparatus images; kept the published-source omission distinct from the supplementary evidence.
- Derived general linear port equivalence and directly solved the shunt circuit by nodal KCL, including capacitor versus battery currents.
- Derived threshold-dependent lamp charging/discharging periods and conditions for sustained relaxation oscillations; no numerical threshold or lamp law invented.

Technical disposition

Source review complete. Main confirmed errors are the twice-as-fast claim and inconsistent primed-resistance equation. The published E8 schematic lacks the drive element present in primary apparatus records. The elementary RC and worked Thevenin/Norton formulas are correct under stated initial-state and linear/quasistatic assumptions. The purported general Thevenin proof and oscillator frequency estimate need the explicit gaps/conditions recorded here.

Limits

- E8 apparatus images establish a related primary series-loop configuration but do not certify all details of the 2004 demonstration or its measured waveforms. The lecture omits the actual generator/secondary connection.
- E13 ignition/extinction voltages, on-state characteristic and observed flash interval are unspecified; only conditional model predictions are possible.
- No live E8/E9/E13 demonstration was performed or viewed. External apparatus instructions were read as historical evidence, not executed.
- The theorem proof supplement assumes a well-posed linear network. Degenerate ideal-source configurations and controlled-source cases are qualified rather than asserted covered by the elementary ratio formula.

Primary corroboration

MIT Technical Services Group, E8 RC Time Constant Displayed on an Oscilloscope | https://web.mit.edu/~tsg/DemoPage/E/E8/E8.htm | Complete short description and links to primary apparatus diagrams/notes | retrieved 2026-10-08
Opened description. It identifies square-wave drive and scope displays but alone does not resolve the lecture schematic. Three linked original images below were downloaded and personally viewed in full. These are corroborating external assets, not required lecture-packet assets.

MIT E8 primary apparatus image E8diag_1.jpg | https://web.mit.edu/~tsg/DemoPage/E/E8/E8diag_1.jpg | Upper 450+50-ohm circuit and lower 400+100-ohm circuit, isolation transformer and two scope channels | retrieved 2026-10-08
The lower drawing explicitly puts a transformer secondary, 400 ohm, 0.3 microfarad capacitor and 100 ohm in a series loop. Upper variant and handwritten scope-polarity notes were also read. This supports the intended series model while preserving differences from lecture labels.

MIT E8 primary apparatus image E8diag_2.jpg | https://web.mit.edu/~tsg/DemoPage/E/E8/E8diag_2.jpg | Entire apparatus sketch, 400-ohm upper resistor, 0.3-microfarad C, 100-ohm lower resistor, total 500 ohm | retrieved 2026-10-08
Explicit isolated source in the left branch resolves why the lecture drawing is incomplete. Resistor labels differ from the lecture; values and positions, not names, are used for comparison.

MIT E8 primary apparatus image E8notes_1.jpg | https://web.mit.edu/~tsg/DemoPage/E/E8/E8notes_1.jpg | H. Bradt MIT, September 3 1987, printed page 54, X36 RC Circuit; full note sheet | retrieved 2026-10-08
Read the full historical apparatus sheet and hand annotations. Shows other values (450+50 ohm and 1 microfarad in the typed version, 0.3 microfarad handwritten), square-wave response sketches, isolation and scope-channel inversion notes. It is not claimed to certify the precise 2004 configuration or any observed experimental trace.

