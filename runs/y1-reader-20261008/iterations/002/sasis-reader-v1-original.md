# SASIS original report: frozen document D002 v1

This report evaluates the supplied teaching as a reading route for the supplied four-subject baseline. It is not a student examination, a retention measurement, or an independent verification of the original MIT source. On the actual interval and punctured-interval domains used here, I found supported routes through the substantive explanations and all six question demands. I found no established consequential teaching defect and no blocked downstream calculation. One limited concern about the scope of the verbal limit definition is recorded below; it does not affect the presented examples. Source-correspondence assertions remain unverified rather than treated as established source facts.

The original report was prepared before subject-content author feedback. An operational clarification about mixed line endings supplied no subject premise. No outside retrieval, other-agent subject input, delegation, or additional subject-content file was used.

## Input identities and actual access

All input hashes and byte counts matched the supplied identities before reading the teaching.

| Input | Bytes | Raw UTF-8 decoded characters | SHA256 |
|---|---:|---:|---|
| baseline.txt | 247840 | 246945 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 |
| document.md | 34994 | 34968 | 8139080278edb96287576629e7d80933b380c1b82af60d3ede888d500cb68a3a |
| figures/unit-circle-proof-v1.png | 90094 | not text | 95616719d3035e9f174367b55c48ccb3e04a8cbf5105434115e4bddff0b3c75d |

The supplied document identity is associated with frozen commit f1c0e91c24e9140049d50c7ca965f41e36f3e1a2. I did not retrieve that commit or the linked lecture PDF. The local hashed inputs are the actual materials evaluated.

The complete baseline was read before the first teaching passage. It included Mathematics A H240; Further Mathematics H245 Pure Core, Statistics and Mechanics; Physics H556; and Chemistry H432, through the final reference/provenance text. No topic names or external links were used in place of operational content.

There was a character-accounting deviation that needs to remain visible. The initial chunk reader used Path.read_text(), which normalizes mixed line endings. Its normalized length was 245568 rather than the raw decoded length 246945. The first thirteen chunks each emitted 18000 normalized characters. The last requested range extended past normalized EOF and emitted 12868 characters; its printed EOF comparison was false because it compared a raw-length endpoint with the normalized length. This was not tool-output truncation. I then compared the normalized text with an explicit character-by-character normalization of read_bytes().decode('utf-8'), verified equality, and mapped every boundary back to raw decoded offsets. The complete delivered text covered raw EOF; 1377 CRLF pairs account for the length difference, with isolated carriage returns also represented as line feeds. No subject text was omitted.

All offsets below are zero-based and half-open. These are the actual ranges, not merely the initially intended raw-character ranges.

| Read order | Delivered normalized range | Corresponding original decoded range |
|---:|---|---|
| 1 | [0,18000) | [0,18123) |
| 2 | [17900,35900) | [18023,36171) |
| 3 | [35800,53800) | [36069,54168) |
| 4 | [53700,71700) | [54066,72142) |
| 5 | [71600,89600) | [72040,90106) |
| 6 | [89500,107500) | [90004,108111) |
| 7 | [107400,125400) | [108009,126085) |
| 8 | [125300,143300) | [125985,144063) |
| 9 | [143200,161200) | [143963,162074) |
| 10 | [161100,179100) | [161974,180098) |
| 11 | [179000,197000) | [179998,198109) |
| 12 | [196900,214900) | [198007,216124) |
| 13 | [214800,232800) | [216024,234120) |
| 14 | [232700,245568) | [234020,246945) |

The explicit raw-decoded verification reread was [246500,246945), emitted 445 characters and confirmed EOF. Apart from the listed overlaps and that tail verification, there were no baseline rereads. Every displayed chunk contained its end marker; the tool results showed successful completion without an output-truncation notice. Output budgets were 14000 tokens for the first thirteen chunks and 12000 for the final chunk, above the returned outputs. The range-mapping check had its own complete output. The newline normalization is a disclosed delivery deviation, not a claim that the initial labels were raw decoded offsets.

