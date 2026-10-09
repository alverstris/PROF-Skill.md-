# Original SASIS reading report: teaching-r15-v2

## Finding and scope

Within the two supplied subject inputs, I found no established missing, invalid or materially ambiguous connection that blocks the document's required conclusions. The tangent and quadratic constructions, scaled-error arguments, examples, and A1–A4 are supported at their points of use. This is an evaluation of the teaching and its available prerequisites, not evidence of a person's learning, retention or examination performance, and not a claim to have discovered every possible error.

This original report was prepared before receiving author feedback. The evaluation used the supplied operating instructions and the two frozen subject inputs only. No source lecture, external citation, repository instruction, other report, other agent's content or other subject input was consulted. This is instruction-only isolation; I make no claim about erased pretraining or unavailable technical memory controls.

## Input binding and actual access

Both objects were retrieved using read-only git show at commit a6b7aaaf2ded04bb6b0c2da2528234d36ca2f6d4 in the specified repository. The returned bytes were decoded with bytes.decode('utf-8'), without universal-newline conversion.

| Input | Immutable repository path | Actual bytes / raw UTF-8 characters | Verified SHA-256 |
|---|---|---:|---|
| Complete operational baseline | references/sasis/ocr-baseline-20261007/student-baseline.txt | 247840 / 246945 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 |
| Complete teaching | runs/y1-reader-20261008/iterations/008/revised-r15-v2/teaching-r15-v2.md | 27868 / 27819 | b6e93b986e2a77763c556a4b5fc5cb42f43269742d0af9bd06021d7aa3ad7668 |

I read all 18 consecutive baseline chunks before reading either teaching chunk. The baseline reading included H240, all selected H245 Pure Core Y540/Y541 and Statistics Y542/Mechanics Y543 material, H556, and H432, including their resource and scope sections. I then read the teaching from its opening anchor through P068 and its final return links, covering P001–P068, A1–A4, all hints and complete solutions, every displayed equation, the prose descriptions of all four visual relationships, and the source/scope statements. The single teaching file was the complete supplied teaching artifact.

Ranges below are zero-based, half-open raw decoded-character ranges. Each chunk contains at most 14500 characters. Every retrieval completed with exit code zero and without output truncation. IDs are the actual exec_command tool-output chunk IDs.

| Read order | Input | Raw range | Tool-output ID |
|---:|---|---|---|
| 1 | Baseline | [0, 14475) | fc2b80 |
| 2 | Baseline | [14475, 28847) | 612b9f |
| 3 | Baseline | [28847, 43077) | 7e3a90 |
| 4 | Baseline | [43077, 57266) | 3b7864 |
| 5 | Baseline | [57266, 71643) | 51c9ae |
| 6 | Baseline | [71643, 85718) | c15805 |
| 7 | Baseline | [85718, 100166) | edb08d |
| 8 | Baseline | [100166, 114481) | 40a918 |
| 9 | Baseline | [114481, 128426) | 5e87bb |
| 10 | Baseline | [128426, 142727) | 036bb9 |
| 11 | Baseline | [142727, 157024) | fe2760 |
| 12 | Baseline | [157024, 171522) | a05568 |
| 13 | Baseline | [171522, 185622) | 020ce2 |
| 14 | Baseline | [185622, 199958) | 548702 |
| 15 | Baseline | [199958, 214244) | 2d09c3 |
| 16 | Baseline | [214244, 228382) | 91ca61 |
| 17 | Baseline | [228382, 242518) | b0f378 |
| 18 | Baseline | [242518, 246945) | 1b0087 |
| 19 | Teaching | [0, 14239) | 6e2301 |
| 20 | Teaching | [14239, 27819) | 238f2d |

The companion reader-access-r15-v2-original.json records the same access sequence and binds this report by its SHA-256.

## Baseline locators used in the reconstruction

These are operational passages actually read, not grants inferred from course names.

