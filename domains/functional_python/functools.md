# functools

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

`functools` is the standard library module for higher-order function utilities. The most interview-relevant tools are `partial` (pre-fill arguments), `lru_cache` (memoization), `wraps` (preserve decorator metadata), and `reduce` (fold a sequence into a single value).

---

## Mental model

`functools` is the toolbox for working with functions as objects. If you want to transform, combine, or memoize functions, `functools` probably has what you need.

---

## Why interviewers ask this

`functools.partial` and `lru_cache` appear frequently in both practical code and interview questions. `wraps` is expected in any decorator implementation. Knowing `reduce` vs comprehensions signals functional programming experience.

---

## Common traps

- **`partial` binds values eagerly** — no late-binding trap.
- **`lru_cache` caches by argument hash** — mutable arguments (lists, dicts) raise `TypeError`.
- **`wraps` goes on the wrapper, not the decorator** — `@wraps(func)` inside the decorator body, not outside.
- **`reduce` reduces left to right** — `reduce(f, [a, b, c])` = `f(f(a, b), c)`.

---

## Code-reading examples

```python
from functools import reduce

result = reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 0)
print(result)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
10
```

**Why:** Starts with accumulator `0`. Each step: `0+1=1`, `1+2=3`, `3+3=6`, `6+4=10`.

---

## Coding drills

- Use `partial` to create `double` and `triple` from a `multiply(x, y)` function
- Cache a Fibonacci function with `lru_cache` and compare performance with/without
- Use `reduce` to compute the product of a list

---

## Related topics

- [partial](partial.md)
- [lru_cache](lru_cache.md)
- [Decorators](decorators.md)
- [Higher-order functions](higher_order_functions.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
