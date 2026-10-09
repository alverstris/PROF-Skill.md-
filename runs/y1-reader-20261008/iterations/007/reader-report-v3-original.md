# SASIS original document-reading report

Condition: D007-r13-v3-SASIS  
Frozen revision: 2c0a49dff10d407296675a9d52a2d664be1bb0f0  
Reader role: evaluate the teaching document against the complete supplied operational baseline.  
Status: original report, preserved before author feedback.

## Finding

The complete teaching has a supported route through its stated mathematical aims for the supplied baseline. I found no established consequential mathematical error, missing prerequisite connection, or unresolved interpretation that blocks a required conclusion. This finding rests on the reconstruction witnesses below, including the tasks at their first positions and the later hints and solutions; it is not inferred merely from the presence of correct final answers.

The baseline already supplies single-variable differentiation, implicit differentiation, principal inverse trigonometric branches, hyperbolic definitions and derivatives, and the relevant algebra. The document reconstructs their consequential connections without needing an additional lecture or an outside formula sheet. Its given foundational limits and positive-base exponential representation are intelligible premises, not unexplained demands to invent a new theorem.

This evaluates what the document makes available under the declared baseline competence assumption. It does not evaluate an individual's ability, measure learning or retention, or claim discovery of every latent error. Source attribution and completeness relative to the linked MIT original were not independently verified.

## Actual input access

Only the following two subject-content objects were retrieved, using read-only git show at the specified commit. Both identities were checked before reading their content.

| Input | Bytes | Raw UTF-8 characters | SHA256 |
|---|---:|---:|---|
| references/sasis/ocr-baseline-20261007/student-baseline.txt | 247840 | 246945 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 |
| runs/y1-reader-20261008/iterations/007/revised-v3/teaching-v3.md | 31051 | 30961 | 6dc2823d9f931c1baaa6eb4ce5076ed2aef1859ba29255d5503eed627824ae54 |

Git stdout was decoded with bytes.decode('utf8'). Universal-newline file reading was not used. The baseline contains 1184 CRCRLF sequences, preserved in the decoded character indexing; the teaching contains none.

The baseline was actually delivered and read in sixteen sequential, contiguous, half-open raw-character ranges: [0,16000), [16000,32000), [32000,48000), [48000,64000), [64000,80000), [80000,96000), [96000,112000), [112000,128000), [128000,144000), [144000,160000), [160000,176000), [176000,192000), [192000,208000), [208000,224000), [224000,240000), and [240000,246945). This included the Mathematics section, all FM01–FM71, all Physics sections, and all Chemistry sections through CH-REF and the final text.

Only after that complete baseline read, the teaching was delivered and read sequentially in [0,11000), [11000,22000), and [22000,30961). Adjoining outputs completed the few sentences or links cut by a mechanical range boundary. All P001–P165, task prompts, grouped hints, complete solutions, and final links were read.

Every content-delivery call exited successfully. Each call had one large content output and a sufficient output budget. No output was marked or observed truncated, and no recovery read was necessary. The companion reader-access-v3-original.json records each range, tool chunk identifier, exit status and truncation assessment. Hash-only inspection and the later structural check are recorded separately and are not counted as content delivery.

A final structural check of the same immutable teaching object confirmed exactly P001–P165 in order, 32 unique anchors, and 53 internal fragment links with no missing targets. It did not fetch any link or add subject content.

No working-tree input, other repository file, history, source PDF, linked resource, prior report, research, state or other agent's findings was inspected. No browsing or agent messaging occurred. The restrictions were instructions on retrieval, not technical runtime isolation. This report makes no claim of erased pretraining, unavailable memory controls, or simultaneous retention of every input byte.

## Baseline locators used in the witnesses

These locators refer to the actual complete packet read above.

