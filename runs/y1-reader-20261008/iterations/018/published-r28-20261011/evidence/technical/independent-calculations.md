# D018 / clean-r28 — independent prompt-only calculations

Status: Phase 1 complete. This is a correctness reviewer's independent solution record, written before viewing any proposed solution or teaching text.

## Input and scope

- Sole mathematical input: `/workspace/scratch/f9c0b7fc7e76/d018-clean-r28/work/prompts-only.md`.
- Observed input SHA256: `bfd16842bf9e8eb3ed3e11edf20b07ff73737d8445aafef387cefb6401f82d86`.
- SHA256 agrees with the value supplied in the assignment.
- Scope: all five exact exercise prompts Q1–Q5, including explanations, hypotheses, signs, and numerical-bound interpretation.
- No generated teaching, proposed solutions, source audits, earlier runs/history, or sibling outputs were read. No external sources or browser were used. Local Python arithmetic was used only to verify Q4 divisions and the corresponding unrounded-log values.
- This file records independent mathematics, not SASIS work and not a review of the unseen lecture or PROF implementation.

## Q1 — accumulated value versus local rate

The integrand is continuous everywhere, so differentiation of an accumulation integral gives

\[
A'(x)=x^2-1,\qquad A'(0)=-1.
\]

Zero-length limits give \(A(1)=0\). Direct evaluation gives

\[
A(x)=\left[\frac{t^3}{3}-t\right]_1^x
=\frac{x^3}{3}-x+\frac23,
\qquad A(0)=\frac23.
\]

