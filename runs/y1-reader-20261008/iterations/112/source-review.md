# D112 — original-source technical preparation

Review date: 2026-10-08. Source-only review: no teaching route, SASIS, reader test, repository change, or iteration closure. No student baseline/reader reports loaded. Original PDFs and audit cache preserved.

## Assignment and integrity

**D112 / mit-8-02t-spring2005-S12 / studio 12 / original order 112 / active order 41.** Title: **Hour 1 Working with Circuits Experiment 4: Part I: Measuring V, I, R Hour 2 RC Circuits Experiment 4: Part II: RC Circuits**. Exact assignment was selected from `runs/y1-reader-20261008/readability-selection.json` and the D112 row of `readability-audit/teal.json`: **entire Chapter 7**, entire presentation, entire associated PRS. The [official lecture index](https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2005/pages/lecture-notes/) row is recorded verbatim in the map. No neighboring session was substituted.

| Alias | Exact original PDF basename | Assigned pages | SHA-256 |
|---|---|---|---|
| C7 | `01decae81aae80df6e65d8831582764a_chap7dc_circuits.pdf` | All 28, including contents and every exercise; printed 0–27 | `31ca5032b01dfa04f5b803a37f8326106cd01433b5cd3f43146a226e97d33cbe` |
| P | `9965e4e342f728436d23e0e191a58e2a_presentati_w05d1.pdf` | All 23 | `3951507e5d3876cc1e2c6a4f6bd85c7a0fe9ebcf950cb503731a0e500fdbba76` |
| Q | `2aa16359b5c77376d08f3301645fefa1_prs_w05d1.pdf` | All 6; three question/answer pairs | `6751b5e62bec7888863c494395a3395fa4c515eb0ab6b3c5b7b65277d73b235f` |

All **57/57 required pages** were freshly read and opened as full-page renders for this packet, including C7 pages previously assigned elsewhere. This is a new complete reading, not credit transferred from another report or the audit. Original PDF hashes, byte counts and page counts were checked. Every cached PNG was checked for nonzero size, successful decoding/loading and dimensions, then visually inspected. No failed cached derivative was established.

P6 initially appeared incompletely displayed. An independent PyMuPDF render at scale 1.6 was **byte-for-byte and pixel-for-pixel identical** to the cached PNG, ruling out a cache-content defect. A scale-2 full-page rendering was opened and the entire text/diagram read; it is retained as `P-p006-verification.png` with its provenance/hash in the map. The issue was resolved display uncertainty, not original-source clipping. No replacement was written to cache. P5–7 footers lack page numerals (P12– only); other P footers correspond to their PDF numbers. Q has no printed page numbering. Chapter printed page = PDF page minus one.

Inspection batches: P1–8,9–16,17–23; Q1–6; C7 1–3,4–9,10–15,16–21,22–25,26–28. Every equation, graph, diagram topology, component value, arrow/polarity, table row, and supplied answer within these pages was included.

## Confirmed findings and model qualifications

Two unambiguous source-error groups:

| ID | Exact locator | Finding and resolution |
|---|---|---|
| E1 | C7 PDF15 / printed14, paragraph between Eq.7.6.24 and Fig.7.6.8 | The prose calls Fig.7.6.8 the voltage graph. It is the **current** graph; the voltage graph is Fig.7.6.7 immediately above. Both plotted functions are correct. |
| E2 | C7 PDF22 / printed21, §7.9.3(c), definition of I′ and final equation | I′=dq′/dt is explicitly **negative** during discharge. The final equation then writes I=I₁+I′ but evaluates it as the sum of positive magnitudes. For downward switch current the correct signed relation is **I=I₁−I′=ε/R₁+(ε/R₂)e^(−t/R₂C)**. The printed final positive expression and physical downward direction are correct; its equality to I₁+I′ is not. |

Other claims need stated conditions rather than indiscriminate error labels:

