# SASIS — dedicated reader protocol

Protocol revision: 2026-10-08-r8.

## Purpose and activation

SASIS evaluates the teaching document. Its dedicated agent is the reader. The central question is whether, at each point in the document, a reader with the supplied baseline can understand the statement, make the required connection, and reach the correct conclusion. It is not a test of the simulated student's ability and is not organised around attempts at held-out tasks.

Activate only for an explicit request to run SASIS or improve/iterate PROF itself. Ordinary authoring, ordinary document revision, and maintaining these instructions do not by themselves start a SASIS run. During a run, apply ordinary PROF to author the teaching. Its relevant practice/help obligations remain; exercises already in the document are read and audited as part of the document, not substituted for reading it.

Read this protocol, [reader contract](sasis/student-testing-contract.txt), [reader operating instruction](sasis/student-role.txt), [profile manifest](sasis/profile-manifest.json) and [rewrite guide](sasis/rewrite-guide.md). The historical acronym and filenames are retained for compatibility; their meaning is governed by the current reader procedure.

## Repository and assigned corpus

For Jonathan's authorised run, GitHub is the source of truth. Read the actual current repository version at the start of each iteration, with a pinned commit. Do not edit the installed Windows skill or operate Jonathan's computer. Save edits and evidence through the available GitHub interface. Preserve concurrent changes; publish with an expected-head check, never an unrequested force push. Verify the published commit, then reload its files before the next material. A proposal, local candidate, or cached earlier skill is not the published revision.

The original inventory contains 126 indexed lectures and 21 TEAL studios, 147 sessions. Jonathan subsequently instructed this run to find the sessions that can be fully read properly and iterate through those only. Audit the complete original inventory, then traverse only the explicitly recorded readable subset in its original order. A packet includes all required associated portions and consequential visual information; file access or an extracted transcript alone does not establish complete reading. Preserve excluded sessions and their precise evidence limits, distinguishing intrinsic illegibility from unestablished complete coverage. This is the user's explicit scope change, not permission to omit required material for convenience in other runs. Keep the complete queue with stable IDs, year-level evidence, original selection provenance, required associated source portions, access status and current evidence. The [lecture CSV](sasis/ocr-baseline-20261007/year1-lecture-index.csv) covers the 126 lectures; resolve the studio list separately from the [registry](sasis/ocr-baseline-20261007/year1-course-registry.json) and official material. Do not silently expand, collapse, or narrow the assignment. A selection index is not source content or evidence of reading. Several assets for one session remain one session, with all required portions tracked.

Obtain and actually inspect the active session's sources, equations and figures. Record unread or inaccessible portions rather than claiming complete coverage. Source mistakes require independent checking. Preserve corrections with precise locators. A source's incorrect wording is not automatically a PROF defect.

## Baseline and roles

The frozen OCR-A-4-subjects-r1 profile comprises Mathematics A H240; Further Mathematics A H245 Pure Core Y540/Y541, Statistics Y542 and Mechanics Y543; Physics A H556; and Chemistry A H432. No MEI, Discrete or Additional Pure option is assumed. [The complete operational baseline](sasis/ocr-baseline-20261007/student-baseline.txt), not qualification names or a syllabus summary, supplies prior knowledge. Use its frozen edition and provenance honestly; verify live editions before claiming it is current. A consequential baseline correction starts a separately labelled profile/condition and cannot retroactively validate old reports.

The author reads the current PROF files, actual sources, complete baseline and relevant research before drafting. The author owns source coverage and the ordinary teaching obligations. The orchestrator preserves state and publishes justified edits. An independent technical reviewer checks scientific/mathematical correctness against inspected sources and explicit deductions. The SASIS agent is a fresh reader, not the author, evaluator, task designer, or a research agent reused under a new name.

The reader receives exactly two subject-content inputs: the complete frozen operational baseline and the complete current teaching document, including its figures, captions, examples, exercises, hints, solutions and appendices. Its short operating instruction is not a third subject-content input. Do not give it raw lecture sources, author chat/history, skill instructions, research notes, suspected defects, previous reader reports or evaluator solutions. Reading instructions and artifact identifiers may be supplied without revealing expected findings.

