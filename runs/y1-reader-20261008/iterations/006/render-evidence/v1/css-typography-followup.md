# D006 P17 CSS typography follow-up

Finding: the actually linked GitHub stylesheet explicitly assigns the four P17 table-header labels semibold weight 600. This establishes a destination-stylesheet conflict with T11's prohibition on bold/italic prose including tables. It is CSS evidence, not a live pixel observation.

The original render report, checks, teaching source and helper are unchanged. This is a separate follow-up to their stated table-styling limit.

## Exact rule and provenance

The captured immutable GitHub page directly links [primer-9be9fe6313f476af.css](https://github.githubassets.com/assets/primer-9be9fe6313f476af.css). Read-only HTTP returned status 200; the saved response is 411,517 bytes with SHA-256:

`92ba9f41530ba1da1844d1a0bea93afb5611683f6c2baa01b6df0c9b47e0d6c3`

Its unconditional top-level rule at character offset 204027 is:

```css
.markdown-body table th{font-weight:var(--base-text-weight-semibold,600)}
```

The captured article is a `markdown-body` element containing the P17 table and four bare `th` cells. Therefore this selector matches “Curve”, “Secant endpoints”, “Secant slope and line”, and “Tangent at zero”. No `strong` or `em` tag is required for this rule to style their prose.

The page also directly links [primer-primitives-97df7784617ce1ea.css](https://github.githubassets.com/assets/primer-primitives-97df7784617ce1ea.css). HTTP status 200; 11,008 bytes; SHA-256:

`88a966eb569aa65ffd1442f7c18a056ac0e44d3c87fcdc373fec51456d9371ce`

That stylesheet's `:root` declaration includes exactly:

```css
--base-text-weight-semibold:600
```

Thus the token resolves to 600; the header rule also specifies 600 as its fallback. The same Primer stylesheet contains this supporting utility rule:

```css
.text-bold{font-weight:var(--base-text-weight-semibold,600)!important}
```

The destination explicitly uses the same token for its named bold utility. The table headers therefore have a specified semibold/bold presentation, not merely a hypothetical browser default.

## Coverage and boundary

All 21 unique active stylesheet `href` URLs present in the captured page were fetched successfully and retained with URL, status and hashes. The semibold token has one assignment across those fetched stylesheets: 600 in the primitives file. The follow-up JSON records the related `th` font-weight rules; the P17 header selector above directly matches the saved markup. Data-href-only theme placeholders were not activated.

The original report's observations remain true: the article has no `strong/b/em/i` elements and the separately rendered local PDF visibly uses regular upright table-header prose. Those checks did not test the destination's CSS and cannot establish T11 compliance at that layer. This follow-up resolves that specific unknown to an observed stylesheet conflict.

No browser, rendered GitHub pixels, computed-style query, clicks or MathJax execution was used. These CSS bytes were fetched now from the exact asset URLs captured in the original GitHub page; they are not claimed to be historical CSS bytes saved during the earlier capture.

## Preservation and files

Every artifact in the pre-follow-up `artifact-hashes.json` remains byte-identical. In particular:

- Original report SHA-256: `a73ceefb7096750380fefb65aa115e93b6d60c9a69d3d54cb5b9bffafd780aaa`.
- Original preview-check SHA-256: `98effac5d4f6467f37127c82eb577562e414fd78e9aa6c332182a977f85d1aca`.

`css-typography-followup.json` holds the exact rule, source URLs/hashes, matching headers, fetch coverage and preservation checks. Raw stylesheet bytes and their fetch inventory are retained only under `css-typography-evidence/`. No teaching, helper or state changes were made; no subagents were used.