- **P3, C7 §§7.2–7.4:** Resistances are fixed, positive and Ohmic. R=ρl/A assumes a uniform specimen and material state. Signed potential changes and positive drop magnitudes must be distinguished. Ideal wires are equipotential; actual wire resistance is neglected. Kirchhoff's node rule assumes no continuing node-charge accumulation; the electrostatic loop integral assumes no changing linked magnetic flux. Battery EMF supplies non-electrostatic work. The ε−Ir terminal-voltage expression is for the shown discharging direction, not a charging battery with the same signed I.
- **C7 PDF6–7:** A dominant series resistor must dominate the sum of the others, and a dominant parallel branch must dominate the sum of other conductances. Saying every other branch current vanishes for a merely near-zero short is a limiting approximation. An ideal nonzero EMF source connected directly to an ideal short is not a finite-current circuit model.
- **P5–7, C7 PDF9:** Voltmeter resistance should be large relative to the measured circuit's source resistance; ammeter burden should be small relative to its branch. The stated 1 Ω on a 250 mA range is a particular course instrument claim, not a universal multimeter specification; 0.25 V at full scale checks arithmetically. P7's ohmmeter-across-R₁ drawing reads R₁ only when other paths do not complete a parallel circuit and there is no external excitation. A measurement may use a known test current or voltage; the source's applied-voltage description is not every meter's implementation. Manufacturer guidance independently confirms de-energized measurement, discharged capacitors and the parallel-path limitation [A]. No experiment was performed.
- **C7 PDF9–10 resistor chart:** The stated two digits + multiplier + tolerance is the four-band convention. Gold/silver entries −1/−2 are powers of ten for the multiplier, not negative significant digits. The example yellow/orange/black/gold is 43 Ω ±5%, confirmed against a manufacturer chart [B]. Five/six-band coding is outside that compressed description.
- **P10–18 and C7 §7.6:** Charging formulas assume q(0)=0, constant ideal ε, fixed R,C and negligible inductance/leakage. Capacitor voltage is continuous absent impulsive current. A capacitor behaves like a short only at the instant its voltage is zero in this ideal initial-condition calculation; “fully charged” means approaching Cε for this source, not a universal physical capacity to hold no more charge. The exponential reaches its limit only asymptotically. Charging uses I=+dq/dt, whereas positive discharge current uses I=−dq/dt; the different arrow conventions are explicit.
- **P18:** The graph inherited from the chapter writes V₀=Q/C while the nearby slide equation uses Q₀ for initial charge. Interpret the graph's Q as the initial charge; the instantaneous relation is V(t)=Q(t)/C. This is mixed notation, not an independently wrong decay constant.
- **P19:** “All quantities” is too broad if read literally. For a single linear RC state variable after a constant-source step, x(t)=x∞+(x₀−x∞)e^(−t/τ); the two displayed zero-initial or zero-final cases are special cases. Energy is quadratic (for discharge U∝e^(−2t/RC)); a multi-capacitor network may have multiple modes. The coefficient of d/dt is τ only after the equation has been normalized so that the coefficient of the state variable is one. These are necessary restrictions on the slide's generalization.
- **P20:** A drop by e identifies τ for an exponential measured relative to its correct asymptote. An offset signal requires subtraction of that offset. Endpoint exclusion in a fit is an experimental judgment for transients/noise/saturation, not a theorem that all endpoint data are invalid. No actual fit, dataset or measured τ is supplied.
- **C7 PDF22, §7.9.3(a):** The displayed pre-closing charging function uses a time origin at the beginning of an earlier charging process. The problem sets t=0 at the later closing event after a long open interval. That earlier expression needs a separate time variable or initial-time statement; at the stipulated closing event q(0)=Cε, not zero. The stated before/after time constants and post-closing solution remain correct.
- **C7 PDF23–24, §7.9.4:** Electrical power comparison for fixed R and fixed ideal terminal voltage is correct. Translating electrical power rankings or ratios into actual visible brightness requires lamp characteristics; incandescent R changes with operating temperature, as the independent MIT lab explains [C]. No exact optical measurement follows from these diagrams.
- **C7 PDF20–21, §7.9.2:** Maximum-load-power condition R=r assumes fixed ε and r>0. It is not maximum efficiency: half the source power is dissipated internally there. An ideal r=0 source has no finite positive-R maximum. The problem is a mathematical model, not equipment-selection guidance.

## Page and figure coverage

