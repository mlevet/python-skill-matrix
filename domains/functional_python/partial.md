# functools.partial

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | Medium |
| Last Reviewed | Never |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

`functools.partial(func, *args, **kwargs)` returns a new callable with some arguments pre-filled. Unlike a lambda closure, `partial` binds argument values eagerly — at the time of creation, not at call time.

---

## Mental model

`partial` is like placing an order with some details pre-filled. When you call the partial, it fills in the remaining details and calls the original function. No late binding — the pre-filled values are frozen at creation.

---

## Why interviewers ask this

`partial` is the canonical answer to "how do you avoid the late-binding trap?" and "how do you partially apply a function without a lambda?". It also appears in callback registration patterns.

---

## Common traps

- **`partial` vs lambda:** `lambda i=i: f(i)` and `partial(f, i)` both capture `i` eagerly, but `partial` is cleaner and preserves `__name__` and `__doc__` from the original.
- **Positional vs keyword:** positional args are prepended; you can also freeze keyword args.
- **Calling a partial with conflicting kwargs raises `TypeError`** — the pre-filled kwarg is already bound.

---

## Code-reading examples

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(4))
print(cube(3))
print(square.__name__)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
16
27
power
```

**Why:** `partial` binds `exp=2` and `exp=3` respectively. `__name__` is inherited from the wrapped function.

---

## Coding drills

- Fix a late-binding loop using `partial` instead of a default argument
- Create a `log_error` function from a generic `log(level, message)` using `partial`
- Demonstrate the difference in behavior between `partial` and a lambda when the source variable changes

---

## Related topics

- [functools](functools.md)
- [Late binding](late_binding.md)
- [Lambda functions](lambda_functions.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
