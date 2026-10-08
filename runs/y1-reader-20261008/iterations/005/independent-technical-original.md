# D005 scoped independent technical review — original report

This is an independent technical review, not SASIS, a student trial, or an assessment of observed learning. It reviews the version of `teaching-v1.md` first read in this review, including P26's original “is not” wording and the missing TeX backslashes recorded below. It does not certify any later author repairs. No teaching file or pre-existing record was edited.

## Actual evidence read and scope

- Read `iterations/005/teaching-v1.md` completely, P01–P41, including every question, hint, and complete solution.
- Read all five supplied source text extractions: `lec5-p01.txt` (5 lines), `lec5-p02.txt` (125 lines), `lec5-p03.txt` (89 lines), `lec5-p04.txt` (58 lines), and `lec5-p05.txt` (34 lines). These correspond to the cover and printed lecture pages 1–4.
- Read the baseline's contiguous ranges 1–74, 99–174, 211–215, and 331–419. The repeated read of 136–174 recovered the end of a previously truncated combined output. Relevant substance includes function/inverse definitions and power conventions, radian trigonometry and principal inverse branches, derivative limits and rules, the derivative sign test, implicit differentiation, the continuous-function root property, Further Mathematics scope, and FM29's inverse-trigonometric derivatives. The 331–419 read also exposed adjacent mechanics, complex-number, matrix, and other Further Mathematics entries; they were not used to justify the lesson.
- Keyword searches across the baseline initially exposed scattered matches outside these contiguous ranges, including Physics/Chemistry matches, and their combined output was truncated. These are not represented as a full baseline read and did not supply premises for the technical findings.
- No other lesson, reader response, author record, or external source was inspected. No rendered source-PDF image was inspected: this review uses the supplied source text only. No external browsing or symbolic package was needed; the checks below are direct algebra and limit arguments.

## Supported issues requiring repair

### T01 — P26 asserts an inequality not entailed by its hypotheses

**Evidence.** P26 asks, “Explain why `g'(5)` is not `1/f'(5)`.” Its hypotheses only give a continuous strictly decreasing function on an open interval with `f(2)=5` and `f'(2)=-3`.

**Consequence.** Read literally, the prompt asks the learner to justify a false general assertion. Take `I=R` and `f(x)=11-3x`. All supplied hypotheses hold. Its inverse is `g(z)=(11-z)/3`; therefore `g'(5)=-1/3=1/f'(5)`. The correct point of the question is that the inverse derivative rule evaluates the forward derivative at `g(5)=2`, while the supplied information does not license replacing this point by 5. An accidental equality remains possible.

**Necessary repair.** Replace the requested inequality with an evaluation-rule question, for example: “Explain why the inverse derivative rule uses `1/f'(2)`, and why `1/f'(5)` is not justified by the supplied information.” P38 already explains the paired input correctly and observes that 5 need not be in `I`; it need not change its computed answer. A clarifying sentence there that accidental equality is possible would remove any remaining ambiguity, but fixing P26's demanded claim is the essential change.

**Independence limit.** The author flagged this possible issue in the review assignment before the read. The counterexample and consequence above were checked independently; the issue's initial discovery should not be attributed solely to this review.

### T02 — P07 has a literal `quad` in the displayed derivative

**Evidence.** The source line reads `y'=-\frac{y^2}{3y^2+2xy}quad(3y^2+2xy\ne0).` The intended spacing command lacks its backslash.

**Consequence.** In math rendering, `quad` is a sequence of letters rather than spacing, corrupting the visible boundary between the formula and its essential nonzero condition. The derivative calculation itself is correct.

**Necessary repair.** Change the literal `quad` at that location to `\quad`.

### T03 — P20 has two literal `qquad` strings in the power-rule derivation

**Evidence.** The displayed line begins `y^n=x^m,qquad ny^{n-1}y'=mx^{m-1},qquad`.

**Consequence.** Both transitions render extra mathematical letters, damaging a central multi-step calculation that the text explicitly says reproduces the lecture's exponent argument. The surrounding algebra is correct when these are read as intended separators.

**Necessary repair.** Restore both commands to `\qquad`.

### T04 — P23 has two literal `qquad` strings in the arctangent derivation

**Evidence.** The display begins `\tan y=x,qquad` and the next line ends `y'=1,qquad`.

**Consequence.** Extra mathematical letters appear between the defining equation, its differentiated equation, and the isolated derivative. This is a notation/rendering defect, not a wrong arctangent derivative.

**Necessary repair.** Restore both commands to `\qquad`.

## Existence, branch, domain, and division checks

