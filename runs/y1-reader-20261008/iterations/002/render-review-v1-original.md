# D002 v1 frozen representation review

The actual GitHub-delivered article markup passes the checks below, and no visual defect was found in the complete local PDF preview. Live GitHub client pixels, MathJax execution, responsive layout and click execution remain unobserved. This is a representation review, not pedagogy or SASIS, and is not a claim of complete live-browser verification.

## Frozen inputs and provenance

- Frozen commit: `f1c0e91c24e9140049d50c7ca965f41e36f3e1a2`.
- Canonical article: https://github.com/alverstris/PROF-Skill.md-/blob/f1c0e91c24e9140049d50c7ca965f41e36f3e1a2/runs/y1-reader-20261008/iterations/002/teaching-v1.md
- Source: `/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/iterations/002/teaching-v1.md`, 34,994 bytes, SHA-256 `8139080278edb96287576629e7d80933b380c1b82af60d3ede888d500cb68a3a`.
- Sole constituent image: `figures/unit-circle-proof-v1.png`, 90,094 bytes, SHA-256 `95616719d3035e9f174367b55c48ccb3e04a8cbf5105434115e4bddff0b3c75d`.
- The parent-supplied `github-page.html`, `github-article.html`, `github-article-text.txt`, `markup-audit.json` and `preview-header.tex` were read and left unchanged. Their exact hashes are recorded in `preview-check.json`. The supplied page's SHA-256 remains `c36cce22b52d7ce15a738b4910c5308b12c0eb77ce14695752e2a74f28f713a8`.
- Public HTTP GETs of both raw commit URLs returned 200. Source bytes match the local frozen file exactly. Image bytes match both the expected hash and the repository constituent exactly. Records: `source-fetch.json` and `image-fetch.json`. The image was fetched from https://raw.githubusercontent.com/alverstris/PROF-Skill.md-/f1c0e91c24e9140049d50c7ca965f41e36f3e1a2/runs/y1-reader-20261008/iterations/002/figures/unit-circle-proof-v1.png . A local Git tree lookup was unavailable, so the independent commit-URL identity check used public raw HTTP.

## Actual destination markup

The entire delivered article was parsed, and its complete text stream was compared with the frozen source after documented removal of Markdown link/image/anchor syntax and math-delimiter conversion, with whitespace normalization. The complete text agrees. Math was protected during that comparison and separately compared exactly; this did not rely on selected excerpts.

| Check | Result |
|---|---|
| Paragraphs | P01–P72 each present once, in order |
| Inline mathematics | All 330 payloads match exactly after HTML parsing |
| Display mathematics | All 24 payloads match exactly after HTML parsing |
| Plain prose typography | No `strong`, `b`, `em`, `i`, or heading elements in the article; no ATX headings in the source |
| Article structure | One article, 95 paragraph elements, 354 math-renderer elements, one image |
| Internal destinations | All 22 unique destination IDs present |
| Internal references | All 41 internal links have a unique corresponding GitHub-prefixed ID |
| Help organization | Hints P52–P58, H1–H6 in order; separate complete solutions P59–P72, S1–S6 in order, all after H6 |
| Image reference | One image, frozen-commit raw path, expected descriptive alt text, `max-width: 100%`; wrapper points to the same frozen image's blob page |

Every question has both a matching hint and solution link. Every hint has its matching return-to-question and solution links. Every solution has its matching return-to-question link. P72 also has the return-to-reading-route link. The exact per-link source paragraph, label, href and destination mapping are in `structural-check.json` and embedded in `preview-check.json`.

| Item | Question destination | Hint destination | Solution destination |
|---|---|---|---|
| 1 | q1 / P09 | h1 / P53 | s1 / P60 |
| 2 | q2 / P14 | h2 / P54 | s2 / P61 |
| 3 | q3 / P24 | h3 / P55 | s3 / P63 |
| 4 | q4 / P33 | h4 / P56 | s4 / P64 |
| 5 | q5 / P45 | h5 / P57 | s5 / P68 |
| 6 | q6 / P50 | h6 / P58 | s6 / P70 |

