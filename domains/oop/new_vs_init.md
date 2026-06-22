# `__new__` vs `__init__`

## Metadata

| Field | Value |
|---|---|
| Domain | OOP |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | Medium |
| Last Reviewed | Never |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

`__new__` creates the instance; `__init__` initializes it. `__new__` is a static method that receives the class and returns a new instance. `__init__` receives the already-created instance and sets it up. You override `__new__` to control object creation — e.g. for singletons or immutable types.

---

## Mental model

`MyClass(args)` triggers `type.__call__`, which does two things: (1) `instance = MyClass.__new__(MyClass, args)` — create, (2) `instance.__init__(args)` — initialize. `__new__` comes first; `__init__` runs on whatever `__new__` returned.

---

## Why interviewers ask this

"How would you implement a singleton?" almost always leads here. It also tests understanding of the object creation protocol and why `__init__` alone can't prevent multiple instances.

---

## Common traps

- **`__init__` still runs even for a Singleton** — if `__new__` returns an existing instance, `__init__` is called on it again. Guard against this.
- **`__new__` must return an instance** — if it returns something that's not an instance of the class, `__init__` is NOT called.
- **For immutable types** (`str`, `tuple`), you must set the value in `__new__` because the object is already frozen by the time `__init__` runs.

---

## Code-reading examples

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = 0

a = Singleton()
a.value = 42
b = Singleton()
print(a is b)
print(b.value)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
True
0
```

**Why:** `a is b` is `True` — same instance. But `__init__` runs again on `b = Singleton()`, resetting `value` to `0`. This is the Singleton `__init__` trap.

---

## Coding drills

- Fix the Singleton so `__init__` only runs once
- Subclass `str` and use `__new__` to validate the value at creation
- Trace the call sequence for `MyClass(42)` step by step

---

## Related topics

- [Classes are objects](classes_are_objects.md)
- [Dunder methods](dunder_methods.md)
- [Metaclasses](metaclasses.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