| Asset/PDF pages | Entire required content inspected |
|---|---|
| P1–4 | Outline, resistor recap, full uniform-wire geometry, series/parallel circuits and equations; measurement transition. |
| P5–8 | Voltmeter parallel, ammeter series, ohmmeter across R₁ with R₂ dangling, all symbols/polarities, comparative meter resistance statements; experiment-I title. P6 independently rerendered/read as above. |
| P9–14 | RC transition; charging/discharging plate-current signs; open/closed charging circuit, loop equation, separated-variable integral and exponential; both q(t) and I(t) graphs with 0.632/0.368 at τ. |
| P15–18 | PRS transition; discharge open/closed diagrams, current arrow, initial Q/Q₀ and capacitor voltage, differential/integral equations, voltage graph. |
| P19–23 | Both general-response plots, formula conditions, two marked points for an e-fold time interval, fit advice, demonstration/experiment-II titles, final multiloop PRS prompt. Titles are not completed demonstrations. |
| Q1–2 | Initially uncharged series RC; late current question and key **1**, nearly zero, checked by I=(ε/R)e^(−t/RC). Diagram shows the post-closing configuration. |
| Q3–4 | Same circuit, initial current question and key **2**, maximal and decreasing; I(0+)=ε/R and derivative negative. |
| Q5–6 | Three-resistor multiloop diagram, switch, ε,C, all current arrows; late central current key **2**, ε/(2R), since capacitor branch carries zero steady current. The switch is still drawn open in the reused diagram, but both text and answer explicitly specify the closed-switch state. This graphic-state mismatch is recorded; it does not change the intended topology. |
| C7 PDF1 / printed0 | Contents: all §§7.1–7.11.6 included, no partial reading boundary. |
| C7 PDF2 / printed1 | §7.1, Fig.7.1.1 both bulb wiring diagrams, component-symbol table and switch text. |
| C7 PDF3 / printed2 | Open/short/ground descriptions; §7.2, Eq.7.2.1, Fig.7.2.1 battery/resistor. |
| C7 PDF4 / printed3 | Eqs.7.2.2–6, Fig.7.2.2 current/loop, Fig.7.2.3 both internal-r circuit and potential profile, all a–e labels and rises/drops. |
| C7 PDF5 / printed4 | Eqs.7.2.7–8 power; §7.3 series circuit/equivalent Fig.7.3.1, Eqs.7.3.1–2. |
| C7 PDF6 / printed5 | Eq.7.3.3, Fig.7.3.2 both parallel/equivalent diagrams, Eqs.7.3.4–6, branch/node arrows. |
| C7 PDF7 / printed6 | Parallel limiting argument; §7.4 and Fig.7.4.1 junction; Eq.7.4.1 and loop-rule text. |
| C7 PDF8 / printed7 | Eq.7.4.2; all four Fig.7.4.2 sign panels; divider Fig.7.4.3 and Eq.7.4.3. |
| C7 PDF9 / printed8 | Divider Eqs.7.4.4–6; all §7.5 measurement prose, course-meter values and complete resistor-color table. |
| C7 PDF10 / printed9 | Tolerances/example; §7.6.1 and Fig.7.6.1 open/closed charging; Eqs.7.6.1–2; both capacitor sign panels Fig.7.6.2. |
| C7 PDF11 / printed10 | Eqs.7.6.3–9, charging ODE, integration bounds, logarithm and initial condition. |
| C7 PDF12 / printed11 | Fig.7.6.3 charge graph; Eqs.7.6.10–13, limiting charge/voltage/current. |
| C7 PDF13 / printed12 | Figs.7.6.4–5 current and voltage plots; Eqs.7.6.14–16; dimensional proof of seconds, e-fold and 0.632 values. |
| C7 PDF14 / printed13 | §7.6.2, both Fig.7.6.6 diagrams, counterclockwise discharge and electron/conventional-current directions, Eqs.7.6.17–20. |
| C7 PDF15 / printed14 | Eqs.7.6.21–24 and Figs.7.6.7–8 discharge voltage/current; reference typo E1. |
| C7 PDF16 / printed15 | Complete §7.7 summary and §7.8 introduction. |
| C7 PDF17 / printed16 | All five circuit-solution steps, independent-equation condition and all six resistor/EMF/capacitor sign panels. |
| C7 PDF18 / printed17 | Figs.7.8.1–2, source polarities, resistor/current labels and node/loop equations. |
| C7 PDF19 / printed18 | Remaining loop relations and all three solved currents; §7.9.1 resistor network Fig.7.9.1. |
| C7 PDF20 / printed19 | Complete equivalent-network algebra; §7.9.2 variable-load power function. |
| C7 PDF21 / printed20 | Power derivative and maximum graph Fig.7.9.2; §7.9.3 Fig.7.9.3, switch location and all three questions. |
| C7 PDF22 / printed21 | All before/after RC solutions and switch-current signs; start §7.9.4. |
| C7 PDF23 / printed22 | Both Fig.7.9.4 connections and all parts (a)–(e); parallel powers and lamp interpretation. |
| C7 PDF24 / printed23 | Full parallel/series source-load power equalities and current relations. |
| C7 PDF25 / printed24 | Power comparison; §7.9.5 Fig.7.9.5 cube, every edge and a–g label, symmetry currents and voltage path. |
| C7 PDF26 / printed25 | Cube result, all four conceptual questions, §7.11.1 both battery-connection figures and first two parts. |
| C7 PDF27 / printed26 | §7.11.1 comparison; §§7.11.2–4 all statements and Figs.7.11.2–4 with every source polarity/value, resistance and ladder branch. |
| C7 PDF28 / printed27 | §§7.11.5–6 all conditions/parts; Figs.7.11.5–6, RC values, resistor-network values, final 7.5 V answer. |

