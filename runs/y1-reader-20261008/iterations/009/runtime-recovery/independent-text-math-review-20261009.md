# D009 recovery-only independent mathematical review

## Status and scope

This is a bounded review of the immutable recovery teaching draft, not SASIS, not authoring, not full-constituent acceptance, and not closure of D009. The cloud execution runtime was unavailable. This work used connector retrieval and pure in-memory JavaScript only: no shell, Windows/user-computer control, local file writes, environment changes, or other iteration reports/root diagnoses. It is useful interrupted-work review, not evidence that the runtime recovered.

**Finding:** no consequential mathematical error was found in the complete available Markdown. The worked calculations, sign classifications, limits, extrema, inflections, hints, and complete task solutions agree with independent reconstruction. This does not establish explanatory availability for the target reader. The four unavailable PNG figures prevent visual or full-document acceptance.

## Exact object and actual access

- Repository: `alverstris/PROF-Skill.md-`.
- Commit: `5f27860bcffb433d26ef125792944b34ac83bf38`.
- Path: `runs/y1-reader-20261008/iterations/009/runtime-recovery/teaching-pending-write-recovery.md`.
- Blob: `92ee517ba0c5c7ddceeacf36ca21e0d135b8bae6`.
- Observed full content: **28,975 characters; 29,022 UTF-8 bytes; P001–P062, consecutive and unique**. The file has 227 content lines and a terminal newline.
- Retrieved and read coherent, exhaustive line ranges at the pinned commit: 1–100 (P001–P032), 101–150 (P033–P040 through the second derivative formula), 151–185 (remainder of P040 through P050), and 186–EOF (P051–P062). Each range reported the expected blob SHA. A subsequent direct fetch of that blob matched the concatenated chunks byte-for-byte in UTF-8 after restoring range-separator and terminal newlines.
- Task A and Task B were calculated independently after their prompts and before their hints/solutions. Task C was calculated before its complete solution; its prompt and Hint C occurred in the same preceding coherent chunk, so this is not a claim of a hint-blind Task C attempt.
- All mathematical prose and displayed formulas were read, not only formulas located by search. Nonmathematical navigation, study instructions, provenance statements, image alt text, and figure descriptions were also encountered; this review does not confer pedagogical acceptance on them.

The original MIT source was opened through web retrieval as an eight-page PDF with extracted text for every page. This was a provenance/terminology check, not a screenshot review. The four examples, lecture title, critical-input convention, and convex/concave-up terminology match the draft. PDF page 3 contains the original cubic; page 4 the reciprocal; page 5 the shifted cubic and start of the logarithmic example; page 6 completes that example; pages 7–8 contain second-derivative information. The cover is PDF page 1. Source: [MIT 18.01 Fall 2006, Lecture 10](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/d41418f410d1e11d0e606a0fc8441b82_lec10.pdf). No conclusions about the missing draft figures are inferred from the source figures.

## Reconstruction and check witnesses

### General mathematical statements: P003–P007, P023–P026, P028, P032, P042, P057

- P004 correctly separates input, height, graph point, function zero, and derivative zero.
- P005 correctly restricts strict derivative-sign monotonicity to an interval of differentiability. Positive/negative height is independent of rise/fall.
- P006 correctly uses negative-to-positive and positive-to-negative derivative signs for strict local minima and maxima of the continuous curve at the joining input. Stationarity alone is insufficient; the corner minimum of |x| at zero is valid. All four worked functions are differentiable at every allowed input.
- P007 correctly splits a sign line at both derivative zeros and domain exclusions; a sampled sign alone needs a reason that no sign change can occur in the interval.
- P023–P024 correctly distinguish height change from slope change. For x², slopes at -1, 0, 1 are -2, 0, 2; for -x² they are 2, 0, -2. An increase of negative slope from -4 to -1 describes decreasing, concave-up behavior.
- P025's second-derivative test is valid in the stated smooth setting. Its accompanying argument explicitly supplies local continuity of the second derivative, so positivity at the input extends to a neighborhood and gives the first-derivative sign change. These are local conclusions.
- P026 correctly treats f''(x₀)=0 as inconclusive and requires an actual concavity change at an included continuous graph point for inflection under the stated convention. An undefined second derivative can require investigation; an excluded input is not a graph inflection.
- P032's distinction among zeros of f, f', and f'' is correct. None of the three vanishing conditions universally implies the other two.
- The reconciliation requirements in P042 and recall in P057 are mathematically consistent with these restrictions.

