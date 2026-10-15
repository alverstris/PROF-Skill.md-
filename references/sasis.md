# SASIS — dedicated reader protocol

Protocol revision: 2026-10-14-r41.

## Purpose and activation

SASIS evaluates the teaching document. Its dedicated agent is the reader. The central question is whether, at each point in the document, a reader with the supplied baseline can understand the statement, make the required connection, and reach the correct conclusion. It is not a test of the simulated student's ability and is not organised around attempts at held-out tasks.

Activate only for an explicit request to run SASIS or improve/iterate PROF itself. Ordinary authoring, ordinary document revision, and maintaining these instructions do not by themselves start a SASIS run. During a run, apply ordinary PROF to author the teaching. Its relevant practice/help obligations remain; exercises already in the document are read and audited as part of the document, not substituted for reading it.

Read this protocol, [reader contract](sasis/student-testing-contract.txt), [reader operating instruction](sasis/student-role.txt), [profile manifest](sasis/profile-manifest.json) and [rewrite guide](sasis/rewrite-guide.md). The historical acronym and filenames are retained for compatibility; their meaning is governed by the current reader procedure.

## Repository and assigned corpus

For Jonathan's authorised run, GitHub is the source of truth. Read the actual current repository version at the start of each iteration, with a pinned commit, and perform the local synchronisation step below when working on his computer. Save skill repairs and evidence to GitHub before refreshing the installation. Preserve concurrent changes; publish with an expected-head check, never an unrequested force push. Publish every revised PROF before using it for a new generation. Verify the published commit, then reload its actual root files. A proposal, local candidate, or cached earlier skill is not the operative revision. Publication does not assert that its fresh-generation checks have passed.

The original inventory contains 126 indexed lectures and 21 TEAL studios, 147 sessions. Jonathan subsequently instructed this run to find the sessions that can be fully read properly and iterate through those only. Audit the complete original inventory, then traverse only the explicitly recorded readable subset in its original order. A packet includes all required associated portions and consequential visual information; file access or an extracted transcript alone does not establish complete reading. Preserve excluded sessions and their precise evidence limits, distinguishing intrinsic illegibility from unestablished complete coverage. This is the user's explicit scope change, not permission to omit required material for convenience in other runs. Keep the complete queue with stable IDs, year-level evidence, original selection provenance, required associated source portions, access status and current evidence. The [lecture CSV](sasis/ocr-baseline-20261007/year1-lecture-index.csv) covers the 126 lectures; resolve the studio list separately from the [registry](sasis/ocr-baseline-20261007/year1-course-registry.json) and official material. Do not silently expand, collapse, or narrow the assignment. A selection index is not source content or evidence of reading. Several assets for one session remain one session, with all required portions tracked.

Obtain and actually inspect the active session's sources, equations and figures. Record unread or inaccessible portions rather than claiming complete coverage. Source mistakes require independent checking. Preserve corrections with precise locators. A source's incorrect wording is not automatically a PROF defect.

## Synchronise the installed PROF from GitHub

Jonathan's 2026-10-14 instruction authorises downloading GitHub PROF to overwrite the local skill and supersedes the previous prohibition on updating his Windows installation. Perform this step at the start of each iteration and after each revised-PROF publication, before the next fresh generation on his computer.

