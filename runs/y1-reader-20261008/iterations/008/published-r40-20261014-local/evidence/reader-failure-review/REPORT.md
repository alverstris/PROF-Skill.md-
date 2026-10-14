# Terminal D008 r40 reader execution: independent audit

A material reader procedure failure is established by the preserved original reader account, with its incomplete prefix independently corroborated by the exact current runtime ledger and state. The reported B0024 invocation altered fixed wrapper logic beyond the authorised STEP_ID datum. It necessarily rejects an expected valid verifier proof before adapter evaluation. The procedure stopped before completing the initial baseline, so no teaching verdict from this reader is admissible. This establishes an execution failure, not a teaching defect or an actual sealed adapter/binding mismatch.

Evidence classification matters: the exact failed call and printed exception come from reader-report-original.md, preserved from the reader’s original return. reader-report-preservation/comparison.md is the same reader’s comparison with its available conversation response, with an explicit terminal-newline serialization limit. No independent session tool-call transcript was supplied or consulted in this review. The local runtime ledger independently supplies the instrumented prefix records described below; it is not a comprehensive host/tool transcript or proof of confinement.

| Evidence | Bytes | SHA256 |
| --- | ---: | --- |
| Original reader report | 9713 | `e3ebb4470b0d91e149e13ca3d4e564986ec1804be8e3690cf70df285431ba749` |
| Reader preservation comparison | 1437 | `dc1a19d67bc30190ea525a08150fbc85923e7d52ed04c68462603f54e44e8e26` |
| Frozen route | 20800 | `940bb751e8f8146ab41747c79ae20132929d1b7155cb8663cd5c113c90ff49dc` |
| Sealed operational core | 1784 | `bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184` |
| Canonical short_call.js | 1853 | `6e95721167265abf588e82d09d74cdd6b866b82983d7d1148cd5ca8af7bd0417` |
| Runtime access.jsonl | 50961 | `a214ceef8df4283c12e7be733c84afd639ae61586ca56a584585c329c5a8bd1f` |
| Runtime state.json | 351 | `8b16b90a28688da5da56ec9bbee69ab16e8ee00853c06b2f15d13328d104ce69` |

The original report has 9701 decoded characters and one terminal LF. Its actual saved hash and character count agree with the preservation comparison. That agreement preserves the stated evidence boundary; it does not independently establish the underlying message’s raw serialization.

The frozen route contains 77 scheduled steps: 45 baseline text slices, 17 main-text slices, six hint slices, six solution slices, and three complete figures. Every route file’s complete bytes and SHA256 match the sealed identity, and every one of the 77 declared byte-range hashes matches the actual current input bytes. All 24 files in binding-inventory.json match their declared identities. The eight core-bound operational files also match the sealed core, including launcher, adapter, verifier, receipt helper, templates and route. The canonical wrapper itself remains unchanged.

Exact observed prefix: runtime/access.jsonl contains 161 events, arranged as 23 consecutive seven-event groups, for B0001 through B0023. Each group has subject_open_attempt → python_subject_open_audit → subject_open_succeeded → bounded_bytes_read → verified_access_receipt → launcher_output_prepared → text_output_delivered. For every group, the subject-open path is the bound baseline file; requested/target IDs, offset, requested and actual lengths, end position, SHA256, cursor-before/after, file ID, and delivered output receipt match the corresponding frozen-route step. All 23 preserved report table rows match these route and ledger identities. Timestamps are monotone.

This is contiguous baseline coverage [0,124245), beginning with B0001 [0,2182) and ending with B0023 [118601,124245). The baseline’s complete size is 247840 bytes; [124245,247840), 123595 bytes in 22 scheduled steps, remains outside the logged delivered prefix. State has cursor 23, exactly B0001–B0023 in baseline_read, and pending_figure=null. The next scheduled step is B0024, start 124245, length 5403, SHA256 7a6eb82ff0511cb213a2562e531dad088d451f487c44f0531b51acc7796d1038.

