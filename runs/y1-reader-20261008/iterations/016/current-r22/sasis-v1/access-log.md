# SASIS access log: D016-r22-learner-v1

Admission remains provisional until root validation. These are actual accesses in order, not a proposed protocol. Subject retrieval was read-only and confined by instruction to exactly the two supplied content inputs. Technically available tools were not erased or isolated. The entire baseline was read in bounded chunks before substantive document access; this does not claim all input bytes were simultaneously in context.

## Input 1 verification and complete read

Path: `/workspace/scratch/6a5c7131498d/prof-r22/references/sasis/ocr-baseline-20261007/student-baseline.txt`.

The first shell/Python call used `read_bytes()`, SHA-256, UTF-8 `decode()`, and `split('\n')`. It returned 247840 bytes, SHA-256 `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`, and 1378 LF slots including the terminal empty slot. All match the supplied specification. No carriage-return normalization or `splitlines()` was used. Numbered line output retained the original CR characters in the strings printed.

Each subsequent range also used `read_bytes().decode().split('\n')`. Ranges below are one-based, inclusive, and were displayed and read in this exact order:

| Access | LF slots | Result |
|---|---:|---|
| 1 | 1–80 | Hash/size/slot verification plus complete displayed range |
| 2 | 81–240 | Complete displayed range |
| 3 | 241–390 | Complete displayed range |
| 4 | 391–510 | Complete displayed range |
| 5 | 511–650 | Complete displayed range |
| 6 | 651–790 | Complete displayed range |
| 7 | 791–900 | Complete displayed range |
| 8 | 901–1010 | Complete displayed range |
| 9 | 1011–1130 | Complete displayed range |
| 10 | 1131–1260 | Complete displayed range |
| 11 | 1261–1378 | Complete displayed range, including terminal empty slot |

Thus Mathematics, Further Mathematics, Physics, and Chemistry were all read; selection was not restricted to presumed relevant mathematics passages. No range gap, truncation banner, clipped endpoint, or failed read was observed. No repair access was required.

## Input 2 verification

Authorized bundle root: `/workspace/scratch/6a5c7131498d/prof-r22/runs/y1-reader-20261008/iterations/016/current-r22/author/`.

After completing baseline access 11, one Python call read only the following seven authorized constituent byte streams for size/hash verification. It printed no hint/solution content at that stage, and printed teaching only through LF slot 15.

| Constituent | Actual bytes | Actual SHA-256 | Match |
|---|---:|---|---|
| teaching.md | 19302 | e670d8dadbb2da53c9df5dc067b5f3ce8028e435b13b6c7330539616034df95c | Yes |
| hints.md | 2183 | f375210f21b8450d7744baa6506835de093421453eb92fde0295ba61c40f3500 | Yes |
| solutions.md | 5775 | 49cda647d4af3d4c5d4a2eb6aeb06393064756b4ded29c3e1c45b6f9a4965b69 | Yes |
| figures/rectangles.png | 55545 | eea99850c7167b44af89914d0c03c6bfe593e30118fdc3f37f5915c1ce0199eb | Yes |
| figures/pyramids.png | 56323 | 1f173f787e408a772f948c80192f86eea7ecb5899362ac33e2e1a75d1b38a8c5 | Yes |
| figures/endpoint.png | 48823 | 5bbfc6671e68c3c67d905ed31590030c172594da2cd114c52cf86819b840daf5 | Yes |
| figures/tag.png | 31479 | 866c570ba5a66275f445b4eb3b55281b6e6908b0d4e1e0ff930f2ffb0c27485d | Yes |

## Actual sequential substantive document access

Text was numbered using the same byte/decode/LF split approach. Teaching has 235 LF slots, hints 32, and solutions 113, each including its terminal empty slot.

| Order after baseline | Access | Result |
|---|---|---|
| 1 | Verify seven constituents; teaching.md LF 1–15 | Complete displayed range; stopped at first image placement |
| 2 | view_image figures/rectangles.png | Successfully displayed and inspected before any teaching beyond 15 |
| 3 | teaching.md LF 16–34 | Complete displayed range; stopped at second image placement |
| 4 | view_image figures/pyramids.png | Successfully displayed and inspected before any teaching beyond 34 |
| 5 | teaching.md LF 35–98 | Complete displayed range; stopped at third image placement |
| 6 | view_image figures/endpoint.png | Successfully displayed and inspected before any teaching beyond 98 |
| 7 | teaching.md LF 99–122 | Complete displayed range; stopped at fourth image placement |
| 8 | view_image figures/tag.png | Successfully displayed and inspected before any teaching beyond 122 |
| 9 | teaching.md LF 123–235 | Complete remaining teaching displayed and read |
| 10 | hints.md LF 1–32 | Complete hints displayed and read after teaching |
| 11 | solutions.md LF 1–113 | Complete solutions displayed and read after hints |
| 12 | view_image figures/endpoint.png, detail original | Successful repeat inspection of the same authorized image to resolve possible shading ambiguity; no image discrepancy retained |

The initial image views used view_image's default detail. Image data was forwarded to the visual tool output using `image(r.image_url)`. All four images visibly rendered; none failed or required clipping repair. All textual output ranges reached their requested terminal line; no tool-reported truncation was observed. Verification reads of entire constituent byte streams are distinguished above from their later substantive sequential displays.

## Boundaries and output actions

No other subject-content file, author file, prior report, personal context, skill, source PDF, website, external source, or other agent was consulted. Links inside the inputs were read as text but not opened. No assessment/problem battery was substituted for reading. No subject input was mutated.

After all authorized reading, a single `mkdir -p` created the requested `sasis-v1` directory, followed by creation of only this original access-log.md and original report.md in that directory. These files are the reader's outputs, not additional subject-content inputs. No library upload or other artifact destination was used because the task explicitly fixed the output directory.
