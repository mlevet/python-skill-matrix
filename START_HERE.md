# Start Here

This repository is a personal Python interview-preparation system.
It tracks what you know, what is stale, and what to study next —
session by session.

---

> **Current Phase: Calibration**
> The baseline assessment has not been completed yet.
> You do not have a skill profile. Study sessions are not calibrated.
> → **[Run the baseline assessment first](baseline_assessment/README.md)**
> *(Update this banner and [state.md](state.md) when your phase changes.)*

---

## Where Are You?

### I have never used this repository before

You are in **Phase 0 — Calibration**.

→ **[baseline_assessment/README.md](baseline_assessment/README.md)**

Time: 60–90 minutes.
Outcome: A skill profile that tells the system what you actually know.
The review queue, priorities, and study sessions are all meaningless
until this is done.

Do not open `TODAY.md`. Do not open `dashboard.md`. Start here.

---

### I completed the baseline assessment

You are in **Phase 1 — Interview Preparation** or
**Phase 2 — Maintenance**.

→ **[dashboard.md](dashboard.md)**

Time: 25–40 minutes per session.
Outcome: One topic reviewed, mastery updated, queue advanced.

---

### I just completed an interview

→ **[interview_log/](interview_log/)**

Time: 10 minutes.
Outcome: Surprises captured, priorities updated for next time.
Then update [state.md](state.md) to reflect your new phase.

---

## The Three Phases

### Phase 0 — Calibration ← you are here

Before you can study effectively, you need an honest picture of where
you stand. The baseline assessment provides this. It is a one-time
audit, not a study session.

**Entry:** this file  
**Exit:** baseline assessment completed → transfer scores → update state.md

---

### Phase 1 — Interview Preparation

Active study toward a specific interview date. The interview mode
in `dashboard.md` tells you exactly which topics to cover and in
what order, based on frequency × weakness × days remaining.

**Entry:** baseline assessment completed + interview date set  
**Exit:** interview completed → log it → update state.md

---

### Phase 2 — Maintenance

No interview scheduled. Study stale topics, deepen weak ones, add
new domains. Cadence is slower — one session every few days is enough.

**Entry:** no interview in next 4 weeks  
**Exit:** new interview date confirmed → update state.md

---

## Reference

### File map

| File | Purpose |
|---|---|
| [state.md](state.md) | Your current phase and next action |
| [dashboard.md](dashboard.md) | Command center — start every study session here |
| [TODAY.md](TODAY.md) | Pre-planned session *(post-assessment only)* |
| [hall_of_pain.md](hall_of_pain.md) | Every mistake, blank, and surprise |
| [matrix/skill_matrix.md](matrix/skill_matrix.md) | All topics with mastery and freshness |
| [matrix/review_queue.md](matrix/review_queue.md) | Priority-ordered queue with direct links |
| [matrix/interview_mode.md](matrix/interview_mode.md) | Top 10 topics and gaps for the interview |
| [domains/](domains/) | Topic files by domain |
| [drills/](drills/) | Coding exercises |
| [code_reading/](code_reading/) | "What does this print?" puzzles |
| [roadmaps/](roadmaps/) | Structured learning paths |
| [baseline_assessment/](baseline_assessment/) | Day 0 audit files |
| [interview_log/](interview_log/) | Interview records |
| [docs/user_journey.md](docs/user_journey.md) | How the system works end-to-end |

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

Interview mode (deadline active):

```
score = freq_weight × (10 − mastery)
```

Frequency weights: Very High = 4 · High = 3 · Medium = 2 · Low = 1

---

### Hall of Pain rule

Every time you blank on something, get surprised, or fail a drill:
add one entry to [hall_of_pain.md](hall_of_pain.md). Review it
before every real interview. Externalized mistakes are easier to
remember than internal ones.
