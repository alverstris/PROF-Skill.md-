# D111 — original-source technical review

Review date: 2026-10-08. This is source preparation only. It is not an authored teaching route, a reader test, a SASIS review, or closure of a PROF iteration. No student baseline or reader report was loaded. Original PDFs and cached renders were not changed.

## Exact selection and provenance

The selected record is **D111 / mit-8-02t-spring2005-S10 / studio 10**, original order **111**, active order **40**: **Hour 1 DC Circuits Hour 2 Kirchhoff’s Loop Rules**. Mapping and boundaries come from `runs/y1-reader-20261008/readability-selection.json` and the D111 row of `readability-audit/teal.json`, read as individual records. The official [lecture index](https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2005/pages/lecture-notes/) assigns Chapter 6, Chapter 7 sections 7.1–7.4, the presentation, and the PRS packet. Adjacency was not used to infer the assignment.

All assets below are under `/workspace/scratch/ac36b9c5ff31/prof-readability/audit-teal/pdfs/`. Their exact official URLs, byte counts, original hashes, assigned page lists, and individual render hashes are in `source-map.json`.

| Alias | Original filename | Assigned coverage | SHA-256 |
|---|---|---|---|
| C6 | `6b2cf7ec2d597d7459930a7e6f700bea_chapter6current.pdf` | Entire PDF, 1–18; printed 0–17, including contents and all exercises | `b10917ed0722e38786c5f9f5a58478445adfb12467e3cd684069ef7ac7e2b423` |
| C7 | `01decae81aae80df6e65d8831582764a_chap7dc_circuits.pdf` | PDF 2–9, printed 1–8; starts at §7.1 and ends immediately before §7.5 on PDF 9, including Eqs. 7.4.4–7.4.6 | `31ca5032b01dfa04f5b803a37f8326106cd01433b5cd3f43146a226e97d33cbe` |
| P | `3b7c9888831050a61eeee17e59ad5bda_presentati_w04d2.pdf` | All 41 pages/slides | `2b27d1f41bc4c7b114fd495811171d5f5001077b5f137eb7a3d02ad8a6d10011` |
| Q | `a0410ea67d4d1545e933b59f33500928_prs_w04d2.pdf` | All 10 pages, five question/answer pairs | `4899b863b115b7f181f064f2218dd1ef07cac9f20bb7fcc3c473ae929cc20de7` |

**77/77 required page occurrences were freshly read and visually inspected**, using the original text and every full-page cached render, not audit descriptions alone. P footers normally read P10–n; PDF 3, 4, and 30 have only P10–, so their PDF page numbers are the reliable locators. Q footers say PRS10 without individual page numbers. Chapter printed-page numbers are PDF minus one. C7 PDF 1 and PDF 10–28 are outside the assignment. Content below §7.5 on the boundary page was visible but is not credited as assigned reading.

Full-page batches: P 1–9, 10–18, 19–27, 28–36, 37–41; Q 1–5 and 6–10; C6 1–5, 6–12, 13–18; C7 2–5 and 6–9. A truncated attempted batch of C6 13–18/C7 2–5 was not credited; these pages were reopened in complete smaller batches. P 3, 34, 38, and 39 were additionally reopened to check scope, circuit topology, and signs. The small P12 labels E, I, J=I/A, and A are readable in the full-page render.

## Confirmed source findings

Seven grouped findings are distinguished from conditional models and unresolved empirical claims below. The first group has two separate slide occurrences.

