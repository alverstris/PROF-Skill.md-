D016 r25 — supplementary disposition of two shared observations

Status and scope

This supplement is additive. technical-original.md remains unchanged at SHA-256 39be729663000277d241c4da558f351f88c899ff484f7e9c92668d3e36b8a05d. It records inspection after the coordinator shared two specific observations. It does not pretend those observations were found during the original independent audit, and it supersedes the original report's no-material-defect disposition for the claims identified below. No teaching or original review file was modified.

Newly inspected evidence: teaching.md 138–158; the full frozen staircase-pyramids.png at original detail; reviews/figure-bounds.json in full; reviews/check_figure_bounds.py in full; boundary pixels and diagnostic crops generated only from the frozen PNG. I did not need to read the SASIS report. I read the supplied replay method and results but did not rerun its Matplotlib replay myself. My own image/hash/pixel checks are distinguished from that supplied replay evidence below.

TC-S1 — verified false general claim about units

Location: teaching.md 154, the sentence beginning “An integral and an average have different units”. The surrounding formula at 151 is f_avg = integral(f dx)/(b−a); line 154 then correctly states the general multiplicative units rule.

The unconditional opening claim is false. If x is dimensionless, multiplying the units of f by the units of x multiplies them by 1. Dividing by the dimensionless interval width also leaves those units unchanged. Thus the rest of this same paragraph supplies a direct counterexample to its opening universal assertion; no new physical theory or external premise is required.

Discriminating calculation: take dimensionless x on [0,2] and a constant f(x)=3 metres. The integral is 6 metres; the average is 3 metres. They are different quantities and different numerical values, but they have the same unit. Equally, if both x and f are dimensionless, both the integral and average are dimensionless. The current lesson already permits abstract real intervals/functions and does not constrain x to a dimensionful variable. The later borrowing model, where time has year units, is a case in which the two units do differ; that valid special case cannot make the universal statement true.

The accurate general relationship is units(integral) = units(f) × units(x), while units(average) = units(f). A difference follows when the integration variable supplies a nontrivial unit/dimension factor. The formulas in lines 151 and 154, the numerical x² example, P4's answer, and the borrowing calculations remain correct. No dependent numerical solution needs a different answer.

Consequence and classification: this is a verified material teaching overgeneralization, not merely a cosmetic wording preference. Units are being taught as a criterion for distinguishing totals from averages, and the unconditional rule could lead a reader to reject a valid integral model or infer the wrong quantity from the absence of a unit change. The correct product/division rule nearby makes the repair narrow, but does not erase the contradictory categorical claim. This is generated-teaching error, not a mistake copied from the original lecture or an extraction error.

Requirements: T1 (relevant conditions), T3 (bound claims to their conditions), and T10 (discriminating dimensional/normalisation verification). My original T1/T3/T10 passes must be qualified as failing this specific claim; the other cited mathematical witnesses are unaffected.

Proposed general PROF trigger/action/check, without a lecture-specific answer:

- Trigger: teaching turns a dimensional product or quotient into a categorical assertion that two quantities necessarily have different units or dimensions.
- Action: derive both unit expressions before making that assertion and test the relevant dimensionless or cancelling-unit case; retain the general relation and state the condition for any claimed difference.
- Observable check: an independent dimensional reconstruction covers one dimensionful and one dimensionless input where the claim's scope permits them, and the wording agrees with both. A successful numerical result in one physical example is insufficient to pass that general assertion.

This is an operative strengthening of the existing dimensional/normalisation check, not a reason to add a universal unit exercise or re-teach established algebra. Under the current iteration policy, encode any repair in PROF and verify a fresh complete generation; do not patch this frozen sentence.

TC-S2 — verified export clipping; mathematical geometry remains valid

Location: output/figures/staircase-pyramids.png, referenced by teaching.md 43 and explained at 45–53. Frozen image SHA-256 remains 242b262c3bedb8cf437f4fb62ee410a1f90336112fd245de79e03a9f223280f8. Its canvas is 1980 by 972 pixels.

The supplied replay code redirects Figure.savefig to an in-memory PNG buffer, records Text artist extents during the actual Agg draw, and compares the produced bytes with the frozen file. Its JSON reports exact byte identity for this image. The repeated records reflect draw repetitions rather than additional labels. Relevant unique bounds, in renderer coordinates with the vertical origin at the bottom, are:

| Text | Vertical extent | Canvas breach |
| --- | --- | --- |
| Top view: centred square slabs | 939.9090384544337 to 973.9090384544337 | About 1.91 pixels above height 972 |
| Central vertical section | 939.9090384544337 to 973.9090384544337 | About 1.91 pixels above height 972 |
| Horizontal ticks −2.5, −2.0, 0.0, 2.0, 2.5 | −5.645485406403999 to 22.354514593596 | About 5.65 pixels below zero |

A text bounding box crossing a canvas edge could in some cases include unused font space. Here actual visible clipping is independently corroborated by the frozen bitmap itself: both panel titles touch and lose glyph strokes at the top edge; the bottoms of horizontal tick numerals are visibly cut at the bottom edge. My pixel check found dark glyph pixels on the exact first row within both title regions (40 and 23 pixels), and on the exact last row within checked negative, zero and positive tick regions (24, 14 and 24 pixels). Enlarged crops show the truncation and are preserved as technical-supplement-staircase-top-crop.png and technical-supplement-staircase-bottom-crop.png. technical-supplement-figure-pixels.json records the hash, dimensions, sample regions and counts. These crops do not reconstruct the missing pixels.

Consequence and classification: this is a verified rendered-output defect under T11, supported by T12's separation of semantic and rendered-quality checks. It is more than a hypothetical bounding-box warning and should fail/reopen the figure's export-quality check. The artifact does not retain all intended title/tick glyphs, so the original report's image-quality assessment was incomplete. A caption carrying some of the same information does not make the clipping disappear.

The mathematical consequence is narrower: no incorrect pyramid, section width, height, containment relation or volume result has been established. The numerical positions and intended tick values remain inferable, and teaching.md 45/47 explicitly supplies the bases, heights and common orientation. The geometric proof and P2 answers still stand. Classify this as an output/rendering failure requiring correction, not as a mathematical failure or a source-coverage omission. It is independent of the previously reported minus-label overlap in a different figure.

Proposed general PROF trigger/action/check:

- Trigger: a plot or figure is exported to a fixed raster/vector canvas containing titles, axes, tick labels, legends or annotations near its edges.
- Action: inspect the actual export at its final size and resolution, including every edge; provide adequate canvas/margins or reposition affected text before export. Where available, supplement inspection with renderer extents, without treating extents alone as a substitute for viewing the glyphs.
- Observable check: all intended meaningful glyphs survive the final exported artifact with no unintended edge clipping; recheck layout after export settings, figure size or font changes. Source geometry and an unclipped interactive preview cannot certify the saved image.

Under the current iteration policy this failure should be handled through the relevant PROF export/inspection procedure and a fresh generation, preserving the frozen image as evidence. No repaired image was created here.

Effect on the original audit

The original report remains a historical record of what that review found. This supplement corrects its scope: there is now one verified material dimensional overgeneralization and one verified figure-export failure. The independent P1–P6 calculations, full source-coverage mapping, and geometric/interest derivations remain valid. The two earlier nonmaterial notes retain their original scope. Live GitHub destination evidence is still not supplied by this supplementary local review; local clipping is already established independently of that pending check.
