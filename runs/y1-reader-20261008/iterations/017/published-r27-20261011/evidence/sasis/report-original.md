# SASIS original report — d017-clean-r27

Frozen teaching: *First fundamental theorem of calculus*, MIT 18.01 Lecture 19 teaching document. This original report was written before receiving author feedback. It evaluates the supplied document, not a student or a held-out test.

**Finding:** no established substantive teaching gap, consequential ambiguity, or blocked mathematical conclusion was found in this reading. The definitions, conditions, examples, representations, questions, hints and solutions have accessible reconstruction routes from the complete supplied baseline and premises introduced at their positions in the teaching. This is a bounded finding, not proof that no latent error exists.

## Access, admission and limits

The complete baseline was read before the teaching: Mathematics logical lines 1–665, Further Mathematics 666–825, Physics 826–1389, and Chemistry 1390–2561 (boundary blank lines included). The actual returned ranges cover all 247,840 bytes continuously. All 536 teaching lines, 25,372 bytes, were read; both exact linked SVGs were rendered and visually inspected. Every text retrieval returned without truncation. The JSON read log records individual actual line and byte ranges, rendering recovery and hash checks.

Locators below use **B** for the baseline and **T** for teaching. Logical line numbers come from Python `bytes.splitlines(keepends=True)`, which respects the source's mixture of CR and LF. Byte intervals in the log are zero-based, half-open. Qualification titles are identifiers, not premises; the operational content was actually read.

All four supplied content hashes matched their expected values on admission and remained unchanged after reading:

| Artifact | Bytes | SHA256 |
|---|---:|---|
| student-baseline.txt | 247840 | `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5` |
| teaching.md | 25372 | `0317f26777f5285616be96713d79e1731818fea76d40954f3e21be2c6dbcb7b5` |
| signed-sine.svg | 34432 | `091bcfe31b315a1cb00a3d4ecc17bb8adfcb31bebdb3b07d8287fe72d9a81c63` |
| interval-addition.svg | 26014 | `e6f98867fc64fc626b01c47c7864f357ac40621fe907c6f4ee3486c5594bea33` |

The published student-role instruction was read completely first. No other subject-content files, source links, author history, research, personal context, other-agent messages or prior reports were read. No browsing occurred. No input was modified. Only the report, log and permitted figure-rendering evidence were written under this SASIS evidence directory.

This was **instruction-confined retrieval**, not technical isolation: tools could in principle access other files, and pretraining was not erased or disabled. The report relies on displayed premises and demonstrated connections, not a claim that latent knowledge is technically unavailable.

The initial text pass used bounded blocks; figure visuals were inspected after blocks 1–150 and 151–300, so those returned blocks contained prose after each figure link. To remove this ordering limitation from the substantive review, a complete second teaching pass was read in exact display order: T1–135, Figure 1, T136–172, Figure 2, T173–536. The log preserves both passes; it does not misdescribe the first as one-element-at-a-time first exposure. Later hints or solutions were not used as missing premises for the initial exercise demands.

CairoSVG imports failed in both Python runtimes. Inkscape then rendered both exact SVGs successfully; a non-fatal GtkRecentManager warning did not obscure their output. There is no remaining unread figure. The Markdown source and its mathematical notation were read directly; rendering of the entire document in a particular delivery application was not tested. External claims about the MIT source and its page allocation remain unverified, because the source PDF is outside the permitted input set.

## Operational premises actually used

The complete four-subject packet was read, though this lesson chiefly depends on the following explicit portions. Unused chemistry or advanced mathematics content was not substituted for a missing connection.

| Baseline locator | Available premise and role |
|---|---|
| B36–56, B72–104 | Signed arithmetic, algebra, domains, intervals, implication, inequalities, modulus, functions and composition; these supply sign checking and meaningful equation transformations. |
| B136, B182–190 | Finite sum notation; sine/cosine coordinates, signs, exact values, symmetry, periodicity and radians; these support accumulation notation and the sine figures. |
| B240–248 | Exponential/logarithm meanings, positivity and monotonicity, including the exponential's derivative; these support the exponential bounds. |
| B256–308 | Derivative as local rate, power/trigonometric/exponential rules, constants and sums, product/chain rules; these support every antiderivative and substitution check. |
| B312–316 | Derivative signs and increasing/decreasing behaviour; these support the auxiliary function used to establish the linear exponential lower bound. |
| B336–386 | Antiderivative families, suitably continuous FTC endpoint evaluation, rectangle-sum limits, elementary antiderivatives, linearity, differential substitution with changed limits, signed integrals and area/distance splitting. |
| B434, B574, B588–604 | Rectangle-area interpretation, consistent units/directions, velocity versus speed, displacement versus distance, componentwise integration and initial conditions. |
| B723 (FM23), B899, B1001 | Explicit cancellation of neighbouring sum terms; graph-area units; instantaneous velocity and signed area. These corroborate the short accumulation explanation. |

