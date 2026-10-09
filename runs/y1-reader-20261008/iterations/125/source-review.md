# D125 source review — Studio 33

Technical source preparation, 2026-10-08. This does not author a lesson, edit the repository, run SASIS, or close a PROF iteration.

## Scope and independent read record

The complete D125 audit row assigns Chapter 14 in full (PDF pp1–35, including contents), presentation pp1–38, and PRS pp1–12. All 85 pages were independently read as extracted text and opened as individual, full page images freshly rendered from the verified original PDFs. The presentation text extraction has disordered reading order; the full page images resolved it. No contact sheet or predecessor review substitutes for this read. Chapter printed page numbers equal PDF page minus one; all references below use **PDF page numbers**. The per-page ledger, exact paths, render/text hashes, and original assignment are in `source-map.json`.

| Original asset | Pages / bytes | Verified SHA-256 |
|---|---:|---|
| `d29b4747c80d0b106628c1af86541ffa_ch14_inter_diffr.pdf` | 35 / 631040 | `bef63947e163d5695e0fa129a078e581675667a96ba1f57a2584bd02edd452dc` |
| `c33f6ad41b1ee66a506860b1c54b23a5_presentati_w14d2.pdf` | 38 / 1233237 | `eb57f7d71ea210fb2a05912cb54ff40e6b67e9a501a82e8af1a3d41cc33ba75b` |
| `6f50e2162a748f7b45b2f1d898c0c76c_prs_w14d2.pdf` | 12 / 938019 | `63de91bfac617c7b5019af2556dcdf5efb8c029f8c1099a8654bbc669e512e0c` |

Original PDFs and repository remain unchanged. New extractions/renders live only in this review directory. Earlier incomplete working files remain preserved; no cause or timing is inferred. One oversized display attempt returned a truncation message; its potentially unseen chapter pp26–35 and presentation/PRS text were subsequently displayed in smaller calls and read completely. PRS pp7–8 visibly contain hollow-square artifacts after `a`; fractions, sine, equality, RHS, diagram and explanatory prose are legible. Their scientific ambiguity below is separate from the cosmetic artifact.

## Valid supplied model and independent checks

The chapter uses linear, scalar, coherent wave superposition, uniform slit illumination, common polarization and the Fraunhofer approximation. With peak field amplitudes, vacuum intensity is `I = ε₀c E_peak²/2` in W/m². More generally the interference cross term is the time average of the vector dot product, so polarization and coherence matter. For two co-polarized monochromatic waves:

`I = I₁ + I₂ + 2√(I₁I₂)cosφ`, giving equal-source `I/I₀ = cos²(φ/2)`, where `I₀ = 4I_single` is the central maximum. Max/min are `(√I₁ ± √I₂)²`; a zero requires matched amplitudes. These follow directly by squaring and averaging the summed fields; intensity is not the signed field nor its instantaneous value.

For normal in-phase illumination, `δ = r₂−r₁ ≈ d sinθ`, `|φ| = 2π|δ|/λ`. Bright interference orders have `d sinθ=mλ`; dark orders have `(m+1/2)λ`. Exact planar-screen geometry is `y=L tanθ`; `y≈L sinθ` additionally requires small angle. `λ`, `a`, `d`, `L`, `y`, `δ` must use the same length units; phase arguments are dimensionless radians and `λf=c` is for vacuum/approximately air. In a medium use its speed and wavelength.

The aperture integral `∫₋ₐ/₂ᵃ/₂ exp(iky sinθ)dy` gives `I/I₀=(sin u/u)²`, `u=πa sinθ/λ`, with value 1 by continuity at zero and zeros `a sinθ=mλ`, nonzero integer m. Two identical finite slits give `I/I₀=cos²v (sin u/u)²`, `v=πd sinθ/λ`. The general equal-slit array amplitude is proportional to `sin(Nφ/2)/sin(φ/2)` with adjacent-slit phase `φ=2πd sinθ/λ`; principal peaks scale as N² at fixed single-slit illumination, and their phase width scales as 1/N. These derivations independently validate the central equations and qualitative envelope/grating diagrams, subject to the qualifications below.

## Consequential findings and conditions

