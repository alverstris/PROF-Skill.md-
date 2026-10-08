# D114 — original-source technical review

Reviewed 2026-10-08. Source preparation only; this record is neither an authored teaching route nor a reader evaluation or iteration closure. No student baseline/reader report was loaded.

## Assignment and integrity

D114 = `mit-8-02t-spring2005-S15`, Studio 15, original order114, active eligible order43. Title: **Hour 1 Magnetic Force Experiment 6: Magnetic Force Hour 2 Creating B Fields: Biot-Savart**. Selection and the exact audit row assign the entire presentation, entire PRS, and **Chapter9 §§9.1–9.2 only**. The index row is `15 Hour 1 Magnetic Force Experiment 6: Magnetic Force Hour 2 Creating B Fields: Biot-Savart Chapter 9: Sections 9.1 - 9.2 ( PDF - 1.9 MB ) ( PDF - 1.1 MB ) ( PDF )`.

There are **61 required page occurrences**: P33 + Q16 + C9 PDF3–14 (12). The reading starts at heading9.1 on PDF3/printed2 and ends immediately before heading9.3 on PDF14/printed13. This includes both examples, §9.1.1, all associated animation/simulation prose and stills, §9.2, Eq9.2.1 and Fig9.2.2/caption. The §9.3 material sharing PDF14 is outside the assignment. No other chapter is inferred from the slide topics.

| Alias | Original filename | Bytes; total PDF pages | SHA-256 |
|---|---|---|---|
| P | 649d27a9dda582b4d1c66f39ea6ddf6d_presentati_w06d2.pdf | 1119119; 33 | 3617eb2631c11d604b5be2676ebe40f127bc4064bd5c8d947930e55124f79067 |
| Q | 9c8c2814a9f5e114c0ea76ea22ae5057_prs_w06d2.pdf | 412736; 16 | 1b0124debe7db687aaf691dcb35a12395b48d7587598ce00fea2a2331f8473e3 |
| C9 | 4c84733e3977ba42a930a4c0414f70d0_ch9sourc_b_field.pdf | 2030041; 69 | 5e743cc2fb71785edb14aa135b6b9edbf6adaaf8e84585289916fa8134c4f126 |

The exact original hashes, byte sizes and page counts were verified at entry and completion. Every assigned text portion was freshly read and every required full-page PNG opened, including all equations, diagrams, labels and answer indications. PNGs passed nonempty/decode/load/dimension validation and hashes were rechecked at completion. No failed derivative was found or regeneration needed for D114. Originals and cache remain unchanged. Every page/render path and hash is in `source-map.json`. P footers are P15-n; Q uses unnumbered PRS15 sheets; C9 assigned printed pages are PDF-minus-one.

## Complete visual/text coverage

| Pages | Content checked |
|---|---|
| P1–8 | Agenda, prior fields/dipoles, compass/bar/Earth sketches, motion prompt, circular +q trajectory and all cyclotron formulas, wire-force dimensional heuristic and carrier geometry, jumping-wire title |
| P9–16 | Horseshoe/zero/up/down-current deflections, PRS/lab/evaluation titles, parallel-wire prompts, two wire-field simulation stills and URLs, Biot–Savart title |
| P17–22 | Source/field-point Coulomb diagram, moving-charge cross product and μ0, current-element field with θ and dot, cylindrical-coordinate/hand-rule graphics, moving-charge animation still, wire-field demo title |
| P23–29 | Every stage of the circular-loop/lead drawing, ds/rhat/θ arrows, scalar integral and into-page result, PRS title, off-center axial group-problem perspective and current arrows |
| P30–33 | Field-stress titles/statements, electric and magnetic pressure/tension stills with force directions and all accompanying prose |
| Q1–10 | All five Experiment6 prediction/answer pairs: above/front/behind magnet, both loop current senses; force arrows, field spreading and full options |
| Q11–16 | Bent-wire, curved-wire and two-particle question/answer pairs; axes, displacement, current/velocity arrows, all options and solution indications |
| C9 PDF3–5 | Figs9.1.1–3, Eqs9.1.1–4; all Simulation9.1 prose/still; finite-wire source/observer/displacement setup and cross product |
| C9 PDF6–8 | Eq9.1.5 angular integral and limits, symmetric/infinite limits9.1.6–7; Figs9.1.4–6; all Example9.2 question and source/observer geometry, Eqs9.1.8–9 |
| C9 PDF9–11 | Complete loop vector integration9.1.10–15; normalized axial field Fig9.1.7; dipole gradient/force9.1.16–17; charge-element conversion9.1.18–21; all Animation9.1 prose and Fig9.1.8 both charge signs |
| C9 PDF12–14 | Complete Animation9.2 and Simulation9.2 prose; Figs9.1.9–11; complete §9.2 with Figs9.2.1–2, Eq9.2.1 and Animation9.3; boundary before9.3 verified |

