# D018 clean-r28 — independent technical, source, and PROF review

Verdict: no verified material mathematical, source-coverage, or teaching-contract defect was found in the frozen generation. All five answers agree with the prior prompt-only independent calculations. The important original-source errors are handled correctly. This is a scoped independent author audit, not SASIS, human learning evidence, or a live GitHub rendering verdict. Global acceptance still requires the separate reader, destination, and revision-bound author-state checks.

## Inputs, independence, and actual reading

The complete frozen `output/teaching.md` was read in order, lines 1–180 and 181–360, including every exercise, hint, complete solution, caption, and final source statement. Both exact linked PNG figures were opened and visually inspected in full at 1428 by 781 pixels, including the canvas edges and axis/annotation text. The teaching has 360 lines and 27,621 UTF-8 bytes.

The following hashes were independently recomputed and match `work/freeze-manifest.json`:

| Artifact | SHA256 |
| --- | --- |
| `output/teaching.md` | `4970a5ae04a73cca02eb62a20de8b5eab8d225c6b9ceb22eee44ec6a6408873c` |
| `output/figures/accumulation-strip.png` | `e3ba29224f4401a89eda0f676860bde1af6d9c17c837bae113de4aa293516c85` |
| `output/figures/error-function.png` | `c03ca91e3ee117d68df1bffd7b29aa4fa18bffa47c23e7e2fc15b360d5ee7899` |

Before seeing any proposed answer or teaching, I independently solved the finalized prompt set and saved `evidence/technical/independent-calculations.md` (SHA256 `5e695dab0ae1e8c9be695a50747448a48b66229277e496c0a284ac24ece5a078`). Its only input was `work/prompts-only.md`, SHA256 `bfd16842bf9e8eb3ed3e11edf20b07ff73737d8445aafef387cefb6401f82d86`. No mathematical findings were supplied to the author before the whole-document freeze.

Then, independently of the teaching, I read all five source-PDF page text extractions and all five original-page raster images, the full operative PROF root SKILL, and its audit-relevant execution/domain/SASIS/role/contract/profile/rewrite/state references. `evidence/technical/source-requirement-preparation.md` records that independent preparation and exact source/skill/baseline identities. All 36 local package manifest hashes were checked without mismatch. Canonical main was supplied as `91fc297103befb64925817dbeddbbe2c0e267601`; I verified the local package against its manifest, not by independently refetching GitHub.

Baseline coverage is selected, not whole: complete lines 1–229, 345–417, and 435–447 of the hash-verified full packet, plus targeted location searches. Those actual passages cover every baseline premise relied on in this technical audit: elementary reasoning, calculus, numerical bounds, improper integrals, averages, and the normal density. This does not replace the author's or fresh SASIS reader's required full-baseline read. No author audit files, prior-run diagnoses, source-audit records, or sibling reviewer outputs were read before this report. No frozen teaching or GitHub content was edited.

## Prompt equivalence and independent answer comparison

The finalized prompts and frozen teaching are not byte-identical representations: the finalized file uses plain-text integral descriptions, whereas teaching uses protected mathematical markup and links. They are mathematically and instructionally equivalent. Q1 changes “The response” to “Your response”; Q2 compresses the same one-sided-calculation requirement; Q5 adds the adjustable-spacing qualification. No quantity, hypothesis, requested justification, or answer target changed.

