from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(r'C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae')
BASE = Path(r'C:/Users/alver/.codex/skills/prof')
STAGE = ROOT / '.prof-maintenance/20261014/prof-r40-candidate'
REVIEW = ROOT / '.prof-maintenance/20261014/prof-r40-review'
REPO = ROOT / '.prof-maintenance/20261014/repository'
PIN = '51abe635150f97baf5b5e84965a66588b208e37b'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def inventory(root):
    return {p.relative_to(root).as_posix(): digest(p.read_bytes()) for p in sorted(root.rglob('*')) if p.is_file()}

def replace_once(relative, old, new):
    path = STAGE / relative
    data = path.read_bytes()
    newline = '\r\n' if b'\r\n' in data else '\n'
    text = data.decode('utf-8')
    old = old.replace('\n', newline)
    new = new.replace('\n', newline)
    if text.count(old) != 1:
        raise ValueError(f'{relative}: expected one replacement, found {text.count(old)}')
    path.write_bytes(text.replace(old, new, 1).encode('utf-8'))

base_inventory = inventory(BASE)
assert len(base_inventory) == 36
assert inventory(STAGE) == base_inventory, 'Stage must begin as exact installed r39 copy'
git_paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', PIN], cwd=REPO).decode().splitlines()
git_paths = [p for p in git_paths if p == 'SKILL.md' or p.startswith(('agents/', 'assets/', 'references/', 'scripts/'))]
assert set(git_paths) == set(base_inventory), 'Pinned package inventory mismatch'
for relative in git_paths:
    blob = subprocess.check_output(['git', 'cat-file', 'blob', f'{PIN}:{relative}'], cwd=REPO)
    assert digest(blob) == base_inventory[relative], f'Pinned base byte mismatch: {relative}'
(REVIEW / 'base-package-verification.json').write_text(json.dumps({
    'repository': 'alverstris/PROF-Skill.md-', 'commit': PIN,
    'installed_base': str(BASE), 'candidate_initial_copy_matches': True,
    'published_blobs_matched': len(git_paths), 'base_sha256': base_inventory,
}, indent=2) + '\n', encoding='utf-8')

replace_once('SKILL.md', 'version: "2026-10-14-r39"', 'version: "2026-10-14-r40"')

activation = 'Before each new/reopened topic, actually reread the current skill, check the exact user constraints, and load the topic record and immediate dependencies. Record the activation and skill revision. The helper\'s `begin-topic` records which bytes it read; it does not prove that the author understood or applied them. Apply the obligations to actual content. An inherited invocation, stale PASS, or “use the same approach” is insufficient. Reload source/definition passages before relying on them when their details have fallen out of working context.'
boundary = 'When the task or delegated scope gives an explicit writable-directory boundary, include dependency installation and its package, script, cache and configuration destinations in that boundary. Before recovering from a missing dependency, identify those resolved write destinations. Use an already available suitable tool, or a task-local environment/installation with its writes directed inside the authorised subtree, and verify the package origin actually used. A default install into a shared runtime, user site or system directory is not permitted merely because that interpreter is available. If no feasible permitted route exists, record the capability limit, keep dependent production/checks unverified and report the specific boundary change needed. Save the actual command, destinations and origin check; separately authorised operations retain their own stated scope.'
replace_once('references/execution-protocol.md', activation, activation + '\n\n' + boundary)

extraction = 'Check the extraction against the original when equations, figures, tables, notation, formatting or scan quality matter. Inspect the relevant rendered page/visual; searchable text may omit a minus sign, subscript, table row or caption. Label OCR/transcription uncertainty and verify consequential details. Never mark a portion fully reviewed merely because it appears in a compressed summary. Retain the original locator, plus short notes tied to it, so it can be reopened.'
attribution = 'Before claiming that an original source contains a typo or error, reopen the exact disputed passage in context and at sufficient resolution to distinguish its consequential glyphs. Record what the original actually states separately from any extraction and from the independently checked result; retain the source-error attribution only when that verified original and the proposed correction actually differ. A correct derivation establishes the result, not what the source printed. If the original remains unreadable, preserve that uncertainty and teach only the independently supported result without asserting an unverified source correction. Check every retained correction attribution, including closing provenance summaries, against that comparison.'
replace_once('references/execution-protocol.md', extraction, extraction + '\n\n' + attribution)

