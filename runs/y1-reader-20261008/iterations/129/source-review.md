D129 source technical review

Poisson and Laplace Equations Curl Uniqueness Theorem Introduction to Conductors

MIT 8.022 Fall 2004, lecture 4. One original PDF, 13 full sheet pages, usually two slides per sheet. Every complete extracted text and original full-page image inspected; raster-only text recovered visually where noted. SHA256 independently recomputed and matches audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only; no teaching authoring, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/94fbcd2167568164328feac8e82c6019_lecture4.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture4/
Local original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D129/source.pdf
SHA256: 21baf0aef68069129e1fe1a55821b8b7089910bd63c309b6f87fcee61a9c0da6
Mapping: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 129, 'active_order': 58}

Page, slide and visual coverage

PDF 1/printed sheet 1/slides 1,2: Lecture 4 title; potential, field energy and differential Gauss recap.
PDF 2/printed sheet 2/slides 3,4: Cartesian Laplacian as divergence of gradient; Laplacian of a quadratic bowl.
Slide 4 quadratic surface plot: Upward paraboloid φ=a(x²+y²)/4 for positive a; Δφ=a. Vertical plotting scale is illustrative.
PDF 3/printed sheet 3/slides 5,6: Poisson equation; Laplace equation, extrema and Earnshaw theorem.
PDF 4/printed sheet 4/slides 7,8: Cube-charge equilibrium example; Circulation and splitting a loop.
Slide 7 cube charge diagram: Eight corner charges described, with seven visible corner markers and one central test charge; rear hidden corner is not separately drawn.
Slide 8 partitioned closed loop: Two subloops share a seam traversed in opposite directions; outer orientation and seam cancellation are consistent.
PDF 5/printed sheet 5/slides 9,10: Curl normal component as circulation density; Stokes theorem by subdivision.
Slide 9 tiled loop: Outer oriented curve encloses a grid of small loops; inner edges cancel.
Slide 10 oriented boundary and spanning area: Curve C bounds area A; orientation and smoothness conditions are recorded below.
PDF 6/printed sheet 6/slides 11,12: Conservativity implies zero electrostatic curl; Four-side Taylor expansion for a yz rectangle.
Slide 12 coordinate rectangle: Vertices a,b,c,d traversed in the positive-x normal orientation; widths Δy and Δz, centered at P.
PDF 7/printed sheet 7/slides 13,14: Cartesian curl components and determinant; Gradient, divergence and curl summary.
PDF 8/printed sheet 8/slides 15,16: Laplacian and electrostatic summary; Conductors, insulators and mobile carriers.
Slide 16 gold conductor and electrolyte sketches: Au block with electron symbols, and solution with Na+ and Cl− markers. The ionic example contradicts the electron-only definition.
PDF 9/printed sheet 9/slides 17,18: Conductor equilibration and carrier movement; Constant potential, surface charge and normal exterior field.
Slide 17 three-stage polarization diagram: Initial uniform rightward field; positive drift right and negative drift left; final negative left face and positive right face bend exterior field and cancel interior field.
PDF 10/printed sheet 10/slides 19,20: Empty closed cavity and electrostatic shielding; Cavity charge and induced inner/outer totals.
Slide 19 empty cavity: Connected surrounding conductor encloses a charge-free hollow, labeled E=0.
Slide 20 charged cavity and Gaussian surface: Central +Q, negative inner charge, positive outer charge; dashed Gaussian contour lies in conducting material.
PDF 11/printed sheet 11/slides 21,22: Surface charge and field jump; Dirichlet uniqueness proof.
Slide 21 charged cavity surface diagram: Positive external and negative internal induced charge; relation requires a signed normal field.
PDF 12/printed sheet 12/slides 23,24: Uniqueness applied to an empty cavity; Concentric conducting shells and potentials.
Slide 23 charged hollow conductor: Outer potential φ0 and unspecified cavity potential; charge-free cavity is assumed.
Slide 24 concentric shells: Outer red sphere is R1 with Q1; inner black sphere is R2 with Q2, so R1>R2. This unconventional indexing is preserved.
PDF 13/printed sheet 13/slides 25: Next topics and historical quiz, lab and problem-set reminders; lower sheet blank.