1. Pin the current main commit, or the just-published verified repair commit. Download its complete root skill package into a separate staging directory: SKILL.md and every tracked file under agents/, assets/, references/ and scripts/. Use that single immutable commit for all files. The historical root prof.zip and runs/ are not the installed package.
2. Before replacement, verify the staged file inventory and bytes against the pinned Git tree and validate all operative package-local manifest hashes. Confirm the resolved destination is exactly C:/Users/alver/.codex/skills/prof. Preserve the existing installation in a dated backup outside that destination, then replace the whole installed directory with the verified stage so obsolete files cannot survive an overlay. Keep skill repairs in the published repository; the installation is its verified copy. If a directory rename is blocked, preserve the actual failure. A file-content replacement is an allowed fallback only after a complete verified backup exists, the existing relative file inventory exactly matches the verified staged package, and the resolved write paths remain inside the authorised installation. Replace every staged file and perform the same complete installed-inventory, byte and manifest checks before generation; do not use a general overlay when obsolete or additional files are present. Record the fallback accurately rather than calling it a whole-directory replacement. If these conditions or verification fail, hold dependent generation under step 4.
3. Verify the complete installed inventory and every file's bytes against the same published package. Save the repository, commit, skill version, time, destination, backup location and verification result in the author recovery state outside the installed package and reader inputs. Reread the installed SKILL.md and relevant references, and bind the fresh author's operative package to that verified commit. The SASIS reader still receives only its baseline and teaching.
4. If staging or verification fails, keep or restore the backup and hold generation that depends on this local installation until it is verified. If the installation is inaccessible from a different execution environment, record local synchronisation as unavailable and continue only from the verified published package; do not claim to have overwritten the computer's files. Synchronisation records package identity, not a lecture pass or human learning outcome.

## Baseline and roles

The frozen OCR-A-4-subjects-r1 profile comprises Mathematics A H240; Further Mathematics A H245 Pure Core Y540/Y541, Statistics Y542 and Mechanics Y543; Physics A H556; and Chemistry A H432. No MEI, Discrete or Additional Pure option is assumed. [The complete operational baseline](sasis/ocr-baseline-20261007/student-baseline.txt), not qualification names or a syllabus summary, supplies prior knowledge. Use its frozen edition and provenance honestly; verify live editions before claiming it is current. A consequential baseline correction starts a separately labelled profile/condition and cannot retroactively validate old reports.

The author reads the current PROF files, actual sources, complete baseline and relevant research before drafting. The author owns source coverage and the ordinary teaching obligations. The orchestrator preserves state and publishes justified edits. An independent technical reviewer checks scientific/mathematical correctness against inspected sources and explicit deductions. The SASIS agent is a fresh reader, not the author, evaluator, task designer, or a research agent reused under a new name.

The reader receives exactly two subject-content inputs: the complete frozen operational baseline and the complete current teaching document, including its figures, captions, examples, exercises, hints, solutions and appendices. Its short operating instruction is not a third subject-content input. Do not give it raw lecture sources, author chat/history, skill instructions, research notes, suspected defects, previous reader reports or evaluator solutions. Reading instructions and artifact identifiers may be supplied without revealing expected findings.

Launch every reader with a fresh agent context and explicitly set `fork_turns: "none"`. Every frozen document revision gets its own reader. Never reuse a prior reader's memory for a new document. Recalling the current supplied baseline, earlier passages and valid deductions within one reading is allowed. Prior lessons needed by the current document must actually be included there; a completed-lecture ledger cannot supply them.

## Admission and actual isolation

Before dispatch, freeze the document and baseline and save their IDs, revisions and hashes or exact immutable locators. Record agent identity, history setting, operating-instruction revision, permitted tools, delivery mode, input extent, known truncation/access limits and an explicit admission state.

Use complete full-text delivery when its actual extent can be established. A link, hash, claimed window size or acknowledgement alone does not establish complete delivery. Alternatively use an explicitly labelled instruction-confined read-only retrieval condition: both complete immutable artifacts are available, the reader may fetch only those artifacts, and its access ranges/results are logged. It must inspect the whole document in order and read the full baseline in coherent retrievable chunks. It may re-fetch the authorised baseline when needed. Do not claim that all bytes were simultaneously in context.

For retrieval of linked or interleaved teaching, prepare an exact ordered route before dispatch: file identities, byte or line ranges with their convention, and each complete figure at its first-use position. Verify that the route covers every text byte and constituent, including prompts, help and endings, without exposing a later section early. Supply this subject-free routing metadata, not excerpts, answers or findings, alongside the two subject inputs. The reader retrieves only the next bounded slice or figure, records its actual access, and then advances; do not guess heading boundaries or batch across a scheduled exercise or figure. Before admitting chronological evidence, compare actual ordered access with that route as well as total coverage. Preserve accidental early exposure or delayed required figure access as a reader-procedure failure; rereading cannot restore first exposure. Complete the audit, repair routing, and dispatch a fresh reader on the unchanged frozen inputs. This recovery does not repair a teaching defect or waive the publication-first fresh-generation rule for a verified material iteration failure.

