# functools.partial

---
**Path:** [Functional Python](../../roadmaps/functional_python_path.md) — Step 7 of 8  
**Prev:** [Decorators](decorators.md) · **Next:** [functools.lru_cache](lru_cache.md)  
**Code Reading:** [M2 — partial vs late binding](../../code_reading/medium.md)

---

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | Medium |
| Last Reviewed | Never |
| Next Review | TBD |

## 30-second explanation

`functools.partial(func, *args, **kwargs)` returns a new callable with
some arguments pre-filled. Unlike a lambda closure, `partial` binds
argument values eagerly — at creation time, not at call time. This
makes it the clean alternative to the late-binding fix with `i=i`.

## Mental model

`partial` is like placing an order with some details already filled in.
When you call the partial, it adds the remaining details and forwards
everything to the original function. The pre-filled values are frozen
at creation — no late binding.

```python
def multiply(x, y):
    return x * y

double = partial(multiply, 2)   # y still required
double(5)  # → 10
```

## Why interviewers ask this

`partial` is the canonical answer to "how do you partially apply a
function?" and "how do you avoid the late-binding trap without using
default arguments?" It also appears in callback registration and
`functools.reduce` patterns.

## Common traps

- `partial` vs `lambda i=i: f(i)`: both capture values eagerly, but
  `partial` is cleaner and inherits `__name__` and `__doc__` from the
  original function.
- Positional args passed to `partial` are prepended. You can also
  freeze keyword args: `partial(func, key=val)`.
- Calling a partial with a conflicting keyword argument raises
  `TypeError` — the pre-filled kwarg is already bound.

## Code-reading example

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

### Answer

```
16
27
power
```

### Explanation

`partial(power, exp=2)` freezes `exp=2`. Calling `square(4)` is
equivalent to `power(4, exp=2)`. `cube(3)` similarly calls
`power(3, exp=3)`. `__name__` is inherited from the original
`power` function — not renamed to `square`.

## Related topics

- functools
- Late binding
- Lambda functions