Findings, conditions and independent derivations

D129-C01 | recap_domain_and_units | lecture4.pdf PDF 1/slides 2 | Recap formulas
The recap is correct in Gaussian electrostatic units under localized-source and finite-energy assumptions.
The infinity reference must exist, E = −∇φ requires conservative electrostatics, and whole-space field energy needs convergence and no unremoved point self-energies.
For a smooth localized density, ∇·(φE)=−E²+4πρφ and the vanishing far boundary term give (1/2)∫ρφ=(1/8π)∫E². Ideal point charges instead have divergent self terms; their finite distinct-pair interaction sum is a different quantity.

D129-S01 | laplacian_calculation_and_operator_types | lecture4.pdf PDF 2,3,8/slides 3,4,5,15 | Laplacian and Poisson derivation
The Cartesian operator, quadratic example and Poisson sign on slides 5 and 15 are correct. A scalar f has a gradient and div grad f; div f and hence grad div f are not defined as ordinary vector calculus operations on a scalar.
Read the Laplacian as the trace of the Hessian, a sum of directional second derivatives; it is not every directional curvature nor generally the geometric curvature of the graph.
For φ=a(x²+y²)/4, ∂xxφ=∂yyφ=a/2 and ∂zzφ=0, hence Δφ=a. In Gaussian units ∇·E=4πρ and E=−∇φ imply Δφ=−4πρ. For a vector F, grad div F is defined and differs generally from the componentwise Laplacian: ΔF=∇(∇·F)−∇×(∇×F).

D129-E01 | harmonic_curvature_false_inference_and_extrema_gap | lecture4.pdf PDF 3,8/slides 6,15 | Interpretation of Laplace equation
The statement that curvature must be zero everywhere is false if it means all directional curvatures or a flat potential. The no-local-maxima-or-minima statement needs the constant-function exception and a maximum-principle argument.
A nonconstant harmonic function on a connected region has no interior local extremum; a constant harmonic function has non-strict extrema everywhere. Zero Laplacian only says the Hessian trace vanishes.
φ=x²−y² is harmonic but has second derivatives +2 and −2 and a saddle at the origin. To justify boundary extrema on a bounded region, apply the second derivative test to φ+ε|r|², whose positive Laplacian prevents an interior maximum, then let ε→0; apply the same argument to −φ for a minimum. The strong local version follows from the harmonic mean-value property. The source does not supply these arguments.

D129-C02 | earnshaw_scope_and_cube_verification | lecture4.pdf PDF 3,4,8/slides 6,7,15 | Stable electrostatic equilibrium and cube example
Earnshaw applies to a freely movable test charge in a source-free neighborhood under fixed static electric forces. The cube example presupposes equal symmetrically arranged corner charges to ensure central equilibrium.
No strict confining minimum of U=qφ exists for either sign of q in that neighborhood. This does not claim to exclude mechanical constraints, time-dependent fields or other forces. A constant potential provides no restoring confinement.
Equal charges at (±a,±a,±a) have cancelling central fields, so E(0)=0. Cubic symmetry makes the central Hessian proportional to the identity; its trace is zero, so the Hessian vanishes entirely. Therefore a second-derivative test alone is inconclusive here. The surrounding harmonic potential is nonconstant, and the maximum principle excludes a local minimum or maximum, verifying the stated lack of trapping without incorrectly claiming a negative quadratic eigenvalue.

D129-E02 | curl_vector_vs_normal_component | lecture4.pdf PDF 5/slides 9 | Curl definition prose
The boxed equation correctly defines (curl F)·n as circulation per area. The following prose incorrectly says the curl vector is normal to the chosen surface A in general.
A chosen infinitesimal loop measures one normal component. Varying the loop orientation determines the vector; the right-hand rule pairs each loop traversal with its normal.
For F=(0,x,y), curl F=(1,0,1). A loop in the xy plane with normal ẑ measures component 1, although the full curl is not normal to that plane. Thus the error is in the prose, not the boxed projection equation.

