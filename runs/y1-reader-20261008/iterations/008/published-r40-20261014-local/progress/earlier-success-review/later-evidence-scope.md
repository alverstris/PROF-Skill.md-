# Later eight cases: attribution and printed-check evidence scope

Read-only evidence audit for D009, D010, D011, D012, D013, D014, D015 and D017. This report inventories exposures and the scope of already-existing reviews. It performs no new numerical or original-source verification, declares no mathematical failure, and supplies no new global acceptance or learner-outcome verdict. The parent verified the exact teaching identities against pinned main; the final authoritative identity manifest is `accepted-teaching-exposure-inventory.json`, including the resolved accepted D014 frozen commit. The earlier supplied candidate inventory provided initial passage locators only. Line references use the extracted exact teaching/evidence copies in each case directory, not rendered-page line positions.

The complete relevant saved root/source/technical review narratives were read, including their qualifications and final-review continuations. Relevant saved numerical/symbolic outputs and scripts were inspected. Huge helper state/dependency manifests are record mechanics, not evidence of the source comparison or printed arithmetic, and are not treated as mathematical review. Original PDFs and their page images were not newly opened in this audit. Thus “covered” below means the existing independent review explicitly records original-source access and the particular contrast; it does not mean that this audit independently repeated that comparison. Presence of an exposure is not evidence of failure. Exact recomputation and a fresh page comparison belong to the parent's next check.

## Exact teaching identities

| Case | Frozen teaching commit | Teaching Git blob(s) |
|---|---|---|
| D009 | `9840e70de6aa7d2c718b60dd13ace7e6f795a50e` | `12692e5b06f7f05fd490dc6a7058a13eb96aa976` (`resumption-20261009/author/teaching-r15-recovery-v3.md`) |
| D010 | `629feb501ffd69447b70011d852ece5bf8a04641` | `fa98f0f7cee0a38c41525fec67370cf16d1fd4b6` (`current-r16/author/teaching-v2.md`) |
| D011 | `d493bae7f5f680e33f2fa891c5d0310bf43e5d23` | `b8b89dd9a0bc6aa3f24c90013cba7d96c93f3364` (`current-r17/author/teaching-v3.md`) |
| D012 | `12f468d985cbc1cb462e41948f0f017a161a2099` | `9013266253204c229f8fd6db4d968ff74a22cd0a` (`current-r18/author/teaching-v2.md`) |
| D013 | `ce407f3f2a5276700e61f43d7d1c371b9f452121` | main `25c015d4827518f2ca8d7d8650ae0d160d55ae4c`; hints `5ca8ffdae8367633353ef181b8750f3557a40e07`; solutions `e0f64817bfec2cfcb530dff91f9141ca9eb9442b` (`published-r34-20261012/teaching/`) |
| D014 | `40151288dfc73314e6efb7ef74794dfa75a0a5ee` | `edb1a433605a708ec243a47fb0c516723c948d0d` (`current-r20/author/teaching-v2.md`; byte-equal at the earlier `fddf71badedb0fa55b9099762e189c24c90c4dac` pin as well) |
| D015 | `97e10125d66e612e3f0446ab1f8460c6fd4064a5` | main `7ad106d3ad18f071a5cba61bffc39152c651b697`; hints `c0e3ecbc5e84af3ca3e61b9859e7841479af40ba`; solutions `d6a60a827be9bf73df0103f0c33890e2434ad423` (`published-r36-20261012/teaching/`) |
| D017 | `a7b7de5e040882fa605716e3a954ee067d3ce9a6` | `bf08e06e2d8cb20bcc5a82b6431a321be3eaa8ac` (`published-r27-20261011/output/teaching.md`) |

All Git evidence paths below begin `runs/y1-reader-20261008/iterations/NNN/`. Exact evidence blobs and hashes are in the case's `evidence-index.json`; only the principal semantic evidence blobs are repeated here.

## Counted passages and category boundary

Counting unit: one unique learner paragraph/line that explicitly attributes a wrong printed term, label, definition, equality or caption to the original source. A paragraph containing several alleged slips counts once. A source-note recap is not counted again. Benign terminology, rounded values, source compression, missing-data boundaries and qualified interpretations are listed separately. Under this narrow rule there are **7 explicit source-error/print-correction passages** across these eight cases; the qualified source-imprecision statements below remain audit exposures without being silently converted into outright error allegations.

