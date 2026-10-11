# D008 immutable GitHub destination: independent visual review

Reviewer: visual_d008_destination. Destination commit: `663311ba27f25206ed868ce9bbfd016447528ef3`.

COMPLETE: no material visual failures in the four teaching pages and three embedded figures at the captured desktop destination.

Verdict: PASS for visual appearance only. Does not determine mathematical correctness, semantic preservation, SASIS, or live navigation/fragment behavior.

## Access and method

Root supplied actual browser captures of the four rendered GitHub teaching files at the immutable commit. I did not control the browser, alter teaching, consult other reviews, or use a substitute local rendering. I visually inspected every crop listed below at original pixel size, across the entire crop area, including the GitHub context, content, figures and final navigation. I verified each source screenshot hash and each crop’s pixel equality with its recorded source rectangle. The 950-pixel-high crops advance by 850 pixels, providing 100 pixels of overlap; final crops may be shorter.

The frozen seven-constituent manifest supplied the package identity; this review checks appearance, not mathematical truth or SASIS, nor semantic source-to-DOM preservation. Link visibility is reviewed; live link and fragment-scrolling behavior remains the root reviewer’s separate responsibility.

## Screenshot coverage

| Page | Screenshot dimensions | Original screenshot SHA-256 | Coverage |
|---|---:|---|---|
| lesson | 1348 × 7761 | `988c74ca627d0d3a30fe369f62ca64879ff7e16e50ddc0b951380b2cb0382376` | Every pixel row 0 through 7760 covered with 100px overlap; all 10 crops visually inspected at original size; last crop is blank page tail |
| practice | 1348 × 2046 | `bbb18c31020957a9627aa2defa1ad7299eb7501c96dbcfcdf109e9367b5b9262` | Every screenshot pixel row 0 through 2045 covered by overlapping unresized crops, all visually inspected. Full teaching opening, all E1–E7 prompts and ending visible. |
| hints | 1348 × 1689 | `c97c81f300f49985cb2ca292c594fbe1f26f1495391c2d332c4a77318b553340` | Every screenshot pixel row 0 through 1688 covered by overlapping unresized crops, all visually inspected. All E1–E7 hints and ending visible. The originally obscured opening is fully covered by the separate actual top viewport described below. |
| solutions | 1348 × 3567 | `0b85360a73b8eded0a5a5c2368b89fbfe7f751b943bb79b332619fa977ddca3b` | Every screenshot pixel row 0 through 3566 covered by overlapping unresized crops, all visually inspected. Full teaching opening, all E1–E7 solutions and ending visible. |

## Visual findings

No material visual failure was observed in the visible teaching portions. The three lesson figures were inspected at their actual displayed size, across overlapping crops: tangent plot, paired sine/cosine plots, and clock model. Their titles, axes, ticks, legends, arrows and captions are readable without clipping or collisions. Across the teaching prose, body text is upright and regular weight; italic mathematical variables are permissible. Equations are visibly typeset and readable, with no raw TeX, parser error boxes, or formula collisions. The labels and visible navigation links identify the learning route clearly.

Two minor, nonblocking formatting observations: section D’s Practice link wraps to its own line; solutions E3 wraps a sentence-ending period to the start of the following prose line. Neither obscures the meaning. Plain-weight section labels are consistent with the no-bold/no-italic prose constraint.

## Resolved capture-coverage item

The original hints full-page image includes a duplicated sticky breadcrumb/Preview toolbar around source y344–446, which hid its title and the start of its introduction. Root then supplied the actual top-of-hints viewport at the same immutable destination. I inspected it at original pixel size: the Hints title, full opening paragraph, Practice and Solutions links, and E1–E3 are readable. This supplies the missing portion and overlaps the earlier full-page evidence. Complete visual coverage of all four pages is now established. The original capture artifact is not classified as a teaching defect.