**F01 — coherence condition overstated (chapter p4, p9; presentation p6).** Monochromaticity is a useful idealization, not a necessary condition for all observable interference. Broadband/white light can interfere within suitable coherence/path ranges; the chapter itself asks about white-light Young fringes on p33. Stable relative phase, spectral averaging, spatial coherence and polarization determine visibility. Conversely, coherence does not make the real cross term nonzero at every point: it vanishes at quadrature, and orthogonal fields do not interfere in total intensity without polarization selection. The introductory p3–4 waveform sum has a constant amplitude 2.79793 and phase 0.529903 rad: its instantaneous zero at x≈2.61169 is not a permanently dark, zero-intensity fringe.

**F02 — signed path label and phase convention (chapter p6 Fig14.2.4; pp9–10; presentation p17).** Fig14.2.4 labels the positive lower-ray excess `r₁−r₂`, opposite to Eq14.2.4 and its own geometry; use `r₂−r₁`. Choosing positive φ as a path-phase magnitude is harmless for cos² intensity, but in `sin(ωt−kr)` a longer path gives a lag, not the positive time-phase advance used in the chapter's illustrative pair. Define the signed phase consistently. Slide17's algebra for `sin(k(x+ΔL))` is correct as spatial algebra.

**F03 — far field and small angle are different restrictions (chapter pp7,13–18,34; slides20–23).** `L≫d≫λ` does not make every diffraction order a small-angle order; require `|m|λ≪d` or `|y|≪L`. Finite-aperture Fraunhofer propagation also requires the omitted aperture quadratic phase to be small, roughly aperture-span²/(λL)≪1 (up to definition-dependent constants), or a suitable lens focal-plane arrangement. A lens is one way to obtain the pattern, not required universally as p13 suggests. The aperture/screen parameters in some worked single-slit examples do not establish a highly accurate far-field limit; their numeric answers are answers within the supplied model. Physical precision without a lens cannot be inferred from large L/a alone.

**F04 — diffraction derivation signs/indexing (chapter p17, Eqs14.6.6,8–10).** With N sampled phasors numbered 1…N, endpoint phase difference is `(N−1)Δβ`, although `NΔβ` correctly spans N cells/width a in the continuum convention. In the last line of Eq14.6.8 the two cosine terms have been reversed while the positive RHS is retained. In Eqs14.6.9–10 the last cosine must contain `ωt+(N−1/2)Δβ`, not a minus. The correctly telescoped sum is
`Σⱼ₌₀ᴺ⁻¹ sin(ωt+jΔβ) = sin[ωt+(N−1)Δβ/2] sin(NΔβ/2)/sin(Δβ/2)`.
The final finite sum and continuum sinc result on p18 are correct.

**F05 — finite sum and phasor limits (chapter pp24–26).** Eq14.10.4 uses `n+1` in the numerator of a sum whose upper limit is N; it must be `N+1`. A finite geometric sum requires no `|a|<1` restriction: `(1−a^(N+1))/(1−a)` holds for a≠1 and the a=1 limit is N+1. The phasor ratio used here has modulus 1. Fig14.10.1 phasors are phase-plane representations of scalar components, not different physical polarization vectors. The resultant amplitude is a magnitude (absolute value of the equal-amplitude cosine expression); an instantaneous value at t=0 is not generally the amplitude. The arc identity `NE₁₀=Rβ` on p26 is a continuum approximation to a polygon; exact finite chords satisfy `E₁₀=2R sin(Δβ/2)`. Agreement with the finite sum is in the small-Δβ limit, not an exact finite-N arc construction.

**F06 — plotted label and grating notation (chapter p15 Fig14.5.2, p22).** Fig14.5.2's vertical label is visibly `sin⁻¹θ` but ticks are `±λ/a`, `±2λ/a`; these are values of sinθ, not arcsinθ. Slide31 uses the correct sine labels. In the grating discussion p22 recalls `β=2πa sinθ/λ`: a is the individual slit width, while the array's adjacent-slit phase is governed by pitch d. Distinguish envelope phase from array phase rather than reusing β indiscriminately.

**F07 — nominal order count is not a general local-maximum count (chapter p20 Eq14.7.3; pp30–32; p35 question14.13.6; slide35).** Eq14.7.3 prints `2(m+1)+1=2m−1`; the intended first expression is `2(m−1)+1`. The latter counts surviving nominal interference orders when d/a=m is an integer and the first envelope zero removes that order. More generally nominal central orders satisfy `|j|<d/a`, giving `2 ceil(d/a)−1`. However, peaks of the complete product generally shift because the envelope has a slope; there can be weak subsidiary peaks beside a missing nominal order. For x=d sinθ/λ and ρ=d/a, stationary nonzero product peaks satisfy `−πtan(πx)+(π/ρ)cot(πx/ρ)−1/x=0`. Explicit numeric checks for14.11.6 below show why the textbook's nine surviving orders must not be called the exact number of local maxima or a measured visibility count.

