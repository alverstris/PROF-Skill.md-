D133 source technical review

EMF, Circuits Kirchhoff’s Rules

MIT 8.022 Fall 2004. Official indexed session 10; published PDF title Lecture 8; linked file lecture8.pdf. These identities are retained separately. One original PDF, 12 full sheets. Every complete text and original full-page render inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/7abaea2ba93dcbc20f6ec38bb95fbdfe_lecture8.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture8/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D133/source.pdf
SHA256: 3b301472dae82e7c7efa486dbbe240b184e1a0f68c4eadd735ca9c96e9cade7c
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 133, 'active_order': 62, 'queue_selection_evidence': 'Official index labels this row SES # 10: EMF, Circuits\n\n\nKirchhoff’s Rules.'}

Page, slide and visual coverage

lecture8.pdf, PDF 1, printed sheet 1, slides 1: Printed Lecture 8 title and topics; otherwise blank sheet.
lecture8.pdf, PDF 2, printed sheet 2, slides 3,4: Quiz commentary and statistics; Recap of current, continuity, Ohm law and Drude conductivity.
lecture8.pdf, PDF 3, printed sheet 3, slides 5,6: Meaning of EMF; Lead-acid battery half-reactions and net reaction.
Slide 6 — electrochemical cell: Left PbO2 positive electrode, right Pb negative electrode, sulfuric-acid electrolyte and leftward H+ arrow; both half-reactions and unbalanced net equation inspected.
lecture8.pdf, PDF 4, printed sheet 4, slides 7,8: Battery connected to resistor; EMF integral and battery/current convention.
Slide 7 — loaded cell: External resistor, PbO2+/Pb− electrodes, rightward E and leftward H+ arrows; terminal integral bounds read.
Slide 8 — battery symbol: Long positive line, short negative line; upward conventional current into external positive-terminal lead.
lecture8.pdf, PDF 5, printed sheet 5, slides 9,10: Loop rule; Three-resistor series circuit.
Slide 9 — single-loop circuit: Battery positive terminal supplies clockwise current through R.
Slide 10 — three-resistor loop: R1 top, R2 right, R3 bottom; clockwise current and ideal wires.
lecture8.pdf, PDF 6, printed sheet 6, slides 11,12: Series equivalent resistance; Node-to-node voltage differences.
Slide 11 — equivalent-circuit pair: Three-resistor loop and single Req circuit with same battery/current.
Slide 12 — labeled loop: Nodes A,B,C,D run clockwise from battery positive; voltage differences checked against positions.
lecture8.pdf, PDF 7, printed sheet 7, slides 13,14: F13 component measurement; Node rule.
Slide 13 — five-element series loop: Saline solution, resistor, diode, lamp and fluorescent lamp represented schematically as R1–R5; current unit is printed mV.
Slide 14 — parallel branches: I enters node N; I1 and I2 leave downward through R1 and R2.
lecture8.pdf, PDF 8, printed sheet 8, slides 15,16: Parallel branch solution; Parallel equivalent resistance.
Slide 15 — parallel circuit: Common voltage V across both branches and current split.
Slide 16 — equivalent-circuit pair: Parallel R1,R2 replaced by Req, retaining source and total current.
lecture8.pdf, PDF 9, printed sheet 9, slides 17,18: Series/parallel comparison; F12 numerical resistor network.
Slide 17 — series and parallel fragments: Series chain and three parallel branches; formula inequalities need positive finite resistances.
Slide 18 — two measured circuits: Top V=1.5 V with RL=1580 ohm and 0.94 mA reading; lower R+(R parallel (R+RL)) ladder, R=912 ohm; ammeter in source return measures total current.
lecture8.pdf, PDF 10, printed sheet 10, slides 19,20: Two-source network; Loop equations, solved currents and sign guide.
Slide 19 — two-source circuit: Both batteries have upper positive terminal; R1 top left, R2 middle, R3 bottom right. I1 label initially marks central-branch current.
Slide 20 — relabelled circuit and equations: I1 now marks current through R1, I2 right branch; central downward current I1−I2. Closed forms and loop-traversal sign box inspected.
lecture8.pdf, PDF 11, printed sheet 11, slides 21,22: Battery internal resistance; Electrical power.
Slide 21 — equivalent battery: Ideal voltage source in series with internal r; source includes a short-circuit homework suggestion, only read and recorded.
lecture8.pdf, PDF 12, printed sheet 12, slides 23,24: Temperature-dependent resistance and F16 lamp example; Summary and historical logistics.

