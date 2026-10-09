# SASIS original fresh-reader report — frozen teaching v1

## Object, inputs and limits

This evaluates the supplied teaching document, not any student's performance. The role used two subject-content inputs only: the complete operational four-subject baseline (B) and the complete frozen teaching document (T). Physical LF line locators below come from `read_bytes().decode().split('\n')`, retaining internal CR characters and the terminal empty element. The baseline was read completely before the teaching was read in intended order. No source links were opened and no other subject files, revisions, reports, directory contents, skills or research were consulted. This is an instruction-confined evaluation, not technical isolation from pretraining or proof that pretraining has been erased. The substantive warrants below identify supplied premises rather than using external knowledge to fill a gap.

- B: `/workspace/scratch/6a5c7131498d/prof-r20/references/sasis/ocr-baseline-20261007/student-baseline.txt`; 247840 bytes; SHA-256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`; 1377 content lines plus terminal empty line 1378.
- T: `/workspace/scratch/6a5c7131498d/prof-r20/runs/y1-reader-20261008/iterations/014/current-r20/author/teaching-v1.md`; 23136 bytes; SHA-256 `60f908bb588e6dea64725b321f6eb753a33f8293bd452105f9fd48cefe68adbb`; 349 content lines plus terminal empty line 350.
- Both measured byte counts and hashes match the task's frozen-input declarations. All packets displayed their requested ranges without a reported truncation or missing line. No retrieval repair was needed. The access log records the actual ranges and ordering.

## Finding

No supported mathematical or prerequisite-connection defect was found in this frozen revision under the supplied baseline. The document explicitly distinguishes exact differentials from approximate finite changes, introduces the mean value theorem with its conditions before using it to justify the constant family, tracks reverse-chain factors, and retains the disconnected real domains of the logarithmic examples. Its prompts, later hints and complete solutions remain supported at their actual positions. This finding is limited to this reading and supplied-premise analysis; it is not a claim of universal error absence, human comprehension, mastery, retention or learning effectiveness.

The document makes several claims about an external lecture and a supplemental source. Their fidelity cannot be independently verified from the two allowed inputs. That is a separate verification limit, not a missing mathematical premise: the mathematics needed for the lesson is printed in T or available in B. The source-fidelity limits are listed after the chronological witnesses.

## Usable baseline connections established by the complete reading

The entire baseline was read, rather than replacing it with these selected warrants. These locators identify the premises actually consequential to this particular lesson.

- B28–42 supplies arithmetic, units, rearrangement, interval/set notation, equality versus identity, domain and division restrictions, implication, deductive explanation and the distinction between examples and unrestricted proofs.
- B46–68 supplies powers and roots, expansion, modulus, functions and inverses, coordinate gradients and lines. B88–97 gives binomial expansion, including rational exponents, the small-parameter restriction and finite-truncation interpretation.
- B101–126 supplies sine/cosine values, identities and inverse-function versus reciprocal notation. B130–142 supplies real logarithm/exponential domains, log identities and the derivative as a limiting difference quotient and tangent gradient.
- B144–174 supplies power, exponential, logarithmic and trigonometric derivatives, constants and linearity, the chain rule and the tangent equation. B178–209 supplies antiderivative notation, additive constants, initial conditions, standard integrals, reverse-chain patterns and substitution with full differential replacement.
- B349–427 adds the selected Further Mathematics premises actually relevant here: B409 supplies elementary Maclaurin expansions with their stated limitations, and B413 explicitly supplies real inverse-trigonometric derivatives and domain checking. T does not require a university theorem to be silently inferred from those topic names.
- B473, B533–545 and B806–820 reinforce units and graph/rate conventions. The remaining Physics and Chemistry premises were read but are not needed to infer the calculus conclusions. In particular no physical or chemical model law is imported into T.
- B339–341, B497–501, B784 and B1361–1367 distinguish provided operations from additional university formalism and distinguish assumed course competence from measured personal mastery. These limits do not prohibit an explicit new theorem in T or legitimate deductions from the permitted premises.

## Chronological reconstruction witnesses

These are concise evidence summaries, not a transcript of private deliberation. Each entry states what can be reconstructed at that point, its warrant, and any consequential interpretation or limit. Routine algebra is grouped only when it introduces no new premise. The sequence includes the existing practice, help, solutions and final ending as teaching; it does not invent a new assessment or treat SASIS as a student attempting problems.

### Opening and L1

1. **T1–3: purpose and route.** The announced distinction between differentials and antiderivatives is an aim, not an assumed theorem. B138–209 supports the declared prerequisites of elementary derivatives, algebra and integration. L1–L8, numbered prompts and matching H/S labels give a usable linear route; P7 is explicitly designated a later return. Nothing in the opening requires an unavailable result.

2. **T5–11: base input and actual changes.** With a specified differentiable function, base `a` and input move `a+h`, subtracting old from new yields `Δx=h` and `Δy=f(a+h)-f(a)`. B30, B62 and B138–142 supply function/domain and difference-quotient meanings. Admissible nearby inputs are implicit in evaluating the displayed function, not an assertion that an arbitrary function is defined everywhere.

3. **T13–19: derivative to linear estimate.** B140–142 defines the derivative as the limit of the nonzero difference quotient. Thus, as a nearby quotient approaches `f'(a)`, multiplying by the input step supplies the local additive linear estimate. T19 explicitly withholds an error guarantee for an arbitrary selected step. This does not require an untaught remainder theorem or claim uniformly small relative error when the derivative vanishes.

