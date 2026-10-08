D145 source technical review

Wave Equation Electromagnetic Radiation

MIT 8.022 Fall 2004. Official indexed session 25; published PDF title Lecture 20; linked file lecture20.pdf. Identities retained separately. One original PDF, 11 full sheets. Every complete page text and original full-page render personally inspected; SHA256 independently recomputed against audit. PDF skill previously read and applied read-only.

Scope: source evidence only. No teaching, PROF/SASIS judgment or iteration closure.

Source: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/d5c891405a068cfb6f4e493cae793000_lecture20.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture20/
Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D145/source.pdf
SHA256: 039e3459414a7703aff514474607e2983de73b9161d24728ce954bc3e43f6057
Mapping evidence: {'audit': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-audit/8022.json', 'queue': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/queue.json', 'selection': '/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/readability-selection.json', 'index_url': 'https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/pages/lecture-notes/', 'queue_order': 145, 'active_order': 74, 'queue_selection_evidence': 'Official index labels this row SES # 25: Wave Equation\n\n\nElectromagnetic Radiation.'}

Page, slide and visual coverage

lecture20.pdf, PDF 1, printed sheet 1, slides 1,2: Title Lecture20; Maxwell/displacement and wave recap.
lecture20.pdf, PDF 2, printed sheet 2, slides 3,4: Fourier and plane-wave ansatz; Phase and dispersion relation.
lecture20.pdf, PDF 3, printed sheet 3, slides 5,6: Wavelength/period; Electric transversality.
Slide 5 — two sinusoid graphs: Spatial wavelength and temporal period arrows; vertical axes marked magnitude despite negative graph lobes.
lecture20.pdf, PDF 4, printed sheet 4, slides 7,8: Magnetic transversality; Cosine-wave curl calculation.
Slide 7 — orthogonal triad: E up, k right, B oblique; right-handed relation checked.
lecture20.pdf, PDF 5, printed sheet 5, slides 9,10: Equal Gaussian amplitudes and orientation; Linear polarization.
Slide 9 — repeated field triad: E/B/k relationship and cross-product direction.
Slide 10 — spatial wave rendering: Electric and magnetic sinusoidal fields in perpendicular planes with common phase.
lecture20.pdf, PDF 6, printed sheet 6, slides 11,12: Dipole transmitting/receiving; DemoK1 microwave antenna.
Slide 11 — antenna charge stages and reception sketch: Three driven dipole states; wave to receiving conductor and parallel/perpendicular response.
Slide 12 — instrument diagram: Horn source, field triad, vertical wire antenna, differential amplifier and scope.
lecture20.pdf, PDF 7, printed sheet 7, slides 13,14: Dichroic polarizer model; Projection on transmission axis.
lecture20.pdf, PDF 8, printed sheet 8, slides 15,16: Claimed random-light sum; Three-polarizer demoT1.
Slide 16 — three polarizer sequence: Unpolarized source passes x-axis P1, intermediate45degree P3 and crossed P2; order matters.
lecture20.pdf, PDF 9, printed sheet 9, slides 17,18: Wire-grid microwave demoK3; Circular field pair.
Slide 17 — microwave-grid apparatus: Horn transmitter, conducting comb, receiver and two scope inputs; conducting direction versus E checked.
Slide 18 — rotating field rendering: Both vector tips rotate while E/B stay perpendicular; formulas inspected at z0.
lecture20.pdf, PDF 10, printed sheet 10, slides 19,20: Rotating dipole/crossed antennas; Two polarization basis states and classification.
Slide 19 — dipole and antenna drawings: Opposite charges/arrow and orthogonal driven antenna pair; amplitude, phase and viewing-direction assumptions recorded.
Slide 20 — two basis-wave drawings: Two perpendicular linear-polarization bases with E/B exchanged; classification bullets compared with formulas.
lecture20.pdf, PDF 11, printed sheet 11, slides 21,22: Summary; Historical subject-evaluation slide.

Recovered complete text provenance