Findings, conditions and independent derivations

D133-N01 | source_identity_pagination_and_statistics_ambiguity | lecture8.pdf, PDF 1,2,12, slides 1,3,24 | Title, quiz statistics and missing slide number
Official indexed session 10 links lecture8.pdf, printed Lecture 8. PDF 1 contains only slide 1; printed slide 2 is absent. Slide 3 reports mean 59 and RMS 16.
Retain all three identities. The published packet has 12 sheets and 23 slides: 1,3–24. No required substantive reference to absent slide 2 is identifiable. RMS 16 cannot mean raw root-mean-square score; it plausibly denotes centered RMS/standard deviation, but original score data are unavailable.
For any finite score sample, RMS²=mean²+variance, so raw RMS≥|59|. The comment that a lower mean proves a harder exam is an interpretation confounded by cohort differences, not a demonstrated statistical conclusion. Historical course/quiz instructions were read as source content, not current instructions.

D133-C01 | recap_and_emf_model_conditions | lecture8.pdf, PDF 2,3, slides 4,5 | Current recap and source of charges phrase
The displayed current, continuity, scalar Ohm law and Drude equations match the preceding packet. Calling a battery a source of charges may be misread as charge creation.
I is signed charge crossing a section per time. J=ρu is for a carrier population, not total neutral-medium charge density; sum species as needed. A battery supplies energy and maintains electrochemical potential differences; it redistributes existing charges. Use DC scalar linear conductivity and steady relaxation-time assumptions for the Ohmic/Drude formulas.
Charge conservation ∂ρ/∂t+div J=0 forbids net charge creation by the source. For a uniform wire, V=EL and I=JA give R=L/(σA). With drift qτE/m, J=nq²τE/m; the multiple-species and collision-statistics caveats remain as localized in D132.

D133-E01 | unbalanced_net_battery_reaction | lecture8.pdf, PDF 3, slides 6 | Bottom chemical equation
The two displayed half-reactions are individually balanced, but their printed net reaction has only one H2SO4 on the left: Pb+PbO2+H2SO4→2PbSO4+2H2O.
Correct the coefficient to 2H2SO4. The accompanying 4.4 eV must be interpreted per two-electron reaction event under specified cell conditions; it is not an exact universal chemical constant or a voltage of 4.4 V.
Add Pb+HSO4−→PbSO4+H++2e− and PbO2+3H++HSO4−+2e−→PbSO4+2H2O; cancel 2e− and one H+ to obtain Pb+PbO2+2H++2HSO4−→2PbSO4+2H2O, hence 2H2SO4. Left/right atom counts then agree. Two transferred electrons give available reversible electrical energy 2e ε, so 4.4 eV corresponds to ε=2.2 V. Primary DOE equation 4-1 corroborates the balanced net reaction. A primary calculation paper reports a different condition-specific experimental voltage (2.11 V); the slide supplies no activities/temperature to certify its 4.4 value.

