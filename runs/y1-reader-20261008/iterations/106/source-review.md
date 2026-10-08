# D106 source review

Source technical preparation only, 2026-10-08. This record neither authors a teaching route nor closes a PROF iteration. D106 maps to **MIT 8.02T Spring 2005 Studio S02**, original order 106, selected active order 35: review of electric fields, charge, dipoles, and continuous distributions. Mapping was read from the assigned selection and audit rows. No excluded session was inspected.

## Packet and provenance

All four cached original PDFs were read without alteration, and fresh SHA-256 computations match the audit. Exact URLs, hashes, bytes and per-page visual receipts are in `source-map.json`.

| Alias | Original PDF | Required coverage | Printed locator |
|---|---|---|---|
| P | `915fb527b640077a671aa90c19c40cf0_presentati_w01d2.pdf` | PDF 1–41, all | P02-1 through P02-41 |
| Q | `3cbf58c60016d128c4a9d9fe0b555b1e_prs_w01d2.pdf` | PDF 1–12, all | PRS02; use PDF page |
| C1 | `85fb9106dc3e09b421f3aa60d47ecaef_chapter1fields.pdf` | §1.6 only: heading on lower PDF 14 through Figure 1.6.1/caption at top PDF 15; stop before §1.7 | printed 13–14 |
| C2 | `c31cd03c1b74a450ec131921f5625f0a_chap2coulomb_law.pdf` | PDF 1–44, entire chapter including contents, solved/conceptual/additional problems | printed 0–43; printed = PDF−1 |

**Fresh coverage: 99 of 99 required page occurrences opened as full-page renders, alongside fresh original-PDF text extraction.** The prior audit was an index only. Every diagram, equation, caption, axis, charge sign, direction arrow and PRS answer indication on those pages was inspected. C1's surrounding §§1.5/1.7 on the boundary pages are outside the assigned semantic coverage. Interactive links and demonstration titles in P are represented by their complete published static page; linked applets, videos and lab manuals are outside this selected packet.

C2 section boundaries: contents PDF 1–2; §2.1 PDF 3; §2.2 PDF 3–5; §2.3 PDF 5–7; §2.4 PDF 7–8; §2.5 PDF 9–10; §2.6 PDF 10–11; §2.7 PDF 11–13 (2.7.1 PDF 12–13); §2.8 PDF 13–16 (2.8.1 PDF 14–16); §2.9 PDF 16–18 (2.9.1 PDF 16–17, 2.9.2 and 2.9.3 PDF 17–18); §2.10 PDF 18–25; §2.11 PDF 25–26; §2.12 PDF 27–28; §2.13 PDF 29–39 (2.13.1 PDF 29–30, 2.13.2 PDF 30–31, 2.13.3 PDF 31–33, 2.13.4 PDF 33–36, 2.13.5 PDF 36–37, 2.13.6 PDF 37–39); §2.14 PDF 39–40; §2.15 PDF 40–44 (2.15.1 PDF 40, 2.15.2 PDF 40–41, 2.15.3–4 PDF 41–42, 2.15.5–6 PDF 42–43, 2.15.7 PDF 43, 2.15.8 PDF 43–44). Boundaries sharing a page stop at the next section heading.

Figure coverage: C1 Figure 1.6.1; C2 Figures 2.2.1–2, 2.3.1, 2.4.1–2, 2.5.1–2, 2.6.1, 2.7.1–3, 2.8.1–3, 2.9.1, 2.10.1–10, Table 2.1 and the comparison table on PDF 28, 2.13.1–4, unnumbered conceptual-question drawings PDF 39–40, and 2.15.1–6, 2.15.9–10. The source itself skips figure numbers 2.15.7–8. All presentation drawings/static visualization frames and Q diagrams on PDF 3–8, 11–12 are included.

## Independent physics and answer checks

Checks used Coulomb vector addition, dimensions, symmetry, direct integrals, Taylor expansion, torque and work; answers were not accepted merely because bolded in Q. Vacuum electrostatics and ideal fixed distributions are the common model. The field excludes the test charge's own field; small test charges do not disturb sources. All numerical recalculations below use the source's rounded constants.

