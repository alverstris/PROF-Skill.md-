# D113 — original-source technical review

Reviewed 2026-10-08. Source preparation only: no authored teaching route, student baseline, reader evaluation, or iteration closure is represented here.

## Exact packet and integrity

Selection and the assigned audit row agree: D113 = `mit-8-02t-spring2005-S14`, Studio 14, original order 113, eligible active order 42. Title: **Hour 1 Magnetic Fields Experiment 5: Magnetic Fields Hour 2 Charges moving in B Fields Exam Review**. Official index row: `6 14 Hour 1 Magnetic Fields Experiment 5: Magnetic Fields Hour 2 Charges moving in B Fields Exam Review Chapter 8 ( PDF ) ( PDF ) ( PDF )`.

The complete assignment is the 31-page presentation (P), 8-page PRS (Q), and **all 28 PDF pages of Chapter 8 (C8), including contents, conceptual questions and additional problems**: 67 required page occurrences. The prior audit supplied the index only. All 67 were freshly read and their full-page renders opened for this packet. Equations, signs, diagrams, arrows, legends and indicated answers were checked. Original files were hash/byte/page verified at entry and completion; originals and cache were not modified.

| Alias | Original filename | Bytes; pages | SHA-256 |
|---|---|---|---|
| P | e18d38e0b1eb8d1d98b6cd72f212cbf2_presentati_w06d1.pdf | 1028006; 31 | 532eb98ac7d3d535b155049c4ef422c5d802e7e708e26f02f544b361ccec9ed3 |
| Q | 01a249e3a9bfb2504d9e4a040a9f62ee_prs_w06d1.pdf | 109128; 8 | d26cd24c99e80c0f064f2f73d14a1a16195e9801dbb76b75225541694fc922f2 |
| C8 | 90510e513af27a2dde30b890a61bbcd1_ch8magneti_field.pdf | 774541; 28 | 89e0f4958f0694de45dc3a44583cf6de161a8f04681ae35bf48a5842e97e7aac |

Original paths, official URLs, every required page, render path/hash and boundary records are in `source-map.json`. P footers are P14-n. Q pages are unnumbered PRS14 sheets; use PDF page numbers. C8 PDF1 has printed 0; PDF2 anomalously prints **8-2**, although the contents assigns §8.1 to page 1; PDF3–28 print PDF-minus-one.

All cached PNGs passed nonempty, decode, load and dimension checks. P9 initially appeared blank in a displayed batch despite substantial original text. It was reopened alone and independently rendered from the hash-verified original at scale 2; all bar-magnet, compass and split-magnet content is present and readable. A fresh scale-1.6 render is byte-identical to cached P9 (SHA-256 ffe516d43be4a5323e06f6362a4ca031ab7214455dfae1ea29c8a7b800cdb7ec). Thus the apparent blank was a display anomaly, not a failed cache file or blank source slide. The necessary verification supplement `P-p009-verification.png` is retained (SHA-256 c1ea2b773195d74f5050115b8444c5442edb330b7292427ab32f4d597430fdeb). No failed cached derivatives remain. A tool-output-truncated attempt at P25–31/Q1–4 was not credited; those pages were subsequently reopened in successful smaller batches.

## Complete coverage ledger

