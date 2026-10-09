# Fresh reader access log — learner-v2

This log records actual subject-content access in this reader turn. Authorization was an instruction whitelist, not technical isolation. No browsing, external links, source PDFs, other reports, author prompts/evidence, history, directory searches, PROF files or other subject-content files were accessed. The two admitted input sets were the full four-subject baseline and the frozen learner-v2 packet. Executables and image-processing dependencies were used only to read/render the authorized constituents and write reader evidence.

## Text reading

Physical locators were obtained exclusively by `Path(...).read_bytes().decode().split('\n')`, without universal-newline conversion. Internal CR characters were preserved. Each numbered output below was actually displayed and read. Text bytes were loaded by the scripts, but only the named ranges were displayed to the reader; later learner prose was not displayed before the prescribed figures.

Baseline: `/workspace/scratch/6a5c7131498d/prof-r19/references/sasis/ocr-baseline-20261007/student-baseline.txt`.

Actual consecutive ranges: 1–100; 101–200; 201–300; 301–400; 401–500; 501–600; 601–700; 701–800; 801–900; 901–1000; 1001–1100; 1101–1200; 1201–1300; 1301–1378. Lines 1–1377 are content, 1378 is the terminal empty line. All four subjects were read anew, including cover, scope limits, data, examples, and final source-reference text. No chunk was truncated; no repair/reread was needed.

Learner root: `/workspace/scratch/6a5c7131498d/prof-r19/runs/y1-reader-20261008/iterations/013/current-r19/author/`.

Actual order after complete baseline:

1. `learner-v2.md` lines 1–31.
2. Read full actual bytes of PNG1 and SVG1, render SVG1, view full PNG1 then full SVG1-derived render.
3. Learner lines 32–61.
4. Read full actual bytes of PNG2 and SVG2, render SVG2, view full PNG2 then full SVG2-derived render.
5. Learner lines 62–103.
6. Read full actual bytes of PNG3 and SVG3, render SVG3, view full PNG3 then full SVG3-derived render.
7. Learner lines 104–165; 166–230; 231–280; 281–327.

Learner lines 1–326 are content, 327 is terminal empty. Hints, all solutions and final source/scope paragraph were read. No truncation, omitted range, repair or display-order departure occurred. Output caps exceeded each returned chunk's actual token count; tools did not report truncation.

## Identities actually computed

| Constituent | Bytes | SHA256 |
|---|---:|---|
| student-baseline.txt | 247840 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 |
| learner-v2.md | 31740 | d17f77d36f7c30db9777230a85decb363a1fb967bb5c51d60cb5af4cd7b078c0 |
| figures/figure-1-parallel-lines.png | 103842 | 802174ba2825a78c2aaeb1e3bb80193398668f9bf8af1fa8185de9c0afe1af1f |
| figures/figure-1-parallel-lines.svg | 32487 | ccd6a2a89eee4be03ea8d1557281bb89fc00801f57dbccd750ca83bb199823fc |
| figures/figure-2-corner.png | 89721 | ffcb7418488dcdb45c9e1eab91ac7a554a578e061a9fc9f6653c889e2432712f |
| figures/figure-2-corner.svg | 34736 | 964b2f582dc78a16248bffb1f947aad61ef082c63f7dfaaf1d3c1ebfc357b162 |
| figures/figure-3-tangent-error.png | 69395 | ffbd570eb22b77c6016f65841db03776dfab02967b6b197cb79ce4245c54a8f1 |
| figures/figure-3-tangent-error.svg | 31838 | 28d2d7ccfbbb0e015bbab0bd06da8a605856ca5f12d3c5b943654f40baa69bba |

All match the supplied frozen identities. Hash agreement was admission checking, not substituted for reading.

## Figure rendering and actual views

Each SVG's complete bytes were read, hashed, decoded, and passed as its authorized file to installed `/usr/bin/inkscape` with `--export-type=png --export-filename=<reader evidence path>`. All three commands exited 0. Each reported a GtkRecentManager initialization warning; none reported a failed export. Derived renders are `figure-1-svg-render.png`, `figure-2-svg-render.png`, and `figure-3-svg-render.png` in this evidence directory.

For each figure, `view_image` displayed the full original PNG (1292 × 765) and the full derived SVG render (730 × 432). No crops were used. The SVG root has dimensions 547.2 pt × 324 pt with viewBox `0 0 547.2 324`; Inkscape's default raster output supplied the smaller frame. All labels, plotted lines, point markers, arrows and legends were visually inspected in both representations. They are readable at the displayed full frames. No substantive visible discrepancy was identified between each PNG and SVG-derived view. This is a visual inspection at those resolutions, not pixel identity, source-editable accessibility testing, or a guarantee about every possible renderer.

Original figure paths were exactly the three PNG and SVG paths in the table. Derived renders represent the same authorized SVG constituents, not third subject sources. PIL metadata inspection afterward read dimensions only from these authorized PNGs and own derived renders.
