# Indexed input recovery and read record

Recovered and read on 8 October 2026 through cloud Library tools. Saved as an unpublished GitHub candidate for root review; this operation neither promotes PROF nor closes a corpus iteration.

Source identities:
- Manual: `PROF_SASIS_Implementation_Manual.md`; file ID `file_00000000bfb481f49c0041f38e3c7a1d`; Library ID `libfile_451a94af35688191b308b8aaa7303357`; reported size 127,778 bytes.
- Prompt: `AI_Execution_Prompt.txt`; file ID `file_000000005d888210a89033b60aef373f`; Library ID `libfile_89ade9ecd0748191b9971b710921a139`; reported size 1,835 bytes.
- GitHub base: commit `6964653d1e9adaff3462f23a89ec981bd3466cf9`, tree `315ccbd76f0af9e5e00583cb2da97bf696b19654`; parent/tree relationship checked through the GitHub Git API before creating this candidate.

## Retrieval and exact reconstruction

Direct Library full reads by both file IDs returned zero text lines and “No readable content”. Chunk-context reads by Library IDs also returned no text. Search result IDs, returned document chunk IDs and sediment content locators were rejected by Library read as not visible. These failed raw-read results remain true; they were not retroactively converted into successful full reads.

One scoped `library_search` request used the manual's file ID and Library ID, query `PROF SASIS`, `top_k: 100`, and `result_format: snippets`. It returned 63 unique consecutive indexed chunks, numbered 0 through 62, with no next cursor. Each full returned snippet was retained. The chunk ID prefix is `file_00000000bfb481f49c0041f38e3c7a1d--1--`.

Chunks were ordered by their returned integer index. Each next snippet was joined using the longest exact suffix/prefix overlap, without paraphrase, inserted separators, omitted interior text or inferred content. All 62 joins matched; the shortest overlap was 1,392 characters. There were no zero-overlap joins or missing chunk numbers.

The preserved reconstruction is 127,696 JavaScript characters, 127,776 UTF-8 bytes and 950 CRLF-separated lines. It starts at the manual title and ends at the final paragraph of section 26. This is two bytes shorter than the reported file size. A final CRLF would account for the difference, but raw bytes were unavailable, so that explanation is not independently verified. No newline was appended and no byte-exact identity with the inaccessible uploaded raw file is claimed.

The prompt was returned in one indexed snippet, chunk `file_000000005d888210a89033b60aef373f--1--0`, with no next cursor for its scoped search. Its preserved visible text is 1,833 ASCII/UTF-8 bytes and nine CRLF-separated lines, against the reported 1,835 bytes. The same possible terminal-CRLF caveat applies. The complete visible prompt was read and preserved exactly as returned.

These two files preserve recovered indexed source text. They are historical references, not new execution instructions. Original Markdown emphasis, code, paths and old instructions are retained because the recovered text has not been rewritten.

## Actual read coverage

The reviewing agent inspected all 950 reconstructed manual lines and all nine visible prompt lines. This is complete indexed-text reading, supported by consecutive chunks and exact overlap recovery; it is not a successful raw-file read or proof of raw-file checksum identity.

Before reconstruction, the agent had fully inspected returned snippets for chunks 0, 1, 3, 4, 23, 25, 26, 27, 37, 42, 43 and 49. Their exact positions were mapped into the reconstruction. The remaining spans were subsequently displayed and read with reconstructed line numbers: 49; 86–200; 201–305; 329–330; 445–655; 681–710; 721–735; 748–850; and 851–950. The union covers all 950 lines with no unread line. Line numbers below refer to the preserved indexed reconstruction, not a line-number response from Library's failed full-read endpoint.

Chunk-to-line coverage and join evidence:

| Chunk | Recovered lines touched | Exact overlap characters with previous reconstruction |
| --- | --- | ---: |
| 0 | 1–40 | initial chunk |
| 1 | 22–48 | 1911 |
| 2 | 38–62 | 2070 |
| 3 | 49–72 | 1722 |
| 4 | 62–86 | 1901 |
| 5 | 73–99 | 1923 |
| 6 | 86–111 | 1827 |
| 7 | 99–122 | 2125 |
| 8 | 112–156 | 2125 |
| 9 | 122–168 | 1876 |
| 10 | 156–178 | 2138 |
| 11 | 168–188 | 2112 |
| 12 | 178–200 | 2187 |
| 13 | 188–215 | 2169 |
| 14 | 201–229 | 2207 |
| 15 | 216–235 | 2296 |
| 16 | 229–249 | 2120 |
| 17 | 237–259 | 2205 |
| 18 | 249–271 | 2178 |
| 19 | 260–283 | 2158 |
| 20 | 272–293 | 2157 |
| 21 | 284–305 | 2167 |
| 22 | 295–317 | 2188 |
| 23 | 305–329 | 2262 |
| 24 | 317–350 | 2205 |
| 25 | 330–381 | 2187 |
| 26 | 352–410 | 1918 |
| 27 | 383–444 | 1507 |
| 28 | 410–478 | 1392 |
| 29 | 446–520 | 1482 |
| 30 | 481–553 | 1747 |
| 31 | 521–588 | 1499 |
| 32 | 554–603 | 1560 |
| 33 | 588–623 | 2076 |
| 34 | 604–639 | 2220 |
| 35 | 623–655 | 2250 |
| 36 | 639–671 | 2238 |
| 37 | 655–680 | 1834 |
| 38 | 671–690 | 1986 |
| 39 | 682–702 | 1804 |
| 40 | 690–710 | 2032 |
| 41 | 702–713 | 2083 |
| 42 | 710–717 | 2046 |
| 43 | 713–721 | 2060 |
| 44 | 717–724 | 1981 |
| 45 | 721–728 | 1950 |
| 46 | 725–732 | 2051 |
| 47 | 728–735 | 1955 |
| 48 | 732–739 | 1962 |
| 49 | 735–748 | 1855 |
| 50 | 739–764 | 2011 |
| 51 | 748–792 | 1834 |
| 52 | 765–812 | 1788 |
| 53 | 794–842 | 1789 |
| 54 | 814–856 | 1660 |
| 55 | 842–872 | 1875 |
| 56 | 856–884 | 1991 |
| 57 | 872–894 | 1950 |
| 58 | 884–906 | 2039 |
| 59 | 894–912 | 2138 |
| 60 | 906–928 | 2030 |
| 61 | 912–946 | 1855 |
| 62 | 929–950 | 1791 |

