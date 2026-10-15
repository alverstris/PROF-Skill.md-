# Same-surface unread-baseline-revisit supplement

This isolated non-subject preflight fills the independent review gap in the sealed r41 candidate: the original candidate tested unread baseline revisits directly at the fixed launcher, while its successful minimal-surface route tested only already-read revisits. No candidate code change is proposed by this supplement.

One explicitly authorised bootstrap was executed as its exact rendered `bootstrap.js` source through the actual `functions.exec` interface. It independently verified and retained the invoker under a fresh key. Before the first retrieval call, the runtime, state and access ledger were absent. The sole retrieval invocation was the exact two-line `unread-revisit-call.js` source:

```javascript
const STEP_ID = "RB002";
await eval(load("prof.reader.r41.unread_revisit.supplement1").invoker_source)(STEP_ID);
```

No baseline step had yet run, so target `B002` was unread. The actual call failed with `launcher rejected/failed: {"error":"baseline revisit target not yet read","ok":false}`. The preserved runtime contains exactly one `launcher_rejected` event for RB002 and no state file. The effective cursor stayed zero; the baseline-read set stayed empty. There were zero subject-open attempts, Python subject-open audit events, bounded reads, verified accesses, output-prepared events, delivery receipts or figure-view receipts. The failure was preserved without reset, recovery or retry. Later activity was read-only inspection and evidence sealing.

The fixture texts and figure are exact copies of the earlier non-subject fixture. The verifier, receipt/audit helpers and all source templates are byte-identical to the reviewed candidate. The launcher differs only in its three permitted fixed route/runtime constants; the adapter differs only in its four permitted fixed constants. Derived invoker/bootstrap/call/instruction sources match after normalizing only fixture root, store key and sealed core digest. Route metadata differs only in absolute fixture paths. `identity-normalized-comparison.json` records all 16 checks. The retained envelope read back from `functions.store` matches the independent canonical proof exactly.

`reviewed-candidate-before.json` records all files in the sealed candidate before preparation. `reviewed-candidate-unchanged.json` verifies the same inventory and exact bytes afterward, including its original review seal, package proposal and successful/failed fixtures. All writes for this supplement are confined to this new subtree. No production reader, subject file, bound input, live runtime, installed skill, repository, teaching generation or publication was accessed or advanced.

The interface limit remains unchanged: the retained invoker expression evaluates before its current canonical identity comparison; tested checks precede dependent subject access, but this is instruction confinement rather than pre-evaluation authentication or a tamper-proof boundary. Root must review this supplemental evidence and the independent review before publishing r41. Fresh generation and a complete fresh reader run remain pending.

The authoritative result is `verification.json`; exact source/error/state evidence is in `bootstrap.js`, `unread-revisit-call.js`, `actual-functions-exec-return.txt`, `bootstrap-retained-envelope.json`, `after-bootstrap-before-call.json` and `runtime/access.jsonl`. `SUPPLEMENT-SEAL.json` pins those records and the complete separate inventory.