topic_start = 'For each requested topic/subtopic, locate its actual teaching and inspect it; a coverage index is the work list, not the outcome.'
numeric = 'For a displayed numerical value used to check or validate an answer, approximation or model, recompute from the actual learner-facing formula and stated inputs, retaining enough precision to decide the claimed rounding. Compare the final printed value, units and precision with that computation, rather than only checking the symbolic formula or an intermediate result. Save a compact formula/input/result/rounding witness for the check; a copied plausible decimal cannot validate itself. If the calculation is only a loose estimate, state its supported precision accordingly. Recheck affected comparisons when the numerical check changes, following the active repair mode.'
replace_once('references/execution-protocol.md', topic_start, numeric + '\n\n' + topic_start)

links_start = 'For linked teaching/help, inventory the source and target file and fragment for each route.'
spacing = r'For GitHub Markdown, use that source expression inventory to check the existing strict-comparison syntax rule in every mathematical payload: each `\lt` and `\gt` command has a terminating literal space, including before a digit or minus sign. Use a payload-aware scan or enumerate manually; record exact file/line violations and the final count, leaving literal code and HTML unchanged. Zero violations establishes this source-format requirement only. Record actual destination preservation separately; a syntax miss alone does not establish a rendering failure.'
wrapper = 'When mathematics appears in or next to a citation/link or another Markdown wrapper, include the exact wrapper boundaries in that destination comparison. Check that each intended mathematical payload maps to its own rendered expression, the link ends at its intended label boundary, and adjacent ordinary words remain prose. In GitHub citation links, keep mathematical payloads outside the link label and use a plain-text label unless the exact protected-math/link nesting has been verified at the actual destination. Test an unfamiliar wrapper combination before repeating it, then inspect every occurrence in the final artifact. Zero renderer errors does not establish separate expressions or correct link boundaries. Preserve an observed merge or swallowed prose as a destination defect and follow the active repair mode.'
replace_once('references/execution-protocol.md', links_start, spacing + '\n\n' + wrapper + '\n\n' + links_start)

replace_once('references/sasis.md', 'Protocol revision: 2026-10-14-r39.', 'Protocol revision: 2026-10-14-r40.')
sync_end = 'Keep skill repairs in the published repository; the installation is its verified copy.'
fallback = 'If a directory rename is blocked, preserve the actual failure. A file-content replacement is an allowed fallback only after a complete verified backup exists, the existing relative file inventory exactly matches the verified staged package, and the resolved write paths remain inside the authorised installation. Replace every staged file and perform the same complete installed-inventory, byte and manifest checks before generation; do not use a general overlay when obsolete or additional files are present. Record the fallback accurately rather than calling it a whole-directory replacement. If these conditions or verification fail, hold dependent generation under step 4.'
replace_once('references/sasis.md', sync_end, sync_end + ' ' + fallback)

preflight_start = 'Preflight the same launcher and invocation shape with non-subject synthetic fixtures:'
adapter = 'When the reader tool interface needs an operational wrapper around that launcher, seal one fixed non-subject adapter with its identity and checks before dispatch. Supply one exact, explicitly authorised bootstrap that verifies and retains that adapter without retrieving subject content; subsequent reader calls reuse that same sealed program through a short step-ID-only surface. Do not require the reader to recopy or edit hash, receipt or retrieval logic for each step. Verify the bound adapter identity before reuse and preserve the launcher\'s argument, order, range, hash, delivery and figure-view checks. Only the verified non-subject operational code may execute; subject bytes must never enter an executable position. A bootstrap or adapter failure is preserved as an input/execution limit under the existing stop-on-failure rule, not repaired by an improvised command or manual recopy. If this reuse cannot be established, hold dependent retrieval dispatch and report the capability limit.'
replace_once('references/sasis.md', preflight_start, adapter + '\n\n' + preflight_start)
replace_once('references/sasis.md', 'Record the instrumented open/access evidence, then compare the reader\'s actual ordered ledger, returned hashes and figure tool receipts with the whole frozen route before admission.', 'Where a wrapper is needed, preflight that same sealed adapter, exact bootstrap and short call surface too: bootstrap retrieves no subject, successive valid step IDs reuse the same program, and an altered adapter identity fails before subject access. Record the instrumented open/access evidence, then compare the reader\'s actual ordered ledger, returned hashes and figure tool receipts with the whole frozen route before admission.')

