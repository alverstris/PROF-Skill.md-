# SASIS document reading: frozen candidate 1, teaching v3

## Bounded finding

No established defect in learner access to the mathematical meanings, consequential steps, or task dependencies was found in this frozen document against the complete supplied four-subject baseline. The reading supports acceptance on that defined criterion. The logarithmic differentiation, derivative-quotient limits, and distinction between instantaneous relative rate and finite percentage change have supported routes before their respective tasks. The later hints and solutions agree with those routes; they are not needed to supply a missing earlier prerequisite.

This is an evaluation of the document, not a test or grade of a student. It makes no claim about human learning, retention, independent performance, or exclusion of every latent error. External accuracy of the source attribution and source-coverage statements remains outside the permitted evidence.

## Inputs and actual access

Both subject inputs were read from the immutable git commit `28825d27b93baef43a5751eacecac81fa46841bc` in `/workspace/scratch/ac36b9c5ff31/PROF-repo`:

| Input | Immutable path | SHA256 | Actual size |
|---|---|---|---|
| B: complete baseline | `references/sasis/ocr-baseline-20261007/student-baseline.txt` | `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5` | 247840 bytes; 246945 raw UTF-8-decoded characters; 1377 LF characters |
| D: complete teaching packet | `runs/y1-reader-20261008/iterations/006/regenerated-r13-candidate1/teaching-v3.md` | `311afdef083a4468f18bcdd11a68975d2e6622661e0be3405a5c9f58b3f3a813` | 28777 bytes; 28753 raw UTF-8-decoded characters; 731 LF characters |

The baseline was delivered and read first, sequentially, in 16 chunks: `[0,16000)`, `[16000,32000)`, `[32000,48000)`, `[48000,64000)`, `[64000,80000)`, `[80000,96000)`, `[96000,112000)`, `[112000,128000)`, `[128000,144000)`, `[144000,160000)`, `[160000,176000)`, `[176000,192000)`, `[192000,208000)`, `[208000,224000)`, `[224000,240000)`, `[240000,246945)`. This included Mathematics H240; Further Mathematics H245 Pure Core Y540/Y541, Statistics Y542 and Mechanics Y543; Physics H556; and Chemistry H432 through its final references and ending.

The teaching was then delivered and read in `[0,10000)`, `[10000,20000)`, `[20000,28753)`, covering P001–P194 in order, including the tasks at their positions, the complete grouped hints and solutions, and the source/scope ending. Intervals are zero-based and end-exclusive over the original decoded string. Input bytes were decoded with `bytes.decode('utf-8')`; CRCRLF was not normalised. Every retrieval succeeded. No output was truncated; no missing interval or recovery remains. The adjacent access JSON records each actual range and tool result.

Only the two exact `git show COMMIT:PATH` objects supplied subject content. No filesystem source copy, directory listing, search, browser, external source, other revision, earlier report, author material, memory retrieval, or subagent was used. The output-writing operation creates only this report and its requested access JSON. These are instruction-confined access restrictions, not a claim of technical isolation of shared tools or erasure of pretraining.

## Baseline locators used in reconstruction

The following locators combine a unique baseline heading or item with its actual retrieved raw-character interval. They locate supplied operational content, rather than merely naming a curriculum topic.

| Locator | Available premises |
|---|---|
| B-M1: Mathematics, “Prior arithmetic, geometry and mathematical language” and “Proof and mathematical work”, `[0,16000)` | Percentage change `100(B-A)/A`; signed arithmetic; domain/denominator checks; implication versus converse; deduction from stated premises; a model's assumptions and limits. |
| B-M2: Mathematics, “Algebra, functions and coordinate geometry”, `[0,16000)` | Positive-base exponent laws, rational powers, function/domain/range and inverse meanings, composition, algebraic rearrangement, straight-line/secant gradient. |
| B-M3: Mathematics, “Sequences, series and binomial expansion”, `[0,16000)` | Sequence indexing, convergence as approach to a finite limit, divergence, geometric powers, and the warning that solving a proposed limiting equation alone does not establish convergence. |
| B-M4: Mathematics, “Exponentials and logarithms”, `[16000,32000)` | Positivity and monotonicity of real exponentials; `e^x` characterised by its derivative; logarithms as inverses; `ln 1=0`; `e^(ln x)=x`; `ln(e^x)=x`; product and power logarithm laws on their stated domains; proportional growth and decay. |
| B-M5: Mathematics, “Differentiation and its applications”, `[16000,32000)` | Difference quotient and tangent/rate meaning; `d(a^(kx))/dx=k ln(a)a^(kx)`, `d(e^(kx))/dx=ke^(kx)`, `d(ln x)/dx=1/x` for positive x; product/chain rules; local inverse-rate rule with its conditions; derivative-sign monotonicity; positive second derivative as increasing gradient/convexity. |
| B-M6: Mathematics, “Integration and elementary differential equations” and “Numerical methods”, `[16000,32000)` | Fundamental theorem for continuous integrands; exponential proportional-rate model; convex curves below chords; ordinary continuous-function and limit reasoning in the stated well-behaved cases. |
| B-F1: Further Mathematics FM27–FM28, `[64000,80000)` | Real Maclaurin expansions, including exponential/logarithmic examples, and explicit finite-limit reasoning; no unrestricted complex-argument expansion or general remainder theorem is assumed. These are available but not required to invent a new limit method here. |
| B-P1: Physics, “Reference data” and “Units and calculations”, `[80000,96000)`; “Vectors, graphs and rates”, `[80000,112000)` | Dimensional consistency; logarithms of ratios or numerical values in stated units; tangent versus secant; exponential models and constant fractional versus constant absolute change. |
| B-C1: Chemistry CH-00 and CH-01.01, `[144000,160000)`; CH-12, `[240000,246945)` | Unit and formula conventions, legitimate cross-subject deductions, and the limit that names do not supply unstated university facts. No additional chemical law is required by this lesson. |