- H240, “Prior arithmetic, geometry and mathematical language,” “Proof and mathematical work,” and “Algebra, functions and coordinate geometry,” baseline [0, 14475): domains, equations versus approximations/identities, signed displacement, powers, polynomial algebra, functions and coordinates.
- H240, “Trigonometry,” “Exponentials and logarithms,” and “Differentiation and its applications,” [14475, 28847): radian trigonometry and values at zero; exponential/logarithmic values and domains; derivative as a difference-quotient limit; power, chain and product rules; tangent equations; second derivatives and concavity.
- H240, “Integration and elementary differential equations,” [14475, 28847): continuous-integrand fundamental theorem, antiderivatives, signed definite integrals and area/rectangle-sum interpretation. These support the two integrations in P026.
- H245 FM27, [57266, 71643): actual Maclaurin coefficient construction and the stated exponential, sine, cosine, logarithmic and binomial expansions, with their conditions. FM27 does not grant a general remainder theorem.
- H245 FM57 and FM71, respectively [71643, 85718) and [85718, 100166): dimensional consistency and the need to identify an actual bridge when combining subjects.
- H556, “Reference data” and “1. Quantities, mathematics, measurement and evidence,” [85718, 100166): speed of light, day/second conversion, units, ratios, scientific notation, precision and numerical reasonableness.
- H556, “2. Forces, motion, energy and materials,” [100166, 114481): velocity, acceleration, and constant-velocity motion; “8. What may be assumed,” [142727, 157024), explicitly does not grant relativistic spacetime theory. P040 therefore has to introduce its physical relation, and does.
- The entire remaining baseline was read. No Chemistry rule or unstated Further Mathematics university formalism was needed to supply a missing mathematical or relativistic premise.

## Chronological reconstruction witnesses

### P001–P008: route, base point, tangent and first-order error

P001–P003 identify the route and prerequisites. The listed algebra, derivatives, integration, radians and standard expansions are actually available at the baseline locators above. The promise to address degree and error is a preview; no early task requires an as-yet-untaught quadratic remainder theorem.

P004–P005 make a fixed input a and the signed displacement h=x−a distinct, with a=x₀. Thus x=a+h is a change of coordinate, not a different function or an assumption that h is positive.

P006 follows the baseline point-slope equation: the point supplies f(a), the gradient supplies f′(a), and their line is L(x)=f(a)+f′(a)(x−a). A zero gradient gives a constant model. The equality defines L; the approximation compares it with f. P007's prose figure supplies both axes, contact point, tangent and label translation. Its source label uses a for slope; the explicit translation prevents that a from being substituted for the base point. Shared height and slope imply contact agreement, not equality at other inputs or monotone error growth.

P008 supplies the consequential first error connection. Subtracting f′(a) from the baseline derivative quotient defines ε₁(h); differentiability gives ε₁(h)→0. Multiplication by nonzero h and rearrangement give the exact formula f(a+h)=f(a)+f′(a)h+hε₁(h). Consequently division of the error by h is licensed, while a numerical error at one fixed h is not bounded. No external error theorem is needed.

### P009–P015: first example, early A1, and all five linear models

P009–P010 use the baseline ln domain and derivative: at a=1, height 0 and slope 1 yield L(x)=x−1, and h=0.02 yields 0.02 as an estimate. Writing u=x−1 gives ln(1+u), with the same nearby inputs represented relative to 1. The domain x>0 remains explicit.

At P011, A1 is already available without the later hint or solution: the power rule gives (√x)′=1/(2√x), so at 4 the height and slope are 2 and 1/4; displacement 0.04 gives the tangent value 2.01. P005–P008 supply the base/displacement distinction and approximate-versus-exact meaning. Asking why 4 is useful calls only for its nearby location and simple square root, not a new optimisation theorem.

P012–P014 construct, rather than merely list, four zero-base models. The respective height/slope pairs are (0,1), (1,0), (1,1), and (0,1) for sin x, cos x, eˣ, and ln(1+x). These yield x, 1, 1+x, and x. The paired sine/cosine sketch descriptions agree with these points and slopes. A horizontal cosine tangent does not imply constant cosine.

P015 adds (1+x)ʳ using a fixed real exponent and positive base. The height is 1 and slope r, giving 1+rx. The local condition and the meaning of |x|≪1 are stated without turning that notation into a numerical accuracy guarantee. A large coefficient can magnify a correction; nothing here grants uniform accuracy over every r.

### P016–P023: substitution, reciprocal, multiplication and a limit

P016–P017 rewrite the original function as the product e⁻²ˣ(1+x)⁻¹ᐟ² on x>−1. Substitution into the prior templates gives 1−2x and 1−x/2. The substituted exponential argument also tends to zero, and the original denominator stays positive.

