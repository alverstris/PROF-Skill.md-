# Independent source-packet cross-check

All five requested paragraphs were extracted from the exact committed Git blobs. This is source extraction only; it makes no rendering, browser, acceptance, or historical-delivery claim. The earlier reader-audit outputs were not accessed or altered.

The extraction contains **5 complete paragraphs, 36 inline math payloads, and 10 plain-text Markdown links**. Payload and link counts include repeated occurrences. No requested paragraph, inline math occurrence, or inline Markdown link was omitted.

Exact paragraph bytes are preserved in the five `*.paragraph.txt` files; `source-extraction.json` records identities, boundaries, paragraph hashes, payloads, and links.

## 005-teaching-v2

- Commit: `32c553f279ac1e5771ff05b78a9951cbff3fee38`.
- Path: `runs/y1-reader-20261008/iterations/005/teaching-v2.md`.
- Git blob OID (independently recomputed from Git object header and bytes): `d8c9a67266e79fec03b069fa3193354882fc3f8b`.
- Blob SHA256: `4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6`; 24261 bytes.
- Complete paragraph: line 190 through 190 inclusive.
- Preceding boundary: blank line 189.
- Following boundary: blank line 191.
- Inline math occurrences: 5; plain-text Markdown links: 2.

Complete paragraph (source text):

```markdown
[P29] H1. Start with $`2x+2yy'=0`$ and substitute the signed coordinates into the coefficient of $`y'`$. Once the slope is $`m`$, construct the tangent as $`y-y_0=m(x-x_0)`$. The two explicit branches explain why the implicit equation can be used at either sign of $`y`$. [Return to Q1](#q1) · [Solution S1](#s1).
```

Exact inline math payloads, in order (delimiters omitted):

```text
1. 2x+2yy'=0
2. y'
3. m
4. y-y_0=m(x-x_0)
5. y
```

Plain-text Markdown links, in order:

1. Label `Return to Q1`; href `#q1`.
2. Label `Solution S1`; href `#s1`.

Omissions: none.

## 007-lesson

- Commit: `4765d39aa399a0a1ff09223cae21b15ce6c7f720`.
- Path: `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/lesson.md`.
- Git blob OID (independently recomputed from Git object header and bytes): `71c1cc93e58f03a1d2f84519398a062190a965db`.
- Blob SHA256: `fd7a5dc52b8c143c8ba392b494ac879ad2722b0231dd21b3dadb50d0eedd988d`; 19817 bytes.
- Complete paragraph: line 301 through 301 inclusive.
- Preceding boundary: blank line 300.
- Following boundary: blank line 302.
- Inline math occurrences: 5; plain-text Markdown links: 2.

Complete paragraph (source text):

```markdown
P5 — generated transfer practice. For $`x\gt 0`$, find the derivative of $`y=x^x`$. Explain why inserting $`r=x`$ into the constant-power rule $`(x^r)'=rx^{r-1}`$ is not justified. A complete response states a representation or logarithmic equation that keeps the varying exponent visible, differentiates it, and gives the derivative in terms of $`x`$. [Hint P5](hints.md#h5) · [Solution P5](solutions.md#s5)
```

Exact inline math payloads, in order (delimiters omitted):

```text
1. x\gt 0
2. y=x^x
3. r=x
4. (x^r)'=rx^{r-1}
5. x
```

Plain-text Markdown links, in order:

1. Label `Hint P5`; href `hints.md#h5`.
2. Label `Solution P5`; href `solutions.md#s5`.

Omissions: none.

## 007-hints

- Commit: `4765d39aa399a0a1ff09223cae21b15ce6c7f720`.
- Path: `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/hints.md`.
- Git blob OID (independently recomputed from Git object header and bytes): `bee957570b6b869f703fd6a98f2429d210722520`.
- Blob SHA256: `d80b7cad63ec6b575b0d567dd4f4213ec4ea77b1ff61525f479859651a659a0c`; 2361 bytes.
- Complete paragraph: line 21 through 21 inclusive.
- Preceding boundary: blank line 20.
- Following boundary: blank line 22.
- Inline math occurrences: 9; plain-text Markdown links: 1.

Complete paragraph (source text):

```markdown
Differentiate $`xy`$ as $`1\cdot y+xy'`$. The derivative of $`y^2`$ is $`2yy'`$. Put terms containing $`y'`$ on one side, factor out $`y'`$, then substitute the point. A tangent of slope $`m`$ through $`(1,2)`$ has equation $`y-2=m(x-1)`$. [Return to P3](lesson.md#p3)
```

Exact inline math payloads, in order (delimiters omitted):

```text
1. xy
2. 1\cdot y+xy'
3. y^2
4. 2yy'
5. y'
6. y'
7. m
8. (1,2)
9. y-2=m(x-1)
```