All four subject sections were read. The teaching's decisive premises are mathematical; the full physics/chemistry reading did not supply an otherwise missing calculus theorem. The baseline already supplies the standard exponential and logarithm derivative rules. Their reconstruction in the lesson therefore need not count as a first proof from an otherwise empty starting point.

## Chronological coverage and reconstruction witnesses

The groups below follow the teaching's order. Routine algebra is grouped only where its premises and consequential result are explicit. Task witnesses describe availability in the document, rather than a battery of simulated student attempts.

### Opening and Part 1: P001–P031

P001–P005 state the topic, reading route, real-variable convention, positive logarithm inputs, derivative meaning, and product/chain rules. The announced changing-power and relative-change connection is a preview, not an unexplained step used immediately. The named starting tools are supplied in B-M1–B-M5. Source attribution in P002 is a provenance claim, considered separately below.

P007–P017 distinguish a fixed base from its varying exponent. Factoring `a^(x+h)-a^x=a^x(a^h-1)` is justified by B-M2; the factor `a^x` is fixed during this limit. With the usual differentiability expressly assumed in P010, the quotient at zero defines `M(a)` and gives `(a^x)'=M(a)a^x`. The interpretation as slope at `(0,1)` follows by setting x=0. The symbols h, M, base a and independent variable x are distinguished; division uses h nonzero before the limit. No construction of all real powers is silently required: continuity and differentiability of that family are explicitly accepted premises and are compatible with B-M4–B-M5.

P018–P025 give the slope-one characterisation of e and label existence as foundational. The graph comparisons in P022 have enough textual data to reconstruct both secants: slopes are 1 from `(0,1)` to `(1,2)` for base 2 and from `(-1/2,1/2)` to `(0,1)` for base 4. Their tangent inequalities are supported without an absent picture. Specifically, B-M5 already gives `(a^x)''=(ln a)^2 a^x>0` for a>1, so the gradient strictly increases; B-M5–B-M6 give the convex/secant interpretation. Equivalently the secant is the interval average of the derivative, strictly between its endpoint values. This uses an actually supplied baseline derivative rule, not the later identification of M as a secretly imported result. P023 explicitly defers the continuity/increase-of-M justification for the bracket and does not pretend that pictures prove existence or uniqueness. P053 later identifies M; no intervening task requires that deferred bracket.

P026–P028 apply the supplied chain rule correctly to `e^u`: evaluate the outer derivative at u and multiply by u'. The `e^(3x)` example exhibits both parts. At A1 (P029–P031), the available construction is already `2e^(2x-1)` and evaluation at x=1/2 gives slope 2. Its requested explanatory factor is taught before the task; later help is not needed to introduce it.

### Part 2: P032–P057

P033–P040 make inverse notation explicit, distinguish a function value from multiplication, enforce positivity, and derive the product logarithm law using `u=e^r`, `v=e^s`. The power law and sign statements are also directly supplied by B-M4. No logarithm at a nonpositive input is used.

