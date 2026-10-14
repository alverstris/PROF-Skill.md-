# Independent mathematical verification: D008 / MIT 18.01 Fall 2006 Lecture 9

Role: technical calculator and original-source checker only. No teaching artifact or prior teaching, reports, or other agents' directories were read. All seven original PNG pages were inspected visually. The extracted text for page 5 was consulted only to double-check the displayed exponent in the binomial reminder. Computations use exact rational arithmetic and 80-digit Decimal arithmetic in `calculate_checks.py`; the complete machine-readable results are in `calculations.json`. All assertions passed.

Original source: `original-inputs/mit-18.01-fall-2006-lec9.pdf` in this run. SHA-256: `d1b383663f7792bbdaa4d6108e17b11679d4688e413e197486941af337892320`.

## Page locators

PDF page 1 is the OCW cover. PDF pages 2-7 correspond to the lecture's printed pages 1-6 respectively. Locators below give both forms to avoid the cover-page offset.

## Source defects that must not be silently inherited

| Locator | Visible source statement | Verified disposition |
|---|---|---|
| PDF p.3 / printed p.2, sine proof sentence after the derivative calculation | With basepoint 0, `f(x)=x`. | `sin x` is not equal to `x` except at 0 in a sufficiently small neighborhood. Correct as `f(x) approximately x`, or `L(x)=x`. |
| PDF p.3 / printed p.2, last line of power-function proof | `f(x)=f(0)+f'(0)x=1+rx`. | General `f(x)=(1+x)^r` needs an approximation sign in the first equality, or use `L(x)` for the polynomial. It is exact for r=0 or r=1. |
| PDF p.4 / printed p.3, sentence immediately below `1-(5/2)x` | `f'(0)=+5/2`. | Incorrect sign. Direct differentiation gives `f'(0)=-5/2`; the immediately preceding linear polynomial already has the correct sign. |
| PDF p.5 / printed p.4, displayed time-dilation approximation | `T'=T(1-v^2/c^2)^(-1/2) approximately 1+(1/2)(v^2/c^2)`. | The right side omits T and is dimensionless. Correct as `T' approximately T[1+v^2/(2c^2)]`, or put `T'/T` on the left. |
| Same display and page, bracketed binomial reminder | `(1+u)^4 approximately 1+ru`, with `r=-1/2`. | The visible exponent is 4. It should be r. The actual substitution into exponent -1/2 and the positive correction +v^2/(2c^2) are correct. |

## Complete formula inventory and checks

### PDF p.1 / OCW cover

No mathematical content requiring verification.

### PDF p.2 / printed p.1

| Source formula or calculation | Independent check |
|---|---|
| Tangent form `y=b+a(x-x0)`, with `b=f(x0)` and `a=f'(x0)` | Substitution at x0 gives y=f(x0); derivative of the line is f'(x0). Correct. |
| `f(x) approximately f(x0)+f'(x0)(x-x0)` | Correct local first-degree Taylor formula when f is differentiable at x0; rigorous remainder is o(x-x0). |
| `f(x)=ln x`, x0=1; `f(1)=ln 1=0`, `f'(1)=(1/x)|x=1=1` | Correct on x>0. |
| `ln x approximately 0+1(x-1)=x-1` | Correct. The omitted leading term is `-(x-1)^2/2`. |
| `x=1+u`, `u=x-1`, `ln(1+u) approximately u`, `u0=x0-1=0` | Algebra and shifted basepoint correct. Real domain u>-1. |

### PDF p.3 / printed p.2

All derivatives at 0 below are independently evaluated; the triplet is `(f(0), f'(0), f''(0))`.

| Listed formula | Derivative triplet and verified result |
|---|---|
| `sin x approximately x` | (0,1,0); L=x. Angles in radians. |
| `cos x approximately 1` | (1,0,-1); L=1. A constant polynomial counts as a first-degree Taylor polynomial with zero x coefficient. |
| `e^x approximately 1+x` | (1,1,1); L=1+x. |
| `ln(1+x) approximately x` | (0,1,-1); L=x; real domain x>-1. |
| `(1+x)^r approximately 1+rx` | `(1,r,r(r-1))`; L=1+rx for fixed real r, with x>-1 sufficient for arbitrary real r. |