The teaching was then read as raw UTF-8 decoded text in exactly this order:

1. [0,18952), through P35 and the complete figure reference, emitted 18952 characters.
2. The exact referenced PNG was opened and visually inspected.
3. [18952,34968), beginning with P36 and continuing through P72 and the final return links, emitted 16016 characters and confirmed EOF.

Both text calls had visible end markers and no truncation. No teaching text was reread. All P01–P72, Q1–Q6, H1–H6, S1–S6 and the constituent PNG are covered below. This is a complete-access conclusion, not a claim that every byte was simultaneously resident in context.

## Baseline locators used in reconstruction

The baseline's Mathematics headings supply these reusable premises:

- **Prior arithmetic, geometry and mathematical language:** signed arithmetic, Pythagoras, right-triangle trigonometry, elementary circle geometry, triangle area, domain/interval notation, implication versus converse, and the nonzero requirement for division.
- **Proof and mathematical work:** deduction from stated premises, counterexamples, interpretation of models and their limits.
- **Algebra, functions and coordinate geometry:** cancellation with retained exclusions, function domain/range, modulus and inequalities, coordinate geometry, circle equations, graph transformations and parameter restrictions.
- **Sequences, series and binomial expansion:** sequence notation and convergence as approach to a finite limiting value.
- **Trigonometry:** unit-circle coordinates, sine/cosine parity and periodicity, exact values, tangent as a quotient, radian arc/sector formulae, and the double-angle identities. Small-angle approximations are supplied, but are not needed as a substitute for this document's proof.
- **Differentiation and its applications:** the finite difference-quotient definition, power/chain/implicit differentiation, tangent-gradient interpretation, derivative units through rates, and the connection between derivative signs and increasing/decreasing graphs. The baseline also already supplies the two small-angle limits used for first-principles sine/cosine differentiation; the document independently justifies them.
- **Mechanics:** signed position/velocity versus distance/speed and differentiation of position in time.

Physics sections **1, Quantities, mathematics, measurement and evidence**, **2, Forces, motion, energy and materials**, and **3, Current and circuits** additionally supply units, rates, signed velocity and charge-flow interpretation. Further Mathematics and Chemistry were read in full; no additional rule from them is necessary for the principal routes below. In particular, no Maclaurin remainder theorem, formal epsilon-delta theorem, outside numerical table or unstated scientific model was used to fill a gap.

## Chronological reconstruction and availability

### P01–P09: orientation, limits and an excluded input

**P01–P02.** The title and navigation identify a lecture-based route, six questions, then hints and solutions. The stated prerequisites are present in the baseline. The document does not require following its external lecture link to define an object used in the first example. Its claim that additional limit/continuity reasoning will be developed is borne out by the subsequent definitions and rules. Lecture identification and exact source fidelity are author-provided provenance, separately limited below.

**P03.** The finite-limit statement distinguishes the input approaching a from the output approaching L, requires all sufficiently close nonexcluded domain inputs, and excludes reliance on f(a). On the domains actually used, this makes a point-value change irrelevant while allowing a two-sided failure when left and right behavior differ. Ordinary quantification and the baseline's function/domain language make this intelligible without a formal epsilon-delta prerequisite. The arbitrary-domain edge of this wording is the limited concern recorded below; no actual example uses an isolated input.

**P04.** Sum, difference, product and quotient limits are explicitly supplied as rules, with finite-limit hypotheses and a nonzero limiting denominator for quotients. They can be accepted as newly stated mathematical premises; no prior university limit-law theorem is silently required. The two exact equalities x/x=1 and x²/x=x on x≠0 give different limits despite numerator and denominator both tending to zero. They therefore justify the warning that a zero-over-zero substitution does not determine the ratio's limit. The exclusion of the point is consistent with P03 and baseline division rules.

