# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A single-document repository: one literature review,
[literature-review-teaching-programming-beginners.md](literature-review-teaching-programming-beginners.md),
written for Lars De Richter (Thomas More Hogeschool) as groundwork for an
educational-sciences research project on teaching programming to beginners in
tertiary education. There is no code, build, lint, or test tooling — all work
here is editing this Markdown document.

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
