D006 whole-iteration issue register — open checkpoint

Main remains r12. Five iterations closed; this record does not close D006. Originals and prior failed checks remain unchanged. Candidate findings are not inferred from v1 passes.

D006-S01: source error

Evidence: PDF3 prose and PDF4 Figure3 label (1,0); true vertical intercept is (0,1).

Disposition: Originals fully inspected; both v1 and current candidate use (0,1). Original lectures unchanged.

Records: source-review.md; lead-source-review.json; lead-technical-review-v1.md

Status: resolved in v1; candidate final check pending.

D006-S02: source error

Evidence: PDF5 inverse box has e^x=w after w=ln x.

Disposition: Correct inverse is e^w=x, checked by inversion and x=1. No course convention ambiguity.

Records: source-review.md; lead-technical-review-v1.md

Status: resolved in v1; candidate final check pending.

D006-S03: source scope

Evidence: Hyperbolic Functions appears in the title only; all8pages have been inspected.

Disposition: Scope accurately states absence of body content; no invented missing continuation or added assigned topic.

Records: source-review.md; lead-source-review.json

Status: resolved in v1; candidate final check pending.

D006-A01: pre-freeze teaching defect

Evidence: Original v1 TaskD asks initial derivative on t>=0 without the endpoint convention.

Disposition: Original preserved; final v1 prompt explicitly requests right-hand rate and solution derives right-hand quotient. This is not a defect automatically inherited by new generated tasks.

Records: task-clarification-v1.md; teaching-v1-pre-endpoint-clarification.md; lead-pre-solution-math-original.md; lead-technical-review-v1.md

Status: resolved in v1.

D006-A02: pre-freeze serialization and ordering

Evidence: Arrow-command tabs, missing quad backslash, and evaluation-bar explanation after first use.

Disposition: Author repaired before immutable freeze; original drafts preserved.

Records: teaching-v1-pre-readback-repairs.md; author-record.md

Status: resolved in v1.

D006-R01: independent reader result

Evidence: Complete fresh v1 reader found no substantive mathematical gap.

Disposition: Root read full unchanged original/access; correct reconstruction witnesses checked. Source provenance was appropriately left outside reader inputs. Not a typography pass or proof of human learning.

Records: reader-report-v1-original.md; reader-access-v1-original.json; reader-admission-v1.json; reader-disposition-v1.md

Status: admitted bounded v1 result.

D006-V01: representation-helper mismatch

Evidence: Initial prose equality retains Markdown table delimiters, whereas actual article contains parsed table; generic Q/H/S route checks not applicable to A–E.

Disposition: Initial failed and null results preserved. Separate exact-cell verification and complete syntax-normalized article comparison plus actual A–E routes resolve content/navigation question. Helper itself not silently altered.

Records: render-evidence/v1/capture-initial; render-evidence/v1/independent_audit.py; render-evidence/v1/independent_audit.json; render-evidence/v1/render-review-original.md

Status: resolved as review-method issue.

D006-V02: preview input failure

Evidence: First page2 PNG truncated despite exporter exit0.

Disposition: Original retained; complete page2 re-rendered from unchanged full PDF and actually opened. All8pages reviewed. Minor page seams retained as secondary-preview limits.

Records: render-evidence/integration-v1.json; render-evidence/v1/render-review-original.md

Status: resolved with disclosed secondary-preview limits.

D006-T11: confirmed destination defect

Evidence: Four v1 table headers receive semibold via actual linked .markdown-body table th CSS even without strong/em tags.

Disposition: V1 not accepted. Frozen candidate adds narrow destination-style trigger/action/check; fresh author regeneration then independent final route, fresh reader and representation check required.

Records: render-evidence/v1/css-typography-followup.md; skill-change-candidate1.md

Status: candidate repair pending verification.

D006-REG01: affected earlier success review

Evidence: New T11 trigger concerns destination-introduced prose emphasis.

Disposition: Independent whole accepted D001–D005 article/source identity and linked CSS checks found no matching structure; no earlier regeneration supported by this trigger. No new broad teaching or learner claim.

Records: prior-typography-regression/report.md; prior-typography-regression/integration.json

Status: resolved narrow empty affected set.

D006-C01: substantive candidate verification

Evidence: Candidate a2389390c0709d65af4a3cf070a04e396e4a4792 changes T11 and metadata only.

Disposition: Fresh fork-none author with original sources/full baseline/no old teaching or diagnosis. Root independent new A1–A6 calculations precede proposed answers. Final author evidence, immutable teaching freeze, full fresh reader and representation checks still needed.

Records: activation.json; lead-pre-solution-candidate1-original.md

Status: pending.

Remaining gates: final whole regenerated document and author evidence; immutable freeze; new fork-none two-input reader and complete access/report disposition; actual destination representation/style and full secondary preview; all new issues resolved; candidate-bound state reconciliation; final cumulative r13 metadata; expected-head publication, verification, full actual published PROF reload, then fresh D007. No installed skill or lecture original may be edited.

D006-C02: candidate destination serialization defect

Actual immutable GitHub article review reports32 inline comparison-sign payloads contain literal entity spellings and two inline/two display percent escapes lose their TeX backslash after ordinary single HTML parsing. Source mathematics remains independently correct; rendered math payload is a separate failure. Original candidate and checks remain unchanged. Author is making a minimal separate v2; verification of exact new article payloads and a fresh full reader are required. Existing correctness/output obligations require this repair; no additional skill instruction is justified merely by detection. Final original representation report is still pending at this checkpoint.

D006-C03: representation-only v2 fails destination pre-reader check

V2 is frozen at09e12f4fad9f3108ec62bd6918d239dc4f732490, SHA53a69398d757bfe20c062450aace5a405ad66664a7f749b8f1f1cbbe2703efc3. Root read the entire actual v2; exact forward and inverse checks confine its changes to equivalent math notation (lead-equivalence-candidate1-v2.json). New actual destination review reports exactly four failing payloads P177/P179/P182/P183: all nine introduced thin-space backslashes are dropped, leaving literal commas. Other333 mathematical payloads, prose, navigation and inspected CSS typography pass separately. Full source-faithful P179 preview page11 fits the text margins; no width repair is justified. V2 has no admitted reader or reader verdict because this pre-reader output gate failed. Separate v3 repair will preserve the word percent using a plain space within the text argument; fresh final destination and whole-reader checks remain required.

D006-C04: v3 renderer interruption

V3 immutable freeze and complete root read/equivalence are recorded in freeze-candidate1-v3.json and lead-review-candidate1-v3.md. The initial renderer saved an exact source/337-payload/prose/navigation check and source-faithful preview but ended without a final report or complete visual-inspection record. Recovery reviewer encountered capacity failures after saving recovered inputs and fresh raw/page retrieval. These are execution/input-completion limits, not evidence of a teaching defect. Preserve all saved evidence and complete remaining verification without inventing a prior verdict. D006 stays open and final fresh SASIS remains pending at this checkpoint.
