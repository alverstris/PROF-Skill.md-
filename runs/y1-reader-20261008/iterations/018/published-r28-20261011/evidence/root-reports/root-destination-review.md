# D018 r28 actual GitHub destination review

Disposition: FAIL. Keep this generation frozen and D018 pending. Repair PROF, publish and verify it, then use a fresh author and fresh SASIS reader for a complete new generation. No frozen teaching was edited.

Exact teaching: commit `f8f76d0775051896326fb400ec5782bf1d954971`, path `runs/y1-reader-20261008/iterations/018/published-r28-20261011/teaching.md`, SHA256 `4970a5ae04a73cca02eb62a20de8b5eab8d225c6b9ceb22eee44ec6a6408873c`.

Root inspected the whole actual GitHub page by successive overlapping viewport observations, including both complete PNG figures, all prose, exercises, hints, solutions and source note. Both disclosure controls were opened through the UI. The live article width was approximately 929 pixels. The source and both full-resolution PNGs had also been read before this destination review. This review is not a fresh SASIS run or a claim of rereading the entire baseline.

## Demonstrated failures

The independent settled preservation report maps all 288 source expressions. Only 271 preserve their structure: one loses tokens, ten display renderer errors, and six remain raw code. All 272 actual MathML expressions were compared; an inventory limited to rendered MathML would miss the other 16 source expressions. See `math-preservation-settled.md` and its complete JSON records.

- Source expression 22, orientation display at line 28, ends `(x<a).`; actual rendering ends `(x`. Root visually confirmed the missing comparison, operand and closing punctuation in `viewport-1.jpg`.
- Ten named-function expressions using `operatorname` produce explicit GitHub error notices and raw TeX. Root visually inspected these across `viewport-5.jpg` through `viewport-9.jpg`. The initial capture's `errors=0` queried only narrow KaTeX/MathML error selectors and is not a valid zero-error conclusion: the same HTML contains ten `.flash-error` notices. The settled capture inventories these correctly.
- Six fenced display equations inside the complete-solutions disclosure remain raw TeX after opening both disclosures and actually scrolling through every solution. Q1 is visible in `viewport-12-recovery.jpg`; Q2, Q3 and Q4 in `viewport-13.jpg`; both Q5 displays in `viewport-14.jpg`. The settled capture still has six raw math blocks, ten error notices and 272 MathML elements. The complete settled source comparison confirms no later restoration.

These are destination failures despite correct source mathematics. Repair must cover all relevant contexts and compare every source expression against the actual published surface; zero explicit error notices alone cannot prove preservation.

## Other destination observations

The independent full nonmath comparison preserves all 22,612 normalized characters, all 26 textual link labels and hrefs, and both image alt texts. Root saw no additional prose omission or crop. Both figures loaded at native size 1428 by 781 and displayed at approximately 929 by 508 pixels; their complete canvases and captions were inspected and legible. Source-to-render mathematics is a separate failed gate.

`typography.json` records 122 paragraph/list/link/summary elements. Every computed font weight is 400 and every computed font style is normal. Mathematical glyph styling is not prose emphasis.

Root actually clicked all 22 local content edges, comprising the two help-group links, five question-to-hint links, five question-to-solution links, and ten return links. All eventually reached their matching hashes/targets. Together with the two loaded linked figures, there are 24 local references; four external reference links are not part of this local-navigation claim. `navigation.json` preserves every observation, including an initial locator-click miss on a wrapped Return to Q1 link: its bounding-box midpoint fell outside the painted text. A screenshot-grounded click on the actual visible text successfully reached `#q1`; do not misclassify this interaction artifact as a broken href.

Initially closed Hint Q1 and Solution Q1 links move to the help area and leave the respective explicitly labeled disclosure control visible; they do not themselves open the disclosure. Opening that control exposes the requested help. This is a usable two-step route, not evidence of one-click reveal. The two distinct controls separate hints from complete solutions.

One minor navigation limitation was observed: the Q1 return target can land partly beneath GitHub's sticky header (target top approximately 40–57 pixels). A small ordinary upward scroll reveals the complete question, as `q1-after-small-scroll.jpg` shows. Record this limitation rather than claiming every target is completely visible immediately. No content is missing; root does not classify this alone as a material blockage.

## Evidence and scope

Saved viewport witnesses are 0, 1, 2, 4–11, 12-recovery, 13 and 14, plus the closed-hint, opened-hint, navigation and return-target screenshots. Viewport 3 was visually observed during the original sequence but its file did not persist; no saved-image claim is made for it. The original viewport 12 did not persist and was replaced by a freshly observed recovery screenshot. Whole-page inspection is based on the actual observations, not an inferred count of screenshot files.

Scientific/source review and fresh SASIS findings are separate evidence, to be dispositioned by the coordinator. A prospective syntax fixture may test a repair, but cannot convert this failed frozen generation into an accepted one. Earlier accepted cases with affected syntax require targeted actual-destination checks before reopening or declaring them unaffected.