4. **T21–27: differential definition and tangent representation.** T24 explicitly defines `dx=h` and `dy=f'(a)dx`; no infinitesimal ontology is needed. B166's tangent equation gives the exact tangent-line output `f(a)+dy`. T separates that equality from `Δy≈dy`, permits signed changes, and obtains output units from output-per-input times input. B28 and B533 support the unit calculation. The new notation is explained before substantive reliance on it.

5. **T29: compact base notation and quotients.** Replacing the base label `a` by `x` explains the compact expression. Dividing the defined equality by nonzero `dx` gives exactly `dy/dx=f'(a)`, distinct from the finite-change quotient. T expressly blocks division at `dx=0`; B32 warrants that restriction. This is a legitimate defined-differential reading, not an unexplained cancellation of two zeros.

6. **T31–37: square example and discrepancy.** From B146, the base derivative is 4. Multiplication and evaluation give differential 0.4, tangent output 4.4, actual output 4.41 and actual change 0.41. Expanding `(2+h)^2` yields `4h+h²`; the omitted-to-retained magnitude ratio for nonzero `h` is `|h|/4`. This ratio is confined to the example and does not silently become a general error bound. Arithmetic and the exact/approximate distinction are consistent.

7. **T39: P1 at its teaching position.** The prompt changes the base and the sign of the step while retaining the just-explained square model. Its requests—differential, new tangent value, actual change and reason for discrepancy—are supported by T7–37 and B arithmetic. The success description identifies meaningful distinctions, including signs; it does not require later hints or solutions as hidden premises. A direct square evaluation and an expansion are both accessible routes.

### L2 and the transition to integration

8. **T41–47: cube-root base and derivative.** B46, B146 and T's specified positive base give `64^(1/3)=4`, `f'(x)=x^(-2/3)/3` near 64 and `f'(64)=1/48`. The negative exponent and reciprocal are available operations, with no zero-domain difficulty in this example.

9. **T49–55: estimate in two representations.** The move 64 to 65 is step 1, so T16 and the computed slope give `4+1/48≈4.02083`. T55 translates the same operation into `dx,dy`, and explicitly distinguishes change from whole output. Changing the step to 0.1 gives `4+1/480≈4.002083`. Both numerical approximations are consistent roundings of the printed rational values.

10. **T57–69: binomial representation and scaling.** Exact factorisation gives `4(1+h/64)^(1/3)`. B95–97 supplies the rational-exponent first-order binomial truncation; with exponent 1/3 it yields `4+h/48`. T63 defines the relative parameter `u=h/64` before using it, preserving the distinction from absolute input change. In the numerical examples it is small and lies inside the baseline's stated convergence interval. No unrestricted assertion about a binomial expansion for every possible `h` is needed.

