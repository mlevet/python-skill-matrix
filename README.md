# Python Skill Matrix

A personal Python knowledge matrix designed to maintain long-term mastery,
freshness, and interview readiness.

This repository tracks Python topics across multiple domains, with emphasis on:

- pure Python interviews,
- code-reading puzzles,
- functional programming,
- OOP internals,
- advanced syntax,
- Python runtime behavior,
- knowledge freshness,
- ADHD-friendly review workflows.

---

## Quick Start

**First time:** read [START_HERE.md](START_HERE.md), then run the
[baseline assessment](baseline_assessment/README.md) (60–90 min).

**Every session:** open [dashboard.md](dashboard.md) → follow the
link to [TODAY.md](TODAY.md).

---

## Core Files

| File | Purpose |
|---|---|
| [dashboard.md](dashboard.md) | Command center — top priorities, interview countdown, status |
| [START_HERE.md](START_HERE.md) | Orientation for new sessions |
| [TODAY.md](TODAY.md) | Current study session with specific exercise references |
| [hall_of_pain.md](hall_of_pain.md) | Mistakes and surprises logged for targeted review |
| [daily_routine.md](daily_routine.md) | The 5-step daily session |

---

## Matrix Files

| File | Purpose |
|---|---|
| [matrix/skill_matrix.md](matrix/skill_matrix.md) | Every topic with mastery, freshness, and frequency |
| [matrix/review_queue.md](matrix/review_queue.md) | Sorted queue of what to review next, with direct links |
| [matrix/interview_frequency.md](matrix/interview_frequency.md) | Four-tier ranking of topics by interview prevalence |
| [matrix/interview_mode.md](matrix/interview_mode.md) | Top 10 topics and Top 5 gaps for the next interview |
| [matrix/scoring_model.md](matrix/scoring_model.md) | Priority formula and scoring rules |

---

## Content Directories

| Directory | Purpose |
|---|---|
| [baseline_assessment/](baseline_assessment/) | Day 0 audit — 35 topics, self-rating, interview Q, code reading |
| [domains/](domains/) | Deep-dive topic notes by domain |
| [roadmaps/](roadmaps/) | Step-by-step learning paths through each cluster |
| [code_reading/](code_reading/) | Code-reading puzzles — easy / medium / hard |
| [drills/](drills/) | Runnable Python drill files |
| [interview_log/](interview_log/) | Notes from past and mock interviews |
| [templates/](templates/) | Blank templates for new topic files |

---

## Scoring Model

Each topic is scored on three dimensions:

**Mastery (0–10)**
0 = unknown · 5 = understands basics · 7 = can explain in interview ·
10 = can explain, code, debug, and teach

**Freshness**
Fresh ≤ 7 days · Medium ≤ 30 days · Stale > 30 days ·
Critical = important topic unreviewed > 60 days

**Interview Frequency**
Very High · High · Medium · Low

Priority formula:

```
priority = freq_weight × (10 − mastery) × freshness_weight
```

Interview mode formula (when a deadline is active):

```
score = freq_weight × (10 − mastery)
```

Fewer days remaining → only Very High and High frequency topics are
worth your time.

---

## Learning Paths

Structured sequences for studying each cluster end-to-end:

| Path | Steps | File |
|---|---|---|
| Functional Python | 8 steps | [roadmaps/functional_python_path.md](roadmaps/functional_python_path.md) |
| Iteration | 4 steps | [roadmaps/iteration_path.md](roadmaps/iteration_path.md) |
| OOP Internals | 8 steps | [roadmaps/oop_internals_path.md](roadmaps/oop_internals_path.md) |

---

## Domains

| Domain | Topics |
|---|---|
| Functional Python | Lambdas, closures, late binding, decorators, HOF, partial, lru_cache |
| OOP | Dunder methods, MRO, `__call__`, properties, descriptors, metaclasses |
| Python Internals | Scoping, mutability, references, GC, GIL, data model |
| Advanced Syntax | Generators, unpacking, walrus, pattern matching, type hints |
| Data Structures | list, dict, set internals and complexity |
| Concurrency | asyncio, threading, multiprocessing |
| Standard Library | collections, itertools, functools |
| Testing & Debugging | pytest, mock, pdb |
