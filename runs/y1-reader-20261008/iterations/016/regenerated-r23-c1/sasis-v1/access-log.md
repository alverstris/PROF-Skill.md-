# SASIS access log — original, before feedback

Frozen revision: d016-r23-c1-learner-v1. This log records actual accesses, not a proposed plan. Final admission remains provisional for root validation.

## Authorized inputs and integrity results

Baseline path: `/workspace/scratch/6a5c7131498d/prof-r22/references/sasis/ocr-baseline-20261007/student-baseline.txt`

Learner prefix: `/workspace/scratch/6a5c7131498d/prof-r22/runs/y1-reader-20261008/iterations/016/regenerated-r23-c1/author/learner/`

| Input | Actual bytes | Actual SHA256 | Result |
|---|---:|---|---|
| Baseline | 247840 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 | Matches supplied |
| notes.md | 24742 | ed58e55175508f36f831dd4340e46f87a62bfb1e0256ffb62f12e3adae4db40f | Matches supplied |
| hints.md | 2903 | 1ce9784fb886d58811990954c0a934b91236d7cfadd00a42294b307b9097f3f2 | Matches supplied |
| solutions.md | 9005 | 00b4bebca64c3ff16de23b2456e5769906a0e74b22683be497e82915410fe65e | Matches supplied |
| figures/rectangles.png | 68208 | 91e367332338640bce2532f89d0b327f7d4404aec075e53cebae3bc380d62112 | Matches supplied |
| figures/staircase.png | 72621 | d9a04631c172d3f649600a3331aca41d08bc2e2c372d05c38b6cff72b3b4565d | Matches supplied |
| figures/sample-rectangle.png | 35502 | d029db7107364ecc5736fb618331c3df740374b598d9c75b021a1658e0a5d4a9 | Matches supplied |

All text accesses used `Path(exact_authorized_path).read_bytes().decode().split('\n')`. Internal CR characters were not stripped or used as line separators. Baseline has 1378 LF slots: 1377 content lines plus the terminal empty slot. Notes has 309 slots (308 content), hints 52 (51 content), solutions 187 (186 content). SHA256 was computed on the original bytes.

## Sequential actual retrievals and results

Each shell read used only the exact authorized input path(s), and every listed shell read exited 0. Tool output carried every requested numbered line; no tool output was truncated. Each image was actually displayed and inspected before subsequent teaching was retrieved.

| Order | Tool/output identifier | Actual access | Result |
|---:|---|---|---|
| 1 | exec_command chunk aa2f04 | Baseline whole-byte integrity check; display B1–100 | Hash/size match; complete range |
| 2 | chunk e490a0 | Display B101–240 | Complete range |
| 3 | chunk c77711 | Display B241–400 | Complete range; Mathematics into Further Mathematics |
| 4 | chunk fff5bd | Display B401–530 | Complete range; Further Mathematics into Physics |
| 5 | chunk 3a588a | Display B531–670 | Complete range |
| 6 | chunk 8c9c0d | Display B671–820 | Complete range; Physics into Chemistry |
| 7 | chunk 87c033 | Display B821–970 | Complete range |
| 8 | chunk b46477 | Display B971–1110 | Complete range |
| 9 | chunk 058de2 | Display B1111–1250 | Complete range |
| 10 | chunk 7aac28 | Display B1251–1378 | Complete range, including terminal empty slot; full baseline reading finished |
| 11 | chunk 4953a4 | Whole-byte checks of the six exact document constituents; display N1–36 only | All six hash/size matches; notes stopped at Figure 1 insertion and caption |
| 12 | view_image via functions.exec | figures/rectangles.png | Actual image displayed; two panels, region and four right rectangles inspected before N37 |
| 13 | chunk 8fb780 | Display N37–68 | Complete range; stopped at Figure 2 insertion and caption |
| 14 | view_image via functions.exec | figures/staircase.png | Actual image displayed; top footprints, four-layer side section, both pyramids and z=1.5 cut inspected before N69 |
| 15 | chunk 290215 | Display N69–127 | Complete range; stopped at Figure 3 insertion and caption |
| 16 | view_image via functions.exec | figures/sample-rectangle.png | Actual image displayed; sample location, full width and graph-height correspondence inspected before N128 |
| 17 | chunk dbd1fb | Display N128–218 | Complete range |
| 18 | chunk f16f10 | Display N219–309 | Complete range including terminal empty slot; notes reading finished |
| 19 | chunk bae2a9 | Display H1–52 | All hints and terminal empty slot read after notes |
| 20 | chunk 78b090 | Display S1–100 | Complete range, after all hints |
| 21 | chunk 5b13be | Display S101–187 | Complete range and terminal empty slot; solutions reading finished |

The integrity operation in order 11 loaded all six constituents' bytes for hashing; it did not print later teaching text. Substantive textual reading stayed at the requested figure boundaries, with captions included and no intervening teaching read before the corresponding view. The image files were hashed and later viewed, not substituted by their hashes or alt text.

## Failures, clipping and coverage

- Missing/mismatched/unreadable inputs: none.
- Clipped ranges: none. No clipping repairs were needed.
- Failed tool accesses: none.
- Baseline coverage: every content line B1–1377, all four subjects, plus empty terminal slot, before any document teaching.
- Document coverage: every content line N1–308, H1–51, S1–186, their terminal slots, and all three actual images. Captions N36, N68 and N127 were read with their insertions; views occurred before later teaching.
- No directory listing, file search, manifest, author evidence, raw lecture, linked webpage, network lookup, previous report, personal context, PROF skill or other-agent subject-content retrieval was performed.
- Two progress messages were sent only to root. No other agent was contacted and none was spawned.
- Output writes: created only the permitted `sasis-v1` output directory and wrote original `report.md` and `access-log.md`. No input was edited. No temporary script file or other artifact was written.

This is an instruction whitelist record, not a claim of technical isolation. The report contains concise reconstruction evidence and limits rather than a private deliberation transcript.