- **P03–P05:** The draft distinguishes an implicit relation from a selected differentiable function. The two circle branches are explicit on `[-1,1]` and differentiable on `(-1,1)`. The chain-rule calculation gives `y'=-x/y` only for `y!=0`. At `(±1,0)` the finite-derivative equation is inconsistent; the separate radius/tangent geometry supports the vertical tangent claim. The baseline's circle geometry and known derivative rules support this route.
- **P07–P08 and P18:** Differentiating the lecture curve gives `(3y^2+2xy)y'=-y^2`. The curve excludes `y=0`. At a zero coefficient its nonzero right side forbids a finite derivative for a differentiable branch. The later existence argument does not assume what this division proved: solving for `x` gives `h(y)=-y-y^-2`, and substitution verifies `h'(y)=-1+2y^-3=-(3y^2+2xy)/y^2`. A nonzero continuous derivative keeps its sign locally, so the baseline derivative sign test supplies local strict monotonicity; the proved inverse result then supplies a differentiable branch. At `(0,-1)`, `h'(-1)=-3`, so `dy/dx=-1/3` and the tangent is `y+1=-x/3`.
- **P10–P17:** The one-to-one restriction, range, inverse, paired points, and domains of both inverse identities are consistent. P14 explicitly makes the chain-rule inference conditional on both derivatives existing. P15–P17 provide a separate sufficient existence argument: continuity and strict monotonicity on an open interval, an interior point, and a nonzero forward derivative. Bracketing works in both monotone directions; continuity supplies intermediate outputs, so the inverse input has a neighborhood and `u=g(z)` tends to `a`. For `z!=b`, both quotient denominators are nonzero by one-to-one correspondence; taking the reciprocal of a limit is legitimate because its limit is `f'(a)!=0`. The result `g'(z)=1/f'(g(z))` has the correct evaluation point. These are sufficient hypotheses for this treatment, not a claim to list the weakest possible theorem.
- **P19–P21:** With `x>0`, all integer `m` and positive integer `n` are accommodated, including `m=0`. The positive root is an inverse of `t^n` on positive inputs, where `nt^(n-1)>0`; composition with `x^m` supplies differentiability before the chain-rule step. Since `y>0`, division is valid. The exponent reduction gives `m/n-1`. Negative-base remarks correctly require reduction and an odd denominator. The `x^(5/3)` zero-point quotient is `(cube_root(h))^2` and tends to zero from both sides. The constant-function treatment avoids the undefined expression `0*x^-1` at zero. The draft does not claim its positive-domain proof establishes all negative-input or endpoint cases.
- **P23–P25:** The principal tangent restriction has nonzero derivative and covers the real inverse inputs. Its inverse derivative is justified before the conditional implicit calculation. The acute triangle is restricted to positive `x`. The identity `1+tan^2 y=sec^2 y` then establishes the derivative for every real `x`, and `cos y>0` on the principal range justifies the unsquared square-root sign. No division by zero occurs.

These are bounded checks of specific mathematical arguments. They are not an all-PASS verdict on the lesson, and they do not remove T01–T04.

## Source-to-draft content correspondence

| Supplied source component | Draft location | Correspondence checked |
| --- | --- | --- |
| Cover: MIT OCW, 18.01, Fall 2006, terms/citation pointer | P41 | Attribution and terms pointer retained. |
| Printed p1: known integer power rule and rational-power extension using `y^n=x^m` | P19–P21 | Integer premise, implicit differentiation, quotient, substituted powers, exponent subtraction, and final `m/n*x^(m/n-1)` are present. Domain/existence discussion is added. The source's final intermediate `m/n-n/n` is consolidated into the draft's equivalent `m/n-1`; no mathematical step is lost. T03 affects notation. |
| Printed p1: explicit upper semicircle calculation | P04 | Both branch formulas and the upper-branch chain-rule calculation ending at `-x/y` are present. |
| Printed p2: implicit circle calculation | P03–P05 | The chain-rule factor, differentiated constant, collection, and quotient are present; endpoint discussion is added. |
| Printed p2: `y^3+xy^2+1=0` | P07–P08, P18 | Original curve, all product/chain contributions, collected coefficient, and final derivative are retained. Local inverse justification is added. T02 affects notation. |
| Printed p2: inverse definition and chain-rule reciprocal derivative | P10, P14–P17 | Reverse assignment and reciprocal derivative are retained, with the paired values and sufficient differentiability hypotheses made explicit. |
| Printed p3: arctangent implicit derivative and triangle simplification | P23–P25 | Defining tangent equation, `sec^2 y*y'=1`, `cos^2(arctan x)`, side-length relationships, Pythagoras, cosine ratio, and squared expression are retained. T04 affects notation. |
| Printed p4: final arctangent derivative | P25 | `1/(1+x^2)` is retained and its real domain is explicitly justified. |
| Printed p4: coordinate renaming for inverse graph, composition identities, and reflection | P10–P13 | `g(x)=y` equivalent to `x=f(y)`, both inverse identities, composition notation, paired points, and reflection in `y=x` are all represented. |

