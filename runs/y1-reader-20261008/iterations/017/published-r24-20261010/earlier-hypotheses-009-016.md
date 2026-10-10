# D009–D016: scoped affected-earlier-success review

Review date: 2026-10-10. Canonical checkout: `/workspace/scratch/f9c0b7fc7e76/prof-iteration`.

This is a read-only retrospective author audit of the last accepted D009–D016 text and help, with this report as its only write. It evaluates the prospective refinement supplied in the dispatch: for a consequential theorem/procedure condition not established by the baseline or prior teaching, identify the object constrained, explain the operational meaning before use, and demonstrate/check it in the first worked application; familiar constituent words alone do not establish a compound technical meaning. It is not new generation, a SASIS run, a complete r24 reacceptance, or evidence of human understanding.

Result: the reviewed retained routes have substantial, concrete condition support. No material missing-condition bridge that blocks a retained worked/task route was established. D016 has one narrowly qualified clarification candidate in its general integrability statement, detailed as C16 below. Its earlier height and bound constructions supply more support than an isolated reading of that sentence suggests; absence of a glossary definition is not itself a failure. The concrete example also has a supplied finite-rectangle route, a separate consideration from interpreting the general condition. This candidate must not be converted either into an unqualified all-purpose PASS or into a failure of the lesson. Original acceptances and evidence are unchanged.

## Controls, access, and exact reading scope

The operative r24 controls were read completely from the canonical root before the coordinator's concurrent candidate edit: `SKILL.md` lines 1–162, version `2026-10-10-r24`, SHA256 `8c157bc21ef93e2c162d2196136afbaa1009dd2e627fef3964dbccf537c8e319`; and `references/execution-protocol.md` lines 1–107, SHA256 `f63eda3d1e8dcfd1e802f909d47c4827e94c8bc0eff15552127027a29c5279a7`. Both initial input identities were subsequently matched against the frozen published snapshot `/workspace/scratch/f9c0b7fc7e76/d017-published-r24/inputs/prof/`. That snapshot's `SKILL.md` and `references/execution-protocol.md` are the recoverable r24 controls for this report; the later working-root r25 candidate is not attributed to r24 and was not used for these conclusions. Pertinent duties are T1–T4, T9–T12; the reconstruction and dependency provisions distinguish an actual missing premise from a word list or a new version label. This reviewer did not publish or amend either control.

