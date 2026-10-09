Independent T11 representation regression — D001–D005

Conclusion: no affected earlier accepted artifact was found for the proposed destination-emphasis trigger in candidate `a2389390c0709d65af4a3cf070a04e396e4a4792`. The affected set is empty. This is a narrow representation finding, not renewed teaching acceptance or a student/subject test.

Each accepted source was independently checked against its closure hash and exact git object. In each saved GitHub page, the embedded immutable commit and path agree; joining its `rawLines` with LF and restoring the final LF reproduces the accepted source bytes exactly. Its complete, untruncated `richText` reproduces the saved article exactly. Whole-article text also agrees with source after explicit math/link/image syntax normalization. No prior PASS assertion is needed for these checks.

| Accepted artifact | Frozen commit | Source SHA-256 |
| --- | --- | --- |
| D001 teaching-v4.md | 0716ea92991d7f9fe2814e137bcc830d91a27511 | 402485baa2767af9625146721e356f92bad76e4cfb738e5729c6c8b94ea79401 |
| D002 teaching-v1.md | f1c0e91c24e9140049d50c7ca965f41e36f3e1a2 | 8139080278edb96287576629e7d80933b380c1b82af60d3ede888d500cb68a3a |
| D003 teaching-v1.md | 4cbf83f2dc2859d5123fc01a0c311a268d580483 | cd7426a9b70d0ac41aa3ca0418db8c89c391b67304016a7ad38f8379fe98b5a8 |
| D004 teaching-v1.md | 197b57555834d36952e948d4100d2f835c86b20c | 5adb3e95c2fa47c94b4c665d85dc2fe669e2c0086dbc2ebc194cd59720d5d8ad |
| D005 teaching-v2.md | 32c553f279ac1e5771ff05b78a9951cbff3fee38 | 4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6 |

The whole captured article DOM was inspected, not a source-only sample.

| Actual article | p | a | math-renderer | img | table/th, h1–h6, strong/em/b/i, caption/figcaption, dt |
| --- | ---: | ---: | ---: | ---: | ---: |
| D001 | 79 | 9 | 288 | 0 | all zero |
| D002 | 95 | 65 | 354 | 1 | all zero |
| D003 | 108 | 95 | 276 | 1 | all zero |
| D004 | 114 | 38 | 305 | 0 | all zero |
| D005 | 81 | 46 | 303 | 0 | all zero |

Each title is a plain paragraph. The only classes anywhere in these articles are `markdown-body`, `entry-content`, `container-lg`, `js-inline-math` and `js-display-math`. Inline styles only set math display mode and image maximum width; none sets prose weight or style. Conventional mathematical notation is exempt, so math variables are not treated as italic prose.

All five pages link the same 21 unique active stylesheet URLs covered by the saved D006 CSS evidence; every saved CSS hash matches that retrieval inventory. Independent exact-rule inspection finds `.markdown-body table th` assigned `font-weight:var(--base-text-weight-semibold,600)`; headings similarly receive 600 and definition terms receive italic plus 600. None of those selectors has a relevant target in these articles. The linked Primer body rule assigns normal weight 400; the article, paragraph, anchor and image rules inspected introduce no prose emphasis. The machine record retains exact rules, offsets, URLs and CSS hashes.

D002’s P35 image explanation and D003’s P19 explanation are ordinary `p[dir=auto]` prose. Both actual image wrappers are `p > a > img`, without caption or emphasis classes. Image styling is maximum width; inspected image/paragraph rules add no weight or italic style. Both captured image references pin their accepted commits, and saved PNG bytes match those git objects. No new diagram teaching test was performed.

Limits: this is saved server markup plus already retrieved current bytes from its exact linked CSS URLs, not historical CSS recovery, live pixels, computed styles, client execution or a complete executable cascade. Inactive theme placeholders and dynamic styling remain unexecuted. No earlier case exercises the newly observed table-header condition, so this empty affected set is not a positive test of a table-to-plain-prose repair. There is no supported reason under this trigger to regenerate these five lessons.

`regression.json` contains full identities, DOM/class/style inventories, actual image wrappers and adjacent prose, CSS evidence, checks and limits. `regression.py` reproduces the read-only checks. All read inputs were hash-checked unchanged at completion; no original source, artifact, helper, skill or repository state was changed. Existing failures and prior review limits remain intact.
