# D008 original-source technical preparation

Status: complete for the original source only. No fresh teaching or finalized learner prompt has been received or read. This is preparatory technical work, not a SASIS judgment and not a verdict on an authored lesson.

## Source identity and actual access scope

- Original: MIT 18.01 Fall 2006, Lecture 9, *Linear and Quadratic Approximations*.
- Stable ID: `mit-18-01-fall-2006-L09`; material ID: `D008`.
- Exact input: `/workspace/scratch/f9c0b7fc7e76/original-inputs/D008/lec9.pdf`.
- PDF SHA256: `d1b383663f7792bbdaa4d6108e17b11679d4688e413e197486941af337892320`.
- Size: 880629 bytes; 7 PDF pages: one cover and printed lecture pages 1-6.
- I read every supplied literal page-text file, viewed each full-page PNG at its full extent, and independently extracted every PDF page. The fresh extraction matches every cached page text byte for byte. All 16 entries in the supplied SHA256SUMS verified (PDF, 7 texts, 7 PNGs, source identity).
- Read metadata: `source-identity.json` and `SHA256SUMS`. The identity metadata contains ancestry paths naming earlier work and a queue hash. I saw those metadata strings but did not follow those paths or read their contents.
- Initial location correction: the originally supplied `earlier-source-preparation-20261011/original-inputs/D008` path did not exist. I searched filenames only within that scope and listed its top-level names, without reading its manifest, preparation script, or `lec7.pdf`. The parent then provided the verified `original-inputs/D008` packet.
- Other reading: the PDF skill, supplied through the skill tool. No PROF/SASIS package or baseline has yet been provided or read in this task.
- No earlier teaching, queue/history contents, held audits, other reviewers' reports, diagnoses, or GitHub/browser content was read for this preparation. No browser control or web search was used. No original was edited and nothing was published.
- This records actual task access. It does not claim technical isolation, inaccessible shared files, or erased prior knowledge.

## Complete page and figure coverage

| PDF page | Printed page | Full source content read and inspected | Technical conclusion |
|---|---:|---|---|
| 1 | Cover | MIT OCW attribution, course/year and terms notice; entire page image and text | No mathematical material |
| 2 | 1 | Lecture/unit heading; linearization formula at arbitrary basepoint; Figure 1 tangent/curve; logarithm at 1; substitution `x=1+u` | Formula and logarithm calculation correct; approximation is local |
| 3 | 2 | Five linear approximations at 0; sine and power derivations; both panels of Figure 2; beginning of Example 2 | Coefficients correct; two misleading equality signs in proof prose/equations require correction |
| 4 | 3 | Completion of product/reciprocal linearization; why higher terms are discarded; derivative inference; polynomial limit; Planet Quirk definition and exact formula; reciprocal shortcut footnote | All target coefficients and limit correct; asymptotic interpretation needed for derivative/limit deductions |
| 5 | 4 | Figure 3 satellite sketch; definitions of `T,T'`; first-order relativity formula and numeric scale; GPS context; general quadratic formula; cosine example; derivation of the `1/2` coefficient from a quadratic | Taylor algebra correct except missing `T` on one displayed approximation and apparent exponent `4` typo; physical/contextual claims need scoped wording |
| 6 | 5 | Figure 4 cosine/parabola; general quadratic formula at 0; five quadratic formulas; logarithm derivative proof; second-order Planet Quirk expansion | All mathematical coefficients correct; quadratic refers to expansion in `v^2/c^2` in that application |
| 7 | 6 | Relativity second-order size and atomic-clock assertion; complete quadratic product Example 5; instruction to discard cubic/higher terms | Product coefficient `27/8` correct; numerical scale correct as order of magnitude; empirical clock claim not independently verified |

Every Figure 1-4 was inspected. Figure 2 contains two panels, both read. Figure 1 is a schematic rising concave-down curve with a tangent; its nearby geometric relationship is consistent with linearization. Figure 2 correctly shows the sine tangent through the origin and cosine horizontal tangent at zero. Figure 3 is contextual rather than quantitative. Figure 4 correctly shows `1-x^2/2` tangent to cosine at its maximum and below cosine nearby. The sketches have no numerical coordinate ticks and should not be treated as measured error plots.

