# D008 r39 actual GitHub destination review

Checked immutable teaching commit 51abe635150f97baf5b5e84965a66588b208e37b in the Codex in-app browser, 1280 by 720 viewport. The exact teaching prefix is runs/y1-reader-20261008/iterations/008/published-r39-20261014-local/teaching/. This is a root-owned destination audit, separate from the dedicated SASIS reader and independent technical review. No frozen teaching was modified.

## Complete source-to-rendered mathematics comparison

Root read the complete source through each GitHub Code view, built an ordered inventory of protected inline and fenced display payloads, and compared every payload with the actual Preview MathML operands, operators and grouping. The independent saved technical-review/source-math-inventory.json supplies the same complete source inventory and line locators. Root inspected the complete paired results in bounded tool outputs: main indices 0–64, 65–129, 130–189, 190–215 and 216–253; hints 0–33; solutions 0–57 and 58–112. After the merge at main indices 215/216, later source indices map to one-lower rendered indices.

| File | Source expressions | Actual math-renderer / MathML expressions | Result |
| --- | ---: | ---: | --- |
| main.md | 254 | 253 | Two source expressions at line 419 merge into one malformed expression. Other 252 preserve the intended mathematics. |
| hints.md | 34 | 34 | Every intended expression preserves operands, operators and grouping. |
| solutions.md | 113 | 113 | Every intended expression preserves operands, operators and grouping. |
| Total | 401 | 400 | 399 correct source-expression mappings; two affected source expressions in one merged rendered expression. |

No renderer error nodes/notices or remaining raw mathematical code blocks were found. Absence of renderer errors does not neutralise the observed merge. All five source-format command-spacing misses still render their intended comparisons correctly; they remain a separate literal contract finding.

R01 — protected mathematics nested in a citation label breaks expression and link boundaries. At main.md line 419, the source puts the first protected inline expression inside a Markdown link label and the second after the citation. Actual rendered node 215 contains both numbers, literal dollar characters and the intervening words as individual mathematical variables. The citation link also contains the remainder of the paragraph rather than ending at the intended label boundary. The actual compact MathML structure read from the live DOM is:

`5.5 × msup(10 | − 19) $ , l a r g e r t h a n t h i s $ 1.19 × msup(10 | − 20)`

The intended two source payloads are `5.5\\times10^{-19}` and `1.19\\times10^{-20}`. The following comparative prose is ordinary prose, not a product of variables. This is an observed rendering/usability defect, not a mathematical disagreement about the numerical comparison. Its dependency is the citation/comparison paragraph; the underlying clock calculations and task solutions remain separately correct. Exact original MathML and surrounding anchor text are present in the browser tool transcript. No claim is made that all raw browser observations were exported to a durable machine-readable file.

## Destination typography

Computed font weight and style were read for every relevant direct prose-bearing paragraph, list item and anchor: 161 main elements, 41 hint elements and 71 solution elements. None had font weight above 400 or non-normal font style. This excludes conventional mathematics/code/SVG from the prose test. R01 separately records ordinary words wrongly absorbed into mathematics; that defect is not waived by the normal styling of the remaining prose. Settled direct browser screenshots visually corroborated the main Attempt F, initial hints and Solution F previews. Initial native getScreenshot observations could lag behind the current DOM; root used the direct tab.screenshot API and separate settled observations instead of attributing stale frames to a new page.

## Navigation — verified portion

Before opening main.md or any of its four image URLs in the new tab, root opened hints.md directly and activated Return to Attempt F. No scroll or full-page capture occurred between activation and settled observation. The correct main Attempt F was visible at y=124.78125, below the sticky controls. All four images were loaded at the later DOM observation. The tab had not visited these URLs; an externally controlled cold cache was not established. An earlier intermediate screenshot still showed hints during transition; only the subsequent settled main screenshot and target rectangle establish the landing.

Root then verified the first 23 of the 43 local teaching/help routes through actual link activation and settled target rectangles. They are all 15 main-file routes (Hints and Solutions A–F, All hints, All complete solutions, Return to the start), plus hint-file Return to Attempt A–D and Complete solution A–D. Each had the exact expected immutable URL, an existing intended target and visible target y between 106 and 304.40625 in the 720-pixel viewport. These include cross-file navigation from an already-fragmented source URL.

All remaining 20 routes were subsequently verified by actual semantic-link activation with Enter. The exact expected immutable URLs and visible target rectangles passed in every case. The hint-file E/F returns and complete solutions landed at y=125.04167,124.78125,124.78125,125.09375; its reading-route and all-solutions links at y=124.66667. All fourteen solution-file routes passed: Return A/Hint A y=125.27084/124.66667; B/Hint B y=124.89584/125.33334; C/Hint C y=125.02084/125.07292; D/Hint D y=124.8125/125.07292; E/Hint E y=125.04167/136.40625; F/Hint F y=124.78125/304.40625; reading route/all hints y=124.66667/124.66667. The total is now all 43 local teaching/help routes, with none missing or below/behind the viewport controls at the settled observation.

A prior ten-route observation cell exceeded its execution window and reset the browser REPL; its unreturned results were not counted. The existing tab was recovered without restarting the reader or altering any subject content. Only the later returned and inspected bounded observations established those twenty routes.

One early automated click attempt unexpectedly reached a repository directory instead of the expected hint. It was preserved as a controller/navigation-attempt failure and resolved by inspecting actual state, restoring the known source and activating the actual semantic link with Enter. A later network-idle observation timed out while the page was already visibly available; root inspected the same tab and used actual target/math readiness. Neither event proves a teaching-link defect, and neither was counted as a successful route merely because the expected link existed.

## Figure geometry and limits

All four actual main-page image elements loaded with the intended source paths and matching intrinsic width/height attributes. Initial observed displayed heights were approximately 507.79169, 380.84375, 465.47919 and 507.79169 pixels respectively, matching the exported aspect ratios. All four complete original figure files were visually inspected locally by root and independently by the technical reviewer.

Root subsequently inspected all four complete embedded images through separate settled viewport screenshots, including their full canvas edges, captions nearby, ticks, legends and labels. The current main layout had a 256-pixel file pane and 910.33337-pixel image width, compared with the earlier 320-pixel pane and 846.33337-pixel image width; the viewport remained 1280 by 720. At the later width, tangent and cosine-quadratic images were 546.19794 pixels high, sine/cosine 409.64584, and clock 500.67709, all preserving the exported aspect ratio. Root used supported native scroll actions from actual bounding rectangles to place full figures below the sticky controls. Tangent top/bottom were 130.14584/676.34378; sine/cosine 129.67709/539.32294; clock 158.29167/658.96877; cosine-quadratic 130.16667/676.36461. All labels and canvas edges were complete and readable. No embedded-image distortion or clipping was established.

A prior off-viewport screenshot crop did not include the whole figure and was not counted as a complete visual check. A direct same-file URL fragment change also did not itself establish a viewport landing; navigation acceptance above relies on actual semantic link activation and settled rectangles. An actually unloaded image box was not captured, so this record does not claim direct verification of unloaded geometry or controlled cache state. Both initial and later loaded layouts were observed, without inferring their timing/cause from the different pane widths.

## Current disposition

The complete mathematical comparison establishes R01 and otherwise supports expression preservation. All 43 local teaching/help navigation routes and all four complete embedded figures are verified. First-use hints-to-late-main navigation passed under the disclosed tab/cache condition. Direct unloaded-image geometry remains unverified. Preserve all supported issues and integrate the complete fresh SASIS report before deciding the PROF repair. The current generation remains frozen and unaccepted.
