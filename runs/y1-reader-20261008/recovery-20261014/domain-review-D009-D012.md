Independent targeted technical review: accepted D009–D012, PROF r38 T10 affected-success domain check.

Result: no independently confirmed consequential general directional/comparison failure was found in these four frozen teaching texts. This is a targeted text result, not renewed acceptance, SASIS, source-completeness or visual-completeness certification.

Repository and identity access

All reads used `alverstris/PROF-Skill.md-` at immutable commit `a512149c36d829405c716f148838b3ddbf2c882a`.

`runs/y1-reader-20261008/queue.json`, blob `9c3abcf20778a52b5aa54994cd56caf663850c45`, was fetched and parsed locally in code mode. Its full payload was not printed. The selected D009–D012 records are closed and identify the following historical transitions:

| Material | Frozen revision | Incoming → outgoing PROF | Recorded document/publication commit |
|---|---|---|---|
| D009 | `r15-recovery-v3` | r15 → r16 | document `9840e70de6aa7d2c718b60dd13ace7e6f795a50e`; acceptance publication `d7b7625dd60a107c1611743b674c85ca7bfb8e2a` |
| D010 | `D010-r16-teaching-v2` | r16 → r17 | publication `fcc989c6bdbbb495bbaf60bca761b04780fb8e45` |
| D011 | `D011-r17-teaching-v3` | r17 → r18 | publication `c07581d03836ad5f02d7367e84cb5a90e012de4d` |
| D012 | `D012-r18-v2` | r18 → r19 | publication `ef9dea1525802ed7f6ba52718f94a558c484e32c` |

The frozen identities were resolved through these metadata files, reading their identity/output fields:

- D009: `runs/y1-reader-20261008/iterations/009/resumption-20261009/final-state/manifest.json`, blob `29b6010ed55e42c04c4d8aadb04429b8752274fb`.
- D010: `runs/y1-reader-20261008/iterations/010/current-r16/author/freeze-v2.json`, blob `1cfe1f5d120a3b511c0aacd731e9f39f42a7d6c6`; final manifest `runs/y1-reader-20261008/iterations/010/current-r16/final-state/.prof-state/manifest.json`, blob `8006b51566bf9ee3734fc0a795aaacbe0bdf38cb`.
- D011: `runs/y1-reader-20261008/iterations/011/current-r17/author/freeze-manifest-v3.json`, blob `ac7c8cd90a4da776d1091d7bea1aed40caabebef`; final manifest `runs/y1-reader-20261008/iterations/011/current-r17/author/.prof-state-final-v3/manifest.json`, blob `54ed712b94e44460b1e0b54995a207cfdf94797a`.
- D012: `runs/y1-reader-20261008/iterations/012/current-r18/author/packet-v2.json`, blob `d386aad24c3ebdec742a947d7ed11d971ee4f5c4`; final manifest `runs/y1-reader-20261008/iterations/012/current-r18/final-state/v2-final/manifest.json`, blob `83ae7d847e6e2d4bdf361155fa053a62001bdb31`.

Each selected final manifest registers `final_review: pass` against its teaching SHA-256. Those are historical metadata statuses, not this review’s findings.

Frozen teaching identities and complete text access

The following files were fetched completely and read from first through last line, including equations, prompts, hints, solutions, captions, image alternative text and source/scope notes. Main teaching, hints and solutions are embedded in the same file; no separate help file was omitted.

| Material | Exact immutable repository path | Git blob | Recorded SHA-256 | Complete access |
|---|---|---|---|---|
| D009 | `runs/y1-reader-20261008/iterations/009/resumption-20261009/author/teaching-r15-recovery-v3.md` | `12692e5b06f7f05fd490dc6a7058a13eb96aa976` | `5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244` | 29,595 bytes; lines 1–228; P001–P062 |
| D010 | `runs/y1-reader-20261008/iterations/010/current-r16/author/teaching-v2.md` | `fa98f0f7cee0a38c41525fec67370cf16d1fd4b6` | `192609d9d62cc50be534df77b5e5700c6eb7c4a9c32e37c832be6b1ab133742c` | 20,323 bytes; lines 1–190; P001–P049 |
| D011 | `runs/y1-reader-20261008/iterations/011/current-r17/author/teaching-v3.md` | `b8b89dd9a0bc6aa3f24c90013cba7d96c93f3364` | `bcb390a295a8cce423b8ebfb9d292c45f7e6be3e37b9fbed1e33c6f60153f6fe` | 21,983 bytes; lines 1–208; P001–P051 |
| D012 | `runs/y1-reader-20261008/iterations/012/current-r18/author/teaching-v2.md` | `9013266253204c229f8fd6db4d968ff74a22cd0a` | `04355b5ac132bfdaecf6a165cf332d0e04a0ff29bd59b53e03d6c801c9838d59` | 32,634 bytes; lines 1–427; P001–P046 |