| Task and frozen locations | Independent result and comparison |
| --- | --- |
| Q1: prompt 48; hint 272; solution 295–303 | `A(1)=0`, `A'(0)=-1`, `A(0)=2/3`. The solution correctly reverses the limits before evaluation and distinguishes positive accumulated value from negative local rate. It checks the polynomial continuity condition. Exact agreement. |
| Q2: prompt 252; hint 275; solution 306–316 | `B(x)=x` for negative inputs and `3x` for nonnegative inputs; one-sided quotients 1 and 3. The solution concludes that the derivative does not exist, rather than merely noting an inapplicable theorem. It explains why the singleton endpoint value does not change area. Exact agreement. |
| Q3: prompt 255; hint 278; solution 319–326 | `H=E(x^2)-E(-x)`, `H'=2x exp(-x^4)+exp(-x^2)`, `H(0)=0`, `H'(0)=1`. Both substitutions and both lower-limit minus signs are correct. Exact agreement, including all real inputs. |
| Q4: prompt 258; hint 281; solution 329–335 | Integral from 100 to 1000, width 900, lower rectangle `900/ln1000`, upper `900/ln100`. Supplied rounded logs yield about 130.283729 and 195.439739; nearest-integer labels 130 and 195. The solution explicitly avoids claiming a rigorous upper bound of 195 from downward rounding and preserves the exact logarithmic inequalities. It separates model error from rectangle bounds. Exact agreement. |
| Q5: prompt 261; hint 284; solution 338–354 | `R'(2)=7`; `R(2)` is not determined. Both admissible continuous functions match endpoints, but their integrals are 2 and `2/3`, since the added quadratic integrates to `-4/3`. Recall and new inference are explicitly distinguished. Exact agreement. |

The computations are independently correct before presentation is assessed; that does not alone prove their teaching accessibility. Their prerequisite routes are audited below.

## Whole-route reconstruction and correctness witnesses

### Opening and section 1, lines 1–48

The route, target capability, exercise provenance, and separate help groups are explicit. Baseline lines 176–203 supply the familiar antiderivative/evaluation interpretation. Teaching lines 18–24 then distinguish the given integrand, fixed base, selected endpoint/input, and integration variable, including a concrete input and a variable-renaming equivalence. Line 33 constructs an accumulation from a desired rate and starting point, so the section teaches building as well as reading the representation.

Lines 26–33 establish signed area, zero-width integrals, and reversed orientation before Q1 uses them. Line 35 gives the meaning of continuity in nearby values, a tolerance-based recognition condition, familiar continuous function families, nonzero-denominator restrictions, and a piecewise-join test. It also explicitly introduces the finite-interval integrability fact. The FTC2 statement follows at 37–43 with interval and endpoint conditions. Thus continuity is not left as a name-only technical hypothesis.

The first worked case at 45 uses a polynomial integrand covered by line 35. Direct integration gives `F=x^2-2x`; derivative `2x-2`; value `F(1)=-1` with local rate zero. These numbers and their interpretation are correct. Q1 at 48 changes the base and tests opposite signs with reversed limits. Its route uses established evaluation, orientation, and endpoint-rate rules, rather than a missing later theorem.

### Section 2 and Figure 1, lines 50–85

Integral additivity cancels the shared old interval to produce the exact strip identity. The picture and caption distinguish its geometric suggestion from the needed limit proof. For positive `h`, the quotient is the interval average (also supplied by baseline FM30 at 415). The tolerance bounds on all heights imply corresponding rectangle-sum and integral-average bounds. Continuity makes the tolerance arbitrarily small as the interval shrinks, yielding the derivative limit.

The negative-increment case at 76–83 explicitly reverses both numerator orientation and denominator sign. Therefore the right-hand expression remains an average over a positive-length left interval, and the same bound proves the left limit. This avoids using a positive-area picture as a proof for negative increments or signed heights. The jump example at 85 is correct and properly cautions that a failed sufficient hypothesis does not by itself imply every possible derivative fails.

Figure 1 has a positive, increasing curve; labeled integration coordinate `t`; base `a`, current endpoint `x`, and moved endpoint `x+h`; the light accumulated region and distinct added strip; and a dashed comparison height `f(x)`. The arrow points to that height, not to the higher right endpoint. All labels and canvas-edge text are intact and legible in the exact PNG. The prose explicitly limits the positive-curve illustration and supplies the general signed argument.

### Section 3, lines 87–110

`P` denotes an arbitrary antiderivative and `G` a specified fixed-base accumulation. The derivative difference is zero under FTC2. The Mean Value Theorem is newly introduced with its continuity/differentiability conditions, finite-derivative meaning, equation, and secant/tangent interpretation; it is not silently borrowed from an unavailable earlier lecture. Applying it to any two endpoints gives the constant-difference conclusion. `G(a)=0` then identifies the constant and yields FTC1.

The concrete cosine example verifies the source correction by differentiation. `G=sin x`, `P=sin x+21` both differentiate to cosine; the endpoint difference cancels 21. A sine integrand would require `-cos x+k`. No original-source typo is copied as a true formula.

