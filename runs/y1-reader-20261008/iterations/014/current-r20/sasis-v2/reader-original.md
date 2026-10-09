# SASIS frozen-document reader report

## Inputs and scope

I read the complete operational four-subject baseline before the teaching document. Locators below are physical LF line numbers: **B** for the baseline and **T** for the teaching. Retrieval used `read_bytes().decode().split('\n')`, preserving internal CR characters. The companion `access-log.md` records packets and the repaired initial output truncation.

- Baseline: `/workspace/scratch/6a5c7131498d/prof-r20/references/sasis/ocr-baseline-20261007/student-baseline.txt`; 247840 bytes; SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`; all B1–B1378 read. Includes Mathematics H240, Further Mathematics H245 Pure Core Y540/Y541 and Statistics Y542/Mechanics Y543, Physics H556, and Chemistry H432.
- Teaching: `/workspace/scratch/6a5c7131498d/prof-r20/runs/y1-reader-20261008/iterations/014/current-r20/author/teaching-v2.md`; 24606 bytes; SHA256 `caf74a9a150f61d2531e8b2768abb1448fb7d5304818a9e1fcc73d02bead826b`; all T1–T414 read sequentially, including route, L1–L8, P1–P7, source note, H1–H7, S1–S7, and ending. One text constituent; no figures or companions were supplied or assumed.

This is a review of the document's accessible meanings and justified connections, not a test of a student's performance. The only subject-content inputs accessed were those two files. Access confinement was instruction-based, not technical isolation. No links or source documents were opened. The theorem expressly introduced in the teaching was evaluated as a supplied premise with conditions, not required to be derived from the baseline.

## Finding

The reviewed route supplies usable connections from the stated baseline to differential notation, antiderivative families, reversed-chain factors, and interval restrictions. I found no established instructional defect that blocks the stated examples or tasks. This finding is confined to the passages and reconstruction evidence below; it is not a universal absence-of-errors claim, an external source-fidelity verdict, or evidence about human learning or retention.

The important dependencies are explicit: tangent changes use a new exact definition distinct from finite changes; completeness of the antiderivative family uses the newly stated mean value theorem; substitution uses the already available chain rule; logarithmic examples use positivity and denominator restrictions before antidifferentiation. None of the numbered tasks needs a later hint or solution to supply an otherwise absent subject premise.

## Chronological reconstruction witnesses

### Route and L1: differential versus actual change (T1–T45)

The reading route identifies lesson order and matches each practice item to its help (T5). The assumed derivative, algebra and integration operations are actually supplied in B28, B138–B209, rather than only named in the baseline.

At T11–T23, the base input `a`, increment `h`, and new input `a+h` are distinct. The actual output change is obtained by subtraction. B138–B142 defines the limiting difference quotient, and B166 gives the tangent through the base. Thus the tangent predicts `f(a)+f'(a)h`, while the actual value is `f(a+h)`. The displayed approximation is not asserted as an exact equation or as a guaranteed error bound. Its small-step interpretation is available from the limiting slope and the warning at T23. Evaluation requires the changed input to be in the function's domain, already inherent in `f(a+h)` and baseline domain rules (B30, B62).

T25–T33 supplies the differential convention as a definition: `dx=h`, `dy=f'(a)dx`. It does not presuppose an infinitesimal theory. Given the tangent equation, its output change is exactly this product. The derivative has output/input units, so the product has output units (B28, B473, B533). Negative input or output changes are compatible with signed arithmetic. For nonzero `dx`, division gives the derivative; at zero the defined change remains zero while the quotient is disallowed (B32). This explains both the compact base notation `x` and the distinction between `dy/dx` and a finite-change quotient.

For the square example, B146 supplies derivative `2x`; expansion gives `(2+h)^2-4=4h+h^2`. The tangent change retains `4h`; the omitted-to-retained magnitude ratio is `h^2/|4h|=|h|/4` for nonzero h (T35–T41). The numerical values and discrepancy follow directly, without an imported approximation theorem.

P1 at T45 is accessible at its location: changing the base to 3 gives derivative 6 and actual change `6h+h^2`, so its sign comparison and explanation require only the just-taught distinction. It introduces neither an error tolerance nor a new recovery rule.