| ID | Exact locator | Finding and supported resolution |
|---|---|---|
| E1 | P PDF 38/P10–38 and PDF 39/P10–39, boxed power equations and the diagrams directly above them | Each diagram defines ΔV as the signed change moving with current: −IR for the resistor and −Q/C for the charging capacitor. The boxes then incorrectly equate **positive dissipated/absorbed power to IΔV**. With those definitions, the first product must be **−IΔV**. Thus resistor absorption is I²R, and capacitor absorption is (Q/C)dQ/dt=d(Q²/2C)/dt at fixed C. Alternatively a positive voltage-drop variable could be introduced explicitly. The displayed signs cannot all be true with one ΔV definition. |
| E2 | C6 PDF 3/printed 2, §6.1.1 paragraph following Eq. 6.1.4 | Drift speed is called the average speed of the carriers. It is the magnitude of their **mean velocity**, not the mean magnitude of rapid random velocities. Equations 6.1.5–6.1.10 use the mean velocity correctly. |
| E3 | C6 PDF 12/printed 11, §6.5.4 paragraph immediately above dR | The text calls the slice thickness dy although the coordinate, radius function, integral, and differential are x and dx. This is a coordinate typo; the displayed dR is correct. |
| E4 | C6 PDF 13/printed 12, sentence following the cone integral | The a=b limit reproduces **Eq. 6.2.10**, R=ρl/A, not Eq. 6.2.9, which defines resistivity as reciprocal conductivity. |
| E5 | C6 PDF 16/printed 15, §6.7.5, paragraph below Fig. 6.7.2 | The moving charged sheet is in the **right** panel, not the left panel named by the prose. The left panel contains parallel wires. Directions and K=σv remain consistent. |
| E6 | C6 PDF 18/printed 17, §6.7.8(c), bracketed answer | The traversal is explicitly right to left, from 0 to +V. The three positive changes sum to a **potential rise** V, although the answer calls it a drop. Their magnitudes are correct. |
| E7 | C6 PDF 7/printed 6, resistivity/conductivity table, Platinum row | The displayed pair ρ=10.6×10⁻⁸ Ωm and σ=1.0×10⁷ (Ωm)⁻¹ does not satisfy the immediately preceding definition σ=1/ρ at the displayed precision: reciprocal of the stated ρ is 9.43×10⁶, about 6% below the tabulated σ. This is an internal numerical inconsistency; it does not establish which experimental table entry should be replaced. |

## Conditions, conventions, and unresolved claims

