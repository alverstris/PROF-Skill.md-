# PROF state tool

`scripts/prof_state.py` is a Python 3.9+ standard-library helper for durable bookkeeping. It has no model, API, package, browser, compiler or runtime-hook dependency. Use it with the execution protocol; the author still reads and applies PROF to each topic and inspects the actual teaching.

Its strongest result is `MECHANICALLY_READY`, scoped to the declared project or a named topic. This means the declared records have no detected mechanical defects. It never means teaching adequacy, learner mastery, authenticated user authorization, or guaranteed skill invocation/application. Reading a source, understanding it, judging applicability, validating a waiver's scope, reviewing semantics, and actually performing reported external checks remain self-reported. A heading-only witness can pass file/locator tests while failing the teaching contract. The author must reject such a witness substantively.

A check that reports pending work, an unanswered student question or an actual defect is useful, honest workflow; its exit code is not a judgment that PROF failed. Never manufacture witnesses, change applicability or refresh hashes to obtain a clean result. Actual learner-facing prerequisite-to-use reconstruction under execution-protocol.md is required before acceptance; source accounting and mechanical readiness cannot perform it.

Text output calls these readiness items. The compatibility JSON field `defects` also includes ordinary readiness blockers such as unanswered consequential questions; it does not classify all of them as teaching errors. A pending item is resolved only by the necessary work/evidence or answer, never by making its status look clean.

## Workflow and commands

Keep the exact user request and constraints in a UTF-8 file. Preserve literal instructions and provenance; a summary is an index, not a replacement. Choose a state directory beside the lesson artifacts. All commands use an explicit state path; there is no global state or hook.

```text
python /path/to/prof/scripts/prof_state.py init --state /project/.prof-state --skill /exact/prof/SKILL.md --request /project/request.txt --topic speed --topic acceleration
python /path/to/prof/scripts/prof_state.py begin-topic --state /project/.prof-state --topic speed --show-skill
python /path/to/prof/scripts/prof_state.py dependencies --state /project/.prof-state --topic speed
python /path/to/prof/scripts/prof_state.py check --state /project/.prof-state --topic speed
python /path/to/prof/scripts/prof_state.py dependencies --state /project/.prof-state
python /path/to/prof/scripts/prof_state.py check --state /project/.prof-state
python /path/to/prof/scripts/prof_state.py status --state /project/.prof-state --json
```

Paths with spaces must be quoted. Windows absolute paths work on Windows. `--project-root` can override init's default of the state directory's parent. IDs start with a lowercase letter and contain lowercase letters, digits, underscores or hyphens, up to 64 characters.

1. `init` records the exact resolved skill/request paths and hashes, creates pending topic records, pending `coverage` and `final_review` output checks, and a small `RUN.md`. It refuses a nonempty state directory. The scaffold intentionally cannot pass.
2. Edit `manifest.json` to declare all required topics, source portions, output files and applicable output checks. Do not let an author-selected learning route omit requested coverage. With no supplied sources, the source list may initially be empty; add researched references and their actual read scope when used.
3. Read the actual skill and next topic packet. `begin-topic` itself reads the current complete skill file and saves its path/hash/time only in that topic's activation. `--show-skill` prints the read text when useful. It proves that this helper read those bytes; it does not prove the author read, understood or applied them. It does not promote statuses, refresh evidence, or update the manifest skill hash.
4. Work on one coherent topic, record its source insights, discover consequential gaps, perform targeted research, and draft/check the actual teaching. Save substantive topic notes and audit witnesses. Record read source portions only after actually reading them.
5. After doing the named review/check at the current revision, record current file hashes and evidence locators, and copy the read-only `dependencies` snapshot into each completed record. This command computes declaration digests and prints required bindings; it does not set statuses or perform those checks. It rejects missing/stale declared file hashes. Compute file SHA-256 with an available trusted file-hash tool, or Python's `hashlib.sha256(Path(path).read_bytes()).hexdigest()`.
6. `check --topic ID` and `status --topic ID` inspect only that topic's detail and relevant files. They explicitly report `topic:ID` and skip global output acceptance and unrelated unfinished topic/output files. A clean topic result cannot establish project completion. The small global manifest is still validated.
7. Full `check` streams every declared topic record, verifies all required source portions are assigned/read, and checks every declared output check. It requires at least one topic and output plus `coverage` and `final_review`. Declare additional compile, visual inspection, navigation, technical execution and bundle checks when the product requires them; the tool cannot infer missing check types from the prose or file extension.

Exit codes: `0` for successful init/begin, an available dependency snapshot, or mechanical readiness; `1` for readiness defects; `2` for CLI/load/structure errors. CLI stdout/stderr use UTF-8, including redirected Windows output and `--show-skill`. Readiness is stated only by `check`/`status`. Both check commands are read-only and never update hashes, statuses, activation or recovery notes. `dependencies` is also read-only. No command from JSON is executed, no arbitrary URL is fetched, and sources/request/skill/evidence/output files are only read. JSON state writes use same-directory temporary replacement; begin-topic rejects resolved topic paths escaping state/topics.

