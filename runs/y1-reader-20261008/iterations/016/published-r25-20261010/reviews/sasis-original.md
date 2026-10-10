# Original SASIS reading report — D016, frozen r25

This is the original report for the bundle frozen at 2026-10-10T14:11:51.625789Z. It was written after the complete reading and before any author feedback. No subject feedback was received.

## Finding

I found no established defect that blocks a requested construction, calculation or explanation in P1–P6. The geometric comparison, passage from sums to area, signed-area distinction, accumulation/average calculations and simple-interest contributions have available routes from this baseline and the teaching supplied before their use. There is one minor literal overstatement about units (E1) and one nonblocking ambiguity about the scope of the general borrowing formulas (P1 below). Neither invalidates the worked case or supplied exercise solutions.

This is an evaluation of the document against the supplied operational knowledge, not a grade, a claim about a human learner's retention, or a claim that every latent error has been discovered. Declared geometric and existence theorems were checked for intelligible meaning and application, not required to be derived from the baseline.

## Input access and locators

Only the two authorized subject-content inputs were read: the entire four-subject baseline and the complete teaching bundle (teaching, its three images, hints, solutions). All seven supplied SHA256 values matched on initial verification and were rechecked unchanged when this report was written. The baseline size is 247,840 bytes. There were no missing files, unreadable passages, truncated retrieval results or unreadable required figure labels.

Locators below use **logical lines**, obtained by `Path.read_text().splitlines()` after Python's universal-newline decoding. The baseline has 1,377 raw LF bytes and 2,561 raw CR bytes, yielding 2,561 logical lines. The first retrieval heading incorrectly called its range “physical”; the actual indexing was logical throughout, and the convention was explicitly corrected during reading. Teaching, hints and solutions have no CR bytes: their logical and LF-delimited line numbers coincide, at 216, 31 and 121 lines respectively.

- **B** = `inputs/prof/references/sasis/ocr-baseline-20261007/student-baseline.txt`.
- **T** = `output/teaching.md`.
- **H** = `output/hints.md`.
- **S** = `output/solutions.md`.
- **F1–F3** = the images embedded at T25, T43 and T120 respectively.

The complete baseline was read in these consecutive ranges: B1–240, 241–460, 461–660, 661–790, 791–910, 911–1040, 1041–1180, 1181–1320, 1321–1480, 1481–1660, 1661–1840, 1841–2050, 2051–2260, 2261–2440, 2441–2561. This includes Mathematics (B17–662), Further Mathematics Pure Core and the selected Statistics and Mechanics (B668–823), Physics (B828–1385), and Chemistry including its reference notices (B1391–2561).

The document reading order was T1–25 → visual inspection of F1 → T26–43 → F2 → T44–120 → F3 → T121–216 → H1–31 → S1–121. Hints and solutions were evaluated after the teaching; they were not used retroactively to supply premises missing at an earlier prompt.

Retrieval was instruction-confined, not technically isolated. I did not browse, open source URLs, search for or read other files or skills, obtain subject information from other agents, or use outside subject references. The access record supplies the exact paths, hashes and ranges.

## Chronological reconstruction witnesses

### Opening and section 1: one rectangle to a sum (T1–31; F1)

**T1–7, scope and assumed knowledge.** The announced antiderivative, summation, elementary-limit, signed-area and fundamental-theorem background is actually present: B132–152 supplies sequence limits and summation; B256–336 supplies derivatives and antiderivatives/definite evaluation; B336 also supplies rectangle-sum limits in the well-behaved cases; B386 supplies signed versus geometric area. The page is entitled to build on this knowledge. T5's separation of prompts, hints and solutions identifies the reading/help arrangement. The MIT attribution is provenance, not an additional premise used in this reading.

**T11–23, rectangle and scaling.** B48 gives rectangle area, and B40 and B136 give interval/integer/index meaning. For b>0 and positive integer n, the width b/n is positive. Piece i ends at ib/n, so its height for x² is (ib/n)². Multiplication gives i²b³/n³; summing i=1,…,n gives the displayed R_n. Thus the cube is accounted for by two height factors and one width factor, not by an unexplained change from area to volume. The spatial variable x, counting index i and fixed endpoint b are distinguished.

