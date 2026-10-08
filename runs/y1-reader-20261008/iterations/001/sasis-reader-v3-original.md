# SASIS original reader report — D001 v3 fresh

## Result and scope

The supplied teaching route is reconstructible from the complete supplied baseline and the document's own introductions. I found no established subject-content defect and no blocked mathematical or physical conclusion in P03–P40. The reciprocal derivative, tangent geometry, positive-integer power proof, motion calculations and existing A–D tasks have accessible, valid connections. This conclusion concerns the frozen notes and their stated models, not a student's performance, learning or retention. It is not a claim of exhaustive error discovery.

No outside source, other report, prior conversation, missing reference sheet or external subject premise was used. The document's links were not opened. Its source-history, historical-attribution, course-provenance and licence claims therefore remain independently unverified. The instruction whitelist governed this reading; it did not provide technical isolation or erase pretrained knowledge, and I do not claim that all the long baseline remained simultaneously retained.

## Actual input access

Both authorised files were read from their exact paths with Python `Path.read_bytes().decode('utf-8')`. Byte identities were computed before reading the subject text. They matched the supplied identities exactly:

| Input | Bytes | Original decoded characters | SHA-256 |
|---|---:|---:|---|
| `/workspace/scratch/ac36b9c5ff31/sasis-d001-v3-fresh/baseline.txt` | 247840 | 246945 | `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5` |
| `/workspace/scratch/ac36b9c5ff31/sasis-d001-v3-fresh/document.md` | 24313 | 24279 | `494a7508d8b7fbe56f3ce3c9a6fbe1bf2261ecdbfca0a80e81c8997d46dc6d13` |

The following are actual zero-based, end-exclusive decoded-character ranges displayed and read, in order. No newline normalisation was used to establish coverage; the mixed carriage-return sequences remained in the original decoded string.

| Baseline reading sequence | Range |
|---:|---|
| 1 | `[0,18000)` |
| 2 | `[17900,35900)` |
| 3 | `[35800,53800)` |
| 4 | `[53700,71700)` |
| 5 | `[71600,89600)` |
| 6 | `[89500,107500)` |
| 7 | `[107400,125400)` |
| 8 | `[125300,143300)` |
| 9 | `[143200,161200)` |
| 10 | `[161100,179100)` |
| 11 | `[179000,197000)` |
| 12 | `[196900,214900)` |
| 13 | `[214800,232800)` |
| 14 | `[232700,246945)` — EOF |

This covered the cover text, Mathematics, all Further Mathematics Pure/Statistics/Mechanics entries, Physics, and Chemistry through CH-REF and the final research-record notice. The last slice was printed through the actual decoded EOF, followed by the length 246945. The reference notice did not authorise or cause retrieval of its named file.

Only after that complete baseline reading, the document was read in physical order as `[0,12200)` and `[12100,24279)` through EOF. These cover P01–P42, every displayed mathematical representation, all attempts, hints and solutions, and the source/licence and changes paragraphs. The final output confirmed decoded length 24279. No displayed reading output was truncated. Subsequent read-only searches within these same two inputs located headings and P-identifiers for this report; no other subject-content input was accessed. There was no identity, decoding, access or missing-input failure.

## Baseline locator key

These locators identify operative supplied content, not merely topic names. Character ranges below refer to the same original decoded baseline.

