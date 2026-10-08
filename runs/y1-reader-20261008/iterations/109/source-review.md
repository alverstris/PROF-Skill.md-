# D109 — original source technical preparation

Completed 2026-10-08. **104/104 assigned page occurrences across 4 original PDFs** were freshly inspected in full-page renders and read, with equations, diagrams, labels and PRS indications checked. This is source-only evidence, not an authored teaching route, student evaluation or iteration closure. Originals and cache remain untouched.

## Exact selection and boundaries

D109 is `mit-8-02t-spring2005-S07`, studio7, original order109, active order38: *Hour 1 Conductors and Insulators Experiment 2: Electrostatic Force Hour 2 Capacitors*. Mapping comes from the D109 entry of `runs/y1-reader-20261008/readability-selection.json` and the matching row of `readability-audit/teal.json`, read selectively. The official index row assigns Chapter4 §§4.3–4.4 and all Chapter5, the presentation and the PRS. No adjacent studio or additional lab handout was assumed.

Official index: https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2005/pages/lecture-notes/ . Asset URL prefix: `https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2005/`.

| Alias | Exact asset | Required portion | Original SHA256 |
|---|---|---|---|
| C4 | `16ff64d64187374a61c28a1f9f16f348_chapte4gauss_law.pdf` | PDF15–24, printed14–23: heading4.3 lower15 to before heading4.5 on24, including Eq4.4.8 | `877dbeee27c807d23bdd7da48755aea8b112da3001d72d9154a013c8b0ddc822` |
| C5 | `99407b81a217613e8ddec21dc3da07de_chap5capacitance.pdf` | Entire PDF1–46, printed0–45 | `370eeb172f37e2eb450c245eb9972e00b83a0fa241b457d17e288d2af96de522` |
| P | `e57a18fe3bcded8e09661fe938ec81c5_presentati_w03d1.pdf` | Entire PDF1–40 | `404696179c674f15927c3811e6d5f602316e9adead9bd5e028eabd0a00d71cda` |
| Q | `61ec5fe99ae5ea5b384247fe47aaa16e_prs_w03d1.pdf` | Entire PDF1–8 | `87905c9cfac0dea65a0d3253158e707e6948d2234827bd469fd70616754c6dff` |

Source-map.json records the byte sizes (905176,1338251,1003307,167675), whole-PDF page counts (39,46,40,8), source paths, boundaries and every credited render/hash. All four original hashes were recomputed and matched. P footers are P07-number except PDF18–19, which show “P07 -” without a numeral; those pages must be cited by PDF position. PRS pages carry PRS07 but no individual printed page numbers.

The self-contained companion `shared-reading-review.md` is an integral part of this packet: it records complete C4/C5 page/figure/equation coverage, 11 grouped confirmed source findings, conditional derivations, all solved/given-answer checks and reviewer-only deductions for unworked problems. The identical shared readings were freshly reviewed once for D109 and D110 together; this is not a claim of two separate visual passes.

## Presentation coverage and technical checks

All P PDF1–40 opened in batches1–10,11–20,21–30,31–40. No contact-sheet substitution. All Q PDF1–8 opened. Source text was extracted directly from original PDFs to support equation/label checking; the visible source took precedence over extraction order.

