# Long-Term Mastery

> **Goal-specific file.** Only relevant when
> `active_goal: long_term_mastery` in [state.md](../state.md).

No deadline. No countdown. The goal is broad, deep, durable Python
knowledge across all domains — built session by session over months.

---

## When to Use This Goal

- No interview in the next 8 weeks
- You want to close coverage gaps across domains
- You want existing knowledge to stay fresh and deep
- You are building toward fluency, not toward a specific event

---

## How the System Adapts

**Priority formula stays the same:**
```
priority = freq_weight × (10 − mastery) × freshness_weight
```

No time-pressure multiplier. No interview-specific urgency tier.

**What gets surfaced:**
- Stale and Critical topics first (freshness_weight is highest)
- Then High and Very High frequency topics with low mastery
- Coverage gaps — domains with no assessed topics
- Topics assessed as Weak in the baseline audit

**What does not get surfaced:**
- Interview countdown
- Campaign risks
- "Days remaining" urgency

---

## Session Structure

Each session: 25–40 minutes.

1. Open [matrix/review_queue.md](../matrix/review_queue.md)
2. Take the top-priority topic
3. Read the topic file → explain aloud → close
4. Solve linked drill exercises
5. Do the linked code-reading puzzle
6. Update mastery and freshness in [matrix/skill_matrix.md](../matrix/skill_matrix.md)
7. Log any surprises in [hall_of_pain.md](../hall_of_pain.md)

Cadence: 3–5 sessions per week is enough to make steady progress.

---

## Coverage Milestones

Track domain coverage. A domain is "covered" when all its topics
are assessed (mastery > 0) and at least half are ≥ 5/10.

| Domain | Status |
|---|---|
| Functional Python | In progress |
| Iteration | Not started |
| OOP Internals | Not started |
| Runtime Behavior | Not started |
| Advanced Syntax | Not started |
| Data Structures | Not started |
| Concurrency | Not started |
| Standard Library | Not started |

*Update as you progress.*

---

## Switching Goals

If an interview is scheduled: switch to `interview_campaign` or
`single_interview_prep`. The baseline scores transfer directly —
the campaign priority formula uses the same mastery values.

After the interview: return here or set `maintenance`.
