# Review log: literature-review-teaching-programming-beginners.md

**Reviewer:** Claude (AI-assisted critical review), June 2026
**Scope:** critical read of the full document; verification of references
against Google Scholar, the ACM Digital Library, publisher sites, and the
Open Universiteit library (WorldCat Discovery / Quick Search); targeted
searches for missing literature; edits applied directly to the document.
The pre-review version is preserved in git.

## Overall assessment

The review is in good shape: the canon is covered, the classical and
modern sources are real and correctly attributed, claims are calibrated
("strong/promising/contested"), and the synthesis sections are defensible.
The numbers spot-checked against the original papers (Bennedsen & Caspersen
67% pass rate; Watson & Li one-third failure; Patitsas 778 distributions,
5.8% multimodal; Stefik & Siebert's Randomo comparison; Finnie-Ansley Codex
top-quartile result) are all accurate.

A specialist reader would nevertheless have found four genuine weaknesses,
all addressed in this pass:

1. **Two topic gaps a CER professor would notice immediately:**
   metacognition/self-regulation (Loksa, Prather — a major CER strand and
   the theoretical bridge to the AI-era "widening gap" findings) and
   debugging instruction (McCauley et al.'s canonical review; recent
   intervention evidence) were absent as topics.
2. **Several empirical claims carried no citation** (mindset meta-analyses,
   mastery-learning outcomes, work-integrated-learning evidence, AI-detector
   bias).
3. **One cited work was missing from the reference list** (MacNeil et al.,
   2023), and Python Tutor was discussed without citing Guo (2013).
4. **Stale cross-references:** five places pointed to §4.6 for media
   computation/contextualisation, which is §4.7 (live coding is §4.6) —
   apparently left over from an earlier numbering.

One claim was strengthened *against* the document's own framing: the
reading-before-writing hierarchy (§2.3) is presented as settled; Fowler et
al.'s (2022) large replication found multiple skill structures fit equally
well and that cross-sectional correlations cannot settle teaching order.
The section now states the hierarchy with that caveat, which is where the
field actually stands.

## Verification of existing references

- All in-text citations were cross-checked against the reference list; the
  only missing entry was MacNeil et al. (2023) — now added.
