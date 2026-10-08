# D107 source review

Technical source preparation only, 2026-10-08. D107 maps to **MIT 8.02T Spring 2005 Studio S04**, original order 107 and selected active order 36: Working in Groups; Experiment 1: Visualizations; Electric Potential. Mapping was read from the exact selection/audit records. This report does not author a teaching route or close an iteration.

## Packet, reading boundaries and fresh coverage

All three original cached PDF SHA-256 hashes were recomputed and match the assigned audit. `source-map.json` records hashes, URLs, exact paths and every inspected page/render hash. Originals/cache were not changed.

| Alias | Original PDF | Required scope | Printed locator |
|---|---|---|---|
| P | `b7a8083d46b9980583bf4336da37f1ed_presentati_w02d1.pdf` | PDF 1–36 entire presentation | P04-1…36; PDF 3–6 print only P04- without a numeral |
| Q | `1840eda396cfce6f0854cdb391dfb17b_prs_w02d1.pdf` | PDF 1–12 entire PRS | PRS04; use PDF page |
| C3 | `2290d16cb4d4f5affd3c57b6ab828ae8_ch3electri_poten.pdf` | §§3.1–3.5: heading §3.1 PDF2 through Example 3.4 on PDF18; stop before §3.6 | printed1–17 (PDF−1) |

**65 of 65 required page occurrences freshly opened as full-page renders and read against fresh original-PDF text extraction.** Complete required equations, diagrams, labels, tables, graph scales and PRS answer indications were inspected. C3 §3.6 text visible on the boundary render is outside this assignment. The prior audit served as inventory only. P1–7's classroom/group instructions were read as historical course instructions, not commands to the reviewer; Experiment 1's separate manual is outside the selected packet.

C3 boundaries: §3.1 PDF2–5 (printed1–4, ends before §3.2); §3.2 PDF5–6; §3.3 PDF6–9, including §3.3.1 PDF8–9; §3.4 PDF9–10; §3.5 PDF10–18, including §3.5.1 PDF11–18 and Examples3.1 PDF13–15, 3.2 PDF15–16, 3.3 PDF16–18, 3.4 PDF18. Every numbered/unnumbered visual covered: Figures3.1.1–2, 3.2.1–2, 3.3.1–3, 3.4.1, 3.5.1–7, source-labelled 3.4.3–4 (disk and potential comparison), and comparison table PDF7. All P drawings, repeated landscape surfaces P21/23/28, graph P32, triangle P35 and three-charge diagram P36 were inspected; Q9–10 diagrams included.

## Mathematical verification and keyed answers

Work/potential signs were checked from dU=−F·ds and dV=−E·ds, gradients by direct differentiation, charge sums pair by pair, and continuous potentials by scalar integration. The common domain is static vacuum electrostatics; fixed source charges and negligible disturbance by a test charge. A potential zero is a chosen reference. V is energy per charge, U energy of the interaction; V=0 at a point does not mean E=0 there.

| Source | Independent result |
|---|---|
| P11–15; C3 3.1.1–8 | W_g=GMm(1/rB−1/rA), negative for pictured outward displacement. U_g=−GMm/r+C. Near Earth's surface W_g=−mgΔy; V_g=U_g/m up to reference. Inverse-square Earth formula is for an exterior point under spherical symmetry, not inside a uniform sphere. |
| P18–22,26; C3 §§3.1–3.3 | ΔV=−∫E·ds, U=qV; point-charge V=kQ/r with infinity zero. Uniform field ΔV=−E·Δr, so travel perpendicular to E has zero potential difference even though E is nonzero. |
| P30–31; C3 3.5.1–9 | E=−∇V; along an equipotential E·ds=0. Nonzero gradient is normal to a regular level surface. At critical points E=0, a unique field direction is not defined. Maximum directional derivative is |∇V|; steepest descent is −∇V. |
| P34–35; C3 3.3.5–9 | U=Σ_(i<j)kqiqj/rij=(1/2)ΣqiV_other(ri). Pair counting and exclusion of self potential verified. First charge costs zero interaction energy only in otherwise empty space, with self-energy omitted. |
| C3 Example3.1, PDF13–15 | V(y)=kλ ln[(sqrt(y²+L²/4)+L/2)/(sqrt(y²+L²/4)−L/2)]=2kλ asinh[L/(2|y|)]. For y>0, E_y=kλL/[y sqrt(y²+L²/4)]. For L≫y>0, V≈2kλ ln(L/y). Infinite line at fixed λ has divergent infinity-referenced V; finite potential differences remain usable. |
| C3 Example3.2, PDF15–16 | On ring axis V=kQ/sqrt(R²+z²), E_z=kQz/(R²+z²)^(3/2); E=0 but V≠0 at center. Far-field potential kQ/|z|; source's kQ/z uses z>0. |
| C3 Example3.3, PDF16–18 | Disk V=σ/(2ε0)[sqrt(R²+z²)−|z|], finite center V=σR/(2ε0)=2V0. For z≠0, E_z=σ/(2ε0)[sgn(z)−z/sqrt(R²+z²)]. One-sided near-sheet limits are ±σ/(2ε0), with sign of z. Graph's finite cusp, disk/point-charge curves and normalization checked. |
| C3 Example3.4, PDF18 / printed17 | V=Ax²y²+Bxyz gives E=(−2Axy²−Byz)i+(−2Ax²y−Bxz)j−Bxy k; all printed derivative results verified. |