**F08 — thin-film formula is conditional (presentation pp14–16).** Slide16's `2d=mλ` constructive rule omits refractive index/wavelength definition, angle and reflection phase changes. For a simple lossless film, propagation contribution is `4π n_f d cosθ_f/λ₀`; add the difference of reflection phases. At near-normal incidence the slide rules work with λ in the film and equal reflection phase shifts at the two interfaces. One relative π reflection shift reverses bright/dark conditions. The film/substrate indices are not supplied, so bubbles, oil and coating examples cannot all inherit one unconditional rule. Cancellation also needs matched reflected amplitudes. The photograph establishes iridescence qualitatively; it is not a thickness or refractive-index measurement. Butterfly wings are a qualitative structural-color example, not a fully specified single uniform film.

**F09 — destructive-wave drawings are schematic/inconsistent (presentation pp8,13).** The lower blue curves have visibly different spatial periods from the red curves while being used to illustrate fixed half-cycle cancellation. Equal-frequency waves in one medium must have equal wavelengths for permanent cancellation. The formulas require equal amplitude, common polarization, and π relative phase; the literal drawn spatial profiles cannot substantiate cancellation at all times.

**F10 — scale arithmetic (presentation pp2,23).** Slide2 gives 2 GHz→15 cm and 4.6×10¹⁴ Hz→about652 nm (its654 nm is consistent with approximate inputs). These wavelengths differ by about230,000, not10,000 as slide23 states. Changing d from0.24 m to0.1 mm is a factor2400. With equal L, the quoted wavelengths predict fringe distances about96 times smaller, not10. The qualitative claim that millimetre-scale optical fringes are measurable survives; its arithmetic needs correction.

**F11 — missing demonstration reading (presentation p22).** L≈1.16 m and d≈0.24 m are supplied, but the first-minimum y is explicitly `?`. Hence `λ≈2dy/L`, `f≈cL/(2dy)` are determined expressions, not measured numerical results. Using slide2's λ=0.15 m would predict y≈0.3625 m in its small-angle model; that prediction is not a demo observation, and its angle≈18° is not especially small. Use exact path geometry if precision matters.

**F12 — half-slit proof skips even minima (presentation p30).** Pairing halves with `(a/2)sinθ=(q+1/2)λ` gives odd orders `a sinθ=(2q+1)λ`. The general integer-zero condition is correct, but does not follow from that one displayed pairing alone; divide into 2|m| parts or use the aperture integral for all orders. Endpoint points in the ray sketch are samples of a continuum, not five equally weighted discrete emitters.

**F13 — Babinet qualification (presentation p37).** For complementary aperture transmissions in scalar diffraction, `E_aperture+E_obstacle=E_unobstructed`. Opposite diffracted fields/equal intensities apply away from the unperturbed forward beam, where that field vanishes, or to an appropriately defined scattered contribution. Total fields do not cancel universally; slide37 omits this qualification and conflates complementary transmission with physically stacking opaque screens. A hair is treated as an opaque thin obstruction in this approximation, not as a guaranteed ideal complement at all angles/materials.

**F14 — PRS answer-number mismatch (pp5–6).** A has longer wavelength and therefore lower frequency than B in the same medium. Correct option is **2, A smaller than B**. Page6 prints `(1)` next to that correct prose.

**F15 — PRS single-slit question has two valid zero conditions (pp7–8).** Intended option2, `(a/2)sinθ=λ/2`, is the first minimum and allows half-to-half cancellation. But option3, `(a/2)sinθ=λ`, is `a sinθ=2λ`, also a minimum whenever geometrically accessible (a≥2λ). The question never says “first” or “cancellation of the indicated half-slit pairs”; the printed answer is not unique as written. Option1 gives u=π/2 and nonzero intensity4/π². Cosmetic squares do not remove this ambiguity.

## Independent answers to every chapter exercise

Numeric values were recomputed from the stated inputs, not copied from the key; `recomputations.json` records the numerical checks. All angular results below are within the source's scalar far-field model unless otherwise noted.

