# SASIS original fresh-reader report — frozen teaching-v2

This report evaluates the teaching document and its five figures against the complete supplied four-subject baseline. It does not administer the embedded tasks, assess an imagined student's achievement, or establish human learning, retention, speed or confidence. All reconstruction below is an audit witness for the explanation, including its existing tasks, hints and solutions.

**Outcome:** No established mathematical error, missing necessary subject premise, consequential figure mismatch, or blocking accessibility gap was found in this frozen revision. The examples, domain distinctions, questions and solutions are reconstructible from the actual baseline plus explicitly introduced definitions, the extreme value theorem and model conventions. Source-history assertions remain unverified because their evidence is outside the two authorized inputs. This is a bounded document finding, not certification of the unseen MIT source or of any learner.

## Input boundary, access and admission evidence

Exactly two subject-content inputs were used: (1) the complete four-subject operational baseline, and (2) the complete frozen teaching packet, consisting of teaching-v2.md and its five PNG figures. Access was instruction-confined and read-only for these inputs. Tools were technically shared; I do not claim technical isolation or erased pretraining. No external or remembered subject source supplied a premise. No other file, skill, previous revision, source PDF, review, author record or provenance record was opened. No browser, URL, web search, other agent or external subject source was consulted. The only agent communication was status/final reporting to the assigning root.

Input 1 path:
`/workspace/scratch/6a5c7131498d/prof-current/references/sasis/ocr-baseline-20261007/student-baseline.txt`

Input 2 text path:
`/workspace/scratch/6a5c7131498d/prof-current/runs/y1-reader-20261008/iterations/010/current-r16/author/teaching-v2.md`

Input 2 figure directory:
`/workspace/scratch/6a5c7131498d/prof-current/runs/y1-reader-20261008/iterations/010/current-r16/author/figures/`

All SHA256 values below were computed from actual bytes, matched the assigned frozen values at initial access, and matched again in a final read-only hash pass after complete reading and figure inspection. There was no hash or file-access failure.

| File | Actual bytes | Actual SHA256 |
|---|---:|---|
| student-baseline.txt | 247840 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 |
| teaching-v2.md | 20323 | 192609d9d62cc50be534df77b5e5700c6eb7c4a9c32e37c832be6b1ab133742c |
| log-over-x.png | 24483 | 2f65842860471e84b269b25e970d60ca588c33e9708ca7331c38df84958b572d |
| candidates.png | 50914 | b267d8b4598fe541f0bd63149ad9357feebc3ac1df3d5a9771ec49142a70f3bd |
| can-geometry.png | 35138 | ed6bccb6ca1a38b897bcbcf498a22058846489da546a6a14590c63568d20acae |
| can-area.png | 51695 | 48752de7d613e45a50c48cc8bc72daeeb43ac306c137a169bf158ff51f13305f |
| wire-and-area.png | 59562 | 6d1eabfa0662e71cc6cfd5baba0cb7fdafb38aa0a2715bbb653b24c0d4da2293 |

The baseline has 1377 LF terminators; the teaching text has 189. Locators in this report use physical LF-delimited lines, obtained by decoding bytes and splitting on `\n`, not universal `splitlines()`. CR characters were retained and did not become extra locators. Both files end with LF; the trailing empty split element is not an additional substantive line.

### Actual baseline reading sequence

Each retrieval read the authorized baseline bytes and displayed the stated numbered range. All four subjects were read before opening teaching-v2.md. These were content readings, not keyword searches or substitutions by course names.

| Order | Requested/displayed LF range | Result |
|---:|---|---|
| 1 | 1–120 | Complete; initial size, LF count and hash also checked |
| 2 | 121–300 | Complete |
| 3 | 301–460 | Complete |
| 4 | 461–620 | Complete |
| 5 | 621–800 | Outer tool output explicitly reported truncation; not accepted as complete |
| 6 | 621–710 | Complete replacement/overlap read resolving the first portion |
| 7 | 711–850 | Complete replacement/overlap read resolving the rest and continuing |
| 8 | 851–990 | Complete |
| 9 | 991–1130 | Complete |
| 10 | 1131–1250 | Complete |
| 11 | 1251–1377 | Complete through the baseline's final line |

The attempted 621–800 output contained a mid-output omission. I did not rely on its unseen span. The complete overlapping 621–710 and 711–850 reads resolved the truncation before substantive packet admission. The admitted ranges cover every LF line 1–1377 without a gap: Mathematics, Further Mathematics, Physics and Chemistry, including their conditions, scope limits and embedded reference resources. References appearing within the baseline were read as text only; their URLs and separately named files were not opened.