**F1 at T25 and caption T27.** The left panel has four width-1/2 rectangles ending at 1/2, 1, 3/2 and 2, with heights 1/4, 1, 9/4 and 4 on the drawn x² curve. This instantiates b=2,n=4. The right panel locates c_i horizontally between x_(i−1) and x_i, projects to f(c_i), and marks the whole interval width Δx. Its schematic curve does not require a missing formula. The sample labels are intelligible as coordinates/function values from B104 and the drawing; their general definitions are supplied later at T91–105, without requiring a calculation from them here.

**T29 and P1 at T31.** For 0≤u≤v, v²−u²=(v−u)(v+u)≥0; hence each left endpoint is a minimum and each right endpoint a maximum on its piece. Multiplying by positive widths preserves the inequalities and adding gives bounds. This also directly matches B434's endpoint-rectangle rule. P1 requires substituting four endpoints into the already constructed products: the right products sum to 15/4 and the left products to 7/4. The area is therefore in [7/4,15/4]. The request for a monotonicity explanation and the distinction from an arbitrary sample are available before any hint or solution.

### Section 2: the solid comparison and geometric limit (T33–87; F2)

**T35–41, stack and supplied law.** Each slab is a prism of thickness 1 and square area k², so B48 gives volume k²; summing the slabs gives S_n. T41 expressly introduces the square-pyramid volume rule base area × perpendicular height /3 as a geometric fact. It is not silently imported from the baseline's prism formula. The objects and dimension of each quantity are clear.

**F2 at T43 and caption T45.** The top view shows aligned concentric square slabs. The central section shows a four-step stack, an inner triangle reaching z=4 with base width 4, and an outer triangle reaching z=5 with base width 5. The caption explicitly states common centre/orientation and that the drawing is a section, not a volume. Thus merely comparing two planar triangles is not substituted for three-dimensional containment.

**T47–59, containment to inequalities.** In slab j, j≤z≤j+1. By similar sections, the inner side is n(1−z/n)=n−z and the outer side is (n+1)(1−z/(n+1))=n+1−z (B36/B48 similarity). The inequalities follow respectively from z≥j and z≤j+1. Since the squares share centre and orientation, side-length containment gives pointwise horizontal-section containment; taking all heights gives solid containment. The outer solid continues above the stack. With T41's law, the comparison volumes are n³/3 and (n+1)³/3. Dividing by n³ is legitimate because n>0. Boundary faces shared by adjacent slabs do not add thickness or alter the volume comparison.

**T61–69, limit.** The displayed lower bound is 1/3 and the upper is (1+1/n)³/3. Their difference from each other shrinks to zero; T61 supplies and explains the squeeze principle needed to transfer the limit to S_n/n³. T19–20 already gives R_n=b³S_n/n³, with b fixed, so its limit is b³/3. The finite sum is not equated with its leading limit expression. The exact formula mentioned at T69 is available independently at B723 (FM23), but the reconstruction above does not need it to repair the geometric argument.

**T71–85, sum limit to actual area.** L_n has the same successive square heights as R_n except that it includes the initial zero and omits the final b². Cancelling the common heights yields R_n−L_n=(b/n)b²=b³/n. Together with the already justified area bounds and R_n→b³/3, this makes the lower bound have the same limit and squeezes the area to b³/3. For b=2 this is 8/3, lying inside P1's finite bounds. T85 handles b=0 separately, preserving the positive-width assumptions used earlier.

**P2 at T87.** Changing each slab thickness from 1 to 2 doubles every vertical coordinate. It leaves square bases unchanged, so it takes the existing inner pyramid to base side n/height 2n and the outer to base side n+1/height 2(n+1). Applying the same map to all points preserves containment (also consistent with the transformation operations at B699). Their volumes divided by n³ bound V_n/n³ between 2/3 and (2/3)(1+1/n)³, giving limit 2/3. The prompt demands a transfer of the displayed construction, not invention of a new volume theorem. This route was available at its position.

### Section 3: general samples, existence and signs (T89–124; F3)

**T91–105, notation and construction.** The positive width (b−a)/n, boundaries x_i=a+iΔx and sample membership c_i∈[x_(i−1),x_i] identify each factor and its interval. f(c_i)Δx is one signed contribution, and the expanded sum shows exactly what the sigma adds (B136). Substituting the right boundary, left boundary or midpoint gives the three named sampling choices. The width is tied to the interval, not to the sample's distance from one boundary. F1's right panel is now explicitly connected to this notation.