D129-C03 | stokes_orientation_regular_limit_and_topology | lecture4.pdf PDF 4,5,6,7/slides 8,9,10,11,12,13,14 | Circulation, Stokes theorem and zero curl
Seam cancellation, Stokes theorem and the electrostatic conclusion are correct. The derivation is an infinitesimal argument requiring regularity and a compatible boundary/surface orientation.
Use a C1 vector field near an orientable piecewise smooth spanning surface. Shrinking loops must shrink to a point in a specified plane. Electrostatic conservativity implies zero curl; the reverse implication globally needs a suitable domain or zero circulation around all noncontractible loops.
For the yz rectangle, the four line integrals sum to (∂yFz−∂zFy)ΔyΔz plus smaller-order terms. Cyclic permutations give the three displayed curl components. Since F=qE for a fixed nonzero test charge, conservative force gives zero circulation of E. A cautionary reverse example is E=(−y,x,0)/(x²+y²): curl zero off the z axis but circulation 2π around it, because the spanning disk crosses the excluded singular axis.

D129-E03 | confirmed_curl_area_variable_error | lecture4.pdf PDF 7/slides 13 | Boxed x-component limit
The numerator uses the yz rectangle, but its area denominator is printed ΔxΔy with limits Δx→0 and Δy→0.
The area is ΔyΔz, and the two shrinking side lengths are Δy and Δz. The final component ∂yFz−∂zFy and determinant below are correct.
Dividing the previous slide result Γ=(∂yFz−∂zFy)ΔyΔz+o(ΔyΔz) by ΔyΔz yields the stated x component. A Δx parameter does not belong to this rectangle.

D129-E04 | conductor_definition_omits_ionic_carriers | lecture4.pdf PDF 8/slides 16 | Conductor and insulator definitions
Defining every conductor as a material with free electrons is too narrow and inconsistent with the NaCl solution example on the same slide.
Use mobile charge carriers: electrons in the stated metals, ions in the stated electrolyte. Insulating behavior means negligible charge transport under the relevant conditions, not a universal categorical absence of electrons or all possible mobile carriers.
IUPAC defines electrolyte current through ion movement and ionic conductivity through ionic charge and mobility. The source solution diagram itself labels Na+ and Cl−, while the gold diagram illustrates electronic carriers. Classification is operational and material/condition dependent.

D129-E05 | carrier_drift_sign_error | lecture4.pdf PDF 9/slides 17 | Explanation of equilibration
The prose says charges move from higher to lower potential without restricting their sign. That is wrong for electrons. The adjacent positive/negative drift arrows are correctly opposite.
Positive carriers drift down electric potential under the electric force; negative carriers drift up potential. Both lower their electrostatic potential energy in dissipative relaxation.
F=qE=−q∇φ and U=qφ. Thus for q>0 force points down φ, while for q<0 it points up φ. In the pictured rightward field, φ decreases rightward, positive carriers move right and electrons left, producing the shown cancelling polarization field.

D129-L01 | relaxation_time_model_and_unverified_numeric_range | lecture4.pdf PDF 9/slides 17 | Claimed 10^(-17)–10^(-16) second equilibration time
The source supplies a numerical range with only typical resistivity of metals as justification. No material, permittivity, scale or response model is given, so this is not an established universal settling time.
Distinguish formal local Ohmic charge relaxation from actual whole-object field equilibration. The printed range is not independently verified; do not substitute a different universal number.
For uniform SI conductivity κ and permittivity ε, continuity, J=κE and ∇·E=ρ/ε give ∂tρ=−(κ/ε)ρ and formal τ=ε/κ. MIT Haus–Melcher section 7.7 tabulates copper κ=5.8×10^7 S/m and τ≈1.5×10^(-19) s, outside the lecture range. Their section 15.3 explicitly warns that electron inertia invalidates the simple conductivity model at such metal relaxation scales. Actual transients also depend on geometry and propagation. This is a model/unsupported-range limitation, not a claimed exact alternative measurement.

