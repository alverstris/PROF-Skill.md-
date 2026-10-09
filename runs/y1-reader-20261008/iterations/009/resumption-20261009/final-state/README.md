D009 separate final content state

Current state is MECHANICALLY_READY for topic and full declared content project: T1–T12 and all four output checks pass, with exact root final-acceptance.md evidence. This is current content bookkeeping, not iteration closure or a human-learning claim. Canonical evidence/version publication and readback remain root's separate closure gate.

Generation binds ../frozen-prof-r15.md, exact SHA256 24b8c2e2d1898384f85eca608f34074d91a78268efcec69d7ceb81052a87659e. It does not bind the metadata-only r16 working SKILL.md as if it generated this teaching. Original author/.prof-state is untouched; inherited-author-state.json preserves its attribution and initial pending destination/final state. Current v3 SHA256 is 5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244.

Read-only verification from repository root:

```sh
python scripts/prof_state.py check --state runs/y1-reader-20261008/iterations/009/resumption-20261009/final-state --topic curve-sketching
python scripts/prof_state.py check --state runs/y1-reader-20261008/iterations/009/resumption-20261009/final-state
```

To reconstruct paths/dependency bindings after relocation, or after root has genuinely re-reviewed changed acceptance evidence, rerun the exact explicit acceptance command:

```sh
python runs/y1-reader-20261008/iterations/009/resumption-20261009/final-state/reconcile.py --root-accepted --acceptance-evidence runs/y1-reader-20261008/iterations/009/resumption-20261009/final-acceptance.md --acceptance-text 'T12 pass for current content acceptance: root reconciled every reported issue, full source/author/technical/reader/destination evidence and current artifact hashes.' --reader-report runs/y1-reader-20261008/iterations/009/resumption-20261009/sasis-reader-v3-original.md
```

This command was executed after root expressly instructed acceptance binding. It requires the exact current v3 hash in both acceptance and reader records, the exact evidence passage, unchanged original source/request hashes, byte-identical figures, unchanged frozen r15 and a reversible v3 markup-only transformation. It saves helper-generated fresh dependency bindings only after those checks and runs both check scopes. It cannot perform semantic review or independently admit a reader. Changed content requires real review and deliberate script/state changes; do not weaken guards to refresh a stale pass. Running without explicit acceptance arguments can scaffold pending status only before acceptance; it refuses silent demotion of an already accepted state.

Output/evidence paths are repository-relative. The helper schema requires absolute skill, request and source paths; reconcile.py derives these from its own location and relocates inherited original paths. Keep the repository's relative structure when moving it. No global RUN, queue, SKILL or original author file is edited by this script.

Destination scope remains server-parsed mathematics/prose, exact immutable image bytes, inspected markup/CSS and correctly mapped links, plus an independently inspected complete local review preview. Live GitHub pixels, computed styles, client MathJax execution, responsive behavior and actual browser clicks remain unobserved. The internal PDF is evidence, not a user deliverable. See reconciliation.md and destination-v3/review.md for attribution and limits.