Sine proof: `f'=cos x`, `f(0)=0`, `f'(0)=1`, and `f(0)+f'(0)(x-0)=0+1x=x` are correct. Only the subsequent equality `f(x)=x` is defective, as listed above.

Power proof: `f(0)=1` and `f'(0)=[r(1+x)^(r-1)] at x=0=r` are correct. Its last line requires the approximation/equality correction above.

Example 2 begins with `f(x)=e^(-2x)/sqrt(1+x)` near x=0 and `e^(-2x) approximately 1-2x`. Correct by substituting u=-2x into the exponential linear polynomial. The real function's domain is x>-1.

### PDF p.4 / printed p.3

| Source formula or calculation | Independent check |
|---|---|
| `sqrt(1+x)=(1+x)^(1/2) approximately 1+x/2` | Correct; f'(0)=1/2. |
| `e^(-2x)/sqrt(1+x) approximately (1-2x)/(1+x/2)=(1-2x)(1+x/2)^(-1)` | Correct to first order. Algebraic equality holds between the two expressions formed from truncated factors. The denominator is bounded away from 0 sufficiently near x=0. |
| `(1+x/2)^(-1) approximately 1-x/2`, u=x/2 | Correct. |
| `(1-2x)(1-x/2)=1-2x-x/2+2(1/2)x^2` | Exact product is `1-(5/2)x+x^2`. Correct. The x^2 coefficient cannot be used as the quadratic coefficient of the original function because the factors were only approximated to first order. |
| Drop x^2 and obtain `1-(5/2)x` | Correct linear truncation. |
| Claim f(0)=1 and f'(0)=+5/2 | First value correct; derivative must be -5/2. Direct calculation: `f'=f[-2-1/(2(1+x))]`, hence f'(0)=-5/2. |
| Footnote shortcut: `1/sqrt(1+x)=(1+x)^(-1/2) approximately 1-x/2` | Correct. The preceding two-step approximation through `1/(1+x/2)` is also correct to first order. |
| Example 3: f(x)=(1+2x)^10; limit of `[(1+2x)^10-1]/x` | f(0)=1 and f'(x)=20(1+2x)^9, so f'(0)=20. Difference-quotient limit equals 20. Correct. |
| `(1+2x)^10 approximately 1+10(2x)=1+20x`, r=10, u=2x | Correct. Exact binomial expansion starts `1+20x+180x^2+960x^3+...`. |
| `[(1+2x)^10-1]/x approximately (1+20x-1)/x=20` | Correct limit reasoning after making the remainder explicit: numerator `20x+O(x^2)`; quotient `20+O(x)` for x nonzero. Bare numerical closeness alone would not justify dividing an uncontrolled error by x. |
| Example 4: `T'=T/sqrt(1-v^2/c^2)` | Correct special-relativistic factor when T is the proper time between two events on the moving satellite clock and T' the corresponding interval in an inertial frame relative to which it moves at constant speed v. Requires |v|<c. |

Exact binomial coefficients of `(1+2x)^10` for degrees 0-10: `1, 20, 180, 960, 3360, 8064, 13440, 15360, 11520, 5120, 1024`. These give a separate exact-polynomial check of the limit.

### PDF p.5 / printed p.4

