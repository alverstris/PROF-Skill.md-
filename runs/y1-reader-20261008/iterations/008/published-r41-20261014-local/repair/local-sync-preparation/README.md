# Prepared PROF publication synchronization helper

This is installation preparation only. No publication, GitHub package download, production installation, new generation, reader dispatch or lecture acceptance was performed by this preparation task. The controlling run remains 147 sessions, 76 eligible, 8 closed and 68 pending; 71 sessions remain excluded. Root owns publication, the actual immutable pin, installation and admission of subsequent generation.

`sync_published_prof.py` accepts a root-supplied verified-published inventory and has three explicit commands: `stage`, `install`, and `verify-installed`. It has no destination override. Only `install` can mutate the production installation, whose path must resolve exactly to `C:/Users/alver/.codex/skills/prof`, with no symlinks, junctions or other reparse points in its path.

At both authorized synchronization checkpoints (iteration start and after repaired-PROF publication), use a new run and the then-current verified published main commit. The current published r40 main reported by root at assignment was `a673a6d58b5abc803cbed9b1835a6888c94b4346`; this preparation did not re-verify that live ref and it is not a substitute for the publication pin supplied at execution. A later main ref that differs from the pin causes a hold, including a change detected after installation.

## Required root input

The inventory JSON has schema `prof-verified-published-package-v1`, exact repository/remote/branch, the full 40-character immutable commit, the PROF version, actual immutable-publication evidence, the independently verified count of operative profile checks, and the complete `package` array. Each package entry has `path`, `bytes`, `sha256`, `git_blob_sha` and Git `mode` (`100644` or `100755`). The helper rejects a false or absent publication verification, duplicate/colliding paths, unsafe Windows names, outside-package entries and an incomplete Git-tree inventory.

`verified-published-input.TEMPLATE.json` is deliberately unusable as a publication input: its commit and evidence are unset and `published_verification.verified` is false. Its 36 candidate identities come from the independent package review and may be retained only if actual published-byte verification confirms every one. Root must replace any changed identity and fill the verified publication fields from actual readback, then save a separate `root-verified-published-input.json`. Do not treat the template or unpublished candidate as the source for installation. The template expects 28 checks for the reviewed r41 profile. The helper calculates the count from the actual profile maps and subject records and compares it to the root's verified count; no 26/28 constant controls its validator.

## Root execution commands

Set the following values only after verifying the published commit and its complete inventory. These commands are written for the existing Python 3.14 installation; no dependency installation is needed.

```powershell
$profPrep = 'C:\Users\alver\.codex\.chatgpt-projects\g-p-6aa4088af61c8191a4b578a4310457ae\.prof-sasis\20261014-d008-r41\local-sync-preparation'
$profPython = 'C:\Users\alver\AppData\Local\Programs\Python\Python314\python.exe'
$profSync = Join-Path $profPrep 'sync_published_prof.py'
$profInput = Join-Path $profPrep 'root-verified-published-input.json'
$profVerified = Get-Content -LiteralPath $profInput -Raw | ConvertFrom-Json
$profPin = $profVerified.commit
$profVersion = $profVerified.version
$profRun = 'post-publication-' + $profPin.Substring(0, 12)
& $profPython -B $profSync stage --commit $profPin --version $profVersion --inventory $profInput --run-id $profRun
if ($LASTEXITCODE -ne 0) { throw 'Staging failed. Hold dependent generation and inspect the preserved staging record.' }
```

Review `runs/<run>/staging-verification.json` and `staged-manifest-checks.json`. `stage` independently queries GitHub main, fetches exactly the pinned commit into its own bare repository inside this preparation folder, enumerates the complete root package from that Git tree and writes binary blobs into a separate stage. It verifies every Git blob ID, byte length and SHA256, the complete staged inventory, the root version, every operative profile hash and JSON syntax. It excludes the historical `prof.zip`, `runs/` and unrelated root files.

After root has reviewed the staging result, execute the concrete installation command:

```powershell
& $profPython -B $profSync install --run-id $profRun --commit $profPin
if ($LASTEXITCODE -ne 0) { throw 'Installation failed. Hold dependent generation; preserve the full backup and inspect failure/rollback records.' }
& $profPython -B $profSync verify-installed --run-id $profRun --commit $profPin
if ($LASTEXITCODE -ne 0) { throw 'Installed readback failed. Hold dependent generation and preserve the verified backup.' }
```