Alternatively, \(A(0)=-\int_0^1(t^2-1)\,dt\). The forward integral is negative because \(t^2-1\le0\) on \([0,1]\), and reversing the limits changes its sign. Thus \(A(0)\) is positive. This is an accumulated, signed value relative to base point 1. In contrast, \(A'(0)=-1\) measures how that accumulated value changes locally as the upper endpoint increases through zero. A function can be positive at a point and decreasing there; the signs need not agree.

## Q2 — explicit one-sided differentiation at a jump

For \(x<0\), reversal gives

\[
B(x)=-\int_x^0 f(t)\,dt=-\int_x^0 1\,dt=x.
\]

The distinct value at the single endpoint \(t=0\) does not change the integral. For \(x\ge0\), \(B(x)=3x\), including \(B(0)=0\). Therefore

\[
\frac{B(0+h)-B(0)}h=
\begin{cases}1,&h<0,\\3,&h>0.\end{cases}
\]

The left derivative is 1 and the right derivative is 3. The two-sided derivative \(B'(0)\) does not exist, so the equality \(B'(0)=f(0)=3\) is false (its left side is undefined). The missing differentiation-FTC hypothesis is continuity of \(f\) at the point in question: \(f\) jumps at zero. Mere integrability does not guarantee differentiability of its accumulation function at every point. The conclusion here follows from the unequal one-sided quotients, rather than solely from the failure of a sufficient hypothesis.

## Q3 — two moving limits

Define one fixed-base accumulation function

\[
G(u)=\int_0^u e^{-t^2}\,dt.
\]

The integrand is continuous on the real line, so \(G'(u)=e^{-u^2}\). Additivity and reversed limits give

\[
H(x)=G(x^2)-G(-x).
\]

Differentiate each composition:

\[
\begin{aligned}
H'(x)
&=G'(x^2)(2x)-G'(-x)(-1)\\
&=2x e^{-(x^2)^2}+e^{-(-x)^2}\\
&=2x e^{-x^4}+e^{-x^2}.
\end{aligned}
\]

Here \(2x\) comes from the upper limit \(x^2\); the outer minus sign subtracts the lower-limit accumulation; and the lower limit's chain-rule derivative is \(-1\). Those last two minus signs produce a plus. The integrand evaluated at the upper limit is \(e^{-x^4}\), whereas at the lower limit it is \(e^{-x^2}\). The formula remains valid for all real \(x\), including where the order of endpoints reverses.

At zero, the limits coincide, so \(H(0)=0\). Substituting zero into the derivative gives \(H'(0)=1\). No elementary antiderivative is needed.

## Q4 — prime estimate and rectangle bounds

Exactly three decimal digits correspond to integers \(100\le n<1000\). The requested model estimate is

\[
I=\int_{100}^{1000}\frac{dt}{\ln t}.
\]

The continuous endpoint convention has no effect on the integral. On \([100,1000]\), \(\ln t\) is positive and increasing, so its reciprocal is positive and decreasing. Therefore

\[
\frac{1}{\ln1000}\le\frac1{\ln t}\le\frac{1}{\ln100},
\qquad
\frac{900}{\ln1000}\le I\le\frac{900}{\ln100}.
\]

The inequalities for the integral can also be made strict because the integrand is not constant on any interval of positive length.

Substitution of the prompt's rounded logarithms gives numerical rectangle values

\[
L\approx\frac{900}{6.908}=130.28372900984365,
\qquad
U\approx\frac{900}{4.605}=195.43973941368077.
\]

To the nearest integer, the lower and upper rectangle values are **130 and 195**, respectively. They should be described as the rounded values of the bounds, with the exact analytic inequality or unrounded approximations retained. Rounding an upper bound downward does not by itself prove \(I\le195\). If literal integer inequalities are wanted from the rectangles alone, outward rounding yields \(130<I<196\), rather than using 195 as a certified integer upper endpoint.

Precision note: the supplied logarithms are rounded. The exact analytic bounds use the true logarithms; their values are approximately 130.28834457097554 and 195.4325168564633, with the same nearest-integer labels. Treating the stipulated logs as computational inputs is appropriate for the requested numerical rounding, but the \(\approx\) sign must not be silently replaced by equality.

These inequalities bound \(I\), an integral used to model the prime count. No error bound connecting that model to the actual number of primes has been supplied. Consequently the rectangle inequalities do not certify bounds for the actual prime count. No prime-count table is needed.

## Q5 — recall and changed application

### Recall component

Use names as well as numbers so the two roles remain unambiguous:

1. **Antiderivative evaluation direction:** If \(f\) is continuous on \([a,b]\) and \(F\) is an antiderivative of \(f\) there, then \(\int_a^b f(t)\,dt=F(b)-F(a)\). More explicitly, one may assume \(F\) is continuous on the closed interval and differentiable on its interior, with \(F'=f\) there. Its role is to compute a definite integral from endpoint values of an antiderivative.
2. **Accumulation differentiation direction (called FTC2 in Q2):** If \(f\) is continuous on an interval containing fixed base point \(a\), and \(G(x)=\int_a^x f(t)\,dt\), then \(G'(x)=f(x)\) at interior points. Its role is to recover the integrand as the local rate of accumulation, and thereby construct an antiderivative. Locally, continuity at the differentiation point together with integrability on the needed intervals is sufficient; full interval continuity is a convenient standard statement.

The learner's later closed-notes recall attempt is a requested study action; an answer key can state what accurate recall would contain but cannot establish that the learner performed it.

### Changed application component

Let \(F(u)=\int_0^u f(t)\,dt\). Continuity of \(f\) on the real line gives \(F'=f\), and

\[
R(x)=F(2x)-F(x),\qquad R'(x)=2f(2x)-f(x).
\]

At \(x=2\),

\[
R'(2)=2f(4)-f(2)=2(3)-(-1)=\boxed7.
\]

In contrast, \(R(2)=\int_2^4f(t)\,dt\) depends on values throughout the interval, not just its endpoints. For a concrete pair of admissible continuous functions, take

\[
f_0(t)=2t-5,\qquad
f_1(t)=2t-5+(t-2)(t-4).
\]

Both are polynomials on the real line and both satisfy \(f_j(2)=-1\), \(f_j(4)=3\). Nevertheless,

\[
\int_2^4 f_0(t)\,dt
=\left[t^2-5t\right]_2^4=2,
\]

whereas, after the substitution \(u=t-2\),

\[
\int_2^4(t-2)(t-4)\,dt
=\int_0^2(u^2-2u)\,du
=\frac83-4=-\frac43.
\]

Thus \(\int_2^4f_1(t)\,dt=2/3\). The given data determine the derivative \(R'(2)=7\) but do not determine \(R(2)\). Stating the two FTC directions is recall; selecting and combining accumulation differentiation, the chain rule, and this insufficiency argument is application in a changed setting.

## Handoff boundary

The computations above are sealed as a prompt-only record for later comparison. No mathematical findings have been communicated to the author. Phase 2 must identify and hash the separately supplied immutable whole-generation files before assessing their technical, source, and PROF fidelity.