P041–P047 reconstruct the logarithm derivative from `e^(w(x))=x`: chain differentiation gives `e^w w'=1`, so division by the positive x gives `w'=1/x`. The inverse's local differentiability is not an inaccessible new prerequisite here: B-M5 supplies both the conditional inverse-rate rule and the actual positive-domain logarithm derivative. Positive derivative gives monotonicity. Continuity follows from differentiability; the short underlying deduction is that an increment equals h times its convergent difference quotient. The composite formula `u'/u` tracks the whole input. In `ln(1+x^2)`, the input is always positive and the derivative is `2x/(1+x^2)`. Its zero value at x=0 is consistent with symmetry; the text does not infer differentiability from symmetry alone.

P049–P054 rewrite a positive constant base as `a=e^(ln a)` and hence `a^x=e^(x ln a)`. Since ln a is fixed, the chain factor is ln a. Comparing with the slope definition identifies `M(a)=ln a`. The established logarithm derivative/inverse relation gives continuity, strict increase and the unique solution `ln a=1`, namely a=e. The extension to bases between zero and one and to base one has the right signs; negative bases are expressly outside the general claim.

At A2 (P055–P057), the earlier formulas and B-M1–B-M5 already determine the real domain of `(1/2)^(3x)` as all real x and its derivative as `3 ln(1/2)(1/2)^(3x)<0`. For `ln(5-2x)`, the domain inequality gives x<5/2 and derivative `-2/(5-2x)<0`. Both inner derivatives and sign arguments are available at the task's position.

### Part 3: P058–P080

P059–P066 state the positive-function condition and rearrange the log chain rule to `f'=f(ln f)'`. P061 explicitly separates differentiation of a composite logarithm from taking a logarithm of the derivative. Multiplication back by f is legal and restores absolute rate; f need not be positive for every calculus problem, only for this stated procedure. The repeated constant-base calculation keeps ln a fixed.

P067–P074 correctly identify the two changing appearances of x in `x^x`. On x>0, `ln f=x ln x`; the product rule gives `ln x+1`, and multiplication by the original function gives `x^x(ln x+1)`. Its value at x=2 is `4(ln 2+1)`. Treating the exponent as fixed would change the function being differentiated. The alternative exponential rewrite confirms the same derivative using established rules, without an additional method.

P075–P077 explicitly construct `u^v=e^(v ln u)` for positive differentiable u and differentiable v. Thus positivity and differentiability of y have an available basis before division by y. Product and chain differentiation give `y'/y=v'ln u+v u'/u`; the two constant cases remove the correct term. There is no assumed general negative-base real power here.

At A3 (P078–P080), x>-1 permits `ln y=x^2 ln(1+x)`. The available derivative is `(1+x)^(x^2)[2x ln(1+x)+x^2/(1+x)]`, with slope zero at x=0. The explanation of the missing exponent-change term is already provided by P075–P077. A correct slope at this one point alone would not establish a correct general derivative; the task asks for both.

### Part 4: P081–P100

P083–P088 define a positive sequence with integer index and carefully rename its logarithm. The equality `a_k=k ln(1+1/k)=ln(1+1/k)/(1/k)` uses only positive inputs and the log power law. With h=1/k, it is exactly the difference quotient of ln at 1 along positive h tending to zero. Restricting the approach to this sequence preserves the derivative limit already supplied in Part 2 and B-M5. P089–P095 consequently obtain `a_k→1`, then `b_k=e^(a_k)→e` by the previously accepted continuity of exp. The existence of b_k's limit is established by that route; it was not assumed before taking logarithms.

P096's finite estimate is consistent with `(1.1)^10=2.5937424601` and the supplied `e≈2.71828`; the percentage shortfall is about 4.58%. It does not infer a finite-index accuracy guarantee from convergence. P097 specifies positivity for negative increments and distinguishes finite logarithm limits, growth to positive infinity, and decay to zero. Increase and unboundedness of exp are an expressly stated property here and have a short route from its inverse covering every positive number; `e^(-x)=1/e^x` then supplies the negative direction. No general asymptotic theorem or l'Hôpital rule is needed.

At A4 (P098–P100), k>2 makes the base positive. Substitution h=-2/k gives `ln b_k=-6[ln(1+h)-ln 1]/h`, with h approaching zero from below. The previously established two-sided derivative yields -6 for the logarithm limit and the continuous inverse yields `e^(-6)` for the original. The side, domain and final inverse operation are all available before this task.

### Part 5 and later return: P101–P120

P102–P104 reproduce B-M1's finite fractional change with the initial value in the denominator. P105–P107 identify the instantaneous relative rate as `F'/F=(ln F)'`, distinguish it from an absolute rate, and carry points/day to 1/day. The fixed positive reference interpretation `ln(F/F_ref)` is dimensionally meaningful (B-P1); differentiating the constant scaling indeed leaves F'/F.