Review `installation-verification.json`, `installed-manifest-checks.json`, `post-install-readback.json` and `generation-hold.json`. A passing synchronization needs successful command exit codes, complete current readback, the correct pin/version, an intact complete backup and a false current generation hold. Reread the actual installed root and relevant references before fresh generation:

```powershell
Get-Content -LiteralPath 'C:\Users\alver\.codex\skills\prof\SKILL.md' -Raw
Get-Content -LiteralPath 'C:\Users\alver\.codex\skills\prof\references\sasis.md' -Raw
Get-Content -LiteralPath 'C:\Users\alver\.codex\skills\prof\references\sasis\profile-manifest.json' -Raw
Get-Content -LiteralPath 'C:\Users\alver\.codex\skills\prof\references\sasis\student-role.txt' -Raw
Get-Content -LiteralPath 'C:\Users\alver\.codex\skills\prof\references\sasis\student-testing-contract.txt' -Raw
```

Bind the fresh author to that published commit in operational recovery state. Keep these helper records outside reader inputs. Package identity does not close a lecture or establish human learning.

## Backup, replacement and failure behavior

Before any mutation, the helper saves the installed file inventory and copies the complete installation to a new dated backup below `C:/Users/alver/.codex/skill-backups/prof/`. It checks every backup byte and verifies the installation stayed unchanged during the copy. It then attempts to rename the whole old installation into the run's `previous-installation/` and rename the verified stage into the authorized destination. The backup remains intact; the displaced old installation is retained as additional evidence.

If the first directory rename fails, the actual exception type, message, errno and Windows error are recorded. Every-file replacement is permitted only after the full backup passed, exact old/staged relative file inventories agree, and every source/write path is confined and ordinary. It rewrites all files as binary bytes; it never patches text, normalizes line endings or changes BOM bytes. An existing extra/obsolete file blocks this fallback. Whole-directory replacement handles obsolete files by retaining the old directory outside the destination and installing only the verified stage.

Any later install/readback/status-record failure triggers best-effort restoration from the preserved verified backup. Restoration first tries a whole-directory move of the failed installation into `failed-installation/` and a complete backup copy to the absent destination. If that move is blocked, byte restoration is allowed only for the exact original relative inventory and confined paths. A failed restoration is explicitly recorded as requiring manual recovery, and the full backup is kept. Failed success records are invalidated; original success-record data is preserved separately when possible. Record-write errors cannot bypass the restoration attempt. Any unsuccessful command holds generation; do not infer readiness from an older pass record.

## Verification and limits

`synthetic-test-readback.json` records 15 passing isolated tests, including dynamic 26/28 counts, 36-file Git-tree extraction, excluded historical files, BOM/CRLF byte preservation, Windows rename refusal, unequal-inventory refusal, partial-write recovery, stage-promotion failure, a final ref/readback failure, final status-record write failure, failed restoration, unsafe paths, alternate destination rejection and a simulated reparse attribute. `test_sync_synthetic.py` invokes only the transaction core on newly created non-subject fixtures under this folder; it never invokes production CLI staging or installation and uses no network. Previous synthetic runs are retained as evidence rather than erased.

The operative profile's `file_hashes`, `control_file_hashes` and `subject_files` define its current internal checks. Historical baseline release/freeze/download manifests are parsed and preserved; archive/source identities pointing outside the installed package are provenance and are not rewritten or falsely treated as required installed paths. Root publication verification must separately preserve unchanged frozen baseline/provenance identities.

Synthetic mocked errors do not establish every Windows locking, disk, permission or crash behavior. The helper does not prevent another process from changing files between checks, and cannot guarantee rollback during power loss, process termination or persistent filesystem failure. Its live ref checks establish a point-in-time main identity; main can change afterwards. Full dated backups and pre-mutation attempt records support manual recovery. Git/HTTP credential outputs and environment contents are never printed or saved. No runtime dependency, reader input, original source, candidate, installed skill or prior record was modified by preparation.
