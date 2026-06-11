# Teaching programming to beginners: a review of the literature

**Author:** prepared for Lars De Richter (Thomas More) — June 2026
**Status:** working document, intended as a starting point for colleagues and
as groundwork for a research project in educational sciences

> **About this document.** This is a narrative literature review compiled with
> AI assistance. The references are real publications and the key claims were
> checked against the published literature, but before citing any individual
> source in formal academic work, verify the quote or claim against the
> original paper. Page numbers for direct quotations are deliberately not
> given; consult the originals.
>
> **Library access.** In June 2026 the availability of the cited sources was
> checked against the Open Universiteit library. Nearly everything is
> retrievable through it; see
> [Appendix: finding the sources](#appendix-finding-the-sources-via-the-ou-library)
> for the routes and the handful of exceptions.

## Contents

1. [Introduction: scope and method](#1-introduction-scope-and-method)
2. [What makes learning to program hard](#2-what-makes-learning-to-program-hard)
3. [Theoretical frameworks and schools of thought](#3-theoretical-frameworks-and-schools-of-thought)
4. [Evidence-based instructional practices](#4-evidence-based-instructional-practices)
5. [Languages, environments, and tools](#5-languages-environments-and-tools)
6. [Feedback and assessment](#6-feedback-and-assessment)
7. [Motivation, affect, and equity](#7-motivation-affect-and-equity)
8. [The associate-degree and vocational context](#8-the-associate-degree-and-vocational-context)
9. [Programming education in the era of generative AI](#9-programming-education-in-the-era-of-generative-ai)
10. [Synthesis: trends and trajectories](#10-synthesis-trends-and-trajectories)
11. [Recommendations for practice](#11-recommendations-for-practice)
12. [Limitations of this review](#12-limitations-of-this-review)
13. [Appendix: finding the sources via the OU library](#appendix-finding-the-sources-via-the-ou-library)
14. [References](#references)

---

## 1. Introduction: scope and method

### 1.1 Why this review

Introductory programming is one of the most heavily researched topics in
computing education. The course universally nicknamed "CS1" (after an early
ACM curriculum designation) has accumulated five decades of studies on why
students struggle, what predicts success, and which teaching interventions
demonstrably help (Becker & Quille, 2019; Luxton-Reilly et al., 2018). Yet
much of this evidence travels slowly into classroom practice, and the arrival
of large language models (LLMs) that can solve most traditional CS1
assignments has destabilised assumptions that held for fifty years (Denny et
al., 2024a; Prather et al., 2023).

This review synthesises the current state of the evidence on teaching
software development and programming to beginners in tertiary education —
specifically young adults entering undergraduate (bachelor) or
associate-degree programmes after completing secondary education. It is
written for two audiences: lecturers who want a research-informed starting
point for course design, and as groundwork for further study in the
educational sciences. It deliberately gives extra attention to the
vocationally oriented associate-degree context (in Flanders: the *graduaat*,
EQF level 5), because that population is underrepresented in the research
literature relative to its size (Lyon & Denner, 2016; see section 8).

### 1.2 Scope and terminology

The review covers:

- **The learner population.** Novice programmers aged roughly 18–25 in formal
  tertiary education. Findings from school-age (K-12) research are cited
  where they transfer plausibly and are flagged as such.
- **The subject.** Introductory programming and early software development:
  the first one to three semesters, before specialisation. "CS1" is used as
  shorthand for any first programming course, whether in a computer science
  degree, an applied informatics programme, or a vocational track.
- **The evidence base.** Peer-reviewed work from the main computing education
  venues — the ACM conferences SIGCSE TS, ITiCSE, ICER, Koli Calling, ACE —
  and journals (*ACM Transactions on Computing Education*, *Computer Science
  Education*), plus general educational psychology where it underpins the
  field (cognitive load theory, self-efficacy, formative assessment).

The review is *narrative*, not systematic: it does not exhaustively catalogue
every study, but synthesises the major findings, identifies schools of
thought, and weighs the strength of evidence. Where systematic reviews and
meta-analyses exist, they are used as anchors (Luxton-Reilly et al., 2018;
Vihavainen et al., 2014; Umapathy & Ritzhaupt, 2017; Keuning et al., 2018;
Ericson et al., 2022).

### 1.3 A note on reading the evidence

Computing education research (CER) has matured considerably since the 2000s.
Early work was dominated by single-institution experience reports; the field
now demands controlled studies, multi-institutional replications, and
theory-driven designs (Fincher & Robins, 2019). Even so, effect sizes vary
across contexts, and very few interventions have been tested specifically on
associate-degree populations. Throughout this review, claims are calibrated:
"strong evidence" means multiple controlled studies or a meta-analysis;
"promising" means consistent but limited evidence; "contested" means the
literature genuinely disagrees.

---

## 2. What makes learning to program hard

Any discussion of best practices needs a model of *why* the subject is
difficult. The literature offers a remarkably stable answer that has been
refined, not overturned, since the 1980s.

### 2.1 The classical difficulty studies

du Boulay (1986) catalogued the difficulties of novice programmers in a
taxonomy that still structures the field: orientation (what programming is
for), the *notional machine* (the abstract model of the computer implied by
the language), notation (syntax and semantics), structures (schemas and
plans), and pragmatics (the craft of planning, writing, and debugging).
Crucially, du Boulay observed that these difficulties arrive *all at once*
for the beginner, which is in modern terms a cognitive-load problem (see
section 3.1).

Soloway (1986) argued that learning to program is learning to construct
*mechanisms* and *explanations*: novices must assemble low-level language
constructs into goal-directed "plans" (e.g., the running-total loop pattern),
and most novice failures are failures of plan composition rather than syntax.
Spohrer and Soloway (1986) showed empirically that the folk wisdom "bugs come
from misconceptions about language constructs" was largely wrong — most bugs
came from putting plans together. Pea (1986) identified "superbug"
misconceptions that are language-independent: novices attribute intentions
and hidden intelligence to the machine, assuming it will interpret what they
*meant*.

This classical work established a consensus that remains foundational: the
hard part of programming is not syntax but the construction of a runnable
mental model of program execution and a repertoire of composable solution
schemas (Robins et al., 2003).

### 2.2 The notional machine and mental models

The term *notional machine* — the idealised abstract computer whose
behaviour a learner must internalise to predict what code does — has become a
central organising concept (du Boulay, 1986; Sorva, 2013). Sorva's (2013)
review argues that many classic novice misconceptions (variables as boxes
that can hold multiple values, assignment as equation, loops executing "all
at once") are best understood as faulty notional machines. An ITiCSE working
group catalogued notional machines in actual teaching practice and found
teachers improvise them constantly — the box metaphor for variables, desk
checking, memory diagrams — but rarely use them systematically (Fincher et
al., 2020).

The practical consequence, strongly supported across this literature: *the
execution model must be taught explicitly*. Program visualisation tools
(memory diagrams, steppers and tracers such as Python Tutor), teacher-led
tracing, and explicit vocabulary for what the machine does at each step all
target this need (Sorva et al., 2013). Hermans (2021) popularised the
cognitive-science framing for practitioners: reading and tracing code
exercises working memory, and novices lack the chunked knowledge that lets
experts read code fluently.

### 2.3 The hierarchy of skills: reading before writing

A landmark multi-national study (McCracken et al., 2001) found that students
finishing CS1 performed far worse on a common programming task than their
teachers expected — a wake-up call about overestimating outcomes. The
follow-up working group (Lister et al., 2004) found that many students could
not even *read and trace* code reliably, suggesting the writing failure had a
more basic cause. Subsequent BRACElet studies established correlational
evidence for a skill hierarchy: tracing and explaining code predict and
plausibly precede the ability to write it (Lopez et al., 2008; Whalley et
al., 2006). Students who can summarise what a code fragment does in one
sentence — "explain in plain English" — tend to be the ones who can write
code (Murphy et al., 2012).

This reading-before-writing finding is arguably the single most
practice-relevant result in the CER canon. It directly motivates several of
the instructional designs in section 4 (PRIMM, Parsons problems,
comprehension-first sequencing) and has gained new urgency in the LLM era,
where reading and evaluating generated code is becoming the dominant skill
(Denny et al., 2024a; see section 9).

### 2.4 Misconceptions and errors at scale

Large-scale data confirmed and refined the classical picture. The Blackbox
project, collecting data from hundreds of thousands of novices using the
BlueJ Java environment, showed that the most frequent novice errors are not
the ones educators believe are most frequent, and that educators' rankings of
error frequency barely agree with each other (Altadmri & Brown, 2015; Brown &
Altadmri, 2017). Some syntax errors that educators consider trivial consume
enormous amounts of novice time. Error messages themselves are a documented
barrier: a fifty-year research landscape review concluded that compiler error
messages remain consistently unhelpful for novices and proposed design
guidelines (Becker et al., 2019).

### 2.5 Failure rates: a real problem, accurately sized

Introductory programming has a reputation as a "killer course". The evidence
supports concern but not fatalism. Bennedsen and Caspersen (2007) estimated a
worldwide CS1 pass rate of 67%; Watson and Li (2014), aggregating 161 courses
across 15 countries, found a mean failure rate of about one third, stable
across time and not strongly dependent on language taught. Bennedsen and
Caspersen (2019) revisited the question and found a slightly improved failure
rate around 28%. Importantly, these rates are comparable to other demanding
introductory STEM courses; the popular claim that CS1 failure is uniquely
catastrophic is not supported (Watson & Li, 2014).

Two further results reframe the failure-rate discussion. First, Vihavainen et
al. (2014) reviewed intervention studies and estimated that adopting any of
the better-evidenced teaching approaches improves pass rates by roughly one
third relative to traditional lecture-based teaching — i.e., outcomes are
substantially under instructor control. Second, the distribution of outcomes
is not what folklore says, as the next section explains.

### 2.6 The "geek gene" myth

A persistent school of thought holds that programming ability is bimodal:
some students "get it" and others never will. This belief matters because
teachers who hold it teach differently and students who absorb it disengage
(see mindset, section 7.2). The empirical support has collapsed. The famous
"camel has two humps" aptitude-test paper was never peer-reviewed and was
formally retracted by its author (Bornat, 2014). Patitsas et al. (2020)
analysed 778 grade distributions at a selective institution and found only
5.8% were multimodal; moreover, instructors who believed in innate ability
were more likely to *perceive* ambiguous histograms as bimodal. Robins (2010)
offered a better explanation for the observed spread of outcomes: *learning
edge momentum*. Because programming concepts are unusually tightly
interdependent, early success compounds and early failure compounds —
an institutional and sequencing effect, not a gene.

The practical upshot of section 2 as a whole: programming is hard for
identifiable, teachable reasons — an unfamiliar notional machine, a skill
hierarchy that classrooms often invert by demanding writing before reading,
high intrinsic cognitive load, hostile error feedback, and tightly coupled
content where early gaps snowball. Every effective practice in this review
attacks one or more of these mechanisms.

---

## 3. Theoretical frameworks and schools of thought

Four broad traditions shape how introductory programming is taught. They are
not mutually exclusive — current best practice is best described as a
synthesis — but they make different predictions and recommend different
defaults, and recognising them helps decode disagreements between colleagues
and between papers.

### 3.1 Cognitive load theory and the explicit-instruction school

Cognitive load theory (CLT) starts from the limits of working memory: novel
information must pass through a working memory that holds only a handful of
elements, while expertise consists of schemas in long-term memory that bypass
this bottleneck (Sweller, 1988; Sweller et al., 2019). Instruction should
therefore minimise *extraneous* load (poor materials, split attention),
manage *intrinsic* load (sequence and isolate interacting elements), and
maximise the working-memory budget available for schema construction.

Programming is close to a worst case for working memory: syntax, semantics,
the notional machine, the problem domain, and the editor/tooling all interact
simultaneously (du Boulay, 1986; Hermans, 2021). CLT therefore predicts — and
the evidence confirms — that *unguided discovery is a poor default for
novices*. Kirschner, Sweller and Clark's (2006) broadside against minimally
guided instruction is frequently cited in CER, and the field's strongest
classroom results come from heavily scaffolded designs: worked examples,
subgoal labels, Parsons problems, and deliberately sequenced micro-practice
(sections 4.1–4.3).

Within this school, the *expertise reversal effect* is an important nuance:
guidance that helps novices becomes redundant or harmful as learners gain
competence, so scaffolding must fade (Sweller et al., 2019). The practical
design is example-first, then completion problems, then independent writing —
not permanent hand-holding.

### 3.2 Constructivism and constructionism

The constructivist tradition emphasises that learners actively build
knowledge from experience, and its computing-specific variant —
constructionism — holds that this building works best when learners construct
*public, personally meaningful artefacts* (Papert, 1980). This school gave
the field Logo, Scratch (Resnick et al., 2009), and the broader conviction
that programming is a medium for creative expression, not only an
engineering discipline. Its fingerprints are on project-based curricula,
creative computing, media computation (Guzdial, 2003), and the "low floor,
high ceiling, wide walls" design language of beginner tools.

The honest reading of the evidence is that constructionism wins on motivation
and breadth of participation but is insufficient as a theory of *skill
acquisition*: meaningful projects without explicit instruction reproduce the
McCracken problem (section 2.3). Conversely, pure CLT-driven drill produces
competence that students may see no reason to use. Mark Guzdial's career
arc is instructive: media computation (section 4.7) is explicitly an attempt
to keep constructionist motivation while adding structure and context
(Guzdial, 2013, 2015).

### 3.3 The sociocultural tradition: apprenticeship and community

Sociocultural theories view learning to program as enculturation into a
community of practice (Lave & Wenger, 1991), mediated by language and social
interaction (Vygotsky, 1978). *Cognitive apprenticeship* (Collins et al.,
1989) is the most directly applicable framework: experts make their thinking
visible (modelling), support learners in doing the task (coaching,
scaffolding), and progressively withdraw (fading), while learners articulate
and reflect.

This tradition underpins several practices with good evidence: live coding as
modelling of expert thought processes including mistakes (Rubin, 2013; Raj et
al., 2018), pair programming as mutual articulation (McDowell et al., 2006),
peer instruction as structured talk (Porter et al., 2013), and PRIMM, whose
authors explicitly ground the method's emphasis on classroom talk about code
in Vygotskian terms (Sentance et al., 2019). It also supplies the standard
account of *why* vocational and work-based models succeed (section 8).

### 3.4 Productive failure and the guidance debate

A fourth position complicates the explicit-instruction consensus: *productive
failure* research finds that, under specific conditions, having learners
attempt problems *before* instruction outperforms instruction-first designs,
because the struggle activates prior knowledge and makes subsequent
instruction stick (Kapur, 2008; Sinha & Kapur, 2021). The conditions matter —
the problem must be designed so learners generate multiple representations,
and the follow-up instruction must explicitly build on their attempts.

In CER this surfaces as a live tension rather than a resolved question.
The field's working synthesis is roughly: *for foundational skills (syntax,
tracing, basic constructs), guidance-first wins decisively; for design-level
and problem-solving skills, brief well-designed struggle followed by explicit
consolidation has a place*. The PRIMM "Predict" phase and peer instruction's
solo-vote-before-discussion step are both small doses of generation-before-
instruction inside an otherwise guided design.

### 3.5 A field-specific synthesis: comprehension-first instruction

Xie et al. (2019) offer the most cited recent attempt to turn all of the
above into an instructional theory specific to programming. They decompose
early programming skill into four components along two axes — reading versus
writing, and code-level semantics versus goal-directed templates: (1) trace
code, (2) write correct syntax, (3) recognise templates/plans in code, (4)
use templates to solve problems. Their theory of instruction says these four
should be *taught and assessed explicitly, in that order*, with distinct
practice types for each, rather than the traditional approach of assigning
open writing tasks and hoping all four skills co-develop.

This "comprehension-first" position — visible in PRIMM, in the
BRACElet-inspired assessment mix, and in the design of tools like Hedy and
adaptive Parsons systems — is probably the closest thing the field currently
has to a consensus model of instruction, and it is the frame this review
adopts. It is also, conveniently, the frame that survives the arrival of
generative AI best (section 9.4).

---

## 4. Evidence-based instructional practices

This section reviews the specific practices with the strongest evidence,
ordered roughly from fine-grained (exercise design) to coarse-grained (whole-
course pedagogy). For each: what it is, what the evidence says, and known
boundary conditions.

### 4.1 Worked examples and subgoal labels

**What.** A worked example presents a complete, annotated solution for study
before (or instead of) asking the learner to produce one. *Subgoal labels*
add short functional names to the steps of the example ("get user input",
"initialise accumulator", "update accumulator"), making the underlying plan
structure explicit and transferable.

**Evidence.** The worked-example effect is among the most replicated findings
in educational psychology (Sweller et al., 2019). In programming
specifically, subgoal-labelled examples improved performance and transfer in
learning App Inventor (Margulieux et al., 2012) and in textual programming
(Morrison et al., 2015). The most compelling result for practitioners: when
subgoal-labelled materials were deployed across an entire semester of CS1,
they improved quiz performance, reduced variance, and improved persistence —
with the largest benefits for the students most at risk of failing or
withdrawing (Margulieux et al., 2019, 2020).

**Boundary conditions.** Benefits concentrate in the early, procedural phase
of learning and on near-transfer tasks; effects on distant summative exams
are weaker (Margulieux et al., 2020). Per the expertise reversal effect,
examples should give way to completion problems and independent writing as
competence
grows. A practical sequence is example → modified example → completion →
full problem, which maps directly onto PRIMM and Use-Modify-Create (4.5).

### 4.2 Parsons problems

**What.** Parsons problems (Parsons & Haden, 2006) give learners a correct
solution scrambled into blocks (sometimes with distractor blocks) to arrange
in order. They isolate algorithm construction from syntax recall and typing.

**Evidence.** This is now one of the best-studied exercise types in CER. A
systematic review and an ITiCSE working group concluded that Parsons problems
deliver learning gains comparable to writing the equivalent code, at
significantly lower time cost and cognitive load — i.e., better learning
*efficiency* (Ericson et al., 2022). Adaptive variants, which adjust
difficulty or merge blocks in response to struggle, show particular promise
for keeping weaker students in the productive zone (Ericson et al., 2018). A
follow-up multi-institutional, multi-national programme is testing
generalisability (Ericson et al., 2023). Subgoal labels and Parsons problems
combine well (Morrison et al., 2016).

**Boundary conditions.** Parsons problems are practice and formative tools,
not a complete replacement for code writing; the efficiency argument is
precisely that the time saved should be reinvested in more and varied
practice. Solution-ordering tasks can be gamed by syntax cues (indentation in
Python) if not designed carefully.

### 4.3 Many small problems, deliberate practice, and drill

**What.** Replacing few large assignments with many small, immediate-feedback
exercises: one concept per item, rapid cycles, mastery thresholds.

**Evidence.** Multiple lines of work converge here. Vihavainen et al. (2014)
found that course transformations bundling small-exercise regimes with
support raised pass rates substantially. Studies of "many small programs"
versus one large program in CS1 found equal or better outcomes with lower
stress (Allen et al., 2018). Drill-oriented platforms with automated feedback
(section 6.1) make the approach scalable, and spaced, interleaved practice is
strongly supported in general learning science (Dunlosky et al., 2013).

**Boundary conditions.** Pure drill risks producing what Soloway warned
about: construct knowledge without plan knowledge. The exercise mix needs
tracing, explaining, Parsons, *and* writing items (Xie et al., 2019), and at
least some larger integrative tasks to teach decomposition (which is also
where vocational programmes' project lines come in; section 8).

### 4.4 Pair programming and peer instruction

**Pair programming** — two students, one keyboard, alternating driver and
navigator roles — has meta-analytic support: positive effects on assignment
performance, exam scores, and pass/persistence rates, though not consistently
on attitudes (Umapathy & Ritzhaupt, 2017). The classic studies found higher
retention and program quality with no harm to individual exam performance,
and benefits concentrated among less experienced students (McDowell et al.,
2006; Werner et al., 2004). Implementation details matter: enforce role
rotation, pair students of broadly similar (not identical) ability, and
teach the protocol explicitly — incompatible or free-riding pairs are the
main documented failure mode (McDowell et al., 2006).

**Peer instruction (PI)** — pre-class preparation, in-class concept questions
answered individually with clickers, peer discussion, re-vote, instructor
debrief (Crouch & Mazur, 2001) — has unusually strong evidence in computing.
Adopting PI roughly halved fail rates across four CS courses in
within-instructor comparisons (Porter et al., 2013), and a multi-institutional
study confirmed benefits across seven instructors and four institutions
(Porter et al., 2016). Students value it when implementation is faithful
(graded for participation, not correctness; genuine discussion time).

These two practices share a mechanism worth naming for colleagues: they
*force articulation*. Talking about code — naming plans, defending a
prediction — is exactly the explain-in-plain-English behaviour that section
2.3 identified as the hinge skill.

### 4.5 PRIMM and Use-Modify-Create: sequencing frameworks

**PRIMM** (Predict–Run–Investigate–Modify–Make) operationalises
comprehension-first sequencing for a single lesson or unit (Sentance et al.,
2019). Learners predict what given code does, run it to confront their
prediction, investigate it line by line (teacher-led questioning, tracing),
modify it incrementally, and only then make something new. Two design
principles do the heavy lifting: students start by *reading working code they
did not write* (lowering load and depersonalising errors), and classroom talk
is structured around the code. Evaluation in schools showed improved outcomes
for the PRIMM cohort and strong teacher uptake (Sentance et al., 2019);
while the controlled evidence is from secondary education, the underlying
mechanisms (2.3, 3.1, 3.3) are age-general, and the framework is widely and
plausibly applied in tertiary intro courses.

**Use-Modify-Create** (Lee et al., 2011) is the coarser-grained ancestor:
learners first use an existing program, then modify increasingly deeply, then
create. It remains a useful curriculum-level progression, especially for
project lines in applied programmes.

### 4.6 Live coding

Writing code live in front of students — including making and fixing
mistakes, while thinking aloud — is the cognitive-apprenticeship "modelling"
step made concrete. Comparative studies find live coding at least as
effective as static code examples (Rubin, 2013) and qualitatively better at
teaching *process*: incremental development, debugging behaviour, and the
normality of errors (Raj et al., 2018; Selvaraj et al., 2021). An empirical
ICER study confirmed benefits for process learning while cautioning that
pacing and note-taking need support (Shah et al., 2023). Practical
recommendations from this literature: go slow, narrate intentions before
typing, deliberately make typical errors, and have students predict at
decision points (a micro-PRIMM inside the lecture).

### 4.7 Media computation and contextualised computing

Guzdial's media computation — teaching introductory programming through
manipulating images, sound, and video — is the best-documented case of
*contextualisation*: anchoring all instruction in a domain students find
meaningful (Guzdial, 2003). Across more than a decade of data, media
computation courses showed dramatically improved retention of non-majors and
women compared with traditional CS1, with comparable learning (Guzdial,
2013). The general lesson is not "use multimedia" but "choose a context your
specific students value, and commit to it" (Guzdial, 2015). For web-oriented
vocational programmes, the directly analogous move is teaching programming
fundamentals through the students' actual target domain (websites, APIs,
data) rather than through abstract puzzles.

### 4.8 Program visualisation and tracing support

Tools that visualise program state — Python Tutor being the most used —
target notional-machine construction directly. Reviews conclude that
visualisation helps *when students actively engage* (predicting, annotating)
rather than passively watching animations (Sorva et al., 2013). Requiring
hand-tracing with a consistent paper protocol (memory tables) is a low-tech
equivalent with observational support: tracing skill correlates with writing
skill (Lister et al., 2004; Lopez et al., 2008), and explicit tracing
instruction is a standard recommendation (Xie et al., 2019; Hermans, 2021).

### 4.9 What does *not* have good evidence

For balance, several widespread practices lack support:

- **Weed-out framing and grading on a curve.** No learning rationale;
  reinforces fixed-ability beliefs the field has discredited (Patitsas et
  al., 2020) and measurably damages climate (section 7).
- **Syntax-first lecturing through language features** without comprehension
  practice — the traditional structure that produced the McCracken result
  (McCracken et al., 2001).
- **Unstructured group projects in semester one.** Group work without
  taught collaboration protocols mostly teaches division of labour;
  structured pairing is the evidenced alternative (Umapathy & Ritzhaupt,
  2017).
- **Aptitude screening for admission to CS1.** Predictive validity of all
  known instruments is too weak to justify gatekeeping (Robins, 2010; Bornat,
  2014; Quille & Bergin, 2019 use prediction for *support*, not selection).

---

## 5. Languages, environments, and tools

### 5.1 Does the first language matter?

Less than the decades of argument suggest, but not nothing. Watson and Li
(2014) found no significant pass-rate differences by language. What *is*
evidenced:

- **Syntax difficulty is real and measurable.** Stefik and Siebert (2013)
  found that novices rated the syntax of Java and Perl no more intuitive than
  a language with randomly generated keywords, while languages designed
  for readability (Quorum, Python, Ruby) fared significantly better. Syntax
  is not the deep difficulty (section 2), but hostile syntax adds extraneous
  load precisely when learners can least afford it.
- **The field has voted with its feet.** Python has displaced Java as the
  dominant CS1 language in most surveyed regions, on the grounds of lower
  notational overhead and broader applicability (Becker & Quille, 2019).
- **Notional-machine fit matters more than popularity.** Each language choice
  buys a different set of misconception risks (e.g., Python's dynamic typing
  postpones type discipline; JavaScript's coercions create their own
  superbugs). The recommendation in the literature is to choose deliberately
  and then *teach the machine model of that language explicitly* (Sorva,
  2013; Fincher et al., 2020), rather than to chase an ideal language.

For vocationally oriented web programmes the genuine tension is between a
pedagogically gentle first language (Python) and immediate authenticity
(JavaScript in the browser). The contextualisation evidence (section 4.7)
cuts towards authenticity; the cognitive-load evidence cuts towards
gentleness. A defensible reading: either can work, but the JavaScript route
demands more aggressive scaffolding of its rough edges (coercion, async,
the DOM as implicit state).

### 5.2 Blocks, text, and hybrid approaches

Block-based environments (Scratch) remove syntax errors entirely and have
strong evidence at school level (Resnick et al., 2009; Weintrop & Wilensky,
2017). Weintrop and Wilensky's comparative study found blocks gave faster
early learning, with the gap closing over time, and recommended hybrid
pathways. For young adults, pure block environments are usually a poor fit
for identity reasons (perceived as childish, low authenticity), but the
*principle* — gradually introducing syntax — survives in other forms:

- **Hedy**, a "gradual" language that adds syntax rules level by level until
  it becomes Python, was designed explicitly on cognitive-load grounds
  (Hermans, 2020) and is being evaluated as a CS1 on-ramp for tertiary
  audiences as well.
- **Frame-based editing** (Stride) occupies a middle point between blocks and
  text (Kölling et al., 2015).
- **Subset-first teaching** in an ordinary language — deliberately
  restricting the construct set and idiom palette in early weeks — achieves
  much of the same load management without special tooling and is implicit
  in most well-designed CS1 materials.

### 5.3 Error messages and novice-friendly tooling

Programming error messages are a major, well-documented novice barrier;
design guidelines exist (increase readability, provide context, show
examples, use positive tone) but mainstream toolchains adopted them slowly
(Becker et al., 2019). Practical mitigations with evidence or strong face
validity: choose toolchains with enhanced messages (modern Python tracebacks,
Elm-style compilers, educational IDEs such as Thonny), teach students
explicitly how to read error messages as a named lesson, and — recently —
use
LLMs to translate messages into actionable explanations, which measurably
improves comprehensibility (Leinonen et al., 2023; section 9.3).

Environment choice follows the same logic as language choice: minimise
incidental complexity early (one-click run, visible state, no build systems),
then deliberately introduce professional tooling (the editor, the terminal,
version control) as *content*, not as assumed background. For
associate-degree audiences heading into industry, tooling fluency is a
learning outcome in its own right, but the literature cautions against
front-loading it (du Boulay's "pragmatics" difficulties compound the others
if introduced simultaneously).

---

## 6. Feedback and assessment

### 6.1 Automated assessment and formative feedback

Automated assessment of programming exercises is mature technology with a
large literature (Ihantola et al., 2010; Paiva et al., 2022). Its educational
value depends entirely on *what the feedback says and when*. The general
principles from educational research hold: feedback is among the strongest
influences on achievement, but its effect depends on addressing the task,
the process, and self-regulation rather than the self (Hattie & Timperley,
2007); formative, low-stakes assessment drives learning (Black & Wiliam,
1998).

Keuning, Jeuring and Heeren's (2018) systematic review of automated feedback
generation found most tools overwhelmingly give *knowledge of results*
(pass/fail on tests) and far less of the more valuable *knowledge about how
to proceed* — hints, next steps, error localisation. The practical
recommendations that follow: instant test-based feedback is good but
insufficient; pair autograders with human feedback moments (code review,
labs); and write test feedback messages as teaching text, not assertions.
LLM-based hint generation is now changing this equation (section 9.3).

Two cautions recur in this literature. First, autograder-driven courses can
induce "shotgun debugging" — students iterating against the grader rather
than reasoning; submission limits, hidden tests, or reflection prompts
mitigate this. Second, what is graded signals what matters: grading only
functional correctness teaches students that code quality, readability, and
testing are optional (Stegeman et al., 2014 propose rubrics for code quality
in CS1).

### 6.2 Aligning assessment with the skill hierarchy

Constructive alignment (Biggs, 1996) plus the skill-hierarchy evidence
(section 2.3) yields a concrete prescription: assessments in early
programming should *explicitly* include tracing items, explain-in-plain-
English items, Parsons items, fix-this-code items, and writing items — not
writing alone. The BRACElet project demonstrated such mixed exams and their
diagnostic value (Whalley et al., 2006; Lopez et al., 2008). Mixed-item
exams also de-risk the failure cliff: students with partial mastery can
demonstrate it, which matters for the momentum effects described by Robins
(2010).

On the summative side, the integrity pressures of take-home programming work
predate generative AI but are now acute (section 9.5). The emerging
consensus combines authentic, collaborative, AI-permitted project work for
formative and competence-building purposes with controlled-conditions
demonstrations of individual fluency — lab exams, oral explanations of one's
own code ("defence"), or in-class writing — for certification of individual
skill (Denny et al., 2024a; Prather et al., 2023).

### 6.3 Mastery and pacing structures

Because programming knowledge is unusually sequential (Robins, 2010),
assessment structures that *force closure of gaps* outperform structures that
let deficits accumulate silently. Approaches with support in the literature
include mastery-based exam retakes, gateway tests of basic fluency (e.g.,
must pass a basic code-writing check to proceed), and frequent low-stakes
testing whose primary function is information, not grading. The
test-enhanced-learning literature supports frequent retrieval practice in
general (Dunlosky et al., 2013), and CS-specific implementations of
mastery learning report reduced failure tails, though the controlled evidence
base is thinner here than for the practices in section 4.

---

## 7. Motivation, affect, and equity

Cognitive design is necessary but not sufficient: a large fraction of CS1
attrition is affective, and the affective findings are among the most
actionable in the literature.

### 7.1 Self-efficacy: the strongest affective predictor

Programming self-efficacy — a student's belief in their own capability to
program (Bandura, 1997) — correlates with and predicts CS1 outcomes more
strongly than most cognitive background variables (Ramalingam et al., 2004).
In the best-validated early-prediction model for CS1 (PreSS), programming
self-efficacy is the dominant factor, alongside prior mathematics performance
— and the model's authors emphasise using prediction to trigger *support*,
not selection (Quille & Bergin, 2019). Self-efficacy is also dynamic: it is
built or destroyed by the texture of early experiences — mastery experiences
being the strongest source — which links it directly to the design choices
above. Many small early successes (4.3), scaffolded tasks that students
complete (4.1–4.2), and error messages that don't humiliate (5.3) are
self-efficacy interventions whether or not they are framed that way
(Kinnunen & Simon, 2012, document how routine assignment experiences erode
computing freshmen's self-efficacy in ways instructors never see).

### 7.2 Mindset: important idea, mixed evidence

Students who believe programming ability is fixed respond to early struggle
by disengaging; those who hold a growth mindset interpret struggle as normal
(Dweck, 2006). CS-specific findings: mindsets about programming
are domain-specific and correlate with practice behaviour (Scott & Ghinea,
2014), and an early intervention study reported benefits of mindset training
in CS1 (Cutts et al., 2010). However, large general-education RCTs and
meta-analyses show small and conditional effects of standalone mindset
interventions. The current reading for practice: do not buy a mindset
*programme*; instead remove the classroom signals that teach fixedness —
geek-gene talk, curve grading, public early rankings — and normalise struggle
explicitly (Patitsas et al., 2020; section 2.6). Messaging matters most when
it comes from how the course actually behaves (retakes exist; early failure
is recoverable), not from posters.

### 7.3 Belonging, climate, and who leaves

The classic qualitative work documented how introductory computing
environments signal who belongs: Margolis and Fisher (2002) at CMU showed
how a curriculum and culture tuned to previous hobbyist experience drove out
capable women (a compact article version of the argument is Fisher &
Margolis, 2002); Barker and Garvin-Doxas (2004) documented "defensive
climates"
in CS classrooms — status jockeying, impersonal interaction, public
correction — that depress participation unevenly. Environmental cues as
subtle as decor shift women's reported interest in CS (Cheryan et al., 2009).
Prior programming experience creates a visible early hierarchy in CS1 that is
routinely misread as talent; structurally separating experienced beginners
(placement, honours tracks) or neutralising the advantage (contexts novel to
everyone, as in media computation) are the documented countermeasures
(Margolis & Fisher, 2002; Guzdial, 2013).

For an associate-degree audience, this literature matters in a specific way:
many students arrive via non-traditional routes with weaker academic
self-concept, and the population is more diverse on most dimensions than
bachelor CS intakes (Lyon & Denner, 2016). Climate effects compound there.

### 7.4 Predicting and catching students early

Given learning edge momentum (Robins, 2010), the highest-leverage moment for
intervention is weeks 2–6. Validated early predictors (PreSS; early
formative performance; engagement telemetry from autograders) can flag
at-risk students with usable accuracy (Quille & Bergin, 2019). The
intervention evidence (Vihavainen et al., 2014) favours structural support —
extra scheduled practice with help present, peer support structures, mastery
gates with retakes — over exhortation. Crucially, prediction without an
attached support pathway merely produces self-fulfilling labels; the PreSS
authors are explicit on this point.

---

## 8. The associate-degree and vocational context

### 8.1 An underrepresented population in the literature

Most CER is conducted on bachelor students at research universities. Evidence
specifically about associate-degree/short-cycle tertiary populations (EQF
level 5; *graduaat* in Flanders; community colleges in the US; foundation
degrees in the UK) is comparatively thin, which is itself a documented
problem given that, in the US, a large share of computing students pass
through community colleges (Lyon & Denner, 2016). The ACM Committee for
Computing Education in Community Colleges publishes curricular guidance for
associate-degree computing programmes, including transfer-oriented CS
(ACM CCECC, 2017), and the joint ACM/IEEE *Computing Curricula 2020* report
explicitly includes associate-degree and vocational profiles (CC2020 Task
Force, 2020).

What the available research says about these learners as a population:
motivations are more directly vocational (employment, career change);
mathematics anxiety and prior academic setbacks are more prevalent; external
constraints (work, family, finances) shape persistence at least as much as
course difficulty; and real-world applicability is a stronger motivational
lever than abstract intellectual challenge (Lyon & Denner, 2016). None of
this implies lower ceilings; transfer students who complete bachelor
programmes perform comparably to direct entrants.

### 8.2 Design frameworks that fit the vocational profile

Two instructional-design traditions are particularly suited to
practice-oriented programmes and are well grounded theoretically:

- **Cognitive apprenticeship** (Collins et al., 1989): modelling, coaching,
  scaffolding, articulation, reflection, exploration — with the explicit goal
  of teaching the *processes* experts use. Live coding, code review, think-
  aloud debugging demonstrations, and studio formats are its classroom
  instantiations (sections 3.3, 4.6). Situated learning theory adds that
  identity formation — coming to see oneself as a developer — happens
  through
  legitimate peripheral participation in authentic practice (Lave & Wenger,
  1991), which is what work placements, real clients, and open-source
  contributions operationalise.
- **Four-component instructional design (4C/ID)** (van Merriënboer &
  Kirschner, 2018): organise the curriculum around whole authentic tasks of
  increasing complexity (not isolated topics), with supportive information,
  procedural information just in time, and part-task practice for routine
  skills. 4C/ID was developed for complex professional skills and maps
  remarkably cleanly onto programming education: the "part-task practice"
  slot is exactly where drill, Parsons problems, and katas belong, while the
  whole-task line carries projects of growing realism. It is also the
  dominant design model in Dutch-language vocational higher education, which
  makes it a natural shared vocabulary for Flemish colleagues.

The synthesis for a graduaat-style programme: a *dual spine*. One spine of
whole, authentic, increasingly complex tasks (4C/ID; situated identity
formation), and one spine of deliberately scheduled part-task practice and
comprehension work (CLT; section 4). The most common failure modes are
running only the first spine ("projects from day one" — which reproduces the
McCracken problem and overloads weaker students) or only the second
("exercises forever" — which demotivates exactly this population).

### 8.3 Work-based learning and employability

Vocational programmes' distinctive asset is structured workplace learning.
The general evidence on internships and work-integrated learning shows
benefits for employability and motivation; the CER-specific literature is
sparse but consistent with it. Two evidence-aligned recommendations: first,
prepare students for workplace code *before* the placement — code reading at
scale, version control collaboration, asking-for-help protocols — because
placements presume exactly the skills (reading unfamiliar code, tooling
fluency) that intro courses underemphasise (sections 2.3, 5.3). Second,
debrief placements reflectively (articulation/reflection in cognitive-
apprenticeship terms) so workplace experience consolidates into transferable
knowledge rather than remaining episodic.

### 8.4 Implications of the general evidence, re-weighted

Almost everything in sections 4–7 applies with at most re-weighting:

- Scaffolding-heavy practices (worked examples, subgoals, Parsons, PRIMM)
  are *more* important, not less, for students with weaker academic
  preparation — these are precisely the practices whose largest effects were
  measured in at-risk groups (Margulieux et al., 2020).
- Contextualisation (4.7) is non-negotiable: tasks should visibly belong to
  the target occupation from early on.
- Affective design (7.1–7.3) carries extra weight given the population's
  prior-setback profile.
- Pacing structures with recovery paths (6.3) fit a population whose external
  lives interrupt study more often.

---

## 9. Programming education in the era of generative AI

No development since the personal computer has destabilised programming
education as quickly as code-generating LLMs. This section reviews the
2022–2026 literature: the capability shock, documented risks, documented
opportunities, curricular redesigns, and the emerging working consensus.

### 9.1 The capability shock

Finnie-Ansley et al. (2022) showed that OpenAI Codex — the model behind early
GitHub Copilot — scored better than the median student on real CS1 exams and
ranked in the top quartile, solving most variants of classic intro problems.
A follow-up found similar results for CS2 (Finnie-Ansley et al., 2023).
Current models far exceed those baselines. The implication was stated bluntly
across the field: every traditional take-home code-writing assessment now
measures, at best, a student's willingness not to use a freely available
tool (Denny et al., 2024a; Becker et al., 2023; Prather et al., 2023).

Two large ITiCSE working groups mapped the terrain: "The Robots Are Here"
documented capabilities, student and instructor attitudes, and immediate
challenges (Prather et al., 2023); the 2024 follow-up, "Beyond the Hype",
systematically reviewed the by-then exploding literature on tools, teaching
practices, and research findings (Prather et al., 2024b). Instructor
reactions initially split between attempts to ban or block and attempts to
integrate; longitudinal interview work found positions converging on
integration-with-guardrails as banning proved unenforceable and
misaligned with industry practice (Lau & Guo, 2023).

### 9.2 Documented risks for novices

The risk literature has moved from speculation to evidence:

- **Over-reliance and the illusion of competence.** In observational and
  eye-tracking studies of novices solving problems with GenAI, Prather et
  al. (2024a) found a clear split: well-prepared students used AI to
  accelerate, while struggling students cycled through AI suggestions
  without understanding, *believed they were progressing*, and finished with
  inflated estimates of their own ability. The authors warn of a "widening
  gap" between the two groups — a finding directly reminiscent of learning
  edge momentum (Robins, 2010), now with a compounding tool.
- **Metacognitive load shifts.** Working with an AI assistant does not
  remove difficulty; it relocates it to prompt formulation, output
  evaluation, and knowing-when-to-trust — skills novices lack most
  (Prather et al., 2024a; Margulieux et al., 2024). Margulieux et al. (2024)
  found that students with lower self-efficacy and higher fear of failure
  used LLMs in less productive ways, suggesting the affective variables of
  section 7 also moderate AI use.
- **Skill atrophy versus skill never-formed.** For professionals, AI
  assistance automates skills they already possess; for novices, it can
  prevent the formation of those skills. Controlled evidence is still
  accumulating, but studies of novices learning *with* code generators show
  the risk is conditional, not automatic: in a controlled experiment with
  young novices, scaffolded Codex access improved task performance without
  harming subsequent manual performance — and learners with stronger prior
  conceptual knowledge benefited most (Kazemitabaar et al., 2023).
- **Integrity and signal collapse in assessment.** Self-explanatory; see 9.5.

### 9.3 Documented opportunities

The opportunity literature is equally concrete:

- **Scalable, guarded help.** Purpose-built LLM tutors that refuse to emit
  full solutions and instead explain, hint, and ask questions have been
  deployed at course scale with broadly positive results: CodeHelp across a
  semester of CS1 (Liffiton et al., 2024), CodeAid with 700 students,
  including design lessons on balancing helpfulness against cognitive
  engagement (Kazemitabaar et al., 2024), and Harvard's CS50 "duck"
  deployment (Liu et al., 2024). Common findings: heavy student uptake
  concentrated around assignments and around moments when human help is
  unavailable; students value 24/7 non-judgemental help; guardrails are
  imperfect but meaningfully shape behaviour.
- **Better error messages and explanations.** LLMs reliably improve the
  comprehensibility of programming error messages (Leinonen et al., 2023)
  and can generate line-by-line code explanations of usable quality (MacNeil
  et al., 2023; Sarsa et al., 2022).
- **Content generation for instructors.** LLMs generate practice exercises,
  test cases, and worked explanations cheaply and at acceptable quality with
  human review (Sarsa et al., 2022) — directly serving the "many small
  problems" regime (4.3) and personalised contexts (4.7).
- **New exercise types.** "Prompt Problems" invert the task: students are
  given a visual/behavioural specification and must construct a prompt that
  makes an LLM produce correct code, forcing precise specification and
  output evaluation (Denny et al., 2024b). Such tasks exercise exactly the
  comprehension-and-evaluation skills the field already valued.

### 9.4 Curricular responses: what changes, what doesn't

The most-cited full-course redesign is CS1-LLM at UC San Diego: a CS1 that
embraces LLM assistance from week one, de-emphasising syntax production and
re-centering the course on problem decomposition, testing, and code reading,
with creative open-ended projects; outcomes and student reception were
broadly positive, with honest reporting of open concerns (Vadaparty et al.,
2024). Porter and Zingaro's (2023) textbook takes the same stance. At the
other pole, many programmes retain an AI-restricted foundational phase on
the skill-formation argument of 9.2. The working-group syntheses chart a
middle path that most of the literature now endorses (Denny et al., 2024a;
Prather et al., 2024b):

1. **The learning objectives shift in emphasis, not in kind.** Reading,
   tracing, explaining, decomposing, specifying, and testing were already the
   evidence-backed core (sections 2.3, 3.5); AI makes unguided code
   *writing* cheaper while making code *judgement* more valuable.
2. **Explicit AI literacy joins the curriculum.** Knowing what models do,
   where they fail, how to prompt, and how to verify output becomes a taught,
   assessed outcome — not an assumed skill (Prather et al., 2024b; Denny et
   al., 2024a).
3. **Process becomes visible.** Whether AI-permitted or not, courses
   increasingly assess the development process (commits, reflections,
   explanations, oral defences) rather than only artefacts.
4. **A protected fluency core remains.** Nearly all positions — including
   the integrationists — retain some controlled-conditions demonstration
   that the student can read, trace, and produce basic code unaided, on the
   argument that evaluation of AI output presupposes exactly this fluency
   (Vadaparty et al., 2024 retain invigilated exams; Denny et al., 2024a).

### 9.5 Assessment under generative AI

The working consensus described in 6.2 sharpens here. Unsupervised
code-writing for marks is no longer a valid measure of individual capability
(Prather et al., 2023). Responses documented in the literature: a shift of
summative weight to invigilated or oral formats; "explain your own code"
defences; process-based and contribution-based grading for project work; and
explicit AI-use policies that distinguish phases of the curriculum (forbidden
/ permitted-with-disclosure / required) rather than blanket rules. The
integrity literature emphasises that policy clarity plus authentic
AI-permitted tasks reduces violations better than detection arms races,
since AI-text detectors are unreliable for code and unfair to non-native
speakers.

### 9.6 What is genuinely unknown

Honest gaps, as of mid-2026: long-term effects of AI-integrated CS1 on
second- and third-year performance are only beginning to be measured;
optimal timing of AI introduction (week 1 versus after a fluency gate) lacks
controlled comparison; effects on the at-risk and vocational populations of
section 8 are nearly unstudied — the widening-gap result (Prather et al.,
2024a) suggests these students have the most to lose from unscaffolded AI
access and possibly the most to gain from guarded tutors; and the tools
themselves change faster than the research cycle. Any policy adopted now
should be explicitly provisional.

---

## 10. Synthesis: trends and trajectories

Five trends summarise where the field has moved and is moving.

**From writing-first to comprehension-first.** The single clearest through-
line from McCracken et al. (2001) to the LLM era: reading, tracing, and
explaining code are foundational, teachable, and were historically skipped.
Frameworks (PRIMM, Use-Modify-Create), exercise types (Parsons, EiPE), and
theory (Xie et al., 2019) all institutionalise this. Generative AI completes
the inversion: judgement about code is now the core occupational skill.

**From innate-talent beliefs to instructional accountability.** The geek-gene
position has been empirically dismantled (Patitsas et al., 2020; Bornat,
2014), failure rates are shown to respond to instruction (Vihavainen et al.,
2014; Porter et al., 2013), and the field's institutions now treat high
failure as a design problem, not a filter working as intended.

**From folk pedagogy to evidence and theory.** The maturation of CER —
multi-institutional replications, meta-analyses, working groups, and imported
theory (CLT, self-efficacy, apprenticeship) — means a lecturer in 2026 can
assemble a course from components with quantified track records, which was
not true in 2005 (Fincher & Robins, 2019; Luxton-Reilly et al., 2018).

**From de-contextualised puzzles to situated, authentic practice.** Media
computation, contextualised CS1s, project spines, and work-based learning all
reflect the same finding: meaning drives persistence, especially for students
outside the traditional hobbyist profile (Guzdial, 2013; Lyon & Denner,
2016). The vocational sector is, in this specific sense, ahead of the
research universities rather than behind them.

**The AI inflection.** 2022–2026 forced the fastest re-evaluation in the
field's history. The emerging settlement — protected fluency core, explicit
AI literacy, judgement-centred objectives, process-visible assessment,
guarded AI help at scale — is coherent with, not a break from, the previous
forty years of evidence. The open question is distributional: whether AI
narrows or widens the gap between strong and struggling beginners, and the
early evidence says this depends almost entirely on scaffolding (Prather et
al., 2024a; Kazemitabaar et al., 2023).

---

## 11. Recommendations for practice

Condensed, opinionated, and traceable to the sections above. For a first
programming semester at bachelor or graduaat level:

1. **Sequence comprehension before production.** Run lessons on a
   PRIMM-like cycle; assess tracing and explaining explicitly (§2.3, §4.5).
2. **Scaffold hard, fade deliberately.** Worked examples with subgoal
   labels → Parsons → completion → writing, per topic (§4.1–4.2).
3. **Use many small exercises with instant feedback**, mixed item types,
   plus one growing authentic project line (§4.3, §8.2).
4. **Teach the notional machine explicitly** — tracing protocols, state
   diagrams, visualisers — and teach error-message reading as content
   (§2.2, §5.3).
5. **Model process live.** Live-code with mistakes and narration; show
   debugging as a discipline, not an embarrassment (§4.6).
6. **Structure collaboration.** Pair programming with taught protocols and
   role rotation; peer instruction for concept-heavy sessions (§4.4).
7. **Design for self-efficacy.** Early wins, recoverable failure, retakes,
   no curve, no geek-gene messaging (§7.1–7.2, §6.3).
8. **Watch weeks 2–6.** Use early formative data to trigger structural
   support, not labels (§7.4).
9. **Adopt an explicit, phased AI policy.** A protected unaided-fluency
   core with invigilated checks; guarded AI tutoring for help; AI-permitted
   authentic work with disclosure and process assessment; taught AI
   literacy (§9.4–9.5).
10. **Contextualise relentlessly** in the students' target occupation, and
    prepare them for workplace code before placements (§4.7, §8.3).

## 12. Limitations of this review

This is a narrative review with the usual risks: selection bias towards
well-cited Anglophone venues; under-coverage of non-English literatures and
of grey literature from vocational education; and a fast-moving target in
section 9, where conclusions may date within a year or two. Findings from
secondary education were occasionally imported where tertiary evidence is
thin (notably PRIMM and parts of the blocks/text literature) and are flagged
as such. The associate-degree evidence gap (§8.1) means several
recommendations for that context are theory-driven extrapolations rather
than directly measured effects — which is precisely the research opportunity
for an educational-sciences project.

---

## Appendix: finding the sources via the OU library

Availability of the cited sources was checked against the Open Universiteit
library (bibliotheek.ou.nl) in June 2026. Access routes, in order of how much
of this bibliography they cover:

- **ACM Digital Library** (via *Databases* on the library portal). Covers
  roughly half of the bibliography: all SIGCSE, ITiCSE, ICER, Koli Calling,
  and ACE conference papers and working-group reports, plus *ACM Transactions
  on Computing Education*, *Communications of the ACM*, *ACM Inroads*, and
  the *SIGCSE Bulletin*. The ACM Digital Library completed its transition to
  full open access, so these papers are also reachable without a library
  login at https://dl.acm.org. Note that individual conference papers do
  *not* appear in the portal's Quick Search — go to the ACM Digital Library
  itself and search there.
- **Taylor & Francis Online**. Covers *Computer Science Education* (Sentance,
  Xie, Robins, Quille & Bergin, Kinnunen & Simon, Barker & Garvin-Doxas,
  Robins et al. 2003), *Educational Psychologist* (Kirschner et al.),
  *Cognition and Instruction* (Kapur), and *Assessment in Education* (Black
  & Wiliam). Full text verified, including the back volumes.
- **SpringerLink**: *Educational Psychology Review* (Sweller et al.),
  *Higher Education* (Biggs). The *International Journal of STEM Education*
  (Margulieux et al., 2020) is open access in any case.
- **SAGE Journals Online**: *Psychological Science in the Public Interest*
  (Dunlosky et al.), *Review of Educational Research* (Sinha & Kapur).
- **EBSCO (PsycARTICLES)**: *Journal of Personality and Social Psychology*
  (Cheryan et al.) — found via Quick Search, full text available.
- **Quick Search** (WorldCat Discovery) works well for journal articles in
  general; for anything ACM, search the ACM Digital Library directly.

**Not available through the OU library**, with workable alternatives:

- Crouch & Mazur (2001), *American Journal of Physics* — not licensed. A
  free author copy circulates via the Mazur group's Harvard page and Google
  Scholar.
- Scott & Ghinea (2014), *IEEE Transactions on Education* — the OU licenses
  the IEEE *Computer Society* library only, which excludes this journal. An
  author copy is findable via Google Scholar.
- du Boulay (1986) and Pea (1986), *Journal of Educational Computing
  Research* — the SAGE backfile for this journal is not licensed. Both
  papers are reprinted in Soloway and Spohrer's collection *Studying the
  Novice Programmer* (1989) and author copies circulate; the secondary
  literature (Robins et al., 2003; Sorva, 2013 — both accessible) summarises
  them faithfully.
- **Books are generally not in the OU e-collection.** This affects Papert
  (1980), Bandura (1997), Lave & Wenger (1991), Vygotsky (1978), Margolis &
  Fisher (2002), Dweck (2006), Fincher & Robins (2019), van Merriënboer &
  Kirschner (2018), Hermans (2021), Guzdial (2015), and Porter & Zingaro
  (2023). Partial workarounds, checked in June 2026:
  - An **O'Reilly Learning** subscription (learning.oreilly.com) carries
    Hermans (2021), *The programmer's brain* (also as audiobook and video
    edition) and Porter & Zingaro, *Learn AI-assisted Python programming*
    (the first edition cited here and a second edition). The
    academic-press titles (MIT Press, Routledge, Cambridge, Basic Books)
    are not on O'Reilly.
  - For Margolis & Fisher, the article version (Fisher & Margolis, 2002,
    in the *SIGCSE Bulletin*) is accessible via the ACM Digital Library and
    covers the core argument.
  - For the rest: inter-library loan via the library portal, or the usual
    acquisition routes.

---

## References

*Formatting note: APA 7th edition. Page ranges for conference papers are
deliberately omitted where they could not be verified; DOIs are given only
where verified. Complete them from the ACM Digital Library or the publisher
before formal use.*

ACM Committee for Computing Education in Community Colleges. (2017).
*Computer science curricular guidance for associate-degree transfer programs
with infused cybersecurity*. ACM.

Allen, J. M., Vahid, F., Downey, K., & Edgcomb, A. D. (2018). Weekly
programs in a CS1 class: Experiences with auto-graded many-small programs
(MSP). In *Proceedings of the 49th ACM Technical Symposium on Computer
Science Education (SIGCSE '18)*. ACM.

Altadmri, A., & Brown, N. C. C. (2015). 37 million compilations:
Investigating novice programming mistakes in large-scale student data. In
*Proceedings of the 46th ACM Technical Symposium on Computer Science
Education (SIGCSE '15)*. ACM.

Bandura, A. (1997). *Self-efficacy: The exercise of control*. W. H. Freeman.

Barker, L. J., & Garvin-Doxas, K. (2004). Making visible the behaviors that
influence learning environment: A qualitative exploration of computer
science classrooms. *Computer Science Education, 14*(2), 119–145.

Becker, B. A., Denny, P., Finnie-Ansley, J., Luxton-Reilly, A., Prather, J.,
& Santos, E. A. (2023). Programming is hard — or at least it used to be:
Educational opportunities and challenges of AI code generation. In
*Proceedings of the 54th ACM Technical Symposium on Computer Science
Education (SIGCSE '23)*. ACM. https://doi.org/10.1145/3545945.3569759

Becker, B. A., Denny, P., Pettit, R., Bouchard, D., Bouvier, D. J.,
Harrington, B., Kamil, A., Karkare, A., McDonald, C., Osera, P.-M., Pearce,
J. L., & Prather, J. (2019). Compiler error messages considered unhelpful:
The landscape of text-based programming error message research. In
*Proceedings of the Working Group Reports on Innovation and Technology in
Computer Science Education (ITiCSE-WGR '19)*. ACM.
https://doi.org/10.1145/3344429.3372508

Becker, B. A., & Quille, K. (2019). 50 years of CS1 at SIGCSE: A review of
the evolution of introductory programming education research. In
*Proceedings of the 50th ACM Technical Symposium on Computer Science
Education (SIGCSE '19)*. ACM.

Bennedsen, J., & Caspersen, M. E. (2007). Failure rates in introductory
programming. *ACM SIGCSE Bulletin, 39*(2), 32–36.

Bennedsen, J., & Caspersen, M. E. (2019). Failure rates in introductory
programming: 12 years later. *ACM Inroads, 10*(2), 30–36.

Biggs, J. (1996). Enhancing teaching through constructive alignment.
*Higher Education, 32*(3), 347–364. https://doi.org/10.1007/BF00138871

Black, P., & Wiliam, D. (1998). Assessment and classroom learning.
*Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74.
https://doi.org/10.1080/0969595980050102

Bornat, R. (2014). *Camels and humps: A retraction*. School of Science and
Technology, Middlesex University.

Brown, N. C. C., & Altadmri, A. (2017). Novice Java programming mistakes:
Large-scale data vs. educator beliefs. *ACM Transactions on Computing
Education, 17*(2), Article 7. https://doi.org/10.1145/2994154

CC2020 Task Force. (2020). *Computing Curricula 2020: Paradigms for global
computing education*. ACM/IEEE Computer Society.
https://doi.org/10.1145/3467967

Cheryan, S., Plaut, V. C., Davies, P. G., & Steele, C. M. (2009). Ambient
belonging: How stereotypical cues impact gender participation in computer
science. *Journal of Personality and Social Psychology, 97*(6), 1045–1060.
https://doi.org/10.1037/a0016239

Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship:
Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick
(Ed.), *Knowing, learning, and instruction: Essays in honor of Robert
Glaser* (pp. 453–494). Lawrence Erlbaum Associates.

Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience
and results. *American Journal of Physics, 69*(9), 970–977.
https://doi.org/10.1119/1.1374249

Cutts, Q., Cutts, E., Draper, S., O'Donnell, P., & Saffrey, P. (2010).
Manipulating mindset to positively influence introductory programming
performance. In *Proceedings of the 41st ACM Technical Symposium on Computer
Science Education (SIGCSE '10)*. ACM.

Denny, P., Prather, J., Becker, B. A., Finnie-Ansley, J., Hellas, A.,
Leinonen, J., Luxton-Reilly, A., Reeves, B. N., Santos, E. A., & Sarsa, S.
(2024a). Computing education in the era of generative AI. *Communications of
the ACM, 67*(2), 56–67. https://doi.org/10.1145/3624720

Denny, P., Leinonen, J., Prather, J., Luxton-Reilly, A., Amarouche, T.,
Becker, B. A., & Reeves, B. N. (2024b). Prompt Problems: A new programming
exercise for the generative AI era. In *Proceedings of the 55th ACM
Technical Symposium on Computer Science Education (SIGCSE '24)*. ACM.

du Boulay, B. (1986). Some difficulties of learning to program. *Journal of
Educational Computing Research, 2*(1), 57–73.
https://doi.org/10.2190/3LFX-9RRF-67T8-UVK9

Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham,
D. T. (2013). Improving students' learning with effective learning
techniques: Promising directions from cognitive and educational psychology.
*Psychological Science in the Public Interest, 14*(1), 4–58.
https://doi.org/10.1177/1529100612453266

Dweck, C. S. (2006). *Mindset: The new psychology of success*. Random House.

Ericson, B. J., Denny, P., Prather, J., Duran, R., Hellas, A., Leinonen, J.,
Miller, C. S., Morrison, B. B., Pearce, J. L., & Rodger, S. H. (2022).
Parsons problems and beyond: Systematic literature review and empirical
study designs. In *Proceedings of the 2022 Working Group Reports on
Innovation and Technology in Computer Science Education (ITiCSE-WGR '22)*.
ACM.

Ericson, B. J., Denny, P., Prather, J., et al. (2023). Multi-institutional
multi-national studies of Parsons problems. In *Proceedings of the 2023
Working Group Reports on Innovation and Technology in Computer Science
Education (ITiCSE-WGR '23)*. ACM.
https://doi.org/10.1145/3623762.3633498

Ericson, B. J., Foley, J. D., & Rick, J. (2018). Evaluating the efficiency
and effectiveness of adaptive Parsons problems. In *Proceedings of the 2018
ACM Conference on International Computing Education Research (ICER '18)*.
ACM.

Fincher, S., Jeuring, J., Miller, C. S., Donaldson, P., du Boulay, B.,
Hauswirth, M., Hellas, A., Hermans, F., Lewis, C., Mühling, A., Pearce,
J. L., & Petersen, A. (2020). Notional machines in computing education: The
education of attention. In *Proceedings of the Working Group Reports on
Innovation and Technology in Computer Science Education (ITiCSE-WGR '20)*.
ACM. https://doi.org/10.1145/3437800.3439202

Fincher, S. A., & Robins, A. V. (Eds.). (2019). *The Cambridge handbook of
computing education research*. Cambridge University Press.
https://doi.org/10.1017/9781108654555

Finnie-Ansley, J., Denny, P., Becker, B. A., Luxton-Reilly, A., & Prather,
J. (2022). The robots are coming: Exploring the implications of OpenAI Codex
on introductory programming. In *Proceedings of the 24th Australasian
Computing Education Conference (ACE '22)* (pp. 10–19). ACM.
https://doi.org/10.1145/3511861.3511863

Finnie-Ansley, J., Denny, P., Luxton-Reilly, A., Santos, E. A., Prather, J.,
& Becker, B. A. (2023). My AI wants to know if this will be on the exam:
Testing OpenAI's Codex on CS2 programming exercises. In *Proceedings of the
25th Australasian Computing Education Conference (ACE '23)*. ACM.

Fisher, A., & Margolis, J. (2002). Unlocking the clubhouse: The Carnegie
Mellon experience. *ACM SIGCSE Bulletin, 34*(2), 79–83.

Guzdial, M. (2003). A media computation course for non-majors. In
*Proceedings of the 8th Annual Conference on Innovation and Technology in
Computer Science Education (ITiCSE '03)*. ACM.

Guzdial, M. (2013). Exploring hypotheses about media computation. In
*Proceedings of the Ninth Annual International ACM Conference on
International Computing Education Research (ICER '13)*. ACM.

Guzdial, M. (2015). *Learner-centered design of computing education:
Research on computing for everyone*. Morgan & Claypool.

Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of
Educational Research, 77*(1), 81–112.
https://doi.org/10.3102/003465430298487

Hermans, F. (2020). Hedy: A gradual language for programming education. In
*Proceedings of the 2020 ACM Conference on International Computing Education
Research (ICER '20)*. ACM. https://doi.org/10.1145/3372782.3406262

Hermans, F. (2021). *The programmer's brain: What every programmer needs to
know about cognition*. Manning.

Ihantola, P., Ahoniemi, T., Karavirta, V., & Seppälä, O. (2010). Review of
recent systems for automatic assessment of programming assignments. In
*Proceedings of the 10th Koli Calling International Conference on Computing
Education Research (Koli Calling '10)*. ACM.

Kapur, M. (2008). Productive failure. *Cognition and Instruction, 26*(3),
379–424. https://doi.org/10.1080/07370000802212669

Kazemitabaar, M., Chow, J., Ma, C. K. T., Ericson, B. J., Weintrop, D., &
Grossman, T. (2023). Studying the effect of AI code generators on
supporting novice learners in introductory programming. In *Proceedings of
the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23)*.
ACM. https://doi.org/10.1145/3544548.3580919

Kazemitabaar, M., Ye, R., Wang, X., Henley, A. Z., Denny, P., Craig, M., &
Grossman, T. (2024). CodeAid: Evaluating a classroom deployment of an
LLM-based programming assistant that balances student and educator needs. In
*Proceedings of the 2024 CHI Conference on Human Factors in Computing
Systems (CHI '24)*. ACM. https://doi.org/10.1145/3613904.3642773

Keuning, H., Jeuring, J., & Heeren, B. (2018). A systematic literature
review of automated feedback generation for programming exercises. *ACM
Transactions on Computing Education, 19*(1), Article 3.
https://doi.org/10.1145/3231711

Kinnunen, P., & Simon, B. (2012). My program is ok — am I? Computing
freshmen's experiences of doing programming assignments. *Computer Science
Education, 22*(1), 1–28.

Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance
during instruction does not work: An analysis of the failure of
constructivist, discovery, problem-based, experiential, and inquiry-based
teaching. *Educational Psychologist, 41*(2), 75–86.
https://doi.org/10.1207/s15326985ep4102_1

Kölling, M., Brown, N. C. C., & Altadmri, A. (2015). Frame-based editing:
Easing the transition from blocks to text-based programming. In
*Proceedings of the Workshop in Primary and Secondary Computing Education
(WiPSCE '15)*. ACM.

Lau, S., & Guo, P. J. (2023). From "Ban it till we understand it" to
"Resistance is futile": How university programming instructors plan to adapt
as more students use AI code generation and explanation tools such as
ChatGPT and GitHub Copilot. In *Proceedings of the 2023 ACM Conference on
International Computing Education Research (ICER '23)*. ACM.

Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral
participation*. Cambridge University Press.

Lee, I., Martin, F., Denner, J., Coulter, B., Allan, W., Erickson, J.,
Malyn-Smith, J., & Werner, L. (2011). Computational thinking for youth in
practice. *ACM Inroads, 2*(1), 32–37.

Leinonen, J., Hellas, A., Sarsa, S., Reeves, B., Denny, P., Prather, J., &
Becker, B. A. (2023). Using large language models to enhance programming
error messages. In *Proceedings of the 54th ACM Technical Symposium on
Computer Science Education (SIGCSE '23)*. ACM.

Liffiton, M., Sheese, B. E., Savelka, J., & Denny, P. (2024). CodeHelp:
Using large language models with guardrails for scalable support in
programming classes. In *Proceedings of the 23rd Koli Calling International
Conference on Computing Education Research (Koli Calling '23)*. ACM.
https://doi.org/10.1145/3631802.3631830

Lister, R., Adams, E. S., Fitzgerald, S., Fone, W., Hamer, J., Lindholm, M.,
McCartney, R., Moström, J. E., Sanders, K., Seppälä, O., Simon, B., &
Thomas, L. (2004). A multi-national study of reading and tracing skills in
novice programmers. In *Working Group Reports from ITiCSE on Innovation and
Technology in Computer Science Education (ITiCSE-WGR '04)*. ACM.

Liu, R., Zenke, C., Liu, C., Holmes, A., Thornton, P., & Malan, D. J.
(2024). Teaching CS50 with AI: Leveraging generative artificial intelligence
in computer science education. In *Proceedings of the 55th ACM Technical
Symposium on Computer Science Education (SIGCSE '24)*. ACM.

Lopez, M., Whalley, J., Robbins, P., & Lister, R. (2008). Relationships
between reading, tracing and writing skills in introductory programming. In
*Proceedings of the Fourth International Workshop on Computing Education
Research (ICER '08)*. ACM.

Luxton-Reilly, A., Simon, Albluwi, I., Becker, B. A., Giannakos, M., Kumar,
A. N., Ott, L., Paterson, J., Scott, M. J., Sheard, J., & Szabo, C. (2018).
Introductory programming: A systematic literature review. In *Proceedings
Companion of the 23rd Annual ACM Conference on Innovation and Technology in
Computer Science Education (ITiCSE '18 Companion)*. ACM.

Lyon, L. A., & Denner, J. (2016). *Student perspectives of community college
pathways to computer science bachelor's degrees* [Report]. ETR & Google.

MacNeil, S., Tran, A., Hellas, A., Kim, J., Sarsa, S., Denny, P., Bernstein,
S., & Leinonen, J. (2023). Experiences from using code explanations
generated by large language models in a web software development e-book. In
*Proceedings of the 54th ACM Technical Symposium on Computer Science
Education (SIGCSE '23)*. ACM. https://doi.org/10.1145/3545945.3569785

Margolis, J., & Fisher, A. (2002). *Unlocking the clubhouse: Women in
computing*. MIT Press.

Margulieux, L. E., Guzdial, M., & Catrambone, R. (2012). Subgoal-labeled
instructional material improves performance and transfer in learning to
develop mobile applications. In *Proceedings of the Ninth Annual
International Conference on International Computing Education Research
(ICER '12)*. ACM.

Margulieux, L. E., Morrison, B. B., & Decker, A. (2019). Design and pilot
testing of subgoal labeled worked examples for five core concepts in CS1. In
*Proceedings of the 2019 ACM Conference on Innovation and Technology in
Computer Science Education (ITiCSE '19)*. ACM.
https://doi.org/10.1145/3304221.3319756

Margulieux, L. E., Morrison, B. B., & Decker, A. (2020). Reducing withdrawal
and failure rates in introductory programming with subgoal labeled worked
examples. *International Journal of STEM Education, 7*, Article 19.
https://doi.org/10.1186/s40594-020-00222-7

Margulieux, L. E., Prather, J., Reeves, B. N., Becker, B. A., Cetin Uzun,
G., Loksa, D., Leinonen, J., & Denny, P. (2024). Self-regulation,
self-efficacy, and fear of failure interactions with how novices use LLMs to
solve programming problems. In *Proceedings of the 2024 Conference on
Innovation and Technology in Computer Science Education (ITiCSE '24)*. ACM.

McCracken, M., Almstrum, V., Diaz, D., Guzdial, M., Hagan, D., Kolikant,
Y. B.-D., Laxer, C., Thomas, L., Utting, I., & Wilusz, T. (2001). A
multi-national, multi-institutional study of assessment of programming
skills of first-year CS students. *ACM SIGCSE Bulletin, 33*(4), 125–180.

McDowell, C., Werner, L., Bullock, H. E., & Fernald, J. (2006). Pair
programming improves student retention, confidence, and program quality.
*Communications of the ACM, 49*(8), 90–95.

Morrison, B. B., Margulieux, L. E., & Guzdial, M. (2015). Subgoals, context,
and worked examples in learning computing problem solving. In *Proceedings
of the Eleventh Annual International Conference on International Computing
Education Research (ICER '15)*. ACM.

Morrison, B. B., Margulieux, L. E., Ericson, B., & Guzdial, M. (2016).
Subgoals help students solve Parsons problems. In *Proceedings of the 47th
ACM Technical Symposium on Computing Science Education (SIGCSE '16)*. ACM.

Murphy, L., Fitzgerald, S., Lister, R., & McCauley, R. (2012). Ability to
'explain in plain English' linked to proficiency in computer-based
programming. In *Proceedings of the Ninth Annual International Conference on
International Computing Education Research (ICER '12)*. ACM.

Paiva, J. C., Leal, J. P., & Figueira, Á. (2022). Automated assessment in
computer science education: A state-of-the-art review. *ACM Transactions on
Computing Education, 22*(3), Article 34. https://doi.org/10.1145/3513140

Papert, S. (1980). *Mindstorms: Children, computers, and powerful ideas*.
Basic Books.

Parsons, D., & Haden, P. (2006). Parson's programming puzzles: A fun and
effective learning tool for first programming courses. In *Proceedings of
the 8th Australasian Conference on Computing Education (ACE '06)*.
Australian Computer Society.

Patitsas, E., Berlin, J., Craig, M., & Easterbrook, S. (2020). Evidence that
computer science grades are not bimodal. *Communications of the ACM, 63*(1),
91–98.

Pea, R. D. (1986). Language-independent conceptual "bugs" in novice
programming. *Journal of Educational Computing Research, 2*(1), 25–36.

Porter, L., Bailey Lee, C., & Simon, B. (2013). Halving fail rates using
peer instruction: A study of four computer science courses. In *Proceedings
of the 44th ACM Technical Symposium on Computer Science Education
(SIGCSE '13)*. ACM.

Porter, L., Bouvier, D., Cutts, Q., Grissom, S., Lee, C., McCartney, R.,
Zingaro, D., & Simon, B. (2016). A multi-institutional study of peer
instruction in introductory computing. In *Proceedings of the 47th ACM
Technical Symposium on Computing Science Education (SIGCSE '16)*. ACM.
https://doi.org/10.1145/2839509.2844642

Porter, L., & Zingaro, D. (2023). *Learn AI-assisted Python programming:
With GitHub Copilot and ChatGPT*. Manning.

Prather, J., Denny, P., Leinonen, J., Becker, B. A., Albluwi, I., Craig, M.,
Keuning, H., Kiesler, N., Kohn, T., Luxton-Reilly, A., MacNeil, S., Petersen,
A., Pettit, R., Reeves, B. N., & Savelka, J. (2023). The robots are here:
Navigating the generative AI revolution in computing education. In
*Proceedings of the 2023 Working Group Reports on Innovation and Technology
in Computer Science Education (ITiCSE-WGR '23)*. ACM.
https://doi.org/10.1145/3623762.3633499

Prather, J., Reeves, B. N., Leinonen, J., MacNeil, S., Randrianasolo, A. S.,
Becker, B. A., Kimmel, B., Wright, J., & Briggs, B. (2024a). The widening
gap: The benefits and harms of generative AI for novice programmers. In
*Proceedings of the 2024 ACM Conference on International Computing Education
Research (ICER '24)*. ACM. https://doi.org/10.1145/3632620.3671116

Prather, J., Leinonen, J., Kiesler, N., et al. (2024b). Beyond the hype: A
comprehensive review of current trends in generative AI research, teaching
practices, and tools. In *Proceedings of the 2024 Working Group Reports on
Innovation and Technology in Computer Science Education (ITiCSE-WGR '24)*.
ACM.

Quille, K., & Bergin, S. (2019). CS1: How will they do? How can we help? A
decade of research and practice. *Computer Science Education, 29*(2–3),
254–282.

Raj, A. G. S., Patel, J. M., Halverson, R., & Halverson, E. R. (2018). Role
of live-coding in learning introductory programming. In *Proceedings of the
18th Koli Calling International Conference on Computing Education Research
(Koli Calling '18)*. ACM. https://doi.org/10.1145/3279720.3279725

Ramalingam, V., LaBelle, D., & Wiedenbeck, S. (2004). Self-efficacy and
mental models in learning to program. In *Proceedings of the 9th Annual
SIGCSE Conference on Innovation and Technology in Computer Science Education
(ITiCSE '04)*. ACM.

Resnick, M., Maloney, J., Monroy-Hernández, A., Rusk, N., Eastmond, E.,
Brennan, K., Millner, A., Rosenbaum, E., Silver, J., Silverman, B., & Kafai,
Y. (2009). Scratch: Programming for all. *Communications of the ACM,
52*(11), 60–67. https://doi.org/10.1145/1592761.1592779

Robins, A. (2010). Learning edge momentum: A new account of outcomes in
CS1. *Computer Science Education, 20*(1), 37–71.
https://doi.org/10.1080/08993401003612167

Robins, A., Rountree, J., & Rountree, N. (2003). Learning and teaching
programming: A review and discussion. *Computer Science Education, 13*(2),
137–172.

Rubin, M. J. (2013). The effectiveness of live-coding to teach introductory
programming. In *Proceedings of the 44th ACM Technical Symposium on Computer
Science Education (SIGCSE '13)*. ACM.
https://doi.org/10.1145/2445196.2445388

Sarsa, S., Denny, P., Hellas, A., & Leinonen, J. (2022). Automatic
generation of programming exercises and code explanations using large
language models. In *Proceedings of the 2022 ACM Conference on International
Computing Education Research (ICER '22)*. ACM.

Scott, M. J., & Ghinea, G. (2014). On the domain-specificity of mindsets:
The relationship between aptitude beliefs and programming practice. *IEEE
Transactions on Education, 57*(3), 169–174.

Selvaraj, A., Zhang, E., Porter, L., & Soosai Raj, A. G. (2021). Live
coding: A review of the literature. In *Proceedings of the 26th ACM
Conference on Innovation and Technology in Computer Science Education
(ITiCSE '21)*. ACM.

Sentance, S., Waite, J., & Kallia, M. (2019). Teaching computer programming
with PRIMM: A sociocultural perspective. *Computer Science Education,
29*(2–3), 136–176. https://doi.org/10.1080/08993408.2019.1608781

Shah, A., Hogan, E., Agarwal, V., Driscoll, J., Porter, L., Griswold,
W. G., & Soosai Raj, A. G. (2023). An empirical evaluation of live coding in
CS1. In *Proceedings of the 2023 ACM Conference on International Computing
Education Research (ICER '23)*. ACM.
https://doi.org/10.1145/3568813.3600122

Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction
works: Evidence for productive failure. *Review of Educational Research,
91*(5), 761–798.

Soloway, E. (1986). Learning to program = learning to construct mechanisms
and explanations. *Communications of the ACM, 29*(9), 850–858.

Sorva, J. (2013). Notional machines and introductory programming education.
*ACM Transactions on Computing Education, 13*(2), Article 8.
https://doi.org/10.1145/2483710.2483713

Sorva, J., Karavirta, V., & Malmi, L. (2013). A review of generic program
visualization systems for introductory programming education. *ACM
Transactions on Computing Education, 13*(4), Article 15.

Spohrer, J. C., & Soloway, E. (1986). Novice mistakes: Are the folk wisdoms
correct? *Communications of the ACM, 29*(7), 624–632.

Stefik, A., & Siebert, S. (2013). An empirical investigation into
programming language syntax. *ACM Transactions on Computing Education,
13*(4), Article 19. https://doi.org/10.1145/2534973

Stegeman, M., Barendsen, E., & Smetsers, S. (2014). Towards an empirically
validated model for assessment of code quality. In *Proceedings of the 14th
Koli Calling International Conference on Computing Education Research (Koli
Calling '14)*. ACM.

Sweller, J. (1988). Cognitive load during problem solving: Effects on
learning. *Cognitive Science, 12*(2), 257–285.
https://doi.org/10.1207/s15516709cog1202_4

Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive
architecture and instructional design: 20 years later. *Educational
Psychology Review, 31*(2), 261–292.
https://doi.org/10.1007/s10648-019-09465-5

Umapathy, K., & Ritzhaupt, A. D. (2017). A meta-analysis of pair-programming
in computer programming courses: Implications for educational practice. *ACM
Transactions on Computing Education, 17*(4), Article 16.
https://doi.org/10.1145/2996201

Vadaparty, A., Zingaro, D., Smith, D. H., IV, Padala, M., Alvarado, C.,
Gorson Benario, J., & Porter, L. (2024). CS1-LLM: Integrating LLMs into CS1
instruction. In *Proceedings of the 2024 Conference on Innovation and
Technology in Computer Science Education (ITiCSE '24)*. ACM.
https://doi.org/10.1145/3649217.3653584

van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex
learning: A systematic approach to four-component instructional design*
(3rd ed.). Routledge.

Vihavainen, A., Airaksinen, J., & Watson, C. (2014). A systematic review of
approaches for teaching introductory programming and their influence on
success. In *Proceedings of the Tenth Annual Conference on International
Computing Education Research (ICER '14)*. ACM.

Vygotsky, L. S. (1978). *Mind in society: The development of higher
psychological processes*. Harvard University Press.

Watson, C., & Li, F. W. B. (2014). Failure rates in introductory
programming revisited. In *Proceedings of the 2014 Conference on Innovation
and Technology in Computer Science Education (ITiCSE '14)*. ACM.
https://doi.org/10.1145/2591708.2591749

Weintrop, D., & Wilensky, U. (2017). Comparing block-based and text-based
programming in high school computer science classrooms. *ACM Transactions on
Computing Education, 18*(1), Article 3.

Werner, L. L., Hanks, B., & McDowell, C. (2004). Pair-programming helps
female computer science students. *ACM Journal on Educational Resources in
Computing, 4*(1), Article 4.

Whalley, J. L., Lister, R., Thompson, E., Clear, T., Robbins, P., Kumar,
P. K. A., & Prasad, C. (2006). An Australasian study of reading and
comprehension skills in novice programmers, using the Bloom and SOLO
taxonomies. In *Proceedings of the 8th Australasian Conference on Computing
Education (ACE '06)*. Australian Computer Society.

Xie, B., Loksa, D., Nelson, G. L., Davidson, M. J., Dong, D., Kwik, H.,
Tan, A. H., Hwa, L., Li, M., & Ko, A. J. (2019). A theory of instruction for
introductory programming skills. *Computer Science Education, 29*(2–3),
205–253. https://doi.org/10.1080/08993408.2019.1565235