The full baseline is an assumed competence inventory. Reading it does not measure an actual learner's mastery or retention.

## Chronological reconstruction witnesses

### Opening and Section 1 — T1–69

1. **Purpose, route and starting point (T1–9).** The promise is endpoint evaluation and applications, not a proof course. The stated prerequisites correspond to B256–386 and B574–604. Radians are declared before any trigonometric calculation. The exercise route distinguishes hints, complete solutions and later retrieval. No unsupported mathematical conclusion is demanded by this introduction.

2. **Objects and hypotheses (T14–24).** `F'=f` defines the antiderivative relation; a fixed-bound definite integral is a number, whereas `F+C` is a family. These meanings match B336. Continuity at an interior point and one-sided endpoint continuity are explicitly introduced, so a learner need not import a formal continuity definition. Polynomial, sine, cosine, exponential and nonzero-denominator quotient continuity are stated facts available for later checks. FTC1 is explicitly supplied as a governing theorem, with `a<b`, continuous `f`, continuous endpoint values of `F`, and `F'=f` inside. Its conclusion is therefore admitted as a premise, rather than inferred from the subsequent informal rate explanation. The local meaning of “FTC1” resolves the naming convention.

3. **Endpoint notation (T26–36).** The bracket and vertical bar both mean evaluate the whole antiderivative at the finishing input and subtract its starting value. T29–33 equate the notations explicitly. This supports constructing and interpreting the bracket, including subtraction of a negative value; no multiplication interpretation survives the explanation.

4. **Power examples and constant cancellation (T38–64).** B272 and B344 give `(x^3/3)'=x^2` and `(x^6/6)'=x^5`. T16 supplies polynomial continuity, so FTC gives `b^3/3-a^3/3` and `1/6`. Adding the same `C` to both endpoint values cancels by ordinary subtraction; different constants at the two endpoints are not licensed. The positive forward-integral plausibility check is already available from B386's signed-area interpretation; it does not need the later comparison section.

5. **Q1 at its position (T67–69).** Its three requirements are all available before the question: derivative of the added constant is zero (B292), polynomial continuity (T16), and finish-minus-start with cancellation (T26–64). The changed negative starting input requires only signed arithmetic, not a missing theorem or a later solution. This is a supported exercise demand.

### Section 2 — T71–153, including Figure 1

6. **Rate and accumulated change (T73–88).** Position `s`, velocity `v=s'`, direction and speed are defined locally and supported by B574–604. Substituting `f=v`, `F=s` in T21 yields the position difference under the stated continuous-velocity condition. Each sampled `v(t_i*) Delta t` is a short-interval rate-times-duration estimate; the star and equal widths are explained. B336 supplies the rectangle-sum limit and B256–264 the rate interpretation. Successive actual position differences cancel intermediate positions, so their sum is total displacement. This is an accessible interpretation of an already supplied theorem, not a purported rigorous proof requiring an untaught uniform-continuity theorem.

7. **Units, speed and distance (T90–102).** Multiplying metres/second by seconds gives metres, and B899 explicitly supports product-of-axis-units for graph areas. Speed is the nonnegative modulus (B100, B574); integrating it preserves each segment's size, while integrating signed velocity permits cancellation (B386). Thus a round trip may have zero displacement and positive distance. The odometer distinction and the restriction of above-minus-below wording to forward limits are meaningful and do not conflate area with an oriented integral.

8. **Sine calculations (T104–134).** B286, B354 supply the antiderivative `-cos x`; B182 supplies the sine signs and cosine values at 0, pi and 2pi. Endpoint subtraction gives `1-(-1)=2`, then `-1-1=-2`, and over the full cycle `-1-(-1)=0`. The nonnegative first hump makes its integral equal to its geometric area; the next hump has area 2 but signed contribution -2. No arbitrary symmetry or numerical integration assumption is needed.