## Confirmed source error

**E1 — finite-wire angular limits and symmetric-angle statement, C9 PDF6/printed5, Eq9.1.5 and adjoining paragraphs.** With the geometry on Fig9.1.3 (PDF4/printed3), x=a cotθ and rhat=sinθ jhat−cosθ ihat, θ runs from **π−θ1** at the negative-x endpoint to θ2 at the positive-x endpoint, where θ1 and θ2 are the acute endpoint angles drawn. The source instead prints the lower limit −θ1 and asserts that integrating −sinθ produces cosθ2+cosθ1. Direct integration from the printed limits gives cosθ2−cosθ1, not the displayed sum. The symmetric-case prose θ2=−θ1 is likewise inconsistent with the acute angles in the diagram; it should be θ2=θ1. The correction is

`B = −(μ0 I / 4πa) ∫[π−θ1 to θ2] sinθ dθ = (μ0 I / 4πa)(cosθ2 + cosθ1)`.

The **final positive endpoint sum**, symmetric finite-wire result and infinite-wire result are correct. This is a real source derivation error, not an extraction artifact or an alternative consistent signed-angle convention.

Independent Cartesian verification avoids the inconsistent angle notation: for endpoints x1<0<x2, `Bz=(μ0 I/4π)∫[x1,x2] a dx/(a²+x²)^(3/2)=(μ0 I/4πa)[x/sqrt(a²+x²)]_[x1,x2]`. Thus for ±L, `Bz=μ0 I L/(2πa sqrt(L²+a²))`, tending to μ0I/(2πa). Direction is +z/out of the source diagram.

## Source ambiguities and conditions, kept distinct from E1

- **Coil leads/gap, P23–27 (especially P24 and P26):** the schematic visibly separates two horizontal leads and leaves a finite opening. “Legs contribute nothing” requires current elements collinear with displacement to P (ideal radial leads), while the full 0-to-2π integral assumes a complete circular turn. The intended negligible-gap/coincident-radial-lead idealization gives μ0I/(2R) into the page. It is not an exact result for every literal finite-gap/off-axis-lead geometry resembling the drawing. No dimensions specify the actual correction. For an arc alone of angular span α, the center field magnitude is μ0Iα/(4πR); nonradial leads require their own integral. This is an unstated geometric idealization, not grounds to invent a finite-gap answer.
- **Front/behind magnet, Q3–6:** the printed answers assume a downward local field. That is consistent with an ideal dipole's equatorial side region, but “in front” or “behind” alone does not specify height, magnetization, or all components of a real magnet field. The pictures provide no measured field map. The printed answer is confirmed **conditionally on the downward-field approximation stated on the solution sheets**. Off the symmetry plane, additional field components can produce additional force components; the photographic perspective is not quantitative evidence that they vanish.
- **Current sign convention, C9 PDF10–11 Eqs9.1.18–19:** writing I=nAq|v| and choosing ds parallel to v is consistent for positive carriers or for signed current relative to the carrier-path coordinate. It must not simultaneously be treated as a nonnegative current magnitude with ds always in conventional-current direction for negative q. The final signed-charge field Eq9.1.20 is correct.
- **Historical μ0, P18 and C9 PDF3 Eq9.1.2:** μ0=4π×10^−7 T·m/A was the exact SI convention for this 2005 source. Since the 2019 SI revision it is experimentally determined; NIST2022 lists 1.25663706127(20)×10^−6 N/A². At this packet's precision, the old value is an excellent approximation. Do not label the original's contemporary convention a 2005 scientific error.
- **Moving-charge scope, P18/P21 and C9 PDF11 Eqs9.1.20–21:** the chapter expressly notes v≪c and neglected retardation. Low speed alone does not justify this instantaneous formula for an arbitrarily accelerating charge at arbitrary distance; it is the low-speed, quasistatic/near-zone approximation (or leading low-speed uniform-motion field). Retarded acceleration/radiation terms can matter even at low speed. The simulations of discrete charges moving in a circle are interpreted within this approximation. No claim of an exact eight-charge threshold for a dipole field is warranted by the qualitative pattern discussion on PDF12.

