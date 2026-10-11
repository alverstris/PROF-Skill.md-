D007 independent technical review: source preparation

Status: source and requirements preparation complete; finalized prompts and whole teaching not yet supplied or read. This is independent technical review, not SASIS, authoring, publication, or a claim about human learning. Do not route the subject findings below to the author before whole-document freeze.

Input identity and access

The complete 36-file local PROF package in d007-clean-r29-20261011/inputs/prof matches its supplied manifest by byte count, SHA256 and Git blob identity, with no unlisted files. Every file also matches the specifically authorized d018-clean-r28/work/release-r29 package copy. No sibling teaching/evidence was read. SKILL.md is 41,937 bytes, SHA256 07d0311f9a8ab43b4391df5846f73393eac62762fd00746e2173da935fff4d3a. The package publication identity 3f7066cd66e517a655ad7dce9b54cd3816655440 and unchanged checkpoints daab62351889f165af744acbf5af77e481912cc1 and 7ab99719c8c0c892929a9ea2f42807af09720220 were supplied by root; this reviewer has not independently fetched the remote repository. Exact per-file evidence is in input-reading-identity.json.

Original source: MIT 18.01 Single Variable Calculus, Fall 2006, Lecture 7. The source identity's short title is “Exam 1 review”; the actual lecture page title is “Lecture 7: Continuation and Exam Review.” These are compatible labels, with the hyperbolic-function continuation included in scope. Original PDF: 113,363 bytes, five pages, SHA256 47316203594d35c47220c7049238045ff0a2ac73ba3292d17107f13d575f3602. The official-source URL is preserved in input-reading-identity.json. Its contents were supplied locally, so no external source was needed for this review.

Actual source reading: every literal text file and every complete page PNG for PDF pages 1–5, read directly. Page 1 is the OCW attribution cover. Pages 2–5 contain all substantive lecture content. The source has no plotted or geometric figures; its mathematical displays were visually inspected. A fresh PyMuPDF render at scale 2.0 matched every supplied page image pixel for pixel, and a fresh literal extraction matched every supplied text file. Those machine checks establish representation identity, separately from the actual visual reading.

Actual requirements reading: complete SKILL.md, execution-protocol.md, domain-patterns.md, sasis/student-testing-contract.txt, sasis.md, and sasis/profile-manifest.json. Truncated combined tool output was repaired through bounded rereading of the missing ranges. The physics/mathematics domain pattern is applicable; other domain sections are not teaching scope.

Baseline identity: 247,840 bytes, SHA256 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5. Selected actual reading used original newline-numbered ranges 1–28, 90–176 and 387–416, plus targeted search results. This is not a full-baseline read and cannot replace the author or SASIS reader's required full read. The selected passages supply radian trig, inverse branches, trig identities/addition formulas, exponential/logarithmic laws and domains, differentiation rules, implicit differentiation, and FM24–FM29 hyperbolic/inverse-function material. No unseen baseline premise is being claimed.

Source scope and independent mathematical reconstruction

S1. PDF page 2 (printed page 1): hyperbolic definitions, derivatives, identity and naming.

For real x, sinh x=(exp x−exp(−x))/2 and cosh x=(exp x+exp(−x))/2. Differentiating exp(−x) gives −exp(−x). Therefore sinh'=(exp x+exp(−x))/2=cosh, whereas cosh'=(exp x−exp(−x))/2=sinh. There is no negative sign in the latter derivative. Difference of squares gives cosh²−sinh²=[(exp x+exp(−x))²−(exp x−exp(−x))²]/4=exp x exp(−x)=1. The original expanded derivation agrees with this.

With u=cosh x and v=sinh x the point satisfies u²−v²=1. Since exp x>0 and exp x+exp(−x)≥2, u≥1, so this parameterization lies on the right branch rather than both branches of the hyperbola. The source only says that the equation is a hyperbola and does not claim that the parameterization covers both branches. Circular functions instead give u²+v²=1 for u=cos x and v=sin x. Naming, sign distinction, and relation to both equations belong in the assigned scope; unrelated hyperbolic identities or inverse hyperbolic calculus are not demanded by this source.

S2. PDF page 3, upper half: general differentiation rules and quotient-rule deduction.

For differentiable functions u and v and constant c, the sum, scalar, product and chain rules have their standard displayed forms. For v≠0, u/v=u v^(−1). Product plus chain gives (u/v)'=u'/v−u v'/v²=(u'v−uv')/v². A formula list alone would omit the requested deduction. The source's chain-rule grouping is f'(u(x)) times u'(x), not f'(x) times u(x).

S3. PDF page 3, lower half: implicit differentiation and inverse sine.

Treating y as a differentiable local function of x, d(y³+3xy²)/dx=3y²y'+3y²+6xyy'=0. Thus (3y²+6xy)y'=−3y² and y'=−3y²/(3y²+6xy) where the denominator is nonzero. The equation y³+3xy²=8 excludes y=0. Cancelling 3y then yields −y/(y+2x), but the original denominator restriction remains. At (0,2), for example, y'=−1, a useful sign and arithmetic check. A zero denominator cannot be licensed as a finite slope by this formula; no general existence theorem is silently assumed in the reconstruction.

