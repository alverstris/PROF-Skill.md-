# D003 technical document check — original v1 comparison

Disposition: **bounded technical pass for the inspected candidate**. No mathematical defect requiring a correction was found in P01–P44 or in the inspected rectangle image. This is a check of mathematical statements, assumptions, source fidelity, exact data, and proposed solutions. It is not an accessibility assessment, a baseline comparison, evidence of a learner's performance, or approval of a later revision.

## Inspected artifacts and independent anchors

The entire actual `teaching-v1.md` was read, including every teaching paragraph, attempt, hint, and complete solution. The complete `product-increment-v1.png` was visually inspected. The candidate was compared with the independently written source analysis and pre-solution task results; neither original report was changed.

| Artifact | SHA-256 at this check |
|---|---|
| `teaching-v1.md` | `4d577f225e8aca3e209752b6f16c63b2c37de497896f92bf43b34a8d5ee80c69` |
| `product-increment-v1.png` | `61bc47e951267028b32ac0007370244d8d6489e8552639572a56bdf5cc2ad2b0` |
| `technical-source-check-original.md` | `e75c84ddf3eefd75565e145a80a00fffb96a56727759f787ba1b7e1ed292e9bb` |
| `technical-task-check-original.md` | `dee576b0162ea3d11efa631b84da034811c112b637a6e4ab8b7ee0bbe527dc02` |

The source independently checked earlier is `lec3.pdf`, SHA-256 `ccf25930cfad63d99e3fd5045e7931860051bbbb3eedd2bd8cd9318ebd32845a`. Its PDF pp2–5 are printed lecture pp1–4. Source text and all five page images were examined in the original source check.

## Paragraph-specific claims and proof checks