### Section 4 and Figure 2, lines 112–168

The Gaussian accumulation `E` is defined on all real inputs; continuity supplies existence, FTC2 its derivative, and coincident limits its initial value. Its listed companion examples have the necessary square-root and sine-quotient domain qualifications. The continuous extension of `sin t/t` at zero uses a limit explicitly present in baseline differentiation lines 138–142.

For erf, the constant factor, derivative positivity, even-integrand substitution, and odd result are correct. The horizontal-limit argument uses actual supplied normal-density knowledge (baseline FM42 and FM44 at 441–445), performs the `z=sqrt(2)t` substitution with its differential factor, obtains total Gaussian integral `sqrt(pi)`, and halves by symmetry. It does not falsely infer a finite horizontal limit merely from a vanishing derivative. Improper integrals are available in FM28, and their meaning is restated. The derivative and second derivative correctly explain increasing shape and the inflection at zero; the positive tail explains why a finite input cannot attain the limiting level.

Figure 2 is the corresponding odd increasing graph, with readable axes, origin, horizontal levels `-1` and `1`, and approach annotations. The curve visually merges with the asymptotes near finite plot edges because of finite raster resolution; the caption correctly states strict finite-input nonattainment, so this is ordinary plotting resolution rather than a misleading mathematical claim. No clipping or missing label was found in the exact image.

Fresnel definitions consistently use the lecture's unscaled integrands. Applying FTC2 produces cosine/sine evaluated at the endpoint; line 158 expressly distinguishes that operation from differentiating the resulting derivative. The course convention is disclosed before reliance, and no calculation silently imports the NIST normalization.

The Bessel integral distinguishes the input parameter from the angular integration variable and fixed bounds. It explicitly declines to apply the simple moving-endpoint formula to this different structure. At zero, the integrand is 1, giving the corrected standard value 1. The factor-of-two correction has primary-source support and a discriminating normalization check.

### Section 5, lines 170–217

The lecture's base-2 logarithmic integral is defined on `x>1`; continuity and its derivative are correctly qualified. The prime approximation is introduced as external number-theoretic information rather than derived from FTC2. The digit rule produces the corrected interval, and the source's 201-digit-versus-200-digit discrepancy is explained accurately.

The written-source interval has endpoint logarithms approximately 460.5170186 and 462.8196037, matching the teaching's 460.52 and 462.82. The coarse rectangle calculation is `1.8*10^198`, with one-significant-figure rounding to `2*10^198`; the 200-digit interval correspondingly yields `1.8*10^197` under the same deliberately coarse denominator. The printed lower-range typo is also explained.

For exact rectangle bounds, positivity and increasing logarithm imply decreasing reciprocal. Multiplying its bounding constant heights by the positive width gives the stated inequalities. Independent arithmetic gives the 200-digit coefficients 1.9543251686 and 1.9641458981 times `10^197`, consistent with line 217. The text distinguishes those integral inequalities from prime-count errors and does not infer cryptographic security from cardinality alone. That is a scope correction of the original motivation, not an unneeded security theory.

### Sections 6–7, lines 219–261

The fixed-base function `K`, endpoint function `g`, and composition `K(g(x))` make the chain rule explicit. The worked upper limit `x^2` gives `2x cos(x^4)`, with correct nested evaluation. Subtracting two fixed-base accumulations gives the two-endpoint formula; the stated continuity-domain and orientation conditions preserve it when the endpoints reverse. The example `integral_x^(2x)t dt=3x^2/2` confirms the derivative `3x` for positive and negative inputs, rather than checking a case that cannot distinguish the sign issue.

The logarithm preview has positive domain, derivative `1/x`, and initial value zero. Its constant-difference comparison to the baseline logarithm is licensed by section 3 and establishes the claimed identity. It clearly distinguishes this current identification from the next lecture's first-principles development.

Q2–Q4 then use conditions and representations already established. Q5 supplies a later closed-notes recall opportunity followed by a changed information-sufficiency problem. The proposed timing is explicitly adjustable; the document makes no claim that later retrieval happened or that a universal spacing optimum exists.

### Hints, solutions, and ending, lines 263–360