**T107–116, definition and existence condition.** The integral is introduced conditionally as a common finite limit, independent of sample choices; a successful limit for just one chosen sampling rule is not presented as sufficient. The explanation of dx distinguishes the limiting operation from multiplying a height by literal zero. Continuity is defined using approach within the domain, including the one-sided endpoint reading. The identity x²−c²=(x−c)(x+c) makes the polynomial continuity example accessible, and for 2x−3 the difference is 2(x−c). The continuous-function existence result is explicitly a theorem being used, not an alleged proof from those two examples. B336 already permits rectangle-sum integration in well-behaved cases. The text does not claim that discontinuity always prevents integration.

**T118, F3 at T120 and T122.** Positive Δx preserves the sign of f(c_i); therefore below-axis contributions subtract. B100 gives |f| as the nonnegative magnitude and B386 explicitly supplies splitting/negating below-axis integrals for geometric area. In F3 the x triangle has base/height 2, giving area 2 by B48. For x−1 the two base-1/height-1 triangles have magnitude 1/2 each: the signed sum is zero while the geometric total is 1. The sign labels are attached to contributions, and T122 explicitly rules out reading cancellation as disappearance of the regions.

**P3 at T124.** The general construction gives Δx=2/n, x_i=1+2i/n and g(x_i)=−1+4i/n. Using the sum-of-integers formula expressly permitted in the prompt gives R_n=(2/n)[−n+(4/n)n(n+1)/2]=2+4/n, tending to 2. Continuity of this precise polynomial was established at T116. The root 3/2 divides the graph into triangles of area 1/4 below and 9/4 above: the geometric total is 5/2, whereas the integral is −1/4+9/4=2. Algebra, straight-line geometry and the sign rule suffice before the later linear worked example.

### Section 4: linear example, accumulation and average (T126–156)

**T128–136.** One right rectangle for x has height ib/n and width b/n. Their sum uses Σi=n(n+1)/2, available at B140/B723, to give b²(1+1/n)/2. Its limit b²/2 agrees with the independent triangle formula. The example keeps its b>0 domain and does not identify a finite endpoint sum with the exact area.

**T138–146.** The integration variable x is bound inside the sum/integral; b determines the endpoint of the resulting function. For fixed a, B336 gives A(b)=F(b)−F(a). The derivative rules at B272/B292 then give A′(b)=F′(b)=f(b), with the lower-end value constant. The two earlier expressions differentiate to b² and b respectively. Evaluating at b=a gives zero, so no undetermined additive constant remains in this definite accumulation. This is a reconstruction using the supplied fundamental theorem, not an unsupported converse from the two examples.

**T148–154.** Defining average as integral/(b−a) is also explicitly available at B737 (FM30). Multiplying it by the interval length recovers the signed total, explaining the constant-rectangle interpretation. On [0,2], (8/3)/2=4/3. The units multiplication/division rule agrees with B36 and B899. The first blanket sentence about units is broader than this rule warrants; see E1.

**P4 at T156.** The available antiderivative x²+x gives A(b)=b²+b−2 on b≥1. This gives A(1)=0 and derivative 2b+1. The [1,3] total is 10, and dividing by the actual width 2 gives average height 5, which yields the same positive area 10. The requested explanation of x versus b directly reuses T144. None of these demands needs additional teaching from the solution file.

### Section 5: borrowing and the final debt (T158–204)

**T160–172, model and principal.** Rate × short duration has units (dollars/year)×years=dollars, consistent with B899's graph-area units. No starting debt, no repayments, no fees and nonnegative borrowing are declared. T162 introduces simple interest on original principal, P(1+rτ), as the model; no compound-interest rule is assumed. T164 explicitly makes times numerical values in years and r the numerical annual fraction while retaining the unit interpretation of rates and widths. Consequently Δt=1/12 at a constant rate of 12,000 gives 1,000 dollars. T166 distinguishes an exact constant-rate monthly principal from a rectangle approximation for a changing rate. Taking the appropriate common sum limit gives B(T)=∫f(t)dt. The regularity scope of this general statement is the nonblocking concern P1 below.

**T174–187, the consequential debt connection.** The same short-interval principal is assigned borrowing time t_i and final time T, so its outstanding duration is T−t_i. Substituting that duration into the newly supplied model gives f(t_i)Δt[1+r(T−t_i)]. The text calls this approximate, appropriately allowing both rate variation and the different times within a finite interval. Adding contributions is licensed by the declared separate simple-interest treatment with no intervening repayments or changing rate. Taking the limit gives the weighted integral for D(T). Distribution of the bracket and linearity of integration (B360) separate principal B(T) and interest. The multiplier is dimensionless and both totals are dollars. Earlier borrowing gets a greater multiplier for the positive rates used in the examples.

