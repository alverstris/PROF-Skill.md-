Scoped earlier-case check: exported figure text at image bounds

Root checked the accepted D001–D015 constituents against their immutable accepted commits. All 17 Markdown constituents match the recorded SHA256 identities and exact Git bytes. A full syntax scan for Markdown images, HTML images/figures, SVG and Mermaid found 25 embedded image assets: 22 PNGs and 3 SVGs. No old teaching or image was edited.

All 25 assets also match the actual immutable Git bytes at the applicable accepted commit. Their paths, source locators, hashes, dimensions and checks are in earlier-figure-identities.json; all 17 Markdown identities and exact image-use lines are in earlier-figure-scope.json.

Root visually opened every one of the 25 assets, in five batches covering indices 0–4, 5–9, 10–14, 15–19 and 20–24. PNGs were viewed directly. The three D015 SVGs were exported to temporary PNGs using the installed Inkscape page renderer, with the original SVG files unchanged, and those full page exports were visually inspected. CairoSVG was unavailable; it was not used, and no package installation was performed.

Inspection scope and result

Titles, axis labels, tick labels, legends and explanatory labels remain within the exported canvas in every inspected earlier figure. No instance of the D016 boundary-text clipping defect was found. Every image has zero dark pixels on its four outermost raster edges in the associated mechanical scan, corroborating the actual visual inspection; the zero count alone is not claimed as a universal clipping test. Several plotted curves correctly continue to the axes' internal limits; this is intentional plot-window cropping, not truncated explanatory text.

| Material | Embedded assets | Scoped disposition |
| --- | --- | --- |
| D001 | 0 | Exported-figure boundary check not applicable |
| D002 | 1 PNG | Complete labels inside canvas |
| D003 | 1 PNG | Complete labels inside canvas |
| D004–D008 | 0 | Exported-figure boundary check not applicable |
| D009 | 4 PNGs | Complete labels inside canvas |
| D010 | 5 PNGs | Complete labels inside canvas |
| D011 | 4 PNGs | Complete labels inside canvas |
| D012 | 4 PNGs | Complete labels inside canvas |
| D013 | 3 PNGs | Complete labels inside canvas |
| D014 | 0 | Exported-figure boundary check not applicable |
| D015 | 3 SVGs | Full page exports retain complete labels inside canvas |

No additional reopening is justified by this scoped check. This does not repeat the earlier lessons' scientific/source/SASIS reviews and does not claim new live GitHub pixel verification. The native SVG page extent check is distinguished from its appearance in a particular browser. D016 and D017 remain open under their current states; this report changes no queue entry.