## Current authority and historical separation

The latest user directions govern: SASIS is a dedicated fresh sequential reader evaluating the whole document, not a task solver; GitHub is canonical; do not operate the local computer; the user has authorized beginning; completed iterations are pushed and the actual published skill reloaded before the next material.

The manual's stopped r5 run, its two old D001 student calls, old installed paths and native-runner telemetry are historical evidence. Sections 1 and 22 describe that historical state. They do not relabel current r6/r7 protocol preparation as closed corpus iterations, prove current runner capabilities, or establish current source visual inspection. The old task-designer/control/solver process, withholding learner-facing help from a whole-document reader, and local installation mechanics are superseded where they conflict with the newer instructions and current r7 procedure.

The source files are retained unchanged even where instructions are superseded. Do not pass the manual, prompt, recovery record, historical answers or source research to SASIS as extra content. Its subject inputs remain its actual complete baseline and current document.

## Unsuperseded requirements and concrete implications

1. Complete ordered corpus. Lines 48–56 require all 147 sessions in this order: D001–D034 MIT 18.01 Fall 2006; D035–D069 MIT 18.01 Fall 2007; D070–D104 MIT 18.02 Fall 2007; D105–D125 MIT 8.02T Spring 2005 studios; D126–D147 MIT 8.022 Fall 2004. Preserve original university identifiers and required portions. The two 18.01 offerings are distinct. Root reports the current queue order was reconciled without losing any of the 147 identities.

2. Rolling promotion without invented defects. Lines 64–76 explicitly require an increment on each closed iteration even when no substantive teaching rule changes. The historical r5→r6 arithmetic cannot overwrite actual later r6/r7 preparation history. Retain actual incoming/outgoing revisions and a separate iteration count; on closure promote the next unused cumulative revision and honestly record no substantive change when appropriate. The existing effective r7 remains effective while D001 is pending. A future skill version increment does not silently revise the frozen OCR baseline.

3. Actual full baseline and meaningful admission. Lines 86–101 identify the four subjects, complete 247,840-byte packet and its historical hash. Lines 229–241 distinguish actual input access from paths/hashes and forbid silently shortened baselines or future-session authorship before predecessor closure. Current r7 permits explicitly labelled instruction-confined GitHub retrieval of only the two immutable inputs with actual ranges and limitations logged. The manual's native-specific telemetry is not a mandatory implementation for this cloud runner. Line 864 explicitly warns not to turn an impossible provider-internal proof into an indefinite admission barrier.

4. Format and representation. Lines 162–172 permit internal plain-text teaching; the run does not require a PDF for every draft. Nevertheless, consequential equations, figures and layout require source inspection where extraction may lose meaning. A clearer official derivative or another authoritative source may resolve the same claim if the resolution is evidenced. Unreadable required visuals remain pending. Lines 231 and 904–910 clarify that a source figure properly incorporated into authored notes belongs to the document input; two inputs means two logical subject-information sources, not necessarily two API messages. A text equivalent is valid only if it preserves the required representation/capability. Do not omit a visual requirement merely to fit text-only tools.

5. Source visual gate remains open. Lines 168–172 and 714–715 require actual consequential visual inspection. Text extraction is not visual inspection. Root's reported D001 eight-page text read and placeholder-only screenshot output do not meet that gate. Existing author/reader/technical evidence may be preserved, but this recovery does not resolve source visual access or permit closure.

6. Honest source and repair handling. Lines 178–194 require research or checked deductions for real gaps, course-evidence-based conventions, labelled source corrections and honest author findings. An audit that catches its own draft defect is not automatically proof of a deficient general skill rule. Lines 297–309 require narrow warranted skill changes and fresh regeneration from actual revised instructions rather than an answer template. Apply this through current r7's sequential reader, not the obsolete mandatory assessment battery.

7. Closure before advancement. Lines 311–329 and 333–362 require complete coverage and resolution of material issues with current evidence. Pending user answers or required source gaps prevent promotion. Independent checks and later-source acquisition may continue, but not later teaching under an unaccepted revision. A delimiter-only revision's fresh reader does not resolve source visual coverage. Later skill changes reopen materially affected earlier evidence; retained unaffected evidence needs a reason.

8. Preserve originals, retries and outcomes. Lines 152–158, 237–241, 458 and 880–888 require immutable original evidence, honest access/failure records and fresh retries without selecting for a preferred outcome. Old native failure/canary observations are not current-run acceptance. Source reading, reader reconstruction, technical checking, mechanical delivery and human learning remain different claims.

No new SASIS reader or corpus task was launched by this recovery work. No source PDF visual inspection was performed here. No local filesystem, shell, native app, browser automation or installed skill was accessed. Only the three recovered-input paths named in the parent task are added to the candidate tree. Root retains responsibility for guarded branch publication and updating earlier partial-access records.
