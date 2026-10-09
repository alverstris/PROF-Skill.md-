# SASIS D015-r21-v2 access log

Original log; report provisional pending root verification of complete actual input access.

## Instruction boundary

Exactly two subject-content inputs were used: the complete frozen baseline and the specified nine-constituent teaching bundle. Retrieval confinement was instruction-based; shared tools remained technically available. This log does not claim erased pretraining or technical isolation. No browsing, source-link following, other-file search, skill read, personal-context retrieval, author-history read, previous-report read, or other-agent contact occurred. Tools were used for exact input reads/hash checks, local rendering/viewing and writing this reader's own outputs. File references inside the baseline and teaching were read as text, not followed.

All text reads used Python `Path(...).read_bytes().decode().split('\n')`, then printed every requested slot with its 1-based prefix. Internal CRs in the baseline were preserved. Byte checks used SHA-256 of the raw bytes. No output returned a truncation indicator or omitted requested slots. No recovery read was needed.

## Input identity checks

Baseline exact path:
`/workspace/scratch/6a5c7131498d/prof-r21/references/sasis/ocr-baseline-20261007/student-baseline.txt`

- Actual bytes: 247840.
- Actual SHA-256: `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`.
- Actual LF slots: 1378, including final empty slot.
- Matches supplied frozen identity.

Teaching bundle root:
`/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/author/v2/`

| Constituent | Actual bytes | Actual SHA-256 | LF slots for text |
|---|---:|---|---:|
| teaching.md | 20163 | 9ff76d7dde73d2270b511421f428e5e3324176bc1666728ea013ec8f0512c4b4 | 247 |
| hints.md | 2272 | 19bf8adb1b6c71a3fdfa65588612e90e8c2431917807c78d7db3ab952fa4f1b5 | 39 |
| solutions.md | 7453 | 9f6a2b4117df5902a1d964de411830e6af4e61862d6ef80d5cc38991be766855 | 100 |
| assets/figure-1-gaussian.svg | 12851 | 700b875ac2ab3ed35373831f39dfdb0f82f852188e017aa3b7da584169dbf7ca | — |
| assets/figure-1-gaussian.png | 34418 | d821bc26eef0a897a2b044a970f94d55ea5da3a3c800d40d24c85e9e504817f4 | — |
| assets/figure-2-slopes.svg | 12066 | 9baea45d2f524cfd6231b26a4ed14c6f54c70719c974a6f546f39cac87c19c01 | — |
| assets/figure-2-slopes.png | 41654 | 435941035d0efb8a9553cf71b23d53555fdedb1bf930138ba8beadf363bb2927 | — |
| assets/figure-3-orthogonal.svg | 23751 | 9b5c6ccd6bd1d4b87ddcb7682408105842fe57c52b9df0b5a9d9ea4fde48f7b7 | — |
| assets/figure-3-orthogonal.png | 131540 | e02b23427fb69da88556d3c101e7da09dd44b9b7dd99ff49f9be729aaaf048e5 | — |

All actual constituent identities match the supplied frozen identities. Image hashes read all bytes but were not treated as substitutes for image inspection.

## Actual chronological access

Tool result chunk IDs identify textual executor outputs where available. Image viewing results are recorded by exact path and placement below.