/workspace/scratch/ac36b9c5ff31/prof-readability/sourceprep-d140-d147/D145/text-recovery-provenance.json
{'original_pdf': '/workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D145/source.pdf', 'original_pdf_sha256': '039e3459414a7703aff514474607e2983de73b9161d24728ce954bc3e43f6057', 'old_cached_text': '/workspace/scratch/ac36b9c5ff31/prof-readability/audit-8022/D145/text.txt', 'old_bytes': 0, 'recovered_text': '/workspace/scratch/ac36b9c5ff31/prof-readability/sourceprep-d140-d147/D145/recovered-complete-text.txt', 'recovered_bytes': 13446, 'recovered_sha256': '2e02b875e85591cb52f079b6758b22ff93da1bd734daf71a2b7715d82716c8bd', 'method': 'PyMuPDF: doc=fitz.open(original_pdf); texts=[page.get_text() for page in doc]; join PAGE n headings and page text with two newlines; UTF-8 write into owned scratch', 'pymupdf_version': '1.26.6', 'recovered_text_chars_per_page': [723, 969, 1528, 1342, 1304, 895, 1568, 1319, 1127, 793, 1062], 'page_count': 11, 'limitation': 'Current empty text cache observed. Original audit records nonzero per-page counts; no evidence here determines historical timing/cause or prior reading. Original cache untouched.'}
Future source reading must use the recovered complete_text_path above; the original audited text cache remains empty and untouched. All recovered page text personally read; character counts exactly match original audit.

Findings, conditions and independent derivations

D145-C01 | fourier_and_generality_conditions | lecture20.pdf, PDF 1,2, slides 2,3,4 | Fourier theorem and most-general plane waves
The fixed real-vector single-sinusoid expressions describe monochromatic linear polarization, not the most general wave or polarization. Any periodic function as stated needs a function class and convergence sense.
For square-integrable periodic fields, Fourier expansion is an L2 statement; pointwise convergence requires additional hypotheses and jumps converge to the side-limit mean under usual piecewise-smooth conditions. A general monochromatic plane wave uses complex transverse amplitude, allowing two components with relative phase.
Use E=Re[Ec exp(i(k dot r-omega t))], k dot Ec=0, and Bc=k-hat cross Ec in Gaussian vacuum. Pulses require a frequency superposition/integral. The source later supplies the missing second polarization and phase explicitly; its early restricted ansatz should not be promoted to a general theorem.

D145-C02 | three_dimensional_argument_and_dispersion | lecture20.pdf, PDF 2, slides 4 | f(x plus/minus ct) to vector-argument expression
The displayed vector argument f(r plus/minus c k-hat t) is insufficiently specified to imply an arbitrary3D function solves the3D wave equation. The phase manipulation is correct for a plane-wave profile.
Use scalar profile F(k-hat dot r minus ct), or a Fourier phase k dot r-omega t with omega=c|k|>0. Arbitrary transverse dependence requires extra conditions.
Laplacian F=|k-hat|^2 F-double-prime=F-double-prime and F_tt=c^2 F-double-prime. By contrast f(x-ct,y,z) leaves residual f_yy+f_zz in the wave equation. Substituting a sinusoid gives -k^2 E=-omega^2 E/c^2, hence omega=c|k| for positive frequency; lambda=2pi/|k| and nu=omega/(2pi) imply lambda nu=c.

D145-E01 | time_slice_sign_and_magnitude_axis | lecture20.pdf, PDF 3, slides 5 | At x=0 temporal formula and two plots
Starting from E=E0 sin(kx-omega t), the x0 slice is -E0 sin(omega t), whereas the slide prints plus. Both plotted axes say |E| but show negative lobes.
Retain -sin for the same wave and phase; plus can represent a redefined phase/sign only if stated. Relabel sinusoid vertical axes as signed field component, or plot a nonnegative absolute value. Wavelength and period statements remain correct.
sin(-omega t)=-sin(omega t). A vector norm cannot be negative and |sin| has period pi in its argument, unlike the signed component period2pi used in the slide. The source relations omega=2pi/T=2pi nu, omega=ck and lambda nu=c are correct for its vacuum monochromatic model.

D145-S01 | maxwell_constraints_and_polarization_scope | lecture20.pdf, PDF 3,4,5,11, slides 6,7,8,9,10,21 | Transversality, handedness and equal amplitudes
The final constraints are correct for a single traveling vacuum plane wave. The source explicitly recognizes that the second-order wave equation alone is insufficient. Its intermediate argument that a time derivative does not change B direction assumes the initial fixed-axis linear-polarization ansatz.
For nonzero monochromatic k, k dot E0=k dot B0=0; Faraday gives B0=k-hat cross E0 and Ampere gives E0=-k-hat cross B0. This proves equal Gaussian amplitudes and E cross B=E^2 k-hat pointwise for one traveling wave, including general polarization.
For cosine phase psi, curl B=-(k cross B0)sin psi and E_t=omega E0 sin psi, yielding the stated relation. The switch from earlier sine to cosine is a harmless common phase choice, not a derivative error. Rotating circular E/B have changing directions, so the same-direction derivative shortcut cannot be used for them. Superposed waves in different directions, standing waves, static/near fields and material media do not obey the same blanket equal-amplitude/perpendicularity claims. In SI a vacuum plane wave has E=cB, not E=B.