- Spot-checked bibliographic details (venue, year, volume/issue, DOI) for
  the entries flagged as risky: Liffiton et al. (Koli Calling '23,
  formally published February 2024 — the (2024) dating is defensible);
  Denny et al. 2024a (CACM 67(2), 56–67, DOI verified); Ericson et al. 2023
  and Prather et al. 2023 working-group DOIs (plausible, sequential within
  the ITiCSE-WGR '23 proceedings). No errors found.
- The APA year-suffix convention for the Prather 2024 entries (2024a =
  widening gap, 2024b = Beyond the hype, plus the new 2024c) follows the
  document's existing usage rather than strict APA title-order lettering.
  If the document is ever submitted formally, re-letter by title order.

## New sources added (all bibliographic details verified)

**Foundational / instructional:**

- Lister, Fidge & Teague (2009, ITiCSE) — replication of the
  tracing–explaining–writing relationship (§2.3).
- Fowler et al. (2022, *Computer Science Education*) — large replication
  that complicates the skill hierarchy (§2.3).
- Qian & Lehman (2017, *TOCE*) — the standard review of novice
  misconceptions; syntactic/conceptual/strategic taxonomy (§2.4).
- Guo (2013, SIGCSE) — Python Tutor (§4.8).
- Loksa et al. (2016, CHI), Prather et al. (2018, ICER), Loksa et al.
  (2022, *TOCE*) — explicit problem-solving stages and metacognitive
  scaffolding (new §4.9).
- McCauley et al. (2008, *CSE*), Michaeli & Romeike (2019, WiPSCE), Yang
  et al. (2024, *TOCE*) — debugging as taught content (new §4.9).
- McCane et al. (2017, ACE) and Ott et al. (2021, ITiCSE) — mastery
  learning in CS1: gains for weaker students; procrastination as the
  documented failure mode (§6.3).
- Sisk et al. (2018, *Psychological Science*) and Yeager et al. (2019,
  *Nature*) — the actual evidence behind the "small and conditional
  mindset effects" claim (§7.2).
- Vihavainen, Paksula & Luukkainen (2011, SIGCSE) — extreme
  apprenticeship, the most direct CS1 evidence for cognitive
  apprenticeship (§8.2).
- Jackson (2015, *Studies in Higher Education*) — work-integrated
  learning evidence; placement design drives skill development (§8.3).
- Lyon & Denner (2019, *TOCE*) — peer-reviewed companion to the 2016
  report; institutional setbacks on the transfer pathway (§8.1).
- Brown & Wilson (2018, *PLOS Computational Biology*) — practitioner
  companion to the recommendations (§11).

**Generative-AI era:**

- Prather et al. (2024c, *TOCHI*) — "It's weird that it knows what I
  want": shepherding vs drifting interaction patterns with Copilot (§9.2).
- Bernstein et al. (2025, Koli Calling) — systematic review of GenAI harms
  in computing education, the natural successor to "Beyond the Hype"
  (§9.2).
- Liang et al. (2023, *Patterns*) — AI-text detectors biased against
  non-native English writers; supports the §9.5 integrity claim.

## Main changes to the document

1. **New §4.9 "Problem-solving process, metacognition, and debugging"**;
   the former §4.9 ("What does not have good evidence") renumbered to
   §4.10. Recommendation 5 extended accordingly (teach a debugging method
   and a problem-solving stage model as content).
2. **§2.3 rewritten at the end:** replication support (Lister et al.,
   2009) plus the Fowler et al. (2022) caveat; the claim is now stated at
   the strength the evidence supports.
3. **§2.4:** added the Qian & Lehman (2017) taxonomy.
4. **§6.3:** mastery-learning claims now cited (McCane et al., 2017) with
   the procrastination caveat (Ott et al., 2021).
5. **§7.2:** the previously uncited mindset-evidence sentence now cites
   Sisk et al. (2018) and Yeager et al. (2019), with the conditional
   nature of the Yeager result spelled out.
6. **§8.1–8.3:** added Lyon & Denner (2019), extreme apprenticeship
   (Vihavainen et al., 2011), and Jackson (2015).
7. **§9.2:** opening now points to the Bernstein et al. (2025) systematic
   review of harms; added the shepherding/drifting result (Prather et al.,
   2024c).
8. **§9.5:** detector-bias claim now cited (Liang et al., 2023).
9. **§11:** Brown & Wilson (2018) referenced as a practitioner companion.
10. **Fixed five stale cross-references** (§3.2, §5.1, §8.4, §9.3, §11
    pointed to §4.6 for contextualisation; now §4.7) and added the missing
    MacNeil et al. (2023) and Guo (2013) references.
11. **Appendix updated** with verified OU access routes for the new
    non-ACM sources (checked live via the OU library, June 2026):
    - Jackson (2015): EBSCO Academic Search Premier (12-month embargo).
    - Sisk et al. (2018): JSTOR backfile of *Psychological Science*
      (1990–2020).
    - Yeager et al. (2019): *Nature* via Springer Complete Journals
      (2010–present).
    - McCauley (2008) and Fowler (2022) fall under the existing Taylor &
      Francis licence; *Patterns* and *PLOS Computational Biology* are
      open access; everything else is ACM (open access).
12. **References:** 22 entries added (107 → 129), all alphabetised and
    formatted to the document's APA conventions; DOIs included only where
    verified.

## Considered and deliberately not added

- **Flipped-classroom and gamification literatures** — evidence is mixed
  and the document's scope statement excludes course-delivery logistics;
  flagging here in case the research project wants them later.
- **Computational thinking (Wing 2006 and successors)** — definitional
  literature, mostly K-12; the document's tertiary skill-acquisition focus
  is cleaner without it.
- **Lyon & Denner (2017, CACM Viewpoint)** — the 2019 TOCE article covers
  the same ground with peer review.
- **Additional 2025–2026 GenAI papers** (student-attitude surveys,
  single-course experience reports): the field is moving fast but the
  working-group reviews plus Bernstein et al. (2025) already anchor §9;
  individual experience reports would add bulk, not robustness.

## Remaining known limitations

- §9 will continue to date quickly; revisit before any formal use after
  mid-2027.
- The Yang et al. (2024) TOCE entry omits its article number (not
  retrievable without a subscription view); the DOI resolves correctly.
- The Lister et al. (2009) and Lyon & Denner (2019) entries carry no DOI
  (not verified); per the document's own formatting note this is
  deliberate.
- The associate-degree evidence gap (§8.1) remains real; the additions
  document the population better but do not close the gap — it is the
  research opportunity the document already identifies.

---

# Second pass: response to an external (Gemini) review

**Reviewer:** Claude, June 2026
**Scope:** assessment and (where warranted) implementation of priorities
1, 2, 3, and 5 from a Gemini review; priority 4 (block-to-text
transition) skipped at Lars's instruction. All new references verified
online (ACM DL, Taylor & Francis, CAST) before adding.

## Assessment of the four priorities

1. **Metacognition/SRL — largely already covered, one valid residue.**
   The Gemini review asked for metacognition as if absent, and proposed
   Loksa et al. (2016) as a missing must-read — but §4.9 already existed
   (added in the first pass) and already cites Loksa et al. (2016, 2022)
   and Prather et al. (2018). The valid residue: self-regulated learning
   *beyond* the single problem-solving episode (course-level planning and
   monitoring). Added a paragraph to §4.9 with Falkner, Vivian & Falkner
   (2014, ITiCSE), linked to the existing Margulieux et al. (2024)
   affect–SRL finding.
2. **Constructive alignment — critique partly incorrect.** §6.2 already
   opened with constructive alignment (Biggs, 1996), which the review
   claimed was missing. Implemented the defensible residue: spelled out
   the principle, added Biggs & Tang (2011) as the standard treatment,
   and added a sentence on programme-level alignment (sampling process as
   well as product) for competence-oriented graduaat programmes, tied to
   the existing §8.2 and §9.4 material. Programmatic assessment as a full
   topic (van der Vleuten) was *not* imported — beyond the document's
   scope and the CS1 evidence base.
3. **UDL — correct gap, added with calibration.** New closing paragraph
   in §7.3: UDL as a structural design framework (CAST, 2024), framed
   honestly — its prescriptions largely repackage practices the review
   already evidences, the Capp (2017) meta-analysis shows process gains
   but undemonstrated outcome effects, and computing-specific evaluations
   are scarce. Positioned as an organising checklist, not a validated
   intervention.
4. *(Skipped per instruction.)*
5. **Computational thinking — implemented as a scope note, not an
   import.** The first pass deliberately excluded the CT literature; that
   decision stands for the literature itself, but the external review is
   right that the document should *position* itself relative to CT. Added
   a boundary paragraph to §1.2 (Wing, 2006; Denning, 2017) explaining
   why the review stays with programming as the measurable skill.

Also added from the review's reference list: **Ben-Ari (1998)** to §3.2 —
a genuine omission; the constructivist argument for explicitly supplying
a machine model bridges §3.2 and the notional-machine consensus (§2.2).

## References added (7, all bibliographic details verified online)

- Ben-Ari (1998), *SIGCSE Bulletin, 30*(1), 257–261 — DOI verified.
- Biggs & Tang (2011), *Teaching for quality learning at university*
  (4th ed.), Open University Press.
- Capp (2017), *International Journal of Inclusive Education, 21*(8),
  791–807 — DOI verified.
- CAST (2024), UDL Guidelines version 3.0 — version and year checked
  against udlguidelines.cast.org (3.0 released July 2024).
- Denning (2017), *CACM, 60*(6), 33–39 — DOI verified.
- Falkner, Vivian & Falkner (2014), ITiCSE '14, pp. 291–296 — DOI
  verified.
- Wing (2006), *CACM, 49*(3), 33–35 — DOI verified against the ACM DL
  (note: search engines conflate it with Wing's 2007 SIGCSE abstract,
  which has a different DOI).

## Other changes

- **Fixed an alphabetisation error:** Bernstein et al. (2025) sat between
  the two Bennedsen & Caspersen entries; reordered.
- **Appendix:** Biggs & Tang (2011) added to the books list;
  *International Journal of Inclusive Education* (Capp, 2017) noted as
  Taylor & Francis but not individually verified for OU access.
- **Count correction:** the first pass reported 129 reference entries;
  the actual pre-pass count was 130. With 7 additions the list now holds
  137 entries.
- No headings were added, renamed, or renumbered, so the Contents list
  and §-cross-references needed no changes.
