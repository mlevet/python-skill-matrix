# Skill Matrix

Master topic table. Update `confidence` and `last_reviewed` after every session.

See [scoring_model.md](scoring_model.md) for what the scores mean.

---

## How to read this table

- **Confidence:** 0 (blank) → 5 (interview-ready)
- **Last reviewed:** YYYY-MM-DD or `never`
- **Interview freq:** high / medium / low
- **Topic file:** link to the domain notes file

---

## basics

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| Variables & scoping (LEGB) | 0 | never | high | [link](../domains/basics/variables_scoping.md) |
| Built-in types & mutability | 0 | never | high | [link](../domains/basics/types_mutability.md) |
| `is` vs `==` | 0 | never | high | [link](../domains/basics/is_vs_eq.md) |
| Exception handling | 0 | never | medium | [link](../domains/basics/exceptions.md) |
| Comprehensions (list/dict/set/gen) | 0 | never | high | [link](../domains/basics/comprehensions.md) |
| `*args` and `**kwargs` | 0 | never | high | [link](../domains/basics/args_kwargs.md) |

---

## data_structures

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| list — internals & complexity | 0 | never | high | [link](../domains/data_structures/list.md) |
| dict — internals & ordering | 0 | never | high | [link](../domains/data_structures/dict.md) |
| set & frozenset | 0 | never | medium | [link](../domains/data_structures/set.md) |
| tuple — immutability traps | 0 | never | medium | [link](../domains/data_structures/tuple.md) |
| `collections.deque` | 0 | never | medium | [link](../domains/data_structures/deque.md) |
| `collections.defaultdict` | 0 | never | medium | [link](../domains/data_structures/defaultdict.md) |
| `collections.namedtuple` | 0 | never | low | [link](../domains/data_structures/namedtuple.md) |
| `heapq` | 0 | never | medium | [link](../domains/data_structures/heapq.md) |

---

## functional_python

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| Lambdas | 0 | never | high | [link](../domains/functional_python/lambdas.md) |
| Closures & late binding | 0 | never | high | [link](../domains/functional_python/closures.md) |
| Decorators | 0 | never | high | [link](../domains/functional_python/decorators.md) |
| `map` / `filter` / `reduce` | 0 | never | high | [link](../domains/functional_python/map_filter_reduce.md) |
| `functools.partial` | 0 | never | medium | [link](../domains/functional_python/functools.md) |
| `functools.lru_cache` | 0 | never | medium | [link](../domains/functional_python/functools.md) |
| `itertools` essentials | 0 | never | medium | [link](../domains/functional_python/itertools.md) |
| Functions as first-class objects | 0 | never | high | [link](../domains/functional_python/first_class_functions.md) |

---

## oop

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| Dunder / magic methods | 0 | never | high | [link](../domains/oop/dunder_methods.md) |
| Inheritance & MRO (C3) | 0 | never | high | [link](../domains/oop/inheritance_mro.md) |
| Descriptors (`__get__`, `__set__`) | 0 | never | medium | [link](../domains/oop/descriptors.md) |
| `@classmethod` vs `@staticmethod` | 0 | never | high | [link](../domains/oop/classmethods.md) |
| `__slots__` | 0 | never | medium | [link](../domains/oop/slots.md) |
| Metaclasses | 0 | never | medium | [link](../domains/oop/metaclasses.md) |
| `dataclasses` | 0 | never | medium | [link](../domains/oop/dataclasses.md) |

---

## python_internals

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| LEGB scoping rules | 0 | never | high | [link](../domains/python_internals/scoping_legb.md) |
| GC & reference counting | 0 | never | medium | [link](../domains/python_internals/gc_memory.md) |
| The GIL | 0 | never | medium | [link](../domains/python_internals/gil.md) |
| Python data model (`__dunder__`) | 0 | never | high | [link](../domains/python_internals/data_model.md) |
| Bytecode & `dis` | 0 | never | low | [link](../domains/python_internals/bytecode.md) |
| Import system | 0 | never | low | [link](../domains/python_internals/import_system.md) |

---

## advanced_syntax

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| Generators & `yield` | 0 | never | high | [link](../domains/advanced_syntax/generators.md) |
| Walrus operator (`:=`) | 0 | never | medium | [link](../domains/advanced_syntax/walrus.md) |
| Extended unpacking | 0 | never | high | [link](../domains/advanced_syntax/unpacking.md) |
| Context managers (`__enter__`/`__exit__`) | 0 | never | medium | [link](../domains/advanced_syntax/context_managers.md) |
| f-strings (advanced) | 0 | never | medium | [link](../domains/advanced_syntax/fstrings.md) |
| Type hints & `typing` module | 0 | never | medium | [link](../domains/advanced_syntax/type_hints.md) |

---

## concurrency

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| `threading` basics | 0 | never | medium | [link](../domains/concurrency/threading.md) |
| `multiprocessing` basics | 0 | never | medium | [link](../domains/concurrency/multiprocessing.md) |
| `asyncio` & `await` | 0 | never | high | [link](../domains/concurrency/asyncio.md) |
| `concurrent.futures` | 0 | never | medium | [link](../domains/concurrency/concurrent_futures.md) |

---

## stdlib

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| `collections` module | 0 | never | high | [link](../domains/stdlib/collections.md) |
| `itertools` module | 0 | never | medium | [link](../domains/stdlib/itertools.md) |
| `functools` module | 0 | never | medium | [link](../domains/stdlib/functools.md) |
| `pathlib` | 0 | never | low | [link](../domains/stdlib/pathlib.md) |
| `re` (regex) | 0 | never | medium | [link](../domains/stdlib/re.md) |
| `datetime` | 0 | never | low | [link](../domains/stdlib/datetime.md) |

---

## testing_debugging

| Topic | Confidence | Last Reviewed | Interview Freq | Topic File |
|---|---|---|---|---|
| `pytest` fixtures & parametrize | 0 | never | medium | [link](../domains/testing_debugging/pytest.md) |
| `unittest.mock` | 0 | never | medium | [link](../domains/testing_debugging/mock.md) |
| `pdb` debugger | 0 | never | low | [link](../domains/testing_debugging/pdb.md) |
| Profiling (`cProfile`, `line_profiler`) | 0 | never | low | [link](../domains/testing_debugging/profiling.md) |

---

## Summary

| Domain | Topics | Avg Confidence |
|---|---|---|
| basics | 6 | 0.0 |
| data_structures | 8 | 0.0 |
| functional_python | 8 | 0.0 |
| oop | 7 | 0.0 |
| python_internals | 6 | 0.0 |
| advanced_syntax | 6 | 0.0 |
| concurrency | 4 | 0.0 |
| stdlib | 6 | 0.0 |
| testing_debugging | 4 | 0.0 |
| **Total** | **55** | **0.0** |
