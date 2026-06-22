# Review Queue

Topics sorted by priority: high interview frequency + low confidence + stale = top.

Update this after each session by re-sorting based on how scores changed.

---

## How priority works

```
priority = freq_weight × (5 - confidence) × staleness_factor
freq_weight: high=3, medium=2, low=1
staleness_factor: 1 + (days_since_review / 30)
```

All topics start at confidence=0 and never reviewed, so all high-freq topics tie at maximum priority.  
Break ties by your gut: which gap hurts most in an interview?

---

## Queue (initial — all unreviewed)

### Tier 1 — High frequency, not yet reviewed

| Priority | Topic | Domain | Confidence | Days Stale | Freq |
|---|---|---|---|---|---|
| 1 | Closures & late binding | functional_python | 0 | ∞ | high |
| 2 | Lambdas | functional_python | 0 | ∞ | high |
| 3 | Decorators | functional_python | 0 | ∞ | high |
| 4 | Functions as first-class objects | functional_python | 0 | ∞ | high |
| 5 | Dunder / magic methods | oop | 0 | ∞ | high |
| 6 | Inheritance & MRO (C3) | oop | 0 | ∞ | high |
| 7 | LEGB scoping rules | python_internals | 0 | ∞ | high |
| 8 | Python data model | python_internals | 0 | ∞ | high |
| 9 | `is` vs `==` | basics | 0 | ∞ | high |
| 10 | Variables & scoping (LEGB) | basics | 0 | ∞ | high |
| 11 | Built-in types & mutability | basics | 0 | ∞ | high |
| 12 | Comprehensions | basics | 0 | ∞ | high |
| 13 | `*args` and `**kwargs` | basics | 0 | ∞ | high |
| 14 | `map` / `filter` / `reduce` | functional_python | 0 | ∞ | high |
| 15 | Generators & `yield` | advanced_syntax | 0 | ∞ | high |
| 16 | Extended unpacking | advanced_syntax | 0 | ∞ | high |
| 17 | `@classmethod` vs `@staticmethod` | oop | 0 | ∞ | high |
| 18 | list — internals & complexity | data_structures | 0 | ∞ | high |
| 19 | dict — internals & ordering | data_structures | 0 | ∞ | high |
| 20 | `collections` module | stdlib | 0 | ∞ | high |
| 21 | `asyncio` & `await` | concurrency | 0 | ∞ | high |

### Tier 2 — Medium frequency, not yet reviewed

| Priority | Topic | Domain | Confidence | Days Stale | Freq |
|---|---|---|---|---|---|
| 22 | GC & reference counting | python_internals | 0 | ∞ | medium |
| 23 | The GIL | python_internals | 0 | ∞ | medium |
| 24 | Descriptors | oop | 0 | ∞ | medium |
| 25 | `__slots__` | oop | 0 | ∞ | medium |
| 26 | Metaclasses | oop | 0 | ∞ | medium |
| 27 | `dataclasses` | oop | 0 | ∞ | medium |
| 28 | `functools.partial` | functional_python | 0 | ∞ | medium |
| 29 | `functools.lru_cache` | functional_python | 0 | ∞ | medium |
| 30 | `itertools` essentials | functional_python | 0 | ∞ | medium |
| 31 | Context managers | advanced_syntax | 0 | ∞ | medium |
| 32 | Walrus operator | advanced_syntax | 0 | ∞ | medium |
| 33 | Type hints & typing | advanced_syntax | 0 | ∞ | medium |
| 34 | f-strings (advanced) | advanced_syntax | 0 | ∞ | medium |
| 35 | set & frozenset | data_structures | 0 | ∞ | medium |
| 36 | tuple — immutability traps | data_structures | 0 | ∞ | medium |
| 37 | `collections.deque` | data_structures | 0 | ∞ | medium |
| 38 | `collections.defaultdict` | data_structures | 0 | ∞ | medium |
| 39 | `heapq` | data_structures | 0 | ∞ | medium |
| 40 | Exception handling | basics | 0 | ∞ | medium |
| 41 | `threading` basics | concurrency | 0 | ∞ | medium |
| 42 | `multiprocessing` basics | concurrency | 0 | ∞ | medium |
| 43 | `concurrent.futures` | concurrency | 0 | ∞ | medium |
| 44 | `itertools` module | stdlib | 0 | ∞ | medium |
| 45 | `functools` module | stdlib | 0 | ∞ | medium |
| 46 | `re` (regex) | stdlib | 0 | ∞ | medium |
| 47 | `pytest` fixtures | testing_debugging | 0 | ∞ | medium |
| 48 | `unittest.mock` | testing_debugging | 0 | ∞ | medium |

### Tier 3 — Low frequency

| Priority | Topic | Domain | Confidence | Days Stale | Freq |
|---|---|---|---|---|---|
| 49 | Bytecode & `dis` | python_internals | 0 | ∞ | low |
| 50 | Import system | python_internals | 0 | ∞ | low |
| 51 | `collections.namedtuple` | data_structures | 0 | ∞ | low |
| 52 | `pathlib` | stdlib | 0 | ∞ | low |
| 53 | `datetime` | stdlib | 0 | ∞ | low |
| 54 | `pdb` debugger | testing_debugging | 0 | ∞ | low |
| 55 | Profiling | testing_debugging | 0 | ∞ | low |

---

## Completed (confidence ≥ 4)

| Topic | Domain | Confidence | Last Reviewed |
|---|---|---|---|
| — | — | — | — |
