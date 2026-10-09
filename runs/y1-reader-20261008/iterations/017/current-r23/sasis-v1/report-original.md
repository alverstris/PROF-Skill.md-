# SASIS original whole-document report

Frozen revision: D017-original-r23-author-v1. This is a read-only evaluation of the exact local inputs identified in the assignment, not a learner examination or a claim of human learning. No author feedback was consulted. The assignment identifies commit ae08f92832c91a7a5652ca874ffe807afedf38a9; I checked the local bytes against the assigned hashes, not the remote commit.

## Input access and conclusion

I read the complete operating instruction, the complete 247,840-byte four-subject baseline, and every constituent of the frozen teaching bundle. I read baseline content lines 1–1377 in fourteen successive chunks, preserving internal carriage returns by decoding bytes and splitting only on LF. I read lesson lines 1–63, viewed sine.png, read 64–89, viewed additivity.png, then read 90–156 and 157–224. I subsequently read all hints (1–38) and all solutions (1–111). Both actual images were visually inspected, not inferred from their captions. All six subject-input hashes match the assignment. No tool response reported truncation; each text response was below its output budget. Precise ranges, offsets and hashes are in access-log.md.

Within the supplied baseline and the lesson's expressly introduced definitions and theorem statements, I found no established substantive defect blocking the intended conclusions or any of P1–P5. The signs, endpoint conventions, units, comparisons and substitutions can be reconstructed at their first required positions. This conclusion is about availability and warrant in the frozen teaching, not verification of external source fidelity or learning effectiveness. General statements of theorems are accepted as introduced results; no proof of every continuous function's antiderivative existence is silently added.

Locator convention: B = student-baseline.txt, L = lesson.md, H = hints.md, S = solutions.md. All locators below are the LF-only content-line numbers used during actual reading. The chronological witnesses first cover the lesson; the subsequently encountered help is covered separately and is not used retroactively to justify the earlier tasks.

## Chronological reconstruction witnesses

### Entry and U1: L1–42

L1–5 identifies the course convention, sequence and objective. “FTC 1” is subsequently explicitly defined, so no externally assumed numbering is needed. The self-contained subject path does not require opening the source URLs.

L10 distinguishes fixed-endpoint numerical accumulation from a function, defines integrand/variable/differential, and explains signed rectangles for forward intervals. B178 supplies the rectangle-limit and antiderivative interpretations; B203 supplies signed rather than universally geometric area. Multiplying heights by positive widths preserves height signs, and nonnegative heights recover ordinary area. Renaming x to t throughout leaves the sampled function values and interval unchanged; it introduces no new physical variable or numerical factor. B62 and B78 supply function and sum meanings.

L12–20 states the evaluation theorem with continuity and a primitive F, and declares it an established result. B138–156 and B178 already make derivative and antiderivative meanings available. L18 gives an intelligible working meaning of continuity and states the continuity of the particular function families used. This is adequate for applying the theorem here, without treating “no break” as a complete formal analysis definition. The warning about 1/x across zero is warranted by B183's domain restriction and B411's requirement of separate one-sided limits at an interior singularity; having primitives on two disconnected intervals is insufficient. L20 expressly disambiguates endpoint evaluation bars from modulus, which B60 would otherwise also make a reasonable reading of bars.

L22–35: differentiating x^3/3 gives x^2 by B146 and B156, so L15 yields (b^3-a^3)/3. The same operation on x^6/6 gives x^5, yielding 1/6 on [0,1]. In (F(b)+C)-(F(a)+C), distribution of the minus sign cancels C; hence the definite result is a number while the indefinite result is a family (B178). These are complete routine algebraic connections, not an inference from merely adjacent equations.

P1, L37–42, is available at its location: the supplied candidate primitive can be differentiated, both endpoints substituted, and the constant cancellation reused. It requires no later hint. Its arithmetic conclusion is (64-1)/6=21/2, and +7 cancels for exactly the reason already taught.

