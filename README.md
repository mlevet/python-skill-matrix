# python-skill-matrix

A personal Python knowledge-management and interview-preparation system.

---

## What this repo is

Not a course. Not a cheat sheet. A living system to:

- track what you know and how fresh it is
- drill the exact patterns that appear in technical interviews
- make the daily "what should I study?" decision in under 30 seconds
- build interview-readiness that doesn't fade between sessions

---

## Navigation

| File / Folder | Purpose |
|---|---|
| [dashboard.md](dashboard.md) | **Start here every session** — what to do today |
| [daily_routine.md](daily_routine.md) | The 15–30 min daily workflow |
| [roadmap.md](roadmap.md) | Long-term topic coverage goals |
| [matrix/skill_matrix.md](matrix/skill_matrix.md) | Master table — every topic, confidence, freshness |
| [matrix/review_queue.md](matrix/review_queue.md) | Sorted list of what to tackle next |
| [matrix/scoring_model.md](matrix/scoring_model.md) | What the scores mean and how to update them |
| [domains/](domains/) | Deep-dive notes per topic |
| [code_reading/](code_reading/) | "What does this print?" puzzles by difficulty |
| [drills/](drills/) | Runnable Python drill files |
| [interview_log/](interview_log/) | Notes from past/mock interviews |
| [templates/](templates/) | Blank templates to copy when adding new content |
| [scripts/](scripts/) | Helper scripts (optional automation) |

---

## Core scoring concepts

**Confidence (0–5):** self-assessed ability to explain and code the topic under interview pressure.  
**Freshness:** days since last review — decays fast.  
**Interview frequency:** how often the topic appears in real Python interviews.  
**Priority:** high interview frequency × low confidence × stale = review first.

See [matrix/scoring_model.md](matrix/scoring_model.md) for the full rubric.

---

## Interview focus areas

Based on real interview experience, these domains carry the most weight:

1. Functional Python — lambdas, closures, decorators, `functools`
2. OOP internals — `__dunder__` methods, MRO, descriptors
3. Python internals — scoping (LEGB), GC, the data model
4. Code-reading traps — unexpected output, late binding, mutability surprises
5. Advanced syntax — walrus, unpacking, generators

---

## Workflow in one sentence

Open `dashboard.md`, pick the top item from the review queue, read the topic file, run the matching drill, update your confidence score, close laptop.
