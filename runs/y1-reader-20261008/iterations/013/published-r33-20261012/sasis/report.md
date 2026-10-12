# SASIS report — frozen revision d013-clean-r33-20261012

The complete content audit found no established substantive teaching defect. **This run is not admissible as a strictly clean next-slice-only reading.** A retrieval error at D14 breached that access condition; its exact limits are recorded below. Complete coverage and a supported content finding do not erase the procedural failure.

This is the original final report, written after the whole audit and before any author feedback. It evaluates the supplied teaching against the supplied operational baseline; it is not an examination, a mastery score, or evidence about human learning or retention.

## Actual admission and access

The operating role and subject-free route were read first. All 247,840 baseline bytes were then displayed in the nine exact ordered half-open byte ranges: [0,28098), [28098,56121), [56121,84460), [84460,112790), [112790,141255), [141255,169377), [169377,197761), [197761,226042), [226042,247840). None was clipped. Only after B9 did teaching retrieval begin.

All 32 document route steps were completed: 29 exact text slices covering all 23,556 bytes of main.md, 2,989 bytes of hints.md and 8,616 bytes of solutions.md, plus the three complete figures at steps 3, 8 and 13. Each figure was inspected immediately at its routed position before subsequent prose. All successful slice hashes match the route. Post-reading complete-file hashes also match. Chronological reconstruction notes were appended during reading, before each next passage; later hints and solutions did not retroactively supply earlier witnesses.

At the first D14 attempt, the command accidentally invoked `python teaching/main.md 14849 15867 D14` rather than the slice helper. Python opened/parsed the Markdown file and failed on an en dash at line 7. Its displayed diagnostic quoted only the already-read introductory paragraph. No new later subject passage was visible. The compiler's internal source-read extent was not instrumented and may have included the complete file. This is an actual deviation from retrieving only the next text slice, not merely a hypothetical risk. The intended [14849,15867) slice was then retrieved correctly, and all later steps followed the route. A repeated read cannot restore strict access admission.

No browsing, external research, other subject file, raw source, author review, personal/project history retrieval, or other-agent consultation was used. Broad tools existed: confinement was instructional, not technical, and no pretraining erasure is claimed. The sole parent communication is this completed report.

| Input | Actual complete SHA256 |
|---|---|
| Baseline | `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5` |
| main.md | `cb49c11d4cbed87151b3060cc7183274a9999df5ff27cf15e70659ea499a61d5` |
| hints.md | `3aef9c100cd37b3b7c83ac20586d4fbb0ba334bb3ae9cfb42649104da95a8012` |
| solutions.md | `ac64ff9cb44f0a90a43a682e4690dc809adda5101abb4d47deb7e57c457a20d2` |
| mvt-geometry.png | `efb63aa355ec94795c035264c4c4eb0d3a7caf3497299b73fe4ede19c6c0e8e5` |
| corner.png | `7d66928396a5dd49e8d903ac8c635d9c188e7f8840e7b7ac30f964ffe1d09360` |
| approximation.png | `e67b214509625cd11e9acc1f4d8c246e7a09a15f2a68f15bdd5f954db18c9a82` |

## Available baseline premises

The full four-subject packet was read, including both selected Further Mathematics options. The relevant prerequisites were actual entries, not course names:

- Mathematics B1 [0,28098), “Prior arithmetic, geometry and mathematical language,” “Proof and mathematical work” and “Algebra, functions and coordinate geometry”: real domains, interval brackets, implication versus converse, counterexample, modulus cases, inequalities and positive/negative multiplication, polynomial algebra, point-slope lines, logarithm domains and exponentials.
- Mathematics B1, “Differentiation and its applications”: finite difference-quotient limit, tangent/local rate, power and chain rules, sum/constant-multiple derivatives. B1 also supplies familiar limits and finite-sum notation. B2 [28098,56121), final Mathematics scope, explicitly does not grant formal epsilon-delta analysis.
- Further Mathematics B2–B3: FM01 induction; FM27 explicitly supplies the real exponential series identity, while withholding general convergence proofs and a remainder theorem.
- Mathematics mechanics in B2 and Physics “Vectors, graphs and rates” and “Motion and forces” in B4 [84460,112790): signed position/displacement/velocity, speed as magnitude and average versus instantaneous rate. Chemistry CH-01.01 in B6 independently supplies the chord/tangent distinction; no additional analysis theorem was inferred from it.

