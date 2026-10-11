# Original SASIS sequential document review — D008 published r30

Frozen revision: published-r30-20261011. This report was written once after the complete reading and before receiving author feedback. It evaluates the teaching document, not a learner’s performance, score, retention or mastery.

## Finding

I found no established teaching defect or unresolved required inferential connection in this reading. The chronological witnesses below give the actual routes from the supplied baseline and already encountered teaching, including domains, remainder conditions, diagrams, exercise demands and complete solutions. This is a bounded review finding, not a claim to have discovered every possible latent error.

The strongest conclusions depend on the declared four-subject competence assumption, particularly the actual calculus rules, integration interpretation and FM27 expansions supplied in the baseline. The clock calculations additionally depend on the physical law expressly introduced in section F. The local error statements do not certify arbitrary finite-input accuracy; the document explains that limitation and supplies numerical references for the exercises that require tolerance comparisons.

## Actual access and scope

- Operating instruction read fully: `verified-prof/references/sasis/student-role.txt` (5,607 bytes, 44 LF-delimited lines).
- The complete operational baseline was read before any teaching content: `inputs/student-baseline.txt`, 247,840 bytes, SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`.
- Actual contiguous baseline byte ranges were [0,23842), [23842,47600), [47600,71126), [71126,95001), [95001,118601), [118601,142316), [142316,166261), [166261,190181), [190181,214097), [214097,237716), [237716,247840). Their LF line ranges were respectively 1–177, 178–334, 335–438, 439–540, 541–655, 656–757, 758–896, 897–1058, 1059–1207, 1208–1334, 1335–1377.
- After the baseline, `reviews/reader-route.json` supplied exact routing and `freeze-manifest.json` supplied identity information. All seven teaching files matched their frozen byte counts and SHA256 values. Full-file byte reads used for hashing did not display later subject text.
- The teaching was exposed in the exact 23-step routed order. All four Markdown files were read completely (lesson: 18,555 bytes/274 LF lines; practice: 4,539/64; hints: 2,467/54; solutions: 7,860/163). Each exact full PNG was visually inspected at its listed position: tangent, sine-cosine, clock-model.
- No tool output reported truncation; every displayed chunk was complete. No truncation recovery or inaccessible passage was required. The images were viewed as full-image displays, without cropping or substitution.
- Byte coordinates are zero-based, half-open raw UTF-8 byte ranges. Line coordinates are one-based physical lines separated by LF bytes, not by every CR character. The baseline includes CR/CRLF variation; there are 1,377 LF delimiters and a final LF. Teaching files use LF with final LF. A displayed empty line created by splitting at a chunk’s terminal LF is a formatting artifact, not exposure of following text.
- A final computational locator check of the already read baseline confirmed relevant heading line numbers and line counts. No subject source, original PDF, author material, other report/history, browser or external resource was accessed. External links in the teaching were not followed. Only routine progress messages went to the coordinator; no subject help was requested or received.
- These are instruction-confined retrieval and reasoning records. They do not assert technical isolation or erased pretraining. The accompanying `access-record.json` records the paths, ranges, access modes and hashes.

## Chronological reconstruction witnesses

### 1. lesson.md LF lines 1–37; bytes [0,2842)

The introduced basepoint and h turn the baseline tangent equation into L(x0+h)=f(x0)+f′(x0)h. Subtracting f′(x0) from the defining difference quotient gives R1(h)/h→0, so local relative-to-displacement error follows without a finite-input bound. The baseline ln derivative/domain and ln1=0 give L=x−1 and ln1.02≈0.02.

Available premises: Baseline Mathematics “Differentiation and its applications” LF 136–174; “Exponentials and logarithms” LF 128–134; “Algebra, functions and coordinate geometry” LF 44–80.

### 2. figures/tangent.png, full exact PNG at lesson line 37

Axes x and y, solid ln(x), dashed x−1 and the annotated contact (1,0) are legible. Both values are zero at x=1; slope agreement is the earlier f′(1)=1. The visible line lies above the concave logarithm and separation shrinks toward the contact. No numerical error claim is inferred from the drawing.

Available premises: Earlier lesson A; baseline derivative/concavity and graph reading.

### 3. lesson.md LF 38–50; bytes [2842,3662)

The figure caption matches inspected curves. Substituting x=1+u changes x>0 into u>−1 and x−1 into u, so the zero-basepoint form refers to the displacement, not the original x. This supplies the proposed transition to an independently chosen nonzero basepoint.

Available premises: Earlier lesson A and baseline substitution/domain arithmetic.

### 4. practice.md E1 LF 1–11; bytes [0,704)

The demand is available now: the baseline power derivative gives f(4)=2 and f′(4)=1/4; A then gives L(x)=2+(x−4)/4. h=0.04 produces 2.01. Replacing h by x would give 3 at x=4 rather than 2, demonstrating the requested basepoint failure.

Available premises: Lesson A; baseline Mathematics power derivative and square-root arithmetic.

### 5. lesson.md B LF 51–100; bytes [3662,6623)

Each zero-basepoint form follows by inserting its value and derivative into A; power differentiation yields slope r with 1+u positive. For the product, inputs −2x and x give slopes −2 and −1/2; their product has constant 1, linear coefficient −5/2 and algebraic x². The omitted individual second-order terms prevent interpreting that x² as the full quadratic coefficient. FM27 supplies the real exponential and binomial expansions used here; their higher powers and bounded near-one factors do not create a new linear term. The displayed product-rule check yields the same slope, and A’s remainder relation justifies reading that coefficient as f′(0).

Available premises: Lesson A; baseline Mathematics trig/exponential/power derivatives and chain/product rules; FM27 Maclaurin expansions.

### 6. practice.md E2 LF 12–18; bytes [704,1197)

The two small inputs are 3x and −2x; using r=−1/2 gives factors 1+3x and 1+x. B’s accounting gives 1+4x, hence value 1 and derivative 4 by A’s negligible-remainder criterion. The square-root denominator requires 1−2x>0, or x<1/2, and closeness to zero additionally controls the approximation. A lone 3x² omits each factor’s quadratic term, exactly the failure explained in B.

Available premises: Lesson A–B; baseline algebra and square-root domain.

### 7. lesson.md C LF 101–124; bytes [6623,7485)

With f(0)=1 the numerator is f(x)−f(0), so the quotient is precisely the derivative at zero. Chain/power rules give 20. A supplies R1(x)/x→0, and subtracting 1 then dividing by nonzero x leaves 20+R1(x)/x, which explains the exact limit rather than treating an approximation as equality.

Available premises: Lesson A remainder and B; baseline derivative definition, chain and power rules.

### 8. practice.md E3 LF 19–31; bytes [1197,1560)

For f(x)=ln(1+3x), f(0)=0 and the chain rule gives f′(0)=3. The domain is x>−1/3, an interval containing zero; C therefore identifies the quotient as a derivative limit. Alternatively A gives f(x)=3x+R1(x) with R1/x→0. A numerical approximation alone specifies no such behaviour after division.

Available premises: Lesson A–C; baseline logarithmic domain and chain derivative.

### 9. lesson.md D LF 125–158; bytes [7485,10194)

Differentiating A+Bh+Ch² twice gives B+2Ch and 2C, so matching at h=0 fixes A,B,C and the one-half. The stated continuity condition is intelligible and sufficient for the offered bound: if |R2″(t)|≤M and R2′(0)=R2(0)=0, baseline definite integration gives |R2′(t)|≤M|t| and then |R2(h)|≤M h²/2 for either direction. Nearby second derivatives make M→0, giving the displayed negligible remainder. For cosine, values 1,0,−1 give 1−x²/2; at 0.2 this is 0.98 and subtraction from the supplied reference yields the stated error improvement.

Available premises: Baseline Mathematics “Integration and elementary differential equations” LF 176–209 (fundamental theorem at LF 178), and ordinary integral bounds from signed-area/rectangle reasoning; derivative rules LF 136–174; lesson A local error meaning. No general remainder theorem was assumed before this explanation.

### 10. figures/sine-cosine.png, full exact PNG at lesson line 158

The full two-panel image has legible axes and distinct solid/dashed/dotted legends. On the left sin has value 0, slope 1, second derivative −sin0=0, so L=Q=x is available from the just-read formula. On the right the horizontal L=1 and downward Q=1−x²/2 share the cosine contact (0,1); the quadratic visually follows the curve more closely nearby. Wider separations illustrate locality, without supplying an error bound.

Available premises: Lesson D and baseline sine/cosine derivatives.

### 11. lesson.md LF 159–182; bytes [10194,11287)

The caption matches the inspected image. Applying the one-half second-derivative coefficient gives respectively 0, −1/2, 1/2, −1/2 and r(r−1)/2 for the five listed forms. The displayed logarithm derivatives follow by reciprocal and chain rules, and the power derivative is obtained by differentiating B’s first derivative. The earlier positivity, fixed-r and radians restrictions carry forward explicitly.

Available premises: Lesson B and D; baseline derivative rules.

### 12. practice.md E4 LF 32–38; bytes [1560,2201)

D’s derivative values 0,1,−1 construct x−x²/2. ln0.9 uses x=−0.1 (not 0.9), so L=−0.1 and Q=−0.105. Subtraction from the supplied reference yields absolute errors 0.0053605157 and 0.0003605157. The quadratic term is negative on both sides because x²≥0 and f″(0)<0. Sine has f″(0)=0, hence no x² correction despite using the quadratic construction.

Available premises: Lesson A displacement and D; ordinary arithmetic.

### 13. lesson.md E LF 183–213; bytes [11287,12644)

Substitution squares −2x as a whole, giving 2x², while r(r−1)/2 with r=−1/2 gives 3/8. The three degree-two products contribute 3/8+2+1=27/8. Higher products have degree at least three; D’s remainders divided by x² tend to zero and factors stay finite, preserving the degree-two accounting. The coefficient corresponds to f″(0)/2, and twice applying the baseline product rule gives 4+2+3/4=27/4 independently.

Available premises: Lesson B’s first-order example and D’s quadratic forms/error condition; baseline power/product rules and algebra.

### 14. practice.md E5 LF 39–45; bytes [2201,2692)

D supplies e^(3x)≈1+3x+(9/2)x² and (1−2x)^(−1/2)≈1+x+(3/2)x². E’s three sources give quadratic coefficient 9/2+3+3/2=9, so Q=1+4x+9x² and g″(0)=18. Cubic products exceed degree two and omit unprovided cubic contributions; the relation to g remains approximate with D’s local error condition.

Available premises: Earlier E2 domain and linear construction; lesson D–E.

### 15. lesson.md F LF 214–224; bytes [12644,13817)

The passage explicitly introduces a new physical law rather than deriving relativity from baseline mechanics. It identifies the same two events, the moving clock’s elapsed T, and the inertial frame’s synchronized coordinate-time T′; prime is explicitly a name. The interval 0≤v<c makes 1−v²/c² positive and the real denominator nonzero. The claim is a supplied model premise; the external citation is not needed or opened.

Available premises: Introduced law and definitions in this passage; baseline units, speed and square-root domains.

### 16. figures/clock-model.png, full exact PNG at lesson line 224

The two circles are explicitly labelled the same moving clock at first and later tick, linked by an arrow at constant speed v. T is attached to elapsed time carried from A to B; T′ labels the stationary reference frame’s coordinate interval. Thus the graphic distinguishes event markers from two different clocks and matches the text’s same-events comparison. It is a schematic, not a scaled plot from which a time ratio is inferred.

Available premises: Earlier F definitions and introduced law.

### 17. lesson.md F LF 225–263; bytes [13817,16925)

With ε=(v/c)², equal speed units cancel. B’s r=−1/2,u=−ε gives +ε/2, and D gives +3ε²/8. For 0<ε<1 the exact denominator is below one, so T′>T for T>0; ε=0 gives equality. Squaring 4/(3×10^5) gives 1.7778×10^−10, half is 8.8889×10^−11 and multiplying by 86400 s gives 7.68 μs. The next ratio contribution is (3/8)ε²≈1.1852×10^−20 and its time contribution ≈1.024×10^−15 s. Baseline binomial cubic coefficient r(r−1)(r−2)/6 with u=−ε gives +5ε³/16. Since ε=(v/c)², powers one and two in ε are powers two and four in v/c. The tolerance/model caveats follow; GPS and historical-clock remarks are contextual claims, not additional derivation premises verified externally in this read.

Available premises: Lesson B,D,F; baseline Mathematics binomial expansion LF 88–97 and FM27 at LF 409; Physics units/prefixes and time reference data.

### 18. practice.md E6 LF 46–54; bytes [2692,3627)

F makes ε=0.0004 and the two multipliers 1.0002 and 1.00020006, hence times 1000.2 s and 1000.20006 s. Their distances from the supplied rounded reference are 0.000060020007 s and 0.000000020007 s, decisively above/below 0.00001 s even allowing rounding of the displayed reference. The ε substitution explains the speed degree, and the model explicitly omits gravity, providing the requested GPS limitation without outside science.

Available premises: Lesson F and ordinary arithmetic; supplied E6 reference and threshold.

### 19. lesson.md G LF 264–267; bytes [16925,17329)

This transition frames a later retrieval/application activity and explicitly distinguishes recalling formulas from using them at a stationary point. It does not claim retention or observed mastery. The requested reconstruction can draw on A and D; the delay is an adjustable study suggestion, not a new subject prerequisite.

Available premises: Earlier lesson A and D; ordinary reading.

### 20. practice.md E7 LF 55–64; bytes [3627,4539)

Matching A+Bh+Ch² at h=0 reconstructs the linear/quadratic formulas from A,D. Here h=0.03, L=5 and Q=5−3(0.03)²=4.9973; the second derivative supplies a downward correction when the slope is zero. The stated continuous-second-derivative hypothesis supplies local R2/h²→0, but no finite-interval numerical bound. Sine already refutes a compulsory nonzero square. The assertion of improvement at every input is also unsupported by a local theorem; an explicit permitted check is cosine at x=4, where Q=−7 and L=1 while baseline cosine lies in [−1,1], so Q is necessarily worse there.

Available premises: Lesson A,D and inspected sine/cosine figure; baseline unit-circle cosine bounds and arithmetic. The cosine x=4 deduction assesses the prompt’s universal claim, not a new learner assessment.

### 21. lesson.md source/notation ending LF 268–274; bytes [17329,18555)

The notes distinguish newly drawn figures/practice from the cited source and reserve equality for exact relations. Within the permitted teaching, retaining T gives time units and r=−1/2 matches the square-root reciprocal, so those mathematical explanations are reconstructible. The assertions about source pages, its four figures, wording and typographical errors cannot be independently checked against an original PDF in this confined read; the external links were not followed. The final navigation does not add a mathematical dependency.

Available premises: Earlier F and baseline dimensional/power reasoning; source-fidelity assertions treated as unverified provenance, not imported subject knowledge.

### 22. hints.md LF 1–54; bytes [0,2467)

All seven hints point to available next operations: E1 [8] fixes h=0.04 before applying slope 1/4; E2 [15] exposes the two signs that produce +x and identifies the omitted factor terms; E3 [22] makes F(0)=0 so the quotient is a derivative; E4 [29] separates negative input from positive square and defines absolute error by magnitude; E5 [36] squares the whole −2x and lists every degree-two pairing, retaining the factor 1/2 in the derivative relation; E6 [43] converts the dimensionless ratio into seconds before comparison; E7 [50] differentiates A+Bh+Ch² to recover A,B,2C. None supplies a previously missing prerequisite for its exercise, and none contradicts the earlier prompts.

Available premises: Earlier lesson A–G and E1–E7; baseline algebra/calculus.

### 23. solutions.md LF 1–163; bytes [0,7860)

E1 [8–15] computes the available slope 1/4, h=0.04 and value 2.01, with the failed replacement giving 3 at the basepoint. E2 [22–31] combines 1+3x and 1+x into the complete linear part 1+4x, checks slope by product rule, and distinguishes domain x<1/2 from small inputs. E3 [38–45] uses F(0)=0 and F′(0)=3, with R1/x→0 showing why division preserves the stated exact limit. E4 [52–76] constructs x−x²/2, inserts −0.1, obtains the earlier two absolute errors, and explains sine’s zero square using its second derivative. E5 [83–104] adds all three square contributions 9/2+3/2+3=9; the direct second-product derivative 9+6+3=18 checks the inferred value. E6 [111–131] computes the dimensionless and seconds corrections consistently; both errors and the threshold decisions match the supplied rounded reference, with rounding too small to reverse either comparison. E7 [138–159] derives A,B,2C, computes 4.9973 from h=0.03, and supplies an accessible cosine counterexample: baseline periodicity makes cos(2π)=1, whereas Q(2π)=1−2π². Its family 5−3h²+Kh³ has the same value/slope/second derivative at h=0 for any finite K; at h=0.03 the omitted 0.000027K can vary without bound over those functions. Thus continuity alone gives locality, not a prescribed finite-input tolerance. All seven solutions and the ending/navigation are read; none was used to retroactively supply an earlier required premise.

Available premises: Baseline calculus, polynomial arithmetic and cosine periodicity; all previously read teaching/practice; no external subject input.

## Established defects

None supported by this reading. In particular, I did not treat a familiar result as supplied merely by its name: the first-order remainder follows from the displayed derivative definition, and the second-order remainder is accompanied by a two-integration argument under an explicit continuity condition. The given baseline is enough to reconstruct the integral bound. The exercise conclusions were checked when their prompts occurred, before hints and solutions were read.

## Provisional concerns and uncertainties

No unresolved mathematical or representational concern that blocks an assigned task was established. The mathematical constructions and model-based numerical comparisons have the dependencies stated above. No unstated clock-precision convention, numerical lookup or outside university method was needed.

The following provenance and empirical assertions remain outside this confined verification, rather than being diagnosed as teaching defects:

1. Lesson LF 270–272 claims coverage of the source PDF and identifies source typographical errors. The original PDF is excluded, so page coverage, source wording and the historical error attribution are unverified here. The correction’s mathematical meaning—retaining a time factor and using exponent −1/2—is independently available within the permitted document.
2. Lesson LF 216–222 introduces the relativistic time relation; LF 260 supplies GPS and historical context. I checked meaning, dimensions, applicability conditions and the deductions from the introduced relation. I did not independently establish its empirical truth or validate the linked sources. Nothing in E6 requires an additional external fact: gravity’s omission and its stated relevance are explicit in the teaching.
3. Supplied reference values in lesson LF 156 and practice E4/E6 are treated as reference data. Their displayed precision supports the requested comparisons; no external calculator or table was required.

## Input limits and dependencies

There was no missing, unreadable or truncated part of either authorized subject input. All four subjects in the operational baseline were actually read, although this lesson mainly uses Mathematics and Further Mathematics, with physical units also available from Physics. Chemistry was not substituted by a topic summary.

Source fidelity and external scientific verification remain limited as stated above because those inputs were intentionally unauthorized. Those limits do not create a missing mathematical step in the reviewed route. The review’s conclusion is about availability and justification under the supplied premises, not observed human learning or guaranteed exhaustiveness.
