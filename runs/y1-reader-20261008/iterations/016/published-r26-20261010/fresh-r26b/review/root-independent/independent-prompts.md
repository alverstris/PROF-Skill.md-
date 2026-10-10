D016 r26 — root's independent prompt solutions

Input: only author/prompts-only.md from /workspace/scratch/f9c0b7fc7e76/d016-r26b, plus root's previously inspected unchanged original source and mathematical reasoning. No r26 proposed teaching, hints, solutions or figures have been read. Results are withheld from the author until the complete generation is frozen. The identity/timestamp record is in independent-prompt-checks.json.

P1

Width is 1/2. Left samples are 0, 1/2, 1, 3/2, with heights 0, 1/4, 1, 9/4. Multiplying their sum by the common width gives (1/2)(0+1/4+1+9/4)=7/4. Since x² increases on [0,2], every left rectangle lies below the curve over its interval. This is an underestimate, with strict inequality on positive-width intervals. No antiderivative is needed for that comparison.

P2

R_n=(b³/n³) times the sum of i² for i=1,...,n, and L_n has the same factor times the sum of i² for i=0,...,n−1. Cancelling the common terms leaves (b³/n³)n²=b³/n. Thus L_n=R_n−b³/n has the same limiting value b³/3 as the given R_n. For a sample c_i in [(i−1)b/n,ib/n], monotonicity gives the corresponding left height ≤c_i²≤right height. Multiply by positive b/n and sum to obtain L_n≤S_n≤R_n. Squeezing therefore proves the same limit for every allowed sample selection, including selections that change with n. This conclusion concerns the equal partitions and allowed samples stated in the prompt; no arbitrary nonuniform-partition theorem is needed.

P3

The width is 3/n, right sample x_i=1+3i/n, and interval [1,4]. Since f(x_i)=1−3i/n, the sum is 3−9(n+1)/(2n)=−3/2−9/(2n), tending to −3/2. The zero at x=2 splits the picture into a positive triangle of area 1/2 on [1,2] and a negative contribution of magnitude 2 on [2,4]. Geometric area is therefore 5/2, while signed accumulation is 1/2−2=−3/2. Average value divides the signed total by width 3, giving −1/2. The mean is a signed height, and the geometric total adds both magnitudes. No physical unit for x was assigned.

P4

Principal P=integral from 0 to 1 of 12000t dt=6000 dollars. A short contribution at t is 12000t dt dollars; it remains outstanding for 1−t years. Under the stated simple-interest model its multiplier is 1+0.06(1−t). The debt is the integral of their product: 6000+720 times integral from 0 to 1 of (t−t²)dt=6000+120=6120 dollars.

Charging a full year on all principal gives 6000(1.06)=6360 dollars, over by 240, because most principal was borrowed later. The principal-weighted borrowing time is (integral t·12000t dt)/6000=2/3 year, so mean outstanding duration is 1/3 year and interest is 6000×0.06×1/3=120. Uniform borrowing at 6000 dollars/year has the same principal but mean outstanding duration 1/2 year, interest 180, and final debt 6180. It costs 60 dollars more because its principal is borrowed earlier on average.

P5

One short-interval contribution is approximately g(t_i)Δt=(3−t_i)Δt litres, with Δt measured in minutes. Net change is integral from 0 to 4 of (3−t)dt=12−8=4 litres. Adding the initial 10 gives final volume 14 litres. At t=3 the net flow changes sign. Inward volume is the triangle 3×3/2=9/2 litres and outward volume is 1×1/2=1/2 litre. Total crossing in either direction is their sum, 5 litres, equivalently the integral of |g|. Mean net flow is 4 litres / 4 minutes =1 litre/minute.

The four requests respectively require a signed integral, addition of the initial stock, integration of absolute flow, and division by duration. Their answers are therefore 4 litres, 14 litres, 5 litres and 1 litre/minute, not one unchanged integral. As a physical consistency check, volume increases from 10 to 14.5 litres by minute 3 and then falls to 14, so the model never empties the tank; sufficient capacity is explicitly assumed.

These independent calculations check answers and warrants, not whether the yet-unseen teaching makes those warrants available at each prompt. That separate question is reserved for the frozen-output review and new SASIS reader.
