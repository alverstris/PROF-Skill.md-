# D008 r31 independent technical report

Reviewer: `/root/technical_d008_r31_prepared`. This report evaluates only the admitted frozen generation. It is a technical review, not a SASIS reading, author revision, destination review or claim about human learning. The access boundary was instructional; shared files were not technically inaccessible.

## Result and limits

The complete local technical inspection found no verified material mathematical error, incorrect answer, mismatched hint, changed prompt demand or contradictory figure in the seven admitted teaching files. All six prompts and the 31 substantive demands recorded before teaching access agree with the independently sealed solutions. The lecture's principal constructions and examples are covered, including conditions, units, the order of approximation and the remainder needed after division in a limit. The new quadratic-remainder argument is mathematically valid under its stated sufficient condition and can use the fully admitted baseline's fundamental theorem of calculus.

This is a bounded technical result, not an unconditional acceptance of the whole generation. External GPS references at README line 292 were not admitted and were not opened. Their supporting contents and present accessibility remain unverified here (U1 below). Destination rendering, live navigation and SASIS sufficiency are also outside this review. No empirical learning, retention or transfer result follows from expert solution agreement or an optional request to return later.

The frozen teaching was not edited. No findings or answers were sent to the author during this review.

## Exact evaluated identity and sequence

The admitted freeze manifest is `d008-clean-r31-20261011/evidence/freeze-manifest.json`, SHA-256 `7bc78597ea26b3fd56ea7ab39e37f7385407215117efa6436ff54dcb9e1da060`. Its declared freeze time is `2026-10-11T23:56:42.189405+00:00`. Its hash and all seven constituents were validated before substantive frozen-teaching access and checked again at completion. The exact copied manifest and complete constituent identities accompany this report.

The independent prompt-only solution seal is SHA-256 `79b8d4cdc6ffcc9af82cb2e60d9502ebd2b9bd9065ca5a7bd8776c296af69894`, sealed at `2026-10-11T23:53:08.446531+00:00`, before teaching receipt/access. The six-prompt packet is 2903 bytes, SHA-256 `1ab828b05bb916c4154ca3aca73d92f097593ae1bbeec164b11da47bc388c35f`. Comparing every frozen prompt with that packet found mathematical presentation changes only, with the same substantive demands and supplied data.

