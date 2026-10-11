# D007 r29 complete destination preservation

**PASS — all 308 expressions preserve their full mathematical structures and types.** Complete nonmath prose, all 41 textual link labels and resolved hrefs, all 25 anchor IDs, and the figure alt text also match. This is preservation only, not a scientific or SASIS verdict.

The complete frozen package was independently inventoried before capture comparison, and all four teaching/PNG hashes match `freeze-manifest.json`. Actual captures use immutable commit `4765d39aa399a0a1ff09223cae21b15ce6c7f720`.

| File | Expressions | Inline / display | Normalized prose characters | Textual links | Result |
|---|---:|---:|---:|---:|---|
| lesson | 200 | 170 / 30 | 15,873 | 17 | PASS |
| hints | 39 | 39 / 0 | 1,871 | 9 | PASS |
| solutions | 69 | 56 / 13 | 4,702 | 15 | PASS |
| Total | 308 | 265 / 43 | 22,446 | 41 | PASS |

Every source math expression was mapped to its article slot, with no extra, missing or raw-code slot. Every complete source structure was independently compared against actual MathML, preserving operands, operators, grouping, primes, fractions, roots, powers, subscripts, sum limits and binomial arguments. The MathML strings embedded in each article exactly equal its ordered math array. None of the captures contains an explicit mathematics renderer error.

The structures include 78 ordinary fractions, one binomial stack, 282 script structures, nine square roots, three limit lower operands and one bounded sum. The binomial is preserved as parenthesized `n` over `k` with no fraction bar; it is never normalized into ordinary division. Useful witnesses in `lesson/math-preservation.json` are records 4, 50, 125, 126, 131 and 142.

Full prose comparisons preserve wording, case, punctuation, order and every math-slot position while removing only document markup and normalizing whitespace. Hyperlinks preserve each label and exact destination after resolving source-relative and GitHub root-relative paths against the same immutable article URL. Source anchor IDs receive only GitHub's verified `user-content-` prefix. The one image-wrapper anchor is recorded separately from the 41 textual links; the complete figure alt text matches.

Root's separate recoverable GitHub SPA page-loading error during cross-file UI navigation is outside this verdict. Href/anchor preservation does not assert successful clicks. Root also owns visual geometry and image inspection.

The complete per-expression, prose, link, anchor and alt records are in `lesson/math-preservation.json`, `hints/math-preservation.json` and `solutions/math-preservation.json`; each has a concise Markdown report. The solutions comparison uses `solutions/rendered-dom-recovered.json`, the persisted recovery of root's actual capture. `math-preservation.json` records all source/capture/report hashes and combined results.

V3 is separately saved at `/workspace/scratch/f9c0b7fc7e76/root-destination-tools/compare_destination_preservation_v3.py`. SHA-256: `9db7b8cb2707ef597b148faaa143447e5e4248a685dca6bb928213653e8db9da`. Its only new equivalences are the observed D007 elementary function tokens, `ne`/`pm`, explicit binomial stack, id anchors and immutable URL resolution. Unknown syntax/MathML still fails explicitly; no algebraic equivalence is used. V2 and its archive, all frozen teaching files and GitHub remain unchanged.