| Key | Precise supplied locator and usable content |
|---|---|
| B1 | Mathematics, “Prior arithmetic, geometry and mathematical language”, `[3257,5815)`: signed arithmetic, units, domains, implication, nonzero division, root checking; triangle area `bh/2` with perpendicular height. |
| B2 | Mathematics, “Proof and mathematical work”, `[5815,7179)`: deduction from definitions/assumptions; one admissible counterexample disproves a universal statement; examples alone do not prove a general rule; model assumptions and limitations. |
| B3 | Mathematics, “Algebra, functions and coordinate geometry”, `[7179,12948)`: expansion/factorisation and real roots; modulus definition at 9050; function/domain and inverse/reflection discussion at 9426; lines, gradients and midpoint averages at 11555. |
| B4 | Mathematics, “Sequences, series and binomial expansion”, `[12948,15243)`, especially the positive-integer expansion beginning at 14437: finite indexed sums, binomial expansion and factorial coefficients. |
| B5 | Mathematics, “Differentiation and its applications”, `[20248,23787)`: derivative as a difference-quotient limit/local rate/tangent gradient; first-principles polynomial expansion/cancellation; power derivatives, sums and constant multiples; point-slope tangent equation and sign of derivative. |
| B6 | Mathematics, “Mechanics”, starting at 41579: units and scalar/vector distinctions (41594); constant-acceleration component position law (42117); velocity as derivative of position (42866); displacement versus distance and speed versus signed velocity. |
| B7 | Further Mathematics FM09–FM11, especially FM11 at 56123: coordinate transformation matrices; reflection in `y=x` swaps the two coordinates. |
| B8 | Further Mathematics FM57 at 80355, and Physics “Units and calculations” at 93236: dimensions of velocity/acceleration, matching dimensions and powered-unit conversion. Physics “Motion and forces” at 104355 and “Energy, work, power and momentum” at 108004 reinforce signed kinematics and idealised model conditions. |

No additional Further Mathematics Statistics, advanced physical law, or Chemistry result was needed to complete this particular document. Those sections were nevertheless read in full and were not replaced by their names or summaries.

## Chronological reconstruction witnesses

The teaching order is P03–P30, with A, B and C at P09, P22 and P29, and D on the later visit specified at P31. Each attempt explicitly points to its own later hint and solution. The witnesses below first check what is available when the attempt occurs, then check the authored help. They do not use a later solution to repair an earlier required inference. P32–P40 were also read in their physical order, as recorded above. No extra problems or student-testing battery was introduced.

### P01–P08: local rate, signed geometry and reciprocal derivative

**P01–P03.** The title, prerequisites and route agree with B3–B6. The reader already has algebra, line gradients, elementary differentiation and finite binomial expansion. The goal is a connected construction and justification, not an unsupported assertion that the topics are wholly new. Secant slope as an interval comparison and derivative as its local limit have B5 support. Slope, velocity and other output-per-input rates share the same quotient structure. Exponentials and inverse trigonometric functions are explicitly a preview and are not used to establish a current result.

**P04.** Fixing `x0` while varying a nonzero `h` gives two distinct input coordinates, both required to be in the domain. Their ordered-pair ordinates are `f(x0)` and `f(x0+h)`. B3's line-gradient formula gives `[f(x0+h)-f(x0)]/[(x0+h)-x0]`, hence the displayed quotient. The two subtractions have the same new-minus-old orientation. Output units divided by input units follow B1/B8; neither an unexplained zero denominator nor a different quantity is introduced.

**P05.** The coordinate construction supplies the complete geometry without a missing picture: `R` shares `P`'s ordinate and `Q`'s abscissa, so `PR` has signed horizontal change `h` and `RQ` signed vertical change `Δf`. The derivative definition agrees with B5 and adds explicit finite/two-sided conditions for an interior point. The prime, evaluation input, fixed versus varying roles, tangent through `P`, and exclusion of an infinite slope from this finite derivative are intelligible. “Both sides” is not silently replaced by a single convenient sign of `h`.

**P06.** At zero the cubic quotient is `(h³-0)/h=h²`, which tends to zero from both signs; B3/B5 then give tangent `y=0`. The cubic has opposite signs on opposite sides of zero, so it crosses that tangent. For the other line, `x³=-x` becomes `x(x²+1)=0`; `x²+1` is positive for real `x`, so the origin is its only intersection. Its slope `-1` differs from the established tangent slope `0`. This is an accessible pair of counterexamples to interpreting tangency by intersection count, using B2 rather than an unsupported drawing convention.

