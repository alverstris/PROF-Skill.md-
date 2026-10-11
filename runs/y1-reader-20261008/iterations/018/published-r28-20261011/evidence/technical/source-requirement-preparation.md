# D018 clean-r28 — independent source and requirement preparation

This record was prepared after prompt-only independent calculations and before reading the frozen teaching. It is a source/requirement preparation record, not a teaching verdict. No source-audit files, previous runs/history, author working text, or sibling reviewer output were inspected.

## Verified identities and actual scope

- Original source: `inputs/source/lec20.pdf`, SHA256 `711e84263db3b675c39d18aa1951a55a4f026783732924324b6578913360c990`. All five literal page text extractions and all five original-page PNG renderings were read/visually inspected in page order, including both figures, all equations, and the final footnote. The PDF cover is page 1; printed lecture pages 1–4 are PDF pages 2–5.
- Operative PROF: `inputs/prof/SKILL.md`, version `2026-10-11-r28`, SHA256 `5d58064ef37d3c9ec8d6a3180a3b70b4324ccf722c079aba5f21730590fd2bdc`. Entire SKILL read. An initial clipped output was supplemented with untruncated ranges 1–69, 70–140, and 141–162.
- Complete local package manifest: `inputs/prof-package-manifest.json` lists canonical current main `91fc297103befb64925817dbeddbbe2c0e267601`; all 36 listed file SHA256 values were recomputed with no mismatches. This independently verifies local package bytes against that supplied manifest, not a fresh remote GitHub fetch. No GitHub writes occurred.
- Audit-relevant references read completely: `references/execution-protocol.md`, `references/domain-patterns.md`, `references/sasis.md`, `references/state-tool.md`, `references/sasis/student-role.txt`, `references/sasis/student-testing-contract.txt`, `references/sasis/profile-manifest.json`, and `references/sasis/rewrite-guide.md`. The profile/rewrite-guide concatenation was reread without clipping where initial combined output had truncated it. No method change is being proposed in this preparation phase, so research-rationale/history files were not required or inspected.
- Baseline: `inputs/student-baseline.txt`, SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5` verified. Selected operational coverage only: complete lines 1–229, 345–417, and 435–447, plus scoped search hits for prerequisite location. This is not a claim to have read the full four-subject baseline. Author and fresh SASIS reader carry their distinct full-baseline obligations.
- Phase 2 freeze manifest was received and read only after source/PROF work began. No teaching content had been read when this preparation record was written.

## Source map and independent mathematical observations

### PDF page 1: cover

MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006. The source is a lecture-note PDF; the cover establishes course/term identity. It does not identify an author on the inspected cover.

### PDF page 2 / printed page 1: FTC directions and accumulation

Course convention is explicit: FTC1 is endpoint evaluation using an antiderivative; FTC2 differentiates a fixed-base accumulation integral. This settles the numbering without a student convention question. FTC1 assumes continuity and `F'=f`; FTC2 states `F(x)=integral_a^x f(t)dt` and continuity implies `F'=f`.

The source motivates integral-defined antiderivatives with `exp(-x^2)` and lists further integrands `x^(1/2)exp(-x^2)`, `sin(x)/x`, `sin(x^2)`, and `cos(x^2)`. The real square-root example requires a nonnegative input domain; `sin(x)/x` is undefined at zero unless extended there. A teaching version should retain the purpose and appropriate scope without asserting that lack of a familiar formula means nonexistence.

The geometric proof interprets `Delta F` as a narrow strip and uses `Delta F approx Delta x f(x)`. Continuity must turn that approximation into a limit argument. The nonnegative diagram cannot by itself justify every signed integrand or negative increment; oriented integrals and the corresponding average-value argument provide the bridge.

### PDF page 3 / printed page 2: strip figure, quotient proof, FTC1 deduction

Figure 1 shows a positive increasing integrand, accumulated region from `a` to `x`, and added strip from `x` to `x+Delta x`. Text derives `[F(x+h)-F(x)]/h=(1/h)integral_x^(x+h) f(t)dt`, whose shrinking interval average approaches `f(x)` under continuity. For negative `h`, both orientation and denominator reverse; it remains an average over the ordered interval.

For FTC1, define `G(x)=integral_a^x f(t)dt`; FTC2 gives `G'=f`, so `(F-G)'=0`. The Mean Value Theorem licenses constant difference on an interval, and `G(a)=0` yields endpoint evaluation. Any needed MVT statement must be available to the reader before this reliance.

The final remark contains a source inconsistency: it announces `f(x)=sin x` but constructs `G(x)=integral_0^x cos t dt=sin x`. The coherent example uses `f(x)=cos x`.

### PDF page 4 / printed page 3: source typo continuation, erf, Li, prime model

At the top, `F(x)=sin x+21` and `F'(x)=cos x` are correct, but the displayed integral incorrectly uses `sin x` while giving endpoint difference `sin b-sin a`. Correcting the integrand to `cos x` repairs the intended constant-cancellation example. Differentiation independently distinguishes the error; this is not merely a notation preference.