| Source locator | Checked result / limitation |
|---|---|
| C1 §1.6, equations 1.6.1–2; P3 | E=kQ r-hat/r², F=qE; source-to-observer unit vector and signed source charge are consistent. |
| P6 | Opposite charges, −q left and +q right: E=−k q d/(s²+d²/4)^(3/2) i-hat. This answer is reviewer derivation, absent from that slide. |
| P12,15,17; C2 2.7.3–8 and 2.13.4 | p=2qa j-hat. θ is measured from +y, so x=r sinθ, y=r cosθ. Far field E=k[3(p·r-hat)r-hat−p]/r³. The presentation says “you can show”; the assigned chapter provides the Taylor derivation. |
| P21; C2 2.8.2–7 | Uniform-field net force zero, torque p×E (into page for shown orientation), U=−p·E with zero at θ=π/2. P21's r×F uses the full separation about one endpoint; about the midpoint both torques must be summed. |
| P25–35; C2 Examples 2.2–4 | General density is dq/dV, dq/dA or dq/dl; Q/V etc. require uniform density. Ring E_x=kQx/(a²+x²)^(3/2); transverse components cancel. P35's kQ/x² limit assumes x>0 as drawn and fixed Q as a→0. |
| P36–38; C2 Example 2.3 | E_y=kQ/[s sqrt(s²+L²/4)] for s>0; far field kQ/s²; long-line result 2kλ/s. The infinite-line limit holds λ fixed, not finite Q. |
| P39–41; C2 Example 2.5 | For x>0, disk E_x=σ/(2ε0)[1−x/sqrt(x²+R²)]. Far field kQ/x²; near-plane limit σ/(2ε0). Opposite face reverses normal direction. Finite line/disk become point-like far away; P41's 1/r and constant apply infinite-source limits. |
| C2 2.13.3, PDF31–33 | Electron deflects upward: a=eE_y/m, t1=L1/v0, y_screen=(eE_y L1/mv0²)(L1/2+L2). Ignore fringing/gravity and assume no plate collision. |
| C2 2.13.5–6, PDF36–39 | Arc E=−2kλ sinθ0/R i-hat; general finite rod Ex=kλ(cosθ2−cosθ1)/y, Ey=kλ(sinθ2−sinθ1)/y. Signs and infinite-line limit verified. |

PRS answer indications: Q1→Q2 **4** requires positive test charge and electric force alone (see issue below); Q3→Q4 **2, repulsive**, like-sign topology shown, no absolute charge sign inferable; Q5→Q6 **1**, 2kqs/(s²+d²/4)^(3/2) j-hat; Q7→Q8 **4**, −kq/R² j-hat, because opposite vertices cancel and the top charge remains; Q9→Q10 **2**, 1/r³ far field; Q11→Q12 **3**, nonzero electric force and torque for the pictured tilted unequal field arrows. The pivot can supply a reaction force; a nonzero electric force need not translate the constrained rod. Q12's explanation is not valid for every nonuniform field or every orientation.

## Confirmed source errors and exact resolutions

1. **C2 Example 2.1, PDF7 / printed6, magnitude calculation:** final `3.0 N` is wrong by 100. Stated q1=6 µC, q3=3 µC, a=0.020 m give Fx=−261.81 N, Fy=143.19 N, |F|=298.41 N≈3.0×10² N. The symbolic formula and angle 151.3° are correct. Original render confirms this is not extraction corruption.
2. **C2 §2.5, PDF9 / printed8, far-field rule (3):** “radially outward unless Q=0” omits negative Q. Outward for Q>0, inward for Q<0. A neutral distribution can have a nonzero dipole or higher multipole. C2 PDF26's blanket point-charge summary needs the nonzero-total-charge condition.
3. **C2 equation 2.10.8, PDF20 / printed19:** the first substituted denominator prints `y³(sec²θ′+1)^(3/2)`; it must be `y³(tan²θ′+1)^(3/2)`. The next expression and final answer already use the correct identity. Source-only algebra typo.
4. **C2 2.13.1(b), PDF29 / printed28:** the problem says r=0.53×10^−10 m; the worked denominator switches to 0.5×10^−10 m and reports 5.76×10¹¹ N/C. With the stated r, E=5.126×10¹¹ N/C≈5.1×10¹¹ N/C. Part (a)'s 8.2×10^−8 N uses the stated distance and is consistent.
5. **C2 2.13.2, PDF31 / printed30:** after correctly finding q≈−8.03×10^−19 C, the source calls +e the electron charge and writes N=q/e=+5. Use q=−Ne, N=|q|/e≈5 **excess** electrons. An oil drop has many bound electrons; “five electrons on the oil drop” means five excess electrons. Mass 1.57×10^−14 kg and negative q are verified. Air buoyancy is neglected by the stated model.
6. **C2 Figure 2.10.9, PDF24 / printed23:** the varying graph is the finite **disk**, not an infinite plane; the latter is Figure 2.10.10 on PDF25. Its axis and two-sided discontinuity are otherwise correct.
7. **C2 2.13.4, PDF35 / printed34:** reference to Figure 2.13.4 for sinθ=x/r, cosθ=y/r points to the rod drawing; the intended dipole geometry is Figure 2.7.1 (PDF11). Formulas are consistent with that dipole geometry.

## Assumptions, wording and unresolved factual claims