### U2: L44–76, including Figure 1 at L63

L47–61: B101 gives the sine/cosine values, signs and periodicity; B152–156 gives (-cos x)'=sin x. Substitution at 0 and pi yields 1-(-1)=2. Substitution at 0 and 2pi yields -1-(-1)=0. For the second hump, evaluation from pi to 2pi yields -1-1=-2. Since its heights are negative, its geometric area is 2 by B203 and L10. Geometric contributions therefore total 4 rather than 0. This does not depend on the later U3 additivity explanation: B203 already supplies splitting signed areas, and each displayed interval can also be evaluated independently.

I viewed sine.png before proceeding past L63. It actually shows a sine curve from 0 to 2pi, y extrema +1 and -1, x labelled in radians, blue shading above and orange shading below the axis, and signed labels +2 and -2. These features agree with B101 and the preceding endpoint evaluations. The area labels are not mistaken for heights: the ordinate ticks show heights separately, and adjacent caption L65 explicitly identifies the vertical coordinate as integrand value. The second hump's -2 means signed contribution, not negative geometric size. The caption's source-reconstruction claim is not independently verifiable within authorized inputs.

L67–74: B297 and B306–312 supply chosen-axis position, signed velocity and component differentiation; B203 and B594 supply velocity integral as displacement and speed integral as distance. Taking x as the primitive of v produces x(b)-x(a). Taking |v| instead counts both directions positively, so agreement when v is nonnegative follows from |v|=v (B60). A negative velocity yields a negative displacement but positive travel amount. A speedometer's magnitude cannot choose between +v and -v; the signed information is therefore necessary for displacement. No source wording is needed to establish this distinction.

L76: constant-velocity displacement is velocity times elapsed time (B299–312), so short nearly constant intervals contribute v(t_i) Delta t. B178 supplies the limiting rectangle interpretation and B543 supplies graph-area units. Refinement for continuous velocity gives the stated integral; replacing the sample values by their magnitudes yields distance. The example -3 times 2 gives -6 metres, while its speed 3 times 2 gives 6 metres. Forward time and the units are explicit. The motion interpretation is correctly not presented as a general theorem proof.

### U3: L78–122, including Figure 2 at L89

L81–87 introduces signed additivity. For a<b<c, the two subdivisions cover the full interval without extra width at their shared endpoint; thus adding their signed sums produces the full signed sum. L10/B178 make the passage to the stated integral relation intelligible. The claim applies to negative contributions by the same signed arithmetic, not by treating every shaded region as a positive area.

I viewed additivity.png before proceeding past L89. The actual figure labels f(x)=1+x^2 vertically and x horizontally; the curve passes through the displayed values 1 at a=0, 2 at b=1, and 5 at c=2. The blue region runs from 0 to 1, orange from 1 to 2, and they partition the whole region with the same upper curve. L91 states the exact function and endpoints. This warrants the illustrated positive case; the general signed relation comes from the text, not an overgeneralization from this one picture.

L93–106 defines reverse orientation and equal-endpoint zero, then checks agreement with primitive differences. Negating F(b)-F(a) gives F(a)-F(b). In the additivity expression the +F(b) and -F(b) cancel for any numerical ordering. For f=1 on endpoints 0,3,1, direct width/evaluation gives 3 and -2, hence 1, explaining removal of overcounted interval. The general continuous-function assertion is supplied as a theorem-level property; the displayed primitive proof reconstructs it wherever that primitive is available. No independent theorem proving existence of a primitive for every continuous function is established here or demanded of the learner.

L108–115: V(t)=t^2/2-t differentiates to t-1. At 0,1,2 its values are 0,-1/2,0. The sign of t-1, not of V, is negative on [0,1) and positive on (1,2]. Displacement is 0, while negating the first interval contribution and retaining the second gives 1 metre. The numerical-time convention avoids reading t-1 as an unqualified subtraction of a dimensionless number from a dimensional physical quantity.

