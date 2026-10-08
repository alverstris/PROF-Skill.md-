D032 source technical review

Infinite series and convergence tests

Source-only preparation. All 8 complete extracted page texts and original full-page renders were read/inspected, including every cover. All PDF SHA-256 values were independently recomputed and match the audit. PDF skill previously read and applied for read-only inspection. No teaching draft, PROF/SASIS judgment, iteration closure, or repository edit is claimed.

lec36.pdf | 8 PDF pages; PDF1 unnumbered cover, PDF2 onward printed1 onward.
Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/ba5ce991638cf6285e431937132e5b32_lec36.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec36/
SHA-256: 7d5e99897f7c24f895c46916b68e3e153699603e6db05f952bee999d95dcae5a

Page and figure coverage

lec36.pdf PDF1/printedcover: MIT OCW cover and terms.
lec36.pdf PDF2/printed1: Geometric sum formal manipulation; Restriction |a|<1; endpoints a=±1; Infinite-series and nth-partial-sum notation.
lec36.pdf PDF3/printed2: Finite-limit definition of convergence; Invalid infinity subtraction warning; p-series and integral-test motivation; Basel sum and zeta(3) historical claim; Harmonic integral comparison setup.
lec36.pdf PDF4/printed3: Upper and lower Riemann bounds for harmonic sums; Logarithmic divergence rate.
Figure 1: Left endpoint rectangles above decreasing1/x on successive unit intervals.
Figure 2: Right endpoint rectangles below1/x; heights1/2,1/3,1/4 on intervals[1,2],[2,3],[3,4].
lec36.pdf PDF5/printed4: Integral comparison statement; p-series threshold; Limit-comparison definition using ratio c>0; Examples1/sqrt(n²+10) and n/sqrt(n⁵−10).
lec36.pdf PDF6/printed5: Stacking demonstration; Support by collective center of mass; Top-down construction and C0,C1,C2 definitions.
Figure 3: Staggered stack with top extending beyond bottom; dashed lines compare endpoints. Sketch qualitative, not dimensioned.
lec36.pdf PDF7/printed6: Two- and three-block positions; Weighted center-of-mass recurrence; C0 through C5 harmonic numbers.
Figure 4: Length2 blocks, C0=0,C1=1,C2=1.5; center of upper block sits at supporting block left edge.
Figure 5: Three blocks, C2−C1=1/2,C3−C2=1/3; left edge of block3 is C2.
lec36.pdf PDF8/printed7: General n+1 block construction; Unbounded harmonic overhang; Table span and block dimensions; Height estimates and astronomical comparisons.
Figure 6: COM of n upper blocks lies over the left edge of block n+1; marginal balance of rigid identical blocks.
Figure 7: One block length30cm, height3cm; earlier length2 means one unit15cm.

Findings and independent deductions

D032-G01 | proof_gap_with_correct_conclusion | lec36.pdf PDF2,3/printed1,2 | Formal subtraction of geometric infinite sums
The source first subtracts infinite sums, then explains convergence is required. The range |a|<1 is correct, but finite-sum proof is missing.
Use finite sums before taking limits. Distinguish n+1 terms in sum_k=0^n from N terms in later harmonic sums.
(1−a)sum_(k=0)^n a^k=1−a^(n+1). For |a|<1 the remainder tends to0, so sum=1/(1−a). For |a|≥1 the terms fail to tend to0 (including the stated alternating a=−1 partial sums0,1). If any series converges, a_n=S_n−S_(n−1)→0. No generalized summation convention is being used.

D032-E01 | undefined_expression_as_written | lec36.pdf PDF5/printed4 | Integral Comparison first displayed inequality
The formula subtracts an infinite series and an improper integral, takes an absolute value, and bounds by f(1), while intending to include their divergent case. For f=1/x both quantities are infinite, so this difference is undefined.
State bounded differences for finite truncations, then derive simultaneous convergence. Strict inequality also needs care at the first truncation or for non-strictly decreasing functions.
For positive nonincreasing locally integrable f, integral_1^(N+1) f≤sum_(n=1)^N f(n)≤f(1)+integral_1^N f. Equivalently f(N)≤sum_(n=1)^N f(n)−integral_1^N f≤f(1). These finite inequalities imply the integral test without infinity−infinity. If both infinite quantities are finite and f is strictly decreasing, the source strict bound holds.

