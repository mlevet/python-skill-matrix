---
topic: is vs ==
domain: basics
confidence: 0
last_reviewed: never
interview_freq: high
---

# `is` vs `==`

## Summary

`==` tests value equality (calls `__eq__`). `is` tests identity — whether two names refer to the exact same object in memory. They are not interchangeable, and confusing them is one of the most common Python interview traps.

---

## Key concepts

- `is` compares `id()` values — same memory address.
- `==` calls `__eq__` — can be overridden; two distinct objects can be `==`.
- CPython interns small integers (-5 to 256) and some strings — `is` may return `True` for them coincidentally.
- Always use `==` for value comparison. Use `is` only for `None`, `True`, `False`, and identity checks.
- `is not None` is the idiomatic None check — never `!= None`.

---

## Code examples

### Lists

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  — same values
print(a is b)   # False — different objects
print(a is c)   # True  — c is an alias for a
```

### Integer interning

```python
x = 256
y = 256
print(x is y)   # True  — CPython interns -5 to 256

a = 257
b = 257
print(a is b)   # False — above the interning range (in most contexts)
```

### None check

```python
value = None

# Correct:
if value is None: ...
if value is not None: ...

# Fragile (could be overridden by __eq__):
if value == None: ...
```

### `float('nan')`

```python
import math
x = float('nan')
print(x == x)    # False  ← nan is not equal to itself
print(x is x)    # True   ← but it is the same object
print(math.isnan(x))  # True  ← correct way to check
```

---

## Common traps

- **Integer interning:** `256 is 256` is `True` in CPython but this is an implementation detail — don't rely on it.
- **String interning:** string literals are often interned; dynamically built strings may not be.
- **`nan != nan`:** the only Python value not equal to itself. Use `math.isnan()`.
- **`bool is int`:** `True == 1` and `False == 0` because `bool` subclasses `int`.

---

## Interview angle

- "What's the difference between `is` and `==`?" → identity vs equality
- "What does this code print: `257 is 257`?" → it depends on context, but generally `False` for CPython
- "How should you check for None?" → `x is None`

---

## Linked drill

`drills/advanced_syntax.py` is not specific here; see code-reading puzzles.

---

## Linked code-reading puzzles

- `code_reading/easy.md` — Puzzle E2, E3, E7

---

## Review notes