## Independent physical/mathematical checks

P5's positive-charge orbit in B into page is counterclockwise; qvB=mv²/r, r=mv/(qB), T=2πm/(qB), ω=qB/m are correct for the drawn +q, v perpendicular to uniform static B, nonrelativistic motion and no other force. For general signed q use |q| in radii/periods; for nonzero parallel velocity the perpendicular motion is circular and the path is helical. The slides do not derive the helical case.

P7's replacement of charge-times-speed units by current-times-length is dimensional motivation, not a derivation. Summing the actual carriers gives Q_segment=nqAL and F=Q_segment vd×B=I Lvector×B with consistent current signs. It assumes uniform imposed B along that straight active segment. The general expression is I∫ds×B. P9's up-current/into-page-B leftward deflection and reverse-current rightward deflection agree with the cross product. A moving charge parallel to B is the zero-force exception to broad “moving charges feel force” prose.

P17–20/C9 §§9.1–9.1.1: rhat points source-to-observer; ds follows the chosen current coordinate; the differential Biot–Savart field is perpendicular to both, with magnitude μ0I ds sinθ/(4πr²). Units reduce to tesla. P18's upward positive-charge velocity at an upper-right observer gives B into page. P19's current element/upper observer gives B out of page. P20's zhat×rhohat=phihat and circular arrows are consistent. The finite isolated element is a contribution within a complete steady circuit, not an independently sustained open-ended DC source. C9 Example9.1 explicitly assumes cancelling lead contributions.

C9 Example9.2 (PDF7–10/printed6–9): ds×r=R dφ[z cosφ ihat+z sinφ jhat+R khat]. The transverse integrals vanish, giving `Bz=μ0 I R²/[2(R²+z²)^(3/2)]`. It is even in z, has maximum μ0I/(2R) at zero and decays as |z|^−3; Fig9.1.7 matches. For fixed small μ=μz khat, `Fz=−3μz μ0 I R² z/[2(R²+z²)^(5/2)]`, correct in Eq9.1.17: toward the loop plane when μz I>0, reversed when the moment is reversed, zero at its center. The maintained/permanent dipole and imposed-field approximation matters; do not differentiate a field-dependent induced μ as if it were fixed.

**P29 group problem, derivation absent on slides:** for its ideal complete loop in the yz plane, x-axis observation point and drawn current, transverse terms cancel. The reviewer deduction is `B(P)=μ0 I R²/[2(R²+x²)^(3/2)] xhat`. The sign follows r×ds along +x for the shown sense. Its corresponding derivation is supplied by assigned Example9.2 after relabeling axes; realistic leads again require specification. The off-center point still has a symmetry axis, so it does not require a general off-axis elliptic-integral solution. P27's “No vectors involved” means common direction permits scalar summation after the vector direction is settled, not that B ceases to be a vector.

C9 §9.2 PDF13–14: long parallel wires have field μ0I2/(2πa) and force per length μ0I1I2/(2πa); same-sense currents attract and opposite-sense currents repel. Taking +z from wire2 to wire1 and +x along both currents gives B2=−(μ0I2/2πa)jhat and F12=−(μ0I1I2ℓ/2πa)khat as printed. Infinite/long-wire approximation, negligible return-path contribution and externally prescribed steady currents are required. The reference to the “previous example” refers physically to the earlier straight-wire result, not the intervening circular-loop formula.

