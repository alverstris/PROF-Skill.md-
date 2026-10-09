Proposed production clarification — not yet applied

Incoming canonical skill is published r14 at e35a59a64ed1b01f7ae43e4ef46042f23cc7e2d6. The current corrected document is frozen at 4b4bcc9b8ff15772031e67282e73f624fe41eed2; its fresh SASIS reading and final destination report are still in progress. Settle all supported findings before freezing a candidate.

Evidence and inference

Current T10/T12 and release requirements already reject mathematically corrupted output; the actual release checks caught it. The narrower operational omission is preservation of mathematical content across host parsing. T11 explicitly addresses destination-added prose emphasis but does not explicitly identify this math-parsing boundary. D008 P124 was served as a hyperlink rather than a mathematical expression, hiding its (-2) factor. Eleven other expressions changed payload. D007 also showed that protected delimiters alone did not prevent literal comparison entities. These are observed representation failures, not evidence of student difficulty or an outcome experiment.

Root and an independent advisory reviewer judge that a single focused production paragraph is warranted. A generic extra instruction to check rendering would merely repeat existing duties. The paragraph should require preservation of operands/operators/grouping in every expression, including inline/help content, and distinguish source, parsed destination and live rendering evidence. It should not demand byte equality between mathematically equivalent syntax or claim that any delimiter recipe guarantees preservation.

Proposed insertion under Verification and release, before format-specific production

For mathematics delivered through markup, check that the actual destination preserves every intended expression’s operands, operators and grouping, including inline mathematics and help. Use destination-supported syntax to prevent parser collisions; correct source, protected delimiters or another renderer’s preview alone cannot establish preservation. Distinguish parsed-content checks from live visual inspection.

Supporting implementation reference

GitHub’s official Writing mathematical expressions page was opened in full by root on 2026-10-09: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions . It documents protected inline delimiters for Markdown-overlap characters and fenced math blocks. That documentation supports available syntax, not an unconditional preservation guarantee. Root’s initial official-domain search returned a diagrams page rather than the target; the directly opened math page supplies the actual syntax evidence. No broad documentation claim or live-browser test is inferred.

Validation consequence if adopted

Treat the change as substantive. Freeze the actual GitHub candidate before a fresh author receives only that candidate’s controls, the original lecture and the complete baseline. Do not give that author the previous lesson, diagnoses, prior solutions or reader reports. Freeze its new prompts for an independent parent calculation, complete independent actual-destination/whole-document review, and send its complete frozen teaching plus the entire baseline to another fresh SASIS reader. Reopen affected earlier final-output evidence against the added preservation duty. The existing metadata-only closure scaffold cannot be used unchanged. Do not call the current local teaching repair a demonstrated skill improvement.