- **M-language:** Mathematics, “Prior arithmetic, geometry and mathematical language” and “Proof and mathematical work”: ordinary algebra, roots, variable domains, logical implication, and the requirement that division use a nonzero denominator. These occur in the first baseline content range.
- **M-functions:** Mathematics, “Algebra, functions and coordinate geometry”: exponent manipulation on positive bases, functions and one-to-one inverses, composition, circle equations, and the perpendicular radius–tangent relationship. These occur in [0,16000).
- **M-trig:** Mathematics, “Trigonometry”: radians, quadrant signs, principal arcsine/arccosine/arctangent intervals, reciprocal definitions, sine/cosine addition identities and squared identities. This section straddles [0,16000) and [16000,32000).
- **M-exp:** Mathematics, “Exponentials and logarithms”: exponential positivity, inverse relations, natural-log power rule and log domains. Located in [16000,32000).
- **M-diff:** Mathematics, “Differentiation and its applications”: the difference-quotient limit, the two trigonometric limits, derivative rules, product/quotient/chain rules, inverse-rate relation under its conditions, implicit differentiation, tangent equations and derivative-sign monotonicity. Located in [16000,32000).
- **FM-induction:** Further Mathematics FM01, [48000,64000), permits finite-product reasoning to be organised inductively if needed.
- **FM-hyperbolic:** Further Mathematics FM24–FM25, [48000,64000), supplies the exponential definitions, identity and derivatives of sinh/cosh.
- **FM-inverses:** Further Mathematics FM29, [64000,80000), supplies the principal inverse trigonometric derivatives with their conditions and the use of implicit inverse relationships to derive them.

The Physics and Chemistry sections were also read completely. They supply no additional scientific premise required by this document, which is mathematical throughout. Reading all four subjects did not require importing material from the references listed within them.

## Chronological reconstruction witnesses

The order below follows the document. Later help is assessed at its later position and is not used to repair an earlier task's prerequisites.

### P001–P005: route, aim and notation

The route makes Q1–Q6 optional pauses and Q7 a later review opportunity, with named help after the core. It does not demand that the reader first classify a personal difficulty. The mathematical aim is choosing and justifying rules from function construction.

P005 fixes real variables, radians, natural logarithms, the differentiation variable, nonnegative square roots and inverse-versus-reciprocal notation. Thus an expression such as arcsin x cannot reasonably be read as 1/sin x within this document, and the prime in y' has a declared referent. M-language, M-trig and M-diff supply the familiar operations named in P004. The assertion that the route covers a particular MIT lecture is a provenance claim rather than a premise of the mathematics; its independent verification is outside the two inputs.

### P006–P014: hyperbolic definitions, derivatives and representation

P007–P009 introduce sinh and cosh by complete exponential formulas and explicitly group each numerator. Applying M-diff to e^(-x) gives -e^(-x). Consequently differentiating the difference defining sinh turns its second minus into a plus, yielding cosh; differentiating the sum defining cosh yields sinh. This reconstructs P010 and explains the contrast with the cosine derivative. Substitution x=0 gives the stated function values and slopes in P011. FM24–FM25 independently make these operations available in the baseline.

For P012–P014, subtracting (a-b)^2 from (a+b)^2 gives 4ab. With a=e^x and b=e^(-x), ab=1, proving cosh²x-sinh²x=1. Declaring u=cosh x and v=sinh x then gives u²-v²=1. Positivity of both exponentials gives u>0; the identity gives u²=1+v²≥1, hence u≥1. The right-branch assertion therefore follows without presuming a diagram. The equation's name “hyperbola” is introduced in the text; the consequential coordinate relation is proved. The comparison with the circle uses the supplied trigonometric identity and carefully distinguishes the parameter from the two coordinates. No transfer of trigonometric signs to all hyperbolic identities is licensed.

### P015–P017: Q1 at its first position

Both requested routes are already available: substitute input 2x into the defining fractions, or combine P010 with the baseline chain rule. The required inner factor is the derivative of 2x. Exponential positivity and M-diff's derivative-sign rule support the monotonicity demand. Nothing in the prompt requires its later hint or solution as a new premise.

### P018–P028: construction order, general rules and quotient reconstruction

P019–P022 specify differentiable u,v, constant c and the nonzero quotient denominator. In the composition formula f'(u(x)) means the derivative of the outer function evaluated at its inner input, followed by multiplication by u'. The sin(3x) example makes that evaluation and factor explicit.

