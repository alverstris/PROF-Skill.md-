# SASIS original reader report — frozen teaching v3

## Admission and access record

This evaluates the supplied document's connections and availability of premises, not the performance or learning of a human student. The subject-content inputs were exactly the complete frozen four-subject baseline and the complete frozen teaching document, including its four constituent figures. Retrieval was instruction-confined; this is not a claim that pretraining was erased or technically sandboxed. No source URL, other subject file, skill, author history, previous report, conversation memory or other agent's subject account was consulted. No external premise was used to repair the teaching.

All six supplied byte counts and SHA-256 digests matched:

| Input | Bytes | SHA-256 |
|---|---:|---|
| student-baseline.txt | 247840 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 |
| teaching-v3.md | 21983 | bcb390a295a8cce423b8ebfb9d292c45f7e6be3e37b9fbed1e33c6f60153f6fe |
| radar-v2.png | 25511 | a43e53adbb091799b2edd0adcaaf2ae350a70ece82f2d4813237dcc628b6e714 |
| cone.png | 52047 | 873e3697a025343f1944d61abf08605bc90475f358967cbf34f94c30fda3ecc6 |
| satellite.png | 20089 | b534b341aad1af8329c18dcda33b3efbfb8c2c87ee78c584864f0f98609d81e5 |
| mirror.png | 44150 | 3f64d89b89f284ec161d66de83da6b080bb42dd9ba2b074fb5e0e2667bdbc692 |

Text retrieval used `read_bytes().decode().split('\n')`, preserving internal CR characters rather than treating them as new physical lines. Actual baseline display order was 1–120, 121–240, 241–360, 361–480, 481–600, 601–720, 721–840, 841–960, 961–1080, 1081–1200, 1201–1320, 1321–1378. There are 1377 physical LF-terminated content lines; displayed entry 1378 is the terminal empty split item. No chunk output was truncated. The bounded retrievals do not mean all baseline bytes were simultaneously held in active context.

After the baseline, teaching retrieval was exactly: lines 1–13; full radar PNG; lines 14–59; full cone PNG; lines 60–97; full satellite PNG; lines 98–118; full mirror PNG; lines 119–164; lines 165–208. The teaching has 207 LF-terminated lines, with 208 the terminal empty item. Every image was viewed before retrieving the text after its insertion; no later teaching was displayed prematurely. All four full images, their labels, alt text and following captions were readable. No truncation required a corrective reread. The report was written only after this full reading and is the original report before feedback; inputs were not edited.

## Baseline coverage and available connections

The baseline was read in its entirety, including scope statements, practical material and final reference entries; reference links were not followed. These chronological witnesses identify what was actually available, without treating a topic name as a grant of an unstated rule.

- Cover and Mathematics, lines 1–341: quantities must retain domains and units; Pythagoras relates right-triangle lengths; similarity matches corresponding lengths; a cone has volume πr²h/3. The derivative is the limit of a difference quotient, and the supplied chain rule explicitly includes connected rates `dy/dt=(dy/dx)(dx/dt)`. Thus an expression such as x(t)² differentiates to 2xx′, while a fixed constant differentiates to zero. Product differentiation, implicit differentiation and the local inverse-rate condition are explicit. A signed one-dimensional velocity differs from its speed magnitude; component vectors support interpreting a distance-rate projection. Probability, statistical tests, sampling, kinematics and force laws were also read through their stated exclusions; none is needed to import a further related-rates rule.
- Further Mathematics, lines 345–501: complex and matrix operations, geometry, series, calculus, differential equations, statistics and mechanics were read with their conditions. Relevant confirmation comes from real-vector scalar products, a·b=|a||b|cos θ, dimensional consistency, and ordinary calculus operations; these can justify the radar's component interpretation without presupposing an unstated radar law. The selected baseline explicitly distinguishes supplied operations from unavailable multivariable or other university formalism. No such formalism is needed here.
- Physics, lines 505–786: constants and powered-unit conversions, graph gradients, uncertainties, practical methods, motion, energy, circuits, waves, thermal models, fields, astronomy and nuclear/imaging content were all read. The usable bridges are signed motion versus speed, a tangent's instantaneous rate versus a secant's average rate, and consistent lengths/time units. The baseline's actual Doppler and echo models are separate from the teaching's expressly assumed direct distance-rate radar. They do not silently replace that premise. The baseline distinguishes approximations and model conditions from universal laws.
- Chemistry, lines 790–1377: the quantities, structural and reaction rules, rates, equilibrium, acids, thermodynamics, electrochemistry, organic transformations, spectroscopy, practical reasoning and closing scope/reference material were all covered. For example, species-rate and coefficient-normalised reaction-rate conventions are distinguished, supporting attention to what a rate measures rather than equating every rate by name; dimensional reasoning and unit conversions are available. None supplies an additional needed premise for the teaching's geometric conclusions. Its provenance URLs and references to other records were not treated as accessible subject inputs.

