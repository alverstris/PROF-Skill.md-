# LaTeX and PDF production

Use this reference when PROF produces or revises a teaching document. The
default deliverables are a compiled PDF and an Overleaf-importable ZIP of
the complete editable LaTeX project. This does not require access to the
user's Overleaf account. Follow a different requested format when explicit.

## Start from the supplied assets

Copy `assets/latex/main.tex` and `assets/latex/prof.sty` into a new project
directory with `main.tex` at its root. Replace the complete example with
the actual lesson; do not leave the demonstration in an unrelated guide.
Use `\documentclass[11pt,a4paper]{article}` and `\usepackage{prof}`.
Set `\ProfHeader{Short topic}` and use `\ProfTitle{Title}{Practical outcome}`.
The short header must fit on one line. Neither a decorative title page nor
a table of contents is required for a short lesson. For a long guide, add a
compact contents list with upright, medium-weight entries and bookmarks;
the standard article contents can introduce bold section entries, so style
it explicitly and inspect its result.

The starter provides A4 pages, 25 mm margins, 11 pt Latin Modern body text,
comfortable paragraph spacing, restrained ink/teal colours, page numbers,
readable mathematics, tables, code and sparse breakable callouts. Preserve
normal paragraph flow. Use hierarchy, spacing and subtle rules instead of
bold or italic prose. This restriction includes headings, captions, table
headers, bibliography titles, code comments and box titles; standard
mathematical notation is unaffected. Do not use `\textbf`, `\emph`,
`\textit`, `\bfseries` or `\itshape` for emphasis. Additional packages and
bibliography styles can reintroduce these faces and require inspection.

Use equations for reasoning, not as unintroduced decoration. Use `align`
for genuinely connected derivation steps. Number equations that will be
referred to, define the objects and assumptions where used, and retain
units. Use `tabularx` with the supplied `Y` column and `booktabs` for compact
comparisons. Avoid vertical table rules and tiny text. Split wide tables
by meaning; use `longtable` for a table that genuinely needs several pages.
Use accurate vector diagrams or plots where they help; place their files
under `figures/` and include them by relative paths. Captions should explain
the inference the figure supports. For code, use `lstlisting` with the
provided `prof` style, a language setting where supported, and a legible
font. Do not require `minted` or shell escape. If extending the template,
keep added features portable and scoped to the lesson's needs.

## Practice navigation in an ordinary PDF

Use one short unique ID per meaningful task, stable across local revisions.
The ID must be safe as a LaTeX label, for example `changed-site`.

```latex
\begin{profattempt}{changed-site}{Interpret the changed model}
The actual task, including all needed data and an observable requested output.
\end{profattempt}

% Later, outside the main lesson route:
\clearpage
\section{Hints}
\begin{profhint}{changed-site}{Identify the next decision}
A direction that helps without doing the whole task.
\end{profhint}

% Group other hints here before starting the full-solution pages.
\clearpage
\section{Full solutions}
\begin{profsolution}{changed-site}{Reason through the decision}
A full answer with the important reasoning and a targeted correction.
\end{profsolution}
```

`profattempt` supplies links to its hint and full solution. `profhint` links
to the full solution and back to the attempt. `profsolution` links back.
The named destinations are `question:ID`, `hint:ID`, and `solution:ID`.
`\ProfAttemptLink{ID}` links to an attempt from another part of the guide.
Never reuse an ID, omit a linked destination, or imply that PDF answer
sections are interactively hidden. They are separate, linked pages or
sections; no JavaScript or special viewer is needed. For multiple levels
of help, put the graduated hints within the matching hint section.

Keep full solutions away from the immediate line of sight of both attempts
and hints. Group hints after a coherent unit or in an appendix, then start
the full solutions on a separate page. A hint link must not land on a page
that also exposes the complete answer. This deliberate page break preserves
graduated help; group several hints and several solutions rather than
creating a page per question. Do not add filler to occupy the resulting
space. A long worked example
may use ordinary prose with a clear heading rather than a large box.
Use `profworked` selectively, never for every definition. Do not turn every
minor term into a boxed check. Explain a fully worked case near its setup;
separating optional help must not force backtracking through the teaching.

## Build, check and bundle

Use pdfLaTeX with common TeX Live packages by default. The supplied assets
compile without absolute paths, system fonts, network downloads or shell
escape. Use LaTeX commands for symbols and supported accented characters.
For scripts that require a Unicode engine, explicitly switch to LuaLaTeX,
replace the pdfLaTeX font/input setup in `prof.sty` with `fontspec` and a
TeX-distributed font covering the required script, then compile and inspect
that configuration. Document the chosen compiler; do not silently depend
on a machine-local font.

Run from the project root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

If `latexmk` is unavailable, run `pdflatex` at least twice and repeat until
cross-references stabilise. When using BibTeX, use pdfLaTeX, BibTeX,
pdfLaTeX, pdfLaTeX; when using biblatex, use its specified backend (usually
Biber) and rerun LaTeX. Include the `.bib` and any custom `.bst` files.
Choose or configure an upright, medium-weight bibliography; do not accept
italic book titles or bold labels merely because a default style adds them.
Keep technical source citations real, nearby and human-readable. Never
invent citations to complete a template.

Before delivery:

1. Fix compilation errors, undefined references or citations, missing
   characters, duplicate destinations and overfull boxes. Investigate
   underfull boxes that visibly damage layout. Check that no stale build
   artefact is masking a missing source file.
2. Inspect extracted PDF text for missing material, malformed equations,
   incorrect exercise numbers and unresolved `??`. Text extraction is a
   coverage check, not proof of visual correctness.
3. Render the latest PDF using the available PDF workflow, or `pdftoppm`
   plus visual inspection, and inspect every page at a readable size.
   Check dense derivations, figures, tables, code, page
   boundaries, callout breaks, captions and help sections. Fix overlaps,
   clipping, awkward spacing and unintended bold or italic prose. Standard
   italic mathematical variables are expected.
4. Verify that every task has the intended hint and complete solution, that
   hyperlinks resolve in both directions, and that PDF named destinations
   are unique. Verify the mathematics and reasoning independently of the
   visual check. A successful build cannot establish learning effectiveness.
5. Create a clean ZIP with `main.tex`, `prof.sty`, all referenced chapter,
   figure and bibliography files, plus a short `BUILD.md` stating the
   compiler and build command. Put `main.tex` directly at the ZIP root,
   not inside an unnecessary outer folder. Exclude logs, auxiliary files,
   temporary renders and unrelated source material. Supply the compiled
   PDF separately. Include it in the ZIP only when useful or requested.
6. Extract the final ZIP into a fresh directory and compile it there using
   the documented command. This checks portability and relative file
   paths. Deliver the final verified PDF and the matching source project
   using the applicable file-saving workflow.

Do not claim an Overleaf import was tested unless it was actually tested
there. A clean local build of the complete portable project supports the
claim that an importable source bundle has been provided. If compilation
or rendering is unavailable, provide the source and clearly state which
verification could not be completed; do not label an unbuilt source a
verified PDF.
