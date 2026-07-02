# Teaching programming to beginners

This repository started as a personal test for the new Claude AI model,
Fable 5. The resulting literature review was interesting enough to push to
GitHub, and it has since grown into a **drieluik** (triptych): three
documents that together form a grounded, research-based foundation for
teaching programming to beginners.

1. **The literature review** — the full evidence base: a narrative synthesis
   of five decades of computing education research, with the strength of each
   claim calibrated.
   [literature-review-teaching-programming-beginners.md](literature-review-teaching-programming-beginners.md)
2. **The reader** — the primary sources themselves: twenty-one key
   publications selected from the review, each read in full, bundled with
   introductions and reading guides. [reader/README.md](reader/README.md)
3. **The leidraad** — the practice guide: the evidence condensed into seven
   concrete recommendations for the classroom, aimed at lecturers and at
   students learning to teach.
   [leidraad/leidraad-programmeeronderwijs.md](leidraad/leidraad-programmeeronderwijs.md)

The three are meant to be used together: the leidraad says *what* to do, the
review says *why* it holds and how strong the evidence is, and the reader
lets you go to the sources. The rest of this README documents how each part
came to be.

## The literature review

The review was created in three passes. The document itself is here:
[literature-review-teaching-programming-beginners.md](literature-review-teaching-programming-beginners.md)

### Pass 1

Prompt:

```markdown
I need a scientific literature review about the current best practices for
teaching software development and programming to beginners at an undergraduate
degree or associate degree level. (Mainly young adults who have completed their
secondary education). Add plenty references and a clear bibliography (in APA
style). Be complete, identify trends, schools of thought etc. I want between 20
and 40 pages. This should work as a starting point for my colleagues as well as
a good starting point for a sideproject in my education sciences studies. Output
as a markdown document. Ask clarifying questions if you run into anything or if
I was not sufficiently clear.
```

