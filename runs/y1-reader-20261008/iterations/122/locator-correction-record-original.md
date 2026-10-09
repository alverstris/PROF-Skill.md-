# Locator corrections to the first delivered D122/shared source-preparation records

These corrections affect new scratch source-preparation records only. No repository, assigned PDF/image, failed cache, recovery source, or predecessor artifact was modified. This is not a teaching iteration, acceptance, or closure. All 51 chapter pages had already been personally read; targeted re-opening and caption checks corrected my locator descriptions, not a missing reading claim. D121 is unchanged. The D122 review itself is unchanged.

## Exact before → after

All numbers in this table are one-based original PDF pages.

| Record or locator | First delivered description | Corrected description |
|---|---|---|
|Chapter map, Figure13.4.2|Associated with p8|The actual xy-loop figure is on p7, alongside Figure13.4.1; p8 continues its algebra.|
|Chapter map, Figure13.4.3|Associated with p9|The actual xz-loop figure is on p8; p9 continues its algebra.|
|Chapter map, Figure13.4.5|Not named in its individual page record|Explicitly located on p12 as the traveling plane-wave figure.|
|Shared review, Figures13.4.5–6|Grouped as showing superposition and node placement|Figure13.4.6 shows conducting boundaries/node placement; Figure13.4.5 is the preceding traveling-wave diagram.|
|Chapter map, Figure13.6.1|Associated with p16 and called an energy cylinder|Actual volume-element figure is on p15; p16 continues the density/flux derivation. Shared review now says volume element, not cylinder.|
|Chapter map, Figure13.6.3|Associated with p18|Actual spherical/plane wavefront figure is on p19; p18 discusses it.|
|Chapter map, Figure13.6.4|Associated with p20|Actual solenoid diagram is on p21; p20 begins the example.|
|Chapter map, Figure13.8.6|Grouped with the p25 stills|Actual zero-mean dipole still is on p26; p25 introduces its formula.|
|Chapter map, Figure13.8.7|p26 called it Animation13.2|It is Animation13.3 on p26; Animation13.2/Figure13.8.6 is also on that page.|
|Chapter map, Figure13.8.10|Associated with p29|Actual magnetic-front diagram is on p30; p29 derives the B formula and external work.|
|Shared review solar example identifier|Example13.6.1|Solar example, pp17–18 (avoids confusing section/equation numbering with the source's example label).|
|Shared review standing-wave example identifier|Example13.6.2|Standing-wave example, p19 (same identifier correction).|
|Shared map figure indexing|Figure names within page-topic prose only|Added an explicit `figures_present_and_read` list to each of all51 page records; absent figures produce an empty list.|
|D122 map, recovered presentation p19|Original cache `error` remained at the recovered-image record's top level|Original error moved into `original_failed_cache`; recovered record says `decode: ok`. Failure text, zero-byte hash and recovery evidence remain preserved.|
|D122 map shared references|Referenced the first shared hashes|References the corrected shared hashes below; exact assigned boundaries and reading coverage are unchanged.|

## Files and hashes

Base directory: `/workspace/scratch/ac36b9c5ff31/prof-readability/sourceprep-teal-d121-d123-recovery`

| Relative path | First delivered SHA-256 | Corrected SHA-256 |
|---|---|---|
|shared-reading-review.md|b6dc87179d9ed52d158175d6700223a4b115abd9f6694c584caf67c271343076|32b33ee9c4f979cc9211fab2629d756c514efccb8201d72488cf17eb881413ce|
|shared-reading-map.json|f42b7852ac0e5c105a74af67732209a5e5f587e127dd793711ff5a5009f7e9de|c5a5d0caa55bb2d6e055f8af69b7376997d10348eb2f55da3713eb3fb327ece1|
|D122/source-map.json|12413f16048746a27a297e8a4577ae7993dcaf048a061234d65700c6e3ff333e|7418ae7ccd3fe667ecac1c1bcfc69165001a7f6ff79b3d87013bd5eedca13715|
|D122/source-review.md|a073c361d6043697c961560c5f0683ae5b5a1dc725d7e8d303d9feecd5500bd6|a073c361d6043697c961560c5f0683ae5b5a1dc725d7e8d303d9feecd5500bd6 (unchanged)|

Intermediate scratch hashes `203af84f8848cd360d992deb683cc9bf99c0e2763490e6e8fd7ec3ed550f80c4` for D122 map were produced before the p19 error-field relocation and are superseded by the corrected hash above. These were not a new authored lesson or closure action.
