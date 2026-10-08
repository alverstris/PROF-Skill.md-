# MIT 18.02 Fall 2007 full-source readability audit

Audited 2026-10-08. Preserves all 35 original IDs (D070-D104). **0 eligible; 35 excluded pending complete semantic visual recovery.**

Available original recordings are not equivalent to established complete source readability. Actual tools provide transcripts and extracted images, but this audit did not obtain a complete, validated visual/gesture reconstruction or independently listen to all audio. Sampling and ffmpeg decoding do not certify those channels. All 35 remain excluded pending that recovery.

## What was actually checked

- eligible_readable: 0
- excluded_incomplete_or_unreadable: 35
- source_pages_downloaded: 35
- transcript_pdfs_downloaded_and_text_extracted: 35
- vtt_assets_downloaded: 35
- original_mp4_head_http_200: 35
- original_mp4s_fully_downloaded_and_audio_video_decoded: 6
- native_video_frames_actually_visually_inspected: 6
- weekly_summary_pdfs_downloaded_and_text_extracted: 14

Six original MP4s (L01-L06) decoded completely through both video and audio without errors. Decoding was an integrity check, not a semantic reading. Exactly one still per lecture was inspected: L01-L03 at 1000 seconds; L04-L06 at their midpoint. L05's wide shot has text too small to read completely; the other inspected frames contain legible local content. No full-lecture visual coverage or independent complete audio listening is claimed.

All 14 official summary PDFs were downloaded and text extracted. Week 1's three pages were visually inspected; its notes explicitly refer to pictures drawn/shown but do not reproduce them. Other notes refer to shown maps, computer plots, applets, and diagrams. Week 14 has only Lecture 33 despite being linked from the final-review sessions. No summary was accepted as a demonstrated replacement for the original recording.

Transient environment tunnel 403 responses cleared on retries. The final access finding is HTTP 200 for all 35 original MP4 HEAD requests, all 35 transcript PDFs/VTTs and all 35 source pages. This audit does not call these files missing.

## Per-session decisions

All rows have status `excluded_incomplete_or_unreadable`; the decision reflects unestablished full-source reading, not intrinsic source unavailability.