9. **Figure 1 and caption (T136–138).** The exact rendered SVG shows `x (radians)` from 0 through pi/2, pi, 3pi/2 to 2pi, and vertical `sin x` with -1, 0 and 1. The curve, positive blue region and negative orange region agree with B182 and the preceding computations. Labels say “signed integral +2” and “signed integral -2”; they do not label a geometric area as negative. The caption's total integral 0 and total area 4 follow from the two already established contributions. All visible labels were legible.

10. **Worked motion split and Q2 (T140–153).** For `t-1`, the zero is 1; signs on the two intervals follow from B96. Differentiating `t^2/2-t` returns the velocity. Its endpoint values give signed changes -1/2 and +1/2. Adding actual displacements is justified by T88 even though the formal interval-addition section is still ahead; adding their magnitudes gives distance 1. Q2 changes slope and final time, but requires the same zero/sign/antiderivative/units sequence. The instruction to check signs, rather than split mechanically at every zero, handles a possible zero without reversal. Q2 is supported when first encountered.

### Section 3 — T155–212, including Figure 2

11. **Adjacent intervals and cancellation (T157–171).** `[a,c]` is split at the declared interior point `b`. The stated signed-accumulation sum has a concrete algebraic witness: `(F(b)-F(a))+(F(c)-F(b))=F(c)-F(a)`. The terms at `b` cancel regardless of the integrand's sign. This uses one common antiderivative on the whole interval, not unrelated choices. B336 and ordinary algebra suffice.

12. **Figure 2 and caption (T173–175).** The rendered SVG has axes `x` and `f(x)`, endpoint labels `a,b,c` in increasing order, a curve wholly above the axis, and two adjacent shaded contributions separated at `b`. No numerical formula or scale is implied. The caption assigns each region to its corresponding integral and explicitly limits the picture to a positive-curve illustration; the preceding cancellation, rather than that one picture, supplies the signed generalisation. Labels and region boundaries are legible.

13. **Reverse and equal endpoints (T177–195).** Reversal and zero-length values are expressly defined, then tied to `F(a)-F(b)=-(F(b)-F(a))`. The phrase lower/upper is clarified as written position, avoiding numerical sorting. For `2 to 1`, the same primitive gives `1/3-8/3=-7/3`. A positive function can consequently have a negative reversed integral. The resulting qualification of geometric-area language follows directly.

14. **Arbitrary endpoint order and Q3 (T197–212).** Cancellation of the common endpoint value still works in any order under the stated existence/whole-interval conditions. The out-of-order example adds `8/3` and `-7/3`, retaining `1/3`; the extra outward-and-back portion cancels. Q3 only needs rearrangement of interval addition and sign reversal, already taught. Neither a formula for `f` nor an assumption that it has one sign is required. A forward integral may be negative by T102, so the interpretive question is supported.

### Section 4 — T214–258

15. **Comparison (T216–222).** The domain is the whole forward interval and the hypothesis is pointwise `f<=g`. Each positive-width rectangle for `g-f` is nonnegative; its limit is nonnegative (B336 and elementary order of limits). B360 permits integrating a difference termwise, giving `integral g-integral f>=0`. This connects the hypothesis to the conclusion without requiring either original curve to lie above the axis. Testing only endpoint values would not supply the hypothesis, and the text says so.

16. **Reversed comparison (T224–228).** Applying the earlier reversal definition negates both numbers. B96 explicitly reverses an inequality on multiplication by a negative number, producing `integral_b^a f >= integral_b^a g`. There is no independent new rule silently assumed.

17. **Constant exponential bound (T230–240).** Increasing `e^x` and `e^0=1` give a pointwise lower curve 1 on `x>=0`; those exponential facts are available from B240 and the stated derivative properties. Comparison on `[0,1]` and the primitive `e^x` give `1<=e-1`, hence `e>=2`. The bound is not treated as equality.

18. **Linear exponential bound (T240–253).** The newly chosen `h=e^x-1-x` satisfies `h(0)=0` and `h'=e^x-1>=0` by the previous step. Derivative-sign monotonicity (B312) makes `h>=0` to the right of zero; this is exactly `1+x<=e^x`, rather than an unsupported tangent-line assertion. Integrating the new lower curve gives `3/2<=e-1`, hence `e>=5/2`. Since the linear curve is at least the constant and strictly higher inside this interval, the interpretation that it captures more area is accessible.