The teaching supplies continuity language and familiar-function continuity, the MVT, and the extreme value theorem locally. The EVT is explicitly an accepted foundation with its proof outside this lesson. Its stated status makes it available; the external citation need not be opened. The reader is not required to invent a compactness or formal real-analysis proof.

## Chronological reconstruction witnesses

Ranges below are raw UTF-8 half-open byte offsets. The contemporaneous `chronological-notes.md` records every B1–B9 and D01–D32 item separately; this table groups only connections sharing premises.

| Route and locator | Meaning, warrant and resulting conclusion |
|---|---|
| D01, main[0,4186) | Continuity requires actual value/approaching-value agreement, with one-sided endpoint approaches. Differentiability requires a common finite quotient limit. For modulus at zero, cases give left slope −1 and right slope +1, distinguishing the checks. The stated MVT is existential with both hypotheses. For t² on [0,2], endpoint slope 2 and derivative 2c give c=1. Point-slope algebra produces y=2t and y=2t−1: parallel, distinct lines. |
| D02–D04, main[4186,4627), Figure 1 | Image labels a=0,c=1,b=2 and points (0,0),(1,1),(2,4), matching the calculation. Blue secant and red tangent have equal slope. The dotted line is visibly lower. For this parabola, t²−(2t+k)=(t−1)²−1−k places first contact at one. The caption labels the general contact justification as later material; it is not silently required now. |
| D05, main[4627,5136), P1 | Before help: declared polynomial continuity and the power derivative check the hypotheses. Endpoint slope is 1; 3c²=1 gives ±1/√3, only the positive root in (0,1). Earlier straight-line example shows why the theorem does not generally guarantee uniqueness. |
| D06, main[5136,8093) | Set m to secant slope, ℓ to its line, h=f−ℓ. Then h(a)=h(b)=0 and h′=f′−m. Locally stated continuity preservation plus baseline differentiation make EVT applicable. A nonzero gap has a positive maximum or negative minimum away from the zero endpoints. At a maximum, right quotients are ≤0 and left quotients ≥0. Their shared finite derivative is therefore zero; minimum reverses the signs. Thus f′(c)=m. This does not assume every extremum is differentiable. The modulus example gives secant 1/3, with no existing derivative other than ±1. |
| D07–D09, main[8093,12174), Figure 2 | The complete V-shaped plot shows branch slopes −1,+1; the red contact line is not labelled a tangent. For −1<m<1, |t|−mt is nonnegative on both branches and zero at the corner, justifying the caption's restricted slope range. The endpoint-jump example separately has interior derivative zero and secant one, witnessing the continuity requirement. |
| D09, motion and sign consequences | Stipulated continuous/differentiable position gives signed velocity 1000/3 miles/hour at some interior time; because positive, its magnitude is the same speed. Accumulated distance is explicitly a separate interpretation. For arbitrary u<v, MVT yields f(v)−f(u)=f′(c)(v−u). The positive length transfers the derivative's sign, proving increasing/decreasing/constant and non-strict variants. t³ illustrates non-converse strictness. Missing domain points prevent connecting-interval use; constants across separate components need not agree. |
| D10, main[12174,12876), P2 | Before help: g(0)=1,g(3)=2 give slope 1/3; shifted modulus has derivatives −1,+1 and none at one, so no match. For r, values at −1 and 1 differ despite componentwise zero derivative. Zero is absent, so [-1,1] is not an admissible theorem interval. |
| D11–D14, main[12876,15867), Figure 3 | Algebra gives exact MVT forms; reversing endpoint order handles x<a. Tangent L uses the additional derivative at a. Its error divided by h equals the defining derivative quotient minus f′(a), tending to zero without an unstated remainder theorem. At a=1,x=1.5 for t², L=2, f=2.25 and exact slope 2.5 gives c=1.25. The full figure displays those outputs and vertical error 0.25. Interior derivative bounds transfer to f′(c); multiplying positive x−a and adding f(a) yields strict output bounds. Negative changes require reversal, explicitly noted. D14 access is qualified above; no hidden subject premise was taken from the failed command. |
| D15, main[15867,16554), P3 | Before help: positive-domain power rule gives 1/(2√t). The tangent slope 1/4 yields 2.01. Since 4<c<4.04, increasing positive roots and decreasing reciprocals give 1/(2√4.04)<f′(c)<1/4. Multiply by 0.04 and add 2 to prove the requested bounds and overestimate. No numerical radical lookup is needed. |
| D16, main[16554,19329) | A zero value anchor plus derivative sign determines the difference's sign; a negative constant shift explains why derivative comparison alone is inadequate. f₁=eˣ−1 is positive for x>0 using eˣ>0. Each next polynomial difference has derivative equal to the previously positive difference and value zero at zero, so MVT proves the successive finite lower bounds. The left-of-zero example d=−2x shows that negative derivative is direction of change, not negative output. |
| D17, main[19329,19884), P4 | Before help: real domain x>−1; d=x−ln(1+x) has d(0)=0 and d′=x/(1+x). On [0,x] for positive x, positive derivative gives d(x)>0. On [x,0] for negative x, negative derivative gives d(0)<d(x). Equality is zero only. The earlier leftward comparison supplies this ordering connection. |
| D18–D19, main[19884,22033), series and P5 | Pₙ is a finite indexed sum, with n=0 and n=1 explicit. Infinite sum is the limit of partial sums; FM27 supplies its exponential value independently. For P5, induction is available from FM01: R₀>0 follows the existing base argument; k/k!=1/(k−1)! gives Pₙ′=Pₙ₋₁. With the hypothesis for every positive input, Rₙ′(c)=Rₙ₋₁(c)>0 and Rₙ(0)=0 prove Rₙ(x)>0 on [0,x]. Finite positivity does not by itself prove gaps tend to zero. |
| D20, main[22033,23556) | Ending distinguishes recall/application/revisit from lasting mastery. Source links supply provenance labels, not necessary exercise premises. Claimed fidelity to the original five-page lecture and its printing mistakes cannot be independently verified with the two permitted inputs. |
| D21–D26, all hints[0,2989) | Introduction and ending read. P1 gives candidate filtering and straight-line nonuniqueness; P2 directs branch formulas and the missing-domain-point check; P3 explains reciprocal order and positive-step multiplication; P4 explicitly directs negative x toward larger zero; P5 explains factorial cancellation and asks for Rₙ→0. These cues elaborate routes already supported at the corresponding task positions. |
| D27–D32, all solutions[0,8616) | Introduction and ending read. P1 verifies √3>1 and distinguishes example-specific uniqueness. P2 gives actual failed matching and cross-gap constancy conclusions. P3 gives the exact c identity, radical chain and negative signed error. P4 explicitly writes d(0)−d(x)=d′(c)(0−x)<0 for negative x. P5 quantifies its induction hypothesis over all positive t, explains finite reindexing, applies it at c, and uses 1−1/(n+1)→1 below ceiling 2 to witness why a bound is not its limiting value. No infinite sum is differentiated. |