**P07.** The reciprocal domain removes `x0=0` and `x0+h=0`; the quotient also removes `h=0`. Combining the reciprocal terms produces numerator `x0-(x0+h)=-h` and denominator `h x0(x0+h)`. Cancelling the nonzero `h` yields `-1/[x0(x0+h)]`. These are B1/B3 fraction operations with all exclusions retained. The original quotient is still undefined at zero change; the simplified nearby expression is what supports the limit.

**P08.** For fixed nonzero `x0`, `x0(x0+h)` approaches the nonzero `x0²`; its reciprocal therefore approaches `1/x0²`, giving derivative `-1/x0²`. This is the ordinary non-singular algebraic limiting operation used in B5's first-principles work, not an imported advanced theorem or replacement of `0/0` by zero. Since a nonzero real square is positive, the derivative is negative. B5's derivative-sign interpretation applies separately on the two domain intervals; the text expressly avoids claiming monotonic passage across the absent input zero. Its caution that cancellation is one method and previously established rules can be used is compatible with the baseline.

### P09: Attempt A, with its supplied help

**Availability at P09.** P07–P08 already give both the finite quotient and its limit, so no later premise is necessary. Substituting `x0=2` gives `-1/[2(2+h)]`; choosing the two nonzero changes leaves the quotient finite. The difference between this interval calculation and the limiting slope has been taught at P04–P08.

**P32 and P37.** The hint preserves `h` for the secants and points to whether the starting point exists at zero. The solution's denominators are `2(2.1)=4.2` and `2(1.9)=3.8`, giving `-5/21≈-0.2381` and `-5/19≈-0.2632`. The derivative is `-1/2²=-0.25`. The explanation correctly contrasts distinct-point quotients with their limit. At zero, the failure precedes any limit: `f(0)` and hence the fixed graph point are absent. This supplies the requested conceptual explanations, not merely three correct numbers. The return to P10 restores the lesson route.

### P10–P15: tangent equation, triangle, symmetry and notation

**P10.** B3/B5 supply `y-y0=m(x-x0)`. Replacing `y0` by `1/x0` and `m` by `-1/x0²` gives the first equation; distributing and adding `1/x0` gives `y=2/x0-x/x0²`. The parameter `x0` remains fixed while the line coordinates vary. Substitution at contact returns `1/x0`, so the algebra represents the tangent at the stated point, not a second curve with moving `x0`.

**P11.** Setting `y=0` and multiplying by the permitted nonzero `x0²` gives `x=2x0`; setting `x=0` gives `y=2/x0=2y0`. Both intercepts are finite and nonzero. The axes and the line therefore bound a right triangle with the listed vertices. B1's perpendicular-base area and B3's modulus give `A=(1/2)|2x0||2/x0|=2`, since the product of the two lengths is 4. If `x0<0`, both intercept coordinates are negative, placing that triangle in the third quadrant; if positive, both are positive. “Coordinate square units” identifies a coordinate-geometric area, and the absolute values resolve the otherwise consequential signed-length ambiguity.

**P12.** For `x0=2`, P10 becomes `y=1-x/4`; its intercepts are `(4,0)` and `(0,1)`, so area is `(1/2)4·1=2`. The general midpoint is the coordinate average of `(2x0,0)` and `(0,2/x0)`, namely `(x0,1/x0)` by B3. The side-length product 4 established at P11 explains shape change with area preservation.

**P13.** On the reciprocal graph `xy=1` is equivalent to `y=1/x` and ensures neither coordinate is zero. Swapping coordinates preserves this equation; reflection in `y=x` is available in B3/B7. The claim that the tangent maps to the tangent is also reconstructible here without assuming a general geometric theorem: swap coordinates in the already derived tangent `y=2/x0-x/x0²` and rearrange to get `y=2x0-x0²x`. At the reflected input `y0=1/x0`, P10 gives `y=2/y0-x/y0²=2x0-x0²x`, the same line. Swapping an old intercept `(0,b)` makes `(b,0)`. Applying P11 at input `y0` gives new x-intercept `2y0`, and hence the original y-intercept. This short substitution supplies the consequential connection; it requires no outside “reflection preserves tangency” convention.