D032-C01 | missing_sign_hypothesis | lec36.pdf PDF5/printed4 | Limit-comparison paragraph
The ratio-limit definition 0<c<infinity is given, but eventual positivity of both sampled terms is not repeated. It is implicit in the preceding positive-function context and essential. The symbol ~ here is explicitly defined more broadly than the usual ratio1 convention.
Require nonnegative terms, with comparator positive eventually, and discard only finitely many defined finite terms. Use the source local notation consistently; no need to label its expressly stated convention false.
For ratio a_n/b_n→c>0, eventually(c/2)b_n≤a_n≤(3c/2)b_n, and comparison proves equivalence. For signed terms this fails: a_n=(-1)^n/sqrt(n), b_n=a_n+1/n have b_n/a_n→1; sum a_n converges by the alternating test while sum b_n diverges.

D032-E02 | real_domain_error | lec36.pdf PDF5/printed4 | Last series starts at n=1
The n=1 term of n/sqrt(n⁵−10) contains sqrt(-9), so the displayed series is not a real series as written.
Start at n=2 (or another integer≥2). The positive real tail does converge. This is a domain/index defect, not an error in its asymptotic exponent.
For n≥2, the radicand is positive, and [n/sqrt(n⁵−10)]/[n^(-3/2)]=1/sqrt(1−10/n⁵)→1. Since3/2>1 the tail converges. For the other example [1/sqrt(n²+10)]/(1/n)=1/sqrt(1+10/n²)→1, so that positive series diverges.

D032-C02 | endpoint_and_parameter_conditions | lec36.pdf PDF4,5,8/printed3,4,7 | Harmonic strict bounds and p-series summary
The strict bound ln N<H_N<1+ln N has equality on the right for N=1. The p≤0 portion of the p-series criterion cannot be justified by the stated decreasing-function integral test.
The strict harmonic bound holds for N≥2; use ≤ on the right for all N≥1. For p≤0 use the necessary term test.
For N≥2, integrate1/x on each unit interval with left/right endpoint bounds, obtaining H_N−1<ln N<H_(N−1)<H_N. For p>0 the integral test gives convergence iff p>1. If p≤0, n^(−p)≥1, so terms do not approach0 and the series diverges.

D032-S01 | independent_model_derivation | lec36.pdf PDF6,7,8/printed5,6,7 | Center-of-mass recurrence and harmonic overhang
The weighted recurrence and listed harmonic values are correct in the stated length2 and unit-mass normalization.
Interpret C_n as COM of first n upper blocks, not the left edge of block n. The left edge of block n+1 is C_n.
Adding a block with left edge C_n places its center at C_n+1. Thus C_(n+1)=[nC_n+(C_n+1)]/(n+1)=C_n+1/(n+1), giving C_n=H_n. C_2=3/2,C_3=11/6,C_4=25/12,C_5=137/60>2. With N blocks, the bottom left edge is H_(N−1) and the total left-to-right span is H_(N−1)+2. This resolves the harmless one-block indexing ambiguity in the height estimate.

D032-C03 | idealized_model_conditions | lec36.pdf PDF6,7,8/printed5,6,7 | Claim of arbitrary horizontal extension
Unlimited overhang is mathematically valid for the ideal identical rigid-block model. Exact COM at a supporting edge is marginal equilibrium, not practical robust stability. The note calls the strategy best without delimiting the admissible arrangements.
Use identical uniform blocks, level supports, static gravity, no deformation or strength limits, sufficient support under the bottom block, and a single block per level. This is not an engineering prediction of room-scale or astronomical stacks.
Every upper substack must have its COM above the support contact interval. The construction saturates each left-edge condition. Choosing a fixed inward margin epsilon in length units,0<epsilon<1, changes the recurrence increment to(1−epsilon)/(n+1), still divergent. Thus arbitrary finite overhang does not depend logically on exact knife-edge balance, though physical material/height limits remain absent.

