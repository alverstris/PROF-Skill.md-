# D003 independent original task check — before proposed solutions

Role: mathematical/source checker, not SASIS. This report solves and checks only the original prompts in `task-prompts-before-solutions.md`, using the already completed independent source analysis. No proposed solutions or complete learner document were read before these results were written. No reader accessibility or baseline comparison is claimed.

The assigned source SHA-256 remains `ccf25930cfad63d99e3fd5045e7931860051bbbb3eedd2bd8cd9318ebd32845a`. Relevant source locators are identified below using PDF pages, with printed lecture pages in parentheses.

## A. Calibrated reading

Source relation: sum and constant multiple rules, PDF p2 (printed p1), with the source's missing primes corrected as documented in the original source check.

Since `2` is constant and both functions are differentiable at `t₀`,

`r′(t₀)=2a′(t₀)−b′(t₀)=2(0.30)−0.40=+0.20 V/s`.

The instantaneous rate is positive: the calibrated reading is increasing at this instant in the prompt's expressly defined sense. This conclusion is not a claim that the function is monotone on a whole time interval. A derivative of the coefficient is not included because the coefficient is fixed. Both terms have voltage-per-time units and their difference has the same units.

## B. Area rate and scaled error

Source relations: product proof, PDF p3 (printed p2); increment rectangle and corner term, PDF p4 (printed p3).

For `A(t)=u(t)v(t)`,

`A′(t₀)=u′(t₀)v(t₀)+u(t₀)v′(t₀)`

`=(−0.2 m/s)(4 m)+(3 m)(0.5 m/s)=−0.8+1.5=+0.70 m²/s`.

The area has a positive instantaneous rate. One side is shortening, but its `−0.8 m²/s` contribution is outweighed by the other side's `+1.5 m²/s` contribution.

At fixed `t₀`, abbreviate `u=u(t₀)`, `v=v(t₀)`, `Δu=u(t₀+h)−u(t₀)`, and `Δv=v(t₀+h)−v(t₀)`. The exact identity is

`ΔA=uΔv+vΔu+ΔuΔv`.

After division by nonzero `h`, the discarded term would be `ΔuΔv/h`, so the assertion in the prompt is invalid as stated: `ΔuΔv→0` alone does not control the scaled term. Under the given differentiability assumptions,

`ΔuΔv/h = h(Δu/h)(Δv/h) → 0·u′(t₀)·v′(t₀)=0`.

Both derivatives are finite. Alternatively, `(Δu/h)Δv→u′(t₀)·0` follows from differentiability of `u` and continuity of `v`. Thus the product rule is justified without treating an approximation as an exact identity.

An explicit check of why the unscaled claim is insufficient is `Δu=Δv=√|h|`: their product tends to zero, but their product divided by `h` is `|h|/h`, which does not tend to zero. These increments do not satisfy the assumed differentiability at zero; that is precisely the missing hypothesis in the invalid argument.

Here the actual side lengths are positive (`3 m` and `4 m`). A negative change in `u` means a positive side is getting shorter, not that the side length becomes negative. Continuity keeps both side lengths positive for sufficiently small time changes. Since `u′(t₀)<0`, `Δu` is negative for sufficiently small positive `h`; the exact algebra also handles negative `h` and signed increments.

## C. Original quotient versus extension

Source relation: quotient formula, PDF p5 (printed p4), qualified by nonzero denominator.

The original domain is `ℝ\{1}`. For every `x≠1`, factorization gives

`q(x)=[(x−1)(x+1)]/(x−1)=x+1`.

This equality on the specified domain proves `q′(x)=1` for every `x≠1`. A quotient-rule check gives

`q′(x)=[2x(x−1)−(x²−1)]/(x−1)²=(x−1)²/(x−1)²=1`,

again only for `x≠1`. The derivative `q′(1)` does not exist because the function `q` is not defined at `1`; cancelling a factor does not supply that absent value.

The separately defined `Q` has domain `ℝ` and satisfies `Q(x)=x+1` at every real input, including `Q(1)=2`. Directly,

`[Q(1+h)−Q(1)]/h=[(2+h)−2]/h=1` for `h≠0`.

Therefore `Q′(1)=1`. This is a derivative of the extension `Q`, not a retroactive definition of `q′(1)`.

## D. Retrieval of rules and limiting warrant

At a fixed interior point `x`, suppose the component functions are defined on a neighborhood of `x` and have finite derivatives there at `x`. Let `c` be constant. The rules are

| Operation | Derivative | Additional condition |
|---|---|---|
| Sum | `(u+v)′(x)=u′(x)+v′(x)` | Both derivatives exist at `x`. |
| Constant multiple | `(cu)′(x)=c u′(x)` | `c` is independent of `x`; `u′(x)` exists. |
| Product | `(uv)′(x)=u′(x)v(x)+u(x)v′(x)` | Both derivatives exist at `x`. |
| Quotient | `(u/v)′(x)=[u′(x)v(x)−u(x)v′(x)]/[v(x)]²` | Both derivatives exist and `v(x)≠0`. |
| Sine | `(sin x)′=cos x` | Real angle variable in radians; every real `x`. |
| Cosine | `(cos x)′=−sin x` | Real angle variable in radians; every real `x`. |