**P14.** Inserting the declared second input `x=x0+Δx` into the output difference explains every equality for `Δy=Δf`. Both delta quotients refer to the same signed change, and `Δf` is explicitly not a new function. The evaluation bar and Leibniz notation are introduced with their roles. The derivative remains a limit, and the notation does not authorise cancellation of a letter `d` or putting zero in a finite-change denominator.

**P15.** Letting the evaluation input vary collects the already defined values into a derivative function; the equal labels `f'`, `df/dx` and `Df` are explicitly introduced. Parentheses specify the operator's operand. Applying it to `1/x` gives the function `-1/x²`; the evaluation bar at 2 gives `-1/4`. Thus operator, function and value are distinguishable. The designation “Lagrange notation” is supplied terminology and creates no computational dependency. Its historical correctness and the assertion that it corrects a particular source were not independently verified from the permitted inputs.

### P16–P21: finite-product proof and polynomial combination

**P16.** A fixed positive integer `n` and fixed evaluation input `x` are distinguished from varying `h`. For `n=1`, expanding the numerator gives `h`, so the nonzero quotient is exactly 1. This separately handles the case without a remainder sum and supplies a value even at input zero.

**P17.** For `n≥2`, expansion of `n` factors gives the all-`x` term `x^n`; selecting one `h` gives `n` copies of `x^(n-1)h`; selecting `k` copies gives `binom(n,k)x^(n-k)h^k`. B4 supplies the finite binomial/counting rules. The explicit sum from 2 through `n` is exactly the remainder, with no infinite series or omitted approximation. The paragraph also explicitly supplies the polynomial convention for a zero exponent at `x=0`: selecting no such factors contributes 1. Thus a generic rule for a positive base is not being silently applied to an unresolved `0^0` expression.

**P18.** Big-O is new notation, but its needed meaning is actually defined: a fixed finite bound `C|h|²` near zero, with `C` independent of `h` and allowed to depend on fixed `x,n`. Factoring `h²` from each remainder term leaves powers `h^(k-2)`. For `|h|≤1` these have magnitude at most 1, and all `n-1` coefficients are fixed. The stated absolute-sum bound yields precisely the displayed `C=sum binom(n,k)|x|^(n-k)`. The absolute-sum inequality is intelligibly supplied and can also be deduced from B3's modulus: each real term lies between minus and plus its magnitude, so the sum lies between minus and plus the sum of magnitudes. The zero-exponent convention just introduced covers the end term at `x=0`. This proves the bound rather than only naming a remainder class.

**P19.** Subtracting the all-`x` term and dividing by nonzero `h` leaves `nx^(n-1)+R_n/h`. The P18 bound becomes `|R_n/h|≤C|h|`, whose nonnegative upper bound tends to zero from either sign of `h`. The remainder's distance from zero therefore vanishes. The constant surviving term is the derivative. This makes the limiting connection explicit enough without requiring formal epsilon–delta analysis, which the baseline does not grant. The scope stays positive integers; the `n=1` convention is tied to its direct calculation, and other exponents are not inferred from finite-product selection.

**P20.** The cubic expansion leaves exact remainder `3xh²+h³`; division leaves `3xh+h²`. For `|h|≤1`, their magnitudes are respectively bounded by `(3|x|+1)|h|²` and `(3|x|+1)|h|`. This reconstructs the two claimed orders and why the divided remainder vanishes. The example of remainder `h` correctly shows the insufficiency of merely tending to zero before division, because `h/h=1`. Setting `x=0` gives quotient `h²`, agreeing with the earlier cubic example without retroactively supporting it.

**P21.** Expanding the output difference of `u+cv` splits it into the output difference of `u` plus `c` times that of `v`, and division by the same nonzero input change preserves the split. Taking the given finite derivative limits yields `u'+cv'`, already an available rule in B5 and now connected to the construction. A constant has zero output change, so its quotient and derivative are zero. The displayed polynomial uses the new positive-integer rule and this linear combination: `2x+3·10x^9=2x+30x^9`. No product-rule assumption about the factor 3 is required.