D145-E02 | curl_product_rule_missing_scalar_factor | lecture20.pdf, PDF 4, slides 8 | Blue vector product identity
The printed mnemonic omits s in its first term: curl(v s)=curl v+grad s cross v. The detailed expansion below correctly multiplies curl B0 by cos phase.
Correct identity: curl(s v)=s curl v+grad s cross v. Since constant B0 has curl0, this local mnemonic error does not spoil the worked result.
In index notation epsilon_ijk partial_j(s v_k)=s epsilon_ijk partial_j v_k+epsilon_ijk(partial_j s)v_k. Dimensions and even constant s=2 disprove the unmultiplied first term for a nonconstant vector field.

D145-C03 | antenna_and_polarizer_idealization | lecture20.pdf, PDF 6,7,9, slides 11,12,13,17 | Reception orientation and absorbing/transmitting axes
The source correctly distinguishes the conducting/absorbing direction from the perpendicular preferred transmission direction. Zero perpendicular antenna reception and total blocking are idealizations; the source gives no finite-geometry/calibration model.
For an ideal straight electric dipole receiver, induced voltage is proportional to E dot effective-length-vector, yielding a cosine amplitude and cosine-squared power dependence. The grid blocks E along its conducting teeth, while the perpendicular component passes ideally. Actual loss, leakage, reflection and bandwidth are unspecified.
Projection onto a thin conductor axis explains the orientation dependence without requiring the literal absence of room as a complete microscopic proof. At the stated10.5GHz, c/nu is approximately0.02855m using2.998e8m/s. No apparatus output or material transmission coefficients were measured; the historicalK1/K3 descriptions are not converted into empirical certifications.

D145-E03 | polarizer_projection_magnitude_bars | lecture20.pdf, PDF 7, slides 14 | Scalar and vector transmitted-field equations
The source first equates a field magnitude to signed E dot p-hat, then places absolute-value bars around that projection in the vector formula. Those bars would rectify the optical oscillation.
The linear ideal projection is Eout=(E dot p-hat)p-hat; its magnitude is |E dot p-hat|. The nonnegative peak amplitude is E0|cos theta| and intensity ratio is cos^2 theta. The polarization axis is p-hat modulo180degrees.
For E=E0 x-hat cos psi and p-hat=x-hat cos theta+y-hat sin theta, Eout=E0 cos theta cos psi p-hat. When cos psi changes sign, the vector must reverse, not remain in the positive p direction. Squaring and cycle averaging gives Malus law; the lost orthogonal component is removed by the polarizer, not converted losslessly into the transmitted axis.

D145-E04 | coherent_sum_does_not_model_unpolarized_light | lecture20.pdf, PDF 8, slides 15 | All components share cos(kz-omega t)
As written with fixed theta_i, the sum has exactly one common temporal phase and is a single fixed vector times cos psi; it is linearly polarized, or identically zero, rather than unpolarized. Random orientations alone do not supply temporal incoherence.
A statistical unpolarized model requires appropriate random phases/time-varying independent transverse components and equal average transverse intensities with zero mutual coherence. The statement that a perfect polarizer produces linearly polarized output remains valid.
Factor the source sum: E=E0[(sum cos theta_i)x-hat+(sum sin theta_i)y-hat]cos psi. Its direction is constant. In a proper transverse isotropic incoherent ensemble, average |E dot p|^2 is half average |E|^2, so ideal transmitted intensity is Iin/2. This half-intensity supplement requires averaging; it cannot be derived by coherently summing equal-phase amplitudes as printed. Bulb/sunlight wording is an approximate source model; scattered/reflected sunlight may be partially polarized.

D145-S02 | crossed_and_intermediate_polarizers | lecture20.pdf, PDF 8, slides 16 | DemoT1 amplitudes and intensities
For input already polarized along the first axis, the stated two45degree amplitude factors give Eafter=EafterP1/2, so intensity after the last two sheets is one quarter of that after P1. This does not equal half the intensity.
For ideal unpolarized incident intensity I0, P1 gives I0/2, the intermediate45degree polarizer gives I0/4, and the final90degree polarizer gives I0/8. Without the middle sheet ideal crossed transmission is zero.
Projection operators P_y P_x=0, but P_y P_45 P_x maps x-hat to y-hat/2. More generally inserting angle theta gives transmission relative to afterP1 cos^2 theta sin^2 theta=(1/4)sin^2(2theta), maximal at45degrees. The source labels E0 as an amplitude at this stage; an unpolarized input cannot be assigned its single deterministic vector amplitude.

