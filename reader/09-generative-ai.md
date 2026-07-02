# Theme 9 — Programming education in the era of generative AI

Nothing has destabilised programming education faster than large language
models. Since 2022, freely available tools solve most traditional
introductory assignments outright, which invalidates unsupervised
code-writing as a measure of individual skill and forces every programming
teacher to re-decide what is taught, practised, and assessed. The emerging
settlement — visible across the field's working groups — is coherent with
everything earlier in this reader rather than a break from it: the learning
objectives shift in emphasis, not in kind. Reading, tracing, explaining,
decomposing, specifying and testing were already the evidence-backed core
(themes 2 and 4); AI makes unguided code *writing* cheap while making code
*judgement* expensive. A protected fluency core remains (nearly everyone
retains invigilated checks that students can read, trace and write basic
code unaided — evaluating AI output presupposes exactly that fluency), AI
literacy becomes taught content, and assessment moves toward process and
oral explanation.

The two articles divide the terrain. Denny et al. (2024) is the field's
overview: capabilities, risks, opportunities, and early pedagogical
responses, written by the group whose 2022 studies first raised the alarm.
Prather et al. (2024) is the close-up empirical study of what actually
happens when novices code with these tools — and its answer, "the widening
gap", is the single most important AI-era finding for anyone teaching an
at-risk population. Both articles describe tools that will be outdated by
the time you read this; the findings about *learners* are the durable part.

Read this theme with theme 3 in your other hand: generative AI is a
momentum amplifier. It can also be a genuine equaliser — guarded tutors give
struggling students 24/7 non-judgemental help — but only by design, never by
default.

## Reading 14 — Denny et al. (2024), Computing education in the era of generative AI

*PDF: [articles/denny-2024-computing-education-genai.pdf](articles/denny-2024-computing-education-genai.pdf)
— Communications of the ACM, 67(2), 56–67.*

### Why this article

It is the best single map of the disruption, anchored in data rather than
punditry. The capability shock, measured: in 2021, Codex scored in the top
quartile of a real CS1 exam cohort; by 2023, GPT-4 scored 99.5% and 94.4% on
the same two exams, outscored by only three students of 71. The challenges,
documented: plagiarism detectors that do not work on generated code; policy
confusion (their advice: be extremely clear about when and how AI use is
allowed, and treat violations as use of an unauthorised resource, not
"plagiarism"); over-reliance and metacognitive atrophy; models producing
code too advanced for novices; and the unsettling security finding that
novices with AI assistants wrote insecure code *and were more confident it
was secure*. The opportunities, equally concrete: generating practice
exercises at scale (with the honest caveat that only a third of generated
exercises had fully passing test suites — human review stays mandatory),
line-by-line code explanations, LLM-improved error messages (in a randomised
trial, students repeated errors 23.5% less often — the first real progress
on a fifty-year-old problem you met in theme 6), Prompt Problems that make
specification the learned skill, and guarded tutors like CodeHelp designed
to help without revealing solutions.

For you, the article is also a stance to emulate: neither ban-and-pretend
nor uncritical embrace, but redesign — because "experts appreciate this
technology only because they already understand the fundamentals", and your
job is producing people who understand the fundamentals.

### How to read it

Read it whole; it is a magazine-format 12 pages. Track three questions as
you go: What does this mean for my assessments? Which opportunity would
save me the most preparation time? Where do my students need guardrails?
Date-stamp everything — the paper is from early 2024, the capabilities are
now higher, and the assessment implications are therefore stronger, not
weaker. Where the paper cites the working-group reports (Prather et al.
2023; Denny et al.'s "Robots are here" line of work), note them as the place
to go deeper.

### Guiding questions

1. List every assessment form used in a course you know and sort them:
   still measures individual capability in 2026 / measures it only under
   invigilation / no longer measures it. What replaces the third category —
   and what is your programme's equivalent of the "protected fluency core"?
2. The error-message result is the clearest quick win. Sketch how you would
   deploy LLM-explained error messages for your students (tool, guardrails,
   what you would tell students about trusting the explanations).
3. "Prompt Problems" make students write specifications instead of code.
   What skills from Xie et al.'s quadrant does that exercise, and which does
   it dangerously skip?
4. The authors argue students must be taught to use these tools responsibly
   from the beginning. Draft the three-sentence AI policy you would put in
   a first-semester course guide — phase by phase (forbidden /
   permitted-with-disclosure / required), not a blanket rule.

## Reading 15 — Prather et al. (2024), The widening gap: the benefits and harms of generative AI for novice programmers

*PDF: [articles/prather-2024-widening-gap.pdf](articles/prather-2024-widening-gap.pdf)
— ICER 2024, 469–486. Open access.*

### Why this article

Because it looks past what students *say* about AI to what they *do* — with
think-aloud protocols and eye tracking — and the two diverge alarmingly.
Twenty-one CS1 students solved a standard problem with Copilot and ChatGPT
available. Nearly everyone finished (20 of 21, versus 20 of 31 in the same
lab before GenAI existed), which on a dashboard looks like success. But half
the students struggled, all five previously documented metacognitive
difficulties persisted, and three new AI-specific ones appeared:
*interruption* (the suggestion stream breaks concentration — "please go
away"), *mislead* (the tool confidently escorts the student down a wrong
path), and *progression* (a student ends conceptually behind but unaware,
because generated code kept things moving). Struggling students accepted
more suggestions than successful ones; successful students' key skill was
recognising and *ignoring* bad output — Minsky's "negative expertise". Most
damning: post-session interviews contradicted observed behaviour. The
student who said "I use ChatGPT like a personal tutor" had done the
opposite; several finished with an illusion of competence. Self-reports
about AI use — including your future students' — are unreliable.

This is the study that connects the AI era to everything this reader has
argued: completion is not learning (theme 7's decoupling, now
tool-assisted); reading-before-writing is precisely the progression AI lets
students skip (theme 4); and momentum (theme 3) now has a compounding tool
attached — the well-prepared accelerate while the under-prepared feel
productive and fall behind. For a graduaat audience this is the central
warning: your students have the most to lose from unscaffolded AI, and
plausibly the most to gain from deliberately scaffolded use.

### How to read it

Read the introduction and related work quickly (it recaps Loksa's
problem-solving stages and the 2018 baseline study), then slow right down
for section 4: Table 2 (the eight difficulties) is the analytic core, and
the participant vignettes (P1, P4, P7, P8, P11) are the evidence — read at
least three in full; the moment P4 builds a fluent solution to the *wrong
problem* with Copilot's help is worth the whole paper. Read the discussion
and conclusions in full. Note the limitations honestly: 21 students, one
site, one problem, tools of early 2024 — this is a rich small-N
observational study, not a measurement of learning outcomes, and the authors
say so.

### Guiding questions

1. Why is "20 of 21 completed the problem" a misleading success metric?
   Which measurements in the study reveal what completion conceals?
2. Of the three new metacognitive difficulties, which is most dangerous in
   your context, and what would you change in lab supervision to catch it?
   (Remember: the student's own report will not reveal it.)
3. The successful students' skill was ignoring bad suggestions. Can
   "negative expertise" be taught directly? Design an exercise in which
   students must evaluate and reject AI output — and say which skills from
   Xie's quadrant it trains.
4. Combine this paper with Robins and with Margulieux: for an at-risk
   intake, argue for a concrete AI policy across the first year — when the
   tools are off, when they are guarded, when they are free — and defend
   the transition points with evidence from this reader.
