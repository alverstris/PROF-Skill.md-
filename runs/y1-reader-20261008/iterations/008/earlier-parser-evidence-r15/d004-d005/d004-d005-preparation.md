# D004–D005 historical parser-regression preparation

Prepared 2026-10-09. Scope: read-only review of the accepted D004 and D005 teaching identities, final closure records, original final destination/render reports and retained local artifacts. This is preparation for the proposed PROF clarification, not candidate regeneration or a final global regression verdict. No repository file, teaching content or skill was edited; no Git fetch, network request, source research, SASIS work or new renderer run was performed.

The proposed clarification asks whether the actual destination preserves every intended expression's operands, operators and grouping, including inline mathematics and help, uses supported syntax against parser collisions, and distinguishes parsed-content evidence from live visuals. For these cases, exact full payload equality supports preservation of all source mathematical characters at the captured parsed-content layer. It does not demonstrate subsequent client interpretation or displayed pixels.

## Identity and destination mapping

All paths below are relative to `/workspace/scratch/ac36b9c5ff31/PROF-repo/` unless explicitly absolute.

| Case | Accepted teaching and immutable destination | Accepted byte identity | Present local frozen-object check |
|---|---|---|---|
| D004 | `runs/y1-reader-20261008/iterations/004/teaching-v1.md`; commit `197b57555834d36952e948d4100d2f835c86b20c`; [immutable GitHub article](https://github.com/alverstris/PROF-Skill.md-/blob/197b57555834d36952e948d4100d2f835c86b20c/runs/y1-reader-20261008/iterations/004/teaching-v1.md) | 22,691 bytes; SHA-256 `5adb3e95c2fa47c94b4c665d85dc2fe669e2c0086dbc2ebc194cd59720d5d8ad` | Read-only `git show COMMIT:PATH` succeeded; its bytes equal the working file and accepted hash. |
| D005 | `runs/y1-reader-20261008/iterations/005/teaching-v2.md`; commit `32c553f279ac1e5771ff05b78a9951cbff3fee38`; [immutable GitHub article](https://github.com/alverstris/PROF-Skill.md-/blob/32c553f279ac1e5771ff05b78a9951cbff3fee38/runs/y1-reader-20261008/iterations/005/teaching-v2.md) | 24,261 bytes; SHA-256 `4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6` | Read-only `git show COMMIT:PATH` succeeded; its bytes equal the working file and accepted hash. |

The current local measurements are in `local-evidence-verification.json` in this preparation directory. They are separate from the original reviewers' observations.

## D004 exact historical witnesses

- Final acceptance identity: `iterations/004/closure.md:5`; actual-representation closure summary: `closure.md:14`; explicit live-render limits: `closure.md:19`. These paths use the common prefix `runs/y1-reader-20261008/`.
- Original final report: `iterations/004/render-review-v1-original.md`, read in full. Lines 11–19 identify the immutable destination, exact source bytes/hash, the reuse of the original immutable capture, and the captured page hash. The final source is v1; the corrected review is not a new teaching version.
- Whole actual destination content: report lines 46–61, particularly line 48 and lines 54–55, say the complete article matches normalized source and all 275 inline plus all 30 display payloads match exactly after HTML parsing. Math is protected during prose normalization and is separately compared exactly. This is stronger than source validity, protected delimiters or a second renderer alone.
- Whole math data, beyond pass flags: `iterations/004/render-markup-v1.json:133` begins the full math record; inline source/actual arrays begin at lines 138 and 415; display source/actual arrays at lines 697 and 729. The destination identity and fetch record are at lines 968–978. The final actual HTML resides at `/workspace/scratch/ac36b9c5ff31/prof-readability/d004-render-review/v1-corrected/github-article.html` and `github-page.html`.
- Help coverage: original report lines 61 and 67–78 explicitly map all tasks A–D and corresponding hints, full solutions and returns. Hints are P26–P30 (entries P27–P30); solutions are P31–P35 (entries P32–P35). The independent preparation count finds 19 inline/0 display payloads in the hint group and 44 inline/6 display payloads in the solution group. Those are subsets of the exact whole-article payload comparison, not a claim inferred from links alone.
- Complete secondary preview: original report lines 80–100 describe exact preview payload conversion, all nine complete final pages opened, and the whole-page coverage table. Pages 7–8 contain all help; page 9 covers the final source/scope continuation. All 30 displays were specifically inspected, and the report notes fractions, evaluation bars, superscripts, primes, inequalities, minus signs and parentheses. Per-page original records begin at `iterations/004/render-preview-v1.json:48`; the complete page list begins at line 190.
- Page-break and modality limits: original report lines 102–114 disclose P05, P17 and P25 heading/body breaks and all continuing text/displays. The preview uses local pdflatex, not GitHub CSS/MathJax; live pixels, responsive behavior and clicking were unobserved. The final closure repeats the limit.
- Prior-failure separation: report lines 23–44 diagnose the earlier label-counting helper failure. This preparation does not use that initial failure, or another case's regression result, to establish D004's final preservation.

The original page report's coverage is:

| Preview page | Historical full-page coverage | Displays |
|---:|---|---|
| 1 | P01–P04; P05 label/title | 1–3 |
| 2 | P05 body; P06–P09; Tasks A/B | 4–6 |
| 3 | P10–P11; P12 through final display | 7–12 |
| 4 | P12 conclusion; P13–P16; P17 label/title | 13–15 |
| 5 | P17 body; P18–P19/Task C; part of P20 | 16–21 |
| 6 | P20 continuation; P21–P24/Task D; P25 label/title | 22–24 |
| 7 | P25 body; P26–P32; all hints and complete Solution A | 25 |
| 8 | P33–P35; complete Solutions B–D; P36 start | 26–30 |
| 9 | Complete P36 remainder and final sentence | None |

Preparation identity checks also confirmed the recorded captured-page SHA-256 `ec8718015dbe2f244f847497c0715563eb10e05e64dda3d3808d1d0f831435fe`, captured-article SHA-256 `f62b483587c9be18efc5febeb16570e352f8b51ce093b3f98bdded0a8a4f5586`, preview PDF SHA-256 `91975b673de656adec1d6559873708a7ad33b1b310364ecb69c063d14e016e9d`, and every recorded `fullpage-1.jpg` through `fullpage-9.jpg` hash. The copied original report equals `v1-corrected/report-v1.md` byte for byte.

D004 preparation recommendation: no accepted-artifact identity gap, formal inline/display/help payload gap or complete-secondary-preview documentation gap was found. Carry the original full-payload and whole-page witnesses into the scoped regression review; do not replace them with readiness flags or a delimiter-only claim. The unobserved actual-client layer remains an explicit gap only for a stronger claim of live destination visual/MathJax correctness. If that stronger claim is required, the minimum recheck is the unchanged immutable destination, with all inline/display mathematics and help inspected in its live renderer; a new local PDF would not close that gap.

## D005 exact historical witnesses

- Final accepted identity: `iterations/005/closure.md:5`; final representation result: `closure.md:9`; live limits: `closure.md:13`. `iterations/005/frozen-inputs-v2.json:2` and lines 21–25 bind the accepted v2 path, byte count and SHA-256. `iterations/005/parent-acceptance-v2.md:3` confirms this is the accepted teaching and that there are no other learner constituents.
- Original final report: `iterations/005/render-evidence/v2/render-review-original.md`, read in full. Lines 7–13 identify the frozen commit/path/hash and raw-source match and distinguish actual captured markup from the secondary preview.
- Whole actual destination content: original report lines 15–28 explicitly state ordinary HTML parsing without a second entity-unescape step, exact ordered/whitespace equality for all 280 inline and 23 display payloads, complete normalized article-text equality and all Q1–Q5 navigation routes. The 13 changed comparator spans preserve their `\lt`/`\gt` spellings, and captured article text has no `&amp;lt;` or `&amp;gt;` form (line 20).
- Whole math data, beyond pass flags: `iterations/005/render-evidence/v2/markup-audit.json:120` begins the complete math record; inline source/actual arrays start at lines 125 and 407; display source/actual arrays at lines 694 and 719. Destination/fetch identity is at lines 1052–1061. Actual captured HTML is retained alongside the report in `github-article.html` and `github-page.html`.
- Final-v2 separation: `iterations/005/parent-acceptance-v2.md:13` records that the 13 protected-inline substitutions change 17 comparison-sign spellings and invert to the exact v1 byte string. Lines 33–35 distinguish failed v1 serialization from actual v2 evidence. The historical v1 failure is not used as final-v2 evidence here. There is direct accepted-v2 destination evidence.
- Help coverage: original report lines 24–25 cover all five question/hint/solution routes and ordering; the page table at lines 41–43 covers all five hints P29–P33, group headings P28/P34, and complete solutions P35–P40 including continuations and returns. Preparation counts 22 inline/0 display payloads in hints P28–P33 and 45 inline/7 display payloads in solutions P34–P40, each included in the whole exact-payload comparison.
- Complete secondary preview: original report lines 30–45 and the eight-row table record every final page opened in full at 1020 × 1320 pixels, 120 dpi. Pages 1 and 7 use complete recovered images, not the rejected original exports. Lines 49–53 disclose the export failure, unchanged PDF, recovered full-page inspection and the preview-only pagination seams. Per-page records begin at `iterations/005/render-evidence/v2/preview-check.json:46`; the independently recorded parser review begins at line 320.
- Modality limit: report lines 3, 13, 28 and 53, closure line 13 and parent acceptance line 41 consistently leave live GitHub MathJax, pixels, responsive layout and clicking unobserved. Local visible comparison signs and server payload equality are explicitly separate findings.

The original page report's coverage is:

| Preview page and final viewed image | Historical full-page coverage |
|---|---|
| 1, `page-recovery-1.png` | P01–P06; circle displays; repaired P04 interval; Q1 beginning |
| 2, `page-2.png` | Q1 continuation; P07–P12; product/implicit derivative and inverse identity; Q2 help labels |
| 3, `page-3.png` | P12 continuation; P13–P17; inverse identity/quotient and repaired P16 comparison |
| 4, `page-4.png` | P17 continuation; P18–P21; cubic inverse, rational powers, zero quotient and repaired positive domains |
| 5, `page-5.png` | P21 continuation; P22–P27; repaired inline inequalities; arctangent/triangle; Q3/Q4; Q5 start |
| 6, `page-6.png` | Q5 continuation; all hints P29–P33 and group labels; S1/P35 and start of S2/P36 |
| 7, `page-recovery-7.png` | P36 continuation; P37–P40; rational-power, zero, inverse-slope and F/G displays; tangent lead-in |
| 8, `page-8.png` | P40 tangent display/explanation/return; complete P41 and document end |

Preparation identity checks confirmed the recorded captured-page SHA-256 `979613f82c70b12b6268df06b947dec4be42977192722de59af55f5018498666`, captured-article SHA-256 `24fbac5e8b61dc3532ac2da047970c01b81a7c5043dd2ca1b0294715bb65316e`, preview PDF SHA-256 `26f6aae873b2c75330c65fd143af0ce11fd486b417141d1a9594978e22afc533`, and all eight historically viewed final page-image hashes. The copied original report equals `/workspace/scratch/ac36b9c5ff31/prof-readability/d005-render-review/v2/render-review-original.md` byte for byte. The rejected `page-1.png` and `page-7.png` are not substituted for the two recovered final viewed images.

D005 preparation recommendation: use only final accepted v2 for regression. No accepted-artifact identity gap, formal inline/display/help payload gap or complete-secondary-preview documentation gap was found. The known v1 entity-serialization collision has direct whole-v2 parsed-content evidence after the supported comparison-command repair. Do not infer live-client correctness from that equality or from the separate PDF. If live destination visual correctness is required, the minimum recheck is an all-content scan of the unchanged v2 immutable destination, including the repaired inline spans, the other inline/display expressions and every help continuation. No source or candidate regeneration is justified by the evidence reviewed here.

## What this preparation itself observed

`local-evidence-verification.json` records fresh local byte/hash checks, successful local frozen Git reads, and comparisons of every formal source math payload with retained captured HTML and the original audit arrays. The parser was Python's standard `HTMLParser(convert_charrefs=True)` with only each math-renderer's `$` or `$$` wrapper removed; there was no additional entity unescape. Both cases' source and captured payload lists match exactly in order, including all operands, operators and grouping characters represented in those payloads. This comparison used retained actual destination captures; it did not generate new destination content.

This preparation read the original reviewers' full-page reports and verified the available page/PDF identities. It did not open those pages for a new visual inspection. Claims that pages were visually inspected belong to the original reviewers and retain their documented secondary-preview scope. Complete normalized prose/article equality is an original-report finding; the new local comparison specifically rechecked all formal math payloads. No new claim is made about mathematical teaching truth, intended meaning outside the accepted source, human learning or present live destination behavior.
