# Closed-session navigation dependency inventory — original report

This is a read-only feature inventory, not a defect verdict. No browser was used. No teaching, package, queue, Git index, checkout, branch, or history was modified. The coordinator and root own any destination test and acceptance decision.

Canonical repository: `alverstris/PROF-Skill.md-`; exact main commit: `663311ba27f25206ed868ce9bbfd016447528ef3`. The local operational queue is byte-identical to `runs/y1-reader-20261008/queue.json` at that commit: SHA256 `ca6ab019d6e81f042322cd9975efbf0e9cfe908f772226dc03670fc8f05e3842`, Git blob `9420cf724c0d0b8db4f2ce7e7e010fe141a0b50d`. Its status fields select exactly 14 currently closed sessions; historical counts inside preserved closure prose do not override the current queue.

## Result

The 14 accepted sessions contain 18 current Markdown learner constituents. Only D007 and D016 have cross-file relative links carrying fragments: 30 routes in D007 and 25 in D016. Every one of those 55 target fragments exists exactly once in its accepted target file. There are no repeated authored fragment IDs between current sibling teaching files, and no target fragment also defined in its source sibling. Thus this inventory identifies **no exact same-fragment sibling dependency candidate** among the 14 closed sessions. D007 and D016 are the only candidates for a broader cross-file navigation check. Neither statement establishes destination behavior or a defect.

D007 uses prompt fragments `p1`–`p6` in lesson.md, hint fragments `h1`–`h6` in hints.md, and solution fragments `s1`–`s6` in solutions.md. D016 uses `p1`–`p5`, `h1`–`h5`, and `s1`–`s5` in the corresponding files. Each listed route changes the fragment relative to its nearest authored source anchor. A user may manually arrive under another URL fragment; this source inventory does not claim to observe the current address or SPA execution.

The remaining closed sessions—D001, D002, D003, D004, D005, D006, D009, D010, D011, D012, D014 and D017—have no cross-file relative anchor route in their accepted Markdown. D008 is not closed and is outside this inventory. Historical superseded teachings and D016 final-state duplicate copies are excluded; D016 uses its original six-constituent freeze identity.

## Accepted identities

All paths below are complete repository paths. Every listed file was read from its exact frozen commit and byte-compared against canonical main; every comparison passed. SHA256 values were calculated from the actual Git blob bytes, not copied from review prose. All queue-provided primary-document hashes matched. Figures are accepted constituents but their binaries were not inspected because this task maps authored Markdown sibling routes.

