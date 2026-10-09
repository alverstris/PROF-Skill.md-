# Actual access log — SASIS D015-r21-v1

Provisional until root independently checks the tool record. This log records actual accesses, not merely requested access. Only the explicitly whitelisted subject files were opened as subject content. Renderer/runtime modules were used to render the supplied SVG inputs. No browsing, file search, linked-source access, skill reading, author-history access or other-agent messaging occurred. The original report is `report.md` in this same output directory. All written artifacts are within this output directory. Renderer failures were followed by a successful local Sharp SVG render and image inspection before dependent teaching resumed.

## Text delivery sequence

All text used Python `Path(...).read_bytes().decode().split('\n')`, preserving carriage returns, and printed every requested slot with its one-based number. The first baseline call verified its complete bytes/hash. The text was actually delivered in the following bounded outputs. No output reported truncation; every range's ending was present. Budgets were 14,000 tokens for baseline packets (actual 1,468–8,635) and 6,000–11,000 for teaching/help (actual 623–1,982). Tool wrapper metadata and actual output can be independently checked using the chunk IDs.

| Order | Input | Delivered LF slots inclusive | Tool chunk | Actual original token count |
|---|---|---|---|---:|
| 1 | student-baseline.txt | 1–150 | 8c4eec | 5462 |
| 2 | student-baseline.txt | 151–300 | 308f5a | 5478 |
| 3 | student-baseline.txt | 301–450 | 3e27d4 | 8144 |
| 4 | student-baseline.txt | 451–600 | 79b05e | 8378 |
| 5 | student-baseline.txt | 601–750 | 4c1957 | 8635 |
| 6 | student-baseline.txt | 751–900 | eb7a8e | 6660 |
| 7 | student-baseline.txt | 901–1050 | 5566b7 | 5981 |
| 8 | student-baseline.txt | 1051–1200 | 9c1114 | 5986 |
| 9 | student-baseline.txt | 1201–1350 | b2b346 | 7587 |
| 10 | student-baseline.txt | 1351–1378, including terminal blank | 9c9b6b | 1468 |
| 11 | teaching.md | 1–72, through figure-1 placement | 06343f | 1670 |
| 12 | figure 1 | See visual sequence/failures below; full PNG and successful rendered SVG viewed before slot 73 | c5c8d3, c87a8d | — |
| 13 | teaching.md | 73–142, through figure-2 placement | 1e3355 | 1326 |
| 14 | figure 2 | Both companions inspected before slot 143 | 3802dd, 145f1e | — |
| 15 | teaching.md | 143–203, through figure-3 placement | 3aa377 | 1099 |
| 16 | figure 3 | Both companions inspected before slot 204 | afd038, 8c76b9 | — |
| 17 | teaching.md | 204–247, including terminal blank | 95c06a | 1223 |
| 18 | hints.md | 1–39, including terminal blank | 93bcbd | 623 |
| 19 | solutions.md | 1–100, including terminal blank | 27784a | 1982 |

The `read_bytes()` call reads each whole text file into memory on each packet invocation, but the sequence of model-visible reading is the bounded slot sequence above. Claims about chronological understanding use only the slots already displayed, not undisplayed bytes in a Python variable. The complete baseline was displayed before the first teaching packet. No hint or solution was displayed before all teaching ended.

## Successful byte identity checks

Baseline path: `/workspace/scratch/6a5c7131498d/prof-r21/references/sasis/ocr-baseline-20261007/student-baseline.txt`.

Author bundle root: `/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/author/`.

| File | Actual bytes | Actual SHA256 | LF slots if text |
|---|---:|---|---:|
| student-baseline.txt | 247840 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 | 1378 |
| teaching.md | 20061 | 82a74376aa5d4bf1272ef2722b371178be81251110d05a81b68655f7ca7e6e4d | 247 |
| hints.md | 2269 | ac3a31d098d0b47b576f3aaa16f1abbb4649a88afbe145ef12b4c944a62e2e7b | 39 |
| solutions.md | 7461 | eecfdabddb8596e6decb9491599ed56786c9ddcac7dabe99773d672d46b0ce74 | 100 |
| assets/figure-1-gaussian.svg | 12851 | 700b875ac2ab3ed35373831f39dfdb0f82f852188e017aa3b7da584169dbf7ca | — |
| assets/figure-1-gaussian.png | 34418 | d821bc26eef0a897a2b044a970f94d55ea5da3a3c800d40d24c85e9e504817f4 | — |
| assets/figure-2-slopes.svg | 12066 | 9baea45d2f524cfd6231b26a4ed14c6f54c70719c974a6f546f39cac87c19c01 | — |
| assets/figure-2-slopes.png | 41654 | 435941035d0efb8a9553cf71b23d53555fdedb1bf930138ba8beadf363bb2927 | — |
| assets/figure-3-orthogonal.svg | 23751 | 9b5c6ccd6bd1d4b87ddcb7682408105842fe57c52b9df0b5a9d9ea4fde48f7b7 | — |
| assets/figure-3-orthogonal.png | 131540 | e02b23427fb69da88556d3c101e7da09dd44b9b7dd99ff49f9be729aaaf048e5 | — |

Every displayed identity matched the task's frozen identity. No input was modified.

