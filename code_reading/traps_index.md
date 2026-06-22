# Traps Index

A reference of every gotcha encountered across code-reading puzzles, organized by pattern.

Add a row each time you discover a new trap — in a puzzle, in an interview, or in code review.

---

## Closure / late binding

| Trap | Puzzle | Domain |
|---|---|---|
| Loop variable closure captures variable, not value | M1 | functional_python/closures |
| Default argument with `i=i` captures value at definition | M1 (fix) | functional_python/closures |
| Mutable default + late binding compounding | H7 | functional_python/closures |

---

## Mutable defaults

| Trap | Puzzle | Domain |
|---|---|---|
| Default list argument shared across all calls | E1 | basics/functions |
| Default list leaks state across calls | E1 | basics/functions |
| Shared mutable default + closure compounds into surprise output | H7 | functional_python/closures |

---

## Identity vs equality

| Trap | Puzzle | Domain |
|---|---|---|
| `is` checks identity, `==` checks value | E2 | basics/is_vs_eq |
| CPython interns integers -5 to 256 | E3 | basics/is_vs_eq |
| `nan != nan` is True (IEEE 754) | E7 | basics/operators |
| `bool` is a subclass of `int`; `0 == False` is True | E6 | basics/types |

---

## Scope / variable leakage

| Trap | Puzzle | Domain |
|---|---|---|
| `for` loop variable stays in scope after loop | E4 | basics/scoping |
| Comprehension loop variable does NOT leak (Python 3) | M8 | advanced_syntax/walrus |
| Walrus `:=` DOES leak out of comprehension | M8 | advanced_syntax/walrus |

---

## Mutability surprises

| Trap | Puzzle | Domain |
|---|---|---|
| Tuple containing mutable object — tuple is immutable, contents are not | E5 | data_structures/tuple |
| Assigning to `self.x += 1` shadows class variable with instance variable | H3 | oop/dunder_methods |

---

## OOP internals

| Trap | Puzzle | Domain |
|---|---|---|
| Decorator application is bottom-up; execution is outside-in | M3 | functional_python/decorators |
| `super()` follows MRO, not class hierarchy — surprising call order with diamond | M5 | oop/inheritance_mro |
| `__getattribute__` vs `__getattr__` — always vs fallback | H8 | oop/dunder_methods |
| `__slots__` in parent doesn't prevent `__dict__` in child | H4 | oop/slots |
| `__init_subclass__` fires at class definition time | H6 | oop/metaclasses |

---

## Generators

| Trap | Puzzle | Domain |
|---|---|---|
| Generator is exhausted after first `list()` — second call returns `[]` | M6 | advanced_syntax/generators |
| `yield` is an expression; `.send(v)` sets its value | H5 | advanced_syntax/generators |

---

## Decorators

| Trap | Puzzle | Domain |
|---|---|---|
| Without `@wraps`, wrapper hides `__name__`, `__doc__` | M9 | functional_python/decorators |
| Decorator application order is bottom-up | M3 | functional_python/decorators |

---

## Descriptors

| Trap | Puzzle | Domain |
|---|---|---|
| Data descriptor (`__set__` defined) takes priority over `__dict__` in normal access | H1 | oop/descriptors |
| Directly writing to `obj.__dict__` bypasses descriptor `__set__` | H1 | oop/descriptors |

---

## Add your own

| Trap | Source | Domain |
|---|---|---|
| | | |