| Case | Count and exact counted learner lines | Qualified source statements / other exclusions |
|---|---|---|
| D009 | 0 | L13 terminology; L126 sequence-vs-all-input warning does not expressly blame the source; source-error language occurs in reviewer evidence |
| D010 | 1: L83/P022, two misprint allegations in one paragraph | L120/P032 is a qualified marker/domain interpretation |
| D011 | 0 | L40/P011 rounded source conversion; L120/P032 incomplete mirror data; L130/P036 rounding, changing referents and abbreviated sketches |
| D012 | 1: L426/P046, four named print/label/caption correction groups | L81/P009 accepts rough source scales without asserting exact last-digit rounding; later conditions in L426 are qualifications, not additional counted paragraphs |
| D013 | 1: main L132, reversed decreasing-definition comparison | Ordinary approximation/MVT numbers are not labelled independent numerical checks |
| D014 | 3: L77 equality-versus-approximation; L128 property number; L260 nested-log domain | L276 recaps existing corrections; reviewer-only constant-factor/bookkeeping observations are not extra learner allegations |
| D015 | 1: main L253, two slips in one paragraph | Contextual quantum citation/author attribution are separate provenance questions |
| D017 | 0 | L100 is a qualified odometer interpretation/source imprecision; it remains a source-contrast exposure even though the learner does not call the source erroneous |

The numerical category is also narrow: expressly labelled independent **decimal** check occurs in D012/P009; expressly labelled direct numerical evaluations occur in D014/L1 and S1. D015 and D017 expressly label exact symbolic checks. D009/P056 labels an exact sign counterexample “direct.” The remaining ordinary approximations, physical examples and broad independently-checked provenance statements are preserved below without changing their category.

## D009 — curve sketching

Learner statements and their exact scope:

- Teaching line 13, P006: “Lecture 10 calls this input a ‘critical point’; we will say stationary input and distinguish it from the graph point.” This is an attribution of terminology, not an accusation of mathematical error.
- Line 87, P026, teaches that a zero second derivative is inconclusive, that an included continuous point must change concavity, and that an excluded input cannot be an inflection point. It does **not** say there that the original source is wrong.
- Line 126, P038: “Checking only selected values such as `x=2^n` would not yet control all intervening inputs.” This contrasts a sampled/sequence argument with an all-input bound, but it does **not** explicitly attribute that deficient argument to the source.
- Line 201, P056: “the `x^4` sign check is a direct counterexample.” The target is the anticipated route that calls both `x^4` and `x^3` inflections merely because their second derivatives vanish. At zero both first and second derivatives are exactly `0`; `x^4` has a minimum and no inflection; `x^3` has an inflection and no extremum. These are symbolic/sign facts, not a decimal numerical check. No physical units are stated.

Existing independent source-contrast evidence is specific. `resumption-20261009/root-technical-and-source-review.md` (blob `bc8b80a64f4f47c48b39b7eaca1e19e94814ca8a`), lines 3, 17, 19 and 27, records all eight original page texts/images, calls the source PDF8 inflection definition false, contrasts the source's sequence-only logarithmic tail with the teaching's all-real bound, and records the complete source/figure comparison. It therefore covers those contrasts in **reviewer evidence**, although the learner text does not itself label them source errors. The saved final acceptance lines 9–11 confirms the terminology/source/provenance comparison and states the v2–v3 changes were markup only.

Mathematical corroboration is distinct. `independent_verify.py/.json` (JSON blob `39a50573afce2fcbb897daa5a6696d6c75e56343`) has 16 derivative identities, four algebra/antiderivative identities, and 30 domain-valid limits. Its stated condition is fresh root recomputation **after reading** authored answers, not blind checking. `author/new-technical-checks.json` (blob `31d067524cd07d47b867a6bf99e288df268e2157`) is a recovery-v2 author check: 60-digit mpmath differentiation at 52 input cases, 104 derivative comparisons, plus symbolic identities and limits. Neither finite samples nor this author output alone proves what the original PDF said. The root review supplies interval-sign reasoning, not sample-only global claims.

There is no expressly labelled independent/direct **decimal** check in this learner text. The direct counterexample and the transformation check at line 193, P053 (`r=2-f`, extremal points `(-1,4)` and `(1,0)`), are exact reasoning checks. Do not import the long numerical strings from author evidence into a claim about learner-facing printed digits.