## Full figure access at actual placements

### Figure 1, after T72 and before T73

1. First attempted Python/CairoSVG rendering; failed before reading the input because `cairosvg` was absent. Then attempted to view its nonexistent output, which also failed. Exact failures are preserved below.
2. Chunk c5c8d3: read/hash both full companion files. Printed the entire 12,851-byte SVG source without truncation (3,280 output tokens). This includes all geometry/labels, not just extracted text. The same call then invoked `view_image` on the supplied PNG; the complete image was displayed at 1120×608. I inspected the whole curve, axes, ticks and label layout.
3. Attempted primary-runtime Python/CairoSVG rendering; failed, followed by a missing-output image-view failure.
4. Attempted ImageMagick `convert` rendering and then `MSVG:` rendering; both failed (see unchanged messages).
5. Chunk c87a8d: Node runtime `sharp` consumed the full SVG and wrote `sasis-v1/figure-1-render.png`, reporting “Rendered with sharp”. `view_image` then displayed the full rendered SVG (504×274). All visual content was inspected; the rendering and supplied PNG agreed in substantive geometry and labels. No teaching after T72 had yet been displayed.

### Figure 2, after T142 and before T143

1. Chunk 3802dd read/hash both complete companions.
2. Chunk 145f1e: Sharp rendered the entire SVG to `sasis-v1/figure-2-render.png` and reported “Rendered full SVG”.
3. `view_image` displayed that complete rendering at 432×360, followed by the supplied PNG at 960×800. I inspected both whole images, including legend and common-point annotation. No rendering or viewing failure occurred. No teaching after T142 had yet been displayed.

### Figure 3, after T203 and before T204

1. Chunk afd038 read/hash both complete companions.
2. Chunk 8c76b9: Sharp rendered the entire SVG to `sasis-v1/figure-3-render.png` and reported “Rendered full SVG”.
3. `view_image` displayed that complete rendering at 504×374, followed by the supplied PNG at 1120×832. I inspected both whole images, including legend, all four dark curves, both teal closed curves, axes and endpoints. No rendering or viewing failure occurred. No teaching after T203 had yet been displayed.

SVG 2 and SVG 3 were not dumped as XML text. Their complete bytes were hashed and consumed by the successful renderer; their complete rendered visual information and supplied PNGs were actually displayed and inspected. This is not a claim that every XML character was separately read in a text display. No external SVG URL was fetched as a subject source.

## All failures, preserved verbatim

Failure 1 — chunk 8c44fa; default Python import, exit code 1:

```text
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ModuleNotFoundError: No module named 'cairosvg'
```

Following tool-level failure in the same functions call:

```text
unable to locate image at `/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/sasis-v1/figure-1-render.png`: No such file or directory (os error 2)
```

The subsequent supplied-PNG view in that call was never reached because the functions script stopped at the missing image. It was successfully performed in c5c8d3's call instead.

Failure 2 — chunk 6cc7b9; primary-runtime Python import, exit code 1:

```text
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ModuleNotFoundError: No module named 'cairosvg'
```

Following tool-level failure in the same functions call:

```text
unable to locate image at `/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/sasis-v1/figure-1-render.png`: No such file or directory (os error 2)
```

Failure 3 — chunk 00ed01; ImageMagick convert, exit code 1:

```text
6a5c7131498d: delegate failed `'rsvg-convert' -o '%o' '%i'' @ error/delegate.c/InvokeDelegate/1997.
6a5c7131498d: unable to open file `/tmp/magick-rvkO8b2DcXGVfAsDo2dSpwp7xKO3e248': No such file or directory @ error/constitute.c/ReadImage/620.
6a5c7131498d: no images defined `/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/sasis-v1/figure-1-render.png' @ error/convert.c/ConvertImageCommand/3234.
```

Failure 4 — chunk 888f9d; ImageMagick MSVG-prefix attempt, exit code 1:

```text
6a5c7131498d: unable to open image `MSVG:/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/author/assets/figure-1-gaussian.svg': No such file or directory @ error/blob.c/OpenBlob/2964.
6a5c7131498d: delegate failed `'rsvg-convert' -o '%o' '%i'' @ error/delegate.c/InvokeDelegate/1997.
6a5c7131498d: unable to open file `/tmp/magick-Mo7jwDpWeng9lU0t5FhvYHuyT5RgxOZz': No such file or directory @ error/constitute.c/ReadImage/620.
6a5c7131498d: no images defined `/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/sasis-v1/figure-1-render.png' @ error/convert.c/ConvertImageCommand/3234.
```

Following tool-level failure in the same functions call:

```text
unable to locate image at `/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/sasis-v1/figure-1-render.png`: No such file or directory (os error 2)
```

The ImageMagick errors mention its internally selected temporary paths; no successful artifact was produced there. I did not inspect those paths or use them as inputs. The only successful figure artifacts were written to the authorized SASIS output directory. The unavailable renderer failures were resolved with the already installed Node Sharp runtime; no packages were installed, files searched or network content retrieved.

No truncation failures, missing baseline packets, missing teaching/help sections, hash mismatches, or unresolved figure-view failures occurred. This sentence is a claim for root to verify against the actual tool record; it does not replace that independent verification.
