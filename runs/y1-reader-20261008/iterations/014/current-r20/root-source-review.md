D014 independent root source and mathematics review

Actual source access

Fresh official MIT OCW18.01Fall2006Lecture15 PDF downloaded2026-10-09T14:44:28UTC:130496bytes, SHA25610c3dc97fa877d3ed97c5561b5082dca3006c632d85e58e01d059484ae455323. Root read all five complete extracted texts and individually viewed all five complete150%dpi page images, including cover and all equations. There are no original figures. The historical old-workspace empty page5 text is not used: the fresh extraction contains all1016characters and agrees with the visible page. Original historical records remain unchanged. source/download.json initially records semantic reading pending; this subsequent actual reading resolves that current work item without rewriting history.

Differentials and three approximation routes (printed1–2)

At fixed input a, choose dx=h and define dy=f′(a)h. This equality is exact; the actual finite change is Δy=f(a+h)−f(a). From the derivative definition, (Δy−dy)/h tends to0 as nonzero h tends to0. This supplies local approximation without identifying dy with every finite change or asserting an unexplained numerical error guarantee. The quotient dy/dx is valid for nonzero selected dx; both differentials are0 for dx0 but that ratio is then undefined. The derivative itself is still defined by its limit, not division by zero.

For the real cube root at64, f64=4 and f′64=1/48. At h1 the tangent value193/48 is approximate, not exact: cubing it gives65+577/110592. Direct high-precision root comparison gives an overestimate0.000107574744275357...; for h0.1 the tangent value1921/480 overestimates by0.000001084128523909.... Method2 factors64 and uses small parameter h/64, not a perturbation65. The normalized binomial approximation reproduces4+h/48. Method3 is the same tangent calculation expressed with differentials. The exact-equality signs in source methods1/3 are therefore actual errors. All three approaches and the64.1variant belong to coverage.

Antiderivatives and all six formulas (printed2)

F′=f defines an antiderivative; a family notation is not a unique function. On each appropriate interval, differentiate the listed representatives: −cos→sin; x^(n+1)/(n+1)→x^n with n≠−1 and real differentiability domain; ln|x|→1/x on either side of0; tan→sec² on intervals avoiding cosine zeros; arcsin→1/sqrt(1−x²) for−1<x<1; arctan→1/(1+x²) on the real line. Principal inverse trigonometric names are not reciprocals. For general real powers positive x is a sufficient domain, not an excuse to exclude legitimate integer/rational domains categorically.

The negative logarithm case is explicitly verified by ln|x|=ln(−x) and chain factors(−1)/(−x)=1/x forx<0. The source's label “Property2” should identify3. Differentiating an arbitrary additive constant gives0. The source's phrase “constant factor” in the uniqueness paragraph is wrong terminology: it is an additive constant. A multiplicative factor generally changes the derivative.

Uniqueness and substitution (printed3–4)

On a common interval, H=G−F has derivative0 when both derivatives equal f. For any two inputs in that interval the MVT gives H(b)−H(a)=H′(c)(b−a)=0, hence one constant. This cannot be assumed from a previous lecture: the current teaching must supply any needed theorem/corollary premise. On disconnected domains constants may differ between components. For ln|x|, add0 on the negative half-line and1 on the positive half-line to exhibit the missing global conclusion. No constant bridges an excluded singularity.

The actual source's six worked primitives are checked by independent differentiation in root-source-symbolic-checks.json. Respectively: (x⁴+2)⁶/24; sqrt(1+x²); e^(6x)/6; −e^(−x²)/2; sin²x/2 or−cos²x/2; ln|lnx|. Each includes an arbitrary additive constant on the chosen interval. The first four are valid for all realx; the first substitution does not require global invertibility of x⁴+2 or division by x³, and the derivative check coversx0. In example1 the source's intermediate evaluated primitive loses+C then equates to an arbitrary+C; keep the family or selected representative convention consistent. Substitution here is justified by the chain rule F(g(x))′=F′(g(x))g′(x), not an unexplained cancellation of infinitesimals.

The two trigonometric representatives differ by1/2. Equal families require shifting the constant; using the same numericalC does not make the two expressions identical. The printed derivation of their difference is correct and must remain explained.

For example6 the integrand1/(xlnx) has domain(0,1)∪(1,∞). The source only statesx>0 but omitsx1 and gives ln(lnx), which is not real on(0,1). Use ln|lnx|, or explicitly restrict tox>1; full stated coverage favors both valid components with separately permitted constants. Atx1/2 the integrand is finite−2/ln2 while ln(ln(1/2)) is not real. For0<x<1, derivative of ln(−lnx) is(−1/x)/(−lnx)=1/(xlnx). Forx>1 the positive-log branch has the same derivative. Both are independently verified; symbolic differentiation alone does not settle the real domain.

Primary corroboration and baseline scope

Root opened actual OpenStax CalculusVolume1 pages on2026-10-09. Section4.2 returned lines33–63 and147–229 supplying linearization, defined differentials and the finite-change distinction; only these relevant claims are used. Section4.10 actual lines36–54 and73–115 supply the antiderivative definition, interval-qualified Theorem4.14, logarithm branches and family notation. Section5.5 actual lines27–55 gives Theorem5.7 and its chain-rule proof; lines104–121 corroborate constant-factor adjustment. These are primary publisher passages actually read, not a claim to read every exercise/page. URLs:
https://openstax.org/books/calculus-volume-1/pages/4-2-linear-approximations-and-differentials
https://openstax.org/books/calculus-volume-1/pages/4-10-antiderivatives
https://openstax.org/books/calculus-volume-1/pages/5-5-substitution

Root targeted baseline access read physicalLF131–211 and actual search-returned lines97,107,409,413 (along with other search hits). Derivative definition, power/chain rules, tangent, concavity, family notation, elementary primitives and substitution are explicitly available; FM29 grants inverse-trig derivatives and domains. This is not a root whole-baseline reading. The fresh author must read the entire baseline. Neither baseline familiarity nor this review substitutes for teaching reconstruction of genuinely new notation/conditions.

Current issues are source/notation/domain corrections under existing PROF duties. No substantive skill amendment is established. Actual authored route, source coverage, prompt-first independent checks, full fresh SASIS, destination and final publication remain pending. This record is source preparation for the active iteration, not a closure or a teaching verdict.