## State layout

```text
.prof-state/
  manifest.json          small global index and output checks
  RUN.md                 tiny recovery index and one concrete next action
  topics/
    speed.json           activation, reads, gaps and T1–T12 for this topic
    acceleration.json
```

Keep detailed capability/prerequisite maps, conventions, supersessions, source insights, final locations and review reasoning in short companion files such as `author/speed.md` and `author/conventions.md`. Link them from RUN and evidence. JSON fields are strict: unsupported keys are rejected, so do not add arbitrary topic-detail fields. Declare a convention record or earlier-topic handoff used by another topic as a local source input with a required portion. Its change then invalidates consumer checks. Declare skill support references actually used (execution protocol, domain guide, production guide and relevant research basis) as dependency source inputs too: the SKILL digest does not include referenced files.

Update RUN after each coherent checkpoint, before delegation/interruption, and when a decision is superseded: current topic, exact constraint locators, relevant convention/learner-evidence locations, remaining defect and one next action. After a reset reread the exact skill, request, RUN and current topic packet. The helper checks that RUN exists; it cannot verify the recovery note's usefulness or that the author followed it.

## Schema version 1

All shown fields are required unless marked optional. Arrays can be empty where permitted. Hashes are lowercase, 64-character SHA-256 strings. Evidence files are UTF-8; source/output files can be binary. Skill, request and source paths are absolute local paths. Outputs/evidence use project-root-relative paths without `..`, absolute paths or symlink escape. Evidence additionally accepts `@request` for the exact request file.

Manifest fields:

| Field | Shape and purpose |
| --- | --- |
| `schema_version` | Integer `1`, with no string/boolean coercion. |
| `project_root` | Absolute existing artifact directory. |
| `skill`, `request` | `{ "path": "absolute path", "sha256": "64 hex" }`. |
| `required_topics` | Array of `{ "id", "title", "source_portions": [{ "source_id", "portion_id" }], "outputs": ["output-id"] }`. A topic must have output assignment(s). |
| `sources` | Array of `{ "id", "path", "sha256", "portions": [portion] }`; optional `url` preserves remote provenance. Save a local snapshot or precise read/research note for web material. The helper does not fetch or authenticate it. |
| `outputs` | Array of `{ "id", "path", "sha256" }` for actual deliverable revisions. |
| `output_checks` | Array of `{ "id", "description", ...condition }`. `coverage` and `final_review` must be present/applicable/pass. Add named product-specific checks. Each completed check binds the entire current declared inventory. |

A source portion is `{ "id", "locator", "disposition", "reason", "evidence": [...] }`. `locator` is a precise nonempty author-reported source locator, e.g. pages 4–7, section 2 and its figure, or whole file. Source-page/section existence is not parsed by this tool; evidence-file locators below are parsed. `disposition` is `required`, `excluded_by_user`, or `inaccessible`. Every required portion must be assigned to a topic and read there. `excluded_by_user` needs a reason and an exact request-text witness. A disclosed inaccessible portion blocks full readiness; it does not become an implicit scope waiver. A genuinely unspecified request's proposed scope belongs in the declared topic map; it does not authorize excluding assigned source portions.

Each `topics/<id>.json` has:

```json
{
  "id": "speed",
  "activation": {
    "skill_path": "absolute exact SKILL.md path",
    "skill_sha256": "64 hex",
    "activated_at": "2026-10-05T12:00:00+00:00"
  },
  "source_reads": [
    {
      "source_id": "foundation",
      "portion_id": "definition",
      "status": "read",
      "reviewed_sha256": "current source-file hash",
      "note": "What was actually read and what it establishes or leaves open."
    }
  ],
  "gaps": [],
  "requirements": {
    "T1": { "applicable": true, "status": "pending", "reason": "", "evidence": [], "dependencies": [] }
  }
}
```

The abbreviated example requires T2 through T12 too. Init generates all twelve. Source read statuses are `read` or `open`; an open/missing read is unread. The hash binds the claim to the source revision but does not prove reading or understanding. A broad prerequisite label or blanket read note is not a substantive topic packet.

A gap is `{ "id", "question", "consequential": true|false, "status", "reason", "next_action", "evidence": [...], "dependencies": [...] }`. Status is `open`, `unverified`, `resolved`, or `waived_by_user`. An open/unverified gap has a concrete research/repair/clarification next action. Consequential open/unverified gaps block readiness. Resolved gaps need a reason, current evidence and the same full topic dependency bindings as completed requirements. Waived gaps additionally need exact user-instruction evidence. Nonconsequential open gaps are reported as notes; the author is responsible for that classification. An empty gap list is not proof that no gaps exist.