P018's two-stage reciprocal route is locally intelligible: the square-root denominator and its linear model both approach 1, and algebraic division therefore does not amplify a first-order vanishing error through a zero denominator. This is a local justification, not a general permission to invert approximations near denominator zeros. P017 already supplies the direct exponent route, and P020 checks the final model independently.

P019 multiplies the model polynomials exactly: 1−5x/2+x². Keeping degrees at most one gives 1−5x/2. The warning about the visible x² is warranted because each factor has omitted its own square term; that cross term alone cannot identify the full quadratic coefficient.

P020 removes any dependence on an informal multiplication convention: the product rule at zero gives f(0)=1 and f′(0)=−2−1/2=−5/2. P008 then supplies the first-order scaled remainder for this actual f. The lesson explicitly declines to infer a derivative from an arbitrary unsupported numerical approximation.

P021–P022 identify the displayed limit as [F(x)−F(0)]/x for F(x)=(1+2x)¹⁰. The power and chain rules give F′(0)=20, so the derivative definition supplies the limit. P023's second route gives F(x)=1+20x+xε₁(x); subtraction and division leave 20+ε₁(x). The result follows because the retained error tends to zero after the actual division.

### P024–P029: quadratic construction and its error argument

P024–P025 introduce Q(a+h)=A+Bh+Ch². Its value and first two derivatives at h=0 are A, B and 2C; matching them sets C=f″(a)/2. The h derivative agrees with the x derivative since x=a+h has derivative one. An exact quadratic is returned exactly. “Best-fit” is expressly confined to local derivative matching, avoiding a conflicting least-squares interpretation.

P026 teaches the new error fact and its reason. For the difference E between f(a+h) and this Q, matching gives E(0)=E′(0)=0 and E″(h)=f″(a+h)−f″(a). Continuity makes |E″|≤η sufficiently near zero. The baseline fundamental theorem, together with the stated bound on integral magnitude, gives |E′(t)|≤η|t| and then |E(h)|≤ηh²/2. Reversing integration endpoints handles negative h as well. Dividing by h² and allowing η to be arbitrarily small establishes the claimed vanishing scaled error. The integral-bound explanation is an accessible extension of signed area/integration, not an extensive untaught theorem. A general Taylor remainder rule was not silently imported from FM27.

P027 preserves the difference between local scaled error and fixed-input accuracy. A zero quadratic coefficient is permitted: sin″(0)=0 leaves the model x.

P028–P029 give cosine's triple (1,0,−1), hence 1−x²/2. The described downward parabola has the stated contact height, horizontal tangent and second derivative. Its distant behaviour is explicitly distinguished from cosine's oscillation. At 0.1 the polynomial values 1 and 0.995 can be compared with the supplied 0.9950041653; the quadratic's smaller discrepancy is evident by arithmetic. This comparison is an instance, not a universal accuracy claim.

### P030–P034: five quadratic models and A2 at its actual position

P030–P031 apply P025 to the triples (0,1,0), (1,0,−1), and (1,1,1), producing x, 1−x²/2 and 1+x+x²/2.

P032 differentiates ln(1+x) twice to obtain the triple (0,1,−1), and thus x−x²/2 with x>−1. At 0.02, its value 0.0198 differs less from the supplied 0.0198026273 than 0.02 does. The surrounding near-zero scope remains in force; the stated real domain is not a claim of numerical accuracy everywhere on that domain.

P033's second power derivative is r(r−1)(1+x)ʳ⁻²; matching gives r(r−1)x²/2. Substitution of kx must square k as well. The functions have continuous second derivatives on appropriate neighbourhoods of zero, so P026 actually applies.

At P034, A2 has the required support before its hint or solution: the whole input 2x in P032 yields 2x−2x². The remainder is (2x)²ε₂(2x), whose quotient by x² is 4ε₂(2x)→0. Subtraction removes 2x and the limit is −2. With only first-order information, the leftover error divided by x² need not tend to zero. The stated domain x>−1/2 contains a two-sided neighbourhood of zero.

### P035–P038: full quadratic product and derivative interpretation

P035–P036 use the inputs and exponent already identified: the factor models are 1−2x+2x² and 1−x/2+3x²/8. P037 collects all three square contributions: 2, 1, and 3/8, summing to 27/8. The linear coefficient remains −5/2. Higher polynomial degrees vanish after division by x² as x→0.