### P22: Attempt B, with its supplied help

**Availability at P22.** P16–P21 supply expansion, a derivative limit and polynomial rules; P10 supplies a line from point and slope. P11's area was conditional on the reciprocal's actual intercepts, so there is no supplied general law forcing another tangent to have the same triangle.

**P33 and P38.** The hint gives `q(1)=-2` and directs expansion before subtraction. Expanding gives `q(1+h)=-2+3h²+h³`; subtracting `-2` and dividing by nonzero `h` gives `3h+h²→0`. The point `(1,-2)` and zero slope give `y=-2`. It meets the vertical axis at `(0,-2)` but cannot meet `y=0`; the lines are parallel and distinct. Consequently the three lines do not close a bounded triangle. The alternative polynomial derivative `3x²-3` agrees at 1, and the explanation identifies exactly which intercept condition made P11 different. Return to P23 is coherent.

### P23–P28: physical model, average and local velocity, endpoint and units

**P23.** Height 400 feet, zero initial velocity, upward-positive coordinate, constant acceleration `-32 ft/s²`, and neglected resistance are declared model premises. B6's constant-acceleration rule gives `400+0·t+(1/2)(-32)t²=400-16t²`. The explicit unitful form makes each term a length; the numerical version states its unit convention. No independently recalled gravitational constant, conversion or collision law is needed.

**P24.** The ground equation gives `t²=25`; B1/B3 give the two algebraic roots, and elapsed time after release selects 5 seconds. This is the first positive ground contact. Limiting the physical phase to release through that event is explicit.

**P25.** Average velocity uses final-minus-initial displacement `0-400=-400 ft` over `5 s`, giving `-80 ft/s`. Average speed uses distance `400 ft`, giving `80 ft/s`. That distance is available before P26: for `0≤t1<t2≤5`, `t2²>t1²`, so `400-16t²` decreases without reversal. B6 supplies the displacement/distance distinction. The explanation of reversals follows signed addition versus adding lengths; it does not require the external links. The claim about the source's wording remains a source-comparison claim rather than a premise in the motion calculation.

**P26.** B6 already identifies velocity with the time derivative; P19/P21 differentiate the quadratic to `-(32 ft/s²)t`, with units `ft/s`. For positive time the result is negative and thus downward. Independently expanding `(t+Δt)²-t²=2tΔt+(Δt)²`, multiplying by `-16` and dividing by nonzero `Δt` gives `-32t-16Δt`; its last term vanishes. Numerical-time conventions are stated, so the displayed quotient's appended `ft/s` is intelligible. The phase restriction keeps both positions within the same falling model. The finite two-sided derivative applies in the interior; endpoint velocities require the initial condition or the appropriate one-sided limit, not an unprovided continuation through a collision.

**P27.** Approaching 5 from below in `v(t)=-32t` gives `-160 ft/s`; taking magnitude gives speed 160. Alternatively at `t=5`, the allowed negative increments give `-160-16Δt→-160`. The new superscript minus notation is explicitly explained, and the text distinguishes this pre-impact limit from a two-sided derivative of the real collision motion. The speed rises from 0 to 160 through this fall, so its terminal value exceeding the computed average 80 is consistent with the actual model, not with an unqualified claim about every acceleration.

**P28.** Both conversion relations are supplied in the notes. Multiplying by `1 mile/5280 ft` and `3600 s/1 hour` multiplies by quantities equal to one and cancels feet and seconds. Arithmetic gives `160·3600/5280=1200/11≈109.1 mph`, and 110 is the coarser stated approximation. No absent table is required to reproduce it; independent checking of the cited tables was not undertaken.

### P29–P30: Attempt C and consolidation

**Availability at P29.** The new position is prescribed directly with time as a numerical value in seconds and output in metres on `[0,2]`; it is explicitly distinct from the preceding acceleration model. The stated down-then-up motion, B3's square function and B5's derivatives support the two legs. P25–P26 already distinguish interval quantities from a rate at an instant.

