# D008 r39: narrow PROF repair candidates

Prepared 2026-10-14 as read-only analysis. No installed skill, teaching, source, publication, dependency or runtime was changed. The only new artifact is this analysis under `repair-analysis/`. Root must integrate the complete fresh SASIS report and actual destination review before deciding the complete r40 change set. These proposals do not assert D008 acceptance or a complete r40 diagnosis.

## Inputs actually inspected

- Installed `C:/Users/alver/.codex/skills/prof/SKILL.md`, version `2026-10-14-r39`, completely; `references/execution-protocol.md`, `references/sasis.md`, `references/sasis/rewrite-guide.md`, and `references/findings-and-rationale.md`, completely.
- `technical-review/full-audit.md`, `fresh-author/evidence/author-audit.md`, and the actual scope record `fresh-author/evidence/execution-scope-finding.json`, completely. The scope record is not at the iteration root.
- Exact frozen teaching passages: main.md 118–140, 183–187, 370–380, 439–443 and 525–532; solutions.md 196–201. The original slope crop `technical-review/source-slope-crop.png` was viewed at original resolution. Its numerator visibly contains `−5`.
- `run-state/root-original-source-check-correction.md` and `run-state/iteration-start-installation-verification.json`; maintenance installer source `../../.prof-maintenance/20261014/download_and_install_prof_iteration_start.py` and prior `installation-verification.json` were read. The relative maintenance locator is only descriptive; the absolute maintenance directory is `C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-maintenance/20261014/`.
- Read-only SHA256/inventory comparison of the current installed PROF, the recorded `20261014T181500Z-r39-before-iteration` backup and the retained `staged-prof-15f0b916d8a6` stage against all 36 entries in the iteration-start record. All three currently have exactly 36 matching files, no different/missing files and no extra files. This independently supports present identity, not the historical timing or success of every individual mutation.

These are execution refinements from the observed run, not new experimental claims about teaching or learner outcomes. No fresh literature claim is needed. Ordinary teaching mode keeps its existing local-document repair; explicit self-iteration keeps its existing frozen-teaching / PROF-only repair and publication-first regeneration.

## Classification and bounds

| Issue | Verified failure | Existing obligation | What needs repair |
| --- | --- | --- | --- |
| I01 | Main 137 and 530 falsely attribute a positive derivative sign to the original. The original and independent correct derivative both have the negative sign. | T10 source-claim verification; T12 truthful provenance; execution-protocol 25 already requires original-visual checking. | Existing rule insufficiently executed. Add a specific comparison before an assertion that the source is wrong. Correct-result derivation alone cannot prove what the source printed. |
| I02 | Main 378 prints an inaccurate direct-evaluation decimal despite the right formula and estimates. The independent technical and final author readback both detect it. | T10 independently verifies important calculations; execution-protocol 71/75 already requires verification. | Existing rule insufficiently executed at the final printed value. Make the final formula/input/rounding comparison an explicit step for numbers used as validation. |
| C01 | Five strict-comparison commands omit the explicitly required terminating space: main 127, 186, 441, solutions 198 twice. | SKILL.md 111 already states the exact syntax. | Existing explicit syntax rule ignored. Reuse the complete source expression inventory for a concrete conformance scan. The missing spaces are not evidence of rendering loss. |
| E01 | A default dependency installation wrote packages and scripts into the shared bundled Python outside the worker's explicit fresh-author write boundary. | Exact delegated constraint; SKILL.md 46/48/131 preserves user constraints and task scope. | The boundary was ignored, and dependency recovery has no operative destination check. Teach the worker to count installation/cache/configuration destinations as writes and choose a permitted route. |
| S01 | Directory rename was blocked, then an equivalent file-content replacement reached a verified exact package. The installed package is not shown to be wrong. | SASIS sync 26 prescribes whole-directory replacement to prevent obsolete files; 27 requires complete inventory/byte verification. | A method mismatch and an undocumented fallback, not an installation-identity failure. A narrowly bounded equivalent-state fallback is justified if root chooses to make the recovery reusable. |

