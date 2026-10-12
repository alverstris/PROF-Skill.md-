# Detailed access summary — D008 clean r31

The complete chronological machine record is access-log.jsonl. The operating instruction and subject-free route metadata were read first, in one tool invocation (chunk 511ad4), with instruction printed before routing metadata. Every following subject retrieval was a separate call of the next bounded slice or complete figure; no entries were batched. Identity checks read whole-file bytes for hashes without displaying later content. All text output was complete and inspected; no clipping or recovery occurred. Each scheduled figure was visually inspected before the next route entry. The final integrity audit matched every original input identity.

## Actual baseline sequence

Byte intervals are zero-based and end-exclusive. The baseline retains CR CR LF; bytes, not splitlines counts, determine coverage.

| Order | Byte interval | Bytes | Result |
|---|---|---:|---|
| B01 | [0,15243) | 15243 | Fully displayed and read; no clipping |
| B02 | [15243,30353) | 15110 | Fully displayed and read; no clipping |
| B03 | [30353,46307) | 15954 | Fully displayed and read; no clipping |
| B04 | [46307,61403) | 15096 | Fully displayed and read; no clipping |
| B05 | [61403,76409) | 15006 | Fully displayed and read; no clipping |
| B06 | [76409,91469) | 15060 | Fully displayed and read; no clipping |
| B07 | [91469,106858) | 15389 | Fully displayed and read; no clipping |
| B08 | [106858,121934) | 15076 | Fully displayed and read; no clipping |
| B09 | [121934,137074) | 15140 | Fully displayed and read; no clipping |
| B10 | [137074,152334) | 15260 | Fully displayed and read; no clipping |
| B11 | [152334,167581) | 15247 | Fully displayed and read; no clipping |
| B12 | [167581,182862) | 15281 | Fully displayed and read; no clipping |
| B13 | [182862,198732) | 15870 | Fully displayed and read; no clipping |
| B14 | [198732,214097) | 15365 | Fully displayed and read; no clipping |
| B15 | [214097,229236) | 15139 | Fully displayed and read; no clipping |
| B16 | [229236,244375) | 15139 | Fully displayed and read; no clipping |
| B17 | [244375,247840) | 3465 | Fully displayed and read; no clipping |

Total baseline: 17 slices; [0,247840) continuous coverage; 247,840 bytes; 1,377 LF bytes. All four subject packets read.

## Actual teaching sequence