D032-C04 | approximation_and_indexing_limit | lec36.pdf PDF8/printed7 | Two-table 24-unit estimate
The numerical calculation0.03 exp(24)≈8e8m is correct, but replacing H_N=24 by ln N=24 is an estimate, not an exact inversion or minimal height. The bottom-block indexing is also implicit.
With M=N−1 and total span26 units, solve H_M≈24. The source inequalities only place the relevant M scale between exp(23) and exp(24); the upper estimate is sufficient and deliberately coarse.
0.03e^24=7.94673664e8m;0.03e^23=2.92344103e8m. NASA’s average lunar distance3.844e8m makes the source upper estimate about2.07 lunar distances. This confirms the rounded comparison for that estimate, not a claim that the minimum stack has exactly that height.

D032-C05 | sensitive_approximation_not_categorical_error | lec36.pdf PDF8/printed7 | Final sentence: 30-ft room and 10^26 meters
If the approximate room length is treated as exactly30ft, the reported10^26m height does not follow from the preceding method and stated block dimensions. Because the source explicitly says approximately30ft, a modest length change can move this exponential estimate by orders of magnitude; this is not an unconditional numerical erratum.
For exactly30ft the source method yields order10^24m. Treat10^26m and the astronomical comparison as unsupported rough estimates rather than verified consequences or categorical falsehoods. In this model a span near32–33ft can produce a scale near10^26m.
30ft=9.144m=60.96 units of0.15m. Subtracting the2-unit block length gives target H_M=58.96. The same logarithmic bounds give0.03e^57.96≈4.45e23m to0.03e^58.96≈1.21e24m for the block-count scale. Even omitting the2-unit subtraction gives0.03e^60.96≈8.95e24m. This is a conditional numerical inconsistency at the stated input; an imprecise actual room dimension is unresolved.

D032-G02 | external_theorem_not_proved_in_packet | lec36.pdf PDF3/printed2 | Basel sum and irrationality of sum1/n³
Both special-value claims are stated without proof; the word recently is historical and has no specified timescale. They are not consequences of the integral test.
Keep convergence separate from evaluation and arithmetic nature. Apéry’s primary paper is1979,27years before these Fall2006 notes. The external theorem is corroborated rather than independently reproved in this preparation.
A supplementary independent check of the Basel value uses the Fourier series of x² on[-pi,pi]: integration by parts gives constant term pi²/3 and cosine coefficients4(-1)^n/n². The piecewise-smooth Fourier convergence theorem at x=pi yields pi²=pi²/3+4sum1/n², hence pi²/6. This relies on that standard Fourier theorem outside the packet. For zeta(3) irrationality, primary Apéry1979 is the authority; a full irrationality proof is beyond the lecture and not silently claimed here.

Independent mathematical coverage

- All8 complete page texts and original full-page renders inspected, including7 diagrams and cover.
- Verified finite geometric identity, ordinary convergence definition, Riemann inequalities, p thresholds, two limit-comparison examples and their domains.
- Derived block recurrence from weighted masses; checked each labeled COM displacement and unit conversion.
- Recomputed both dimensional height estimates and distinguished logarithmic estimates from exact inversion.

Technical disposition

Source review complete. Confirmed defects: undefined infinity subtraction in the integral-test display and a non-real first term in one example. The room-height estimate is highly sensitive to an explicitly approximate room dimension and cannot be certified at the stated precision. Intended convergence and ideal harmonic overhang conclusions hold with recorded conditions.

Limits

- No full independent proof of Apéry’s irrationality theorem is claimed; primary corroboration is provided.
- Observable-universe size analogy is not certified; it follows a highly sensitive approximate height estimate and does not affect the calculus conclusions.
- Actual lecture-room measurements and real stack mechanics are not recoverable from the packet.

Primary corroboration

Roger Apéry, Irrationalité de zeta2 et zeta3, Astérisque61(1979),11–13 | https://numdam.org/item/AST_1979__61__11_0.pdf | PDF2–4/printed11–13, especially zeta3 construction on printed12–13 | retrieved 2026-10-08
Primary theorem/historical corroboration; not a new independent proof.

NASA Moon Facts | https://science.nasa.gov/moon/facts/ | Size and Distance | retrieved 2026-10-08
Average lunar distance384400km to check the source rounded comparison.

