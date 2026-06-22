---
topic: GC & Reference Counting
domain: python_internals
confidence: 0
last_reviewed: never
interview_freq: medium
---

# GC & Reference Counting

## Summary

CPython uses reference counting as its primary memory management mechanism: every object stores a count of references to it, and is freed when the count reaches zero. A cyclic garbage collector (GC) handles reference cycles that reference counting alone cannot free.

---

## Key concepts

- `sys.getrefcount(obj)` returns the reference count (adds 1 for the function call itself).
- When refcount hits 0, `__del__` is called (if defined) and the object is freed.
- Reference cycles: A → B → A prevents both from reaching refcount 0 even when unreachable.
- The cyclic GC (`gc` module) periodically collects cycles by detecting unreachable objects.
- Three generations: new objects start in gen 0; surviving objects are promoted.
- `__del__` is not guaranteed to be called promptly (or at all for cycle members before Python 3.4).

---

## Code examples

### Checking refcount

```python
import sys

x = []
print(sys.getrefcount(x))   # 2 (x + the function call argument)

y = x
print(sys.getrefcount(x))   # 3

del y
print(sys.getrefcount(x))   # 2
```

### Reference cycles

```python
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

a = Node("A")
b = Node("B")
a.other = b   # A → B
b.other = a   # B → A  (cycle!)

del a
del b
# Both still alive — refcounts are 1 (from each other's .other)
# They will only be freed by the cyclic GC

gc.collect()   # trigger manually
```

### `weakref` — reference without ownership

```python
import weakref

class Big:
    pass

obj = Big()
ref = weakref.ref(obj)

print(ref())       # <Big object>  — still alive
del obj
print(ref())       # None  — was collected
```

### `gc` module basics

```python
import gc

gc.disable()   # turn off cyclic GC (risky — only if you control all lifecycle)
gc.enable()
gc.collect()   # force a collection cycle
print(gc.get_count())   # (gen0, gen1, gen2) collection counts
```

---

## Common traps

- **`sys.getrefcount` overcounts by 1:** the temporary argument in the call itself is a reference.
- **`__del__` is not a destructor in the C++ sense:** don't rely on it for critical cleanup. Use context managers instead.
- **Cycles involving `__del__` (pre-3.4):** objects with `__del__` in a cycle were never freed. Fixed in Python 3.4 with PEP 442.
- **`weakref` for caches:** if you cache objects by reference and want the cache to not prevent GC, use `weakref.WeakValueDictionary`.

---

## Interview angle

- "How does Python manage memory?" → reference counting + cyclic GC
- "What is a reference cycle and why is it a problem?" → prevents refcount from reaching 0
- "What's a `weakref`?" → a reference that doesn't increment the refcount

---

## Linked drill

No dedicated drill — understanding is conceptual + `sys` / `gc` module exploration.

---

## Linked code-reading puzzles

None directly — usually a follow-up question after OOP or closure questions.

---

## Review notes