- **P3 dielectric recap:** Q²/(2C), Q|ΔV|/2, and C|ΔV|²/2 agree for a linear fixed-geometry capacitor. The further equality to ∫ε₀E²/2 is the vacuum-field expression and must not silently be used for total stored energy in a polarizable medium with macroscopic E. For a linear nondispersive dielectric the appropriate macroscopic stored-energy density is E·D/2. C=κC₀ requires the relevant field region to be filled with the same linear isotropic dielectric; arbitrary partial filling is not covered. These are scope restrictions on a compressed recap, not newly asserted numerical errors.
- **P8–12; C6 §§6.1–6.2:** I=∫J·n dA is general; I=JA needs a uniform normal component. E=ρJ and scalar σ assume local isotropic Ohmic behavior at a specified material state. A resistive conductor carrying current has an internal field and need not be equipotential; the assertion does not apply to the ideal zero-resistance wire abstraction. Drift depends on carrier density and current density, not just material name.
- **C6 PDF 4–5, Eqs. 6.1.7–6.2.2:** The Drude result σ=ne²τ/m is consistent with randomizing collisions and a relaxation time. The printed argument passes rapidly from velocity before a collision to an ensemble drift velocity. A constant collision probability per unit time makes the mean time since the last collision equal to τ; a model in which every free flight lasts exactly τ does not justify the same averaging. This is a missing statistical assumption, not evidence that the displayed conductivity formula is wrong. An independent primary lecture source explicitly supplies it [B].
- **P10:** 4×10⁻⁵ m/s equals 0.04 mm/s. At that drift speed, one metre takes 25,000 s=6.94 h, while the slide says about 10 h. Treat that phrase only as an order-of-magnitude illustration. Electrical response is a propagating field/circuit disturbance, not the arrival of one electron from the source. No specific signal speed or startup time is established for this diagram; a transmission-line derivation gives v=1/√(L′C′), with c only under its additional vacuum/perfect-conductor assumptions [D].
- **C6 PDF 2/printed 1:** The phrase putting “common currents” at mega-amperes in lightning is not corroborated as a typical scale. NWS gives about 30,000 A for a typical flash [C]. This review does not rule out exceptional larger events or settle a maximum; the source's broad scale claim should not be presented as a typical measured value. The nerve-current comparison is likewise an illustrative scale without a specified anatomical or measurement context and was not independently quantified.
- **C6 PDF 6–7/printed 5–6, Eq. 6.2.11, table; PDF 14/printed 13, conceptual question 2:** The linear temperature law is an approximation and depends on material and temperature range. The question's increase-with-temperature premise needs an ordinary-metal condition; the same source table includes negative coefficients. Its placement of generic graphite under semiconductors does not establish a universal band classification or isotropic resistivity: primary measurements identify natural single-crystal graphite as an anisotropic semimetal [E]. Table entries are nominal values, not a newly validated database for unspecified samples, directions, or temperatures. Apart from E7, no recalibration of the table is claimed.
- **C6 PDF 10–11 and 17–18, current interfaces:** With equal cross sections in steady state, J is continuous, E=ρJ, and total surface charge is ε₀ times the normal E jump. If free interfacial charge in polarizable materials is sought, the D jump and material permittivities are needed. The source's ε₀ expressions are valid as total-charge statements (or its simple equal-background-permittivity model), not an unqualified identification with free charge. Ideal metal endcaps have zero interior field in that model; real resistive electrodes need an approximation.
- **C6 PDF 11/printed 10, seawater example:** Using n=6×10²⁰ cm⁻³ adds both ionic populations. The answer 2.5×10⁻⁵ cm/s is the population-weighted mean of **drift-speed magnitudes** in this two-carrier conductivity calculation. Positive and negative ions drift oppositely; the calculation does not show that each species has this individual speed, and the number-weighted vector mean is a different quantity.
- **C6 PDF 12–13 and 15, tapered resistance:** R=∫ρ dx/A(x) follows the stated cross-section-uniform/one-dimensional approximation, explicitly motivated by small taper in §6.7.3. It is not an exact three-dimensional current-flow solution for every cone geometry.
- **C6 PDF 14/printed 13, §6.7.1(c):** “Area traversed by the sphere” is not geometrically defined. A plane perpendicular to the instantaneous direction with cross-sectional area π(10 mm)² yields the current-density value given below; an orbital disk or swept annulus would require the orbital radius. That interpretive ambiguity remains open. The quantity 100π rad/s is an angular frequency, despite being called a rotation frequency.
- **C6 PDF 15/printed 14, §6.7.2:** The printed approximate answers ~10 A and ~10 Ω are very coarse; direct calculation gives 13.0 A and 8.82 Ω. They are not suitable as precise check values. The stated 4.18 J conversion is for a small calorie; one kilocalorie is 4180 J. The capitalization of “Calorie” should not be mistaken for the nutritional kilocalorie.
- **P20–22, 29–33; C7 §§7.2–7.4:** Voltage signs refer to a chosen traversal, whereas “drop” sometimes denotes a positive magnitude. Kirchhoff's node equation assumes no continuing node-charge accumulation. The zero closed-loop electrostatic-field integral assumes no changing linked magnetic flux; battery EMF represents non-electrostatic energy input per charge. Real-battery terminal voltage ε−Ir is for the shown discharging current; it changes sign in the resistive correction when current reverses. Constant ideal ε, r, R are circuit models. A nonzero but small r is not a universal material fact.
- **P36–40:** Writing d(qΔV)/dt=ΔV dq/dt on P36 assumes ΔV is fixed in that derivative. The general instantaneous two-terminal power relation follows instead from incremental work dW=v dq, with a declared current/voltage convention. U=qV is not the accumulated energy of a capacitor charging from zero. P39's current arrow describes charging plate currents; conduction current does not pass through an ideal dielectric. P40's energy balance is correct for fixed C and ideal components.
- **C7 PDF 7–9/printed 6–8:** The approximation that the smallest parallel resistance dominates requires it to dominate the *sum* of other conductances, particularly for many branches. A finite near-short does not literally make every other branch current zero. The divider ratio R₂/(R₁+R₂) assumes an unloaded output (or an explicitly incorporated load), positive resistances, and the shown source polarity.
- **Q PDF 5–6 and 9–10:** Halving current and quartering each bulb's dissipated power require identical **fixed-resistance** bulbs and an ideal voltage source. Interpreting that power ratio as an exact ratio of visible brightness adds another assumption. Incandescent resistance changes with temperature, confirmed by a separate MIT laboratory source [A]. Neither a bulb I–V curve nor its optical output law is supplied. The literal brightness ratio is therefore unresolved, while the intended ideal-model key is identifiable. No arbitrary replacement answer has been imposed.