### L2 and P2: the cube-root representations (T47–T81)

B46 and B146 justify the power derivative at positive input 64: `f'(64)=(1/3)64^(-2/3)=1/48`. T49–T61 separately identify whole value, estimated change and base. Consequently input steps 1 and 0.1 multiply the same base slope; one does not mistake `1/48` for the cube root itself.

The exact factorisation at T63–T67 follows from positive-base power laws. B93–B97 explicitly supplies the binomial expansion, its `|u|<1` interval and small-parameter truncation. With `u=h/64` and exponent 1/3, its linear term multiplied by 4 is `4+h/48` (T69–T77). For the displayed steps the relative parameter is small and within the stated baseline interval. The text identifies the exact factorisation and approximate truncation separately, and correctly avoids treating agreement of equivalent methods as independent accuracy evidence.

P2's step `63.7-64` and relative parameter `(63.7-64)/64` are available by this same construction. Its required agreement and location of approximation follow before any help is read. The task does not require an unprovided true cube-root value or guaranteed numerical accuracy.

### L3–L4: change versus recovery, notation and standard forms (T83–T128)

T85 distinguishes two questions: a local tangent prediction and an exact derivative identity on an interval. This connects the prior section to the baseline's antiderivative definition (B178), without making integration an inversion of a finite approximation.

T89–T101 assigns roles to `F`, `f`, the integral sign, integration variable, and additive `C`. `C` is fixed while x varies. The equivalent differential statement uses the definition already introduced, and the sine example follows from `(-cos x)'=sin x` (B152–B156). The instruction to verify by differentiation is actionable.

Every displayed standard form at T103–T119 has a supplied route: power and logarithm rules in B182–B195; tangent derivative in B154; arcsine and arctangent derivatives in B413. Domains are specified: avoid zero for `1/x`, cosine zeros for secant squared, and endpoints ±1 for the inverse-sine integrand. B107 supplies the principal inverse meanings, so inverse-function notation is not confused with reciprocals. The explanation of `dx` in the numerator identifies the implicit factor 1. The generic power rule is limited to intervals on which its terms are defined and differentiable, including exclusion of n=-1.

T121–T128 verifies the logarithmic rule rather than merely labelling it correct. For negative x, B60 gives `|x|=-x`; B130 and B149 require a positive logarithm input; B162–B164 supplies the chain factor -1, cancelling the negative denominator. The conclusion `1/x` therefore holds on each allowed branch and establishes nothing at zero.

### L5 and P3: why the family is complete (T130–T168)

Constant differentiation and derivative subtraction are already supplied (B156). T132 correctly distinguishes preservation of a derivative from proving that all primitives have this form. T134–T140 introduces continuity and a mean value theorem, with closed-interval continuity, open-interval differentiability, ordered endpoints and an intermediate point. Its link is supplementary: the operational statement is present in the file.

For T142, differentiability at a point gives a finite limiting difference quotient (B138–B142); multiplying that quotient by its increment makes the output difference tend to zero. This supplies the needed continuity connection. Between two eligible points in the interval, the theorem gives `H(b)-H(a)=H'(c)(b-a)=0` when the derivative vanishes throughout. Hence all pairs of values agree. T144–T150 then uses `(G-F)'=0` and the preceding result to establish `G=F+C`. The interval restriction prevents carrying this inference across an undefined point.

At T152–T164, the chain rule gives derivatives of both half-square trigonometric expressions equal to `sin x cos x`. B111 gives their difference `1/2`. Thus `A+C_A=B+C_B` requires `C_B=C_A+1/2`. This shows both equality of families and unequal labels for the same particular member. A supplied function value fixing C is already supported by B178.

P3's piecewise constants and excluded zero (T168) preserve the valid local result on each half-line. An interval joining a negative and positive point includes zero, so the theorem cannot be applied there. This connection is available before H3 or S3. No general topology theory is needed for the concrete hole in this domain.

### L6: substitution as a reversed chain rule (T170–T203)

B158–B164 and B197 already provide the chain and substitution operations. T172–T179 makes their exact role visible: if `A'=q`, differentiating `A(g(x))` yields `q(g(x))g'(x)`. Thus the entire `g'(x)dx` factor corresponds to `du`; replacing the inner expression alone is insufficient. The construction and reverse derivative check specify both directions.

