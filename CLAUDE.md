# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A documentation repository for Lars De Richter (Thomas More Hogeschool),
groundwork for an educational-sciences project on teaching programming to
beginners in tertiary education. Its content is a **drieluik** (triptych) of
three mutually referencing documents:

1. **The literature review**,
   [literature-review-teaching-programming-beginners.md](literature-review-teaching-programming-beginners.md)
   — the full narrative evidence base.
2. **The reader**, [reader/](reader/) — twenty-one key articles selected from
   the review, with introductions and reading guides, plus a build tool
   ([tools/build-reader-pdf.py](tools/build-reader-pdf.py)) that assembles the
   bundled PDF.
3. **The leidraad**, [leidraad/leidraad-programmeeronderwijs.md](leidraad/leidraad-programmeeronderwijs.md)
   — a Dutch practice guide condensing the review into seven recommendations,
   with hand-written SVG figures in [leidraad/figuren/](leidraad/figuren/) and
   CC0 section photographs in [leidraad/beelden/](leidraad/beelden/), plus a
   build tool ([tools/build-leidraad-pdf.py](tools/build-leidraad-pdf.py))
   that assembles its bundled PDF.

The three are designed to be read together: the leidraad gives the practice,
the review the justification and evidence strength, the reader the sources. A
change to one may need reflecting in the others (e.g. a claim or citation
added to the leidraad should trace back to the review). The two PDF build
tools aside (see [tools/](tools/)), there is no code, build, lint, or test
tooling — work here is editing Markdown (and the leidraad's SVGs).

## Document status and caveats

- Marked "working document" / draft, compiled with AI assistance. The
  document's own header notes that claims and references must be verified
  against original sources before use in formal academic work.
- The appendix's library-access information was checked against the Open
  Universiteit library (bibliotheek.ou.nl) in June 2026 and will go stale —
  treat its dates and access routes as a snapshot, not current fact.
- The References section deliberately omits page ranges and DOIs that could
  not be verified (see the formatting note at the start of that section).
  Don't invent or "complete" these — leave them as-is unless verified.

## Structure and conventions to preserve when editing

The conventions below are written for the literature review; the reader and
leidraad share the APA and 80-character rules but differ otherwise. The
leidraad is in Flemish Dutch (see the user's house-style rules), uses seven
recommendations clustered from the review's §11, labels its callout boxes as
**Definitie** / **Verdieping** / **Werkvorm** blockquotes, and references the
review inline as "literatuurstudie §n". Its references are copied verbatim
from the review's list — don't invent DOIs or page ranges there either.

### The literature review

- 12 numbered top-level sections (`## 1. ...` through `## 12. ...`), plus an
  unnumbered Appendix and References section. The "Contents" block near the
  top links every section/subsection via its GitHub-generated anchor
  (lowercased, hyphenated heading text). If you rename, add, renumber, or
  reorder a heading, update the Contents list and any anchor links to match.
- Subsections are referenced inline in the prose as `§N.M` (e.g. "see section
  4.5", "(§2.2, §5.3)"). If a subsection is renumbered, find and update these
  cross-references too.
- Citations are APA 7th: in-text `(Author, year)`, full entries alphabetical
  in References. Match the existing entry format (italics via `*...*`,
  volume/issue/page conventions) when adding or editing references.
- Prose paragraphs are hard-wrapped at roughly 80 characters per line. Long
  lines in the Contents list and References are exceptions — they're single
  links/citations that can't be wrapped without breaking Markdown rendering.