**P05–P06.** Fixing a gives vertical change f(a+Δx)−f(a) and horizontal change Δx, so the ratio is the coordinate-geometry secant gradient. Substitution x=a+Δx gives x−a=Δx and exactly the second quotient. Neither quotient is evaluated at zero increment. The baseline already supplies this derivative definition and gradient interpretation; the document correctly requires a finite limiting slope. Output-unit/input-unit follows directly from the two differences' units.

**P07.** Charge divided by time has the current interpretation supplied in Physics, and the limiting ratio is its instantaneous version. An accumulated distance has nonnegative change and its time rate is speed; signed position instead gives signed velocity and magnitude gives speed, as supplied in Mathematics mechanics and Physics. Temperature plotted against position has a temperature-per-length ratio. This last interpretation requires no time variable: identifying the input is enough to distinguish a spatial gradient from a time rate. These are conditional interpretations of the named quantities, not newly inferred physical laws.

**P08.** For R, polynomial sum/product rules yield numerator 12 and denominator 4 at input 3. Their quotient is 3 because 4≠0. Factoring the numerator as x(x+1) gives equality R(x)=x only on the retained domain x≠−1. Baseline algebra explicitly supplies this cancellation-with-exclusion rule.

**P09 / Q1 at its actual position.** P08 has already supplied equality to x on all nearby allowed inputs. P03–P04 make those inputs sufficient for the limit −1, while the original denominator is zero at the excluded point. Thus the requested distinction is available before any hint, P20 extension discussion or S1 solution. No later explanation is needed retroactively to license this question.

### P10–P14: a declared flat model and sensitivity

**P10.** The text identifies satellite altitude s, slant distance h and surface arc L, then explicitly changes to a flat right triangle with a horizontal leg called L. It does not equate that leg with an exact curved-Earth arc. The schematic's missing measurements and Earth radius prevent a numerical or exact spherical calculation, but neither is requested. This is an intelligibly declared approximation; the following deductions are conditional on it.

**P11.** With s>0 fixed and L≥0, Pythagoras gives h²=s²+L². Solving and choosing the nonnegative root gives L=√(h²−s²), h≥s. For h>s, the root is positive and the baseline's power and chain rules give (1/2)(h²−s²)^(−1/2)(2h)=h/L. The point h=s is deliberately outside this derivative formula's asserted range.

**P12–P13.** Positive h and L give positive sensitivity and length/length units. At a fixed interior point, the definition of derivative says ΔL/Δh approaches h/L; multiplying by the small increment gives the stated local approximation, with the perturbed input still in the domain. Near h=s the positive numerator stays near s while L becomes small, so the factor grows. At the endpoint, L(s)=0 and direct expansion of (s+δ)²−s² gives 2sδ+δ². For δ>0, division by δ gives the positive square root √(2s/δ+1), which exceeds any finite bound when δ is sufficiently small. Consequently there is no finite right-hand slope there. This also justifies the distinction between an admissible endpoint and a differentiable point; it does not extrapolate a finite linear approximation to that endpoint or to arbitrary errors.

**P14 / Q2 at its actual position.** Holding h fixed instead of s changes the inner derivative of h²−s² to −2s. The same already available chain rule therefore gives −s/L; alternatively implicit differentiation is baseline knowledge. The stated 0<s<h makes L positive and the sign negative. More vertical length at fixed hypotenuse leaves less horizontal length. This meaning and length/length units are available at Q2 without H2 or S2. The held-fixed parameter change is explicit, so copying the earlier positive rate is not licensed.

### P15–P24: sides, values and types of failure

**P15–P17.** Right and left refer to the input inequalities, not the output sign. The finite two-sided criterion and continuity definition are introduced explicitly. For a two-sided approach, both sets of nearby inputs must meet the same target; conversely their separate sufficiently-close conditions can be met together by using the smaller neighborhood. Continuity adds equality to a defined point value. At an interval endpoint only the within-domain side is relevant. Open and filled markers specify branch inclusion/value rather than the approach of the branch. These explanations connect the new terms to the baseline's domains and graph representations. The restricted-domain scope is maintained in the later motion example.

