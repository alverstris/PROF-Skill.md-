# Original SASIS report — D008-r35

Status: provisional pending the coordinator's comparison of the actual launcher route, original view-tool objects, preserved image-URL bytes and displayed extents. This report is the original reader report, written after complete reading and before any author feedback. It evaluates the frozen document, not a student's ability, retention or score.

## Finding

The supplied baseline and frozen teaching support the consequential calculations and all six existing exercise demands. I found no established missing connection that blocks a worked result or exercise conclusion. The teaching distinguishes polynomial identities from approximations, derivative matching from a finite-interval fit, local error from a numerical bound, a next term from an entire remainder, and a supplied physical law from its mathematical expansion.

One scope ambiguity remains in §8's sentence, “No approximation order makes a local model uniformly reliable over an unlimited interval.” Read as saying that degree alone gives no general global guarantee, it is supported. Read as an unrestricted impossibility, it conflicts with §5's explicit exact-quadratic case: its matched degree-two polynomial has zero error on the full real domain. The natural question is whether §8 means “does not by itself guarantee” or “can never.” The earlier exactness explanation preserves the correct understanding, and no dependent calculation is blocked. This is a wording/generalisation concern, not a finding that the local formulas are invalid.

## Admitted inputs and limits

Exactly two subject-content artifacts were admitted:

1. OCR-A-4-subjects-r1, revision 20261007-frozen: the complete operational Mathematics H240, Further Mathematics H245 Pure Core Y540/Y541 plus Statistics Y542 and Mechanics Y543, Physics H556 and Chemistry H432 packet. 247840 bytes; SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`.
2. D008-complete-r35, revision whole-freeze-4d758921: complete main lesson, grouped hints, complete solutions and four figures. 248908 bytes altogether.

Teaching identities supplied in routing metadata:

| File ID | Bytes | SHA256 |
|---|---:|---|
| main | 23965 | c6208e042063e806a2d0709bc9974994504280c40f5efb592598158ae4ef2938 |
| fig1 | 50373 | f0fbfb25b9bdc5a1b4a737a2b4c1f13e6da98fb237f6f26e76c32a2656dc3d97 |
| fig2 | 58561 | f0994b23abda13ba561f589bb156277f96a9ffcc681b3d8c0214e9c87d833928 |
| fig3 | 62506 | ad60cddb0fa8e7b8b6a8330e2d8162bcc5d4c69037f48bce6ee5aef571dccd94 |
| fig4 | 43506 | 5f154706d4163f6eacfb64ea5ca1498dcb0d179c96b96874f3cf286855b3d8be |
| hints | 2818 | 1f249ea34d4879407cbc91ce4e30e564607ddc9d845fb0160616e3cd04cb647d |
| solutions | 7179 | 47fbfc2749aa724863e7e483cc04d0d93909504206136d2e975a07694ddbd5f1 |

Initial non-subject access was limited to student-role.txt and route.json, route-seal.json and route-sequence.txt. Route D008-r35-reader1 has supplied route SHA256 `31e823138bcd6977fef511985188fbf062df5fa4be0e42505bcf4181fab9f48b`. No author/reviewer findings or outside subject source were used. A coordinator status-only message during MAIN15 reiterated preservation and unchanged publication; it contained no subject findings.

All subject text was obtained with the exact fixed read-step launcher and the next scheduled ID. Each request was separate; no steps were batched and no baseline revisit was used. No subject file was executed, imported, compiled or evaluated. No browser, source-link retrieval, other-agent request, search for another file, or improvised subject retrieval occurred. This was instruction-confined access, not technical isolation, erased pretraining or unavailable-memory control.

All 52 scheduled stages completed: 13 baseline text, 17 main text, 4 figure stages, 4 figure receipt stages, 7 hint text and 7 solution text. Subject text was 281802 bytes and images 214946 bytes, totaling 496748 bytes. No launcher failure or displayed-output truncation was observed. Baseline calls used max_output_tokens 8000; actual displayed token counts were 977–5233. Main/hint/solution slices were smaller and displayed completely. Raw text math/markup remained legible; actual figures, not alt text alone, were inspected.

Byte ranges below are zero-based half-open raw UTF-8. The baseline's CRCRLF was not normalised into a misleading line-count claim.

| Part | Consecutive slice boundaries, including start and final end |
|---|---|
| B01–B13 | 0, 20245, 40661, 60726, 80770, 101296, 121383, 142313, 162989, 183392, 203727, 223917, 243932, 247840 |
| MAIN01–MAIN17 | 0, 3160, 3508, 3957, 5596, 8281, 8856, 11717, 12758, 13192, 14581, 15126, 16462, 19757, 20730, 21722, 22877, 23965 |
| HINTS01–HINTS07 | 0, 192, 590, 990, 1429, 1906, 2382, 2818 |
| SOLUTIONS01–SOLUTIONS07 | 0, 249, 1107, 1991, 2848, 4023, 5444, 7179 |

All baseline chunks preceded MAIN01. Figure/view/receipt stages occurred immediately after MAIN01, MAIN04, MAIN07 and MAIN12 respectively, before later text. The entire main document preceded grouped hints; all hints preceded solutions. No early solution exposure or delayed first figure inspection occurred.

Each tools.view_image invocation used the exact launcher-returned path and detail original, displayed the actual returned image and saved its entire unchanged returned object immediately through apply_patch. The wrapper includes the actual invocation, caller-assigned correlation ID, explicit absence of a native returned call ID, and completion timestamp. The permitted record-view operation then preserved original URL bytes and generated the compact receipt; each FIGnVIEW stage accepted that receipt.

| Figure | Original result file | URL bytes | Decoded bytes |
|---|---|---:|---:|
| FIG1 | original-view-results/FIG1.json | 67201 | 50373 |
| FIG2 | original-view-results/FIG2.json | 78121 | 58561 |
| FIG3 | original-view-results/FIG3.json | 83381 | 62506 |
| FIG4 | original-view-results/FIG4.json | 58045 | 43506 |

The receipt returns explicitly say semantic_inspection_proven=false. They evidence tool-result persistence, not comprehension by themselves. The actual representation witnesses below and in chronological-reconstruction.md supply the reading evidence. The output-only notes/results were not reopened for a reader hash/readback. The report's hash is computed from the exact report string supplied to apply_patch; coordinator file-level comparison remains necessary.

## Baseline coverage and available premises

B01–B02 supply domains, algebra/substitution, graphs, logarithms, real powers, radians, small-angle formulas, derivative definition and rules, tangent equations, curvature, definite integration/FTC and rectangle-sum interpretation. These already support the elementary operations; reteaching them is not necessary.

B03 completes Mathematics mechanics and begins Further Mathematics. B04's FM27 explicitly supplies real Maclaurin coefficients and exponential, sine, cosine, logarithm and binomial series with validity ranges. It expressly does not supply a general remainder theorem or convergence proof. B04–B05 complete further mathematics, statistics and mechanics and begin Physics. B05–B08 fully cover the Physics packet, including units, error/uncertainty distinctions, model conditions and constants. The physics baseline does not supply relativistic spacetime or this clock-comparison law.

B08–B13 fully cover Chemistry: quantities, electron/bond structure, inorganic chemistry, rates, equilibrium, acid/base, energetics, electrochemistry, organic methods, spectroscopy, practical reasoning and declared scope. Cross-subject deductions are allowed only from actual supplied premises. None of the chemistry or provenance links was treated as an absent mathematical or physical theorem. Full per-chunk witnesses were recorded before teaching exposure.

## Chronological teaching and representation witnesses

**MAIN01 / §1, then FIG1.** The base x0 and its value/slope are fixed; h=x−x0 varies. B02's tangent equation gives L=f(x0)+f′(x0)h. The definition of epsilon as secant-slope discrepancy rearranges exactly to f(x0+h)=L+h epsilon, with epsilon→0 by the derivative definition. Thus error divided by displacement tends to zero; a numerical bound or monotone increase of error does not follow. Log at 1 has value 0, derivative 1 and domain x>0, giving L=x−1. FIG1 visibly labels x/output, solid ln x, dashed x−1 and contact (1,0). Their visible separation away from contact illustrates locality without proving a global error bound.

**MAIN02, MAIN03 / E1.** u=x−1 rewrites the same approximation as ln(1+u)≈u; ln1.03 uses .03. E1's sqrt at 4 has derivative 1/(2sqrt x), value 2, slope 1/4 and h=.08, so L(4.08)=2.02. The preceding tangent/error account explains estimate versus identity; the prompt demands no unprovided accuracy guarantee.

**MAIN04 / §2, then FIG2.** Values and derivatives at zero yield the five linear models: sine x, cosine 1, exponential 1+x, log(1+x) x, and power 1+rx. Log and arbitrary real powers retain positive-base domains; locality and whole substituted input are explicit. A zero slope is permitted by degree at most one. FIG2's left panel shows sine and y=x sharing the origin/slope; the right shows cosine against horizontal y=1. Both axes say radians, and legends/dashes identify models. It does not portray cosine as a globally constant function.

**MAIN05 / §§3–4, MAIN06 / E2.** e^(−2x)/sqrt(1+x), x>−1, becomes a product with first-order slopes −2 and −1/2. Constant 1 and slope −5/2 follow; the cross-product x² is not a full quadratic coefficient because both factors omitted same-degree terms. Product/chain differentiation independently verifies the slope. The power limit has numerator p(x)−p(0); p′(0)=20, or the controlled x epsilon error leaves epsilon→0 after division. E2 similarly has g=e^(3x)(1−2x), L=1+x, and independently g′(0)=3−2=1. The required limit is the derivative quotient, not an uncontrolled approximate equality.

**MAIN07 / §5, then FIG3.** Differentiating A+Bh+Ch² gives matching data A=f0, B=f′0, 2C=f″0. This explains the half factor, uniqueness, possible degree reduction and meaning of local matching rather than least squares. The new continuous-second-derivative condition is defined and supports error/h²→0. Its twice-integration sketch is accessible from B02: a small bound eta on |f″(x0+t)−f″0| leaves a twice-integrated residual bounded by eta h²/2. This is a short deduction from the supplied integration account, not an assumed untaught Taylor theorem. Exact quadratics are explicitly exact after shifting. Cosine gives Q=1−x²/2, with FM27 next term x⁴/24. FIG3 clearly identifies solid cosine, dashed parabola and dotted horizontal tangent, sharing (0,1) and separating farther away. At .2 the next term is about .0000667; it is described as a term, not an entire error bound.

**MAIN08, MAIN09 / E3.** Second derivatives produce all five quadratic formulas; sine's second-degree coefficient vanishes. Finite approximations are distinguished from infinite-series validity. For log at 2, f′=1/2 and f″=−1/4, giving Q=ln2+(x−2)/2−(x−2)²/8. At h=.1 the change estimate is .04875; ln2 cancels, so no missing numerical resource is needed.

**MAIN10 / §6, MAIN11 / E4.** Retaining both factors through degree two produces three quadratic contributions 2+1+3/8=27/8, independently checked by f″(0)=27/4. The .00135 difference between L and Q at .02 is an included correction, not the exact residual. E4 uses (1+2x)^(−1/2)≈1−x+(3/2)x² and e^x≈1+x+x²/2: linear terms cancel and quadratic contributions total 1. Hence L=1,Q=1+x². The earlier residual/h²→0 supports the positive leading change on both sides sufficiently near zero, without claiming an all-domain identity.

**MAIN12 / §7 opening, then FIG4.** The clock law is expressly a supplied physical premise for constant speed, 0≤v<c, ignoring gravity/acceleration. T is the interval between two ticks of the same onboard clock; T′ assigns the same events in a synchronized ground frame, explicitly distinct from uncorrected received-signal intervals. FIG4 shows first/second tick markers, one moving clock and a straight arrow, onboard T and ground-frame T′ labels. It is intelligible as an event-identification schematic, not an orbit or a scaled spacetime diagram. External scientific truth is not established by this reading.

**MAIN13, MAIN14 / E5.** z=v²/c² is dimensionless and u=−z,r=−1/2 gives F≈1+z/2+3z²/8. Multiplication by T retains time units. At the supplied v and c, z≈1.78e−10, first fractional correction≈8.89e−11 and next≈1.19e−20; T=86400 s gives 7.68 microseconds at first order. Linear/quadratic refer to z, corresponding to speed powers two/four. GPS/gravity and historical instrument statements are marked additional empirical context, not consequences of the expansion.

The whole-segment tangent bound is newly taught before E5: |f″|≤M and continuity allow integration of derivative change to ≤M|t|, then output error to ≤Mh²/2 in either direction. F″=(3/4)(1−z)^(−5/2)<1 on [0,1e−4] gives ratio error ≤z²/2 and time error ≤Tz²/2. E5 obtains .05 s or .05000375 s; its entire linear error ≤5e−6 s is below the 1e−5 s tolerance. The quadratic contribution 3.75e−6 s is correctly distinguished from a complete remainder bound. This bridges the precise theorem absent from FM27 before dependent use.

**MAIN15 / §8, MAIN16 / E6, MAIN17 / source notes.** Method selection checks output/tolerance, base/domain, effective input, degree contributions, units and conditions. |x| has incompatible one-sided slopes at zero, directly following its baseline piecewise definition. The global-reliability sentence has the scope ambiguity already identified. E6 distinguishes unscored formula recall from method choice: sine remains x through degree two; 50x=1 at x=.02 is not justified by x's smallness; sqrt's positive-side quotient 1/sqrt h lacks a finite limit. These are accessible from prior teaching and baseline. Provenance claims about all source pages and original printed errors cannot be independently verified without admitting the external lecture, but no such external content is needed for the presented calculations.

## Grouped help and solutions, in actual later order

HINTS01 is navigation. HINTS02–07 respectively identify E1's displacement/base slope, E2's effective argument and derivative quotient, E3's shifted variable and constant cancellation, E4's three degree-two pairings, E5's time multiplier and whole-error comparison, and E6's controlling coefficient/input/finite slope. Each directs attention to an already available connection; none is needed to retroactively repair an earlier unsupported exercise.

SOLUTIONS01 permits equivalent correct reasoning. SOLUTIONS02–07 are consistent with the corresponding original demands:

- E1 gives 2.02 and checks 2.02²=4.0804, establishing nonidentity without promising decimal accuracy.
- E2 rejects the truncated product's −6x² as the full coefficient and proves limit 1 independently.
- E3 gives .04875 and verifies it through the exact logarithm identity ln(2.1)−ln2=ln1.05 with input .05.
- E4 gives 1+x² and explicitly uses residual/x²→0 to justify the local sign on both sides.
- E5 gives both time estimates and the complete linear-error guarantee; subtracting exact fixed T leaves error unchanged. The claim excludes gravity and input uncertainty.
- E6 restates L/Q correctly; sine's first omitted nonzero correction is −x³/6. The exponential series at 1 begins 1+1+1/2 with further positive terms, concretely exposing the large omission. Sqrt's right quotient is unbounded, so a vertical geometric tangent is not a finite-slope output function. Other approximation methods/positive base points remain possible.

## Issue classification and supported endpoint

**Established missing or invalid consequential teaching connections:** none found in this complete reading. This is not a claim to have discovered every latent error.

**Supported ambiguity:** the §8 unlimited-interval sentence, with the two readings and consequence described above. It should not erase the earlier supported exact-polynomial case. No result is conditionally blocked by it.

**Conditional claims and input limits:** the stated time-dilation law and empirical GPS values are accepted only as supplied model/empirical premises; source-completeness and historical-correction claims were not independently checked. No missing subject bytes, unreadable figure region, failed retrieval or clipped output was observed. Reader understanding does not prove real human learning, retention or instrument/physical truth.

The original incremental records are reader-access-notes.md and chronological-reconstruction.md in this same reader directory. They preserve each step's displayed-output observations and first-encounter witnesses, including the scope concern before later help. Original figure objects are in original-view-results/FIG1.json through FIG4.json; compact receipts are in view-results/fig1.json through fig4.json. The coordinator's audit must compare these with the launcher ledger before removing this report's provisional status.