P30–33's pressure/tension description is consistent with vacuum Maxwell stress: tension along each pure E or B field, transverse pressure of magnitude ε0E²/2 or B²/(2μ0). These are field-stress descriptions, not literal mutually repelling strings. The full tensor contains the vector products and isotropic terms; dynamic momentum balance includes field momentum. P32 positive q in downward imposed E has downward force; P33 positive q moving out of page in downward imposed B has rightward force. The rendered superposed-field textures show the claimed asymmetry but are not a quantitative stress-surface integration or a derivation of qv×B. No live animation was executed.

## PRS answer audit

All eight question/answer pairs were inspected. Let right/up/out of page be +x/+y/+z except where the sheet explicitly provides axes.

| Q PDFs | Item | Source option | Independent check and condition |
|---|---|---|---|
| 1–2 | Prediction1, wire above N | 6, out | (+x)×(+y)=+z, axial upward-field approximation |
| 3–4 | Prediction2, front | 5, into | (+x)×(−y)=−z **if local B is downward**, as answer assumes; position caveat above |
| 5–6 | Prediction3, behind | 5, into | Same cross product under the stated downward-field approximation; position caveat above |
| 7–8 | Prediction4, loop | 2, down | Drawn front current right/back left means upward μ; above N, outward radial B gives downward axial force; radial components cancel by symmetry |
| 9–10 | Prediction5 | 1, up | Reversing every loop current reverses I∫ds×B for the same imposed field; printed arrows and force match |
| 11–12 | Bent wire | 6, −z | Vertical segment is collinear/antiparallel to displacement and contributes zero; rightward horizontal segment, observer below, gives into-page B. For a semi-infinite horizontal leg magnitude is μ0I/(4πy); finite length changes magnitude only |
| 13–14 | Curved wire | 2, semicircle plus long wire | Clockwise semicircle and both tangential semi-infinite legs each give into-page B. Magnitude μ0I/(4R)+μ0I/(2πR); dashed extension arrows are geometric continuation, while labeled lower I points left. Finite leads do not give the infinite-wire magnitude |
| 15–16 | Two particles | 2, +y | r21 has +x and −y components; v2=−y gives B2 at q1 along +z; v1=−x gives q1v1×B2 along +y. This is only the magnetic contribution, not total electric/magnetic/track force. Printed unit-vector equality conveys direction with magnitude suppressed |

The ring-force prediction uses the field's radial component or equivalently its gradient; a perfectly uniform upward B would give zero net loop force. The PRS answers' stated approximation is retained, not converted into universal predictions for arbitrary lab placement.

## Primary checks, completeness and limits

- [Feynman II21](https://www.feynmanlectures.caltech.edu/II_21.html), §21–1 and Eqs21.21–24: acceleration/radiation fields and why the instantaneous Biot–Savart expression requires a quasistatic region, not just v≪c.
- [Feynman II31](https://www.feynmanlectures.caltech.edu/II_31.html), §31–6 and concluding electromagnetic-stress discussion: principal tension/pressure and field energy-momentum accounting. Tensor coefficients were checked independently for the pure-field cases used here.
- [BIPM CGPM Resolution1 (2018)](https://www.bipm.org/en/committees/cg/cgpm/26-2018/resolution-1), Appendix2, effective20May2019; [NIST2022 listing](https://physics.nist.gov/cuu/Constants/Table/allascii.txt), vacuum magnetic permeability row: historical versus present μ0 exactness/value.

No required assigned page, equation, label or answer remains unreadable. The sole confirmed algebraic-error group is E1. The coil's literal lead geometry and PRS front/behind-field components remain underdetermined, with the conditional intended answers recorded explicitly. P8/P11/P12/P14/P22 provide titles rather than live demonstrations, actual experiment results, course-evaluation content or lab protocol. Simulation stills/prose do not demonstrate interactive behavior. No supplemental calculations are represented as source-authored answers. All 61 required occurrences were inspected; the remaining 57 C9 pages are outside this packet's assigned reading and are not claimed as covered here.