P023 distinguishes multiplication in x sin x from composition in sin(x²). For the latter, the inner derivative is 2x, giving 2x cos(x²). For [sin x]² the outer derivative is twice its input and the inner derivative is cos x, giving 2 sin x cos x. Thus the two displayed derivatives support, rather than merely label, the construction distinction.

On v≠0, P024–P026 rewrite u/v as uv^(-1). Product differentiation yields u'v^(-1)+u(-v^(-2)v'); combining denominators gives (u'v-uv')/v². The subtraction order and the denominator condition are consequences of those steps. The worked R has denominator 1+x²>0. Its numerator after differentiation is 1+x²-2x²=1-x². The sign conclusions for |x|<1 and |x|>1 follow from that numerator, and R'(0)=1. At |x|=1 the displayed formula itself supplies zero; the prose makes no inconsistent claim there. All operations are supported by M-functions and M-diff.

### P029–P031: Q2 at its first position

The two expressions have respectively multiplication and division as their last operations. The denominators never vanish, and sine is defined on the real line. The chain derivative of sin(3x) was just exemplified. Thus choosing rules, stating real domains and tracing the factor 3 are supported before the help is encountered. The reciprocal-product alternative is also already justified by P024–P026.

### P032–P038: implicit differentiation and its limitations

P033 does not equate an entire implicit curve with one global function: it conditions the calculation on a local differentiable y(x). The chain rule then explains 3y²y' versus 3x².

For P034–P036, differentiating 3xy² gives 3y²+6xyy'; collecting terms yields (3y²+6xy)y'=-3y². Division produces the stated formula only where that coefficient is nonzero. At (0,2), the original relation is satisfied, and the coefficient is 12. The resulting slope -1 gives y-2=-x by the baseline tangent equation.

This is a baseline implicit-differentiation operation, not an unexplained demand for a general implicit-function theorem. A further available local check is to rewrite the same relation for y>0 as x=8/(3y²)-y/3. Its derivative with respect to y is -16/(3y³)-1/3<0, so it is one-to-one there; at y=2 its derivative is -1. The supplied inverse-function and inverse-rate rules therefore agree with the stated local slope.

P038 preserves the undivided relation when division fails. It does not infer “no tangent” or automatically infer “vertical tangent” from a zero denominator. The stated alternatives are appropriate limitations on this calculation. No dependent step uses a value at an excluded denominator.

### P039–P041: Q3 at its first position

The circle relation, both points and local differentiability at those points are specified. M-diff and the preceding example permit differentiation to 2x+2yy'=0 and division when y≠0. Using both coordinates, rather than only x, is required by this relation. Identifying failed division means combining y=0 with the original equation, an available algebraic step. The question asks what the failure alone establishes, which P038 has already delimited; it does not require an untaught singularity classification.

### P042–P050: principal inverse functions and branch-dependent signs

P043 fixes both the arcsine input domain and output branch. Differentiating sin y=x yields cos y·y'=1. In the branch interior, cos y is positive by M-trig. Substituting sin y=x into cos²y=1-sin²y gives cos y=+√(1-x²), not a freely chosen sign. Division yields the stated derivative for -1<x<1. P047 separates the function's endpoint values from the finite-derivative formula's domain.

For arctangent, the specified branch permits tan y=x. The chain rule gives sec²y·y'=1 and the identity replaces sec²y by 1+x². This denominator is strictly positive for all real x. Both inverse procedures are also explicitly available in FM29; no new theorem about inverse differentiability has to be invented. The branch information changes the consequential square-root sign, and it is supplied before that sign is used.

### P051–P053: Q4 at its first position

The new prompt specifies the arccosine branch [0,π]. Implicit differentiation is already taught and the cosine derivative is already baseline knowledge. In the stated interior, y lies in (0,π), where sin y>0. Thus the negative factor from differentiating cosine and the positive square root are separately justified. FM29 also supplies this inverse derivative. The prompt's finite-domain and sign-comparison demands are supported here, independently of the later solution.

