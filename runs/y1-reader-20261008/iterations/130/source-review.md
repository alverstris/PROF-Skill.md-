D130 source technical review

Fields and Potentials around Conductors Capacitance

MIT 8.022 Fall 2004. Official indexed session 6; published PDF title Lecture 5; linked file lecture5.pdf. These identities are retained separately. One original PDF, 9 full sheets. Every complete text and original full-page render inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/bbd323d11bd97ec8e514027495551a09_lecture5.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture5/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D130/source.pdf
SHA256: 752defdfe953d4cc5eb1239256b41eecaf276a1b416c9458096e81559553a4c3
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 130, 'active_order': 59, 'queue_selection_evidence': 'Official index labels this row SES # 6: Fields and Potentials around Conductors\n\n\nCapacitance.'}

Page, slide and visual coverage

lecture5.pdf, PDF 1, printed sheet 1, slides 1,2: Printed Lecture 5 title and conductor/vector-calculus recap.
lecture5.pdf, PDF 2, printed sheet 2, slides 3,4: Nonuniform conductor surface charge; Connected unequal spheres and curvature explanation.
Slide 3 — two teardrop charge sketches: Uniform proposal versus concentrated tip charge; equipotential does not imply constant normal field.
Slide 4 — connected spheres: Large R1 sphere linked by thin wire to small R2 sphere; mutual electrostatic influence is omitted from the formula.
lecture5.pdf, PDF 3, printed sheet 3, slides 5,6: Shielding and mesh questions; Point charge above an infinite conducting plane.
Slide 5 — empty enclosed cavity: Conductor surrounds the region labeled E=0.
Slide 6 — point/plane field lines: Positive point charge and negative surface charge; lines approach plane normally.
lecture5.pdf, PDF 4, printed sheet 4, slides 7,8: Image charge and uniqueness; Two-conductor capacitance and scaling.
Slide 7 — charge and mirror image: Positive real charge above plane and equal negative mirror below; mathematical extension is restricted to the upper half-space.
Slide 8 — two irregular conductors: Separated bodies with opposite net charges and nonuniform shapes; equipotential boundary conditions.
lecture5.pdf, PDF 5, printed sheet 5, slides 9,10: Capacitance units; Isolated conducting sphere and reference at infinity.
Slide 10 — sphere with coordinate axes: Radius R and net Q; isolated spherical geometry.
lecture5.pdf, PDF 6, printed sheet 6, slides 11,12: Parallel plates and small-gap approximation; Sheet-versus-conductor field conventions.
Slide 11 — parallel plates: Positive upper plate, negative lower plate, separation d; downward field in gap.
Slide 12 — two sheet/slab diagrams: Infinitely thin charged plane versus two charged faces of a symmetric conducting slab; the two definitions of σ differ.
lecture5.pdf, PDF 7, printed sheet 7, slides 13,14: Concentric spherical shell fields; Spherical capacitance and narrow-gap limit.
Slide 13 — shell radial field: Positive inner shell, negative outer shell; field confined to gap by spherical symmetry.
Slide 14 — shell radii: R1 inner black shell, R2 outer red shell; this indexing differs from the preceding packet.
lecture5.pdf, PDF 8, printed sheet 8, slides 15,16: Charging work and field energy; Coaxial cylindrical capacitor.
Slide 15 — charge transfer between plates: Positive dq moves from negative plate to positive plate during charging.
Slide 16 — coaxial geometry: Inner radius a, outer b and finite drawn length L; equations neglect end fields.
lecture5.pdf, PDF 9, printed sheet 9, slides 17: Next lecture agenda; lower sheet blank.

Findings, conditions and independent derivations

D130-N01 | official_vs_printed_numbering | lecture5.pdf, PDF 1, slides 1,2 | Source identity
The official index/queue/selection identify session 6 (stable ID L06), while the linked lecture5.pdf labels itself Lecture 5.
Retain official session 6 and printed Lecture 5 separately; this is an identity offset, not a reason to reassign the corpus ID.
Audit, queue and selection agree on D130 and the exact asset hash. Printed slide numbers run 1–17 on nine sheets.