### Actual sequential packet reading and figure viewing

The text was read in order, stopping at each image insertion. Hash checking an image was followed by actual image viewing, not a filename-based inference. Each next text range was retrieved only after viewing the preceding image.

| Order | Text range | Figure actually viewed immediately afterward |
|---:|---|---|
| 1 | 1–17, P001–P006 | Figure 1, log-over-x.png, inserted at line 17 |
| 2 | 18–27, P007–P010 | Figure 2, candidates.png, inserted at line 27 |
| 3 | 28–45, P011–P015 | Figure 3, can-geometry.png, inserted at line 45 |
| 4 | 46–71, P016–P020 | Figure 4, can-area.png, inserted at line 71 |
| 5 | 72–100, P021–P026 | Figure 5, wire-and-area.png, inserted at line 100 |
| 6 | 101–189, P027–P049 | Complete remaining route, Q3, source note, hints, solutions and ending |

All these packet outputs were untruncated. Every figure was legible at the provided view. The final read-only hash pass reopened only the same seven authorized input files and reproduced the values in the table. Inputs were never edited. This original report is the only file written by this reader, and it was written before receiving evaluative feedback.

## Premise notation and baseline availability

`B` below means physical LF lines of student-baseline.txt. `T` means physical LF lines of teaching-v2.md. `Pnnn` is the packet's own passage label. Earlier-passage availability is chronological: later solutions are not used to justify earlier explanations or the initial accessibility of tasks. The following short index records operational premises actually present; it does not replace the complete reading documented above.

- **B28–34:** ordinary arithmetic, algebra, units, standard-shape geometry; expression/equation/function-domain language; interval endpoints; nonzero division and logical implication; circle area/circumference, rectangle area, cylinder volume and length/area/volume scaling.
- **B38–42:** deduction from assumptions, counterexamples, proof versus numerical examples, interpretation and evaluation of models.
- **B46–64:** power laws with real-domain conditions; completing the square at B48–56; sign reasoning and inequalities at B58; the piecewise definition of modulus at B60; functions, domains and ranges at B62; graph features and reciprocal/polynomial end behavior at B64.
- **B128–134:** logarithms as inverses of positive exponentials, ln(1)=0, ln(e)=1, logarithm power rules and monotonicity considerations. These are explicit formulae, not a grant based on the topic name alone.
- **B138–168:** derivative as a difference-quotient limit, its existence condition, power and logarithmic derivatives, constants and sums, quotient/product/chain rules; stationary points, sign changes, increasing/decreasing intervals, local classification and optimisation with domain/end restrictions.
- **B409 (FM27):** the full exponential expansion e^t=sum t^n/n! for real t; validity is expressly supplied. This Further Mathematics premise supports P006's tail bound; it is not silently imported from a prior MIT lecture.
- **B473 (FM57), B527, B533–535:** dimensions and units, explicit cylinder curved area 2πrh and volume πr²h, and consistent powered-unit interpretation. Physics reinforces the geometry even before P015 derives the wall area.

No Chemistry rule is needed by these optimisation examples. All Chemistry text was nevertheless read as part of the required combined starting input; absence of a used Chemistry premise does not mean that subject was omitted.

The packet explicitly adds the definitions of absolute and local extrema, interior and critical inputs, continuity in the relevant interval sense, upper/least upper bounds, the stated extreme value theorem, and its idealised modelling conventions. Such declarations may supply new content. They need not all be derived from the baseline. Their use and conditions are audited below.

## Chronological reconstruction witnesses

### P001–P006: first objective, value/location distinction, graph and limits

**P001 (T1).** The title identifies a lecture, institution and date. This is metadata supplied by the packet. It is readable but its historical accuracy is not independently established by the two authorized inputs. It supplies no mathematical premise needed downstream.

**P002 (T3).** The goal separates modelling, the correct domain, an attained extremal output and the producing configuration. B30, B42, B62 and B168 already support those operations. The reading route points forward to Q1–Q3 and separate hints/solutions without relying on their results. Algebra, differentiation and elementary geometry actually used are available as claimed. The theorem added at P009 is explicitly taught, so the opening does not require an unseen earlier lecture. The route says P003–P036; P037–P049 are separately labelled help, rather than silently omitted content.

**P003 (T5).** The absolute-maximum definition requires c∈D and comparison with every permitted x; the minimum reverses the inequality. This is explicit new definition built on B30/B62. The distinction among output, input and graph point is sound. The local definition compares only nearby allowed inputs; it can be read with non-strict inequalities, consistently with the displayed absolute definition and allowance for ties. B166 supplies stationary f'=0 and local derivative tests, while B168 already warns to check other restrictions. Calling a stationary input only a candidate is correct: it does not assert a converse theorem. Endpoints may be local extrema relative to their domain, but P007 correctly restricts its derivative argument to interior inputs.