11. **T71: agreement and accuracy.** The three constructions share a first-order term; the algebra in T52, T55 and T68 directly establishes that agreement. T does not treat them as independent numerical error checks. Its distinction between exact factorisation and approximation follows from B97 and L1. The aside about the external lecture's equality signs is a provenance claim only; the mathematical reason for using `≈` is present here.

12. **T73: P2.** The new input requires the signed step `63.7-64` and its division by 64 for the binomial parameter. Those are precisely the operations taught in T43–71. The request to identify approximation can be satisfied from the earlier exact-factorisation/truncation distinction, without seeing S2. Accessible alternatives include retaining rational step values throughout or using the printed decimal arithmetic.

13. **T75–77: reversal of question.** B178 already defines antiderivatives by differentiating back. T contrasts an exact derivative identity on an interval with a local estimate of a finite change. The distinction preserves L1's meaning; it does not infer integration from an approximate equality. This transition is explicit and warranted.

### L4 and L5

14. **T79–87: indefinite integral definition and notation.** The interval-based antiderivative definition matches B178. T supplies the meanings of integral sign, integrand, integration variable and arbitrary additive constant; the absence of bounds prevents confusion with a definite integral. `dF=f(x)dx` follows by applying T's defined differentials with `F'=f`. The all-antiderivative-family claim is already permitted by B178 and is subsequently justified in L5, so this is not an essential unsupported early use.

15. **T87–93: sine primitive and derivative check.** B153, B156 and B187 give `(-cos x)'=sin x`. Thus the sign and added constant are justified, and differentiating a proposed answer is an exact verification method. No extra trigonometric interpretation is required.

16. **T95–111: standard primitive collection and domains.** B182–195 supports the power and logarithmic rules; B154 supports the tangent primitive; B413 supplies the two inverse-trigonometric derivatives. T111 explains `dx` as `1 dx`, excludes `n=-1` from division by `n+1`, restricts powers to real differentiable intervals, excludes zero for `1/x` and cosine zeros for `sec²x`, and gives `(-1,1)` for arcsine and all reals for arctangent. These are the appropriate scopes for the displayed relations. The inverse notation is disambiguated using B107. The domain paragraph is adjacent to the list, before any downstream use.

17. **T113–120: logarithmic absolute value.** B60, B130, B149 and B164 permit the two branches. For negative `x`, `|x|=-x>0` and the chain derivative `(1/(-x))(-1)=1/x`. For positive `x` it is the ordinary logarithm derivative. T explicitly leaves zero undefined. This checks the claimed antiderivative on both intervals without treating a negative logarithm argument as legal. The comment on the source's property numbering cannot be verified here but contributes no mathematical premise.

18. **T122–124: why the constant is exhaustive.** Constant differentiation already explains why every `F+C` is an answer. T distinguishes that sufficient construction from proving that no other kind of difference is possible. The interval condition is named before the proof rather than concealed.

19. **T126–132: continuity and the new theorem.** T defines continuity in approach-to-value language, including one-sided endpoint approaches, and explicitly introduces the mean value theorem as an established theorem with continuity on `[a,b]`, differentiability on `(a,b)` and `a<b`. This is an allowed new mathematical premise. B140–142 supplies limit/derivative meaning, B30 supplies interval notation, and the printed theorem states exactly the net-change/intermediate-derivative connection used next. The external link is not needed to learn or apply the supplied statement. Demanding a separate derivation of the theorem would wrongly reject an explicitly introduced premise.

20. **T134: zero derivative implies constancy.** T supplies the needed connection from differentiability to continuity: a finite limiting difference quotient multiplied by a step tending to zero makes the output change tend to zero. For any two selected points in the differentiability interval, the closed segment between them remains in the interval; the theorem then gives difference zero. The ordinary meaning of an interval and T's supplied continuity connection make the argument accessible. No crossing of a domain hole or unsupported assertion of a global result is required.