The original source is the seven-page MIT 18.01 Fall 2006 Lecture 9 PDF, 880629 bytes, SHA-256 `d1b383663f7792bbdaa4d6108e17b11679d4688e413e197486941af337892320`. Original preparation read all seven page texts and inspected both all seven supplied whole-page images and all seven fresh PDF renders, including the cover. Those image sets were not pixel-identical; the earlier preparation accurately records their rendering differences and corresponding mathematical content. The full 247840-byte operational baseline, SHA-256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`, was read across Mathematics, Further Mathematics, Physics and Chemistry before independent solutions. These unchanged preparations were reused rather than replaced by topic labels.

The admitted corrected PROF package is the complete 36-file local copy at `d008-clean-r30-20261011/corrected-prof-r31-published/`. Its admission seal is SHA-256 `74f458080256b6524340290f528fb53cc34f22808cb384719fb04297338cab40`. All 36 file identities were rechecked unchanged during this review. The earlier full requirements reading, corrected two-file reading and all 34 bundled internal-hash checks remain valid. Initial package-failure evidence was preserved, not rewritten.

The parent supplied publication pin `da856ff6379c75e051e0afc8410a24a5a2822bc9`. The frozen manifest names the later incoming pin `db14dd37eb1ee3a69873036a8100fd2a6cb53dce`. Root operationally confirmed that all 36 operative package files are byte-identical between them and that the later commit concerns progress/evidence handover. This reviewer checked the admitted local bytes, not either remote publication, and did not open root's separate receipt.

After the substantive report draft was written but before its final seal, root sent an unsolicited operational statement that it had separately verified the narrow GPS claim against NIST and Ashby publisher text, then explicitly instructed this reviewer not to rely on that statement as independent evidence. This exposure is disclosed; complete review-history blindness is not claimed. No external text, calculation, author finding or other review file was received through it. The independent mathematical conclusions and U1 access limitation remain based on this reviewer's own admitted inputs. The original-only and prompt-only seals predate the message and are unchanged.

## Whole-source coverage and mathematical findings

Physical page numbers include the cover; lecture-page numbers begin on physical page 2. The separate `source-coverage.json` supplies a machine-readable mapping.

| Original source | Frozen teaching coverage | Technical result |
|---|---|---|
| Physical 1, cover | README 3–5, 342–344 | MIT course, term and lecture attribution retained. No mathematical claim on the cover was mistaken for a premise. Terms links were not followed. |
| Physical 2 / lecture 1: tangent construction, logarithm at 1, shift to zero, local diagram | README 13–45, 53–55; tangent image | Correct point-slope formula, fixed basepoint and displacement. Remainder ratio follows from differentiability. `ln(1+u)` uses the correctly shifted coordinate and positive domain. Local contact does not become a universal monotonic-error claim. |
| Physical 3 / lecture 2: five linear models, sine/cosine diagrams, exponential factor | README 53–80, 84–95; basic-tangents image | All five value/slope pairs correct, radians explicit, real-power/log domain and fixed parameter stated. The source's literal approximation-as-equality shorthand is not repeated as a function identity. |
| Physical 4 / lecture 3: reciprocal root, linear product, derivative, difference-quotient limit, clock law and reciprocal shortcut | README 84–119, 127–151, 243–258 | Linear coefficient `-5/2` verified by differentiation. The apparent cross-term coefficient 1 is correctly rejected as a full quadratic coefficient. Limit 20 has a derivative/remainder justification. Alternative reciprocal route retained; nonzero denominator and stated model conditions explicit. |
| Physical 5 / lecture 4: clock ratio and numerical scale, general quadratic construction, cosine coefficients | README 153–199, 243–290 | Factor `T` and the ratio/time distinction are correct; the source's exponent-template typo is absent. General quadratic matching gives coefficient `f''(a)/2`; exact quadratics reproduced. The model is explicitly local, not a least-squares fit. The added remainder proof is assessed below. |
| Physical 6 / lecture 5: cosine figure, quadratic table, clock quadratic term | README 193–219, 260–290; cosine-quadratic image | Five quadratic coefficients correct, including sine's zero square term. Clock coefficient `3/8` has correct substitution/sign and is fourth order in speed ratio, second order in `q`. |
| Physical 7 / lecture 6: next clock correction, precision/GPS context, complete quadratic product | README 274–334 | Clock arithmetic and complete coefficient `27/8` correct. Source precision claim is qualified rather than asserted as a current experimental fact. GPS motion/oscillator context is retained with an expanded gravity distinction; external support for that distinction has the U1 access limit. |

The more general source claims were also checked. Approximation is distinguished from equality throughout. A degree-two approximation may have zero quadratic coefficient. Domain membership and a small input do not independently certify a numerical tolerance. The notes do not claim that quadratic approximations are universally closer at every finite input. The logarithm and cosine figures illustrate specified local examples rather than global error theorems.

For the original combined function `F(x)=exp(-2x)(1+x)^(-1/2)`, the real domain is `x>-1`. Independent product differentiation gives `F'(0)=-5/2`, `F''(0)=27/4`, and quadratic coefficient `27/8`. The expansion obtains the same coefficient as `2+1+3/8`. README 111 and 322 correctly preserve the relevant remainder ratio when multiplying by bounded factors, and the polynomial terms discarded beyond the requested degree vanish after division by that degree's power. They do not treat multiplication of two approximate equalities as unexplained exact algebra.

README 175–191 explicitly assumes a continuous second derivative on an open interval about the basepoint. For `E=f-Q`, the matched derivatives give `E(a)=E'(a)=E''(a)=0`. Continuity gives `|E''|<epsilon` throughout a sufficiently short interval. Applying the fundamental theorem twice gives `|E'(a+t)|<=epsilon|t|` and `|E(a+h)|<=epsilon h^2/2`, for either sign of displacement. Hence `E(a+h)/h^2` tends to zero. This is a valid sufficient-condition proof, not an unsupported inference from the existence of a value at the basepoint, and it does not promise a fixed-input error tolerance. The full Mathematics baseline explicitly grants the fundamental theorem for a suitably continuous integrand (raw LF line 178, Integration and elementary differential equations). FM27 separately grants Maclaurin expansions but not a general remainder theorem; the teaching supplies the extra local argument rather than assuming that exclusion away. Expert validity here does not establish SASIS availability at every reading step.

