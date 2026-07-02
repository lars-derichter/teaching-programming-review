# tools — building the bundled PDFs

Two scripts build the two bundled PDFs in the *ldr* house style, sharing
[style.css](style.css) and the same pipeline (pandoc → headless Chrome →
PyMuPDF):

- **[build-reader-pdf.py](build-reader-pdf.py)** — the integrated reader (front
  matter + theme introductions with each source article spliced in full). See
  below.
- **[build-leidraad-pdf.py](build-leidraad-pdf.py)** — the leidraad. See
  [the leidraad section](#building-the-leidraad-pdf).

## The reader PDF

[build-reader-pdf.py](build-reader-pdf.py) assembles the whole reader into a
single PDF: [../reader/teaching-programming-to-beginners-reader.pdf](../reader/teaching-programming-to-beginners-reader.pdf).

It renders the Markdown front matter and theme introductions with the `ldr`
house style, then splices each source article PDF in *after its introduction*,
untouched — original vector pages, original page numbering. It adds a clickable
table of contents, a PDF sidebar outline, and discreet footers on the rendered
pages only.

## What it produces

1. Title page.
2. Colophon: AI-use note, the Claude Fable 5 experiment note, and the licence
   (CC BY-NC-SA 4.0 scoped to Lars's own material; the articles stay under
   their own copyright).
3. Clickable table of contents (every row is a link) plus a bookmark outline.
4. Introduction (theme 0).
5. Themes 1–9: each theme's introduction, and after *each* reading's
   introduction the corresponding article, in full.
6. Theme 10 "Extra": all six introductions first, then all six articles.

## How it works

- **Sources** are read straight from [../reader/](../reader/): the `00`–`10`
  Markdown files and the PDFs under `reader/articles/` (and `articles/extra/`).
  Article placement is derived automatically from the `*PDF: [...]*` line in
  each reading — no hard-coded article list to keep in sync.
- **Markdown → HTML** via `pandoc`; **HTML → PDF** via headless Google Chrome
  (`--print-to-pdf`), which honours the A4 `@page` size and emits the link
  rectangles used for the TOC.
- **Splicing, TOC links, outline, footers** via **PyMuPDF** (`fitz`). Chrome's
  internal TOC links are not carried across the merge, so the script reads the
  link rectangles from the rendered TOC and re-adds them on the merged pages,
  retargeted to the computed article/theme pages.
- Styling lives entirely in [style.css](style.css). Heading colours, the accent
  rules, eyebrows, the "Source" callout, and footers are all defined there.

## Requirements

- `pandoc`, Google Chrome, Python 3 with **PyMuPDF** (`pip install pymupdf`).
- Fonts **Gentium Book Plus** and **IBM Plex Mono** installed
  (`brew install --cask font-gentium-book-plus font-ibm-plex-mono`).
- macOS paths are assumed for Chrome and the Gentium font file. Override the
  Chrome binary with `CHROME_BIN=...`; adjust the `GENTIUM` path near the top of
  the script for other platforms.

## Run

```sh
python3 tools/build-reader-pdf.py
```

Intermediates land in `tools/.build/` (gitignored); the final PDF is written to
`reader/`. Re-run after editing any theme Markdown, swapping an article PDF, or
changing `style.css`.

## Building the leidraad PDF

[build-leidraad-pdf.py](build-leidraad-pdf.py) turns the single leidraad
Markdown file into
[../leidraad/leidraad-programmeeronderwijs.pdf](../leidraad/leidraad-programmeeronderwijs.pdf).
It reuses [style.css](style.css) plus a small
[style-leidraad.css](style-leidraad.css) (tables, figure captions, the
Definitie/Verdieping/Werkvorm callouts, section photos, TOC page numbers).

### What it produces

1. Title page with a warm hero photograph.
2. Colophon: AI-use note and the CC BY-NC-SA licence (in Flemish; the licence
   note is moved out of the body and into this front page).
3. Table of contents with **real, clickable page numbers** and a bookmark
   outline.
4. The body as one continuous document: the four hand-drawn SVG figures from
   `leidraad/figuren/` inline, three warm section-opener photographs from
   `leidraad/beelden/`, and discreet footers with a folio page number.

### How it differs from the reader build

- **One flowing body**, not per-section PDFs, so the recommendations don't each
  start on a fresh page.
- **Page numbers in the TOC.** The reader's TOC has none. Each TOC heading gets
  an invisible sentinel span; after rendering the body, the script finds each
  sentinel's page with PyMuPDF, then renders the TOC with the resulting folios
  (iterating until the TOC's own page count is stable) and stamps matching
  folios in the footers.
- **Photographs.** Warm, permissively-licensed (CC0) images sourced via
  Openverse, given a light sepia duotone so they harmonise with the palette.
  Credits: [../leidraad/beelden/BEELDVERANTWOORDING.md](../leidraad/beelden/BEELDVERANTWOORDING.md).

### Requirements and run

Same toolchain as the reader (`pandoc`, Chrome, PyMuPDF, the two fonts).

```sh
python3 tools/build-leidraad-pdf.py
```

Intermediates land in `tools/.build/parts-leidraad/` (gitignored); the PDF is
written to `leidraad/`. Re-run after editing the leidraad Markdown, an SVG, a
photo, or either stylesheet.
