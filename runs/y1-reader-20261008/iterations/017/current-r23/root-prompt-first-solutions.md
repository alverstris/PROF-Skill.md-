D017 independent important answers — before authored teaching/solutions

Prompt-only packet read in tool 57bbb4. At this freeze, root has read the original source and selected actual baseline passages, but has not opened the author's learner notes, hints, solutions or answer evidence. These are independent technical answers, not SASIS or a claim of learner understanding. Later whole-route checks must establish that these warrants actually occur before use. The original proof record is preserved in GitHub commit 9cc7fc340efd8ccdad3518070126dcbf50322e68; this revision improves spacing without changing the mathematics.

P1

F′(x)=x⁵, continuous on [1,2], so the integral is F(2)−F(1)=(64−1)/6=21/2. Using F+7 adds 7 to each endpoint, which cancels. The integrand is unchanged because a constant has zero derivative.

P2

v=2t−2 changes from negative to positive at t=1. A primitive is H=t²−2t, with H(0)=0, H(1)=−1 and H(3)=3. Displacement is H(3)−H(0)=3 m. Distance is −[H(1)−H(0)]+[H(3)−H(1)]=1+4=5 m, the nonnegative odometer increment. The reverse oriented integral is −3 m by definition; this reorders mathematical limits rather than specifying a new chronological trajectory. Physical travel is from time 0 to 3. Units: (m/s)×s=m.

P3

The positive orientation from 0 to 2 permits integral comparison. The simpler integral is ∫₀²(1+t)dt=2+2=4, while ∫₀²eᵗdt=e²−1. Hence 4≤e²−1 and e²≥5. The reverse integrals give −4≥1−e². Multiplication by −1 reverses the inequality; retaining its forward direction after reversing endpoints would be an error.

P4

Set u=2−x², so du=−2x dx and x dx=−du/2. At x=0, u=2; at x=1, u=1. The entire integral becomes −(1/2)∫₂¹u⁴du=(1/2)∫₁²u⁴du=(32−1)/10=31/10. The original integrand is nonnegative on [0,1] and positive for x>0, so the positive answer is consistent. The direct antiderivative −(2−x²)⁵/10 differentiates to the original integrand and gives the same endpoint difference. No residual x is mixed with u.

P5a

For continuous f on [a,b], an antiderivative F continuous on the closed interval and differentiable in its interior with F′=f gives ∫ₐᵇf=F(b)−F(a). Reversed or equal endpoints use the oriented definition. For continuously differentiable u and continuous g on an interval containing u([a,b]), ∫ₐᵇg(u(t))u′(t)dt=∫ᵤ₍ₐ₎ᵘ₍ᵦ₎g(w)dw. The chain rule with G′=g proves the endpoint identity. Continuity and continuous differentiability are sufficient conditions, not claimed necessary. Monotonicity is not required for this composed-integrand form.

P5b

v=2t(t²−1) is zero at t=0 and t=1, negative on (0,1), and positive on (1,√2). The composite u=t²−1 pairs with du=2t dt, giving primitive H=(t²−1)²/2. Its values are H(0)=1/2, H(1)=0, H(√2)=1/2. Displacement is 0 m; distance is minus the first signed part plus the second, (1/2)+(1/2)=1 m. Split at the interior sign change t=1. The boundary zero t=0 requires no additional split. The expanded primitive t⁴/2−t² differs by a constant and corroborates the answer. Equal start and end positions mean zero net displacement, not zero travel. This is changed application and method selection, separate from retrieval in part (a).

Source-important cases

These were independently handled in root-source-review.md and root-source-calculations.json before this packet. All were checked against original equations and pages, including the substitution result 99757/15 and the qualified motion interpretation. These independent answers alone do not establish teaching acceptance.
