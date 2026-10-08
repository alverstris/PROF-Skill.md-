# Frozen representation review helper

`frozen_render_review.py` generalizes the validated D002 workflow. It only reads the frozen source and public immutable GitHub URLs, and writes into a new/empty scratch output directory. No repository, GitHub, browser, CUA or installation operations are performed. D002 originals are not modified.

After the parent provides the exact freeze, use:

```bash
python3 /workspace/scratch/ac36b9c5ff31/prof-readability/render-tools/frozen_render_review.py \
  --source /absolute/path/to/frozen/teaching-vN.md \
  --url https://github.com/OWNER/REPO/blob/FULL_40_HEX_COMMIT/path/to/teaching-vN.md \
  --out /workspace/scratch/ac36b9c5ff31/prof-readability/REVIEW_NAME/vN
```

Local image paths default to the Markdown source's relative image references. If a constituent is elsewhere, add one `--image` per override:

```bash
--image figures/diagram-vN.png=/absolute/path/to/frozen/diagram-vN.png
```

The argument before `=` must exactly match its Markdown reference. The workflow supports the existing source format: plain prose, P labels, protected inline math, fenced math blocks, explicit HTML anchors, Markdown links, and relative constituent image paths without `..`. It derives math, paragraph, question, hint, solution and link counts from the supplied source rather than retaining D002 counts. If that source format changes, inspect the evidence and adapt deliberately instead of bypassing a failed check.

For just actual markup and frozen-image checks, add `--markup-only`. Otherwise, read the PDF skill and follow its existing pre-authoring marker requirement before invoking the PDF-producing command. Dependencies are the existing Python standard library, Pandoc, pdflatex and Poppler tools; there is no installer or browser fallback in this helper.

The helper fetches and saves the actual GitHub page/article, compares the entire normalized article text, separately compares every TeX payload exactly, checks plain prose typography, every P label and every internal href/target, and records matching Q/H/S links and return links. It verifies source and constituent image bytes against public raw URLs at the same commit. GitHub's `#qN` links and `user-content-qN` IDs are checked as corresponding markup, not as observed click execution.

For the internal preview it transparently changes only math delimiters, verifies the Pandoc AST's mathematical payloads, uses the existing `\gt`/`\lt` compatibility definitions, and compiles twice at 11 pt with 25 mm margins. It renders every final PDF page at 120 dpi and extracts page labels and compiler diagnostics. These operations do not mark any page visually reviewed.

Primary evidence files are `markup-audit.json`, `source-fetch.json`, `image-fetch.json` and `preview-check.json`, alongside the actual HTML, converted Markdown, LaTeX, PDF and complete page images. The output directory must be empty so a new freeze cannot overwrite earlier evidence.

Open every complete final page using the available image viewer, including all prompts, image labels, hint entries and complete solution entries. Record `complete_page_viewed`, the actual viewed file and precise findings in `preview-check.json`, and write the human review report. Only after that inspection can the local visual result be signed off. If an individual PNG has an image-viewer decode failure, the successful D002 fallback was a complete-page JPEG from the same final PDF:

```bash
pdftoppm -f PAGE -l PAGE -r 150 -jpeg -singlefile preview.pdf page-PAGE-full
```

Do not infer page pixels from text extraction. Do not infer GitHub navigation from PDF links. Pandoc may create captions from alt text, float images or introduce page breaks; distinguish those preview-only effects from actual Markdown/GitHub defects. Do not impose PDF help-page segregation on the GitHub product. The report must retain the limitation that live GitHub pixels, MathJax execution, responsive behavior and clicking were unobserved.

`regression-d002.json` records the one-time generalization check against the existing complete D002 v1 GitHub evidence and converted math AST. It is a workflow regression check, not a new review of D002 or any later draft.