No B0024 subject-open/read/access/output event, baseline revisit, teaching-file read, figure invocation/result/output receipt, or cached image exists in the preserved runtime. Runtime contains only access.jsonl and state.json. Thus the logged reader route contains zero main, hint, solution or figure steps. The reader also reports that none was retrieved. This is a statement about these records; absence of a logged event is not proof that unlogged outside access was impossible or absent.

Exact failed-call comparison, after changing only the canonical STEP_ID datum from B0001 to B0024:

```diff
-p.schema !== "prof-reader-reuse-proof-v1"
+p.schema !== "prof-reader-reuse-store-v1"
```

That line-nine string literal is the only non-datum difference. Every other character is identical, including whitespace, LF line endings, and the terminal newline. Each compared body has 1853 UTF-8 bytes and eleven LF-terminated lines. The line-four cached.schema comparison already uses prof-reader-reuse-store-v1 in both bodies; it was not changed. failed-call.diff preserves the complete unified diff. The independently delegated bounded comparison reached the same result; both compared bodies agree byte for byte with that reviewer’s files.

verify_reuse.py constructs the nested seal with schema prof-reader-reuse-store-v1 and the returned top-level proof with schema prof-reader-reuse-proof-v1. The altered top-level comparison therefore becomes true for an expected valid proof, even if every other comparison passes, and throws before the later eval of adapter_source. The error text “cached adapter/binding identity mismatch” consequently cannot establish an actual artifact mismatch. The report does not separately preserve the historical verifier output, so the static analysis does not prove which other disjuncts were false on that particular invocation. The verifier’s inspected dependencies perform metadata-only load_config in this proof path; adapter-driven subject retrieval appears only after the throwing guard.

The fixed operating instruction expressly permits changing only STEP_ID and prohibits editing wrapper/hash/retrieval/receipt logic. The deviation is material because it stopped retrieval with the initial baseline incomplete, making the required complete reader input unavailable. The subsequent stop preserved the failure; no retry, reset, repair, recovery or new reader was performed by this audit. It would be unsupported to classify the guard’s message as a proved corrupt adapter, source error, mathematical failure or teaching gap.

The existing audit_bound_run.py was inspected and executed read-only with the bound Python executable, -B, and bytecode writing disabled. Its stdout is empty; it exits 2 and its preserved stderr contains:

```json
{"operational_route_audit_passed": false, "error": "route/display evidence incomplete"}
```

That is the expected whole-route failure at cursor 23/77. The existing whole-route auditor reaches its incomplete-route guard before its final full-run open/read count checks, so this review separately validated all 23 prefix open/read/output groups. The preserved command and result are in whole-route-audit-execution.json and the stdout/stderr files. Runtime, immutable operational files, subject inputs and original report were byte-identical before and after this audit.

Admissibility: no teaching correctness, accessibility, bridge, source-coverage, figure or help verdict can be admitted from this reader’s unfinished execution. There is no teaching reconstruction witness because teaching was not reached in the documented route. The independent technical teaching audit is separate evidence and cannot substitute for the missing fresh reader’s full reading. Root retains repair, fresh-condition, publication and acceptance decisions.

Limits: local open/read/output receipts support operational delivery evidence, not semantic inspection, human learning or a technical sandbox. The original report’s claims that all prior wrappers were unchanged, each functions.wait completed, bootstrap succeeded, the B0024 outer verifier ran, and no outside tools/files were used remain reader-return evidence to the extent no independent tool transcript is provided. The ledger does not record metadata-only verifier calls, so absence of B0024 there is expected if rejection occurred before adapter evaluation. No host-wide absence of unlogged access is inferred. Current identity matches cannot prove that no temporary unlogged change-and-restoration ever occurred. All writes for this review are confined to reader-failure-review/. Existing reader evidence, teaching, bound inputs, installed PROF, earlier sealed audits and repository were not changed.
