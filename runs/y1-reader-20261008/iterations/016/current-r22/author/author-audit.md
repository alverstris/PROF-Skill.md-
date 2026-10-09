D016 r22 author audit — frozen learner v1

Status boundary

This is a source and author reconstruction audit, not SASIS or observed learner understanding. Incoming published skill r22: 65e1338c9695ec4cdd72a536b762cb2698d44744. Root later published source-only checkpoint 54a067832b58ef8c1c144f6bb75bec05e645cf45. Learner bytes frozen by learner-manifest-v1.json. Independent root review, fresh SASIS, actual GitHub mathematics/typography/navigation, final integrated acceptance and publication are pending. No skill change or closure is claimed here.

Contract and provenance

Requested product is repo-native Markdown teaching for the full readable D016 source, retaining its useful capability while applying current PROF to the actual complete OCR baseline. No PDF/ZIP/workbook requested. Source is MIT OpenCourseWare 18.01 Single Variable Calculus Fall 2006 Lecture 18: Definite Integrals; PDF p1 cover and p2 printed title establish identity. Source PDF SHA256 3469042c0ca6aa75aa7e420b2bbf726228c31093aea11ddb2fc0044a4404fec0. All six rendered pages of the PDF and corresponding six text files inspected; awkward extracted mathematics checked against PNG originals. No authorship beyond MIT/course/year asserted because the provided lecture PDF does not print a person author.

Exact user requests retained in inputs/runs/y1-reader-20261008/requests.md. The later scheduling reconciliation in inputs/runs/y1-reader-20261008/iterations/015/current-r21/continuation-status-reconciliation.json records disabled tasks and no warranted schedule mutation. No Windows/installed-skill operation; all changes confined to assigned author directory. No previous teaching or answer template was read. The initial broad file listing revealed filenames only, not their contents. Current source and controls have byte-identical snapshots under inputs. GitHub is canonical; author does not publish.

Actual reading and repair

read-log.json records calls and scope. SKILL.md completely read at cdef59, execution protocol at 45d8e5 with its clipped late section reread at e1eeac lines80–107. A second combined output e1eeac clipped between profile tail and reader text; 083e0a reread full reader contract/role plus profile110–125. The rewrite guide, requests and reconciliation were visible completely in e1eeac. state-tool read at a74549. All source text is visible in 6f0be5; two image calls inspected all six PNG pages. Frozen baseline 247840 bytes, 1378 LF slots, internal CR retained by read_bytes().decode().split('\n'); fifteen nontruncated outputs cover exactly1–1378 as listed in baseline-chunks.json. No claim that all baseline bytes were simultaneously retained in context.

Prerequisite decisions from actual baseline

Baseline LF28–34 supplies signed arithmetic, units, standard area/volume and similarity; LF62 supplies function input/output; LF76–86 supplies limit meaning, indexed sums and finite arithmetic sums; LF138–168 supplies derivative limit and power differentiation; LF178–203 supplies rectangle-limit interpretation, antiderivative evaluation and signed versus geometric area; LF223–227 supplies monotone endpoint bounds; LF401 supplies exact integer and square sums; LF415 supplies average value; LF543 supplies axes-product units. These are curriculum-based permissions, not measured mastery.

C1 compresses existing rectangle area and units while mapping them to contributions. C2 newly makes the staircase and square-pyramid containment explicit; pyramid volume is an introduced geometry premise, since the exact square-pyramid rule is not explicitly displayed in baseline. C3 connects existing differentiation to the moving endpoint and handles both signs of increment. C4 teaches roles of boundaries/tags/widths and a concrete construction; general continuous-function existence is explicitly a theorem premise, while the square and line cases get direct enclosures. C5 reconnects familiar antiderivative/area rules to current notation. C6 introduces the simple-interest model rather than assuming a real financial contract, distinguishing rates from amounts and contribution time from final time. Nothing depends on a previous lecture's availability. No chemistry/advanced physics premises are needed despite their complete reading.

Complete source coverage map

S01. PDF p1 cover: course/year/provider/provenance. Final: Source and scope. No teaching demand on the cover.

