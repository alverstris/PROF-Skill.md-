D001 math-format repair, v2 to v3

Inspection of GitHub's canonical HTML for frozen v2 revealed that all 249 inline expressions received math-renderer elements, but none of the 39 display blocks did. Literal $$ delimiters remained inside ordinary paragraph markup. Markdown escaping also damaged six inline thin-space commands and nine display blocks. Source delimiter counts and a successful Pandoc preview would not detect these GitHub-specific failures. The original rendering report is preserved separately.

V3 uses GitHub's protected dollar/backtick inline syntax and fenced math display blocks, with blank paragraph boundaries. These forms are documented at https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions (read 2026-10-08). All 249 inline and 39 display mathematical payloads remain exact; inverse delimiter conversion preserves every nonblank source line, including all prose, conditions and help. This replaces an unpublished spacing-only candidate before freezing; that candidate never received a reader or acceptance claim.

The mathematical/physical review retains the same content dependency; actual GitHub markup and visual checks and a fresh SASIS reading are required for this revision.

This is an execution defect under existing T11 and the existing rendering gate, not evidence that a general teaching rule is missing. No pedagogical improvement claim or iteration closure follows merely from the format patch.
