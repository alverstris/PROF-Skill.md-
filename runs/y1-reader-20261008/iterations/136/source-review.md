# D136 source review

Identity: official MIT8.022 session L13, PDF printed Lecture11; 12 physical pages / 24 numbered slides. Session/PDF numbering is preserved.

Official asset: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/d876dcd7dec74b158ff59b54f9e706d0_lecture11.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture11/

# Original access recovery and correction

Preserved cache: 12288 bytes, SHA-256 17b6d9bc1c32846d9c9db35b509815294a7c3fcba3dfb39b5b00b0a3bf74104e; matches historical audit but currently parses zero pages. Its header declares /L97217 /N12. pdfinfo reports invalid XRef, missing endstream and null top-level pages (exit99).

Fresh official HTTP200 recovery: 97217 bytes; SHA-256 c1f34755a19ec268f2ccc41e7b00f99fcf3a656b9d31a554e3f2226e810540db;12 pages. Exact response URL/headers, content length97217, application/pdf, ETag and response date are in official-response.json. The full recovered PDF is official-recovered.pdf. Standard urllib.request.urlopen(URL,timeout=25) performed recovery after an unavailable-requests import failed without writing an asset.

Byte comparison confirms the entire12288-byte cache is an exact prefix of the97217-byte official PDF. All12 fresh PNGs rendered from the recovered file with PyMuPDF Matrix(1.7,1.7) are byte-identical and pixel-identical to the surviving cached PNGs. Each decodes, has nonuniform content, and was actually inspected as a full page. Complete recovered original text was read and saved as fresh-text.txt. render-validation.json and byte-comparison.json hold the exact page hashes and comparison results.

Historical original/audit/selection files remain unchanged. An explicit current access-evidence correction is warranted: the historical cached hash is not the hash of a currently complete readable PDF; this review relies on the separately recovered complete official asset. The matching prefix and all-page renders establish content identity. Nothing here establishes when or why the defect occurred.
# Complete text and visual coverage

- p1, slides1–2: Title/topics and motivation only.
- p2, slides3–4: Two SR postulates/inertial-frame statement; train, velocity arrow, table, falling ball and observer descriptions.
- p3, slides5–6: Train transverse light apparatus, height h, sensor/source; diagonal h-prime light path and vertical leg; full Pythagoras/time equations.
- p4, slides7–8: Gamma definition and time-dilation statements; train longitudinal light source, mirror, two directions and leftward motion.
- p5, slides9–10: Train-rest length L dimension; station shifted dashed train boundaries, both light legs and moving-endpoint timing equations.
- p6, slides11–12: Round-trip sum, contraction derivation and summary equations.
- p7, slides13–14: Cosmic-muon inputs, both reference-frame calculations and numerical values.
- p8, slides15–16: Muon exponential-decay graph with axes; sea/Everest survival values; transverse train/tunnel contradiction arithmetic.
- p9, slides17–18: Both unprimed/primed xyz frame drawings, common boost direction; full A,B,C,D coefficient equations.
- p10, slides19–20: Repeated frame drawings; light along x and y constraints, coefficient algebra and positive gamma branch.
- p11, slides21–22: Forward/inverse spacetime maps, xyz boost frames, full longitudinal velocity derivative and inverse.
- p12, slides23–24: Transverse-velocity derivative, boxed forward/inverse forms, boost axes; summary.

# Technical findings

- D136-F1 (confirmed source algebra typo, p3 slide6): Pythagorean expansion prints Δt2² where h²/c²=Δt1² belongs: the displayed intermediate equality becomes Δt2²=Δt2²+(v²/c²)Δt2². Replacing that first RHS time by Δt1 gives the correct final Δt2=γΔt1.
- D136-F2 (confirmed arithmetic error, p7 slide14): For β=.9999, γ=70.71245 and τ0=2.2 μs, γτ0=155.567 μs and mean lab decay length βcγτ0=46.633 km (about46.8 using source rounded156μs and c=.3km/μs), not42km.
- D136-C1 (missing condition / probabilistic interpretation, p2–8 slides3–16): SR postulates here concern inertial Cartesian frames and vacuum light; the train/station are idealized constant-velocity frames in a Newtonian gravity picture. γ≥1 for |v|<c, strictly>1 only v≠0. One-way transverse emission/detection occur at distinct y positions, so h/c is a rest-frame coordinate interval, not their timelike proper interval; the factor follows Δx=0 or can describe a full light-clock cycle. Length means endpoint coordinates simultaneous in the measuring frame, parallel to boost. Muon lifetime is an exponential mean, not a fixed maximum; “cannot reach ground” overstates the nonrelativistic prediction.
- D136-C2 (conditional model and proof boundaries, p8–12 slides15–24): Muon flux illustration assumes fixed20km origin, vertical paths, fixed speed/no energy loss and decay-only attenuation, not a complete atmospheric flux prediction. Tunnel argument excludes the posited perpendicular contraction; unchanged transverse coordinates and linearity also use aligned axes, homogeneity/isotropy and identical units. A=+γ chooses continuity/time orientation; algebra yields ±. Velocity formula denominators are positive for |v|<c and physical |u|≤c. Light retains speed c; summary “v always<c” applies to massive particles and frame boosts, not light.
- D136-T1 (minor source wording typo, p12 slide23): The transverse-velocity question names measured ux while the calculation and boxed conclusion correctly compute uy.

# Independent checks

For the train moving left in the longitudinal diagrams, the outward right-going leg is L′/(c+v) and return leg L′/(c−v). Their sum is2L′γ²/c; comparing with γ(2L/c) gives L′=L/γ. The source’s leftward arrow makes these signs consistent. Time-dilation formula is used legitimately for the longitudinal round trip, whose emission and return are at the same train location.

Muon source estimates0.65N0 and0.77N0 imply about15–16% fewer at sea level relative to Everest, not a15-percentage-point difference. Exact source-model calculation gives {"gamma": 70.71244595191452, "mean_lab_lifetime_us": 155.56738109421195, "mean_decay_length_km": 46.63326377010024, "sea_survival": 0.6512391087934126, "everest_survival": 0.7731153283267974, "sea_relative_decrease": 0.15764299978006324}. The later exponential account qualifies the earlier categorical reach/no-reach wording.

Coefficient check: origin motion gives B=−Av and D=A; x-directed null propagation gives C=−Av/c²; y-directed null propagation gives A²(1−β²)=1. With the positive branch, both spacetime maps are inverse and preserve c²dt²−dx²−dy²−dz². Differentiation yields ux=(ux′+v)/(1+vux′/c²) and uy=uy′/[γ(1+vux′/c²)], with the correctly printed inverse signs. At v=0 they reduce to identity, and longitudinal light speed±c remains±c.

No learner diagnosis, lesson authoring, skill judgment or additional asset claims.
