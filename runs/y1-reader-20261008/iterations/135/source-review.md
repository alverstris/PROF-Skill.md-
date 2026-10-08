# D135 source review

Identity: official MIT8.022 session L12; PDF printed Lecture 10. One assigned PDF, 11 physical pages / 22 numbered slides. The session/PDF numbering difference is preserved.

Official asset: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/f8443a251633d63eeb0e19a7b213d4ce_lecture10.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture10/
SHA-256: 76c2f871ae70bbfe143eaa65196e001464e7695adae65b2142c53d3b9e66c11e; 130794 bytes; matches recorded original-cache hash.

Access: complete original PDF text read and all eleven full original-page renders actually inspected. Every current PNG decodes and has nonuniform content. No failed derivative; no source/cache/history changes.

# Complete page and visual coverage

- p1: slides 1–2. Title/topics; N/S bar-magnet drawing, pole colors and compass/pole statements.
- p2: slides 3–4. Oersted text; parallel/antiparallel current arrows and force arrows; circular field/right-hand-rule drawing.
- p3: slides 5–6. Gaussian and SI Lorentz laws and units; xyz frame, out-of-page B dots, v/F arrows and curved positive-charge track.
- p4: slides 7–8. Cathode-ray tube with electrodes and B arrow; repeated tube, xyz axes, crossed-field balance and electron deflection equations.
- p5: slides 9–10. High-energy tracking equations; full BaBar event plot with detector outlines, charged pion/kaon/muon trajectories and labels, neutral Ks label and inset interaction-region boundaries.
- p6: slides 11–12. Electric-work sign; magnetic-work dot product; distributed-current force equations and straight-wire reduction.
- p7: slides 13–14. Gauss/Ampere integral laws, closed path; long-wire axial current, circular Amperian loop, radius and B arrow.
- p8: slides 15–16. Two-wire force directions/equations; finite strip cross-section, into-page currents, width L, xy axes and angle theta.
- p9: slides 17–18. Strip integral and angular substitution; upper/lower B arrows, into-page wire array, finite width and infinite-sheet jump.
- p10: slides 19–20. SI conversion and constants; Cartesian azimuthal-field components/divergence derivation, monopole caveat.
- p11: slides 21–22. Frame-dependent electric/magnetic interpretation and summary/outlook; no additional figures.

# Technical findings

- D135-F1 (confirmed source inconsistency, p4 slide8): Printed Δy=−qEL²/(2mv²), v=cE/B imply q/m=−2Δy c²E/(B²L²), but final equation has plus. No fixed signed Δy/q convention makes the two printed equations agree. If Δy is a positive deflection magnitude, the first equation must be rewritten accordingly.
- D135-F2 (confirmed source error in stated application, p5 slide9): The explicitly high-energy tracking example prints R=mvc/(qB), p=mv. For rest mass m, relativistic p=γmv and R=p_perp c/(|q|B) in Gaussian units. If m meant relativistic mass this must be stated; the preceding Newtonian derivation does not establish that convention.
- D135-F3 (confirmed source typo, p10 slide19): Printed μ0=4·10^−7 N/A² omits π. Even the historical SI value is 4π·10^−7 N/A². The adjacent wire-field formula μ0 I/(2πr) is correct.
- D135-F4 (confirmed source algebra error, p10 slide20): After correct φhat=(x yhat−y xhat)/r, the source prints B=(2I/(cr))[(x yhat−y xhat)/(x²+y²)], introducing an extra 1/r. Correct B=(2I/c)(x yhat−y xhat)/(x²+y²). Its displayed divergence also treats the leftover r factor as constant. Correct component differentiation cancels, yielding div B=0 for r>0; the final zero is not evidence that the intermediate formula is right.
- D135-F5 (confirmed source wording typo, p7 slide13): The Ampere-law application repeats “E can be easily computed”; this context requires B.
- D135-C1 (conditional models and missing domains, p2–3 slides3–6; p7–9 slides13–18): Neutral ideal steady wires need a stated zero-external-E model; global neutrality alone does not prove it. Circular motion requires uniform B, E=0 and v perpendicular B; otherwise the parallel component yields a helix. Positive radius uses |q| and nonrelativistic derivation requires v≪c. Ampere without displacement term is magnetostatic. Infinite wire has r>0 and neglects ends. Infinite-sheet independence of y holds only in the wide-sheet/infinite limit at fixed K=I/L; finite strip has Bx=sgn(y)4I arctan[L/(2|y|)]/(Lc).
- D135-C2 (conditional interpretation, p6 slides11–12; p10–11 slides19–21): −q∫E·ds is external quasistatic work, not work by the electric force. The magnetic part of force does no instantaneous particle work, not a claim of zero energy cost for every magnetic apparatus. SI conversion phrase is a mnemonic for displayed B-source formulas, not a universal conversion of numerical quantities. Div B=0 is the no-magnetic-charge Maxwell model; a single wire example cannot prove it generally. Special-relativistic frames should be inertial; moving observers generally see both E and B, and force components are not invariant.

# Independent checks and boundaries

The Lorentz cross product gives downward bending for positive q moving +x with B out of the page; electron bending reverses. The cathode-ray balance gives speed cE/B. The beam displacement formula assumes a uniform field of length L, constant vx, no fringe/drift contribution and negligible relativistic effects. The terminal e/m equality has the explicit sign conflict recorded above.

For a steady straight wire, Ampere gives Bφ=2I/(cr); current-force integration gives F/L=2I1I2/(c²r), attractive for parallel conventional currents. Strip superposition uses dI=(I/L)dx and ∫y dx/(x²+y²), producing the finite arctangent formula and the ±2πK/c sheet limits, with jump 4πK/c. The drawings’ signs are consistent with current −z. Wire/sheet idealizations have singular or discontinuous boundaries; field at an ideal sheet requires one-sided limits.

The BaBar figure is an illustrative event display: all trajectory labels, inset and outer detector boundaries were inspected. It supplies no quantitative scales or B orientation sufficient to infer individual momenta or independently verify particle identification from the image. Curvature alone determines transverse momentum per charge magnitude with known B, not mass or total energy.

The historical name is printed “J.J. Thompson”; the physicist is J. J. Thomson. Historical narratives, referenced demos and experimental particle identifications were not externally audited. Magnetic response of gold/silver/copper is idealized in the ferromagnet contrast. No learner diagnosis, lesson design or skill-quality judgment is included.
