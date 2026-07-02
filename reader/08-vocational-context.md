# Theme 8 — Teaching in a vocational context

Most computing education research is done on bachelor students at research
universities. The population you will teach — associate degree / graduaat
students, EQF level 5 — is underrepresented in the literature relative to
its size, and it differs in ways that matter: motivations are more directly
vocational, prior academic setbacks and non-traditional routes are more
common, and work, family and finances shape persistence at least as much as
course difficulty does. None of this implies lower ceilings; it implies
different design priorities. The scaffolding-heavy practices of themes 4–5
matter *more* here, not less — their largest measured effects were in
at-risk groups — and the affective design of theme 7 carries extra weight.

The two articles look at this context from opposite sides. Vihavainen et al.
(2011) is the instructional side: a course design — extreme apprenticeship —
that takes cognitive apprenticeship (modelling, scaffolding, fading) and
pushes the scaffolding to industrial strength, built on exactly the values a
practice-oriented programme professes: learning by doing, under guidance,
with no compromise on quality. Lyon and Denner (2019) is the institutional
side: what happens to community-college students — the closest US analogue
to the graduaat population — as they try to move through and beyond their
programme, and how institutional obstacles unrelated to ability get read, by
students, as personal failure.

For curriculum-level design in this context, two frameworks from the
literature review are worth knowing by name: *cognitive apprenticeship*
(Collins et al., 1989), which both articles here instantiate, and
*four-component instructional design* (4C/ID; van Merriënboer & Kirschner,
2018) — the dominant design model in Dutch-language vocational higher
education, whose "whole authentic tasks plus scheduled part-task practice"
structure is the mature answer to the projects-versus-exercises dilemma.

## Reading 12 — Vihavainen, Paksula & Luukkainen (2011), Extreme apprenticeship method in teaching programming for beginners

*PDF: [articles/vihavainen-2011-extreme-apprenticeship.pdf](articles/vihavainen-2011-extreme-apprenticeship.pdf)
— SIGCSE 2011, 93–98.*

### Why this article

Six pages that redesign a course from values outward. The values: learning
by doing (the craft is mastered only by practising it), continuous
bidirectional feedback, no compromise (skills are practised until mastered —
instructors send solutions back for rework until they could pass as model
answers), and "the apprentice becomes the master". The practices that
follow: lectures cut from five hours a week to two; exercises start the
first day (thirty small ones in week one — 88% of students completed at
least 25); labs with instructors continuously present who give hints, never
answers; exercise chains that build big programs from small steps
(output-driven and main-driven programming, where the expected output or a
given test acts as the specification); visible progress checklists — "every
check was a small victory". The result at Helsinki: a spring-cohort pass
rate of 70% against a long-term spring average of 44%, and the follow-up
course hitting an all-time high — the routine built early kept compounding,
exactly as theme 3's momentum account predicts.

Notice how many threads of this reader the design ties together: Kirschner's
critique of unguided homework (take-home exercises are a minimally guided
environment — so move the work into supported labs); many small early wins
as self-efficacy engineering (theme 7); Vygotskian scaffolding with fading
(themes 4–5). This paper — later folded into the systematic review finding
that course transformations of this family raise pass rates by roughly a
third (Vihavainen et al., 2014, in `articles/extra/`) — is the closest thing
in the literature to a blueprint for an intensive graduaat-style programming
line.

### How to read it

Read it whole; it is short. As you read sections 3–4, maintain two running
lists: which practice implements which principle from earlier themes, and
what each practice costs (instructor hours, materials, room scheduling).
Section 5's evidence is honest but weak by design — a before/after
comparison across cohorts, no controls — so practise the same critical
reading you applied to Porter and Sentance: what besides the method could
explain the jump?

### Guiding questions

1. "No compromise" means rejecting working-but-ugly solutions and requiring
   rework. Defend this against the objection that it will crush weak
   students' motivation — using self-efficacy theory, not intuition. (Hint:
   what does the availability of scaffolding do to the meaning of rework?)
2. The method spends teacher time in labs instead of lectures at
   approximately constant total cost. What breaks first when class size
   doubles, and what parts can tooling (autograders, theme 6; LLM tutors,
   theme 9) take over without violating the hints-not-answers rule?
3. Design week 1 of your own course in extreme-apprenticeship style: how
   many exercises, how small is the first one, what does the checklist look
   like, and where does fading begin?
4. The follow-up course's record pass rate is arguably the most important
   result in the paper. Why? Connect it to learning edge momentum and to
   the "fragile routine" the authors blame for previous cohorts' failures.

## Reading 13 — Lyon & Denner (2019), Chutes and ladders: institutional setbacks on the computer science community college transfer pathway

*PDF: [articles/lyon-denner-2019-chutes-ladders.pdf](articles/lyon-denner-2019-chutes-ladders.pdf)
— ACM Transactions on Computing Education, 19(3), Article 25.*

### Why this article

Because your students' success will be decided partly outside your
classroom, and this is the rare computing education paper that looks there.
Fourteen community-college students from groups underrepresented in
computing — all of whom had taken introductory programming and intended to
complete a CS bachelor's — were interviewed five years later. One had the
degree. The paper sorts what happened to the rest into pathway *setbacks*
(wrong advising, credits refused in transfer, courses retaken because of
poor instruction), *discontinuities* (leaving and re-entering, usually
because work and study collided), and *departures* (leaving CS or college —
one student left within weeks upon hearing about a calculus requirement).
The titular metaphor replaces the tidy "pipeline": students move as in a
game of chutes and ladders, sliding backwards or off the board for reasons
that have nothing to do with ability but are easily internalised as personal
failure — the institutional-scale version of theme 7's attribution problem.

Read as a design brief, the paper's supports table is directly actionable
for a graduaat programme: accurate programme-specific counselling, credit
flexibility, accommodating working students, career information, and
supporting the effective, encouraging instructors who repeatedly turn out to
be the reason a student stayed. The four case studies (Luis, Kylie, Felipe,
Brittany) are worth reading slowly; versions of all four will sit in your
classroom.

### How to read it

Skim the background (section 2) noting the population statistics; read the
findings and the four cases (sections 4–5) closely; read the discussion
(section 6) with a pen, translating each suggested support into its Flemish
equivalent — the graduaat-to-bachelor bridge, EVC/EVK credit recognition,
werkstudent arrangements, study-cost support. The US context differs
(transfer between institutions is the central mechanism there), so the
transferable content is the *categories* of barrier and the student's-eye
view, not the specific policies.

### Guiding questions

1. Map each barrier category onto a Flemish graduaat context: what are the
   local equivalents of credit loss, advising gaps, math chains, and the
   work-study collision? Which does a lecturer see, and which stay
   invisible?
2. Felipe dropped the same course twice because of one ineffective
   instructor, and several students stayed because of one encouraging one.
   What follows for how a small programme should deploy its best teachers
   across the curriculum?
3. Where is the line between a lecturer's job and the institution's job in
   removing these barriers — and what can a lecturer realistically do from
   below (signposting, advising accuracy, flexible deadlines) without
   waiting for policy?
4. Connect this paper to Kinnunen & Simon and Robins: how do institutional
   setbacks, attribution, and momentum interact to turn a solvable
   logistical problem into "I'm not cut out for this"?
