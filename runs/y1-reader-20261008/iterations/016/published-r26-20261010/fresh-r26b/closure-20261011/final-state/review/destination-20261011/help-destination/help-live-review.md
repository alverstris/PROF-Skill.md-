# D016 r26b — actual GitHub help destination review

PASS for the exact assigned render/navigation gates. No defect found. This additive review does not replace any original review.

Frozen commit: `51a78beccef858072b1da8d057ef3dff09878409`. Destination directory: `runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b/teaching/`. Review date: 2026-10-11 UTC. Separate cloud Chrome tab 2 was used; root tab 1 was not navigated.

## Full read and preservation scope

Read hints.md completely (33 source lines; title, route, P1–P5 and all navigation) and solutions.md completely (170 source lines; title, route, P1–P5, every worked expression, final paragraphs and returns). Applied the exact local r26 PROF T11, T12 and markup-destination output conditions. This was a destination-only review; no baseline/SASIS or new subject-matter audit was started.

All 76 intended expressions were compared individually against hydrated MathML obtained from the actual GitHub article DOM: 12 inline expressions in hints; 48 inline and 16 display expressions in solutions. Operands, operators, signs, subscripts, powers, fraction boundaries, round/square/absolute-value grouping, integral and sum limits, evaluation-bracket limits, and the three aligned rows in solution P4 all preserve the frozen source. A second narrow reviewer independently compared every expression to the saved actual-destination DOM and found the same result. That secondary check did not claim its own browser visual inspection. See mathml-preservation.json for each source expression, corresponding MathML, and structural witness.

The complete nonmath prose and link-label streams also match the frozen sources after removing Markdown/HTML markup and normalizing whitespace. Local teaching hashes remain the freeze values:

- hints.md: `f8db498eb437546f39916714a35b7a1217dba1d6407d94bde33ed6d2c5ed6014`
- solutions.md: `5a616e257b6c83bce341e5332b036ab92b23f4430b2308b09ac74123b6d57c9a`

## Actual visual and style inspection

Visually inspected the entire hints article, all five solutions at readable desktop viewport size, and the solutions title/introduction separately. Full-page solutions evidence supplements the five viewport solution captures. No omitted, clipped, overlapping, unresolved-TeX or malformed expression was found. Math in initial accessibility output was transient raw TeX before hydration; acceptance uses the final rendered MathML and screenshots, not that initial output.

The actual computed font weight/style is `400`/`normal` for every help prose paragraph and anchor sampled exhaustively from each article, including the titles, labels, route text, and return/help links: hints has 17 paragraph elements (12 nonempty) plus 16 anchors; solutions has 43 paragraph elements (38 nonempty) plus 12 anchors. Conventional mathematical italics are distinct from prose. GitHub's surrounding repository chrome is outside the authored teaching article.

Hints and complete solutions are grouped on separate files with distinct plain labels. Hints show intermediate help and route links, with no complete answer interleaved. Complete solutions provide an explicit route back to tasks and separate hints.

## Navigation actually clicked

All five route types were clicked and verified for each P1–P5: task→hint, task→solution, hint→task, hint→solution, solution→task. All 25 unique required edges retain the frozen commit, reach the matching file/hash, contain the correct GitHub-prefixed target anchor, and settle with the corresponding label visibly within the 936-pixel-high viewport. Global solutions→hints was also clicked and reached the separate hints article.

| Task | Required edges | Task anchor top (px) | Hint anchor top (px) | Solution anchor top (px) |
| --- | --- | --- | --- | --- |
| P1 | 5/5 | 125.31 | 231.00 | 125.00 |
| P2 | 5/5 | 124.55 | 359.00 | 125.47 |
| P3 | 5/5 | 124.69 | 487.00 | 125.22 |
| P4 | 5/5 | 318.64 | 615.00 | 125.31 |
| P5 | 5/5 | 518.64 | 743.00 | 238.64 |

Near-end P4/P5 and the shorter hints page settle lower in the viewport because document-bottom clamping prevents placing every target at the top; the complete requested target remains visible. GitHub navigation and scroll are asynchronous: several immediate same-call observations show pre-scroll positions. Those observations remain unchanged in navigation-observations.json and are not accepted as settled evidence. The later `settled` witnesses and screenshots establish actual landing. The report's summary selects only settled in-viewport witnesses for the 25 edges.

## Evidence and remaining limits

- hints-rendered-dom.json and solutions-rendered-dom.json: full hydrated article HTML/MathML, exhaustive prose styles, anchors and links.
- mathml-preservation.json: all 76 source-to-render expression comparisons and full prose correspondence.
- navigation-observations.json: raw actual-click history, including provisional and later settled positions.
- help-destination-summary.json: the exact 25 accepted edge witnesses and scoped PASS.
- hints-bottom-final.jpg: complete hints article at usable size.
- solution-p1-final-landing.jpg through solution-p5-final-landing.jpg: all complete solution sections at usable size.
- solutions-full.jpg: supplementary full-page visual coverage; its sticky header obscures the opening title/intro, which was checked in a separate top-of-page screenshot.
- task-p1-final-landing.jpg and task-p5-final-landing.jpg: representative stable return destinations.

This PASS concerns the inspected desktop Chrome destination only. It makes no mobile, other-browser, alternate-zoom, student-mastery, historical-review, subject-correctness or Overleaf claim. Root owns lesson-expression and figure review. No frozen teaching, PROF package, GitHub file, original review or earlier report was edited. No remaining render or navigation issue was found within this assigned scope.

## Additive global-navigation completion — 2026-10-11

The four remaining global local-content links were actually clicked in the same separate browser tab and their final article titles and exact frozen-commit URLs verified in subsequent observations:

| Origin | Clicked label | Verified destination | Article title visible at (px) |
| --- | --- | --- | --- |
| solutions.md | tasks in the lesson | lesson.md | 396 |
| lesson.md | Hints | hints.md | 204 |
| hints.md | solutions | solutions.md | 396 |
| lesson.md | complete solutions | solutions.md | 224 |

All four PASS. Together with the previously verified solutions→hints global link, all five global local-content navigation edges are covered. The 25 task/help edges remain accepted without re-audit. Combined local-navigation scope is now 30/30 actual-click content links; root separately owns the three embedded figure loads. Exact observed URLs and article titles are in global-navigation-supplement.json. Earlier reports and raw observations were preserved.