P2, L117–122, can be handled before help: solve 2t-2=0, determine signs using B58/L115, and use primitive t^2-2t. Its values 0,-1,3 yield displacement 3 metres and distance 1+4=5 metres. L96 makes the reversed integral -3 metres; L67 and L106 preserve the distinction between reversing the mathematical orientation and describing a new physical trip. Odometer meaning is already given in L74.

### U4: L124–155

L127–133 starts with explicit continuous f<=g on forward [a,b]. The difference g-f has nonnegative sampled heights, so its rectangle sums and integral are nonnegative. B190 supplies integration over sums/differences, yielding integral(g)-integral(f)>=0 and the desired order. The condition a<b matters: reversing endpoints negates both values, reversing the inequality by B58; equal endpoints give zero. Nonnegative f and g individually are not needed because the argument uses their difference.

L135–141: B130 supplies exponential increase and e^0=1, while B147 supplies its primitive. Thus integral_0^1 1=1 <= e-1, and adding 1 gives e>=2. The improvement is supported rather than merely recalled: h=e^x-1-x has h'=e^x-1>=0 on x>=0, and h(0)=0. The derivative sign/monotonicity connection is available in B166; hence h>=0 and 1+x<=e^x. This is a short available calculus argument, not an untaught extensive theorem.

L143–148 integrates 1+x to 3/2 on [0,1], compares with e-1 and obtains e>=5/2. A larger certified lower bound is stronger, and the text avoids replacing inequality by equality. P3 at L150–155 gives the needed pointwise inequality on [0,2]; integrating gives 4<=e^2-1 and e^2>=5. Applying the already taught reversal produces -4>=1-e^2. Extending beyond [0,1] requires no unprovided inference: P3 supplies the premise and L141 also established it for x>=0.

### U5: L157–206

L160–166 defines u as an inner function and g as a function of the new input, under G'=g. B158–164 supplies the chain rule, so G(u(x)) differentiates to g(u(x))u'(x). It is consequently a primitive of that whole product. The du instruction packages the derivative factor, rather than replacing only the inner expression. The clarification of the source's f notation prevents interpreting integral f(x) alone as the claimed transformed object.

L168–176 supplies continuous differentiability of u and continuity of g over all intervening u values. Applying endpoint evaluation to the composite primitive gives G(u(x2))-G(u(x1)), exactly the endpoint evaluation of integral g in the u variable. Endpoint mapping therefore follows from substitution into the primitive, not from sorting endpoint magnitudes. This proof works when u decreases; no inverse-function operation or division by u' is used. As with U3, the displayed argument starts from the earlier G'=g setup; accepting the general continuous-g form as an introduced substitution theorem does not require an unstated learner proof of primitive existence.

L178–199: for u=x^3+2, du=3x^2 dx, giving x^2 dx=du/3. Old endpoints 1 and 2 map to 3 and 10. Power integration supplies another factor 1/5, so the primitive is u^5/15 and the result (10^5-3^5)/15. Differentiating (x^3+2)^5/15 recovers the complete original integrand using the chain rule. Restoring x before evaluating at 1,2 is a legitimate alternative; using those old endpoints on u^5/15 is not, because those numbers then refer to different input values. Expansion is available from B88–97 and termwise integration B190, so the alternative method is genuinely supplied.

P4, L201–206, is available before H/S: choose u=2-x^2, obtain x dx=-du/2 and map 0->2, 1->1. Orientation reversal turns -1/2 integral_2^1 u^4 du into +1/2 integral_1^2 u^4 du, giving 31/10. The integrand is nonnegative on [0,1], so the positive result is consistent. The zero derivative at x=0 causes no division problem: replacing the product x dx uses a constant factor, and the chain-rule proof did not assume an everywhere nonzero u'.

### U6 and source route: L208–224