| Material | Session | Unrecovered or unverified required information |
|---|---|---|
| D070 | mit-18-02-fall-2007-L01: Dot Product | Vector/axis drawings, vector projections, parallelogram addition and vertical-plane geometry; full relation between gestures and equations has not been reconstructed. |
| D071 | mit-18-02-fall-2007-L02: Determinants | Oriented parallelogram/rotated-vector diagram, determinant sign and cross-product/right-hand-rule visual demonstrations have not been recovered over the whole lecture. |
| D072 | mit-18-02-fall-2007-L03: Matrices | Prepared color plane diagram, normal-vector placement, and complete matrix writing/pointing sequence have not been reconstructed. |
| D073 | mit-18-02-fall-2007-L04: Square Systems | Projected intersecting-plane geometry and full square-system/matrix manipulation sequence have not been reconstructed. |
| D074 | mit-18-02-fall-2007-L05: Parametric Equations | Drawn lines/planes, intersection locations and all displayed parametric equations have not been reconstructed. Inspected midpoint wide shot contains board text too small to read reliably at native resolution; later close-up recovery was not established. |
| D075 | mit-18-02-fall-2007-L06: Kepler's Second Law | Trajectory/swept-area diagrams, tangent-direction gesture and velocity decomposition over the full Kepler-law derivation have not been reconstructed. |
| D076 | mit-18-02-fall-2007-L07: Exam Review | The exam-review diagrams, referenced problem-set picture and complete written systems/solutions have not been reconstructed. |
| D077 | mit-18-02-fall-2007-L08: Partial Derivatives | Graphs, contour plots, maps and the visual comparison underlying partial derivatives have not been reconstructed; summary notes mention shown real-world maps/computer plots. |
| D078 | mit-18-02-fall-2007-L09: Max-Min and Least Squares | Complete written least-squares/minimum example, indicated lines and stationary-point geometry have not been reconstructed. |
| D079 | mit-18-02-fall-2007-L10: Second Derivative Test | Quadratic graph/shape comparison and second-derivative-test demonstration have not been reconstructed. |
| D080 | mit-18-02-fall-2007-L11: Chain Rule | Full on-board differential and chain-rule notation, equality references, intermediate transformations and any visual demonstration remain semantically unverified. |
| D081 | mit-18-02-fall-2007-L12: Gradient | Gradient arrows on contour plots, direction and perpendicularity/tangent relationships have not been reconstructed. |
| D082 | mit-18-02-fall-2007-L13: Lagrange Multipliers | Level-curve/hyperbola tangency, illustrated constrained extrema and associated illustrated examples have not been reconstructed. |
| D083 | mit-18-02-fall-2007-L14: Non-Independent Variables | Displayed equations and notation for which variable is fixed remain semantically unverified. Transcript flattens one displayed relation to x^2 yz z^3=8, so exact equation recovery needs the visual source/notes reconciliation. |
| D084 | mit-18-02-fall-2007-L15: Partial Differential Equations | Graphical maxima/minima review and the complete displayed partial-differential-equation/chain-rule reasoning have not been reconstructed. |
| D085 | mit-18-02-fall-2007-L16: Double Integrals | Slicing diagrams, graph geometry and the visual relationship between iterated integrals and regions have not been reconstructed. |
| D086 | mit-18-02-fall-2007-L17: Polar Coordinates | Polar grid/area-element diagrams and integration-bound geometry have not been reconstructed; transcript itself says one picture is hard to read. |
| D087 | mit-18-02-fall-2007-L18: Change of Variables | Coordinate-transformation diagrams, parallelogram mapping and exact region/bound correspondence have not been reconstructed. |
| D088 | mit-18-02-fall-2007-L19: Vector Fields | Projected wind-pattern image, vector-field arrows and complete geometric interpretation have not been reconstructed. |
| D089 | mit-18-02-fall-2007-L20: Path Independence | Vector field versus chosen path geometry, pointed-at directions and all written path-integral computations have not been reconstructed. |
| D090 | mit-18-02-fall-2007-L21: Gradient Fields | Complete written gradient-field test/potential calculations and referenced displayed examples remain semantically unverified. |
| D091 | mit-18-02-fall-2007-L22: Green's Theorem | Oriented boundary/region drawings, center-of-mass example and visually indicated curves have not been reconstructed. |
| D092 | mit-18-02-fall-2007-L23: Flux | Flow-through-curve diagrams, chosen normal directions and the moving-fluid/fixed-curve illustration have not been reconstructed. |
| D093 | mit-18-02-fall-2007-L24: Simply Connected Regions | Curves enclosing/excluding the origin, annulus/cut construction and orientation changes have not been reconstructed. |
| D094 | mit-18-02-fall-2007-L25: Triple Integrals | Solid/cross-section diagrams and all displayed integration bounds have not been reconstructed. |
| D095 | mit-18-02-fall-2007-L26: Spherical Coordinates | Spherical-coordinate angle conventions, vertical half-plane slice and spherical area/volume-element diagrams have not been reconstructed. |
| D096 | mit-18-02-fall-2007-L27: Vector Fields in 3D | 3D vector-field pictures, spatial directions and full flux/surface-normal illustrations have not been reconstructed. |
| D097 | mit-18-02-fall-2007-L28: Divergence Theorem | Small versus enlarged geometric pictures, surfaces/normals and the complete divergence-theorem diagram/derivation have not been reconstructed. |
| D098 | mit-18-02-fall-2007-L29: Divergence Theorem (cont.) | Vertically simple solid decomposition, donut illustration, flow directions and diffusion derivation have not been reconstructed. |
| D099 | mit-18-02-fall-2007-L30: Line Integrals | Full written 3D line-integral/curl/potential computations and spatial interpretation remain semantically unverified. |
| D100 | mit-18-02-fall-2007-L31: Stokes' Theorem | Stokes boundary/surface orientation, clockwise change, curl picture and blackboard-relative directions have not been reconstructed. |
| D101 | mit-18-02-fall-2007-L32: Stokes' Theorem (cont.) | Loops, donut-shaped surfaces, closure assumptions and Stokes orientation/homotopy pictures have not been reconstructed. |
| D102 | mit-18-02-fall-2007-L33: Maxwell's Equations | Rotation/torque/position-vector demonstrations and exact displayed Maxwell equations remain semantically unverified. Transcript gives a rotation-field component as yj while companion notes give xj; text cannot be accepted without reconciliation. |
| D103 | mit-18-02-fall-2007-L34: Final Review | Review diagrams, cylinder-plane ellipse intersection and full written review calculations have not been reconstructed. Linked Week 14 PDF contains Lecture 33 only, not Lecture 34 review notes. |
| D104 | mit-18-02-fall-2007-L35: Final Review (cont.) | Drawn integration regions, top/bottom boundaries, polar bounds, right-angle geometry and full final-review writing have not been reconstructed. Linked Week 14 PDF contains Lecture 33 only, not Lecture 35 review notes. |

## Exact asset and inspection records

`audit.json` contains every original/derived asset URL, final and retry access result, downloaded path, transcript scope/caption timing, per-session visual dependency excerpt, linked weekly-summary URLs and actual coverage, video sample timestamps, and complete-decode evidence. Source downloads and extraction artifacts are retained in each `Lxx` folder and `notes/`.

No PROF authoring, SASIS, GitHub write, replacement offering, or installed-skill edit was performed.
