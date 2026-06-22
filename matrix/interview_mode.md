# Interview Mode — July 7, 2026

> **Goal-specific:** This file is only relevant when
> `goal: technical_interview` is set in [state.md](../state.md).
> If your goal is different, open
> [START_HERE.md](../START_HERE.md) → Goal Selection instead.

**Target event:** Python technical interview
**Interview date:** 2026-07-07
**Days remaining:** 15 *(update daily)*
**Preparation status:** Baseline assessment not started

→ Run [baseline_assessment/README.md](../baseline_assessment/README.md) first
to calibrate scores. The recommendations below use current mastery
scores from `skill_matrix.md` — they will sharpen after the audit.

---

## Priority Formula

```
score = freq_weight × (10 − mastery)
```

Frequency weights: Very High = 4 · High = 3 · Medium = 2 · Low = 1

With **15 days left**, there is no slack for Medium or Low topics.
Every session must target a Very High or High frequency topic with
mastery below 6.

---

## Top 10 — Review These Before July 7

Ordered by score (freq_weight × weakness). Ties broken by interview
prevalence.

| # | Topic | Freq | Mastery | Score | File |
|---|---|---|---:|---:|---|
| 1 | Generators & `yield` | Very High | 0/10 | **40** | [topic](../domains/advanced_syntax/) |
| 2 | Late binding | Very High | 0/10 | **40** | [topic](../domains/functional_python/late_binding.md) |
| 3 | Comprehensions | High | 0/10 | **30** | — |
| 4 | Context managers | High | 0/10 | **30** | — |
| 5 | LEGB scoping | High | 0/10 | **30** | — |
| 6 | `*args` / `**kwargs` | High | 0/10 | **30** | — |
| 7 | `map` / `filter` / HOF | High | 0/10 | **30** | [topic](../domains/functional_python/higher_order_functions.md) |
| 8 | Iterables vs iterators | High | 0/10 | **30** | — |
| 9 | `is` vs `==` | High | 0/10 | **30** | — |
| 10 | Closures | Very High | 5/10 | **20** | [topic](../domains/functional_python/closures.md) |

Scores drop sharply after these. The next tier (MRO at 18,
`__call__` at 18) only matter if you've completed the Top 10.

---

## Top 5 High-Risk Gaps

These are the topics most likely to end the interview badly — either
Very High frequency with near-zero mastery, or foundational topics
whose absence is immediately visible.

### 1. Generators & `yield` — score 40, mastery 0
An interviewer who asks "walk me through what happens when you call
a generator function" will expose a gap here within 30 seconds.
Covers: function body not executing on call, `next()`, `StopIteration`,
`yield from`, generator expressions.

### 2. Late binding — score 40, mastery 0
The single most common Python surprise question. Any closures or
lambda question can pivot to late binding. Knowing closures at 5/10
is not enough if late binding is 0.

### 3. Closures — score 20, mastery 5
Already half-known, but "half" is not safe. The risk is confidently
explaining closures incorrectly. Specifically: captured by reference
not value, `nonlocal`, cell objects.

### 4. Comprehensions — score 30, mastery 0
Interviewers use comprehensions as shorthand in every code snippet.
Not knowing list/dict/set/generator comprehensions signals a Python
skill floor problem.

### 5. LEGB scoping — score 30, mastery 0
Underpins closures, decorators, and late binding. An interviewer
who probes any of the top topics will reach LEGB within one
follow-up question.

---

## 15-Day Study Plan

At one session per day (~45 min each):

| Days | Topics |
|---|---|
| Day 1–2 | Generators & `yield` |
| Day 3 | Late binding + Closures refresh |
| Day 4 | LEGB scoping |
| Day 5–6 | Comprehensions (list, dict, set, generator) |
| Day 7 | Context managers |
| Day 8 | `*args` / `**kwargs` / function signatures |
| Day 9 | `map` / `filter` / HOF |
| Day 10 | Iterables vs iterators |
| Day 11 | `is` vs `==` / mutability refresh |
| Day 12 | MRO + `__call__` |
| Day 13–14 | Hall of Pain review + code reading pass |
| Day 15 | Mock session — answer each Top 10 aloud, no notes |

---

## After Baseline Assessment

Run `baseline_assessment/` (60–90 min), then:

1. Transfer scores to `matrix/skill_matrix.md`
2. Recompute scores in the table above — mastery values will change
3. Drop any topic that scores Strong from the Top 10
4. Add any Very High or High topic that scored Weak and isn't listed

The formula stays the same. The inputs improve.
