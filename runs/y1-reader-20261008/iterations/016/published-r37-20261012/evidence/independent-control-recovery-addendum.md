# D016 r37 targeted control-recovery addendum

All 88 targeted checks pass. Seven late-preserved control-result records contain 39,777 output bytes that exactly match the seven permitted frozen control files. The original reader report, completed ledger, parse-failure disclosure and initial final-audit seal are unchanged. The prior 2,537 subject-access checks were not repeated.

| Control | Reported original chunk ID | Complete output bytes | Match |
|---|---|---:|---|
| reader-operating-instruction.txt | 5378a0 | 6591 | Exact |
| dispatch-instructions.txt | 757c48 | 8437 | Exact |
| chronological-route.md | a324fe | 7536 | Exact |
| view-invocations/view-F01.js | 2a0d63 | 4302 | Exact |
| view-invocations/view-F02.js | 49c18e | 4305 | Exact |
| view-invocations/view-F03.js | 0f32a8 | 4300 | Exact |
| view-invocations/view-F04.js | f899b9 | 4306 | Exact |

The current absence of separately archived control outputs is remedied by these seven late files. Every record has the expected exposed exec-result fields, exit0, a distinct reported chunk ID and complete output without truncation. The controls themselves still match the original route-packet hashes. No source teaching bytes or reader result were regenerated or changed by this auditor.

Provenance must remain precise. The reader states these are copies of seven already-exposed native transcript result entries, not live original JavaScript objects: the original isolates ended and functions store was not used. The recovery record states no file was reread and no command/script rerun. This auditor has the late records and frozen control files, not independent direct access to the original reader transcript. Therefore exact content consistency is established; independent authentication of original IDs, command argv, timestamps and read order is not. The exposed result objects do not contain argv/timestamp fields. No fabricated host attestation is inferred or claimed.

Late preservation does not retrospectively satisfy immediate separate archival at read time. The original report’s disclosure and the initial final audit remain intact; this addendum narrows their current missing-file condition without rewriting the historical lapse.

Root’s final-disposition.md explicitly records the output-only recovery: retain the exposed report-write parse failure and successful pinned original report, and accept the recovered report output for audit. No new reader is required solely by that report-write error. The existing error-text record remains unchanged; provenance says no additional structured host error object is available, and none is manufactured. Content adjudication and the independently required next revision remain root’s responsibility.

No subject reread, fixture repetition, browser, image view or route execution occurred in this targeted audit. The reader’s claim of no recovery rereads is preserved as provenance, not transformed into proof of technical confinement. No semantic-comprehension or substantive-acceptance conclusion is made.

| Preserved identity | SHA256 |
|---|---|
| Recovery provenance | 96c5dd9a511c6296046d534ceec3926e2a248966565f82327aaaa5d8835d5493 |
| Initial final-audit output manifest | 05507374e3eff79194d114630e816053cd3541020228aa3f1a777c9f1f0461ef |
| Original reader report | b169f65f634e1206dc4fde728a76f34970c94d1164cc049ae6102ea7909f4d1e |
| Original completed ledger | 96b57ce9c6813e3956cb18263891a68a69a1598ed0492c932fd474355c9449f1 |
| Original parse-failure disclosure | 8c5ef0fc393f79c5fa8198564e2030f2625bea1d4402a29a8b16bffc315f7b6c |
| Coordinator disposition as inspected | bffc17ae5a5f2da5ef7a65f581b9c063d535bb7b74363d32e7543796c18bfa03 |

verification.json contains all 88 checks, every late-record identity, complete output digests, original-seal checks and the precise coordinator recovery paragraph. audit_addendum.py is the targeted read-only verifier.