19. **Q4 at its position (T256–258).** The established inequality holds on the larger requested interval `[0,2]`. Its two antiderivatives, the comparison warrant and the reversal of an inequality are all present. Changing 1 to 2 introduces only endpoint arithmetic. No later hint is needed to justify the exercise's inference.

### Section 5 — T260–339

20. **Substitution from the chain rule (T262–270).** With the given `G'=g`, B304–308 directly supplies `(G(u(x)))'=g(u(x))u'(x)`. The whole product is therefore an antiderivative match. `du=u' dx` is explained as notation recording the derivative factor, not a free replacement of variable names. The text states continuous `u'` and continuous `g` over an interval containing all reached values, including their endpoint interpretation. These are supplied rule conditions, not unstated regularity assumptions.

21. **New endpoint order (T272–284).** FTC applied to the composition gives `G(u(x2))-G(u(x1))`; FTC in the new variable yields exactly the same difference. Thus new bounds are the images of start and finish, with their order preserved. This endpoint argument does not divide by `u'`, presume invertibility, or need the inner function to increase. The instruction to change all of the integrand/differential and either change bounds or return completely to the original variable prevents mixing unlike inputs.

22. **Composite polynomial example (T286–310).** `u=x^3+2` has `du=3x^2 dx`, so the old factor is `du/3`; the endpoints become 3 and 10. Power integration contributes `1/5`, giving the displayed primitive `u^5/15` and difference `(10^5-3^5)/15`. The chain derivative of `(x^3+2)^5/15` returns the original integrand, checking both factors. Continuity follows from the stated polynomial facts. Expansion is also licensed by baseline algebra and termwise integration; it is not required to invent a new method.

23. **Decreasing substitution (T312–327).** For `u=2-x`, `du=-dx` while endpoints separately map 0 to 2 and 1 to 1. This gives `-integral_2^1 u^2 du`, then `-(1/3-8/3)=7/3`. Reordering to increasing limits introduces a second minus by T180. The two sign sources are distinguished rather than silently cancelled. A positive forward result is consistent with the original squared integrand.

24. **Q5 at its position (T330–339).** Differentiating `1+x^2` produces `2x`; only A visibly contains the whole needed `x dx`. Earlier factor matching and changed-bound examples therefore support both the evaluation demand and the explanation why B does not immediately become a constant multiple of `integral u^3 du`. The question carefully does not assert B is impossible to integrate, nor require an inverse substitution involving division at x=0.

### Section 6 and all hints — T341–383

25. **Later retrieval and mixed task (T344–350).** The timing is explicitly optional and no optimal-schedule claim is made. Q6's recalled theorem refers to T16–24, and its reopened application combines already supported polynomial integration, factor sign analysis (B96), the T102/T148 area distinction, interval splitting, orientation and optional substitution. Expansion gives only two powers, so an efficient route is available without help. This review checks the demand; it does not simulate a next-day memory test or report personal recall.

26. **Hints Q1–Q3 (T355–368).** Hint Q1 points to the derivative check and fully parenthesised subtraction, preserving both constants until cancellation. Hint Q2 identifies the zero/sign process and supplies the primitive whose derivative is the stated velocity; converting a negative signed segment to distance follows T92–100. Hint Q3's `X+10=7` is precisely the already taught interval decomposition, with reversal left to endpoint comparison. These are valid reductions of the existing tasks, not new hidden laws.

27. **Hints Q4–Q6 (T370–383).** Q4's brackets use the correct antiderivatives and original bounds; negating both values uses B96. Q5's `du=2x dx` preserves the whole differential factor and directs endpoint substitution. Q6 connects theorem conditions, candidate zeros, expansion or inner derivative recognition, and signed pieces before area. A candidate zero is not incorrectly equated with a reversal. All hints remain valid at their later positions and are linked back to their intended questions.

### All complete solutions and closing scope — T385–536

28. **Solution Q1 (T389–405).** Polynomial continuity and derivative of the constant establish the hypotheses. The displayed subtraction `(8/3+7)-(-1/3+7)` cancels 7 and gives 3. The explanation identifies the negative-starting-value sign issue. It answers every original requirement and does not change the problem.