No missing substantive algebraic result was found in this text-to-text correspondence. This does **not** verify the source figures' exact visual layout, colors, or dashed-line placement: P12's black/blue descriptions and P24's page-orientation description cannot be certified from the source text extraction alone. The triangle's algebraic side roles and the inverse graph's mathematical reflection are checkable from the extracted labels and equations and are consistent. The added questions are correctly described as generated applications, not original MIT questions.

## Questions, hints, and complete solutions

| Task and help | Independently checked result and conditions |
| --- | --- |
| Q1 P06; H1 P29; S1 P35 | Point lies on circle. `m=-(3/5)/(-4/5)=3/4`; tangent `y+4/5=(3/4)(x-3/5)`. Lower branch and forbidden division at `(±1,0)` are handled. Hint and solution address each requested component. |
| Q2 P09; H2 P30; S2 P36 | For the changed mixed term `xy`, `(3y^2+x)y'=-y`; divisor is `3y^2+x`. At `(0,-1)`, slope `1/3`, tangent `y+1=x/3`. The supplied differentiable-branch assumption is retained rather than inferred from the calculation. |
| Q3 P22; H3 P31; S3 P37 | On positive inputs `u'=(4/3)x^(1/3)` and `v'=(1/3)x^(-2/3)`. At zero the quotients are respectively `r` and `1/r^2`, where `r=cube_root(h)`. Thus `u'(0)=0` and `v` has no finite derivative at zero. Both-sided reasoning and the exclusion of infinity as a real derivative are correct. |
| Q4 P26; H4 P32; S4 P38 | `g(5)=2`, `g'(5)=-1/3`, points `(2,5)` and `(5,2)`, and identity domains `I` and `J` are correct. The hint selects the right evaluation point. T01 remains a defect of the original prompt despite the correct intended solution. |
| Q5 P27; H5 P33; S5 P39–P40 | Part (a) retrieves the lesson's sufficient hypotheses. For part (b), `F(1)=1+pi/4`, `F'(1)=3/2`, so inverse output is 1 and slope `2/3`; tangent `y-1=(2/3)(z-1-pi/4)`. The question supplies monotonicity, continuity, and range, and the solution checks the remaining nonzero condition. No closed-form inverse is needed. |

The anchor IDs and displayed return routes in the source Markdown match the intended question/hint/solution labels. This was a text inspection, not a browser interaction test. The review establishes correctness of the listed intended results, not successful student performance, delayed retention, transfer, or a guarantee that every wording choice is optimally teachable.

## Review limits and disposition

The supported repairs are T01–T04. The report is original evidence of the pre-repair wording observed here; it should remain unchanged if the author later fixes the teaching. Any post-repair claim must identify a separate verification step. Figure fidelity beyond extracted text, rendering after the TeX repairs, learner readability, accessibility, empirical teaching effectiveness, and any lesson outside D005 remain outside this review.

## Addendum: separately requested amendment spot check

After the original report above was written, the author requested a current-version spot check. The original findings above are retained. This addendum records a distinct read of current teaching lines 35–60, 80–145, 148–158, and 162–197. The current file returned SHA-256 `2279a7267fdd143a3266ffb03097abe65b7194af3cbbb31dfd3433406c6068e0` at this check. This is a hash of the current amended teaching, not of the original version.

- **P26 / T01:** The amended question asks why the rule uses `f'(2)` “rather than requiring `f'(5)`.” This no longer asserts that the two reciprocal numerical values must differ. It resolves the counterexample-based defect identified above.
- **P07 / T02, P20 / T03, P23 / T04:** All five specific missing spacing-command backslashes are present in the current source. This resolves the observed source-token defects; rendered-page inspection remains outside this spot check.
- **P16:** The new sentence explicitly applies the baseline's continuous sign-change root fact to `f(t)-z` at the bracket endpoints. For an intermediate output `z`, the endpoint differences have opposite signs in either monotone direction, and the resulting root gives `f(t)=z`. This is a valid deduction from the baseline passage at line 213 and makes the availability of intermediate outputs explicit.
- **P17:** The new reciprocal-limit explanation uses `1/A-1/L=(L-A)/(AL)` and `|A|>=|L|/2` sufficiently near the nonzero limit. Then `|AL|>=|L|^2/2`, so the difference has magnitude at most `2|L-A|/|L|^2`, tending to zero. The added argument is mathematically sound and makes a formerly compressed limit step explicit without assuming a new inverse-function theorem.

No additional mathematical repair is indicated by these amendment spot checks. This narrow statement is not a fresh full-file re-review or an all-PASS verdict, and it does not extend the original review's figure, rendering, or learner-performance limits.
