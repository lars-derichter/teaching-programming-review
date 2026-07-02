# Theme 3 — Is programming ability innate?

No belief does more quiet damage in programming education than the "geek
gene": the idea that some students simply have it and others never will,
allegedly visible in a two-humped grade distribution. Teachers who hold this
belief invest less in students they have mentally filed in the second hump;
students who absorb it interpret their first struggle as a verdict. This
theme pairs the paper that empirically dismantled the belief with the paper
that offers the best alternative explanation for what teachers actually see.

The two articles disagree with each other in an instructive way: Robins
(2010) *accepts* the bimodal distribution as a premise and explains it
without innate ability; Patitsas et al. (2020) then show the premise itself
is largely wrong — real grade distributions are rarely bimodal, and the
perception of bimodality is driven by the very belief it is used to justify.
Read them in that order and let them argue. What survives the collision is
robust: outcomes spread widely for structural, teachable reasons; nothing
requires two kinds of people. The practical stakes are quantified by a
systematic review you should know exists: adopting any of the better-
evidenced teaching approaches improves pass rates by roughly one third
relative to traditional lecture-based teaching (Vihavainen et al., 2014, in
`articles/extra/`) — outcomes are substantially under instructor control.

## Reading 4 — Robins (2010), Learning edge momentum: a new account of outcomes in CS1

*PDF: [articles/robins-2010-learning-edge-momentum.pdf](articles/robins-2010-learning-edge-momentum.pdf)
— Computer Science Education, 20(1), 37–71.*

### Why this article

Two reasons. First, section 2 is the best available review of six decades of
attempts to *predict* who will learn to program — aptitude tests, cognitive
styles, Piagetian stages, personality, demographics — and its conclusion is
bracing: no instrument reliably identifies "programmers" versus
"non-programmers", most predictors are weak and probably reduce to general
intelligence, and the two hypothetical populations have never been found.
Second, the paper proposes a mechanism that explains extreme outcomes without
innate ability: *learning edge momentum*. We learn at the edge of what we
already know; programming concepts are unusually tightly interconnected (a
jigsaw puzzle, not a pile of blocks); therefore early success makes the next
concept easier and early failure makes it harder, and the effect compounds.
A simple simulation shows that adding just this dependence to an otherwise
normal model of learning pushes outcomes to the extremes.

The teaching consequences are immediate and testable: the first two or three
weeks are disproportionately decisive (in Robins's data, week-1 lab
attendance already predicts the final grade); disengagement must be chased
the week it appears, not at the mid-term; and structures that let students
close gaps before moving on (recovery paths, flexible pacing, mastery
elements) attack the mechanism directly. You will recognise this snowball
again in theme 7 (self-efficacy compounds the same way) and theme 9
(generative AI can accelerate it in both directions).

### How to read it

Read section 1, skim-read section 2 with an eye for the pattern (every
predictor family fails the same way), and read sections 3–5 closely — the
model is presented in a few lines of Java and needs no statistics. Do not
over-invest in the simulation's parameters; Robins is explicit that only the
general principle matters. Note that the paper takes bimodality as given
("frequently reported anecdotally") — you will re-evaluate that premise in
the next reading.

### Guiding questions

1. Explain learning edge momentum in your own words using the jigsaw/block
   tower analogy. What property of programming content drives the effect,
   and do you agree that programming has it to an unusual degree?
2. The geek-gene hypothesis and LEM predict the same grade distribution.
   What *different* predictions do they make — about interventions, about
   timing, about repeat attempts? How could a programme test which is at
   work?
3. Design an early-warning system for weeks 1–4 of a graduaat programming
   course: what signals would you collect, and — crucially — what support
   pathway triggers when a signal fires? (Prediction without support merely
   produces labels.)
4. Robins suggests flexible pacing and mastery structures but notes they are
   resource-intensive. What is realistic in your institution, and what is
   the cheapest intervention that still respects the mechanism?

## Reading 5 — Patitsas, Berlin, Craig & Easterbrook (2020), Evidence that computer science grades are not bimodal

*PDF: [articles/patitsas-2020-grades-not-bimodal.pdf](articles/patitsas-2020-grades-not-bimodal.pdf)
— Communications of the ACM, 63(1), 91–98.*

### Why this article

Because it is a small masterclass in checking a belief everyone "knows" to be
true. Study 1 tests 778 final-grade distributions from eighteen years of CS
courses at one university: only 5.8% pass a statistical test of
multimodality, and about 85% are consistent with a normal distribution.
Study 2 is the sting: 53 computing instructors were shown ambiguous
histograms; those primed with "it is commonly believed CS grades are bimodal"
saw bimodality more often, and instructors who believe ability is innate saw
it more often still — with evidence of a feedback loop in which labelling
distributions bimodal strengthens the innate-ability belief. The authors then
argue the geek-gene belief functions as a *social defense*: it is easier to
attribute non-learning to students' genes than to one's own teaching. They
also link it to equity: fields whose members believe success requires
brilliance have worse gender diversity, and teacher expectations measurably
shape student performance.

The paper is short, statistically gentle, and ends with an invitation you
should take literally as a future teacher: analyse the grades in your own
classes with the same rigour you would demand of a research paper.

### How to read it

Read it whole; it is seven pages. Give real attention to section 2 (what
bimodality technically requires — two well-separated modes, low kurtosis)
because the "eyeballing histograms" error it corrects is one you will be
tempted by every semester, especially with class sizes around 30–100 where
random noise produces bumps. Also note the alternative explanations reviewed
in section 1.1 — especially *coarse assessment*: all-or-nothing exam
questions can manufacture apparent bimodality, which connects directly to the
mixed assessment formats of theme 6.

### Guiding questions

1. Before calling a grade distribution in your own course "bimodal", what
   checks would you now perform? (Bin widths, sample size, ceiling effects,
   a formal test...)
2. Explain the priming experiment to a colleague in three sentences. Why is
   the feedback loop (seeing bimodality → believing in innate ability →
   seeing bimodality) educationally dangerous even if each step is small?
3. How do Patitsas et al. and Robins fit together? Does learning edge
   momentum survive if grades are mostly unimodal? What exactly does it
   still explain (failure tails, variance, the felt experience of
   "snowballing")?
4. The "social defense" argument implies the belief persists because it
   protects teachers. What institutional practices (curve grading, weed-out
   talk, public rankings) feed it, and which of them exist in programmes you
   know?
