# SASIS access log

Input reads were confined to the operating instruction and the two authorized subject inputs. No external URLs or other files were read. Hash verification was performed before subject reading. Text was decoded from exact bytes using UTF-8 and split on `\n`, preserving internal CR. All content and terminal LF were accounted for. Byte intervals below are zero-based, half-open; line intervals are one-based inclusive.

## Verified inputs

| Input | Bytes | SHA256 |
|---|---:|---|
| controls/references/sasis/student-role.txt | 5607 | 3dd6e341ca5e22d24d54a3377569e52062ef0f6cfbc54b169fc8d8ccd6de4469 |
| controls/references/sasis/ocr-baseline-20261007/student-baseline.txt | 247840 | 3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5 |
| author/learner/lesson.md | 15371 | 0153f228f9a7303827479731e0e312877852999f08802a20610cf23f49a255f2 |
| author/learner/figures/sine.png | 39445 | 3f117510cea147971aae5fe13cc8963020a530e6f3a31a0c25d445061a6e8de6 |
| author/learner/figures/additivity.png | 37146 | 63f32292f4e8a6c24a35a39175360f13d39a86ce6fc4926fd449ee4cca435cb1 |
| author/learner/hints.md | 2005 | 16ccd70824d53918a6b75180746cf832b60352aa5789015723dd99b044a4cd8f |
| author/learner/solutions.md | 4607 | 140dc4c04bba5a5a7bbc8906d2547206d60ac31877488db4005222623159bdc1 |

## Actual access order

1. Operating instruction: complete raw `cat`, all 5607 bytes (44 LF-delimited content lines). Tool output chunk 90e5d7; 1402 output tokens; budget 16000.
2. Metadata/hash pass: seven exact input files only. Tool output chunk dc3a6f; 252 output tokens; budget 3000.

| Sequence | Input and actual range | Byte range | Tool output chunk | Output tokens | Budget |
|---:|---|---|---|---:|---:|
| 3 | Baseline L1–L100 | [0, 15261) | e70d23 | 3914 | 14000 |
| 4 | Baseline L101–L200 | [15261, 25385) | 24ec56 | 2656 | 14000 |
| 5 | Baseline L201–L300 | [25385, 42269) | f48c63 | 4346 | 14000 |
| 6 | Baseline L301–L400 | [42269, 62401) | 0f18e1 | 5158 | 14000 |
| 7 | Baseline L401–L500 | [62401, 89411) | 67e303 | 6878 | 14000 |
| 8 | Baseline L501–L600 | [89411, 106855) | a87a88 | 4486 | 14000 |
| 9 | Baseline L601–L700 | [106855, 129645) | 818435 | 5823 | 14000 |
| 10 | Baseline L701–L800 | [129645, 151678) | 4a8e0e | 5634 | 14000 |
| 11 | Baseline L801–L900 | [151678, 166532) | 5d190b | 3839 | 14000 |
| 12 | Baseline L901–L1000 | [166532, 181185) | 5ceca0 | 3789 | 14000 |
| 13 | Baseline L1001–L1100 | [181185, 197184) | f8bdf2 | 4150 | 14000 |
| 14 | Baseline L1101–L1200 | [197184, 212695) | 1fc7dc | 4028 | 14000 |
| 15 | Baseline L1201–L1300 | [212695, 230748) | 8981ff | 4664 | 14000 |
| 16 | Baseline L1301–L1377 | [230748, 247840) | 378fd9 | 4389 | 14000 |
| 17 | lesson.md L1–L63 | [0, 4182) | 24e5bc | 1107 | 14000 |
| 18 | figures/sine.png, actual image visually inspected before further lesson reading | [0, 39445) | view_image | image | image |
| 19 | lesson.md L64–L89 | [4182, 6674) | 9a653f | 649 | 14000 |
| 20 | figures/additivity.png, actual image visually inspected before further lesson reading | [0, 37146) | view_image | image | image |
| 21 | lesson.md L90–L156 | [6674, 10902) | fbd69b | 1139 | 14000 |
| 22 | lesson.md L157–L224 | [10902, 15371) | 728644 | 1203 | 14000 |
| 23 | hints.md L1–L38 | [0, 2005) | f670b1 | 537 | 14000 |
| 24 | solutions.md L1–L111 | [0, 4607) | 8bb3c9 | 1264 | 14000 |

The metadata pass and this final verification pass read exact authorized input bytes for hashing/range calculation. They do not substitute for the substantive complete text reads and image inspections listed above. All input byte counts and SHA256 values remained unchanged on final verification.

No response contained a truncation notice. Every text output token count was below its requested budget. Baseline has 1377 content lines and terminal LF (split yields 1378 entries, final empty); lesson 224, hints 38, solutions 111 likewise end in LF. All contents were read in the specified order. Figures were inspected through view_image at their lesson insertion points, before reading the adjacent following captions.

Output files authored only in the authorized sasis-v1 directory: report-original.md and access-log.md. Original report preserved before feedback. Root admission remains provisional until independent access verification.
