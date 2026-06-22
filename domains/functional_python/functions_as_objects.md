# Functions as Objects

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 7/10 |
| Freshness | Medium |
| Interview Frequency | High |
| Last Reviewed | TBD |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

In Python, functions are first-class objects. They can be assigned to variables, stored in data structures, passed as arguments, and returned from other functions. `type(f)` returns `<class 'function'>`. This is the foundation of decorators, callbacks, and functional programming patterns.

---

## Mental model

A function is just an object that happens to be callable. The `def` statement creates a function object and binds it to a name — exactly like `x = 42` creates an int object. After that, the name is just a reference.

---

## Why interviewers ask this

Tests whether you understand that Python functions are not special syntax magic — they're objects with attributes. A good answer demonstrates understanding of `__name__`, `__doc__`, callable dispatch, and the difference between a function and the name that points to it.

---

## Common traps

- **Name vs object:** `f = print; del print` — `f` still works because it holds a reference to the object, not the name.
- **`__name__` doesn't change:** if you assign a function to another variable, `__name__` still reflects the original definition name.
- **`callable()` vs type check:** classes and instances with `__call__` are callable — never check `type(x) is function`.

---

## Code-reading examples

```python
def greet(name):
    return f"hello {name}"

say = greet
print(say is greet)
print(say.__name__)
greet = None
print(say("Alice"))
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
True
greet
hello Alice
```

**Why:** `say` and `greet` point to the same function object. Setting `greet = None` only rebinds the name — `say` still holds the original reference. `__name__` is an attribute of the object, not the variable name.

---

## Coding drills

- Build a dispatch table: dict mapping strings to functions, call by key
- Write `apply(func, value)` that calls any single-argument function
- Sort a list of dicts by a key using a lambda as the `key=` argument

---

## Related topics

- [Lambda functions](lambda_functions.md)
- [Closures](closures.md)
- [Higher-order functions](higher_order_functions.md)
- [Decorators](decorators.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
