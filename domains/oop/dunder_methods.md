---
topic: Dunder / Magic Methods
domain: oop
confidence: 0
last_reviewed: never
interview_freq: high
---

# Dunder / Magic Methods

## Summary

Dunder methods (double-underscore methods like `__init__`, `__repr__`, `__add__`) are Python's protocol for operator overloading and hook points in the object lifecycle. They form the "Python data model" — the mechanism by which Python's syntax translates to method calls.

---

## Key concepts

- Called by the interpreter, not directly by user code (mostly).
- `__repr__`: unambiguous string for developers; used by `repr()`, REPL, `[item]` in lists.
- `__str__`: readable string for end users; used by `str()`, `print()`, `f"{}"`.
- `__eq__`, `__lt__`, etc.: comparison operators. Defining `__eq__` also makes `__hash__` None (object becomes unhashable) unless you also define `__hash__`.
- `__len__`, `__getitem__`, `__iter__`: sequence/container protocol.
- `__call__`: makes an instance callable.
- `__enter__` / `__exit__`: context manager protocol.
- `__getattr__` vs `__getattribute__`: fallback vs intercept.

---

## Code examples

### Arithmetic operators

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):   # scalar * vector
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(1, 2) + Vector(3, 4)   # calls __add__
print(v)           # Vector(4, 6)
print(3 * v)       # Vector(12, 18)  ← __rmul__
```

### `__repr__` vs `__str__`

```python
class Point:
    def __repr__(self): return "Point(repr)"
    def __str__(self):  return "Point(str)"

p = Point()
print(str(p))    # Point(str)
print(repr(p))   # Point(repr)
print(f"{p}")    # Point(str)   ← __str__
print(f"{p!r}")  # Point(repr)  ← forced __repr__
print([p])       # [Point(repr)] ← list uses __repr__
```

### Context manager

```python
class ManagedFile:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # don't suppress exceptions
```

### `__getattr__` vs `__getattribute__`

```python
class Demo:
    def __init__(self):
        self.x = 1

    def __getattr__(self, name):
        # Only called when normal lookup fails
        return f"missing: {name}"

    # __getattribute__ is called for EVERY attribute access — override with care
```

### `__eq__` and hashability

```python
class MyObj:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val
    # __hash__ is now implicitly None → unhashable
    # To keep hashable: define __hash__ = object.__hash__ (or a custom one)
```

---

## Common traps

- **`__str__` fallback to `__repr__`:** if only `__repr__` is defined, `str()` uses it. If only `__str__` is defined, `repr()` returns the default `<ClassName object at 0x...>`.
- **`__eq__` kills `__hash__`:** defining `__eq__` implicitly sets `__hash__ = None`, making instances unhashable (can't be used as dict keys or in sets).
- **`__getattr__` vs `__getattribute__`:** `__getattr__` is safe (only runs on missing attributes). `__getattribute__` runs on every access — an infinite recursion bug is easy to introduce.
- **Reflected operators:** `a + b` tries `a.__add__(b)` first; if that returns `NotImplemented`, Python tries `b.__radd__(a)`.

---

## Interview angle

- "What's the difference between `__repr__` and `__str__`?"
- "How do you implement operator overloading?" → `__add__`, `__mul__`, etc.
- "Why does defining `__eq__` break hashing?"
- "What's the context manager protocol?" → `__enter__` / `__exit__`

---

## Linked drill

`drills/oop_internals.py` — Exercises 1, 7

---

## Linked code-reading puzzles

- `code_reading/hard.md` — Puzzle H3 (class var shadowing), H8 (`__getattr__` vs `__getattribute__`)

---

## Review notes