D145-S03 | circular_pair_and_generation_conditions | lecture20.pdf, PDF 9,10, slides 18,19 | Circular formulas and crossed-source examples
The circular pair on slide18 is mathematically consistent: E=E0(x-hat sin psi+y-hat cos psi), B=E0(y-hat sin psi-x-hat cos psi) for positive z propagation. Circular emission from a rotating dipole or crossed antennas requires observation direction and equal transverse amplitudes in addition to quadrature.
At fixed z the vector tips trace circles with angular frequency omega, |E|=|B|=E0 and B=z-hat cross E. Orthogonal equal-amplitude fields90degrees out of phase make a circle; unequal observed amplitudes make an ellipse.
At z0 E=E0(-x-hat sin omega t+y-hat cos omega t), matching source signs. For a dipole rotating in xy, the far-field transverse projection viewed along its rotation axis preserves equal quadrature components. Viewed in the dipole plane, projection can be linear, and general oblique directions give ellipses. Handedness labels require a viewing convention, absent here. A photography filter is a manufactured example, not itself evidence for the source statement about occurrence in nature; this review makes no empirical correction or priority claim.

D145-E05 | quadrature_mislabeled_linear_and_phase_cases_missing | lecture20.pdf, PDF 10, slides 20 | Two phase-classification bullets
The source labels phi1=phi2+90degrees as linear polarization. For its equal nonzero amplitudes, that case is circular. The remaining phase cases also need modulo and amplitude qualifications.
Linear occurs for relative phase delta=0 or pi modulo2pi, or when one amplitude vanishes. Circular requires equal nonzero amplitudes and delta=plus/minus pi/2 modulo2pi. Other nondegenerate cases are elliptical.
For normalized components X=Ex/A=cos u, Y=Ey/B=cos(u+delta), eliminate u to obtain X^2+Y^2-2XY cos delta=sin^2 delta. At delta0/pi this degenerates to a line; at quadrature X^2+Y^2=1, an ellipse generally and a circle whenA=B. The source basis gives two transverse complex degrees of freedom for fixed nonzero k, with B determined, rather than independently selectable E/B directions.

D145-N01 | historical_slide_scope | lecture20.pdf, PDF 11, slides 22 | Subject evaluation instructions
The final complete slide contains2004 subject-evaluation logistics, staff/tutor names and a radio-station demonstration teaser. These are historical source content, not instructions to this preparer or a new external action.
Preserve them in coverage; no forms, messages, signal interference, demonstrations or evaluation actions were performed.
The substantive mathematical packet ends with its summary on slide21; reading slide22 completes the actual linked original PDF without inferring an extra required source from its teaser.

Independent coverage

- Read recovered complete text for all11pages and personally viewed all11original full-page renders/22slides; all recovered per-page text counts exactly equal originalaudit.
- Checked every wave/curl/projection equation, waveform graph, antenna/circuit-like apparatus, polarization triad and three-polarizer order.
- Independently derived dispersion, both transverse constraints, correct vector product rule, signed projection/Malus law, incoherent half-intensity and three-sheet one-eighth transmission.
- Derived polarization ellipse equation, checked circular signs atz0 and supplied source-generation viewing/amplitude conditions.

Technical disposition

Source review complete. Correct plane-wave Maxwell constraints coexist with local time-sign/axis/product-rule/projection notation errors. The claimed unpolarized common-phase sum is not unpolarized, and the quadrature classification is incorrect. The empty current text cache is repaired only by an independently verified scratch extraction; future reading is explicitly directed to that complete replacement.

Limits

- Original audited text.txt currently0bytes; exact replacement path/hash and matching counts are embedded. No cause/timing or historical-read inference is made, and original cache remains untouched.
- No microwave, optical or radio demonstration was performed; reported apparatus frequencies and qualitative effects retain their historical/model scope.
- Real polarizer extinction/transmission, antenna effective length, observation geometry and material microscopic response are not numerically specified.
- The source gives no explicit circular-handedness convention or complete stochastic model for unpolarized light; supplementary derivations are labeled as reviewer checks.