**P18–P19.** The corrected formula assigns −x for x≤0 and x+1 for x>0, covering each real input once. Constants and linear-limit rules give left limit 0 and right limit 1; the included first branch gives f(0)=0. This yields left continuity, failure of right continuity, and no common two-sided limit. Replacing f(0) cannot change either nearby formula, so no point-value repair can equal both limits. The mathematical route uses the fully displayed formula; the separate claim about a printed-source sign error is not independently verified.

**P20.** A removable defect retains a common finite approach value, so assigning precisely that value meets P16. For R, the already established limit −1 makes the extension value −1 uniquely suitable. At a jump, unequal finite side limits cannot both equal any one assigned value. The verbally described horizontal-level sketch supplies only unequal levels, so the document properly refrains from assigning numerical heights or a point value. Its warning about reversed source superscripts is not needed for the mathematical distinction because P15 supplies the side meanings.

**P21–P22.** For x>0 small, 1/x exceeds any selected positive bound by taking x smaller than its reciprocal. For x<0 close to zero, writing x=−u with u>0 gives −1/u and the corresponding negative-bound behavior. Thus +∞ and −∞ denote unbounded approaches, not real values. The two signs differ, and neither side supplies a finite candidate fill-in. The statement about equal infinite behavior also follows from P16: continuity there would still require a finite real function value and finite limit. No multiplication or subtraction with infinity is used.

**P23.** The persistent-height sketch is distinguished from a mere claim of oscillation. In the separate formula v(x)=sin(1/x), the two defined positive input sequences have denominators increasing without bound and hence inputs tending to zero. Their reciprocal arguments differ by full sine periods from π/2 and 3π/2, giving exactly 1 and −1 using baseline trigonometry. If P03's universal nearby limit existed, both outputs would eventually have to lie arbitrarily close to the same number; neighborhoods smaller than half their separation cannot do that. This is a direct contradiction of the stated limit meaning, not an imported sequential-limit theorem. The symbol v_n is explicitly an input sequence, distinct from the function v. No unspecified original sketch formula is inferred.

**P24 / Q3 at its actual position.** The three disjoint cases give both near-zero formulas and the point value. P04 and P15 yield left and right limits 2; P16 then requires a=2. P19 has already shown why its unequal limiting heights cannot be repaired. Q3 therefore asks for an available comparison, before H3, S3 or the later corner discussion.

### P25–P33: slope graphs, symmetry, time coordinates and endpoints

**P25.** The power rule gives −x^(−2) on x≠0. The displayed first-principles calculation independently puts the reciprocal difference over x(x+Δx), producing numerator −Δx; cancellation is allowed for Δx≠0. At fixed x≠0, the remaining denominator tends to x²≠0, so the quotient-limit rule gives −1/x². Excluding x+Δx=0 is sufficient and is stated.

**P26–P27.** Substitution at −2,−1,1,2 gives the four listed pairs of function height and slope: (−1/2,−1/4), (−1,−1), (1,−1), (1/2,−1/4). The derivative graph places the second number at the same input coordinate; it is not plotted against the function's height. The negative derivative on each branch agrees with each branch falling as x increases. As |x| becomes small, 1/x² becomes large; as |x| becomes large, it becomes small. Its negative gives the stated steep and flattening slopes. The domain still excludes zero. The baseline explicitly supports constructing derivative graphs from tangent slopes and signs. The lecture's red graphical items are described rather than directly inspected; the numerical illustrations are correctly identified as calculated examples.