Concrete additional check: reopen the exact source's terminology, PDF8 inflection definition and logarithmic-tail passage, record the original operands/wording beside P006/P026/P038/P056, and independently rederive the `x^4`/`x^3` signs and the integral bound. This would freshen the source comparison; it would not repair an established defect. Preserve the important distinction that the sharper source-error labels presently occur in reviewer prose rather than in the learner statements.

## D010 — max/min problems

Teaching line 83, P022, explicitly says: “In the original lecture's printed page 3, the first displayed height has a misprinted denominator, and the final surface-area simplification is also misprinted.” It points to P016/P021 as direct corrections. Their exact displayed formulas are at lines 50–52 and 76–80:

`h=V/(pi r^2)`, `S(r)=pi r^2+2V/r`, `r>0`; `h_*=V/(pi r_*^2)=r_*`, `h_*/r_*=1`, `S_min=3pi r_*^2=3pi^(1/3)V^(2/3)`.

These are symbolic corrections, not rounded numerical checks. Volume has cubic units, radius/height length units, and area square units. The illustrative fixed-volume plot in P020, line 69, uses `V=pi` cubic units, `r_*=1` length unit, `S_min=3pi` square units; it is an example of the formula rather than an independently labelled numerical confirmation.

Line 120, P032, separately says the original Figure 6 uses hollow markers “even at the midpoint,” so hollow style alone should not establish a deleted domain point. This is a visual/source-attribution contrast, not an algebraic one.

The independent root comparison is specific, not merely agreement with correct can algebra. `current-r16/root-source-review.md` (blob identity in D010/evidence-index.json), lines 3, 7, 9 and 11, records six original texts/images and figures; it transcribes the original first height as `V/(2pi r)`, identifies the wrong reciprocal-radius/`pi`-power simplification, gives the corrected formulas, and separately compares the hollow midpoint with the source's included-minimum prose. It also withdraws a **historical reviewer's false allegation** about the source wire derivative: the original `x/8-1/8+x/8` is correct. That historical allegation is not repeated in current teaching.

`root-technical-review-v1.md`, lines 13 and 17, expressly checks the original height/area errors and the marker explanation while independently deriving all-domain can and wire results. Final acceptance lines 5 and 11 identifies the two-definition v2 repair and records unchanged mathematical expressions/figures, preserving this contrast's revision relevance. `author/technical-check.py` lines 16–17 and `technical-check-results.json` lines 42–47 add the discriminating `V=8pi`, `r=h=2`, direct/formula area `12pi` check. That is **author-side saved evidence**, not an exact numeric check printed in the lesson and not, on its own, source-identity evidence.

Concrete additional check: inspect the original printed page 3 height and final area line visually, retaining every denominator, exponent and grouping; compare them against the exact P016/P021 expressions, derive from `V=pi r^2h`, and inspect Figure 6 together with its surrounding text. Include the correct wire derivative as a negative control against propagating the preserved old allegation. No new error is inferred here.

## D011 — related rates

Two learner attribution statements are precise but mostly qualified source-imprecision claims:

- Line 40, P011: “The source rounds the limit to `95 ft/s`; using the exact conversion leaves the conclusion unchanged.” The exact preceding result, lines 36–37, is `65 mile/hour = 65(5280/3600) ft/s = 95 1/3 ft/s`.
- Line 130, P036, says the original rounds that conversion, calls `V` tank volume before changing water dimensions, and leaves the final problem-set sketches abbreviated. Lines 120–122 explain that the source gives neither a quantitative mirror equation nor complete absolute `a,theta` definitions. These are stated limits and clarified referents, not claims that the original's important numerical answers are wrong.

`current-r17/root-source-review.md`, lines 3, 5, 7, 9 and 13, explicitly records all five source texts/images and figures, the printed `95 ft/s` versus exact `286/3 ft/s`, the radius-arrow ambiguity against the source text `radius 4 ft`, the tank/water wording shift, omitted final water-rate units and missing mirror calibration. This is specific original-vs-teaching evidence. `root-technical-review-v1.md`, lines 5, 9, 11, 13 and 15, independently reconstructs those relationships. Final acceptance lines 5 and 9 records the final-v3 preservation of all 201 mathematical payloads while fixing the arrow, parser and local referent; the source comparison is not silently borrowed across a mathematical rewrite.

