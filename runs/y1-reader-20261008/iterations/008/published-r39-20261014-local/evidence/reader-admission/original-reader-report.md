# Original SASIS reader report — D008 R39

Status: **procedure-limited, incomplete teaching coverage; no substantive admission or overall teaching verdict**.

This is the reader's original report, written before author feedback. The reader identity is D008_R39_FIRST_READER_R1. The stated frozen route SHA-256 is `11fd968ea07bc2278cf4af473c2d45fcae6f65df0963e0884351dda4c9175d8d`; teaching revision is `d008-r39-first-delivery`.

## Actual access and boundary

The bootstrap consisted of two read-only PowerShell Get-Content calls on the exact authorised subject-free reader-launch-message.txt, selecting lines 1–90 and 91–186. Both returned fully. I read the returned operating instructions, including the complete fixed adapter, before subject access. I did not independently inspect any other metadata or input file.

I then used the adapter in the recorded order for B0001 through B0022, main-01 and figure-01. Each text result passed its extent/hash checks, was displayed through functions.text and yield_control, and the corresponding execution was waited to completion. The figure passed the adapter's original-image checks, displayed completely, and its execution was waited to completion before the next attempted step. There were no baseline revisits, early teaching exposure or delayed figure inspection.

The attempted next call, main-02, failed before invoking the launcher because I made a copying error in the adapter's SHA-256 constants. The exact submitted code and result remain preserved in this reader conversation. STEP_ID was `main-02`; the submitted k-array contained the segment `0x2748774c,0x34b0bcb5,0x682e6ff3,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x748f82ee`. The authorised segment was `0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee`. Thus that call changed more than STEP_ID, contrary to the fixed-adapter instruction. This is my procedural error, not a document defect.

Exact failure returned:

```
Script failed
Wall time 0.0 seconds
Output:
Script error:
Error: adapter hash self-check failed
    at requireValue (exec_main.mjs:9:53)
    at exec_main.mjs:58:1
```

The failure was at the `sha256(utf8("abc"))` self-check. No launcher command, subject packet or main-02 content was returned by this call. I have not corrected and retried it, advanced the route, skipped ahead, or improvised retrieval. The operating instruction says that if any call fails, preserve the exact failure and report the input/procedure limit rather than improvising another command or advancing state.

The authorised delivery condition is instruction confinement, not a technical sandbox or erased memory. I have not browsed, searched for files, accessed original source, read the PROF skill, used author history, contacted another agent, or used another subject-content source. I made no invented task battery and make no learner grade or mastery claim. My own report writing accesses no further input content.

## Coverage ledger

Byte ranges below are half-open, using returned start and byte_length. All listed successes were actually read. The full baseline comprises the contiguous range [0,247840), all 22 initial chunks.

| Order | Step | File ID | Bytes read | Result |
|---:|---|---|---|---|
| 1 | B0001 | BASELINE | [0,11972) | Complete text and completed receipt |
| 2 | B0002 | BASELINE | [11972,23842) | Complete text and completed receipt |
| 3 | B0003 | BASELINE | [23842,35589) | Complete text and completed receipt |
| 4 | B0004 | BASELINE | [35589,46917) | Complete text and completed receipt |
| 5 | B0005 | BASELINE | [46917,58627) | Complete text and completed receipt |
| 6 | B0006 | BASELINE | [58627,70567) | Complete text and completed receipt |
| 7 | B0007 | BASELINE | [70567,82297) | Complete text and completed receipt |
| 8 | B0008 | BASELINE | [82297,94288) | Complete text and completed receipt |
| 9 | B0009 | BASELINE | [94288,105690) | Complete text and completed receipt |
| 10 | B0010 | BASELINE | [105690,117614) | Complete text and completed receipt |
| 11 | B0011 | BASELINE | [117614,128999) | Complete text and completed receipt |
| 12 | B0012 | BASELINE | [128999,140647) | Complete text and completed receipt |
| 13 | B0013 | BASELINE | [140647,152334) | Complete text and completed receipt |
| 14 | B0014 | BASELINE | [152334,164018) | Complete text and completed receipt |
| 15 | B0015 | BASELINE | [164018,175642) | Complete text and completed receipt |
| 16 | B0016 | BASELINE | [175642,187166) | Complete text and completed receipt |
| 17 | B0017 | BASELINE | [187166,198963) | Complete text and completed receipt |
| 18 | B0018 | BASELINE | [198963,210918) | Complete text and completed receipt |
| 19 | B0019 | BASELINE | [210918,222601) | Complete text and completed receipt |
| 20 | B0020 | BASELINE | [222601,233903) | Complete text and completed receipt |
| 21 | B0021 | BASELINE | [233903,245588) | Complete text and completed receipt |
| 22 | B0022 | BASELINE | [245588,247840) | Complete text and completed receipt |
| 23 | main-01 | T006 | [0,3773) | Complete text and completed receipt |
| 24 | figure-01 | complete PNG | Complete original image | Displayed and completed receipt |
| 25 attempted | main-02 | No subject result | None | Adapter self-check failure |