D133-C02 | electrochemical_transport_cartoon_scope | lecture8.pdf, PDF 3,4,11, slides 6,7,21 | H+ arrows, open/closed cell explanation and internal current
The picture has H+ moving left against the drawn rightward electric field. Unlike the simple field-only electrolyte example in D132, this is an electrochemical cell with reactions and concentration driving; the arrow alone is not a proven sign error. The source reduces the full mechanism to electric-field inhibition and H+ transport.
Treat these as qualitative cell cartoons. Ionic electrochemical gradients, reaction kinetics and other electrolyte species are required for a quantitative transport/current model. No statement that all internal current is exclusively a proton flux or that all no-load microscopic motion ceases is justified.
At equilibrium it is the electrochemical potential μ̃=μ+qφ that is spatially balanced for a mobile species, not necessarily the separate electrical or chemical terms. A constitutive flux proportional to −grad μ̃ can run against E when grad μ is sufficiently strong. This is a reviewer model explanation, not a computed transport solution of the illustrated battery. Atomic/charge balance of the provided half-reactions is verified independently; rates and spatial fields are undetermined.

D133-E02 | emf_electric_field_integral_sign | lecture8.pdf, PDF 4, slides 7 | Integral below terminal-voltage definition
The text defines EMF=φ(positive terminal)−φ(negative terminal), but the displayed integral is +∫ from negative terminal to positive terminal E·ds. The image confirms there is no leading minus.
For electrostatic E, φ+−φ−=−∫_-^+ E·ds. Chemical EMF instead is non-electrostatic work per charge around the source/circuit; terminal voltage equals that EMF in the ideal/no-load model and is ε−Ir in the discharge series-r model.
E=−grad φ gives ∫_-^+ E·ds=φ−−φ+. A positive φ+−φ− therefore requires the missing minus, or a reversed integration path. Integrating the non-electrical force per charge inside the source can define ε, but that is not the electrostatic E shown in the source and cannot repair the notation silently.

D133-C03 | current_convention_and_kirchhoff_regime | lecture8.pdf, PDF 4,5,7, slides 8,9,14 | Current direction and Kirchhoff rules
Conventional current leaves a discharging battery at its positive terminal through the external passive load; inside the source it runs from negative to positive. The source phrases current + to − and no charge accumulation broadly.
Use lumped quasistatic circuits, negligible wire voltage drops, node charge storage neglected, and no unmodelled time-varying magnetic flux. In a charging source, terminal current reverses. KCL expresses local conservation with possible accumulation; KVL as a zero sum of electrostatic voltage changes needs conservative E or explicit induced EMF elements.
Integrating continuity gives ΣI_in−ΣI_out=dQ_node/dt, reducing to the displayed KCL when node storage is negligible. Faraday induction instead gives ∮E·dl=−dΦB/dt in SI (−(1/c)dΦB/dt in Gaussian units), so a changing linked flux cannot simply be discarded. Around a static resistor loop, +ε−IR=0 follows with passive-current direction.

D133-S01 | series_parallel_and_node_voltages_verified | lecture8.pdf, PDF 5,6,7,8,9, slides 10,11,12,14,15,16,17 | Series, parallel and labeled-node formulas
The resistor-reduction formulas and four displayed node-voltage expressions agree with the diagrams. Source ΔVi=−IRi is a signed change along current, whereas its later Vi in V−ΣVi=0 is the positive drop magnitude.
Make the two voltage conventions explicit. Define V_AB=φA−φB. All comparison inequalities assume positive finite resistors and at least two branches/elements; current increases/decreases statements hold at fixed applied voltage.
For S=R1+R2+R3, I=V/S and V_AB=VR1/S, V_BC=VR2/S, V_CD=VR3/S, V_AC=V(R1+R2)/S; omitted V_DA=−V. For parallel branches I=ΣV/Ri, hence 1/Req=Σ1/Ri and Req<min Ri; series Req=ΣRi>max Ri under the stated positivity. No additional physical resistance results from merely relabeling nodes.

D133-E03 | current_given_in_voltage_units | lecture8.pdf, PDF 7, slides 13 | F13 measurement prompt
The prompt says the known current is 135 mV, which has voltage units. The intended current value/unit cannot be recovered from this packet.
Do not silently substitute 135 mA. If the actual current I is independently supplied in current units, measure each element voltage and form its operating-point resistance V_i/I. Diodes and lamps need not have constant Ohmic resistance.
Dimensional analysis: [R]=[V]/[I]; mV alone cannot supply I. The voltmeter must have sufficiently high input resistance to avoid changing a branch voltage/current appreciably. For nonlinear elements, V/I differs from differential dV/dI; a single operating point does not determine their full constitutive law.

