D003 lead independent pre-solution calculation

These calculations followed reading only author-work/task-prompts-before-solutions.md, before the proposed teaching or solutions or independent child checker answers. They are provisional until final prompts are compared. Prompt SHA256: 2a9cd44a0b13c88e7f95370e782f5cf28f74b924cb3f48cb7724d766a34fd39d. This is a technical author-side check, not SASIS and not a student test.

A: r′=2a′−b′=0.60−0.40=+0.20 V/s. Positive instantaneous rate; differentiability at one point alone need not imply monotonicity over a whole neighborhood. Prompt explicitly bounds “locally”.

B: A′=u′v+uv′=(−0.2)(4)+(3)(0.5)=+0.7 m²/s. Positive side u=3 m can be decreasing, so a negative increment is not a negative physical length. The exact corner contribution divided by h is (Δu/h)Δv. Differentiability supplies finite limit u′ and continuity supplies Δv→0, hence product→0. Mere ΔuΔv→0 is insufficient: a numerator |h| tends0 while |h|/h does not have zero two-sided limit. The counterexample only refutes the unsupported smallness implication, not the actual differentiable-rectangle conclusion.

C: On x≠1, q=x+1 and q′=1. Alternatively the quotient numerator is 2x(x−1)−(x²−1)=(x−1)². At x=1 q is undefined, so q′(1) does not exist. With Q(1)=2, Q equals x+1 for all real x and [Q(1+h)−Q(1)]/h=1; Q′(1)=1. A simplified formula does not extend the original function unless that extension is defined.

D: At a fixed point where u,v are differentiable, (u+v)′=u′+v′, (cu)′=cu′ for a fixed constant c, (uv)′=u′v+uv′, (u/v)′=(u′v−uv′)/v² when v≠0. With radians, sin′=cos and cos′=−sin. Exact increment: Δ(uv)=uΔv+vΔu+ΔuΔv. Divide by h and use finite difference-quotient limits plus continuity to remove only the last term in the limit. Raw product equality has the cross term, not approximate omission.

E: F domain is R excluding (2k+1)π, k integer; G domain excludes every kπ. On their common domain, sin²x=(1−cosx)(1+cosx) establishes equality. Quotient rule gives F′=[cosx(1+cosx)+sin²x]/(1+cosx)²=1/(1+cosx), valid on F's domain. F′(π/3)=2/3; F′(0)=1/2. G(0) is undefined, so [G(h)−G(0)]/h cannot be used. Legitimate alternative: one may replace F(h) by G(h) for sufficiently small nonzero h while retaining the actual F(0)=0; this is still F's difference quotient, not the derivative of undefined-at0 G. Final wording should distinguish whole-function replacement from this valid partial substitution, rather than banning all uses of G near0.

No source conclusion is inferred from a numerical approximation. Final proof-route accessibility remains to be read in the actual teaching and independently by fresh SASIS.
