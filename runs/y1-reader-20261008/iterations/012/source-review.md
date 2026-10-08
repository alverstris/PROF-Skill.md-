# D012 source review

Mapping: D012 = MIT 18.01 Fall 2006, Lecture 13, Newton's Method and Other Applications. Review is SOURCE preparation only. All seven cached text pages were read and all seven 1224 by 1584 page renders were individually inspected, including all six figures and the numerical table. PDF page 1 is the cover; PDF pages 2-7 carry printed pages 1-6.

PDF: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L13/lec13.pdf
Official asset: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/fb8c24f09aba8413984f8ce5961586bd_lec13.pdf
SHA-256 recomputed: bf5673e95549bb93b6383c6be924baf315d4e0761d4f7e653744b1b87c8c8f65. Exact match to audit.json; 1,224,586 bytes, seven pages. No source content was inferred from the earlier readability verdict.

## Page coverage

| PDF page | Printed page | Content and visual inspection |
| --- | --- | --- |
| 1 | cover | MIT OCW course, term and terms notice; no mathematical content. |
| 2 | 1 | Newton tangent construction; x²-3 with x0=1; Figure 1 and all tangent equations inspected. |
| 3 | 2 | General first-step formula; Figure 2 shows second tangent and ordering x0 < root < x2 < x1; square-root recurrence inspected. |
| 4 | 3 | Entire iterate/error table; general recurrence; Figure 3 tangent intercept; proposed limit calculation. |
| 5 | 4 | Limit algebra, negative-root warning and Figure 4; nonconvergent two-cycle and Figure 5. |
| 6 | 5 | Ring geometry and Figure 6, length constraint, implicit derivative and stationary condition. |
| 7 | 6 | Equal angles/tensions, ellipse reflection interpretation, every step of x/y formula derivation, final Lagrange-multiplier remark. |

## Resolved mathematical witnesses

Newton's tangent equation gives x_(k+1)=x_k-f(x_k)/f'(x_k) whenever f is differentiable at x_k and f'(x_k) is nonzero. For f(x)=x²-3, this is (x_k+3/x_k)/2. Starting at 1 gives exactly 1, 2, 7/4, 97/56, 18817/10864; the displayed 7/8+6/7 equals 97/56. Corresponding absolute errors are approximately 0.7320508076, 0.2679491924, 0.01794919243, 0.00009204957398, and 2.445850247e-9. The displayed error magnitudes after x0 are coarse upper estimates, not exact errors; 3e-9 is a valid bound but not nearest one-significant-digit rounding.

Writing r=√3 gives x_(k+1)-r=(x_k-r)²/(2x_k). For x0>0, x1≥r by AM-GM, and thereafter r≤x_(k+1)≤x_k. Thus a positive limit exists, is nonzero, and the limit equation yields +√3. The negative start -1 gives the negatives of the positive iterates and hence -√3. Starting at zero is undefined. The statement about doubling digits describes local quadratic convergence at a simple root, not an unconditional property of Newton iterations. Figures 1-4 have the appropriate intercept order and tangent signs, but are schematic rather than metric plots.

The Figure 5 two-cycle mechanism is realizable: f(x)=(5x-x³)/2 has f(-1)=-2, f(1)=2 and f'(-1)=f'(1)=1, so Newton maps -1 to 1 and 1 to -1. This supports the body text and diagram, not its caption.

For the ring write r1=√(x²+y²), r2=√((x-a)²+(y-b)²), and s=√(L²-a²). Under the nondegenerate condition L>√(a²+b²), the source answer x=a(1-b/s)/2, y=(b-s)/2 is correct. It gives y<min(0,b), and, for a>0, 0<x<a. Here r1=L(s-b)/(2s)>0 and r2=L(s+b)/(2s)>0, so r1+r2=L and x/r1=(a-x)/r2=a/L. The implicit differentiation is correct and its denominators are nonzero at this point. Both depicted angles are acute for a>0, making sin α=sin β imply α=β. The vertical sum gives cos α=s/L, recovering y and then x.

Global minimality does not follow from stationarity alone, but has a short independent certificate: r1+r2≥||(x,-y)+(a-x,b-y)||=√(a²+(b-2y)²). Therefore y≥(b-s)/2. The displayed point attains equality, so it is the unique minimum for the nondegenerate ellipse. This also treats a=0 by continuity/direct substitution, although the drawn nondegenerate right triangles then collapse. Equal tensions plus the equal angles give zero horizontal force, and the upward component 2T cos α balances the ring's weight. The ellipse reflection claim uses angles to the normal, which is vertical at this lowest point.

## Confirmed source errors

1. PDF p3, printed p2: the first expanded Newton step has denominator 2x instead of 2x0. The formula before it and all subsequent recurrence formulas establish the correction.
2. PDF p4, printed p3: the table calls the iterate-value column y and its accuracy |y-√3|, despite y having already meant f(x). Values 1,2,7/4,... are x_k, not f(x_k); label them iterate value and |x_k-√3|.
3. PDF p5, printed p4: Figure 5's caption says convergence to an unexpected root. It actually depicts a nonconvergent two-cycle; the adjacent warning states this correctly.
4. PDF p6, printed p5: Figure 6 labels the right segment √[(a-x)²+(b-y²)]. The correct distance is √[(a-x)²+(b-y)²], as the length constraint and later algebra correctly use.
5. PDF p6, printed p5: the instruction asks for the position (x,y) of the string; the diagram, constraint and solution use the ring's position. This is an object-name typo, not a change to the mathematics.

## Missing conditions and pedagogical omissions

- The opening identifies √3 as the solution of x²-3=0 without restricting x positive. There are two roots. The later explicit negative-root warning resolves the intended positive target, so this is an initial scope omission rather than a packet-level wrong solution.
- General Newton iteration requires nonzero derivative and legal domain values at every step. Smoothness near a simple root and a sufficiently close start support local quadratic convergence; no universal convergence theorem is established. The warnings correctly preclude an unconditional interpretation. The limit passage itself needs existence and nonzero limit, supplied above for this example.
- The ring model tacitly uses a taut, inextensible string with negligible mass, a freely sliding frictionless ring, and straight string segments. These are conditions for the stated constraint and equilibrium model.
- L>√(a²+b²) is needed for the nondegenerate ellipse and this interior differentiable argument. For L<√(a²+b²) the feasible set is empty; for equality it is the line segment between the foci, whose minimum is min(0,b). If L=|a| and b=0, the formula divides by s=0 and must not be used. Diagram orientation assumes a>0 and depicts b>0; for the same a>0 formulas also work when b≤0 under the strict length condition.
- The whole ellipse is not a single global y(x); implicit y(x) is local on the lower branch near the minimum, where F_y=y/r1+(y-b)/r2<0. The source's local derivative argument is valid there. Endpoint comparison and physical intuition are not a full proof of the global minimum; the bound above closes this gap.

Open technical uncertainties: none. The identified errors are visible in the page renders; the missing conditions have explicit witnesses or boundary resolutions. No teaching audit, external record, or repository was edited.