The clock treatment supplies the physical law as a model premise. README 243–258 defines the same two events, the onboard interval, synchronized reference clocks, the speed and units, the restriction `0<=v<c`, and positive `T`. It separates reference elapsed time from light-arrival delay at one observer. The new figure matches those meanings. Under that stated law, `q=(v/c)^2`, fractional excess `q/2` and next term `3q^2/8` are correct. At the lecture's speed 4 km/s they give about `8.89e-11` and `1.19e-20`; for 86400 seconds these contribute `7.68` microseconds and `1.024e-15` seconds. All displayed rounding is consistent. No full relativistic derivation or contemporary clock-resolution premise is silently demanded from the baseline.

## Every prompt and its help

The original independent solutions include their own analytic derivations and numerical checks. They were sealed before access to the authored answers. The authored proof need not reproduce the independent solution's particular series-tail bound: another correct, adequately supported proof is acceptable.

| Prompt and final location | Agreement and complete demand coverage | Help inspected |
|---|---|---|
| P1, README 49 | `h=.08`, derivative `1/4`, tangent `2+(x-4)/4`, estimate `2.02`; squaring gives `4.0804`, so the approximation is not an identity. The overestimate conclusion is justified for positive roots. | Hints 9–13; solutions 9–25. |
| P2, README 123 | Domain excludes `1/2`; the authored `|x|<1/4` is a legitimate neighborhood, different from but as valid as the independently chosen one. Actual small inputs `3x` and `-2x` give `1+5x`. The cross-term 6 cannot establish the full quadratic coefficient because factor-square contributions were omitted. The optional full coefficient `29/2` is correct. | Hints 17–21; solutions 29–50. |
| P3, README 231 | Correct value, first and second derivatives at 2; `L=ln2+(x-2)/2`, `Q=L-(x-2)^2/8`. Estimates `.71314718` and `.71294718` have shown discrepancies `.00019737` and `.00000263`; both rounded-reference and nonuniversal-comparison qualifications are explicit. Squared displacement preserves matched value/slope while adding curvature. | Hints 25–29; solutions 54–84. |
| P4, README 237 | Limit `1/2`; cancellation makes a first-order model insufficient. Authored `R2/x^2 -> 0` is the required sufficient error condition. The exponential satisfies the prior C2 argument. The example of an arbitrary multiple of `x^2` correctly discriminates first-order from second-order information. | Hints 33–37; solutions 88–106. |
| P5, README 296 | `q=4e-10`; first fraction `2e-10`; time difference `1.728e-5 s=17.28 microseconds`; next fraction `6e-20`. Adding that term is below the absolute fractional scale `1e-12`. Powers of `v/c` are 2 and 4. Comparison of these two terms is explicitly distinguished from bounding the whole omitted remainder. | Hints 41–45; solutions 110–145. |
| P6, README 338 | Domain `x>-1/2`; `H=2x-4x^2+R`, with two nonzero quadratic contributions `-2x^2` and `-2x^2`. The exponential square contributes no degree-two term because the logarithm's constant is zero. Bounded-factor remainder reasoning gives `R/x^2 -> 0` and limit `-4`. Expansion order is connected to cancellation and division. | Hints 49–53; solutions 149–176. |

All six hints address the corresponding task and contain correct mathematics. All six full solutions supply reasons as well as results and match the requested units, domains and variables. Neither a hint-only fact nor an answer-only theorem is needed to retrospectively supply the earlier quadratic remainder condition: its proof appears in the main teaching before P4. P2's early linear-factor question asks why a quadratic coefficient is unestablished; the necessary missing-contribution argument is already explained in section 3, and baseline algebra supports it. Its answer's optional later quadratic confirmation is labeled accordingly.

The presealed P5 interpretation note was resolved without changing the task. The prompt compares a contribution to a fractional scale in the displayed dimensionless correction, and the solution compares that absolute fractional amount. It does not claim `1e-12` relative accuracy of the tiny correction itself. That different denominator would produce a different question, not a verified error in this one.

