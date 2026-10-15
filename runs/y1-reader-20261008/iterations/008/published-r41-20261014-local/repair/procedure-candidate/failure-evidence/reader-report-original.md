Original SASIS reader report — D008 r40, frozen revision `2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce`

**Substantive admission is blocked by an execution/procedure failure.** I stopped during the attempted retrieval of `B0024`. The initial baseline was therefore incomplete, and no teaching text, hints, solutions or figures were retrieved. This report makes no teaching judgement about the frozen document.

The stopping event was my deviation from the authorised short call: I incorrectly changed the proof-schema comparison from `prof-reader-reuse-proof-v1` to `prof-reader-reuse-store-v1`. The resulting guard raised `cached adapter/binding identity mismatch; preserve failure and stop` before the adapter was evaluated. This is a reader execution error, not an established artifact, verifier or teaching defect. I did not retry, repair the call, use another access route, advance, reset, or reconstruct unread material.

**Inputs and condition**

The declared two subject inputs were:

- `OCR-A-4-subjects-r1` / `frozen-operational-20261007`, complete-artifact SHA256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`.
- `D008-r40-fresh-author-1` / `2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce`, with constituent identities supplied by the frozen route.

The route was `D008_R40_FROZEN_2102C1FC`, route SHA256 `940bb751e8f8146ab41747c79ae20132929d1b7155cb8663cd5c113c90ff49dc`. The condition was `D008-r40-instruction-confined-fixed-reuse-1`, with sealed binding `bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184`.

The one-time bootstrap completed successfully. Its displayed result included the bound operating instruction and:

```json
{
  "bootstrap_verified": true,
  "binding_sha256": "bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184",
  "bootstrap_sha256": "809825a68fe36747edc0bf89058702f92222832e0985df83ede191269cf2820c",
  "short_call_sha256": "6e95721167265abf588e82d09d74cdd6b866b82983d7d1148cd5ca8af7bd0417",
  "subject_retrieval": false
}
```

The bootstrap supplied no subject content. I subsequently used the authorised short-call body for `B0001` through `B0023`, changing only `STEP_ID`. Those calls delivered their scheduled baseline text and receipt metadata in order.

**Chronological access and displayed coverage**

Each row below represents one successful ordered subject retrieval. Every receipt reported `file_id: "BASELINE"` and `baseline_revisit: false`. Each call returned a running cell with the scheduled text already displayed; its subsequent `functions.wait` returned `Script completed` with no additional output. No text delivery in these steps was marked truncated or missing.

| Step | Zero-based byte start | Displayed byte length | Displayed receipt SHA256 | Cell completed through wait |
|---|---:|---:|---|---:|
| B0001 | 0 | 2182 | `46173fbf1387e9a2611b28670bd4f4d355031c2596fed54f981e4a0bb4e8f6d1` | 2 |
| B0002 | 2182 | 5836 | `cfb556d8b4ebb439a96e0fa5287ff65ae4807a28adbb5c5e2f3e286776503dc6` | 3 |
| B0003 | 8018 | 5963 | `e506e6edcbcf71aa5151d3a900eed2a8242f998872f4ea89c00e592770286add` | 4 |
| B0004 | 13981 | 5790 | `03e58e1c01991fa2cdfc90944f957c050a552a738b62ddd531d34e57979ac934` | 5 |
| B0005 | 19771 | 5900 | `f8f0f60f9744294abe2bac1456c1b8e2b88b5ea2410e8eef8411f7c4d9aaf051` | 6 |
| B0006 | 25671 | 5518 | `6d805eeed7cebff56b99eca7c1d6dd20b47bf53a57a9d99e3e57352f5b611616` | 7 |
| B0007 | 31189 | 5417 | `8b6df3d602569dc533cf6ae3e5fc71381761b056729b18de9a2a80872efc1b82` | 8 |
| B0008 | 36606 | 5770 | `f4a984400b65693d4270848a0fd2ee0b12ab775da212289c0532b6ddd7ebe7ae` | 9 |
| B0009 | 42376 | 5224 | `a829529078040eccee43d37259d5b36afd59af05af43517baea5e17b92c12023` | 10 |
| B0010 | 47600 | 5567 | `03f59c81ec04903fd4ea74d4b7d2f6ce977beb67f9f4a6ff862c2f26e01aea57` | 11 |
| B0011 | 53167 | 5460 | `c845562f3ffe783121c2aca35f8b48203fa369226656b388044c2acd7742a3dc` | 12 |
| B0012 | 58627 | 5245 | `2ff94eeee61e65355c653518fcd9ad3be08d505466279b5b722a1a2f3e161848` | 13 |
| B0013 | 63872 | 5893 | `0805241fc1a25865d1e3ec49de0d3cb8743fcd74157902636b6f75f15d33749f` | 14 |
| B0014 | 69765 | 5484 | `390715f651da9f3e61dc0d6f0e29e916bf7ffa8216fe670468df9b690ffdaead` | 15 |
| B0015 | 75249 | 5523 | `25fc2b0059fe97df561599fce0e1999b046c6ea6466135150ca94fb5edcc8cd8` | 16 |
| B0016 | 80772 | 5655 | `af2dac234afb6cd073226c382d422ce1f788b571da11380017f3450887a3da1d` | 17 |
| B0017 | 86427 | 3683 | `7538ace5e9412e92836d56d1b6ab69e88a16152407d95397051afa133192a4b4` | 18 |
| B0018 | 90110 | 5514 | `ded859dfcfa136677d5f435575d3d5ebb263aeb51c6b1d333265b217b1650e86` | 19 |
| B0019 | 95624 | 5881 | `8cdd0beb147b2362084e97e7ca2718ac41a51312692a7a7b4a2de44052d69c46` | 20 |
| B0020 | 101505 | 5791 | `bf63f9f2400b9fab280c73fb1a9157e42abc845fa5ef22bd598e3d2c5a09e308` | 21 |
| B0021 | 107296 | 5497 | `45b7784ab2923a69224f08352476913f1fc2a632c943c81469c0aafe918283e8` | 22 |
| B0022 | 112793 | 5808 | `fb02037092dd8886302a8a0d76225633a8a5cd8c7a4fffeeec2792b12abf957d` | 23 |
| B0023 | 118601 | 5644 | `ea8bd43e7386bec99ee88ba32f73a815e89cb313cf8a0f01b5b15fb9e0ac1968` | 24 |

This is contiguous displayed baseline coverage of bytes `[0,124245)` out of the declared `247840` bytes. It comprises the baseline cover, the complete Mathematics and Further Mathematics sections, and the Physics section through the end of the ideal-gas paragraph in `B0023`. The remaining baseline bytes `[124245,247840)`, including later Physics and Chemistry, were not displayed or read.

The attempted next step was `B0024`, but its adapter did not execute. The outer verifier command was called and returned far enough for the wrapper to parse its proof and reach the incorrect schema guard. Its output was not separately displayed. No `B0024` subject receipt or subject text was delivered, and I do not count it as subject access.

No baseline revisit was used. No teaching step `M0001`–`M0017`, figure `F01`–`F03`, hint `H0001`–`H0006`, or solution `S0001`–`S0006` was accessed. There were no actual figure view results or delivered figure-image receipts. There was no accidental early teaching exposure or delayed figure inspection because teaching was never reached.

**Exact stopping call**

The following is the exact failed `functions.exec` body. It is reproduced as an execution record, not as a repaired or authorised replacement:

```javascript
const STEP_ID = "B0024";
const cached = load("prof.reader.d008.r40.2102c1fc.condition1");
if (typeof STEP_ID !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(STEP_ID)) throw new Error("exactly one plain STEP_ID is accepted");
if (!cached || typeof cached !== "object" || Array.isArray(cached) || cached.schema !== "prof-reader-reuse-store-v1" || cached.binding_sha256 !== "bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184") throw new Error("missing/stale reader bootstrap; preserve failure and stop");
const r = await tools.exec_command({cmd: "$v='C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r40/reader-inputs/verify_reuse.py'; if ((Get-FileHash -LiteralPath $v -Algorithm SHA256).Hash.ToLowerInvariant() -ne '3a7fcbe5b0ef4814bca83877cd3fec2d6628be34376c6bc2f2bb24bc2c716ca1') { throw 'verifier identity mismatch' }; & 'C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe' $v 'step' 'bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184' '" + STEP_ID + "'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader operational identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("verification output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "mode,schema,seal,step_id" || p.schema !== "prof-reader-reuse-store-v1" || p.mode !== "step" || p.step_id !== STEP_ID || JSON.stringify(cached) !== JSON.stringify(p.seal)) throw new Error("cached adapter/binding identity mismatch; preserve failure and stop");
// Only the exact verified operational source enters eval; STEP_ID is a parameter, never source text.
await eval("(async function(STEP_ID) {\n" + p.seal.adapter_source + "\n})(STEP_ID)");
```

The exact displayed result was:

```text
Script failed
Wall time 0.8 seconds
Output:
Script error:
Error: cached adapter/binding identity mismatch; preserve failure and stop
    at exec_main.mjs:9:225
```

The consequential altered expression is the line-nine comparison:

```javascript
p.schema !== "prof-reader-reuse-store-v1"
```

The authorised comparison was against `prof-reader-reuse-proof-v1`. My altered guard therefore cannot establish a mismatch in the sealed adapter or binding. It establishes that this invocation departed from the fixed procedure and stopped before subject retrieval.

**Assessment status and limits**

- Established execution defect: the reader changed wrapper logic during the `B0024` attempt, contrary to the fixed-call requirement.
- Established teaching defects: none assessed; the teaching input was not read.
- Provisional teaching concerns: none assessed.
- Reconstruction witnesses for teaching conclusions: unavailable because no teaching conclusions were encountered.
- Whole-document chronological coverage: incomplete at the initial baseline stage.
- Figure inspection coverage: none reached.
- Substantive admission: blocked pending root’s audit and separately authorised access repair or fresh-reader recovery.

I used no browsing, other-agent messaging, other-file inspection, searches, source/author/history material, alternate retrieval, subject execution, or recovery attempt. Root owns any next condition and the preservation of this original report unchanged.