[Versie 1](https://github.com/lars-derichter/teaching-programming-review/blob/e2f600716abdf63634397ef726b1eec4811fa83c/literature-review-teaching-programming-beginners.md)
was already very complete.

### Pass 2

Now with direct access to scientific databases that are normally behind a
paywall or university login:

```markdown
I want you to do a critical and thorough review of
@literature-review-teaching-programming-beginners.md Use worldcat, google
scholar and the other relevant databases that can be reached through:
https://bibliotheek.ou.nl/databases (I am logged into the ou ibrary using
chrome, but ask my help if you need me to click anywhere or input credentials).
Focus on adding extra relevant sources and adapt the contents of the paper when
necessary. Create a second document review.md to log your findings and a concise
overview of the main changes that you have made. The original is in git, so do
not worry about making edits or deletions to the original text. This literature
review should be robust and be able to withstand a critical reading by a
university professor who has specialised is this area.
```

[Versie 2](https://github.com/lars-derichter/teaching-programming-review/blob/b9b2d4abd2449e154e2288e86ef3fec797cee119/literature-review-teaching-programming-beginners.md)
has minor changes.

### Pass 3

#### Review by Gemini Pro

As part of the experiment I wanted Google’s AI to do a review of Claude’s work.
For no reason whatsoever I switched to Dutch.

Gemini Prompt:

```markdown
Beoordeel dit document zoals een universiteitsprofessor in de
onderwijswetenschappen met een focus op programmeeronderwijs dit zou doen.

Maak een geprioritiseerde lijst met verbetersuggesties en een lijst met
belangrijke referenties die misschien nog ontbreken.
```

#### Final version and Claude’s answer to Gemini

I then used Gemini’s answer as part of this Claude prompt:

```markdown
This is a review by the Gemini AI-agent:

**Beoordeling van het Literatuuroverzicht "Teaching programming to beginners"**

Als professor in de onderwijswetenschappen met een focus op
informatica-didactiek (Computing Education Research of CER) ben ik zeer te
spreken over dit werkdocument. Het biedt een indrukwekkende, bijzonder goed
gestructureerde synthese van de state-of-the-art. Het document slaagt erin om
klassieke theorieën, zoals de _notional machine_ en du Boulay's taxonomie,
naadloos te verbinden met de meest actuele onderwijsuitdagingen, waaronder
Generatieve AI en evidence-based praktijken zoals PRIMM en Parsons problems. Het
is bovendien didactisch zeer sterk dat de hiërarchie van vaardigheden ("reading
before writing") als een centraal thema is gepositioneerd.

Om dit document van een uitstekende synthese verder te ontwikkelen naar een
robuust, allesomvattend fundament voor curriculumontwerp en wetenschappelijk
onderzoek, heb ik de onderstaande geprioritiseerde lijst met verbetersuggesties
opgesteld, gevolgd door enkele essentiële publicaties die nu nog ontbreken.

### Geprioritiseerde lijst met verbetersuggesties

1. **Prioriteit 1: Explicitering van Metacognitie en Zelfregulerend Leren
   (SRL)** Het document besteedt terecht veel aandacht aan cognitieve belasting
   (Cognitive Load Theory) en het expliciet maken van expert-processen (zoals
   via _live coding_). Wat echter onderbelicht is, is het metacognitieve aspect.
   Novices lopen vaak vast omdat ze niet weten _hoe_ ze hun eigen
   probleemoplossende proces moeten plannen, monitoren en evalueren (vooral
   tijdens het debuggen). Het aanleren van expliciete strategieën voor
   zelfregulatie zou als een cruciaal evidence-based leerdoel toegevoegd moeten
   worden.
2. **Prioriteit 2: Constructive Alignment in het Toetsbeleid** Sectie 6 biedt
   waardevolle perspectieven op formatieve feedback en _mastery learning_, maar
   mist de conceptuele kapstok van _Constructive Alignment_. Zeker binnen de
   beroepsgerichte Associate Degrees (de graduaten in Vlaanderen), waar het
   document specifiek op focust, is de keiharde afstemming tussen beoogde
   leerdoelen, leeractiviteiten en summatieve evaluatie essentieel. Er mag
   dieper worden ingegaan op hoe docenten een valide toetsprogramma
   (programmatisch toetsen) opzetten dat het "proces" meet en niet uitsluitend
   het afgewerkte eindproduct.
3. **Prioriteit 3: Kaders voor Inclusie en Universal Design for Learning (UDL)**
   Sectie 7 levert goed werk door de "geek gene"-mythe te ontkrachten en de
   invloed van _mindset_ en vroege interventies te bespreken. Echter, het
   bevorderen van een diverse instroom en het vasthouden van deze studenten
   vraagt ook om structurele ontwerpkaders, zoals Universal Design for Learning
   (UDL). Dit geeft docenten concrete handvatten om drempels in cursusmateriaal
   te verlagen zonder de inhoudelijke lat omlaag te halen.
4. **Prioriteit 4: De didactische transitie van Visuele naar Tekstuele Talen
   (Block-to-Text)** Sectie 5.2 bespreekt de voordelen van block-based
   omgevingen (zoals Scratch) en de vergelijking met tekstuele talen. Aangezien
   steeds meer studenten in het voortgezet/secundair onderwijs al visueel hebben
   leren programmeren, is juist de overgang (de _block-to-text transition_) een
   belangrijk onderzoeksgebied in CS1. De inzet van hybride tools of
   overbruggende didactiek verdient hier een extra alinea.
5. **Prioriteit 5: Verhouding tot 'Computational Thinking' (CT)** Voor
   niet-informatica opleidingen en graduaten gaat leren programmeren vaak hand
   in hand met het breder aanleren van 'Computational Thinking'
   (patroonherkenning, abstractie, algoritmisch denken). Het is verhelderend om
   de relatie (of overlap) tussen louter het schrijven van code en CT kort te
   positioneren in het begin van het rapport.

---

### Belangrijke Ontbrekende Referenties

Om de wetenschappelijke diepgang rondom deze verbetersuggesties te borgen, raad
ik aan de volgende "must-reads" uit de CER- en onderwijsliteratuur toe te
voegen:

- **Metacognitie & Probleemoplossing:**
- _Loksa, D., Ko, A. J., Jernigan, W., Daniels, A., Barr, C., & Marble, A.
  (2016)._ "Programming, Problem Solving, and Self-Awareness: Effects of
  Explicit Guidance." (Dit artikel levert prachtig bewijs dat het expliciet
  aanleren van probleemoplossende fases en metacognitieve reflectie de
  prestaties van novices aanzienlijk verbetert).

- **Constructivisme & Mentale Modellen:**
- _Ben-Ari, M. (1998)._ "Constructivism in computer science education." (Een
  onmisbare klassieker die fundamenteel uitlegt waarom een correcte _notional
  machine_ een absolute voorwaarde is binnen de constructivistische
  leertheorie).

- **Toetsing & Onderwijsontwerp:**
- _Biggs, J., & Tang, C. (2011)._ "Teaching for Quality Learning at University."
  (Het standaardwerk voor Constructive Alignment. Cruciaal om de link tussen
  CS-onderwijsactiviteiten en toetsing te theoretiseren).

- **Zelfregulerend Leren (SRL):**
- _Falkner, K., Vivian, R., & Falkner, N. J. G. (2014)._ "Identifying computer
  science self-regulated learning strategies." (Zeer nuttig om te duiden hoe
  effectieve informaticastudenten buiten de les omgaan met complexe obstakels).

- **Computational Thinking:**
- _Wing, J. M. (2006)._ "Computational thinking." _Communications of the ACM_.
  (Het startpunt van het moderne debat over computationeel denken als
  fundamentele vaardigheid naast lezen, schrijven en rekenen).

I want you to look at priority 1,2,3 and 5. Ignore 4 (this will lead nowhere
interesting).

If you deem these correct critiques of the current document, implement the
necessary changes and then update your log: claude-review-log.md
```

Claude created
[the final version](https://github.com/lars-derichter/teaching-programming-review/blob/b5d53ba4b1fc1eff8193ad9626c1f6f085c2249c/literature-review-teaching-programming-beginners.md)

It also gave the following answer. The pushback is interesting:

```markdown
I'll start by reading the document and the existing review log to evaluate the
four critiques against what's actually there.

All key references verified. One last check — the current version of the CAST
UDL guidelines, so the citation doesn't claim a stale version:

Now let me sanity-check the reference count and run a quick consistency check on
the new cross-references:

137 genuine entries (the previous log's "129" was an undercount — the actual
pre-pass total was 130). Now updating the review log with this second pass:

Final check — line-wrap discipline on the added prose and a diff overview:

Done. The verdict on Gemini's review is mixed, and I implemented accordingly —
both files are updated.

**Per-priority assessment and what changed:**

- **Priority 1 (metacognition/SRL) — mostly stale.** Gemini proposed Loksa et
  al. (2016) as a missing must-read, but §4.9 already exists from the previous
  review pass and already cites it, plus Loksa et al. (2022) and Prather et al.
  (2018). The valid residue was self-regulated learning _beyond_ the single
  problem-solving episode: I added a paragraph to §4.9 with Falkner, Vivian &
  Falkner (2014, ITiCSE) and linked it to the existing Margulieux et al. (2024)
  affect findings.
- **Priority 2 (constructive alignment) — partly wrong.** §6.2 already opens
  with constructive alignment (Biggs, 1996); Gemini claimed the concept was
  absent. I implemented the defensible residue: spelled out the principle, added
  Biggs & Tang (2011), and added one sentence on programme-level alignment
  (assessing process as well as product) for the graduaat context. I did _not_
  import programmatic assessment (van der Vleuten) as a topic — out of scope and
  not part of the CS1 evidence base.
- **Priority 3 (UDL) — correct gap, added with calibration.** New closing
  paragraph in §7.3 citing CAST (2024) and Capp's (2017) meta-analysis, framed
  at the strength the evidence supports: UDL's prescriptions largely repackage
  practices the review already evidences, outcome effects remain undemonstrated,
  and computing-specific evaluations are scarce. An organising checklist, not a
  validated intervention.
- **Priority 5 (CT) — implemented as a scope note.** The first pass deliberately
  excluded the CT literature; that holds, but Gemini is right the document
  should position itself. Added a boundary paragraph to §1.2 (Wing, 2006;
  Denning, 2017).
- **Bonus:** Ben-Ari (1998) was a genuine omission from Gemini's reference list
  — added to §3.2, where it bridges constructivism and the notional-machine
  consensus.

**Housekeeping:** 7 references added (all DOIs/editions verified online; note
that search engines conflate Wing 2006 with her 2007 SIGCSE abstract — I
verified the correct CACM DOI). Fixed a pre-existing alphabetisation error
(Bernstein 2025 sat between the two Bennedsen entries). Appendix updated for
Biggs & Tang and Capp. No headings changed, so Contents and §-cross-references
needed no updates. [claude-review-log.md](claude-review-log.md) now documents
this second pass, including a count correction (the list held 130 entries, not
the 129 the first pass reported; now 137).

Sources used for verification:
[Falkner et al. 2014 (ACM DL)](https://dl.acm.org/doi/10.1145/2591708.2591715),
[Capp 2017 (T&F)](https://www.tandfonline.com/doi/full/10.1080/13603116.2017.1325074),
[Ben-Ari 1998 (ACM DL)](https://dl.acm.org/doi/10.1145/274790.274308),
[Denning 2017 (ACM DL)](https://dl.acm.org/doi/10.1145/2998438),
[Wing 2006 (ACM DL)](https://dl.acm.org/doi/pdf/10.1145/1118178.1118215),
[CAST UDL Guidelines](https://udlguidelines.cast.org/),
[Biggs & Tang 4th ed.](https://www.biblio.com/book/teaching-quality-learning-university-what-student/d/1571163691).
```

I had Claude create a kind of logbook from version 2 onwards:
[claude-review-log.md](claude-review-log.md)

## The reader

In a follow-up session, Claude turned the review into a course reader for
students learning how to teach programming to beginners in an associate
degree programme: fifteen key articles (selected from the review, downloaded
via open access and the OU library, and each read in full before the final
keep-or-replace decision), bundled with an overall introduction, theme
introductions, and a per-article introduction with reading guide and
discussion questions.

Start here: [reader/README.md](reader/README.md)

The complete reader — all fifteen articles plus the introductions and reading
guides bundled into one PDF — is here:
[reader/teaching-programming-to-beginners-reader.pdf](reader/teaching-programming-to-beginners-reader.pdf)
(527 pages, 36 MB).

## The leidraad

The third part of the drieluik condenses the review into a practice guide
(*leidraad*) for lecturers: seven concrete, evidence-informed recommendations
for teaching programming to beginners, modelled on the structure and register
of Thomas More's *Leidraad EHBO docenten*. It is written in Dutch and is also
meant as course material for students learning to teach. Its load-bearing
claims were verified against the primary articles in the reader; where a claim
rests only on the narrative review, the guide says so.

Start here:
[leidraad/leidraad-programmeeronderwijs.md](leidraad/leidraad-programmeeronderwijs.md)
(figures in [leidraad/figuren/](leidraad/figuren/)).

The leidraad is also bundled as a single styled PDF, in the same *ldr* house
style as the reader, with a page-numbered table of contents, the hand-drawn
figures inline, and a handful of warm, permissively-licensed (CC0) section
photographs:
[leidraad/leidraad-programmeeronderwijs.pdf](leidraad/leidraad-programmeeronderwijs.pdf)
(26 pages). See
[leidraad/beelden/BEELDVERANTWOORDING.md](leidraad/beelden/BEELDVERANTWOORDING.md)
for the image credits.
