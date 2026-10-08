D034 source technical review

Final review

Source-only preparation. All 4 complete extracted page texts and original full-page renders were read/inspected, including every cover. All PDF SHA-256 values were independently recomputed and match the audit. PDF skill previously read and applied for read-only inspection. No teaching draft, PROF/SASIS judgment, iteration closure, or repository edit is claimed.

lec38.pdf | 4 PDF pages; PDF1 unnumbered cover, PDF2 onward printed1 onward.
Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/7cf354a7d1697b69ad8b7d28879b1edb_lec38.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec38/
SHA-256: cf22137b1ae1237d5a4d020b13b9c91a857b393c21e5ec9a4d7ba2f3bb497eac

Page and figure coverage

lec38.pdf PDF1/printedcover: MIT OCW cover and terms.
lec38.pdf PDF2/printed1: Termwise differentiation and integration summary; Gaussian primitive series; Sine series at pi/2; Improper arcsine integral for pi/2; Binomial expansion with exponent−1/2.
lec38.pdf PDF3/printed2: Substitution u=−x² and integrated arcsine series; Endpoint pi/2 series and optional convergence problem; Weighted-average quotient; Exponential survival and expected decay payoff; Substitution u=kt.
lec38.pdf PDF4/printed3: Evaluation of first exponential moment; Half-life and isotope identification; Annuity analogy and two-life claim; Multivariable chain rule perspective and closing verse.

Findings and independent deductions

D034-C01 | missing_domain_and_regular_operation_conditions | lec38.pdf PDF2,3/printed1,2 | Opening series rules and binomial substitution
The formulas for differentiation and integration are correct but the common interior convergence domain is unstated in this recap. The binomial series is subsequently evaluated at an endpoint where the derivative series diverges.
Require |x|<R for general power-series operations and justify endpoint evaluation separately. The exp/sin series have infinite radius; (1+u)^(-1/2) requires |u|<1 and, after u=−x², |x|<1.
On |x|≤r<rho<R, bounded |a_n rho^n| gives summable geometric bounds for original and derivative series. Uniform convergence on that compact interval justifies the displayed operations. The coefficients c_n=(2n)!/(4^n(n!)²)=product_(j=1)^n(2j−1)/(2j) are1,1/2,3/8,5/16,..., verifying every coefficient shown.

D034-G01 | endpoint_proof_gap_explicitly_left_as_exercise | lec38.pdf PDF2,3/printed1,2 | Improper arcsine integral and pi/2 series
The endpoint identity is correct, but the source passes to x=1 before proving convergence; it explicitly poses the justification as an optional problem. Its L’Hôpital hint does not by itself specify an argument for the discrete product coefficients.
Treat the endpoint integral as a limit, then supply a separate convergence/limit argument. Do not count the optional problem as a supplied proof or treat the final value as false.
For0≤r<1, termwise integration gives arcsin r=sum_(n≥0) c_n r^(2n+1)/(2n+1). For n≥1, log c_n=sum log(1−1/(2j))≤−H_n/2≤−log(n+1)/2, hence c_n≤1/sqrt(n+1). Thus a_n=c_n/(2n+1)≤1/(2n^(3/2)), and sum a_n converges. This bound is uniform for0≤r≤1, allowing r→1 under the series and yielding sum a_n=pi/2. Independently x=sin theta on[0,arcsin r] gives the integral=arcsin r→pi/2; near1 the integrand is comparable to(1−x)^(-1/2), so it is integrable. After n=N≥1, the pi/2 tail is≤1/sqrt(N), and the corresponding pi tail≤2/sqrt(N).