### Original cubic: P008–P013, P029–P031

For f(x)=3x-x³:
- f'=3(1-x)(1+x), with signs **negative, positive, negative** on (-∞,-1), (-1,1), (1,∞).
- f(-1)=-2 and f(1)=2 give the stated local minimum and maximum.
- f=x(3-x²) gives zeros -√3, 0, √3.
- -x³(1-3/x²) establishes f→+∞ at -∞ and f→-∞ at +∞. Neither local extremum is absolute.
- f''=-6x: concave up for x<0, concave down for x>0. Thus (0,0) is an inflection with slope 3, not a horizontal tangent.
- f''(-1)=6 and f''(1)=-6 confirm the stationary classifications.
- Every ordered construction statement in P012 and P030 matches the joint first/second derivative signs. P013's claims about actual dots and dashed tangents cannot be verified without the image.

### Reciprocal: P015–P019, P027

For q(x)=1/x:
- Domain ℝ excluding zero; q'=-1/x²<0 on each domain interval.
- The cross-gap witness q(-1)=-1<1=q(1), with -1<1, correctly disproves global decrease on this disconnected domain.
- q→-∞ at 0⁻ and +∞ at 0⁺; q→0⁻ at -∞ and 0⁺ at +∞. Both axes are asymptotes and neither meets this graph.
- No stationary input or extremum exists.
- q''=2/x³ is negative on x<0 and positive on x>0. This does not give an inflection because zero is excluded.
- The branch descriptions in P019 are correct. The general statement that a horizontal asymptote may be crossed is true; Task C itself supplies an example.

### Shifted cubic: P020–P022, P027

For s(x)=x³-3x²+3x=(x-1)³+1:
- s'=3(x-1)², zero only at 1 and positive elsewhere.
- s(1)=1; s is strictly increasing, including across 1, directly from strict order preservation by cubing.
- Its only root is 0; the tails are -∞ and +∞.
- s''=6(x-1) changes negative to positive at 1. Hence (1,1) is a stationary inflection and neither kind of extremum.
- The claimed tangent equation y=1 is mathematically correct. Its actual dashed rendering in P022 is unverified.

### Logarithmic quotient: P034–P041

For L(x)=(ln x)/x:
- Domain x>0; no vertical-axis intercept; L'=(1-ln x)/x².
- Since ln x increases, L'>0 on (0,e) and <0 on (e,∞). Thus (e,1/e) is the absolute maximum, not merely a local maximum.
- L=0 only at 1, with negative heights before 1 and positive heights afterward.
- For 0<x<e⁻¹, L(x)<-1/x. This pointwise bound establishes L→-∞ at 0⁺.
- For every x≥1, integrating 1/t≤1/√t over [1,x] gives
  0≤ln x≤2(√x-1), hence 0≤L(x)≤2/√x.
  This supplies a genuine all-input squeeze limit, L→0⁺ as x→∞; it does not rely only on a selected sequence.
- L''=(2 ln x-3)/x³. The denominator is positive, so concavity changes from down to up at e^(3/2).
- The inflection height is 3/(2e^(3/2)); its input exceeds e and is on the descending branch. L''(e)=-1/e³<0.
- P041's descending piece first steepens and then becomes less steep because L'' is negative before e^(3/2) and positive afterward.

### Task A, hint and solution: P014, P047, P051–P053