Hints are grouped separately from complete solutions, with distinct collapsed containers and bidirectional task/help links in the source. Q1's hint supplies an oriented integral; Q2 supplies negative/positive interval constructions and the quotient step; Q3 gives a fixed-base decomposition and warns of the double minus; Q4 gives the interval width and smaller height; Q5 gives a vanishing-endpoint perturbation construction. These advance an intermediate decision rather than merely restating a prompt.

Every full solution is present, matched, and mathematically correct as independently established above. Q5's quadratic perturbation is available from ordinary factorization and integration; no new theorem is hidden in the help. The only learner-error statement is labeled anticipated, not observed. The final source statement accurately describes retained conventions and explained source corrections.

## Complete source-portion correspondence

| Required original portion | Frozen teaching coverage |
| --- | --- |
| PDF p1: course/term identity and cover | Source statement, line 360. |
| PDF p2: FTC1, primitive notation, existence question, Gaussian and other new integrands, FTC2, geometric difference quotient | Lines 10–45, 53–85, 115–123. |
| PDF p3: Figure 1, interval average, FTC1 from FTC2/MVT, fixed accumulation versus arbitrary primitive, inconsistent trigonometric example | Figure 1 and lines 53–83, 90–110, including corrected cosine example. |
| PDF p4: continuation of constant-cancellation example, erf definition/limit/Figure 2, Li definition, prime-count motivation, large-digit setup and logs | Lines 110, 127–147 and Figure 2, 173–217. Digit and source-log issues are explained. |
| PDF p5: coarse rectangle estimate and footnote, security motivation, Fresnel pair and requested derivative, Bessel example, logarithm preview | Lines 191–217, 151–168, 249. Corrections preserve source meaning while avoiding false mathematics or unsupported security inference. |

All substantive source portions have a usable equivalent or an explicit correction. Neither figure is omitted by relying only on text extraction. No required source component was silently relabeled optional.

## T1–T12 disposition

These dispositions concern actual frozen learner-facing content and the independent checks performed here. They do not certify unseen author state, full SASIS admission, or the live destination.

| Duty | Disposition and substantive witness |
| --- | --- |
| T1 Meaning/first use | Content pass. Lines 24 and 33 establish integral roles and construction; 35 gives continuity's meaning/checks before FTC2 use; 96–102 introduce MVT and differentiability; 168 distinguishes a parameter integral; 181 labels the prime model as new information. |
| T2 Representation | Content pass. Reading and construction at 24/33; signed orientation at 26–33; figure-to-equation maps at 59–83 and 135–147; nested endpoint evaluation and two-limit decomposition at 222–244. |
| T3 Legitimacy/derivation | Content pass. Rectangle additivity, two-sided shrinking averages, MVT constant difference, Gaussian normalization substitution, source corrections, reciprocal inequalities, and both chain-rule factors each have their actual warrant and conditions. |
| T4 Connected worked reasoning | Content pass. Polynomial accumulation at 45; full proof at 53–83; constant-cancellation example at 110; erf properties and normalization at 127–147; prime rectangle at 191–217; upper/two-endpoint examples at 229–244. |
| T5 Application/handover | Content pass for the declared capability. Q1 is an early supported attempt after the first usable FTC2 result. Q2 changes continuity; Q3 changes both moving endpoints and sign; Q4 changes digit interval and requires a model/error distinction; Q5 changes what information is sufficient. These are not solely changed-number drills. |
| T6 Purposeful prompts | Content pass. Each prompt's requested justification identifies what distinguishes a defensible response. Q2's two-sided calculations prevent a hypothesis-name-only answer; Q3 requires every factor/sign; Q4 requires the integral/count distinction; Q5 requires an insufficiency argument. A previously described jump does not eliminate Q2's required explicit computation. |
| T7 Help/feedback | Content pass. Five matched useful hints and complete reasoned solutions. Exact hint, answer, and return-link locations are in the task table. Q1 labels the hypothetical wrong route anticipated. No observed mastery/error is fabricated. |
| T8 Retention/transfer | Content pass. Q5 at 261 separates later unaided theorem recall from subsequent changed application, and 338–354 models both parts. Timing is described as adjustable. |
| T9 Load/prior knowledge | Content pass. Familiar rules are used compactly; local novelty is explicitly bridged. Both figures are mapped to relevant inferences. The normal-density deduction uses an actually supplied baseline resource rather than opening an unnecessary probability course. No concrete obstruction from irrelevant expansion was found. |
| T10 Technical verification | Independent-review pass within this report's scope. All five answers were solved blind before comparison; source equations/figures checked against originals; specialty claims checked with primary NIST passages; numerical endpoint bounds independently recomputed; important sign, zero, domain and limiting cases inspected. Author's own saved verification record remains outside this audit. |
| T11 Usable output | Local source/figure/navigation checks pass; live GitHub parsing, visible math, click behavior and destination styling remain for the separate destination reviewer. No ATX headings or bold/italic markers were found in the teaching; both exact figures are legible. See the narrow non-material formatting observation below. |
| T12 Honest acceptance | Content and this review's reporting pass. The document does not claim measured mastery/retention or a completed external rendering review. This report explicitly preserves the independent/partial-baseline/destination/state limits. Global project acceptance is not established by this report alone. |

