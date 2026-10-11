# D007 r29 root source-audit and content comparison

Scope: root read the complete frozen lesson (lines 1–180 and 181–341), complete 43-line hints file, complete 149-line solutions file, and actually viewed the exact full PNG figure. Root also read the full independent original-only D007 audit and the independent prompt calculations. This is a post-freeze comparison, not a fresh SASIS run, a new full-baseline read, or a claim that root independently reread every original PDF page in this cycle. The technical reviewer independently read those originals.

Frozen identity is in `d007-clean-r29-20261011/freeze-manifest.json`: lesson SHA256 `fd7a5dc52b8c143c8ba392b494ac879ad2722b0231dd21b3dadb50d0eedd988d`; hints `d80b7cad63ec6b575b0d567dd4f4213ec4ea77b1ff61525f479859651a659a0c`; solutions `3716815362b8d3c4240fffeb8cc5e95dd524939a99c9d6c0b9a189976ae035de`; PNG `0a97913b20995af483fe384be00ca172ac921c2ca722693280cdd00ed9cb2126`.

All five original-audit qualifications have clear corresponding treatment:

| Source-audit item | Frozen teaching comparison |
|---|---|
| F01, differentiation-rule hypotheses | Section 2 specifies differentiable constituent functions, constant coefficient, nonzero quotient denominator and differentiability at relevant outer inputs. |
| F02, implicit cubic division/branch | Section 3 treats a local differentiable branch, derives the exact coefficient equation before dividing, checks the concrete point, and explicitly withholds division when the coefficient vanishes. The source does not require solving its exceptional-point geometry; no unsupported global branch claim is made. |
| F03, inverse-sine branch/domain | Section 5 identifies the principal interval, derives the positive square root from cosine's sign, and distinguishes function endpoints from the open finite-derivative domain. P6 and its solution apply these distinctions to a changed inner input. |
| F04, real-power/logarithm domain | Section 6 holds the exponent constant, restricts the general real-power and logarithmic arguments to positive inputs, and distinguishes selected integer/rational extensions. Both required source methods are present. |
| F05, angle convention | Radians are stated in the starting toolkit, trigonometric derivation and P4. The two limit premises are supplied rather than derived circularly from the derivatives being proved. |

The source's hyperbolic definitions, derivative signs and identity, general rules, implicit cubic, inverse differentiation, elementary derivative deductions, two real-power routes and final nested exponential example are present. The source audit reports no demonstrated printed formula error requiring correction. The new figure supplements the source's hyperbola/circle relation and correctly shows only the right hyperbola branch traced by cosh/sinh.

All six exercise solutions, including both P6 parts, agree with the prior blind independent calculations. The important decisions are supplied: inner derivative signs; original quotient exclusions; both product contributions in the implicit equation; fixed versus varying quantities in the difference quotient; constant versus variable exponent; and inverse-function versus finite-derivative domains. The P5 countercheck at x=e discriminates the mistaken constant-exponent substitution whereas x=1 would not. The complete answers do not replace the separately provided useful hints.

Root saw the whole figure canvas. Its two coordinate systems, plotted branches, five marked points, parameter labels, axes and titles are present. The three orange hyperbolic coordinates match the equations and caption. All labels are readable at the native image size. Final embedded-size visibility and all math/link preservation remain separate actual-GitHub checks.

No material mathematical, original-source-coverage or answer defect is established by this scoped comparison. This is not global acceptance: independent technical review, fresh full-baseline SASIS, author-state review, and actual destination preservation/visual/navigation gates remain required. No frozen content was modified and no subject finding was supplied before freeze.
