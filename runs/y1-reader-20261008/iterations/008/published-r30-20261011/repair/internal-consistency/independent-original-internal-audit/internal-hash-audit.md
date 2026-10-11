# Admitted r31 internal hash audit

All 36 admitted package files were scanned and rehashed unchanged against the prior preparation manifest. All 65 SHA-256 declarations were accounted for: 34 target occurrences name bundled files (32 match, 2 mismatch); 31 describe external or historical research PDFs, unbundled Markdown companions, or the earlier release ZIP. No external resource was accessed. No additional mismatch was found.

The two failures are in references/sasis/profile-manifest.json:

- Entry /control_file_hashes/student-role.txt
  - Target: references/sasis/student-role.txt
  - Expected: 3dd6e341ca5e22d24d54a3377569e52062ef0f6cfbc54b169fc8d8ccd6de4469
  - Actual: 6d98143c1de5b38bcfb7d350c9110988dae4bcf4e15a2cff925565d9cdef55c4
- Entry /control_file_hashes/student-testing-contract.txt
  - Target: references/sasis/student-testing-contract.txt
  - Expected: d87ddbf9593386b39a6fe7a5bf6a27548fb12bbf528802af4421212cc05b46ae
  - Actual: 70e49900903a167c058c8cdd056b277ffacff8a933c15358fb9aa747c000ec38

The full ledger preserves every exact declaring file, entry, expected hash, included target and actual hash when applicable. External references are not treated as claims that those absent files are bundled. The parent-supplied publication pin remains 7cf8e4745680b2042efae1db73cb2e33665549c9; no independent remote verification is claimed.

All earlier original/package seals remain unchanged. Awaiting corrected pin/admission before any prompt or teaching access.