**P004 (T7–11).** The function is (ln x)/x, with real domain x>0; the explicit reading of the fraction prevents confusing it with ln(x/x). B130 supplies ln x and B149 its derivative on x>0; B158–163 supplies the quotient rule with nonzero denominator. Taking u=ln x and v=x gives [x(1/x)−ln x]/x²=(1−ln x)/x². Every denominator is permitted and no input is lost. The calculation is correct and available before its application.

**P005 (T13).** On x>0, x²>0, so derivative sign is numerator sign. The logarithm is increasing here, available either through the inverse increasing exponential in B130 or derivative 1/x>0 with B166. ln(e)=1 divides the interval at e. B166 then gives strict increase on (0,e) and strict decrease on (e,∞). For any allowed x different from e, the corresponding interval connects x to e and gives f(x)<f(e). Thus globality does not come merely from a sign change arbitrarily near e; the sign is established on both whole sides. f(e)=1/e, location e, and point (e,1/e) are correctly distinguished. No endpoint-at-infinity comparison is assumed.

**P006, left side and nonexistence of minimum (T15).** B132 gives ln(e^−1)=−1; monotonicity gives ln x<−1 for 0<x<e^−1. Division by positive x yields f(x)<−1/x. The reciprocal behavior in B64, or ordinary reciprocal inequalities, shows that values can be made lower than any finite proposed lower bound. Therefore no absolute minimum exists. The axis crossing at x=1 follows ln 1=0, and strict monotonicity of ln makes that the only zero. This preserves the difference between an excluded boundary and an allowed extremum.

**P006, right-tail argument (T15).** The change of variable t=ln x gives x=e^t by B130. As x increases without bound, t does too: for each finite T, x>e^T implies t>T. B409 explicitly supplies the convergent real exponential series; when t≥0 every term is nonnegative, so retaining t²/2 gives e^t≥t²/2. For t>0 division yields 0≤t/e^t≤2/t. The trapping conclusion requires no unmentioned advanced theorem: for any positive tolerance ε, t>2/ε forces 0≤t/e^t<ε. Hence the tail approaches zero; it is above zero for x>1. This reconstruction uses the actual Further Mathematics entry, not outside memory of logarithmic growth or l'Hôpital's rule. P005's maximum proof remains independent of this tail argument.

**Figure 1 (T17, viewed).** The actual blue curve crosses the horizontal zero line at tick 1, rises to the orange point above e, then decreases while positive. Dashed guides connect that point to x=e and height 1/e. Axes label x and f(x)=ln(x)/x, with ticks including −1, 0 and 1/e vertically and 1, e, 5, 10 horizontally. Its left branch leaves the finite display downward; its right branch is still above the axis at the display edge. These are consistent with P004–P006. The finite image does not itself prove either infinite limit; the preceding algebra does. Labels, curve and guides are distinct and legible; the image does not confuse the value 1/e with the location e.

### P007–P012: candidate completeness, exceptional points and Q1

**P007 (T19).** “Interior” is explicitly defined by a small open interval of allowed inputs. For an interior local maximum, the numerator f(c+h)−f(c)≤0 for both signs of sufficiently small h. Dividing by h>0 gives a nonpositive quotient; h<0 gives a nonnegative quotient. The two-sided derivative, if it exists (B138–142), is a common limit. Its sign cannot be positive on the nonpositive side or negative on the nonnegative side, leaving zero. Reverse the inequalities for a minimum. This is a valid derivation of the needed necessary condition, with both existence and interior hypotheses present. At an endpoint the second side may not be allowed; at a corner no common derivative may exist. These are exactly the cases the argument cannot exclude. No converse is inferred.

**P008 (T21).** The locally declared definition of a critical input requires a defined function, an interior input, and derivative zero or derivative nonexistence. It is a usable convention, with endpoints kept separately in P009. From B60, |x| equals −x left of 0 and x right of 0, giving one-sided slopes −1 and +1 and nonnegative values with value zero at 0. This is a correct corner minimum. From B146, (x³)'=3x² and vanishes at 0; negative inputs have negative cubes and positive inputs positive cubes, and the function increases across zero. Thus zero is neither a local maximum nor a local minimum. Both counterexamples are available at this point and correctly distinguish a necessary stationary condition from sufficiency. An undefined point, such as x=0 for 1/x, is not accidentally called a critical input.

