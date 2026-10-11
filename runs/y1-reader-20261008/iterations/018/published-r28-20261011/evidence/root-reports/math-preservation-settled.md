# D018 settled destination preservation

**FAIL — the settled capture confirms the original preservation failures. No lazy-loading restoration was observed.** All 288 source slots were compared again. Their rendered MathML/raw fallback content and individual comparison results are unchanged from the first capture.

Source SHA-256: `4970a5ae04a73cca02eb62a20de8b5eab8d225c6b9ceb22eee44ec6a6408873c`  
Settled capture SHA-256: `c1dbf83066c5a0aca2eba40b84ca9b99b2805fd1669aee7a23e60ef1243c1b73`  
Settled observation: `2026-10-11T21:59:09.226Z`  
Destination: https://github.com/alverstris/PROF-Skill.md-/blob/f8f76d0775051896326fb400ec5782bf1d954971/runs/y1-reader-20261008/iterations/018/published-r28-20261011/teaching.md#s1

| Check | Settled result |
|---|---|
| Source expressions | 288: 259 inline, 29 display |
| Actual native MathML | 272: 253 inline, 19 display |
| Preserved structures | 271 |
| Truncated rendered expression | 1: source record 22 |
| Explicit `operatorname` errors | 10 |
| Raw solution displays without MathML | 6 |
| Existing MathML types | All 272 match their source types |
| Full nonmath prose | Exact match; 22,612 normalized characters |
| Textual links | All 26 labels and hrefs match |
| Image alt texts | Both match |

Record 22, source line 28, ends `(x<a).` in source but only `(x` in actual MathML. The missing tokens are `<`, `a`, `)` and the final period.

The ten explicit renderer errors are source records 123, 126, 132, 133, 134, 157, 160, 161, 163, 165. Their destination message remains “The following macros are not allowed: operatorname.”

The six raw solution displays are source records 252, 258, 264, 271, 281, 286. All six remain inside open disclosures as `<pre lang="math"><code>…</code></pre>` with no MathML. Their surviving raw text matches the source, but mathematical rendering has not been restored. The settled capture itself reports ten error messages and six raw math blocks.

Root additionally confirmed these blocks after actual scrolling with both disclosures open: `viewport-12-recovery.jpg` covers Q1; `viewport-13.jpg` covers Q2, Q3 and Q4; `viewport-14.jpg` covers both Q5 displays. Those are root-provided visual witnesses, not a claim of independent browser inspection by this comparator. Their paths and hashes are recorded in the settled JSON.

The 272 embedded article MathML strings still exactly match the capture's MathML array. Every operand/operator, visible delimiter, fraction, root, script attachment and integral bound in those expressions was compared through independent source and actual-MathML structures. Failed slots retain complete raw HTML and source-text witnesses; no failed rendering is treated as a pass.

The separate nonmath prose comparison removes markup and collapses whitespace while preserving words, case, punctuation, order, disclosure summaries and all mathematical-slot positions. Normalized prose SHA-256: `b35c4d7e10c5f90fe68369d2d5b012aff8160b8fe4c4faec55f89f1053345d5c`. Two image-wrapper anchors are recorded separately from the 26 textual links.

`math-preservation-settled.json` contains all 288 per-expression records and full prose/link/alt comparisons. The original capture and original `math-preservation.json` / `math-preservation.md` remain unchanged. The frozen source, D017 reports and v1 comparator also remain unchanged. No browser operation or GitHub write was performed here. Scope is destination preservation only, never scientific or SASIS validation.
