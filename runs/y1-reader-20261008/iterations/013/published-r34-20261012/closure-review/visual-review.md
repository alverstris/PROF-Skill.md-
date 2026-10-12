# D013 r34 rendered visual review

Reviewed pin: `ce407f3f2a5276700e61f43d7d1c371b9f452121`.

Status: complete visual inspection, including both requested ordinary-viewport recoveries. No material visual defect found in the reviewed rendered teaching. One minor, nonblocking label overlap is recorded below. This is a rendered visual and information-visibility review, not SASIS evidence or mathematical closure.

## Scope and provenance

The frozen `main.md`, `hints.md`, `solutions.md`, and all three figure PNGs match every byte count, SHA-256, and Git blob SHA-1 in the supplied freeze manifest. The recomputation is in `identity-verification.json`. The three actual DOM captures identify the requested immutable pin; all three image sources are the corresponding raw paths at that pin, all report complete loading, and their natural sizes are 960×564. The actual screenshots visibly contain those same three plotted compositions. I did not independently retrieve the remote PNG bytes; the local byte check, pinned DOM identities, and actual visual match are distinct supporting evidence.

Only the allowed frozen content, actual main/hints/solutions screenshots and DOMs, the first-Q6-return screenshot, and root-supplied capture recoveries were inspected. No prior teaching version or review was consulted. The initial filesystem inventory listed pathnames within the package before reads were restricted to the exact permitted files. No browser or GitHub operation was performed by this reviewer.

The original full-page screenshots were preserved. Each was inspected in full-width 1348-pixel crops of up to 1200 pixels, with 200-pixel overlap and no skipped vertical intervals: eight main crops covering y=0–7810, two hints crops covering y=0–1217, and three solutions crops covering y=0–2869. All three complete original PNGs were separately viewed at their native 960×564 resolution. `crop-manifest.json` supplies crop rectangles; `read-log.json` records the actual inspection sequence. A 4× diagnostic crop was added only after the native inspection identified the Figure 3 label contact.

## Coverage and result

| Region | Actual evidence | Visual result |
|---|---|---|
| Main introduction, continuity and differentiability definitions | Main crops 1–2, y=0–2200 | Body text, inline conditions, one-sided/end-point qualifications and displayed difference quotient are readable. No raw math delimiters or equation clipping. |
| MVT statement, square example, Figure 1, Q1 | Main crops 2–3, y=1000–3200; original `mvt-square.png` | Displayed theorem fraction is readable. Curve, secant, tangent, dotted parallel line, axis labels, endpoint labels and c=1 annotation are distinguishable. Caption and question are complete. |
| Subtract-a-line proof | Main crop 3, y=2000–3200 | h(t) construction, interior extremum argument, one-sided sign argument and concluding displayed equation remain visibly readable. |
| Failed condition, Figure 2, Q2 | Main crop 4, y=3000–4200; original `cusp.png` | V branches, secant, red support line and corner annotation are clear. Legend says support line rather than derivative-bearing tangent; caption explains the distinction. Q2 and its help links are visible. |
| Motion example | Main crops 4–5, plus `root-review-d013-r34/destination/d013-r34-motion-recovery-cached.jpg` | Recovery shows the complete model, endpoint values, displayed speed equation, conclusion, and signed-velocity distinction. All are legible and unobscured. |
| Exact change, tangent approximation, Figure 3, Q3 | Main crops 5–6, y=4000–6200; original `linear-approximation.png` | Exact and approximate equations have visibly different equality/approximation symbols. Figure has correct visible heights 3.24 and 2.60 and an error 0.64 annotation, matching nearby prose. Minor overlap is recorded below. Caption and Q3 are complete. |
| Derivative signs, strict increase/decrease/constant cases, Q4 | Main crops 6–7, y=5000–7200 | Strict inequality signs, universal interior sign statements and interval qualifications are readable. No overflow in longer inline expressions. |
| Exponential comparison chain, Q5, series caveat | Main crops 7–8, y=6000–7810 | Subscripted difference functions, derivative equations, factorial fractions and the series sum are visible and readable. The caveat distinguishing finite bounds from infinite equality is fully visible. |
| Changed comparison, Q6, later revisit | Main crop 8, y=7000–7810; first-Q6-return screenshot | Entire question, positive/negative input ranges, strictness and zero-endpoint requirements, help links and revisit paragraph are visible. |
| Hints Q1–Q6 | Both hints crops, y=0–1217 | All six hint paragraphs and both links per hint are readable; no capture obstruction or clipping. |
| Solutions Q1–Q4 | Solutions crops 1–2, y=0–2200 | Roots, fractions, one-sided limit, exact/estimated values and sign proof are readable. Explanations and corresponding return/help links are visible. |
| Solution Q5 | Solutions crops 2–3 plus `d013-r34-solution5-recovery-clean.jpg` | Recovery independently inspected. The whole solution, including both displays, strict-bound/zero-endpoint paragraph and finite-bound counterexample, is readable and unobscured. |
| Solution Q6 | Solutions crop 3, y=2000–2869 | Domain, rational derivatives, positive and negative comparison equations, strictness, zero case and excluded logarithm inputs are all visible and readable. |

