D006: justified PROF candidate change and regeneration condition

Incoming published main remains r12 at bd3453eac9cddd3fa96513aff204f44b8d8196eb. D006 is not closed. Its v1 mathematical/reader checks remain preserved, while T11 is blocked by an independently established destination typography defect.

Observed cause

The v1 P17 Markdown table produces four bare th elements inside the GitHub markdown-body article. Its markup contains no strong/b/em/i, and a complete local PDF preview uses regular upright table headings. Those checks therefore did not detect the destination's prose emphasis. A separate read of all21 stylesheets linked from the captured GitHub page found the matching unconditional rule .markdown-body table th{font-weight:var(--base-text-weight-semibold,600)}. The linked primitives define the token as600; the same Primer stylesheet uses that token for its text-bold utility. Thus this is a concrete destination-stylesheet conflict, not an assumed browser default or a claim based on unseen pixels.

The parent independently reread the exact matching CSS rules and verified their full-file hashes: Primer92ba9f41530ba1da1844d1a0bea93afb5611683f6c2baa01b6df0c9b47e0d6c3 and primitives88a966eb569aa65ffd1442f7c18a056ac0e44d3c87fcdc373fec51456d9371ce. Full provenance and limits are in css-typography-followup.md/json under the v1 render evidence. The initial qualified report and every earlier check remain unchanged.

Narrow trigger/action/check

Existing T11 already forbids bold/italic prose including tables. Its execution here treated unstyled source markup plus a different renderer as enough evidence for part of that requirement. The new clause strengthens that demonstrated inspection trigger, rather than changing the user's typography rule or inserting a lecture-specific answer:

“Check destination styling that can add emphasis without explicit markers, such as table headers. A different renderer's preview or absence of emphasis tags cannot verify this. When the destination forces bold or italic prose and its styling cannot be controlled, preserve the same information and relationships in a representation without that forced emphasis.”

No compulsory browser, universal table ban, new exercise battery or subject-matter instruction is introduced. Controlled-format tables may remain valid when their actual prose styling is compliant. The action applies only when the destination introduces forbidden emphasis; its observable check is the real representation and applicable style evidence, with any runtime limits stated honestly.

Candidate identity and validation

Candidate version2026-10-08-r13-candidate1 is frozen at actual GitHub commit a2389390c0709d65af4a3cf070a04e396e4a4792, tree847aaa8b4318a42ecb195845de1a9e79e39b3b90. SKILL.md SHA2563f7d903a399bdbaaeef397e7af7033dc0229cbb982371ea7c0679fe042c9cc8f,37,454bytes. Parent fetched that actual commit and verified byte equality. Only candidate metadata and the quoted T11 clause differ from r12; reversing those two replacements exactly reproduces every incoming byte, including line endings. All references, baseline and helpers are unchanged. The skill-creator quick validator ran against the user-authorised GitHub checkout and returned “Skill is valid!”; this is syntax validation, not behavioral or installation evidence. The user's explicit GitHub-only/no-installed-edit instruction controls storage and overrides the skill-creator's ordinary installation routing. No installed skill was edited.

Fresh generation, not a patched template

A new fork-none author /root/author_d006_r13_candidate1 was dispatched with the pinned actual skill, exact request, full original eight-page text/images and complete four-subject baseline. It may access only those inputs, applicable operating references and its own new regenerated-r13-candidate1 directory. It receives no v1 teaching, diagnosis, intended representation, previous source-preparation report, reader report, parent answer or rendered example. The candidate instruction itself supplies the general requirement. The original author and original v1 document are not being repurposed as an independent validation.

The parent will independently calculate the new fixed task prompts before reading proposed solutions, inspect the entire regenerated teaching/source coverage, freeze it, and dispatch a separate fresh two-input SASIS reader. It will also check the actual destination representation/styles and a complete secondary preview, then diagnose all new issues and recheck affected earlier successes. Candidate existence and the previous v1 mathematical result do not close this iteration or prove the generation succeeded.

Earlier-case dependency scope

The substantive addition concerns emphasis introduced by destination markup/style; subject teaching, ordinary source checks, baseline and reader protocol are unchanged. A targeted scan of every existing D001–D005 teaching version found no Markdown pipe tables. Accepted versions are D001v4,D002v1,D003v1,D004v1,D005v2. Their actual accepted artifact/markup evidence must be checked for the new trigger before recording the earlier-case disposition. No automatic universal regression pass is inferred from unchanged prose or that initial scan.