**P28–P29.** Symmetric domain, evenness and oddness are defined before their use. Replacing x by −x verifies oddness of 1/x and evenness of −1/x² without adding a zero value. For a differentiable odd function, applying the baseline chain rule to f(−x)=−f(x) gives −f′(−x)=−f′(x), hence an even derivative on the paired points. For an even function it gives −f′(−x)=f′(x), hence an odd derivative. The required paired interior derivatives are an explicit condition. The counterexample x+1 has derivative 1, which is even, but f(−x)=1−x and −f(x)=−x−1 differ. This uses the baseline's counterexample and implication/converse distinction to block the unintended reverse reading of “vice versa.”

**P30–P31.** The given height model and interval are complete mathematical premises, even though their physical units are unspecified. Since t²≥0, its maximum 400 occurs at the chosen coordinate origin t=0; negative t can label earlier events without being negative elapsed duration. Differentiating gives −32t on the interior, positive before zero and negative afterward. At t=−2,0,2 the arithmetic yields heights 336,400,336 and signed velocities 64,0,−64. Taking velocity magnitude gives speed. Substitution of −t verifies even height on the symmetric interval, and substitution into −32t verifies odd interior velocity. No height or time unit is manufactured from the coefficient 16 or the building scene.

**P32.** Substituting the two endpoints gives height zero. Expanding around −5 gives a quotient 160−16δ; expanding around 5 gives −160−16δ. Within the restricted interval, allowable small increments have signs δ>0 and δ<0 respectively, giving the stated one-sided derivatives. A polynomial extended outside the interval permits two-sided derivatives with those same numerical values, but that is a different function-domain statement. The document explicitly leaves the source dots' intended convention unresolved. The named within-domain derivatives and interior result do not depend on choosing it.

**P33 / Q4 at its actual position.** The coordinate relation is algebraically invertible: t=τ−5, so the interval maps to [0,10] and substitution gives 400−16(τ−5)². The baseline's chain rule and d(τ−5)/dτ=1 give the corresponding velocity. Its zero occurs at τ=5, the event previously called t=0. P32 already supplies the endpoint distinction, and P28 makes domain symmetry an explicit prerequisite for evenness about zero. Since [0,10] is not symmetric about zero, the shifted restricted function is not even in that sense. These demands are all available before H4/S4; no new time-scaling or physical law is needed.

### P34–P45 and PNG: construction and trigonometric limits

**P34–P35 and figure.** Unit-circle coordinates and radian arc/sector formulae are baseline premises. With 0<θ<π/2, B=(cosθ,sinθ) is in the first quadrant, C is its perpendicular foot, and OA=OB=1. The ray has slope sinθ/cosθ=tanθ, so its intersection with x=1 is T=(1,tanθ). Coordinate differences give BC=sinθ, OC=cosθ and CA=1−cosθ, while the curved arc AB has length θ. The inspected PNG locates O,C,A on one horizontal line, BC vertically, B and T on the same ray, and AT vertically at A. Its arc is visibly curved and separately labelled. OA=1, OB=1, all length labels, the radian interval and the inner/sector/outer containment heading agree with the text. No numerical angle or scale is needed from the drawing.

**P36.** The squeeze rule is both stated and explained: if both bounds eventually lie within the same prescribed interval around L, any value between them lies there as well. The absolute-value form is the special case −B≤F≤B with both bounds tending to zero. This gives the needed connection from inequalities to a limit rather than asking the learner to infer convergence from a shrinking sketch alone.

**P37.** Elementary circle geometry places chord AB inside the disk; the triangle formed by O and that chord stays within the same sector. For the outer containment, sector points are between the two rays, with x≤1, hence inside the triangle bounded by OA, OT and x=1. With base OA=1, the two triangle heights are the already identified BC and AT, giving areas sinθ/2 and tanθ/2. The sector area is θ/2 by the radian formula. Ordering these contained areas and multiplying by 2 yields sinθ≤θ≤tanθ. The figure and stated geometric reasons make this an accessible use of elementary geometry, not an untaught extensive area theorem.

