D016 r25 independent prompt calculations

Root read only author/prompts-only.md from the fresh packet before deriving these results. No generated lesson, hint or proposed solution was read. Source notes were independently inspected earlier. Results are withheld from the author until the complete generation is frozen.

P1

Width is 1/2. Right endpoints are 1/2, 1, 3/2, 2; right rectangle contributions are 1/8, 1/2, 9/8, 2, summing to 15/4. Left endpoints are 0, 1/2, 1, 3/2; contributions are 0, 1/8, 1/2, 9/8, summing to 7/4. The exact area lies between 7/4 and 15/4 because x squared increases on this nonnegative interval, so each left height bounds the curve below and each right height bounds it above on the same subinterval. Independent optional check: the exact area 8/3 lies inside.

P2

At height z in [2k,2(k+1)], k=0,...,n−1, the staircase has square side n−k. An inner square pyramid has base side n and perpendicular height 2n, with cross-section side n−z/2. An outer pyramid has base side n+1 and perpendicular height 2(n+1), with side n+1−z/2. The first side is at most n−k and the second at least n−k throughout that slab. Thus (2/3)n cubed < V_n < (2/3)(n+1) cubed, and 2/3 < V_n/n cubed < (2/3)(1+1/n) cubed. Both limits are 2/3. Doubling slab thickness stretches all vertical dimensions, including the bounding pyramid heights, by 2; retaining height n would be an incorrect geometric comparison.

P3

Width is 2/n; right sample is 1+2i/n; its height is −1+4i/n. Therefore R_n = (2/n) sum(−1+4i/n) = −2 + (8/n squared)n(n+1)/2 = 2+4/n, whose limit is 2. The graph crosses at x=3/2. The negative triangular area is (1/2)(1/2)(1)=1/4; positive triangular area is (1/2)(3/2)(3)=9/4. Signed total is 9/4−1/4=2; geometric area is 9/4+1/4=5/2. Cancellation removes twice the negative-area magnitude from the geometric total.

P4

A(b)=b squared+b−2=(b−1)(b+2), with A(1)=0 and derivative 2b+1. One can obtain this area geometrically as a trapezoid with width b−1 and heights 3 and 2b+1, or by integrating the polynomial. x is the bound integration variable, while b is the varying upper endpoint that parametrizes the whole area. On [1,3], area is 10 and width is 2, so the average value is 5. A rectangle of height 5 and width 2 has the same area 10.

P5

Principal is 24000 times 1/2 = 12000 dollars. Interest is 24000(0.06) times integral from 0 to 1/2 of (1−t)dt = 1440(3/8) = 540 dollars. Debt is 12540 dollars. Uniform borrowing at 12000 dollars/year yields principal 12000, interest 12000(0.06)(1/2)=360, and debt 12360. The early borrowing schedule costs 180 more because its average dollar is borrowed at time 1/4 rather than 1/2, and therefore accrues interest for an additional quarter year. The hypotheses specify continuous borrowing and simple interest, so this is not the discrete month-end model.

P6

Principal is integral from 0 to 2 of 6000(1+t)dt = 24000 dollars. Dividing by the two-year duration gives average rate 12000 dollars/year. Final debt is integral from 0 to 2 of 6000(1+t)[1+0.10(2−t)]dt. The time-left term is 2−t years: the length of time that a dollar borrowed at t accrues simple interest before the common final time. The interest part is 600 times integral from 0 to 2 of (2+t−t squared)dt = 600(10/3)=2000 dollars, so debt is 26000 dollars. Multiplying principal by 1.20 gives 28800 dollars, an overestimate of 2800, because it incorrectly treats all borrowing as occurring at the start and accruing interest for two full years. Here the amount-weighted average age of the loans is 5/6 year.

These calculations establish independent proposed answers, not that the new lesson supplies an accessible route to them. That comparison must wait until its exact generation is frozen.