Opening viewport: `root-review-d008-r30/destination/hints/opening-viewport.jpg`, dimensions 1348 × 926, 125850 bytes, SHA-256 `177114fccee084e6e95bb5523c285a6faf5987c87d2c5c853d67ac1ac9a784ff`. Root reported an unanchored Hints click from Solutions and settled scrollY=0. The reviewer independently inspected the actual image and computed the file evidence.

## Crop evidence

Each crop below was visually inspected at original size. Pixel identity with the specified source box was independently verified.

| Page / crop | Box [left, top, right, bottom] | Crop SHA-256 |
|---|---|---|
| lesson / 00.png | [0, 0, 1348, 950] | `2135a708c825ff4c5e0cc07c3480b87b93dc9832290e26e3b067129e3f01c29a` |
| lesson / 01.png | [0, 850, 1348, 1800] | `f8c45226c56cb039f12c872c7e3e2ac241b1b537a1a53e4b0529846e373cd605` |
| lesson / 02.png | [0, 1700, 1348, 2650] | `f675a414bde428f61060aedf5a1538476deb60b0f76cac095af1d504a4dfc267` |
| lesson / 03.png | [0, 2550, 1348, 3500] | `51945beaff27dbab88a83f9a4a96536ae7400e2ecdcd4fe0c00ecd470ae88482` |
| lesson / 04.png | [0, 3400, 1348, 4350] | `d5fe70df2b7045878973a95bb35c9ec6445958ecedb228015a6e5a5d4bb114e6` |
| lesson / 05.png | [0, 4250, 1348, 5200] | `44e6203c93cae46a964d09bed07b1c70bee132a6be1d9a0dfb459a952ec1ba49` |
| lesson / 06.png | [0, 5100, 1348, 6050] | `76e30fb982cf4de61a2e775806e2a4805fdde04b333f3eef8a3fef999c33f14f` |
| lesson / 07.png | [0, 5950, 1348, 6900] | `a622dd258e2e7ae8d6700dcdef474a56a94e411886a53878d6098dfbed80aedd` |
| lesson / 08.png | [0, 6800, 1348, 7750] | `4fda9058cea1ee64c746328245a7c40fd9bc09f21af529c67d5aa91e8420c001` |
| lesson / 09.png | [0, 7650, 1348, 7761] | `8b1c1094b3d77662976b733821be20d5117765001603e60976ea3e506cd173aa` |
| practice / 00.png | [0, 0, 1348, 950] | `bfe0b35f183696f330010fb4ddda152727c4723c6a10404245bb017dc1521dd9` |
| practice / 01.png | [0, 850, 1348, 1800] | `58e6f99440e0cd53698ff0ded93ad405d03efdf3b4ded750808bd0ff57a13277` |
| practice / 02.png | [0, 1700, 1348, 2046] | `216242e557a0c27a237c07994c106d0553a1f9fef6b427ea32f3bf3a5c1a5771` |
| hints / 00.png | [0, 0, 1348, 950] | `4817eceb3cc333da66c6a8894d9a3e65674b7f6db061fa2fe10fc2c760682b1a` |
| hints / 01.png | [0, 850, 1348, 1689] | `5f619a7fe8367c34ab5b51c84bf889aedf5f8123d1305e69adccdc85008f81e7` |
| solutions / 00.png | [0, 0, 1348, 950] | `32ef70d36a616cc152b936111ee0e0138ac230512b8749c3e4eedbb4529b9d4f` |
| solutions / 01.png | [0, 850, 1348, 1800] | `fb6a3769222345d295d3cc20af0dfa062c024615bc369a3d2b9678936f801517` |
| solutions / 02.png | [0, 1700, 1348, 2650] | `38583e53d1743d29ae78491eea58eb3023557916e49bd794b97ba3dbec3cf0f6` |
| solutions / 03.png | [0, 2550, 1348, 3500] | `bdbd029bb3c200c9e3b6c9686027de76cdaec053e2a569144b1c56160623a44c` |
| solutions / 04.png | [0, 3400, 1348, 3567] | `484c24c32e4a682310947b0dc5008f28068baad273b12b92b97867376ea2b32d` |