The learner text contains ordinary numerical results and an exact-versus-approximate comparison, but no local sentence calling these a “direct numerical check” or “independent numerical check.” Its P036 “independently checked” is a whole-lesson provenance claim. For the parent's numerical recheck, the exact final printed strings are:

| Teaching location | Input/formula | Exact final printed digits and units |
|---|---|---|
| P009–P011, lines 27–40 | Offset `30 ft`, `D=50 ft`, `D'=-80 ft/s`; `x=sqrt(50^2-30^2)=40 ft`; `x'=(50/40)(-80)` | `-100 ft/s`; speed `100 ft/s`; limit `95 1/3 ft/s` contrasted with source `95 ft/s` |
| P020, line 80 | Cone `r/h=4/10`, net inflow `2 ft^3/min`, depth `5 ft`; `h'=1/(2pi)` | `0.159 ft/min` |
| P044, line 168 | Same cone/depth; leak `1 ft^3/min`, net `1 ft^3/min`; `h'=1/(4pi)` | `0.0796 ft/min` |
| P047–P048, lines 182–193 | `c=3 km`, original `h=5 km`, `L=4 km`, `Delta h=0.01 km`; estimate `(5/4)(0.01)` versus `sqrt(5.01^2-3^2)-4 = sqrt(16.1001)-4` | estimate `0.0125 km`; exact-geometry approximation `0.01249299 km` |
| P049, line 196 | Estimate minus exact geometry above; `1 km=1000 m` | “about” `0.00000701 km`, or `0.00701 m`; estimate overstates the change |
| P050–P051, lines 203–207 | `(5(0.2)-3(-0.1))/4`, with rates in `km/s` | `0.325 km/s`; the fixed-`c` shortcut would give `0.25 km/s` |

The saved root whole review line 15 records fresh derivation `sqrt(16.1001)-4=.01249299064808336 km` and difference `.0000070093519 km=.0070093519 m`. The saved author JSON records exact `-4+3sqrt(17889)/100` and difference `321/80-3sqrt(17889)/100`, plus numerical `0.012492990648083` and `7.0093519166373e-6`. These support the printed rounding, but the JSON is expressly author evidence. The root record also checks concavity to discriminate the direction of the approximation, not just closeness.

Concrete additional check: view the original speed and tank/mirror statements, then recompute the conversion, cone rates and finite square-root change from exact rational decimal inputs. Round separately to each displayed precision and explicitly verify the kilometre/metre conversion and overestimate direction. Do not promote a finite agreement into a universal error bound; P049 explicitly disclaims one.

## D012 — Newton's method and ring application

The learner makes four explicit source contrasts in line 426, P046:

1. Printed p.2 square-root update denominator uses the current estimate, `2x_0`.
2. Printed p.3 table lists input estimates, so error is `|x_k-sqrt(3)|`; the digit-doubling remark is qualified by the exact error identity.
3. Printed p.4 Figure 5 shows a cycle rather than the caption's “unexpected root.”
4. Figure 6 on printed p.5 right segment uses `(b-y)^2`, not `b-y^2`.

Line 81 separately says the source's rough error values are “consistent with these scales.” This is not a claim that every source entry is correctly rounded to its last digit.

The expressly labelled independent printed numerical check is P009, lines 81–89. Exact final learner strings are:

`1.73205080^2=2.99999997378064<3`; `1.73205081^2=3.0000000084216561>3`; hence positive `sqrt(3)` lies between those inputs and rounds to seven decimal places as `1.7320508`. The inputs, squared outputs and root are dimensionless. Line 81 labels this “an independent check.” The equal signs in these square calculations assert exact decimal arithmetic; their trailing digits therefore warrant an exact-integer/rational check, not only a tolerance comparison.

The adjacent approximate input-error table, lines 69–77, uses iterates `x_0=1`, `x_1=2`, `x_2=7/4`, `x_3=97/56`, `x_4=18817/10864` and prints, in order:

`0.7320508076`; `0.2679491924`; `0.0179491924`; `0.0000920496`; `0.0000000024`.

