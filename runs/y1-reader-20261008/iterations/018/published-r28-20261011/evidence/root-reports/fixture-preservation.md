# D018 prospective syntax fixture preservation

**Six native expressions pass; four disclosure displays fail.** This is the independent fixture only, not a repaired lecture or evidence of teaching/scientific/SASIS acceptance.

Source SHA-256: `1079963d3a7917efe60d967e5f9c9560fde28f4171b670d97cf36203c11605fa`  
Capture SHA-256: `6bdbce6088ec0c9b332dc12c57e8815f4c959486d02122beebe93ba0fdf03558`  
Observed: `2026-10-11T22:02:44.436Z`  
Immutable fixture: https://github.com/alverstris/PROF-Skill.md-/blob/19ae7d1816f52649c65d1e5cbf54044a777b8c90/runs/y1-reader-20261008/iterations/018/published-r28-20261011/evidence/repair-probe/syntax-fixture.md

| Fixture | Source type | Actual result |
|---|---|---|
| P1 | inline | Native structure fully preserved |
| P2 | inline | Native structure fully preserved |
| P3 | display | Native structure fully preserved |
| P4 | display | Native structure fully preserved |
| C1 | inline | Native structure fully preserved |
| C2 | display | raw fenced display |
| C3 | display | raw double dollar display |
| O1 | inline | Native structure fully preserved |
| O2 | display | raw fenced display |
| O3 | display | raw double dollar display |

All six native structures were independently checked in full. P1, C1 and O1 retain the complete upright `Aux` name, input, equality and squared operand. P2 retains `u < v > w`. P3 retains the derivative prime on the whole name, both equations, the square root of `u²`, the strict comparison, closing parenthesis and final period. P4 retains `M(u)=`, the left case brace, both rows and two cells per row: first value `u` with condition `u < 0`; second value `u²` with condition `u ≥ 0`, including source punctuation. No operand, comparison, power, row or delimiter is lost in these six expressions.

Both disclosures are open in the actual capture. C2/O2 remain raw fenced `pre lang="math"` code. C3/O3 remain raw double-dollar text in paragraphs. All four raw contents equal their source expressions, but none has MathML, so all four fail rendered-math preservation. There are zero explicit renderer errors. The native total is four inline and two display expressions versus four inline and six display expressions in source.

The full nonmath prose and disclosure summaries match after markup/whitespace normalization with ten positional math markers. This fixture has no links or images. `fixture-preservation.json` records every source expression, complete actual MathML or failed-slot HTML/raw text, independently specified expected structures, and full normalized prose.

The result demonstrates the tested `\mathrm`, strict-comparison and cases syntax in plain content at this pin. It does not establish display rendering inside either initially closed or initially open disclosures. V2, its archive, all frozen lecture files and GitHub were unchanged.