**P38.** θ>0 permits division of the first inequality without reversing its sign. In the second, cosθ>0 permits multiplication by cosθ/θ after substituting the tangent quotient. The resulting bounds are cosθ≤sinθ/θ≤1. All positivity conditions are provided by the chosen quadrant.

**P39–P40.** To avoid assuming the desired trigonometric continuity, the earlier inequality gives |sin u|≤|u| for small positive u; sine oddness gives the negative case. Applying the baseline double-angle identity to θ gives 1−cosθ=2sin²(θ/2), hence the displayed bound between zero and θ²/2. P04 makes θ²/2 tend to zero and P36 therefore makes cosθ tend to 1. Substituting this into P38 gives the positive sine-ratio limit. For θ<0, u=−θ>0 and oddness cancel both signs in sinθ/θ, giving the same limit. P15 joins the two sides. This route uses geometry, identities and squeeze; it does not depend on differentiating sine or cosine to justify their prerequisite limits.

**P41–P42.** Dividing the nonnegative numerator bound by |θ| on θ≠0 gives |(1−cosθ)/θ|≤|θ|/2. Its bound tends to zero, so P36 gives the two-sided quotient limit. The argument includes negative angles through the absolute value and never evaluates the quotient at zero. The sine ratio's limit 1 therefore supplies its continuous extension value. For numerical degree input d, the radian argument is πd/180; multiplying and dividing by this argument extracts π/180, so the limit is π/180. This explains the unit convention by an exact substitution, not an unexplained warning about calculator mode.

**P43–P44.** Multiplying and dividing by 2 makes sin(2x)/(5x)=(2/5)[sin(2x)/(2x)] for nonzero x. As x approaches zero, its scaled argument approaches zero as well; the definition from P03 ensures the standard ratio can be used along these inputs. Multiplication by 2/5 gives the stated limit. No general unstated composition theorem is needed for this linear substitution. The warning about the cosine numerator is supported by its quadratic bound: tending to zero alone says nothing about how division by a vanishing denominator changes the result.

**P45 / Q5 at its actual position.** The scaled-sine example already licenses a factor 3 for the first expression. For the other two, P39 and the baseline double-angle identity give 1−cos(2x)=2sin²x. Division by x leaves 2x(sin x/x)²; division by x² leaves 2(sin x/x)². P04 and P40 give limits 0 and 2. Thus the question's contrast is available before H5 or S5. Using only the bound from P39 would not by itself determine the exact last limit, but the identity needed to do so has already been supplied; the learner is not required to invent an additional theorem.

### P46–P51: differentiability, continuity and the integrated question

**P46–P48.** The theorem explicitly assumes an interior point, a defined f(a), and a finite two-sided difference-quotient limit. For x≠a the displayed product is an exact identity. Its first factor tends to finite f′(a), and its second tends to zero, so P04 gives difference limit zero. Adding the fixed value f(a) gives the equality required by P16. The proof establishes continuity of f, not continuity of f′. An infinite quotient is deliberately outside the finite product rule. The meaning, assumptions and consequential connection are all present.

**P49.** The previously constructed g₂ has both side limits and point value 2. Its left quotient is (x+2−2)/x=1 and its right quotient is (2−x−2)/x=−1. Unequal one-sided quotients block the derivative while leaving continuity intact. This gives a concrete counterexample to the converse using an already introduced function. The discontinuity implication follows by contradiction: a finite derivative would imply continuity by P46–P48. This uses baseline logic, without assuming the converse.

**P50 / Q6 at its actual position.** The first demand recalls definitions already taught and the proved implication. Looking back is optional; it introduces no new prerequisite. For the new w, sine's unit-circle range gives |x sin(1/x)|≤|x| on x≠0, so P36 supplies the limit zero, matching w(0). The derivative quotient cancels x and becomes exactly P23's nonconvergent sine expression. Both the shrinking-height bound and the persistent quotient behavior are available before H6/S6. Calling something oscillatory alone would fail for the reason this question explicitly asks the reader to examine. The next-day revisit is labelled adjustable advice rather than an asserted learning law or an evaluation requirement.