The Q5–6 reused open-switch artwork is a third, graphic-state finding separate from the two algebra/reference groups. The question/answer text supplies the intended closed state unambiguously.

## Independent mathematical checks

The following checks include reviewer deductions for unworked questions; they are not attributed as printed solutions or as an authored teaching route.

Charging/discharge ODEs were checked by differentiation and boundary substitution: q=Cε(1−e^(−t/RC)), I=(ε/R)e^(−t/RC), discharge q=Q₀e^(−t/RC), I=(Q₀/RC)e^(−t/RC). Their plotted initial values, asymptotes, concavity, signs and τ ordinates agree. More generally a single-capacitor linear network has τ=Rseen C after independent ideal voltage sources are suppressed; this extends the simple circuit only under the stated linear model. The Q5 topology gives i₂(∞)=0 and i₁=i₃=ε/(2R); the key does not require solving the full transient.

| C7 item / locator | Independent result and comparison |
|---|---|
| §§7.2–7.4, PDF3–9 | I=ε/(R+r); terminal V=ε−Ir; Iε=I²R+I²r. Series and parallel reductions and unloaded divider Vout/Vin=R₂/(R₁+R₂) all check. |
| §7.8, PDF18–19 | With D=R₁R₂+R₁R₃+R₂R₃, printed I₁=[ε₁R₃+ε₂(R₂+R₃)]/D, I₂=−[ε₁(R₁+R₃)+ε₂R₃]/D and I₃=(ε₂R₂−ε₁R₁)/D satisfy I₁+I₂=I₃ and both loop equations. I₂<0 for positive displayed EMF magnitudes/resistances; I₃ may have either sign. |
| §7.9.1, PDF19–20 | Rtotal=R₁+R₁(R₀+R₁)/(R₀+2R₁); setting Rtotal=R₀ gives positive root R₁=R₀/√3, correct. |
| §7.9.2, PDF20–21 | P=ε²R/(R+r)²; derivative ε²(r−R)/(R+r)³ changes + to − at R=r>0. Pmax=ε²/(4r), supplemental check. |
| §7.9.3, PDF21–22 | Before closure τ=(R₁+R₂)C and q(0)=Cε after long charging. After closure τ′=R₂C; downward switch current ε/R₁+(ε/R₂)e^(−t/R₂C). This confirms the final magnitude while exposing E2's incompatible intermediate sign. |
| §7.9.4, PDF22–25 | Parallel Pk=ε²/Rk; series Pk=ε²Rk/(R₁+R₂)²; in both configurations source power equals sum of resistor powers. Pparallel/Pseries=(R₁+R₂)²/(R₁R₂)≥4 for positive R. |
| §7.9.5, PDF25–26 | Opposite cube vertices: three entrance edges carry I/3, six middle edges I/6, three exit edges I/3. Along a–c–d–b, drop is IR(1/3+1/6+1/3)=5IR/6. Printed Req=5R/6 correct. |
| §7.10, PDF26 | Three positive resistors: all series maximizes and all parallel minimizes Req when all are included without bypasses. Starter current can reduce terminal voltage via source/lead impedance, dimming shared lamps; actual regulated systems may differ. Single ideal series-RC final Q=Cε does not depend on R, though charging time does. A zero external terminal voltage is the ideal short-load limit for a battery model with finite internal r, not an instruction to short a physical battery. |
| §7.11.1, PDF26–27 | Series Is=2ε/(R+2r); parallel Ip=ε/(R+r/2). Equal for R=r, series larger for R>r, parallel larger for R<r, with identical aligned batteries and positive R,r. Current in external R is left-to-right in the figures. |
| §7.11.2, PDF27 | Choose common bottom/right node 0 V. Top-right source node=30 V, lower-left node=10 V, central top x, upper-left=x+20 V. KCL: (x+10)/2+x/4+(x−30)/5=0, giving x=20/19 V. Currents: 2 Ω downward 105/19 A; 4 Ω downward 5/19 A; 5 Ω right-to-left 110/19 A. They conserve charge at the central node. No printed key. |
| §7.11.3, PDF27 | 1 Ω∥3 Ω=3/4 Ω, total=27/4 Ω, source current=80/27 A, parallel voltage=20/9 V. Powers: 2 Ω:12800/729 W; 4 Ω:25600/729 W; 1 Ω:400/81 W; 3 Ω:400/243 W. Sum=1600/27 W=20 V×80/27 A. No printed key. |
| §7.11.4, PDF27 | Self-similar ladder X=2R₁+(R₀X)/(R₀+X) gives X²−2R₁X−2R₁R₀=0; positive finite resistance is R₁+√(R₁²+2R₁R₀), as printed for positive resistances. |
| §7.11.5, PDF28 | At t=0+, C has zero voltage, so R₂∥R₃=12/5 Ω and total=52/5 Ω. I₁=50/13 A left-to-right; I₂=20/13 A downward; I₃=30/13 A downward. At infinity R₃ current=0; Vc=40×6/(8+6)=120/7 V, top plate positive; Q=480/7 μC≈68.6 μC. No printed key. |
| §7.11.6, PDF28 | Middle branch is 3 Ω+5 Ω across ideal 12 V; I=1.5 A, hence 5 Ω drop=7.5 V, printed answer correct. Other branch is (6 Ω∥12 Ω)+4 Ω=8 Ω; it does not alter ideal supply voltage. |

