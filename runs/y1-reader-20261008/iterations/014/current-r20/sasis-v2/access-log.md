# Actual input-access log

## Mechanism and boundaries

Only the two exact subject-content files named in the task were retrieved. Each bounded packet used Python `Path(exact_path).read_bytes().decode().split('\n')` and printed sequential physical-LF line labels without replacing internal CR. No directory listings, other subject files, browser, skills, history, reports, research or source links were accessed. The output directory was created solely for this report and this log. Input files were not modified.

The line count includes the trailing empty string after a final LF. Hashes were calculated from the original bytes.

## Baseline

Path: `/workspace/scratch/6a5c7131498d/prof-r20/references/sasis/ocr-baseline-20261007/student-baseline.txt`

Bytes: 247840

SHA256: `3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5`

Physical-LF entries: 1378

Actual chronological packet accesses:

1. B1–B300 requested with byte count/hash/line count. The tool result was JSON-wrapped and the outer functions output was truncated (reported original token count 11612; visible omission included material around B124–B178). This first packet alone was not accepted as full coverage.
2. B1–B150 reread, raw command output returned; complete, no truncation warning.
3. B151–B300 reread, raw command output returned; complete, no truncation warning. Steps 2–3 fully repair the initial packet, including all potentially omitted material.
4. B301–B450; complete, no truncation warning.
5. B451–B570; complete, no truncation warning.
6. B571–B720; complete, no truncation warning.
7. B721–B870; complete, no truncation warning.
8. B871–B1000; complete, no truncation warning.
9. B1001–B1140; complete, no truncation warning.
10. B1141–B1260; complete, no truncation warning.
11. B1261–B1378; complete, no truncation warning.

All reads exited successfully. Full baseline coverage completed before first teaching read. Section spans: cover B1–B15; Mathematics B16–B344; Further Mathematics B345–B504; Physics B505–B789; Chemistry B790–B1378. Section-boundary blank lines are included.

## Teaching

Path: `/workspace/scratch/6a5c7131498d/prof-r20/runs/y1-reader-20261008/iterations/014/current-r20/author/teaching-v2.md`

Bytes: 24606

SHA256: `caf74a9a150f61d2531e8b2768abb1448fb7d5304818a9e1fcc73d02bead826b`

Physical-LF entries: 414

Actual chronological packet accesses, all after the baseline:

1. T1–T150 plus byte count/hash/line count; complete, no truncation warning.
2. T151–T290; complete, no truncation warning.
3. T291–T414; complete, no truncation warning.

All reads exited successfully. These cover the complete one-constituent teaching document in order, including all tasks, hints, complete solutions, source note and ending. No missing companion was assumed.

## Remaining limits

No unread subject-input range remains. The initial display truncation is repaired as recorded. No external source contents were retrieved; source-fidelity/pagination assertions are not verified. This is instruction-confined input use, not a claim of technical isolation or erased background knowledge.
