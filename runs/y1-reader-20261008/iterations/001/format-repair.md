Output repair F01

Original:v1 at a82371f2ae8183927877bfd85759e73cf4e0b070, blobf495acc6019b0fbef67bfbb873624b16d816b3cd.
Target: repo-native GitHub Markdown.
Evidence: official GitHub documentation, https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions (read2026-10-08), specifies dollar-delimited inline math and double-dollar blocks or math fences. The authored file instead used backslash-parenthesis and backslash-bracket chat delimiters. This is a format compatibility concern, not a false mathematical conclusion or a reader reasoning defect.

Repair: changed only math delimiters to GitHub's documented syntax in teaching-v2.md. Actual glyph rendering remains unverified; do not present a syntax check as visual inspection.
Verification: all288extracted mathematical payloads (249inline,39display) unchanged and all intervening prose unchanged. No scientific or explanatory edit. A fresh SASIS reader receives v2 alone with the complete baseline, under the same r7 protocol.
PROF decision: no additional skill change warranted. Existing T11 requires format-appropriate output; this is a document-production repair. The author already marked rendering unverified, so there is no false author claim that visual QA passed.
