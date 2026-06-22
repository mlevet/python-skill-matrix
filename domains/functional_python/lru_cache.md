# functools.lru_cache

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

`@functools.lru_cache(maxsize=128)` memoizes a function — it caches return values keyed by arguments. On a repeated call with the same args, it returns the cached result instead of calling the function. `maxsize=None` makes it an unbounded cache (`@cache` in Python 3.9+).

---

## Mental model

`lru_cache` wraps your function in a dictionary. The arguments are the key; the return value is the value. "LRU" means when the cache is full, the Least Recently Used entry is evicted.

---

## Why interviewers ask this

Classic decorator question and optimization question combined. Appears in "how would you optimize this recursive function?" contexts (Fibonacci, DP problems). Tests knowledge of memoization, decorator mechanics, and hashability constraints.

---

## Common traps

- **Arguments must be hashable** — lists and dicts as arguments raise `TypeError`. Use tuples instead.
- **The cache is per-function-object** — if you recreate the decorated function, you lose the cache.
- **`maxsize=None` disables LRU eviction** — useful but can consume unbounded memory.
- **`cache_info()` and `cache_clear()`** — the decorated function gains these methods.

---

## Code-reading examples

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))
print(fib.cache_info())
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
55
CacheInfo(hits=8, misses=11, maxsize=None, currsize=11)
```

**Why:** Without the cache, `fib(10)` would make 177 calls. With it: 11 unique values computed, 8 cache hits.

---

## Coding drills

- Add `lru_cache` to a naive recursive Fibonacci and measure the speedup
- Try passing a list as an argument — observe the `TypeError`
- Clear the cache mid-run with `cache_clear()` and observe the re-computation

---

## Related topics

- [functools](functools.md)
- [Decorators](decorators.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