21. **T136–142: two primitives and independent components.** B156 gives derivative linearity, so `(G-F)'=f-f=0`. Applying the immediately preceding interval result yields `G-F=C`, hence `G=F+C`. This is additive, as T emphasizes. Where intervals are separated, the theorem cannot connect across an undefined point; independent constants are allowed. All inferential dependencies are already supplied.

22. **T144–156: sine-square and cosine-square families.** The chain rule and trig derivatives give `A'=sin x cos x` and `B'=sin x cos x`. B111 gives `A-B=1/2`. Substitution into `A+C_A=B+C_B` produces `C_B=C_A+1/2`. T correctly distinguishes equality of families from equality of particular functions and explains why an initial value chooses a particular member. A direct identity comparison provides an accessible alternative to using the general theorem; neither path requires inaccessible facts.

23. **T158: P3.** The piecewise example is fully defined in the prompt, including the absent zero point. Its derivative claim follows from B156 separately on each open half-line. T126–142 already establishes why a theorem on an interval need not link two disconnected parts. The question is meaningful at this point, and a legitimate domain-based explanation is available before H3/S3.

### L6 and L7

24. **T160–169: substitution from the chain rule.** `du=g'(x)dx` follows from the defined differentials. With the explicitly stipulated `A'=q`, B164 gives `(A∘g)'=q(g)g'`, establishing the displayed primitive on intervals where it applies. T names the full product to replace and requires returning to `x` and differentiating the whole expression. This justifies the notation without treating an unmatched factor as dispensable. B197 independently supplies the same substitution rule.

25. **T171–183: polynomial substitution.** Choosing `u=x⁴+2` gives `du=4x³dx`, so the available factor is `du/4`. Integration of `u⁵` gives `u⁶/6`, hence total denominator 24, followed by restoration of the original variable. No division by `x³` is performed; the calculation therefore does not require excluding `x=0` or treating the inner function as globally invertible. This legitimate whole-product reading is explicitly taught in T162 and T177.

26. **T186–193: check and alternative route.** Differentiating the proposed polynomial gives `(6/24)(x⁴+2)⁵(4x³)`, equal to the integrand. The explanation of denominator 24 accounts for both operations. B88–97 and B190 permit finite expansion and termwise integration as another route, so the asserted alternative is available. It need not be carried out to justify the checked answer.

27. **T195–197: recognising and adjusting a guess.** B156's constant-multiple derivative rule justifies correcting a constant mismatch with a constant multiplier. A nonconstant derivative ratio cannot be made identically one by choosing a fixed scalar. T's statement concerns that scalar-adjustment method, not a claim that no other primitive can exist. The examples that follow keep this scope.

28. **T199–205: square-root example.** The rewriting as a negative half power uses B46. The chain derivative introduces `2x` and the outer factor `1/2`; they cancel and leave the original integrand. Since `1+x²` is positive on the real line, both the integrand and the given primitive are real and differentiable there. The equivalent `u=1+x²` route gives half the integral of `u^(-1/2)`, whose power-rule factor is 2. Both routes support the stated cancellation.

29. **T207–211: scaled exponential.** B147 yields derivative `6e^(6x)` for the guess, so dividing by 6 makes the derivative exactly the integrand. This is a concrete constant mismatch with a fully available check.

30. **T213–219: Gaussian-shaped exponential with an outside factor.** B147/B164 gives `(e^(-x²))'=-2xe^(-x²)`, hence multiplier `-1/2` yields the primitive of `xe^(-x²)`. T219 explicitly limits the answer to that integrand and explains how removing `x` changes the pattern. The two sine/cosine substitutions use the already supplied derivatives and recover the L5 pair; their signs are correct. No fact about a primitive of the factor-free exponential is assumed.

31. **T221: P4.** The modified polynomial inner derivative is `3x²`, a constant-ratio change from L6; using `F(0)=0` is supplied in B178 and illustrated conceptually in T156. The separate exponential proposal is assessable by the check just taught. The question does not require an unavailable special-function primitive or proof of its nonexistence. These are two linked uses of already stated decisions, not new missing premises.