| Asset/PDF pages | Freshly inspected content and figures |
|---|---|
| P1–6 | Agenda and transition; point gravity/electric fields and dipole torque; like/unlike pole force sketches; bar-magnet and compass demonstration title cards |
| P7–11 | Compass arrows and external N-to-S field lines; cut magnets; complete P9 repeated dipole graphic; separated electric charges versus inseparable bar-magnet poles; electric and magnetic closed-surface flux comparison; field/torque summary |
| P12–18 | Prompts; Earth's polarity globe; MIT spherical/Cartesian field-component sketches; Experiment 5 title; full simulation still with pale field curves; recap and television demonstration title |
| P19–25 | Positive/negative charge force illustrations; tesla/gauss dimensions; dot/cross convention; parallelogram cross-product magnitude; hand/vector animation still; all six cyclic/anticyclic unit-vector identities |
| P26–31 | PRS transition; full Lorentz force; selector plates, field, velocity and force arrows; selector balance; Hall PRS and exam-review title cards |
| Q1–8 | Three complete right-hand-rule question/answer pairs and Hall-effect question/answer, including every option and diagram |
| C8 PDF1–4 | Contents; Figs 8.1.1–8.1.3, compass/poles/split magnet; Fig 8.2.1 force hand; Eqs 8.1.1, 8.2.1–3; Fig 8.3.1 wire deflection |
| C8 PDF5–7 | Figs 8.3.2–8.3.6: wire carriers, differential segment, curved path/endpoints, closed loop, semicircle; Eqs 8.3.1–5; complete Example 8.1 integration |
| C8 PDF8–10 | Figs 8.4.1–8.4.3: numbered rectangle sides, side forces, lever arms/angle/axes, loop-current hand rule; Eqs 8.4.1–11 including energy integral and equilibria |
| C8 PDF11–13 | Figs 8.4.4–8.4.6: axial attraction, dip needle, Earth/needle field-line still; Eqs 8.4.12–16; all Animation 8.1 text, including continuation before §8.5 |
| C8 PDF13–15 | Complete §8.5; Figs 8.5.1–3 circle/helical orbit/field-region still; Eqs 8.5.1–5; all Animation 8.2 text |
| C8 PDF16–19 | Figs 8.6.1–2 Thomson and Bainbridge apparatus; Eqs 8.6.1–6; complete summary and Cartesian cross-product/problem-solving discussion |
| C8 PDF20–23 | All four solved problems; Figs 8.9.1–4 plus coordinate inset diagrams; Eqs 8.9.1–16; rolling rod, suspension, mass ratio and ring force |
| C8 PDF24–28 | All five conceptual questions and eight additional problems, every subpart and supplied answer; Figs 8.11.1–5: pivoted square, inclined bar, finite plates, particle orbits, semicircle/triangle loop |

## Confirmed source defects and overstatements

1. **E1 — categorical monopole claim:** P8–11, especially P9, and C8 PDF2/printed 8-2, last paragraph/Fig 8.1.3, say isolated monopoles do not exist. Cutting an ordinary magnet does preserve two poles; it does not prove fundamental monopoles impossible. Classical no-monopole Maxwell theory is the working assumption. CERN/ATLAS describes hypothetical monopoles and searches with no established signal, not a proof of nonexistence. This is an overstatement, not evidence that a monopole has been found.
2. **E2 — wrong equation cross-reference:** C8 PDF8/printed7, paragraph immediately after Fig 8.4.1 says “From Eq. 8.4.1” to justify zero force on sides 1 and 3, but that equation below concerns sides 2 and 4. The applicable general force is Eq 8.3.1 (or 8.3.2). The actual force/torque calculations are correct.
3. **E3 — plane/normal angle conflation:** C8 PDF9/printed8, paragraph before Fig 8.4.2 says the loop “or the area vector” makes θ with B. The diagram and sinθ torque formulas use **the area normal's angle with B**; the plane's angle is complementary. This is a prose error, not a faulty diagram or torque equation.
4. **E4 — accelerating-electron work attribution:** C8 PDF16/printed15, paragraph before Eq8.6.2 calls ΔU=qΔV the external work done “in accelerating” the electrons. For the stated free electrical acceleration, work on the particle is −ΔU=ΔK, while W_external-agent=ΔU describes a different quasistatic transport. The displayed speed and following e/m formula are correct for negligible initial speed and ΔV=V_A−V_C>0.
5. **E5 — rolling wording:** C8 PDF20/printed19, paragraph below Eq8.9.3 says “rolling with slipping implies ω=v/R.” It must be **without slipping**, as the problem correctly states. The final speed is correct for a solid cylindrical rod, constant current, adequate static friction and no dissipation; I is reused for current and moment of inertia.
6. **E6 — supplied acceleration exponent:** C8 PDF24/printed23, §8.11.1(b) prints approximately 10^−15 m/s². Direct substitution gives approximately **5.7×10^14 m/s²**, of order 10^15, under the chapter's nonrelativistic model. This is a 30-order exponent-sign error, visually confirmed in the PDF, not OCR ambiguity.