D129-C04 | electrostatic_conductor_equilibrium_conditions | lecture4.pdf PDF 9/slides 17,18 | Zero field, equipotential and surface charge
These statements are correct in the macroscopic electrostatic equilibrium model. A finite-resistivity conductor carrying steady current can have nonzero internal E. Infinite supply of charge is an idealization of ample mobile carriers, not literal creation of net charge.
Require a connected conducting body in equilibrium without sustained driving current. The conducting material has zero macroscopic net volume density; excess charge resides on its boundaries, including cavity boundaries. Distinct disconnected conductors need not share one potential.
E=0 implies ∇φ=0 along interior paths and ∇·E=4πρ=0 in bulk. At a smooth equilibrium surface tangential E must vanish to avoid carrier drift, so the exterior field is normal and each connected surface is equipotential. Microscopic surface layers are represented as ideal surface charge.

D129-E06 | potential_difference_missing_minus_sign | lecture4.pdf PDF 9/slides 18 | First corollary integral for Δφ
The source prints Δφ=∫_(P1)^P2 E·ds=0. With the established convention Δφ=φ(P2)−φ(P1), the line integral needs a minus sign.
Use Δφ=−∫_(P1)^P2 E·ds. The conclusion zero remains correct because E=0 along the interior path.
The sign follows from E=−∇φ and the fundamental theorem for line integrals; it agrees with the earlier lecture and the recap.

D129-C05 | cavity_shielding_and_total_charge_conditions | lecture4.pdf PDF 10,12/slides 19,20,23 | Hollow-conductor corollaries and first uniqueness application
The empty-cavity result is correct for a closed cavity bounded by one equilibrium conductor. Slide 20 correctly states neutrality at the end of its derivation; its headline requires that condition. Slide 23 silently assumes no cavity charge.
A closed charge-free cavity has constant boundary potential and hence constant interior potential. For a cavity containing charge Q, induced inner charge is −Q. If the isolated conductor initially has total charge Qc, its outer charge is Qc+Q; +Q is the neutral case. Grounding changes the total-charge constraint.
A Gaussian surface wholly inside conducting material encloses Q+Q_inner and has zero flux, yielding Q_inner=−Q. Charge conservation then gives Q_outer=Qc−Q_inner. For the empty cavity, the constant φ=φ0 solves Laplace with its boundary values, and Dirichlet uniqueness fixes it. Open apertures or nonstatic shielding are outside this argument.

D129-C06 | surface_density_signed_normal_convention | lecture4.pdf PDF 11/slides 21 | σ_induced=E_surface/(4π)
The relation is correct only if E_surface denotes the one-sided normal field just outside the conducting material, not a nonnegative magnitude or an arbitrarily assigned surface value.
Let n point from the conductor into the adjacent vacuum, including into a cavity on an inner surface. Then E_vac·n=4πσ because E_cond=0. The ideal surface has two different field limits.
A pillbox gives n·(E_vac−E_cond)=4πσ. At the inner cavity wall around a positive charge, E_vac points into the metal, opposite n, so σ is negative. On the outer positively charged boundary the normal component is positive. The source diagram is consistent once the sign convention is supplied.

D129-E07 | uniqueness_proof_poisson_sign_and_superposition_errors | lecture4.pdf PDF 11/slides 22 | Displayed Poisson equations and superposition sentence
Both Poisson equations in the uniqueness proof print +4πρ; the lecture correctly established −4πρ earlier. The claim that any combination of two same-source solutions is a solution of the same problem is also false.
Write Δφ1=Δφ2=−4πρ. Their difference w=φ2−φ1 solves the homogeneous equation Δw=0 and has zero Dirichlet boundary data.
For aφ1+bφ2, Δ(aφ1+bφ2)=−4π(a+b)ρ, and the common boundary value g becomes (a+b)g. General linear combinations do not retain the original data; coefficients summing to one do. The difference has zero source and boundary data. The sign typo cancels in the subtraction, so the intended uniqueness conclusion survives after correction.

D129-G01 | dirichlet_uniqueness_domain_and_existence_scope | lecture4.pdf PDF 11,12/slides 22,23,24 | Uniqueness theorem statement and proof
The proof establishes at most one solution under appropriate boundary/regularity conditions, not existence for arbitrary data. A bounded domain or adequate infinity condition is needed.
For a bounded connected domain with suitable boundary, let solutions be C2 inside and continuous on the closure, sharing density and Dirichlet data. For exterior problems impose matching behavior at infinity.
For w=φ2−φ1, Δw=0 and w=0 at the boundary. The maximum principle applied to w and −w yields w=0. Independently, Green identity gives ∫|∇w|²=∮w∂n w−∫wΔw=0, so w is constant and the boundary fixes zero. Without infinity data, on r>a both zero and w=1−a/r solve Laplace with zero finite-boundary value at r=a, demonstrating the missing exterior condition.