The error function definition is `erf(x)=(2/sqrt(pi)) integral_0^x exp(-t^2)dt`, with limit 1 as real `x` tends to positive infinity. Figure 2 is an odd increasing S-shaped curve passing through zero and flattening at positive and negative extremes. The source figure omits numeric axis markings; the analytic definition, symmetry, derivative, and limit can support a clearer reexpression. The derivative is positive everywhere but tends to zero in both tails; no elementary primitive is needed to differentiate the accumulation.

The lecture's `Li(x)=integral_2^x dt/ln t` is a fixed-base convention, safely defined on `x>1`. Its relation to prime counting is a model/asymptotic motivation, not an exact count or finite-error certificate. Differences `Li(B)-Li(A)` give the lecture's interval estimate.

The source says “200-digit” but integrates from `10^200` to `10^201`: that interval represents 201-digit integers except for its endpoint convention. Exactly 200 decimal digits require `10^199 <= n < 10^200`. Its endpoint logarithms are approximately 460 and 462 for the written 201-digit interval. Prime-density statements should remain approximations. The cryptographic story does not establish security from the number of available primes alone.

### PDF page 5 / printed page 4: prime rectangle, Fresnel, Bessel, logarithm preview

The source writes `ln t approx 500 for 200 <= t <= 10^201`; the lower bound `200` is a printed error for `10^200` in that written example. On `[10^200,10^201]`, replacing the denominator by 500 gives `(10^201-10^200)/500 = 1.8*10^198`. That is order `10^198`, but nearest one-significant-figure rounding is `2*10^198`, not `1*10^198`. The footnote correctly states `integral_a^b c dx=c(b-a)` and explains the rectangle width/height.

Fresnel definitions are the lecture's unscaled convention: `C(x)=integral_0^x cos(t^2)dt`, `S(x)=integral_0^x sin(t^2)dt`. Hence `C'(x)=cos(x^2)` and `S'(x)=sin(x^2)` by FTC2. These are conventionally rescaled from NIST's common `pi t^2/2` definitions, not mathematical errors.

The printed Bessel representation uses `1/(2pi)` times the integral from 0 to pi. Standard `J_0` uses `1/pi` for those limits. The zero-input check gives 1/2 for the source formula and 1 for the standard normalization. The variable `x` is inside an integrand whose integration variable is theta and whose limits are fixed: FTC2's simple moving-upper-limit rule does not directly differentiate this parameter integral.

The lecture ends by previewing `L(x)=integral_1^x dt/t`. On positive real `x`, FTC2 gives `L'=1/x`, with `L(1)=0`; this is `ln x` and fits the baseline derivative/evaluation rules. A proof from first principles beyond this preview belongs to the next lecture unless required for the current route.

## Primary-source verification of niche claims

NIST Digital Library of Mathematical Functions was independently opened with the web retrieval tool. The relevant formula passages, not just snippets, were inspected:

- `https://dlmf.nist.gov/10.9.E1`: equation 10.9.1 states `J_0(z)=(1/pi) integral_0^pi cos(z sin(theta)) dtheta`, also the cosine-angle version. Retrieval `turn74view0`, line 51. Confirms the normalization correction; the zero-input check is an independent deduction.
- `https://dlmf.nist.gov/7.2.E1`: equation 7.2.1 is the erf definition above. `https://dlmf.nist.gov/7.2.E2` supplies its complementary-tail identity; equation 7.2.4 supplies its limit 1 along the positive real axis. Retrieval `turn78view0`, lines 45–118.
- `https://dlmf.nist.gov/7.2.E7` and `.E8`: NIST's Fresnel integrals use `cos(pi t^2/2)` and `sin(pi t^2/2)`. Retrieved formula passages `turn75view1` line 181 and `turn75view2` line 197, also `turn78view0`. The lecture's different scaling should be preserved or explicitly mapped. Substitution `u=sqrt(2/pi)*t` gives lecture `C(x)=sqrt(pi/2)*C_NIST(sqrt(2/pi)*x)` and similarly for `S`.

