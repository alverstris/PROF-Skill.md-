D001 candidate v3 render recheck

This recheck is separate from the frozen-v2 report, which remains unchanged. No teaching content or GitHub file was edited during review.

Artifact identity

- Candidate commit: 964c91ebf2947f557315e1583229f8365bc6a2fc.
- File: runs/y1-reader-20261008/iterations/001/teaching-v3.md.
- Canonical candidate URL: https://github.com/alverstris/PROF-Skill.md-/blob/964c91ebf2947f557315e1583229f8365bc6a2fc/runs/y1-reader-20261008/iterations/001/teaching-v3.md.
- Verified source SHA256: 494a7508d8b7fbe56f3ce3c9a6fbe1bf2261ecdbfca0a80e81c8997d46dc6d13.
- Verified source size: 24,313 bytes and 24,279 Unicode characters.
- Canonical HTTP response: 200; 401,838 bytes.
- Retrieved GitHub HTML SHA256: 122b731d0d2b8818869ac9ab09eccc34618c0b29fb79ee631b8386e9a4877b4d.

Full markup verification

All 288 source expressions were compared in order against GitHub's delivered article HTML, with delimiter removal and ordinary HTML entity parsing. The audit includes each source payload, each resulting payload and its equality result; it is not a sample.

| Check | Result |
|---|---|
| Source inline expressions | 249 |
| GitHub inline math-renderer elements | 249 |
| Source fenced display expressions | 39 |
| GitHub display math-renderer elements | 39 |
| Inline payloads exactly equal after one HTML parse | 248 of 249 |
| Display payloads exactly equal after one HTML parse | 38 of 39 |
| All thin-space commands preserved | Yes |
| All paragraph labels retained in order | P01–P42 |

The original confirmed conversion defects are repaired: all 39 display expressions now receive block math-renderer elements, and every thin-space command that previously became a comma is preserved. The original P07 row separators are no longer reduced to single backslashes.

Two residual serialization differences prevent an honest claim that all 288 parsed inputs are byte-for-byte exact:

1. Inline expression 186, at P26: source t>0 appears as t&gt;0 after one HTML parse. The raw page contains t&amp;gt;0. A second entity-decoding step would recover the source, but that client step was not observed.
2. Display expression 5, at P07: each of the two source row terminators has two backslashes; the delivered HTML supplies three. All other characters in that display payload, including alignment ampersands and thin-space commands, match. This may be intentional GitHub preprocessing, but no executed renderer result was available to establish that.

To investigate these differences, the page's actual element registry and runtime assets were retrieved. The registry selects the math-renderer lazy module. Its runtime-declared asset URL, https://github.githubassets.com/assets/lazy-element-math-renderer-caed0228afce781b.js, returned HTTP 404. Consequently this review could not verify any subsequent client normalization. These two differences are unresolved serialization observations, not claims of observed visual failure.

Preview scope and equivalence

An independent inverse transformation removes only the new protected inline delimiters and converts the fenced math delimiters back to v2 delimiters. The result matches frozen v2 byte-for-byte, with SHA256 5a892606c9064d56bb6dea693ed5b3dfbb823608da9a4b1926c408aed00aca5b. Thus prose, mathematical payloads and task/hint/solution order are unchanged.

The previously inspected eight-page local Pandoc/LaTeX preview therefore remains evidence that those unchanged mathematical expressions and prose typeset legibly. That inspection covered every complete page, all P01–P42 material, all equations and all four attempts, hints and complete solutions. No new PDF was generated for this delimiter-only candidate, since an inverse-equivalent local preview would duplicate the same content. The prior PDF's legibility is not evidence of GitHub's layout or client renderer behavior.

Tasks, hints and complete solutions remain separate: attempts at P09/P22/P29/P31, hints at P32–P35, the complete-solution introduction at P36 and solutions at P37–P40. No answer was relocated alongside its corresponding main-lesson attempt.

Disposition

The 39-display recognition failure and comma-substitution defects from frozen v2 are repaired in the actual candidate GitHub markup. All 288 mathematical payloads were checked; 286 match after ordinary HTML parsing, and two retain explicitly documented serialization differences. No live GitHub pixels have been observed, so this report establishes corrected markup structure and preserved source content, with the two client-normalization questions and actual GitHub visual appearance still unverified.

Evidence

- github-page.html and github-article.html: unmodified canonical response and extracted article.
- markup-audit.json and markup-audit.log: all 288 ordered comparisons and both differences.
- check_markup.py: reproducible HTML payload audit.
- inverse-check.json: exact source inversion result.
- element-registry-f287ea780276e196.js and wp-runtime-164177510e1e41fc.js: retrieved GitHub registration/runtime evidence.
- ../report.md, ../preview.pdf and ../page-1.png through ../page-8.png: original preserved review and full visual-preview scope.