The main-01 returned SHA-256 was `38e7c96ef69e43173e453977e69491ab6fd9965e82975bd62d2c5102715798cb`. For figure-01, input and displayed tool-result SHA-256 both were `ddcd4c45d90dd3473cfb5f95c3bc658d9144c9e7682195407a2a1d7db1bf15fa`. Mechanical receipts establish delivery checks, while the semantic witness below records my inspection.

Unread scheduled teaching steps are main-02, main-03, figure-02, main-04, main-05, figure-03, main-06, figure-04, main-07, main-08, main-09, main-10, main-11, hints-intro, hint-a, hint-b, hint-c, hint-d, hint-e, hint-f, solutions-intro, solution-a, solution-b, solution-c, solution-d, solution-e and solution-f. No claims are made about their content, support, accuracy, exercises or solutions. In particular, the later material announced in main-01 has not been inspected.

## Baseline availability recorded during the chronological read

The entire four-subject baseline was read before teaching. Relevant locators for the part actually inspected are:

- B0001, Mathematics “Prior arithmetic, geometry and mathematical language” and “Algebra, functions and coordinate geometry”: signed differences, identity versus equation, domains, implication, rearrangement, functions, straight-line slope and coordinates. These supply the ordinary operations and the distinction between a defined polynomial and a claim about another function.
- B0002, Mathematics “Exponentials and logarithms” and “Differentiation and its applications”: ln(1)=0; real ln domain x>0; derivative 1/x; derivative as the limit of a difference quotient; constant and sum differentiation; tangent equation at a basepoint. These are direct premises for main-01, without needing new calculus theory.
- B0003, Mathematics “Integration and elementary differential equations” and “Vectors,” and B0004–B0005 mechanics and scope boundaries, were all read; they are not needed to justify the inspected tangent construction.
- B0005–B0008, Further Mathematics FM01–FM71, were all read. FM27 explicitly supplies standard Maclaurin expansions and their stated validity conditions, while withholding a general remainder theorem. The opening's assertion that standard expansions are available is supported; no later use of them was inspected. FM57 states dimensional matching, also available for the slope-times-displacement units check.
- B0008–B0013, Physics sections 1–8, were all read. B0009 “Vectors, graphs and rates” supplies tangent versus secant reading and labelled graph interpretation. B0011's thermal and oscillation content and all later physics were read without treating its university-formalism exclusions as missing algebra.
- B0013–B0022, Chemistry CH-META through CH-REF, were all read, including actual operational calculation, reaction, equilibrium, Gibbs, organic, spectroscopy and practical explanations. CH-06.03 (B0018) grants quantitative Gibbs and entropy reasoning but explicitly withholds statistical thermodynamics. No chemistry premise is needed for main-01, and no future topic is inferred from these sections.

These are availability observations, not measures of a person's retention or performance. The curriculum-completion competence assumption is supplied by the baseline itself.

## Chronological reconstruction witnesses for the teaching actually encountered

### main-01 opening and purpose

The document is titled “Linear and quadratic approximations” and identifies a complete teaching route. It announces a tangent model, basic formulas, algebra with approximations, limits, a clock example, quadratic models and a later revisit. This is a preview; it makes no clock inference in the portion read. Differentiation, tangent lines, limits, binomial expansion and standard Maclaurin expansions mentioned as starting knowledge are supplied by the Mathematics/Further Mathematics baseline cited above.

