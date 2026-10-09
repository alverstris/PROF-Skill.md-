D014 current-r20 author audit

This is an author reconstruction, not SASIS or observed student learning. Frozen teaching-v1.md has SHA256 60f908bb588e6dea64725b321f6eb753a33f8293bd452105f9fd48cefe68adbb, 23,136 bytes and 349 lines. After the local prose repair, I actually read the full final file in order, including prompts, hints and solutions (tool chunk f1af4b, 5,784 tokens, untruncated). The earlier draft was read in packets 1–180 and 181–349.

Author repair preserved: the draft needed an explicit meaning of continuity before MVT. Added the limit-based definition at line 126 and reread its downstream uses. The original is teaching-draft-before-author-review.md. Also removed the learner-facing word “baseline” before inverse-function derivatives. No teaching changes followed the freeze.

C1 reconstruction: L1, lines 5–39

Baseline LF 138–166 supplies the derivative limit and tangent equation. Define actual changes Δx=h and Δy=f(a+h)-f(a); approximating the difference quotient by f'(a), then multiplying by h, motivates the linear estimate. Independently define dx=h and dy=f'(a)dx. The tangent value follows from the baseline line equation, without treating actual Δy as exactly dy. Expanding the square produces 4h+h², checking 0.41 versus 0.4; output/input units multiplied by input units give output units. Zero dx gives zero dy but no quotient. P1 changes the step to negative: polynomial algebra gives 6h+h² and preserves the distinction between -0.6 and -0.59. S1 uses only these warrants. P7a changes the function to logarithm, requiring application of the same construction with the derivative from baseline LF 149.

C2 reconstruction: L2, lines 41–73

All three cube-root methods and the 64.1 variant from printed pages 1–2 appear. Baseline power differentiation gives (1/3)64^(-2/3)=1/48. Base input 64 and output 4 retain distinct roles. The differential and tangent estimates coincide by L1. Baseline LF 95–97 permits the first-order binomial truncation; exact factoring transforms h into u=h/64. Algebra 4h/(3×64)=h/48 maps back to the original estimate. P2 reproduces the map with negative absolute change -0.3 and relative change -0.3/64. S2 separates exact factoring from approximate truncation. Independent numerical evaluation gives cube-root 65 as about 4.02072576 versus linear estimate 4.02083333, confirming they are unequal. The 64.1 and 63.7 cases were also numerically checked.

C3 reconstruction: L3–L4, lines 75–120

Baseline LF 178–199 already supplies elementary integration. The lesson connects F'=f, dF=f dx and integral notation before substitution uses these forms. All six source formulas remain, with the power exception n=-1, real differentiability conditions, reciprocal exclusion x=0, secant exclusions at cosine zeros, arcsine interval (-1,1), and unrestricted real arctangent. The negative logarithm branch uses |x|=-x and the chain rule: [1/(-x)]×(-1)=1/x. Its input remains positive. Baseline LF 107 and 413 distinguish inverse functions from reciprocals and supply the inverse-trig derivatives. These facts permit direct verification without an additional university theorem.

C4 reconstruction: L5, lines 122–158

The source's “constant factor” becomes an additive constant. The baseline does not supply MVT by name, so the lesson introduces the independently researched theorem with continuity, differentiability and interval conditions. Differentiability implies continuity by multiplying the finite limiting difference quotient by an input change tending to zero. Between any two points in one differentiability interval, MVT then makes H'=0 imply equal endpoint values. Applying this to G-F proves uniqueness. No earlier lecture is assumed. The sine-cosine primitives are checked by the chain rule, and their difference is 1/2 by the identity in baseline LF 111. P3 deliberately breaks the interval condition: joining negative and positive inputs passes through undefined zero. P6 adds a value condition: C_A=-1/2 and C_B=0 give identical full functions. The constants are found separately before their representations are compared.

C5 reconstruction: L6–L7, lines 160–221

Substitution follows from the chain rule in baseline LF 158–164 and its integration form at LF 197. Composition A(g(x)) is supplied by LF 62. With A'(u)=q(u), differentiating the composition gives q(g(x))g'(x); reading this in reverse licenses the integral. In the source example, u=x⁴+2 matches the outside x³ up to factor 4. Replace the whole x³ dx by du/4, integrate u⁵, restore x and differentiate the whole answer. All factors are explained before use; polynomial expansion is identified as a valid alternative. Every source guess appears with its derivative: sqrt(1+x²), e^(6x), and e^(-x²). The two trig substitutions reconnect to L5.

P4 changes the inner polynomial and adds a value condition, then removes a controlling outside factor in the exponential proposal. S4 rejects that proposal by differentiation. At x=0 its derivative is 0 while the proposed target integrand is 1, a discriminating check. It does not claim that no other antiderivative exists. Baseline LF 178 supplies how a value condition determines C; the solution explicitly substitutes F(0).

C6 reconstruction: L8, lines 223–250