Do not invalidate the correct derivative, coefficient, linear/quadratic model, complete task answers or improvement conclusion merely because I01/I02 exist. Do not allege a rendering defect from C01. Do not uninstall the shared packages: the recorded root disposition explicitly leaves them in place. Do not treat S01 as a failed package identity when the byte evidence says otherwise.

## Candidate A: source-error attribution

Proposed location: `references/execution-protocol.md`, immediately after the current paragraph at line 25 under “Source-portion accounting and bounded work”. Keep that paragraph; this addition supplies its missing conditional execution trigger.

Exact proposed text:

> Before claiming that an original source contains a typo or error, reopen the exact disputed passage in context and at sufficient resolution to distinguish its consequential glyphs. Record what the original actually states separately from any extraction and from the independently checked result; retain the source-error attribution only when that verified original and the proposed correction actually differ. A correct derivation establishes the result, not what the source printed. If the original remains unreadable, preserve that uncertainty and teach only the independently supported result without asserting an unverified source correction. Check every retained correction attribution, including closing provenance summaries, against that comparison.

Trigger: a proposed learner-facing or author-evidence claim that the original source is wrong. Action: inspect the original text/pixels and compare the actual statement with the proposed correction, separately from the result derivation. Observable check: every retained attribution has the exact source locator and original/corrected comparison; repeated summary claims agree with it.

Rationale: the existing extraction rule was read and the original source was reportedly viewed, yet the small minus was misread. Both root's old source check and the lesson inherited that false premise. The discriminating missing operation is comparing the actual original with the proposed correction, rather than taking a correct recalculation as proof of a typo. This applies to original digital text, notation, scans and figures without prescribing one image tool.

Risk control: do not enlarge every source or mandate duplicate independent source reviews. Trigger this only for an error attribution, and inspect at sufficient resolution, not an arbitrary zoom factor. Unreadable evidence should yield a qualified attribution, not an invented correction or unnecessary refusal to teach a verified result. The actual mathematical error in other source passages remains separately auditable; this repair does not rehabilitate every source statement.

Affected successful behavior to preserve: genuine independently established source corrections, course notation, concise routine algebra and the correct local models. In fresh r40 output, inspect all retained source-error assertions against the original; absence of the false attribution alone does not certify the full document.

## Candidate B: final numerical validation values

Proposed location: `references/execution-protocol.md`, a new paragraph immediately after current line 75 and before the current full-topic/help paragraph at line 77. This specializes the existing independent-answer check and keeps it beside reconstruction.

Exact proposed text:

> For a displayed numerical value used to check or validate an answer, approximation or model, recompute from the actual learner-facing formula and stated inputs, retaining enough precision to decide the claimed rounding. Compare the final printed value, units and precision with that computation, rather than only checking the symbolic formula or an intermediate result. Save a compact formula/input/result/rounding witness for the check; a copied plausible decimal cannot validate itself. If the calculation is only a loose estimate, state its supported precision accordingly. Recheck affected comparisons when the numerical check changes, following the active repair mode.

Trigger: a decimal or other numerical value presented as a direct/independent check of a result. Action: evaluate the actual formula/input with sufficient precision and compare the final authored representation. Observable check: the displayed value and units agree at their claimed precision with reproducible computation; any dependent comparison remains supported.

Rationale: T10 is already adequate at the policy level, and the author eventually found this defect. The omission happened between formula checking and the final published/checking decimal. The proposed step gives that interval a concrete acceptance witness. It does not embed the lecture's value or formula in the skill.

Risk control: do not demand high-precision arithmetic for every number, a full numerical dossier, or machine execution where a named manual check suffices. Use the precision and method the actual check requires. A loose estimate must be labelled honestly rather than forced into unsupported decimal places. A correct changed-task answer cannot excuse an unrelated wrong validation number.