Before retrieval dispatch, the orchestrator prepares and validates one fixed route-bound launcher. Each reader command consists only of that launcher and a permitted step ID; subject paths and byte ranges are resolved from the frozen route, never supplied in a per-step interpreter or executable position. A permitted ID is the next scheduled step or a predeclared bounded baseline-revisit ID whose initial baseline chunk has already been read. A baseline revisit does not advance the document cursor, and no future teaching access is allowed. Complete the initial baseline route before teaching. Before opening subject files, reject extra arguments, unknown or out-of-order steps, invalid types/ranges and mismatched route identity. Read text as binary data with a bounded seek/read, verify the exact returned range and its expected hash, and append an actual-access receipt before returning content. Never execute, import, evaluate or compile a subject file to retrieve it. For a figure, return the complete identified image and hold advancement until its actual view-tool result is recorded at the scheduled inspection stage; a checksum or image path alone is not a view. Preserve unsuccessful calls and distinguish internal byte access from content actually displayed.

When the reader tool interface needs an operational wrapper around that launcher, seal one fixed non-subject invoker containing all per-step schema, identity, retrieval, receipt and view checks. An exact explicitly authorised bootstrap independently verifies and retains that invoker without subject access. Subsequent calls use only a fixed invocation surface and the permitted STEP_ID datum; the reader must not reproduce or edit any guard, proof parser, hash, receipt or retrieval logic. On serializable-store interfaces such as functions.exec, the fixed two-line call may evaluate the retained invoker expression and pass STEP_ID; all guards stay inside the reused program. The expression evaluates before its current retained-source/envelope comparison. That comparison must use independently verified canonical metadata and reject changes before subject launcher or view access; do not claim authentication before evaluation, a persistent callable, or technical confinement. Only the bootstrap-verified designated non-subject program belongs in this position; subject bytes never may. Preserve all existing argument, order, range, hash, delivery and figure-view checks and stop/preserve without retry on failure. If this narrow reuse surface is unavailable, hold dependent dispatch and state the exact capability limit. Extract the four named [sealed invoker templates](#sealed-reader-invoker-templates) programmatically from this published reference and verify their exact bytes before binding; do not manually recreate their logic.

Preflight the same launcher and invocation shape with non-subject synthetic fixtures: a valid next slice returns only its exact bytes; wrong arguments, a skipped step and an unknown step fail before any subject-file open; a figure cannot be bypassed without its actual view invocation/result receipt; an already-read baseline revisit succeeds without moving the document cursor and a not-yet-read baseline revisit fails before subject access. Where a wrapper is needed, preflight that same sealed invoker, exact bootstrap and minimal invocation surface too: bootstrap retrieves no subject; successive step data reuse the same program without caller-authored guards; an altered retained source/envelope, missing/stale store, invalid/extra/out-of-order step, unread baseline revisit and truncated output stop before dependent access; and the observed proof/store schema-copy mistake is reproduced synthetically and absent from the repeated invocation surface. Check the actual evaluation order and preserve failures; source/envelope comparison occurs after invoker-expression evaluation and before subject launcher/view access. Record the instrumented open/access evidence, then compare the reader's actual ordered ledger, returned hashes and figure tool receipts with the whole frozen route before admission. The launcher reduces executable/data confusion and checks its own calls; it is not a technical boundary against other available tools, and a recorded view receipt alone does not prove semantic inspection. A verified material runner failure follows the PROF repair and publication-first fresh-generation rule even if visible diagnostic output contains only previously read text.

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

## Diagnose the whole document; repair PROF

Preserve every generated document and original reader report unchanged. Independently verify reported technical issues and important scientific results. A reader assertion alone is not a verified defect; inspect the actual route and legitimate alternatives. External checking cannot grant a premise absent from the reader's inputs.

Audit all required source portions, every section and help item, relevant PROF obligations and all reader findings. Keep an issue register with exact evidence, causes, affected instances and dependencies, the necessary PROF change and verification state. Distinguish teaching, source, baseline, input, reviewer, rendering and execution failures, and legitimate pending questions. The earliest gap orders repair; it never ends the audit. Revisit previously blocked dependencies in the next fresh generation.

For this user-authorized self-iteration run, every verified material failure requiring correction must be addressed in PROF's operative instructions or supporting execution procedure. Do not patch the generated document, even for a local, mathematical-delimiter or representation-only defect. If an existing rule was ignored, strengthen the specific activation or execution step that should enforce it; if the rule is missing or inadequate, revise it. Source, input and runner failures require the relevant handling/recovery instruction, not a false claim that the subject lesson itself is wrong. A disproved concern or honestly unresolved external fact is not an invented teaching failure.

Use the rewrite guide to turn the demonstrated cause into a reusable trigger, concrete author action and observable check. Do not insert lecture answers or patched example passages into PROF. Preserve useful existing behavior and check over-application where the change creates a concrete risk. An adequate no-failure generation does not require an invented rule.

## Publish the revised PROF before restarting

Freeze and validate the complete revised skill package, including changed supporting resources and matching manifests. Push it to the current main branch of alverstris/PROF-Skill.md- with an expected-head check. Verify the commit/tree and actual fetched bytes. The newly published version is the source for the next generation; an unpublished candidate is insufficient. Publication alone does not establish acceptance: record pending generation/review honestly.

When changing a resource bound by a package manifest, inventory and refresh its operative internal hash references as part of the same release. Before publication, validate every declared package-local control/profile hash against the actual candidate bytes; repeat that validation against the fetched published package before author or reader admission. Preserve unchanged frozen-baseline and historical provenance identities rather than refreshing them indiscriminately. A byte-for-byte publication match does not establish internal consistency. If a mismatch is found, preserve the original release and its accurate readback evidence, hold new generation, correct the complete package and verify a new immutable commit before dispatch.

After publication and published-package verification, complete the installed-PROF synchronisation step above when working on Jonathan's computer. Retain only a concise operational handover: the task goal, exact controlling user instructions, repository and verified commit, local synchronisation result, frozen baseline/source identities, active lecture, entire queue/counts, next tasks, ownership and material access limits. Start generation in a fresh agent context with fork_turns: "none". Where a coordinator is replaced, give that new coordinator only this operational handover and original inputs. Keep previous teaching, diagnoses, reader reports, proposed solutions and detailed reasoning out of the new generation context. Preserve them separately for later audit, not as authoring inputs.

No exposed tool can be presumed to erase the current agent's live conversation or pretraining. Use an actually fresh agent when an erasure control is absent, and report that boundary honestly. Freshness is an operational separation, not proof of technical memory erasure.

The fresh author fetches and reads the verified published root PROF and supporting files, the complete unchanged operational baseline, the original lecture and the original task. It regenerates the complete teaching without a patched answer template. Freeze that output and dispatch a separate fresh SASIS reader with exactly the complete baseline and complete new document. Independently check correctness, source coverage, required output evidence and affected earlier successful cases. Preserve every complete generation and original report.

## Closure and the next lecture

Close an iteration only when the complete required audit is covered and every supported material issue has verified resolution in fresh generation under published PROF, with affected earlier checks current. Pending external facts, inaccessible required sources and unresolved questions remain pending. A revised PROF can be published while its current lecture remains open; do not confuse those states or advance the queue as though the checks passed.

At closure save the source/coverage record, incoming/outgoing published revisions, complete generated document versions, admission/access records, original reader reports, independent technical evidence, issue dispositions and concise change log. Verify the published progress record. Preserve the existing rolling cumulative version convention without inventing a substantive defect to justify a number. Reload current main and start the next eligible material with fresh author and reader contexts. Do not carry an old author or reader into the next cycle.

Retain the entire 147-ID queue, the authorized 76-session readable subset and 71 exclusions. Later skill changes reopen affected earlier checks; address those dependencies before corpus acceptance. Do not stop a corpus run because one document is adequate. If a real external limit or user instruction prevents continuation, preserve the exact state and next action and report the unfinished scope honestly.

After a reset, read current published PROF, this protocol, exact user constraints and the concise operational handover. Reacquire original sources and the complete baseline. Old summaries or all-clear assertions do not replace current checks. Inspect preserved diagnosis records only in the separate auditing stage after new generation is frozen; never leak them into its author or reader inputs.

## Durable records

Keep author/orchestrator records outside reader inputs, for example `runs/<run-id>/`. Use a small recovery index, full queue, sharded session evidence and immutable original reports. Record actual conditions rather than ceremonial logs. Hashes prove identity, not explanatory sufficiency.

The concise iteration log identifies material, incoming/outgoing revision, all justified skill changes and result. It links to the detailed issue register. At corpus completion provide the final effective PROF and the change log, with actual verification limits. Distinguish protocol editing, author checks, SASIS reading, rendered-artifact checks and human learning evidence.

## Sealed reader invoker templates

These four named blocks are operational source templates, not subject content or reader role text. The orchestrator extracts their exact UTF-8 payload bytes programmatically between the named markers, including the final newline, then binds and seals them before dispatch. Keep them in this existing reference so the complete installed package inventory remains unchanged. The reader receives only the exact authorised bootstrap and two-line invocation, not PROF or these template instructions. The function expression evaluates before the reused program's current identity comparison; no pre-evaluation authentication or persistent-callable claim is made.

<!-- PROF-READER-TEMPLATE-BEGIN: invoker_template.js -->
```javascript
(async function retainedReaderInvoker(STEP_ID) {
if (arguments.length !== 1) throw new Error("exactly one STEP_ID datum is accepted");
const cached = load("__STORE_KEY__");
if (typeof STEP_ID !== "string" || !/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(STEP_ID)) throw new Error("exactly one plain STEP_ID is accepted");
if (!cached || typeof cached !== "object" || Array.isArray(cached) || cached.schema !== "prof-reader-invoker-store-v1" || cached.binding_sha256 !== "__CORE_SHA256__") throw new Error("missing/stale reader bootstrap; preserve failure and stop");
const r = await tools.exec_command({cmd: "__VERIFY_COMMAND__ 'step' '__CORE_SHA256__' '" + STEP_ID + "'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader operational identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("verification output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "mode,schema,seal,step_id" || p.schema !== "prof-reader-reuse-proof-v1" || p.mode !== "step" || p.step_id !== STEP_ID || JSON.stringify(cached) !== JSON.stringify(p.seal)) throw new Error("cached adapter/binding identity mismatch; preserve failure and stop");
// Only the exact verified operational source enters eval; STEP_ID is a parameter, never source text.
await eval("(async function(STEP_ID) {\n" + p.seal.adapter_source + "\n})(STEP_ID)");

})
```
<!-- PROF-READER-TEMPLATE-END: invoker_template.js -->

<!-- PROF-READER-TEMPLATE-BEGIN: bootstrap_template.js -->
```javascript
// Explicitly authorized once: load only the sealed non-subject operating instruction and operational adapter.
const KEY = "__STORE_KEY__";
if (load(KEY) !== undefined) throw new Error("reader bootstrap already present; preserve it and stop");
const r = await tools.exec_command({cmd: "__VERIFY_COMMAND__ 'bootstrap' '__CORE_SHA256__'", max_output_tokens: 18000});
if (r.exit_code !== 0 || r.session_id) throw new Error("reader bootstrap identity verification failed: " + r.output);
let p;
try { p = JSON.parse(r.output.trim()); } catch (_) { throw new Error("bootstrap output missing/truncated; preserve failure and stop"); }
if (!p || Object.keys(p).sort().join(",") !== "instruction,mode,schema,seal" || p.schema !== "prof-reader-reuse-proof-v1" || p.mode !== "bootstrap" || typeof p.instruction !== "string") throw new Error("invalid bootstrap proof shape");
if (!p.seal || p.seal.schema !== "prof-reader-invoker-store-v1" || p.seal.binding_sha256 !== "__CORE_SHA256__" || typeof p.seal.adapter_source !== "string" || typeof p.seal.invoker_source !== "string") throw new Error("invalid bootstrap seal");
store(KEY, p.seal);
text(p.instruction);
text({bootstrap_verified: true, binding_sha256: p.seal.binding_sha256, bootstrap_sha256: p.seal.bootstrap_sha256, short_call_sha256: p.seal.short_call_sha256, invoker_sha256: p.seal.invoker_sha256, subject_retrieval: false});
```
<!-- PROF-READER-TEMPLATE-END: bootstrap_template.js -->

<!-- PROF-READER-TEMPLATE-BEGIN: short_call_template.js -->
```javascript
const STEP_ID = "B001";
await eval(load("__STORE_KEY__").invoker_source)(STEP_ID);
```
<!-- PROF-READER-TEMPLATE-END: short_call_template.js -->

<!-- PROF-READER-TEMPLATE-BEGIN: verify_reuse_template.py -->
```python
"""Metadata/code-only identity proof. Never reads or executes subject files.

Run only after the fixed wrapper checks this file's SHA256. All paths are fixed
within this directory. This is instruction confinement, not a caller sandbox.
"""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = ROOT / "seal-core.json"
EXPECTED_NAMES = {
    "verify_reuse.py", "bootstrap_template.js", "short_call_template.js", "operating_instruction_template.md", "invoker_template.js",
    "operational_adapter.js", "fixed_launcher.py", "record_receipt.py", "__FIXED_ROUTE_FILENAME__",
}
ID = re.compile(r"[A-Za-z][A-Za-z0-9_-]{0,63}\Z")


def require(ok, why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def unique(raw):
    def pairs(items):
        d = {}
        for k, v in items:
            require(k not in d, "duplicate metadata key")
            d[k] = v
        return d
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs)


def render(template, core_hash, core):
    verifier = str(ROOT / "verify_reuse.py").replace("\\", "/")
    # Get-FileHash runs before Python executes the identity verifier.
    command = ("$v='" + verifier + "'; if ((Get-FileHash -LiteralPath $v -Algorithm SHA256).Hash.ToLowerInvariant() -ne '" + core["files"]["verify_reuse.py"]["sha256"] + "') { throw 'verifier identity mismatch' }; & '" + core["python"] + "' $v")
    for marker, value in {"__VERIFY_COMMAND__": command, "__CORE_SHA256__": core_hash, "__STORE_KEY__": core["store_key"]}.items():
        template = template.replace(marker, value)
    require("__" not in template, "unbound wrapper marker")
    return template


def proof(mode, core_hash, step_id=None):
    raw = CORE.read_bytes()
    require(len(raw) < 100000 and sha(raw) == core_hash, "sealed binding hash mismatch")
    core = unique(raw)
    require(type(core) is dict and set(core) == {"schema", "scope", "python", "store_key", "route_sha256", "route_path", "runtime_path", "files"}, "invalid core shape")
    require(core["schema"] == "prof-reader-reuse-core-v1" and core["scope"] == "__FIXED_SCOPE__", "wrong binding schema/scope")
    require(type(core["files"]) is dict and set(core["files"]) == EXPECTED_NAMES, "unpermitted operational path set")
    sources = {}
    for name, spec in core["files"].items():
        require(type(spec) is dict and set(spec) == {"sha256", "bytes"}, "invalid operational identity shape")
        require(type(spec["bytes"]) is int and 0 < spec["bytes"] < 1000000, "invalid operational extent")
        data = (ROOT / name).read_bytes()
        require(len(data) == spec["bytes"] and sha(data) == spec["sha256"], "operational identity mismatch: " + name)
        sources[name] = data.decode("utf-8")
    require(core["route_path"] == str(ROOT / "__FIXED_ROUTE_FILENAME__").replace("\\", "/"), "route path binding mismatch")
    require(core["runtime_path"] == str(ROOT / "__FIXED_RUNTIME_DIRNAME__").replace("\\", "/"), "runtime binding mismatch")
    require(core["route_sha256"] == core["files"]["__FIXED_ROUTE_FILENAME__"]["sha256"], "route hash binding mismatch")
    require(Path(core["python"]).is_absolute() and "'" not in core["python"] and "'" not in str(ROOT), "unsafe fixed command path")
    spec = importlib.util.spec_from_file_location("sealed_metadata_only_launcher", ROOT / "fixed_launcher.py")
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    require(str(runner.CONFIG_PATH).replace("\\", "/") == core["route_path"] and runner.EXPECTED_CONFIG_SHA256 == core["route_sha256"] and str(runner.RUNTIME_DIR).replace("\\", "/") == core["runtime_path"], "launcher route/runtime binding mismatch")
    config = runner.load_config()  # Bounded metadata read + pure metadata validation only.
    require(config["route_id"] == "__FIXED_ROUTE_ID__", "unpermitted fixture route")
    adapter = sources["operational_adapter.js"]
    require(adapter.count("await readerStep(STEP_ID);") == 1 and not re.search(r"const STEP_ID\s*=", adapter), "invalid parameterized adapter shape")
    require('const ROUTE_SHA256 = "' + core["route_sha256"] + '";' in adapter, "adapter route binding mismatch")
    invoker = render(sources["invoker_template.js"], core_hash, core)
    bootstrap = render(sources["bootstrap_template.js"], core_hash, core)
    short = render(sources["short_call_template.js"], core_hash, core)
    instruction = render(sources["operating_instruction_template.md"], core_hash, core)
    for name, text in {"invoker.js": invoker, "bootstrap.js": bootstrap, "short_call.js": short, "reader-operating.md": instruction}.items():
        require((ROOT / name).read_bytes() == text.encode("utf-8"), "derived bootstrap/wrapper/instruction identity mismatch: " + name)
    seal = {"schema": "prof-reader-invoker-store-v1", "binding_sha256": core_hash,
            "adapter_sha256": core["files"]["operational_adapter.js"]["sha256"],
            "route_sha256": core["route_sha256"], "bootstrap_sha256": sha(bootstrap.encode()),
            "short_call_sha256": sha(short.encode()), "runtime_path": core["runtime_path"], "invoker_sha256": sha(invoker.encode()), "invoker_source": invoker, "adapter_source": adapter}
    result = {"schema": "prof-reader-reuse-proof-v1", "mode": mode, "seal": seal}
    if mode == "bootstrap":
        result["instruction"] = instruction
    else:
        require(type(step_id) is str and ID.fullmatch(step_id), "exactly one plain STEP_ID is accepted")
        result["step_id"] = step_id
    return result


def main():
    try:
        require(len(sys.argv) in (3, 4), "invalid identity-verifier argument shape")
        mode, digest = sys.argv[1:3]
        require(mode in ("bootstrap", "step") and re.fullmatch(r"[a-f0-9]{64}", digest), "invalid verification mode/hash")
        require(len(sys.argv) == (3 if mode == "bootstrap" else 4), "mode argument shape mismatch")
        result = proof(mode, digest, sys.argv[3] if mode == "step" else None)
        sys.stdout.buffer.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")).encode("utf-8") + b"\n")
        return 0
    except Exception as exc:
        sys.stderr.write(json.dumps({"ok": False, "error": str(exc)}) + "\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
```
<!-- PROF-READER-TEMPLATE-END: verify_reuse_template.py -->