The source's last example is visibly corrected. Baseline LF 130 requires x>0 for ln x and establishes ln x=0 exactly at x=1. The denominator excludes 1. Reading (1/ln x)(dx/x) separates u=ln x from du=dx/x. The reciprocal-u rule in L4 gives ln|u|, then the original variable is restored. Composition order and both real branches are explicit; separate interval constants follow L5. Differentiating the lower branch uses two cancelling negatives. P5 changes the exponent from -1 to -2 while selecting 0<x<1. H5 provides the intermediate u^-2. S5 integrates to -1/ln x, uses ln(e^-1)=-1, obtains C=-1, and distinguishes the chosen interval from the second interval on which the same formula could be used. The condition does not determine a constant across the singularity.

C7 and complete help reconstruction: lines 250–349

P1–P7 all state observable response criteria and point to matched H/S labels. H1 supplies an expansion; H2 distinguishes absolute and relative changes; H3 isolates the interval issue; H4 groups the differential factor; H5 changes the power; H6 supplies values at π/2; H7 isolates each first decision. None repeats only the failed instruction. All hints at 262–274 precede solutions starting at 278. Every complete answer reconstructs its result using previously taught or baseline premises. Navigation is static text/search labels, with no promised interactive reveal or click evidence.

P7a/c retrieve the approximation/domain distinction, while P7b applies exact function recovery to cos(3x). S7 checks both derivative and initial value, then both logarithmic branches. The later return is an adjustable heuristic, not an optimal-spacing or learning claim. The source note at 258 retains the cover's course/date/title and generated-practice provenance. The ending and all solutions are included in the full audit.

Technical and structural evidence

check_math.py differentiates all six standard forms and all source substitution/guess answers, plus P4, P5 and P7b. It checks initial values, constant identities, polynomial changes and the wrong-pattern discriminator. technical-checks.json records 26 exact symbolic/rational checks passing and three numerical cube-root comparisons. Domain adequacy comes from the manual arguments above; it is not inferred from formal symbolic cancellation. I did not read root's presolutions. Root reported saving independent presolutions before opening any authored solutions; comparison remains root-owned.

structural-checks.json records seven unique and matching P/H/S labels, 346 mathematics expressions (310 inline, 36 display), balanced braces, no raw angle comparisons inside math, no Markdown prose headings/emphasis, no tables and no placeholders. The initial checker falsely reported a help-order failure because text.index('S1.') found a forward reference inside P1. Preserved structural-checks-initial-parser-failure.json, corrected the check to match start-of-line H7/S1 labels, then reran it successfully. This was a checker defect, not an authored navigation defect.

The assigned original has no figures. There are no authored figures or companion assets. L1's explicit algebra maps actual and tangent changes; L2 maps factorisation to relative change. No figure inspection is claimed. Actual destination expression preservation and typography remain unverified by this local source check.

Requirement evidence at this revision

T1 author pass: definitions precede use in L1, L4, L5 and L8, including the repaired continuity introduction.
T2 author pass: L1 maps base, step, output and units; L2 maps h to h/64 and back; L4 reads integral/inverse notation; L6 replaces complete factors; L8 explains nested order and domains. P4/P5 reuse these maps.
T3 author pass: approximation is licensed by derivative limit; MVT is an introduced theorem with conditions; uniqueness is deduced; the chain rule licenses substitution; constant repairs and logarithm domains are explicitly justified.
T4 author pass: connected worked routes cover cube-root methods, uniqueness, the paired primitives, substitution, every source guess and both logarithmic intervals.
T5 author pass: study purpose makes application required. P1 is early supported work. P4 removes an outside factor; P5 changes reciprocal power/domain; P6 imposes a condition on equivalent representations; P7 combines approximation and exact recovery. These are meaningful changes beyond numerical repetition.
T6 author pass: each prompt supplies a criterion; reasoning and checks discriminate plausible wrong conclusions. P7 has no method-revealing section headings. No observed student mistake is fabricated.
T7 author pass: all seven retained tasks have useful hints and complete reasoned solutions. Earlier premises support every help step. Proposed wrong routes are not presented as actual learner performance.
T8 author pass: P7 is a later covered-explanation opportunity; retrieval and transfer are distinguished and the suggested interval is adjustable. No extra tracking or automation was created.
T9 author pass: full baseline inspection allowed compression of familiar rules while retaining local bridges. No redundant calculus course or unneeded formal MVT proof was added.
T10 author-scope pass: 26 independent calculations, explicit domain review, all five assigned source texts and visuals, source identity/hash verification, and primary MVT research. Independent external review is a separate pending gate.
T11 pending: local source format/help structure checked; actual GitHub destination preservation, typography and appearance are root-owned.
T12 pending: author whole-route audit complete; fresh SASIS, destination and root independent final review remain pending. No global completion, mastery, live-pixel or click claim.

No substantive PROF edit is proposed from author evidence alone. Root owns later diagnosis and publication. Next action: independent complete review and fresh reader against the frozen packet, preserving all original inputs and findings.
