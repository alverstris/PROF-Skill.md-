D128 source technical review

Energy Density of the Field Electric Potential Gradient Gauss’s Law Revisited Divergence

MIT 8.022 Fall 2004, lecture 3. One original PDF, 12 full sheet pages, usually two slides per sheet. Every complete extracted text and original full-page image inspected; raster-only text recovered visually where noted. SHA256 independently recomputed and matches audit. PDF skill previously read and applied in read-only mode.

Scope: source evidence only; no teaching authoring, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/9b5b6faf40963626e33a59428df627ad_lecture3.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture3/
Local original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D128/source.pdf
SHA256: aaa4606ed1202a67e25e5350ef47823c79e7a5d5fec00deeadfd481b37ae9465
Mapping: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 128, 'active_order': 57}

Page, slide and visual coverage

PDF 1/printed sheet 1/slides 1,2: Lecture 3 title; interaction energy, field and integral Gauss recap.
PDF 2/printed sheet 2/slides 3,4: Solid-angle proof of Gauss law; Spherical shell field and demonstration questions.
Slide 3 solid-angle geometry: Point charge Q, small concentric sphere S1, generic boundary S, cone dΩ, distance R and outward normal at angle θ.
Slide 4 charged spherical shell: Positive surface charges and outward radial arrows; formula zero inside and Q/r² outside.
PDF 3/printed sheet 3/slides 5,6: Cylindrical shell induction demonstration; Compression of a spherical charge shell; pressure and work.
Slide 5 open finite cylinder: Positive lateral surface, E>0 outside and E=0 label in the hollow; this picture requires qualification.
Slide 6 shell compression: Concentric radii r and r−dr; inward work arrows; symmetry preserves exterior field at fixed Q.
PDF 4/printed sheet 4/slides 7,8: Electric field energy density and whole-space energy; Potential difference from external work and units.
Slide 8 radial work geometry: Source Q at origin, test charge q on r1, inward path to r2; work signs verified.
PDF 5/printed sheet 5/slides 9,10: Infinity-reference potential and point charge; Potential sums and volume, surface, line integrals.
PDF 6/printed sheet 6/slides 11,12: Potential reference and distinction from interaction energy; Energy as half charge times potential and field integral.
PDF 7/printed sheet 7/slides 13,14: E equals minus gradient of potential; One- and two-dimensional gradients.
PDF 8/printed sheet 8/slides 15,16: Gradient of sin(x)sin(y); uphill/downhill; Equipotential contours and perpendicular field.
Slide 15 surface and vector plots: Sinusoidal scalar surface and planar gradient arrows; peaks, minima and zero vectors agree with derivatives.
Slide 16 surface and contour plots: Same sinusoidal surface with closed contours about extrema and crossing zero-level geometry near saddles; regular-level qualification applies.
PDF 9/printed sheet 9/slides 17,18: Flux additivity across a partition; Divergence as local flux density and divergence theorem.
Slide 17 split volume diagram: Region split into two volumes; common interface has opposite outward normals. Printed last algebra line has a sign error.
PDF 10/printed sheet 10/slides 19,20: Differential Gauss law; Cartesian component flux of a shrinking box.
Slide 20 coordinate box: Box centered at P(x,y,z), side lengths Δx, Δy, Δz; opposite z-face contribution and cyclic analogues.
PDF 11/printed sheet 11/slides 21,22: Cartesian divergence formula; Recover uniform-sphere charge from a piecewise radial field.
PDF 12/printed sheet 12/slides 23: Next lecture agenda; lower sheet region blank.

Findings, conditions and independent derivations

D128-C01 | solid_angle_proof_conditions | lecture3.pdf PDF 2/slides 3 | General boundary Gauss proof
The local cancellation dΦ = q dΩ is correct for a transverse surface patch. The drawn single-intersection cone does not by itself cover every nonconvex closed boundary.
Use signed solid angle with outward orientation, accounting for all intersections; point charges must lie off the boundary. The inverse-square comment applies to isotropic point-charge fields in three spatial dimensions.
dΩ = (r̂·n̂)dA/R², so dΦ = q dΩ. Its oriented total is 4π for an enclosed point and zero for an exterior point. For E = C r^(-p) r̂, spherical flux is 4πC r^(2−p), independent of radius precisely when p=2. Tangencies can be handled by limits; superposition supplies many charges.