| Session | Frozen teaching commit | Accepted Markdown repository path | SHA256 | Git blob |
| --- | --- | --- | --- | --- |
| D001 | `0716ea92991d7f9fe2814e137bcc830d91a27511` | `runs/y1-reader-20261008/iterations/001/teaching-v4.md` | `402485baa2767af9625146721e356f92bad76e4cfb738e5729c6c8b94ea79401` | `b5c7ccb11e2d9f2f05e5b8f2c7830d62f26b1d66` |
| D002 | `f1c0e91c24e9140049d50c7ca965f41e36f3e1a2` | `runs/y1-reader-20261008/iterations/002/teaching-v1.md` | `8139080278edb96287576629e7d80933b380c1b82af60d3ede888d500cb68a3a` | `40377331cacc1b661c5fbb53272a1334a171c402` |
| D003 | `4cbf83f2dc2859d5123fc01a0c311a268d580483` | `runs/y1-reader-20261008/iterations/003/teaching-v1.md` | `cd7426a9b70d0ac41aa3ca0418db8c89c391b67304016a7ad38f8379fe98b5a8` | `0f3041ba650c0b04321db6b1f6ec0c607fa6f163` |
| D004 | `197b57555834d36952e948d4100d2f835c86b20c` | `runs/y1-reader-20261008/iterations/004/teaching-v1.md` | `5adb3e95c2fa47c94b4c665d85dc2fe669e2c0086dbc2ebc194cd59720d5d8ad` | `b9128c0ba3110e14cd30ceca8d2c87b07893307c` |
| D005 | `32c553f279ac1e5771ff05b78a9951cbff3fee38` | `runs/y1-reader-20261008/iterations/005/teaching-v2.md` | `4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6` | `d8c9a67266e79fec03b069fa3193354882fc3f8b` |
| D006 | `28825d27b93baef43a5751eacecac81fa46841bc` | `runs/y1-reader-20261008/iterations/006/regenerated-r13-candidate1/teaching-v3.md` | `311afdef083a4468f18bcdd11a68975d2e6622661e0be3405a5c9f58b3f3a813` | `568fd03397f022bf2725a22476d155d470d84788` |
| D007 | `4765d39aa399a0a1ff09223cae21b15ce6c7f720` | `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/lesson.md` | `fd7a5dc52b8c143c8ba392b494ac879ad2722b0231dd21b3dadb50d0eedd988d` | `71c1cc93e58f03a1d2f84519398a062190a965db` |
| D007 | `4765d39aa399a0a1ff09223cae21b15ce6c7f720` | `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/hints.md` | `d80b7cad63ec6b575b0d567dd4f4213ec4ea77b1ff61525f479859651a659a0c` | `bee957570b6b869f703fd6a98f2429d210722520` |
| D007 | `4765d39aa399a0a1ff09223cae21b15ce6c7f720` | `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/solutions.md` | `3716815362b8d3c4240fffeb8cc5e95dd524939a99c9d6c0b9a189976ae035de` | `5b55ac240e578efe14e81dc71c3122e2815dd00a` |
| D009 | `9840e70de6aa7d2c718b60dd13ace7e6f795a50e` | `runs/y1-reader-20261008/iterations/009/resumption-20261009/author/teaching-r15-recovery-v3.md` | `5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244` | `12692e5b06f7f05fd490dc6a7058a13eb96aa976` |
| D010 | `629feb501ffd69447b70011d852ece5bf8a04641` | `runs/y1-reader-20261008/iterations/010/current-r16/author/teaching-v2.md` | `192609d9d62cc50be534df77b5e5700c6eb7c4a9c32e37c832be6b1ab133742c` | `fa98f0f7cee0a38c41525fec67370cf16d1fd4b6` |
| D011 | `d493bae7f5f680e33f2fa891c5d0310bf43e5d23` | `runs/y1-reader-20261008/iterations/011/current-r17/author/teaching-v3.md` | `bcb390a295a8cce423b8ebfb9d292c45f7e6be3e37b9fbed1e33c6f60153f6fe` | `b8b89dd9a0bc6aa3f24c90013cba7d96c93f3364` |
| D012 | `12f468d985cbc1cb462e41948f0f017a161a2099` | `runs/y1-reader-20261008/iterations/012/current-r18/author/teaching-v2.md` | `04355b5ac132bfdaecf6a165cf332d0e04a0ff29bd59b53e03d6c801c9838d59` | `9013266253204c229f8fd6db4d968ff74a22cd0a` |
| D014 | `40151288dfc73314e6efb7ef74794dfa75a0a5ee` | `runs/y1-reader-20261008/iterations/014/current-r20/author/teaching-v2.md` | `caf74a9a150f61d2531e8b2768abb1448fb7d5304818a9e1fcc73d02bead826b` | `edb1a433605a708ec243a47fb0c516723c948d0d` |
| D016 | `51a78beccef858072b1da8d057ef3dff09878409` | `runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b/teaching/lesson.md` | `48b85e7b62abb2ca9794fa712b24a87124d400e5818a5f483b2a8fd4320eb564` | `fd0f0020e82ccb74c8df1597055e66440053f822` |
| D016 | `51a78beccef858072b1da8d057ef3dff09878409` | `runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b/teaching/hints.md` | `f8db498eb437546f39916714a35b7a1217dba1d6407d94bde33ed6d2c5ed6014` | `2ae9b89f11b358e9c3aa5d54af3c6f200c95e1b5` |
| D016 | `51a78beccef858072b1da8d057ef3dff09878409` | `runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b/teaching/solutions.md` | `5a616e257b6c83bce341e5332b036ab92b23f4430b2308b09ac74123b6d57c9a` | `3ce7deec7d0933460374f7c7d79d30a046b01e28` |
| D017 | `a7b7de5e040882fa605716e3a954ee067d3ce9a6` | `runs/y1-reader-20261008/iterations/017/published-r27-20261011/output/teaching.md` | `0317f26777f5285616be96713d79e1731818fea76d40954f3e21be2c6dbcb7b5` | `bf08e06e2d8cb20bcc5a82b6431a321be3eaa8ac` |

## Exact relative anchor routes

