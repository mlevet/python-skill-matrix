# OOP Internals Learning Path

Covers the Python object model — how classes, instances, and attribute
lookup actually work under the hood.

**Estimated total time:** 4–5 sessions of 30 minutes each.

---

## The Path

```
Classes Are Objects
       ↓
Dunder Methods
       ↓
__call__ and Callable Objects
       ↓
Properties
       ↓
Descriptors
       ↓
__new__ vs __init__
       ↓
MRO and super()
       ↓
Metaclasses
```

---

## Step 1 — Classes Are Objects

In Python, a class is an instance of `type`. This unlocks everything
else in this path.

→ [Topic](../domains/oop/classes_are_objects.md)  
→ [Drill](../drills/oop_internals.py)

**You're ready for Step 2 when:** you can explain what
`type(MyClass)` returns and why.

---

## Step 2 — Dunder Methods

The Python data model. `__repr__`, `__str__`, `__len__`, `__eq__`,
`__hash__`, `__contains__`.

→ [Topic](../domains/oop/dunder_methods.md)  
→ [Drill](../drills/oop_internals.py)

**You're ready for Step 3 when:** you can explain the difference
between `__repr__` and `__str__` and when Python calls each.

---

## Step 3 — `__call__` and Callable Objects

Any object with `__call__` can be used as a function.

→ [Topic](../domains/oop/callable_objects.md)  
→ [Drill](../drills/oop_internals.py)  
→ [Code Reading M11](../code_reading/medium.md)

**You're ready for Step 4 when:** you can implement a stateful
callable that counts how many times it has been called.

---

## Step 4 — Properties

`@property`, `@setter`, `@deleter` — computed attributes without
breaking the interface.

→ [Topic](../domains/oop/properties.md)  
→ [Drill](../drills/oop_internals.py)

**You're ready for Step 5 when:** you can convert a plain attribute
to a validated property without changing how callers access it.

---

## Step 5 — Descriptors

The protocol behind `@property`, `@classmethod`, and `@staticmethod`.

→ [Topic](../domains/oop/descriptors.md)  
→ [Code Reading H1](../code_reading/hard.md)

**You're ready for Step 6 when:** you can explain the difference
between a data descriptor and a non-data descriptor.

---

## Step 6 — `__new__` vs `__init__`

`__new__` creates; `__init__` initializes. The Singleton pattern.

→ [Topic](../domains/oop/new_vs_init.md)  
→ [Code Reading M4](../code_reading/medium.md)

**You're ready for Step 7 when:** you can implement a Singleton
using `__new__` and explain why `__init__` still gets called.

---

## Step 7 — MRO and `super()`

C3 linearization. Why cooperative inheritance requires `super()`.

→ [Topic](../domains/oop/mro.md)  
→ [Drill](../drills/oop_internals.py)  
→ [Code Reading M5](../code_reading/medium.md)

**You're ready for Step 8 when:** you can write out the MRO of a
diamond inheritance class by hand.

---

## Step 8 — Metaclasses

Classes that create classes. `type`, `__init_subclass__`, and
auto-registration.

→ [Topic](../domains/oop/metaclasses.md)  
→ [Code Reading H2](../code_reading/hard.md)  
→ [Code Reading H6](../code_reading/hard.md)

**You've completed this path when:** you can explain the difference
between `__init_subclass__` and a metaclass and when to use each.

---

## After this path

→ [Functional Python Path](functional_python_path.md)  
→ [Iteration Path](iteration_path.md)