Launch every reader with a fresh agent context and explicitly set `fork_turns: "none"`. Every frozen document revision gets its own reader. Never reuse a prior reader's memory for a new document. Recalling the current supplied baseline, earlier passages and valid deductions within one reading is allowed. Prior lessons needed by the current document must actually be included there; a completed-lecture ledger cannot supply them.

## Admission and actual isolation

Before dispatch, freeze the document and baseline and save their IDs, revisions and hashes or exact immutable locators. Record agent identity, history setting, operating-instruction revision, permitted tools, delivery mode, input extent, known truncation/access limits and an explicit admission state.

Use complete full-text delivery when its actual extent can be established. A link, hash, claimed window size or acknowledgement alone does not establish complete delivery. Alternatively use an explicitly labelled instruction-confined read-only retrieval condition: both complete immutable artifacts are available, the reader may fetch only those artifacts, and its access ranges/results are logged. It must inspect the whole document in order and read the full baseline in coherent retrievable chunks. It may re-fetch the authorised baseline when needed. Do not claim that all bytes were simultaneously in context.

Shared tools remain technically available unless the runtime truly restricts them. State that an instruction whitelist is not a technical access boundary or erasure of pretraining. Do not invent memory controls or capacity figures. Every consequential connection must be traceable to permitted content regardless of how familiar the answer seems.

An absent, mismatched, incomplete or truncated input blocks substantive admission until repaired. Reading may be dispatched to establish input availability, but its report remains provisional until access evidence shows the required inputs were received/read. If delivery fails later, preserve that result as an input failure, not a teaching verdict. Do not repair it with remembered content or shorten the baseline silently. Verified unauthorised subject access invalidates the affected reader report. A fresh reader is required after input or content repair.

## Read sequentially and audit every teaching step

Freeze the unedited authored document. SASIS reads from beginning to end. At each substantive definition, claim, equation, diagram, example and transition, identify:

1. Meaning: what the words, symbols, referents and representations denote, including consequential conditions.
2. Availability: the baseline passage, earlier document passage or premise explicitly introduced at this point that supplies what is needed.
3. Connection: a concise reconstruction of the inference the reader can make from those premises.
4. Conclusion: whether that inference actually yields the stated result; note plausible competing readings or conclusions.
5. Accessibility: whether the required connection is reasonably available at the declared starting knowledge, rather than merely possible for an expert who invents an extensive untaught theorem.

Use stable document and baseline locators. Cover every substantive step, grouping only routine operations that share an already established warrant. Do not replace a trace with “clear”, “correct”, an answer score, or a checklist tick. Short reconstruction and precise evidence are sufficient; do not request private chain of thought or a diary of every internal deliberation.

New definitions, empirical laws, declared model assumptions and conventions may be introduced as premises. Identify their status, meaning and conditions; do not demand that every physical law be derived from school mathematics. The independent technical review checks that introduced premises are accurate and appropriately scoped. Logical availability and scientific correctness are separate requirements.

At a gap, preserve what is supported and state the exact missing connection or question. Continue the entire document: read independent material and mark dependent conclusions blocked or explicitly conditional on the unresolved step. Do not secretly grant a missing premise. Later explanations cannot justify an earlier required use retroactively. A clearly labelled roadmap may announce a later result without using it prematurely.

Read exercises, hints and solutions at their actual positions and check their supported reasoning, wording and navigation. They are teaching content. SASIS does not become a problem-solving exercise merely because a document contains exercises. Do not withhold later teaching from the full reading to imitate an examination. No mandatory task-designer stage, held-out battery, learner grading, pass/fail student score, or arbitrary control quota defines this protocol. Add a targeted author check only when it resolves a concrete uncertainty.

The reader report records input access, chronological coverage, consequential reconstruction witnesses, all supported gaps/ambiguities/incorrect conclusions, downstream dependencies, and limits. It evaluates the document, not the student's intelligence or achievement. No model report proves human learning, delayed retention or absence of every possible latent error.