These general hypotheses are sufficient conditions for the rules; they should not be mistaken for a necessary characterization of when an isolated sum or product might happen to have a derivative. In the quotient case, continuity of `v` and `v(x)≠0` imply that `v` stays nonzero in a sufficiently small neighborhood. One does not need to assume it is nonzero at every possible input.

For increments `Δu=u(x+h)−u(x)` and `Δv=v(x+h)−v(x)`, and unshifted abbreviations `u=u(x)`, `v=v(x)`,

`(u+Δu)(v+Δv)−uv = uΔv+vΔu+ΔuΔv`.

Then

`[(u+Δu)(v+Δv)−uv]/h = u(Δv/h)+v(Δu/h)+h(Δu/h)(Δv/h)`.

As nonzero `h→0`, the first two terms tend to `uv′` and `vu′`; the last tends to zero because both difference quotients have finite limits. This is the required limiting warrant, beyond recall of the formula. It is valid for signed increments.

Source locators: sum/constant multiple, PDF p2 (printed p1); trigonometric rules and product rule, PDF pp2–3 (printed pp1–2); increment identity, PDF p4 (printed p3); quotient, PDF p5 (printed p4). Radians are inferred from the displayed sine limit, as documented in the original source check.

## E. Trigonometric quotient and representation domains

Source relations: trigonometric derivative formulas, PDF p3 (printed p2); quotient formula, PDF p5 (printed p4). All angles in this task are expressly in radians.

The domain of `F(x)=sin x/(1+cos x)` is

`D_F = ℝ\{(2k+1)π : k∈ℤ}`,

because `1+cos x=0` exactly at odd multiples of `π`. The denominator is nonzero at every point in this domain, and the sine/cosine functions are differentiable there. Therefore

`F′(x)=[cos x(1+cos x)−sin x(−sin x)]/(1+cos x)²`

`=[cos x+cos²x+sin²x]/(1+cos x)²`

`=(1+cos x)/(1+cos x)²=1/(1+cos x)` for `x∈D_F`.

Consequently `F′(π/3)=1/(1+1/2)=2/3`.

The domain of `G(x)=(1−cos x)/sin x` is

`D_G = ℝ\{kπ : k∈ℤ}`.

Its denominator vanishes at every integer multiple of `π`, so `D_G` is a proper subset of `D_F`. On the common domain, which is exactly `D_G`,

`sin x/(1+cos x) = sin x(1−cos x)/[(1+cos x)(1−cos x)]`

`=sin x(1−cos x)/sin²x=(1−cos x)/sin x`.

The divisions in this derivation are permitted on that common domain. Alternatively, cross multiplication verifies the equality using `sin²x=1−cos²x`, provided both original denominators are nonzero. That identity does not erase the denominator conditions.

In particular, `F(0)=0`, whereas `G(0)` is undefined. Thus `G` cannot be substituted wholesale as the function in the difference quotient for `F′(0)`: writing `[G(h)−G(0)]/h` is invalid. The ordinary derivative `G′(0)` does not exist for the stated function `G`.

There is an important qualification: for sufficiently small nonzero `h` (for example `0<|h|<π`), both expressions are defined and `G(h)=F(h)`. It is valid to replace the shifted value `F(h)` by `G(h)` inside `[F(h)−F(0)]/h` while retaining the actual value `F(0)=0`. A punctured-neighborhood equality may be used in a limit; it simply does not manufacture `G(0)`. An explanation that forbids any such use of `G(h)` would be too strong.

A direct valid route is the quotient derivative above, since `1+cos 0=2≠0`: `F′(0)=1/2`. The defining limit independently verifies it:

`[F(h)−F(0)]/h = [sin h/h]/(1+cos h) → 1/2`.

If one chooses the qualified replacement route instead,

`[G(h)−F(0)]/h=(1−cos h)/(h sin h)`

`=sin h/[h(1+cos h)] → 1/2`,

again using equality only at the nonzero nearby inputs where the expressions are both defined. Defining a new extension with value zero at the even multiples of `π` can recover `F` on its domain, but the task's original `G` does not contain those values.

## Comparison anchors for later proposed solutions

- A: `+0.20 V/s`, positive instantaneous rate; no whole-interval monotonicity claim.
- B: `+0.70 m²/s`, positive instantaneous area rate; the scaled corner term, not only the unscaled product, must tend to zero. Signed increments do not imply negative side lengths.
- C: `q′(x)=1` for `x≠1`; `q′(1)` is absent; the separately defined extension has `Q′(1)=1`.
- D: all six rules, finite derivative assumptions, constant coefficient, nonzero quotient denominator locally supported by continuity, radian convention, exact increment identity, and vanishing scaled cross term.
- E: `D_F=ℝ\{odd multiples of π}`, `D_G=ℝ\{all integer multiples of π}`, equality on `D_G`; `F′=1/(1+cos x)` on `D_F`; `F′(π/3)=2/3`; `F′(0)=1/2`; no `G(0)` or `G′(0)` for the given `G`. Allow qualified use of `G(h)` on a punctured neighborhood while retaining `F(0)`.

This original report is preserved as the pre-solution mathematical result and should not be overwritten by later comparison commentary.
