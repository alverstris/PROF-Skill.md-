D001 final-v4 secondary-preview visual recheck

No observed rendering/notation/legibility defect in the six inspected complete final-v4 secondary-preview pages.

I personally opened all six complete page images at original resolution and compared their visible text and mathematical notation against the exact final teaching source. I used page text extraction only to locate continuations. This is fresh secondary-preview evidence, not live GitHub rendering or candidate acceptance.

PDF: /workspace/scratch/ac36b9c5ff31/prof-readability/d001-render-review/v4/preview.pdf
Recorded and current PDF SHA-256: 62aa9ea95c941630f8da512bcabb08857a94f636b03ecbceb17d534dd8fc51d9 (verified before rendering and after inspection).
Final source: /workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/iterations/001/teaching-v4.md
Recorded and current teaching SHA-256: 402485baa2767af9625146721e356f92bad76e4cfb738e5729c6c8b94ea79401; recorded freeze commit 0716ea92991d7f9fe2814e137bcc830d91a27511.

Only pages 1, 3, 4, 5, 7 and 8 were generated, using full-page pdftoppm output at 160 dpi. Each viewed image is 1360 × 1760 pixels. The six source ranges contain 187 inline and 30 display expressions; the exact per-page source inventories are preserved in inspection.json.

| Page | Source/page scope | Inline expressions | Display indices | Viewed file | SHA-256 |
|---|---|---:|---|---|---|
| 1 | Complete P01–P06 and P07 opening through “which has no value.”; P07 reciprocal derivation continues on the previously inspected page 2. | 39 | 1, 2, 3, 4 | page-01.png | 235cd55fd3ad3633077e00c6ba8453e4b2b40f9c8941c52774e5e85d6d880512 |
| 3 | P11 continuation beginning “in coordinate square units”; complete P12–P16 through the sentence ending “factors x+h.” | 52 | 11, 12, 13, 14, 15 | page-03.png | 74be5ecb7c4ace65b169cb6d6eac22179f6a53aafff450ed14d787bea345b8a7 |
| 4 | Complete P17–P19 and P20 through the final word “We”; P20 continues at the top of page 5. | 39 | 16, 17, 18, 19, 20, 21, 22, 23 | page-04.png | 9857d364582acb570da5d4e0a032ca34f3da13a8c4705c1d64e6a5b568c686d1 |
| 5 | P20 continuation from “need the remainder”; complete P21–P25 and P26 opening through its first displayed instantaneous-velocity equation. P26 continues on the previously inspected page 6. | 21 | 24, 25, 26, 27, 28 | page-05-full.jpg | f2863b6b26272e59ac9279fb218a8ac3a77f8fff745d18ffe05e609afb56f4e8 |
| 7 | Complete P33–P39 (Hints B–D, solutions introduction, complete Solutions A–C), plus P40 introduction and its complete derivative-definition display. Solution D continues on page 8. | 31 | 32, 33, 34, 35, 36 | page-07.png | e856f364ba3c9e00fb0d84d746f755610947566426932d015c07263ace4705e6 |
| 8 | Remaining P40 in full, including all three final Solution D displays and its interpretation; complete P41–P42 through the document ending. | 5 | 37, 38, 39 | page-08.png | cdde62ac5dd8c921d7c72781c79dc7555f49fc3dbe08f1b06a444f2e3b1cf952 |

Page 1 — personally inspected complete page

Complete P01–P06 and P07 opening through “which has no value.”; P07 reciprocal derivation continues on the previously inspected page 2.

- P04’s coordinates P/Q, Delta-x/Delta-f definitions and complete secant quotient retain both function arguments, subtraction, denominator h and subscripts.
- P05’s derivative limit retains the prime, x0 arguments, h-to-zero limit and complete numerator/denominator; surrounding inline coordinate R and positive/negative-h language remain readable.
- P06’s cubic quotient, h-not-equal-zero condition, y=-x alternative, x(x^2+1)=0 grouping and minus-one slope are visible with intact signs/exponents.
- P07’s opening reciprocal/domain restrictions retain x-not-equal-zero, x0-not-equal-zero, h-not-equal-zero, x0+h-not-equal-zero, h=0 and 0/0.
- All visible text and formulas fit inside the page; there is no clipping, collision, missing glyph or raw TeX.

Page 3 — personally inspected complete page

P11 continuation beginning “in coordinate square units”; complete P12–P16 through the sentence ending “factors x+h.”

- P11’s branch/positive-length continuation and P12’s point (2,1/2), tangent y=1-x/4 and both intercepts are intact.
- P13’s reflection and coordinate-swap forms retain all variables, subscripts and 2y0 factor.
- P14’s complete Delta-y/Delta-f equality chain and evaluated dy/dx retain both subtraction terms, grouping, vertical evaluation bar and x=x0 subscript.
- P15’s function/operator forms and both reciprocal derivative examples retain evaluation at x=2, grouping and negative signs on -1/x^2 and -1/4.
- P16’s power quotient retains (x+h)^n-x^n over h, and inline n=1, h/h=1, h-not-equal-zero and n-greater-or-equal-two conditions remain visible.
- The blue notation-reference label wraps normally; no text, expression or evaluation bar is clipped or lost.

