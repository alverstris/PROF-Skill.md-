# Independent latest synthetic sync fixture cross-check

**Result: corroborated, with no actual byte/record discrepancy found.** This is a read-only review of the exact final helper, complete test source, readback record, and named latest fixture. No owner helper or test was imported or executed. No production stage/install, network command, skill mutation or stale-fixture access occurred. All writes are confined to this review directory.

The helper SHA256 matches the requested pin `cb0c8b31a3d857edc3d8ed47f79afea61d7b3a752061c14f94f76a888b86b5f0`. Complete test-source SHA256 is `4ef6261d8fb22c5439e0715df19c52e1af3817ba56b9823f6bf9d2d90302f5cd`; readback SHA256 is `0932ed1868949c040ab38bbcf11821d8ba80370fc43bdc571cef34a7252068e8`. The readback binds that helper and `synthetic-fixtures/20261014T212433699002Z`.

## What was independently checked

Rehashed all 1,221 files in that exact fixture tree, totaling 390,904 bytes. Independently reconstructed the test's literal synthetic package, BOM/CRLF/binary payloads, complete manifest serialization and old-byte prefix without executing owner code. Compared 42 expected present/absent package states, including 29 actual package trees, across two dynamic-manifest cases and eight transaction cases. Every before inventory matched the reconstructed original and actual complete backup bytes. Six substantive failure records matched their actual paths, original error, generation hold, mutation/rollback disposition and intact backup. The complete fixture file inventory and all owner input bytes remained stable across the review.

Recomputed five manifest groups from actual fixture bytes, including 26/22 and 28/24 record/distinct-path counts. Compared saved installed-manifest rows with independently measured hashes, including the preserved pre-failure package in the final-status failure case. Read-only local Git commands verified all 36 immutable package blobs at synthetic commit `8eaecdf7c9adedba24518b0e423e3d26d27473c5` against both working and package-copy fixture bytes. Only `prof.zip` and `runs/evidence.json` were excluded from the tracked operative inventory. The synthetic Git configuration has no remote.

## Actual saved transaction outcomes

| Case | Current installation | Backup / other byte evidence | Substantive record consistency |
|---|---|---|---|
| Whole directory with obsolete file | Exact new 36-file package | Exact old 37-file backup and previous installation; stage absent | Successful whole-directory replacement, obsolete file absent |
| Blocked rename fallback | Exact new 36-file package | Exact old 36-file backup; exact staged package remains | Mock WinError 5 / errno 13 retained, equal-inventory fallback recorded |
| Blocked rename with unequal inventory | Exact old 37-file package | Exact old 37-file backup; new stage retained | Mutation false, rollback not attempted, generation held |
| Partial fallback write failure | Exact old 36-file package | Exact old backup; new stage retained | Fourth-write error and equal-inventory restoration recorded, generation held |
| Stage promotion failure | Exact old 36-file package | Exact old backup and previous installation; new stage retained | Mock promotion error and complete backup restoration recorded |
| Late live-ref failure | Exact old 36-file package | Exact old backup/previous installation; exact new failed-installation tree | Synthetic live-check error, restoration and generation hold recorded |
| Final status-record failure | Exact old 36-file package | Exact old backup/previous installation; exact new failed-installation tree | Prior successful verification preserved; current verification invalidated and generation held |
| Rollback itself fails | Exact old 36-file package | Exact old backup; new stage retained | Initial and restoration writes refused; manual recovery required and generation held |

## Fifteen claims and evidentiary limits

All 15 readback test names were accounted for. Eleven have direct complete-package or immutable-Git byte corroboration: both dynamic-manifest cases, all eight transaction cases, and the local-Git package case. This verifies the saved final states and substantive records, not an independent historical exception transcript.

Four claims have static guard/input consistency plus readback claims, without separately saved exception traces: nine unsafe paths, alternate production destination, simulated Windows reparse attribute, and unverified publication input. The exact unsafe forms map to rejecting guards in the inspected helper. The alternate destination test patches AUTHORIZED to a fixture, while the helper still requires the literal production destination. The final synthetic input actually has published_verification.verified=false. The reparse fixture is an ordinary file and the test supplies st_file_attributes=0x400 through a mock; no actual junction was tested.

Rename/write failures, the late-live-ref failure and final status-record failure are deliberate synthetic injections. WinError 5 is assigned to a synthetic PermissionError, rather than observed from a naturally blocked Windows rename. The rollback-itself-fails test refuses the first attempted payload write, so its actual current installation remains the original bytes. The recorded destination_mutated=true marks the attempted replacement path; this test does not demonstrate recovery of a partly damaged target when rollback also fails.

Static test-source inspection shows local Git operations and stubbed live checks, with no production CLI or remote_main invocation. The no-network statement is consistent with those paths and the remote-free fixture repository; this review is not a system-wide historical network trace. No real GitHub/live-main verification or production synchronization is established.

## Output identity and ownership

`fixture-file-identities.json` records every actual fixture file hash. `actual-package-state-checks.json`, `manifest-and-Git-checks.json`, `substantive-failure-record-checks.json`, `claim-corroboration.json` and `validation-summary.json` preserve the detailed comparisons. `review-manifest.json` seals those initial review outputs; `review-freeze.json` additionally binds this final report. Root retains publication, production synchronization and acceptance decisions.