| Order | Read/view | Result and completeness |
|---:|---|---|
| 1 | Baseline B1–150; raw-byte identity and LF-slot count | chunk `beb9a0`; 5565 output tokens; all 150 requested slots visible |
| 2 | Baseline B151–300 | chunk `72d665`; 5553 tokens; complete |
| 3 | Baseline B301–450 | chunk `5b2ace`; 8219 tokens; complete |
| 4 | Baseline B451–600 | chunk `eddb7d`; 8453 tokens; complete |
| 5 | Baseline B601–750 | chunk `d483eb`; 8710 tokens; complete |
| 6 | Baseline B751–900 | chunk `a00e03`; 6735 tokens; complete |
| 7 | Baseline B901–1050 | chunk `ec5450`; 6043 tokens; complete |
| 8 | Baseline B1051–1200 | chunk `10579b`; 6024 tokens; complete |
| 9 | Baseline B1201–1378 | chunk `e0ce31`; 9098 tokens; complete through final empty slot |
| 10 | Teaching T1–72; raw-byte identity and LF-slot count | chunk `24bdde`; 1714 tokens; complete |
| 11 | Figure 1 PNG/SVG raw-byte identities | chunk `6c534c`; matches frozen identities |
| 12 | Full supplied `assets/figure-1-gaussian.png` via view_image | whole figure viewed after T72, before T73 |
| 13 | Render supplied `assets/figure-1-gaussian.svg` using Node Sharp | chunk `145b94`; successful full PNG output 504×274, 14227 bytes |
| 14 | Full `sasis-v2/figure-1-svg-render.png` via view_image | whole SVG rendering viewed after T72, before T73 |
| 15 | Teaching T73–142 | chunk `90a306`; 1352 tokens; complete |
| 16 | Figure 2 PNG/SVG identities and SVG render | chunk `65ad08`; identities match; rendering successful, 432×360, 15724 bytes |
| 17 | Full supplied `assets/figure-2-slopes.png` via view_image | whole figure viewed after T142, before T143 |
| 18 | Full `sasis-v2/figure-2-svg-render.png` via view_image | whole SVG rendering viewed after T142, before T143 |
| 19 | Teaching T143–203 | chunk `3c925d`; 1118 tokens; complete |
| 20 | Figure 3 PNG/SVG identities and SVG render | chunk `efcccf`; identities match; rendering successful, 504×374, 36837 bytes |
| 21 | Full supplied `assets/figure-3-orthogonal.png` via view_image | whole figure viewed after T203, before T204 |
| 22 | Full `sasis-v2/figure-3-svg-render.png` via view_image | whole SVG rendering viewed after T203, before T204 |
| 23 | Teaching T204–247 | chunk `64a428`; 1253 tokens; complete through final empty slot |
| 24 | Hints H1–39; raw-byte identity and LF-slot count | chunk `f4737b`; 651 tokens; complete through final empty slot |
| 25 | Solutions S1–100; raw-byte identity and LF-slot count | chunk `28f3b7`; 2038 tokens; complete through final empty slot |
| 26 | Write original report.md in own output directory | chunk `eaefc4`; completed successfully |
| 27 | Write this original access-log.md in own output directory | current write; no subject-content read |

This ordering covers every baseline content slot before any teaching read, every teaching slot in order, all figures at their placements, and complete hints followed by complete solutions. There were no skipped or sampled portions.

## Figure rendering and inspection details

Only supplied SVGs were rendered, using the installed runtime Node and Sharp:
`require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES + '/sharp')`.
The render call for each was `sharp(exact_supplied_svg_path).png().toFile(exact_own_output_path)`; no crop, extraction or replacement artwork was applied. The files were viewed in full with `view_image` and emitted as images. Source SVG XML was not separately printed: complete rendering and viewing was the specified content-access route.

- Figure 1: full axes, -6 to 6 horizontal range, positive symmetric peak at (0,1), and tails inspected in the supplied PNG and SVG rendering. Rendering succeeded on the first call. No truncated plot or hidden consequential annotation observed.
- Figure 2: complete legend, three equations/styles, axes, chosen point and tangent/ray relationship inspected in both. Rendering succeeded on the first call. All consequential labels readable.
- Figure 3: complete legend, four parabola branches, two closed ellipses, coordinate ticks, intersections and axis points inspected in both. Rendering succeeded on the first call. All consequential labels readable.

No renderer failure, image-view failure or output truncation occurred. No repair or recovery was necessary. Derived renders were written only to the permitted own output directory.

## Preserved outputs

Output root:
`/workspace/scratch/6a5c7131498d/prof-r21/runs/y1-reader-20261008/iterations/015/current-r21/sasis-v2/`

- `report.md` — original chronological witness report, not subsequently revised in response to author feedback.
- `access-log.md` — this original access log.
- `figure-1-svg-render.png`, `figure-2-svg-render.png`, `figure-3-svg-render.png` — faithful derived full SVG renderings used for actual access.

The access claim and report remain provisional pending the requested root audit. Content evaluation is instruction-confined, not evidence of a real student's learning or a guarantee of exhaustive error detection.