The actual baseline used was `references/sasis/ocr-baseline-20261007/student-baseline.txt`, SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`. Inspected continuous ranges were lines 1–237 and 312–433, with lines 373–395 reread after an oversized result truncated that middle portion. Line numbers here are the file's LF-numbered `nl -ba` lines (1377 in the whole baseline), not Python's additional splits at retained carriage returns. No complete-baseline read is claimed. Whole-file keyword searches also located occurrences of continuity, differentiability, bounds, domains, intervals, and related conditions; searches are not represented as reading every other baseline passage. The later matches at 441, 443, 445, 461, 463, 640, 706, 768, and 1347 were visible as search snippets and supply no essential new premise to the conclusions below.

Concrete baseline warrants inspected include:

- Lines 28–34: elementary geometry, domains and interval brackets, nonzero division, checking roots against domains; 58–72: factor signs, functions/inverses and domain restriction, graph and coordinate rules.
- Lines 76–97: convergence versus merely solving the limit equation, finite/geometric sums, binomial validity; 101–134: trig branches, logarithm positivity and exponentials.
- Lines 138–174: finite derivative limit, differentiation rules, related/inverse rates, stationary/sign tests and implicit differentiation; 178–209: antiderivatives, domain-restricted rules, substitution, signed integrals, separation and lost constant solutions.
- Lines 213–227: continuity/sign bracketing, Newton's nonzero denominator and failure modes, monotonic rectangle bounds. These are actual supplied rules, not expertise inferred from a topic title.
- Lines 231–235 and 391: vector components, nonzero unit directions, scalar products and angles. Lines 327–335: force balance, light/inextensible/taut strings and model conditions. Lines 357, 401, 409–419: induction, exact sum of squares, real exponential series, improper-integral restrictions, inverse trig derivatives, averages, and first-order integrating factors.

All eight closure files were read completely: `009/closure.md` 1–15; `010/closure.md` 1–13; `011/closure.md` 1–11; `012/closure.md` 1–15; `013/closure.md` 1–13; `014/closure.md` 1–9; `015/closure.md` 1–15; `016/closure.md` 1–17. Paths in this report beginning with a three-digit iteration are relative to `runs/y1-reader-20261008/iterations/`.

Queue evidence was inspected by parsing the exact selected records in `runs/y1-reader-20261008/queue.json`: `/sessions/8` through `/sessions/15` (zero-based), material IDs D009–D016. Each is `closed`, with incoming versions r15 through r22 respectively and the closure/evidence paths described here. Their outer `material_id` line locators are 597, 652, 703, 754, 805, 856, 907, and 959. D016 is Lecture 18, not Lecture 17. The record projection included identity, status, incoming/outgoing version, available document hashes/commits, and all evidence-path arrays. D009 additionally records recovery-v3 and its exact accepted text hash.

No D017 learner lesson, diagnosis, SASIS/teaching audit, or `017/earlier-r24-review/` content was read. An initial filename-only inventory incidentally displayed names in D017; none of those prohibited files was opened. Historical acceptance/disposition records for D009–D016 were used to locate identities and rendering evidence, not as substitutes for reading the actual teaching.

## Accepted artifact identities and complete text/help coverage

Every listed Markdown file was read from first line through the ending, including all prompts, hints, solutions, figure captions/alt text, and source/scope notes. Its current SHA256 was independently recomputed and its exact bytes compared with `git show <accepted-commit>:<path>`; all twelve comparisons matched. The following are the actual last accepted outputs, not the superseded attempts.

| Material | Accepted relative path | Complete inspected lines | Accepted constituent commit | Recomputed SHA256 |
| --- | --- | --- | --- | --- |
| D009 / Lecture 10 | `009/resumption-20261009/author/teaching-r15-recovery-v3.md` | 1–227 / P001–P062 | `9840e70de6aa7d2c718b60dd13ace7e6f795a50e` | `5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244` |
| D010 / Lecture 11 | `010/current-r16/author/teaching-v2.md` | 1–189 / P001–P049 | `629feb501ffd69447b70011d852ece5bf8a04641` | `192609d9d62cc50be534df77b5e5700c6eb7c4a9c32e37c832be6b1ab133742c` |
| D011 / Lecture 12 | `011/current-r17/author/teaching-v3.md` | 1–207 / P001–P051 | `d493bae7f5f680e33f2fa891c5d0310bf43e5d23` | `bcb390a295a8cce423b8ebfb9d292c45f7e6be3e37b9fbed1e33c6f60153f6fe` |
| D012 / Lecture 13 | `012/current-r18/author/teaching-v2.md` | 1–426 / P001–P046 | `12f468d985cbc1cb462e41948f0f017a161a2099` | `04355b5ac132bfdaecf6a165cf332d0e04a0ff29bd59b53e03d6c801c9838d59` |
| D013 / Lecture 14 | `013/current-r19/author/learner-v2.md` | 1–326, sections A–F and all P1–P6 help | `ea627ac47e24cd309a3e7b75a4ecfd070e54a3b5` | `d17f77d36f7c30db9777230a85decb363a1fb967bb5c51d60cb5af4cd7b078c0` |
| D014 / Lecture 15 | `014/current-r20/author/teaching-v2.md` | 1–413, L1–L8 and all P1–P7 help | `40151288dfc73314e6efb7ef74794dfa75a0a5ee` | `caf74a9a150f61d2531e8b2768abb1448fb7d5304818a9e1fcc73d02bead826b` |
| D015 / Lecture 16 | `015/current-r21/author/v2/teaching.md` | 1–246 | `f531ccd1a3ec4b4918b96fbab30a7f6d8c03aafa` | `9ff76d7dde73d2270b511421f428e5e3324176bc1666728ea013ec8f0512c4b4` |
| D015 | `015/current-r21/author/v2/hints.md` | 1–38 | same | `19bf8adb1b6c71a3fdfa65588612e90e8c2431917807c78d7db3ab952fa4f1b5` |
| D015 | `015/current-r21/author/v2/solutions.md` | 1–99 | same | `9f6a2b4117df5902a1d964de411830e6af4e61862d6ef80d5cc38991be766855` |
| D016 / Lecture 18 | `016/regenerated-r23-c1/author-v2/learner/notes.md` | 1–308 | `80c86f6d11c0cbec403dad2da04ee887ca52ce6f` | `7b91a08087ddfee2137ac13ce7a0dbd276e487166db1fa112ef4b11beda84c3a` |
| D016 | `016/regenerated-r23-c1/author-v2/learner/hints.md` | 1–51 | same | `1ce9784fb886d58811990954c0a934b91236d7cfadd00a42294b307b9097f3f2` |
| D016 | `016/regenerated-r23-c1/author-v2/learner/solutions.md` | 1–186 | same | `77368b5c1607522f2e358b849a9c10ec17b10366265553081c159747d449e2a0` |

D009–D014 hashes agree with the closure identities. D014's exact constituent freeze commit is supplied by the later admitted accepted binding, rather than its closure's subsequent evidence-publication commit. The D015 nine-constituent manifest `015/current-r21/author/v2-evidence/freeze-manifest-v2.json` was read completely (1–63); its SHA256 is `de468d1f028bd24f30dbc4ddad64e8d1acf08130c6fa24d8c7ce2287942f087e`. The D016 six-constituent manifest `016/regenerated-r23-c1/author-v2/learner-manifest-v2.json` was read completely; its SHA256 is `a622167a2069f2b9606884702fb1f8e059f5dfcf675f9e75fcfe61740cf41047`, exactly the closure identity. Every manifest constituent's byte count and SHA256 matched, and all nine D015 and six D016 constituent bytes matched their accepted Git blobs. Stale pending-gate sentences inside the immutable freeze manifests do not override the later closure records.

The four D009 replacement PNGs, five D010 PNGs, four D011 PNGs, four D012 PNGs, and all three PNG/three SVG D013 companions also matched their accepted Git blobs. These were byte-identity checks. No new visual inspection of figure pixels was performed; the complete nearby prose/captions were read. D009's accepted replacement figures are not reclassified as recovered historical originals.

## Condition findings

The locators in this section refer to the accepted files above. A familiar operation was credited only when the actual baseline supplies it or the lesson establishes it. Later explanations were not used to erase an earlier dependency gap. Where a different supplied route already supports the result, that limits the consequence of a compact or unfamiliar phrase.

### D009 — curve sketching

The domain is the object constrained by the derivative-sign rule: P005–P007 (11–15) specify an interval of differentiability, derivative sign throughout it, and splitting at excluded inputs as well as zeros. P008–P012 (17–35) demonstrate a polynomial sign analysis; P015–P019 (45–61) explicitly refuse to join the reciprocal's branches and show why a negative derivative cannot prove decrease across its disconnected domain. The baseline already supplies derivative signs and sign-line algebra (58, 138–168). This is substantive support, not reliance on the familiar word “interval.”

P018 (57) gives an operational one-sided vertical-asymptote condition: all sufficiently nearby inputs on the chosen side, rather than isolated unbounded values. The reciprocal construction supplies the immediate example. P023–P027 (81–89) distinguish slope change, a stationary input, continuity/inclusion, and actual concavity change. P029–P032 (93–99) apply the tests to the cubic; P054–P061 (197–225) retain the conditions in help, including the excluded zero and the inconclusive zero second derivative.

The second-derivative continuity premise in P025 (85) is a sufficient explanatory premise for the local sign argument; the baseline already grants the second-derivative test, and the worked classifications also have explicit first-derivative/sign routes. It is not a newly unexplained compound condition essential to obtaining a classification. P034–P041 (105–155) state the logarithm's positive domain and positivity needed to divide inequalities; P038–P039 compare the integrands for every input in the interval and explain the shrinking bound. Task C's whole help route repeats domain and sign checks. No material condition bridge found missing in this scope.

### D010 — extrema and optimisation

P007–P011 (19–29) define interior input operationally, explain why a two-sided derivative at an interior extremum must vanish, define the critical candidates, explain continuity including the allowed endpoint side, and state the finite closed-interval existence theorem. The examples show both ways the guarantee can be lost: excluded endpoint and reassigned discontinuous endpoint. “Least upper bound” is explicitly defined using outputs and attainment, rather than inferred from its component words. Baseline interval brackets and nonzero division are available at 30–32.

The first changed-domain application uses the derivative's sign throughout the admitted interval (Q1/Solution Q1: 33, 138, 154). The first worked finite candidate comparison identifies the domain and endpoint convention before use (P024–P028, 89–108), compares the stationary and endpoint values, and supplies a complete-square alternative (110–118). The physical can conditions are attached to the actual variables: fixed positive volume, positive radius/height, open top and equal area cost (35–55); the derivative sign and open-end checks justify a global minimum (57–83). The lid task and constrained-wire help preserve the changed controlling conditions (87, 128, 158–189). No material missing-condition bridge found.

### D011 — related rates

P003–P009 (5–31) define the common time, the changing quantities, the signs, and the requirement that the geometric relation hold at nearby times before differentiating. The worked case checks the divided formula at a nonzero road coordinate. P011–P014 (40–53) show precisely what fails at zero, use the undivided equation there, and give equivalent root-based routes. This is a concrete check of the exact divisor, not merely a generic “avoid zero.”

The cone's constraints are attached to water depth/radius and fixed tank geometry (P016–P023, 57–87); the first application inserts depth 5, and the singular sharp-point boundary is explicitly excluded. Net inflow is given as the premise for the changed problem, and its sign/interior-depth restrictions are checked in its full help (91, 142, 164–178).

The sensitivity approximation specifies a fixed positive horizontal leg and a small input change that stays in the square-root domain (P027–P030, 99–114); RR3 compares the approximation with exact new geometry (182–207). P033's differentiable-local-inverse/nonzero-derivative clause (122) is the same inverse-rate condition explicitly granted in baseline 62 and 164. It is stated conditionally for an incompletely specified mirror setup, not used to invent a numerical mirror result. The absence of supplied mirror coordinates is disclosed in P032. No new unsupported condition needed for the retained numerical route was found.

### D012 — Newton iteration and the ring

The exact denominator and its role are identified before Newton's first step (19–36); the current slope is calculated and nonzero there. P007–P015 (44–141) distinguish legal steps, convergence, possible limits and the desired root. The square-root error identity supplies an actual convergent bound, while the two-cycle verifies nonzero derivatives without convergence. The alternative bisection route names and applies continuity/opposite signs, already supplied in baseline 213–221. The task/help route checks these conditions again (137, 342–392).

For the ring, the newly named nondegenerate ellipse is tied immediately to the concrete length inequality L greater than the support separation (145–157). The actual lower-branch derivative, nonzero segment lengths, position below/between supports, and acute-angle range are all named with their geometric objects (167–216). P023–P026 (224–281) check the candidate's region, both positive segment lengths, total length and global lower bound; the connected numerical example checks the strict length inequality. P027 (283–285) then explains collapsed and impossible cases. The earlier conditional stationary construction is not the only warrant for the final global answer: the supplied triangle-inequality bound plus an attaining point covers every allowed position. That alternative limits any demand to infer a general implicit-function theorem from “smooth interior.”

The arbitrary-point reflection proof explicitly checks that its proposed normal is nonzero before dividing by its magnitude (299–312), using the nondegenerate length inequality to exclude opposite unit directions. All corresponding task help (354–416) retains feasibility, domain and alternative/global checks. No material condition bridge found missing.

### D013 — Mean Value Theorem and inequalities

This is a strong positive instance for the proposed refinement. Lines 15–29 identify the actual function and interval, explain closed versus open endpoints, continuity from the allowed side, and differentiability as a finite derivative limit; then check both hypotheses in the very first polynomial case. Lines 45–57 identify the gap function, why subtraction preserves the necessary properties, the extreme-value existence premise, and why the attained extremum is interior. The boundedness in that extreme-value premise concerns the interval with fixed finite real endpoints already established at 15; it is not a condition on an unidentified object.

The corner and endpoint cases discriminate the two hypotheses (59–70, 278); the endpoint corner outside the interval is correctly separated from an interior failure (65). The interval-wide sign proof identifies the closed subinterval on which MVT applies and the continuity bridge (117–135). The disconnected-domain task and solution test exactly that dependency (140–142, 253, 288–290). Exponential difference proofs restrict sign claims to the correct side of zero and distinguish finite-degree inequalities from a convergent infinite expansion (149–191, 295–305). Derivative-bound examples and all P6 help check interval order, domain and strict interior location (203–224, 263, 310–322). No material missing-condition bridge found.

### D014 — differentials and antiderivatives

L1 (11–41) defines the derivative-based small-step approximation and its limit, distinguishes exact differential equality from finite-change approximation, identifies the nonzero divisor, and calculates the first example's omitted term. L2 (49–77) identifies the relative binomial input as h/64; the baseline's expansion domain at 93–97 and 409 is available, and the concrete steps lie within it. The lesson does not claim a universal finite-step error guarantee.

The antiderivative object and interval-wide derivative equality are defined at 85–101. The exceptional power and logarithm/trigonometric domains are operationally specified at 103–128, including both signs of the logarithmic argument. L5 explains continuity, supplies MVT with its actual function/interval roles, derives zero-derivative constancy, and confines the additive-constant conclusion to the same interval (132–164). The disconnected-domain task/help checks precisely why that route cannot cross a hole (168, 292, 335).

Substitution requires the entire inner derivative factor and checks it in the first worked case (172–203). L8 names each of the two distinct logarithm/denominator constraints before transforming the integral (243–260). All P4–P7 solutions (341–411) retain the initial-value, branch and domain checks and distinguish failure at a single input from an interval-wide claim. No material missing-condition bridge found.

### D015 — separation and orthogonal curves

In `teaching.md`, the solution object must be differentiable and satisfy the ODE throughout a stated interval (12). Separation names the exact divisor and its nonzero interval before the first use, restores the zero solution by substitution, and supplies a division-free product-rule completeness check (36–68). This is stronger than merely reminding the reader of nonzero division. The general template identifies f, g, reciprocal h, antiderivatives, inverse branch and the inverse's input domain (84–126), then checks the two sign branches of the original logarithmic example. Q2's hint and solution explicitly preserve the arctangent range, finite solution interval and absence of constant solutions (`hints.md` 15; `solutions.md` 21–36).

The geometric slope procedure specifies x nonzero before forming a ray slope (136–144), preserves that restriction after polynomial simplification, and distinguishes extending a formula from satisfying the original ODE (153–168; `solutions.md` 43–55). Perpendicularity is operationally stated as tangent-line right angles, with finite nonzero slopes and the exceptional axes treated separately (178–218). The first ellipse example checks parameter positivity, branch, finite derivative, slope product and endpoint status (195–218); Q4's complete help repeats those conditions (`hints.md` 29; `solutions.md` 62–84). Q5 distinguishes both initial-data and equation failures and restates the conditions for separation (`solutions.md` 91–97). No material missing-condition bridge found. The quantum aside's coordinate scaling is qualified as context and is not an unprovided premise for solving the ODE.

### D016 — integrals and accumulation

In `notes.md`, the first rectangle bounds explicitly rely on nonnegativity and increase, and the decreasing case reverses the order (11–44). The square-pyramid proof ties containment to common centre and parallel corresponding sides before comparing lengths; it demonstrates the inequalities at every height and with an actual layer value (60–82). Q2 changes thickness while retaining that original construction; its solution explicitly rechecks centre/orientation (31–37). Those are concrete positive witnesses for conditions that cannot be inferred from merely seeing a square side length.

The common-limit definition identifies the whole sequence of sums, finite limit, every allowed sample choice, each sample's own interval, and fixed endpoints versus increasing n (117–150). Continuity is explained as an output limit agreeing with the point value (152). The accumulation proof identifies f at the moving endpoint and explains why continuity controls every strip height, why b must be interior for the two-sided conclusion, and what fails at a jump (175–197). Q4's help uses the exact difference quotient and distinguishes the endpoint one-sided derivative (`solutions.md` 102–118). The general finite-jump integrability sentence is examined separately as the limited candidate C16 below.

The borrowing model identifies rate versus amount, fixed simple interest, each loan's remaining duration, a finite payment schedule versus a continuous rate, and common settlement time before constructing the product (217–288). The first numerical loan checks duration at nine months and the endpoint alternatives (248). Q5 preserves equal principal while changing timing, explicitly checking both principal and weighted interest (`solutions.md` 126–151). Q6 uses sign changes and the same positive duration for distance/displacement and their averages (`solutions.md` 159–184). No material condition gap was found in these retained applications.

## C16 — limited clarification candidate in the finite-jump integrability criterion

Exact path: `/workspace/scratch/f9c0b7fc7e76/prof-iteration/runs/y1-reader-20261008/iterations/016/regenerated-r23-c1/author-v2/learner/notes.md`. The candidate sentence is line 152; surrounding lines 144–156 contain the common-limit definition, integral-object explanation, the criterion, and its next two-level example. The sentence says that bounded functions continuous on finitely many pieces, with finitely many jumps, also have the integral. Its exact object is the integrand's output over the whole integration interval. The paragraph defines continuity but does not expressly connect “bounded” to one finite bound for all those outputs, equivalently some finite M with absolute value of f no greater than M throughout that interval. It does not expressly name the bound M=2 or the single jump at x=1 in the next example.

Earlier support was reread specifically to test whether that express wording is needed. Lines 13–36 fix b, identify graph heights, and state that x² increases for nonnegative inputs. Together with the supplied algebra this allows the actual output bound 0≤f(x)≤b² for every x in [0,b], not merely a finite set of numerical samples. Lines 38–44 make lower/upper bounds operational for the area A. Lines 70–97 compare all cross-sections, bound the auxiliary volume and its normalized sequence, and explain being trapped between bounds. Lines 136–142 also use the heights of a linear function on a fixed interval, from which the output cap 3≤f(x)≤4 can be obtained. Thus earlier usable constructions, not just familiar constituent words, are available for interpreting a bounded quantity and bounding graph heights.

Those passages weaken the original isolated-sentence concern. They do not explicitly attach the new adjective to an interval-wide output bound, but a missing glossary entry does not establish a missing teaching bridge. The distinction potentially worth making explicit is a bounded input interval versus one shared finite bound on all function outputs. The inspected baseline supplies integration in suitably continuous/well-behaved cases (178) and separately handles improper singularities (411); no separate baseline definition of a bounded function was located. D010's earlier definition of an upper bound was not imported as a hidden prerequisite: D016 says no earlier MIT lecture is needed.

Consequence and evidential status: the general criterion's exact range-wide meaning is not explicitly checked in its own paragraph, and “all examples here meet these conditions” is an assertion there. However, the earlier constructions can support an interpretation of bounded graph heights, so this audit does not establish that the general condition is unusable from the supplied material. In particular, the absence of a displayed M is not itself a defect. No specific required discrimination between bounded and unbounded functions was found whose completion is demonstrably blocked. This is not a finding that the theorem is false or that a numerical answer is wrong.

Alternative already available: line 154 gives two constant heights and exact widths, computes the signed total as 2×1−1×2 and geometric area as 2+2, using the established rectangle/signed-area route. All assigned continuous polynomial/rate examples have their own supplied calculations, and Q6's sum-limit solution explicitly identifies a continuous velocity. Thus no retained worked answer or task is shown to depend solely on interpreting the undefined adjective. A minimal future bridge would distinguish input interval from output bound and check the two-level example; no teaching edit was made here.

Severity: low, local clarification candidate; material missing bridge not established. The earlier bound constructions are relevant counterevidence to declaring an explanation failure. The general-condition interpretation and the independent numerical route are deliberately assessed separately. Keep this exact qualification for coordinator adjudication; do not silently expand it into a new SASIS verdict, required repair, or full reacceptance decision.

## Actual math syntax and latest located rendering evidence

The counts below were recomputed from the accepted source bytes. Protected inline means dollar/backtick delimiters; ordinary inline means single-dollar delimiters; displays distinguish double-dollar pairs from fenced `math` blocks. These are syntax inventories, not renderer tests. Zero means that delimiter form was absent.

| Accepted text | Protected inline | Ordinary inline | Double-dollar displays | Fenced math displays | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| D009 | 273 | 0 | 0 | 12 | 285 |
| D010 | 145 | 0 | 0 | 11 | 156 |
| D011 | 185 | 0 | 0 | 16 | 201 |
| D012 | 281 | 0 | 28 | 0 | 309 |
| D013 | 0 | 190 | 24 | 0 | 214 |
| D014 | 310 | 0 | 36 | 0 | 346 |
| D015 teaching | 234 | 0 | 0 | 19 | 253 |
| D015 hints | 29 | 0 | 0 | 0 | 29 |
| D015 solutions | 110 | 0 | 0 | 6 | 116 |
| D016 notes | 224 | 0 | 20 | 8 | 252 |
| D016 hints | 21 | 0 | 0 | 0 | 21 |
| D016 solutions | 71 | 0 | 12 | 6 | 89 |

For D009–D015, the latest additional actual-server preservation evidence located within the permitted earlier records is `016/earlier-r23-review/per-case-dispositions.json` (entries D009–D015) and `016/root-earlier-r23-parser-verification.json` (results for the exact paths/commits above), admitted by `016/root-earlier-r23-disposition.md` lines 1–11. The latter narrative was read completely, as were the selected structured per-case records and the independent parser-verification record. These records report exact immutable raw/Git identity and every ordered math type/payload. Their counts agree with this audit's actual source counts. They expressly do not reopen all earlier semantic or visual gates. The historical checks identify D013's ordinary inline dollars accurately; they do not pretend all earlier accepted files used r24's future-authoring syntax.

The original accepted destination and preview locators remain separate from that later parser-only check:

| Material | Preserved destination evidence | Inspected admission/disposition and its limit |
| --- | --- | --- |
| D009 | `009/resumption-20261009/destination-v3/final-audit.json` | `009/resumption-20261009/final-acceptance.md` 1–21, especially 15–17: 285 server payloads and 10-page internal preview; no live-browser claim. |
| D010 | `010/current-r16/destination-v2/final-audit.json` | `010/current-r16/root-destination-v2-disposition.md` 1–9: 156 payloads, 8-page preview; live pixels/client MathJax/styles/clicks unobserved. |
| D011 | `011/current-r17/destination-v3/final-audit.json` | `011/current-r17/root-destination-v3-disposition.md` 1–9: 201 payloads, 9-page preview; live rendering unobserved. |
| D012 | `012/current-r18/destination-v2/final-audit.json` | `012/current-r18/root-destination-v2-disposition.md` 1–11: 309 payloads, 13-page preview; qualified pagination and no live-browser evidence. |
| D013 | `013/current-r19/destination-v2/final-audit.json` | `013/current-r19/root-destination-v2-disposition.md` 1–13: 214 payloads, 13 pages; only `destination-v2/preview-final4/verified-build.pdf` accepted, damaged other PDFs preserved. |
| D014 | `014/current-r20/destination-v2/final-audit.json` | `014/current-r20/root-destination-v2-disposition.md` 1–7: 346 payloads, 11-page preview; no client rendering/clicks claim. |
| D015 | `015/current-r21/destination-v2/final-audit.json` | Entire `015/current-r21/root-destination-v2-disposition.md`: 398 payloads and 12-page preview; only `preview-attempt3/verified-build.pdf` accepted; live rendering unobserved. |
| D016 | `016/regenerated-r23-c1/destination-v2/final-audit.json` | Entire `016/regenerated-r23-c1/root-destination-v2-disposition.md`: 362 payloads and 15-page preview; separate exact parser/raster evidence, no live-browser pass. |

Every final-audit path in the table was confirmed to exist. The original root dispositions, not all their bulky underlying audit archives, were read in this scoped review. D016's complete `final-content-acceptance.md` (1–9) was also inspected to corroborate the accepted six-constituent identity. “Latest located” is limited to these allowed D009–D016 records: the prohibited D017 earlier-r24 directory was not inspected, so this report does not assert a repository-wide search for every later rendering record.

No current network fetch, GitHub parse, browser session, MathJax execution, screenshot, PDF build, live rendering, click test, or visual rerender was performed by this reviewer. The source syntax inventory and historical accepted evidence must not be described as a fresh r24 renderer pass.

## Final limits and preservation

The complete accepted text/help inspection supports the specific condition findings, including later help uses; it does not re-audit every original MIT page, source claim, numerical result, figure pixel, typographic property or native link. No outside lesson or pretraining was credited as a missing subject premise. This is an author affectedness review with supplied baseline passages, not a fresh isolated reader or measured learner trial.

There are no teaching edits, control changes, queue/status changes, publication actions, regenerated lessons, or replacement evidence in this work. The current files and their accepted identities were preserved. The coordinator retains responsibility for integrating C16's narrow scope and deciding whether any further targeted check is warranted; this report supplies neither blanket earlier reacceptance nor an automatic reopening of all D009–D016 gates.
