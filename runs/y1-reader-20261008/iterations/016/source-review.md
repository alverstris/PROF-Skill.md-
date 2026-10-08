D016 source technical review

Definite integrals

Source: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/d1b3d809b6505825b5cde0cee823fa0f_lec18.pdf
Resource: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec18/
SHA-256: 3469042c0ca6aa75aa7e420b2bbf726228c31093aea11ddb2fc0044a4404fec0

Independently recomputed SHA-256 matches the audit. Read all 6 complete page text extractions and opened every original full-page render with view_image, including the cover. PDF page 1 is the unnumbered cover; PDF pages 2–6 are printed pages 1–5. The PDF skill was read and applied for read-only inspection. No unreadable portion. This preparation is source evidence only, not a teaching draft, PROF judgment, SASIS review, or lecture closure.

Page and figure coverage

PDF 1 / printed cover: MIT OCW course identity, Fall 2006 and terms/citation notice.
PDF 2 / printed 1: Area by rectangle sums and thin-rectangle limit; Example x² on [0,b], right endpoints ib/n and sum b³/n³ times sum i².
Figure 1(i),(ii): Positive curve above [a,b], gray area versus rectangle approximation; axes and endpoints read.
PDF 3 / printed 2: Right-endpoint rectangles for x²; Staircase pyramid layers n²,(n-1)²,...,1; Inner and outer pyramid volume bounds n³/3 < sum i² < (n+1)³/3.
Figure 2: Three upper rectangles under/around increasing x², labels a=0 and b.
Figure 3: n=4 nested square top view; staircase side view with green inner and red outer triangular profiles; side n indicated.
PDF 4 / printed 3: Squeeze limit for sum i²/n³; Integral/area of x and triangle b²/2; Derivative-of-area pattern A-prime(b)=f(b).
Figure 4: Right triangle below y=x, base b and height b.
PDF 5 / printed 4: General equal subdivision, arbitrary tags ci, summation notation and definite-integral limit; Simple-interest model P(1+rt); Borrowing rate f(t), monthly example and ti=i/12.
Figure 5: Single red rectangle with interior tag ci under positive y=f(x), endpoints a,b; tag lies in its own subinterval.
PDF 6 / printed 5: Monthly borrowed amount f(ti)Δt and continuous total integral; Remaining-time simple interest factor 1+r(1-ti); End-of-year amount owed integral from 0 to 1.

Findings and independent deductions

D016-E01 | confirmed_units_source_error | PDF 6 / printed 5 | Sentence below integral of f(t) from 0 to 1
The source says the total borrowed has units dollars per year.
The integral has units dollars.
f has units dollars/year and dt has units years, so their product and sum/integral have dollars.

D016-E02 | confirmed_geometric_terminology_error | PDF 3 / printed 2 | Inner prism and outer prism prose
The objects bounding the staircase are called prisms, while their volume formulas have factor 1/3 and their side profiles are triangular.
These are inner and outer square pyramids, not prisms.
A prism with constant cross section has base times height; a pyramid has one-third base times height. The displayed inequalities and diagram agree with pyramids.

D016-C01 | area_orientation_condition | PDF 2, 4, 5 / printed 1, 3, 4 | b arbitrary and area interpretation
The geometric construction calls b/n a length and the result b³/3 an area, with no explicit b>0 condition. General integral is called area without f≥0.
For these drawings take b>0, and for ordinary geometric area take a≤b and f≥0. Signed integrals extend to other signs/orientations; geometric area uses absolute values as needed.
If b<0 then b³/3<0 cannot be ordinary area. If f=-1 on [0,1], its integral is -1 while enclosed geometric area is 1.

D016-C02 | omitted_integrability_and_tag_condition | PDF 5 / printed 4 | General Picture and definition
The limit definition is stated without an existence or tag-independence hypothesis; ci must be in the ith subinterval, not arbitrarily anywhere in [a,b].
Assume f is Riemann integrable, e.g. continuous on [a,b], with ci∈[a+(i-1)Δx,a+iΔx]; require one common limit for every allowed tag choice.
For f=1 on rational inputs and 0 on irrational inputs, rational tags yield b-a and irrational tags yield 0, so no common Riemann integral exists. For continuous f, uniform continuity bounds tag discrepancies by (b-a)ωf(Δx)→0.

D016-G01 | stated_pattern_not_proved_theorem | PDF 4 / printed 3 | A-prime(b)=f(b)
The source says the area should satisfy the derivative identity after two examples. It is a motivated pattern, not a general proof here.
With continuous f at b, A(b+h)-A(b)=integral_b^(b+h) f and the difference quotient tends to f(b).
Subtract f(b) from the quotient; its magnitude is at most sup{|f(t)-f(b)|: |t-b|≤|h|}, which tends to zero. This is reviewer-derived supplementation.

D016-C03 | model_assumption | PDF 5, 6 / printed 4, 5 | Borrowing and owed-amount example
P(1+rt) and the final weighted integral use simple interest, a constant rate, no repayments and borrowing amounts accumulated independently. A fixed 12-month sum is followed by Δt→0 without changing its written upper index.
Interpret the monthly sum as one approximation; for the limit use n intervals, Δt=1/n, ti=i/n. The displayed interest formula is valid for the stated simple-interest model.
An amount f(t)dt borrowed at t is held 1-t years and grows to f(t)[1+r(1-t)]dt. Integration gives total. With f=12000 dollars/year and r=.06/year over one year, principal=12000 and interest=360, total=12360; this independent check is not source-displayed.

D016-S01 | reviewer_supplementary_sum_check | PDF 2, 3, 4 / printed 1, 2, 3 | Square-sum squeeze and linear example
The displayed bounds and limits are correct.
Independently verify via finite sums without relying on the geometric picture.
sum i²=n(n+1)(2n+1)/6, so sum i²/n³=1/3+1/(2n)+1/(6n²)→1/3; it is >1/3 and <(n+1)³/(3n³) for n≥1. sum i=n(n+1)/2 gives sum i/n²→1/2.

Independent mathematical coverage

- Checked every rectangle height/base product and b-power in the x² and x examples.
- Verified both strict staircase-pyramid inequalities and the squeeze; inner base/height n and outer base/height n+1 match Figure 3.
- Differentiated b³/3 and b²/2; checked area theorem conditions separately from the motivating examples.
- Checked summation indexing, ci interpretation, Δx and signed-area qualifications.
- Checked simple-interest weighting, remaining time and all units; no current financial guidance is inferred.

Technical disposition

The x² and x sums and area results are correct in the positive-area setting. Confirmed source issues are the dollars/year total label and the word prism for pyramids. Integrability, sign/orientation and simple-interest assumptions are separately recorded; the general derivative-of-area assertion remains a motivated pattern in this packet, with an independent conditional proof supplied.
