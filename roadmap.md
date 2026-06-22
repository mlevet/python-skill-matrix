# Roadmap

Long-term coverage goals. Update when major milestones are hit or priorities shift.

---

## Phase 1 — Foundation (weeks 1–4)

Goal: every topic at confidence ≥ 2 (aware and can explain roughly).

**Priority domains:**
- [ ] Functional Python — lambdas, closures, decorators, `functools`, `itertools`
- [ ] OOP internals — dunder methods, MRO, descriptors, dataclasses
- [ ] Python internals — LEGB scoping, mutability, `is` vs `==`, GC basics
- [ ] Advanced syntax — walrus, unpacking, generators vs. iterators

**Code-reading target:** complete all easy puzzles, start medium.

---

## Phase 2 — Interview-ready core (weeks 5–8)

Goal: functional Python and OOP internals at confidence ≥ 4.

**Priority domains:**
- [ ] Deepen functional Python — `partial`, `lru_cache`, higher-order functions
- [ ] Deepen OOP — `__slots__`, metaclasses, abstract base classes
- [ ] Python internals — bytecode basics, `__dict__` vs `__slots__`, import system
- [ ] Concurrency surface — `threading` vs `multiprocessing` vs `asyncio` (conceptual)

**Code-reading target:** complete all medium puzzles, attempt hard.

---

## Phase 3 — Deep coverage (weeks 9–16)

Goal: all topics at confidence ≥ 3, flagged topics at ≥ 4.

**Priority domains:**
- [ ] Concurrency — asyncio patterns, GIL implications, `concurrent.futures`
- [ ] stdlib fluency — `collections`, `itertools`, `functools`, `pathlib`, `re`
- [ ] Testing & debugging — `pytest` fixtures, `mock`, `pdb`
- [ ] Type system — `Protocol`, generics, `TypeVar`, `Literal`

**Code-reading target:** complete hard puzzles, revisit medium ones from memory.

---

## Phase 4 — Maintenance (ongoing)

Goal: confidence never drops below 3 on high-frequency topics due to staleness.

- Weekly: review the stalest high-freq topic.
- Monthly: re-score the entire matrix honestly.
- After each interview: log unexpected topics, add new puzzles to code_reading/.

---

## Coverage tracker

| Domain | Topics | ≥2 | ≥3 | ≥4 | ≥5 |
|---|---|---|---|---|---|
| basics | 6 | 0 | 0 | 0 | 0 |
| data_structures | 8 | 0 | 0 | 0 | 0 |
| functional_python | 8 | 0 | 0 | 0 | 0 |
| oop | 7 | 0 | 0 | 0 | 0 |
| python_internals | 6 | 0 | 0 | 0 | 0 |
| advanced_syntax | 6 | 0 | 0 | 0 | 0 |
| concurrency | 4 | 0 | 0 | 0 | 0 |
| stdlib | 6 | 0 | 0 | 0 | 0 |
| testing_debugging | 4 | 0 | 0 | 0 | 0 |
| **Total** | **55** | **0** | **0** | **0** | **0** |

> Update this table after each phase milestone.