The distinction between `L(x)=x-1` as the exact definition of a polynomial and `ln x ≈ L(x)` as an estimate of another function is intelligible from B0001's expression, equation, identity and function language. The declared purpose of an approximation is new explanatory framing rather than an unsupported mathematical theorem.

### main-01 §1: tangent model construction and notation

The basepoint x0 is a fixed input; h=x-x0 is signed displacement. The values f(x0) and f'(x0) stay fixed while x varies. Starting from B0002's tangent equation y-f(x0)=f'(x0)(x-x0), rearranging gives the defined line `L(x)=f(x0)+f'(x0)(x-x0)`. Substitution x=x0 returns height f(x0), and differentiation with respect to x gives constant slope f'(x0). Thus it meets both stated tangent requirements. The slope multiplying the whole displacement is explicitly explained; an alternative reading that multiplies x alone is excluded by the parentheses and prose.

The description “degree at most one” includes the constant case when f'(x0)=0, as stated. For a unit-bearing input, the derivative is output change divided by input change; multiplying by x-x0 restores output units, so addition to f(x0) is consistent with the baseline's unit rules. No external physical law is required.

### main-01 §1: local justification and its limit

B0002 defines differentiability through the difference quotient. With h nonzero and tending to zero, the displayed quotient tends to f'(x0). The new error definition is `E1(h)=f(x0+h)-f(x0)-f'(x0)h`. Dividing it by h yields exactly the quotient minus f'(x0), hence tends to zero. This reconstructs the consequential link: omitted output change becomes small relative to input change locally. A finite numerical error tolerance does not follow from this limit without additional information; the text explicitly says so.

The advice to choose a close and easy basepoint is appropriately qualified. It neither asserts monotonic error growth for arbitrary functions nor extends the local justification to faraway inputs. For an exactly linear f, substituting its constant slope and basepoint value reproduces f for every admissible x, supporting the exception stated in the text.

### main-01 worked logarithm example

For x>0, B0002 supplies f(x)=ln x, f(1)=0, f'(x)=1/x, hence f'(1)=1. Substitution into the established construction gives L(x)=0+1(x-1)=x-1. At x=1.1, the estimate is 0.1. The actual value is supplied as approximately 0.09531, so arithmetic gives 0.1-0.09531=0.00469, a positive overestimate. The numerical comparison therefore checks its own stated example, with no external calculator value needed. It supplies no universal error bound, as the text acknowledges.

### figure-01 at its scheduled first use

I actually inspected the complete 1280×768 image after main-01 and before the attempted main-02 call. The horizontal axis is x and the vertical axis is function value. The legend identifies green solid f(x)=ln x and red dashed L(x)=x-1. They meet at the black point (1,0), labelled “same value and slope at x0=1.” At x=1.3 the red point is near 0.3 and the green point near 0.26, with an arrow identifying the vertical error. This visually represents the difference between outputs at one common input. The plotted tangent lies above the logarithm in the displayed interval. The image illustrates the tangent and local error; the derivative argument in the text, not the appearance alone, supplies the justification. Labels and curves were legible and complete in the returned view.

## Issues, provisional concerns, dependencies and limits

No established teaching defect is supported by the part actually read. The inspected tangent construction, its local difference-quotient justification, unit interpretation, logarithm example and first figure have reconstructible support from the supplied baseline and preceding text.

No claim that the whole document is adequate follows from this. The reading was prevented from reaching all remaining teaching, three further figures, all six labelled attempts, hints and solutions. Their availability, consequential connections, ambiguity and dependencies are unverified. A later explanation cannot be assumed to justify an earlier unseen exercise.

The established issue is the reader's procedure failure, specified above. It invalidates any claim of completed-route delivery or full document coverage. It must not be reported as a mathematical or pedagogical defect in the document. There is no basis to invent a provisional concern about unseen content. No missing independent scientific fact has been established in the inspected part; no separate technical truth assessment has been performed.

The report preserves the last supported understanding: a tangent line at a differentiable basepoint matches value and first derivative, and its residual divided by the input displacement tends to zero. Everything after the first figure remains unverified in this run.