Additional typography: C8 PDF25/printed24, §8.11.3 leaves the length symbol blank in its first sentence; Fig8.11.2 supplies ℓ. PDF2's anomalous footer is recorded above. Minor grammar (“rotates oscillates”, “toque”, “close loop”) does not alter physics.

## Valid results, assumptions and absent derivations

- P3/P11 point-source gravity/electric formulas concern point sources or suitable spherical exterior fields; distinguish source charge/mass from test charge/mass. P7 and C8 PDF2 describe the **outside** N-to-S portion of B lines; lines continue through the magnet and do not literally terminate at a pole. A compass indicates the local permitted component of B, not necessarily a line aimed at one geographic point.
- P13's “North magnetic pole … southern hemisphere” uses **north-type bar-magnet polarity**, whereas geographic naming convention calls the northern dip pole the North Magnetic Pole. The S label near geographic north and north-end-down dip are physically consistent. NOAA's definitions settle the terminology; no new Earth pole coordinates or local MIT measurements are inferred. P14's ideal dipole with μ along −z gives negative radial and polar components in the shown northern quadrant; its Cartesian axes are global schematic axes. It is not a dated field measurement.
- P19/P27, C8 §§8.2–8.3: F=qv×B, |F|=|q|vB sinθ and F·v=0 check dimensionally and algebraically. P27's “final word” is scoped to the classical electromagnetic force on a test charge; other forces and self-force are not addressed. Wire force is I∫ds×B, reducing to I(endpoint displacement)×B in a uniform field; a closed steady loop then has zero net force. Uniformity is required in C8 PDF18's compact straight-wire summary.
- Example8.1 (C8 PDF6–7): straight segment +2IRB k, arc −2IRB k, total zero. Rectangular loop (PDF8–10): side2 +IaB k, side4 −IaB k, torque +IabB j; general τ=μ×B, μ=NIA, and −μ·B mechanical potential check. Clockwise/counterclockwise wording depends on viewpoint; the vector equations remove ambiguity. Nonuniformity permits, but does not guarantee, a nonzero dipole force. F=∇(μ·B) assumes a small fixed permanent/maintained dipole and an imposed slowly varying field; induced moments need additional treatment.
- C8 PDF10–13/20 use work on a macroscopic dipole/wire. This does not contradict zero magnetic work on an individual point charge. Mechanical effective energy −μ·B at maintained current excludes electrical/source energy. Feynman II15 §§15–1–2 explicitly treats this distinction. Animation field-pressure/tension narratives are qualitative visualizations, not a complete stress-tensor or field-momentum derivation; the full system including source currents and fields conserves momentum/angular momentum. No animation was executed or historical Faraday quotation independently authenticated.
- C8 PDF13–19: r=mv_perp/(|q|B), T=2πm/(|q|B), ω=|q|B/m and helix pitch v_parallel T hold for nonrelativistic particles in static uniform B, neglecting other forces/radiation. The explicit +q assumption makes omission of absolute values in Eqs8.5.1–4 legitimate; pure parallel velocity is a straight line, not a finite-radius helix. Eq8.5.5 is a low-speed/quasistatic moving-charge field, not the full retarded field for arbitrary acceleration.
- P28–29 and C8 PDF16–17: the depicted perpendicular-field beam is undeflected at v=E/B for either charge sign. Neutral particles are a trivial exception; with arbitrary three-dimensional velocities the parallel-to-B component is unconstrained. Thomson e/m=E²/(2ΔVB²), Bainbridge m=qB0Br/E, and their pictured deflection signs check. C8 PDF17's “most precise … to date” is a historical statement, not current metrology: NIST 2022 gives signed electron charge/mass −1.75882000838(55)×10^11 C/kg.
- C8 solved problems: §8.9.1 v=sqrt(4IℓBa/(3m)); §8.9.2 leftward current I=λg/B; §8.9.3 r²∝m/q at a common accelerating voltage magnitude yields m_A/m_B=1/8; §8.9.4 dF=IB ds(sinθ zhat−cosθ rhat), radial cancellation and F=2πrIB sinθ zhat are correct for the drawn clockwise current/axial symmetry. In §8.9.3 ΔV is an accelerating **voltage-drop magnitude**, unlike the signed V_A−V_C convention of the electron apparatus.
- P5/P6/P15/P18/P31 contain demonstration, experiment or exam-review titles without the live demonstration, lab instructions/data or worked exam. P16/P24 and chapter animations provide stills and prose only. Their existence does not supply an authored teaching derivation, a lab outcome or an executed animation.

