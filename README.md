# Python Skill Matrix

A personal Python knowledge matrix designed to maintain long-term mastery, freshness, and interview readiness.

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

## Goals

- Know what I know
- Know what is stale
- Know what is weak
- Track unexpected interview questions
- Build reusable code-reading drills
- Maintain Python interview readiness over time

---

## Core files

| File | Purpose |
|---|---|
| [dashboard.md](dashboard.md) | Start here — global status and top priorities |
| [matrix/skill_matrix.md](matrix/skill_matrix.md) | Every topic with mastery, freshness, and priority |
| [matrix/review_queue.md](matrix/review_queue.md) | Sorted queue of what to review next |
| [matrix/scoring_model.md](matrix/scoring_model.md) | Priority formula and scoring rules |
| [daily_routine.md](daily_routine.md) | The 5-step daily session |
| [code_reading/](code_reading/) | Code-reading puzzles by difficulty |
| [domains/](domains/) | Deep-dive topic notes |
| [drills/](drills/) | Runnable Python drill files |
| [interview_log/](interview_log/) | Notes from past and mock interviews |
| [templates/](templates/) | Blank templates for new content |

---

## Method

Each topic is scored on:

- **Mastery** (0–10): from unknown to can explain, code, debug, and teach
- **Freshness**: Fresh / Medium / Stale / Critical based on days since last review
- **Interview Frequency**: Low / Medium / High / Very High

Priority is computed as:

```
Priority = Interview Frequency Weight × (10 − Mastery) × Freshness Weight
```

The highest-priority topics are reviewed first.

---

## Domains

| Domain | Focus |
|---|---|
| Functional Python | Lambdas, closures, decorators, higher-order functions |
| OOP | Dunder methods, MRO, descriptors, metaclasses |
| Python Internals | Scoping, mutability, GC, data model |
| Advanced Syntax | Generators, unpacking, walrus, pattern matching |
| Data Structures | list, dict, set internals and complexity |
| Concurrency | asyncio, threading, multiprocessing |
| Standard Library | collections, itertools, functools |
| Testing & Debugging | pytest, mock, pdb |
