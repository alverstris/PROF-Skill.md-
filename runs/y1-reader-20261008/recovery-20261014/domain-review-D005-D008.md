Independent targeted technical review: D005–D008

At repository pin `a512149c36d829405c716f148838b3ddbf2c882a`, I confirmed one directional/domain failure in the currently accepted D005–D008 teaching: D008 states a strictly positive clock correction over a declared speed domain that includes zero. No additional failure was confirmed in the other reviewed claim groups.

This is an affected-success review for PROF r38 T10’s general directional/comparison claim domain check. It is not SASIS, fresh authoring, a source-completeness review, or an acceptance decision.

The pinned queue was fetched and parsed in memory rather than printed whole. Its blob is `9c3abcf20778a52b5aa54994cd56caf663850c45`, path `runs/y1-reader-20261008/queue.json`. A selected-session metadata output was too broad and incidentally exposed embedded historical/review-summary fields. No prior diagnosis, review, or evidence file was fetched, and those summaries were not used to derive the findings. Independence is therefore bounded by that incidental metadata exposure; this is not a clean blinded review.

The current identities selected by the queue are:

| Material | Accepted revision | Frozen commit |
|---|---|---|
| D005 | `v2` | `32c553f279ac1e5771ff05b78a9951cbff3fee38` |
| D006 | `r13-candidate1-v3` | `28825d27b93baef43a5751eacecac81fa46841bc` |
| D007 | `published-r29-20261011` | `4765d39aa399a0a1ff09223cae21b15ce6c7f720` |
| D008 | `published-r35-20261012` | `d1d087414376a6b2d8ac5368075a72a3cb60817a` |

I fetched and inspected the entire text of all eight files below at their frozen commits. D005 and D006 contain their complete hints and solutions within the main file. D007 and D008 use separate linked help files. Fetching each same path at the repository pin confirmed the same blob and exact returned text.

| Material/constituent | Exact repository path | Blob ID | UTF-8 text bytes inspected |
|---|---|---|---:|
| D005 main, H1–H5, S1–S5 | `runs/y1-reader-20261008/iterations/005/teaching-v2.md` | `d8c9a67266e79fec03b069fa3193354882fc3f8b` | 24,261 |
| D006 main, A1–A6 hints/solutions | `runs/y1-reader-20261008/iterations/006/regenerated-r13-candidate1/teaching-v3.md` | `568fd03397f022bf2725a22476d155d470d84788` | 28,777 |
| D007 main | `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/lesson.md` | `71c1cc93e58f03a1d2f84519398a062190a965db` | 19,817 |
| D007 hints | `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/hints.md` | `bee957570b6b869f703fd6a98f2429d210722520` | 2,361 |
| D007 solutions | `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/solutions.md` | `5b55ac240e578efe14e81dc71c3122e2815dd00a` | 6,309 |
| D008 main | `runs/y1-reader-20261008/iterations/008/published-r35-20261012/teaching/lesson.md` | `a22bb65a65b0057d08ef916f7949f246ccf1bd01` | 23,965 |
| D008 hints | `runs/y1-reader-20261008/iterations/008/published-r35-20261012/teaching/hints.md` | `a86fcac5b1ede1e84572f65ea03774a0e1970ae9` | 2,818 |
| D008 solutions | `runs/y1-reader-20261008/iterations/008/published-r35-20261012/teaching/solutions.md` | `21ed4997c27f5484bc140875d65bb761e76897b3` | 7,179 |

Total full text inspected: 115,487 UTF-8 bytes. This includes prose, displayed mathematics, prompts, all linked hints and complete solutions, captions/alt text present in the Markdown, and source/notation notes.

Confirmed failure D008-DC1

