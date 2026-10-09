D014 independent prompt-first presolutions

Root read only the frozen prompts-only-v1.md for this comparison, after independent source/baseline-targeted review. No authored lesson or solution was opened before these results were saved. These are technical reviewer calculations, not SASIS or measured learner performance.

P1. Base value9 and derivative6; dx=−1/10 gives exact differential dy=−3/5. Tangent estimate9−3/5=42/5=8.4. Actual new value(29/10)²=841/100=8.41, so exact Δy=−59/100=−0.59. Expanding(3+h)²−9=6h+h² shows Δy−dy=h²=1/100. The definition dy=f′(3)dx is exact, and the linear estimate of the nonlinear function is approximate. Both changes are negative but unequal.

P2. h=63.7−64=−3/10 and derivative at64 is1/48, so dy=−1/160. Tangent estimate4−1/160=639/160=3.99375. Factorization is exact: (63.7)^(1/3)=4(1−3/640)^(1/3). Applying the first-order binomial approximation at relative perturbation u=−3/640 gives4[1+(1/3)(−3/640)]=4−1/160. That truncation, or replacing the finite change by dy, is the approximation step. Negative perturbation is valid with positive radicand, and|u|<1; no exact equality to the tangent value is asserted.

P3. Domain is(−∞,0)∪(0,∞), not an interval. A comparison between−1and1 cannot apply the interval theorem because0is absent. H is separately constant0and5 on the two components, satisfying the valid per-interval conclusion. No contradiction.

P4. Let u=x³+2, du=3x²dx, so x²dx=du/3. A primitive is u⁶/18+C. At0 its unadjusted value is64/18=32/9; F(0)=0 gives C=−32/9. Thus F(x)=[(x³+2)⁶−64]/18, on all realx. Differentiation gives(6/18)(x³+2)⁵(3x²)=x²(x³+2)⁵, includingx0. The separate proposal has derivative[−1/2]e^(−x²)(−2x)=xe^(−x²). It does not recover e^(−x²) as a function: atx0the derivative is0whereas the proposed integrand is1. Agreement atx1would not validate an antiderivative identity.

P5. With u=lnx, du=dx/x, integrate u^(−2) to−u^(−1)+C. Thus F=−1/lnx+C, valid on the assigned interval(0,1), where lnxis negative but nonzero. Atx=e^(−1),−1/lnx=1, giving C=−1. Final F=−1/lnx−1. Derivative is (1/x)/(lnx)² as required, and the initial value is0. The same algebraic formula is real forx>0,x≠1, but the initial condition fixes its constant only on(0,1); an extension to(1,∞) may have an independent constant. A negative u is allowed for u^(−2) and−1/u; do not import a logarithm-domain restriction from a different integral.

P6. Atπ/2, A=1/2+C_A=0 so C_A=−1/2; B=0+C_B=0 so C_B=0. Therefore A=(sin²x−1)/2=−cos²x/2=B using sin²+cos²=1. Derivatives of both forms are sinxcosx on the real line. The unshifted representatives differ by1/2, hence the constants differ by the opposite1/2 to select the same function. Family equality is compatible with unequal numerical constants.

P7. (a) At1, ln1=0, f′1=1, dx=.04; exact differential.04 and tangent estimate ln1.04≈.04. The derivative's linearization need not equal the finite logarithm change. (b) J=sin(3x)/3+2; differentiation givescos(3x), andJ0=2, both exactly on the real line. (c) Real integrand domain is(0,1)∪(1,∞): xmust bepositiveandlnxnonzero. ln(lnx) is real only on(1,∞). Correct primitive ln|lnx|+C on each component: forx<1 it is ln(−lnx), whose derivative(−1/x)/(−lnx)=1/(xlnx); forx>1 it is ln(lnx), whose derivative is the same. Constants may be independently chosen on disconnected components. The absolute value preserves a positive logarithm argument without changing the required derivative; it does not define the original integrand atx1.

Comparison with authored answers and their prerequisite warrants remains pending. Every prompt must also be answerable at its actual position in the full teaching; correct reviewer calculations alone do not establish that route.
