# SASIS original fresh-reader report — D015-r21-v2

Status: provisional pending root verification of complete actual input access. This is an unchanged original report on the frozen bundle, not author feedback, an edit, a simulated student's performance, a problem battery, or a grade.

## Scope and outcome

I read the complete four-subject baseline before the teaching. I then read all teaching in its intended order, inspecting each supplied PNG and a complete local rendering of its supplied SVG at the stated placement; only afterward did I read every hint and solution. Exact access and hashes are in `access-log.md`.

Within the permitted inputs, I found the central mathematical development available, justified and correct: operator action, the Gaussian family including its completeness and zero case, the conditional separation template, inverse branches and intervals, the ray-slope parabola family, and the ellipse construction with its exceptional points. The questions' requested mathematical connections are available before their use; the later hints and solutions are not needed to repair an earlier required step. This conclusion is confined to the recorded witnesses below and is not a claim that every latent error is absent or that a human has learned the material.

There are two limits to the conclusion, not mathematical defects in the assessed development. The quantum aside supplies contextual physical assertions rather than a derivation from the baseline; its precise quantum interpretation and scientific validity cannot be independently checked from these inputs. Historical/source-fidelity assertions, including the stated source typos and examination notice, are likewise reports within the teaching rather than independently verified history. I did not follow their links. Neither limit blocks the ODE work.

## Locator and premise conventions

`B` means the baseline's stable 1-based LF slots from `read_bytes().decode().split('\n')`, retaining internal CRs; `T`, `H`, and `S` mean the analogous teaching, hints and solutions slots. Figures are identified by their complete supplied filenames. Blank lines, anchors and links were read too. They introduce no extra subject premises.

Every witness identifies the meaning/conditions, permitted premises, consequential connection, accessibility and consequential alternative readings. An introduced definition, theorem or physical assertion is explicitly distinguished from a deduction where that matters. Routine substitution, rearrangement and arithmetic use B28, B30–32 and B38; subsequent witnesses cite that warrant without expanding each arithmetic operation. No qualification name or topic label supplies an unstated rule.

## Complete baseline intake

These are intake witnesses, not a substitute for the actual full reads recorded in the log.

| Read packet | Content actually read and usable status |
|---|---|
| B1–150 | Instruction-confined baseline contract; arithmetic, logic, algebra, functions, graph changes, gradients, trigonometry, logarithms, and derivative definition. Particularly B32 division/non-converse cautions, B38 deduction, B62 inverse branches, B68 slopes, B130 exponential positivity and logarithmic inverse, B138–150 derivatives. |
| B151–300 | Product/quotient/chain rules B158–164; derivative signs and tangents B166–170; antiderivatives and initial constants B178–201; separation and omitted constants B205–209; component vectors, probability and data, normal models, and beginning of mechanics. B183 explicitly supplies the logarithmic absolute-value antiderivative on either nonzero interval. |
| B301–450 | Remaining mathematical mechanics and declared limits; Further Mathematics induction, complex numbers, matrices, real scalar products, calculus, improper integrals, inverse trigonometry, ODEs, statistics. Relevant explicit premises include B413 arctangent derivative and B419 general/particular solutions. Excluded topics are not silently granted. |
| B451–600 | Further statistical inference, regression and mechanics through all FM71; Physics reference data, units, measurements, practical methods and early motion/force discussion. B497 explicitly withholds quantum formalism and B501 disallows inferring it merely from complex arithmetic. |
| B601–750 | Physics equilibrium, energy, circuits, waves, photon and matter-wave models, gases, oscillations, gravity, astronomy, fields and nuclear introduction. B666 explicitly withholds wavefunctions/operators/Schrödinger theory; B686–688 supply classical harmonic-oscillator meaning; B706 supplies discrete atomic energy levels, not the quantum-oscillator postulate. |
| B751–900 | Remaining Physics, its scope limits, then Chemistry metadata, calculations, atoms, bonding, structure and shape. No quantum-state formalism is added here. |
| B901–1050 | Chemistry polarity, acid/base, redox, inorganic complexes, rate laws, equilibrium and start of quantitative acidity. Usable original explanations were read, but they do not supply premises needed by this ODE lesson. |
| B1051–1200 | Chemistry weak acids/buffers, enthalpy/entropy/Gibbs, electrochemistry, organic representation and mechanism introduction. B1135 explicitly withholds statistical-mechanical identities; none is imported here. |
| B1201–1378 | Remaining mechanisms, synthesis, analysis/spectroscopy, practical reasoning, scope and source references, including final empty LF slot. These were read as part of the complete baseline; source links were not followed. |

