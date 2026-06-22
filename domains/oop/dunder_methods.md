# Dunder Methods

## Metadata

| Field | Value |
|---|---|
| Domain | OOP |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | High |
| Last Reviewed | Never |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

Dunder methods (double-underscore, e.g. `__repr__`, `__add__`, `__len__`) are hooks into Python's object protocol. They define how objects behave with operators, built-in functions, and control flow. Python calls them implicitly — `len(x)` calls `x.__len__()`, `x + y` calls `x.__add__(y)`, and so on.

---

## Mental model

Python syntax is a thin layer over dunder method calls. Every operator, keyword, and built-in function has a corresponding dunder. The Python data model is a catalog of all these hooks.

---

## Why interviewers ask this

A candidate who knows dunder methods can implement rich objects from scratch. Questions range from "implement `__repr__`" to "why does defining `__eq__` break sets?". It also leads into descriptors, context managers, and the iterator protocol.

---

## Common traps

- **`__repr__` fallback:** if only `__repr__` is defined, `str()` uses it. If only `__str__` is defined, `repr()` falls back to the default `<ClassName object>`.
- **`__eq__` kills `__hash__`:** defining `__eq__` sets `__hash__ = None` implicitly — the object becomes unhashable.
- **Reflected operators:** `a + b` tries `a.__add__(b)` first. If it returns `NotImplemented`, Python tries `b.__radd__(a)`.
- **`__getattr__` vs `__getattribute__`:** `__getattr__` is the fallback (missing attributes only); `__getattribute__` intercepts every access — infinite recursion risk.

---

## Code-reading examples

```python
class Box:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return f"Box({self.items!r})"

b = Box([1, 2, 3])
print(len(b))
print(2 in b)
print(b)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
3
True
Box([1, 2, 3])
```

**Why:** `len(b)` → `b.__len__()`, `2 in b` → `b.__contains__(2)`, `print(b)` → `str(b)` → falls back to `__repr__` since `__str__` is not defined.

---

## Coding drills

- Implement a `Vector` class with `__add__`, `__mul__`, `__abs__`, `__repr__`
- Show the `__eq__` / `__hash__` interaction: add to a set before and after defining `__eq__`
- Implement `__enter__` and `__exit__` for a simple resource manager

---

## Related topics

- [Callable objects](callable_objects.md)
- [Descriptors](descriptors.md)
- [Properties](properties.md)
- [`__new__` vs `__init__`](new_vs_init.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
