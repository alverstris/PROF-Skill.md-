# MIT 18.01 Fall 2007 recordings: full-source readability audit

All 35 stable IDs (D035–D069) are preserved. **0 eligible; 35 excluded pending verified complete multimodal recovery.** This is an evidence limit, not a claim that the lectures or videos are inherently unreadable.

The official [video gallery](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/video_galleries/video-lectures/) distinguishes the Fall 2007 recordings from the Fall 2006 notes and warns of imperfect correspondence. Each recording’s linked notes/review packet is recorded exactly. Those associations do not establish a complete substitute for board work and recorded explanations.

Official PDF transcripts, timed VTT captions, Archive.org MP4 URLs, YouTube embeds, and linked note URLs are in `audit.json`, with actual HTTP results and local evidence. Transcript text acquisition is distinguished from exhaustive semantic reading. The archive lists roughly 28.52 hours and 3.95 GB across the 35 recordings.

A helper inspected five native 480×360 video frames across L01–L03. L03 at 23:00 clearly supplies geometric diagrams referenced by the text, proving a viable image-reading route. It does not prove whole-lecture or whole-series visual coverage. Initial whole-file requests for L01–L03 ended short of Content-Length. L03 was subsequently completed through ordinary HTTP Range continuation (115,324,849 bytes), MD5-matched to archive metadata and fully decoded (video and audio, ffmpeg exit 0). This proves full technical capture/decode is possible for that recording. No full semantic video/audio inspection is claimed.

Complete eligibility would require a full acquisition/decode plus a time-ordered semantic pass resolving every relevant board state, equation, diagram, pointing reference and unexplained speech gap, then reading the associated notes. Caption time span alone does not establish this.