## Independently checked mathematics

Write `h=x-a`. A first-order Taylor polynomial is `L_a(x)=f(a)+f'(a)h`. Differentiability at `a` gives the precise statement `f(a+h)=f(a)+f'(a)h+o(h)`. Under a sufficient smoothness hypothesis such as `f` being twice continuously differentiable on a neighborhood, the quadratic Taylor polynomial is `Q_a(x)=f(a)+f'(a)h+f''(a)h^2/2`, with remainder `o(h^2)`. Bounded higher derivatives justify the stronger remainder orders commonly used for the analytic examples here.

For all formulas below, expansions are at zero, the angle is in radians for trigonometric functions, and the parameter `r` is fixed:

| Function | Linear Taylor polynomial | Quadratic Taylor polynomial | Natural real local domain |
|---|---|---|---|
| `sin x` | `x` | `x` | all real `x` |
| `cos x` | `1` | `1-x^2/2` | all real `x` |
| `exp x` | `1+x` | `1+x+x^2/2` | all real `x` |
| `ln(1+x)` | `x` | `x-x^2/2` | `x>-1` |
| `(1+x)^r` | `1+rx` | `1+rx+r(r-1)x^2/2` | `x>-1` suffices for every real `r` |

The power coefficient follows directly from `f'(x)=r(1+x)^(r-1)` and `f''(x)=r(r-1)(1+x)^(r-2)`. The sine second derivative at zero vanishes, so its degree-at-most-two Taylor polynomial has no quadratic term. For the smooth examples, the omitted terms are `O(x^3)` after the quadratic polynomial; cosine actually has `O(x^4)` remainder and sine has leading remainder `-x^3/6`.

The logarithm example at basepoint 1 gives `ln x = (x-1)+O((x-1)^2)`, and the coordinate substitution gives `ln(1+u)=u+O(u^2)`. This is a shift of variable/basepoint, not a claim that the physical value of the original input has become zero.

For `f(x)=exp(-2x)/(sqrt(1+x))`, `x>-1`:

1. `exp(-2x)=1-2x+2x^2-(4/3)x^3+O(x^4)`.
2. `(1+x)^(-1/2)=1-x/2+3x^2/8-5x^3/16+O(x^4)`.
3. Linear coefficient: `-2-1/2=-5/2`.
4. Quadratic coefficient: `2+(-2)(-1/2)+3/8=27/8`.
5. Therefore `f(x)=1-(5/2)x+(27/8)x^2-(163/48)x^3+O(x^4)`.
6. Independent derivative route: `f'/f=-2-1/[2(1+x)]`, so `f(0)=1`, `f'(0)=-5/2`, and `f''(0)=(-5/2)^2+1/2=27/4`; division by `2!` reproduces `27/8`.

In the source's linear computation, multiplying first-order factor approximations produces an `x^2` cross term. That cross term alone is not the true quadratic coefficient: the omitted quadratic terms of the two factors also contribute. Dropping it is correct when retaining only degree one. A quadratic calculation must first retain both factors through degree two and then include all degree-two contributions.

For the polynomial limit, the exact binomial expansion starts `(1+2x)^10=1+20x+180x^2+960x^3+...`. For `x` nonzero, division after subtracting 1 gives `20+180x+960x^2+...`, with limit `20`. This independently agrees with the derivative definition and the source result. An unqualified approximate numerical equality alone would not license division by a vanishing `x`; the remainder order does.

For the stipulated relativity model, set `z=v^2/c^2`. Then

`T'/T=(1-z)^(-1/2)=1+z/2+3z^2/8+O(z^3)`.