D133-S02 | f12_network_reduction_and_numerics | lecture8.pdf, PDF 9, slides 18 | Second circuit topology and ammeter
The lower network is an input series R followed by parallel branches R and R+RL; its ammeter measures total input current. This is not an infinite ladder or the current through RL alone.
With ideal source/wires/ammeter, Req=R+R(R+RL)/(2R+RL). At V=1.5 V, R=912 ohm and RL=1580 ohm, Req≈1579.656874 ohm, total I≈0.949573306 mA and load-branch current≈0.254409769 mA.
The top ideal calculation is 1.5/1580≈0.949367089 mA; the source labels 0.94 mA as an ammeter reading, not exact arithmetic. No precision/calibration data support calling this small measurement difference a false claim. Setting lower Req=RL gives 3R²=RL², so R=RL/√3≈912.213425 ohm: the given 912 makes the two input currents nearly identical while the load current changes substantially.

D133-E04 | two_source_current_solution_sign_error | lecture8.pdf, PDF 10, slides 19,20 | Second closed-form current on slide 20
The source loop equations and displayed I1 solution are correct, but its printed I2 numerator is (V1−V2)R2+V2R1. The last term must be negative for the displayed battery polarities and current directions. Slide 19 uses I1 for the central branch, while slide 20 reassigns I1 to R1; retain this notation change explicitly.
Let D=R1R2+R1R3+R2R3. Correct I1=[V1R3+(V1−V2)R2]/D and I2=[(V1−V2)R2−V2R1]/D; middle downward current is I1−I2=(V1R3+V2R1)/D.
The printed equations give (R1+R2)I1−R2I2=V1 and −R2I1+(R2+R3)I2=−V2. Matrix inversion gives the stated corrections. Countercheck V1=V2=V0, R1=R2=R3=R yields I1=V0/(3R), I2=−V0/(3R), middle=2V0/(3R); the printed positive I2 fails the right loop. A negative solution means actual current reverses its chosen arrow. Simple series/parallel resistor reduction alone is unavailable for this active topology; source transformations or node analysis remain valid.

D133-E05 | resistor_loop_traversal_sign | lecture8.pdf, PDF 10, slides 20 | Yellow sign guide, final bullet
The guide allows arbitrary current direction and clockwise/anticlockwise traversal but says voltage always drops on R.
For chosen branch current I, the signed change in potential is −IR when traversing along that current and +IR when traversing opposite. The actual dissipated power is nonnegative for a positive resistor regardless of traversal choice.
For a resistor from a to b with I oriented a→b, φa−φb=IR. Thus φb−φa=−IR while the reverse change is +IR. Reversing only the loop path flips every term in a correct loop equation; the source blanket drop rule would not.

D133-C04 | internal_resistance_and_heat_model_limits | lecture8.pdf, PDF 11, slides 21 | Equivalent source and maximum current
The ideal EMF plus positive constant series r model correctly gives I=ε/(Rload+r) and short-circuit limit ε/r. Calling chemical conversion itself dissipative conflates useful free-energy conversion, irreversible losses and reversible thermal effects.
Treat r and ε as model parameters for an operating range, not a universal guarantee of a real battery maximum. Real state, temperature, electrochemical overpotentials and time response are unspecified. The source short-circuit homework suggestion was inspected as historical content and was not performed or converted into a procedure.
Power balance in the simple model: εI=I²Rload+I²r, with terminal voltage ε−Ir. Chemical free-energy conversion can be reversible; thermodynamics distinguishes ΔG from ΔH via ΔG=ΔH−TΔS, so not all heat can be identified with I²r or all reaction energy described as lost. A quantitative battery thermal model is not supplied.

