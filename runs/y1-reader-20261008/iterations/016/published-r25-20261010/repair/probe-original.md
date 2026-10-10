Bounded reference audit

Scope and actual reads

This is an ordinary PROF author audit of the supplied reference, not SASIS, document generation or a student-understanding assessment. I read candidate/prof/SKILL.md in full (162 lines; version 2026-10-10-r26) and references/execution-protocol.md in full (111 lines). The initially clipped tool output was reopened to recover the omitted text. I then read all 11 lines of probe-input/notes.md and visually inspected both complete PNG exports, motion-a.png and motion-b.png, at their original 1152 × 576 size, including all canvas edges. No adjacent reports, repair scripts, previous artifacts, other contextual files or external sources were read. No browser inspection was performed or required by the requested local-export scope.

The excerpt states its prerequisites: ordinary definite integrals, average value and multiplication of units. It explicitly contains no learner-response tasks. The task instruction says “do not demand practice for this explicit reference-only scope”: practice is waived_by_user within that scope (T5); retained-task requirements T6–T7 are not_applicable because there are no tasks; an added retrieval programme under T8 is not_applicable to this reference audit. No missing exercise, hint or solution is reported as a defect.

Findings

1. Mathematical error, notes.md line 3, final sentence (T3, T10).

“Integrals and averages always have different units” is false under the excerpt’s own stated conditions. The integral has units [q][u], whereas the average has units [q][u]/[u] = [q]. Here u and its interval width are dimensionless, so both quantities have units of joules. As a direct check, taking q(u) = 3 J throughout [0,1] gives an integral of 3 J and an average of 3 J. The preceding description of adding q(u) times du and dividing by the width one is correct. Preserve it; replace only the universal conclusion with the conditional units rule or the explicit statement that both quantities here are in joules.

The comparison in line 5 is valid: watts multiplied by seconds gives joules; dividing that integral by the duration in seconds gives watts. It illustrates a dimensional integration variable and does not rescue the unconditional sentence.

2. Export usability defect, motion-b.png, bottom and top canvas edges (T11).

The bottom horizontal axis and tick marks are visible, but their numerical labels and the horizontal-axis name/units are outside the visible export. At the top, the “4.0” vertical-axis tick label is cut by the canvas edge. These omissions prevent reading the time scale directly from the figure. Its vertical-axis label and the visible line remain readable; no incorrect displacement relation is established by this cropping. Re-export with margins that retain the full text, then inspect the saved export at the intended reading size. An absent title alone is not treated as proof that a title was clipped, because no intended title for this file was supplied.

Preserved valid content

motion-a.png has a complete readable title, both axis labels and units, and numerical ticks. Its line passes through (0 s, 0 m), (1 s, 2 m) and (2 s, 4 m), consistent with the line 7 description. The line touching the plot boundary at its endpoints is appropriate for the stated interval, not a figure defect. No mathematical or local-export usability issue was found in this first figure. The introductory integral/average definitions and the power comparison also remain valid.

Revision binding and limits

SHA-256 of the inspected inputs:

- notes.md: af59e82b19da0b02e77428960529c71ff2c687473559f752af58c2b09a100c86
- motion-a.png: 7578e74150bae7cfcd6f5cab234f704c60df49f96c61c54c82d99065cd265e35
- motion-b.png: 754acdfbeed5a83f7acf4e9d1ab0c622318ac4cc2532afcc653d4349b15cd46e
- SKILL.md: a92d012395263f3410152045424c2e6f02300705d81720b5e1fd9590584448a0
- execution-protocol.md: ea32dc1af6c2141192eeadabd3f8360570dade0bf010f3f34dade298acdd2a60

This report records two observed defects and preserves the valid material. All requested input portions were reviewed; the inputs remain unchanged. No global PROF acceptance, browser rendering, source-bundle portability, corrected-export verification or learner mastery is claimed. The report is the sole new artifact.
