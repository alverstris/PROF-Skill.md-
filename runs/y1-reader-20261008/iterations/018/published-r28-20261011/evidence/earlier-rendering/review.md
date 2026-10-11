# D001–D017 affected-rendering audit

Verdict: five accepted cases require a targeted current destination check for the demonstrated strict-comparison failure family: D007, D008, D012, D013, and D015. Their 25 display expressions contain 43 literal comparison characters. All 25 survive their preserved server-rendered GitHub payloads, but those cases' closure records explicitly leave client rendering unobserved. This audit therefore establishes a verification dependency, not current visual damage. It does not mark those cases reaccepted or silently change their queue status.

The other twelve accepted cases have none of the three specified feature families in their accepted Markdown. No accepted D001–D017 constituent contains `\operatorname` or a fenced math block inside `<details>`. No accepted inline expression contains a literal strict-comparison character. Their existing acceptance is not reopened by those absent features. This is narrowly scoped absence evidence, not a new whole-document quality verdict.

## Identity and read-only scope

Pinned canonical commit: `f8f76d0775051896326fb400ec5782bf1d954971`. All canonical reads used `git show` or `git ls-tree` on that exact object in `/workspace/scratch/f9c0b7fc7e76/prof-iteration`. The worktree HEAD was observed to be older (`5699ffff98bdf6cc529338fc3245670f976258c8`) and was not used as content authority. No checkout, reset, index mutation, commit, push, or browser operation was performed.

The incoming queue identifies 17 closed cases. Each accepted teaching path was reconciled against its actual closure, final queue digest where supplied, and freeze manifest for multi-file generations. In particular, D016's original r22/r23 closure is historical and reopened; the current accepted object is fresh-r26b under published r26, closed on 2026-10-11. D017 is its complete first r27 generation. Failed, preliminary, and superseded teaching artifacts were excluded.

The audit covers all 17 cases, all 21 accepted Markdown constituents, and all 4,968 extracted math expressions. `math-feature-inventory.json` contains every exact path, full SHA256, byte count, expression payload, line range, delimiter kind, and details-container depth. Every accepted source digest matches its closure/freeze identity. The extraction counts agree with the existing case evidence. The purpose-built delimiter parser is an inventory tool, not a substitute for GitHub's parser or live MathML.

An independent delegated evidence reviewer established and checked D001–D009 acceptance identities and saved destination payloads. I inspected that complete report, independently inventoried all 17 canonical teaching sets, and inspected D010–D017 closure/destination records. Detailed earlier-case evidence remains in `d001-d009-evidence.md` and its JSON; D012/D013/D015 raw archive checks remain in `saved-destination-target-checks.json`.

## Exact accepted Markdown coverage

Paths are relative to `runs/y1-reader-20261008/` in the pinned commit. Full hashes also appear in the machine inventory.

| Case | Accepted Markdown | SHA256 |
| --- | --- | --- |
| D001 | `iterations/001/teaching-v4.md` | `402485baa2767af9625146721e356f92bad76e4cfb738e5729c6c8b94ea79401` |
| D002 | `iterations/002/teaching-v1.md` | `8139080278edb96287576629e7d80933b380c1b82af60d3ede888d500cb68a3a` |
| D003 | `iterations/003/teaching-v1.md` | `cd7426a9b70d0ac41aa3ca0418db8c89c391b67304016a7ad38f8379fe98b5a8` |
| D004 | `iterations/004/teaching-v1.md` | `5adb3e95c2fa47c94b4c665d85dc2fe669e2c0086dbc2ebc194cd59720d5d8ad` |
| D005 | `iterations/005/teaching-v2.md` | `4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6` |
| D006 | `iterations/006/regenerated-r13-candidate1/teaching-v3.md` | `311afdef083a4468f18bcdd11a68975d2e6622661e0be3405a5c9f58b3f3a813` |
| D007 | `iterations/007/revised-v3/teaching-v3.md` | `6dc2823d9f931c1baaa6eb4ce5076ed2aef1859ba29255d5503eed627824ae54` |
| D008 | `iterations/008/revised-r15-v2/teaching-r15-v2.md` | `b6e93b986e2a77763c556a4b5fc5cb42f43269742d0af9bd06021d7aa3ad7668` |
| D009 | `iterations/009/resumption-20261009/author/teaching-r15-recovery-v3.md` | `5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244` |
| D010 | `iterations/010/current-r16/author/teaching-v2.md` | `192609d9d62cc50be534df77b5e5700c6eb7c4a9c32e37c832be6b1ab133742c` |
| D011 | `iterations/011/current-r17/author/teaching-v3.md` | `bcb390a295a8cce423b8ebfb9d292c45f7e6be3e37b9fbed1e33c6f60153f6fe` |
| D012 | `iterations/012/current-r18/author/teaching-v2.md` | `04355b5ac132bfdaecf6a165cf332d0e04a0ff29bd59b53e03d6c801c9838d59` |
| D013 | `iterations/013/current-r19/author/learner-v2.md` | `d17f77d36f7c30db9777230a85decb363a1fb967bb5c51d60cb5af4cd7b078c0` |
| D014 | `iterations/014/current-r20/author/teaching-v2.md` | `caf74a9a150f61d2531e8b2768abb1448fb7d5304818a9e1fcc73d02bead826b` |
| D015 | `iterations/015/current-r21/author/v2/teaching.md` | `9ff76d7dde73d2270b511421f428e5e3324176bc1666728ea013ec8f0512c4b4` |
| D015 | `iterations/015/current-r21/author/v2/hints.md` | `19bf8adb1b6c71a3fdfa65588612e90e8c2431917807c78d7db3ab952fa4f1b5` |
| D015 | `iterations/015/current-r21/author/v2/solutions.md` | `9f6a2b4117df5902a1d964de411830e6af4e61862d6ef80d5cc38991be766855` |
| D016 | `iterations/016/published-r26-20261010/fresh-r26b/teaching/lesson.md` | `48b85e7b62abb2ca9794fa712b24a87124d400e5818a5f483b2a8fd4320eb564` |
| D016 | `iterations/016/published-r26-20261010/fresh-r26b/teaching/hints.md` | `f8db498eb437546f39916714a35b7a1217dba1d6407d94bde33ed6d2c5ed6014` |
| D016 | `iterations/016/published-r26-20261010/fresh-r26b/teaching/solutions.md` | `5a616e257b6c83bce341e5332b036ab92b23f4430b2308b09ac74123b6d57c9a` |
| D017 | `iterations/017/published-r27-20261011/output/teaching.md` | `0317f26777f5285616be96713d79e1731818fea76d40954f3e21be2c6dbcb7b5` |