The baseline is an explicit competence assumption, not an observed mastery claim. New model premises in the teaching may be accepted as premises without proving their independent empirical truth.

## Chronological teaching reconstruction

### P001–P006, then Figure 1 at line 13

P001–P002 identify the aim and intended reading/task order. The source attribution is a provenance assertion; no source verification is available from these two inputs. P003 defines prime as a time derivative, relates negative distance rate to shrinking separation, and identifies speed as a magnitude. P004 connects a geometry function D(x) to time through the already available chain rule. Its units multiply `(length/length)(length/time)` to length/time. Substitution of an instantaneous value before differentiation would instead create a constant function, so the stated sequencing follows from what a derivative differentiates.

P006 introduces fixed offset 30 ft, the positive road-side domain x>0, D=50 ft and D′=−80 ft/s. The direct distance-rate reading is an explicit model premise, not an unstated consequence of radar hardware. Figure 1 visibly places fixed radar above the road, a right-angle mark at the foot, x(t) horizontally to the car, D(t) on the slant, a 30 ft vertical leg and an approach arrow pointing toward the foot. These identify the corresponding lengths before the equation is used. The horizontal double arrow is a length marker; the separately labelled approach arrow identifies travel direction.

### P007–P016, including RR1, then Figure 2 at line 59

P007's right triangle yields 30²+x²=D² in the declared feet convention. P008 differentiates it to 2xx′=2DD′ and divides only for x≠0. P009 uses the positive root x=40 ft, making x′=(50/40)(−80)=−100 ft/s. P010 converts the speed limit using supplied conversion factors: 65×5280/3600=95⅓ ft/s. P011's comparison follows because 100>95⅓, irrespective of rounding the limit to 95.

The geometrical explanation in P011 has a reconstructible component meaning: the road direction's component along the radar-to-car line has magnitude x/D, so D′=(x/D)x′ has smaller magnitude for positive nonzero offset. At the closest point the text explicitly changes x from a positive-side distance to a signed coordinate. With finite x′, the undivided equation at x=0, D=30 imposes D′=0 but puts no condition forcing x′=0. The earlier divided formula is not extended to that point.

RR1 at P012 can already be reconstructed: unchanged geometry gives x=40, departure gives D′=+80, and 2xx′=2DD′ gives x′=+100 ft/s and speed 100 ft/s. Reversal changes the sign at the same geometry, not the magnitude. This uses the preceding teaching, not the later hint or solution.

P013–P014 differentiate D=(900+x²)^(1/2), giving D′=xx′/D, and alternatively x=(D²−900)^(1/2) on the positive branch. Both recover the same relation in the specified domain. The choice of shorter implicit differentiation is supported by the number of operations involved, not a new theorem. Freezing D at 50 would lose its time dependence.

P016 introduces the inverted cone's fixed 10 ft height and 4 ft top radius, horizontal water surface, no outflow, and time in minutes. The water's h, r and V vary. Figure 2 shows an apex-down cone with shaded smaller water cone, centre-to-edge radius arrows r and 4 ft, heights h and 10 ft, and a separate half-section with a right angle and corresponding horizontal sides. The centre-to-edge markings and half-section prevent a radius/diameter substitution. It is schematic; no numerical ratio was inferred from pixel measurements.

### P017–P026, including RR2, then Figure 3 at line 97