At `v=4 km/s`, `c=300000 km/s`, `z=1/5625000000 = 1.7777777777777778e-10`, the leading fractional increase is `z/2 = 8.888888888888889e-11`, and the quadratic fractional correction is `3z^2/8 = 1.1851851851851851e-20`. Thus the source's powers `10^-10` and `10^-20` are legitimate order-of-magnitude descriptions. The two approximations for elapsed time are `T' approximately T(1+z/2)` and `T' approximately T(1+z/2+3z^2/8)`. An absolute time error requires multiplying the fractional correction by the stated interval `T`.

The intended small parameter is `z`, so the first-order expansion in `z` already has a term quadratic in `v/c`, and the second-order expansion in `z` contains `(v/c)^4`. Labeling these simply linear/quadratic in speed would be incorrect.

## Source slips and qualifications to preserve in later review

1. PDF page 3, sine proof: the source says `f(x)=x` after defining `f(x)=sin x`. That equality is false as a function identity. It should be `f(x) approximately x`, or an exact definition `L_0(x)=x` of the linear Taylor polynomial.
2. PDF page 3, power proof: the last equation writes `f(x)=f(0)+f'(0)x=1+rx`. The first equality is generally false. Use an approximation or name the polynomial separately. Exceptional exponents do not validate the general equality.
3. PDF page 5, relativity display: after `T'=T(1-v^2/c^2)^(-1/2)`, the right side is printed as `approximately 1+(1/2)(v^2/c^2)`. It omits the factor `T`. Correct either the right side to `T[1+(1/2)(v^2/c^2)]` or the left side to `T'/T`. The same line's bracket prints `(1+u)^4 approximately 1+ru` with `r=-1/2`; the exponent should be `r`, not `4`. These readings are confirmed on the page image and are not extraction artifacts.
4. PDF page 2's statement that approximation becomes less accurate as one moves away is a useful local warning, not a theorem that absolute error must grow monotonically with distance for every function.
5. The source does not state differentiability/smoothness hypotheses or numerical remainder bounds. `|x|<<1` describes a local regime, not a guaranteed tolerance. Coefficients, substitutions, domain, parameter size and requested accuracy matter. With fixed `r`, the binomial approximation is asymptotically valid; arbitrary large varying `r` needs additional control.
6. A derivative cannot be inferred from an arbitrary close-looking approximate line; the first-order remainder must be `o(x)` at zero. The listed analytic examples satisfy this. The polynomial limit also needs a remainder that remains vanishing after division by `x`.
7. The phrase "best-fit parabola" should mean the local Taylor polynomial matching the function's value, first derivative and second derivative at the basepoint. It is not a least-squares fit or a global optimum, and may have degree less than two. Quadratic approximation is not guaranteed to improve every numerical evaluation away from the basepoint.
8. The relativity formula is treated as the stipulated special-relativistic model. A careful physical interpretation uses elapsed intervals for specified events, the moving clock's proper time `T`, and the other frame's coordinate interval `T'`, with `|v|<c`. A lone observer's wristwatch wording does not by itself define a distant timing protocol. The source itself mentions other approximations for GPS; this lecture formula alone is not a full satellite-clock model.
9. The GPS calibration claim and the historical/current claim about the best atomic clocks are empirical context, not verified by the mathematical source check. In particular, fractional precision and absolute elapsed-time error must not be conflated. Do not present the atomic-clock sentence as a newly checked current fact.
10. Discarding a term is a choice of retained order and acceptable error, not a claim that the term is literally zero. Here every omitted contribution can be tracked through the smooth factor expansions.

## Handoff state

The complete newly published PROF package, current pin and full baseline paths are awaited. Baseline read scope at this moment is zero. The finalized prompts are also awaited. No proposed or finalized exercise solutions have been inspected. After the prompts arrive, I will solve those exact prompts and record their hashes/calculations before accessing teaching, figures, hints or solutions. The source calculations in this record are preparatory source checks, not a substitute for that later independent prompt-solving step.

Supporting records: `source-calculation-checks.json`, `original-full-text-from-pdf.txt`, `source-read-ledger.json`, and `SOURCE_PREPARATION_SHA256SUMS` in this directory.
