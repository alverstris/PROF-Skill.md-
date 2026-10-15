# Unpublished r41 retained-invoker procedure candidate

This bounded proposal addresses the verified r40 execution failure before teaching. At B0024 the fresh reader recopied the outer proof-schema comparison as `prof-reader-reuse-store-v1` instead of `prof-reader-reuse-proof-v1`. The existing guard correctly stopped; baseline reading remained incomplete and no teaching had been read. The saved original report and exact stopping call are preserved in `failure-evidence/`. The synthetic reproduction is labelled separately and uses stubs with zero actual launcher, subject or view calls.

The proposed repair removes schema, identity, retrieval, receipt and view logic from every repeated caller-authored cell. One explicitly authorised independently verified bootstrap retains the designated non-subject invoker source and seal. Each subsequent cell has the fixed two-line form below. The only permitted edit is the STEP_ID literal from the sealed route.

```javascript
const STEP_ID = "B001";
await eval(load("prof.reader.r41.synthetic.invoker1").invoker_source)(STEP_ID);
```

This is the exact tested synthetic form; its store key and step IDs are not production bindings. Subject bytes never enter an executable position. The reader never manually reconstructs any operational program or guard.

## Exact evaluation order and limit

1. The authorised bootstrap runs a fixed command that checks the metadata helper's exact SHA256 before Python executes it. That helper verifies the sealed core, route metadata, operational code, named templates and exact derived bootstrap/invoker/call/instruction. Its bootstrap proof contains the canonical invoker and adapter source. Bootstrap stores that envelope once and retrieves no subject.
2. A later minimal cell loads the envelope, selects `invoker_source`, and evaluates that function expression. It then invokes the resulting function with the STEP_ID datum. Missing storage can therefore fail at the property access before any invoker code runs.
3. Inside the reused invoker, argument count, ID shape and envelope binding checks precede a fixed metadata command. The command first verifies the helper file hash, then the helper independently reconstructs the current canonical seal. The invoker checks proof shape/schema/mode/STEP_ID and exact cached-envelope equality, including its own canonical source and digest.
4. Only after those checks pass does the invoker evaluate the canonical operational adapter. The preserved launcher, range/hash/order/delivery/receipt/view rules then govern subject access and route advancement.

The current retained invoker expression is not authenticated before it evaluates. A deliberately hostile replacement expression could execute before the in-program checks. The tested accidental source/envelope mutations stop before subject launcher/view access, but this is instruction confinement, not a tamper-proof boundary, sandbox, memory erasure or persistent callable. `functions.store` rejected a function value, and a `globalThis` function did not survive the next cell; exact observations are in `interface-probes.json`. The parent explicitly accepted this narrow evaluation/invocation surface rather than an unavailable persistent-function interface.

## Package proposal and installation boundary

`proposed-package/` contains five replacements for existing root-package files: `SKILL.md`, `references/sasis.md`, `references/sasis/student-role.txt`, `references/sasis/student-testing-contract.txt`, and `references/sasis/profile-manifest.json`. The four portable operational templates are exact named fenced payloads inside the existing `references/sasis.md`. They are extracted programmatically and verified byte for byte; the reader receives only the exact authorised bootstrap, fixed call and operating instruction. No new package file or dependency is needed.

The virtual merged complete root package remains 36 files. The manifest now verifies 28 operative entries: the unchanged 19 frozen baseline/provenance identities, four subject-file identities, and five control identities, including `../sasis.md` and `../../SKILL.md`. Visible and manifest protocol revisions are r41; existing update notes are retained with one r41 note appended. No baseline, provenance, subject file or rewrite guide is changed. The installed and repository r40 package remains untouched and was checked against immutable source commit `2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce`.

Root still owns review, complete-package publication, readback, local synchronization and acceptance. A future installer must expect 28 checks rather than a hard-coded 26 and must preserve full backup/readback semantics. The relative file inventory remains exactly the existing 36-file inventory, so this proposal does not require an inventory migration. No proposed package has been published or installed.

## Synthetic verification

The actual `functions.exec` interface ran one verified bootstrap and successive exact two-line calls for two baseline chunks, teaching text, a figure, ending text and two already-read baseline revisits. The complete synthetic route audit verifies seven accesses. The four template payloads extracted from the proposed package match the template bytes used in that test; only the documented fixed helper bindings differ in the derived verifier.

The evidence preserves 32 negative checks, three additional invocation/store-shape checks and five fresh launcher/revisit/argument/order checks. These include the observed r40 schema-copy failure, retained invoker source and digest mutations, stale/missing storage, malformed or extra arguments, invalid/skipped/out-of-order steps, an unread baseline revisit and operational-code changes. All rejection assertions passed without dependent subject access. Four figure-stage checks prove that staging, view invocation and tool return alone do not permit the next text step; advancement waits for actual image delivery and its receipt. Actual truncated output fails and its failed synthetic runtime is retained separately. The successful synthetic audit and failure runtimes are clearly distinguished; synthetic harness resets/restores are test setup only and are not reader permission to retry.

`metadata-subject-free-verification.json` independently denies every synthetic subject path during the bootstrap metadata proof: zero attempted subject opens, 18 operational/metadata open events, and unchanged synthetic runtime state. The existing mechanical skill validator passes. The new narrow controls and templates are synthetically preflighted; they are not evidence of a complete fresh reader run or an improved teaching outcome.

## Review records and pending work

- `proposed-controls.diff`, `proposed-file-identities.json`, `manifest-validation.json` and `validation.json` give the proposed bytes, hashes, checks and status.
- `templates/` contains the four unbound portable templates; `verified-extracted-templates/` preserves exact package extraction readback.
- `synthetic-preflight/` preserves the actual invocation surface, fixture, bound programs, evidence and distinct successful/failed test runtimes.
- `failure-evidence/` preserves the original r40 reader failure, exact call and separately labelled synthetic reproduction. Preparation-only encoding and validator assumptions were corrected and retained as labelled local preparation records.
- `SEALING.md` gives the narrow substitutions and ordering for a future reviewed binding; it authorises no production action.
- `REVIEW-SEAL.json` and `INVENTORY.json` identify this final review snapshot. Prior review snapshots remain available.

Production route/subject bindings have not been created for r41. No reader was dispatched, no teaching was generated, and no old r39/r40 evidence, frozen teaching, bound reader inputs, live reader runtime, installed skill or repository was changed. The completed r40 evidence-publication preparation remains separate and excludes the later failed reader/runtime pending the parent's final seal. Fresh generation, complete fresh reading and affected-success evidence remain pending after root approval, publication, readback and full local sync.
