# Higher-Order Functions

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | High |
| Last Reviewed | Never |
| Next Review | TBD |

## 30-second explanation

A higher-order function either takes a function as an argument or
returns a function. `map`, `filter`, `sorted`, and `functools.reduce`
are classic examples. They enable composable, reusable logic without
boilerplate loops.

## Mental model

Higher-order functions operate on behavior, not just data. Instead of
writing `for x in items: process(x)`, you describe the operation —
`map(process, items)` — and let the runtime handle the loop.

```python
# Imperative
results = []
for x in range(10):
    if x % 2 == 0:
        results.append(x ** 2)

# Functional
results = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
```

Both produce the same result. The functional version composes two
operations; the imperative version mixes filtering and transformation.

## Why interviewers ask this

Tests whether you can think functionally. A candidate who knows
`map`/`filter`/`reduce` and can explain when to prefer list
comprehensions over them shows Python fluency and understanding of
the functional programming paradigm.

## Common traps

- `map` and `filter` return lazy iterators in Python 3. Wrap in
  `list()` to materialize them, otherwise you get a generator object.
- `reduce` is not a builtin in Python 3 — it moved to
  `functools.reduce`.
- `[f(x) for x in items]` is usually more readable than `map(f, items)`.
  Prefer `map` for simple function references like `map(str, items)`.
- `filter(None, items)` removes falsy values — a useful but
  non-obvious idiom.

## Code-reading example

```python
result = list(map(lambda x: x ** 2,
                  filter(lambda x: x % 2 == 0, range(10))))
print(result)
```

### Answer

```
[0, 4, 16, 36, 64]
```

### Explanation

`filter` keeps even numbers `[0, 2, 4, 6, 8]`, then `map` squares
each to `[0, 4, 16, 36, 64]`. Both return lazy iterators, so `list()`
is needed to materialize the result.

## Related topics

- Lambda functions
- functools
- Functions as objects
- Generator expressions