D133-S03 | power_formulas_and_units_verified | lecture8.pdf, PDF 11, slides 22 | Work and dissipated power
dW=Vdq and P=VI=I²R are correct with voltage defined as the passive element drop and current entering its higher-potential terminal.
Also P=V²/R for positive finite R. For a source, VI with the same passive convention may be negative, meaning electrical energy supplied.
Divide dW=Vdq by dt and use I=dq/dt, then V=IR. Units are joule/second=watt in SI and erg/second in Gaussian CGS, as displayed. Integrating P over time rather than using an unspecified constant gives energy for changing I and R.

D133-C05 | temperature_and_nonlinear_resistance_conditions | lecture8.pdf, PDF 12, slides 23 | Any resistor statement and lamp sawtooth prompt
A fixed Ohmic constant does not characterize every resistor. R(T) can vary during Joule heating; an increase with T is typical for metallic lamp filaments in the relevant range, not a universal material law.
V=IR can define an operating ratio R=V/I, but linear Ohm law requires fixed state and proportional response. For a changing-temperature I–V trajectory, its slope is not automatically 1/R(T). No exact lamp trace is determined by this slide.
If I=V/R(T), differentiating along a trajectory gives dI/dV=1/R−[V/R²](dR/dT)(dT/dV). A thermal balance such as Cth dT/dt=VI−P_loss(T), plus waveform, material law and initial temperature, is needed to predict time evolution or hysteresis. These are reviewer-supplied conditions; F16 data are not present.

Independent coverage

- Read all 12 complete original page texts and personally viewed every full sheet, including the title-only first sheet; 23 published slides, with printed slide 2 absent.
- Independently balanced both half-reactions and the total lead-acid reaction, checked EMF sign, current convention and energy-per-charge conversion.
- Read every circuit topology, source polarity, node/current arrow and equation; reduced all series/parallel examples and the F12 numerical network.
- Solved the two-source linear system independently and tested the equal-source/equal-resistor limiting case, exposing the I2 sign error.
- Checked conservation, power dimensions, temperature-dependent I–V slope and limitations of the simple internal-r model.

Technical disposition

Source review complete. Confirmed substantive errors include the net-reaction coefficient, EMF integral sign, current units in F13, I2 solution sign and unconditional resistor-loop drop rule. The circuit reductions are otherwise consistent with their diagrams under the recorded ideal/quasistatic conditions. Missing slide 2 is a published pagination gap, not an inferred unread required page.

Limits

- The intended current and unit in F13 cannot be determined from the packet; no replacement value is invented.
- Battery 4.4 eV lacks temperature/activities/operating conditions; exact empirical certification is unresolved and unnecessary to the balanced reaction and two-electron voltage relation.
- Quiz raw scores, measured F12 instrument accuracy and live demonstration outcomes are not supplied.
- The full electrochemical transport/thermal model is outside the source; the simple cartoons are not certified as a complete quantitative mechanism.
- Some NASA PDF retrievals and an arXiv HTML retrieval failed; they are not claimed read or used as proof. Primary sources successfully opened above are scoped corroboration only.

Primary corroboration

U.S. Department of Energy, DOE-HDBK-1011/2-92 Electrical Science Volume 2 | https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1011-92_VOL2.pdf | PDF 54 (zero-based P53), printed ES-04 page 6, equation 4-1; PDF 55, equation 4-2 | retrieved 2026-10-08
Opened and relevant extracted reaction text inspected. Corroborates the coefficient 2H2SO4 and charge/discharge reversal. This is a scoped external check, not a claim to read all 118 pages or adopt its simplified microscopic prose.

Ahuja et al., Relativity and the lead-acid battery | https://arxiv.org/abs/1008.4872 | Primary author abstract, submitted 2010; linked Physical Review Letters 106, 018301 | retrieved 2026-10-08
Opened primary abstract reports calculated 2.13 V and comparison experimental 2.11 V. Used only to establish that the slide’s 4.4 eV is not a universally fixed exact energy without conditions; no detailed relativistic calculation or standard-state conversion is claimed.