For T181–T203, `u=x^4+2` has derivative `4x^3`, giving `x^3dx=du/4` by division by the nonzero constant 4. This does not divide by x or require x to be nonzero. The power antiderivative adds an independent factor 1/6, producing 1/24. The displayed derivative check cancels both factors. The polynomial is defined on the real line, and this reverse-chain route does not require `x^4+2` to be one-to-one globally. No untaught global change-of-variable theorem is needed.

### L7 and P4: constant versus variable mismatch (T205–T233)

T207's rule follows from derivative linearity: a constant multiplier scales the entire derivative by that constant (B156), so it repairs a constant ratio. A varying discrepancy is not removed that way.

For T209–T215, the derivative of `(1+x^2)^(1/2)` is `(1/2)(1+x^2)^(-1/2)2x`. The inner expression is positive for real x, so the displayed real-line domain is available. The equivalent substitution contributes 1/2, and integration of `u^(-1/2)` contributes 2. T217–T228 similarly retains inner derivatives 6 and -2x. These justify the multipliers 1/6 and -1/2 with their signs. T229 explicitly retains the outside x and relates the two trigonometric choices to the earlier family comparison; `u=cos x` brings a minus sign while `u=sin x` does not.

P4 (T233) changes the inner polynomial to `x^3+2`. Its derivative `3x^2` supplies a constant factor 1/3, and the initial value then determines C. The separate proposed exponential can be rejected by its derivative using the already shown -2x factor. No elementary/non-elementary classification of the other integral is required or granted.

### L8, P5–P7 and the ending of the lesson (T235–T276)

T243 establishes the real integrand domain before the substitution: B130 requires x>0 for ln x, and B32 excludes `ln x=0`, equivalent to x=1. B130's monotonicity/inverse facts give the positive and negative inner-logarithm branches.

T245–T251 groups the expression as `(1/ln x)(dx/x)`, so `u=ln x` and `du=dx/x` replace all factors. The previously verified `∫du/u=ln|u|+C` applies on a nonzero-u interval. T254–T260 gives the order of operations and checks both branches. On `(0,1)`, the outer input is `-ln x>0`, and the chain factors `(-1/x)/(-ln x)` give the stated integrand; on `(1,infinity)` the direct chain check works. Independent constants across the hole at 1 follow from L5. Absolute value does not change the original inner logarithm's domain.

P5 at T264 replaces a reciprocal first power by a reciprocal square. The already available power rule with exponent -2 gives `-1/u`, valid for negative nonzero u as well as positive u. B130 gives `ln(e^-1)=-1`; the condition is therefore usable. The requested derivative and domain verification require no later premise.

P6 at T268 reuses the two established primitives, the unit-circle values at pi/2 (B101) and the displayed constant-offset relation. Its requirement to compare complete functions, rather than bare constants, follows from L5.

P7 at T272 recombines three established constructions: the ln derivative at base 1 with an input step 0.04; the chain factor 3 in a sine primitive and a value condition; and the exact same logarithmic domain distinction already taught. None requires numerical tables or outside lookup. T274 describes an adjustable use of the task and does not add a subject-matter premise. I do not treat its suggested timing as evidence of any learning outcome. The source-coverage and source-printing claims at T276 and earlier references cannot be independently checked under the two-input restriction; the mathematics does not depend on their fidelity.

### Hints in their supplied order (T278–T308)

H1 (T284) directs expansion into linear and quadratic terms, an available algebraic route. H2 (T288) retains the signed input step and base divisor, matching L2. H3 (T292) directs an endpoint/domain check that matches the mean value theorem's stated conditions. H4 (T296) retains the whole derivative factor and the separate initial-value step; its exponential reminder retains the inner derivative. H5 (T300) explicitly distinguishes exponent -2 from -1 and permits negative nonzero u, consistently with the power rule's real domain. H6 (T304) supplies unit-circle values already in B101 and the identity already used in L5. H7 (T308) points to the base data, constant chain factor and sequential domain tests. The hints offer focused paths through previously available content. They are not retroactively used here to justify a missing premise at a prior task.

