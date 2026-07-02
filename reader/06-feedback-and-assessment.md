# Theme 6 — Feedback and assessment

Feedback is among the strongest influences on learning that education
research knows (Hattie & Timperley, 2007), and in programming courses much of
it is delivered by software: autograders, test runners, online judges. That
makes the *content* of automated feedback a first-order design decision for
any programming teacher — and, in most tools, a disappointment. The
systematic review in this theme shows that tools overwhelmingly tell students
*that* and *where* they are wrong, and rarely *how to proceed* — while it is
precisely feedback about how to proceed that novices, stuck mid-problem,
need. Meanwhile binary correct/incorrect feedback has documented harmful
effects: more gaming of the grader, fewer attempts.

Assessment is feedback's summative twin, and the skill-hierarchy evidence
from theme 2 gives it a concrete prescription: early programming assessment
should explicitly include tracing items, explain-in-plain-English items,
Parsons items, fix-this-code items — not writing alone. Mixed formats are
more informative, fairer to partial mastery (which matters given the
momentum effects of theme 3), and — as theme 3 noted — all-or-nothing
code-writing questions can manufacture the very bimodality folklore expects.
The generative-AI theme will sharpen all of this further: unsupervised
code-writing for marks no longer measures individual capability at all.

For the affective dimension of feedback — what an autograder's red cross
does to a student at 23:00 — hold this theme together with theme 7.

## Reading 10 — Keuning, Jeuring & Heeren (2018), A systematic literature review of automated feedback generation for programming exercises

*PDF: [articles/keuning-2018-feedback-review.pdf](articles/keuning-2018-feedback-review.pdf)
— ACM Transactions on Computing Education, 19(1), Article 3.*

### Why this article

It is the definitive map of what automated feedback tools actually say to
students, built from 101 tools described in 146 papers — and it was written
at the Open Universiteit, by researchers working in the Dutch-language
higher-education context you will teach in. The authors classify feedback
content using Narciss's categories: knowledge about task constraints, about
concepts, about *mistakes* (test failures, compiler errors, solution errors,
style, performance), about *how to proceed* (fix-it hints, next steps,
improvements), and about metacognition. The headline: 96% of tools report
mistakes; under half offer any "how to proceed"; metacognitive feedback
barely exists; and teachers can rarely adapt any of it beyond supplying test
data. The review predates LLM-based hints — which is exactly why it matters
now: it defines the gap that current LLM tutors (theme 9) are trying to
fill, and the vocabulary for judging whether they succeed.

For you the review doubles as a buyer's guide and a design brief. When your
programme chooses or configures a grading platform, Narciss's categories are
the checklist; and since most platforms let teachers write the messages
attached to failing tests, the cheapest intervention available to you is to
write those messages as teaching text — a hint about how to proceed — rather
than as assertions that something failed.

### How to read it

This is a 43-page review; read it strategically. Sections 1–4 (motivation,
method, and especially the labelling in section 4) are essential — the
feedback taxonomy is the takeaway. In sections 5–9, read section 6 for the
worked examples of each feedback type (the BIP message from the 1970s is a
small delight) and skim the rest, returning to tables as reference material.
Read sections 10–11 (discussion and conclusion) in full. Throughout, keep
one question active: which of these categories does the tooling in *your*
programme produce?

### Guiding questions

1. Audit a grading tool you know (Dodona, CodeGrade, Moodle CodeRunner...)
   against Narciss's categories. Which types does it produce, at what level
   of detail, and which are absent?
2. Take one exercise from your course and rewrite its three most-triggered
   test-failure messages so each contains "knowledge about how to proceed"
   without giving away the solution. What is hard about this?
3. Instant test-based feedback invites "shotgun debugging" — iterating
   against the grader instead of reasoning. Which countermeasures (submission
   limits, hidden tests, reflection prompts, required trace-before-submit)
   fit your context, and what does each cost?
4. The review finds teachers cannot easily adapt tools. Who, in your
   programme, effectively decides what feedback students receive hundreds of
   times per semester? Is that a deliberate decision?