| Item | Recomputed result / condition |
|---|---|
| Introductory superposition, pp2–4 | `sin x+2sin(x+π/4)=√(5+2√2)sin(x+0.529903)`; amplitude2.79793. Instantaneous extrema/zeros are not time-averaged fringes. |
| Example14.1, pp7–8 | δ≈2.50 μm, δ/λ≈3.00; approximately third bright order. The stated833 nm and2 cm are rounded, not an exact integer-path equality. |
| Example14.2, pp11–12 | Three-slit amplitude `E₀(1+2cosφ)`; normalized intensity `(1+2cosφ)²/9`. Principal φ=2πm:1; secondary φ=(2m+1)π:1/9; zeros φ=2πm±2π/3. |
| Example14.3, pp15–16 | L≈1.33333 m; central width2.00 mm. These are ideal Fraunhofer answers. |
|14.11.1, pp26–27 | `|m|<d sin45°/λ=452.548…`; m=−452…452, total905. Strict angular endpoints handled. |
|14.11.2, pp27–28 | (a)17.5454 rad; (b)5.02655 rad using small angle; (c)0.0151982°; (d)0.0716197°. |
|14.11.3, pp28–29 Fig14.11.1 | With the pictured signed angles, `d(sinθ₁−sinθ₂)=mλ`. Reversing phase-difference sign merely reverses integer m; θ₂=θ₁ is the undeviated order. |
|14.11.4, p29 | Minimum absolute phase `2acos√.6=1.369438 rad`; path difference108.976 nm at500 nm. Include ± and2π periodic equivalents for all solutions. |
|14.11.5, p30 | Source's explicitly approximate midpoint method gives640 nm. True second secondary maximum has u=7.72525184; exact screen angle within the sinc model gives650.663 nm. The discrepancy is the stated midpoint approximation, not a numerical slip. |
|14.11.6, pp30–32 | Nominal m=0,±1,…,±5 give0°,±10.2866°,±20.9248°,±32.3924°,±45.5847°,±63.2345°. Envelope removes m=±4. Nine surviving nominal orders have ratios1,.810569,.405285,.0900633,.0324228 for m=0,1,2,3,5. Eq14.11.28 omits cos² only because it is evaluating at those nominal orders; it is not the full angular pattern. |
|14.12 conceptual1, p33 | Fringe spacing λL/d: d increased→smaller; λ decreased→smaller; L increased→larger. |
|14.12 conceptual2 | White-light central region overlaps colors; colored side fringes wash out with path difference/spectral averaging, provided suitable spatial coherence. |
|14.12 conceptual3 | Independent car headlights have no stable mutual phase for a resolved time-averaged Young pattern. |
|14.12 conceptual4–5 | Larger a narrows central lobe; smaller a broadens it. At fixed incident irradiance the peak and total transmitted power also decrease with narrowing; normalization to I₀ hides this. For a<λ no first zero exists in the forward hemisphere. |
|14.12 conceptual6 | Add fields, then square/average. Intensities add without cross term only under appropriate incoherence/orthogonality/averaging conditions. |
|14.13.1, p33 | Adjacent bright spacing60.0 μm; third-order displacement180 μm. |
|14.13.2, p33 | d/a=20; nominal central orders−19…19:39. This is the source's nominal-order convention (F07). |
|14.13.3, p34 | Three-slit zeros: `φ=2πn/3`, n not divisible by3; `y≈nλL/(3d)`. Both positive and negative n are needed for the whole screen. Basic unit1.80 mm; successive positive-side gaps alternate1.80 and3.60 mm, not one uniform spacing. Across the central pair the gap is3.60 mm. |
|14.13.4, p34 | Squaring/averaging gives `I₁+I₂+2√(I₁I₂)cosφ`; fields must be mutually coherent and co-polarized for the stated scalar expression. |
|14.13.5, pp34–35 | For u=β/2, `d(sin²u/u²)/du=2sin u(u cos u−sin u)/u³`. Nonzero secondary maxima obey tan u=u. First u4.49340946, second7.72525184, hence β8.98681892 and15.45050367. Midpoint estimates3π/2,5π/2 exceed true u by0.218980 and0.128730. Roots independently bracketed between mπ and(m+1/2)π; no physical experiment implied. |
|14.13.6, p35 | Seven **nominal** central orders imply `3<d/a≤4`. Equality4 needs an extra missing-order/coincidence assumption; the count alone does not uniquely determine d/a. Actual visible/local-maxima counting needs the definition and detection threshold (F07). |

For14.11.6 the **full supplied product** has positive interior local maxima at approximately10.0661°,20.3944°,31.1938°,41.6331°,49.6200°,64.4580°, with ratios .814270,.415270,.100816,.00226505,.00172358,.0334416. Their negative counterparts plus the center give13 interior local maxima, rather than9; extremely weak split peaks straddle the missing nominal fourth order. This follows by bounded maximization in every interval between successive zeros and differentiation of the product, not from a claimed observation. The physical wide-angle accuracy of scalar slit theory and whether weak peaks would be visible are separate limits.