## Complete content and figure coverage

The following ledger records the required text, mathematics, and visual roles. All mentioned source formulas and supplied answers were independently checked; unworked solutions below are labeled reviewer deductions. A title or demonstration placeholder was inspected as such and was not treated as a completed demonstration.

### Presentation and PRS

| P PDF / footer | Text and full-page visual content checked |
|---|---|
| 1–4 / 1,2,unnumbered,unnumbered | Studio outline, recap/transition headings, capacitor calculation recipe, energy identities, dielectric flux and C multiplier. P3 scope restriction above. |
| 5–7 / 5–7 | Battery/resistor and switch/RC pictures; average/instantaneous current; charge-flow direction for positive and negative carriers. No completed RC solution appears here. |
| 8–12 / 8–12 | Oblique area/current-density diagram; conducting material and field; random microscopic path, drift arrow and E arrow; density/scattering explanation; microscopic Ohm-law cylinder with E,I,J,A labels. P10 numerical qualification and E2 above. |
| 13–14 / 13–14 | Temperature/resistance demonstration title and PRS resistance prompt. No demonstration measurements supplied. |
| 15–17 / 15–17 | Uniform-wire geometry and endpoints Va,Vb, integration path, E,J,I,A,l,ρ and R derivation, ohm unit. Here ΔV=Vb−Va is positive while the integration path runs a→b against the field; no sign error in −∫aᵇE·ds=El. |
| 18–22 / 18–22 | Physical circuit images and schematic symbols; both battery polarities, both resistor-current directions, and both capacitor-plate polarities. All signed ΔV rules checked against traversal a→b. |
| 23–26 / 23–26 | Bulb wiring diagrams; series and parallel resistor derivations and current branches; PRS prompt. Equivalent resistance formulas correct under fixed Ohmic R. |
| 27–30 / 27–29,unnumbered | Kirchhoff transition; labeled node; battery/internal-r/load circuit and potential trace; battery terminal-voltage model. Rise ε, drop Ir, constant wire segments, drop IR checked in order. |
| 31–33 / 31–33 | Loop-solving instructions, branch reduction with two R/2 resistors and a 2ε source, mesh arrows I₁,I₂, equations and signed solution. All topology and source polarities checked. |
| 34 / 34 | Two group-problem drawings, both batteries and polarities, meters, a,b terminals, each resistor, and equivalence of the harder diamond to the easier middle R. No source answer; reviewer deduction below. |
| 35–37 / 35–37 | Power transition, incremental-work calculation and battery-supply sign. P36 derivative restriction above; battery supply Iε agrees with depicted current from − to +. |
| 38–40 / 38–40 | Resistor power, capacitor charging, RC circuit arrows and source/plate polarities; two erroneous power products distinguished from correct positive-energy formulas; correct RC conservation equation. |
| 41 / 41 | Final light-bulb power/brightness PRS prompt. |