D034-S01 | independent_series_verification_and_terminology | lec38.pdf PDF2/printed1 | Gaussian-distribution example and sine comparison
The Gaussian primitive coefficients and sine evaluation are correct. The displayed integral from0tox is related to a Gaussian distribution but is not itself a normalized cumulative distribution function. Non-elementarity is asserted without proof.
Keep the primitive distinct from a probability CDF. The series is an exact computable representation for every real x; the non-elementarity theorem is not proved by these computations.
Integrating the exp(−t²) series gives J(x)=sum_(n≥0)(−1)^n x^(2n+1)/(n!(2n+1)); the absolute consecutive-term ratio tends to0 for fixed x, so the series converges for all real x and uniformly on compact intervals. This verifies x−x³/3+x⁵/10−x⁷/42+... . For the normalized density exp(−t²)/sqrt(pi), the CDF is1/2+J(x)/sqrt(pi). The sine factorial series also converges everywhere; at pi/2 it equals1 because Taylor remainder bounds identify it with the usual radian sine.

D034-C02 | weighted_average_conditions | lec38.pdf PDF3,4/printed2,3 | Weighted-average definition and monetary interpretation
The normalized quotient is presented without restrictions on w, denominator or integrability. The particle example also needs k>0 and an implicit dollars-per-second payment rate.
For an ordinary weighted mean require w≥0,0<integral w<infinity, and integral|fw|<infinity. For the example use k>0 and a payoff rate of1dollar/second. Equal expected payment is a fair-game mathematical benchmark; no unique real-world purchase price follows without preferences, discounting and contract assumptions.
Writing p=w/integral w makes p a density, so the quotient is expectation with respect to that density and lies between bounds for f when they exist. For w=exp(−kt), the total is1/k only for k>0. If payoff is c*t in consistent money/time units, its expected monetary amount is c/k rather than a bare time1/k.

D034-G02 | survival_density_conflation_with_correct_special_case | lec38.pdf PDF3,4/printed2,3 | Decay likelihood used as weighting function; annuity analogy
The source calls exp(−kt) the probability of surviving until t and then uses its normalized version as the decay-time density. This yields the right answer for the exponential model, but survival functions are not generally densities.
State S(t)=P(T>t)=exp(−kt) and p_T(t)=−S′(t)=k exp(−kt). In this special case normalizing S happens to give exactly p_T because the hazard is constant. Do not generalize the normalized-survival formula to arbitrary lifetime distributions.
E[T]=integral_0^infinity t*k exp(−kt)dt=1/k. Equivalently the survival-tail identity E[T]=integral_0^infinity S(t)dt gives the same answer. Counterexample: for T uniform on[0,1], S(t)=1−t, E[T]=1/2, but [integral_0^1 t(1−t)dt]/[integral_0^1(1−t)dt]=1/3. Thus the source construction is justified by the exponential restriction, not by a general identification of survival and density.

D034-E01 | confirmed_notation_and_contextual_data_defects | lec38.pdf PDF3,4/printed2,3 | w(x)=exp(−kt); isotope/half-life sentence
The weight uses x on the left and t on the right. The last page identifies Polonium with superscript120 and gives131days, inconsistent with the preceding calculus application to Po-210 and its rounded138-day half-life.
Use w(t). The intended isotope is inferred to be Po-210, with rounded half-life138days, corroborated by CDC. Treat both120and131as source defects for that intended application; do not silently attribute those numbers to another isotope.
The algebraic relation k=ln2/H remains correct for any positive H. Using the intended source input, H=138*24*3600=11923200seconds. D031/L35 lec35.pdf PDF3/printed2 explicitly uses Po-210 and138days; this cross-source identity check is corroborated by the CDC primary fact sheet. The source does not explain a deliberate change of isotope.

D034-S02 | independent_exponential_moment_check | lec38.pdf PDF3,4/printed2,3 | Substitution and integration-by-parts calculation
All displayed integral transformations and the final expected value1/k=H/ln2 check out for k>0.
Distinguish mean lifetime1/k from median/half-lifeH=ln2/k. Keep the endpoint limits in the integration-by-parts proof.
Integral_0^M u exp(−u)du=[−(u+1)exp(−u)]_0^M=1−(M+1)exp(−M)→1. With u=kt, k integral_0^infinity t exp(−kt)dt=(1/k)integral_0^infinity u exp(−u)du=1/k. The half-life relation exp(−kH)=1/2 yields H=ln2/k, so mean/H=1/ln2≈1.4427.