## Targeted findings

| Case | Source locations and family | Existing exact destination evidence | Present disposition |
| --- | --- | --- | --- |
| D007 | Fenced displays beginning at 179, 293, 322, 548. Two inverse-trigonometric domains `-1<x<1`, and two positive-domain `x>0` statements. Six literal operators. | Independently reparsed saved `render-evidence/v3/github-page.html`: all 371 ordered math payloads match; targeted display indices 122, 184, 209, 331 preserve exact contents outside details. | Current client-rendered comparisons unverified; targeted live check needed. |
| D008 | Dollar displays at 71, 147, 196: `x>-1`, `x>-1`, and `0<=v<c`. Three literal operators. | Saved `render-evidence/r15-v2/github-article.html`, all 305 ordered payloads exact; targets 73, 153, 195. | Current client-rendered comparisons unverified; targeted live check needed. |
| D012 | Dollar displays at 83 and 388: root-bracketing comparisons to 3 and positivity of `f(-3/2)`. Three literal operators. | `current-r18/destination-v2-final.zip`, `destination-v2/github-article.html`, 309 math-renderer elements; both exact target payloads independently recovered after one HTML entity parse. Identity record binds accepted SHA and immutable commit `12f468d985cbc1cb462e41948f0f017a161a2099`. | Current client-rendered comparisons unverified; targeted live check needed. |
| D013 | Dollar displays at 91, 123, 131, 155, 159, 163, 173, 175, 205, 211, 297, 303, 314, 318. MVT interior-point conditions, exponential/remainder signs, derivative bounds, and logarithm inequalities. Twenty-seven literal operators. | `current-r19/destination-v2-complete-evidence.zip`, `destination-v2/github-article.html`, 214 math-renderer elements; all 14 target payloads independently recovered intact. Identity binds accepted SHA and immutable commit `ea627ac47e24cd309a3e7b75a4ecfd070e54a3b5`. | Current client-rendered comparisons unverified; targeted live check needed. |
| D015 | `solutions.md` fenced displays at 29 and 78: `-pi/2 < x^2/2 < pi/2` and `-sqrt(6)<x<sqrt(6)`. Four literal operators. | `current-r21/destination-v2-complete.zip`, `solutions/github-article.html`, 116 solution math-renderer elements; both exact target payloads preserved outside details. Archive identity binds the accepted solution path and SHA. | Current client-rendered comparisons unverified; targeted live check needed. |

All literal comparison-bearing expressions occur in displays, not inline math. Six are fenced displays (D007 and D015), and nineteen are dollar displays (D008, D012, D013). The precise payloads and source lines in the machine inventory remove the need to rereview unrelated expressions.

D001–D006, D009–D011, D014, D016, and D017 are unaffected by these three specific feature triggers because none occurs in their complete accepted mathematical source. Existing destination records were inspected for those exact accepted revisions: D001–D009 delegated retained payload checks; D010 `current-r16/root-destination-v2-disposition.md`; D011 `current-r17/root-destination-v3-disposition.md`; D014 `current-r20/root-destination-v2-disposition.md`; current D016 `fresh-r26b/closure-20261011/final-state/review/final-acceptance-20261011.md`; D017 `published-r27-20261011/evidence/root/destination/final-destination-disposition.md`.

D001–D015 retained reviews deliberately distinguish server preservation and secondary previews from unobserved live client execution. D016 and D017 have separate complete live MathML/visual/navigation evidence bound to their current generations. Neither those newer successes nor a static payload pass retroactively supplies a missing live observation for the five affected older cases.

## Required follow-up and limits

Root, the sole browser owner, has been given the exact five paths and expression inventories. The highest-priority matching family is D007/D015 fenced displays; dollar-display cases must also be checked because the demonstrated risk is mathematical content preservation after client processing, not merely source delimiter spelling. Capture the actual mathematical operands/operators/grouping and the visible condition for each affected expression at its accepted immutable revision.

- If a targeted condition is truncated or rejected, record the concrete rendered result and lost meaning; reopen that case's affected rendering acceptance and apply the active PROF-only repair/fresh-generation procedure. Preserve original teaching and historical closure evidence.
- If each affected expression is preserved live, record those observations as a narrow dependency revalidation. Do not call this fresh generation or an improvement in the old teaching.
- Until that evidence exists, keep the affected destination gate unverified rather than converting syntax presence into a false material-failure finding or static payload presence into a live pass.

The source inventory and retained destination audit are complete. Current live checks are deliberately pending with root; this report does not claim current browser damage, perform queue mutation, invalidate unrelated mathematics/SASIS evidence, or broaden into an unrestricted review of all previous material.