The preceding prose explicitly says approximately; these are input errors, not residual heights. Other nearby numerical geometry checks are not labelled independent: line 281 uses `a=8 m,b=3 m,L=10 m`, `D=6 m`, point `(2,-1.5) m`, lengths `2.5 m,7.5 m`, sine ratio `0.8`, vertical angles “about” `53.13 degrees`; line 406 uses `a=6 m,b=2 m,L=10 m`, point `(9/4,-3) m`, lengths `15/4 m,25/4 m`, ratios `3/5` and angles `arcsin(3/5) approximately 36.87 degrees`.

Existing independent review covers the source **contrasts**, not just Newton/ring correctness. `current-r18/root-source-review.md`, lines 3, 7, 9, 11 and 13, records all seven original texts/images, the actual source expanded denominator `2x` versus required `2x_0`, misleading `y` input-iterate table heading, rough errors, repeated unexpected-root caption versus cycle diagram/body, and misprinted right-distance label versus correct constraint. Its line 9 explicitly says source `3e-9` is not the nearest one-significant-digit rounding of `2.44585e-9`, while retaining it as a coarse scale. Thus the learner's more cautious “consistent with these scales” should not be rewritten as exact-source-rounding acceptance.

`root-technical-review-v1.md`, lines 7, 14–15 and 26, records full source/teaching comparison, exact independent iterates/error identity, a separately checked decimal square/rounding interval in `root-v1-extra-calculations.json`, the actual final cycle `x-x^3` at `+/-1/sqrt(5)` rather than an earlier source-audit witness, and the explicit P046 corrections. The filter omitted the extra-calculation file from the extracted index, so this audit additionally read its exact current Git blob directly: `runs/y1-reader-20261008/iterations/012/current-r18/root-v1-extra-calculations.json`, blob `dfd3076d8cdd70475325df31424e9b531a47fd23`. Its stated role is “independent root calculation after full source and teaching read; complements earlier prompt-only solutions.” Its `square_bracket` values are exactly `2.9999999737806400` and `3.0000000084216561`; it records `matches_final_teaching: true`, as well as the actual final cycle map `2*x**3/(3*x**2-1)`, exchanged inputs and derivative `2/5`. This is direct saved independent numeric output for the lesson's final square values, with after-reading chronology honestly declared. The file does not itself record the exact decimal input strings or a fresh-run transcript; the whole review and final teaching supply that mapping. `author/technical-checks-v2.json` lines 17–20 independently contains the same square values, but remains expressly author evidence. Final acceptance lines 13 and 19 binds v1 mathematical review to the markup-equivalent final v2.

Concrete additional check: compare all four source passages/figures visually, and independently square decimal inputs by exact integer/rational arithmetic before comparing every printed output digit and the seven-place rounding interval. Independently recompute each rational iterate's absolute error at high precision, then round to its displayed precision. Separately check the cycle/map, right-distance grouping and acute-angle conversions. No wrong printed digit is established by this inventory.

## D013 — mean value theorem and inequalities

The explicit learner source-error statement is main line 132: “The source's printed decreasing definition repeats the increasing inequality; the decreasing comparison must point the other way.” The same line defines strict increase by `a<b => f(a)<f(b)` and strict decrease by `a<b => f(a)>f(b)`. This is a direction/operator attribution, not merely a correct replacement theorem.

`published-r34-20261012/closure-review/technical-review.md` (blob `17201e372bfba1dfe0de338f3278653c968d8d48`), lines 7–11, 31 and 62, records prior complete five-page original-source/baseline admission, full final main/hints/solutions/figure reading and a 30-unit source reconciliation, then expressly says main132 corrects the original printed decreasing-definition error. Line 21 separately identifies an unrestricted false original contact statement that the new proof avoids. Thus the saved independent review addresses source correspondence.

