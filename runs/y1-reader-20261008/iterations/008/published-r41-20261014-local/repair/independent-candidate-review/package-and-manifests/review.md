# Independent r41 package and manifest review

**Bounded result: pass.** No complete-package inventory, proposed identity, operative manifest, frozen baseline/provenance, installed-byte or review-seal discrepancy was found. This is preparation review, not production execution, publication, synchronization or acceptance.

The expected and measured `REVIEW-SEAL.json` SHA256 is `7679387d9640b65221c959ec314fdd145da419b72389393662933ddd167e65dc`. All 18 named sealed records matched their exact byte lengths and SHA256, including the candidate inventory record.

## Complete package and current installation

The actual root package was read from Git blobs at pinned commit `2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce`. Its inventory is exactly 36 files: `SKILL.md` and all tracked files under `agents/`, `assets/`, `references/`, and `scripts/`. The root `prof.zip` and historical `runs/` tree are outside this operative inventory, as the actual synchronization text specifies. Every source blob OID was recomputed from its Git object header and exact bytes.

The candidate contains exactly the five documented replacement files and no additional package file. Overlaying them virtually on the pinned package leaves the exact 36-file inventory, with 31 byte-identical source files and five actual changes. The installed `C:/Users/alver/.codex/skills/prof` was recursively enumerated: exactly 36 relative paths, no extra/missing files, no symlinks/junctions, and every file byte-identical to the pinned r40 blob. No stage or installation was created.

The complete path inventory, all source/proposed/installed byte lengths and SHA256 values, and source/proposed Git blob OIDs are in `package-inventory-and-identities.json`. The raw line-ending-sensitive diff is `actual-five-file.diff`; the separately labelled normalized content-review diff does not substitute for that raw evidence.

## Exact changed-file identities

| Path | Proposed bytes | Proposed SHA256 |
|---|---:|---|
| `SKILL.md` | 44237 | `f644289b87bc50247bfaccc00a043e2dcce004e422717cf7604a4cfee0903a5a` |
| `references/sasis.md` | 37113 | `a45af8fc59d050e62e247a81e30760ab4ff2c24ecf223993503a9b5f4c84470b` |
| `references/sasis/profile-manifest.json` | 13436 | `aa564e3e2dfaaeeabfdd1e3c6de2bd65aca1fa1245d521ba62a641e9d74cba31` |
| `references/sasis/student-role.txt` | 7341 | `b43364db24a239b48899fd7df19cd57cd5b68b2808c5ac130138a9feaad197ad` |
| `references/sasis/student-testing-contract.txt` | 9595 | `97cacfa2eebaf29690e24e502a82caea451563ca07e8f883da4ebceb1f0d3123` |

## Manifest and actual file inspection

All 28 operative check records were recomputed from the actual virtual merged package:19 frozen baseline/provenance records, five control records and four subject records. They cover24 distinct paths because the four subject paths already occur among the 19 baseline paths. All saved manifest check rows, expected hashes and measured hashes were independently reproduced exactly; pass flags were not the basis for the result.

All 19 frozen baseline/provenance files and the full file_hashes map are unchanged from pinned r40. Their actual bytes also match the current installation. The subject-file records remain unchanged. The profile has exactly three semantic field changes: `control_file_hashes`, `protocol_revision` and `protocol_update_notes`. All previous notes are preserved in order and exactly one r41 note is appended. The exact five control keys are role, contract, unchanged rewrite guide, `../sasis.md` and `../../SKILL.md`; normalized paths stay within the package.

Actual changed prose and all four named embedded code payloads were inspected. The bootstrap/store proof schemas remain distinct; the repeated call is two lines with only a STEP_ID datum and evaluation/invocation surface. The invoker contains the proof-schema check before adapter evaluation. The metadata template still reconstructs and compares the current canonical envelope. All four uniquely named carrier payloads match both the separate candidate templates and saved extraction byte for byte, and match the actual preflight files after only the four enumerated verifier substitutions. No candidate validator or proof helper was executed.

## Additional byte detail and validator limits

The sealed `SKILL.md` includes 156 CRLF-to-LF conversions. Pinned r40 has 156 CRLF endings and 166 LF characters total; the candidate has zero CRLF and 166 LF characters. After normalization solely for content inspection, its only content change is metadata version r40 to r41. The candidate provided text diff was generated through `read_text()`, which normalizes input newlines and does not display this byte change. All other changed files already used LF. No BOM is present in the five source or proposed files. This detail is disclosed for root review; the actual sealed hashes already bind it.

Inspection of `validate_candidate.py` found three generality gaps: its five-file assertion does not enforce the exact intended names; its 28-record assertion does not enforce the exact five control keys; and its installed check compares expected paths without rejecting extras. The independent exact name/key/inventory checks performed here close all three for this snapshot. They are limits of the reusable validator, not identified incorrect current package data.

The candidate validator writes candidate records and invokes synthetic proof logic, so it was inspected rather than run. This review verifies the 18 seal-named sidecars and the owned package/template identities, but does not rerun or substantively audit all 111 preparation inventory entries or saved synthetic execution claims. It does not establish absence of unrelated repository working-tree changes or current remote-main identity.

The current installed package is verified r40. Future safe synchronization still requires the reviewed published r41 commit, staging, recoverable backup, and complete installed inventory/byte/manifest readback. No production route, runtime, fresh reading, generation, scientific teaching result or acceptance is established. Root retains those actions. All review writes are limited to this package-and-manifests directory; all old outputs and candidate/installed/repository files remain unchanged.