Plain-text Markdown links, in order:

1. Label `Return to P3`; href `lesson.md#p3`.

Omissions: none.

## 007-solutions

- Commit: `4765d39aa399a0a1ff09223cae21b15ce6c7f720`.
- Path: `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/solutions.md`.
- Git blob OID (independently recomputed from Git object header and bytes): `5b55ac240e578efe14e81dc71c3122e2815dd00a`.
- Blob SHA256: `3716815362b8d3c4240fffeb8cc5e95dd524939a99c9d6c0b9a189976ae035de`; 6309 bytes.
- Complete paragraph: line 108 through 108 inclusive.
- Preceding boundary: blank line 107.
- Following boundary: blank line 109.
- Inline math occurrences: 10; plain-text Markdown links: 2.

Complete paragraph (source text):

```markdown
Equivalently, differentiating $`e^{x\ln x}`$ by the chain and product rules gives the same expression. The constant-power rule assumed the exponent's derivative was zero. Here the exponent is $`x`$, whose derivative is 1, and its variation creates the $`\ln x`$ term. Substituting $`r=x`$ into a rule derived for fixed $`r`$ changes that assumption. A check only at $`x=1`$ would miss this mistake because $`\ln1=0`$; at $`x=e`$ the correct derivative is $`2e^e`$, which distinguishes it from the incorrectly substituted constant-power result $`e^e`$. [Return to P5](lesson.md#p5) · [Hint P5](hints.md#h5)
```

Exact inline math payloads, in order (delimiters omitted):

```text
1. e^{x\ln x}
2. x
3. \ln x
4. r=x
5. r
6. x=1
7. \ln1=0
8. x=e
9. 2e^e
10. e^e
```

Plain-text Markdown links, in order:

1. Label `Return to P5`; href `lesson.md#p5`.
2. Label `Hint P5`; href `hints.md#h5`.

Omissions: none.

## 009-recovery

- Commit: `9840e70de6aa7d2c718b60dd13ace7e6f795a50e`.
- Path: `runs/y1-reader-20261008/iterations/009/resumption-20261009/author/teaching-r15-recovery-v3.md`.
- Git blob OID (independently recomputed from Git object header and bytes): `12692e5b06f7f05fd490dc6a7058a13eb96aa976`.
- Blob SHA256: `5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244`; 29595 bytes.
- Complete paragraph: line 227 through 227 inclusive.
- Preceding boundary: blank line 226.
- Following boundary: end of blob at line 227.
- Inline math occurrences: 7; plain-text Markdown links: 3.

Complete paragraph (source text):

```markdown
P062. To assemble the branches: on the left, begin just below the horizontal axis and descend, becoming steeper, toward negative infinity near $`0^-`$. On the right, begin at arbitrarily negative heights near $`0^+`$, rise through $`(1,0)`$ to the maximum $`(2,1/4)`$, and then descend toward the horizontal asymptote from above. The descending branch is concave down until $`(3,2/9)`$ and concave up afterward, so after that point its negative slope becomes less negative. Leave a gap at zero. This description accounts for every domain interval and distinguishes the maximum at $`2`$ from the inflection at $`3`$. [Return to Task C](#task-c) · [Hints](#hints) · [Start](#start).
```

Exact inline math payloads, in order (delimiters omitted):

```text
1. 0^-
2. 0^+
3. (1,0)
4. (2,1/4)
5. (3,2/9)
6. 2
7. 3
```

Plain-text Markdown links, in order:

1. Label `Return to Task C`; href `#task-c`.
2. Label `Hints`; href `#hints`.
3. Label `Start`; href `#start`.

Omissions: none.

## Source preservation and verification limits

Only `git rev-parse` and `git cat-file blob` were used to retrieve repository material. No working-tree source file was used as the source. Each Git blob OID was recomputed as SHA1 of the Git `blob <length>\0` header plus the exact blob bytes and matched the resolved OID. No repository content was edited.

All inline math used the `$`-backtick delimiters shown in the paragraph extracts. A check found no unaccounted dollar delimiters, and every inline `](` link marker was accounted for. The listed links all have plain-text labels. Standalone HTML anchor elements and nearby headings are outside the blank-line-bounded paragraphs and are intentionally excluded.

Source bytes, including any original non-ASCII separator characters, were retained without repair or normalization in the paragraph files. JSON also records the exact non-ASCII code points. The Markdown report displays source as text; that display is not evidence of mathematical or browser rendering.

All writes were limited to `earlier-browser-boundary-source-packets/independent-cross-check/`. No earlier audit output was read or changed, no browser was used, and no rendering or acceptance claim is made.