P017 pairs the two right triangles' shared apex angle and horizontal radii, giving r/h=4/10 and r=2h/5 for 0<h≤10. P018 substitutes into V=πr²h/3 to obtain V=4πh³/75. P019 differentiates, so V′=(4π/25)h²h′. At h=5 the coefficient is 4π ft²; with V′=2 ft³/min, P020 yields h′=1/(2π) ft/min, approximately 0.159.

P021 identifies the coefficient with πr², using the earlier r=2h/5. This is the derivative dV/dh, so its limiting volume-per-rise interpretation follows without needing a new integral formula. For constant positive inflow, h′ is proportional to 1/h² for h>0, explaining the decreasing rise rate as the cone widens. The exclusion of a finite initial rate at the ideal sharp point is consistent with the positive-inflow expression becoming unbounded as h tends to zero. It is not a formula evaluated by division at h=0.

P022's product-rule alternative gives V′=(π/3)(2rr′h+r²h′); substitution of r=2h/5 and r′=2h′/5 yields (4π/25)h²h′. Keeping r fixed would remove a genuine changing factor. P023 explicitly introduces stored-volume balance as a model premise: nonnegative inflow minus outflow, absent other volume changes.

RR2 at P024 supplies its leak law rather than requiring it to be inferred. Its equivalent k=(1/5) ft²/min makes kh a volume/time rate. At h=5 ft the leak is 1 ft³/min, so V′=1 and h′=1/(4π) ft/min. At every interior depth, 2−h/5>0 and the area coefficient is positive. Therefore the height rises throughout the interior, and zero net flow occurs only at h=10, excluded by the open interval. No falling or stationary interior depth follows. This reconstruction is available before hints and solutions.

P025–P026 shift from time rates to input sensitivity; the derivative definition already permits an independent variable other than time. Figure 3 visibly marks c on the vertical leg, L on the horizontal leg, h on the slant and a right angle, and labels h as slant distance/c as vertical separation. Those labels supply the meaning before the next paragraph; h need not retain its cone meaning.

### P027–P031, then Figure 4 at line 118

P027 explicitly resets h's meaning and fixes c>0. Pythagoras gives L²+c²=h² and L=√(h²−c²), selecting L>0 and thus h>c. Differentiation with respect to h gives 2L(dL/dh)=2h, so dL/dh=h/L. P028's derivative is dimensionless when both lengths use the same unit. The supplied difference-quotient limit connects this local derivative to ΔL≈(h/L)Δh for sufficiently small nonzero Δh at a fixed admissible point. This is an explained new application of the baseline limit definition, not an assumed finite-error equality.

P029 retains h>c and warns that large h/L near L=0 demands smaller input changes. Its alternative 2LL′=2hh′ requires fixed c; division by h′ additionally needs h′≠0. The measurement derivative does not need actual motion. P030's c=3, h=5 yields L=4 and sensitivity 5/4; it scales small changes, not the original distance. If c varies, the extra 2cc′ follows directly by the same chain rule.

P031 introduces only a schematic comparison of nearby angles and positions. Figure 4 shows a curved profile, two sloping blue paths from a common marked point to different profile positions, two vertical continuations, Δθ between the sloping paths, and horizontal Δa between the continuations. Its internal caption explicitly says schematic. I infer those displayed separations, not a focal point, reflection law, calibration equation, direction of propagation or an absolute coordinate convention absent from the input.

### P032–P044, including RR3, provenance, all hints and the start of solutions

P032 correctly limits what follows from the mirror figure: its two separations are visible, while a quantitative mirror relation and full absolute-coordinate definitions are absent. P033 states a conditional differentiable relation a=f(θ). Given that premise, da/dθ is the local position sensitivity; the reverse derivative is its reciprocal only with a differentiable local inverse and nonzero derivative. The chain rule product equal to one supplies the connection. Neither mirror numerical values nor orbital prediction is inferred. P034's reusable sequence accurately collects operations already demonstrated, including matching the independent variable and separating a local derivative from a finite-error approximation.