**T189–198, worked case and timing check.** Integrating 12,000 gives 12,000 dollars. Integrating 1+0.06(1−t) on [0,1] gives 1+0.06(1−1/2)=1.03, so debt is 12,360 and interest 360 dollars. The alternative multiplier 1.06 would assign the entire principal the maximum duration of one year. Uniform principal contributions have mean duration ∫₀¹(1−t)dt=1/2 year, reproducing the 0.03 interest factor. This connection follows from the already supplied average and contribution model, without an imported finance convention.

**T200–202, jumps and exercise conventions.** The extension is given as an existence theorem, with boundedness and jump meanings explained. The instruction to split into continuous pieces makes the intended class continuous between finitely many jumps. For the actual P5 function, the pieces are constant and the only jump is at 1/2. The expressly stated invariance under changing an isolated point value explains why the endpoint assignment there does not change an integral. Multiplication by the continuous time-left factor leaves polynomial pieces and that same finite jump, so the debt integral is covered too. T202 expressly applies the numerical-year, simple-interest, no-fees/no-repayments conventions to both P5 and P6.

**P5 at T204.** The active width is 1/2 year, so principal is 24,000/2=12,000 dollars. Interest requires the still-varying duration 1−t, yielding 0.06·24,000∫₀^(1/2)(1−t)dt=1,440(1/2−1/8)=540. Debt is therefore 12,540, exceeding the uniform worked case by 180. Equal principal over the first half-year has mean outstanding duration 3/4 year, explaining the difference from the uniform full-year mean of 1/2. Both the computation and the reason are supported at the prompt's position.

### Section 6 and end matter (T206–216)

**P6 at T208 and guidance T210.** This is explicitly a later retrieval exercise after the model/conventions have been supplied; closing the teaching does not make its requested prior recall an untaught premise. Its numerical-year convention makes the polynomial 6000(1+t) interpretable. Principal is ∫₀²6000(1+t)dt=24,000 dollars and average rate is that total divided by two years, 12,000 dollars/year. The contribution at t has duration 2−t, so the debt multiplier is 1+0.10(2−t). Expanding the interest product gives (1+t)(2−t)=2+t−t² and interest 600[2t+t²/2−t³/3]₀²=2,000 dollars; debt is 26,000. Multiplying all principal by 1.20 would instead give 28,800 and falsely assign two full years to amounts borrowed later. The prompt demands transfer of the existing contribution construction, elementary polynomial integration and the previously explained units, not a new interest law. T210's hint/solution fallback is consistent with this demand; the stated lack of a fixed delay does not create an additional subject premise.

**T212–216, source and conventions.** The internal pyramid law and drawings justify the terminology used, and the unit-product rule justifies dollars for the borrowing integral. The particular claims about what the original MIT source calls its solids or units cannot be independently checked from this bundle: the original PDF is referenced but not supplied as a content input. They are not needed to reconstruct any mathematical conclusion here. The navigation links identify the help files actually included and read.

### Hints in their supplied order (H1–31)

- **H1–9, P1:** matching-number navigation is clear. The width instruction and replacing final endpoint 2 by initial endpoint 0 correctly changes the set of sampled heights while preserving common terms and width.
- **H11–13, P2:** a vertical stretch by 2 carries the prior containment to the changed solid. The inner height 2n and one further thickness 2 for the outer give 2(n+1), so the hint directs the consequential geometric choice.
- **H15–17, P3:** 1+2i/n respects the nonzero interval origin; substitution gives −1+4i/n. Keeping width 2/n outside the sum preserves the contribution. Solving the zero before drawing the two triangles applies the already taught sign split.
- **H19–21, P4:** x²+x differentiates to 2x+1; its lower-end subtraction is constant in b. Dividing by width rather than endpoint follows the average definition.
- **H23–25, P5:** only the first-half interval has nonzero rate. Keeping 1−t distinguishes borrowing amount from interest. The midpoint of that active interval is t=1/4, leaving 3/4 year until the endpoint.
- **H27–31, P6:** the principal product, duration 2−t, separate interest multiplier and two-year averaging denominator all reuse earlier definitions. Expanding the supplied polynomial product is ordinary algebra. No hint changes the model or supplies a previously absent theorem needed to make its prompt possible.

### Solutions in their supplied order (S1–121)