Affected successful behavior to preserve: exact symbolic reasoning, existing short manual checks, the valid approximation estimates and bounded improvement claim. In fresh r40 output, check its actual displayed numerical validation values, including the final rounding; do not feed this old diagnosis or corrected decimal to the fresh author.

## Candidate C: strict-comparison syntax execution

Proposed location: `references/execution-protocol.md`, immediately after current line 85 (the complete source-to-destination mathematics inventory paragraph). Keep the existing SKILL.md 111 syntax contract rather than restating another universal formatting rule in SKILL.md.

Exact proposed text:

> For GitHub Markdown, use that source expression inventory to check the existing strict-comparison syntax rule in every mathematical payload: each `\lt` and `\gt` command has a terminating literal space, including before a digit or minus sign. Use a payload-aware scan or enumerate manually; record exact file/line violations and the final count, leaving literal code and HTML unchanged. Zero violations establishes this source-format requirement only. Record actual destination preservation separately; a syntax miss alone does not establish a rendering failure.

Trigger: GitHub Markdown mathematics governed by SKILL.md's existing strict-comparison contract. Action: apply a mechanical or manual command-spacing check to the existing complete mathematical payload inventory. Observable check: exact violations and a zero final count on the checked revision, separately from the actual renderer evidence.

Rationale: the five omissions all follow a command with a number or minus sign, so the author appears to have treated ordinary TeX command termination as sufficient. That does not satisfy the explicit space instruction. The existing 401-expression inventory already identifies the relevant scope; another inventory or generic “check formatting” instruction would add little.

Risk control: do not globally replace comparison symbols or edit code/HTML; do not use a raw whole-file regex as though all matches were mathematics. Do not classify these command forms as actual parse failure absent destination evidence. If root adds a scanner, the useful narrow checks are that it finds all five frozen misses and ignores literal code/HTML; no universal extra fixture battery is required merely to add this procedural text.

Affected successful behavior to preserve: correct inequalities, delimiter protection, math outside unsupported disclosure containers and the existing complete destination comparison. In r40, a syntax count cannot substitute for source-expression-to-rendered-expression matching or live visual inspection.

## Candidate D: dependency recovery within an explicit write boundary

Proposed location: `references/execution-protocol.md`, immediately after current line 11 under “Durable state and activation”. This activates after exact scope is recovered and before tool/dependency work. It applies to ordinary teaching and delegated authoring when the boundary exists, without making a bounded directory mandatory for every lesson.

Exact proposed text:

> When the task or delegated scope gives an explicit writable-directory boundary, include dependency installation and its package, script, cache and configuration destinations in that boundary. Before recovering from a missing dependency, identify those resolved write destinations. Use an already available suitable tool, or a task-local environment/installation with its writes directed inside the authorised subtree, and verify the package origin actually used. A default install into a shared runtime, user site or system directory is not permitted merely because that interpreter is available. If no feasible permitted route exists, record the capability limit, keep dependent production/checks unverified and report the specific boundary change needed. Save the actual command, destinations and origin check; separately authorised operations retain their own stated scope.

Trigger: dependency recovery within an explicitly bounded author/worker task. Action: determine installation and related destinations, use an existing capability or an in-boundary environment/target, verify the actual imported origin; otherwise preserve the capability limit and report the concrete need. Observable check: command/destination/origin evidence stays within the stated subtree or identifies a separately authorised operation. Absence of a module does not enlarge the boundary.

Rationale: the author honored output paths but treated a default package install into the bundled interpreter as environment setup rather than a write. The explicit task boundary was already binding; the missing operative check is dependency destinations before installation. The shared runtime installation is a real execution-scope failure even though it produced usable figures and did not alter teaching after freeze.