The delivered HTML uses fragment links such as `#q1` and sanitized IDs such as `user-content-q1`. The table and checks account for that GitHub prefix convention. They establish corresponding target markup, not observed JavaScript navigation or pixel position. The reading-route destinations are core/P03, theorem/P46, hints/P52 and solutions/P59. Conventional math italics are not classified as italic prose.

## Internal preview and complete visual inspection

The PDF skill was read from `/opt/codex/runtimes/codex-primary-runtime/plugins/openai-primary-runtime/plugins/pdf/skills/pdf/SKILL.md`. This PDF is an internal secondary-renderer QA preview; the requested product remains the frozen Markdown.

`prepare-preview.py` creates `preview.md` by changing protected inline `$`-backtick delimiters into ordinary dollar delimiters and fenced math into display-dollar blocks. All 330 inline and 24 display payloads are retained. The Pandoc AST confirms exact inline payloads and exact display payloads after removing the single wrapping newline added on each side by the delimiter conversion. Prose, links, anchors and image reference were retained in the converted Markdown. The existing header supplies only LaTeX-compatible `\gt` and `\lt` definitions.

Pandoc generated LaTeX at 11 pt with 25 mm margins; pdflatex compiled twice. The final preview has 11 US Letter pages. Each complete page was rendered with Poppler and visually opened, not just text-extracted or inspected as a contact sheet. Pages 2 and 8 encountered PNG viewer decode errors; they were re-rendered from the same final PDF as full-page 150 dpi JPEGs and successfully opened. Other full pages were opened at 120 dpi PNG. No teaching or figure changes were made.

| PDF page | Complete inspection scope | Display formula indices |
|---|---|---|
| 1 | P01–P08; route and initial definitions | 1 |
| 2 | P09–P16; Q1, Q2, sensitivity expressions | 2–3 |
| 3 | P16 display, P17–P23 beginning; piecewise and one-sided expressions | 4–6 |
| 4 | P23 continuation, P24–P29 beginning; Q3 and long reciprocal derivation | 7–8 |
| 5 | P29 continuation, P30–P36 beginning; Q4 and geometric setup | — |
| 6 | Complete unit-circle figure, P36 continuation, P37–P39 | 9–10 |
| 7 | P39 display, P40–P47; Q5 and all three limit prompts | 11–15 |
| 8 | P47 display, P48–P54; Q6, attribution, hints introduction, H1–H2 | 16–17 |
| 9 | P55–P64; H3–H6, solutions introduction, S1–S3 and S4 setup | 18–19 |
| 10 | P65–P71; remaining S4, S5 and S6 through the quotient | 20–24 |
| 11 | Complete P72; final solution continuation and return labels | — |

No clipping, overlapping text, missing glyphs, black boxes, raw/unrendered TeX, truncated expressions or unreadable figure labels were observed on any of the 11 complete pages. The long P25 derivation and P42 inline degree-angle expression fit. Fractions, radicals, cases, subscripts, superscripts, signs and limits were legible. All prompts and both complete support groups were visually inspected. Extracted PDF labels also confirm P01–P72 in order. The final LaTeX log has no overfull/underfull boxes, missing-glyph or other warning diagnostics.

## Concrete findings and limits

No product representation defect was found in the checked markup or supporting local visual evidence. The following are preview-specific differences, not asserted GitHub defects and not grounds for editing the frozen product:

- Pandoc promotes the image's alt text to a Figure 1 caption. GitHub keeps it as alt text.
- LaTeX floats the figure to page 6 between the two parts of P36; the frozen source and GitHub markup put the image immediately after P35.
- P16, P39 and P47 have their following displays across a PDF page boundary; P72 occupies the final page. These are local pagination effects.
- Hints and solutions retain their separate source groups but can share PDF pages. No separate-PDF-page help rule was imposed.

The PDF's font, equation renderer, fixed page size, floating behavior and pagination differ from GitHub. No PDF hyperlink parity is claimed; link destinations were checked in the actual GitHub markup. Browser installation was not retried, no CUA/browser session was initialized, and no live GitHub pixels or MathJax execution were observed. No subject research, fresh readers, pedagogy/SASIS work, GitHub writes, teaching edits, figure edits, repository edits or skill edits were performed.

Machine-readable result: `preview-check.json`. Supporting local artifacts remain within this review directory; no PDF is proposed as a requested deliverable.
