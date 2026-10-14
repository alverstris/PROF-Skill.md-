Coverage and conventions for D008

Requested capability: construct, justify, use and interpret the complete original lecture's linear and quadratic approximations from the frozen four-subject baseline. All supplied original lecture content is required. Format: GitHub Markdown main route plus linked hints/solutions and local figures. No lecture subtopic is excluded. This is a generated teaching route, not a claim of the original exam's assessed scope.

One coherent state-tool topic d008 groups the connected lecture. Stable coverage items:

C01 — tangent as local approximation
Original PDF p.2 / printed p.1, Figure 1 and general formula.
Capability: build/read the tangent model at general x0; justify local use via derivative; choose easy basepoint.
Immediate premises: baseline Maths 104–116, 256–312.
Final: main.md lines 9–37; worked logarithm 39–65; figure tangent-log.png; Attempt A and Solution A.
The sketch's monotonic-error language is qualified, not copied as a theorem.

C02 — logarithm shifting and five first-degree models
Original PDF pp.2–3 / printed pp.1–2, Figure 2, all five formulas, sine/power proofs.
Capability: change variable to displacement; derive each model from value/slope; preserve radians, power real domain and fixed exponent.
Immediate premises: baseline Maths exp/log 236–248, derivatives 268–308, FM27.
Final: main.md lines 59–93 and sine-cosine-linear.png. Solutions A/B apply the substitutions.
All five formulas have actual value/slope explanations, including constant cosine.

C03 — algebraic composite and reciprocal shortcut
Original PDF pp.3–4 / printed pp.2–3, Example 2 and footnote.
Capability: rewrite e^(-2x)/sqrt(1+x), combine models, explain order truncation, read correct f'(0).
Immediate premises: C01/C02, powers and product rule.
Final: main.md lines 95–139; Attempt B and Solution B.
Both original long reciprocal route and direct -1/2 shortcut retained. Source +5/2 typo corrected by direct derivative.

C04 — power difference-quotient limit
Original PDF p.4 / printed p.3, Example 3.
Capability: obtain limit20 by derivative and by expansion, justify division with controlled error.
Immediate premises: C01/C02/C03, baseline limit/derivative and finite binomial.
Final: main.md lines 154–175. Attempt C later tests quadratic cancellation; F(c) changes function.
No arbitrary approximate equality is promoted to an exact limit.

C05 — Planet Quirk first correction and physical meaning
Original PDF pp.4–5 / printed pp.3–4, Example 4, Figure 3 and GPS remark.
Capability: interpret given law; define small dimensionless z; compute scale, sign, accumulated time and physical-model scope.
Immediate premises: C02, baseline units/time/light speed. Relativity law is introduced, not presupposed from baseline.
Final: main.md lines 177–230, clock-intervals.png. Attempt D changes speed/tolerance.
Source missing T and incorrect reminder exponent corrected. GPS statement checked with R2, limited to motion contribution.

C06 — general quadratic model and factor1/2
Original PDF p.5 / printed p.4, formula and exact quadratic illustration.
Capability: construct/read value-slope-second-derivative matching at general x0 and justify coefficient; state usable sufficient smoothness condition.
Immediate premises: derivatives, polynomial algebra, baseline FTC.
Final: main.md lines 232–269. Shifted example lines 438–474 makes general form concrete; Attempt E changes representation to quantities with units.
Local match distinguished from least-squares fitting. Continuous second derivative meaning and error-warrant supplied before applications depend on it.

C07 — cosine picture and all five quadratic formulas
Original PDF pp.5–6 / printed pp.4–5, Figure 4, list and logarithm proof.
Capability: compute three derivatives at0, interpret curvature and zero square coefficient, reconstruct all five models.
Immediate premises: C06, baseline derivatives and FM27.
Final: main.md lines 271–342, cosine-quadratic.png. Attempt F(a,d) later distinguishes recall and degenerate cases.
Sine degree-two polynomial remains linear; model degree does not force a nonzero coefficient.

C08 — quadratic composite
Original PDF p.7 / printed p.6, Example5.
Capability: substitute inside square, retain every degree-two contribution, infer f''(0), discard unjustified higher-degree products.
Immediate premises: C03/C06/C07.
Final: main.md lines 344–378. Attempt C/Solution C and changed H example F(b,c)/Solution F.
Exact coefficient27/8 verified by independent differentiation, not only repeated expansion.

C09 — clock's quadratic term and precision decision
Original PDF pp.6–7 / printed pp.5–6, binomial substitution and 10^-20 remark.
Capability: distinguish quadratic z from quartic speed ratio, compare same-unit corrections and tolerances, handle v=0, identify failure at high speed.
Immediate premises: C05/C07, units and ratios.
Final: main.md lines 394–436; Solution D.
Term sizes independently computed. Original atomic-clock assertion addressed as dated/contextual via R3, not omitted or accepted as universal.

C10 — full lecture integration, changed application and revisit
General x0 formulas and requested understanding/justification/use.
Capability: select basepoint/order, carry dimensions, preserve error after cancellation, compare exact/approximate/degenerate cases.
Final: main.md lines 438–532; Attempts E/F, hints E/F and complete solutions E/F.
Generated square-root and sensor examples extend use of the lecture's own formulas; no extra companion subject introduced.

Course conventions
x0 is fixed basepoint; x varies; h=x-x0 is signed displacement. u is each whole substituted small input. z=(v/c)^2 is the clock expansion variable. Coefficient r is fixed real exponent with 1+u>0 sufficient local real domain. Trig inputs radians. L and Q denote exact polynomials; f≈L/Q estimates original function. Every power/form change is mapped back. Units in example E are explicit. T and T' remain in the original lecture's assignment, clarified as proper/local interval versus inertial ground-frame coordinate interval.

Baseline and scope limits
Course completion is a supplied competence assumption, not observed mastery. Full baseline was read; operations already supplied are compressed. No formal epsilon-delta analysis, infinite-series convergence proof, or full relativistic theory is assumed/added. The local quadratic remainder is established with the supplied FTC and a stated continuous-second-derivative condition. No pending user convention question or source access dependency remains.
