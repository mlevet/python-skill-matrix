# Start Here

This repository is a personal Python interview-preparation system.
It tracks what you know, what is stale, and what to study next —
session by session.

---

> **Current Phase: Calibration**
> The baseline assessment has not been completed yet.
> → **[Run the baseline assessment first](baseline_assessment/README.md)**
> *(Update this banner and [state.md](state.md) when your phase changes.)*

---

## Where Are You?

### I have never used this repository before

You are in **Phase 0 — Calibration**.

→ **[baseline_assessment/README.md](baseline_assessment/README.md)**

Time: 60–90 minutes.
Outcome: An honest skill profile. The review queue and study sessions
are meaningless until you have one.

Do not open `TODAY.md`. Do not open `dashboard.md`. Start here.

---

### I completed the baseline assessment but haven't set a goal

You are in **Phase 1 — Goal Selection**.

What are you trying to achieve right now?

**Technical Interview** — preparing for a specific upcoming interview.
→ Set `goal: technical_interview` in [state.md](state.md).
→ Fill in `date`, `target_role`, `target_seniority`.
→ Open [dashboard.md](dashboard.md).

**Long-Term Mastery** — no deadline, deepen Python across all domains.
→ Set `goal: long_term_mastery` in [state.md](state.md).
→ Open [matrix/review_queue.md](matrix/review_queue.md).

**Domain Mastery** — focus on one specific domain end-to-end.
→ Set `goal: domain_mastery` and `domain:` in [state.md](state.md).
→ Open the relevant [roadmap](roadmaps/).

**Maintenance** — no active goal, keep existing knowledge fresh.
→ Set `goal: maintenance` in [state.md](state.md).
→ Open [matrix/review_queue.md](matrix/review_queue.md) for stale topics.

---

### I have a goal set and want to study

You are in **Phase 2 — Active**.

→ **[dashboard.md](dashboard.md)**

Time: 25–40 minutes per session.
Outcome: One topic reviewed, mastery updated, queue advanced.

---

### I just completed an interview or finished a goal

→ **[interview_log/](interview_log/)** — capture lessons (10 min)
→ Update [state.md](state.md): set `goal: null`, `phase: goal_selection`
→ Return to Goal Selection above

---

## The Phases

### Phase 0 — Calibration *(current)*

Run the baseline assessment. This is a one-time measurement — not
a study session. The output is your skill profile.

**Entry:** first use
**Exit:** assessment completed → update state.md → Phase 1

---

### Phase 1 — Goal Selection

Choose what you are trying to achieve. The system adapts its
recommendations to your goal. Two users with identical skill profiles
but different goals should study different things.

**Entry:** baseline assessment completed
**Exit:** goal set → update state.md → Phase 2

---

### Phase 2 — Active

Study sessions driven by your goal and skill profile. The dashboard
shows goal-specific recommendations.

**Entry:** goal set
**Exit:** goal achieved or changed → update state.md → Phase 1

---

## Reference

### File map

| File | Purpose |
|---|---|
| [state.md](state.md) | Current phase, goal, and next action |
| [dashboard.md](dashboard.md) | Command center — goal-aware priorities |
| [TODAY.md](TODAY.md) | Pre-planned session *(post-assessment only)* |
| [hall_of_pain.md](hall_of_pain.md) | Every mistake, blank, and surprise |
| [matrix/skill_matrix.md](matrix/skill_matrix.md) | All topics with mastery and freshness |
| [matrix/review_queue.md](matrix/review_queue.md) | Priority-ordered queue with direct links |
| [matrix/interview_mode.md](matrix/interview_mode.md) | Top 10 + gaps *(goal: technical_interview only)* |
| [domains/](domains/) | Topic files by domain |
| [drills/](drills/) | Coding exercises |
| [code_reading/](code_reading/) | "What does this print?" puzzles |
| [roadmaps/](roadmaps/) | Structured learning paths |
| [baseline_assessment/](baseline_assessment/) | Day 0 audit files |
| [interview_log/](interview_log/) | Interview records |
| [docs/user_journey.md](docs/user_journey.md) | End-to-end system diagram |

---

### Mastery scale

| Score | Meaning |
|---|---|
| 0 | Unknown |
| 3 | Recognized but weak |
| 5 | Understand basics |
| 7 | Can explain in an interview |
| 10 | Can explain, code, debug, and teach |

---

### Priority formula

```
priority = freq_weight × (10 − mastery) × freshness_weight
```

Technical interview mode:

```
score = freq_weight × (10 − mastery)
```

Frequency weights: Very High = 4 · High = 3 · Medium = 2 · Low = 1

---

### Hall of Pain rule

Every time you blank on something, get surprised, or fail a drill:
add one entry to [hall_of_pain.md](hall_of_pain.md). Review it
before every real interview.