P6 is suggested for a later return, but no delayed attempt was observed. Its zero constant, cancellation and divisor create mathematical decisions beyond substituting new numbers; this report does not infer learner transfer from that design or from a successful expert answer.

## Complete visual inspection

All four full PNGs were opened and visually inspected, including their titles, legends, axes, annotations and whitespace. No crop was used as a substitute for the full view. Image dimensions and hashes are in `static-artifact-checks.json`.

| Figure | Inspected relationship and result |
|---|---|
| tangent.png | `ln x` and `x-1` meet at labeled `(1,0)` with matching tangent; logarithm lies below its tangent on the shown positive domain. Axes, curve legend and basepoint arrow agree with README 43–45. |
| basic-tangents.png | Full left sine and right cosine panels show tangents `x` and `1`, contact at zero, correct signs and qualitative shapes. No degree-two correction is invented for sine. Caption agrees with README 76–78. |
| cosine-quadratic.png | Full cosine curve, horizontal linear model 1 and downward parabola `1-x^2/2` meet at `(0,1)`. Labels and plotted curvature/order agree with README 201–203. |
| clock-model.png | Same moving clock is represented at two ticks, with elapsed onboard `T`, constant-speed arrow and synchronized reference clocks assigning `t1,t2`; `T'=t2-t1` is explicit. Caption prevents interpreting the arrow as a light-signal path. |

The source-level local image paths and internal explicit-anchor links resolve in the frozen package. This static fact is not evidence that the destination renderer displayed the images, math or navigation correctly. A temporary checker failure treating a same-page `#anchor` as an empty file path was corrected to use the current file; it was a reviewer-checker bug, not a teaching defect.

## Obligations and unresolved evidence

| Obligation group from admitted PROF | Technical disposition |
|---|---|
| T1–T3: meaning, hypotheses, representations and valid inference | No verified material defect in reviewed mathematics, domains, units or conditional clock model. Remainder conditions and their implications were checked, including both signs of displacement. |
| T4–T7: connected reasoning, application, task criteria and matched help | All six tasks, hints and full solutions inspected and cross-checked. Main reasoning supports the later limit tasks. No help-only missing premise identified. |
| T8–T9: retention/transfer and full-baseline fit | Baseline scope was read in full and used explicitly; formal learning outcomes and chronological SASIS sufficiency are not inferred by this reviewer. Optional return instruction is not an observed delay. |
| T10: independent correctness and important claims | Source constructions, expansions, limits, rounding, model dimensions and all answers verified. External GPS support has the specific U1 limitation below. |
| T11–T12: separation, format and verification status | Main notes, hints and solutions are separate, with static paths/anchors checked. Browser rendering, destination-added emphasis and live navigation are not claimed. |

U1 — external-source verification limitation, not a demonstrated false statement. README line 292 says GPS accounts for motion and gravity and satellite oscillator frequencies are adjusted, and attributes the distinction to NIST and Neil Ashby. The original lecture already supplies GPS/frequency-calibration context, but the expanded gravity distinction and the two cited pages' actual support were not independently checked from admitted contents. No network or adjacent author-research evidence was accessed. No counterexample or factual contradiction has been established. A fully source-verified scientific release therefore needs separate source-evidence verification or disclosure of this bounded limitation; this report supplies neither an independent validation of those pages nor evidence that they are wrong. Root's later operational statement is disclosed above, not adopted as this reviewer's verification. This report does not prescribe a teaching rewrite or a new PROF rule on the basis of the unverified concern.

No verified material teaching defect was found, so there is no invented defect list or reusable repair proposal. The source-level errors discovered in original preparation were actually corrected or appropriately qualified in the frozen notes; their historical existence is not a defect in these evaluated bytes.

## Completion evidence

The accompanying files preserve the admitted manifest, exact constituent checks, full prompt/demand mapping, all-page source coverage, numerical witnesses, static-link/image checks and exact read/access record. All original, package-failure, corrected-package and prompt-only seals and their declared artifacts were checked unchanged. Source, baseline, prompt packet, all 36 operative PROF files and all seven teaching constituents were also checked unchanged. The final report seal binds the review artifacts after the whole audit, and carries the same limited result stated above.
