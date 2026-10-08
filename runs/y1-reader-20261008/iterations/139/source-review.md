# D139 source review

Identity: official MIT8.022 session L16; PDF printed Lecture14. The official session and printed PDF numbers are preserved. One assigned PDF, 11 physical pages / 22 numbered slides.

Official asset: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/dc89e80ee651b20cf525d2c89e026fd8_lecture14.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture14/
Original SHA-256: 7b1301592940a98a663abd31089893a0e74a7e454a718be8445e20b9ded95a31; 337112 bytes; matches recorded original-cache hash.

Complete original PDF text read; all full original-page images actually inspected, including every diagram, label and equation. All current PNGs decode and have nonuniform content. No failed derivatives, source/cache edits, or historical-audit changes.
# Complete coverage

- p1, slides1–2: Title/topics; static E/B equations, potentials, correct Biot–Savart order.
- p2, slides3–4: Perspective moving rod, B/v and effective-force/E2 arrows, charge signs; uniform out-of-page dot field and descending rectangular loop with separated charges.
- p3, slides5–6: Loop crossing dashed field boundary, out-of-page B above/zero below, current path and downward velocity; upward reaction force and claimed nonconservative E.
- p4, slides7–8: Sliding bar/rails/resistor complete topology, width x, length L, B dot, endpoint signs, rightward velocity and counterclockwise current; emf/current/flux equations.
- p5, slides9–10: Both repeated rail-circuit diagrams; left/right motion current cases and clockwise/counterclockwise bar-force claims.
- p6, slides11–12: Original/final arbitrary loop solid/dashed boundaries, swept ribbon, dl, B and mislabeled displacement; full flux-transport/triple-product proof.
- p7, slides13–14: Work-source explanation; magnet-gap/loop/ammeter demonstration and narrow/retraced-wire comparison.
- p8, slides15–16: Stationary-loop changing-B argument; electromagnet pole gap, ring/disk drawing, B arrows, full/cut conductor questions.
- p9, slides17–18: Falling ring front/back current arrows; finite-solenoid return-field drawing with two loop/ammeters; levitating-ring core/B/current/force geometry.
- p10, slides19–20: Spinning conducting disk, magnet N pole, support/plastic-separator context, motion and charge signs; Stokes derivation and boxed differential Faraday law.
- p11, slides21–22: Incomplete Maxwell set, divergence interpretation and missing-term hint; integral/differential Faraday summary.

# Technical findings

- D139-F1 (confirmed charge-factor typo, p4 slide7): After emf=(1/q)∫F·ds, the next integrand substitutes(v/c)×B but retains prefactor1/q. Since F=q(v/c)×B, either q must remain inside or outside1/q must cancel. Final vBL/c is correct and has no test-charge dependence.
- D139-F2 (confirmed sign inconsistency, p4 slide8 with rail geometry slide7): x is distance from the moving left bar to fixed right resistor, so rightward speed v gives dx/dt=−v. Source prints emf=vBL/c=(BL/c)dx/dt while saying fluxBLx decreases. With counterclockwise positive traversal and outward normal, correct emf=−(BL/c)dx/dt=vBL/c.
- D139-F3 (confirmed force-direction error, p5 slide10): For depicted external B out of page, counterclockwise current flows downward in left bar: (−yhat)×zhat=−xhat, so force is left. Clockwise current flows upward and force is right. Source lists clockwise→left and counterclockwise→right, reversed. Force on the bar uses external B; the field created by the induced current is not a substitute for it.
- D139-F4 (physical field/force conflation, p2–3 slides3–6): E1=v×B/c is a magnetic force-per-charge shorthand in the lab, not the lab electric field. For the imposed static B model, nonzero motional emf does not imply ∮E_lab·dl≠0 or curlE_lab≠0. The correct moving-circuit integral is∮[E+v_wire×B/c]·dl. Source slide6’s equation is false if E means the Maxwell electric field in that same static-field lab; it can describe an effective field only with that definition, or an appropriately transformed frame.
- D139-F5 (confirmed source typo, p6 slide11): Swept-loop picture labels its displacement v+Δt, dimensionally invalid; formula directly below correctly uses vΔt.
- D139-F6 (confirmed wrong proof hint, p11 slide21): Hint says take divergence of Faraday law to find missing Maxwell ingredient. That gives0=−c^−1∂t(divB), already0. Divergence of uncorrected Ampere instead gives divJ=0; with continuity and Gauss it exposes need for displacement term(1/c)∂tE. The hint names the wrong law for this argument.
- D139-C1 (proof scope / missing conditions, p4–8 slides7–15; p10 slide20): Sliding-bar I=vBL/(cR) neglects self-inductance/transients, contact effects and other resistance. Ribbon proof derives motional flux rule for static B and moving material loop using divB=0 and matched orientation; it is not by itself proof for an arbitrary time-changing field. Relativity motivates corresponding relative-motion cases, not every B(t) as a Lorentz boost of a static field. Fixed-loop ∮E·dl=−c^−1∂t∫B·da and differential curlE=−c^−1∂tB are correct. For moving surfaces, use total flux derivative with the motional term.
- D139-C2 (unsupported generalization / missing experimental conditions, p7–10 slides14–19): Nonzero area alone does not guarantee emf; changing linked flux is required. Zero geometric signed area is not a universal no-emf test in nonuniform fields; the retraced-wire ideal is narrower. Falling finite-resistance loop in static localized B develops drag, not guaranteed sustained levitation: at rest motional emf vanishes and current decays. Disk has local eddy paths; a cut ring suppresses the large closed path but not every local eddy current. Levitating/spinning demos need geometry, time dependence/speed, resistance and force-vs-weight conditions not supplied.
- D139-C3 (idealization / overbroad field-line statement, p9 slide18; p11 slide21): Solenoid B outside=0 is an infinite-solenoid idealization; drawn finite solenoid has return lines. A loop outside but encircling an ideal solenoid can link changing interior flux and have emf even if B at the wire is zero. DivB=0 means no local magnetic source/sink, not that every field line is a closed curve; uniform B has unbounded straight field lines.

