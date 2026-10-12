# SASIS original report — D015-r36 frozen revision

## Result and scope

The supplied baseline and frozen teaching make the mathematical route accessible. I found no established blocking defect in the core explanations, figures, five questions, hints or solutions. Every required calculation has a route from actual baseline rules or earlier teaching, and the document supplies the consequential domain, excluded-case and branch distinctions rather than relying on a correct final answer alone. This is a document-accessibility finding, not a grade, a claim of human learning or retention, or a claim that every latent error has been discovered.

The strongest feature is the continuous connection between operations and their conditions: division can exclude a solution without disproving it; an implicit relation can contain several explicit branches; and a curve can extend geometrically through a point where its original slope equation remains undefined. Q1–Q5 require these distinctions only after they have been taught. The later help confirms the already available routes.

There is one nonblocking wording concern: Section 1 says an initial condition “selects a curve from the possibilities.” Read as restricting the candidates, this is appropriate. Read as promising that arbitrary first-order initial data always select exactly one curve, it would be stronger than anything established here. The notes do not explicitly make that universal uniqueness claim, and none of their questions needs it. Their Gaussian and parabola completeness arguments are instead proved for the particular equations. I therefore record the broader reading as a provisional concern, not an established mathematical defect.

## Actual inputs and access

The published role instruction was read first from student-role.txt. Its supplied identity is 6591 bytes, SHA256 `3c575ca7751f9fac1ee4a8cd67273404e689695ae238bd9a01e9def7457abacf`. I read route.json and route-seal.json once for operational paths and fixed step identifiers. Their supplied SHA256 identities are respectively `862bf62a76c06706588c45f84597e16c84a93a5c8234fca5599723485d70c4d6` and `a3a27e00875e6b340da393b9f94dbbb0a1f6ceff904a2c1b96b6f95ad2d804b5`. I did not independently hash those files; the launcher and operational tools returned successful checks under the supplied route.

