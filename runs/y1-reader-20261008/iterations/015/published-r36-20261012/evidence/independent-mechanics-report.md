# D015 r36 final independent reader mechanics audit

PASS for mechanical integrity, with explicit authentication and semantic limits. All 2,356 independent checks passed. The original reader report and reconstruction match their final seal; all frozen teaching files, baseline, route, route seal and provided launcher remain exact. This is not a scientific or reader-comprehension verdict.

| Raw evidence checked | Verified result |
|---|---|
| Chronological ledger | 384 events, 36 successful calls/stages, exact canonical serialization and full SHA256 chain |
| Actual baseline access/output | All 247,840 bytes in 11 contiguous initial slices, before teaching |
| Actual teaching text access/output | All 28,990 bytes in 19 contiguous slices |
| Actual figure access/results | All 3 original result objects decode to exact frozen PNGs, 157,992 bytes total |
| Receipt dependency | All 3 fixed receipt stages follow dispatch and recorded actual-view completion; cursor held until receipt |
| Retained exec results | All 36 exact output objects accounted for; 30 text outputs equal routed bytes without truncation |
| Prefix retention | Initial empty snapshot plus all 36 completed-call boundaries: 37 exact final-ledger prefixes |
| Failed launcher calls / revisits | 0 / 0 |
| Final state | All 33 retrieval steps completed, all 3 receipts accepted, no pending figure |

No omitted, reordered or bypassed stage was found in the retained route. Every actual open/read/close/access event was matched to its authorized path, exact byte range and hash; access verification precedes output. Both output-begin and output-complete digests match the retained output bytes. All 107 audit inputs were unchanged when reread at the end of this audit.

| Figure | Retained result SHA256 | Exact image SHA256 |
|---|---|---|
| F01 | 32c30294dc0c15b7aa2421233db1b0637fdb2b7aa50bddb56ea74964ea4e31fa | 48f747d12b85ffb468362594ddb0f9a60329271ce770066797f98aa977243951 |
| F02 | 741586bc1fd7e8a0482673788092969cce7888f5e8639a8abea78914885fa4c1 | cd0646d133e98963b96ea10f96ade2528c59fd1a2215cea0fad448c28abd0c61 |
| F03 | bab624bd73b298f425e6cb3fd8869a48322911dbcf00ba40166a873ede730ac4 | 446fd2aff1200e81384520f218e0f371e04d1edd92a75dc0f7bdb6142491b221 |

For every image, the retained detail=original wrapper has a complete data URL. Decoding produces the exact source PNG bytes; URL length/hash and returned MIME label match the receipt. Each invocation path, fixed figure identity, completion timestamp, accepted receipt bytes and receipt-helper returned digest are consistent. No new image view was performed. The helper only converts retained result metadata to a receipt; it does not invoke the image tool or authenticate provenance.

The view IDs are explicitly local correlation IDs because no provider IDs were exposed. Launcher call UUIDs and exec chunk IDs are recorded in verified-ids.json with their actual provenance. Retained locally generated ledgers, snapshots and result objects are not cryptographically authenticated platform transcripts. Their byte and chronology agreement does not prove visual attention, semantic comprehension, absence of pretraining, technical isolation, or absence of every possible access outside the retained evidence.

The original reconstruction discloses a failed post-reading apply_patch attempt using Delete File and Add File for the same reconstruction path. It then records separate sequential Delete/Add operations to arrange that reader-authored record. The displayed error is explicitly a transcription; no original structured failed-patch result is available and none has been synthesized. This is distinct from the 36 successful launcher calls. This audit proves the final sealed report/reconstruction identities and unchanged source/ledger bytes; it does not independently authenticate the absent failed-patch invocation or its broader effects.

The earlier unexplained synthetic preflight ledger-shortening anomaly remains preserved and unresolved. No shortening appears in this actual run: every saved checkpoint matches its exact call-boundary prefix in the final ledger. The current result does not retroactively establish the cause of the synthetic anomaly.

Chronology is explicit: independent route admission occurred after reader dispatch. This final audit started after the original final report/reconstruction seal. No reader input, raw result, report, reconstruction, ledger, receipt or frozen source was altered; no browser, launcher, fixture or view_image operation was repeated.

| Identity | SHA256 |
|---|---|
| Final ledger (164,535 bytes) | 1d6ed39855efdca74381115f064aa7f0f2a0ae26b4011da7033d86f6bb51c710 |
| Final chain tail | 5b0b2975eadda3289266fd1b87af2679abc3b335a50b1f9cf50fafd9cff308f8 |
| Original report (22,442 bytes) | 848e53c923a129e13c281e99194f58454017a22d6fc0eb3bebab48a74880b279 |
| Original reconstruction (14,319 bytes) | d2384fa3260d6075af981bec132d6ec47aeedaef725f1eb4bd552284a93103a8 |
| Original final seal | ba19fbaeb06e4c49dc496622f667f90c6daed053d4ddd3e215abf47af1407fce |

The full verification JSON records every check, exact stage and returned-output identity, image bindings, coverage and checkpoint hashes. input-manifest.json binds all 107 actual inputs read; verified-ids.json lists all call/result identities. audit_final_reader.py is the independent read-only checker.
