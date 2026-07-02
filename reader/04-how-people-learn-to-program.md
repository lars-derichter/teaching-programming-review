# Theme 4 — How people learn to program

This theme supplies the theory that disciplines everything practical in the
rest of the reader. Its core is an uncomfortable fact about human cognition:
working memory can hold only a handful of novel elements at once, while
programming confronts a beginner with syntax, semantics, the notional
machine, the problem, and the tooling *simultaneously*. From this, the
cognitive-load tradition draws a hard conclusion — unguided discovery is a
poor default for novices — and the computing education field has translated
that conclusion into a specific, sequenced theory of programming instruction.

The pairing is deliberate. Kirschner, Sweller and Clark (2006) is the most
cited, most combative statement of the case for explicit guidance, written
for education in general. Xie et al. (2019) is the field-specific synthesis:
four programming skills, taught explicitly, in order. Between them sits a
translation step you should watch carefully — general learning theory rarely
survives contact with a subject unchanged.

Two calibration notes. First, Kirschner et al. provoked substantial
responses; the modern reading is not "projects are bad" but "novices need
guidance *within* whatever format you use", and well-designed struggle
followed by explicit instruction has a documented place for design-level
skills (productive failure; Kapur, 2008; Sinha & Kapur, 2021). Second,
guidance must *fade*: what helps novices becomes redundant or harmful for
more advanced learners (the expertise reversal effect). Both nuances matter
enormously for practice-oriented programmes built around projects — the
resolution, developed in theme 8, is scaffolded authentic tasks, not
unguided ones.

## Reading 6 — Kirschner, Sweller & Clark (2006), Why minimal guidance during instruction does not work

*PDF: [articles/kirschner-2006-why-minimal-guidance-does-not-work.pdf](articles/kirschner-2006-why-minimal-guidance-does-not-work.pdf)
— Educational Psychologist, 41(2), 75–86.*

### Why this article

It anchors half the design decisions in this reader — worked examples,
small-steps exercise regimes, live modelling — in a single argument from
cognitive architecture: learning means changing long-term memory; novel
information must pass through a severely limited working memory; searching
for solutions ("discovery") consumes exactly the working-memory resources
that schema-building needs, so novices can problem-solve for hours and learn
almost nothing. The empirical core is the worked-example effect — novices
learn more from studying worked solutions than from solving equivalent
problems — plus half a century of failed revivals of minimally guided
teaching under changing names.

For programming teachers the paper's sharpest distinction is between the
*epistemology* of a discipline and its *pedagogy*: how professional
developers work is not how beginners learn to work. "Learning by doing what
professionals do, only slower" is the default instinct of practice-oriented
programmes, and this paper is the standing correction to it. Note also the
sobering ATI evidence: weakly guided instruction harms weaker learners most —
some measurably know *less* after instruction than before — while stronger
learners cope. Guidance is, among other things, an equity instrument.

### How to read it

Read the whole article; it is twelve dense but well-organised pages. Fix the
three memory-architecture claims first (long-term memory as the seat of
skill; working-memory limits for novel material; limits vanish for familiar
material) — everything else follows. Read the worked-example and expertise-
reversal passages twice; fading guidance is the design principle you will
apply most often. Read critically: the definition of "minimal guidance" is
contested, and defenders of problem-based learning replied that modern PBL
is heavily scaffolded (Hmelo-Silver et al., 2007; Schmidt et al., 2007).
Where exactly does the disagreement lie once both sides accept scaffolding?

### Guiding questions

1. Reconstruct the argument in four steps from cognitive architecture to
   "explicit guidance for novices". Which step would a critic attack first?
2. Translate the worked-example effect into programming teaching: what does
   a worked example look like for a `while` loop lesson, and what does the
   fading sequence (example → completion → independent writing) look like
   across two weeks?
3. Your programme is built around projects. Using this paper plus the
   expertise reversal effect, argue *for* keeping the projects — and
   specify what guidance inside them must look like in semester one versus
   semester four.
4. The Clark finding — weaker learners choosing less guided courses enjoy
   them more and learn less — is awkward for student-evaluation culture.
   How should a teacher weigh satisfaction against learning when the two
   diverge?

## Reading 7 — Xie et al. (2019), A theory of instruction for introductory programming skills

*PDF: [articles/xie-2019-theory-of-instruction.pdf](articles/xie-2019-theory-of-instruction.pdf)
— Computer Science Education, 29(2–3), 205–253.*

### Why this article

This is the closest thing computing education currently has to a consensus
model of introductory instruction, and it is built directly on the results
you met in theme 2. Xie and colleagues decompose early programming skill
along two axes — reading versus writing, and language semantics versus
reusable *templates* (solution patterns) — yielding four skills: (S1) trace
code, (S2) write correct syntax, (S3) recognise templates and their purpose,
(S4) use templates to solve problems. Their theory of instruction: teach and
assess these four explicitly, in that order, with distinct practice types for
each, instead of assigning open writing tasks and hoping all four skills
co-develop. The article's own indictment of standard practice is memorable:
a typical first lesson makes students *write* code they cannot yet *read* —
within one hour of first contact.

Be aware of what the evidence is: the theory is grounded in the substantial
BRACElet/SOLO research line (tracing precedes explaining precedes writing),
but the paper's own evaluation is exploratory, with nine participants. You
are reading it for the framework and the instructional designs, which are
unusually concrete — memory tables for tracing, syntax-rule tables with
bad/fixed code pairs, template steps in plain language, plan-first writing —
and for the diagnostic idea that different errors (S1 versus S2 versus S3
versus S4) require different remediation.

### How to read it

Sections 1–4 are the core: the gap analysis, the four-skill quadrant (study
Figure 1, the variable-swap example, until you can reproduce it), and the
worked instructional designs. Skim sections 5–6 (the small study) but read
enough to judge the evidence honestly. Section 7's discussion of limitations
and out-of-scope skills (debugging, problem-solving, inventing new
templates) is short and worth reading — it tells you what this theory does
*not* claim.

### Guiding questions

1. Map the first two weeks of a programming course you know onto the
   quadrant: which skills does each activity demand, and where are students
   asked for S4 before S1–S3 are in place?
2. Design one exercise for each of S1–S4 for a single concept you will teach
   (e.g. conditionals), including how you would tell an S1 error from an S2
   error in student work.
3. "Templates" are the modern version of Soloway's plans and the schemas of
   cognitive load theory. Why does naming and teaching them explicitly help
   the students who would not induce them on their own? Connect to the
   worked-example effect.
4. The evaluation had nine participants. What would a convincing evaluation
   of this theory look like — and, given the underlying BRACElet evidence,
   how much should the small N lower your confidence in the *sequencing*
   claim specifically?