role_old = 'Do not add subject paths, ranges or interpreter commands; never execute, import, evaluate or compile an input file. If the launcher fails, preserve the exact call/result and report the access limit instead of improvising another retrieval command.'
role_new = 'Do not add subject paths, ranges or interpreter commands; never execute, import, evaluate or compile an input file. If a retrieval wrapper is supplied, use only its exact explicitly authorised verified non-subject bootstrap once, then reuse that same sealed adapter through its short step-ID-only call; change only the ID, without recopying or editing operational logic. Only that verified operational code may execute; subject bytes never may. If the bootstrap, adapter or launcher fails, preserve the exact call/result and report the access limit instead of retrying, improvising another retrieval command or advancing.'
replace_once('references/sasis/student-role.txt', role_old, role_new)

replace_once('references/sasis/student-testing-contract.txt', 'SASIS reader contract — revision 2026-10-12-r38', 'SASIS reader contract — revision 2026-10-14-r40')
contract_old = 'Prepare and synthetically preflight its fixed launcher before dispatch. Reader invocations use only that launcher'
contract_new = 'Prepare and synthetically preflight its fixed launcher before dispatch. When a tool wrapper is needed, also seal and preflight one non-subject operational adapter and its exact explicitly authorised verified bootstrap, then reuse that same program through a short step-ID-only call; do not recopy hash or receipt logic per step, and never execute subject bytes. Preserve any bootstrap/adapter/launcher failure and stop without retry, improvisation or advancement. Reader invocations use only that launcher'
replace_once('references/sasis/student-testing-contract.txt', contract_old, contract_new)

replace_once('references/sasis/profile-manifest.json', '"protocol_revision": "2026-10-14-r39"', '"protocol_revision": "2026-10-14-r40"')
profile_path = STAGE / 'references/sasis/profile-manifest.json'
profile = json.loads(profile_path.read_text(encoding='utf-8'))
for relative in ['student-role.txt', 'student-testing-contract.txt']:
    old = profile['control_file_hashes'][relative]
    new = digest((profile_path.parent / relative).read_bytes())
    replace_once('references/sasis/profile-manifest.json', f'"{relative}": "{old}"', f'"{relative}": "{new}"')
note_old = '    "2026-10-14-r39 implements Jonathan\'s explicit request to download the published GitHub PROF package over the local Windows installation at iteration start and after revised-PROF publication. Stage and verify the complete package, retain a recoverable backup, replace the installation and verify its bytes against one pinned commit before local generation. This supersedes the previous local-update prohibition; frozen baseline files, reader controls, teaching evidence and corpus acceptance counts are unchanged."'
note_new = note_old + ',\n    "2026-10-14-r40 strengthens source-error attribution, final numerical validation, strict-comparison source syntax, citation/math wrapper boundaries and dependency write-destination checks after verified execution and destination findings. A blocked installation-directory rename has a verified equal-inventory fallback. Retrieval wrappers reuse one sealed non-subject adapter through an explicitly authorised verified bootstrap and step-ID-only calls. Frozen baseline/provenance bytes remain unchanged; the incomplete r39 reader provides no whole-document verdict, and fresh generation, complete reading and affected-success checks remain pending."'
replace_once('references/sasis/profile-manifest.json', note_old, note_new)

final_inventory = inventory(STAGE)
changed = [p for p in base_inventory if base_inventory[p] != final_inventory[p]]
assert set(final_inventory) == set(base_inventory)
(REVIEW / 'candidate-changed-files.json').write_text(json.dumps({
    'base_commit': PIN, 'candidate_revision': '2026-10-14-r40', 'file_count': len(final_inventory),
    'changed': [{'path': p, 'before_sha256': base_inventory[p], 'after_sha256': final_inventory[p]} for p in changed],
    'unchanged_files': len(final_inventory) - len(changed),
    'candidate_sha256': final_inventory,
}, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'files': len(final_inventory), 'changed': changed}, indent=2))
