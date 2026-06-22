# Decorators

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 6/10 |
| Freshness | Medium |
| Interview Frequency | High |
| Last Reviewed | TBD |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

A decorator is a callable that takes a function and returns a replacement. `@deco` above a `def` is syntactic sugar for `func = deco(func)`. Decorators are built on closures and first-class functions — understanding both is required to truly understand decorators.

---

## Mental model

`@deco` is just assignment. When Python sees `@deco` above `def f`, it runs `f = deco(f)` immediately after defining `f`. The decorator replaces the function with its return value — usually a wrapper that calls the original.

---

## Why interviewers ask this

Decorators are among the most common advanced Python interview topics. They test closures, first-class functions, `*args/**kwargs`, and `functools.wraps` in one question. "Implement a timer decorator" is a standard coding task.

---

## Common traps

- **`@wraps(func)` is mandatory** — without it, `__name__` and `__doc__` are replaced by the wrapper's, breaking introspection and logging.
- **Application order is bottom-up:** `@A @B def f` → `f = A(B(f))`. The bottom decorator runs first.
- **Execution order is outside-in:** when calling, A's wrapper executes before B's.
- **Decorator with arguments needs three layers:** `@repeat(3)` → `repeat(3)` returns a decorator, which wraps `f`.
- **Decoration happens at import time:** side effects in the decorator body run when the module loads.

---

## Code-reading examples

```python
from functools import wraps

def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

print(greet("world"))
print(greet.__name__)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
HELLO WORLD
greet
```

**Why:** `greet` is replaced by `wrapper`, which calls the original and uppercases the result. `@wraps(func)` preserves `__name__` as `"greet"`.

---

## Coding drills

- Implement a `@timer` decorator that prints elapsed time
- Implement `@repeat(n)` — a decorator that calls the function `n` times
- Stack `@shout` and `@timer` — predict and verify the output order

---

## Related topics

- [Closures](closures.md)
- [Functions as objects](functions_as_objects.md)
- [functools](functools.md)
- [Callable objects](../oop/callable_objects.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
