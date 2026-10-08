Protocol preparation, 2026-10-08

Incoming commit: 3d90fcfe9f63d4bd7ff465ac11e33eb2c9d02450 (r6).
Published commit: 6486b2afcee950d8d4cc4bfe7f443c05e10beb9f (r7).
Change basis: explicit user correction, not a measured comparison with r6 teaching.

Changed six controls: SKILL.md, references/sasis.md, reader role, reader contract, rewrite guide and profile manifest. Replaced the task-solver core with a dedicated fresh sequential reader. Preserved baseline bytes and every other original file. Added run index and147-session queue.

Checks performed:
- Read existing main and applicable controls before edits.
- Independent agent audit_sasis_pipeline inspected all six candidate controls through immutable Git blobs and found no material contradiction with the user's reader requirement.
- Pure-JS SHA256 and Git blob SHA1 routines checked against known test vectors; old SKILL computed blob matches actual GitHub.
- All8new/changed tree blobs matched exact candidate contents.
- All31untouched original files retained the exact original Git blob IDs.
- Profile control hashes recalculated; original19baseline/profile payload hashes unchanged.
- All modified Markdown relative file links resolve in candidate tree.
- update_ref used expected old head, forcefalse.
- Published main SHA verified; exact SKILL and protocol contents reloaded and matched.

This is protocol preparation. It does not claim that a lecture, a SASIS reading, human understanding or an entire corpus has been evaluated.