| Q question/answer PDF pages | Marked source answer | Independent check and status |
|---|---|---|
| 1 / 2 | **3**, proportional to length and inversely to cross-sectional area | R=ρL/A at fixed material state. Correct. |
| 3 / 4 | **1**, battery current increases after an identical parallel bulb is added | At ideal fixed V, each identical branch retains the original operating point; total current doubles. Correct, even for identical nonlinear steady bulbs. |
| 5 / 6 | **2**, battery current decreases after an identical series bulb is added | Fixed-R model: total R doubles, I halves. Qualitative decrease also fits ordinary monotonic lamp I–V behavior; exact half is model-dependent. |
| 7 / 8 | **2**, battery power is twice as large with a second parallel bulb | P=VI and total I doubles at the same ideal source voltage. Correct under the stated ideal source and identical steady bulbs. |
| 9 / 10 | **5**, first bulb is one quarter as bright after adding the second in series | Intended fixed-R calculation gives each P′=(I/2)²R=P/4. A literal optical-brightness ratio does not follow without the additional model assumptions described above. |

PRS keys in order: **[3, 1, 2, 2, 5]**. Each question and the indicated answer page were inspected; the last key is conditional rather than an experimentally certified brightness ratio.

### Chapter 6, every page

| PDF / printed | Reading, equations, figures, and answers checked |
|---|---|
| 1 / 0 | Contents through §6.7.8; includes all examples, conceptual questions, and additional problems in this assignment. |
| 2 / 1 | §6.1; Eqs. 6.1.1–2; Fig. 6.1.1 positive moving charges and cross section; ampere definition, carrier types, current direction, scale claim qualified above. |
| 3 / 2 | §6.1.1; Eqs. 6.1.3–5; Fig. 6.1.2 swept charge cylinder; Fig. 6.1.3 microscopic electron path with drift opposite E; distinction between vector mean and mean speed. |
| 4 / 3 | Eqs. 6.1.6–10 and 6.2.1; electron force/acceleration and averaging; J parallel E for negative carriers; Drude assumptions. |
| 5 / 4 | Eq. 6.2.2–6; Fig. 6.2.1 wire with Vb left, Va right and field/current right; conductivity and geometrical resistance derivation. |
| 6 / 5 | Eqs. 6.2.7–11; Fig. 6.2.2 linear and nonlinear I–V plots; reciprocal resistivity, geometry, temperature law. |
| 7 / 6 | Every row, exponent, unit, and coefficient in the material table; Fig. 6.3.1 battery/resistor circuit and signs; E7 and material qualifications above. |
| 8 / 7 | Eqs. 6.3.1–2; source electrical input/heat; §6.4 summary of current, flux, density, Ohm relations. Voltage here is the positive magnitude, unlike P38's explicitly signed change. |
| 9 / 8 | Remaining summary including temperature/power; start §6.5.1 cable data. |
| 10 / 9 | Seven-strand cable calculation; §6.5.2 junction; Fig. 6.5.1 cylinder, material labels, interface, Gaussian surface, E₁/E₂ and current; charge-continuity and Gauss argument. |
| 11 / 10 | Interface result; §6.5.3 seawater drift calculation, both ionic species, centimetre units and answer. |
| 12 / 11 | Seawater dimensional check; §6.5.4 truncated cone; Fig. 6.5.2 axes/radii, slice, h; uniform-section assumption and dR. |
| 13 / 12 | Cone integral and limit; §6.5.5 hollow cylinder; Fig. 6.5.3 a,b,L,ρ; axial resistance derivation. |
| 14 / 13 | Radial cylindrical-shell resistance integral; all three §6.6 questions; §6.7.1 rotating sphere, all parts; start §6.7.2 heater. |
| 15 / 14 | Heater questions/approximate answers; §6.7.3 cylinder-plus-cone Fig. 6.7.1, L₁,L₂,a,b and current; all parts including numerical dimensions; §6.7.4 current density and electron transit data. |
| 16 / 15 | Printed transit answers; §6.7.5 Fig. 6.7.2 both panels and xyz directions, K relation, moving-sheet and belt questions with answer; §6.7.6 drawn-wire start. |
| 17 / 16 | Drawn-wire conditions/answer; §6.7.7 rated bulb, cost, R and I answers; §6.7.8 Fig. 6.7.3 layered slab/electrodes a,b,c,d, +V/0 boundaries and part (a) answer. |
| 18 / 17 | Remaining §6.7.8 parts (b)–(e), resistance, three potential changes, four surface charges, and high-ρ₂ limit prompt. |