For y=arcsin x, the principal range is [−π/2,π/2]. On −1<x<1 this gives cos y>0. From sin y=x, differentiation gives cos y·y'=1, and cos²y=1−x² gives cos y=+sqrt(1−x²). Hence y'=1/sqrt(1−x²) on the open interval. The source's implicit positive-root step requires this inverse branch, and the endpoint values do not have finite derivatives given by the formula. Inverse notation is not reciprocal notation. Both branch and derivative domains are explicit in the selected baseline.

S4. PDF page 4, upper section: specific derivatives and deduction responsibility.

The source specifically names x^n, arcsin x, arctan x, sin x, cos x, tan x, sec x, exp x and ln x, and says the learner should know formulas and how to deduce them from prior information. Their derivatives are n x^(n−1), 1/sqrt(1−x²), 1/(1+x²), cos x, −sin x, sec²x, sec x tan x, exp x, and 1/x, respectively, on their real differentiability domains. Radian input is required for the trig formulas; sec/tan require cos x≠0; ln x requires x>0; arcsin's derivative requires |x|<1; the real-power proof below uniformly uses x>0. Arctan's principal range (−π/2,π/2) implies sec²y=1+tan²y=1+x², so differentiating tan y=x yields y'=1/(1+x²). Quotient differentiation of sin x/cos x gives tan'=1/cos²x. Reciprocal differentiation of cos x gives sec'=sin x/cos²x=sec x tan x. The source explicitly works the secant calculation.

Using the supplied radian limits A=lim sin h/h=1 and B=lim (cos h−1)/h=0, the sine addition formula gives [sin(x+h)−sin x]/h=sin x·(cos h−1)/h+cos x·sin h/h, whose limit is cos x. The cosine addition formula gives [cos(x+h)−cos x]/h=cos x·(cos h−1)/h−sin x·sin h/h, whose limit is −sin x. The derivative definition and both source limit premises are substantive assigned content. The source supplies the limits; their separate proof is not demanded here.

The power formula for positive integer powers can be obtained from the binomial difference quotient or product rule; the lecture describes rational exponents as previously obtained by implicit differentiation. The exponential derivative is an available foundation in the selected baseline; with y=ln x and exp y=x it yields exp y·y'=1, hence y'=1/x. Correct coverage need not re-prove an established foundational definition circularly.

S5. PDF page 4, lower section: two real-power derivations.

For a fixed real r and x>0, define/use x^r=exp(r ln x). The derivative is exp(r ln x)·r/x=r x^(r−1). Alternatively f=x^r>0 gives ln f=r ln x, hence f'/f=r/x and f'=r x^(r−1). In the second route, (ln f)'=f'/f follows from the chain rule and the logarithm derivative. r is constant, not a function of x. Taking real logarithms requires positive quantities at the point of use. Integer powers and some rational powers also exist outside x>0, but this uniform arbitrary-real-exponent proof does not establish those cases by substituting ln x at nonpositive x. Both methods are requested source content.

S6. PDF page 5: integrated chain/product/inverse-trig derivative.

For F(x)=exp(x arctan x), let g=x arctan x. Product rule gives g'=arctan x+x/(1+x²). Outer chain rule gives F'=exp(x arctan x)[arctan x+x/(1+x²)] for every real x. The source's e^(uv) rule has u and v both functions of x. The closing rhetoric “differentiate anything” cannot license nonexistent derivatives or unlearned arbitrary-function methods; the concrete capability is composition of the established rules. The expression is even, so its derivative is odd; at x=0 the derivative is 0. These are discriminating checks of the final answer's structure.

Review obligations reserved for the later freeze

All six source units must be located in actual teaching, including the brief final page and both real-power methods. Review important prompts independently before seeing proposed solutions. After freeze, read the whole teaching and all hints/solutions, compare answers and their conditions, inspect all supplied figures in full, and trace important warrants to earlier teaching or the inspected baseline. Particular technical checks include inverse branches, differentiability/domain restrictions, quotient-rule signs, the negative inner derivative in exp(−x), constant-vs-variable exponents, and composition grouping.

T1–T4 and T9–T12 apply to relevant teaching. T5–T8 require capability-level applicability decisions and adequate tasks/help for a study document; every retained prompt requires meaningful response criteria, a useful separate hint, and a reasoned solution unless the user waived them. Baseline knowledge should not be gratuitously retaught, but specific unfamiliar connections still need support. This reviewer can assess source coverage and correctness; a complete SASIS reading and live destination render verification are separate evidence.

No generated teaching has been edited or read in this preparation. No GitHub write, browser use, queue mutation, or communication of subject findings to the author occurred. Root has been informed only of readiness and evidence scope. The next action is to receive the finalized prompt-only packet and preserve independent solutions before any teaching/answer access.
