D001 frozen-v4 render recheck

The complete actual GitHub markup comparison passes: all 288 mathematical payloads are preserved exactly after ordinary HTML parsing. The two changed mathematical forms also pass local visual inspection. GitHub's live rendered pixels remain unobserved. Earlier v2 and v3 reports and evidence are unchanged.

Artifact identity

- Commit: 0716ea92991d7f9fe2814e137bcc830d91a27511.
- File: runs/y1-reader-20261008/iterations/001/teaching-v4.md.
- Canonical URL: https://github.com/alverstris/PROF-Skill.md-/blob/0716ea92991d7f9fe2814e137bcc830d91a27511/runs/y1-reader-20261008/iterations/001/teaching-v4.md.
- Verified source SHA256: 402485baa2767af9625146721e356f92bad76e4cfb738e5729c6c8b94ea79401.
- Verified source size: 24,315 bytes and 24,281 Unicode characters.
- Canonical HTTP response: 200; 402,122 bytes.
- Retrieved GitHub HTML SHA256: e17ed975ea3afa2036f7cf048249e7d5faaf76e5ed7db34991b7da7cf53191be.

Full GitHub markup verification

The immutable canonical page was retrieved through public HTTP without a signed-in browser or personal-computer session. All source expressions were compared in order against the actual delivered article's math-renderer contents. The comparison removes only the renderer's dollar delimiters and performs ordinary HTML parsing. It does not apply an additional entity-decoding pass, infer client normalization, or normalize payload whitespace.

| Check | Result |
|---|---|
| Source inline expressions | 249 |
| GitHub inline math-renderer elements | 249 |
| Exact inline payload equality | 249 of 249 |
| Source display expressions | 39 |
| GitHub display math-renderer elements | 39 |
| Exact display payload equality | 39 of 39 |
| Residual payload differences | 0 |
| Paragraph labels retained in order | P01–P42 |

P07's two aligned row separators retain exactly two backslashes, followed by the intended space and alignment marker. P26's comparison retains exactly t\gt0. Thin-space commands, alignment ampersands, all other operators, units and complete mathematical expressions are preserved. All 39 display equations receive block renderer elements, and all 249 inline equations receive inline renderer elements.

The original v2 display-recognition and comma-substitution defects are resolved, and the two v3 serialization differences are eliminated in the delivered v4 markup. The full audit records every source payload, every parsed GitHub payload and its exact equality result.

Source equivalence and visual scope

An independent inverse transformation replaces only the new \gt spelling with the previous greater-than character and restores the two P07 source newlines after their row separators. The result equals v3 byte-for-byte, with SHA256 494a7508d8b7fbe56f3ce3c9a6fbe1bf2261ecdbfca0a80e81c8997d46dc6d13. The prior v3 review separately established an exact inverse to frozen v2. No prose, task, hint, solution or unrelated mathematical payload changed.

For a fresh local visual check, v4's GitHub delimiters were converted into Pandoc-compatible dollar delimiters without changing the mathematical payloads. Pandoc and pdflatex produced an eight-page preview using the same 11-point text and 25 mm margins as the original preview. A local LaTeX header provides \gt as greater-than where needed; this is a preview compatibility definition, not evidence of GitHub client execution.

Poppler rendered preview pages 2 and 6 at 1237 × 1600 pixels. Both complete page images were inspected:

- Page 2, including P07: the three rows of the reciprocal simplification align correctly, with intact fractions, minus signs and spacing. No row is lost or merged, and there is no clipping or unrendered TeX.
- Page 6, including the changed P26 continuation: the comparison visibly reads t > 0 with the correct greater-than symbol and normal inline spacing. The surrounding equations and prose remain legible.

Both rendered PNGs are pixel-identical to the corresponding pages in the previously inspected v2 preview. That earlier full inspection covered all eight complete pages, P01–P42, all equations, all attempts, the hint group, the complete solutions and source/licence material. Unchanged content retains that earlier preview evidence; this recheck directly inspected the two changed forms. The new preview PDF SHA256 is 62aa9ea95c941630f8da512bcabb08857a94f636b03ecbceb17d534dd8fc51d9.

Tasks, hints and complete solutions remain separate in both source order and GitHub article markup: attempts at P09/P22/P29/P31, hints at P32–P35, the solution introduction at P36, and complete solutions at P37–P40. The preview still places Attempt A on page 2, B on page 5, C/D and Hint A on page 6, remaining hints and Solutions A–C on page 7, and Solution D across pages 7–8. No answer has moved next to its corresponding main-lesson attempt.

Disposition and limits

Pass for complete GitHub markup integrity and local mathematical-preview legibility within the stated inspection scope. No consequential defect remains in those checked representations. This is not a certification of live GitHub visual appearance: no browser rendered this page, and client MathJax execution, responsive layout and GitHub-specific pixel appearance remain unobserved. No further browser installation was attempted. No teaching file or GitHub content was edited during this review.

Evidence

- github-page.html and github-article.html: canonical HTTP response and extracted article.
- markup-audit.json and markup-audit.log: all 288 ordered payload checks, all exact.
- check_markup.py: reproducible payload audit.
- inverse-check.json: exact v4-to-v3 inversion result.
- preview-source.md and preview-header.tex: transparent local-preview compatibility inputs.
- preview.pdf, page-2.png and page-6.png: new preview and inspected changed-form pages.
- preview-check.json: PDF identity and pixel-equality results.
- pandoc.log: empty successful conversion diagnostic log.
- ../report.md and ../v3/report-v3.md: preserved earlier findings and scope.
