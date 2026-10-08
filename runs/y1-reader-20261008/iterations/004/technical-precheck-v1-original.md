# D004 technical precheck v1: original source and independent task solutions

Status: COMPLETE. Independent pre-solution check performed before seeing any authored solutions, teaching output, reader output, or earlier iteration artifact. The review read the complete four supplied text files and visually inspected all four full-page PNGs. No SASIS was dispatched, and no global state was changed.

## Source identity and scope

- Original: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L04/lec4.pdf
- SHA-256 measured with sha256sum: df83eb89d84220591c909921a5c6a0529e77a661f913009f57741d8220d885d6
- Required SHA-256: identical.
- pdfinfo reports 4 pages, 612 by 792 points, 308895 bytes.
- Text files read in full: lec4-p01.txt, lec4-p02.txt, lec4-p03.txt, lec4-p04.txt in the same source directory.
- Full-page images inspected: lec4-p01.png, lec4-p02.png, lec4-p03.png, lec4-p04.png in the same source directory.
- PDF skill read in full and applied read-only. No PDF creation or editing was performed.
- Physical page 1 is the MIT OpenCourseWare cover. Physical pages 2, 3, 4 are lecture pages numbered 1, 2, 3 respectively.

## Exact observations from the original

### Physical page 1: cover

The cover identifies MIT OpenCourseWare, 18.01 Single Variable Calculus, Fall 2006, with a Terms of Use/citation notice. It contains no calculus argument or exercise.

### Physical page 2 / lecture page 1

The page is headed Lecture 4, Sept. 14, 2006, 18.01 Fall 2006, and titled "Chain Rule, and Higher Derivatives."

1. The opening example uses y=f(x)=sin x and x=g(t)=t^2, hence y=f(g(t))=sin(t^2).
2. The increment setup uses x0=g(t0), y0=f(x0), and the identity Δy/Δt=(Δy/Δx)(Δx/Δt).
3. The text states that Δt tending to zero makes Δx tend to zero because of continuity, then presents dy/dt=(dy/dx)(dx/dt).
4. The worked derivative is d/dt sin(t^2)=2t cos(t^2). This is correct for every real t, with trigonometric arguments measured in radians.
5. The functional notation is d/dt f(g(t))=f'(g(t))g'(t), with the analogous x notation. The outer derivative must be evaluated at g(t), not at t.
6. The composition comparison uses f(x)=sin x and g(x)=x^2: (f∘g)(x)=sin(x^2), whereas (g∘f)(x)=sin^2(x). These are different functions, although they can agree at individual inputs. The noncommutativity statement should be read as "composition is not commutative in general"; it is not a claim that every possible pair fails to commute.

### Physical page 3 / lecture page 2

1. Figure 1 sends x through g, giving g(x), then through f, giving f(g(x)). This confirms rightmost/inner function first.
2. Example 2 sets u=1/x for y=cos(1/x). The outer derivative is -sin u and the inner derivative is -1/x^2. Their product is sin(1/x)/x^2. Both minus signs are essential. The result is correct for x≠0, in radians.
3. Example 3 differentiates x^(-n) by two compositions:
   - x^(-n)=(1/x)^n, so n(1/x)^(n-1)(-1/x^2)=-n x^(-n-1).
   - x^(-n)=1/(x^n), so (n x^(n-1))(-1/x^(2n))=-n x^(-n-1).
   Both derivations are correct for positive integer n and x≠0. The source does not explicitly state those hypotheses alongside the calculation. Extending n to arbitrary real numbers needs separate real-power definitions and domain restrictions; that extension is not established here.

### Physical page 4 / lecture page 3

