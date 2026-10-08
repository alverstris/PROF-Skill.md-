D001 frozen-artifact render review

Reviewed on 2026-10-08. No teaching content was edited, no GitHub write was performed, and no SASIS or learner evaluation was performed.

Artifact identity

- Repository commit: 3bdad7a365b5ce56e7430702d6daf3d963a11de3.
- File: runs/y1-reader-20261008/iterations/001/teaching-v2.md.
- Canonical URL: https://github.com/alverstris/PROF-Skill.md-/blob/3bdad7a365b5ce56e7430702d6daf3d963a11de3/runs/y1-reader-20261008/iterations/001/teaching-v2.md.
- Frozen source SHA256: 5a892606c9064d56bb6dea693ed5b3dfbb823608da9a4b1926c408aed00aca5b. The local source matched this hash before review.
- Fetched canonical GitHub HTML SHA256: 58a7177200162e50db4b71be66c2fac1013ab1834038fbcc32ddd5a487cabc84.

Render route and limits

The canonical immutable GitHub page was retrieved by public HTTP with status 200 (373,962 bytes), without a signed-in browser or personal-computer session. Its actual delivered article HTML was extracted and checked. Cloud Playwright was installed but had no browser binary. One browser installation attempt returned a non-ZIP payload and was stopped; no browser subsequently rendered the page. Consequently, GitHub's live visual appearance, responsive layout, MathJax execution and client-side recovery behavior were not observed.

A local preview was generated from the unchanged source using Pandoc's markdown+tex_math_dollars reader, pdflatex, 11-point text and 25 mm margins. The eight-page PDF was rasterized with Poppler to eight 1237 × 1600 PNGs. All eight complete images were visually inspected, covering every paragraph P01–P42, all equations, attempts A–D, hints A–D, complete solutions A–D, and source/licence material. This was a local typeset preview, not a reproduction or verification of GitHub's appearance. PDF SHA256: 440e24d9b8301bc054963bc5a53b316d31ea0b5fc530c2b9e8c6f4010501deb5.

Findings

1. Consequential GitHub markup defect: all 39 source display-math blocks remain literal $$-delimited text inside paragraph HTML. There are zero display-math renderer elements. In contrast, all 249 inline expressions are placed in math-renderer elements. The source's display delimiters have no blank paragraph separation; GitHub's delivered markup does not recognize them as display math. This is an observed conversion defect, even though its final client-rendered pixels remain unobserved. A successful Pandoc preview does not discharge it.

2. Nine of those 39 display blocks also lose TeX escapes during Markdown processing. In P07, the two aligned row terminators become single backslashes. In several equations, thin-space commands become literal commas. The affected ordered display-block indices are 5, 10, 26, 27, 28, 30, 31, 35 and 39. Exact before/after strings are recorded in markup-audit.json.

3. Six inline renderer inputs also lose thin-space commands and acquire literal comma semantics: P23's acceleration, P28's two unit equalities, and P39's three rates. Blank lines around display math will not address these inline cases. The source's \,-commands should be protected from Markdown or expressed with an equivalent command that survives this renderer. One additional inline expression, P26's t>0, is represented with an extra entity-encoding level in fetched HTML. Whether that last representation is correctly decoded by GitHub's client was not established and is not classified here as a confirmed visual defect.

4. The local PDF preview displays all mathematical notation legibly, including P07's aligned fractions, P17–P20's binomial/summation argument, units, one-sided impact notation and solution equations. No clipping, overlaps, missing glyphs, literal dollar delimiters or unrendered TeX was seen on the eight pages. Some paragraphs continue across ordinary page boundaries; no equation is clipped. These observations apply only to the preview.

5. Tasks, hints and solutions remain separate in both source order and delivered GitHub markup: attempts A–C occur at P09/P22/P29; later attempt D is P31; the hint group is P32–P35; the solutions introduction is P36 and complete solutions are P37–P40. In the preview, Attempt A is on page 2, B on page 5, C/D and Hint A on page 6, remaining hints and Solutions A–C on page 7, and Solution D spans pages 7–8. Their labels are readable and no complete solution has been inserted beside its corresponding main-lesson task. The hints and solutions are not hidden or protected from incidental viewing.

6. The title, transitions, attempts, hints and solutions use the same ordinary paragraph treatment. GitHub's article has no heading tags or details elements. This leaves a dense continuous reading surface, but paragraph labels and the opening route remain available. It is a hierarchy limitation rather than evidence of mathematical illegibility.

Disposition

Do not certify this frozen artifact as having passed GitHub final-format QA. The local preview passes a legibility inspection, while the GitHub-delivered markup has a consequential display-math conversion defect and six altered inline spacing commands. A corrected candidate requires a new immutable identity and a fresh GitHub markup check; actual GitHub visual inspection remains outstanding unless a working browser becomes available.

Evidence

- github-page.html: complete unmodified HTTP response.
- github-article.html and github-article-text.txt: extracted article and decoded text.
- markup-audit.json and markup-audit.log: full 39-display/249-inline ordered audit and before/after strings.
- check_markup.py: reproducible markup audit.
- preview.pdf and page-1.png through page-8.png: local preview and all visually inspected pages.
- pandoc.log: empty successful conversion diagnostic log.
- render.cjs: attempted cloud Playwright route; it stopped at launch because the browser executable was absent.