### L8 and final lesson prompts

32. **T223–231: domain of the nested-log example.** B130 makes the inner logarithm real only for positive `x`; B32 excludes a zero denominator; `ln x=0` exactly at `x=1` follows from logarithm/exponential inversion. Thus the two open intervals are correctly identified before integration. This prevents reliance on the later absolute value to repair an invalid inner logarithm.

33. **T233–240: substitution and logarithmic primitive.** `u=ln x` has `du=dx/x` by B149 and T162. Factoring the differential integrand as `(1/ln x)(dx/x)` exposes the full replacement, giving `∫du/u`. T102–120 supplies `ln|u|+C` on nonzero branches; restoring `u` gives `ln|ln x|+C`. Every component of the substitution is explicitly mapped.

34. **T242–248: branch interpretation, exact check and constants.** The earlier domain excludes inner value zero, so absolute value makes the outer input strictly positive. For `x>1`, the inner value is positive; for `0<x<1`, it is negative and the expression becomes `ln(-ln x)`. B130 and B132 support those signs. The printed chain derivative `(-1/x)/(-ln x)` equals the desired integrand. T142 supports independent constants. The math establishes the repaired range internally; the statement about what the original source printed remains separately unverified.

35. **T250: P5.** The requested new power of the logarithm changes the `u` integrand to `u^(-2)`, for which B182/T98 supplies a primitive on nonzero real intervals, including negative `u`. The value `ln(e^(-1))=-1` follows from B130, and an additive constant is fixed by the given condition. The requested domain and derivative checks are exactly the skills just taught. No rule requiring a logarithm of negative `u` is introduced.

36. **T252: P6.** T144–156 already provides the two primitive representations and their constant relation. B101 supplies the sine/cosine values at `π/2`, so independently fitting the value condition and comparing the full expressions is available. It is not necessary to assume the constants equal merely because both are called integration constants.

37. **T254: P7.** Part (a) uses the established differential construction with B130/B149's logarithm value and derivative; part (b) uses B152's chain factor in differentiating `sin(3x)` and an initial value; part (c) directly revisits L8's domain distinction. All requests are supported before the help. The prompt explicitly contrasts approximate finite-step prediction with exact recovery, so it does not silently treat the two as one operation.

38. **T256: return and learning-use paragraph.** Returning later is presented as an adjustable way to use the supplied task, with no universal optimal schedule or retention claim. The references to recall and applying ideas to changed cases describe the observable task types. The instruction to retain an established part and consult matching help is operationally clear; it does not introduce an additional subject premise or substitute task success for learning evidence.

39. **T258: source note.** The titles, source coverage, fidelity and generated-practice assertions are statements within T, not independently verified provenance. They do not expand the permitted subject input or require following the links. Mathematical understanding through this point is supported without them. The named supplemental theorem has already been given in full.

### Hints in their printed positions

40. **T260–262: hint route and H1.** The heading correctly places help after the lesson and before complete solutions. Expanding `(3+h)²-9` uses baseline algebra and isolates the linear term exactly as L1 did. It points toward the required distinction without asserting a different definition of a differential.

41. **T264: H2.** The hint explicitly identifies both absolute change and relative binomial parameter and retains the sign. This helps the precise representation choice requested in P2; there is no new or missing mathematical premise.

42. **T266: H3.** Choosing endpoints of opposite sign reveals that the intervening closed interval includes the absent zero. T126 supplies why that matters to the theorem. This is a legitimate accessible diagnostic of the domain condition, not a demand for an untaught abstract connectedness theorem.

43. **T268: H4.** The hint points to the whole `x²dx` replacement, then the original value condition, and separately the derivative of `-x²`. Each is already supplied by L6/L7 and the baseline. It does not drop the inner derivative or imply that a constant can correct a variable mismatch.

