# D018 r28 — independent disposition of SASIS C1–C3

This is an additive post-freeze review. The original SASIS report and my original independent review remain unchanged. I read the complete 110-line original SASIS report, including all chronological witnesses and concerns, and reconsidered the exact frozen teaching passages against the independently inspected baseline/source and prompt-only calculations. The teaching SHA256 remains `4970a5ae04a73cca02eb62a20de8b5eab8d225c6b9ceb22eee44ec6a6408873c`.

Conclusion: C1 identifies a real overbroad mathematical condition in a learner-facing domain statement. Its generic literal reading is false, although every subsequent worked calculation stays correct under continuity. Treat this as a narrow T1/T3 condition-scope defect, not as failure of FTC2 or of the five answers. C2 and C3 identify wording risks, but their sound contextual readings and available short routes prevent a demonstrated material teaching failure on the present evidence.

## C1 — “defined” versus existence of the finite integral

Exact location: teaching line 33, “an input below the starting point is permitted when f is defined on the intervening interval.” The surrounding construction is a real-valued accumulation function. The previous lines supply orientation, not an existence theorem for every defined integrand.

Independent counterexample: let the base be 1 and define a function on all of `[0,1]` by `f(0)=0` and `f(t)=1/t` for positive `t`. This satisfies the sentence's stated condition for the proposed input 0: the function is defined everywhere on the intervening interval. Nevertheless,

`integral_epsilon^1 (1/t) dt = -ln(epsilon)`

diverges as positive epsilon tends to zero. Hence the reversed integral from 1 to 0 is not a finite real value. Defining the value at the endpoint cannot repair the unbounded nearby contribution. This counterexample uses actual baseline standard integration, logarithm behavior, and FM28's improper-integral meaning; it does not require an untaught pathological integrability theorem.

The legitimate restricted interpretation is “when the signed integral exists in the continuous/integrable setting of this lesson.” Line 35 supplies continuity as a sufficient condition, explains its meaning, and explicitly says the continuous-integral existence result is used in the definition above. That makes all subsequent examples and exercises sound and prevents any whole-proof or whole-task blocking conclusion. However, it does not make “defined throughout” a sufficient general domain condition, and the sentence does not state the restricted interpretation. A learner using the stated domain test can admit the counterexample incorrectly.

Disposition: verified local mathematical overstatement with a consequential domain-condition role (T1/T3). The narrow repair behavior is to distinguish a formula being defined from the associated operation existing, and bind a stated admissibility test to the actual sufficient hypotheses before using it as a domain guarantee. No additional exercise, pathological-function catalogue, or lecture-specific answer belongs in PROF. In this self-iteration run the teaching must remain frozen; the coordinator determines the corresponding general operative instruction and verifies the whole fresh generation after publication.

This concern was not identified as a material issue in my original pre-SASIS report. This additive disposition corrects that limited finding; it does not alter the historical report or invalidate its correct calculations/source checks.

## C2 — nearest-integer values of bounds

Exact location: Q4 at line 258 requests “numerical bounds to the nearest integer.” Its exact rectangle inequalities are fully established before the task at 210–217. The prompt-only independent solution already obtained `900/ln(1000) <= I <= 900/ln(100)`, then approximate rectangle sizes 130.28 and 195.44 from the rounded supplied logarithms, and nearest-integer reported sizes 130 and 195.

There are two possible answer presentations:

- Sound: retain the exact symbolic inequality and report its endpoint values as approximately 130 and 195 to the requested precision.
- Unsupported by nearest rounding alone: assert the exact new integer inequality `I <= 195` merely because 195.44 rounds to 195. Outward integer bounding instead would use 196 as the upper endpoint.

The prompt does not explicitly require the second presentation or tell the learner to replace the exact inequality with integer endpoints. “Bounds to the nearest integer” can conventionally request rounded numerical values of exact bounding expressions. Earlier line 217 itself models approximate numerical reporting of rectangle endpoints. The baseline supplies ordinary rounding and bound reasoning; no new theorem is needed to preserve the exact inequality while qualifying its approximate endpoint values. The solution at 335 then makes this distinction explicit and gives no false inequality.

Disposition: a real potential ambiguity, but not a proved material false-answer requirement or blocked task. The sound reading supports all requested work at the prompt's actual position, independently of its later solution. The later solution is corroborating explanation, not the premise that makes the task possible. No separate mandatory PROF repair is justified solely by this concern. A general instruction already being revised for justified reasons may naturally require approximation/bound labels to retain their logical force, but it should not impose a universal prohibition on rounded bounds or require an extra task.

## C3 — a singleton and finite rectangle sums

Exact locations: hint at 275, “A single endpoint value contributes no area”; solution at 306, “changes no rectangle-sum area: its possible contribution has zero width.” In a literal finite tagged rectangle sum, an endpoint can be chosen as the sample of an adjacent interval whose width is positive. Therefore changing that sample value can change a finite sum. The limiting integral is the unaffected object.

Independent discriminating check: in Q2 on an ordered interval ending at zero, changing the sampled endpoint height from 1 to 3 changes at most the endpoint rectangle by `2*Delta t` (or the relevant mesh-width bound). It need not be zero at a finite partition. As the maximum width tends to zero, the change tends to zero; therefore the definite integral, and all the stated B values and one-sided quotients, are unchanged.

The sound contextual reading is the area defined by the limit of rectangle sums. That is precisely how line 26 defines the integral, and line 306 is explaining the integral B rather than announcing a theorem about arbitrary finite sums. Geometrically a single vertical endpoint contributes zero signed area. The baseline's rectangle-sum definition makes the width-bound correction a short available deduction; SASIS reconstructs it before the task and preserves the supported conclusion. No final numerical or logical answer depends on asserting equality of all finite approximants.

Disposition: explanatory precision concern, not a demonstrated material failure under the stated integral-as-limit context. The finite-sum reading would be false and should not be repeated as an unconditional technical claim. The task remains accessible and the natural limiting-area interpretation is correct. Do not manufacture a broad new finite-sum proof obligation from this local wording.

## Combined consequence

Preserve C1–C3 and their original reader classifications. The supported mathematics, source corrections and five independent answer comparisons remain valid. C1 supplies a narrow condition-scope correction; C2/C3 remain documented wording limitations with valid routes. Actual destination failures are separate, independently material evidence and must not be conflated with these semantic concerns. No frozen teaching, reader report, original independent report, or GitHub content was changed in producing this note.