D128-C02 | cylinder_geometry_missing_assumptions | lecture3.pdf PDF 2,3/slides 4,5 | Shell demonstrations
The spherical-shell formula is valid for a uniform shell or isolated equilibrium spherical conductor. The finite open cylinder pictured on slide 5 does not have exactly zero cavity field merely by Gauss law.
Exact zero in a hollow cylinder follows for an infinitely long, uniformly charged cylindrical shell by symmetry, or in a closed conductor cavity without internal charges in electrostatic equilibrium. A finite open conductor may have small deep-interior field, but end penetration prevents an automatic exact conclusion.
For a finite uniform lateral cylinder of radius a and length L, the on-axis field is E_z = 2πaσ{[a²+(z−L/2)²]^(-1/2) − [a²+(z+L/2)²]^(-1/2)}. It vanishes at z=0 by reflection but is nonzero at generic interior z. This explicit counterexample shows the missing geometry condition; an actual conductive open cylinder has nonuniform charge and needs a separate boundary solution. The unprovided classroom demonstration cannot supply quantitative verification.

D128-S01 | independent_shell_pressure_and_energy | lecture3.pdf PDF 3,4/slides 6,7 | Compression argument
The pressure and infinitesimal work formulas are correct when Q is fixed and compression is quasistatic. The surface force uses the field of other charges, not the discontinuous full field evaluated arbitrarily on the sheet.
Use E_other = (E_out + E_in)/2 = 2πσ and pressure p = σE_other = 2πσ² = E_out²/(8π). Here dr denotes the positive amount of radius decrease.
The shell has U(r) = ∫_r^∞ (Q²/s⁴)/(8π)·4πs² ds = Q²/(2r). Thus U(r−dr)−U(r) = Q²dr/(2r²)+O(dr²), equal to p·4πr²dr. For fixed Q the exterior field is unchanged; only the newly exposed thin layer acquires field. Spherical symmetry makes the energy-location argument valid for this example.

D128-C03 | field_energy_domain_self_energy_boundary | lecture3.pdf PDF 1,4,6/slides 2,7,11,12 | Interaction energy to field energy
The whole-space field energy and continuum expression are correct for suitable localized continuous charges. They cannot be directly equated to the finite pair interaction sum of ideal point charges without removing divergent self-energies. The stated φ(∞)=0 is a useful reference but is not by itself every convergence condition.
Require sufficient regularity and decay to make the integrals finite and the boundary term vanish. For point charges retain distinct-pair interaction energy or explicitly regularize/subtract self-energy.
From ∇·(φE) = −E² + 4πρφ, (1/2)∫_V ρφ dV = (1/8π)∫_V E² dV + (1/8π)∮_∂V φE·n dA. Localized charges have φ=O(1/r), E=O(1/r²), so the far boundary term tends to zero. A point-charge self term diverges as q²/(2a) with cutoff a. In |ΣE_i|² the cross terms yield finite pair energies while individual square terms are self energies. This resolves positive total field energy versus possibly negative pair energy.

D128-E01 | confirmed_voltage_unit_error | lecture3.pdf PDF 4/slides 8 | Units at bottom of potential-difference slide
The source states SI Volt = N/C. That is an electric-field unit, not a potential unit.
Volt = J/C = N·m/C. The listed statvolt = erg/esu and approximately 3×10² volts are correct.
Potential is work/charge and E = −∇φ, so [φ]=[E]·length. Using 1 erg = 10^(-7) J and 1 statC ≈ 3.33564×10^(-10) C gives 1 statV ≈ 299.792458 V.

D128-C04 | potential_reference_and_kernel_conditions | lecture3.pdf PDF 4,5,6/slides 8,9,10,11 | Potential definitions and superposition
The signs and point-charge formulas are correct. Scalar potential is defined up to a constant; a reference fixes its representative. Work language on slide 11 omits per unit test charge. A line of charges prevents an infinity reference only for nonlocalized cases such as an infinite uniform line, not every finite line.
Use electrostatic conservative fields, nonperturbing test charge and quasistatic external work. In continuum kernels write the separation |r−r′| explicitly rather than ambiguous r. Require convergent integrals and exclude field points on singular ideal line/point sources unless regularized.
φ(r) = ∫ρ(r′)/|r−r′| d³r′ and E = −∇φ. For one charge, −∫_∞^r q/s² ds = q/r and φ2−φ1 = q(1/r2−1/r1). For an infinite line, E_s = 2λ/s and φ(s)−φ(s0) = −2λ ln(s/s0), so φ(∞)=0 is unavailable. A finite charged segment has a convergent infinity-referenced potential away from the segment.

D128-N01 | minor_energy_sum_index_defect | lecture3.pdf PDF 6/slides 12 | Last discrete sum before continuum limit
The rewritten last expression retains j≠i under a sum over j although i is no longer a free index after defining φ(r_j).
Write U = (1/2)Σ_j q_j φ_except_j(r_j). The exclusion belongs inside the definition φ_except_j = Σ_(i≠j) q_i/r_ij.
Substituting that definition gives exactly (1/2)Σ_jΣ_(i≠j) q_iq_j/r_ij, counting each unordered pair once. This is a notation defect, not a different physical answer.