44. **T270: H5.** Explicitly distinguishing `u^(-2)` from `u^(-1)` makes the changed antiderivative rule visible. Negative nonzero `u` is legal for a reciprocal integer power by B46 and B32. The given base produces `u=-1` through B130. This help resolves the relevant notation concern with premises already available.

45. **T272: H6.** The values at `π/2`, independent constants and identity comparison are all supported by B101, B111 and L5. The hint targets the same-family versus same-constant distinction in the prompt.

46. **T274: H7.** Each hint targets an established choice: base value/slope/step; trigonometric inner derivative; and inner logarithm, denominator, then outer logarithm. The ordering of the domain check is meaningful and prevents a later absolute value from being used to legalise an undefined inner expression.

### Complete solutions through the ending

47. **T276–278: solution route and S1.** The instruction to match solution to prompt is unambiguous. The printed derivative 6, differential `-0.6`, estimate 8.4, exact output 8.41 and exact change `-0.59` agree. Expansion gives discrepancy `h²=0.01`, explaining a smaller true decrease. The return prompt reinforces change versus new value. The solution does not convert a tangent estimate into an exact curve value.

48. **T280–287: S2.** The signed change `-0.3` produces differential `-0.00625` and estimate 3.99375. The factorisation `4(1-0.3/64)^(1/3)` is exact; dropping higher binomial terms is the approximation. The displayed result follows from the same linear factor 1/48. The caution against using `-0.3` as the bracket parameter is precisely warranted by the factorisation, not an arbitrary rule.

49. **T289: S3.** Each open half-line admits its own constant. A closed interval spanning both contains a point where the function is absent, violating the mean value theorem's assumptions. The solution answers the supplied counterexample question without weakening the interval theorem. The phrase 'connected interval' adds no required unfamiliar machinery because its operational meaning is explained by the hole at zero.

50. **T291–304: S4 polynomial component.** `du=3x²dx` gives a factor 1/3, and integrating `u⁵` gives total denominator 18. At zero, `2⁶/18=32/9`, so constant `-32/9` enforces the supplied condition. The printed derivative cancels `(6/18)3` to 1, and the answer is a polynomial real everywhere. All arithmetic, value and domain claims are supported. Writing `F(x)` alongside the temporarily substituted integral is conventional shorthand whose meaning is immediately restored by the last equality; it does not require treating `u` as the final independent variable.

51. **T306–313: S4 exponential component.** Differentiating the proposal gives `xe^(-x²)`, not the factor-free integrand on an interval. B130 makes the exponential positive; a fixed scalar multiplying its derivative cannot remove the variable factor on an interval. T313 also correctly limits what this rejection proves: no conclusion about whether some other primitive form exists is warranted by this particular check. This protects against an unsupported special-function assertion.

52. **T315–325: S5 construction and condition.** The whole-product substitution gives `∫u^(-2)du=-u^(-1)+C`; the exponent, rather than the mere presence of a logarithm, determines the rule. At `e^(-1)`, the primitive before constant is 1; thus `C=-1`. The displayed answer is explicitly restricted to the requested interval. These facts use T233 and the baseline's power/log rules, with no hidden sign convention.

53. **T327–333: S5 verification and extension.** The chain derivative `-(-1)(ln x)^(-2)/x` matches the requested derivative. The formula is real on both positive intervals excluding 1, while the initial condition determines only the component containing `e^(-1)`. Negative nonzero inner logarithm is acceptable in a reciprocal square; the solution explicitly distinguishes that operation from taking its logarithm. The possible independent extension is supported by L5, not imposed by the first condition.

54. **T335–343: S6.** At `π/2` the first unadjusted primitive is 1/2 and the second is zero, giving constants `-1/2` and 0. The trig identity converts the full first expression to the second, both derivatives match and both initial values vanish. `C_B=C_A+1/2` agrees with T156. The final interpretation accurately says a constant's numerical label depends on the chosen unadjusted primitive.

55. **T345: S7(a).** At base 1, `ln 1=0` and derivative 1 give differential 0.04 and logarithmic estimate 0.04. The exact equality belongs to the definition of `dy`; the finite output estimate remains approximate. The reference to the curved function is supported by the supplied derivative `1/x`, which is not constant near 1, and is not a claimed error estimate.

