D031 source technical review

Improper integrals

Source-only preparation. All 7 complete extracted page texts and original full-page renders were read/inspected, including every cover. All PDF SHA-256 values were independently recomputed and match the audit. PDF skill previously read and applied for read-only inspection. No teaching draft, PROF/SASIS judgment, iteration closure, or repository edit is claimed.

lec35.pdf | 7 PDF pages; PDF1 unnumbered cover, PDF2 onward printed1 onward.
Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/6f78763852e7fd656a9aa1dc67fef6ee_lec35.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec35/
SHA-256: 526d15e1609795621993060e3981ba7ad7625a6188087d40b2ec9bd09827a2bc

Page and figure coverage

lec35.pdf PDF1/printedcover: MIT OCW 18.01 Fall 2006 cover and terms link.
lec35.pdf PDF2/printed1: Improper integral definition; Exponential integral finite truncation and infinite limit; Radioactive decay integral and half-life relation.
lec35.pdf PDF3/printed2: Polonium historical example: half-life, units, activity and power arithmetic; Biological and heating claims; Arctangent integral.
Figure 1: Tangent on (-pi/2,pi/2), both vertical asymptotes; M=tan(theta), theta approaches pi/2 from below.
lec35.pdf PDF4/printed3: Inverse-tangent limit and graph; Gaussian integral and non-elementary finite primitive claim; Harmonic integral divergence; Power tail integrals for p>1 and 0<p<1.
Figure 2: Arctangent increasing between horizontal asymptotes ±pi/2; point (M,theta) matches inverse graph.
lec35.pdf PDF5/printed4: Power-integral convergence summary; Nonnegative comparison and both logical directions.
Figure 3: Nonnegative f below g on tail [a,infinity); shaded-domain logic concerns integrals over that tail.
lec35.pdf PDF6/printed5: Split locally finite contribution from tail in examples 7–8; Comparison with x^(-3/2) and exp(-x); Limit comparison statement; Rational example divergent like 1/x.
lec35.pdf PDF7/printed6: Polynomial times exponential convergence; Singular endpoint definition; Integral of x^(-1/2); Power singularity criterion p<1.

Findings and independent deductions

D031-C01 | missing_conditions | lec35.pdf PDF2,5,6,7/printed1,4,5,6 | Definition and comparison statements
Convergence is said to mean the limit exists; finite is implicit, and local existence of finite truncations is not stated. The comparison proof is illustrated rather than supplied.
Require a finite real limit and local integrability on every truncated interval; singular endpoints must be treated separately. Eventual inequalities suffice only when the discarded initial integral exists.
For nonnegative locally integrable f, F(M)=integral_a^M f is increasing. If 0≤f≤g and integral g is finite, F(M) is bounded and hence has a finite limit. If integral f diverges, G(M)≥F(M) is unbounded. The extended limit +infinity is divergence, as the source later correctly says. A two-ended improper integral requires two separate finite limits; symmetric principal values are a different notion.

D031-S01 | reviewer_supplement | lec35.pdf PDF2,3/printed1,2 | Exponential model and numerical units
The formulas integral_0^infinity exp(-kx)=1/k, N=R/k, k=ln2/H and rounded activity/power values are arithmetically consistent.
Keep k>0 and the ideal exponential macroscopic/expected-population model explicit. The finite-truncation error is exp(-kM)/k, relative error exp(-kM).
H=138*24*3600=11923200 seconds. Using the source rounded 6e23 atoms/mol and molar mass 210 gives R=1.6609807064e14 s^(-1), about 4489 curies using 3.7e10 s^(-1)/Ci; multiplying by 5.3 MeV and 1.602176634e-13 J/MeV gives 141.04 W. These verify the source rounded 1.66e14, 4500, 140 values. N(t)=N(0)exp(-kt) follows by differentiating; integration counts total expected decays.

D031-C02 | unsupported_application_generalization | lec35.pdf PDF3/printed2 | Polonium paragraph after activity calculation
The paragraph turns activity/power into a white-hot description and gives an unqualified biological danger multiplier and fixed ingested lethal amount. None follows from the integral calculation.
Distinguish verified units and arithmetic from heat-transfer and biological assumptions. Do not use this paragraph as a medical dose model. CDC supports the rounded half-life and distinction between intact-skin and internal exposure. ICRP distinguishes absorbed/equivalent dose and states that RBE varies with dose, dose rate and endpoint. The numerical lethality claim was inspected but is not validated or reproduced here.
Power is energy/time; temperature additionally requires surface area, emissivity, thermal contact and loss laws. Activity alone does not specify absorbed organ dose or biological effect. Primary-source checks below support the qualification; the specific universal multiplier is not an independently verified consequence of these notes.

D031-G01 | overstatement_and_proof_gap | lec35.pdf PDF4/printed3 | Example 3 finite Gaussian integral
The correct infinite value sqrt(pi)/2 is recalled without proof; the finite integral is described as evaluable only numerically because it lacks an elementary formula.
The non-elementarity assertion is not proved in this packet; numerical evaluation is not the only representation. An exact special-function definition or convergent series is available. Do not confuse absence of elementary primitive with absence of exact representation.
Let J_M=integral_0^M exp(-x²)dx. Uniform convergence on each finite interval gives J_M=sum_{j≥0}(-1)^j M^(2j+1)/(j!(2j+1)). For the infinite value, square J_R using finite double integration; the quarter disk of radius R lies within [0,R]^2, itself within the quarter disk of radius sqrt(2)R. Polar integration bounds J_R² between pi(1-exp(-R²))/4 and pi(1-exp(-2R²))/4. Squeeze gives J_infinity=sqrt(pi)/2. This is a reviewer derivation, not a proof supplied here.