D129-E08 | concentric_shell_integral_limits_reversed | lecture4.pdf PDF 12/slides 24 | Inner-shell potential difference
The diagram labels the outer radius R1 and inner radius R2, with R1>R2. The source correctly gives both final potentials, but prints φ2−φ1 as −∫_(R2)^(R1) E dr and obtains Q2/R1−Q2/R2, the negative of the required difference.
To compute φ2−φ1, integrate from R1 to R2: −∫_(R1)^(R2) Q2/r² dr = Q2(1/R2−1/R1). Preserve the source indexing; do not swap shell labels.
For r>R1, E=(Q1+Q2)r̂/r² and φ1=(Q1+Q2)/R1. In R2<r<R1, E=Q2 r̂/r². Thus φ2=φ1+Q2(1/R2−1/R1)=Q1/R1+Q2/R2. For r<R2, E=0 and φ=φ2, including r=0. The first displayed difference is inconsistent with the correct final line; the latter is independently verified by superposing shell potentials.

Independent mathematical coverage

- Read all 13 complete extracted texts and personally viewed every full original sheet, including the final blank lower half. Inspected 25 slides and every figure.
- Independently checked Laplacian examples, Poisson signs, harmonic maximum-principle conditions, equal-charge cube symmetry and the limits of a quadratic stability test.
- Checked all four yz-rectangle side integrals, cyclic curl components, seam cancellation, Stokes orientation and the normal-component definition.
- Verified equilibrium conductor/cavity/surface relations, Dirichlet uniqueness with boundary and existence qualifications, and the full concentric-shell piecewise field and potential.
- Primary research checked ionic-carrier terminology and the unsupported numerical equilibration-time range.

Technical disposition

Source review complete. Localized source defects concern harmonic-curvature language, curl direction and area variables, carrier definition and motion sign, a potential-difference sign, Poisson signs and superposition in the uniqueness proof, and the shell integration direction. The main electrostatic results remain valid with the recorded source-free, equilibrium, boundary, regularity and sign conventions.

Limits

- The printed metallic settling-time range is not quantitatively verified. Formal Ohmic relaxation is not a universal physical equilibration time; model limits are explicit.
- The lecture gives an outline of maximum principles and uniqueness, not a complete existence theory. Supplemental proofs here are reviewer derivations.
- Historical course logistics and references to Purcell are transcribed context, not additional packet assets. Direct IUPAC page opens failed; only the cited official indexed definitions were read.

Primary corroboration

Haus and Melcher, Electromagnetic Fields and Energy, section 7.7 | https://web.mit.edu/6.013_book/www/chapter7/7.7.html | Opening Ohmic relaxation derivation and Table 7.7.1, copper row | retrieved 2026-10-08
Primary MIT-hosted textbook, opened. Uniform conductivity/permittivity assumptions and copper formal relaxation estimate; not treated as a measured whole-object equilibration time.

Haus and Melcher, Electromagnetic Fields and Energy, section 15.3 | https://web.mit.edu/6.013_book/www/chapter15/15.3.html | Characteristic Times and Lengths, paragraph before footnote 1 and footnote 1 (HTML lines 123–128) | retrieved 2026-10-08
Primary MIT-hosted textbook, opened and relevant passage read. At metallic charge-relaxation scales electron inertia invalidates the elementary conductivity model.

IUPAC Gold Book, electrolyte | https://goldbook.iupac.org/terms/view/09061 | Definition, first sentence; official indexed plain record | retrieved 2026-10-08
Official primary search extract defines conduction by ion movement. Direct HTML/plain opens failed; no full-page reading is claimed.

IUPAC Gold Book, ionic conductivity | https://goldbook.iupac.org/terms/view/I03175 | Definition λ=|z_B|F u_B | retrieved 2026-10-08
Official primary search result gives ionic species, charge number and mobility; corroborates ionic carrier terminology.