This audit additionally located and selectively read the two relevant archived members **in memory**, without expanding the archive or modifying evidence. `published-r34-20261012/evidence/technical-complete.zip` is Git blob `f5622c610bf2bc5b859478a4e99e995b85c100d3`, 104334 bytes, archive SHA256 `575b014e7dd43313158474c34596acdfdf44eb79da149a81ca2fedfef907a4af`; its member manifest is blob `5f8cd744b94139ee4b8848827c36cccb92c4d2b6`. The complete `independent-technical/SOURCE-TECHNICAL-AUDIT.md` member (15003 bytes, SHA256 `bb7d4f017f3cd8e15e71e1e731346bc8ab18581f8b0162e63afd76172ad250b3`, matching the member manifest) was read. Its line3 states original-source/full-baseline-only preparation; line60/M10 explicitly records: “PDF page 4 actually prints f(a)<f(b) for decreasing too. Visual inspection confirms it is an original sign error, not a text-extraction accident.” It gives strict increase `f(a)<f(b)` and strict decrease `f(a)>f(b)` for every ordered pair `a<b`. This is a precise saved original-versus-corrected operand/direction witness. The complete `independent-technical/whole-technical-review/source-coverage.json` member (10852 bytes, SHA256 `c92f887054a5e522df011bf5aa488765234ff5dbf3447ab1fc9f377d091d59b7`, matching the member manifest) maps C17, original PDF page4, “Strict monotonic definitions and printed decreasing error,” to main132 and says “Original sign typo explicitly identified and corrected.” A fresh viewing of the actual original page remains an additional check, but the earlier independent contrast is no longer merely an uninspected reference in this audit.

`closure-review/root-review.md` (blob `1dca6d7a664e643062067023964f967fa3cea67c`), lines 5–19, records the exact freeze, independent prompt solving before teaching, full current teaching and complete technical-review inspection, plus root primary corroboration of continuity/EVT/MVT. The technical reviewer explicitly had **not** opened the three new external support targets; root's relevant-primary-source check is a separately bounded role, not silently credited to that reviewer.

No learner sentence labels a numerical value as a “direct,” “independent” or “numerical” check. There are ordinary exact-versus-estimated worked values, which should not be promoted into an independently labelled numerical-check exposure: main117–121 gives `f(t)=t^2,a=1`, error `h^2`, values `0.01` at `h=0.1` and `0.64` at `h=0.8`; at `x=1.8`, exact height `3.24`, tangent `2.60` (figure/root wording; alt text says two point six), MVT secant `(3.24-1)/0.8=2.8`, `c=1.4`, anchor derivative `2`. Variables are mathematical, with no physical units stated. The motion example instead has `1000/3 miles/hour`, under explicit forward-route assumptions. The technical report lines 25–27 and independent prompt comparison lines 43–52 covers these mathematical values and conditions.

Concrete additional check: open the exact original decreasing definition, record both inequalities with their variable order, and compare to main132. If the parent's new check includes the nearby ordinary numbers, use rational inputs `1/10` and `4/5` to verify the exact error/height/slope strings separately from the source attribution. No new independent-decimal-check claim should be inferred from the worked figure.

## D014 — differentials and antiderivatives

Explicit source contrasts in the exact learner text:

- Line 77: “We retain `approx` where the lecture's worked lines sometimes print `=`.” This follows the three cube-root routes and carefully says their agreement is not three independent guarantees.
- Line 128: the logarithm verification is item 3, “though the lecture calls it ‘Property 2’.”
- Line 260: “The source assumes only `x>0` but prints `ln(ln x)`: that expression actually requires `x>1`.” It retains `ln|ln x|` and excludes `x=1`, with separately chosen constants on `(0,1)` and `(1,infinity)`.

The existing root source review additionally identifies the source's “constant factor” versus additive-constant terminology and inconsistent arbitrary-constant bookkeeping, but the current learner does **not** explicitly accuse the source of those two errors. Its teaching correctly uses additive constants; do not turn every reviewer observation into a learner attribution exposure.

`current-r20/root-source-review.md`, lines 5, 11, 17, 23 and 27, explicitly records all five original texts/page images, the original exact-equality signs in methods1/3, a discriminating cube of `193/48`, the property-number error, additive-vs-multiplicative wording, and source `x>0`/`ln(ln x)` versus the real-domain counterexample `x=1/2`. It independently computes negative/positive branch derivatives. This is direct recorded source contrast, not only a list of valid primitives. `root-independent-presolutions-v1.md`, lines 3–17, separately records all seven prompt-first derivations before authored teaching. Final acceptance lines 5–7 covers complete source-correction review and full final-v2/inverse comparison.

The learner's **direct evaluation** numerical checks are exact and short:

| Location | Exact inputs and operation | Printed values |
|---|---|---|
| Line 35, L1 | `f(x)=x^2`, base `a=2`, `dx=0.1`; compare tangent with direct `f(2.1)` | `dy=0.4`; tangent `4.4`; direct `4.41`; actual `Delta y=0.41`; exact omitted term `h^2` |
| Line 316, S1 | Same function, base `3`, `dx=-0.1`; direct `(2.9)^2` | `dy=-0.6`; tangent `8.4`; direct `8.41`; exact `Delta y=-0.59`; omitted `h^2=0.01` |

