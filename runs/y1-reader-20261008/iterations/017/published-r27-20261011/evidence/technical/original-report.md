# D017 r27 — original independent technical/source/PROF audit

Disposition: no verified material defect found in the complete frozen teaching route, its six prompts/hints/solutions, source coverage or locally inspected figures. This is a local independent author audit, not the SASIS report, evidence of human learning, or a global release/destination pass. The current document was not edited.

## Identity and actual access

- Teaching: `output/teaching.md`, SHA256 `0317f26777f5285616be96713d79e1731818fea76d40954f3e21be2c6dbcb7b5`, all 536 lines read sequentially, including source/scope and all help.
- Source: `inputs/source/lec19.pdf`, SHA256 `f3bccf9b801aebb3266932eb8a549f700e5a38f26d377c85f6fd96ed9e7fb3b7`. All five extracted page texts read; all five full page PNGs visually inspected at usable size. These are the cover and printed lecture pages 1–4, not five numbered lecture pages. Source equations and figures were checked against the images, not inferred from the defective text extraction.
- Operative skill: `inputs/prof/SKILL.md`, SHA256 `a8220e60802e9dc8f79bade1ad4d73e0d4afcccf8c8f1c0514927e4a08731c8e`, version 2026-10-11-r27, read completely. Parent supplied published pin `fb4db9390459b2b9b95c8c2db74d9cd6a335cb37`; this reviewer verified local bytes, not the remote pin. Relevant references read: complete execution-protocol.md; domain-patterns.md (including mathematics/physics); sasis.md; profile-manifest.json; rewrite-guide.md; student-testing-contract.txt; student-role.txt. No new method/research rule was proposed, so the historical research rationale was not needed for a change.
- Baseline: `inputs/student-baseline.txt`, SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`. This technical reviewer read operational Mathematics lines 1–218, mechanics 295–320, physics units/graphs 529–545 and motion 590–596, plus search results locating related rules. I did not read all 1377 baseline lines and do not claim to have done so. Every prerequisite used in the reconstruction below is in those inspected passages or explicitly taught by the lesson. The full-baseline author and full-baseline SASIS admission are separate roles/checks.
- `author/prompts-only.md` read and Q1–Q6 independently solved before opening the lesson or any proposed solution. Original answers saved first in `evidence/technical/independent-calculations.md`. No root solution record, historical generation, old diagnosis, sibling output or old commit diff was read.
- Both linked SVG files were exported locally with Inkscape and the exact exports visually inspected, including all canvas edges: `evidence/technical/signed-sine-from-svg.png` and `interval-addition-from-svg.png`. This checks local SVG content, not the eventual embedded GitHub surface.
- Current `author/route.txt`, `.prof-state/RUN.md` and `.prof-state/topics/ftc.json` read only after independent solving and full teaching review. Their pending acceptance state was checked with the coordinator; it intentionally awaits the integrated SASIS/destination evidence. No incomplete state was treated as an existing PASS.

Some initially batched tool output was truncated. The required skill/reference and lesson material was subsequently reopened in bounded chunks; no truncated result was accepted as full reading. The baseline limits above remain explicit.

## Original-source coverage and corrections

| Source portion actually inspected | Frozen teaching location | Technical/coverage witness |
| --- | --- | --- |
| Cover: MIT OCW, 18.01, Fall 2006 | 1–3, 533–535 | Title, course and term match the source; no lecturer identity is invented. |
| Printed p.1 FTC1 statement and endpoint notation | 14–36 | Same endpoint difference and MIT numbering; continuous integrand and endpoint/interior antiderivative conditions are made explicit. Brackets and evaluation bar are mapped, including construction from the intended operation. |
| Printed p.1 Example 1, arbitrary endpoints for x² | 38–52 | Derivative x³/3 → x² and b³/3−a³/3; constant cancellation is explicitly justified. |
| Printed p.1 Example 2 and Figure 1, positive sine hump | 104–138 and signed-sine.svg | −cos antiderivative gives 2 on [0,π]; first shaded hump reproduces the required sign/area relation. |
| Printed p.1 Example 3, x⁵ on [0,1] | 54–64 | x⁶/6 endpoint evaluation gives 1/6; derivative and sign check supplied. |
| Printed p.2 rate/position/rectangle-sum interpretation | 73–100 | Signed v=s′, sampled v(t*)Δt, summation and endpoint displacement are coherent. Source position symbol x(t) is consistently renamed s(t), not confused with an integration coordinate. |
| Printed p.2 odometer/speed wording and round trip | 73, 90–100, 140–148 | Source's initially loose identification of signed derivative with speed/odometer change is corrected: speed=|v|, odometer accumulates distance, displacement is signed. A −1/2,+1/2 trip gives displacement 0 and distance 1. This is a handled source imprecision, not a defect in the teaching. |
| Printed p.2 Example 4 and Figure 2, full sine cycle | 118–138 and signed-sine.svg | Second half-cycle −2, full cycle 0, geometric area 4. The source's two sine diagrams are combined with an explicit explanation of the combination. |
| Printed p.3 addition formula and Figure 3 | 155–175 and interval-addition.svg | Adjacent contributions are joined; F(b) cancels. The new positive curve has the same relevant interval/shading relationship, and the caption does not pretend the picture proves the negative-contribution case. |
| Printed p.3 reversed limits and arbitrary ordering | 177–207 | Negation is explicitly a definition; equal endpoints are added correctly. x² on [2,1] gives −7/3 despite positive integrand. Out-of-order addition gives 8/3−7/3=1/3. |
| Printed p.4 integral comparison | 214–228 | Pointwise comparison, forward order, continuity and sign reversal are correctly stated. Nonnegative rectangle sums of g−f justify the rule; neither f nor g individually has to be positive. |
| Printed p.4 Examples 5–6, exponential bounds | 230–253 | Constant lower bound gives e≥2; linear lower bound gives e≥5/2. The previously taught source inequality is reconstructed using h=eˣ−1−x and h′≥0. |
| Printed p.4 indefinite and definite change-of-variable forms | 260–284 | Chain rule gives the substituted antiderivative; differential factor and both new bounds are identified. The indefinite relation is supplied through the chain-rule/antiderivative connection rather than copied as a redundant separate equation. The source f=g∘u role is embodied by g(u(x)); no operation is omitted. |
| Printed p.4 Example 7 | 286–310 | u=x³+2, du=3x²dx, bounds 3 and 10, coefficient 1/15 and result (10⁵−3⁵)/15 all match. Independent direct polynomial expansion verifies it. |

All source figures' consequential content is covered. No formal FTC proof is promised by the source packet or the lesson; lines 24 and 535 honestly distinguish the supplied theorem and intuition from proof. A missing formal proof is not a verified omission here.

## Prerequisite and reconstruction evidence

The following are actual inspected operational baseline rules, not assumed knowledge from qualification names:

| Needed premise | Baseline location | Use in this lesson |
| --- | --- | --- |
| Signed arithmetic, substitution, factorisation, powers, units | 28–32, 46–60 | Endpoint calculations, cancellation, Q1, Q3, sign splits in Q2/Q6. |
| Interval bracket notation, domains and function composition | 30, 62 | Closed interval conditions; G(u(x)), meaning of new endpoint values. |
| Inequality negation and polynomial sign intervals | 58 | Reversed comparison and sign analysis at 1. |
| Modulus is x or −x by sign | 60 | Speed, magnitude of signed pieces and geometric area. |
| Sigma as sum of indexed terms | 76–78 | Rectangle sum at lines 81–88; local text adds n, i, sample star and Δt. |
| Radians, sine/cosine signs and exact values | 101–103 | Half/full sine cycle and graph interpretation. |
| Exponential positivity/growth and derivative | 130, 144–156 | eˣ≥1; h′=eˣ−1; exponential antiderivative. |
| Derivative as local rate; chain rule; derivative sign and growth | 138–168 | Accumulated rate interpretation, h nondecreasing, substitution derivation. |
| Antiderivative family; FTC; rectangle-sum limit | 178 | Distinction between definite number and indefinite family, intuitive accumulation. |
| Power/trig/exp antiderivatives and linearity | 180–195 | All elementary exact computations; integrating g−f termwise. |
| Whole-integrand substitution and transformed limits | 197 | Source substitution and Q5; lesson nevertheless teaches the local factor/endpoints connection. |
| Signed area and velocity integral versus speed integral | 203, 297, 306–312, 594 | Motion/source correction and Q2/Q6. |
| Unit consistency and graph-area unit product | 28, 297, 533–543 | Metres per second times seconds; dimensionless-variable qualification at line 90. |

Chronological substantive reconstruction:

- Lines 14–64: antiderivative is defined; operational continuity is supplied at 16, including one-sided endpoint interpretation and usable continuous-function examples. Lines 18–24 specify F's continuity and interior derivative condition. This is sufficient for the endpoint theorem and does not assert that discontinuous functions can never be integrated. Baseline power differentiation licenses both derivative checks; lines 26–36 license the complete bracket operation, and 48–52 license cancellation of C.
- Lines 73–153: baseline rate, modulus and sum rules plus the local sample-time/duration definitions license v(t*)Δt and accumulation. Continuity on the finite interval supports the intuitive small-piece limit. The text explicitly does not claim that this is a proof of FTC. Every sign/area interpretation is bounded to forward limits. The sine values follow from inspected trigonometry and −cos differentiation. Motion example and Q2 require only a linear zero/sign check and taught endpoint evaluation, not a hidden kinematics formula.
- Lines 155–212: disjoint adjacent intervals motivate addition and exact endpoint cancellation verifies it for the continuous/antiderivative setting. Reversal and zero-width definitions make endpoint order consistent. Worked reversed/out-of-order cases distinguish orientation from integrand sign. Q3 applies these laws without requiring an invented formula for f; negative net area is allowed.
- Lines 214–258: pointwise comparison on every input plus nonnegative rectangle-sum accumulation and baseline integral linearity gives the integral inequality. Negating both sides reverses the relation. Exponential positivity and derivative/growth facts license h′≥0 and h(x)≥h(0), so the linear lower curve is established before use. Q4 changes both endpoint and orientation, requiring a new inference rather than arithmetic alone.
- Lines 260–339: baseline composition and chain rule give the displayed derivative; local text identifies the entire differential factor and reads/builds the new bound operation. The sufficient conditions u∈C¹ and continuous g on an interval containing u's range are technically sound. Continuity of u′ is identified as a property of the derivative, not merely renamed. Endpoint evaluation establishes substitution without requiring monotonic u. The increasing source example and decreasing added example expose different coefficients and orientation. Q5 asks a genuine factor discrimination and its answer correctly stops short of claiming B is unintegrable.
- Lines 341–350: Q6 deliberately separates closed-note recall from reopened application and asks a method choice. The heading does not reveal that choice. Polynomial expansion, sign intervals, and integral orientation are already available.
- Lines 352–531: every hint narrows a decision or supplies an intermediate construction; all solutions use earlier available premises. The proposed solutions match the pre-solution independent answers. Q6 accepts the valid alternate substitution method and retains its area sign split; it does not invent a unique personal recall report.
- Lines 533–535: course provenance, source page map, teaching additions, redrawn figure status and no-formal-proof boundary agree with the inspected source.

## PROF obligations and complete help audit

| Obligation | Finding and witness |
| --- | --- |
| T1 | Met locally: continuity and antiderivative conditions (14–24); signed velocity/speed (73); orientation (177–195); pointwise comparison (216–228); continuous derivative and substitution domains (262–282). Necessary premises precede application. |
| T2 | Met locally: endpoint expression read/build mapping (26–36); rectangle-sum roles (81–88, baseline sigma); figure-to-signed-contribution captions (138,175); composition, differential factor and new endpoint roles (262–284). |
| T3 | Met locally: FTC is an explicit supplied theorem, reversal a definition, addition cancellation a deduction, comparison a sum/linearity inference, and substitution a chain-rule inference. Coefficients 1/3 and 1/5 are exposed. Valid expansion alternatives are stated. |
| T4 | Met locally: complete representative endpoint, sine/velocity, addition/orientation, comparison and substitution cases. Interpreted signs and units accompany the calculations. |
| T5 | Met locally: Q1 is an early supported attempt; Q3 removes a formula, Q4 reverses comparison, Q5 discriminates missing factors, Q6 integrates method selection, signs, area and orientation. |
| T6 | Met locally: each Q1–Q6 names its requested reasoning/criterion; explanation demands have a prior worked model. No copied visible final answer or method-revealing mixed-task heading found. |
| T7 | Met locally: each of six tasks has a useful distinct hint and a complete reasoned solution. All 18 task/help IDs occur exactly once. No observed learner error is fabricated; errors are framed as possible or conditional. |
| T8 | Met locally: lines 344–346 and 494–529 distinguish later recall from changed application; timing is explicitly adjustable, not a universal optimum. |
| T9 | Met locally: actual baseline operations are used without demanding complete reteaching. Local continuity/notation bridges address real new conditions. Both figures aid the stated signed/interval inference and are mapped nearby. |
| T10 | Met for this independent local review: every source page/figure checked; important prompts solved first; all answers and major formulas independently checked. Calculation files below record exact evidence. Remote source freshness/publication is outside this review. |
| T11 | Local structure/figure checks pass. Plain paragraph labels, no prose headings/bold/italic markup or table headers in teaching. Hints and solutions are in separate groups with distinct links. Exact SVG exports are readable and complete at canvas edges. Actual destination math, typography, figure embedding and link navigation remain coordinator-owned checks. |
| T12 | Complete local route and help audited with limits disclosed. This report makes no global acceptance or learner-outcome claim. Current helper acceptance records are honestly pending until the remaining gates complete. |

Help details: Q1 hint preserves subtraction parentheses and constant cancellation; Q2 gives the zero/sign decision and antiderivative; Q3 gives X+10=7; Q4 gives matching endpoint evaluations and negation; Q5 gives du=2x dx and asks for its whole factor; Q6 gives the theorem elements, zero/sign split and two admissible method routes. None is merely a repetition of the original demand. Full solutions explain their respective theorem/physical/sign/comparison/substitution warrants.

## Independent correctness and usable-output evidence

`independent-calculations.md` preserves pre-solution Q1–Q6 computations: 3; displacement 3 m/distance 5 m; −3,−10,−7; e²≥5 with reversed comparison −4≥1−e²; A=15/8; and I=2, geometric area=5/2, J=−2. These are agreement checks, not proof of teaching accessibility by themselves; the reconstruction above supplies the latter's local witness.

`exact-checks.py` and `exact-checks.json` record 18 passing exact rational computations, including independent binomial expansion of the source substitution and Q5, motion pieces, reversed intervals, interval addition and Q6's area. Exponential numeric sanity checks are labelled as sanity checks, not proofs. The general comparison and h arguments were checked analytically above. Sine endpoint values were checked directly as −cosπ−(−cos0)=2, −cos2π−(−cosπ)=−2, and full-cycle zero.

`mechanical-checks.json` records 208 protected inline formulas, 40 fenced math blocks, 21 unique anchors, 34 internal links with no missing target, both linked figures present, six prompts/six hints/six solutions exactly once, no unresolved placeholder marker and no raw < or > inside inline math. Its raw non-math underscore candidate is solely the source URL filename, not prose emphasis.

The SVG exports show: signed-sine has complete x (radians), sin x, 0/π/2/π/3π/2/2π and −1/0/1 labels and both signed-integral annotations; interval-addition has complete f(x), x, a/b/c and contribution labels. No clipped canvas-edge text, absent glyph, overlap or false sign relation was found. Colours are supplemented by text and captions. SVG hashes are in the mechanical record.

One nonmaterial lexical observation was considered: `\lt1` at 408/511 and `\lt0` at 511 omit the skill's preferred terminating space, but a following digit itself terminates the TeX control word. They are valid TeX, contain no raw HTML-sensitive comparison and do not establish a lost operand or mathematical defect. Actual destination preservation remains to be checked, rather than presumed from this local conclusion.

## Issues, limits and necessary next step

Verified material issue register: empty after the entire document/source/help/figure audit. No necessary PROF repair is supported by this review. The original source's velocity/speed/odometer imprecision is already corrected, and the absence of a formal FTC proof is an explicit honest boundary rather than a false completion claim.

Remaining acceptance limits: I did not run the full-state validator, inspect the complete four-subject baseline, verify remote current-main bytes, navigate live GitHub help links, inspect computed destination typography, or inspect live rendered mathematics. The coordinator has the separate fresh SASIS/full-baseline and actual-destination tasks and will integrate the current requirement/source state. Local mathematical correctness does not by itself close those gates. No GitHub writes were made, no frozen output was patched, and no human mastery/retention or absence of all latent error is claimed.
