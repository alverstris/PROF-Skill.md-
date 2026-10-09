D010 closure-publication correction

The final teaching/evidence and metadata-only r17 publication fcc989c6bdbbb495bbaf60bca761b04780fb8e45 remains byte-verified. The subsequent closure commit dd2fbd33e7492e24b44a78b862c4cc3d543fbd11 contained a corrupted queue.json transfer, discovered immediately in the fresh D011 checkout. The prior tree readback checked uploaded blob identity, but did not check that one uploaded blob against intended local source bytes; its all-five-source-equality implication was incorrect. Every other closure path was compared to intended source bytes and matches.

Repair3033debafa1f712fca1b8f89efaee3490c60366e restores the exact intended304873-byte UTF-8 JSON, SHA2565202b47919d20d09bcb12f3a42969fdaa1baf4b69151bd1218359e3dd238d1e9. Root fetched the actual commit through git, compared raw queue bytes to original intended bytes, parsed the JSON and verified all147unique original IDs,10closed,76eligible/71excluded,66remaining. Actual published SKILL is byte-identical to the fully reloaded r17. No teaching, reader input, source or skill instruction was affected.

Original faulty commit and exact corrupted bytes are preserved; detailed cause and readback are in ../011/current-r17/queue-publication-incident.json and queue-repair-readback.json. Future publication reads check expected base64 length and local Git blob SHA before branch mutation, then compare the actual published tree to those local identities. An API blob hash alone is not a source-byte check.

D010 is closed after this repaired canonical metadata readback. D011 continues under the same actual r17 bytes. No new skill rule, rerun of unchanged teaching or human learning claim follows from this transport correction.