### P054–P062: review dependencies and sine from the derivative definition

P055 distinguishes reconstructing formulas from proving all foundational limits. P056–P059 actually state the two limits and the derivative definition. The baseline also explicitly contains them, so neither a topic label nor an absent reference sheet is being substituted for a premise.

With x fixed, substituting sin(x+h)=sin x cos h+cos x sin h into the difference quotient and collecting the sin x terms gives the displayed two terms in P061. Their limits are sin x·0 and cos x·1, yielding cos x. P060 identifies h as a nonzero varying increment, including the alternate Δx notation. P062 correctly distinguishes the exact limiting argument from a finite small-angle approximation. The conclusion and its real/radian conditions follow from supplied premises.

### P063–P065: Q5 at its first position

The prompt supplies the cosine addition identity and both necessary limits again. Grouping the terms in the difference quotient is ordinary distributive algebra, and identifying x-dependent factors as constant in h was just taught. The demand to reconstruct without using the known cosine derivative is therefore feasible within its specified premises. The prompt's derivation is not circular even though the cosine derivative is independently part of the baseline.

### P066–P074: tangent, secant, exponential and logarithm

For tangent, quotient differentiation gives [cos²x-(-sin²x)]/cos²x. The unit-circle identity makes this 1/cos²x=sec²x. For secant, the reciprocal chain rule gives -(cos x)^(-2)(-sin x), which equals sin x/cos²x=tan x sec x. P070 carries cos x≠0 for both. The numerator signs and final factorisation are justified, rather than left as a remembered outcome.

P071 supplies lim_(h→0)(e^h-1)/h=1 as a premise. The exponent law factors the exponential difference quotient as e^x times that ratio, yielding e^x for fixed x. P073 expressly does not claim an existence proof of e. The earlier use of the exponential derivative was already licensed by M-diff and did not wait for this later explanation.

For ln x, x>0 gives e^y=x with y=ln x. Chain differentiation yields e^y y'=1, so replacing e^y by x gives 1/x. M-exp supplies the inverse relation and positivity; M-diff supplies the rules. There is no omitted sign or domain choice.

### P075–P077: integer and rational powers

For a positive integer exponent, differentiating a product of n copies of x produces n equal terms x^(n-1); finite product-rule reasoning, or FM01 induction, supplies the connection. P075 states x≠0 for the separate x^0 convention and for reciprocals of positive powers. The zero function case is not used to justify an undefined reciprocal.

For rational p/q with q>0 and x>0, y=x^(p/q)>0 makes y^q=x^p. Differentiating the integer powers gives qy^(q-1)y'=px^(p-1). Division is permissible because q>0 and y>0. Substitution yields the exponent p-1-p(q-1)/q=p/q-1 and factor p/q. P077 expressly leaves negative-input and zero-input extensions to separate domain checks. The positive-domain argument does not silently grant those extensions. Baseline power and implicit differentiation rules also make the operation available; this is a reconstruction within that competence assumption.

### P078–P084: fixed real exponent and logarithmic differentiation

P079 states the representation x^r=e^(r ln x) on x>0 and describes each operation. It is compatible with M-exp's log-power and inverse rules: ln(x^r)=r ln x, then exponentiating recovers the representation. The constant r has a declared role.

The direct chain derivative is e^(r ln x)·r/x, which becomes rx^(r-1). In the logarithmic route, differentiating ln f=r ln x gives f'/f=r/x; multiplication by the positive f recovers the same answer. P084 explicitly prevents confusing f'/f with f', and the x^π example is an immediate fixed-real-constant instance. The warning about variable exponents follows from differentiating a product involving a varying exponent; no unsupported general variable-power formula is required.

### P085–P087: Q6 at its first position

The positive domain and constant √2 are specified. The preceding representation permits x^(√2)=e^(√2 ln x). M-exp equally permits (√2)^x=e^(x ln√2). Differentiating the two inner expressions requires respectively √2/x and ln√2; the question's comparison of fixed and varying quantities is therefore already supported. It does not need the later hint to introduce a new method.