PRS Q1→Q2: **3**, only the nonzero-gradient linear gravitational potential produces acceleration; “constant potential” must mean spatially constant in a neighborhood, not merely a horizontal equipotential surface in nonzero gravity. Q3→Q4: **2**, positive charge initially released from rest moves toward lower V and U. Q5→Q6: **4**, negative charge initially released from rest moves toward higher V and lower U. Q7→Q8: **4**, statements I and II true under quasistatic external-work convention and electrostatic field; III false since q<0 and ΔV<0 imply ΔU>0. Q9→Q10: **3**, midpoint V=kq/r−kq/r=0, so field work is zero and external work is zero if initial/final kinetic energies agree. Q11→Q12: **2**, local steepest descent in V; this is not a shortest-time particle trajectory statement.

## Confirmed errors and conditions that prevent misuse

1. **C3 equation3.5.2, PDF10 / printed9:** both expanded expressions omit the minus sign from dV=−E·ds. Correct is dV=−(Ex dx+Ey dy+Ez dz). Equations3.5.1, 3.5.3 and 3.5.5 immediately surrounding it are correct; original full render confirms a source sign error.
2. **P30, bottom prose:** “Ex = Rate of change in V” lacks “negative”; the boxed equation correctly gives Ex=−∂V/∂x. Treat the prose literally as a sign error and use the verified equation.
3. **Q4 and Q6:** “Objects always move to reduce their potential energy” is false in general. For a positive charge initially moving against a uniform E, dU/dt=−qE·v>0 while it slows down. The keyed directions are valid for release from rest/initial free acceleration with no competing force. The source does not state that condition in these PRS questions; preserve it as an added assumption, not as source text. No extraction ambiguity is involved.
4. **C3 PDF7 / printed6, comparison table:** rows label `V_g=−∫_A^B g·ds` and `V=−∫_A^B E·ds`; those integrals are potential **differences**, or potentials at B only after V(A)=0. Final row `|ΔU|=qEd` needs `|q|` if q is signed, and d must be displacement projected along the field (or motion parallel/antiparallel). Table context follows a positive-charge example, but it should not be generalized verbatim.
5. **C3 Examples3.2–3.3, PDF15–16:** “distance z from the central axis” is inconsistent with the drawings and calculations. P is **on** the central axis at axial displacement z from the center/plane. The diagrams and full derivations resolve this wording; it is not an off-axis potential result.
6. **C3 PDF18 / printed17:** text after equation3.5.16 cites equation2.10.18, which is the disk's far-field Taylor expansion, rather than the matching two-sided field in 2.10.16–17. Its stated positive near-sheet value assumes z>0; for z<0 it reverses. Example3.4 mentions an unused constant C; it does not occur in V. A constant C, if added, would not affect E.

**Work convention requiring explicit scope:** P14/P19 and C3 PDF3 equate W_ext=ΔU=−W_field without initially stating ΔK=0. General relation with no other work is W_ext=ΔK+ΔU. C3 PDF4 explicitly supplies “without changing its kinetic energy” and PDF8 describes assembly ending at rest; these resolve the intended quasistatic/endpoint-rest convention. “No work required along an equipotential” refers to electric work or external work with ΔK=0, not every externally driven motion. Likewise static-field conservative work is not a claim about induced fields in time-dependent magnetism.

## Supplemental deductions for unkeyed presentation problems

These are reviewer computations absent from the slides, not an authored lesson or source answer key.

- **P32:** source graph passes through (−2 m,−10 V), (−1 m,0 V), (0,10 V), (2 m,5 V). Thus Ex=−10 V/m on the left of x=0 and +2.5 V/m on the right, over the shown linear intervals. E at the ideal cusp is undefined as a single two-sided derivative. If V depends only on x (planar symmetry), the jump implies a positive sheet at x=0, σ=ε0(12.5 V/m). A one-dimensional slice alone does not establish the complete three-dimensional charge distribution; transverse second derivatives are unspecified. The unequal field magnitudes can coexist with a uniform background field.
- **P36:** charge positions are (−a,0):−Q; (0,0):−Q; (a,0):+Q; P=(0,a). Side charges have equal distance √2 a from P and cancel in the scalar potential, so V(P)=−kQ/a. Pair energies are +kQ²/a, −kQ²/a, and −kQ²/(2a), totaling U3=−kQ²/(2a). Bringing +3Q quasistatically from infinity to P adds ΔU=3QV(P)=−3kQ²/a; negative work means energy is extracted, not positive energy supplied. U4=−7kQ²/(2a) if requested. Originals supply no numerical Q or a, so these are symbolic quantities with SI units when Q,a are in C,m.

## Handoff limits

No required reading glyph, graph label or answer indication remains unresolved. All six PRS pairs are legible; each answer has been independently checked with its assumptions. Six grouped source error/notation findings above are resolved mathematically or by the source's own diagrams; the complete 3D charge distribution behind P32 remains underdetermined without a symmetry assumption. No claims of observed live demonstrations, lab completion, learner performance, authored route or iteration closure are made.