- **S1–24, P1:** the displayed four products sum to 15/4 and 7/4. The explanation at S24 explicitly multiplies endpoint height inequalities by positive width and adds; it justifies the reported interval rather than merely naming the right answers.
- **S26–41, P2:** volume doubles with slab thickness; stretching all three solids preserves point containment. The specified bases/heights produce bounds 2n³/3 and 2(n+1)³/3. Positive division and the stated squeeze yield 2/3; the finite/limiting distinction is retained.
- **S43–56, P3:** substitution, Σ1=n and the permitted Σi formula give 2+4/n. Continuity licenses identification of its limit with the integral. The antiderivative check 0−(−2)=2 is independent of the rectangle arithmetic. Evaluation brackets are intelligible from this explicit upper-minus-lower substitution and the prior fundamental theorem. The two triangle dimensions produce −1/4+9/4 versus 1/4+9/4, explaining 2 versus 5/2.
- **S58–68, P4:** upper-minus-lower evaluation gives b²+b−2; substitution at 1 and differentiation give 0 and 2b+1. The total 10, width 2 and average 5 agree, and the explanation directly addresses the endpoint/width distinction asked in the prompt.
- **S70–88, P5:** the zero-rate half contributes zero. The integral of 1−t over the active half is 3/8; multiplying by 1,440 gives 540 interest. Adding principal gives 12,540 and comparison with 12,360 gives 180. The stated 3/4-year mean follows by dividing 3/8 by active width 1/2, so the timing explanation is supported.
- **S90–121, P6:** principal evaluates to 24,000; averaging over two years yields 12,000 dollars/year. The debt integral retains both rate and time-left multiplier. The expansion 2+t−t² integrates over [0,2] to 10/3; multiplying by 600 gives 2,000 interest and 26,000 debt. The proposed all-principal multiplier gives 28,800, and 2,000/24,000=1/12<0.20 supports the stated timing comparison. All units match the supplied convention, and the final links introduce no further content.

## Established defect and provisional concern

### E1 — Minor literal overstatement about units (T154)

The sentence “An integral and an average have different units” is unconditional. The rule immediately following it is the supported statement: integral units are [f][x], and average units are [f]. If x is dimensionless, these units coincide. The baseline admits numerical mathematical variables (B40/B104), and the examples x and x² do not assign a physical unit to x. The natural question is therefore whether the assertion is intended only for integration over a dimensioned variable.

This is a local precision issue, not a blocked inference: the next sentence supplies the correct general relation, and all borrowing calculations use years as the interval unit and correctly distinguish dollars from dollars/year. It has no downstream effect on the supplied numerical results. Qualifying the blanket sentence by the dimensioned-variable condition would remove the overstatement.

### P1 — Provisional scope ambiguity for arbitrary borrowing rates (T160–187)

T107 makes a common finite limit a condition for the integral, and T116 gives a sufficient continuity condition. Section 5 initially declares f nonnegative, then writes the general B(T) and D(T) formulas without locally stating that the relevant sums/integrals exist. Nonnegativity alone has not been supplied as an existence theorem.

There are two readings. Carrying forward section 3's existence condition makes these formulas conditional on the appropriate common limits, which is a valid reading. Treating section 5's nonnegativity/no-repayment assumptions as the complete class for an unconditional general existence claim is not justified by the supplied premises. The natural question is “Which borrowing-rate functions are admitted by these general formulas?”

The scope of an arbitrary unspecified rate remains conditional, but no actual exercise is blocked: the worked rate is constant, P5 is expressly covered by the finite-jump extension at T200, and P6 and its weighted debt integrand are polynomials. A local integrability/continuity-or-piecewise-continuity qualification would settle the ambiguity. I do not treat the lack of that restatement as proof that the author intended the invalid broader reading.

## Input limits and remaining status

- No content-access failure affects the reading: both full inputs and all three figures were available and read in order.
- The referenced original MIT lecture PDF and external OCR URLs were not opened. Historical/source-fidelity claims at T214, including its exact page wording, remain unverified; they do not supply a missing premise in the reconstruction above.
- No unresolved course convention affects the constructions or exercise results. The document explicitly chooses simple interest, years for numerical time, positive interval widths, and signed versus geometric totals.
- No requested exercise depends on granting an unsupported repair. The only conditional generalization is the unspecified-rate scope described in P1. Declared theorem truth/source fidelity can be considered separately by a technical reviewer; this report does not import an external proof or corroboration.