### Chapter 7, exact assigned portion

| PDF / printed | Reading, equations, and figures checked |
|---|---|
| 2 / 1 | §7.1 introduction; Fig. 7.1.1 physical parallel/series bulbs and wiring; source/resistor/switch symbols and switch behavior. |
| 3 / 2 | Closed/open/short circuits and arbitrary ground; §7.2; Eq. 7.2.1 EMF as supplied work per charge; Fig. 7.2.1 battery and resistor. |
| 4 / 3 | Eqs. 7.2.2–6; Fig. 7.2.2 simple loop/current; Fig. 7.2.3 internal-r circuit and full potential trace. Signed loop sum and terminal voltage agree with discharging arrows. |
| 5 / 4 | Eqs. 7.2.7–8 including internal/external power; §7.3; Fig. 7.3.1 series circuit and equivalent; Eqs. 7.3.1–2. |
| 6 / 5 | Series sum Eq. 7.3.3; Fig. 7.3.2 both parallel/equivalent diagrams, node/branch currents; Eqs. 7.3.4–6. |
| 7 / 6 | Parallel limiting approximation; §7.4 junction and loop rules; Eq. 7.4.1; Fig. 7.4.1 I₁=I₂+I₃. |
| 8 / 7 | Eq. 7.4.2; all four sign-convention panels Fig. 7.4.2; Fig. 7.4.3 divider, input/output terminals, source polarity; Eq. 7.4.3. |
| 9 / 8, top only | Eqs. 7.4.4–6 and the paragraph on divider ratio. Assigned reading ends **before §7.5 Voltage-Current Measurements**. |

## Independent solution checks and source omissions

These are technical reviewer deductions. They do not imply the presentation itself contains the missing derivations or answers.

**Presentation circuits.** P32–33: using the shown clockwise meshes gives −2ε−RI₁−R(I₁−I₂)=0 and ε−R(I₂−I₁)=0, hence I₁=−ε/R, I₂=0, as printed. Independently, the bottom ideal source fixes Va−Vb=ε; middle current is ε/R from a to b, top current ε/R from b to a, and bottom branch current zero. The negative mesh sign denotes actual reverse flow.

P34 has no supplied meter answer. Let x=Va−Vb in the easier drawing, with all branch currents provisionally a→b. Top current is (x+ε)/R, middle current x/R, and bottom current (x−ε)/R. Their sum is zero, giving x=0. An **ideal voltmeter reads zero and the ideal ammeter has magnitude ε/R**, flowing b→a in its branch. The harder drawing has two 2R paths in parallel replacing middle R; neither carries current at x=0. Meter polarity is not marked, so a signed display value is not inferable. Finite meter resistance would require additional data. This calculation is absent from the slide.

P40: ε−Q/C−IR=0, I=dQ/dt and fixed C yield εI=I²R+d(Q²/2C)/dt. The resistor and capacitor receive positive power while charging. No exponential charging solution is supplied or needed to verify that balance.

**C6 worked examples.** §6.5.1 gives R=ρL/[7π(d/2)²]=30,719 Ω using its own specified ρ=3×10⁻⁶ Ωcm, L=3000 km, d=0.73 mm. This agrees with 3.1×10⁴ Ω; its given ρ need not equal the nominal copper-table value. §6.5.2 gives q=ε₀I(1/σ₂−1/σ₁)>0 for σ₁>σ₂ and the shown rightward current; dimensions and Gaussian-surface signs check. §6.5.3 gives 12/[6×10²⁰×1.6×10⁻¹⁹×25×200]=2.5×10⁻⁵ cm/s, subject to the two-species meaning above. §6.5.4 integrates to ρh/(πab), with limit ρh/(πa²). §6.5.5 gives axial R=ρL/[π(b²−a²)] and radial R=ρ ln(b/a)/(2πL); both dimensions, signs and thin-wall limits agree.

