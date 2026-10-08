# D138 source review

Identity: official MIT8.022 session L15; PDF printed Lecture13. The official session and printed PDF numbers are preserved. One assigned PDF, 9 physical pages / 18 numbered slides.

Official asset: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/c60353232b6ab6cb77de48f0f6572b50_lecture13.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture13/
Original SHA-256: 2dca9b750c3146b97bb49d2b9fb4e879d791154c041b3451e1ebbdf572f63dde; 142912 bytes; matches recorded original-cache hash.

Complete original PDF text read; all full original-page images actually inspected, including every diagram, label and equation. All current PNGs decode and have nonuniform content. No failed derivatives, source/cache edits, or historical-audit changes.
# Complete coverage

- p1, slides1–2: Title/topics; Lorentz, Ampere and wire-field summary equations.
- p2, slides3–4: Full Cartesian wire-field/divergence derivation; Stokes surface and differential Ampere proof.
- p3, slides5–6: Static Maxwell-equation collection; scalar/vector potential definitions and curl/divergence identities.
- p4, slides7–8: Uniform-B vector-potential component equations and three candidate potentials; question on generating current; curl-curl identity and Coulomb-gauge Poisson equation.
- p5, slides9–10: Three component Poisson equations, source volume/wire integrals; full Biot–Savart differentiation with product rule and final cross-product order.
- p6, slides11–12: Curved current element, dl and source-to-observer rhat arrows, into-page dB; loop, xyz axes, radius/height geometry, theta/90−theta, full axial-field derivation.
- p7, slides13–14: Finite stacked-ring solenoid and integration range; horizontal solenoid with rectangular Ampere loop crossing interior/exterior.
- p8, slides15–16: Finite-solenoid current arrows, internal and returning external field lines; demo references and quantitative solenoid line with question marks.
- p9, slides17–18: Electron-beam V,I,R and stated e/m answer; summary equations.

# Technical findings

- D138-F1 (confirmed source algebra error, p2 slide3): Repeats extra1/r in Cartesian B: after φhat=(x yhat−y xhat)/r, prints (2I/(cr))(x yhat−y xhat)/(x²+y²). Correct factor is2I/c. Printed divergence also ignores derivatives of the leftover1/r. Correct Cartesian field has zero divergence for r>0; final zero does not validate wrong intermediate field.
- D138-F2 (confirmed source sign typo, p4 slide7): Bz requirement is printed ∂Ax/∂y−∂Ay/∂x=B0, the negative of correct curl component. All three candidate potentials instead satisfy ∂Ay/∂x−∂Ax/∂y=B0, so candidates are correct for stated B=B0 zhat and the requirement line has its sign reversed.
- D138-F3 (confirmed numerical/unit error in explicitly questioned line, p8 slide16): The line substitutes4.5 into Gaussian4πnI/c while given current is4.5mA, without statampere conversion; it also substitutes length50cm instead of stated46cm. Its raw displayed arithmetic is1.0405×10^−7, not230×10^−8. Taking stated4.5mA,2760turns,.46m literally gives long-solenoid SI B≈3.39292×10^−5T=.339292G. Source ends “Gauss ???”, so the line is visibly questioned rather than an unambiguously endorsed measured result. Whether mA was intended instead of A remains unresolved.
- D138-C1 (conditional equations / missing mathematical conditions, p1–5 slides2–10): Ampere without displacement current and instantaneous Green-function A are magnetostatic. E=−gradφ and curlE=0 are electrostatic, as acknowledged by incomplete-Maxwell wording. DivcurlA=0 requires smoothness (or distributions); divB=0 alone gives local A, with global existence/boundary/topology qualifications. Coulomb gauge divA=0 and decaying localized steady currents justify component Poisson solution A(x)=c^−1∫J(xprime)/|x−xprime|d³xprime; arbitrary homogeneous/boundary solutions are otherwise missing. Infinite-wire A needs a reference/gauge regularization though B remains finite off-axis.
- D138-C2 (overbroad interpretation, p3 slide6; p4 slide7): “A is not connected to work or energy (but to angular momentum)” is too broad. A is not a scalar work-per-charge potential, but enters canonical linear momentum pcan=pmechanical+qA/c and the Hamiltonian; time-varying A contributes −∂tA/c to E. Scalar potential uniqueness needs specified appropriate boundaries/reference (Neumann data leave a constant); gauge change A→A+gradχ leaves B unchanged. Uniform B implies local J=0 in magnetostatics, not a unique generating apparatus.
- D138-C3 (conditional solenoid model, p6–8 slides12–16): Loop on-axis formula is correct; intermediate r=sqrt(R²+h²) uses undeclared h where axial z was specified. Stacked-ring integral is for midpoint and ideal continuum of turns. Exact outside-zero, radius-independent interior B=4πnI/c applies to infinitely long ideal solenoid with no imposed background; finite drawing/field-line picture has return field and end effects. L≫R gives central approximation, not exact everywhere/outside. A drawn finite Ampere rectangle cannot alone remove its external/edge contributions.
- D138-U1 (unresolved required numerical calibration / source omission, p9 slide17): V=300V,I=1.4A,R=5cm do not determine e/m without the apparatus B(I) calibration or coil geometry/turn count. From nonrelativistic eV=mv²/2 and R=mv/(eB), e/m=2V/(B²R²); stated2.02×10^11 C/kg would require B≈1.09001mT at1.4A. This is a reviewer inference, not evidence of missing coil parameters. The stated comparison value1.76×10^11 gives an experimental difference≈14.8%, not by itself a confirmed source error.

# Independent checks


Correcting the uniform-field curl sign, A1=(−B0y,0,0), A2=(0,B0x,0), A3=(−B0y/2,B0x/2,0) each give curlA=B0zhat and divA=0. A2−A1=grad(B0xy); A3 differs by half this gradient. Gauge freedom therefore survives divA=0 for these examples. CurlcurlA=grad(divA)−LaplacianA gives LaplacianA=−4πJ/c in Coulomb gauge.


Biot–Savart source sign is correct despite scrambled text extraction: the image explicitly has dl×rhat. Derivative is with respect to observation point; grad(1/r)=−rhat/r², and (−rhat)×dl=dl×rhat. The diagram has dl rightward, r down-right and dB into the page, consistent with the cross product. A current segment alone is not a self-contained steady current; the wire integral presupposes a complete steady distribution.


Loop-axis integration gives Bz=2πIR²/[c(R²+z²)^(3/2)], center2πI/(cR), even in z, and far-axis decay proportional|z|^−3. Transverse components cancel. For turns per length n, midpoint integration gives B=4πnI L/[c sqrt(L²+4R²)], approaching4πnI/c asL/R→∞. The finite-length correction is smaller than one. Thin-wire observation points on the wire itself are excluded.


Taking printed solenoid inputs literally in consistent SI units gives B≈.339292G, subject to unknown finite-radius correction. The source’s I=4.5mA is not silently changed to4.5A. Demo questions about collapse can be explained conditionally by attraction of parallel currents in neighboring turns; the actual experiment was not observed. Electron beam e/m follows from the stated nonrelativistic model, but missing B(I) prevents reproducing the numeric answer from this PDF alone.

# Limits

- Referenced problem set7, classroom demonstrations and coil calibration are not assigned assets and were not inspected.
- No targeted external research was needed; consequential issues are algebra/unit/model checks or an explicit missing apparatus parameter.
- The empirical no-monopole remark and historical “Thompson” name were not externally audited; universal absence is not proved by the wire example.

No learner diagnosis, lesson authoring, skill judgment or additional-asset inspection claims.