Immutable locator: [D008 frozen lesson, section 7, line 262](https://github.com/alverstris/PROF-Skill.md-/blob/d1d087414376a6b2d8ac5368075a72a3cb60817a/runs/y1-reader-20261008/iterations/008/published-r35-20261012/teaching/lesson.md#L262), blob `a22bb65a65b0057d08ef916f7949f246ccf1bd01`.

The lesson says “The correction is positive” and states that the ground-frame interval is longer than the onboard interval. The preceding time-dilation law explicitly declares `0 ≤ v < c` at line 240:

\[
T'=\frac{T}{\sqrt{1-v^2/c^2}}.
\]

The displayed first correction is \(Tv^2/(2c^2)\). For positive elapsed proper time \(T\), that expression is nonnegative over the declared domain; strict positivity requires \(v>0\).

Permitted discriminating witness: \(T=1\,\mathrm{s}\), \(c>0\), \(v=0\). Then

\[
z=0,\qquad T'=T=1\,\mathrm{s},\qquad T'-T=0.
\]

Both displayed approximations also produce zero correction at this witness. Thus neither the strict positivity nor the strict interval ordering holds at an explicitly permitted input. This is an equality-boundary failure, not an approximation-error issue. The exact law, the linear correction and the quadratic correction agree about the boundary.

The warranted domain statement is \(T'\ge T\) for \(T>0,\ 0\le v<c\), with equality at \(v=0\), and \(T'>T\) for \(T>0,\ 0<v<c\). The subsequent numerical example at positive speed remains consistent with the formulas.

Reviewed D005 claim groups

| Locators | Declared domain and sign/order warrant | Discriminating check and result |
|---|---|---|
| P04–P05, Q1/H1/S1 | Circle branches on `−1<x<1`; slope `−x/y` only for `y≠0`. The actual signed coordinate controls the slope. | At `(3/5,−4/5)`, slope is `+3/4`. At `x=0`, both branch slopes are zero. At `(±1,0)`, the differentiated equation prevents a finite slope. Conditions preserved. |
| P07–P08, P18; Q2/H2/S2 | Implicit division is conditional on branch differentiability and a nonzero coefficient. For the source cubic, `y≠0`; continuity of nonzero `h'(y)` supplies a local fixed sign and monotonic inverse. | For the source cubic, `y=∛2`, `x=−3y/2` gives zero coefficient but numerator `−y²≠0`: no finite derivative. At `y=−1`, `h'=-3`, inverse slope `−1/3`; at `y=1`, inverse slope is positive. No unsupported global sign asserted. |
| P10–P18; Q4/H4/S4 | Continuous strictly monotone function on an open interval; interior input; existing nonzero forward derivative. Increasing/decreasing order and reciprocal slope are tied to the same paired values. | `f(t)=−3t+11` gives `f(2)=5`, `g(5)=2`, `g'(5)=−1/3`. `f(t)=t³` at zero tests the excluded zero-forward-slope boundary. The reciprocal proof expressly excludes it. |
| P19–P22; Q3/H3/S3 | Rational-power derivation on positive inputs; positive root and nonzero divisor. Negative-input conventions and zero are handled separately. | Zero exponent on `x>0` gives derivative zero without invalid division. At zero, cube-root quotients correctly distinguish `x^(4/3)` with derivative zero from `x^(1/3)` with no finite derivative. |
| P23–P25; Q5/H5/S5 | Principal arctangent branch; `1+x²>0` for every real input. Positive derivative and flattening depend on `1/(1+x²)`. | At `x=−1,0,1`, slopes are `1/2,1,1/2`. Increasing `|x|` decreases the positive slope. The triangle argument is explicitly restricted to positive inputs; the identity supplies zero/negative inputs. |

No directional/comparison-domain failure was confirmed in these D005 groups.

Reviewed D006 claim groups

| Locators | Declared domain and sign/order warrant | Discriminating check and result |
|---|---|---|
| P007–P023, P049–P054 | Initial exponential comparisons use bases greater than one. Later `M(a)=ln a` covers `a>0`; strict convexity supplies the endpoint-tangent/secant ordering for the two plotted bases. | `M(2)=ln2≈0.693<1`; `M(4)=ln4≈1.386>1`. At `a=1`, derivative zero; at `a=1/2`, derivative negative. These boundaries are explicitly addressed. |
| P037–P047; A2 hint/solution | Logarithm inputs positive; `ln` increasing because derivative `1/x>0`. Composite derivative includes the entire inner derivative. | `ln(1)=0`; signs reverse across input one. For `ln(1+x²)`, derivative is negative at negative `x`, zero at zero and positive at positive `x`; no globally positive composite derivative is asserted. For `ln(5−2x)`, denominator stays positive exactly on `x<5/2`, so derivative is negative there. |
| P059–P077; A3 solution P157–P163 | Positive base/functions permit logarithmic differentiation. Varying base and exponent each contribute a term; no fixed slope sign is asserted for `x^x`. | At `x=e^(−1)`, `x^x(ln x+1)=0`, changing sign across that point. The text does not incorrectly call it globally increasing. A3 expressly notes that the missing exponent term vanishes at zero and can be hidden by that check. |
| P083–P097; A4 and A6 help/solutions | Positive sequence terms; logarithm derivative quotient at one; negative increments require positive logarithm input. Divergence conclusion for A6 uses positive integer `k` and an eventual lower bound. | A4 excludes `k=2`, where the base would be zero. For `k>2`, logarithm limit `−6` gives positive original limit `e^−6`. A6’s bracket eventually exceeds `1/2`, so `ln c_k>k/2→∞`; the inference is valid. |
| P102–P113; A5 hint/solution | Positive levels; relative rate `F'/F`; finite fraction uses starting level. Sign and magnitude comparisons use the stated growth/decay models. | Equal `−0.02` relative rates give different absolute losses. The same 50-point fall gives approximately `−16.67%` versus `−0.5%`. One-day decay is about `−1.9801%`, smaller in loss magnitude than the local `−2%`; growth gives about `+3.045%` versus instantaneous `+3%`. The distinctions are preserved. |

No directional/comparison-domain failure was confirmed in these D006 groups.

Reviewed D007 claim groups

| Locators | Declared domain and sign/order warrant | Discriminating check and result |
|---|---|---|
| Section 1; P1/H1/S1 | Hyperbolic definitions on all real inputs. Algebra determines the coefficient sign of the derivative; `cosh²−sinh²=1` plus positive `cosh` determines `cosh≥1`. | At zero, `cosh=1` and `q'(0)=0`. At `x=−ln2`, `sinh x=−3/4`, while `cosh x=5/4`. The phrase about positive hyperbolic sine is contextual coefficient-sign language; the displayed equation does not warrant or establish a globally positive slope. |
| Section 1 figure caption | Negating the parameter leaves `cosh` unchanged and reverses `sinh`; right hyperbola branch differs from the circle constraint. | Parameters `±ln2` yield `(5/4,±3/4)`; zero yields `(1,0)`. Equality and both signs satisfy the stated constraint. |
| Sections 2–3; P2/H2/S2 and P3/H3/S3 | Quotient operations retain original denominator exclusions; implicit slope division requires a nonzero coefficient. | For P2, `x=(2k+1)π` stays excluded after cancellation. At zero the derivative is `1/2`. P3’s coefficient at `(1,2)` is five, so the negative slope `−4/5` is licensed. |
| Section 4; P4/H4/S4 | Radians; derivative signs follow addition identities and given limits. Secant’s positive algebraic coefficient is distinct from the value of its derivative. | At `x=−π/6`, `sec'(x)=sin x/cos²x=−2/3`, consistent with the formula. The prose concerns the algebraic plus sign, not positive slope on every permitted interval. |
| Section 5; P6(a)/H6/S6 | Principal arcsine branch chooses positive cosine in the interior; endpoint function domain differs from finite-derivative domain. Arctangent denominator is positive for all real inputs. | At zero, arcsine slope is positive. Inputs `±1` and composite inputs `±1/2` have no finite derivative. Negative interior inputs still select positive cosine. Arctangent at zero and negative input remains finite and positive. |
| Sections 6–7; P5/H5/S5 and P6(b) | General real-power rule restricted to positive inputs; constant exponent distinguished from changing exponent. Nested expressions retain all changing factors. | Exponent zero gives derivative zero. P5 correctly identifies `x=1` as masking an omitted term and `x=e` as distinguishing it. The final nested exponential has derivative zero at zero; no global directional conclusion is inferred from that check. |

No directional/comparison-domain failure was confirmed in these D007 groups.

Reviewed D008 claim groups

| Locators | Declared domain and sign/order warrant | Discriminating check and result |
|---|---|---|
| Sections 1–2; E1/E6 help and solutions | Finite derivative at an interior base point unless one-sided use is specified; first-order error is small relative to displacement. Zero slope is allowed. | Cosine at zero yields constant tangent without claiming cosine is constant. `sqrt(x)` at zero has divergent right quotient and is correctly excluded from the finite-slope tangent construction. No monotonic error growth is claimed. |
| Sections 3–4; E2 help/solution | Products retain all terms through the chosen degree. Difference-quotient limits require controlled divided error. | Cancellation at zero and the omitted quadratic term are treated consistently. E2 independently computes derivative one; the limit is not inferred from an uncontrolled approximation sign. |
| Sections 5–6; E3 help/solution | Quadratic matching with continuous second derivative near the base; coefficient `f''/2`. Zero second derivative may leave the polynomial unchanged. | Sine’s second derivative at zero vanishes, so linear and quadratic polynomials coincide. Fixed powers with exponent zero or one have zero quadratic coefficient. Exact quadratics are explicitly returned exactly. |
| E4, especially complete solution | Smooth `H=e^x/sqrt(1+2x)` near zero, `x>−1/2`; zero linear coefficient and positive quadratic coefficient. | `H=1+x²+o(x²)` warrants `H>1` for sufficiently small nonzero inputs on both sides. At zero, equality holds. The solution explicitly excludes zero from the strict-increase statement. |
| Section 7 clock comparison | `0≤v<c`, positive elapsed time; exact factor `(1−z)^−1/2`. | Zero-speed witness contradicts the strict comparison, as documented in D008-DC1. Positive-speed numerical examples are consistent. |
| Section 7 error bound; E5 help/solution | Bound over `0≤z≤10^−4`; positive time multiplier; total omitted error rather than next term alone. | Maximum second derivative is approximately `0.750187533<1`. At zero the error bound is zero. For E5, time bound is `5×10^−6 s<10^−5 s`; quadratic correction is `3.75×10^−6 s`. The guarantee and next-term comparison are correctly distinguished. |
| Section 8; E6 solution | Effective substituted input controls small-input reasoning; adding a zero coefficient does not improve the polynomial. | `50×0.02=1`, so small raw `x` does not itself warrant a good exponential truncation. The solution identifies the substantial `1/2` next contribution. Sine’s quadratic label adds no term. |

A further contextual scope ambiguity remains in D008 section 8, line 302. Its categorical sentence about no approximation order making a local model uniformly reliable over an unlimited interval can be read too broadly: `f(x)=x²` on all real inputs has `Q=f` exactly, as section 5 itself explains. In context, the sentence can instead mean that approximation order alone supplies no general global-accuracy guarantee. I have therefore preserved this ambiguity without counting it as a second confirmed failure.

Limits of this report

All main/help text was inspected, but figures were not visually examined, original source packets were not independently reconstructed, and external provenance/engineering facts were not independently validated. No full baseline, learner chronology, destination rendering, navigation, SASIS, or acceptance audit was performed. These findings establish only the stated targeted text-domain results. No GitHub edits, shell commands, Windows-computer operations, automations, or teaching creation were performed.