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

## 30-second explanation

`functools` is the standard library module for higher-order function
utilities. The most interview-relevant tools are `partial` (pre-fill
arguments), `lru_cache` (memoization), `wraps` (preserve decorator
metadata), and `reduce` (fold a sequence into a single value).

## Mental model

`functools` is the toolbox for working with functions as objects. If
you want to transform, combine, cache, or memoize functions, `functools`
probably has what you need.

## Why interviewers ask this

`functools.partial` and `lru_cache` appear frequently in both practical
code and interview questions. `wraps` is expected in any decorator
implementation. Knowing `reduce` vs comprehensions signals functional
programming experience.

## Common traps

- `partial` binds values eagerly — no late-binding trap. This is the
  key difference from a closure over a loop variable.
- `lru_cache` caches by argument hash — mutable arguments (lists,
  dicts) raise `TypeError`. Use tuples instead.
- `@wraps(func)` goes on the wrapper inside the decorator body, not
  on the outer decorator function itself.
- `reduce` reduces left to right: `reduce(f, [a, b, c])` is
  `f(f(a, b), c)`.

## Code-reading example

```python
from functools import reduce

result = reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 0)
print(result)
```

### Answer

```
10
```

### Explanation

Starts with accumulator `0`. Each step: `0+1=1`, `1+2=3`, `3+3=6`,
`6+4=10`.

## Related topics

- functools.partial
- functools.lru_cache
- Decorators
- Higher-order functions
