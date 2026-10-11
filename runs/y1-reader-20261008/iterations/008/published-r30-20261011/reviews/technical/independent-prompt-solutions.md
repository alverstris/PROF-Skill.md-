# D008 independent solutions sealed before teaching access

Role: independent technical reviewer, not SASIS. These are reviewer calculations, not a report of a real learner's performance.

Exact prompt input: `/workspace/scratch/f9c0b7fc7e76/d008-clean-r30-20261011/author/exercise-prompts.txt`.

Prompt SHA256: `4e1a9174104dd053bd5ff29bb3fdbdaa4081ea27c35d0f81c3b138153d607742`.

The operative r30 pin supplied by the parent is `3c3f28bd75d29ac7f967dde66b5e41e49aae51e4`, with the same 36 package blobs as the previously admitted preparation package. The source and full baseline preparation records remain separate and unchanged. During this prompt-solving phase, the only new external subject-content file read was the exact prompt packet. No lesson, figure, hint, proposed solution, held audit or other reviewer report was opened. No answers or findings were sent to the author.

## E1. Local estimate from a known point

For `f(x)=sqrt(x)`, `f(4)=2` and `f'(x)=1/(2 sqrt(x))` for `x>0`, so `f'(4)=1/4`.

The tangent line is

`L_4(x)=2+(x-4)/4`.

At `x=4.04`, the displacement from the basepoint is `h=4.04-4=0.04`. Therefore

`sqrt(4.04) approximately L_4(4.04)=2+0.04/4=2.01`.

The basepoint check is `L_4(4)=2=f(4)`. Replacing the displacement `x-4` by `x` would instead produce `2+x/4`, whose value at `x=4` is `3`, not `2`. It therefore fails even to pass through the point of tangency. As an independent arithmetic check, `2.01^2=4.0401`, consistent with a close estimate of the requested square root.

## E2. Combining first-order information

Rewrite `g(x)=exp(3x)(1-2x)^(-1/2)`. The inputs substituted into the basic expansions are `u=3x` for the exponential and `w=-2x` for the power. Both tend to zero as `x` tends to zero.

Near zero,

`exp(3x)=1+3x+O(x^2)`

and

`(1-2x)^(-1/2)=1+(-1/2)(-2x)+O(x^2)=1+x+O(x^2)`.

Thus `g(x)=1+4x+O(x^2)`, and its linear Taylor polynomial is `L_0(x)=1+4x`. In particular, `g(0)=1` and `g'(0)=4`. Here `O(x^2)` means a remainder bounded in absolute value by a constant times `x^2` for sufficiently small `|x|`; dividing it by `x` gives a term tending to zero, which justifies the derivative inference. This notation is used in this independent technical check, not presumed to have been taught by the still-unread lesson.

For a real nonzero denominator, `1-2x>0`, so the full real domain is `x<1/2`. For example, `(-1/4,1/4)` is a neighborhood of zero contained in that domain. The approximations concern sufficiently small `|x|` inside such a neighborhood; membership in the domain alone is not an accuracy guarantee.

The product of the two linear polynomials is `1+4x+3x^2`. Its `3x^2` is only the cross term. Each original factor also has its own quadratic term, and those contribute at exactly the same order. Retaining only the cross term therefore cannot give a justified quadratic approximation to the original product.

Independent differentiation gives `g'(x)=3 exp(3x)(1-2x)^(-1/2)+exp(3x)(1-2x)^(-3/2)`, hence `g'(0)=3+1=4`.

## E3. A limit from local behaviour

Let `F(x)=ln(1+3x)`. Then `F(0)=0` and `F'(x)=3/(1+3x)`, so `F'(0)=3`. The expression in the question is precisely its derivative difference quotient at zero:

`lim_(x->0) ln(1+3x)/x = lim_(x->0) [F(x)-F(0)]/(x-0) = F'(0) = 3`.

The logarithm requires `1+3x>0`, or `x>-1/3`; the quotient also excludes `x=0`. A sufficiently small punctured neighborhood of zero lies in this real domain.

