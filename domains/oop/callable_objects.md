# Callable Objects

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

Any object that defines `__call__` can be called like a function using `()`. `callable(obj)` returns `True` for functions, lambdas, classes, and any instance with `__call__`. This enables stateful callables — objects that behave like functions but carry state between calls.

---

## Mental model

`obj(args)` is syntactic sugar for `type(obj).__call__(obj, args)`. For regular functions, `function.__call__` is handled by the runtime. For instances, Python looks for `__call__` on the class.

---

## Why interviewers ask this

`__call__` is the bridge between OOP and functional programming. It appears in class-based decorators, factory patterns, and stateful callbacks. Knowing `callable()` and `__call__` together shows depth.

---

## Common traps

- **`callable()` checks the class, not the instance:** `callable(obj)` is `True` if `type(obj)` defines `__call__`, even if `obj.__call__` would fail.
- **Classes are callable** — `MyClass()` calls `type.__call__` → `MyClass.__new__` + `MyClass.__init__`.
- **Class-based decorators must implement `__call__`** to make the decorated function callable.

---

## Code-reading examples

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))
print(triple(5))
print(callable(double))
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
10
15
True
```

**Why:** `double(5)` calls `Multiplier.__call__(double, 5)`. `callable(double)` is `True` because `Multiplier` defines `__call__`.

---

## Coding drills

- Implement a class-based decorator using `__call__`
- Write a `CallCounter` that wraps any callable and tracks how many times it's been called
- Show that a class is callable: `MyClass()` creates an instance via `type.__call__`

---

## Related topics

- [Dunder methods](dunder_methods.md)
- [Decorators](../functional_python/decorators.md)
- [Classes are objects](classes_are_objects.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