**P34 and P39.** The hint's positions are obtained by substitution: `z(0)=1`, `z(1)=0`, `z(2)=1` metres. The complete solution adds the two one-metre legs to obtain distance 2, while final-minus-initial displacement is zero. Over 2 seconds these give average speed 1 and average velocity 0 m/s. Expanding to `t²-2t+1` and using P19/P21 gives derivative `2t-2`; at 1.5 it is positive 1 m/s, hence upward velocity and speed of magnitude 1. The explanation connects cancellation of signed displacement to the difference of averages, rather than simply listing results. It returns to P30.

**P30.** The summary preserves what the construction differentiates, its input, the point or interval, and domain/phase. It generalises the algebraic quotient structure already taught at P04 and interpreted in B5; it does not introduce an unsupported law about a new subject.

### P31: later Attempt D, with its supplied help

**Availability at P31.** The requested revisit is an instruction about using this lesson, not evidence that recall or retention has occurred. Reopening is expressly permitted. For the changed function, P08/P21 provide the reciprocal and constant-multiple derivative, P10 the point-slope construction, and P11 the distinction between signed intercept coordinates and positive lengths. All needed content precedes the attempt.

**P35 and P40.** The hint maintains the two minus signs and contact height. The solution repeats the difference-quotient definition with nonzero increment, domain and interior two-sided finite-limit restrictions. Multiplying the reciprocal derivative by `-2` gives `g'(x)=2/x²`. Point-slope form through `(x0,-2/x0)` is `y+2/x0=(2/x0²)(x-x0)`, which expands to `y=2x/x0²-4/x0`. Setting `y=0` gives `x=2x0`, and setting `x=0` gives `y=-4/x0`; both are nonzero and their signs oppose for every admitted `x0`. B1's area rule with B3's absolute values gives `(1/2)|2x0||-4/x0|=4`, independent of nonzero `x0`. The final explanation correctly treats slope as a signed rate and area as a product of nonnegative lengths: a positive slope does not imply negative area.

### P32–P42: authored support group and document end

P32–P35 were read and checked individually with A–D above; their substitutions, prompts and domain/sign reminders introduce no missing prerequisite. P36 accurately separates hints from complete solutions. P37–P40 were read and checked in full, including their explanatory prose and return instructions, not only their answers. Their conclusions agree with the independently available earlier route.

P41 supplies source, instructor, licence and non-endorsement assertions with links. Those assertions cannot be independently checked under the two-input restriction. In particular, naming the course does not by itself independently verify any external bachelor-year eligibility requirement. This limitation does not remove a subject premise needed for the displayed mathematics. P42 describes claimed changes; the present document visibly contains domain restrictions, the remainder bound, positive-length geometry, endpoint scope and complete coordinate descriptions, so those present features can be assessed. Whether each is a change from an earlier source cannot be established without that source. No absent source artwork is necessary to reconstruct any of the stated geometry.

## Defects, provisional concerns and dependency status

**Established defects:** none found in the inspected subject-content route. There is no identified last-supported-point/failed-next-step pair to report, and no dependent result had to be accepted conditionally on an unsupported subject premise.

**Provisional instructional concerns:** none that presently establish a missing or invalid connection. Two potentially consequential points were explicitly resolved from the permitted text: P13's reflected tangent follows by swapping coordinates in P10 and comparing at the reflected input; P18–P19's remainder conclusion follows from the displayed uniform-in-`h` bound. Neither was granted merely because its final answer looked familiar. Endpoint scope was checked against P23–P27 rather than silently extending the real motion through impact.

**Independent-verification limitations:** the claims about source corrections, historical notation attribution, source course identity/year, unit-table provenance and licensing were not externally verified. Supplied numerical conversions and declared model assumptions were usable as supplied premises. No conclusion about a real falling object's drag, collision or subsequent motion is established by this ideal model. No inference about a person's competence or successful learning follows from this reading.

The bounded result is that this frozen document supplies an accessible and correct connected route for the stated baseline and its own declared conditions. That judgement rests on the reconstruction witnesses above and remains limited to the two exact inputs inspected.