Risk control: do not ban dependencies or require approval for routine setup already within scope. Do not imply task-local import configuration alone redirects installer caches or generated library configuration. Redirect the writes actually used; choose an existing suitable tool when simpler. Do not silently switch to inferior figures, omit them or claim their checks passed. The explicitly authorised installed-PROF synchronization is a separate coordinator operation and must not be incorrectly blocked by a worker's narrower fresh-author boundary.

Affected successful behavior to preserve: dependency discovery, runtime reuse for read/import operations, honest partial capability reports and normal autonomous in-scope work. On fresh generation, inspect actual dependency-recovery commands and resulting origins if dependency recovery occurs; do not force an unnecessary install merely to exercise this trigger.

## Candidate E: bounded local-sync fallback

Recommendation: an explicit fallback is justified as an operational clarification, not as a newly discovered package defect. The stated purpose of whole-directory replacement is to prevent obsolete files surviving an overlay. The observed recovery established the exact same relative file inventory beforehand, preserved a backup, overwrote all 36 expected files from the verified stage and checked all final bytes. The evidence therefore supports successful package identity while also exposing an execution path the written procedure did not permit. Do not invent a failed installation verdict or hide the initial rename failure.

Proposed location: `references/sasis.md`, amend current step 2 at line 26 by appending the following text; retain the existing staged verification, exact destination, backup and preferred whole-directory replacement. Step 3 remains the mandatory final full check.

Exact proposed text:

> If a directory rename is blocked, preserve the actual failure. A file-content replacement is an allowed fallback only after a complete verified backup exists, the existing relative file inventory exactly matches the verified staged package, and the resolved write paths remain inside the authorised installation. Replace every staged file and perform the same complete installed-inventory, byte and manifest checks before generation; do not use a general overlay when obsolete or additional files are present. Record the fallback accurately rather than calling it a whole-directory replacement. If these conditions or verification fail, hold dependent generation under step 4.

Trigger: the authorised local synchronization cannot rename the installed directory. Action: preserve the failed attempt, use verified backup plus exact-inventory content replacement only in the demonstrated equal-inventory condition, then verify all installed bytes/manifests. Observable check: the record identifies the actual method and final installed package exactly equals the single pinned published package.

Rationale and bounds: do not mandate an alternate branch when preferred replacement succeeds, nor treat a transient rename failure as a reason to abandon already authorised local synchronization. The fallback is intentionally stricter than a general directory reconciliation: mismatched inventory does not permit arbitrary deletion/overlay. It does not claim atomicity or immunity to concurrent readers. If root requires an atomic directory transaction as the actual acceptance condition rather than exact package state before generation, this fallback is not equivalent and must be rejected; current wording gives obsolete-file prevention as its reason and requires post-replacement verification.

Historical evidence limit: the saved run-state record reports WinError 5 and states the original failed rename was preserved. The maintenance source contains the attempted directory rename but not the subsequent fallback implementation. I did not find a separate raw failure-output file through the narrow `.prof-sasis/` search. The current installed/staged/backup byte comparison independently establishes matching present inventories; it does not authenticate the original console event or every intermediate write. Root may have the original tool result in its conversation. Record that distinction if publishing the evidence.

## Integration guidance

The minimal recommended operative changes are four conditional paragraphs in `references/execution-protocol.md` (A–D). Keep T10, T11, the mode gate and rewrite-guide's general repair instruction; another copy of these rules there would be redundant. Candidate E is a bounded synchronization procedure clarification if root adopts the demonstrated recovery method. Version/manifest updates belong to the root's complete release, not this analysis.

Before publication, root still must reconcile the complete fresh reader report, source audit, literal syntax findings, execution finding and live destination results. Do not stop at these known defects or invent others from exposure inventories. Preserve the frozen document and reports. After publication, verify the complete skill package and local synchronization, then use a new author and reader with the existing clean-input restrictions. These findings stay outside their generation inputs; compare the newly frozen output in the later audit.