## Findings and limits

**Established teaching defects:** none identified in the completed audit. This finding is supported by the connection witnesses above and the contemporaneous per-step notes, not by answer-only checks. There was no identified subject dependency requiring conditional acceptance or later repair.

**Provisional content concerns:** none retained as consequential. New foundations are explicitly declared; the approximation is carefully separated from equality; strict/non-strict signs, domains, variable c, and leftward comparisons have usable meanings. Ordinary baseline algebra and finite differentiation are sufficient for the demands. This does not assert discovery of every possible latent error.

**Established procedural defect:** the D14 failed command prevents strict clean admission. Its compiler-internal access extent is unknown; no later subject text was visibly disclosed. A new fresh run would be required if the surrounding process needs a fully clean next-slice-only reader. The completed content observations remain documented, but must not be labelled such a run.

**Input and verification limits:** no supplied artifact was missing, truncated or unreadable; no output clipping or delayed figure inspection occurred. External source fidelity, citation accuracy and claims about the source's printing errors were not independently checked because the original sources were not permitted inputs. The EVT's independent proof is outside the teaching's declared scope and was not reconstructed from outside knowledge. No conclusion about a real student's retention, performance, optimal study delay or laboratory competence follows.

Evidence files in this directory: `access-log.jsonl`, `chronological-notes.md`, `admission.json`, and `coverage.json`. The JSON records contain actual per-range hashes, all 32 route matches, the failed-access record and the explicit false strict-admission flag.
