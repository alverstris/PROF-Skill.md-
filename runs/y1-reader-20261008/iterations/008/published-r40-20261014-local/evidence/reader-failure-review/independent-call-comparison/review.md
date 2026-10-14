# Independent static comparison of the reported failed call

This is a bounded procedure review for D008 r40, frozen revision `2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce`. It compares the call text reproduced in `reader-report-original.md` against `reader-inputs/short_call.js`, after making only the authorized datum substitution `STEP_ID = "B0001"` to `STEP_ID = "B0024"`. It also inspects `reader-inputs/verify_reuse.py` to determine the expected valid proof schema. It makes no teaching judgment, no acceptance/publication decision, and no recovery recommendation. Root retains those decisions.

## Report identity and preservation boundary

- Saved original report SHA256: `e3ebb4470b0d91e149e13ca3d4e564986ec1804be8e3690cf70df285431ba749`.
- Saved original report length: 9713 UTF-8 bytes; 9701 decoded characters.
- This measured hash and decoded character count match the figures stated in `reader-report-preservation/comparison.md`.
- That preservation comparison attests to matching the visible original response available in the reader's context, with a stated terminal-newline serialization boundary. It does not supply an independently observed tool transcript. This review does not convert that attestation into independent runtime evidence.

The original report, preservation comparison, authorized call, and verifier were read without alteration. Their complete measured identities are recorded in `comparison-evidence.json`.

## Exact comparison result

There is exactly **one non-datum textual difference**, at line 9 of the JavaScript body:

```diff
-p.schema !== "prof-reader-reuse-proof-v1"
+p.schema !== "prof-reader-reuse-store-v1"
```

This is exactly one string-literal replacement, `prof-reader-reuse-proof-v1` to `prof-reader-reuse-store-v1`, in the post-verifier guard. The original `B0001` to `B0024` substitution is the allowed datum change and is excluded from the non-datum count.

All other characters are identical after that datum substitution. In particular, the cache/store schema check on line 4 already uses `prof-reader-reuse-store-v1` in both versions; it was not changed. The verifier command, verifier hash, binding hash, cache key, output limit, proof key-set check, mode and step checks, seal equality comparison, thrown error, comment, and adapter evaluation are unchanged. There are no whitespace, line-ending, or terminal-newline differences in the compared call bodies. Each body is 1853 UTF-8 bytes over 11 LF-terminated lines, with zero CR characters. These statements were checked without whitespace normalization.

`exact-call.diff` contains the full unified diff with surrounding source lines. `authorized-call-B0024.js.txt` and `reported-failed-call.js.txt` preserve the two compared bodies. The reported body was extracted from the first JavaScript fence following **Exact stopping call** in the saved original report; its fence-body terminal newline was retained.

## Consequence for an expected valid proof

The inspected verifier constructs two distinct schema-bearing objects:

- At `verify_reuse.py:83`, `seal.schema` is `prof-reader-reuse-store-v1`.
- At `verify_reuse.py:87`, the returned top-level `result.schema` is `prof-reader-reuse-proof-v1`.
- In `step` mode it supplies `result.step_id` at line 92, returns the object at line 93, and serializes it as the verifier output at lines 102–103.

For the expected valid `step` proof for `B0024`, the top-level schema therefore equals `prof-reader-reuse-proof-v1`, and the sorted top-level keys equal `mode,schema,seal,step_id`. Even if the cache and seal match and every other condition is valid, the changed line-9 condition evaluates `"prof-reader-reuse-proof-v1" !== "prof-reader-reuse-store-v1"` to `true`. The disjunction consequently enters the throw. This rejection is necessary for any expected valid proof produced by the inspected verifier; it does not depend on the adapter source or its equality with the cache.

The wrapper evaluates `p.seal.adapter_source` only on line 11, after the throwing guard. If execution reaches the altered line-9 guard with the expected valid proof, adapter evaluation is unreachable, so the adapter-driven subject retrieval cannot occur in that invocation. The inspected code supports this ordering without executing the wrapper, verifier, launcher, or adapter.

The altered guard therefore rejects valid proof data by confusing the outer proof schema with the nested seal/store schema. Its error text cannot, by itself, establish that the sealed adapter or binding actually mismatched. Conversely, this static consequence does not establish that every other comparison was true in the reported real invocation: an earlier disjunct could also have been true, and the verifier output is not reproduced separately in the report.

## Evidentiary limits

The failed JavaScript and displayed exception are reader self-report in the saved original report. No independent tool transcript was supplied or consulted. This review independently establishes the text difference, input-file hashes, the inspected verifier's expected schema, and the conditional control-flow consequence. It does not independently establish that the reproduced call was actually submitted, that the displayed error came from that submission, that the verifier returned the expected valid proof on that occasion, or that the claimed successful `B0001`–`B0023` retrievals or absence of `B0024` output occurred.

The ordering conclusion is specifically that the wrapper does not reach **adapter evaluation** after receiving an expected valid proof. The verifier invokes an imported launcher module and its configuration loader before returning; this bounded review did not inspect those dependencies or execute them. Its claim of metadata-only operation is visible in the verifier source and in comments, but absence of all possible side effects in uninspected dependencies is not independently proven here. Thus an unconditional historical claim that no subject access occurred anywhere is beyond this review's evidence.

No reader runtime was executed or mutated. No launcher/adapter execution, subject retrieval, repair/retry, teaching/source inspection, receipt validation, or SASIS adjudication was performed. The only writes were review artifacts under `reader-failure-review/independent-call-comparison/`.