L211 offers a later revisit without claiming it has occurred or measuring mastery. P5(a), L216, asks for the two rules and conditions already stated at L12/L168. P5(b), L218, combines supported sign analysis, motion and integration rather than introducing new physics. On the given interval 2t is nonnegative, while t^2-1 changes sign at the interior point t=1. With u=t^2-1 the full endpoints are -1,1 and the sign split maps to 0. The odd signed contributions give zero displacement; their magnitudes total 1 metre. Alternatively expansion gives primitive t^4/2-t^2 and values 0,-1/2,0, establishing the same result without requiring substitution. These connections are available before reading the hints or solutions.

L222–224 gives provenance and source-coverage claims. Those claims cannot be independently checked without the excluded source. This is a provenance input limit, not a barrier to the self-contained mathematics in this bundle.

### Complete help read after the lesson

H1–38 were all read. H8 repeats the already taught differentiate/evaluate/cancel procedure, including subtraction parentheses. H15 points to the velocity zero and side-sign checks, supplies the valid primitive, and preserves forward physical time versus oriented integration. H22 retains the inequality while integrating and delays isolation of e^2 until after that comparison; multiplying by -1 then explains reversal. H29 correctly prompts the negative factor and endpoint mapping separately. H36 preserves the P5 interior sign distinction and offers both the matched substitution and expansion. These hints do not introduce an otherwise missing premise needed by the initial task statements.

S1–17: S8 verifies the derivative and continuity conditions; S11–12's 63/6=21/2 and S15's cancellation of +7 match P1. S19–38: S22's sign intervals and primitive values yield early displacement -1 and later +4. S25/S31–36 therefore correctly distinguish displacement 3, distance/odometer 5, and reversed integral -3, all in metres. Taking only |3| would lose the backtracking because summing before taking modulus differs from summing magnitudes.

S40–59: S46–50 obtains 4<=e^2-1 and e^2>=5, and S53–57 negates both integrals to get -4>=1-e^2. The explanation correctly distinguishes changed integral orientation from unchanged pointwise function order.

S61–76: S64–71 accounts for the factor -1/2, new endpoints 2,1, their subsequent reversal, and power integration to 31/10. S74's direct primitive -(2-x^2)^5/10 differentiates to the original integrand; its endpoint values -1/10 and -32/10 confirm the result. The sign check is consistent with the original integrand; it is not used as a replacement for calculation.

S78–111: S81–88 restates the theorem conditions and complete substitution factor. S90 distinguishes an endpoint zero at 0 from the interior sign split at 1. S92–97 maps the full integral to integral_-1^1 u du=0; S100–106 maps each signed piece separately, obtaining 1/2+1/2=1 metre. S109's alternative primitive and its three values verify the same two contributions. “Returns to initial position” follows from zero displacement, while the positive distance establishes travel despite that return. All help-file links and anchors were read as supplied text; no external references were opened.

## Issues, uncertainties and limits

Established defects: none identified in the mathematical meanings, local inferential connections, task demands or complete help under this operational baseline.

Formal scope: the bundle states FTC and integral/substitution properties as teaching results. Its primitive-based demonstrations support the applications and make the connections accessible; they are not a construction of a primitive for every continuous function. I did not turn that absent full analysis proof into an extra learner requirement or claim to have established it from pretraining. No included exercise depends on finding an unknown general continuous-function primitive: every required primitive is available by supplied power, trigonometric, exponential or chain rules.

Input limits: I did not verify source authorship, printed-page coverage, source example numbering, fidelity to the source figures, or independent references, because only the exact local baseline and bundle were authorized. All subject files themselves were present, fully read, and hash-matched. There was no identified unreadable constituent, omitted section, truncated response or unresolved course convention affecting a task. Inspection covered the actual two PNGs and Markdown content; it was not a test of a separate rendered publication or future interface.

The findings do not certify human retention, actual learner success, empirical teaching effectiveness, or discovery of every latent error. No invented assessment battery, learner grading or document edits were performed. The instruction whitelist confined retrieval; it is not a claim of erased pretraining or technical isolation.