D130-C01 | recap_equilibrium_and_uniqueness_conditions | lecture5.pdf, PDF 1, slides 2 | Recap
The vector formulas and Gaussian Poisson/Laplace signs are correct. Stokes alone does not imply curl E=0 without electrostatic conservativity. Conductor properties require equilibrium.
Use mobile carriers (the electron description applies to metals), E_inside=0 in equilibrium, E_out·n=4πσ at a smooth surface, and Dirichlet uniqueness with density and suitable boundary/infinity data.
For fixed test charge F=qE and conservative electrostatic work, all closed circulations vanish, hence curl E=0 locally. With w the difference of two same-data potentials, Δw=0 and zero boundary values imply w=0 by the maximum principle. Charge-free means ρ=0; vacuum alone does not exclude free charges.

D130-C02 | connected_sphere_approximation_and_curvature_scope | lecture5.pdf, PDF 2, slides 3,4 | Charge concentration at a tip
The two-sphere calculation uses isolated-sphere potentials Q_i/R_i while the spheres are connected and influence one another. R1≫R2 alone does not control that approximation. The curvature conclusion is qualitative, not a universal pointwise law.
Require separation much larger than both radii, a thin negligible wire and no nearby external bodies. In that limit Q1/R1≈Q2/R2 and E1/E2≈σ1/σ2≈R2/R1.
For large separation D, φ1≈Q1/R1+Q2/D and φ2≈Q2/R2+Q1/D; the omitted mutual terms reveal the approximation. At a fixed common potential, isolated-sphere E=φ/R, explaining the qualitative enhancement. Local curvature alone does not determine E: a spherical conductor in an external uniform field has fixed surface curvature yet varying normal field, e.g. E_n=Q/R²+3E0 cosθ. The tip diagram illustrates a trend, not a quantified ratio.

D130-C03 | shielding_and_image_boundary_conditions | lecture5.pdf, PDF 3,4, slides 5,6,7 | Shielding and method of images
Exact empty-cavity shielding assumes a closed conductor and no cavity charge. The image construction is correct for a plane held at zero potential with appropriate infinity behavior. The source asks about mesh/perfection but supplies no quantitative answer.
State a grounded infinite plane y=0, real charge Q at (0,h,0), h>0, and physical domain y>0. The image −Q at (0,−h,0) is mathematical and lies outside the physical domain. A candidate must satisfy Poisson as well as the boundary data, not merely match boundary values.
The verified potential is φ=Q/[x²+(y−h)²+z²]^(1/2)−Q/[x²+(y+h)²+z²]^(1/2). It vanishes at y=0, has the correct sole source in y>0 and decays at infinity, so uniqueness applies. E_y(0+) = −2Qh/(s²+h²)^(3/2), giving σ(s)=−Qh/[2π(s²+h²)^(3/2)] and total induced charge −Q by integrating 2πs ds. Mesh apertures do not automatically inherit the closed-boundary proof; no unprovided demonstration is claimed.

D130-E01 | capacitance_scaling_caveat_error | lecture5.pdf, PDF 4, slides 8 | Caveat below potential integral
The source says C is proportional to Q only if there is enough Q, uniformly spread. This conflicts with the displayed V∝Q and Q=CV and is mathematically incorrect in the stated linear model.
For fixed geometry and linear medium, V is proportional to Q and C=Q/V is independent of Q. Uniform surface charge is not required; irregular conductors generally have nonuniform equilibrium charge.
Scaling all prescribed conductor charges by α scales the electrostatic solution φ,E,σ by α through linearity and uniqueness, leaving Q/V unchanged. Continuum electrostatics can fail for very small discrete charges or nonlinear material response, but neither implies the printed C∝Q rule. Choose V=φ_positive−φ_negative so C>0.

D130-S01 | units_sphere_and_parallel_plate_checks | lecture5.pdf, PDF 5,6, slides 9,10,11,12 | Basic capacitances
C_sphere=R and C_plate=A/(4πd) are correct Gaussian formulas. One centimeter of capacitance is approximately 1.11265 pF. The typical pF–μF remark is historical orientation, not a universal range.
Sphere: isolated equilibrium body in vacuum, no internal cavity charges, zero potential at infinity. Plates: lateral dimensions large relative to d and interest away from edges; outside E≈0, not exactly zero for finite plates. Dielectric properties matter if the medium changes.
Sphere E=Q r̂/r² outside and zero inside, so V=Q/R and C=R. For ideal plates, each facing charge sheet contributes 2πσ, yielding gap E=4πQ/A, V=Ed and C=A/(4πd). SI restores C_sphere=4πε0R and C_plate=ε0A/d. From statC/statV, 1 Gaussian cm≈1.11265×10^(-12) F.