The SHA-256 values above are recorded frozen identity values; no separate local hashing claim is made.

Constituent coverage:

- D009: main P001–P045; hints P046–P049; solutions P050–P062.
- D010: main P001–P036; hints P037–P040; solutions P041–P049.
- D011: main P001–P036; hints P037–P040; solutions P041–P051.
- D012: main P001–P034; hints P035–P039; solutions P040–P044; concluding source and boundary notes P045–P046.

Claim groups and domain checks

D009 — curve sketching

1. Derivative-sign, extrema and concavity rules, P005–P007, P023–P027, P032, P057. The monotonicity rule is declared on an interval of differentiability. The second-derivative test concerns a stationary input and smooth local conditions. Zero first or second derivative is explicitly separated from a sufficient turn/inflection test. The worked `x³` and `x⁴` cases in P054–P056 preserve that distinction.

2. Polynomial directional claims, P008–P014, P020–P022, P029–P031, P047–P048, P051–P056. Factor signs provide the declared interval warrants. The positive even-power assertions in the hints refer to the two sides of zero, rather than asserting positivity at zero. Stationary zero cases remain explicitly admitted and treated separately.

3. Reciprocal domain and cross-gap ordering, P015–P019, P027. The domain excludes zero. `−1/x²<0` is warranted because every allowed `x` is nonzero. The text explicitly rejects extending decreasing behavior across the domain gap: `−1<1` but `q(−1)=−1<q(1)=1`. This is an appropriate discriminating comparison.

4. Logarithmic quotient, P034–P041. Its domain is `x>0`, so `x²` and `x³` are positive. The numerators retain their variable signs and their zeros at `e` and `e^(3/2)`. At permitted input `x=1`, the height is zero while the derivative is positive; the text’s claim of positive heights begins strictly after 1. The integral comparison uses positive reciprocals with `1≤t≤x`; the subsequent division is by positive `x`.

5. Rational transfer example, P049, P058–P062. The domain is `x≠0`. For `h=(x−1)/x²`, the claims retain the odd denominator sign in `h'=(2−x)/x³` and the positive even denominator in `h''=2(x−3)/x⁴`. Discriminating checks give:
   - `x=−1`: `h'=−3`, `h''=−8`.
   - `x=1`: `h=0`, `h'=1`, `h''=−4`.
   - `x=2`: `h'=0`, `h=1/4`.
   - `x=3`: `h''=0`, `h'=−1/27`.
   - `x=4`: `h'<0`, `h''>0`.

   The global maximum across both branches is also independently warranted by
   `h(x)=1/4−(x−2)²/(4x²)` for every allowed input.

No failure confirmed in D009.

D010 — max/min problems

1. Candidate and attainment claims, P003, P007–P011, P046. The closed-interval guarantee explicitly requires continuity. Interior critical inputs and endpoints are distinguished. The examples `x` on `(0,1)` and the discontinuous endpoint assignment on `[0,1]` correctly prevent confusing an approached upper bound with an attained maximum.

2. Logarithmic quotient, P004–P006, P012, P038, P042. The domain is `x>0`; denominator positivity and numerator sign changes are warranted. The restricted task has `1≤x≤√e`, hence `1−ln x≥1/2>0`. Its zero height at 1 does not contradict increasing behavior. In the tail bound, the division by `t` is explicitly restricted to `t>0`; `t=0` remains outside that division.

3. Open and closed cans, P013–P023, P039, P043–P045. The model declares `V>0`, `r>0`, `h>0`. Thus dividing by `r²`, using positive multipliers, and interpreting the numerator sign are legal throughout the feasible domain. Zero radius or zero volume is not an admitted witness against these claims. The comparison with the same-volume open can is warranted:
   `r_closed/r_open=2^(−1/3)<1` and
   `h_closed/h_open=2^(2/3)>1`.

4. Wire areas and changed domains, P024–P032, P035, P040, P047–P049. Degenerate zero-length pieces are expressly admitted only in the closed model. Independent values are
   `A(0)=A(1)=1/16`,
   `A(1/2)=1/32`,
   `A(1/4)=A(3/4)=5/128`.
   The completed-square expression and declared intervals warrant all order comparisons. The open model correctly excludes endpoint attainment while retaining its midpoint minimum.

No failure confirmed in D010.

