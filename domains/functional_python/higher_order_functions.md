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
| Priority | TBD |

---

## 30-second explanation

A higher-order function either takes a function as an argument or returns a function. `map`, `filter`, `sorted`, and `functools.reduce` are classic examples. They enable composable, reusable logic without boilerplate loops.

---

## Mental model

Higher-order functions are function factories or function processors. They operate on behavior, not just data. Instead of writing `for x in items: process(x)`, you describe the operation — `map(process, items)` — and let the runtime handle the loop.

---

## Why interviewers ask this

Tests whether you can think functionally. A candidate who knows `map`/`filter`/`reduce` and can explain when to prefer list comprehensions over them shows Python fluency and understanding of the functional programming paradigm.

---

## Common traps

- **`map` and `filter` return lazy iterators in Python 3** — wrap in `list()` to materialize.
- **`reduce` is not a builtin** — it moved to `functools.reduce` in Python 3.
- **`map` vs list comprehension:** `[f(x) for x in items]` is usually more readable; prefer `map` for simple function references (`map(str, items)`).
- **`filter(None, items)`** removes falsy values — a useful but non-obvious idiom.

---

## Code-reading examples

```python
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
print(result)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
[0, 4, 16, 36, 64]
```

**Why:** `filter` keeps even numbers `[0, 2, 4, 6, 8]`, then `map` squares each to `[0, 4, 16, 36, 64]`.

---

## Coding drills

- Rewrite the example above as a list comprehension
- Use `sorted()` with a `key=` function to sort a list of tuples by second element
- Implement your own `my_map(func, iterable)` as a generator function

---

## Related topics

- [Lambda functions](lambda_functions.md)
- [functools](functools.md)
- [Functions as objects](functions_as_objects.md)
- [Generator expressions](../advanced_syntax/generator_expressions.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
