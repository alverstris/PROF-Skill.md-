Hints for Lecture 18

These hints provide a next step without giving the complete solution. Read only the item matching your attempt, then return to it. The [complete solutions](solutions.md) are in a separate file.

<a name="q1"></a>

Q1 hint

The width is the whole horizontal length divided by four. For the right sum, sample at one, two, three and four widths from zero. For the left sum, start at zero and stop one width before 2. Square the sample coordinates to get heights; multiply their sum by the common width. Compare a rectangle's flat top with the increasing curve inside its interval.

[Return to Q1](notes.md#q1) · [Q1 solution](solutions.md#q1)

<a name="q2"></a>

Q2 hint

The $`j`$th layer now occupies $`2j\le z\le2(j+1)`$ and still has side $`n-j`$. By similarity the inner pyramid's cross-section side is $`n-z/2`$, since its side falls from $`n`$ to zero over height $`2n`$. Compare this with the layer side and with the outer side $`n+1-z/2`$. The staircase volume includes the factor 2 from every layer's thickness.

[Return to Q2](notes.md#q2) · [Q2 solution](solutions.md#q2)

<a name="q3"></a>

Q3 hint

The interval does not start at zero: each right sample is “left boundary plus $`i`$ widths”. Substitute that entire coordinate into $`4-x`$ before multiplying by the width. The graph decreases, so its right-edge height is the smallest height in each interval. For a separate exact calculation, the region is a trapezium, or you can use an antiderivative of the linear function.

[Return to Q3](notes.md#q3) · [Q3 solution](solutions.md#q3)

<a name="q4"></a>

Q4 hint

Use an antiderivative of $`2x+1`$ at both endpoints. The lower-endpoint contribution is a fixed number. To explain the derivative, compare $`A(b+h)`$ with $`A(b)`$: the overlapping region cancels, leaving a strip near $`b`$. Divide that strip's area by its width $`h`$ before taking the limit.

[Return to Q4](notes.md#q4) · [Q4 solution](solutions.md#q4)

<a name="q5"></a>

Q5 hint

During a small time interval the principal is approximately $`24000t\Delta t`$. Its duration until settlement is $`1-t`$ years, so multiply this principal by $`1+0.06(1-t)`$ for its debt. Keep a separate integral for principal. For the comparison, decide whether this borrowing rate places more of the total early or late; equal principal totals alone do not guarantee equal interest.

[Return to Q5](notes.md#q5) · [Q5 solution](solutions.md#q5)

<a name="q6"></a>

Q6 hint

Solve $`2-t=0`$ to locate a possible reversal. A signed velocity integral lets the two directions cancel; distance adds their magnitudes. Divide each resulting total by the same three-second duration for its corresponding average. For the sum, the width is $`3/n`$ and the $`i`$th right sample is $`3i/n`$; evaluate velocity at that sample, then multiply by the width.

[Return to Q6](notes.md#q6) · [Q6 solution](solutions.md#q6)