### Complete solutions in their supplied order (T310–T414)

S1 (T316) checks the derivative-based change -0.6 against actual change -0.59 through the explicit omitted term 0.01. It correctly adds the former to 9 when forming a new-value estimate, preserves both negative signs, and distinguishes equality from approximation.

S2 (T322–T329) uses `dx=-0.3`, `dy=-0.3/48=-0.00625`, and a base value of 4. In the binomial line the parameter is `-0.3/64`; multiplying its linear contribution by 4 gives the identical estimate 3.99375. The equalities before truncation and approximations after it have the right roles.

S3 (T335) identifies the two constant branches and the failed closed-interval condition, preserving the zero-derivative conclusion within each branch. The term “connected interval” has its concrete meaning available from this explanation; no additional machinery is used.

S4 (T341–T363) combines factors 1/3 and 1/6 into 1/18, substitutes zero to obtain C=-32/9, then explicitly verifies both conditions. The polynomial domain is all real x. For the separate proposal the chain factor produces `x exp(-x^2)`, not `exp(-x^2)` on an interval. The observation about an isolated point follows from the definition of an antiderivative on an interval. The solution carefully limits the rejection to the proposed form rather than inferring nonexistence of other primitives.

S5 (T369–T387) integrates exponent -2, evaluates the condition at u=-1 to obtain C=-1, and differentiates the result with both minus signs retained. The answer is restricted to the requested `(0,1)` interval. The discussion of an extension to x>1 leaves its constant independent, rather than allowing the single initial value to fix it. Negative ln x is permissible as a nonzero denominator; no logarithm of a negative number is taken.

S6 (T393–T401) finds C_A=-1/2 and C_B=0, then uses the trigonometric identity to equate the complete expressions. Both derivatives and the required value are checked, and the constants satisfy the already established offset.

S7 (T407–T411) uses the tangent data `(f(1),f'(1))=(0,1)` to produce the approximate logarithm value 0.04. It uses the inverse chain factor 1/3 and initial value 2 for the exact trigonometric recovery. Its final branch-by-branch derivative and domain discussion retains x>0, excludes x=1, and assigns absolute value only to the outer input. The return link at T413 and final empty line T414 were read; there is no unseen ending used in the review.

## Defects, provisional concerns, alternatives and dependencies

**Established instructional defects:** none identified in the supplied teaching route from the complete baseline. The witnesses above support that bounded finding rather than inferring it from correct final answers alone.

**Provisional precision consideration:** the informal notation `Delta y ≈ f'(a)h` is a local linear approximation, not a specified relative-error criterion. In particular, the text does not license an accuracy guarantee at a selected finite step or a relative-error claim when the linear term vanishes. T23 expressly declines an arbitrary-step error guarantee, and all worked approximation bases have nonzero derivatives. I therefore do not identify this as a defect in the required inferences or tasks. A reader asking “how accurate is this particular estimate?” receives a bounded method, not an unprovided universal tolerance claim.

**Reasonable alternative routes retained:** polynomial expansion could replace substitution in L6/P4; either trigonometric inner function produces a valid primitive with a shifted additive constant; and branchwise logarithmic forms are equivalent to the absolute-value form on their respective intervals. These alternatives are supported by B90–B97, B190, B156–B164 and the explicit lesson connections. None needs to be silently selected as an outside convention.

**Dependencies checked:** without the new mean value theorem premise, completeness of the one-constant family would not follow merely from constant differentiation; the file does supply that premise and its application. Without positivity and nonzero-denominator restrictions, the nested logarithm would be ambiguous; these restrictions are established before use. Without keeping the outside derivative factor, the exponential and polynomial guesses could fail; both derivations and checks retain it. These are satisfied dependencies, not unresolved gaps.

**Input/access limits:** the initial baseline output was truncated by the outer tool-output budget; its entire requested range was reread in two smaller packets before continuing. There is no remaining unread baseline or teaching range. External source fidelity, source pagination, and claims about what an original lecture printed remain unverified because the original sources were not permitted inputs. External technical truth review is separate. No alternative revision or previous reader report was accessed, and this report concerns only the teaching hash recorded above.