For the following route tables, append each source/target filename to its stated repository directory. This defines the complete source and target path without changing path resolution. The machine-readable inventory repeats the complete paths on every route. “Source anchor” is the nearest preceding authored anchor, not an observed browser URL. Target line is the exact explicit-anchor line in the frozen target file.

### D007

Directory: `runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/`

Frozen commit: `4765d39aa399a0a1ff09223cae21b15ce6c7f720`. 30 routes; no source-target fragment repeats.

| Source file:line | Source anchor | Exact relative href | Target file:line | Target fragment |
| --- | --- | --- | --- | --- |
| `lesson.md:43` | `#p1` | `hints.md#h1` | `hints.md:5` | `#h1` |
| `lesson.md:43` | `#p1` | `solutions.md#s1` | `solutions.md:5` | `#s1` |
| `lesson.md:102` | `#p2` | `hints.md#h2` | `hints.md:11` | `#h2` |
| `lesson.md:102` | `#p2` | `solutions.md#s2` | `solutions.md:22` | `#s2` |
| `lesson.md:136` | `#p3` | `hints.md#h3` | `hints.md:17` | `#h3` |
| `lesson.md:136` | `#p3` | `solutions.md#s3` | `solutions.md:39` | `#s3` |
| `lesson.md:184` | `#p4` | `hints.md#h4` | `hints.md:23` | `#h4` |
| `lesson.md:184` | `#p4` | `solutions.md#s4` | `solutions.md:67` | `#s4` |
| `lesson.md:301` | `#p5` | `hints.md#h5` | `hints.md:29` | `#h5` |
| `lesson.md:301` | `#p5` | `solutions.md#s5` | `solutions.md:90` | `#s5` |
| `lesson.md:335` | `#p6` | `hints.md#h6` | `hints.md:35` | `#h6` |
| `lesson.md:335` | `#p6` | `solutions.md#s6` | `solutions.md:110` | `#s6` |
| `hints.md:9` | `#h1` | `lesson.md#p1` | `lesson.md:41` | `#p1` |
| `hints.md:15` | `#h2` | `lesson.md#p2` | `lesson.md:100` | `#p2` |
| `hints.md:21` | `#h3` | `lesson.md#p3` | `lesson.md:134` | `#p3` |
| `hints.md:27` | `#h4` | `lesson.md#p4` | `lesson.md:182` | `#p4` |
| `hints.md:33` | `#h5` | `lesson.md#p5` | `lesson.md:299` | `#p5` |
| `hints.md:41` | `#h6` | `lesson.md#p6` | `lesson.md:327` | `#p6` |
| `solutions.md:20` | `#s1` | `lesson.md#p1` | `lesson.md:41` | `#p1` |
| `solutions.md:20` | `#s1` | `hints.md#h1` | `hints.md:5` | `#h1` |
| `solutions.md:37` | `#s2` | `lesson.md#p2` | `lesson.md:100` | `#p2` |
| `solutions.md:37` | `#s2` | `hints.md#h2` | `hints.md:11` | `#h2` |
| `solutions.md:65` | `#s3` | `lesson.md#p3` | `lesson.md:134` | `#p3` |
| `solutions.md:65` | `#s3` | `hints.md#h3` | `hints.md:17` | `#h3` |
| `solutions.md:88` | `#s4` | `lesson.md#p4` | `lesson.md:182` | `#p4` |
| `solutions.md:88` | `#s4` | `hints.md#h4` | `hints.md:23` | `#h4` |
| `solutions.md:108` | `#s5` | `lesson.md#p5` | `lesson.md:299` | `#p5` |
| `solutions.md:108` | `#s5` | `hints.md#h5` | `hints.md:29` | `#h5` |
| `solutions.md:147` | `#s6` | `lesson.md#p6` | `lesson.md:327` | `#p6` |
| `solutions.md:147` | `#s6` | `hints.md#h6` | `hints.md:35` | `#h6` |

### D016

Directory: `runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b/teaching/`

Frozen commit: `51a78beccef858072b1da8d057ef3dff09878409`. 25 routes; no source-target fragment repeats.