1. Higher derivatives are defined as derivatives taken repeatedly, with (f')'=f''.
2. The notation table correctly matches f', f'', f''', f^(n) with Df, D^2f, D^3f, D^nf and the corresponding Leibniz notation. These are orders of differentiation, not powers of derivative values.
3. The displayed examples give Dx=1, D^2x^2=2, D^3x^3=6, and D^4x^4=24; all are correct.
4. The factorial definition n!=n(n-1)⋯2·1 is appropriate for positive integers.
5. The proof of D^n x^n=n! is valid: it starts at n=1 and obtains
   D^(n+1)x^(n+1)=D^n((n+1)x^n)=(n+1)D^n x^n=(n+1)n!=(n+1)!.
   The proof uses the ordinary power rule, repeated differentiation, and the constant-multiple rule. It does not infer the result solely from the first four cases.

## Technical issue: completing the chain-rule proof safely

The source's increment calculation is useful intuition, but the displayed ratio factorization is only defined when Δx≠0. Differentiability of g does not ensure that every nonzero Δt gives a nonzero Δx. A constant inner function is an immediate counterexample to that intermediate division; the chain rule itself remains correct.

Sufficient local hypotheses: g is differentiable at t0, f is differentiable at x0=g(t0), and the composition is defined for t near t0 (for example, both functions have appropriate open-neighborhood domains). Differentiability of g implies continuity at t0.

A proof that includes zero inner increments follows directly from the differentiability remainder. For k near zero, write

f(x0+k)-f(x0) = [f'(x0)+r(k)]k,

where r(k) tends to 0 as k tends to 0 and define r(0)=0. For k≠0 this is just the derivative remainder; for k=0 the equation is also true. Set h=t-t0 and k(h)=g(t0+h)-g(t0). For every nonzero h sufficiently close to zero,

[f(g(t0+h))-f(g(t0))]/h
= [f'(x0)+r(k(h))] [k(h)/h].

There is no division by k(h). Since k(h) tends to zero and k(h)/h tends to g'(t0), this expression tends to f'(x0)g'(t0). This proves the chain rule even if k(h)=0 along a sequence or for every h.

Additional hypotheses to make explicit in teaching:
- Standard derivatives of sin and cos here use radians. Degree-based functions introduce the conversion factor π/180.
- Reciprocal examples require x≠0; polynomial and sin/cos composition examples are defined for all real inputs.
- The chain rule requires the outer derivative at the actual inner value.
- Higher derivatives require enough differentiability in a neighborhood for each repeated derivative to exist; all functions in A, B, D, E, F are smooth on the real line.
- Positive-integer n is the scope for the stated factorial induction.

## Independent solutions of proposed tasks A-G

The following computations use only the task statements and the original mathematical material. They were completed before reviewing any authored solution.

### A. y=cos(t^2): derivative and slope at t=0

Let u(t)=t^2 and F(u)=cos u. Then u'(t)=2t and F'(u)=-sin u, so

y'(t)=F'(u(t))u'(t)=-2t sin(t^2).

At t=0:
- Inner value u(0)=0.
- Outer derivative evaluated at the inner value F'(u(0))=-sin 0=0.
- Inner derivative u'(0)=0.
- Slope y'(0)=0·0=0.

The point on the curve is (0,1); the tangent is horizontal. Neither a bare -sin(t) nor omission of the 2t factor is valid.

### B. H(x)=sin(x^2), K(x)=(sin x)^2

Let f(u)=sin u and g(u)=u^2.

H=f∘g: square first, then apply sine.
H'(x)=cos(x^2)·2x=2x cos(x^2).

K=g∘f: apply sine first, then square the result.
K'(x)=2 sin x·cos x.

The functions have different operation order and different formulas; sin(x^2) is not the same expression as sin^2 x. Their derivatives are also different functions. Equality at some inputs does not establish equality of the functions.

### C. Supplied values f(4)=7, f'(4)=-2, g(1)=4, g'(1)=3

For P(t)=f(g(t)),

P'(1)=f'(g(1))g'(1)=f'(4)·3=(-2)·3=-6.

The value P(1)=7 follows as well, but f(4)=7 is not needed to calculate the derivative.

For Q(t)=g(f(t)),

Q'(1)=g'(f(1))f'(1),

provided the relevant derivatives and composition exist. The given data do not determine this. In general one needs f(1), f'(1), and g' at the resulting input f(1), together with the needed domain/differentiability information. Knowing g'(1)=3 helps only if f(1)=1; that identity was not supplied. The data at f's input 4 cannot be silently moved to input 1.

### D. y=sin(t^2): second derivative and its value at 0

First y'(t)=2t cos(t^2). Apply the product rule to the two factors and the chain rule to the cosine factor:

y''(t)=2 cos(t^2)+(2t)[-sin(t^2)·2t]
      =2 cos(t^2)-4t^2 sin(t^2).

Therefore y''(0)=2·1-0=2.

A useful distinction is y'(0)=0 while y''(0)=2: zero first derivative at one point does not force the second derivative there to be zero.

### E. Prove D^n x^n=n! for positive integer n

Claim: for every integer n≥1 and every real x, D^n(x^n)=n!.

Base n=1: D(x)=1=1!.

Inductive hypothesis: for an arbitrary integer n≥1, assume D^n(x^n)=n! as an identity of functions.

Inductive step:

D^(n+1)(x^(n+1))
 =D^n(D(x^(n+1)))
 =D^n((n+1)x^n)
 =(n+1)D^n(x^n)
 =(n+1)n!
 =(n+1)!.

Thus the claim holds for all positive integers by induction. The constant (n+1) can pass through every one of the n differentiations. This proves a family of identities rather than differentiating a single equality at only one x.

### F. D^3((2x-1)^3), compared with (D((2x-1)^3))^3

Let p(x)=(2x-1)^3. Repeated differentiation gives

Dp=3(2x-1)^2·2=6(2x-1)^2,
D^2p=6·2(2x-1)·2=24(2x-1),
D^3p=24·2=48.

An independent expansion gives p(x)=8x^3-12x^2+6x-1, whose third derivative is also 48.

Cubing the first derivative gives instead

(Dp)^3=[6(2x-1)^2]^3=216(2x-1)^6.

These are different functions: at x=1/2 the third derivative is 48 and the cube of the first derivative is 0. D^3 means apply differentiation three times; it does not mean cube the result of one derivative.

### G. Constant inner function g(t)=5

For every h, Δg=g(t0+h)-g(t0)=0. Thus the factor Δy/Δg in the proposed quotient cancellation is undefined: it has denominator zero (and numerator zero when f(5) exists). One cannot justify a proof by canceling that denominator.

Nevertheless f(g(t))=f(5) is constant wherever it is defined, so its derivative is 0 directly from its difference quotient. If f is differentiable at 5, the chain rule also gives f'(5)g'(t)=f'(5)·0=0. In fact the composite is constant and differentiable even if f is merely defined at 5 and not differentiable there; in that weaker situation the usual chain-rule hypothesis is not met and the expression f'(5)·0 must not be written.

The remainder proof above handles the differentiable-outer case because it never divides by Δg.

## Findings and limits

- Verified: original derivative examples, composition order, higher-derivative notation, displayed factorial cases, and positive-integer induction.
- Required mathematical repair: replace or qualify the division-by-Δx argument so zero inner increments are covered.
- Required assumptions to surface: radians, reciprocal-domain exclusions, chain-rule differentiability at the correct points, and positive-integer scope for the induction.
- Proposed A-G tasks are mathematically coherent and have the independent solutions above. C is intentionally underdetermined for the reversed composition; G tests a proof gap without disproving the theorem.
- This is a technical source and pre-solution audit only. It does not assess the quality of any teaching artifact, learner response, readability result, or later authored solution, and none were inspected.