The remainder explanation also covers the omitted factor errors. If the original factors are U+r and W+s, with r/x²→0 and s/x²→0, their product differs from UW by r(W+s)+Us. Bounded factors/models make this difference divided by x² tend to zero. This reconstructs P037's stated multiplication rule using algebra and its explicit error premises.

P038 identifies f″(0)=27/4. For these differentiable factors, the independently displayed twice-applied product rule gives 4+2(−2)(−1/2)+3/4=27/4. Thus the coefficient interpretation is not resting on a bare approximate sign. Equivalently, P026's matched polynomial and P037's scaled-error polynomial must have the same coefficients: a nonzero difference in constant, linear or square coefficient cannot have quotient by x² tending to zero. This uniqueness argument is short algebra with the already supplied error condition.

### P039–P044: new physical premise and degree in the chosen variable

P039–P040 explicitly introduce a gravity-free constant-relative-speed clock model. The schematic's observer and motion arrow do not supply orbital geometry. T>0 is the onboard interval and T′ is the observer-frame interval for the same two events; the prime is a label. The formula T′=T/√(1−v²/c²), with 0≤v<c, is a new declared physical relation, not a deduction demanded from the baseline. The text also distinguishes event-time comparison from uncorrected signal-arrival timing. Its cited page is not needed to obtain the displayed premise or identify its quantities.

P041 divides by nonzero T and chooses q=(v/c)². Taking u=−q and r=−1/2 in the power model gives 1+q/2. The sign follows from the product of the two negative factors; for nonzero v the exact positive denominator is less than 1. Restoring T supplies time units. The approximation needs q small, not merely v<c.

P042 uses equal speed units before squaring: q=16/(9×10¹⁰)≈1.78×10⁻¹⁰. Its half is approximately 8.89×10⁻¹¹; multiplication by 86400 s gives 7.68×10⁻⁶ s. These are a dimensionless fraction and its corresponding time, respectively.

P043 introduces the separate empirical statement about real GPS using both motion and gravitational effects, while expressly preventing the gravity-free calculation from becoming a full orbital prediction. No gravitational correction formula or real-orbit numerical conclusion is required downstream.

P044 applies the same power model through degree two: the coefficient is 3/8 and (−q)²=q², giving 1+q/2+3q²/8. Since q²=(v/c)⁴, the two stated degrees are consistent. With P042's values the new ratio term is approximately 1.185×10⁻²⁰ and its one-day time approximately 1.024×10⁻¹⁵ s, supporting the displayed rounded numbers. Comparing added terms is explicitly separated from certifying a required accuracy or an instrument's capabilities.

### P045–P054: A3, method selection, later A4 and scope

At P045, A3 has the model, both polynomial forms, a reference ratio, a rounding precision and an absolute time-error threshold. q=10⁻⁴ gives ratios 1.00005 and 1.00005000375. Multiplication by 100 s gives the two time estimates; comparing each with 100.00500037503125 s separates errors of about 3.75×10⁻⁷ s and 3.125×10⁻¹¹ s. The first fails and the second meets the stated threshold. Even the reference's maximum rounding uncertainty, 5×10⁻¹⁵ s after scaling, cannot reverse either decision. The demand is supported before the help.

P046–P048 collect methods already used. Choosing degree in light of subsequent cancellation/division is supported by P023 and A2. Keeping every product contribution is supported by P037. The distinction between a limiting error and a fixed-input numerical bound follows from P008/P026 versus the supplied numerical comparisons. Agreement of two truncated models alone does not supply their unknown common error.

P049–P050 make the later timing and recall attempt optional study instructions, without making an empirical claim of optimal spacing or treating an imagined performance as evidence.

At P051, A4 changes both factor inputs but requires no new operation. P031/P033 give 1+2x+2x² and 1−x/2−x²/8; the linear coefficient is 3/2, and the square coefficient is 2−1−1/8=7/8. The factors are twice continuously differentiable near zero inside x<1. P025–P026 and the product argument make the derivative readings 3/2 and 7/4 legitimate; P038 has also taught the independent product-rule check. Subtracting 1+(3/2)x leaves 7x²/8 and a remainder vanishing after division by x², giving limit 7/8. All of this is available at the task position, without relying retrospectively on P067–P068.