56. **T347: S7(b).** Differentiating `sin(3x)` produces factor 3, so division by 3 supplies the primitive and the zero-input condition fixes constant 2. Both the derivative and the supplied function value can be checked exactly using baseline trig values and chain rule. The comparison with (a) preserves the lesson's distinction between a recovered function and a finite-step estimate.

57. **T349–350: S7(c) and actual ending.** The final paragraph retains positive `x` and nonzero `ln x`, names both permitted intervals, confines `ln(ln x)` to the upper interval, and repairs the primitive with `ln|ln x|`. Independent constants and the inability of the outer absolute value to repair either `x≤0` or `x=1` are explicitly stated. Both branch derivatives are shown and correct. The final content line is 349 and the terminal empty element is 350; there is no unread mathematical ending or companion figure.

## Issues, alternatives and dependency status

No supported subject-content gap or ambiguity requiring correction was identified. In particular, the following apparent risks have legitimate accessible readings and are therefore not reported as defects:

- The differential equality is exact because T defines a tangent-line change; an interpretation requiring actual finite changes to be equal would contradict T's explicit explanation, not expose an omission.
- The early indefinite-integral family notation is available in B178; L5 then supplies an explicit theorem-based explanation of exhaustiveness. Later teaching is not being used retroactively to rescue an otherwise unavailable essential premise.
- The mean value theorem is a new established premise with conditions, which T is permitted to introduce. The continuity connection needed in its application is explained before the application is completed.
- Substitution replaces a whole product; neither the polynomial example nor `u=1+x²` requires dividing by a vanishing inner derivative or requiring a globally one-to-one inner function. The chain-rule verification supplies a direct legitimate route.
- The claimed limitation of constant adjustment is confined to correcting that guessed form. The final exponential discussion expressly avoids claiming that no other primitive can exist.
- Negative inner logarithm values are consistently separated from negative inputs to an outer logarithm. The two real domain components and their independent constants remain visible through the final paragraph.
- Hint and solution access is optional according to the printed route. The main lesson supplies the premises needed for each prompt before the prompt; no substantive answer is blocked pending information introduced only in its later help.

Accordingly there is no blocked mathematical dependency chain to carry into later conclusions in this report. Conclusions remain conditional on the baseline's declared usable-competence assumption, T's explicitly introduced mean value theorem, the usual real-domain conditions stated with its formulas, and the frozen-input scope. This says that premises and warranted connections are present; it does not certify actual learner performance.

## Independent verification limits

The following statements cannot be independently checked without reading prohibited additional subject/source material:

- T29's attribution of a compact differential form to the lecture; T71's claim about printed equality signs; T95's attribution of a standard-form list; T120's property/item numbering comparison.
- T132's claim that the linked supplemental document gives the stated theorem on page 1.
- T144, T171, T197, T219 and T225's descriptions of examples or terminology as lecture/source content; T248's assertion about the original source's stated domain and printed primitive.
- T258's claim of coverage of the cover and four printed pages, retained mathematical content, and generated rather than quoted practice.

These are source-fidelity limits, not newly established errors. The supplied theorem can be evaluated as a declared premise and all displayed calculations can be checked internally without verifying its citation. No new scientific law, empirical model or quantitative learning-effect claim is required by this calculus lesson. The adjustable scheduling suggestion at T256 does not claim an empirically optimal interval; this reading provides no evidence of its effect on any person.

## Coverage statement

Actual complete baseline coverage: B1–1378, displayed consecutively in nine packets before teaching access. Actual complete teaching coverage: T1–350, displayed consecutively in three packets. The witnesses cover the definitions, explanations, equations, example checks, transitions, prompts P1–P7, hints H1–H7, solutions S1–S7 and final domain explanation. No missing/truncated input, unread ending, uninspected companion or retrieval repair occurred. This original report applies only to the stated teaching hash and must not be reused as a fresh-reader evaluation of a changed revision.
