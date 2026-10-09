D007 independent fixed-prompt calculation before any proposed solutions

Input: author-work-r13/task-prompts-original.md SHA25693bed04239828e9206d1e77722ad6c0c28d6644288f3a39a8f6270afafac5978. Root read only these exact seven prompts, original lecture sources and actual baseline/controls; no author teaching, hints, proposed answers or reader report has been opened. Calculations below were made independently and must remain unedited after comparison.

Q1

Subtracting the two supplied exponential definitions gives H(x)=exp(-2x). Therefore H'=-2exp(-2x), strictly negative for every realx, so H is decreasing. Directly applying chain rule to the hyperbolic expression gives2sinh(2x)-2cosh(2x)=-2H(x), the same result. The factor2 is indispensable in both routes; a cancellation of e^(2x) does not remove the inner derivative.

Q2

F is an outer product; first apply product rule. F'=2x sin(3x)+3(x²+1)cos(3x). G is an outer quotient; first apply quotient rule (or explicitly equivalent multiplication by reciprocal). G'=[3(x²+1)cos(3x)-2x sin(3x)]/(x²+1)². In each case the factor3 comes from differentiating the argument3x in sine. Both functions and derivatives have real domainR because x²+1 is always positive. The quotient minus sign and squared denominator cannot be borrowed from the product expression.

Q3

Under the specified local differentiability,2x+2y y'=0 gives y'=-x/y wheny≠0. At(1,2) slope=-1/2; at(1,-2) slope=+1/2. A curve can have different local branches; the ordinate enters the derivative, so a common abscissa does not force equal slopes. Division fails at(√5,0) and(-√5,0). That failure alone only says this divided expression cannot be used there; it is not, by itself, proof of a vertical tangent or nondifferentiability. Additional analysis is possible in this particular case: a hypothetical finite derivative in the original differentiated identity would imply2x=0, contradicting x=±√5; circle geometry/parameterization separately identifies vertical tangents. An answer clearly separating that further reasoning from mere division failure is acceptable. The prompt does not require a general implicit-function theorem or proving the supplied local branches.

Q4

For x∈(-1,1), the given branch has y∈(0,π), so siny>0. Cosine is strictly decreasing there with nonzero derivative, and the inverse-rate rule on this actual local inverse gives -sin(y)y'=1. Because sin²y=1-x², the positive sine is√(1-x²), yielding y'=-1/√(1-x²). Finite derivative domain is(-1,1); arccos is real on[-1,1] but endpoints do not have finite derivative. The minus sign follows the decreasing cosine branch. Principal arcsin uses an increasing sine branch with positive cosine and hence positive reciprocal derivative. This sign is not an arbitrary square-root convention. A derivation must justify the nonzero/positive sine and the local inverse conditions, not silently identify inverse notation with a reciprocal function.

Q5

For h≠0, [cos(x+h)-cosx]/h = cosx[(cosh-1)/h]-sinx[(sinh)/h], where cosh/sinh in this displayed sentence denote cos(h)/sin(h), not the hyperbolic functions. In unambiguous notation: cos(x)[(cos(h)-1)/h]-sin(x)[sin(h)/h]. The fixed factorscos(x),sin(x) can be taken outside the h-limit. The supplied radian limits are0 and1, so the derivative is-sin(x), for every realx. There is no invocation of the desired derivative as a known rule. Keep trigonometric parentheses visible to avoid collision with the newly taught hyperbolic names.

Q6

Let r=√2, a positive constant. On x>0, f=exp(r ln x), so f'=exp(r ln x)r/x=r x^(r-1). Its base varies and its exponent is fixed. The second expression is g=exp(x ln r), so g'=exp(x ln r)ln r=r^x ln r. Its base is fixed and exponent varies. ln r=(ln2)/2 is constant; using the ordinary power template on r^x loses the correct varying argument. Atx=1 the derivatives differ:√2 versus√2 ln(√2). Both formulas are valid on the requested positive interval; the fixed-base second function also extends to all realx, but no extension is needed to answer the supplied task.

Q7

(a) Principal arcsin has y∈[-π/2,π/2]. For interior inputsx∈(-1,1), cosy>0 and cosy=√(1-x²). Differentiating siny=x with the local inverse/nonzero derivative gives cosy y'=1, hence y'=1/√(1-x²), finite only on the open interval. The square-root sign follows that branch, not an unexplained absolute-value deletion.

(b) J=E/D with E=exp(u),u=x arctan(x),D=1+x². Choose the outer quotient rule, while u'=arctan(x)+x/(1+x²) by product and chain/inverse-tangent derivative. Thus J'={exp(u)[arctan(x)+x/D]D-exp(u)2x}/D² = exp(x arctan(x))[(1+x²)arctan(x)-x]/(1+x²)². Domain is all realx since D>0 and exp/arctan are defined there. An unsimplified form preserving both numerator derivative and denominator derivative is equally correct. Checking onlyx=0 would be nondiscriminating because several missing terms vanish there; numerical checks below use nonzero arguments.

Independent mathematical disposition of prompts

All incidental data/branches and domain restrictions are supplied. Each task has a determinate supported mathematical target; no private course decision is required. Q3 explicitly distinguishes formula failure from a geometrical inference. Q4 introduces a stated new inverse branch as a meaningful change. Q5 is a source-derived reasoning request, while the other six are labelled generated. This mathematical prompt check does not establish that the still-unread teaching makes every route available before the task. That requires the later complete document review and fresh SASIS.