**P51.** The source link and page map serve provenance. The actual teaching route supplies the flat-model premises, generated oscillation formula, area argument and all questions, so no unseen problem set is required for the mathematical deductions. The assertions that these constitute complete source coverage and correct particular source signs cannot be independently checked from the permitted artifacts. They are not additional usable subject premises obtained from the absent PDF.

### P52–P58: hints read after the main explanation

**P52.** The hint/solution separation and return links agree with P02's stated route. Their placement does not create a dependency needed earlier: the question-demand checks above used only baseline and preceding teaching.

**P53 / H1.** Writing x=−1+ε with ε≠0 makes the preserved exclusion explicit, permits P08 cancellation, and distinguishes the ε→0 limit from evaluation at −1. No new premise is introduced.

**P54 / H2.** Treating h as constant makes the derivative of h² zero; the baseline chain rule applied to L(s)² gives 2L(dL/ds). Thus 0=2L(dL/ds)+2s and L>0 permit division to get the negative rate. This alternative implicit route is already baseline knowledge.

**P55 / H3.** Choosing each side's formula and then applying P16 separates the unchanged limit from the adjustable point value. P19 supplies the contrasting jump. The hint does not silently put a into a side formula.

**P56 / H4.** The inverse coordinate relation, endpoint mapping and dt/dτ=1 are ordinary algebra and power-rule differentiation. They explain why translation changes the labels but not the rates. The domain-first evenness check directly invokes P28.

**P57 / H5.** The instructions point to exact denominator matching and the already available identity 1−cos(2x)=2sin²x. Extracting the squared sine ratio leaves precisely the different outside factors identified at Q5. No missing higher-order approximation is needed.

**P58 / H6.** The sine bound licenses a bound on function height. Forming the quotient before reusing it exposes cancellation of x, so the old shrinking bound cannot be applied to claim a derivative. P23 supplies explicit disagreeing approaches. The hint advances the requested distinction with existing content.

### P59–P72: complete solutions read last

**P59.** The comparison instructions focus on warrants, domains, held-fixed variables and height versus slope. They ask for the distinctions established in the teaching rather than an unprovided reference answer rule.

**P60 / S1.** Equality to x for allowed nearby inputs gives limit −1; the original zero denominator supplies no R(−1). Defining an extension at −1 is expressly a new function definition, with the unique continuity-compatible value already explained in P20. The two conclusions and their different justifications remain separate.

**P61–P62 / S2.** The chain-rule calculation has the required negative inner derivative −2s and positive L denominator. The sign and length/length units match Q2's held-fixed h. Multiplying a small altitude change by −s/L is the derivative approximation under the stated domain/locality conditions. The explanation distinguishes this variation from P12's different experiment.

**P63 / S3.** Linear limits give 2 on each side; the value is a, so P16 gives exactly a=2. Other values are removable defects, whereas P18's 0 and 1 side limits cannot meet a single value. The reference to P49 is a later interpretive connection and was not required for the original continuity question.

**P64–P65 / S4.** Substitution and expansion give Y(τ)=400−16(τ−5)²=160τ−16τ² on [0,10]. Differentiation yields 160−32τ in the interior, zero at 5 with height 400; τ=0 gives height zero. Substituting t=τ−5 into the old velocity yields the same derivative because the translation factor is one. The claimed unchanged motion is therefore equality of heights and rates at corresponding events, not an unsupported physical assumption.

**P66–P67 / S4 continuation.** Direct expansion gives the two endpoint quotients 160−16δ and −160−16δ with the correct allowed signs of δ. Their one-sided limits are 160 and −160. A two-sided extension remains a distinct convention rather than being selected to interpret the absent source dots. The nonsymmetric domain prevents evenness about the new origin; for an extended polynomial, direct substitution also gives Y(−τ)=−160τ−16τ², generally different. Substitution of 5±r gives identical height 400−16r² for |r|≤5, showing the different symmetry center without contradicting the domain-based conclusion.