The source contains 196 inline plus 13 display expressions in main, 14 inline expressions in hints, and 103 inline plus 7 display expressions in solutions. These match the DOM math-renderer counts of 209, 14 and 110. All three captured `errors` and `rawMath` arrays are empty. These checks support, and do not replace, the visual examination. See `dom-inspection-summary.json`.

## Minor finding

**V1 — Figure 3 label crosses the curve; nonblocking.** In frozen `teaching/figures/linear-approximation.png`, the dark parabola runs through the final digits of the annotation `estimate 2.60`, approximately x=570–600, y=265–290 in the native 960×564 image. It is also visible in main full-page screenshot crop 5 near full-page y=5000–5025. The preserved diagnostic crop is `crops/figure3-estimate-label-detail-4x.png`.

The numeric label remains identifiable as 2.60, its leader ends at the blue estimate point at input 1.8, and the legend, exact-height label, error annotation, alt text and nearby calculation preserve the intended meaning. This is a small label-placement defect, not a material teaching or information-visibility failure. A later graphical revision could move the estimate annotation slightly left/up or place an opaque white box behind the text. No frozen constituent was changed.

## Capture obstructions and recoveries

The main full-page image has GitHub's sticky toolbar over x=273–1347, y=4144–4233. This covers the end of the paragraph beginning `Since s(0)=0 and s(3)=1000`, the displayed instantaneous-speed equation and the opening of `An instantaneous speed equals…`. This was classified as capture obstruction, never as a teaching defect. The independently inspected ordinary-viewport recovery is `root-review-d013-r34/destination/d013-r34-motion-recovery-cached.jpg`. It clearly shows the complete motion section through the next heading, including s′(c)=(s(3)−s(0))/(3−0)=1000/3 miles/hour and the full following paragraph. No missing information remains in that strip. The initially announced root-level motion filename was not locally present; only the final existing cached file named here was inspected.

The solutions full-page image has the same toolbar over x=273–1347, y=1908–1998. It covers the end of the Q5 derivative-sign/anchor paragraph and the start of its finite-lower-bound paragraph. The supplied `d013-r34-solution5-recovery-clean.jpg` was independently viewed at its original resolution. The relevant content, including the sequence 1−1/n counterexample and its limit explanation, is clear; no missing information remains in that strip. The pointer is in blank space beside the Q5 heading.

`d013-r34-first-return.jpg` shows the complete Q6 prompt, its links and the revisit paragraph visible after the recorded first return. This review makes no claim about other navigations or interaction history from that one screenshot. Source/DOM anchor presence is not treated as a substitute for testing those other routes.

## Boundaries

The observed typography is legible at the supplied desktop capture sizes, including ordinary script-sized primes, indices, powers and limit conditions. Titles and section labels use the same body-scale paragraph styling as the prose; they remain recognizable by wording and spacing. I did not classify a preference for stronger heading hierarchy as a failure. The three figures have complete axes, legends and captions; no missing image, distorted aspect ratio, clipped label, blank rendered formula or off-page prose was found, aside from the minor label intersection already specified.

This report does not certify mobile layouts, screen-reader behavior, unobserved navigation, source mathematical completeness or learner mastery. Its conclusion is confined to the actual supplied rendered desktop teaching at the frozen pin.