**P009 (T23).** The extreme value theorem is introduced as a stated result for a continuous function on a finite closed interval. It is an explicit new theorem, not a claim that its name is pre-taught. Continuity is explained by agreement of limiting and actual value, using the permitted one-sided limit at endpoints. Together with P007 and ordinary logic, any attained absolute extremum is either an endpoint or an interior local extremum; in the latter case its derivative is zero if it exists and otherwise it meets P008's other critical category. Therefore all possible extrema are included. Comparing their outputs is correct. The text explicitly qualifies finite comparison by “when there are finitely many candidates”; a constant function would have infinitely many critical inputs but is not falsely promised a finite derivative-root list. The condition is on the whole finite closed interval; no theorem guarantee has yet been extended to (0,∞), open intervals or discontinuities.

**P010 and Figure 2 (T25–27, viewed).** The blue schematic is drawn over a to b with dots at the two ends and each visible local turn. The highest orange dot is an interior peak; the right endpoint is the lowest orange dot. Several dark local peaks/valleys are lower/higher than the absolute extrema respectively. Axis text explicitly says function value and input on a closed interval. The text declines to assign numerical extrema or an equation. Thus the figure communicates the candidate-height relation supplied by P009 without pretending its shape calculates exact numbers. All substantive labels and dots are legible. Nothing requires differentiating a missing formula. “Calculus lets us make the comparison” is supported by locating candidates analytically and evaluating them; it is not a universal promise that every such equation is explicitly solvable.

**P011 (T29), open interval.** With f(x)=x on (0,1), the allowed input y=(x+1)/2 satisfies x<y<1 for every allowed x. Hence every output has a larger allowed output, and no maximum exists. The newly stated upper-bound and least-upper-bound definitions are accessible using B30/B58. All outputs are below 1. For any proposed bound b<1, an allowed input between max(b,0) and 1 has output greater than b; hence 1 is the least upper bound. This is correct and does not call 1 an attained value.

**P011, discontinuity example.** g agrees with x on [0,1) and assigns g(1)=0. It has a jump because the left values approach 1 while the assigned endpoint value is 0, using P009's continuity explanation. For any x<1 the preceding midpoint argument produces a greater output; for the assigned endpoint output 0, g(1/2)>0. No maximum exists despite a closed domain. Every output is nonnegative; 0 is attained at exactly 0 and 1. The instruction to compare actual values and side behavior correctly prevents substituting a one-sided limit for an assigned value. It is guidance for cases with discontinuities, not an assertion that any finite list automatically resolves all pathological functions.

**P012, Q1 (T31–33).** This is an existing supported application, not a new assessment administered by this report. Its restricted domain [1,√e], given derivative reference and explicit value/location requirements supply the needed problem. Before the later hint or solution is read, B46/B130/B132 and P004–P005 already show 1<√e<e and ln(√e)=1/2. The derivative is positive throughout that new interval, so endpoints determine the unique minimum and maximum. The answer can be reconstructed without any missing constant, table or source. The intended distinction between a stationary input of the larger domain and permitted candidates of the restricted problem is mathematically meaningful. P038/P042 are not needed to repair the prompt's premise availability.

### P013–P023: open can, one-variable reduction and changed-model task

**P013 (T35).** Fixed V>0, positive r and h, an open top, negligible thickness/seams and equal area cost are explicit new modelling premises. They make surface area a coherent objective and exclude volume-zero degeneracy. B42 supports interpreting an idealisation rather than treating it as all manufacturing costs. The formulation selects a right circular cylinder in the ordinary baseline cylinder model, reinforced by the illustration and equations. There is no requirement for an unstated materials law.

**P014 (T37–41).** V=πr²h is supplied directly by B34 and B527. One base disk plus the curved wall gives S=πr²+2πrh, with curved area explicitly available at B527 before the next explanatory passage. Thus the formula's appearance before P015 is not an unsupported forward dependency. Both expressions have the required dimensions. An additional top disk is excluded by the stated open-top condition.

**P015 and Figure 3 (T43–45, viewed).** The stated unrolling gives a rectangle of width 2πr (B34 circumference) and height h, hence area 2πrh by B34 rectangle area; the base contributes πr². In the viewed figure the left cylinder has an open top label, radius r and height h; the middle disk shows radius r and area πr²; the right rectangle labels width 2πr, height h and area 2πrh, separated by a plus sign. The correspondence is readable without treating an ellipse in perspective as a different base shape. The radius label refers to centre-to-edge, not diameter. The diagram supports the count of one disk and one wall; a later lid is not already included. With V fixed, decreasing both positive dimensions would decrease πr²h, so they cannot both be independently reduced while meeting the constraint. That observation is a valid deduction from the equation.

