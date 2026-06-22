# MRO — Method Resolution Order

## Metadata

| Field | Value |
|---|---|
| Domain | OOP |
| Mastery | 4/10 |
| Freshness | Stale |
| Interview Frequency | Medium |
| Last Reviewed | TBD |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

MRO is the order Python searches classes when resolving a method or attribute. Python uses the C3 linearization algorithm, which ensures each class appears after all its parents and respects the order of base class declarations. `super()` follows MRO — it calls the next class in the chain, not necessarily the direct parent.

---

## Mental model

Flatten the class hierarchy into a single ordered list where: (1) a class always comes before its parents, (2) parents appear in left-to-right declaration order. `super()` always calls the next item in this list for the current runtime instance's type.

---

## Why interviewers ask this

Diamond inheritance is a classic OOP trap. Interviewers use it to test whether you can trace MRO manually and whether you understand cooperative multiple inheritance. A good answer includes reading `__mro__` and tracing `super()` calls through the chain.

---

## Common traps

- **`super()` is not "call my parent"** — it calls the next class in MRO for the *runtime instance's type*, which can be a sibling class.
- **Non-cooperative hierarchies break:** if `B` doesn't call `super()`, then in `D(B, C)`, `C` is skipped.
- **Inconsistent MRO raises `TypeError`** — e.g. `class X(A, B)` where `B` inherits from `A` violates C3.

---

## Code-reading examples

```python
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        super().hello()
        print("B")

class C(A):
    def hello(self):
        super().hello()
        print("C")

class D(B, C):
    def hello(self):
        super().hello()
        print("D")

D().hello()
print([c.__name__ for c in D.__mro__])
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
A
C
B
D
['D', 'B', 'C', 'A', 'object']
```

**Why:** MRO is `D → B → C → A → object`. Each `super().hello()` goes to the next in that list. Execution unwinds in call order: A prints first, then C, B, D as each returns.

---

## Coding drills

- Read `D.__mro__` for a diamond hierarchy and draw the resolution order
- Trace what prints when `super()` is called in each class
- Break cooperative inheritance by removing one `super()` call and observe what is skipped

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
