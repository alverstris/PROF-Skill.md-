D018 source technical review

Second fundamental theorem

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/3cd98c68cec64e9214c8c9003f6cf983_lec20.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec20/
SHA-256: 711e84263db3b675c39d18aa1951a55a4f026783732924324b6578913360c990

Independently recomputed SHA-256 matches the audit. Read all 5 complete page text extractions and opened every original full-page render with view_image, including the cover. PDF page 1 is the unnumbered cover; PDF pages 2–5 are printed pages 1–4. The PDF skill was read and applied for read-only inspection. No unreadable portion. This preparation is source evidence only, not a teaching draft, PROF judgment, SASIS review, or lecture closure.

Page and figure coverage

PDF 1 / printed cover: MIT OCW course identity, Fall 2006 and terms/citation notice.
PDF 2 / printed 1: FTC 1 recall and endpoint evaluation of indefinite antiderivative; Existence of integral-defined antiderivatives; Gaussian and other examples; FTC 2 with continuity assumption; Geometric increment approximation and derivative limit.
PDF 3 / printed 2: FTC 2 area diagram; Average-integral difference quotient proof; Proof of FTC 1 via FTC 2 and mean value theorem; Remark distinguishing integral-defined G from arbitrary antiderivative F; sin/cos example begins.
Figure 1: Positive increasing curve above [a,x+Δx]; light region F(x), darker strip ΔF; labels a,x,x+Δx and y axis.
PDF 4 / printed 3: Continuation F=sin x+21 example; Error-function definition, limit and graph; Li(x)=integral_2^x dt/ln t and approximate prime counts; Cryptography motivation and proposed 200-digit interval; Endpoint logarithm estimates 200 ln10 and 201 ln10.
Figure 2: Odd increasing S-shaped erf curve through origin, flattening at both ends; axes have no numerical ticks.
PDF 5 / printed 4: Constant-denominator approximation of prime-count integral; Cryptography probability assertion; Fresnel integral definitions and C-prime(x)=cos(x²); Bessel J0 integral representation; Next-lecture L(x)=integral_1^x dt/t; Footnote integral of constant c over [a,b].

Findings and independent deductions

D018-E01 | confirmed_integrand_source_errors | PDF 3, 4 / printed 2, 3 | Remark at end of printed2 and opening displayed integral on printed3
Remark announces f(x)=sin x but computes G=integral cos t=sin x. Next page correctly gives F=sin x+21 and F-prime=cos x, yet prints integral sin x=sin b-sin a.
Use f=cos x in the remark and cos x as the integrand on PDF4; then the displayed F,G and endpoint difference are consistent.
Differentiating sin x+21 gives cos x. Counterexample a=0,b=π: integral sin x=2 but sinπ-sin0=0.

D018-E02 | confirmed_special_function_normalization_error | PDF 5 / printed 4 | Bessel J0 displayed formula
Source prints J0(x)=(1/(2π)) integral_0^π cos(x sinθ)dθ.
For these limits, replace 1/(2π) by 1/π. NIST DLMF Eq.10.9.1 gives the standard formula.
At x=0 the printed expression equals 1/2, while the standard normalized J0(0)=1. Doubling the integration interval to 2π would alternatively make the source prefactor valid; no such upper limit is printed.

D018-E03 | confirmed_digit_interval_error | PDF 4, 5 / printed 3, 4 | Integral offered for number of 200-digit primes
The limits 10^200 to 10^201 count the 201-digit range, not the 200-digit range (prime endpoints are absent).
Use 10^199≤p<10^200 for 200-digit primes, so the approximation is integral_(10^199)^(10^200) dt/ln t.
A positive integer has d decimal digits iff 10^(d-1)≤n<10^d. This elementary check settles the mismatch.

D018-E04 | confirmed_lower_bound_typo | PDF 5 / printed 4 | First sentence: ln t approximately 500
The source prints the range 200≤t≤10^201. The lower limit required by its own calculation is 10^200.
For the printed integral use 10^200≤t≤10^201. For a corrected 200-digit computation use 10^199≤t≤10^200.
ln200≈5.3, so ln t≈500 is not a uniform rough approximation on the printed literal range.

D018-E05 | precision_mismatch_in_approximation | PDF 5 / printed 4 | Final approximation to 10^198
The source declares one significant figure but changes 9×10^200/500=1.8×10^198 to approximately 10^198.
Treat 10^198 only as an order-of-magnitude estimate; rounding 1.8×10^198 to one significant figure gives 2×10^198. The corrected 200-digit integral has magnitude about 2×10^197.
For its printed interval, monotonicity bounds the integral between 9×10^200/(201 ln10) and 9×10^200/(200 ln10), approximately 1.9446×10^198 and 1.9543×10^198. These bounds concern the integral, not a proven exact prime count.

D018-G01 | abbreviated_limit_proof | PDF 2, 3 / printed 1, 2 | Geometric/average proof of FTC 2
The source uses approximate rectangle area and then states that the average tends to f(x), without an explicit error bound or negative-increment discussion.
For an interior x and h of either sign, use oriented integrals and bound the difference from f(x).
|(F(x+h)-F(x))/h-f(x)| ≤ sup_{|t-x|≤|h|}|f(t)-f(x)|→0 by continuity. This completes the proof for both signs and does not require positivity of f. At an endpoint the corresponding one-sided statement holds.