# Independent checks


In the descending-loop picture v=−v yhat and B=B0 zhat, so v×B points−x: positive charges move left on the top segment. The current path is counterclockwise, creates outward B to oppose loss of outward flux, and its top-segment force(−xhat)×zhat=+yhat points upward. The dashed boundary separates B0 from0; this discontinuity is tangential to its normal, consistent with divB=0 in the ideal imposed-field model.


For the shrinking rail rectangle with external B out of page and positive counterclockwise circulation, flux=BLx and dx/dt=−v. Thus emf=vBL/c, current I=vBL/(cR), bar current downward, Fbar=−ILB xhat/c. Maintaining speed requires mechanical power (ILB/c)v=I emf=I²R. This directly verifies the Lenz sign and resolves magnetic-force work: total charge velocity is wire velocity plus drift, magnetic force dot total velocity is zero, while the mechanical driver supplies Joule heat. The source’s later work discussion is consistent with this.


For a material loop translating through static B, oriented swept area is da=(v dt)×dl with compatible boundary orientation. Flux difference follows from zero flux through the closed ribbon plus old/new caps (divB=0). Triple product gives dΦ/dt=−∮(v×B)·dl, hence emf=−(1/c)dΦ/dt. For general moving loop the transport identity is dΦ/dt=∫S∂tB·da−∮(v×B)·dl; combining with local Faraday gives∮(E+v×B/c)·dl=−(1/c)dΦ/dt. A deforming/sliding circuit additionally requires a well-defined circuit boundary velocity and material/contact model.


The stationary-loop Stokes calculation is correct for smooth fields and fixed oriented surface: surface integral of curlE+(1/c)∂tB vanishes for arbitrary surfaces, implying the local equation. CurlE can still vanish where ∂tB=0 even though it is not generally zero. The provisional Maxwell set is explicitly announced incomplete; omitting displacement current at that stage is not itself presented as final general Maxwell theory.


Demo conclusions can only be conditional from this PDF: closed conductor paths crossing gradients yield dissipative eddy-current braking; an open large ring cannot carry the same continuous ring current. A stationary loop linked to switched solenoid flux responds during switching, while constant current gives no transformer emf after transients. The rotating disk can exchange mechanical work with induced currents and magnetic forces; no dimensions/speed/mass are given to prove lift. The source’s actual classroom demonstrations were not observed.

# Limits

- No demo video, apparatus specification, experimental trace or outside activity is an assigned inspected asset.
- No external research required to resolve sign/algebra questions. Levitation strength and detailed demo behavior remain conditional because source parameters are absent.
- The source repeatedly spells Lenz as “Lentz” and eddy as “Eddie”; these naming typos do not change the equation checks.

No learner diagnosis, lesson authoring, skill judgment or additional-asset inspection claims.