A numerical statement such as `ln(1+3x) approximately 3x` does not by itself specify how its error behaves after division by a vanishing `x`. Even an error tending to zero can leave a nonzero quotient: an error equal to `x` would become `1` after division. The derivative definition above supplies the needed exact limiting warrant. Alternatively, the valid expansion `ln(1+3x)=3x-(9/2)x^2+O(x^3)` gives quotient `3-(9/2)x+O(x^2)` and the same limit.

## E4. Curvature and a comparison

For `f(x)=ln(1+x)`,

`f(0)=0`, `f'(x)=1/(1+x)`, `f'(0)=1`,

`f''(x)=-1/(1+x)^2`, `f''(0)=-1`.

Therefore `Q_0(x)=x-x^2/2`, while `L_0(x)=x`. To estimate `ln(0.9)`, use `x=-0.1`, giving

`Q_0(-0.1)=-0.1-0.01/2=-0.105`

and `L_0(-0.1)=-0.1`.

Using the supplied reference `-0.1053605157`, the absolute errors are

| Estimate | Absolute error relative to the supplied reference |
|---|---:|
| Linear `-0.1` | `0.0053605157` |
| Quadratic `-0.105` | `0.0003605157` |

The quadratic estimate has the smaller error in this comparison. The numerical errors use the reference's shown digits rather than claiming more precision than was supplied.

The quadratic correction is nonpositive because its coefficient is `f''(0)/2=-1/2` and `x^2` is nonnegative. It lowers the tangent-line estimate on either side of the basepoint, reflecting the negative curvature near zero. Here that correction is `-0.005`.

For sine, `f(0)=0`, `f'(0)=cos(0)=1`, and `f''(0)=-sin(0)=0`. Its quadratic Taylor approximation is therefore `Q_0(x)=x`. A Taylor polynomial through second order may have a zero squared-term coefficient; it has degree at most two.

## E5. A complete product through second order

The expansions of both factors, to the required order, are

`exp(3x)=1+3x+(9/2)x^2+O(x^3)`

and

`(1-2x)^(-1/2)=1+x+(3/2)x^2+O(x^3)`.

The power coefficient is `(-1/2)(-3/2)(-2x)^2/2=(3/2)x^2`.

Multiplying and collecting every contribution of degree two gives:

| Degree-two contribution | Coefficient of `x^2` |
|---|---:|
| Exponential quadratic times reciprocal-root constant | `9/2` |
| Exponential linear times reciprocal-root linear | `3*1=3` |
| Exponential constant times reciprocal-root quadratic | `3/2` |
| Total | `9` |

Thus the quadratic polynomial is `Q_0(x)=1+4x+9x^2`, and the local statement is `g(x)=Q_0(x)+O(x^3)`, or `g(x) approximately Q_0(x)`. It is not an exact identity between `g` and the polynomial.

Since the squared coefficient is `g''(0)/2`, `g''(0)=18`. A separate derivative check uses `g'/g=3+1/(1-2x)`. At zero this equals `4`, and its derivative equals `2`. Therefore `g''(0)=g(0)(4^2+2)=18`.

Multiplying the displayed quadratic factors produces cubic terms as well, such as `(3x)((3/2)x^2)=(9/2)x^3`. Such a term is beyond the retained degree. It also cannot by itself certify the full cubic coefficient, because the omitted cubic terms of each factor contribute at the same degree. Exact rational expansion through one further order independently gives the true cubic coefficient `16`, while the product of the quadratic truncations alone contributes only `9` at that degree. Neither cubic contribution belongs in the requested degree-at-most-two polynomial.

## E6. Choosing accuracy in the clock model

The stipulated model defines `T` as the moving clock's elapsed proper time and `T'` as the inertial frame's elapsed coordinate time between those same clock events. Let `epsilon=(v/c)^2`. Here

`epsilon=(0.02)^2=0.0004`.

The dimensionless factor has expansion

`(1-epsilon)^(-1/2)=1+epsilon/2+(3/8)epsilon^2+O(epsilon^3)`.

With `T=1000 s`, the estimate linear in `epsilon` is

`T'_L=1000(1+0.0004/2)=1000.2 s`.

The estimate quadratic in `epsilon` is