## Chronological teaching witnesses

### Opening and section 1

**W01 — T1–7: identity, route and purpose.** The text identifies itself as reconstructed notes, declares five generated tasks, and specifies sequential reading followed by later retrieval. Familiar operations named here have actual operational warrants in B28, B62, B68, B138–209, B413 and B419, so their availability is not inferred from their names. The source/course identity is a supplied provenance assertion; it is not independently authenticated. No calculation depends on its truth.

**W02 — T12: ODE and solution.** An ODE is introduced as a relation involving an unknown one-variable function and derivatives; first order is defined by derivative order. The every-point differentiability and interval requirement defines what counts as a solution in this lesson. B62 supplies function meaning and B138–142 the derivative/tangent meaning. Thus checking only an initial point cannot establish a solution. The distinction between a function and its value, and between an equation and an initial condition, is accessible before use.

**W03 — T14: direct integration and selection.** For a chosen antiderivative F of f, y=F+c follows from B178 and B190; constants have zero derivative by B156. B64 explains vertical translation. The example y'=2x gives x²+c by B146/B182, and y(1)=3 gives c=2 by arithmetic. General versus particular solution is already supported by B419 and also explained here. The claim is conditional on a suitable antiderivative/domain, not an assertion that every arbitrary f automatically has one. Direct integration as the simplest choice is a local method recommendation for this form.

**W04 — T16–29: operator notation and first construction.** The new word operator is immediately defined by input/output action. L[u]=u'+xu defines both summands and the use of the same input. B156 and B146 give L[x]=1+x²; the displayed operator equation consequently expands to y'+xy=0 and y'=-xy using B32 algebra. The prose explicitly excludes treating the parentheses as an ordinary numerical factor or differentiating the preceding x. The consequential change from a prescribed x-only slope to a slope depending on y is visible in the expanded equation. No quantum operator knowledge is needed.

**W05 — T31: quantum aside and its limits.** The text introduces, as contextual physical assertions, a scaled quantum harmonic oscillator, an annihilation operator proportional to this mathematical action, its lowering action, and zero output on the lowest-energy state. B686–688 supply a classical oscillator and B706 discrete energy levels in atoms, but B497/B666 explicitly do not supply quantum states or this operator law. The mathematical connection is intelligible as a newly stated claim: proportional operators have the same zero-output equation when the proportionality is nonzero, which is the intended meaning of “same mathematical form.” No actual scale factor, quantum-state construction, energy spectrum or independent evidence appears. Therefore only this contextual description is available, not its physical derivation or quantitative use. The text explicitly makes it unnecessary for the ODE; all following mathematical reasoning remains independent. The linked chapter was not treated as an input or verification.

### Section 2 and figure 1

**W06 — T36–50: separation and logarithm.** On an interval with y≠0, division gives y'/y=-x (B32). B183 gives the logarithmic absolute-value primitive, and B158–164 gives its composition derivative y'/y on either sign branch. Integration then gives ln|y|=-x²/2+c (B178, B182, B190). The dy/y notation is explicitly an abbreviation of this chain-rule reasoning, not unsupported cancellation of independent infinitesimals. Combining two integration constants into one uses routine rearrangement. The nonzero interval condition is present before division.

**W07 — T52–59: exponentiation, sign and restored zero.** B46/B130–132 support exponent laws, positivity and inverse logarithms, giving |y|=e^c e^(-x²/2). B60 gives y=±|y|. On the current interval the text states continuous y cannot pass from one sign to the other without zero, consistent with B213's continuous sign-change property; the sign is fixed, so a=±e^c is a fixed nonzero real number. Direct substitution of y=0 yields the missing constant solution. There is no mistaken claim that e^c itself could be zero. The statement that this is the final family is followed immediately by its completeness argument; it is not used in an exercise before that argument.