These are mathematical quantities without stated physical units. The phrase “Direct evaluation gives” occurs at both lines. Their displayed decimals are exact rational arithmetic, not rounded approximations.

The cube-root estimates are **not** presented as independent numeric checks: lines 58–61 prints `65^(1/3) approx 4+1/48 approx 4.02083` and `64.1^(1/3)` estimated by `4+1/480 approx 4.002083`. S2 lines 322–326 gives input `63.7`, step `-0.3`, differential `-0.00625`, estimate `3.99375`, with relative binomial input `-0.3/64`. Line 77 explicitly rejects counting the three methods as independent accuracy guarantees.

Existing numerical evidence is differentiated by role. The root prompt-first record line5 contains exact fractions for all S1 values, and line7 contains exact `639/160=3.99375`. Root source review line11 records independent high-precision errors for `65` and `64.1`. The saved author-v2 technical JSON records source actual/linear comparisons at `65`, `641/10`, `637/10`, with actual values `4.020725758589058`, `4.002082249204809`, `3.993740208863938`; its source formulas are independently differentiated, but it is author output. No lesson passage prints those long actual-root decimals or claims them as an independent check.

Concrete additional check: use exact rational arithmetic for both labelled direct squares and changes; separately verify rounding of the three linear estimates. Inspect the original equality signs, property label and nested-log domain statement, including an admissible `0<x<1` witness and both derivatives. Keep any high-precision actual-root comparison separate from the lesson's justified linear approximation.

## D015 — differential equations and separation

Main line 253 explicitly attributes two slips to the original: printed p.2 Gaussian example needs `f(x)=-x`, consistent with `F(x)=-x^2/2`; printed p.3 member with `a=-2` is `y=-2x^2`. It says each correction can be checked by differentiation and substitution.

`published-r36-20261012/evidence/technical-report.txt` (blob `76b95d9287447add5e79c79c763054184bd2f12a`), lines 14–18, 32 and 38, records independent entire-original five-page source admission, exact final teaching admission and full review. It specifically contrasts original `f=x` with corrected `f=-x`, and original `-2y^2` with corrected `-2x^2`. These are the actual operands the learner's corrections depend on, not merely evidence that the corrected Gaussian/parabola solve their equations. Root `evidence/root-original/whole-teaching-review.md` (blob `f15bdfc98eb85acd1f1f06b47c2243fd51c3b10f`), lines 5, 13, 17 and 23, independently reconstructs the routes and confirms the two source slips with printed-page numbering.

Main64–71 calls the product-rule identity a “useful independent check”:

`d/dx[e^(x^2/2)y] = e^(x^2/2)(xy+y') = 0`, hence `e^(x^2/2)y=a` on an interval for a solution of `y'+xy=0`.

This is symbolic, not a numerical check with printed decimal digits. Its exact result is `0`, and its point is all-interval completeness without division by `y`, including `y=0` and a coefficient that cannot switch partway through an interval. Main161–164 also says “Direct differentiation confirms” `y'=2ax=2ax^2/x` for `x!=0`; main205–209 checks slopes `2` and `-1/2` at `(1,1)`, product `-1`. All are real mathematical quantities with no physical units stated. Hints35 asks the learner to calculate a derivative “independently”; that is an instruction, not evidence that any learner did so. Solution72 checks ray/tangent slopes `-2,-6` at `(-1,2)`; solution109 checks `-1,1` at `(2,-1)`; solution151 checks `-2,1/2` at `(1,2)`; these are exact point checks, not long decimal numerics.

The technical report lines 28, 38, 42, 56, 58, 62 and 76 explicitly verifies these symbolic/point relationships and supplements exact reasoning with pre-exposure forward-mode differentiation at 37 admissible sample points, tolerance `1e-12`. The finite samples do not supply the all-domain proof or source attribution. Its external-claim limits, lines 82–84, remain narrow: the quantum contextual source and the David Jerison attribution were outside that reviewer's admitted inputs. Root's whole review lines 33–35 separately checks the quantum primary-source identity. The reader-mechanics report explicitly declines a scientific/semantic verdict and adds no source-contrast evidence.