D034-C03 | annuity_model_assumptions | lec38.pdf PDF4/printed3 | Real-world annuity paragraph
The analogy uses f(t)=t as total money and exp(−kt) as survival; it suppresses payment rate, timing and discounting and implicitly assumes a constant mortality hazard.
Treat this as a simplified mathematical lifetime-payoff model, not a full annuity definition or pricing result. If a continuous unit-rate benefit is paid while alive, total undiscounted benefit is T and E[T]=integral S; a general survival law need not be exponential.
For a continuous rate c and deterministic discount factor d(t), nonnegative integration gives expected discounted benefits=c*integral_0^infinity d(t)S(t)dt. In the specific mathematical model S=exp(−kt),d=exp(−delta*t), this equals c/(k+delta) when k+delta>0. Discrete monthly payments instead require a survival-weighted sum. These are reviewer-derived model distinctions, not additional source claims or a product recommendation.

D034-E02 | overstated_mathematical_necessity | lec38.pdf PDF4/printed3 | Two-life annuity requires multiple integrals
Multiple integrals can describe joint lifetimes, but the categorical statement that they are needed is false as a mathematical necessity. The benefit rule is also unspecified.
A single integral of the appropriate joint survival probability suffices for many two-life payoff models. Distinguish a benefit ending at first death from one ending at last death and state dependence assumptions.
For T_min=min(T1,T2), E[T_min]=integral_0^infinity P(T1>t,T2>t)dt. For T_max, use P(T1>t or T2>t). If the lifetimes are independent exponentials with rates k1,k2>0, E[T_min]=1/(k1+k2) and E[T_max]=1/k1+1/k2−1/(k1+k2), all by one-variable integrals. Independence is required only for replacing the joint survival by a product.

D034-C04 | chain_rule_hypotheses_and_supplement | lec38.pdf PDF4/printed3 | Closing claim that multivariable chain rule unifies rules
The conceptual unification is correct for differentiable maps. Implicit differentiation additionally needs a differentiable branch and a nonzero partial derivative to solve for its slope.
Interpret the closing prose as motivation, not a theorem that every function is differentiable or every implicit equation defines a differentiable function.
For h(x)=G(f(x),g(x)), h′=G_u f′+G_v g′. Choosing G(u,v)=uv gives the product rule; G=u/v gives the quotient rule for v≠0. For F(x,y(x))=0, chain differentiation gives F_x+F_y y′=0 and y′=−F_x/F_y if F_y≠0. Suitable continuous first partials and F_y≠0 also supply the local branch through the implicit-function theorem. The displayed closing verse contains no additional mathematical formula.

Independent mathematical coverage

- All four complete page texts and original full-page renders read; no figures occur. Every binomial coefficient, integral, series limit, weighting formula and physical unit was inspected.
- Proved convergence of the endpoint pi/2 series by an elementary product/logarithm bound and uniform comparison, independently of the optional hint.
- Verified all Gaussian and sine coefficients, the improper arcsine integral and exponential moment calculation.
- Checked probability interpretation by deriving the exponential density and providing a nonexponential counterexample.
- Separated the two-life necessity claim from the correct multivariable-chain-rule motivation.

Technical disposition

Source review complete. Intended series and exponential-mean values are correct; the endpoint proof is an explicit exercise, now recorded as reviewer supplementation. Data/variable typos, survival-density conflation outside the exponential case, and the overstated necessity of multiple integrals are precisely localized.

Limits

- The Gaussian primitive non-elementarity theorem is not independently proved.
- The intended Po-210 correction is inferred from the earlier original lecture and corroborated externally; no alternative isotope is specified in this packet.
- Annuity prose remains an illustrative model, with no actual contract or pricing data reviewed.

Primary verification

CDC Facts About Polonium-210 | https://www.cdc.gov/radiation-health/data-research/facts-stats/polonium-210.html | What to know: isotope identity and138-day rounded half-life | retrieved 2026-10-08
Corroborates correction of source isotope/half-life context only.