**C6 conceptual questions, PDF 14.** At the same ρ and length, RA=4RB gives area ratio AA/AB=1/4. Ordinary-metal resistance usually rises with increased lattice scattering as temperature increases, but this cannot answer the second question for every material. At the same applied voltage, RA=2RB gives PB=2PA by V²/R. These answers are reviewer deductions, not a supplied key.

**C6 §6.7 additional problems.** All displayed answers and unworked parts were checked as follows:

| Item and PDF locator | Check / reviewer deduction |
|---|---|
| 6.7.1, PDF 14 | I=dQ/dt; angular frequency 100π rad/s gives f=50 s⁻¹ and time-averaged loop current qf=4.0×10⁻⁷ A. If the intended perpendicular area is π(0.010 m)², mean J=1.27×10⁻³ A/m². Alternative “area traversed” interpretations remain underdetermined. No source answers are printed. |
| 6.7.2, PDF 14–15 | I=1500/115=13.04 A; R=115²/1500=8.817 Ω; one hour gives 5.40 MJ, or 1.292×10³ kcal using the given conversion. Printed ~10 A/~10 Ω are only coarse estimates. |
| 6.7.3, PDF 15 | Cylinder R₁=ρL₁/(πb²); total R=(ρ/π)[L₁/b²+L₂/(ab)]. For a=b this becomes ρ(L₁+L₂)/(πb²). The dimensions supplied give R=(200000/π)ρ in SI, or 1.095 mΩ if the chapter's nominal copper ρ=1.72×10⁻⁸ Ωm is selected. The numerical resistivity selection and uniform-section approximation must be stated. |
| 6.7.4, PDF 15–16 | J=nqv, with current opposite electron drift. Given data yield J=3.6859×10⁶ A/m², drift-speed magnitude 2.7097×10⁻⁴ m/s, mean-drift transit time 52.59 min. These agree with the source's 3.69×10⁶, 2.71×10⁻⁴, and 52.5 min at its constant precision. The transit time is not the starter's electrical response delay or a deterministic microscopic trajectory. |
| 6.7.5, PDF 16 | Current crossing strip width w is σvw, so K=σv in A/m, or vector K=σv. In the shown coordinates +y points into the page, so out-of-page positive current is −ĵ. Belt σ=(2.83×10⁻³)/(.50×30)=1.8867×10⁻⁴ C/m²=189 μC/m², as printed, for the stipulated total transported charge and width. |
| 6.7.6, PDF 16–17 | Constant mass/density preserves volume; tripling length divides area by three, making R′=9R=54 Ω at unchanged ρ. Printed answer correct. |
| 6.7.7, PDF 17 | At the specified constant 100 W, 31 days consume 74.4 kWh, costing $4.464 at the problem's assumed six cents/kWh; rounded $4.46. At rated 120 V, R=144 Ω and I=.8333 A. These are given historical/model inputs, not a current electricity-price lookup or a cold-filament resistance. |
| 6.7.8, PDF 17–18 | Steady J=I/A is common. R=d(2ρ₁+ρ₂)/(3A), J=3V/[d(2ρ₁+ρ₂)], E₁=ρ₁J and E₂=ρ₂J to the right. For right-to-left travel the positive rises are Vρ₁/(2ρ₁+ρ₂), Vρ₂/(2ρ₁+ρ₂), Vρ₁/(2ρ₁+ρ₂), summing V. With normal rightward and zero field in ideal caps, total charges per area are σa=−σd=ε₀E₁ and σb=−σc=ε₀(E₂−E₁), matching the formulas printed. At fixed V, ρ₂≫ρ₁ gives R≈dρ₂/(3A), J≈3V/(dρ₂), E₁→0, E₂→3V/d, outer rises→0, middle rise→V, σa,d→0, σb→+3ε₀V/d and σc→−3ε₀V/d. The last limit is a reviewer deduction; only the question is supplied. |