Concrete additional check: inspect the two exact original page statements, including the original `x` sign and `y`/`x` symbol in the `a=-2` member, then differentiate/substitute the corrected forms. Reconstruct the product identity with zero/nonzero `y` and interval condition; distinguish the standalone ellipse equation's `x=0` allowance from the original family's exclusion if checking the slope examples. No independent-decimal-digit exposure needs invention here.

## D017 — first fundamental theorem of calculus

Teaching line 100 says: “The lecture's odometer analogy must be read with this distinction: position differences are not generally odometer differences.” The preceding exact distinction is displacement `integral v` versus distance `integral |v|` over forward time. This is a source-imprecision clarification, not a claim of a source arithmetic error.

`published-r27-20261011/evidence/technical/original-report.md` (blob identity in D017/evidence-index.json), lines 7–15 and 27, records all five original texts/full page images and full exact teaching, then explicitly contrasts the source's initially loose identification of signed derivative with speed/odometer change against the corrected signed/magnitude interpretation. Thus existing independent evidence addresses **what the source said**, as well as mathematical correctness. Lines 34 and 92 independently check the source substitution by binomial expansion. Root final integrated review lines 7–11 records full source/content/independent reconciliation; no student mastery is inferred.

The specifically labelled “independent check” is line310, with a symbolic derivative:

`d/dx[(x^3+2)^5/15] = (x^3+2)^4 x^2`.

Inputs for the associated definite integral, lines 289–307, are original `x=1` to `x=2`, transformed `u=3` to `u=10`, and the exact printed result `(10^5-3^5)/15`. No decimal approximation and no physical units are stated for that example. The `1/15` is explained as `1/3` from the differential times `1/5` from the fourth-power antiderivative. Calling this an independent check concerns the derivative conversion, not a claim of an unseen numerical evaluation.

`technical/exact-checks.py/.json` records a genuinely different **exact arithmetic** route: independently expand `(x^3+2)^4 x^2` by the binomial theorem and integrate coefficients on `[1,2]`, obtaining `99757/15` against expected `(10^5-3^5)/15`. It has 18 exact rational cases plus expressly nonproof numerical exponential sanity checks. Root and technical prompt-first calculations separately agree on all six tasks. None of those saved numeric sanity checks is printed as a learner-facing decimal check.

The worked motion witness, lines 140–148, is `v(t)=t-1` metres/second on `0<=t<=2` seconds, signed pieces `-1/2 m,+1/2 m`, displacement `0 m`, distance `1 m`. The source-comparison row in the technical report expressly uses that witness; direct exact-check JSON contains the two halves. Q2 changes this to `2t-2 m/s` on `[0,3]` seconds, with pieces `-1 m,4 m`, displacement `3 m`, distance `5 m`. These exact physical values are relevant to the odometer distinction but are not independently labelled decimal checks in learner prose.

Concrete additional check: inspect the original odometer/speed wording together with the round-trip context, independently differentiate the printed substitution primitive, and evaluate the exact polynomial by expansion or rational endpoint arithmetic. Verify the motion sign split and metre/second-to-metre units. A correct endpoint number alone cannot substantiate either the source-wording attribution or the all-point derivative identity.

## Decision boundary for the parent

Existing full reviews do contain specific independent original-source comparisons for the explicit source claims in D010, D011, D012, D014, D015 and D017. D013's inspected original-only archived technical audit supplies the exact printed decreasing inequality, its page, and explicit visual-versus-extraction confirmation; its inspected source map binds that contrast to current main132. D012's inspected additional Git blob supplies the saved independent final decimal-square values with after-reading chronology. D009's stronger source-error descriptions occur in reviewer evidence; the learner statements themselves teach the corrected conditions and sampled-vs-all-input distinction without explicitly accusing the source.

The clearest exact printed numeric-check recheck targets are D012's labelled independent decimal squares/bracket and D014's labelled direct squared-value comparisons. D011 has detailed finite-geometry/rounding comparisons and a broad independently-checked provenance claim, so its exact printed numeric strings are retained above without relabelling them as local independent numerical-check claims. D009, D010, D013, D015 and D017 mainly expose symbolic/sign/source distinctions or ordinary numerical examples in this narrow category. All requested fresh checks above are concrete additional verification, not evidence that any case has failed or that a previously recorded acceptance must be revoked.