### P088–P094: exponential of a product

P089 resolves the potentially consequential grouping of e^(x arctan x) and translates inverse notation. The last construction step is the exponential, so E'=e^w w' for w=x arctan x. The product rule gives w'=arctan x+x/(1+x²), using the already established arctangent derivative. Resubstitution yields P093.

Arctangent and its derivative are defined for every real x, 1+x²>0, and the exponential is differentiable everywhere. Thus the rule combination applies on the claimed whole real domain. At zero, E=1 and the bracket is zero, giving the stated horizontal tangent. P094 limits the motivational word “anything” to existing functions and derivatives; it does not use the phrase as a mathematical premise.

### P095–P098: Q7 at its first position

Part (a) retrieves P043–P047, including the branch sign and finite-derivative interval. Part (b) adds division by 1+x² to the expression just worked. Product, chain and quotient rules, the exponent derivative and denominator positivity have all appeared before the task. Permitting a justified unsimplified answer removes any extra demand for a particular algebraic form.

The suggestion to revisit after a delay is presented as adjustable, not as a universal optimum or a claim about anyone's retention. Closing the core initially is an optional practice instruction, not missing subject-content provision; help is supplied in the packet.

### P099–P100: provenance boundary

This paragraph states the source, page mapping and which tasks were generated. Those are readable claims but cannot be independently certified using the two authorised objects. No later mathematical step depends on confirming the external PDF. The paragraph correctly makes no inference from an “Exam 1 Review” label to a current syllabus. The URL was not followed.

### P101–P123: grouped hints, at their actual later position

P101–P102 clearly distinguish hints from the full-solution group and supply navigation.

- **P103–P105, Q1:** common-denominator subtraction points to the definition; the displayed composite hyperbolic derivative rules are direct chain-rule instances of P010. Comparing with H and using exponential positivity supplies a usable next step without a new premise.
- **P106–P108, Q2:** A=x²+1 and B=sin(3x) preserve the distinction between AB and B/A. Obtaining A',B' separately prevents swapping numerator and denominator. Their derivatives are already taught.
- **P109–P111, Q3:** 2x+2yy'=0 is the correct undivided equation. The divisor 2y and original circle equation together locate where it vanishes. The hint does not equate failed division with absence of a tangent.
- **P112–P114, Q4:** -sin y and y' arise from the chain rule. The branch interior (0,π) supplies the positive sine when replacing its square by 1-x².
- **P115–P117, Q5:** collecting the cos x terms in the cosine difference quotient exposes exactly the two given limit ratios. Constancy is with respect to h, as already specified.
- **P118–P120, Q6:** the two exponential rewritings keep √2 and ln√2 fixed while x and ln x vary. They are valid for the task's positive domain.
- **P121–P123, Q7:** the inverse differentiated relation and branch cue match part (a). Naming N=e^w and D=1+x², then computing w',N',D' and assembling (N'D-ND')/D², preserves the actual order of operations in part (b).

These hints are usable at their stated positions. They do not supply a prerequisite missing from the corresponding earlier prompt.

### P124–P165: complete solutions, at their actual later position

P124–P125 identify the solution group and offer a return to intermediate hints.

**P126–P130, Q1.** Subtracting the defining numerators leaves 2e^(-2x), hence H=e^(-2x). Its derivative is -2e^(-2x). The direct derivative 2sinh(2x)-2cosh(2x)=-2H is the same expression. Since e^(-2x)>0, the derivative is strictly negative for every real x, supporting decreasing behaviour. The solution answers both methods, agreement, the inner factor and monotonicity.

**P131–P136, Q2.** With A'=2x and B'=3cos(3x), product differentiation gives 2x sin(3x)+3(x²+1)cos(3x). For B/A, the numerator is B'A-BA', giving exactly P134. The squared positive denominator and sine's full domain justify both real domains. P135 identifies precisely where the inner factor 3 enters; it is not incorrectly applied to the term where only A is differentiated.

