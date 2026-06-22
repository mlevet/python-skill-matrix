# functools.lru_cache

---
**Path:** [Functional Python](../../roadmaps/functional_python_path.md) — Step 8 of 8  
**Prev:** [functools.partial](partial.md)  
**Drill:** [drills/decorators.py](../../drills/decorators.py)

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

`@functools.lru_cache(maxsize=128)` memoizes a function — it caches
return values keyed by arguments. On a repeated call with the same
args, it returns the cached result without calling the function.
`maxsize=None` makes it an unbounded cache (`@cache` in Python 3.9+).

## Mental model

`lru_cache` wraps your function in a dictionary. The arguments are
the key; the return value is the value. "LRU" means when the cache
is full, the Least Recently Used entry is evicted first.

```python
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Without the cache, `fib(10)` makes exponentially many recursive calls.
With it, each unique argument is computed once and reused.

## Why interviewers ask this

Classic decorator question and optimization question combined. Appears
in "how would you optimize this recursive function?" contexts (Fibonacci,
DP problems). Tests knowledge of memoization, decorator mechanics, and
hashability constraints.

## Common traps

- Arguments must be hashable — lists and dicts as arguments raise
  `TypeError`. Pass tuples instead.
- The cache is per-function-object. Recreating the decorated function
  (e.g., in a loop) loses the cache.
- `maxsize=None` disables LRU eviction — useful but can consume
  unbounded memory for large argument spaces.
- The decorated function gains `cache_info()` and `cache_clear()`
  methods. `cache_info()` returns hits, misses, maxsize, currsize.

## Code-reading example

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

### Answer

```
55
CacheInfo(hits=8, misses=11, maxsize=None, currsize=11)
```

### Explanation

Without the cache, `fib(10)` would make 177 calls. With it, 11 unique
values are computed (misses=11) and 8 are served from cache
(hits=8). The current cache size is 11 entries.

## Related topics

- functools
- Decorators
