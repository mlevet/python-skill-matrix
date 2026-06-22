# Classes are Objects

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

In Python, classes are objects too — instances of `type`. `type(MyClass)` returns `<class 'type'>`. Because classes are objects, they can be assigned to variables, stored in dicts, passed as arguments, returned from functions, and even created dynamically with `type()`.

---

## Mental model

The class definition `class Foo: ...` creates a `type` object and binds it to the name `Foo`. It is not special syntax that lives outside the object system — it is just another object, created at runtime.

---

## Why interviewers ask this

Tests deep understanding of Python's object model and opens the door to metaclasses. A candidate who understands that classes are `type` instances can reason about class decorators, `type(name, bases, dict)` dynamic class creation, and why `isinstance(MyClass, type)` is `True`.

---

## Common traps

- **`type()` is dual-purpose:** `type(obj)` returns the type of `obj`; `type(name, bases, dict)` creates a new class.
- **`isinstance` vs `type`:** `isinstance(True, int)` is `True` (bool is a subclass of int); `type(True) is int` is `False`.
- **Class attributes are shared:** accessing `MyClass.attr` and modifying it affects all instances that haven't shadowed it.

---

## Code-reading examples

```python
class Dog:
    sound = "woof"

print(type(Dog))
print(isinstance(Dog, type))

Animal = Dog
print(Animal.sound)
print(Animal is Dog)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
<class 'type'>
True
woof
True
```

**Why:** `Dog` is a `type` instance. Assigning it to `Animal` just adds another reference — same object, so `is` is `True`.

---

## Coding drills

- Create a class dynamically using `type("MyClass", (object,), {"x": 42})`
- Show that a class stored in a list can be instantiated from that list
- Write a function that returns a different class based on a string argument

---

## Related topics

- [Metaclasses](metaclasses.md)
- [Dunder methods](dunder_methods.md)
- [MRO](mro.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
