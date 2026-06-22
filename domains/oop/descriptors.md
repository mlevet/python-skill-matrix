# Descriptors

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

A descriptor is any object that defines `__get__`, `__set__`, or `__delete__`. When such an object is a class attribute, Python routes attribute access through these methods instead of the usual `__dict__` lookup. `property`, `staticmethod`, and `classmethod` are all descriptors.

---

## Mental model

Descriptors are attribute interceptors living on the class. When you access `obj.attr`, Python checks whether `type(obj).attr` is a descriptor and routes the access through it — before looking in `obj.__dict__`.

**Data descriptor** (defines `__set__`): takes priority over instance `__dict__`.  
**Non-data descriptor** (only `__get__`): instance `__dict__` takes priority.

---

## Why interviewers ask this

Descriptors are the mechanism behind `property`, `classmethod`, and `staticmethod`. Knowing them signals senior-level Python understanding. They appear in "how would you implement a typed attribute?" or "how does `property` work internally?" questions.

---

## Common traps

- **Data vs non-data priority:** a data descriptor shadows the instance dict; a non-data descriptor doesn't.
- **`__set_name__` hook:** called when the descriptor is assigned to a class body — lets the descriptor know its own name.
- **Writing to `obj.__dict__` bypasses `__set__`** even for data descriptors — but `__get__` will still be called on attribute access.

---

## Code-reading examples

```python
class Positive:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class Circle:
    radius = Positive()

c = Circle()
c.radius = 5
print(c.radius)
c.radius = -1
```

**Question:** What does this output/raise?

**Prediction:** write your answer before checking.

**Answer:**
```
5
ValueError: radius must be positive
```

**Why:** `Positive` is a data descriptor (has `__set__`). Assignment routes through `__set__`, which validates before storing in `obj.__dict__`.

---

## Coding drills

- Implement a `TypedAttribute` descriptor that enforces a type on assignment
- Show the difference in lookup priority between a data and non-data descriptor
- Explain how `property` is implemented as a descriptor

---

## Related topics

- [Properties](properties.md)
- [Dunder methods](dunder_methods.md)
- [Classes are objects](classes_are_objects.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