## PRS, demonstrations and experiment representations

| PRS pages | Independent assessment |
|---|---|
|1–2 | Option2: diagram depicts opposite phases at P. Complete zero additionally assumes equal amplitudes and compatible polarization. |
|3–4 | Option1: δ≈d sinθ for far-separated observation point; diagram lower path is longer for positive y. Incident sketch is illustrative; coherent plane-wave premise controls the question. |
|5–6 | Option2; wrong printed answer number, F14. |
|7–8 | Intended option2, also option3 under its accessible second-order condition; F15. |
|9–10 | Option1: coarse envelope zeros depend on a; fine zeros on d. In sinθ coordinate their spacings are λ/a andλ/d. |
|11–12 | Option4, d/a≈8, from fine-zero spacing relative to first envelope zero. Counting eight fine zeros supports approximate ratio; zero count alone does not establish exact equality8. Graph x/y labels have no physical units, so no absolute wavelength/slit measurement follows. |

All presentation titles and figures were read: bullets/waves pp3–5, phase drawings pp8–13, iridescence pp14–16, microwave apparatus/renderings pp9,19,22, Young setup pp20–27, slit ray/curve representations pp29–35, Babinet p37, and Experiment13 p38. The applet and MPEG links are static references here; no animation or demonstration was executed. The classical “bullets” comparison is about a classical particle model, not a denial of quantum particle interference.

Slide38 supplies four tasks, not results or a lab manual: four single slits to estimate λ; a hair to estimate thickness using λ; four double slits to estimate λ; CD track spacing. Model-level deductions are `λ≈a y_m/(mL)` for single-slit zeros, hair thickness `h≈mλL/y_m` in the Babinet approximation, `λ≈d y_j/[(j+1/2)L]` for identified double-slit interference minima, and `d=mλ/sinθ` for normal-incidence grating orders. Use full trigonometry outside small angles; distinguish envelope zeros from interference zeros; for a CD at oblique incidence include the incident-angle term with defined signs. Actual slit widths, screen distances, zero readings, hair properties, incidence geometry, order assignments, spreadsheet and uncertainty data are absent. No measured wavelength, hair thickness, track pitch, wiring, detector calibration or experiment outcome can be recovered from the assigned packet.

## Targeted external checks and remaining limits

Research was confined to these specific uncertain conditions, not a substitute for the complete assigned read:

- [MIT2.717J Statistical Optics](https://ocw.mit.edu/courses/2-717j-optical-engineering-spring-2002/pages/syllabus/statops/), opened the page and read the white-light-interferometry paragraph. Confirms broadband interference exists; no medical-performance claim is adopted here.
- [MIT2.71 Optics2014 Recitation3](https://live.ocw.mit.edu/courses/2-71-optics-spring-2014/821609ddc97b5e4a46e1e5e5c8ba29cc_MIT2_71S14_Rec3.pdf), retrieved text around §4, PDF p4, concerning omitted quadratic aperture phase and lens cancellation. A requested screenshot timed out; this external source is a targeted text check, not a full-image-read claim. The condition in F03 was independently obtained from the omitted phase term.
- [University of Alabama Wave Optics notes](https://pages.physics.ua.edu/faculty/fabi/ph106/classnotes/14waveoptics.pdf), retrieved pp5–7 thin-film reflection-phase and in-film wavelength discussion, and p8 half/quarter-slit cancellation. Supports F08/F12/F15 only; unrelated claims in those notes were not adopted.
- [Hitachi & Takata, Babinet in the Fresnel regime](https://arxiv.org/pdf/0904.1269), read introduction Eq1 and its scalar-theory qualification (PDF p2). Confirms `U₀=U₁+U₂`; the away-from-forward-field deduction in F13 follows directly. The paper's full experiment was not reviewed or reproduced.

Searches also returned sources not relied upon. A University of Virginia page could not be opened (502); the MSU openbook lookup produced no usable targeted text and is not evidence. No broad claims of external full-document reading are made.

Every assigned page is readable and covered. Remaining limitations are missing experimental inputs, unexecuted linked media, the explicit scalar/Fraunhofer/normal-incidence/coherence assumptions, and source question/figure defects identified above. These do not justify silently correcting the originals or treating this review as completed teaching work.
