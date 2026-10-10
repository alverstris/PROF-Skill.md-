# Independent mathematical comparison of frozen D017

Reviewed artifact: lesson.md, SHA256 adaf6fb78d72cfd02b9579dc821e2daa25f770cc05e8a6f99e73cb42c833d62d, all 352 lines. Both accompanying PNGs were opened at original resolution and visually inspected. The record root-independent-calculations.md was completed before this document or its solutions was opened.

Decision: no material mathematical or figure-content error found in this frozen generation. This is a technical disposition only; it does not substitute for the separately admitted SASIS reading, the complete PROF/source audit, or the actual-destination rendering checks.

## Whole-document comparison

| Portion | Evidence and disposition |
| --- | --- |
| Lines 15–51: endpoint theorem and first examples | The continuity and antiderivative hypotheses are stated. Endpoint order, evaluation-bar construction, derivative checks, cancellation of the additive constant, x-squared and fifth-power results are correct. The course's numbering convention is identified at line 9. |
| Lines 61–91: sine and motion | The half-period integral is 2 and the full-period integral is 0. Geometric area is distinguished from signed integration. The Riemann-sum motion interpretation has correct units and distinguishes signed velocity from speed and odometer increase. |
| Lines 101–134: additivity and orientation | Increasing-interval splitting, intermediate-endpoint cancellation, reversed bounds and equal bounds are consistent. The stated continuous-function/antiderivative conditions support extension to any order. The 2x calculations yield 3+5=8 and -8 when reversed. |
| Lines 144–169: comparison and bounds | The comparison requires increasing bounds and accounts explicitly for reversed/equal bounds. Nonnegativity of g-f supports the integral ordering. The derivative argument establishes the exponential lower line before integrating it. The resulting e>=2 and e>=5/2 are correct. |
| Lines 179–221: substitution | The composition and derivative factor are kept distinct. The chain-rule derivation, transformed endpoint order, sufficient regularity conditions and nonmonotone-inner-function statement are correct. The source example gives 99757/15, and the alternative antiderivative differentiates correctly. No division by a potentially zero inner derivative is used. |
| Lines 55, 247, 277–283: P1 and help | Antiderivative, derivative, endpoint values 4 and 1, result 3 and additive-constant explanation match the independent calculation. |
| Lines 95, 251, 287–293: P2 and help | Cosine sign intervals, turning time pi/2 seconds, displacement 0 metres and distance 2 metres agree. Units and the signed/unsigned distinction are preserved. |
| Lines 138, 255, 297–304: P3 and help | Both reversed integrals (-2 and 3), nonuniqueness of unsigned area and its lower bound 8 are correct. Continuous curves with the stated sign pattern and extra cancelling lobes exist; an explicit independent construction is recorded in root-independent-calculations.md. |
| Lines 173, 259, 308–317: P4 and help | The previous inequality gives r'>=0 on the specified domain. The zero initial value yields the quadratic lower bound before integration. The derived e>=8/3 and improvement of 1/6 match the independent calculation. |
| Lines 225, 263, 321–330: P5 and help | Substitution maps endpoints 1 to 3 and 2 to 0 while retaining the negative differential factor. The result 81/8, original-integrand sign check and alternative antiderivative are all correct. |
| Lines 231–233, 267, 334–352: P6 and help | The recalled theorem is distinguished from the transfer task. F=e^(x^2-3x) differentiates to f, both endpoint values equal e^-2, and the sign changes at 3/2. The area 2(e^-2-e^(-9/4)) is positive despite zero signed total. The independent numeric corroboration agrees. |
| Navigation, source note and remaining prose | All lines outside the mathematical portions above were also read. The core, hints and solutions are visibly separated in the source. Destination behaviour and links still require their own actual rendering check. |

## Figure-content inspection

figures/sine-areas.png (SHA256 080ab6b7e608bf3d12ad24669de0ff33034fd048771666da93750bf99d46ac21) shows the correct zeroes, extrema, positive/negative regions and magnitude labels. Its two panels reconstruct the two separate source sine figures. The caption explicitly says area labels are magnitudes and explains the sign convention.

figures/additivity.png (SHA256 08c12fcee59c5dd761188918ae5fd20fcd7d2d4ae3d14b43a5d31b291b32e14f) shows a single positive curve over increasing a,b,c, with two abutting regions meeting at b. The axes and contributions are readable; the caption identifies it as a schematic. No source claim requires this illustrative curve to have a specified formula.

## Limits

The seven independent numerical checks are corroboration, not a proof of the general theorems. No authored teaching was edited during this review. No assertion of simulated-reader accessibility, final publication correctness or lecture closure is made here.