S02. PDF p2 opening and Figure1: totals/averages/areas and thin-rectangle procedure. Final: C1 and Figure1; average meaning/example C5. Width-height product and limiting refinement made explicit.

S03. PDF p2 Example1: x squared, width b/n, first and second heights, expanded sum and b cubed factor. Final: C2 opening expanded and indexed forms. Required condition b>0 made explicit and b=0 handled separately. P1 checks concrete construction and bound interpretation.

S04. PDF p3 Figure2: rising square curve with right rectangles. Final: Figure1 right panel and C2. Same consequential right-height enclosure retained; more strips are an author illustration choice.

S05. PDF p3 Figure3 and volume inequalities: nested square levels, unit height, centred top/side pictures, inner and outer envelopes. Final: Figure2 and C2 slab/cross-section argument. Every level side and height, inner n dimensions, outer n+1 dimensions, concentric containment, and positive-volume gaps supplied. Source calls pyramids prisms; corrected as D01 below.

S06. PDF p4 top: normalize by n cubed and take squeeze limit. Final: C2 normalized bounds and explicit shrinking enclosure; left-right gap supplies an extra connection from upper-sum limit to region area. Exact square-sum identity is an independent familiar check, not replacement of the assigned geometric route.

S07. PDF p4 Example2 and Figure4: line sum, triangle area, derivative pattern. Final: C3 line-sum evaluation, Figure3 left and moving-endpoint explanation/right. Both derivative patterns retained. Two-sided derivative warrant added locally; general version C5 clearly theorem-backed.

S08. PDF p5 general picture and Figure5: arbitrary ci, equal widths, sum, limiting integral. Final: C4 and Figure4. Per-strip tag restriction, boundary labels, mapping from words to concrete tagged sum and back, dx role, tag independence/continuity condition explicit. P2 changes monotonicity rather than only numbers.

S09. PDF p5 Example3: principal, time/year, six-percent rate, simple-interest factor; monthly borrowing and 1000/month example. Final: C6 model, unit conversion, twelve strips, then n strips. The finite rate product approximation/exact piecewise constant condition and difference from discrete loans are stated.

S10. PDF p6: total borrowing integral and year-end debt weight. Final: C6 full derivation, worked numerical case; P3 changed time profile plus complete help; dimensional and endpoint checks. Source unit error corrected as D02.

Source corrections independently checked

D01 established source wording error. PDF p3 says inner/outer prism but both depicted comparison solids taper to an apex and the displayed volumes contain factor1/3. A prism of base area n² and height n would have volume n³, which is different and fails the lower-bound claim at n=2 (square sum5<8). A square pyramid has area of cross-section (n−z)², so an author-only baseline-calculus check integrates from0 to n to yield n³/3. Independently the exact square-sum identity gives positive inner gap n(3n+1)/6 and outer gap (n+1)(3n+2)/6 for every positive integer n. Thus the learner comparison is correct independently of copying the source label. Both cross-section containment and full top/side visuals were checked.

D02 established source units error. PDF p6 says the integral of f(t) over one year represents dollars per year. f is explicitly a rate in dollars/year and dt a time in years; their product and integral have dollars. A constant12000/year over1year gives12000 dollars, not a rate. C6 and Solution P3 use the corrected units. This is not an alternative course convention requiring student adjudication.

D03 source scope omissions made explicit, not competing conventions. Positive-area b arbitrary requires b≥0 here, with construction b>0. General integral-as-area requires f≥0; C5 distinguishes signed accumulation. Simple interest P(1+rs) means no compounding. Numerical times carry year convention. Finite sampled monthly rates give an approximation unless constant on each month; finite debt timing remains an approximation for continuous borrowing. These are necessary conditions supplied from the displayed mathematics, not invented empirical premises.

Reconstruction witnesses

W1 — Meaning/construction. Baseline rectangle area plus C1 width formula leads to C2 stripi right input ib/n. Substituting into x² yields height i²b²/n²; multiplying by b/n yields i²b³/n³. Summing maps exactly to the displayed square sum. P1 uses the same operation with numeric width, and its solution's bounds follow the increasing-curve warrant already present in Figure1. No unintroduced sum/height distinction is required.