**P137–P140, Q3.** The quotient -x/y gives -1/2 and +1/2 at the two full points, explaining why the common x-coordinate is insufficient. With y=0, the original equation gives x=±√5. A finite y' there would make the undivided differentiated equation require 2x=0, impossible at those points. The further assertion of vertical tangents uses the baseline circle rule: each radius is horizontal and the tangent perpendicular. Thus the solution distinguishes what division failure alone says from what the additional equation and geometry establish.

**P141–P145, Q4.** Differentiating cos y=x gives -sin y·y'=1. On the branch interior, sin y>0 and sin²y=1-x², hence y'=-1/√(1-x²). The open finite-derivative interval and defined function endpoints are distinguished. The sign comparison with arcsine separates the derivative of the original trigonometric function from the sign selected by the branch.

**P146–P150, Q5.** Substitution and grouping yield cos x·(cos h-1)/h - sin x·sin h/h. Holding x fixed and taking the two given limits yields -sin x. This uses the addition identity and limits, not the cosine derivative as a premise. The source of the minus sign and the radian condition are explained.

**P151–P157, Q6.** For f, the derivative of √2 ln x is √2/x; multiplication by e^(√2 ln x) gives √2 x^(√2-1). For g, the derivative of x ln√2 is the constant ln√2; the result is (√2)^x ln√2. The stated extension of the second formula to all real x follows because its fixed base is positive and its exponential representation has no log of x. The solution does not extend the first formula beyond the requested positive domain.

**P158–P165, Q7.** Part (a) repeats the legitimate arcsine derivation with its sign and open domain. For (b), w'=arctan x+x/(1+x²), N'=e^w w' and D'=2x feed the quotient rule. Multiplying w' by 1+x² and subtracting 2x leaves (1+x²)arctan x+x-2x=(1+x²)arctan x-x. This verifies the simplified numerator in P163. Denominator positivity gives validity for every real x; substitution zero gives zero. The alternative reciprocal-product route follows P024–P026. The feedback about differentiating only the numerator correctly identifies the lost denominator contribution without diagnosing any particular person.

## Coverage, ambiguity and dependencies

Every labelled passage P001–P165 is covered above, including headings, route instructions, all formulas, the coordinate representation, each task at its initial position, each hint, each solution and the final return links. There are no separately supplied images or assets whose meaning had to be inferred. The geometric representations are given in equations and words sufficient for the stated conclusions.

Consequential alternative readings are actively resolved: inverse functions versus reciprocals; sine of a square versus square of sine; product versus composition; an exponential's whole exponent; parameter versus coordinate; and a selected inverse branch versus an unsigned square. Variable domains, radians, derivative variable and positive-root convention are explicit. I found no unresolved course convention that changes a required answer.

No later passage was needed to retroactively license an earlier use. In particular, the cosine derivative before Q5 and exponential derivative before P071 were already in the baseline; Q5 and P071 reconstruct those known rules rather than first making them available. The same applies to hyperbolic and inverse trigonometric derivatives already granted by Further Mathematics. The report has not withheld that supplied prior knowledge merely because the document teaches it again.

## Established defects, provisional concerns and limits

**Established consequential defects:** none found in the mathematical instruction, task support, hints, solutions or internal navigation.

**Provisional mathematical concerns:** none requiring a blocked or conditional downstream conclusion beyond the explicit domain and differentiability conditions already stated. This does not certify absence of every possible error.

**Input limits:** neither authorised input was missing, truncated or unreadable. Full access was established, so no mathematical finding is left unverified because of incomplete input delivery.

**Verification boundaries:** the external MIT source, its stated page mapping, the historical provenance of tasks and the breadth of coverage relative to that source were not independently checked. The Markdown source was read as complete text; no rendered-browser behaviour or external-link availability was tested. The internal anchor check supports the written navigation, not a claim about any particular renderer. These boundaries are separate from a demonstrated teaching defect.

The supported outcome is that this frozen document makes its mathematical meanings, rule choices, derivations and task conclusions available from the supplied baseline and its own stated premises. It is an evaluation of the document's accessible reasoning, not an assessment score or a claim about human learning.