| P PDF / slide locator | Freshly inspected content and assessment |
|---|---|
| 1–4 / P07-1–4 | Session outline, Gauss recap with closed-box/nested-surface diagrams and symmetry table, conductor transition. Gauss's law is general; extracting E simply from flux requires the stated symmetry. |
| 5–6 / P07-5–6 | Conductor/insulator definitions, external and induced field diagrams. E=0 and equipotential mean electrostatic equilibrium inside conducting material, not every current-carrying conductor or a charged cavity. An insulator can polarize without mobile conduction charge. |
| 7–12 / P07-7–12 | Equipotential transition, 3D topographic surface/projected contours with x,y,z,C,P(x,y) labels, level curves C1–C3, PRS prompt and uniform/point/dipole equipotential diagrams. E=−gradV is perpendicular to regular level surfaces when E≠0; it points toward lowerV. Zero electrical work along an equipotential does not assert zero work by all possible mechanical forces. |
| 13–14 / P07-13–14 | Four conductor properties, shaped conductor/arrows A,B and excess-charge migration illustration. Signed outward En=σ/ε0; magnitude requires |σ|. “Anywhere inside” must mean free excess charge within conducting material, not a separate cavity charge. Equilibrium minimizes the appropriate energy subject to constraints; “as far apart as possible” is qualitative. |
| 15–17 / P07-15–17 | Electrostatic-force apparatus photo, static sphere/plate field visualization and experiment transition. The picture/prose identify the role; no unprovided measurements, lab steps or animation outcome are inferred. |
| 18–21 / PDF position | Capacitor transition, two-conductor +Q/−Q and C=Q/|ΔV|, parallel-plate diagram, charged-particle simulation still. Q is a positive magnitude; C unitsC/V=F. Field confinement and uniformity neglect finite-edge fringing. A transient particle frame need not itself show final equilibrium. |
| 22–24 / P07-22–24 | Pillbox, single-sheet superposition arrows/signs, gap potential integration and C=ε0A/d. Pillbox enclosed charge comes from one plate while E is the total field of both; no source is omitted. Superposition scalar signs use downward-positive in the illustrated gap. ΔVtop−bottom=Ed>0 is consistent with upward integration opposite downwardE. |
| 25–29 / P07-25–29 | Big-capacitance demonstration prompt, concentric spherical capacitor geometry, E regions, potential/C derivation and Earth/self-capacitance estimate, 1F12V charge. Integrating a→b gives Vb−Va=kQ(1/b−1/a)<0. C=4πε0/(1/a−1/b), limitb→∞ gives4πε0a; a=6.4×10^6m yields0.712mF, matching0.7mF. This is an ideal isolated sphere, not a modeled Earth–ionosphere capacitor. 1F×12V=12C. |
| 30–32 / P07-30–32 | Dimension-change PRS/demonstration prompts and energy transition. Results depend on isolated versus battery-connected condition. |
| 33–37 / P07-33–37 | Charge-transfer stairs and +q/−q diagram, dW=(q/C)dq, integration and energy formulas, uniform field energy density. Correct for quasistatic charging, fixed geometry and linearC: U=Q²/(2C)=Q|ΔV|/2=C|ΔV|²/2; volumeAd givesu=ε0E²/2. |
| 38–40 / P07-38–40 | Numerical energy examples, PRS prompt, dissectible-capacitor demonstration title. 1F12V gives72J;100µF3kV gives450J. The final title alone provides no experiment result; none is invented. |

## PRS answers checked independently

| Question PDF / answer PDF | Source indication | Independent check and limits |
|---|---|---|
| Q1 / Q2 | (1) North | At the red dot, the drawn contour is nearly horizontal and the enclosing summit is southward, so the locally downhill normal is North among the eight offered compass directions. The source's aside about “from the peak” going NW is only a coarse map remark: at an exactly smooth summit grad h=0, so no unique first-order descent follows. The pictured red-dot choice remains supported. |
| Q3 / Q4 | (4) V increases, Q same | Battery disconnected, d→D>d: Q fixed, C∝1/d falls, V=Qd/(ε0A) rises; ideal gapE remains fixed. No leakage/fringing assumed. |
| Q5 / Q6 | (9) V same, Q decreases | Battery connected: idealV fixed, C decreases, Q=CV decreases, E=V/d decreases. The selected answer is correct. |
| Q7 / Q8 | (2) U increases | Disconnected fixedQ: U=Q²d/(2ε0A); positive mechanical separation work raises stored energy. |

**Confirmed packet-specific source error:** Q6's first explanatory sentence says “With no battery connected” while claiming the battery holds potential constant; Q5 explicitly says the battery remains connected. Delete “no” or state “with the battery connected.” The answer9 and subsequent field/charge reasoning correspond to Q5's connected condition. This is a prose contradiction, not an incorrect key.

## Findings and limits

There are **12 grouped confirmed source findings**: this PRS contradiction plus the 11 shared-reading findings, including editorial references, the electric/magnetic polarization typo and the inappropriate literal Pauli-force/never-polarizes generalizations. Conditional geometry, dielectric-response, energy-accounting and simulation claims are separately identified in the companion review; they are not disguised as incorrect algebra or cleaned up without provenance.

No required scientific symbol or diagram role remains unreadable. The C5 miniature simulator numeric controls remain unsuitable for numeric extraction. Static demonstrations/animations do not demonstrate live behavior. The shared reading's cooling question has a conditional material-dependent answer, sphere/plate density wording lacks a quantitative model, trap population outcomes were not executed, the historical quotation attribution was not checked, and the100MV/m accelerator maximum remains unsupported by the targeted primary lookup. All such limits remain explicit. No teaching route, student baseline, reader report, repository change or iteration closure was produced.