`T'_Q=1000[1+0.0004/2+(3/8)(0.0004)^2]=1000.20006 s`.

Using the supplied comparison value `1000.200060020007 s`:

| Estimate | Absolute error | Below `0.00001 s`? |
|---|---:|---|
| Linear in `epsilon` | `0.000060020007 s = 6.0020007e-5 s` | No |
| Quadratic in `epsilon` | `0.000000020007 s = 2.0007e-8 s` | Yes |

Only the quadratic-in-`epsilon` estimate meets the stated requirement. Independent 65-digit evaluation of the model begins `1000.200060020007002520924343... s`; the reference rounding cannot change either tolerance decision.

Because `epsilon=(v/c)^2`, the first correction `epsilon/2` is `(v/c)^2/2`: linear order in `epsilon` is already quadratic order in `v/c`. The next correction, `3epsilon^2/8`, is fourth order in `v/c`. The factor multiplying `T` is dimensionless; both estimates and their errors retain seconds.

One reason this is not a complete GPS clock calculation is explicit in the model: it neglects gravity. It cannot account for effects of the differing gravitational environment of a satellite clock and an Earth-based clock. No gravitational correction is calculated or assumed from this equation.

## E7. Later return and method choice

I reconstructed the coefficient relations from derivative matching without reopening earlier material during this prompt-solving phase. This is a reviewer reconstruction, not evidence about a learner's retention.

Let `h=x-a` and propose `P(x)=A+Bh+Ch^2`. At the basepoint, `P(a)=A`, `P'(a)=B`, and `P''(a)=2C`. Matching the given function's value, slope and second derivative requires

`A=f(a)`, `B=f'(a)`, `C=f''(a)/2`.

Hence

`L_a(x)=f(a)+f'(a)(x-a)`

and

`Q_a(x)=f(a)+f'(a)(x-a)+[f''(a)/2](x-a)^2`.

For the supplied data, `a=2` and `h=2.03-2=0.03`. The linear polynomial predicts `L_2(2.03)=5`, because the basepoint slope is zero. The quadratic correction is

`(-6/2)(0.03)^2=-3(0.0009)=-0.0027`.

Thus `f(2.03) approximately Q_2(2.03)=4.9973`. The quadratic term captures the local downward curvature that the horizontal tangent omits.

The proposed universal claim is false in both parts. First, `f''(a)` may be zero, as for sine at zero, so the degree-at-most-two Taylor polynomial need not contain a nonzero squared term. Second, derivative matching is local and does not ensure a quadratic polynomial is strictly more accurate at every input. If the second derivative is zero, the two polynomials coincide. Even when it is nonzero, they can behave differently at a specified nonzero displacement.

A counterexample using exactly the supplied derivative data is the smooth family

`f_C(2+h)=5-3h^2+C h^3`.

Every member has `f_C(2)=5`, `f_C'(2)=0` and `f_C''(2)=-6`, with continuous second derivative. At `h=0.03`, its absolute quadratic error is `|C|*0.000027`. Choosing `C=100` gives `f_C(2.03)=5`: the linear prediction is exact there, while the quadratic error is `0.0027`. Choosing larger `|C|` can make the fixed-input quadratic error arbitrarily large while preserving all the supplied derivative data.

Continuous second derivative near the basepoint supports the local statement that the quadratic remainder becomes small compared with `h^2` as `h` tends to zero. It does not specify a numerical neighborhood or certify an absolute tolerance at `h=0.03`. A numerical guarantee requires additional quantitative control of how the derivatives vary, a suitable remainder bound, or an independently known reference value. With the nonzero `f''(2)` here, the quadratic approximation does improve on the linear one sufficiently close to the basepoint for each fixed sufficiently smooth function; the supplied data alone do not identify how close is sufficient.

## Verification boundary

Arithmetic was checked using exact rational coefficient convolution and high-precision Decimal evaluation in `prompt-arithmetic-checks.json`. All demanded parts E1-E7 are covered above. No accuracy verdict about the upcoming lesson follows from these answers alone. Their role is to preserve independently obtained results for the later comparison against the exact frozen teaching and its supplied warrants.
