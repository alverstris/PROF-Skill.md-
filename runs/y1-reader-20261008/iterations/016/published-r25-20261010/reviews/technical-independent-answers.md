D016 r25 independent answers, preserved before inspection of teaching, hints or supplied solutions

Input: author/prompts-only.md, complete P1–P6. Also inspected original lecture and baseline premises. This is an independent technical calculation, not a learner attempt or human outcome.

P1. Width 1/2. Right endpoints 1/2, 1, 3/2, 2. R4=(1/2)[(1/2)^2+1^2+(3/2)^2+2^2]=15/4. L4=(1/2)[0^2+(1/2)^2+1^2+(3/2)^2]=7/4. x² increases on [0,2], so left rectangles lie below the graph and right rectangles above it; 7/4 ≤ area ≤ 15/4. Independent exact area 8/3 lies in that interval.

P2. Let z be height from bottom. For 2j<z<2(j+1), j=0,...,n-1, staircase section is a centred square of side n-j. Inner pyramid: base side n, perpendicular height 2n; its section side n-z/2 lies in [n-j-1,n-j], so is contained. Outer pyramid: base side n+1, height 2(n+1); section side n+1-z/2 lies in [n-j,n-j+1] on the same slab, so contains the staircase. At horizontal faces the closed solids preserve containment. Thus (2/3)n³ ≤ Vn ≤ (2/3)(n+1)³ and 2/3 ≤ Vn/n³ ≤ (2/3)(1+1/n)³ → 2/3. Changing only slab thickness stretches the vertical coordinate by 2; horizontal square sides remain unchanged, so heights, not base sides, double. Exact check Vn=2 Σk²=n(n+1)(2n+1)/3.

P3. Δx=2/n, xi=1+2i/n, g(xi)=-1+4i/n. Rn=(2/n)Σ[-1+4i/n]=(2/n)[-n+2(n+1)]=2+4/n →2. Root at x=3/2. Below-axis triangle has base 1/2, height 1, area 1/4; above-axis triangle has base 3/2, height 3, area 9/4. Signed integral 9/4−1/4=2; total geometric area 9/4+1/4=5/2.

P4. A(b)=[x²+x]1^b=b²+b−2. A(1)=0; dA/db=2b+1. x is bound integration variable; b is a variable upper endpoint and argument of A. Average on [1,3] is A(3)/2=10/2=5: height 5 on width 2 gives the same area 10.

P5. Principal 24000·(1/2)=12000 dollars. Simple interest I=.06·24000∫0^(1/2)(1−t)dt=1440(1/2−1/8)=540 dollars. Debt 12540 dollars. Constant 12000/year: principal 12000, interest .06·12000∫0^1(1−t)dt=360, debt 12360 dollars. Early borrowing adds 180 dollars because the same dollars are held longer on average (3/4 year versus 1/2 year).

P6. Principal B=∫0²6000(1+t)dt=24000 dollars. Average rate B/(2 years)=12000 dollars/year. Debt D=∫0²6000(1+t)[1+.10(2−t)]dt. Expand (1+t)(1.2−.1t)=1.2+1.1t−.1t²; D=6000[1.2t+.55t²−t³/30]0²=26000 dollars. Interest 2000 dollars. Multiplying principal by 1.20 gives 28800 dollars and incorrectly applies two full years of interest to every dollar; actual remaining times range from 2 to 0 years. Weighted mean remaining time is 5/6 year, consistent with 24000·.10·(5/6)=2000.