**P016 (T47–53).** Since r>0 and π>0, division in h=V/(πr²) is allowed. Substitution into S cancels the positive r and yields S(r)=πr²+2V/r for every r>0. B28/B32/B46 support the algebra. V remains a constant of the problem; h is now determined, not held fixed during subsequent differentiation. The domain is stated beside the reduced expression.

**P017 (T55).** For each positive r, h=V/(πr²) is one positive height satisfying the volume equation; conversely any original feasible pair satisfies exactly this formula. Hence no feasible can is lost or added by the reduction. As r shrinks, πr² decreases while 2V/r increases; as it grows, the reverse holds. Although the prose describes the wall via its increasing height, the earlier formula supplies the full curved-area behavior. r=0 cannot meet V>0 for a finite height; infinity is not an input in the domain. Those endpoint distinctions are correct and visible before the derivative is used.

**P018 (T57–65).** With V fixed, B146/B156 gives S'=2πr−2Vr^−2. Putting over r² gives 2(πr³−V)/r². Since r²>0, S'=0 is equivalent to πr³=V, with one positive real root r*=(V/π)^(1/3). The admissibility and uniqueness follow from positive-power arithmetic and the strict increase of r³, not from discarding a second feasible root. Every displayed equivalence is valid on the stated domain.

**P019 (T67).** The star is explained as a label. On all 0<r<r*, πr³−V<0; on all r>r* it is positive. B166 gives decrease over the entire first interval and increase over the second. Therefore S(r)>S(r*) for every different positive r. This is a valid global proof, independent of the closed-interval theorem, which would not directly apply to (0,∞). A merely local sign change would be insufficient, but that is not what is asserted here.

**P020 and Figure 4 (T69–71, viewed).** Both terms of S are positive. As r tends to zero from above, the reciprocal term increases without bound; as r increases without bound, the quadratic term does. B64 supplies these basic end behaviors, and positivity prevents cancellation. Thus no maximum exists. For the illustrative V=π, the earlier derivative gives r*=1 and substitution already yields S(1)=π+2π=3π; P021 is not needed retroactively. The viewed curve bottoms at the orange point (1,3π), with a dashed guide to r=1. Axes explicitly label radius in length units and S in square units, with 3π,6π,9π vertical ticks. Labels on the two arms describe their respective infinite limits. The finite drawing is consistent with the exact formula and clearly identifies V=π. “For other volumes” is justified by P019's symbolic sign argument, not by extrapolating a single plotted numerical case.

**P021 (T73–81).** From V=πr*³, h*=V/(πr*²)=r*. Substituting the same equality into the area gives Smin=πr*²+2πr*²=3πr*²=3π^(1/3)V^(2/3). All cancellations are positive-domain operations already available at B32/B46. The value, its dimensional inputs and the ratio are recovered after the minimising radius is established. No factor of two or power is missing.

**P022 (T83).** h*/r*=1 means height equals radius and is half the diameter 2r*. The ratio is independent of V; B34's similarity scaling and B473's dimensional rules confirm V^(1/3) has length dimensions and V^(2/3) area dimensions. These mathematical conclusions are correct. The separate claims about two misprints on the original printed page and preservation of the source cannot be verified without an unauthorized source/provenance read. Their verification is therefore not admitted. They are not premises for the corrected equations, which have been independently reconstructed from allowed content.

**P023, Q2 (T85–87).** The changed model explicitly supplies a lid, fixed positive V, positive dimensions, and the same ideal-area assumptions. Before P039 or P043–P045, the available circle area and the prior reduction already support adding exactly πr², using S=2πr²+2V/r, then differentiating on r>0. The task requests the appropriate domain, both dimensions, ratio, area and global justification. It neither requires an unstated theorem on constrained multivariable optimisation nor silently changes to a weighted material cost. A complete route is available from P016–P022 and the declared change; later help is support rather than repair of a missing physical premise.

### P024–P036: wire, boundary convention, Q3 and source note

**P024 (T89).** The total length 1 in chosen length units and no-waste conversion into square perimeters are explicit premises. The interval [0,1] and the area-zero convention for a zero-length square are declared deliberately before endpoint comparisons. This is an ideal mathematical extension, not an unannounced physical assertion that a positive piece has zero length. The planned later strict-positivity variant is a labelled future model change; no result from it is assumed at this point.

**P025 (T91–96).** Four equal sides give x/4 and (1−x)/4; square area is side squared using B28/B34. Adding yields A=[x²+(1−x)²]/16 on [0,1]. Here x is a numerical length in the chosen unit, as the axes later clarify; 1−x uses the same unit. The factor 1/16 is correct. Treating a wire length as a side would change the area by a factor of sixteen, but the paragraph explicitly prevents that alternate reading.