D018-C01 | integral_domain_conditions | PDF 2, 4, 5 / printed 1, 3, 4 | New-function examples and Li,L definitions
Continuity is correctly required by FTC 2; several displayed examples need domains.
For real x^(1/2)e^(-x²) use x≥0; for sin x/x fill the removable value 1 at 0 if integrating across 0. The ordinary integral from 2 of 1/ln t stays on x>1; L from 1 of 1/t stays on x>0.
The integrands 1/ln t and 1/t have singularities at 1 and 0 respectively. The source neither defines a principal value nor an improper continuation, so none is assumed.

D018-C02 | special_function_convention_not_error | PDF 5 / printed 4 | Fresnel C and S definitions
The source uses integrands cos(t²), sin(t²); common standard normalization uses cos(πt²/2), sin(πt²/2).
These source-defined functions are valid scaled Fresnel integrals; retain its explicit convention and C-prime(x)=cos(x²).
If Cstd(z)=integral_0^z cos(πt²/2)dt, then Csource(x)=sqrt(π/2) Cstd(sqrt(2/π)x), and likewise S. This is a change-of-variable derivation; the normalization difference is not a source error.

D018-G02 | external_theorem_not_proved_in_packet | PDF 4, 5 / printed 3, 4 | Li as approximation to prime counts
The prime-count connection is asserted, not derived from FTC 2. NIST DLMF §27.12 supplies a prime-number theorem estimate relative to logarithmic integral.
Treat prime counting as a specialized application imported from number theory. Do not infer an exact count or a numerical error bound solely from the rectangular estimate.
The integral denominator bounds are elementary; controlling the difference between π(x) and Li(x) requires additional theory. The base-2 Li differs from other conventions by a constant.

D018-G03 | unsupported_security_inference_and_oversimplification | PDF 4, 5 / printed 3, 4 | Secret prime and hacker-odds prose
A large number of candidate primes is used to infer cryptographic safety; the scheme, attacker and probability model are not specified.
The prime-count illustration cannot establish security. If RSA is intended, its public modulus has at least two prime factors and decryption uses a private exponent or an equivalent factor-based representation, not simply an unexplained secret-prime search.
RFC8017 §§3.1–3.2 describes modulus, public exponent and private-key representations. Candidate count alone does not constrain an algorithm exploiting structure; even an arbitrarily large key set is not secure when the key is disclosed. This is a logical limitation, not a current security recommendation.

D018-S01 | reviewer_supplementary_function_checks | PDF 3, 4, 5 / printed 2, 3, 4 | FTC1 proof and erf/Fresnel checks
The abstract FTC1 proof from FTC2 is correct; the later illustration has the separately recorded typos. erf definition and positive-infinity limit agree with NIST.
Keep the valid proof: F-prime=G-prime implies F-G constant on a connected interval, and G(a)=0.
erf-prime(x)=2exp(-x²)/sqrtπ>0 and erf-double-prime(x)=-4x exp(-x²)/sqrtπ; symmetry of the integrand makes erf odd. This verifies the schematic graph. C-prime and S-prime follow immediately from FTC2.

Independent mathematical coverage

- Read all FTC hypotheses, geometric increments and average-value expressions; verified signed-increment proof supplement.
- Verified zero derivative implies constant via MVT on a connected interval and cancellation of the antiderivative constant.
- Independently differentiated the sine/cosine example to isolate its errors.
- Checked erf normalization, monotonicity, oddness and curvature; checked specialized infinity value against NIST.
- Checked digit ranges, powers of ten, constant-integral footnote and monotonic denominator bounds.
- Checked Fresnel source convention, FTC derivative, Bessel normalization at zero and L-domain.

Technical disposition

FTC2 and the abstract deduction of FTC1 are mathematically sound with the explicit limiting estimate supplied. The illustrative sin/cos mismatches, Bessel normalization, digit range, missing exponent in a bound and claimed precision are actual source defects. The prime theorem and security motivation are kept separate from proved calculus; no security conclusion is certified.

Limits

- Non-elementary antiderivative impossibility is not proved here: the source says these are new functions, and this review does not supply differential-algebraic non-elementarity proofs.
- Exact prime counts and finite error certification were not computed; only the integral estimate and cited asymptotic connection were checked.
- The optics/circular-symmetry application labels are contextual; their physical derivations are outside this packet.

Primary references consulted

- https://dlmf.nist.gov/10.9.E1 | Eq.10.9.1 | Bessel J0 normalization 1/π for integration 0 to π | retrieved 2026-10-08
- https://dlmf.nist.gov/7.2 | Eqs.7.2.1,7.2.4,7.2.7,7.2.8 | erf definition and infinity limit; normalized Fresnel convention | retrieved 2026-10-08
- https://dlmf.nist.gov/27.12 | Eq.27.12.5 and prime number theorem discussion | Asymptotic link between prime count and logarithmic integral | retrieved 2026-10-08
- https://www.rfc-editor.org/rfc/rfc8017.html | Sections 3.1 and 3.2 | RSA modulus and private-key representations | retrieved 2026-10-08