Independent reconstruction for r(x)=x³-3x+2=(x-1)²(x+2):
- r'=3(x-1)(x+1), with signs **positive, negative, positive** across -1 and 1.
- (-1,4) is a local maximum; (1,0) is a local minimum.
- At -2, the simple factor x+2 changes sign while the square stays positive: the graph crosses from negative to positive.
- At 1, both nearby sides have positive height: it touches the axis from above and turns upward.
- Tails are -∞ on the left and +∞ on the right; neither local extremum is absolute.
- r(0)=2 and r=2-f provide independent height/transformation checks of the ordered sketch.
- Hint A's factor signs and substitution instruction are correct. The complete solution addresses all requested mathematical components.

### Task B, hint and solution: P033, P048, P054–P056

- For v=x⁴: v'=4x³ changes negative to positive; v''=12x² is positive on both sides. The origin is a strict local and absolute minimum, with no inflection.
- For w=x³: w'=3x² is positive on both sides; w''=6x changes negative to positive. The origin is neither maximum nor minimum and is a stationary inflection.
- Both first and second derivatives vanish at zero for both functions. The second-derivative test is inconclusive for each; neighboring signs settle the different outcomes.
- Hint B's parity and derivative statements are correct. The solution answers the sign, classification, inflection, and test-status requests.

### Task C, hint and solution: P043, P049, P058–P062

For h(x)=(x-1)/x²=x⁻¹-x⁻²:
- Domain ℝ excluding zero; sole intercept (1,0); no vertical-axis intercept.
- For 0<|x|<1/2, x-1<-1/2, so h(x)<-1/(2x²). Both one-sided limits at zero are -∞.
- Both inverse-power terms tend to zero at either infinity. The numerator sign supplies approach from below at -∞ and above at +∞.
- h'=(2-x)/x³ has signs **negative, positive, negative** on (-∞,0), (0,2), (2,∞).
- (2,1/4) is the only stationary point and is both a local and absolute maximum. A separate algebraic witness is
  1/4-h(x)=(x-2)²/(4x²)≥0 for every allowed x,
  with equality only at 2.
- Values near zero are unbounded below; there is no absolute minimum. The derivative signs give no local minimum.
- h''=2(x-3)/x⁴ is negative on (-∞,0) and (0,3), positive on (3,∞).
- (3,2/9) is an inflection; h'(3)=-1/27, so it is nonstationary. Zero is neither a stationary input nor an inflection.
- The left branch descends, concave down, from 0⁻ to -∞. The positive branch rises concave down from -∞ through (1,0) to (2,1/4), descends concave down to (3,2/9), then descends concave up toward 0⁺. This agrees with P062.
- Hint C preserves the necessary domain restriction and gives correct differentiation, denominator-parity and endpoint guidance. The solution covers every mathematical item requested.

## Supported errors, ambiguity, and limits

**No consequential mathematical error found.** There is no supported wrong derivative, sign, value, limit, extremum classification, inflection classification, or task-answer contradiction in the available text.

One minor precision point is **P018's informal vertical-asymptote description**: “at least one approach ... without bound” should be understood as a one-sided infinite limit, not merely unbounded values along a selected sequence. P017 explicitly supplies the required limits for the example, and P037/P058 justify their limits by pointwise bounds, so this wording creates no erroneous worked conclusion. It is a potential ambiguity of the general phrasing, not evidence of a consequential error.

The following figures were referenced but unavailable in the archive and were not inspected:
- `figures/cubic.png`
- `figures/reciprocal.png`
- `figures/stationary-inflection.png`
- `figures/logarithmic.png`

Accordingly, P002's claim that nearby descriptions carry the same essential relationships as the figures is not verified as an equivalence claim. The prose and alt text can be checked for mathematical consistency, but actual plotted branches, coordinates, labels, holes/filled dots, dashed lines, scaling, clipping, and text–image agreement cannot. Descriptions are not substitutes for an inspected constituent when deciding full-document acceptance.

Mathematical reconstruction by this reviewer does **not** show that the intended reader can perform every inference from the material available to them. Explanatory availability, complete constituent inspection, and SASIS remain pending. The result neither establishes a skill defect nor closes D009.