| Paragraphs | Check and deduction |
|---|---|
| P01–P03 | The stated scope is consistent with the actual mathematical content: rules are connected to difference quotients and used with pointwise rates. These framing paragraphs do not claim additional mathematical results. No learner-accessibility conclusion is drawn from them. |
| P04 | Sum, product, and quotient are pointwise operations on outputs at the same input. The quotient explicitly retains `v(x)≠0`. The distinction from composition is correct. Keeping `x` fixed and letting only the increment `h` tend to zero is the correct derivative setup. |
| P05 | The derivative is a two-sided finite limit on a neighborhood, consistent with the standing open-interval assumption. The numerical sum, product, and quotient limit laws are stated with finite limits and a nonzero denominator limit. `A→3`, `B→0` implies `AB→0` but does not determine `A/B`, as claimed. |
| P06–P07 | The sum quotient splits by exact algebra. Differentiability supplies both finite limits. A fixed `c` factors out, and `c=−1` correctly gives subtraction. A varying coefficient would require the product rule. Both primes missing in the original source's separate listing/title are present in the candidate's mathematical rules. |
| P08–P09 | The worked calibration uses coefficient `3` and rates `0.2`, `0.5`, giving `3(0.2)−0.5=0.1 V/s`. Attempt A intentionally uses different data: coefficient `2`, rates `0.30`, `0.40`, giving `0.20 V/s`. Neither set was accidentally substituted into the other. The instantaneous-sign interpretation is properly bounded. |
| P10 | Both trigonometric limit premises are stated explicitly, with radians. The first yields sine derivative `1` at zero and the second cosine derivative `0` at zero. A quotient may be undefined exactly at the limiting input. The source imports the sine limit from earlier work; the candidate does not claim to rederive that fundamental limit here. |
| P11–P12 | The sine and cosine addition identities are correct. Subtraction and division give respectively `sin x (cos h−1)/h + cos x sin h/h` and `cos x (cos h−1)/h − sin x sin h/h`. Their limits are `cos x` and `−sin x`. The fixed factors legitimately leave the `h`-limits. At `π/3`, these slopes are `1/2` and `−√3/2`. |
| P13 | For the numerical degree variable `d`, substitution `k=πδ/180` gives a multiplier `π/180`, not its reciprocal. The base angle is `πd/180`. Both resulting derivative formulas and the slope at zero are correct; the argument derives the factor by increments without depending on an unstated chain-rule calculation. |
| P14 | The identity `u(x+h)−u(x)=h·[u(x+h)−u(x)]/h` for `h≠0` proves continuity from finite differentiability. The use of a product law for numerical limits is not circular use of the derivative product rule. |
| P15–P16 | The intermediate product is exactly `u(x+h)v(x)`. Expansion of the displayed regrouping cancels the inserted mixed terms and recovers the original product change. The factor `u(x+h)` is retained through the quotient and then tends to `u(x)` by P14. This yields `u′v+uv′` with no sign or shifted-factor error. |
| P17 | For `x sin x`, the derivative is `sin x+x cos x`, giving `−π` at `π`. The incorrect proposed rate-product rule would give `cos x`, which is a different expression. The counterexample `u=v=x` correctly contrasts `2x` with `1`, including the disagreement at zero. |
| P18 | The increments all use the same input change. The exact identity has all three terms: `Δ(uv)=uΔv+vΔu+ΔuΔv`. It correctly distinguishes a change in a product from the product of changes. |
| P19 and image | Widths are labeled `u` and `Δu`; heights are `v` and `Δv`. The orange, top red, right yellow, and white corner regions have the correct labels `uv`, `uΔv`, `vΔu`, and `ΔuΔv`. All four fill the outer rectangle. The text states the positivity assumptions for a literal added-area picture and preserves the algebra for signed values and changes. No geometric sign claim is being used to replace the general algebraic proof. |
| P20 | The relevant omitted contribution is checked after division: `(ΔuΔv)/h=(Δu/h)Δv→u′·0=0`. Differentiability and P14 provide the two needed limits. The counterexample `h/h=1` validly refutes the general inference “numerator tends to zero, so the quotient does too.” The remaining terms give the product derivative. |
| P21 | Attempt B exactly preserves `u=3 m`, `v=4 m`, `u′=−0.2 m/s`, `v′=0.5 m/s`; the prompt asks for both signed area rate and a scaled error argument. It does not substitute a negative side length for a negative rate. |
| P22 | At a point with `v(x)≠0`, continuity allows `|v(x+h)−v(x)|<|v(x)|/2` for every sufficiently small increment. The reverse triangle inequality then gives `|v(x+h)|>|v(x)|/2>0`. The example with `v(x)=2` correctly gives nearby values between `1` and `3`. The argument also holds when `v(x)<0`. |
| P23–P24 | Common-denominator subtraction gives exactly `vΔu−uΔv`; the denominator is `(v+Δv)v`. After division by `h`, the numerator tends to `vu′−uv′` and the denominator to nonzero `v²`. The final denominator is the original denominator's value squared, not a derivative squared. The stated sign interpretation is restricted to positive quantities and is consistent with the exact formula. |
| P25 | For `(x²+1)/(x+1)`, the stated domain is `x≠−1`. Expansion gives `2x(x+1)−(x²+1)=x²+2x−1`. At `x=1`, the derivative is `2/4=1/2`. Polynomial division yields `x−1+2/(x+1)`, and `1−2/(x+1)²` is the same derivative on the same domain. |
| P26 | Attempt C preserves the original domain `x≠1`, defines a distinct extension by `Q(1)=2`, and requests derivatives of the actual functions rather than silently cancelling a domain hole. |
| P27 | The conditions are explicitly called sufficient for the quotient rule, and the text says not to apply that rule when its conditions fail. It does not assert that failure of a component derivative necessarily destroys differentiability of an otherwise defined quotient. The separate-function observation correctly covers a possible extension when the original formula is undefined. The product statement expressly avoids the converse. Starting with the actual domain is valid and is not contradicted by P44's carefully qualified punctured-neighborhood use. |
| P28 | The summary correctly identifies the exact manipulations and limit conditions used in the actual proofs. No new unsupported mathematical conclusion appears. |
| P29–P31 | The tasks distinguish formula retrieval from the cross-term limit warrant and the trigonometric transfer/domain issue. Attempt E preserves radians, `F=sin x/(1+cos x)`, evaluation at `π/3`, the alternative `G=(1−cos x)/sin x`, and the derivative question at zero. |
| P32 | The source identity/title, four teaching pages after the cover, Figure 1 attribution, and the two missing-prime descriptions agree with the inspected source. The candidate adds an explicit cosine addition calculation, continuity reasoning, corner-term limit, and quotient condition rather than reproducing the source's omissions. This checks the attribution against the local source, not the live status of the external URL. |
| P33–P39 | The hint and solution framing makes no additional mathematical claim. Each actual hint is checked below against its corresponding task and result. |

## Task, hint, and solution comparisons

| Task and paragraphs | Independent result | Candidate comparison |
|---|---|---|
| A: P09, P34, P40 | `r′(t₀)=2a′−b′=2(0.30)−0.40=+0.20 V/s`; positive instantaneous rate, no whole-interval monotonicity inference. | The hint keeps the fixed multiplier and subtraction on the correct rates. P40 has the exact relation, signed result, units, and bounded interpretation. |
| B: P21, P35, P41 | `A′=u′v+uv′=(−0.2)(4)+(3)(0.5)=+0.70 m²/s`. The corner contribution tends to zero as `(Δu/h)Δv`, or as `h(Δu/h)(Δv/h)`. | The hint identifies the correct scaled expression and the continuity requirement. P41 gives both independently checked limit routes, correct arithmetic and units, and the distinction between decreasing positive length and negative length. The invalid unscaled claim is explicitly rejected. |
| C: P26, P36, P42 | `q′(x)=1` for `x≠1`; `q′(1)` does not exist because `q(1)` does not exist. The separate extension satisfies `Q(x)=x+1` on all reals, so `Q′(1)=1`. | The hint focuses on legal cancellation and the actual point value. P42 retains the original restriction, identifies the missing original value, and verifies the new derivative with a valid difference quotient. |
| D: P30, P37, P43 | Six correct rules with differentiability, fixed coefficient, nonzero quotient denominator, radians; exact product increment identity and scaled cross-term limit. | P43 states every requested rule and condition. Its neighborhood and finite-derivative meanings inherit the explicit P05 convention. Local quotient existence is supplied by P22. The exact increment identity and `(Δu/h)Δv→0` argument match the independent solution. The hint properly keeps the cross term until after division. |
| E: P31, P38, P44 | `D_F=ℝ\{(2k+1)π}`, `D_G=ℝ\{kπ}`; equality on `D_G`; `F′=1/(1+cos x)` on `D_F`; `F′(π/3)=2/3`; `F′(0)=1/2`. | The quotient numerator, sign, cancellation, and all domains match. P38 permits multiplication by `(1−cos x)/(1−cos x)` only when it is defined. P44 explicitly uses the nonzero sine condition to justify both factors before cancellation. Neither an excluded odd multiple nor a missing even-multiple value is silently restored to `G`. |