## Independently checked PRS answers

Let right/up/out of page be +x/+y/+z.

| Q PDFs | Item | Printed answer | Independent check |
|---|---|---|---|
| 1–2 | Right-hand rule #1 | 5, into page | (+x)×(−y)=−z, q>0 |
| 3–4 | #2 | 6, out | (+x)×(+y)=+z |
| 5–6 | #3 | 1, up | (−x)×(+z)=+y |
| 7–8 | Hall effect | 1, positive | J right, B out: magnetic drift force downward for either carrier sign; higher bottom potential means upward Hall E, balancing downward force on positive carriers. Correct in the intended ordinary single-carrier model; not a universal inference for arbitrary multiband material. |

## Supplemental reviewer deductions for the entire assigned problem set

These are independent checks, not answers purportedly present in the slides. The chapter supplies only selected numerical answers.

**§8.10, C8 PDF24/printed23:** (1) v parallel/antiparallel to B (or zero) gives no magnetic force. (2) A perpendicular force changes direction without changing speed. (3) Electric force acts at rest and can change energy; reversing v reverses the magnetic contribution, leaving qE fixed. One trajectory alone need not uniquely separate E and B. (4) A gradient can exert dipole force, with attraction or repulsion depending on orientation and gradient. (5) Uniform B gives zero net force on a small ideal compass, but μ×B torque except at parallel/antiparallel orientations.

**§8.11.1, PDF24/printed23:** electron motion north with B down deflects east. Using stated rounded 12keV and B=5×10^−5T gives v≈6.49×10^7m/s, a≈5.71×10^14m/s², r≈7.38m and deflection after 0.20m longitudinal travel r−sqrt(r²−0.20²)≈2.71mm (same leading result for 0.20m arc length). At v≈0.22c the nonrelativistic answer is an approximation; relativistic momentum changes these results by a few percent, not the exponent conclusion.

**§8.11.2, PDF24–25/printed23–24:** with uniform wire mass and θ measured from vertical, τ_g=mgℓ sinθ/2 and opposing τ_B=Iℓ²B cosθ. Hence I=mg tanθ/(2ℓB)≈17.8A, consistent with the source's rough 20A, and torque≈0.00838N·m. Current must run so the bottom side's horizontal magnetic force is away from the vertical plane through the hinge (it increases θ), with opposite force on the hinge side; the two connecting-side magnetic forces cancel along the hinge and contribute no hinge-axis torque. Equivalently choose μ so μ×B opposes gravity's hinge torque. This geometry statement avoids unmarked viewing-direction ambiguity in a perspective sketch. Total magnetic force is zero: total pivot reaction on the loop is mg≈0.49N upward; the loop exerts the opposite force on its supports. Symmetry gives mg/2 at each pivot if equal support sharing is assumed. The phrase “force … on the axis by the pivots” does not specify a separate mechanical axis model.