The complete baseline was read in B01–B11 before M01: 247840 bytes, SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`, including Mathematics H240, Further Mathematics H245 Pure Core and both Statistics Y542 and Mechanics Y543, Physics H556 and Chemistry H432. No names or summaries substituted for a baseline chunk.

The teaching artifact is `D015-r36-whole`, revision `0f52edf74fe3bf9794a061880c201e423fbc37faa71416828c6c2bf682c2f3bb`. All six frozen files were covered: main.md 19044 bytes, hints.md 2935, solutions.md 7011, Gaussian image 30594, tangent-ray image 32937, perpendicular-families image 94461; total 186982 bytes. No additional appendix was scheduled or implied as a necessary mathematical input.

The actual route was B01–B11; M01,F01,F01R,M02,M03,M04,F02,F02R,M05,M06,F03,F03R,M07,M08,M09; H01–H05; S01–S05. All subject text came from the fixed read-step launcher, one bounded step per call. No optional baseline revisit was used. Every launcher result exited successfully and was saved as an actual returned exec object in raw-results. No text output was clipped, no input failed, and no content gap was reconstructed from memory.

Before the first step and after each of the 36 launcher calls, the fixed checkpoint command was executed. All 37 outputs reported `prefix_preserved=true`; the final output reported 384 events and 164535 ledger bytes. I did not repair, reconstruct or independently inspect the ledger. Those statements describe the actual checkpoint returns.

At each figure, the launcher returned its exact path, an actual tools.view_image call used detail `original`, the original result object was JSON-stringified directly into F01/F02/F03-result.json, and invocation metadata with actual timestamps was saved separately. The image was displayed and inspected before the operational receipt was made, read by F01R/F02R/F03R and followed by a checkpoint. Each receipt reported a decoded-image SHA matching its route image. Receipts explicitly say `semantic_inspection_proven=false`; they establish recorded tool-result identity, while the semantic evidence is the observations below. There was no early exposure to later teaching or delayed figure inspection.

This was instruction confinement. I do not claim technical isolation or erased pretraining. No web, other-agent consultation, personal/project memory, author files, historical reports, research sources or external review sheets supplied subject premises. URLs in the inputs were read as text and not followed. I did not render the Markdown interface or click its links; visible anchor names and destinations were read, so actual interface navigation is untested.

## Baseline warrants actually available

| Baseline locator and route chunk | Operational warrant used |
|---|---|
| Mathematics, Prior arithmetic / mathematical language and Proof; B01 | Domain conditions, division only by nonzero expressions, checking original equations, interval notation, deduction and counterexamples. |
| Mathematics, Algebra, functions and coordinate geometry; B01 | Functions give one output per input; one-to-one inverses need a selected domain and range; modulus, square roots, logarithmic/exponential algebra, coordinate gradients, graph scaling/reflection, perpendicular slopes and horizontal/vertical exception. |
| Mathematics, Exponentials and logarithms; B01 | Positivity of exponential, inverse log/exp operations, logarithm powers, growth/decay and limiting graph interpretation. |
| Mathematics, Differentiation and applications; B01–B02 | Derivative as tangent slope, power/product/quotient/chain rules, implicit and parametric differentiation, slope signs and stationary behaviour. |
| Mathematics, Integration and elementary differential equations; B02 | Antiderivative families with constants; conditions fixing constants; fundamental theorem for suitably continuous integrands; integral 1/x = ln|x|; reverse chain rule and substitution; separability with omitted zero-factor solutions checked separately. |
| Mathematics, Vectors; B02; Further Mathematics FM17–20, FM27, FM31–36; B03–B04 | Further geometry and calculus are genuinely supplied, although the notes' required route can be reconstructed using the simpler Mathematics premises. I did not import an unlisted theorem merely because related advanced topics appear. |
| Physics sections 1–8; B04–B07; Chemistry CH-00–CH-REF; B07–B11 | Entire packets were read. Their units, graph/rate and model-condition reasoning is available, but no extra physics or chemistry premise is needed for these pure calculus examples. Their subject names do not license the quantum context claim as independently verified. |

Differentiability/continuity and constant-sign reasoning on a nonzero interval are used only in the ordinary sense already implicit in the baseline derivative, continuous-function and interval rules. In particular, a continuous function cannot move from positive to negative on an interval without reaching zero. The antiderivative family of zero is constant on an interval; this supports the two completeness checks without importing an existence-and-uniqueness theorem.

## Chronological reconstruction witnesses

### M01: Sections 1–2 before Figure 1

The unknown is expressly y(x), the independent variable x, and a solution is differentiable and satisfies the equation at every point of its interval. “First order” is defined by the first derivative and absence of higher ones. Direct integration of 3x²+1 gives x³+x+C; the value at zero fixes C=2 and differentiating verifies it. These are baseline operations with meanings retained.

The operator `(d/dx+x)y` is explicitly defined as differentiating y then adding xy. Expanding it gives y'+xy; the check on u=x² yields 2x+x³. The zero denotes a function equal to zero on the whole interval, not a numerical multiplier. Thus the notation does not require operator theory from quantum mechanics. The quantum association and linked scaling are context, not used in the mathematical argument; their external scientific/provenance accuracy was not independently assessed.

For y'=-xy, division by y is confined to y!=0. The chain rule and integral of 1/y produce ln|y|=-x²/2+C. Exponentiation gives |y|=e^C e^(-x²/2), and the fixed sign on a nonzero solution interval gives y=a e^(-x²/2), with a positive or negative. The zero case is then checked in the original equation and retained. This prevents “not covered by division” from being mistaken for “not a solution.”

The product-rule check differentiates e^(x²/2)y to e^(x²/2)(xy+y')=0. Hence that product is an interval constant a, including a=0. This independently covers every differentiable interval solution without division by y and rules out arbitrary coefficient changes. It is a short baseline deduction, not an untaught general uniqueness theorem.

The initial value at zero is a because the exponential is 1 there. For a=1, positivity, even dependence on x², the sign of -xy, and decay of the exponential yield the stated hill: increasing left of 0, decreasing right, peak 1, and no finite zero.

### F01 and M02: Figure 1, caption and Q1

The actual image showed readable x/y axes, the legend y=e^(-x²/2), a symmetric positive hill and labelled point (0,1). Its tails become visually indistinguishable from the axis at display scale; M01's exact positivity already prevents interpreting that as a finite root. Positive scaling and negative reflection in the caption follow the baseline graph transformations.

Q1 asks precisely about the excluded zero case and negative coefficient just taught. The justified route is to substitute y=0 into the undivided equation and use a=y(0) for the second condition. The resulting -2e^(-x²/2) differentiates to 2x e^(-x²/2)=-xy. The reasoning and checks were available at the question's position before any help was read.

### M03: Section 3 and Q2

Separable means a right side f(x)g(y), with f and g functions. Zeros g(b)=0 are inspected in the original domain, so a constant b is retained only if the original right side exists. On a branch where g!=0, h=1/g and antiderivatives H'=h,F'=f give H'(y)y'=f by the chain rule, then H(y)=F(x)+C. The text gives continuous f and continuous nonzero g as sufficient conditions for the antiderivatives. Reverse differentiation explicitly requires a differentiable branch and restores the original equation there.

The inverse notation is defined, including the need for one-to-one H on a selected y interval and F(x)+C in its range. This connects the new implicit relation to the baseline inverse/function rules. A branch is defined by one y per allowed x. No assumption that a whole implicit relation is automatically one solution function is needed.

For y'=x/y with y(0)=-2, the original domain excludes zero. Integrating y dy=x dx gives y²=x²+4 after the condition. The negative square root is selected on the negative branch, is nonzero for all real x, differentiates to -x/sqrt(x²+4)=x/y and meets the data. The positive root solves the ODE but fails the data; constant zero fails the original domain. The distinction between excluded zero of a divisor and undefined original expression is available.

Q2 transfers this method to g(y)=1-y. Checking y=1 first gives a constant solution. For the other condition, the antiderivative is -ln|1-y|, not +ln|1-y|, by the reverse chain rule. Thus 1-y=Ae^(-x²/2), A=-1 for y(0)=2, giving y=1+e^(-x²/2). Its derivative equals x(1-y); positivity keeps it strictly above 1 for finite real x. This route needs no new rule at the exercise.

### M04, F02 and M05: Section 4, Figure 2 and Q3

The origin-to-point slope is (y-0)/(x-0)=y/x with x!=0. Twice this slope is the tangent condition y'=2y/x. At (1,1), the two slopes are 1 and 2. The text distinguishes doubling a slope from doubling its angle; the baseline relation between slope and trigonometric direction makes that distinction intelligible.

The actual Figure 2 showed blue y=x², a dashed origin line of slope 1 and a red tangent of slope 2 meeting at labelled P=(1,1). The tangent meets the x axis near .5 while the dashed line passes through the origin, visibly distinguishing their roles. The coordinate scales are equal. The parabola is drawn through the origin, but the prior equation already excludes x=0; M05 explicitly confirms that geometric extension does not remove the equation's denominator.

Separation on x!=0,y!=0 yields ln|y|=2ln|x|+C. Exponentiation gives e^(2ln|x|)=|x|²=x² and hence y=ax². Direct checking adds a=0. Differentiating y/x² gives (x²y'-2xy)/x⁴=0 under the original equation, so each connected interval has a fixed coefficient without dividing by y. Positive/negative/zero a have the stated upward/downward/axis shapes. Since an interval cannot cross excluded x=0, coefficients on the two sides need not be linked; a valid nonzero x0 fixes a=y0/x0² on its interval.

Q3 changes only the numerical slope factor and specifies x<0. It gives y'=3y/x and ln|y|=3ln|x|+C on the relevant nonzero branch. The positive ordinate at x=-1 fixes y=2|x|³, and |x|=-x there gives y=-2x³. Its derivative and 3y/x both equal -6x²; the two slopes at the point are -2 and -6. Evaluating the polynomial at zero does not define 3y/x there. No hidden sign convention is required.

### M06, F03 and M07: Section 5, Figure 3 and Q4

Perpendicular curves are defined through their tangent lines. The baseline negative-reciprocal rule applies to finite nonzero slopes; the text expressly retains the horizontal/vertical exception. Differentiating y=ax² at fixed a and substituting a=y/x² gives the family slope 2y/x for x!=0. Taking its negative reciprocal additionally requires y!=0 and yields -x/(2y). Integration then gives x²/4+y²/2=C.

The ellipse form is taught, not merely named. Scaling the unit circle by x=Au,y=Bv gives x²/A²+y²/B²=1. For C>0, comparison identifies A=2sqrt(C), B=sqrt(2C), so A/B=sqrt(2). C=0 forces x=y=0 and cannot be a function solution on an interval; C<0 is impossible because the left side is nonnegative. The point (1,1) fixes C=3/4 and slopes 2,-1/2; multiplying the general off-axis slopes gives -1 under the stated exclusions.

The actual Figure 3 showed grey upward/downward parabolas and solid/dashed blue ellipses labelled C=.75 and C=1.5 on equal scales. The solid intercepts were approximately ±1.73 horizontally and ±1.22 vertically, with the larger ellipse approximately ±2.45 and ±1.73, consistent with the taught semiaxes. Both are wider than tall; off-axis intersections visually support the algebraic perpendicularity check. The figure alone does not prove exact right angles or global ODE validity, and the surrounding text does not use it that way.

M07 distinguishes each square-root branch from the full ellipse. The radicand is positive for -2sqrt(C)<x<2sqrt(C), so each fixed-sign branch has nonzero y and differentiates to -x/(2y) there. That scalar equation exists at x=0, whereas the original parabola slope does not; the paragraph explicitly adds x!=0 for perpendicular-family intersections. Thus the branch through (1,1) has relevant interval (0,sqrt3).

Endpoint geometry is reconstructible without a new theorem. Near a left/right endpoint, write x=±sqrt(4C-2y²); its derivative with respect to y is zero at y=0, so the tangent is vertical in the original axes. This is perpendicular to the horizontal zero member. At top/bottom, x=0 but y!=0, whereas every finite-a parabola has y=0 at x=0; there is no such intersection. The whole loop has two y values for interior x and is therefore not one function y(x). These qualifications resolve natural alternative readings of the full-curve figure.

For Q4, P=(2,-1) fixes C=3/2, giving x²/6+y²/3=1 and semiaxes sqrt6,sqrt3. The negative coordinate selects -sqrt(3-x²/2). Combining positive radicand with x>0 gives the requested maximal open interval (0,sqrt6), which contains 2. At P, family and perpendicular slopes are -1 and +1. At the two interval boundaries, respectively the original x denominator and reciprocal y denominator fail; the full ellipse can still exist geometrically. All these requirements are taught before Q4.

### M08: Section 6 and Q5

The method summary reconnects the previous choices: direct antidifferentiation when the RHS depends only on x, separation with excluded cases when it factors, and construction of the slope equation before solving a geometric problem. It requires data, branch/domain and differentiation checks. Q5 permits adjustable timing; no learning or retention claim follows from that prompt.

Part (a) integrates 2x to x²+C and y(1)=3 gives C=2. Part (b) is a meaningful transfer of the earlier construction: at fixed a, (a/x)'=-a/x²; replacing a by xy gives -y/x. For positive x and nonzero y its perpendicular slope is x/y. Integrating y dy=x dx gives y²-x²=K, and (1,2) fixes K=3. The positive branch sqrt(x²+3) exists on all x>0, keeps both slopes finite and nonzero at every finite point, and has derivative x/y. At the point the slopes -2 and 1/2 multiply to -1. The conic name is expressly unnecessary; the baseline algebra and earlier method suffice.

### M09: Section 7 context

The two mathematical correction values are internally verifiable: derivative of -x²/2 is -x, and the member a=-2 in ax² is -2x². The claim that those errors occurred on particular original pages cannot be checked from the two permitted inputs alone; source provenance is unverified here. The historical exam guidance, listed review topics and absent external review sheet do not become prerequisites for the present exercises. In particular, mentioning the mean value theorem in that historical list is not a demand to use an untaught theorem.

### H01–H05: all hints

H01 directs the original-equation zero check, value of exponential at zero and derivative comparison. H02 identifies the zero of 1-y, the separated integral and necessary minus sign, then exponential positivity. H03 keeps |x| during exponentiation and uses |x|=-x on the declared negative interval. H04 connects P to C, denominators to squared semiaxes, sign of the data to the lower branch and positive radicand to the requested interval. H05 distinguishes differentiating at fixed a and reciprocating the slope from reciprocating the y-coordinate, then supplies y dy=x dx and the data/sign/check sequence. Each is matched to its actual question and uses available meanings and rules. None is needed to retroactively justify an otherwise unsupported earlier demand.

### S01–S05: all complete solutions

S01 carries both original-equation and initial-value checks for zero and -2e^(-x²/2), correctly locating the invalid generalisation at division. S02 carries the minus logarithm, renames the arbitrary constant after multiplying by -1, fixes A=-1, checks derivative/RHS and proves the above-1 behaviour and all-real domain. S03 retains |x|³ until the negative-x restriction is applied, checks slopes -2,-6 and explains why a smooth extension does not cure an undefined quotient. Its separately mentioned zero solution is correctly rejected by the nonzero data.

S04 explicitly obtains C=3/2, semiaxes sqrt6,sqrt3, lower branch and maximal requested interval. It identifies which denominator fails at each endpoint, checks slopes -1,+1, differentiates the branch and explains why it omits the upper half. S05(a) checks x²+2 and all-real domain. S05(b) derives -y/x before taking its reciprocal, uses K=2C consistently, selects the positive branch and verifies both original-family and new slopes at (1,2). Its closing explanation identifies what changed from the parabola problem rather than treating the old ellipse formula as transferable. The solutions match the questions and preceding teaching throughout.

## Issues, alternatives and dependencies

**Established defects:** none supported by this reading. In particular, I did not find a missing operation that blocks solving, an exercise placed before its necessary teaching, a lost constant solution incorrectly excluded, an unresolved sign/branch convention, or a figure that forces a contradictory interpretation.

**Provisional concern:** the initial-condition wording described at the start can be overread as universal uniqueness. The last fully supported reading is that initial data restrict the family of candidates. The natural question under the stronger reading would be whether data always ensure existence and uniqueness. These notes do not establish that theorem, but no later conclusion requires it. Their explicit product/quotient checks independently establish the relevant complete families.

**Resolved alternatives:** (i) an exponentiated coefficient is nonzero only in the divided derivation, while the original Gaussian equation permits zero; (ii) positive and negative roots are different branches, with the initial datum selecting the relevant one; (iii) a smooth polynomial extension can coexist with an undefined original slope equation at zero; (iv) a full implicit ellipse differs from a function branch; and (v) the perpendicular scalar equation may exist at x=0 where the original parabola-family slope does not. Each distinction is either already in the baseline or taught before the related exercise. No affected dependency remains blocked.

**Limits:** independent truth of the quantum-context association and historical/source-page claims was not verified; those claims do not supply needed calculus premises. Exact browser rendering and clickable link navigation were not tested. Figures were inspected as actual original-detail returned images, not inferred solely from alt text. There are no subject-input omissions, truncations or tool-failure limits in this run.

The original report is preserved here before any author feedback. Chronological per-call notes are in reconstruction.md; actual launcher outputs, view objects, captures and receipt-command results are in raw-results, with operational figure receipts in view-results. These records describe the supplied frozen revision only.