| Order | Constituent | Bounded bytes / complete figure | LF lines | Result |
|---|---|---|---|---|
| T01 | README.md | [0,3357) | 1–42 | Fully displayed and read; no clipping |
| T02 | README.md | [3357,3430) | 43–43 | Fully displayed and read; no clipping |
| T03 | figures/tangent.png | Full PNG | — | Immediately visually inspected before next entry |
| T04 | README.md | [3430,3840) | 44–46 | Fully displayed and read; no clipping |
| T05 | README.md | [3840,4199) | 47–49 | Fully displayed and read; no clipping |
| T06 | README.md | [4199,5927) | 50–75 | Fully displayed and read; no clipping |
| T07 | README.md | [5927,6028) | 76–76 | Fully displayed and read; no clipping |
| T08 | figures/basic-tangents.png | Full PNG | — | Immediately visually inspected before next entry |
| T09 | README.md | [6028,8812) | 77–120 | Fully displayed and read; no clipping |
| T10 | README.md | [8812,9389) | 121–123 | Fully displayed and read; no clipping |
| T11 | README.md | [9389,13867) | 124–200 | Fully displayed and read; no clipping |
| T12 | README.md | [13867,13973) | 201–201 | Fully displayed and read; no clipping |
| T13 | figures/cosine-quadratic.png | Full PNG | — | Immediately visually inspected before next entry |
| T14 | README.md | [13973,15577) | 202–228 | Fully displayed and read; no clipping |
| T15 | README.md | [15577,16122) | 229–231 | Fully displayed and read; no clipping |
| T16 | README.md | [16122,16213) | 232–234 | Fully displayed and read; no clipping |
| T17 | README.md | [16213,16595) | 235–237 | Fully displayed and read; no clipping |
| T18 | README.md | [16595,17739) | 238–253 | Fully displayed and read; no clipping |
| T19 | README.md | [17739,17846) | 254–254 | Fully displayed and read; no clipping |
| T20 | figures/clock-model.png | Full PNG | — | Immediately visually inspected before next entry |
| T21 | README.md | [17846,20704) | 255–293 | Fully displayed and read; no clipping |
| T22 | README.md | [20704,21501) | 294–296 | Fully displayed and read; no clipping |
| T23 | README.md | [21501,24166) | 297–335 | Fully displayed and read; no clipping |
| T24 | README.md | [24166,24711) | 336–338 | Fully displayed and read; no clipping |
| T25 | README.md | [24711,25716) | 339–346 | Fully displayed and read; no clipping |
| T26 | hints.md | [0,331) | 1–6 | Fully displayed and read; no clipping |
| T27 | hints.md | [331,743) | 7–14 | Fully displayed and read; no clipping |
| T28 | hints.md | [743,1187) | 15–22 | Fully displayed and read; no clipping |
| T29 | hints.md | [1187,1628) | 23–30 | Fully displayed and read; no clipping |
| T30 | hints.md | [1628,2017) | 31–38 | Fully displayed and read; no clipping |
| T31 | hints.md | [2017,2486) | 39–46 | Fully displayed and read; no clipping |
| T32 | hints.md | [2486,3119) | 47–55 | Fully displayed and read; no clipping |
| T33 | solutions.md | [0,322) | 1–6 | Fully displayed and read; no clipping |
| T34 | solutions.md | [322,1093) | 7–26 | Fully displayed and read; no clipping |
| T35 | solutions.md | [1093,2489) | 27–51 | Fully displayed and read; no clipping |
| T36 | solutions.md | [2489,3840) | 52–85 | Fully displayed and read; no clipping |
| T37 | solutions.md | [3840,4764) | 86–107 | Fully displayed and read; no clipping |
| T38 | solutions.md | [4764,6200) | 108–146 | Fully displayed and read; no clipping |
| T39 | solutions.md | [6200,7918) | 147–178 | Fully displayed and read; no clipping |

Totals: 39 route entries, 35 text slices, four complete figures. README.md: 25,716 bytes / 346 LF lines; hints.md: 3,119 bytes / 55 LF lines; solutions.md: 7,918 bytes / 178 LF lines. Text totals: 36,753 bytes / 579 LF lines. Figure totals: 268,753 bytes. Complete teaching: seven constituents / 305,506 bytes.

## Figure inspection witnesses

- T03: Full displayed image: labelled x/y axes, blue ln x, orange dashed tangent x-1, marked (1,0); tangent lies above curve on displayed interval; labels readable. Inspected immediately before T04.
- T08: Full two-panel image inspected before T09: sine at zero, blue curve and dashed tangent y=x; cosine at zero, blue curve and horizontal dashed y=1; x/y axes, contact and widening separation visible; no clipping.
- T13: Full image inspected before T14: blue cosine, grey dotted y=1, orange dashed 1-x^2/2, contact dot (0,1), readable axes and legend; quadratic visibly follows local bending and separates farther away.
- T20: Full schematic inspected before T21: first and second ticks shown at two positions of the same moving clock; rightward arrow constant speed v; onboard elapsed T; dotted alignments with t1,t2 for synchronized stationary reference clocks; T prime=t2-t1. Text readable.

## Integrity and condition

All eight subject-input identities matched at first access and in the final audit. Source files were read-only and not modified. No directory searches, other subject files, browsing, early help/solution exposure, other-agent messages, or author feedback occurred. Shared tools were technically available; this was instruction-confined access, not technical isolation or erased pretraining. No simultaneous-complete-context claim is made.