P052–P054 distinguish added teaching/tasks from source material and explain the transition to hints and complete solutions. Their provenance and full-source-coverage assertions are not independently checkable from the two allowed inputs; that limitation does not remove any premise used in the examples or tasks.

### P055–P060: hints in their actual group

P055 is the hints heading. P056 directs A1 back to the base height, power derivative and displacement already taught. P057 points A2 to whole-input substitution and the already established quadratic scaled error. P058 keeps A3's ratios distinct from times and requires absolute-error comparison before coarse rounding. P059 identifies A4's two substituted inputs, the three square contributions and the factor of two for a second derivative. Each hint uses material already encountered and addresses a consequential step. P060 clearly marks the end of partial help and the start of complete solutions. The task and return anchors in this single file have corresponding destinations.

### P061–P068: complete solutions

P061 marks the solution group.

P062's A1 solution uses slope 1/4 and displacement 0.04 to obtain L(4.04)=2.01. Squaring gives 4.0401>4.04; because both numbers are positive, this does show that 2.01 is too large. The square-root concavity remark is supported by differentiating again: f″(x)=−1/(4x³ᐟ²)<0. Its wrong-displacement discussion is explicitly hypothetical, not a claim about a reader's observed response.

P063 makes the rescaled A2 remainder explicit: δ(x)=4ε₂(2x)→0. The quotient is −2+δ(x). P064 explains the inadequacy of first-order information by observing that δ₁(x)=kx tends to zero for every fixed k while δ₁(x)/x=k. This is a valid illustration of the lost information, not a later premise needed to rescue an unsupported earlier task.

P065's A3 arithmetic gives 100.005 s and 100.005000375 s, the reference time 100.00500037503125 s, and absolute errors approximately 3.7503125×10⁻⁷ s and 3.125×10⁻¹¹ s. The 16-place ratio rounding contributes at most 5×10⁻¹⁵ s after multiplication. P066 correctly connects q² to (v/c)⁴ and limits the acceptability conclusion to the task's reference comparison and threshold.

P067 reconstructs A4's general formula and factor 1/2, then obtains both factor polynomials and all three square contributions. The negative square coefficient of √(1−x) follows from (1/2)(−1/2)/2, while the squared input has positive sign. The resulting coefficients 3/2 and 7/8 agree with derivative values 3/2 and 7/4 under the previously established matching conditions. P068 supplies the product remainder explicitly, so subtracting the constant and linear terms and dividing by x² gives the stated limit 7/8. Its final distinction between recalling a formula and applying it to a changed expression is an instruction about the task, not evidence of an actual learning outcome.

## Defects, concerns, ambiguities and limits

### Established defects

None established in the required teaching connections under these inputs. No dependent conclusion was left blocked by a missing mathematical or physical premise.

### Provisional concerns

No unresolved provisional content gap remains after the reconstructions above. In particular, I did not treat ordinary supported algebra, differentiation or arithmetic as missing teaching, and did not require the document to derive its newly introduced physical law from A-level physics.

The important alternative readings are explicitly resolved in the document: base-point a versus a source figure's slope a; displacement versus full input; equality versus approximation; constant linear and degenerate quadratic models; time-label prime versus differentiation; event times versus received signals; and degree in q versus degree in v/c. The positive-base domains and near-zero approximation scope also remain distinct. None leaves an unresolved course convention that changes a required answer.

### Input and verification limits

There was no missing, unreadable or truncated part of either required subject input. Hashes were used to bind the inputs, not as substitutes for reading.

The external MIT lecture, OpenStax and NIST pages were not opened. Accordingly, claims about exactly what the source lecture contained, its omitted time factor, its historical clock claim, and complete coverage of its examples and figures remain source-provenance assertions rather than independently verified comparisons. The internal teaching descriptions and calculations were evaluated in full.

The special-relativity relation and the GPS contextual statement were treated according to their declared status as new physical premises/context. Independent scientific validation of them is outside this two-input reading. No external relativity or GPS fact was supplied to repair a connection.

The representation check concerns the complete frozen Markdown and its mathematical/prose representations. No separate source-image or application-rendering inspection was performed. This does not leave an unexamined constituent of the supplied single-file teaching.