**P026 and Figure 5 (T98–100, viewed).** Replacing x by 1−x exchanges the two squared terms, so A is unchanged. This gives symmetry about 1/2 using the graph transformation/symmetry tools in B54/B64. The viewed left panel shows the blue x segment and green 1−x segment of a line from 0 to 1, then matching blue and green squares labelled side x/4 and side (1−x)/4; it explicitly calls the shown cut schematic at x=0.3. The right panel has a curve over 0≤x≤1, filled orange endpoints at height 1/16 and a filled midpoint at 1/32, with length/area units on axes. The highlighted extrema are accessible even before P027: expanding/completing the already supplied quadratic via B54 gives A=1/32+(x−1/2)²/8, whose squared term ranges from 0 to 1/4 on [0,1]. Thus the figure/alt text do not need later teaching to supply an unavailable premise, although the subsequent passages make the comparison explicit. The two panels use the same x meaning; the left drawing is one cut, not the midpoint-optimal configuration.

**P027 (T102–106).** Differentiating (1−x)² contributes −2(1−x), by the chain rule B162–164 or expansion. Thus A'=[2x−2(1−x)]/16=(2x−1)/8. It is defined throughout the interval, so no hidden interior nondifferentiable candidates exist. The negative sign is correct.

**P028 (T108).** The sole stationary input is 1/2, and the derivative is negative below it and positive above. Direct substitution gives A(1/2)=1/32, A(0)=A(1)=1/16. The polynomial is continuous on [0,1] in P009's sense: its elementary arithmetic expression approaches its actual value at every permitted input, including the permitted one-sided endpoint approaches. Consequently P009's conditions hold and its candidate list is complete. The endpoints tie for the maximum; strict derivative signs make the midpoint the unique minimum. The ratio (1/16)/(1/32)=2 validates the whole-wire versus equal-split comparison. This is explicitly the domain with degenerate squares permitted, so it does not incorrectly offer an attainable maximum for two strictly positive pieces.

**P029–P030 (T110–116).** Completing the square, an operation explicitly available in B48–56, gives x²+(1−x)²=2(x−1/2)²+1/2 and hence the displayed A. On [0,1], |x−1/2| ranges from 0 to 1/2; squaring gives the minimum at the midpoint and maximum exactly at both ends. These are routine supported algebraic operations and a second correct warrant for the same conclusions. The comment that differentiation remains useful for other objectives is method guidance, not a claim that this square identity applies to the can.

**P031 (T118).** Changing the domain to (0,1) removes only the previously maximizing cuts. The midpoint remains allowed and still minimises the nonnegative square term. For x<1/2, choosing a smaller positive x moves farther from 1/2 and raises A; for x>1/2, choosing a larger x below 1 does likewise. At x=1/2 any unequal permitted split increases A. Thus every allowed cut has an allowed improvement in the maximisation direction. A<1/16 in the open interval because |x−1/2|<1/2; values approach 1/16 at either excluded end by the explicit polynomial. P011's definition makes this an unattained least upper bound. No maximum can be restored by rounding. The phrase about moving the shorter piece is grounded in these inequalities, not an unsupported picture-based inference.

**P032 (T120).** The packet's Figure 5 actually has filled endpoints and midpoint, consistent with [0,1]. Removing the two endpoint dots for the strict model, while retaining the midpoint, correctly represents domain membership. The assertion about hollow markers in an original Figure 6 is source-history content not independently verifiable here. It is not needed to interpret the viewed figure, and the paragraph explicitly warns against inferring a domain from an unexplained marker style. No mathematical downstream claim is blocked by the unverified historical assertion.

**P033 (T122).** The five decisions accurately summarise the established routes: select objective; translate geometry and constraint; reduce with the feasible domain; find relevant candidates and end behavior; return to values/configurations. The caution about a stationary result being only part of the work is supported by the earlier counterexamples and wire minimum versus maximum. The caution about tempting excluded boundaries is supported by P011/P031. It does not conflate an optimisation objective with the sign of a derivative equation. The summary is available from earlier passages and provides a useful transition to changed constraints.

**P034, Q3 recall portion (T124–126).** This is a request already in the teaching text to retrieve categories and explain the insufficiency of f'=0, with an optional break. P007–P011 and P031 supply its entire subject content before the task. I treat its “checks retained recall” wording as a description of the task's intended function, not evidence that a real learner retained anything. No break was imposed, no new quiz created and no learner scored. The adjustable timing does not introduce a prerequisite mathematical fact.