**§8.11.3, PDF25/printed24:** introducing the unspecified mass m, IℓB cosθ=mg sinθ, so I=mg tanθ/(Bℓ). Direction is the crossbar current for which Iℓ×B is horizontal uphill; normal reaction is mg/cosθ. Requires 0≤θ<π/2, ideal contact and imposed current. No numerical mass or field magnitude is given, so no numerical current is determined.

**§8.11.4, PDF26/printed25:** negative charge initially right in B into page curves downward. Introducing its unstated mass m, r=mv/(qB), q>0. If the lower plate is reached while the particle remains in the field region, x_hit=sqrt(rd−d²/4). A hit is not guaranteed by the prompt: need r≥d/4 and no earlier side exit. For r≥d/2 need ℓ≥x_hit; for d/4≤r<d/2 need ℓ≥r because the trajectory first turns at x=r. Otherwise it exits a side before touching that plate. These conditions presume the drawing's ideal field bounded between the plate ends; exterior fringe fields are unspecified.

**§8.11.5, PDF26–27/printed25–26:** pictured downward bending with B out means q>0; mv²/R=qvB gives R1=m1v/(qB), m2/m1=2. E=+vB yhat cancels magnetic force for both and is independent of mass at common v.

**§8.11.6, PDF27/printed26:** uniform-field closed-loop force is zero. The drawn current is clockwise, μ into page. Area A=πR²/2+ℓ²sinθ/2 (with closure R=ℓsin(θ/2)); τ=−IAB yhat for B right and y up. Keeping the triangle term is necessary.

**§8.11.7, PDF27/printed26:** F=IℓBsin20°≈0.0479N, consistent with 0.05N. Direction is perpendicular to the current/B plane by their cross product; no unique compass direction is supplied. For fixed wire length, orient it perpendicular to B to maximize force at 0.14N.

**§8.11.8, PDF28/printed27:** eastward current in northward B gives upward J×B. J=ρ_mg/B≈1.7444×10^9A/m². Joule power density ρJ²≈5.173×10^10W/m³=5.17×10^4W/cm³. Diameter cancels. This is the ideal force balance and given-resistivity instantaneous heating calculation, not evidence of a thermally sustainable levitation experiment.

## Primary checks and limits

External sources were consulted to resolve consequential scope/current-claim questions, not to replace inspection of this packet:

- [ATLAS Collaboration, 18 July 2024 briefing](https://atlas.cern/Updates/Briefing/Monopoles-First-Run3), opening and search-result paragraphs: monopoles are hypothetical; null/background-consistent searches set limits. A fresh date-filtered search also returned NOvA's 2026 search abstract (arXiv:2608.03888), but its page open failed; no uninspected paper details are relied on.
- [NOAA NCEI geomagnetism FAQ](https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions), “What is a magnetic pole?”, north-end-down description and compass-direction section: geographic naming, inclination, and local horizontal-field response. No claim is made that old model coordinates on that page are current.
- [Feynman Lectures II15](https://www.feynmanlectures.caltech.edu/II_15.html), §§15–1–2, Eqs15.4 and15.12: maintained-current mechanical energy and electrical/source energy accounting; distinction from zero work on each point charge.
- [NIST 2022 CODATA complete listing](https://physics.nist.gov/cuu/Constants/Table/allascii.txt), electron charge-to-mass, electron mass and elementary-charge rows: dated metrology update and constants for arithmetic. The direct single-value endpoint was unreliable; the official full listing was successfully read.

No required source symbol, label, indicated PRS answer or assigned text remains unreadable. Source ambiguities remain: geographic pole naming without convention, angle prose, unspecified problem parameters and finite-plate hit conditions, and apparatus demonstrations absent from the packet. These are explicitly bounded above, not silently resolved by invented data. Historical attribution and live-animation/lab behavior were not independently verified. This packet is usable as source evidence with the recorded corrections and conditions; it does not close an authored iteration.