D011 — related rates

1. Radar signed rates and speed comparison, P003–P014, P038, P042–P043. The approach and departure examples both use the stated positive road-distance branch, `x>0`; `D>0` and `0<x/D<1` follow from the offset triangle. Reversing the supplied signed distance rate reverses the road-coordinate rate while preserving its magnitude. At the discriminating closest-point boundary, the text switches to a signed road coordinate and uses the undivided equation. With finite road rate and `x=0`, `D=30`, it obtains `D'=0`, without asserting zero road speed.

2. Cone inflow, P016–P024, P039, P044–P046. The positive-height rate formula uses `h>0`. In the leak task the directional domain is expressly `0<h<10`; there `2−h/5>0` and the height-rate multiplier is positive. At `h=5`, the net volume rate is 1 and `h'=1/(4π)>0`. At boundary `h=10`, the net rate is zero, which the text expressly excludes from its interior stationary claim. The sharp-point boundary `h=0` is not passed through division by `h²`.

3. Satellite and mirror sensitivity, P027–P033, P035, P040, P047–P051. Fixed `c>0`, `L>0`, and `h>c` warrant positive `h/L`; the boundary `L=0` is explicitly identified as sensitive and outside the divided formula. Finite-error approximation is distinguished from equality. Reverse mirror sensitivities require a differentiable local inverse and nonzero derivative. The positive contributions in P051 are tied to the supplied `h'=0.2` and `c'=−0.1`, rather than asserting that `hh'−cc'` is positive for arbitrary rates.

No failure confirmed in D011.

D012 — Newton’s method and ring constraint

1. Newton update, signed errors and convergence, P003–P015, P036–P037, P041–P042, P044. A defined nonzero derivative is required for division. The positivity argument in P010 is tied to the actual trajectory beginning at `x₁=2>√3`; it does not assert that `e_k²/(2x_k)` is positive for all nonzero real `x_k`. The negative start is handled separately using `z_k=−x_k`, and zero start is explicitly illegal. Exact-root zero error therefore is not a permitted counterexample to the strictly positive errors on the described non-root trajectory. Both concrete two-cycles independently retain legal steps without claiming convergence.

2. Bisection comparison, P015, P037, P042. The guarantee requires continuity and opposite endpoint signs. The midpoint `−3/2` gives `13/8>0`, so retaining `[-2,−3/2]` is valid. A sign change across a discontinuity is explicitly rejected.

3. Ring signs, geometry and global bound, P016–P028, P038–P039, P043–P044. The general domain is `a>0` and `L>√(a²+b²)`; no positive sign is required of `b`. It follows that `D=√(L²−a²)>|b|`, which warrants `D±b>0`, `0<x<a`, `y<0` and `y<b`. Acute angles warrant equal angles from equal sines and legal positive rises.

   Discriminating allowed cases with `a=8`, `L=10`, `D=6`:
   - `b=0`: `(x,y)=(4,−3)`, lengths `(5,5)`.
   - `b=3`: `(x,y)=(2,−1.5)`, lengths `(2.5,7.5)`.
   - `b=−3`: `(x,y)=(6,−4.5)`, lengths `(7.5,2.5)`.

   All satisfy the length constraint, positive rises and the global bound. The triangle-inequality proof squares nonnegative quantities and keeps both signs through `|b−2y|≤D`; it does not assume arbitrary allowed positions have positive `b−2y`. The equality boundary `L=AB` and impossible case `L<AB` are treated separately. The unequal-length wording in P024 has a legitimate reading as explaining unequal support heights; the admitted level-support example in P044 explicitly has equal lengths.

4. Ellipse reflection, P029–P031. The argument applies to a nondegenerate ellipse and unit radial vectors. The summed normal cannot vanish because opposite radial vectors would put the point between the foci with distance sum `AB<L`. Equal cosines compare ordinary angles to the same normal; propagation directions and inward-facing ray segments are explicitly distinguished. No universal vertical-normal claim remains.

No failure confirmed in D012.

Limits

This reviewer read complete frozen teaching text and identity metadata. Original lecture PDFs, figure image pixels, destination renderings, the full student baseline and original SASIS reports were not reviewed. Earlier review-report bodies and future teaching were not opened. Identity retrieval did expose brief historical repair/status summaries inside freeze/inventory metadata, including D010’s author-check field; those summaries were not used as mathematical evidence. This review therefore makes no blindness or technical-isolation claim.

All counterexample checks and warrants above were derived from the frozen teaching’s declared models and equations. No GitHub edits, shell commands, Windows operations, automations or new teaching generation occurred.