## Diagnose and repair the whole document

Preserve the original document and original reader report unchanged. Independently verify reported technical issues and all important scientific results. External checking can establish correctness but cannot add an unprovided premise to the reader's original inputs. A correct conclusion obtained through an unsupported rule is not evidence of adequate teaching. A reader error is not automatically a document defect: inspect the actual route and alternatives.

Audit all required source portions, all sections including the ending/help, relevant PROF obligations and the reader's findings. Maintain an issue register with exact evidence, all supported causes, affected instances and dependencies, necessary repairs, any justified skill edit and verification state. Distinguish teaching gaps, false/ambiguous source claims, baseline faults, input/restriction problems, review errors and legitimate pending questions.

Use the earliest unsupported connection to order a repair, not to stop the audit. Collect every supported issue the full audit exposes. Revisit previously blocked dependent passages after repair; newly exposed issues belong to the same iteration. Missing essential connections block acceptance. Modest useful explanation is preferable to underteaching, but repeated baseline lessons, irrelevant details and obstructive scaffolding are also defects when evidenced. Length alone establishes neither.

Use the rewrite guide to repair actual causes. A document error does not automatically require a new PROF rule. If a present instruction was ignored, inspect its execution/recovery trigger; change the skill only when evidence supports that change. If a rule is absent or inadequate, record its observed trigger, concrete required action and the evidence that will establish repair. Do not insert lecture-specific answers into the general skill.

When the skill changes, freeze the actual candidate files and have a fresh author regenerate affected teaching from the original sources and task using that candidate. Do not pass the patched passage as an answer template. A manual repair alone does not establish that the skill produces the repair. Run a fresh SASIS reader on the complete regenerated document, and independently check correctness and affected previously successful passages. Preserve every version and report. Candidate files may be stored at an immutable Git tree/commit before the final branch publication.

## Closure, publication and next iteration

Close an iteration only when the complete required audit is covered and every supported material issue has a verified repair or evidence-backed resolution, including newly exposed issues and affected earlier successes. Pending external facts, inaccessible required sources or unresolved questions remain pending and prevent an unqualified completion claim. Continue independent useful work without pretending the blocked iteration is closed.

At closure save source/coverage records, incoming/outgoing skill revisions, complete document versions, admission/access records, original reader reports, independent technical audit, issue dispositions and concise change log. Push all justified skill edits and iteration evidence to GitHub, verify the new branch commit, reload the published skill, and start the next session with a fresh authoring/reader cycle. For this run, the user's rolling-version instruction requires the next cumulative version identifier at each valid closure, even when no substantive teaching-rule change is warranted. Publish the evidence and record that outcome honestly; a progression identifier is not evidence of improved teaching. Never invent a defect or teaching clause to justify the increment.

Maintain the entire corpus queue across resets. Later skill changes invalidate affected earlier checks; record the dependency and reopen those cases before final corpus acceptance. Local retries of A do not replace the new-material B iteration. Do not stop a full-corpus run merely because an early document is adequate. If a real external limit or user instruction prevents continuation, save the exact active state and next action and report the unfinished scope honestly.

After recovery, reread current GitHub PROF, this protocol, exact user constraints, the run index and necessary original sources/artifacts. Do not treat summaries or past all-clear assertions as current evidence. The fresh reader still receives only its two authorised content inputs.

## Durable records

Keep author/orchestrator records outside reader inputs, for example `runs/<run-id>/`. Use a small recovery index, full queue, sharded session evidence and immutable original reports. Record actual conditions rather than ceremonial logs. Hashes prove identity, not explanatory sufficiency.

The concise iteration log identifies material, incoming/outgoing revision, all justified skill changes and result. It links to the detailed issue register. At corpus completion provide the final effective PROF and the change log, with actual verification limits. Distinguish protocol editing, author checks, SASIS reading, rendered-artifact checks and human learning evidence.