| Source formula or calculation | Independent check |
|---|---|
| Rewriting gamma factor as `(1-v^2/c^2)^(-1/2)` | Correct. Substitute u=-v^2/c^2, r=-1/2; ru=+v^2/(2c^2). The missing factor T and printed exponent 4 defects are recorded above. |
| v=4 km/s, c=3*10^5 km/s, `v^2/c^2 approximately 10^(-10)` | Correct as an order-of-magnitude statement; actual value for these inputs is `1.777777777777...*10^(-10)`. It is not an accurate numerical equality to 1*10^(-10). |
| General quadratic formula `f(x0)+f'(x0)h+[f''(x0)/2]h^2`, h=x-x0 | Correct. C^2 near x0 is sufficient for remainder o(h^2); C^3 plus a bound on f''' gives an O(h^3) error bound. |
| Cosine example: f(0)=1, f'=-sin x, f'(0)=0, f''=-cos x, f''(0)=-1 | All correct in radians. |
| `cos x approximately 1+0*x-x^2/2=1-x^2/2` | Correct. Actual leading error is +x^4/24, because the cubic coefficient also vanishes. |
| `f=a+bx+cx^2`, `f'=b+2cx`, `f''=2c` | Correct. At 0, f(0)=a, f'(0)=b, f''(0)=2c, so c=f''(0)/2. The quadratic formula reproduces every polynomial of degree at most 2 exactly, also for any other basepoint. |

### PDF p.6 / printed p.5

| Source formula or calculation | Independent check |
|---|---|
| General quadratic formula at 0 | Correct specialization of the previous formula. |
| `sin x approximately x` listed under quadratic approximations | Correct second-degree Taylor polynomial: zero constant and quadratic coefficients; actual error begins -x^3/6. The polynomial has degree 1 but includes all coefficients through order 2. |
| `cos x approximately 1-x^2/2` | Correct. |
| `e^x approximately 1+x+x^2/2` | Correct. |
| `ln(1+x) approximately x-x^2/2` | Correct for x near 0 in x>-1. |
| `(1+x)^r approximately 1+rx+[r(r-1)/2]x^2` | Correct for fixed real r near 0 with 1+x>0. |
| Log proof: f(0)=ln1=0; f'=1/(1+x), f'(0)=1; f''=-1/(1+x)^2, f''(0)=-1 | All correct. |
| Planet Quirk quadratic substitution: r=-1/2, x=-v^2/c^2 | Coefficient `r(r-1)/2=(-1/2)(-3/2)/2=3/8`. Squaring x removes its sign. Hence gamma `approximately 1+(1/2)z+(3/8)z^2`, z=v^2/c^2. Correct. The term is fourth order in v/c but second order in z. |

### PDF p.7 / printed p.6

| Source formula or calculation | Independent check |
|---|---|
| If z has magnitude about 10^-10, z^2 has magnitude about 10^-20 | Correct. For the lecture's exact stated inputs, z^2=3.16049382716049...*10^-20 and the included quadratic term (3/8)z^2=1.185185185185...*10^-20. |
| Example 5 rewrite `e^(-2x)/sqrt(1+x)=e^(-2x)(1+x)^(-1/2)` | Exact on x>-1. |
| Exponential factor `1-2x+(1/2)(-2x)^2` | Correct quadratic polynomial `1-2x+2x^2`. |
| Reciprocal-root factor `1-x/2+[(-1/2)(-1/2-1)/2]x^2` | Correct coefficient +3/8. |
| Multiply and retain degree <=2: `1-2x-x/2+(-2)(-1/2)x^2+2x^2+(3/8)x^2` | Cross-term contributes +x^2; total x^2 coefficient is `1+2+3/8=27/8`. Correct final polynomial `1-(5/2)x+(27/8)x^2`. |
| Discard x^3 and higher product terms | Correct for a quadratic truncation. The full product of those two quadratic polynomials is `1-(5/2)x+(27/8)x^2-(7/4)x^3+(3/4)x^4`; the true cubic coefficient of the original function is -163/48, not -7/4. |

Independent derivative cross-check for the last example: set A(x)=-2-1/[2(1+x)]. Then f'=fA; f''=f(A^2+A'), with A'=1/[2(1+x)^2]. At 0, A=-5/2 and A'=1/2, so f''(0)=25/4+1/2=27/4, giving f''(0)/2=27/8. Also A''(0)=-1 and f'''(0)=A^3+3AA'+A''=-163/8, hence true cubic coefficient -163/48.

## Numerical verification of the time example

All values below use the lecture's rounded c=300000 km/s, with v=4 km/s. They do not replace c with a more precise externally sourced value.

| Quantity | Calculated value |
|---|---|
| z=v^2/c^2 | 1.77777777777778 * 10^-10 |
| gamma-1 | 8.88888889007407 * 10^-11 |
| Linear correction z/2 | 8.88888888888889 * 10^-11 |
| Quadratic correction 3z^2/8 | 1.18518518518519 * 10^-20 |
| Absolute error in linear gamma | 1.18518518536077 * 10^-20 |
| Absolute error in quadratic gamma | 1.75582990425118 * 10^-30 |
| Leading omitted term after quadratic, 5z^3/16 | 1.75582990397805 * 10^-30 |

