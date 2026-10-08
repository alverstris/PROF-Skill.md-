# D005 v1 frozen GitHub serialization diagnosis

Status: FAIL at the server-delivered payload layer. Exactly 13 of 280 inline math payloads differ from source, all at literal angle comparison signs. All 23 display payloads match. No live GitHub client rendering was observed.

Scope: inspect the immutable v1 capture and extraction helper; no source, helper, repository file or old evidence was edited. No PDF was generated in this diagnosis. This is not a teaching-content review.

## Frozen identity and extraction

- Frozen commit: `bdfe638d531ae5a37aa699304d5ba9042a115f2b`.
- Source: `runs/y1-reader-20261008/iterations/005/teaching-v1.md`, 24,210 bytes, SHA-256 `2279a7267fdd143a3266ffb03097abe65b7194af3cbbb31dfd3433406c6068e0`.
- The captured `source-fetch.json` reports HTTP 200 and exact local/remote equality with that hash. The current source independently has that hash.
- Reextracting `richText` from the saved `github-page.html` yields the saved `github-article.html` exactly. The saved page hash also matches its fetch record.
- Recomputing the helper audit reproduces its math arrays and every check exactly. An independent lxml HTML parser gives the same complete article text and all 303 math-renderer text values.
- An initial supplementary local git-object lookup could not find the frozen path before the parent fetched the objects. Its failure is preserved in `diagnosis.json`; after that fetch, an independent lookup succeeds and exactly matches the v1 bytes (`git-object-recovery.json`). This was missing local object availability, not a source discrepancy.

## Complete mismatch inventory

Indices below are 1-based among inline payloads. Lines refer to frozen v1. P20 and P25 locators include their continuation prose after displays.

| Logical paragraph | Source line | Inline index | Source payload | Payload after ordinary HTML parse |
|---|---:|---:|---|---|
| [P04] | 15 | 12 | `-1<x<1` | `-1&lt;x&lt;1` |
| [P16] | 87 | 98 | `l<a<r` | `l&lt;a&lt;r` |
| [P19] | 115 | 140 | `x>0` | `x&gt;0` |
| [P19] | 115 | 145 | `p'(t)=nt^{n-1}>0` | `p'(t)=nt^{n-1}&gt;0` |
| [P20] | 125 | 150 | `y>0` | `y&gt;0` |
| [P20] | 134 | 152 | `x>0` | `x&gt;0` |
| [P21] | 136 | 157 | `x>0` | `x&gt;0` |
| [P22] | 148 | 166 | `x>0` | `x&gt;0` |
| [P23] | 150 | 169 | `-\pi/2<y<\pi/2` | `-\pi/2&lt;y&lt;\pi/2` |
| [P24] | 158 | 172 | `x>0` | `x&gt;0` |
| [P25] | 168 | 185 | `1+x^2>0` | `1+x^2&gt;0` |
| [P25] | 174 | 186 | `\cos y>0` | `\cos y&gt;0` |
| [P35] | 214 | 237 | `-1<x<1` | `-1&lt;x&lt;1` |

These 13 payloads occupy 10 logical paragraphs and contain 17 comparison signs: eight `<` and nine `>`. The other 267 inline payloads are exact.

## Inspection layers and fault attribution

For the P04 example, the source payload is `-1<x<1`. Inside the page's embedded JSON, the ampersand is JSON-escaped as `\u0026amp;lt;`; JSON decoding produces the article HTML fragment `$-1&amp;lt;x&amp;lt;1$`. A single ordinary HTML parse produces math-renderer text `$-1&lt;x&lt;1$`. Removing the dollar wrapper leaves `-1&lt;x&lt;1`, which differs from source. The analogous greater-than fragment is `$x&amp;gt;0$`, yielding payload `x&gt;0`.

JSON decoding and ordinary HTML parsing are the required two syntax layers. An additional entity-unescape operation on the resulting text would be a third transformation that the supplied helper does not perform. It would mask the actual mismatch. No such extra decode was used here.

The frozen source contains literal comparison characters, not pre-encoded `&lt;` or `&gt;` strings. There is no evidence of a local source mismatch, parser error, helper extraction error, lost math element, or mathematical content mistake in this finding. GitHub's captured server representation has an additional entity layer in these payloads. This establishes a serialized payload difference; it does not establish how the live custom element or MathJax handles that text.

The complete normalized prose comparison differs in exactly 17 spans, each `<` to `&lt;` or `>` to `&gt;`, with no other normalized text difference. Thus its failure has the same cause as the inline math failure, not an additional prose loss. The helper's documented normalization removes Markdown wrappers, preserves TeX and normalizes whitespace. The independent parser check validates the observed article text without changing this criterion.

All remaining captured checks pass: 41 logical paragraph labels match uniquely and in order; 23 displays match exactly; source anchors match GitHub's prefixed IDs in order; internal hrefs match in order; targets occur once; the question/hint/solution links and returns match; hints precede solutions; the specified prohibited emphasis/heading tags are absent. These are markup checks, not click or visual checks.

## Preserved D001 recurrence

D001 directly establishes the same greater-than over-encoding at P26:

| Version | Source location and spelling | Saved renderer inner HTML | After ordinary HTML parse |
|---|---|---|---|
| v2 | `teaching-v2.md:182`, `$t>0$` | `$t&amp;gt;0$` | `$t&gt;0$` |
| v3 | `teaching-v3.md:210`, protected-inline `t>0` | `$t&amp;gt;0$` | `$t&gt;0$` |
| v4 | `teaching-v4.md:208`, protected-inline `t\gt0` | `$t\gt0$` | `$t\gt0$` |

Directly inspected evidence: `prof-readability/d001-render-review/github-article.html`, `v3/github-article.html`, `v4/github-article.html`; corresponding source and audit files under `runs/y1-reader-20261008/iterations/001`; and `format-repair-v4.md`. V3's protected-inline syntax alone did not cure the angle-sign issue; the v4 named relation did. D001 does not establish a `<` / `\lt` repair precedent; that direction is observed in D005 v1. D001's separate display row-separator issue is not present in D005's exact-matching display payloads.

## Narrow conditional rule supported by the evidence

A targeted GitHub formatting rule is justified by recurrence, without making it a teaching rule or a claim about every renderer: when a frozen GitHub capture changes a literal `<` or `>` in protected inline math to entity text after ordinary HTML parsing, treat the payload check as failed; make a presentation-only repair at those affected relations using TeX `\lt` or `\gt`; freeze a new version and require a fresh exact-payload audit. Keep the source, failed capture and full repair inventory. Do not add an extra unescape pass to turn failure into success.

The prior evidence supports `\gt` at this destination. `\lt` is a corresponding repair candidate for D005, subject to its own fresh capture; this v1 diagnosis alone cannot assert its success. No global ban on literal angle signs, changes to mathematical meaning, or changes to prose are warranted.

## Limits and reproducibility

Live client pixels, client entity handling, MathJax execution, responsive GitHub layout and fragment clicking are unobserved. No PDF preview evidence is part of this diagnosis. The final source spelling's visual success needs its own inspection layer.

`diagnosis.json` contains every mismatch's exact line, column, global and within-paragraph ordinal, raw article body and character offset, the 17 complete-text differences, checks and input hashes. `reproduce.py` reads the preserved inputs, runs the helper and an independent ordinary HTML parse, and writes only the diagnosis JSON beside itself. It performs no network request, PDF operation, source edit or additional entity unescape.