D128-C05 | gradient_direction_and_regular_levels | lecture3.pdf PDF 7,8/slides 13,14,15,16 | Gradient and equipotential interpretation
The Cartesian gradient formulas and sin(x)sin(y) derivatives are correct. Deepest slope is imprecise; the gradient points in steepest ascent. Always uphill and always perpendicular need a nonzero gradient and a regular level set.
For a differentiable scalar field and unit direction u, D_uφ=∇φ·u, maximal at u=∇φ/|∇φ| when ∇φ≠0. At a critical point there is no gradient direction, and the level set may not be a smooth curve.
For φ=sin x sin y, ∇φ=(cos x sin y, sin x cos y), E=−∇φ and Δφ=−2φ. At (0,0), ∇φ=0 and the zero contour crosses, so the regular-level qualification is substantive. Along a regular contour r(t), 0=dφ/dt=∇φ·r′, proving perpendicularity; the plots agree with this geometry.

D128-E02 | confirmed_flux_partition_sign_typo | lecture3.pdf PDF 9/slides 17 | Last displayed equality in partition derivation
The last line prints ∮_S1 E·dA − ∮_S2 E·dA = Φ1+Φ2. The second surface integral must have a plus sign.
The common interface cancels because the two subvolume outward normals oppose one another; both outer-subvolume fluxes add.
Let I1 and I2 be interface fluxes with their respective outward normals. I1+I2=0. Then Φ(S) = [Φ(S1)−I1]+[Φ(S2)−I2] = Φ(S1)+Φ(S2). The source diagram and subsequent divergence theorem use this correct addition.

D128-C06 | divergence_theorem_regular_limit_conditions | lecture3.pdf PDF 9,10,11/slides 18,19,20,21 | Shrinking-volume divergence and local Gauss law
The theorem and Cartesian formula are correct for C1 fields on suitable regions. V→0 must mean volumes shrink to the point, not merely lose volume while remaining extended. Finite-box equalities in the infinitesimal argument represent leading-order limits. Surface V on slide 19 should read volume V.
Use piecewise smooth outward boundaries and smooth fields; where charges or field derivatives are singular, use weak/distributional formulations or excision. Arbitrary-volume integral zero implies pointwise zero for a continuous integrand, or almost-everywhere zero with weaker hypotheses.
Taylor expansion gives z-face flux = ∂_zF_z ΔxΔyΔz + o(ΔV) for shrinking boxes; summing yields ∇·F = ∂_xF_x+∂_yF_y+∂_zF_z. Interior interface cancellation yields the volume integral. If continuous g=∇·E−4πρ were nonzero at a point, a small ball where it retains sign would have nonzero integral, contradicting the arbitrary-volume statement.

D128-S02 | uniform_sphere_inverse_problem_verified | lecture3.pdf PDF 11/slides 22 | Recovering charge density from given field
The displayed result is correct: constant K inside radius R and zero outside. The interface must also be checked so a hidden surface charge is not missed.
Inside, E=(4πK/3)(x,y,z). Outside, E=(4πKR³/3)r/r³. Both normal limits at R equal 4πKR/3, hence no surface delta charge.
Interior divergence is 3·4πK/3=4πK. Exterior divergence of r/r³ is zero away from the origin, which is outside that branch. The global continuous field has density K·1_(r<R), total charge 4πKR³/3, no point charge at the origin and no surface charge at R. The value of the volume density exactly at the sharp interface is immaterial to its distribution.

Independent mathematical coverage

- Read the entire 12-page extracted text and personally viewed every original full-sheet image; covered 23 slides and the blank lower half of the final sheet.
- Checked the solid-angle argument, shell pressure/work/field energy, potential kernels and reference choices, gradient example and all field/contour diagrams.
- Derived the field-energy boundary term and point self-energy distinction; checked the flux partition, Cartesian divergence limit and sphere inverse problem including interface charge.

Technical disposition

Source review complete. Confirmed errors are the voltage unit and one flux-additivity sign; one discrete-sum index is malformed. The open-cylinder claim needs essential geometry/equilibrium conditions. Energy, potential and vector-calculus results are supported under the stated convergence, symmetry and regularity assumptions.

Limits

- Classroom apparatus demonstrations D7/D8/D24/D26/D29 and proposed board explanations are not included assets; no unprovided observation or experimental accuracy is asserted.
- The source illustrates a general energy-density law using one shell compression. The general electrostatic identity is supplied here as an independent derivation, not claimed as a source proof.