W2 — Geometric warrant. C2 specifies concentric square slabs and height variable before comparing sides. Given k≤z<k+1, subtracting z/k from n establishes the inner and outer side inequalities; concentric squares convert length comparison to inclusion. The introduced pyramid-volume premise produces both n³/3 bounds. Dividing by n³ preserves order because n>0; the upper bound tends to1/3. Subtracting the telescoped endpoint gap shows the lower rectangle sum reaches the same limit, so the area inference is licensed. This is an author reconstruction, not proof of learner success.

W3 — Changed ordering and tags. C4 defines each tag between adjacent boundaries and its height as f(ci). P2 changes the function to decreasing; larger x now makes smaller height. Thus right≤tag≤left within each strip; multiply by positive2/n and add. Baseline arithmetic sum yields2±2/n, enclosing all tags in a gap4/n. The full solution uses only those established construction and comparison rules. It does not silently reuse the rising-square ordering.

W4 — Endpoint rate. C3 line triangle checks its sum limit using a different geometric representation. The added strip is bounded by two endpoint rectangles for h>0; dividing by h gives height bounds and continuity makes them agree. For h<0 both removed area and width reverse sign, retaining a positive mean height between the two endpoint heights. C5 states the general continuous signed theorem before P4 requires a below-axis interpretation. Differentiating A(b)=3b−b² is also supported by the baseline power rule.

W5 — Weighted borrowing. C6 first gives P(1+rs), then f(t)Δt as the principal of one contribution, and s=1−t as its age at year end. The product's brackets preserve these two roles before summing. The continuum limit uses C4. Baseline power antiderivatives then evaluate the uniform worked case. In P3 the same amount-per-strip and age construction works for a changing f, and the comparison fixes total principal before selecting a uniform rate. Solution P3's optional quantitative mean divides total dollar-years by dollars, giving years; its meaning is explicitly attached to the displayed weighted duration, not borrowed from outside material.

W6 — Signed/unsigned transfer and help. C5's constant negative example and split-at-crossings rule precede P4. Solving3−2x=0 locates the split; power antiderivative or two triangle areas produces positive9/4 and negative−1/4 contributions. P4(c) then uses the variable-endpoint rule already stated to explain a locally decreasing signed total. Hints for P1–P4 narrow the blocked construction without displaying complete final values; all solutions explain their decisions and return to exact task anchors.

Verification performed

Author full learner reread: teaching1–120 at b23eda; teaching121–end plus full hints at72f7ab; solutions entire at6c73f1. All four generated PNGs visually inspected in one view_image call. Pyramid legend overlapped the apex; moved below the diagram before freeze, regenerated figures, then visually reread repaired pyramid at b23eda. Other diagrams retained their read content. No learner bytes changed after the manifest freeze.

check_author.py independently calculates22 mathematical checks using exact rational/symbolic expressions plus numerical midpoint debt sums and sampled geometric containment; author-checks.json records outputs. Square sum positive gaps establish strict pyramid inequalities; n=1 is valid. Signed P4 checks separately calculate each contribution, so cancellation cannot conceal a sign error. C6 r=0 and t=0/1 checks distinguish duration from borrowed time; uniform/all-at-start comparison distinguishes the timing model. The symbolic pyramid cross-section check uses baseline calculus only as an author check; it is not a circular learner derivation.

Mechanical checks found21 existing local links/anchors, four matching P/H/S IDs, valid figure paths, paired fences, no unresolved placeholders, no ATX/setext headings, no emphasis markers outside mathematics, and no tables introducing forced header emphasis. Source-level correctness cannot establish GitHub rendering. The math uses GitHub-protected inline syntax and math fences; root must inspect actual parsed operand/grouping preservation and live visual styling/navigation before T11/global release pass.

Unresolved boundary and next action

There is no currently established uncorrected mathematical/source defect in this author audit. External assessments may expose defects and must be recorded without revising this original checkpoint. T11 remains unverified in the actual destination and T12 pending final integration; SASIS and root independent review remain pending. Root should use frozen learner v1 and complete baseline, preserving the original reader report. If repairs are warranted, preserve this version and prepare a separately identified revision. This packet does not assert mastery, actual retention, or corpus completion.
