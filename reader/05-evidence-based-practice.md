# Theme 5 — Evidence-based classroom practice

Theory earns its keep in lesson design. This theme presents two designs with
evidence behind them, chosen because together they cover the two levels a
teacher plans at: PRIMM structures a *lesson* (or short sequence) so that
comprehension precedes production, and subgoal-labelled worked examples
structure the *materials* students learn from, with measured benefits
concentrated in exactly the students a graduaat programme worries about most.

Both designs operationalise the same principles from themes 2 and 4 —
reading before writing, managed cognitive load, explicit schemas — but from
different theoretical homes: PRIMM is argued from Vygotsky (language,
social interaction, and the gradual transfer of ownership), subgoal labelling
from cognitive load theory. Noticing that opposed theoretical traditions
converge on similar classroom moves should raise, not lower, your confidence
in the moves.

Two adjacent practices belong in your toolkit even though their primary
papers sit in `articles/extra/`: *peer instruction* (pre-class preparation,
solo clicker vote, peer discussion, re-vote, debrief) roughly halved fail
rates across four CS courses in within-instructor comparisons (Porter et
al., 2013), and *Parsons problems* (reorder scrambled code blocks) deliver
learning comparable to writing the code at markedly lower time cost
(Ericson et al., 2022). Both share a mechanism with PRIMM: they force
students to articulate reasoning about code — talking about code is the
explain-in-plain-English skill that theme 2 identified as pivotal.

## Reading 8 — Sentance, Waite & Kallia (2019), Teaching computer programming with PRIMM

*PDF: [articles/sentance-2019-primm.pdf](articles/sentance-2019-primm.pdf)
— Computer Science Education, 29(2–3), 136–176.*

### Why this article

PRIMM — Predict, Run, Investigate, Modify, Make — is the most directly
usable lesson framework in this reader. Students first predict what a given
program does (in pairs, on paper), run it to confront their prediction,
investigate it through structured questions, modify it through graded
extensions, and only then make something new. Two design ideas do the heavy
lifting. First, students begin by reading working code *they did not write*:
this lowers cognitive load and depersonalises error — the code's failure is
not their failure. Second, ownership transfers gradually ("not mine → partly
mine → mine"), with classroom talk about code as the engine, grounded
explicitly in Vygotsky's ideas of mediation and the zone of proximal
development.

The evidence: a quasi-experiment in 13 schools (493 students in the PRIMM
condition, 180 controls, ages 11–14, 8–12 weeks) found a statistically
significant advantage on a post-test, with a modest effect size, and teacher
interviews reporting that the structure worked notably well in mixed-ability
classes — with one recurring caveat, a "modify ceiling", where weaker
students never reached the Make phase. Note the transfer question honestly:
the controlled evidence is from secondary schools. The underlying mechanisms
(reading-before-writing, load management, structured talk) are age-general,
and PRIMM is widely and plausibly used in tertiary intro courses, but its
tertiary effectiveness is an extrapolation, not a measurement.

### How to read it

Sections 2–3 recap literature you now know; skim them, but slow down at
section 3.5 (the three sociocultural principles). Read section 4 — the
framework and the concrete lesson mechanics — closely; this is the usable
core. In the study (sections 5–7), read the design and quantitative results
carefully enough to critique them (non-random assignment, materials designed
by the researchers, r = .13), then give the qualitative results real
attention: the teacher quotes about Predict and about structure are the
practical wisdom of the paper. Section 8 you can read as a summary.

### Guiding questions

1. Assign each letter of PRIMM to the mechanism(s) it implements: cognitive
   load management, prediction-before-feedback, depersonalised error,
   articulation, transfer of ownership. Which phase could you *not* drop
   without breaking the design?
2. Build one full PRIMM cycle for a concept in your own course: the starter
   program, the prediction task, five Investigate questions (aim them at the
   notional machine, not at syntax trivia), a graded series of Modify tasks,
   and a Make task. Where in your cycle is the "modify ceiling" risk, and
   what is your plan for it?
3. Why does it matter that students predict *in pairs* and commit their
   prediction to paper before running the code? Connect to Brown & Wilson's
   tip 4.
4. The effect size is modest and the setting is secondary education. What
   would you want to measure in your own classroom to decide whether PRIMM
   earns its place — and what would count as "no"?

## Reading 9 — Margulieux, Morrison & Decker (2020), Reducing withdrawal and failure rates in introductory programming with subgoal labeled worked examples

*PDF: [articles/margulieux-2020-subgoals.pdf](articles/margulieux-2020-subgoals.pdf)
— International Journal of STEM Education, 7, Article 19. Open access.*

### Why this article

This is the strongest classroom-scale test of the worked-example tradition in
programming, and its most interesting result is distributional. A
semester-long quasi-experiment (N = 265, five sections of the same Java
course, identical quizzes and exams) compared conventional worked examples
with versions whose steps were grouped under short functional labels
("subgoals": *diagram which statements go together*, *determine whether true
or false*, *follow the correct branch*). The subgoal sections did better on
formative quizzes (medium effect) and produced markedly better
explain-in-plain-English answers. On exams the average difference vanished —
but variance shrank, more students took all exams, and roughly *half as
many* students dropped or failed. The benefits concentrated in students with
risk factors: lower GPA, expecting the course to be difficult, younger
students with weaker self-regulation.

Two further things earn this paper its place. Methodologically, it shows how
much of teaching-relevant truth hides outside the headline mean: if you only
read "no significant exam difference", you would miss the halved failure
rate. Practically, its account of the TAPS procedure — an analyst
interrogating a subject-matter expert until the expert's automatised steps
become explicit ("why did you do that?" — "that's just how it's done") — is
a portrait of the *expert blind spot* you will have to overcome in yourself
to write good materials.

### How to read it

The background section is an efficient recap of cognitive load and
worked-example research; read it as consolidation of theme 4. Study Figure 1
(a subgoal-labelled example) until the format is obvious. In the results,
follow the three-way split — quiz performance, exam performance,
retention/failure — and the risk-factor analyses; Table 9's pattern is the
heart of the paper. The SOLO-based analysis of explain-in-plain-English
answers connects back to theme 2 and forward to theme 6 (it is an assessable
comprehension format you can adopt as is).

### Guiding questions

1. Why would labels that *add* text to an example *reduce* cognitive load?
   Answer using intrinsic versus extraneous load and the surface-versus-
   structure distinction.
2. Write subgoal labels for a worked example you might actually use (e.g.
   reading a file and computing an average). Then do a mini-TAPS on
   yourself: which steps did you initially skip because they are "obvious"?
3. Subgoals helped on quizzes but not on exam averages, while cutting
   withdrawals and failures in half. Construct two different explanations
   for this pattern, and say what data would distinguish them.
4. For a graduaat intake with many at-risk students, which finding of this
   paper matters most, and how would it change your materials for the first
   six weeks?