For scale only, multiplying gamma-1 by T=86400 s gives approximately 7.680000001024 microseconds, and multiplying just the quadratic correction by that T gives 1.024*10^-15 s. Thus the dimensionless relative effect is small; the absolute elapsed-time difference depends on T. This extra scale calculation is verification evidence, not a numerical claim made on the original page.

## Assumptions and limits on qualitative statements

1. **Linear tangent approximation is local.** Differentiability gives `f(x0+h)=L(x0+h)+o(h)`. A known small numerical error requires additional information or bounds; with |f''|<=M on the interval, `|f-L|<=M h^2/2`. Merely writing approximately does not specify a tolerance.

2. **Error need not grow monotonically with distance.** The statement on PDF p.2 about becoming less accurate as one moves away is a useful schematic tendency, not a universal theorem. Smooth counterexample at x0=0: `f(x)=x+x^2(1-x)^2`, L=x. Absolute errors at x=0, 1/2, 1 are 0, 1/16, 0. A linear f is exact everywhere.

3. **Small powers do not alone bound approximation errors.** If 0<|x|<1, then |x|^3<|x|^2<|x|. Coefficients still matter, as do domain and scaling. For substitution u=kx, it is u that must be near 0. For `(1+x)^r`, the assertions are asymptotic as x->0 with r fixed; they are not uniform over arbitrarily large r.

4. **Arithmetic on truncated approximations requires controlled remainders.** Smooth factors near 0 can be written as polynomials plus O(x^2) or O(x^3); bounded denominators make the quotient expansion legitimate. A denominator tending to zero can magnify error. Products retain only the orders to which all necessary factors are known. This is why the spurious x^2 coefficient 1 from the product of the two linear factors in Example 2 must be discarded.

5. **Quadratic does not imply strictly more accurate at every finite nearby point.** With C^2 smoothness, Q has remainder o(h^2), compared with generally O(h^2) for L. If f''(x0) is nonzero, `|f-Q|/|f-L| ->0` as h->0. If f''(x0)=0, Q=L, including sine at 0. A fixed-point counterexample: f(x)=x^2-100x^3, x0=0, x=0.01. Here f=0 and L=0 are exact, while Q=0.0001 has error 0.0001. C^3 plus |f'''|<=M gives `|f-Q|<=M|h|^3/6`.

6. **"Best-fit parabola" needs a local interpretation.** Q matches f, f', and f'' at the basepoint, uniquely among polynomials of degree <=2. It is not automatically a least-squares or minimax fit on an interval. With f''(x0)=0 it is not a genuine parabola at all. No global optimization criterion is specified by the source.

7. **Radians and domains are essential.** The trig coefficients assume radians. `ln x` requires x>0; `ln(1+x)`, the reciprocal-root composite, and an arbitrary real power are safely handled in x>-1. The time factor requires |v|<c, and its small-parameter approximation requires |v|/c much less than 1.

8. **The time model needs its frame and interval assumptions.** T is proper time on the moving clock; T' is the corresponding inertial coordinate interval. A single observer's remote wristwatch reading requires a convention for comparing separated events. Constant relative speed and the special-relativistic model are assumed. The example does not itself include gravitational effects, orbital details, or signal propagation corrections. The source explicitly mentions other approximations for the GPS application.

9. **Precision and historical GPS assertions exceed a purely mathematical check.** The original 2006 statement about the best atomic clocks cannot be inferred solely from the 10^-20 order of a dimensionless factor, and cannot be treated as a verified contemporary claim. Measurement duration, comparison protocol, and uncertainty matter. The calculations support the small size of the quadratic term; they do not by themselves prove detectability limits or the engineering history. No outside source was consulted for those claims in this independent original-source-only check.

## Verification limits

The audit checks all displayed lecture equations and all numerical examples in the seven-page PDF, plus the local interpretation of its diagrams. It does not verify historical or current atomic-clock specifications or GPS engineering documentation. The schematic drawings are not scaled data, and no numerical accuracy is inferred from their drawn distances.