RR3 at P035 is reconstructible at its insertion. Part (a) starts with L=4 km and dL/dh=5/4, giving estimated change +0.0125 km, while the exact change is √(5.01²−3²)−4 km. The curved function need not equal its tangent's finite change. Part (b) differentiates all three lengths, giving L′=(hh′−cc′)/L=[5(0.2)−3(−0.1)]/4=0.325 km/s; omitting the changing c term would give 0.25 km/s. The task permits a calculator for the square root and the exact radical itself is available without one. The suggested break/next-day return is an optional study instruction; no efficacy or observed recall is claimed here.

P036 supplies source/scope assertions and labels generated practice and its leak law. Their historical fidelity cannot be independently checked under the input restriction. This does not remove the displayed geometry or model premises supporting the calculations. P037 and P041 separate hint and solution navigation. P038 points RR1 to the positive factors in the differentiated relation. P039 points RR2 to net volume rather than height rate and to the signs of its two factors. P040 gives the two-geometry radical difference and the additional 2cc′ term. All hints use already introduced relations; none supplies a prerequisite that was absent at its prompt. Links identify matching prompts/hints/solutions by visible anchors; navigation behaviour was not separately tested.

P042–P043 solve RR1 with x=40, D′=+80 and x′=+100, and correctly explain the speed/sign distinction. P044 begins RR2 by evaluating the leak as 1 and net stored rate as 1, then recalls the established cone relation. Its derivation continues across the retrieval boundary without a change of meaning.

### P044 continuation–P051 and actual ending

P044's displayed continuation gives h′=1/(4π) ft/min≈0.0796. P045 retains variable h in (4π/25)h²h′=2−h/5, expressly using numerical feet/minutes. P046 tests signs on 0<h<10, finds the sole zero numerator at 10, and excludes it from the interior. Treating V′ as 2 would ignore outgoing water and give a greater rise rate. This matches both the model premise and the prompt.

P047–P048 solve RR3(a): original L=4, tangent change 0.0125, exact new difference √16.1001−4≈0.01249299 km. P049's difference is about 0.00000701 km=0.00701 m, with the derivative estimate slightly larger. The original-point slope is being held constant in the estimate while the exact relation changes slope over the interval; the explanation does not assert a universal error bound.

P050 retains 2cc′ and obtains 0.325 km/s, with numerator units km²/s divided by km. P051 interprets the signs: hh′ is positive and −cc′ is positive when c′<0. With fixed slant length, reducing the squared vertical contribution must increase L², so the shrinking vertical leg contributes to increasing horizontal separation. The omitted-term comparison 0.25 km/s identifies a changed condition rather than rounding. The final return link and terminal empty split entry complete coverage; no unseen ending is presumed.

## Concerns, dependencies and limits

No substantive missing or invalid mathematical connection was found within the displayed teaching and declared models. The domains, changing/fixed distinctions, root choices, rate signs, units and approximation qualifications needed for its worked examples and three tasks are available before their use. No later passage was needed to retroactively repair an earlier reliance.

The limits remain consequential:

1. The radar result is conditional on direct measurement of D′, fixed geometry and the stated side/direction. Real hardware behaviour is not established. The closest-point result requires the explicitly extended signed coordinate and finite x′; the divided formula remains unavailable at x=0.
2. Cone results assume the described shape, horizontal level and stored-volume balance. The leak law is supplied, not derived or empirically validated. Neither an interior solution at the brim nor a finite divided-form height rate at the sharp point is justified. The text appropriately makes neither claim.
3. Satellite error propagation is local, with fixed c and h>c. It supplies no general error tolerance or uniform bound near L=0. The numerical RR3 comparison supports only that particular input change. Allowing c to change alters the differentiated relation, as the document explicitly demonstrates.
4. Mirror absolute coordinates, calibration and quantitative optical model are not provided. Numerical sensitivity therefore remains undetermined; only the stated conditional derivative/inverse connection is supported. The figure is adequate for the two marked separations, not for extracting additional optical physics.
5. Historical source fidelity, the independent scientific accuracy of introduced empirical models, rendered navigation and human usability/performance were not tested. Readable input and reconstructible argument do not establish measured learning, retention, assessment success or a grade.

There is no blocked dependent calculation among the requested tasks. The intentionally unsupported mirror numerical calculation and unverified provenance remain separate from the supported rates and sensitivity arguments. This report preserves those limits rather than filling them from familiarity.