## Focused qualification checks

**P27 — sufficient conditions and actual domains.** The candidate's statement does not make the invalid converse claim that an existing derivative of `u/v` requires differentiability of each chosen component. For example, `u=v=1+|x|` has a differentiable quotient at zero despite the nondifferentiable components; P27's instruction only forbids applying the proved quotient rule using missing derivatives. If the denominator itself is zero, the original quotient is undefined and a separately specified extension may have a derivative, as demonstrated in C. The wording remains mathematically defensible in both situations.

**P44 — the alternative expression near zero.** The solution makes both distinctions required by the independent result:

1. `[G(h)−G(0)]/h` is invalid because the given `G` lacks a value at zero.
2. `[G(h)−F(0)]/h` is valid for sufficiently small nonzero `h`, since there `G(h)=F(h)` and `F(0)=0` is defined.

For instance `0<|h|<π` supplies a common punctured neighborhood. Thus the solution neither silently extends `G` nor overstates the domain objection as a prohibition on all uses of `G(h)`. The independent derivative limit `F(h)/h=(sin h/h)/(1+cos h)→1/2` is valid. Continuity of cosine has already been established from its derivative via P14, so that justification is not circular.

## Bounds of this pass

The inspected version has correct mathematical claims, computations, domain restrictions, exact increment algebra, and limiting justifications within the stated prerequisites. It assumes the fundamental trigonometric limit(s), addition identities, elementary function derivatives used in examples, and numerical finite-limit laws, as the document says; it is not a reconstruction of all calculus foundations. No exact mathematical defect is identified for author correction in this version. Subsequent edits need a comparison with these inspected hashes before this result can be carried forward.

This report is the original solution-aware technical comparison and is preserved separately from both pre-solution reports.

## Author readback addendum — current candidate binding

After the full-document check above, the author reported four narrow edits and requested a targeted recheck. The preceding record, including the initial inspected teaching hash, is preserved. I reread the actual current P04, P23, P31, and P32 from disk after those edits; this addendum does not falsely describe those revisions as present during the initial full read.

- Current `teaching-v1.md` SHA-256: `cd7426a9b70d0ac41aa3ca0418db8c89c391b67304016a7ad38f8379fe98b5a8`.
- Rechecked `product-increment-v1.png` SHA-256: `61bc47e951267028b32ac0007370244d8d6489e8552639572a56bdf5cc2ad2b0`, unchanged from the inspected image.

| Changed paragraph | Targeted technical finding |
|---|---|
| P04 | The added specific/general distinction matches the source's distinction between derivative formulas for named functions and combination rules. It does not assert an additional unqualified power rule. Pointwise definitions and the quotient restriction remain correct. |
| P23 | The revised verbal interpretation now explicitly holds the other variable fixed for each individual effect. For positive values, increasing the numerator with denominator fixed raises the quotient; increasing the denominator with numerator fixed lowers it. The text correctly directs simultaneous changes back to the combined exact numerator `vΔu−uΔv`. The displayed algebra is unchanged and correct. |
| P31 | The prompt now asks specifically whether `[G(h)−G(0)]/h` may replace the defining quotient. The independent answer remains no because `G(0)` is absent, while the qualified use of `[G(h)−F(0)]/h` remains valid. This wording aligns exactly with P44 and does not prohibit the valid partial substitution. All functions and evaluation inputs remain unchanged. |
| P32 | Removal of the instructor attribution removes no mathematical information. The source, page-count statement, figure attribution, and exact missing-prime descriptions remain accurate against the source inspected earlier. |

**Current disposition:** the bounded technical pass carries forward to the current teaching hash above after these four targeted checks, with the initial full-document and image inspection retained as the underlying record. No new mathematical defect was found at these changed seams. This remains a mathematical/source check only and makes no unperformed baseline or learner-accessibility claim.