29. **Solution Q2 (T408–418).** The zero at 1 lies in `[0,3]` and the two signs show reversal. Evaluating `t^2-2t` gives -1 on the first segment and +4 on the second. Their signed sum 3 m agrees with whole-interval endpoint evaluation; their positive sizes sum to 5 m. The explanation why absolute final displacement loses backtracking follows the earlier motion model and is accessible.

30. **Solution Q3 (T421–441).** Subtracting the known tail from the whole integral gives `7-10=-3`. The other requests reverse the known bounds, hence -10 and -7. A net negative contribution says below-axis size exceeds above-axis size by 3; it does not imply `f<0` at every point. The solution keeps this distinction, so neither its value nor its interpretation depends on an invented graph.

31. **Solution Q4 (T444–470).** The established pointwise inequality covers `[0,2]` and both functions are continuous. The lower primitive evaluates to 4, the other to `e^2-1`, yielding `e^2>=5`. Reversal gives `-4>=1-e^2`, the same assertion after rearrangement. The solution explains the changed comparison direction and does not accidentally infer an upper bound.

32. **Solution Q5 (T473–491).** The factor `1/2`, new bounds 1 and 2 and primitive `u^4/8` yield `(16-1)/8=15/8`. The displayed derivative check reproduces `x(1+x^2)^3`; polynomial continuity covers the endpoints even though the inner derivative is zero at x=0. For B the absence of `x dx` blocks only that immediate simplification; replacing `dx` by `du/2` would falsely discard x. The explicitly available polynomial expansion alternative avoids the stronger false conclusion that B is unintegrable.

33. **Solution Q6 theorem and integral values (T494–509).** The recalled statement preserves continuity of f and F, the interior derivative relation, a<b, and finish-minus-start. Reversal/equal-endpoint conventions are distinguished from the original forward hypothesis. For the application, expanding gives `x^3-x`; differentiating `x^4/4-x^2/2` checks the primitive. Its values 0, -1/4 and 2 give I=2 and J=-2. All needed operations are already available.

34. **Solution Q6 area and alternative route (T511–529).** Factor signs show negativity only between 0 and 1 and positivity between 1 and 2; the root 0 is correctly treated as an endpoint. Subinterval differences are -1/4 and 9/4, so area is 5/2 while the signed integral is 2. Reversing limits does not alter the geometric region. Alternatively `u=x^2-1`, `du=2x dx` maps endpoints to -1 and 3 and gives `(9-1)/4=2`. The zero at u=0 corresponds to x=1, so even this method must retain the area split. This explicitly justifies the relationship between the two representations. The text does not infer actual recall from a correct worked calculation.

35. **Navigation and source/scope (T531–536).** The hints and solution anchors correspond to all six named questions; their textual separation makes their roles clear. The closing paragraph says which material is claimed to follow the lecture and which is added, and repeats that a formal FTC proof is not being offered. The mathematical lesson can be read without opening the link. Accuracy of the source attribution/page mapping is outside this permitted-input review; no missing mathematical step was filled from that link.

## Issues, alternatives and downstream status

**Established teaching defects:** none identified in the complete reading.

**Unresolved substantive concerns:** none identified that requires blocking one of the lesson's stated conclusions. This does not certify completeness of error discovery.

**Potential alternative readings checked and resolved by the document:** FTC numbering is locally declared; a definite integral is distinguished from an antiderivative family; brackets enclose the whole evaluated expression; lower/upper denotes notation position rather than number size; a negative integral can arise from either integrand sign or reversed orientation; total distance/area differs from magnitude of net change; comparison must hold throughout the interval; substitution needs the derivative factor and correctly mapped endpoints; B in Q5 fails only the proposed immediate simplification; roots must be sign checked before an area or motion split. None remains an ambiguity changing the intended result under the stated conditions.

**Conditional scope:** FTC is used under its supplied continuity and antiderivative hypotheses; the rate interpretation uses the given continuous signed-velocity model; comparison is first established for forward bounds then converted for reversed bounds; substitution uses the regularity conditions at T270. Conclusions outside those stated models are not granted. A proof of FTC, independent truth of all newly supplied mathematical facts, and verification against the source PDF are not outcomes of this reader review.

**Dependencies:** no unsupported connection was silently granted, so there is no blocked downstream branch to preserve. The provided answers are supported as explanations of these existing questions, not evidence from a separate assessment. No learner was graded, and no claim of human learning, retention or absence of every latent error is made.