**C7 formulas.** The ideal loop yields I=ε/R; adding r yields I=ε/(R+r), terminal voltage ε−Ir and supplied power Iε=I²R+I²r. Series voltage sums and parallel current sums reproduce all Eqs. 7.3.1–6. The four Fig. 7.4.2 sign panels agree with their arrows and polarities. The unloaded divider gives I=Vin/(R₁+R₂), Vout=IR₂ and Vout/Vin=R₂/(R₁+R₂), agreeing with Eqs. 7.4.3–6. These direct substitutions resolve the mathematical checks without assuming the erroneous P38/P39 sign convention.

## Independent primary-source checks

Only the following specific external results are used. They qualify the original packet; they do not replace it or expand its assigned reading. No online student solutions or reader reports were used.

- **[A] MIT 6.200, Spring 2026, [Buttons, Pots, and Joysticks](https://circuits.mit.edu/S26/labs/pots), §§4–5, especially §5 first paragraph and voltage/current measurement procedure.** This independent laboratory explicitly measures the difference between unpowered and powered lamp resistance and its temperature dependence. Supports the conditional status of the fixed-R bulb calculation. It supplies no exact brightness ratio for this PRS circuit.
- **[B] IISc PH-208, [Lecture 1: Drude model](https://physics.iisc.ac.in/~aveek_bid/wp-content/uploads/2019/07/Lecture-1-Drude-model.pdf), PDF 1–2, collision-probability assumption and DC conductivity derivation.** The model specifies collision probability dt/τ and averages time since the last collision; this supplies the statistical assumption compressed in C6. No claim is made that Drude is a complete microscopic theory of every material.
- **[C] NOAA/NWS, [How Powerful Is Lightning?](https://www.weather.gov/safety/lightning-power), main numerical statement.** Gives about 30,000 A as typical. Used only to challenge treating the C6 mega-ampere illustration as a typical value, not to establish an upper bound.
- **[D] Feynman Lectures, Caltech edition, [II §24–1, The transmission line](https://www.feynmanlectures.caltech.edu/II_24.html), Eqs. 24.1–24.5 and assumptions following the coaxial result.** Voltage/current disturbances propagate with speed determined by line parameters. This independently separates signal propagation from carrier drift without assigning an unjustified speed to P10's unspecified wire.
- **[E] Edman et al., [Physical Review B 57, 6227 (1998)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.57.6227), accessible abstract.** Reports direction-dependent measurements and identifies natural single-crystal graphite as an anisotropic semimetal. Only the public abstract was used; paywalled figures/full text were not inspected or claimed.

Additional searches/opened pages were exploratory and are not scientific authority for this report. In particular, no numerical optical law, universal nerve-current scale, or material-table recalibration is claimed.

## Completion and limits

The assignment is fully readable at the required-content level: **4 exact original PDFs, 77 required pages, 77 fresh full-page inspections, five inspected PRS answer pairs, seven grouped confirmed source findings**. Equations, diagram topology, fine labels, polarities, answer indications, tables, exercises and section boundaries were included. There is no unresolved symbol or required figure-role extraction issue. The lack of slide numbers on P3/P4/P30 is handled by PDF locators.

Open technical limits are the rotating-sphere area wording, literal incandescent-brightness ratio, empirical lightning/nerve scale generalizations, unspecified sample/temperature/direction behind table values, and real-meter/nonideal-circuit data absent from idealized questions. Demonstrations were not performed. Supplemental calculations are clearly separated from what the sources actually supply. The source packet remains scientifically usable with these caveats; this report does not certify a teaching route or close an iteration.