P108–P112 justify the local approximation directly from the derivative: for nonzero small Δt the difference quotient is close to F', so the increment is approximately F'Δt; division by positive F gives the local fractional-change formula. Applying the derivative of ln at 1 to a small fractional increment gives `ln(1+r)≈r`. These are explicitly approximations, not a false equality of finite percentages and logarithmic changes.

P113's model has derivative `2.4e^(0.03t)`, ratio 0.03/day, and exact daily percentage `100(e^0.03-1)≈3.045%`. The differing outputs refer to different quantities; the numerical exponent uses time in the specified days. At A5 (P114–P116), the construction already gives absolute rates -6 and -200 points/day at zero, equal relative rates -0.02/day, separate 50-point changes of `-50/3%` and `-0.5%`, and the model's exact daily change `100(e^(-0.02)-1)%`. No market data, lookup or financial premise is needed.

P117–P120 present A6 as a later optional return route with a retrieval request and then method/limit requests. The requested meanings and derivatives were established before this point. For the changed sequence, Part 4 gives `a_k=k ln(1+1/k)→1`, while `ln c_k=k a_k`. The ordinary meaning of convergence to 1 ensures `a_k>1/2` eventually, so `ln c_k>k/2→+∞`, and P097 gives `c_k→+∞`. This is a short supported bound, not an unprovided theorem or an assumption that an infinity-times-zero expression has a value. The later hint makes the bound explicit, but the route is already available from the earlier result. P118's description of revisiting the lesson is not treated as evidence about anyone's performance or retention.

### Hints, complete solutions, ending: P121–P194

The six hints (P123–P140) were read in their actual later positions. A1 specifies the inner/outer chain factors; A2 specifies the exponential rewrite and positive-input inequality; A3 preserves the product-rule contributions; A4 supplies k=-2/h; A5 separates derivatives, relative rates and finite ratios; A6 supplies the eventual half-bound. Each develops the corresponding earlier route and introduces no incompatible convention.

All six solutions were then read fully. P143–P147 give the A1 derivative and slope with a reason to differentiate before substituting. P148–P155 give the correct A2 domains and negative derivatives. P156–P164 give the A3 formula and correctly explain that the missing term happens to vanish at zero. P165–P173 give the left-sided quotient, -6 logarithm limit, and positive original limit `e^(-6)`. P174–P184 keep the two rate units and the separate finite falls distinct; `100(e^(-0.02)-1)%≈-1.9801%` has the correct sign and smaller magnitude than 2%. P185–P191 recover M's geometric meaning, distinguish power/exponential/changing-power derivatives, and provide the explicit eventual bound for divergence. The explanatory cautions describe possible errors without asserting that a reader made them (P142). No solution contradicts its question or repairs a demonstrated missing prerequisite.

P192–P194 provide source attribution, scope, generated-task status and claimed source corrections. These were read, including the final sentence. The present packet contains no embedded graphical assets to inspect. Its references to three figures are accompanied by enough formulas, points, slope descriptions and orientation to reconstruct the mathematical connections being used. A missing source image therefore does not establish a mathematical accessibility defect in this complete single-file packet.

## Defects, alternatives, and limits

**Established defects:** none found within the two-input accessibility remit. No identified dependency remains blocked or merely conditional on missing subject content.

**Considered concerns resolved by available routes:** The inverse-differentiation sentence does not require inventing a university inverse-function theorem, because the baseline supplies the actual inverse/log derivative rules. The geometric comparisons do not require importing unseen figures, because their coordinates and slope relationships are given and baseline curvature/calculus suffices. The e bracket is explicitly deferred rather than used as a necessary earlier conclusion. The sequence arguments do not require assuming convergence of the original powered expressions, nor a general theorem for indeterminate forms. The eventual bound in A6 follows from the earlier finite logarithm limit; the later help is confirmatory rather than retroactive support.

**Provisional concerns:** no unresolved mathematical-accessibility concern is established by this reading. This is a bounded judgment, not proof that all alternative reader interpretations or latent technical errors have been excluded.

**External-provenance limits:** P002, P017, P021–P023, P063, P067, P082, P096, P104 and P193–P194 make claims about a lecture, its figures, page coverage, title, closing remarks and typos. The linked MIT PDF, course-year evidence, original diagrams, and claimed corrections were not accessed under the task's restrictions. Their fidelity and external truth cannot be verified here. These claims are not needed as mathematical premises for the reconstructed results. Foundational real-exponential properties are evaluated as explicitly declared premises with intelligible scope, not independently established external facts. No verdict about provenance or educational effectiveness is inferred from this document-access finding.

This report records one frozen revision and is not an author-feedback revision.
