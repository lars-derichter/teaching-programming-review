# tools — building the integrated reader PDF

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