- **Q1–2:** field-line direction is acceleration direction only for a positive charge under the electric force alone. Negative charges accelerate oppositely. “Particles do NOT move along field lines” should mean “paths are not generally field lines”; a particle released at rest in a uniform field is an immediate counterexample. Preserve the intended answer 4 with those qualifications; do not present the literal generic wording as a universal law.
- **Q11–12; C2 PDF15–16, §2.8.1:** nonuniformity alone does not guarantee both force and torque. Exact force is q[E(r+)−E(r−)]; small-dipole force is (p·∇)E. Uniform-field torque p×E vanishes when aligned or antialigned. C2's own aligned Figure 2.8.2 has zero torque. For the actual Q11 figure, both are nonzero. Eventual alignment also requires damping; free lossless dipoles can oscillate.
- **P22; C2 PDF4–5:** field-line tension is a representation of electromagnetic stress, not material strings or a required mechanical ether. Independent primary reference: Feynman Lectures II §31-8, https://www.feynmanlectures.caltech.edu/II_31.html, describes electrostatic stress with longitudinal tension ε0E²/2 and transverse pressure. No physical medium is needed. Propagating changes require full electrodynamics; the instantaneous Coulomb model here is electrostatic/quasistatic.
- **C2 PDF30 / printed29, 2.13.1(d):** uncited claim that the electron–proton charge-magnitude difference is “on the order of 10^−24” is dimensionless without an explicit normalization, and confuses an experimental bound with a nonzero difference. Do not carry it forward as established. Primary measurements inspected: Marinelli & Morpurgo (1984), DOI 10.1016/0370-2693(84)91752-0, https://www.sciencedirect.com/science/article/abs/pii/0370269384917520 reports (0.8±0.8)×10^−21 e; Bressi et al. (2011), https://arxiv.org/abs/1102.2766 gives ~10^−21 under neutron β-decay charge conservation. These do not support the source's number; no claim is made here to identify the globally strongest 2026 bound. Planetary gravity dominance uses near neutrality; “entirely” is an idealization.
- **C2 PDF43 / printed42, 2.15.7(b):** x=5.0 cm is supplied while the drawing and part (a) name separation r. x is undefined. If intended x=r, |q|≈2.38×10^−8 C. The intended variable cannot be established from the source alone; retain this as unresolved author intent.
- **C2 PDF41 / printed40, 2.15.3:** “field at the location of charge q” must exclude q's singular self-field. “Conducting” balls in 2.15.7 are tiny-sphere/point-charge approximations; a finite charged conductor need not have uniform surface density.

## Supplemental reviewer deductions for unkeyed problems

These are independent checks, not source-provided answers or a teaching sequence. C2 §2.14 PDF39–40: (1) both forces obey inverse-square pair laws, gravity attractive for positive masses while charge force has either sign; (2) unique field direction prevents ordinary field-line crossings; (3) null lies on smaller-charge side, left of −q at distance d/(√3−1) for separation d; (4) fixed-source field unchanged on changing test charge; (5) nonuniform-field dipole force/torque require actual geometry, as above.

C2 §2.15, using k=9×10^9 where numerical: 2.15.1 F_(9µC)=(1.0125 i−0.58457 j) N and F_(−6µC)=(−1.125 i+1.16913 j) N. 2.15.2 E(P)=4√2 kq/a² i. 2.15.3 E_at_q=(kq/a²)[(3+√2)i+(2+√2)j]; F_on_2q=(kq²/a²)[(8+3/√2)i−(2+3/√2)j]. 2.15.4 uses θ measured from +y, not +x: Q=2λ0R, F_origin=−kπqQ/(4R²) j. 2.15.5 Iθ¨=−pE sinθ≈−pEθ, ω=√(pE/I), f=ω/(2π). 2.15.6 for the shown axial observation point z>h: shell Ez=(kQ/h)[1/√(R²+(z−h)²)−1/√(R²+z²)]; solid Ez=ρ/(2ε0)[h+√(R²+(z−h)²)−√(R²+z²)]. Shell means curved cylindrical surface, as implied by ring hint. 2.15.7 r³=q²l/(2πε0mg) using the small-angle condition; part (b) ambiguous as above. 2.15.8 p=3.2×10^−28 j C m; τ=−9.6×10^−28 k N m; mutual central forces supply zero torque on the rigid pair.

## Limits and handoff

All required original content is readable; no consequential glyph or figure uncertainty remains. Cosmetic prose/numbering issues are not silently corrected in the originals. The unknown `x` in 2.15.7(b) and unsupported charge-equality number remain explicitly bounded issues. Review checks do not certify every historical attribution, and no external applet behavior was inferred from still frames. Authoring, PROF evaluation, SASIS and repository changes have not been performed.