**W08 — T61–68: verification and completeness.** B146–164 supply the derivative and product rule. Multiplying any solution by e^(x²/2) gives derivative e^(x²/2)(y'+xy)=0 without division by y. T68 expressly supplies the theorem that a differentiable zero-derivative function is constant on an interval; it is also consistent with B178's antiderivative family. Hence every solution has y=a e^(-x²/2), including any taking a zero value. This excludes unexamined zero-crossing solutions without an imported uniqueness theorem. The quantifier “on an interval” matters: independently disconnected domains would not share a forced constant.

**W09 — T70: initial height, transformations and units.** B46 and B130 give e^0=1, hence a=y(0); B64 gives scaling/reflection, with a=0 the axis. This explains every real a geometrically. The explicit dimensionless convention prevents a physical units interpretation from being tacitly assumed.

**W10 — T72, full figure 1 PNG and SVG render at this placement.** Both show labelled x and y axes, x=-6 to 6, a symmetric positive bell peaking at (0,1), and tails visually merging into the axis at finite drawing resolution. This is consistent with W08–09. Mathematical positivity already supplied by B130 prevents reading the rendered tail as exact finite zero. Both formats convey the same consequential graph information; neither is clipped or missing labels. No unrendered SVG filename was used as a proxy for viewing it.

**W11 — T74: graph explanation.** Replacing x with -x preserves x² (B28); -xy changes from positive to negative across zero for the positive solution, so B166 gives a maximum of 1. The tail limit follows from the supplied exponential: for t=x²/2 growing positively, e^t≥1+t follows from B409's real exponential series with positive terms, so 0<e^-t≤1/(1+t) tends to zero. Thus the non-reaching-zero statement is justified independently of pixels. “Redraw of the source” remains a provenance assertion, separate from this verified mathematical graph.

**W12 — T77–79, Q1.** The requested distinction L[x²] versus solving L[y]=0 uses W04 and B146; the two initial values and zero-divisor discussion use W07–09. All required connections are present before the task. A response need not infer operator meaning from unfamiliar notation or use a later solution as a premise. Checking both the equation and initial condition implements W02 rather than conflating them.

### Section 3

**W13 — T84–90: separable definition and construction.** The definition y'=f(x)g(y) is explicit and also supplied by B205–209. f and g have identified roles. In x(1+y²), x is the independent-variable factor and 1+y² the value-dependent factor. The reverse construction from a verbal multiplicative slope condition follows by multiplication, not by an unexplained selection method. The definition does not claim every equation can be rearranged this way.

**W14 — T92–105: antiderivative template.** Where g(y)≠0, h=1/g is defined, H'=h and F'=f are chosen. B158–164 gives dH(y(x))/dx=H'(y)y'=y'/g(y)=f(x), so B178 gives H(y)=F(x)+c. Every capital/small-letter relationship is explicit. Existence of those chosen antiderivatives is a condition of this template, not a theorem for arbitrary discontinuous functions. The path from factorisation to integrable expression is complete.

**W15 — T107–113: implicit and explicit, inverse conditions.** Implicit relation is defined; when H is invertible on a selected branch and the input lies in its inverse domain, B62 permits applying H^-1. The inside-out composition order and distinction from reciprocal are explicit. Differentiation of H(y)=F+c reverses the chain-rule step for a differentiable branch where the functions/division are defined. It does not license arbitrary multi-valued relations as globally differentiable y(x).

**W16 — T115: excluded constants and domain limits.** For g(b)=0, the constant y=b has derivative zero (B156), and the original RHS is zero wherever f is defined. Testing it is justified by B205–209 and W02. The requirement to remain on valid intervals and not join branches or cross singularities prevents treating the generic template as an exhaustive existence/uniqueness theorem. In equations with other kinds of nonconstant zero-crossing solutions, this template alone is expressly not offered as a completeness proof.

**W17 — T117–124: Gaussian matching, sign correction and inverse branches.** f=-x, F=-x²/2, g=y, h=1/y and H=ln|y| agree with B146/B183 and W06. The stated alternative f=x is inconsistent with that F by differentiation, so the internal sign correction is checkable; its attribution to a source page is not independently checkable. B60/B62/B130 give the two inverse branches ±e^z. The same output at y and -y explains why no single inverse exists on all nonzero reals. This supplies the reason for both signs rather than merely displaying them.

**W18 — T126: square-root branch example.** B46/B48–60 supplies the two real roots and x≥-1 domain. y(0)=1 selects the positive root locally; the negative root fails that datum. B146/B164 gives 1/(2√(x+1)), which excludes the endpoint as a differentiable solution input. The text says to check the relevant ODE too; it does not invent a specific ODE from the relation or claim that square-root reality alone establishes one.

**W19 — T129–131, Q2.** W13–16 and supplied arctangent antiderivative/range make all roles and branch questions accessible. Independently B413 and B107 supply that derivative/range. From arctan y=x²/2 after the initial datum, inverse-domain consistency gives x²<π and the interval (-√π,√π); differentiation uses B154/B164 and identity B111. Positivity of 1+y² shows division loses no root of g. A constant candidate would fail at any nonzero x in an open interval, so zero slope at x=0 alone is insufficient. This witness records availability of the requested connections, not a learner score.

### Section 4 and figure 2

**W20 — T136–140: ray slope to equation.** B68 gives the slope from (0,0) to (x,y) as y/x for x≠0, B138 supplies tangent slope y', and the stated twice-slope condition yields y'=2y/x. Signed slope multiplication is intended. No conclusion about twice the angle is implied; slope is the actual named quantity.

**W21 — T142, full figure 2 PNG and SVG render at this placement.** The legend identifies y=x², dashed ray y=x and red tangent y=2x-1; the marked (1,1) is their common point. The parabola and two straight lines, labelled axes and scale are fully visible in both. From B146/B166 the derivative at x=1 is 2 and its tangent has the plotted equation; the ray has slope 1 by B68. The figure illustrates the general condition with a specific instance; it neither proves it for every curve nor depicts a general angle-doubling rule. Different horizontal/vertical plot extents do not affect the numerical slope equations.

**W22 — T144: figure caption.** The caption explicitly identifies chosen point/curve and supplies the tangent equation; expanding it recovers the legend equation. The twice-slope/twice-angle distinction is correct from B68 and B101's tangent ratio. Claimed relation to a source schematic is a historical assertion; the actual exact illustration is independently checkable from its displayed functions.

**W23 — T146–159: solving the parabola equation.** On nonzero y and x, W06/W14 and B183 yield ln|y|=2ln|x|+c. B132/B46 gives e^c|x|²=e^c x²; fixed sign gives y=ax² and testing zero restores a=0. B146 verifies 2ax=2y/x on an interval avoiding zero. The sign of x cannot be discarded inside a logarithm, but squaring its absolute value is legitimate. The interval qualification accompanies the family.

**W24 — T159–166: completeness and family examples.** B161 quotient rule simplifies d(y/x²)/dx to (xy'-2y)/x³, zero for x≠0 by the original equation. The T68 constant-derivative result now supplies y/x²=a without division by y. Positive/negative a transforms x² according to B64, while a=0 degenerates to a line. Every displayed parameter/function pair, including -2x² and 100x², follows by substitution. The alternative printed expression y=-2y² would not be that family substitution, so the correction is internally meaningful. Actual source typography remains unverified.

**W25 — T168: continuation and independent sides.** The polynomial itself differentiates at zero (B146), but 2y/x is undefined there by B32. Thus the ODE and origin-ray interpretation have no value at zero. Each connected positive or negative interval has its own constant by W24; no requirement given so far equates them across the excluded input. The statement is explicitly qualified by possible additional connecting requirements. Showing a full polynomial in a plot is not a claim that the ODE holds at every plotted input.

**W26 — T171–173, Q3.** W20 and W23–25 supply construction, family, parameter selection and forbidden-input explanation before the task. Substituting (2,-4) fixes a=-1; B68 and differentiation yield signed slopes -2 and -4. “Twice” cannot be mistaken for only an unsigned magnitude rule because the signed equation is already specified. No missing datum or later-only justification is needed.

### Section 5 and figure 3

**W27 — T178: family parameter elimination.** For x≠0, y=ax² solves uniquely for a=y/x² by B32; B146 gives 2ax=2y/x. Every non-axis point with such x therefore identifies a member and its tangent slope. The origin is correctly outside this parameter-elimination step, where division would fail and many parabolas pass through one point.

**W28 — T180–184: perpendicular direction.** B68 explicitly supplies the finite perpendicular-slope product and horizontal/vertical exception. T180 restricts to finite nonzero slopes, so x≠0 and y≠0 give the negative reciprocal -x/(2y). This is a deduction from geometry with explicit conditions, not a new unchecked slope rule. A zero original slope is deliberately not processed by this reciprocal formula.

**W29 — T186–193: integration and verification.** Multiplying y'=-x/(2y) by y gives yy'=-x/2. The chain rule B164 makes y²/2 a primitive, B182 integrates -x/2, and rearrangement gives x²/4+y²/2=c. Implicit differentiation B170 restores x/2+yy'=0 and the slope where y≠0. Multiplying the two finite slopes gives -1 where x and y are nonzero. Every algebraic and geometric implication retains its conditions. No restriction that c be positive has yet been assumed; it is considered next.

**W30 — T195–201: ellipse identification and exceptional c.** For c>0, division and positive square roots rewrite the denominators correctly. The word ellipse is intelligibly introduced as a coordinate-stretched unit circle; B70 supplies the circle equation and B377 the coordinate-axis stretching meaning. Substitution X=x/(2√c), Y=y/√(2c) verifies that description directly. Ends at ±2√c and ±√(2c) give the defined semiaxes and ratio √2. A sum of nonnegative squares is zero only at the origin and cannot be negative, establishing the c=0 and c<0 alternatives. No unprovided conic theorem is required.

**W31 — T203, full figure 3 PNG and SVG render at this placement.** Both show four dark parabolas through the origin, two teal ellipses wider horizontally, and labelled axes/legend. The crossings away from axes have visibly distinct tangent directions; their exact right angles rely on W28–29, not eyesight. The horizontal-to-vertical semiaxis ratio is consistent with W30 and the equal coordinate scaling. Ellipse tops on the y-axis and ends on the x-axis are visible; at this placement they do not imply that the reciprocal-slope calculation was defined there, since W28–29 already excluded the axes for that derivation. All consequential information is present in each full rendering.

**W32 — T205: figure parameters and the a=0 case.** The named ±0.4 and ±1 parabolas have the plotted signs/openings by W24; c=0.4 and 1.2 produce approximate horizontal ends 1.265 and 2.191, and vertical ends 0.894 and 1.549 by W30, consistent with visible ticks. The horizontal a=0 member is identified as not separately drawn as a dark family curve; the axis is visible. The text appropriately rests perpendicularity on the slope product. These exact parameter claims are internal descriptions checked against the plotted geometry, not independent certification of how the source figure was produced.

**W33 — T207–214: explicit branches and domains.** Rearrangement of the implicit relation gives y=±√(2c-x²/2). B46/B62 and W18 identify upper/lower branches and strict interior differentiability. Their derivative is -x/(2y), finite on (-2√c,2√c); in particular x=0 is permitted by this simplified ODE, even though its original geometric derivation required x≠0. This is directly checkable from the displayed formula at this point and does not depend on the later explanation. Endpoints have y=0 so the derivative quotient fails there. The c=1 example and point (√2,1) give slope -1/√2, parameter 1/2 and original slope √2 by W27–29; the product is -1. Reality at an endpoint is kept distinct from differentiability there.

**W34 — T214–216: vertical endpoint tangent.** The vertical-tangent statement is immediately supported by switching local graph direction: near either nonzero-x endpoint the ellipse can be written x=±2√(c-y²/2); B146/B164 or B170 gives dx/dy=-2y/x, zero at y=0. The tangent then has constant x direction and varies in y, so is vertical (B68/B166). No division by y or reciprocal of zero is needed. The geometry claim is justified before any practice requires it.

**W35 — T218: geometric continuation versus ODE graph.** B62's single-output function definition explains why the complete ellipse is not a single y(x). The x-axis endpoint tangent from W34 is perpendicular to horizontal y=0 using the exceptional slope pair in B68. At x=0, every finite-a parabola has y=0, while the ellipse has y=±√(2c)≠0, so there is no member intersection there. The ellipse branch ODE is regular at those points by W33. These are three distinct propositions: a geometric orthogonality extension at horizontal ends, an undefined ODE at those ends, and regular ODE points with no intersecting family member at the vertical axis. The prose separates them explicitly; there is no unresolved demand to apply the original 2y/x at x=0.

**W36 — T221–223, Q4.** W27–35 supply all requested connections before this task: parameter elimination, negative reciprocal, integration, c from (2,1), coordinate stretches, branch selection, valid ODE interval and full-curve endpoint interpretation. Arithmetic gives c=3/2, semiaxes √6 and √3, positive branch √(3-x²/2), a=1/4, slopes 1 and -1. The wording asks where the branch satisfies the simplified ODE, whose domain includes x=0 with y≠0, rather than silently requiring 2y/x there. Thus the possible domain ambiguity has an explicit resolution in earlier teaching.

### Ending and later retrieval

**W37 — T226–237: historical notice.** The six named examination topics and a harder-than-first-exam warning are presented only as the source's closing notice. The note explicitly disclaims teaching all six or forecasting this reader's examination. The mean value theorem is only named here; it is not imported backward to justify the zero-derivative theorem at T68, which was explicitly supplied there. Source-history accuracy cannot be independently established under this read restriction. No substantive course computation depends on it.

**W38 — T240–242: study instruction.** Retrieval is explained as stating conditions from memory and application as choosing/checking methods. The suggested delay is adjustable rather than an empirical optimality claim. These instructions do not grant new mathematical premises or constitute evidence of actual learning, retention or fixed ability.

**W39 — T244–246, Q5.** The x-only derivative invokes W03 and B182, while the product 2y/x on the negative half-line invokes W23–25 and B183's absolute-value logarithm. The proposed 2x can be tested separately against its derivative, RHS and initial value using W02. Requirements before separation were explicitly taught in W14–16. Direct integration is a simpler choice for (i), but separation with g=1 is not logically excluded by the definition; the question asks to justify a choice, not assert mutually exclusive method classes. All needed content is present before the ending.

## Subsequent hints: chronological witnesses

**W40 — H1–10.** The hint route and Q1 cue use T22, T59–70 and B146. Differentiating x² and multiplying that same input by x are independently specified actions; evaluating at zero selects a. Testing the zero function in the original operator correctly targets the division issue. No new repair premise is introduced.

**W41 — H12–17.** The Q2 cue uses T90–113/T131 and B107/B413: reciprocal factor, arctangent primitive, its output range, then the inequality in x. The warning against periodic tangent extension is warranted because an inverse branch has a fixed range. It does not deny that other disconnected tangent expressions may solve a differential equation on their own domains.

**W42 — H19–24.** The Q3 cue follows T136–168: signed rise/run, twice that slope, point substitution in the family and original denominator check. Each hinted operation already has a prior warrant.

**W43 — H26–31.** The Q4 cue follows T178–218: eliminate a, take the reciprocal only where allowed, substitute point in the implicit family, identify squared semiaxes, select positive root and strictly positive radicand. A positive radicand is the appropriate finite-derivative condition for this family with c>0, not a universal claim about every square-root expression.

**W44 — H33–39.** The Q5 cue follows T14, T146–168, T244: direct integration for prescribed x-only slope, separation for this product, x<0 with ln|x|, and independent equation/initial-condition checks. The last return link and final empty slot were read. Nothing later is needed to validate the hints' mathematics.

## Subsequent complete solutions: chronological witnesses

**W45 — S1–8.** The solutions identify their role and Q1 computes L[x²]=2x+x³ using B146 and T22. The explicit function-input/function-output distinction corrects the consequential misreading of x² as a constant label. Correct and accessible.

**W46 — S10–16.** The two initial values select -2e^(-x²/2) and zero via T70. Differentiation and multiplication cancel exactly in the first; both terms vanish in the second. T61–68 supplies completeness, and B130 supplies exponential positivity, so the anticipated e^c=0 error is correctly rejected. These are verification steps using earlier teaching rather than missing explanations first supplied in a solution.

**W47 — S18–25.** Q2 assigns f,g,h,H,F correctly; 1+y²>0 for every real y supplies the no-zero-factor condition. Integrating to arctan y=x²/2+c uses T92–105 and B413. No unannounced inverse convention appears.

**W48 — S27–34.** arctan 0=0 follows from B101/B107, fixing c=0. The tangent inverse is restricted to (-π/2,π/2); the inequality gives x²<π, hence the largest open interval containing zero. As x approaches either endpoint from within it, the argument approaches π/2 from below, where sin tends to 1 and cos tends to 0 positively (B101 and its continuous differentiable trig functions B152–154), so tangent is unbounded. Periodic finite pieces cannot pass continuously through that blow-up and cannot obey the same principal arctangent relation. The interval conclusion is thus justified, not guessed from a familiar answer.

**W49 — S36–38.** Chain rule and sec²=1+tan² (B154/B164/B111) verify the ODE; evaluating at zero verifies the initial datum. The constant-candidate argument uses the every-point interval requirement T12 and 1+b²>0, distinguishing a single zero of f from a zero of g. Correct.

**W50 — S40–49.** Q3 constructs the signed geometry equation and uses ln x on x>0, which is valid by B130/B183. The integration and y=ax² reduction repeat T146–159 with the correct domain. No omitted-negative-y restriction is imposed; |y| is retained.

**W51 — S51–57.** The zero family member fails the datum, a=-1 follows, and direct differentiation verifies y=-x². Signed slopes -2 and -4 are correct. The distinction between a smooth polynomial value at zero and the undefined original ODE/ray is exactly T168, not a new late exception.

**W52 — S59–74.** Q4 repeats parameter elimination and the qualified reciprocal, then integrates to x²/4+y²/2=c. Substitution gives 3/2; multiplying/dividing yields x²/6+y²/3=1. These routine operations have B28/B32 and T178–201 warrants, and the equations are mutually consistent.

**W53 — S76–82.** Positive semiaxis lengths √6 and √3 follow from T201, not from mistaking denominators for lengths. The datum selects the plus root and interval (-√6,√6). Differentiation gives the stated slope, point value 1, parameter 1/4, and slope product -1. All values and conditions agree.

**W54 — S84–86.** Full ellipse, two branches, endpoints and non-single-valued status are distinguished using T214–218/B62. Continuous endpoint inclusion is not called an ODE extension; the vertical tangents are justified by the already supplied reverse-graph calculation. The two y-axis points do not intersect the finite-a family. No new unsupported geometric rule appears.

**W55 — S88–91.** Q5(i) integrates to x³+c and the datum fixes c=1; derivative and value checks are correct on all reals. The observation that g=1 also permits separation follows directly from T84–90 and prevents falsely treating method choice as an exclusive classification.

**W56 — S93.** For Q5(ii), ln|x| remains real on x<0; the zero case is checked then rejected by the datum. a=2 gives y=2x² with derivative 4x and correct initial value. Negative x does not introduce a sign change into |x|². This repeats an earlier complete route with changed interval/data.

**W57 — S95.** The proposed y=2x has derivative 2 but RHS 4 on every allowed x and value -2 at x=-1, so both required conditions fail. Either failure suffices by the solution definition. The conclusion is logically stronger than merely checking the initial value and is arithmetically correct.

**W58 — S97–100.** The final rules retain original domain, require g(y)≠0 for division, test factor zeros separately, and respect logarithm/inverse/square-root restrictions after integration. “Conditional equivalence” accurately summarises T92–115 rather than promising legal cancellation at zero. The final return links and final empty LF slot were read; independent material was followed through the ending.

## Precise unresolved matters and dependent conclusions

1. **Quantum scientific verification (T31):** the exact coordinate scaling, nonzero proportionality coefficient, quantum state definition and physical derivation/evidence are not supplied. The qualitative operator-context claim is available as newly stated information; it cannot be independently derived or scientifically authenticated from this baseline. Only that aside's deeper physical interpretation depends on this missing information. Operator action and every ODE result remain supported independently.
2. **Historical/source verification (T3, T7, T31, T74, T124, T144, T166, T205, T228–237):** no permitted input contains the linked source documents for independent comparison. The internal corrected equations and figures are checkable, but assertions about original printing, figure fidelity, course identity and exam notice remain supplied reports. No mathematical answer depends on independently establishing those provenance claims.
3. **Access certification:** my report and actual transcript record complete input access with no observed truncation or rendering failure. The requested root verification is still pending. This is an audit-status limitation, not a remaining teaching dependency.

No unresolved mathematical connection was found in the main development or its hints/solutions within this reading. This qualified conclusion does not assert exhaustive detection of every possible error or any human learning outcome.