No current cryptographic security guidance or prime-count table was researched or asserted. The review can assess whether the teaching refrains from unsupported security claims without needing to replace the lecture with a cryptography lesson.

## Baseline availability relevant to the upcoming review

- Lines 26–42: signed arithmetic, units, logical implication, counterexamples, deduction, model/approximation distinction.
- Lines 46–72: algebra, modulus, functions, domains, composition, graphs and transformations.
- Lines 101–132: trigonometric symmetry and identities, radians, exponentials/logarithms and their domains/laws.
- Lines 136–174: derivative as a two-sided difference-quotient limit, first-principles differentiation, derivative rules, chain rule, monotonicity and curvature.
- Lines 176–203: antiderivatives, FTC evaluation under suitable continuity, rectangle-sum interpretation, standard primitives, substitution, integration by parts, signed definite integral and geometric area distinction.
- Lines 211–227: numerical methods and endpoint rectangle bounds for nonnegative monotone functions.
- FM28, line 411: improper integrals as separate endpoint limits; no cancellation across a divergent singularity.
- FM30, line 415: interval average `integral_a^b f/(b-a)` with `a<b`.
- FM42–FM44, lines 441–445: density normalization and probabilities, and the normal density formula. These can support an erf probability interpretation and Gaussian normalization through an explicit substitution.

The inspected baseline supplies substantial familiar calculus and algebra, so those need not be retaught indiscriminately. It does not provide a usable explicit meaning of continuity in the inspected calculus passages, nor a stated Mean Value Theorem there. If relied on, the teaching must supply those consequential local bridges, or the reviewer must locate an actual additional baseline passage before accepting availability. Search hits alone do not grant an unstated theorem.

## Applicable PROF checks for Phase 2

- T1: new integral-defined function, continuity, FTC hypotheses, special-function/model status and parameter roles must be meaningful before use. In particular r28 requires a usable test/recognition rule for a new consequential condition, tied to its object and first application.
- T2: fixed base, moving endpoint, dummy variable, accumulation value versus derivative, composition and two moving limits; construct and read exact expressions, including figures and all help.
- T3: additivity/reversal, shrinking-average limit, MVT constant difference, substitutions/scaling, chain-rule factors, approximations and source corrections must have correct warrants and conditions.
- T4: representative connected worked reasoning for the newly taught procedures; no independent untaught demand buried in examples.
- T5: early supported practice and meaningful changed application are default obligations for this lesson; changed numbers alone are insufficient.
- T6: all five retained prompts need purpose and response criteria that distinguish correct reasoning from a lucky number; labels must not reveal a method choice if method selection is the target.
- T7: every prompt needs useful matched hint and complete reasoned solution. Hints must supply an intermediate state/narrowed decision. Anticipated errors must not be represented as observed learner errors.
- T8: later recall/application opportunity must distinguish retrieval from changed-setting application; no universal optimal interval claim.
- T9: use known baseline operations compactly, teach genuine local novelty; figures/representations must be mapped where their relationship supports an inference.
- T10: independently verify substantive claims, full worked answers, source mistakes, approximations and important edge cases; do not infer truth from citation presence.
- T11: actual GitHub markup/typography and figure usability need destination checks; protected inline math, fenced math, strict `\\lt ` and `\\gt ` inside protected math. No bold/italic prose or heading syntax. Hints and solutions must be grouped separately with usable navigation. This reviewer will inspect exact PNG files but cannot substitute that for the separate live-destination review.
- T12: whole-document and source coverage, revision binding, truthful limits; distinguish scientific correctness, teaching accessibility, original SASIS evidence, semantic state evidence, and rendered destination evidence.

The state helper only checks mechanical presence/freshness; no independent semantic pass follows from `MECHANICALLY_READY`. The source map and every T1–T12 claim require actual teaching witnesses after the freeze. During this self-iteration cycle, any verified material defect is addressed through PROF-only repair, publication, and whole fresh generation; frozen teaching must remain unchanged.