**P035, Q3 changed constraints (T128).** “Each” gives x≥1/4 and 1−x≥1/4, hence [1/4,3/4] by ordinary inequalities B58. The geometry remains that of P025 and its derivative P027 remains available. Comparing 1/2 with the two new included endpoints follows P009 because the same polynomial is continuous on the new finite closed interval. The second requested model removes the minimum-length bound but keeps strict positivity; P031 already gives the relevant nonattainment reasoning. All inputs and units are present. “Greatest possible area” could colloquially suggest an attained maximum, but the prompt explicitly requires distinguishing approached from achieved values, so this wording is resolved rather than a consequential ambiguity. Hints and solutions are not needed to supply a missing constraint.

**P036 (T130).** The source note says the lesson reconstructs four examples and six visual relationships, identifies a lecture/page range and links a retained original PDF. It labels the drawings as new and Q1–Q3 as generated. These are attribution/provenance assertions supplied by the packet, not independently verified under the input restriction. I did not follow the PDF link. Five supplied images can contain more than five relationships, notably the two-panel wire figure, so the count alone is not an established contradiction. This audit cannot certify complete source coverage, fidelity or file preservation. The mathematical route remains self-contained without that certification.

### P037–P049: every hint, solution and final transition

**P037 (T132–134).** The hints are introduced as a separate optional help group, with full solutions below. This is navigation/study guidance, not a subject premise or evidence of learning. The complete group was read. Anchor identifiers for hints, h1–h3 and solutions appear in the provided text; no external navigation was necessary for content access.

**P038, Hint Q1 (T136–138).** B132 gives ln(√e)=(1/2)ln e=1/2. Monotonicity yields 0≤ln x≤1/2 on the stated interval, hence positive derivative numerator. Endpoint evaluation is the correct next step. The hint supports the declared target while leaving the value/location comparison to the existing task. It contains no new unexplained mathematical rule.

**P039, Hint Q2 (T140–142).** The lid adds one disk to P014, giving S=2πr²+2πrh. P016 supplies the unchanged height constraint. After differentiation, multiplying by r²/2 is valid and sign-preserving because r>0; the resulting sign factor is 2πr³−V. The hint correctly directs attention to the global sign argument. It does not erase the positive-radius domain.

**P040, Hint Q3 (T144–146).** The two inequalities and their intersection express the two-sided minimum-length condition correctly. Comparing stationary and admitted endpoints is the correct closed-interval procedure. When the bound is removed, the old endpoint cuts remain allowed but cease to be boundaries, which is the right question to ask. The corner and excluded-endpoint references are grounded in P008/P011 and identify distinct reasons a zero-derivative search alone is incomplete. There is no reliance on an unseen diagram or earlier course.

**P041 (T148–150).** Solutions are explicitly positioned as a comparison after an attempt, and the note distinguishes numerical slips from an incorrect domain. That distinction is meaningful document guidance, consistent with the problem goals. It neither grades a reader nor supplies a new mathematical theorem. The audit continues through all solutions rather than stopping at the main route.

**P042, Solution Q1 (T152–154).** On [1,√e], 0≤ln x≤1/2, so 1−ln x≥1/2>0 and x²>0. P004 therefore gives a positive derivative everywhere. e is outside the interval because 1<√e<e. Strict increase gives a unique minimum at 1 and unique maximum at √e. Evaluation gives 0 and 1/(2√e) respectively. Every requested value and location is supplied and correctly distinguished. No stationary input has been included despite the domain restriction. The return anchor matches the provided q1 anchor.

**P043 (T156–164).** The solution constructs two disk areas plus the wall, substitutes h=V/(πr²), and obtains S(r)=2πr²+2V/r on r>0. Its derivative 4πr−2V/r²=2(2πr³−V)/r² is correct using B146/B156. This is the changed objective, not a reuse of the open-can optimum under a new name. V remains fixed. The calculation is complete enough to reconstruct all cancellations and constants.

**P044 (T166–173).** The unique positive zero is r*=(V/(2π))^(1/3). The numerator has opposite strict signs on the entire two sides, so P019's decreasing-then-increasing proof applies globally. The positive reciprocal and quadratic terms also diverge at the open ends; this is a boundary check, not the sole existence proof. From V=2πr*³, h*=2r*, ratio 2, and Smin=2πr*²+4πr*²=6πr*²=6π(V/(2π))^(2/3). The equations and dimensional exponents are all correct. No unprovided general optimisation theorem is needed.

**P045 (T175).** Height 2r* equals diameter. Compared at the same V, the closed-can radius is 2^(−1/3) times the open-can radius, hence smaller; its height is 2·2^(−1/3)=2^(2/3) times the open-can height, hence taller. These factors are immediate deductions from the earlier displayed formulae using B46; the qualitative explanation about an extra disk's radius-dependent area cost is consistent with them. The unit check follows P022. The return link targets q2, which is present. The shape claim is not generalized to unequal material costs.

