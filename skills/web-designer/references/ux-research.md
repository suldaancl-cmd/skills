# UX research & design

Design without research is guessing. Research without synthesis is trivia. Both must serve decisions.

## The short loop

1. **Frame the question** — What decision does this research inform? If none, don't do it.
2. **Pick the method** matching the question (see below).
3. **Recruit honestly** — real users of the problem, not friends of the company.
4. **Run the sessions** — listen more than you talk.
5. **Synthesize into patterns** — not quotes, patterns.
6. **Decide** — research that doesn't change the design is a waste.

## Method selection

| Question | Method | Sample size |
|---|---|---|
| Who are our users and what do they need? | Generative interviews | 5–8 per segment |
| Does this design work? | Usability test (moderated) | 5 users finds 85% of issues (Nielsen) |
| How do users behave at scale? | Analytics + session recording | Full population |
| Which of A or B works better? | A/B test | Statistical power calc — usually 10k+ |
| Why did users behave this way? | Follow-up interview | 5–8 |
| Is this concept worth building? | Prototype + test | 5 |
| How satisfied are users? | Survey (NPS, CSAT, SUS) | 100+ for reliability |

## Personas — research-backed, not fictional

A persona is a synthesis of real user data, not a character sheet.

**Template:**

```
Name / Role
Archetype label (e.g., "Time-constrained operator")

JOBS TO BE DONE
- Primary: [what they're trying to accomplish]
- Secondary: [adjacent outcomes]

CONTEXT
- Where they encounter the problem
- Tools they already use
- Who else is involved

PAIN POINTS (ranked by frequency × severity)
1. ...
2. ...

MOTIVATIONS
- What "good" looks like to them
- What they'll pay for / switch for

BEHAVIORAL TRAITS (observed, not assumed)
- ...

QUOTES (from interviews — verbatim)
- "..."

ANTI-PATTERNS — what they are NOT
- ...
```

Skip demographic fluff (age, hobbies) unless it's load-bearing for the product. "Loves coffee" never improved a design.

## Journey maps

A journey map is not a flowchart. It's emotion + action + thought over time.

**Swim lanes:**
1. **Phase** — awareness, consideration, onboarding, regular use, issue, advocacy
2. **Actions** — what they do
3. **Thoughts** — what they're asking themselves
4. **Emotions** — line graph from frustrated to delighted
5. **Touchpoints** — where your product shows up
6. **Pain / opportunity** — the design brief for that moment

Focus on the **valleys** (emotional lows) — those are where design has the highest leverage.

## Usability testing

### Moderated think-aloud

**Script skeleton:**
1. **Warm-up** (2 min) — "Tell me about the last time you [did the task in general]."
2. **Task scenarios** (15 min each, 3 max) — "You're trying to [goal]. Show me how you'd do that here."
   - Don't lead. Ask "what are you thinking?" when they go quiet.
   - Never explain the UI unless they're completely stuck and blocking.
3. **Debrief** (5 min) — "What was confusing? What was easy?"

### What to measure
- **Task success rate** — did they complete it?
- **Time on task** — only compare relative (before/after), not absolute.
- **Errors** — miscliks, wrong paths, abandonment.
- **Satisfaction** — SUS (10-question standard) or single-question SEQ (1–7).

### Sample size
- 5 users finds 85% of usability issues on a single persona.
- Don't test 1 persona with 20 people; test 3 personas with 5 each.

## Synthesis — from interviews to insight

### Affinity diagramming
1. Each observation / quote → sticky note.
2. Cluster by theme (without pre-deciding themes).
3. Name each cluster.
4. Identify patterns that recur across participants.
5. Pattern must appear in ≥3 participants to be reportable.

### Insight statement template
> **Observation**: [What we saw]
> **So what**: [Why it matters]
> **Now what**: [Design implication]

Bad: "Users clicked the wrong button."
Good: "Users confused Save and Submit because the UI uses the same color for both, leading to abandoned drafts. Consider distinct visual weight or labeling."

## Empathy map (for a single user)

Quadrants:
- **Says** — direct quotes
- **Thinks** — what they're not saying aloud
- **Does** — observed behavior
- **Feels** — emotional state at key moments

Bridges: **Pains** (negative) + **Gains** (positive). These map directly to product opportunities.

## Research repository

Every study should produce:
1. **Raw notes / recordings** — archived.
2. **Top-line report** — decision-focused, 1 page.
3. **Atomic insights** — tagged, searchable, linkable from roadmap tickets.

Don't let research become shelfware. If it's not linked from a design file or a ticket, it might as well not exist.

## Common research mistakes

- **Leading questions** — "How much do you love feature X?" → "Tell me about the last time you used feature X."
- **Asking about the future** — "Would you use this?" is worthless. "Show me how you solved this last month" is gold.
- **Conflating preference with need** — users will say they want choice; they actually want correct defaults.
- **Designing for the vocal 1%** — users who email support are not representative.
- **Stopping at 'n'** — if you see a new theme emerging in session 5, recruit more. If themes saturated at session 3, stop.

## Triggers to do more research

- Team is arguing based on opinion, not data.
- Metrics show a drop but no hypothesis explains it.
- Scope is expanding and you don't know if the new surface solves a real problem.
- You're building something novel with no analog to reference.

## Triggers to NOT do research

- You already know the answer; you're research-laundering a decision.
- The question is "what should this button be called" — just A/B test, or just pick and ship.
- The cost of being wrong is low and reversible.