D130-C04 | sheet_face_density_convention | lecture5.pdf, PDF 6, slides 12 | 2πσ versus 4πσ
The comparison is correct when Q/A is total charge per projected area of an isolated symmetric sheet and Q/(2A) is the charge on each face of an isolated symmetric slab. It is not the charge split on capacitor plates.
For the capacitor, most charge resides on the facing surfaces in the ideal plate limit, with σ_face≈±Q/A. For an isolated symmetric conductor slab, charge splits equally onto two faces.
The boundary jump is E_n^+−E_n^−=4πσ_sheet. Reflection gives ±2πσ_sheet for a charged sheet; zero conductor interior gives E_out,n=4πσ_face. This explains the two diagrams while avoiding an erroneous factor of two for the capacitor.

D130-E02 | spherical_flux_area_typo | lecture5.pdf, PDF 7, slides 13 | Last flux equation
The source prints E(4πr)=4πQ, omitting the square on r; its subsequent E=Q/r² is correct. The integral uses ds as a surface element without distinguishing it from path displacement elsewhere.
Write ∮ E·dA=E(r)4πr²=4πQ. Spherical symmetry is required to extract E and conclude zero field from zero enclosed charge.
With inner radius R1 and outer R2, E=0 for r<R1 and r>R2, while E=Q r̂/r² in the gap. The surface area and dimensional consistency identify the missing square. At the charged surfaces use one-sided field limits.

D130-S02 | spherical_capacitance_and_limit_verified | lecture5.pdf, PDF 7, slides 14 | Potential difference and thin gap
The spherical integral, sign and capacitance are correct. R1 is inner and R2 outer in this packet. The printed small-gap phrase should be understood as d/R1→0 with d=R2−R1>0.
V=φ1−φ2=Q(1/R1−1/R2)>0 for Q>0; C=R1R2/(R2−R1).
Writing R2=R1+d gives exact C=R1²/d+R1. With inner-sphere area A1=4πR1², the plane approximation A1/(4πd) has relative error d/(R1+d) relative to exact C. As R2→∞ at fixed R1, C→R1, checking the isolated sphere limit.

D130-S03 | charging_work_and_energy_verified | lecture5.pdf, PDF 8, slides 15,16 | Capacitor charging energy
U=Q²/(2C)=CV²/2 and the parallel-plate field-energy check are correct for fixed, linear C and reversible quasistatic charging.
dq denotes positive charge transferred from negative to positive conductor, so dW=V(q)dq. Variable geometry or nonlinear material would require integrating the actual V(q) relation and accounting for other work.
Integrating q/C from 0 to Q gives Q²/(2C). Ideal-plate field energy is E²Ad/(8π)=2πQ²d/A=Q²/(2C). These are stored-energy formulas; a real dissipative charging circuit may draw additional energy from its source.

D130-C05 | cylindrical_end_effects_and_verification | lecture5.pdf, PDF 8, slides 16 | Coaxial capacitor
The coaxial formulas are correct for infinitely long cylinders per unit length or a long finite capacitor neglecting end effects. The finite drawn cylinder is not exactly translationally symmetric.
Use a<b and length L large relative to transverse dimensions, or treat λ=Q/L and capacitance per length. Empty interior and zero exterior field are ideal-model conclusions; finite open ends can leak field.
Gauss gives E=2λ r̂/r in the annulus. V=∫_a^b E dr=2Q ln(b/a)/L and C=L/[2ln(b/a)]. Energy integral ∫_a^b E²(2πrL dr)/(8π)=Q²ln(b/a)/L agrees with Q²/(2C). For b=a+d with d≪a, C≈aL/(2d)=A_inner/(4πd), matching the plate limit.

Independent coverage

- Read all nine complete page texts and personally viewed every original full-page image, including 17 slides and the final blank lower half.
- Checked recap conditions, conductor-tip reasoning, image potential and induced density, capacitance scaling and unit conversion.
- Independently derived sphere, plates, spherical-shell and coaxial fields/capacitances, narrow-gap limits and charging/field-energy formulas.

Technical disposition

Source review complete. Main confirmed defects are the C-versus-Q caveat and missing r² in spherical flux. Other findings distinguish far-separated sphere approximations, grounded-plane uniqueness, equilibrium and charge conventions, fringing/end effects and finite-energy assumptions.

Limits

- Demonstrations D28/D29/D32 and unresolved classroom questions about mesh shielding are not additional assigned assets; no demonstration or quantitative mesh result is claimed inspected.
- Official session number 6 differs from printed Lecture 5 and linked lecture5.pdf; no attempt was made to rename or alter originals.
