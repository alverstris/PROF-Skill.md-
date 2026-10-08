# D003 independent mathematical and source check — original report

Role: independent mathematical/source checker, not SASIS. This report checks source fidelity, algebra, limits, and assumptions. It makes no claim about reader accessibility or reader performance. It was written before receipt of proposed task solutions. No D001/D002 material or full baseline was consulted.

## Source examined and identity

- File: `/workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L03/lec3.pdf`.
- Independently computed SHA-256: `ccf25930cfad63d99e3fd5045e7931860051bbbb3eedd2bd8cd9318ebd32845a`, matching the assigned source identity exactly.
- Read all five actual extractions, `lec3-p01.txt` through `lec3-p05.txt`, and inspected all five corresponding page images, `lec3-p01.png` through `lec3-p05.png`. The images govern when extraction and visible equations disagree.
- PDF page 1 is the MIT OpenCourseWare cover. PDF pages 2–5 carry printed lecture page numbers 1–4. All locators below distinguish these two numbering systems.

## Source errors versus extraction errors

| Locator | Visible source evidence | Mathematical finding |
|---|---|---|
| PDF p2 / printed p1, “General Examples” | The sum rule has its prime, but the constant multiple example visibly reads `(cu) = cu′`. | This is a genuine missing prime in the source. The intended rule is `(cu)′ = cu′`, as confirmed by the final sentence of the sum-proof block on the same page. Without that prime, the statement is generally false. |
| PDF p2 / printed p1, sum-proof heading | The heading visibly reads `Proof of (u+v) = u′+v′`. | This is a second genuine missing prime in the source. The following displayed proof begins and ends with `(u+v)′(x)`, identifying the intended rule. |
| PDF p3 / printed p2, immediately above “Product formula” | The image displays `d(cos x)/dx = −sin x`. | The extraction drops the sine term. That omission is an extraction defect, not a missing result in the source. |
| PDF p5 / printed p4, final quotient formula | The image displays `(u/v)′ = (u′v − uv′)/v²`. | The extraction's final denominator resembles `u2` and loses surrounding structure. The actual source denominator is `v²`, and its sign and numerator order are correct. |

The two visible missing primes need explicit correction in any faithful mathematical restatement; they must not be described as merely OCR mistakes.

## General derivative formulas and their hypotheses

Locator: PDF p2 / printed p1, “Derivative Formulas,” notation convention, and sum proof.

The source distinguishes specific functions, such as `xⁿ` and `1/x`, from rules for arbitrary functions `u` and `v`. Its notation means pointwise operations: `(u+v)(x)=u(x)+v(x)` and `(uv)(x)=u(x)v(x)`. It does not compute a general power rule in this block; its examples should not be inflated into such a claim.

For functions defined near a fixed point `x` and differentiable there with finite derivatives, and a constant `c`, the correct general formulas are

`(u+v)′(x)=u′(x)+v′(x)` and `(cu)′(x)=c u′(x)`.

For nonzero `h`, the difference quotient of the sum is exactly the sum of the two difference quotients. Taking their finite limits yields the sum rule. For the constant multiple, the quotient is exactly `c[u(x+h)−u(x)]/h`, whose limit is `c u′(x)`. The constant condition is necessary: if `c` depends on `x`, this is a product rather than the stated constant multiple rule. The source explicitly calls `c` a constant. It does not explicitly restate the differentiability hypotheses in this first block, so they should accompany a precise version of the rules.

## Trigonometric limits and the radian convention

Locators: PDF p2 / printed p1, “Derivatives of sin x and cos x,” through the bottom difference quotient; PDF p3 / printed p2, top addition identity and the sine/cosine derivative conclusions.

The source explicitly imports `lim(h→0) sin(h)/h = 1` from the previous lecture. It then uses `lim(h→0) [cos(h)−1]/h = 0`. The angle unit is not stated on these pages. The value `1` in the first limit, and hence the derivative formulas without any conversion factor, imply that the variable measures angles in radians. This is an inference from the displayed equations, not an explicit sentence in the source. For a degree-valued variable `t`, `sin_deg(t)=sin(πt/180)` instead gives a limit and sine derivative factor of `π/180`; the cosine-limit value alone would not identify the unit.

The cosine limit can be derived without presupposing the derivative being proved. With `t=h/2`, the half-angle identity gives

`[cos(h)−1]/h = −sin(t)[sin(t)/t] → 0`.

Here `sin(t)/t→1`, and `sin(t)=t[sin(t)/t]→0`. Thus the claimed cosine limit follows from the imported sine limit and a trigonometric identity. This derivation supplies support that is not written out in this source block.

For fixed `x`, the source's sine addition formula gives the exact quotient

`[sin(x+h)−sin(x)]/h = sin(x)[cos(h)−1]/h + cos(x)sin(h)/h`.

Its limit is `sin(x)·0 + cos(x)·1 = cos(x)`. In this limit `x` is fixed; only `h` tends to zero. The same expansion with the cosine addition identity gives

`[cos(x+h)−cos(x)]/h = cos(x)[cos(h)−1]/h − sin(x)sin(h)/h → −sin(x)`.

This verifies the source's “similar calculation” claim and the negative sign. The special values at `x=0` are `sin′(0)=1` and `cos′(0)=0`. The source takes the fundamental sine limit as prior knowledge; this report does not pretend these pages establish it from scratch.

## Differentiability implies continuity

Locator: PDF p3 / printed p2, note following the product proof and final paragraph.

The source states that having derivatives implies continuity and uses `u(x+h)→u(x)`. It does not prove that implication on these pages. A direct proof, independent of the product rule, is:

For `h≠0`, `u(x+h)−u(x) = h·[u(x+h)−u(x)]/h`. Since the bracket tends to the finite derivative `u′(x)`, the product tends to `0`. Therefore `u(x+h)→u(x)`, which is continuity at the point. The same reasoning applies to `v`.

This supplies the exact premise needed by the product proof without circularly using the product rule. Differentiability at the point is sufficient; a continuous derivative is not required. In the source's chosen product rearrangement, it is specifically continuity of `u` that is used in the shifted factor, although both functions are continuous under the stated differentiability assumptions.

## Product proof: exact add/subtract identity

Locator: PDF p3 / printed p2, “Product formula (General)” and its displayed proof.

The inserted zero is precisely `u(x+h)v(x)−u(x+h)v(x)`. Thus for `h≠0`,

`[u(x+h)v(x+h)−u(x)v(x)]/h`

`= ([u(x+h)−u(x)]/h)v(x) + u(x+h)([v(x+h)−v(x)]/h)`.

Expanding the right side cancels the two inserted mixed terms and recovers the original numerator; no sign error or shifted-factor error occurs. The two difference quotients tend to `u′(x)` and `v′(x)`, and `u(x+h)→u(x)` by the direct continuity argument above. Sum and product limit laws therefore yield

`(uv)′(x)=u′(x)v(x)+u(x)v′(x)`.

The source algebra is valid. A precise proof must preserve the shifted factor `u(x+h)` until its limit is justified; replacing it by `u(x)` before taking the limit is not an exact algebraic equality.

## Increment proof: the corner term after division

Locator: PDF p4 / printed p3, rectangle figure, definitions of `Δu` and `Δv`, and final instruction to divide by `Δx` and take a limit.

At the fixed point `x`, abbreviate `u=u(x)`, `v=v(x)`, `Δu=u(x+h)−u(x)`, and `Δv=v(x+h)−v(x)`. The exact algebra is

`(u+Δu)(v+Δv)−uv = uΔv + vΔu + ΔuΔv`.

The red and yellow terms in the source's figure are `uΔv` and `vΔu`; the white corner is `ΔuΔv`. The source says the corner is small and writes an approximation before asking the reader to divide by `h`. Merely knowing `ΔuΔv→0` does not justify omitting it after division by a quantity also tending to zero.

The needed statement is

`ΔuΔv/h = (Δu/h)Δv → u′(x)·0 = 0`,

using differentiability of `u` and continuity of `v`. Equivalently, since both finite derivatives exist,

`ΔuΔv/h = h(Δu/h)(Δv/h) → 0`.

After dividing the exact identity by `h`, these facts yield the product rule. This completes the source's intuitive argument under its differentiability assumptions.

The distinction is substantive: at `x=0`, let `u(x)=v(x)=√|x|`. Both increments tend to zero and their product is `|h|→0`, but `ΔuΔv/h=|h|/h` fails to tend to zero. These functions are not differentiable at zero, illustrating why “small increments” alone are insufficient. The pictured areas use positive side lengths and positive increases; the exact increment algebra and limit proof remain valid for signed increments, so the diagram need not be treated as an all-signs geometric proof.

## Quotient rule and local nonvanishing

Locator: PDF p5 / printed p4, “Quotient formula (General),” common-denominator calculation, and limit arrow.

Assume `u` and `v` are defined near `x`, differentiable at `x`, and `v(x)≠0`. Abbreviate values and increments as above. The exact numerator is

`(u+Δu)v−u(v+Δv) = vΔu−uΔv`.

Consequently, for sufficiently small nonzero `h`,

`(1/h)[(u+Δu)/(v+Δv)−u/v]`

`= [v(Δu/h)−u(Δv/h)]/[(v+Δv)v]`.

Continuity of `v` gives `Δv→0`. More precisely, because `v≠0`, choose a neighborhood in which `|Δv|<|v|/2`; then `|v+Δv|≥|v|−|Δv|>|v|/2>0`. Thus the shifted denominator is nonzero throughout a sufficiently small neighborhood, and `(v+Δv)v→v²≠0`. The quotient limit law now gives

`(u/v)′(x)=[u′(x)v(x)−u(x)v′(x)]/[v(x)]²`.

The source's algebra, sign, and final squared denominator are correct. The explicit condition `v(x)≠0` is missing from these pages and is essential. Nonvanishing of `v` everywhere is unnecessary: its continuity and nonzero value at the differentiation point supply the needed local condition. If `v(x)=0`, the source quotient `u/v` is undefined at that point, even when a separately defined extension might exist; the stated formula cannot be used there.

## Findings to preserve in later checks

1. Correct two real source typos: the absent prime on `(cu)` in the initial general examples, and the absent prime on `(u+v)` in the sum-proof heading (PDF p2 / printed p1).
2. State that the trig formulas use radians; describe this as inferred from the source's unit-normalized sine limit (PDF pp2–3 / printed pp1–2).
3. Supply a noncircular difference-quotient proof of differentiability implying continuity when that implication is part of the explanation (PDF p3 / printed p2).
4. Preserve the exact add/subtract product identity and justify the limit of the shifted factor (PDF p3 / printed p2).
5. Show `ΔuΔv/h→0`; an unscaled “small corner” claim alone is insufficient (PDF p4 / printed p3).
6. State `v(x)≠0` and derive local nonvanishing from continuity for the quotient proof (PDF p5 / printed p4).
7. Do not copy extraction defects into mathematical claims: the cosine derivative and quotient denominator are complete and correct in the images (PDF pp3 and 5).

This original report is to be preserved without replacement by later solution-aware checks.