Page 4 — personally inspected complete page

Complete P17–P19 and P20 through the final word “We”; P20 continues at the top of page 5.

- P17’s full binomial expansion and remainder sum retain both terms, coefficients, k=2/n summation limits, binomial grouping, and x^(n-k)h^k factors. The inline factorial denominator retains its square brackets and (n-k)! grouping.
- P18’s h^2 factorization, h^(k-2) exponent, C sum and inline absolute-value bounds are legible and retain all bars, coefficients, inequalities and exponents.
- P19’s quotient and remainder bound retain the absolute-value bars around Rn/h, the C|h| factor and arrow to zero; the derivative rule retains n x^(n-1) and its positive-integer condition.
- Both P20 cubic displays retain 3x^2h, 3xh^2, h^3 and the complete quotient-to-limit chain; all inline O(h^2)/O(h), h/h=1 and other continuation expressions are readable.
- No overflow, clipped summation limits, missing factors, raw TeX or sign/grouping defect was observed. The final sentence continues across an ordinary page boundary.

Page 5 — personally inspected complete page

P20 continuation from “need the remainder”; complete P21–P25 and P26 opening through its first displayed instantaneous-velocity equation. P26 continues on the previously inspected page 6.

- P20’s continuation retains division by h, x=0 and h^2. P21’s sum/constant-multiple equation and polynomial derivative retain primes, parentheses, powers 10/9 and the factor 3(10x^9).
- Attempt B’s entire bracketed quotient [q(1+h)-q(1)]/h is visible with both operands, square brackets, subtraction and denominator; q(x)=x^3-3x, h-not-equal-zero and x=1 are intact.
- P23/P24’s height model retains the leading minus, the grouped 16 ft/s^2 coefficient, t^2, and all time/root equations. No thinspace command becomes a comma.
- P25’s signed average-velocity quotient and positive average-speed quotient retain numerators, denominators, -80/80 and ft/s units.
- P26’s first velocity display retains dy/dt, the negative sign, grouped 32 ft/s^2 coefficient and multiplicative t. All content fits; no clipping, raw TeX or unreadable signs were found.

Page 7 — personally inspected complete page

Complete P33–P39 (Hints B–D, solutions introduction, complete Solutions A–C), plus P40 introduction and its complete derivative-definition display. Solution D continues on page 8.

- Hint B’s q(1)=-2 and q(1+h)=(1+h)^3-3(1+h) retain both grouped factors and minus signs; Hint C retains the three positions and z=t^2-2t+1; Hint D retains -2/x0 and both intercept conditions.
- Solution A’s positive/negative h, both negative secant fractions and decimal approximations, tangent -1/4=-0.25, x0=0 and f(0) are complete and legible.
- Solution B’s full expanded cubic, cancellation terms, difference quotient, zero limit, q-prime values, tangent equation y+2=0(x-1), y=-2 and intercept (0,-2) all retain intended operands, signs and grouping.
- Solution C retains z(2)-z(0)=1-1=0, 0/2=0 m/s, 2/2=1 m/s and both z-prime expressions, including the rate-unit spacing.
- P40’s full derivative-definition numerator, denominator, prime and limit are visible near the page bottom without clipping. The complete hint/solution text and return labels are present.

Page 8 — personally inspected complete page

Remaining P40 in full, including all three final Solution D displays and its interpretation; complete P41–P42 through the document ending.

- Solution D’s g-prime display visibly preserves both negative factors (-2)(-1/x^2) and resulting 2/x^2.
- Both tangent forms retain y+2/x0, 2/x0^2, the complete (x-x0) factor, and 2x/x0^2-4/x0. Inline intercepts (2x0,0) and (0,-4/x0) are intact.
- The complete area expression retains 1/2, both absolute-value groups |2x0| and |-4/x0|, multiplication by adjacency and =4; no factor/sign/bar is missing.
- All following interpretation, source/licence text, blue link labels and final P42 text are visible and legible through “artwork.” No clipping, collision, raw TeX or missing glyph was found.

Viewer failure and recovery

The first attempt to open page-05.png failed with: “unable to process image: invalid or unsupported image data”. The PNG is preserved. I rendered page 5 again directly from the same verified PDF as the complete page-05-full.jpg, at 160 dpi and JPEG quality 95. That complete image opened successfully and was personally inspected. No other view or render failed. Exact hashes for both images and all command results are in inspection.json and render-commands.json.

Historical scope preserved

The original final-v4 report inspected pages 2 and 6, establishing pixel equality for those two pages only. It carried earlier whole-preview evidence for the remaining content. This recheck supplies fresh observations of the previously uninspected final pages 1, 3, 4, 5, 7 and 8 without altering the original reports. In combination with the original pages 2/6 observations, it supplies per-page visual evidence for this exact eight-page secondary preview. Pages 2/6 were not reopened here.

Boundaries

No live GitHub client, MathJax, responsive layout or navigation was observed. The source/destination parsed-math reports remain separate evidence. No scientific/learner/SASIS evaluation, new teaching generation or candidate acceptance occurred. The parent owns the final regression decision. No original artifact, repository file or Git reference was changed; all outputs are confined to this new directory.
