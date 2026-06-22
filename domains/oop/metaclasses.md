# Metaclasses

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

A metaclass is the class of a class. Just as instances are created by classes, classes are created by metaclasses. The default metaclass is `type`. You can write a custom metaclass to intercept class creation, enforce constraints, or auto-register subclasses.

---

## Mental model

The class hierarchy goes: `object` is the base of all instances; `type` is the base of all classes. When you write `class Foo: ...`, Python calls `type("Foo", bases, namespace)` to create the class object. A metaclass replaces `type` in this process.

---

## Why interviewers ask this

Metaclasses signal deep Python knowledge. They appear in "how does Django's ORM know your model fields?" or "how would you enforce that all subclasses implement a method?". The honest answer in an interview: "they're powerful but rare — I'd reach for `__init_subclass__` or class decorators first."

---

## Common traps

- **`__init_subclass__` is usually enough** — use metaclasses only when `__init_subclass__` can't do the job.
- **Metaclass conflicts:** if two base classes have different metaclasses, Python raises `TypeError` unless one inherits from the other.
- **`__new__` on a metaclass** controls class creation (not instance creation).

---

## Code-reading examples

```python
class RegistryMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:
            RegistryMeta.registry[name] = cls
        return cls

class Base(metaclass=RegistryMeta):
    pass

class Alpha(Base):
    pass

class Beta(Base):
    pass

print(list(RegistryMeta.registry.keys()))
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
['Alpha', 'Beta']
```

**Why:** `RegistryMeta.__new__` is called each time a class is defined. `Base` itself is excluded by the `if bases:` guard. `Alpha` and `Beta` are registered automatically.

---

## Coding drills

- Rewrite the auto-registration example using `__init_subclass__` instead
- Write a metaclass that raises `TypeError` if a subclass doesn't implement `process()`
- Explain the difference between a metaclass `__new__` and a class `__new__`

---

## Related topics

- [Classes are objects](classes_are_objects.md)
- [MRO](mro.md)
- [`__new__` vs `__init__`](new_vs_init.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