D031-E01 | confirmed_false_equality | lec35.pdf PDF6/printed5 | Example 8 displayed comparison
The source writes integral_1^infinity exp(-x)dx=1.
The exact value is exp(-1). The intended upper comparison and convergence conclusion remain correct; ≤1 would also suffice.
[-exp(-x)]_1^M=exp(-1)-exp(-M), tending to exp(-1), not 1.

D031-C03 | missing_conditions | lec35.pdf PDF6/printed5 | Limit comparison boxed prose
From 0≤f and lim f/g≤1 the source concludes f≤2g eventually, without requiring g positive.
Require g>0 eventually and a finite limit L in [0,1]. More generally 0<L<infinity gives two-sided comparability and the same convergence behavior for nonnegative locally integrable functions.
Choose epsilon=1 when L≤1 to obtain f/g<2 eventually. Without positivity f=1,g=-1 has ratio -1≤1 but f≤2g is false. For L>0, eventually L/2≤f/g≤3L/2, providing both comparison directions.

D031-G02 | proof_gap | lec35.pdf PDF6/printed5 | Example 9 rational integrand
The divergence conclusion is correct but the immediately preceding one-sided upper comparison alone cannot imply it. The displayed asymptotic expression also carries an extraneous dx on the left ratio.
Use an eventual lower comparison; distinguish integrand asymptotics from differential notation.
For x≥1, (x+10)/(x²+1)−1/x=(10x−1)/(x(x²+1))≥0. The integral therefore dominates the divergent harmonic tail. Independently a primitive is (1/2)ln(x²+1)+10 arctan x, which diverges as its upper endpoint tends to infinity.

D031-C04 | missing_parameter_restriction | lec35.pdf PDF7/printed6 | Example 10 integral_0^infinity x^n exp(-x)
The claim of convergence has no explicit restriction on n in this packet; the argument only addresses infinity.
For the intended nonnegative integer n it is correct. For real n the whole integral converges exactly when n>-1; n≤-1 diverges at zero.
On (0,1), exp(-1)≤exp(-x)≤1, so comparison with x^n gives the threshold n>-1. At infinity, for any fixed real n, n ln x−x/2 tends to -infinity (ln x/x→0), hence x^n exp(-x)≤exp(-x/2) eventually. For integer n≥0, integration by parts and vanishing boundary terms yield I_n=n I_(n-1), I_0=1, so I_n=n!; this evaluation is supplementary.

D031-S02 | reviewer_supplement | lec35.pdf PDF4,5,7/printed3,4,6 | Both p-integral criteria
The stated p>0 tail cases and all-real endpoint cases are correct. The tail conclusion also extends to p≤0, although those cases are outside the displayed general-story range.
Retain separate threshold directions for infinity and zero; p=1 is logarithmic.
For p≠1, integral_1^M x^(-p)dx=(M^(1-p)-1)/(1-p), finite at infinity exactly for p>1 with value1/(p-1). For p≤0 the integrand is ≥1 on x≥1. At zero, integral_a^1 x^(-p)dx=(1-a^(1-p))/(1-p), finite exactly for p<1 with value1/(1-p). At p=1 both endpoint limits diverge logarithmically. The reciprocal-square-root example equals2.

D031-S03 | reviewer_supplement | lec35.pdf PDF3,4,6/printed2,3,5 | Arctangent and split-comparison examples
All remaining definite-integral and comparison conclusions check out.
Keep the original figures as graphical support, with proofs through finite truncations.
The derivative of arctan x is1/(1+x²), so integral_0^M tends to pi/2. For 1/sqrt(1+x³), the initial [0,1] integral is≤1 and the tail is≤integral_1^infinity x^(-3/2)dx=2. For exp(-x³), [0,1] integral≤1 and x³≥x on[1,infinity), giving a finite tail≤exp(-1).

Independent mathematical coverage

- Read every formula, paragraph, caption and axis label in all seven original full-page renders; covers included.
- Checked all ten numbered examples, all parameter restrictions, every finite primitive by differentiation, and both convergence directions of comparison.
- Checked Figures1–3 for inverse/asymptote relations and ordering used in the proof.
- Independently recomputed physical-unit arithmetic without deriving or validating a biological dose threshold.
- Established Gaussian improper value by bounded-domain squeeze; recorded rather than silently supplied source proof gaps.

Technical disposition

Source review complete. One definite-integral equality is false; an asymptotic display has a stray differential; comparison and parameter hypotheses need explicit restrictions. Core intended convergence outcomes are correct. The historical biological aside is qualified and not validated as dose guidance.

Limits

- Non-elementarity of the Gaussian primitive is not independently proved here.
- The source supplies no clinical or thermal model for the historical radiation aside; those claims cannot be certified from this packet.

Primary verification for the historical application

CDC Facts About Polonium-210 | https://www.cdc.gov/radiation-health/data-research/facts-stats/polonium-210.html | What to know; Is Po-210 harmful to humans? | retrieved 2026-10-08
Rounded half-life and qualitative exposure-route distinction only.

ICRP Publication103 free extract | https://www.icrp.org/docs/ICRP_Publication_103-Annals_of_the_ICRP_37(2-4)-Free_extract.pdf | PDF24/printed23 Equivalent dose; PDF31/printed30 Radiation weighting factor; PDF32/printed31 Relative biological effectiveness | retrieved 2026-10-08
Distinguish physical absorbed dose, protection weighting, and biological effectiveness depending on endpoint and exposure. Extract does not establish the note’s fixed numerical danger multiplier.