## Independent primary checks and limits

- **[A] [Fluke, How to Measure Resistance with a Digital Multimeter](https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-resistance), steps 1–2 and final parallel-path discussion.** Confirms external excitation/stored-charge and parallel-path restrictions; no particular course-meter model or measurement accuracy was verified.
- **[B] [Vishay, Color Code and Standard Resistance Series, document 20143](https://www.vishay.com/docs/20143/colorcod.pdf), one-page four-band diagram and color table, revision 28-Aug-2009.** Supports the stated digits, multiplier and tolerance conventions, including gold ±5% and silver ±10%; not used to claim all resistors have four bands.
- **[C] [MIT 6.200 Spring 2026 laboratory](https://circuits.mit.edu/S26/labs/pots), §5, independently inspected during the same source-preparation session.** Establishes temperature-dependent incandescent resistance; it provides no optical brightness law for the chapter's examples.

All exact source and derivative hashes and page-level coverage are in `source-map.json`. **57 required pages, 3 original PDFs, 3 inspected PRS pairs, two algebra/reference error groups plus one reused switch-state graphic discrepancy.** No required symbol, equation, figure role or answer indication remains unreadable after the P6 display check. Laboratory instructions are only those actually present in these assigned assets; the title-only experiment slides do not provide missing apparatus procedures, measurements or demonstrations. Instrument specifications, actual lamp optical output, experimental fitting choices and nonideal transient behavior remain conditional. This packet is source preparation, not an authored or closed iteration.