**P68–P69 / S5.** Exact rewritings on x≠0 give the first limit 3 and the two cosine-numerator limits 0 and 2. The finite product-limit rule applies to the extracted constants, x and squared sine ratio. The explanation correctly locates the difference in the remaining factor x, and it never cancels or evaluates an undefined quotient at zero.

**P70 / S6 definitions.** The solution keeps the nearby-output limit separate from a point value, adds equality for continuity, and uses the difference-quotient limit for differentiability. Its implication is the proved direction; the corner example supplies the failed converse. For the actual real domains under discussion these are the same meanings introduced earlier.

**P71–P72 / S6 application.** The unit-circle bound yields |w(x)|≤|x|, so squeeze and the defined w(0)=0 establish continuity. The exact nonzero-input quotient is sin(1/x). Along the two P23 input sequences it is 1 and −1, so the universal nearby-limit requirement fails even from the right. Thus no derivative exists at zero. “Slopes” here are explicitly the difference-quotient slopes; the solution does not substitute a claim about the continuity of a derivative function. The decisive factor x disappears only after forming the derivative quotient, which explains why the height result does not settle differentiability.

## Issues, uncertainties and dependency status

**Established teaching defects:** none found in the substantive routes evaluated. This is a bounded finding from this reading, not a guarantee that no latent error exists and not evidence about any human learner's retention or mastery.

**Limited scope concern, P03/P15/P70:** the verbal finite-limit definition does not separately state that the domain has distinct inputs arbitrarily near the approached point; P15 says that the domain contains inputs on both sides. If these statements were intended for arbitrary domains including an isolated point, sufficiently small neighborhoods could contain no permitted nonzero-distance inputs, making an unqualified “all such inputs” condition vacuous. The natural question is whether “approach” is intended to restrict discussion to points that really can be approached within the domain, and, for P15, from each side. Ordinary reading may already carry that restriction, so I do not classify this as an established defect. Every worked function and question has the required near inputs, and the theorem explicitly uses an interior point. No presented conclusion is blocked. A claim about limits on completely arbitrary domains remains outside what this verbal treatment settles unambiguously.

**Explicit unresolved course/source convention, P32/P67:** the absent source derivative dots could represent one-sided endpoint derivatives or derivatives of a polynomial extension. The document retains both interpretations and does not assert a source choice. The interior motion, named one-sided endpoint limits and Q4 conclusion remain justified independently. The natural unresolved question is what convention the source intended, not what the supplied restricted function permits.

**Source-fidelity uncertainty, P01/P18/P19/P20/P27/P30/P32/P35/P51:** assertions about original lecture pictures, sign misprints, page locations and completeness were read as author statements. Only this document's PNG was directly inspected. The supplied formulas and geometric reconstructions are enough for the mathematical route; verifying that they accurately represent every original source page would require an additional authorized source input. I did not convert these unverified provenance claims into a teaching defect or silently browse the PDF.

**Input limits:** no missing or unreadable portion of either permitted subject-content input remains. The baseline line-ending normalization and corrected ranges are recorded above. They do not leave subject admission provisional because the equality and boundary checks establish complete text delivery. The teaching text and its PNG were available in their prescribed order. No external source, missing numerical datum, or absent table is needed to reach the document's own mathematical conclusions.

**Dependency status:** all six question demands have a preceding supported route; hints and solutions were checked at their later positions and were not used to retroactively justify an earlier demand. The trigonometric proof depends on the supplied unit-circle geometry, radian sector area, parity/double-angle identities and the introduced squeeze principle. The final theorem depends on the introduced finite product-limit rule. Neither route requires an extensive untaught theorem or a borrowed scientific premise. No failed connection was silently repaired in reaching these conclusions.