| Material | Stable ID | Recording | Specific remaining visual dependency (selected evidence, not complete inventory) |
|---|---|---|---|
| D035 | `mit-18-01-fall-2007-recordings-L01` | Rate of Change | 00:04:49–00:05:10: Graph and point P introduced by spatial references; subsequent colored tangent/secant construction needs the board geometry. |
| D036 | `mit-18-01-fall-2007-recordings-L02` | Limits | 00:22:16–00:24:06: Left/right limits are arranged on opposite board sides; the subsequent piecewise-function picture is referenced spatially. |
| D037 | `mit-18-01-fall-2007-recordings-L03` | Derivatives | 00:15:45–00:16:40: Geometric trigonometric-limit proof introduces a unit-circle diagram, angle and colored vertical distance; its exact relations need the drawing. |
| D038 | `mit-18-01-fall-2007-recordings-L04` | Chain Rule | 00:05:32–00:06:30: Product-rule derivation refers to parts above, the current equality and cancellations; transcript contains an explicit change-in-x/change-in-u correction requiring equation alignment. |
| D039 | `mit-18-01-fall-2007-recordings-L05` | Implicit Differentiation | 00:18:33; 00:31:19–00:31:43: Implicit-derivative slopes and the combined function/inverse-function graph depend on displayed pictures. |
| D040 | `mit-18-01-fall-2007-recordings-L06` | Exponential and Log | 00:03:41–00:04:38: Exponential graph and tangent behavior are presented using a drawn curve and spatial references. |
| D041 | `mit-18-01-fall-2007-recordings-L07` | Exam 1 Review | 00:14:27–00:14:40; 00:43:56–00:44:20: Review formulas are collected on the board and graphing the derivative is discussed by reference to a picture. |
| D042 | `mit-18-01-fall-2007-recordings-L09` | Linear and Quadratic Approximations | 00:04:11–00:04:38: Logarithm graph and its tangent at x=1 compare curves drawn close together; exact graphical relation is not supplied as a transcript figure. |
| D043 | `mit-18-01-fall-2007-recordings-L10` | Curve Sketching | 00:31:21–00:31:39; 00:34:45–00:34:54: Curve sketching uses derivative signs and a newly drawn descending curve; complete board graph coverage is required. |
| D044 | `mit-18-01-fall-2007-recordings-L11` | Max-min | 00:08:52–00:09:02: Graph construction uses horizontal asymptote y=1 and another line; full arrangement and subsequent optimization work remain visually unverified. |
| D045 | `mit-18-01-fall-2007-recordings-L12` | Related Rates | 00:02:11–00:02:39: Related-rates setup explicitly starts by drawing a schematic, choosing variables and pointing to unit length. |
| D046 | `mit-18-01-fall-2007-recordings-L13` | Newton's Method | 00:07:42–00:08:40: Conical tank problem uses two drawings and a similar-triangle construction with dimensions 10 and 4. |
| D047 | `mit-18-01-fall-2007-recordings-L14` | Mean Value Theorem | 00:01:03–00:01:42: Newton iteration illustrates successive tangent lines in different colors and the next intercept x1. |
| D048 | `mit-18-01-fall-2007-recordings-L15` | Antiderivatives | 00:04:36; 00:06:12–00:06:18; 00:23:00: Differential-distance diagram for dx/dy and graph of ln(-x) require visual/spatial reading. |
| D049 | `mit-18-01-fall-2007-recordings-L16` | Differential Equations | 00:26:36–00:26:47; 00:40:20–00:40:29: Differential-equation geometry specifies a curve, ray and point; later ellipses are overlaid on the previous diagram. |
| D050 | `mit-18-01-fall-2007-recordings-L18` | Definite Integrals | 00:08:11–00:08:51; 00:10:17–00:10:29: Definite-integral construction draws a parabola, right-endpoint rectangles and a table of x and f(x) values. |
| D051 | `mit-18-01-fall-2007-recordings-L19` | First Fundamental Theorem | 00:07:16–00:07:25; 00:15:39–00:15:53: Area under a sine hump and directed travel/return picture are referenced without transcript figures. |
| D052 | `mit-18-01-fall-2007-recordings-L20` | Second Fundamental Theorem | 00:30:00–00:30:30: FTC proof explicitly uses an area-under-curve picture with vertical lines at the variable bounds. |
| D053 | `mit-18-01-fall-2007-recordings-L21` | Applications to Logarithms | 00:04:52–00:05:47: Logarithmic integral function is graphed using concavity, its value at 1 and the tangent slope. |
| D054 | `mit-18-01-fall-2007-recordings-L22` | Volumes | 00:01:42–00:01:55; 00:04:34–00:05:15: Volume slicing shows a colored bread slice, then rotates a drawn graph into a three-dimensional solid. |
| D055 | `mit-18-01-fall-2007-recordings-L23` | Work, Probability | 00:00:47–00:00:55; 00:06:47–00:06:58; 00:13:09–00:13:19: A prior board misprint is corrected; a semicircle diagram links angle, height and sine via pointing. |
| D056 | `mit-18-01-fall-2007-recordings-L24` | Numerical Integration | 00:13:29–00:13:39; 00:32:00–00:32:39: Radial-probability explanation distinguishes a red annular band from radial width; a student asks about the displayed w(r) graph. |
| D057 | `mit-18-01-fall-2007-recordings-L25` | Exam 3 Review | 00:02:54–00:03:04; 00:19:23–00:20:23: Numerical-integration review uses hyperbola values and bell-curve half-area with an asymptote from the previous board panel. |
| D058 | `mit-18-01-fall-2007-recordings-L27` | Trig Integrals | 00:17:00–00:17:12; 00:19:10–00:19:31: Trig integration refers to earlier board cases and erased half-angle formulas subsequently rewritten. |
| D059 | `mit-18-01-fall-2007-recordings-L28` | Inverse Substitution | 00:08:15–00:08:22; 00:30:29–00:30:41: Inverse-substitution work refers to a prepared board and a triangle with angle theta and adjacent/opposite/hypotenuse labels. |
| D060 | `mit-18-01-fall-2007-recordings-L29` | Partial Fractions | 00:14:03–00:14:10; 00:21:38–00:21:49: Partial-fraction coefficient calculations refer to the preceding board; general repeated-power form is described spatially. |
| D061 | `mit-18-01-fall-2007-recordings-L30` | Integration by Parts | 00:37:22–00:37:35; 00:41:49–00:42:00; 00:46:46–00:46:56: Integration-by-parts formula is moved to another board; exponential revolution and shell-volume diagrams are subsequently drawn. |
| D062 | `mit-18-01-fall-2007-recordings-L31` | Parametric Equations | 00:01:02–00:01:45; 00:03:52–00:04:02: Arc length uses a divided roadway/graph with endpoint and subdivision labels, then a rewritten formula on the next board. |
| D063 | `mit-18-01-fall-2007-recordings-L32` | Polar Coordinates | 00:01:17–00:01:30; 00:07:55–00:08:07; 00:16:05: Circle parametrization is traced counterclockwise; a displayed expression is explicitly marked as something never to write, requiring exact board notation. |
| D064 | `mit-18-01-fall-2007-recordings-L33` | Exam 4 Review | 00:01:45; 00:04:12–00:04:37; 00:06:54–00:07:07: Polar-area review compares a circular sector, extra/short areas and an offset circle with point (2a,0). |
| D065 | `mit-18-01-fall-2007-recordings-L35` | Indeterminate Forms | 00:07:54–00:08:07: Indeterminate-form derivation extends a fraction line while rewriting the numerator using f(a)=0; exact displayed equation chain remains unverified. |
| D066 | `mit-18-01-fall-2007-recordings-L36` | Improper Integrals | 00:08:57–00:09:10; 00:30:48–00:31:10; 00:38:49–00:38:58: Improper-integral graph and the tail used in limit comparison are spatially indicated; the convergence condition is moved between boards. |
| D067 | `mit-18-01-fall-2007-recordings-L37` | Infinite Series | 00:01:25–00:01:34; 00:07:35–00:08:07: Improper-integral comparison uses a descending function and later combines two diagrams including y=1/x. |
| D068 | `mit-18-01-fall-2007-recordings-L38` | Taylor's Series | 00:00:46–00:00:56; 00:20:43–00:20:53: A block-stacking construction is drawn using spatial references; a later extremely slow-growing graph is described through physical scale. |
| D069 | `mit-18-01-fall-2007-recordings-L39` | Final Review | 00:11:34–00:12:06; 00:16:51–00:17:01; 00:28:34–00:28:43: Final review refers to a graph with a pole at x=-1, a fourth derivative shown on the board and a previously written power series. |

Transport failures from the first pass are retained; later ordinary same-URL checks are separately recorded. No proxy/access settings were changed. No GitHub writes, installed-skill edits, authoring or SASIS work was performed.