| Source file:line | Source anchor | Exact relative href | Target file:line | Target fragment |
| --- | --- | --- | --- | --- |
| `lesson.md:42` | `#p1` | `hints.md#h1` | `hints.md:5` | `#h1` |
| `lesson.md:42` | `#p1` | `solutions.md#s1` | `solutions.md:5` | `#s1` |
| `lesson.md:194` | `#p2` | `hints.md#h2` | `hints.md:11` | `#h2` |
| `lesson.md:194` | `#p2` | `solutions.md#s2` | `solutions.md:19` | `#s2` |
| `lesson.md:226` | `#p3` | `hints.md#h3` | `hints.md:17` | `#h3` |
| `lesson.md:226` | `#p3` | `solutions.md#s3` | `solutions.md:57` | `#s3` |
| `lesson.md:286` | `#p4` | `hints.md#h4` | `hints.md:23` | `#h4` |
| `lesson.md:286` | `#p4` | `solutions.md#s4` | `solutions.md:94` | `#s4` |
| `lesson.md:292` | `#p5` | `hints.md#h5` | `hints.md:29` | `#h5` |
| `lesson.md:292` | `#p5` | `solutions.md#s5` | `solutions.md:135` | `#s5` |
| `hints.md:9` | `#h1` | `lesson.md#p1` | `lesson.md:38` | `#p1` |
| `hints.md:9` | `#h1` | `solutions.md#s1` | `solutions.md:5` | `#s1` |
| `hints.md:15` | `#h2` | `lesson.md#p2` | `lesson.md:190` | `#p2` |
| `hints.md:15` | `#h2` | `solutions.md#s2` | `solutions.md:19` | `#s2` |
| `hints.md:21` | `#h3` | `lesson.md#p3` | `lesson.md:216` | `#p3` |
| `hints.md:21` | `#h3` | `solutions.md#s3` | `solutions.md:57` | `#s3` |
| `hints.md:27` | `#h4` | `lesson.md#p4` | `lesson.md:282` | `#p4` |
| `hints.md:27` | `#h4` | `solutions.md#s4` | `solutions.md:94` | `#s4` |
| `hints.md:33` | `#h5` | `lesson.md#p5` | `lesson.md:288` | `#p5` |
| `hints.md:33` | `#h5` | `solutions.md#s5` | `solutions.md:135` | `#s5` |
| `solutions.md:17` | `#s1` | `lesson.md#p1` | `lesson.md:38` | `#p1` |
| `solutions.md:55` | `#s2` | `lesson.md#p2` | `lesson.md:190` | `#p2` |
| `solutions.md:92` | `#s3` | `lesson.md#p3` | `lesson.md:216` | `#p3` |
| `solutions.md:133` | `#s4` | `lesson.md#p4` | `lesson.md:282` | `#p4` |
| `solutions.md:170` | `#s5` | `lesson.md#p5` | `lesson.md:288` | `#p5` |

## Extraction and scope checks

The extraction covered inline Markdown links, reference-style links, HTML href attributes, explicit HTML id/name targets, and potential Markdown heading targets. All 265 recorded anchors are explicit HTML targets; no inferred heading fragment is needed here. An independent broad scan of every literal relative `.md#fragment` token exactly matches the extracted cross-file-route multiset in every accepted file. All 55 targets resolve syntactically to one explicit target in the accepted set. No duplicate anchor IDs occur within any accepted file. Unanchored sibling-file links exist in D007 and D016 and are excluded from the fragment-route count because they carry no fragment.

Necessary current closure, acceptance and freeze/readback identity records were read at canonical main. They identify the accepted version and frozen commit; they are not being treated as fresh browser evidence. Each identity record and its SHA256/Git blob is retained in inventory.json. Batch explicit-object reads were used for identity and teaching acquisition; no network browse, repository publication, teaching edit, queue edit, or historical teaching audit was performed.

## Uncertainty and handoff

- Matching source syntax cannot establish GitHub SPA behavior. This report does not confirm or reject root’s separately observed same-fragment behavior in another document.
- The current fragment in an actual address bar depends on entry/navigation history. Nearest source-anchor context records authored structure only.
- Authored IDs are recorded exactly. GitHub DOM prefixing, hash normalization, scroll timing, retained scroll position, loaded content and browser environments require destination checks.
- Exact same-fragment affected IDs in this closed14 inventory: none. Broader cross-file feature IDs: D007, D016. No session is reopened, repaired, or reaccepted by this inventory.
- This task does not evaluate mathematics, pedagogy, complete rendering, learner outcomes or historical acceptance quality. No superseded teaching was read.

Machine-readable companion: `inventory.json`. Reproducible acquisition/extraction script: `build_inventory.py`. All source identities, paths, anchor lines, link labels, hrefs and scope limitations are in the inventory.