For a needed student answer, use `open` or `unverified` and put the focused question, affected work and "await student answer" next action in the gap/companion record and RUN; do not invent an unsupported `awaiting_student` JSON status. Keep dependent conditions pending/unverified and continue independent teaching. Preserve the exact answer in the request/constraint record, then inspect/recompute the affected content and save new dependency bindings. A choice made by the author cannot resolve an ambiguous course convention; a student-authorized alternative must remain distinct from proof of the course's actual convention.

A condition, used for each T requirement and output check, is:

```json
{
  "applicable": true,
  "status": "pass",
  "reason": "The trigger, check performed, actual finding and material limits.",
  "evidence": [
    {
      "path": "author/speed.md",
      "sha256": "current witness-file hash",
      "locator": { "kind": "text", "value": "Exact substantive witness passage." }
    }
  ],
  "dependencies": [
    { "kind": "skill", "id": "", "sha256": "current skill-file hash" }
  ]
}
```

The dependency list above is abbreviated; use `dependencies` to print the full required list. Allowed condition statuses are `pending`, `pass`, `fail`, `unverified`, `not_applicable`, `waived_by_user`. All T1–T12 applicability decisions are explicit. False applicability requires `not_applicable` and a concrete false-trigger reason. Unknown is not false. T12 and the universal global coverage/final-review duties cannot be waived or inapplicable. A waiver requires applicability true, a reason naming the effect/scope, and an exact `text` locator in `@request`. Presence of that text is mechanically verified; its authority and claimed meaning remain substantive author judgments.

`pass` needs a reason and at least one existent, current witness, not just a status. Evidence locators are either `{ "kind": "text", "value": "exact nonempty text" }` or `{ "kind": "lines", "start": 10, "end": 18 }` with valid inclusive 1-based lines. Unsupported bare section/page-label locators and nonexistent text/ranges are rejected. An existent heading supplied as an exact-text locator can be mechanically located, but does not substantiate the teaching duty: the author must reject a heading-only witness. For a PDF, binary artifact, browser read or external check, save a UTF-8 inspection/research/check record with precise actual artifact/source locations and limits, reference that record, and bind the PDF/source/output hash as a dependency. A saved record is self-reported evidence, not independent observation by this helper.

## Dependencies and revision changes

Every completed topic condition (including not_applicable and waived_by_user) and resolved/waived gap requires bindings to the request, skill, the topic declaration, each assigned source's bytes and declaration, and all assigned output bytes. Completed global output checks require every current reference plus the inventory digest. Bindings are `{ "kind", "id", "sha256" }`:

| Kind | ID | Digest |
| --- | --- | --- |
| `request`, `skill` | Empty string | Actual declared file bytes. |
| `source`, `output` | Declared source/output ID | Actual declared file bytes. |
| `source_scope` | Source ID | Canonical full source declaration (portions, locators, provenance, exclusions). |
| `topic` | Topic ID | Canonical required-topic declaration (title, assignments and output IDs). |
| `inventory` | Empty string | Canonical manifest with only `output_checks` omitted, avoiding self-reference. |

Canonical digests use UTF-8 `json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` followed by SHA-256. The `dependencies` command computes these; no manual implementation is needed. Snapshot printing is not a review and not a safe substitute for rechecking.

Changed request/skill/source/output bytes fail the stored file hash. Updating only the manifest hash still leaves stale read records, evidence or check dependency hashes. Changed scope/source portions/topic inventory invalidates declaration bindings even when artifact bytes are unchanged. Adding a source or topic invalidates old global acceptance. Changes to a topic record's reported reasoning are not themselves tracked: put substantive prerequisite/convention/handoff notes in separately bound source inputs. Undeclared dependencies, missing topics never entered in the manifest, misleading witness text and false semantic passes remain outside the tool's knowledge.

After a change, reopen affected conditions, actually re-read/research/review the material and downstream consumers, refresh the relevant witness/input hashes, then save the newly checked dependency snapshot. Re-run begin-topic after a new activation/reset or changed skill. Recheck build/render/bundle after content changes. Neither `check` nor `begin-topic` makes stale acceptance fresh automatically. A two-sentence micro-answer keeps proportional applicability/evidence; the tool does not demand a workbook or an exercise per concept.

## Verification scope

The development tests use a readable speed lesson fixture, a 200-topic inventory with missing/stale last-topic state, single-topic partial readiness, omitted/open source portions, consequential gaps, malformed paths/IDs/statuses/schema/JSON, nonexistent witnesses/locators, changed source/output/skill/scope records, explicit waivers and micro-answer applicability. They deliberately show that a falsely labelled heading-only witness can be mechanically current while semantically inadequate. These are validator tests, not behavior guarantees, independent review or learner-outcome evidence.