**P046, Solution Q3 recall (T177–179).** The solution includes stationary and defined-but-nondifferentiable interior inputs, included endpoints, excluded boundaries, unbounded directions and discontinuity values/side behavior. It correctly limits the automatic attained-extrema comparison guarantee to the continuous finite closed-interval setting. P007–P011 establish these principles, and P008 supplies the |x| and x³ examples. The allowance for equivalent explanations is assessment guidance rather than a substantive mathematical gap. In connection with P009, this is a candidate/existence framework, not a finite algorithm for arbitrary infinitely complicated domains; P009's finite-candidate qualification remains part of the explanation.

**P047 (T181–185).** Solving the inequalities gives [1/4,3/4]. The unchanged perimeters give the unchanged A, and its sole stationary input remains 1/2. Direct substitution gives A(1/2)=1/32 and A(1/4)=A(3/4)=[1/16+9/16]/16=10/256=5/128. The displayed arithmetic is correct and the endpoints are genuinely admitted in this model. No source-specific number or calculator lookup is required.

**P048 (T187).** Continuity and the full candidate list give the stated maximum 5/128 at both endpoint cuts, and minimum 1/32 only at 1/2. Uniqueness of the minimum follows the strict sign pattern or the square identity; no additional interior tie is omitted. The comparison 1/32=4/128<5/128 is valid. Swapping x and 1−x exchanges the sizes of the two squares, as already established in P026. Both attaining cuts are correctly reported even though they represent the same unordered size pair.

**P049, complete ending (T189).** The final domain is (0,1); the minimum at 1/2 remains attained. The old boundary cuts 1/4 and 3/4 are ordinary permitted interior points now. Moving toward an excluded zero-length piece while remaining positive gives values greater than at either old cut. P031's direct improvement proof and strict inequality A<1/16 show no maximum, while the limiting values give least upper bound 1/16. This conclusion concerns exact admissibility, not numerical rounding or experimental error. The final q3 and hints return targets exist in the text. The entire final passage, including its last links, was read; there is no unexamined ending after the reported result.

## Findings, dependencies and limits

**Established defects:** None found within the admitted mathematical content and actual figures. In particular, the stationary-versus-global distinction, open/closed domains, degenerate-wire convention, missing-lid change, formula coefficients, all requested values/locations and the no-maximum cases are correctly handled.

**Established supported bridges:** P006's exponential comparison is grounded in the actual Further Mathematics expansion B409. P007 derives the necessary stationary condition with its two hypotheses. P009 explicitly introduces the new existence theorem and continuity condition. P014's wall formula is already supplied in Physics B527 before P015 explains it. P016–P017 preserve all feasible can configurations. P019 proves globality over the entire positive domain. Figure 5's extremum markers are reconstructible at insertion from B54 and P025, and subsequently explained in detail. None requires later material to retroactively repair an earlier mandatory use.

**Provisional concerns checked and resolved:** A finite graph cannot prove an infinite limit, but the packet gives independent inequalities/sign arguments. Divergence at open ends alone would not prove a unique global minimum, but P019/P044 use whole-domain derivative signs. Solving f'=0 alone could omit a corner or endpoint, but P007–P011 explicitly handle those categories. Treating a wire piece as a side, confusing radius with diameter, and including an excluded endpoint are all consequential alternate readings that the text and images directly address. P009's finite-candidate qualifier prevents an overclaim that all candidate sets are finite. These are not unresolved defects.

**Input/role limits:** The lecture identity, claimed original misprints, original hollow-marker style, six-relationship coverage and retained-source assertions in P001/P022/P032/P036 are not verified. Verification would require a third content/provenance input and is outside this reader's permission. Their truth is independent of the displayed derivations, so their unknown status does not block the mathematical conclusions. I have made no assessment of an unseen PDF or rendered publication beyond the actual authorized Markdown text and viewed PNGs, and no claim about a real student's mastery or learning.

**Dependency consequence:** There is no unresolved mathematical gap requiring dependent results to be marked conditional or blocked. All optimisation conclusions remain conditional on the explicit model premises: fixed positive volume, ideal surface-area cost and geometry for the cans; no waste, specified total length and the stated admissible cuts for the wire. These are legitimate stated premises, not defects. Changing them would require a changed objective/domain, as Q2 and Q3 themselves demonstrate.

This is the original report for this one frozen teaching-v2 revision. It has not incorporated feedback or another revision's content.