No T5–T8 capability was declared inapplicable to evade its trigger. This review does not inspect or certify the author's formal applicability ledger; it evaluates that those duties are actually met in the teaching.

## Primary-source checks and local mechanical evidence

Primary pages actually opened and relevant formula passages read:

- NIST DLMF `https://dlmf.nist.gov/10.9.E1`, equation 10.9.1: standard Bessel factor `1/pi` for the 0-to-pi interval (`turn74view0`, line 51).
- NIST DLMF `https://dlmf.nist.gov/7.2`, equations 7.2.1–7.2.4 and 7.2.7–7.2.8: erf normalization/limit and the differently scaled Fresnel convention (`turn78view0`, lines 45–118 and 181–197).
- NIST DLMF `https://dlmf.nist.gov/27.12`, equation 27.12.5 and the linked logarithmic-integral definition: the prime approximation is an external asymptotic relation (`turn81view0`, lines 95–114).
- NIST DLMF `https://dlmf.nist.gov/6.2.E8`, equation 6.2.8: the common principal-value convention (`turn81view1`, lines 144–158). On the teaching's real domain above 1, subtracting the value at 2 gives its fixed-base convention; the derivative and interval differences agree. This is an explicit reviewer deduction, not a claim that the learner must know principal-value integration.

Mechanical inspection found 24 unique declared anchors and no unmatched local target, exactly Q1–Q5 with corresponding five hints and five solutions, and two properly balanced details containers. Local source inspection is not a live click test. Input/output hashes bind this report to the frozen generation, but do not prove semantic quality by themselves.

Narrow non-material formatting observation: at lines 173, 189, 249, 252 (twice), 306, and 329, protected inline `\\lt` or `\\gt` directly precedes a digit rather than the literal following space mentioned in the r28 formatting instruction. A digit already terminates a TeX control word; no literal HTML-sign collision or mathematical ambiguity is introduced. I therefore do not classify this as a verified material teaching/rendering failure or propose a fresh generation on that basis. The separate destination check should establish actual operand/operator preservation. No generated content was changed to normalize this spelling.

## Issue register and acceptance boundary

- Verified material teaching/math/source failures: none found in this independent audit.
- Unresolved substantive mathematical concerns: none.
- Original-source defects: sine/cosine inconsistency, digit-count mismatch, printed logarithm-range lower endpoint, coarse-estimate rounding, Bessel normalization, and overstrong security inference; all handled correctly in this frozen teaching.
- Provisional/non-material observation: the seven comparison-command spacing instances above; no demonstrated semantic or visual loss.
- Unverified here: live GitHub rendering and help-click behavior; the full fresh SASIS read/admission; the author's complete baseline-read and source/state records; current remote package publication identity beyond the supplied locally verified manifest; any human learning outcome.

No PROF repair is justified by this report's material findings. Preserve the frozen generation unchanged and combine this report with the independent reader, destination evidence, and author-state audit before making a global acceptance claim. If another review supplies a concrete concern, compare it to the exact passages and legitimate routes rather than treating either agreement or disagreement alone as proof.
