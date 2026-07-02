# Theme 2 — What makes learning to program hard

Any teaching decision presupposes a diagnosis: *why* is this subject hard?
The research answer has been remarkably stable since the 1980s, and it is not
the folk answer. The hard part is not syntax, and not some general
"problem-solving ability" that students either have or lack. The hard part is
twofold. First, novices must construct a runnable mental model of an
invisible machine — what the field calls the *notional machine* — because
code only has meaning in terms of what that machine does when the program
runs. Second, the skills involved form a rough hierarchy: reading and tracing
code precede explaining it, which precedes reliably writing it. Traditional
courses invert this hierarchy by demanding writing from day one.

The two articles in this theme are the primary sources for both halves of the
diagnosis. Lister et al. (2004) is the landmark multi-national study showing
that many students who "finished" an introductory course cannot trace short
code fragments — and that this, rather than a mysterious problem-solving
deficit, explains much of the disappointing writing performance documented
earlier by McCracken et al. (2001). Sorva (2013) synthesises three decades of
work on misconceptions and mental models into the notional machine concept
and derives concrete teaching implications from it.

For further reading, Qian and Lehman (2017, in `articles/extra/`) catalogue
novice misconceptions and their sources — useful later as a checklist when
you design diagnostic questions.

## Reading 2 — Lister et al. (2004), A multi-national study of reading and tracing skills in novice programmers

*PDF: [articles/lister-2004-reading-tracing.pdf](articles/lister-2004-reading-tracing.pdf)
— ITiCSE working group report, SIGCSE Bulletin, 36(4), 119–150.*

### Why this article

This is arguably the single most practice-relevant result in computing
education research, from the source. Twelve researchers in seven countries
gave 941 end-of-course students twelve multiple-choice questions requiring
them to trace code or select a missing line. Many students performed poorly;
the bottom quartile scored 4 or less out of 12. The paper's interpretation
reframed the field: before concluding that students "can't problem-solve",
check whether they have the *precursor* skills — systematically reading and
tracing code — because many demonstrably do not. The study also produced two
enduring practical insights: students who sketch traces on paper ("doodles")
answer far more correctly than those who leave the page blank (roughly 75%
versus 50%), and the think-aloud transcripts show that what separates strong
from weak students is not a different method but the *meticulousness* of the
same method.

The concept to take away is *fragile knowledge* (borrowed from Perkins &
Martin): the student "sort of knows, has some fragments, can make some
moves", but cannot marshal that knowledge reliably. Most of your future
students will live in this zone for months. Teaching decisions look different
once you assume fragility rather than absence or presence of knowledge.

### How to read it

Sections 1–3 (the study and the performance data) and sections 5.4–7 (the
transcripts and conclusions) are the core. Section 4 (the doodle analysis) is
short and worth reading in full — the table of doodle categories is a
ready-made vocabulary for teaching tracing on paper. Appendix A contains all
twelve questions: do them yourself, honestly, before reading the results, and
keep them — they are a directly usable diagnostic instrument for your own
teaching. Appendix B (question-by-question analysis) can be skimmed.

Note while reading: this is a 2004 study using Java and multiple-choice
items, and it shows correlations at one point in time. A later replication
with over 600 students (Fowler et al., 2022) found that the data cannot, by
themselves, fix the best *teaching order* — the robust core is that
comprehension and writing travel together and that comprehension is teachable
and assessable in its own right.

### Guiding questions

1. What exactly is the difference between "this student cannot problem-solve"
   and "this student has a fragile grasp of tracing"? What different teaching
   responses follow from each diagnosis?
2. The doodle data show that tracing on paper strongly predicts correctness,
   yet over half the students did not doodle on the harder questions. Give
   two plausible explanations, and describe how you would *teach* (not just
   encourage) systematic tracing.
3. Would the students you will teach pass Question 2 and Question 8 at the
   end of their first semester? What would you change in a course if 40% of
   them could not?
4. The authors note their MCQs use non-idiomatic, context-free code. What are
   the arguments for and against assessing novices with such "unnatural"
   code?

## Reading 3 — Sorva (2013), Notional machines and introductory programming education

*PDF: [articles/sorva-2013-notional-machines.pdf](articles/sorva-2013-notional-machines.pdf)
— ACM Transactions on Computing Education, 13(2), Article 8.*

### Why this article

Every programming language implies an abstract machine — the thing that
"runs" the code — and your students must build a workable mental model of it,
whether you help them or not. Sorva's review is the definitive treatment of
this idea. It gathers the misconceptions literature (variables that "hold two
values", assignment read as algebra, loops executing "all at once"), the
psychology of mental models (learners' models are incomplete, superstitious,
and hard to repair once ingrained), and two useful theoretical lenses:
program dynamics as a *threshold concept* — transformative, troublesome, and
easy for experts to forget having crossed — and the finding that some
students experience programming as mere text-writing, with the running
program absent from their picture entirely.

For a future teacher, the pay-off is section 8: make the notional machine an
explicit learning objective; give students a conceptual model of the machine
early, before flawed intuitions take root; and use visualisation *actively* —
the evidence says watching an animation does little, while predicting,
annotating, and tracing with it does a lot. This is also the article that
best explains *why* Ben-Ari's famous constructivist argument (1998, in
`articles/extra/`) cuts against discovery learning in programming: novices
have no effective prior model of a computer to build on, and "the computer
does not negotiate" — flawed models are punished with bugs, not discussed.

### How to read it

Read sections 1–3 (the concept and the misconceptions evidence), section 4.3
(tracing as "running" a mental model — connects directly to Lister), and
sections 8 and 10 (teaching implications and conclusions) closely. Sections
5–7 tour three theoretical traditions (constructivism, phenomenography,
threshold concepts); read them once for the ideas without trying to master
the theory. Section 9 (object-oriented programming needs two notional
machines) matters if your programme teaches OO early — which in Flanders it
often does.

### Guiding questions

1. Describe, concretely, the notional machine of the language taught in your
   programme: what are its "moving parts" (variables, frames, objects,
   references...), and how would you draw its state on a whiteboard? If you
   cannot, what does that imply about how you learned — and how you would
   teach?
2. Pick two classic misconceptions from section 3 and design a diagnostic
   question for each that a student with the misconception would answer
   incorrectly *with confidence*.
3. The mental-models literature says repairing an ingrained flawed model is
   harder than building a good one early. What follows for the first three
   weeks of a programming course? What is the cost of that choice?
4. Sorva argues visualisation tools only work with active engagement. Sketch
   a lab exercise around a program visualiser (or debugger) in which students
   must commit to predictions before stepping.
