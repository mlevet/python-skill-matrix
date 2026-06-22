# Generator Expressions

## Metadata

| Field | Value |
|---|---|
| Domain | Advanced Syntax |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | High |
| Last Reviewed | Never |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

A generator expression `(expr for x in iterable if cond)` creates a lazy iterator — it computes values one at a time on demand, without building a list in memory. It's a generator written as a one-liner. Ideal for large sequences or pipelines.

---

## Mental model

A generator expression is to a list comprehension what a stream is to a buffer. List comprehension fills a bucket; generator expression turns on a tap. You drink one cup at a time.

---

## Why interviewers ask this

Memory efficiency is a common interview theme. "How would you process a 10 GB file without loading it?" → generator pipeline. Also tests whether you know the exhaustibility trap.

---

## Common traps

- **Generators are exhaustible** — iterate once and they're empty. `list(g)` twice gives `[]` the second time.
- **Tiny in memory** — `sys.getsizeof((x for x in range(10**9)))` is ~200 bytes regardless of range.
- **`sum(x**2 for x in range(n))`** — the parentheses inside a function call can be omitted for a single generator arg.
- **Not subscriptable** — `gen[0]` raises `TypeError`; you can't index a generator.

---

## Code-reading examples

```python
gen = (x * 2 for x in range(5) if x % 2 == 0)

print(next(gen))
print(next(gen))
print(list(gen))
print(list(gen))
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
0
4
[8]
[]
```

**Why:** Even numbers in `range(5)` are `0, 2, 4`. Generator yields `0, 4, 8`. Two `next()` calls consume `0` and `4`. `list(gen)` drains the remainder (`[8]`). Second `list(gen)` gets nothing — generator is exhausted.

---

## Coding drills

- Write a generator expression that yields the first 10 squares of odd numbers
- Show memory difference between `[x**2 for x in range(10**6)]` and `(x**2 for x in range(10**6))`
- Chain two generator expressions as a pipeline without materializing intermediate lists

---

## Related topics

- [Comprehensions](comprehensions.md)
- [Generators & yield](generators.md)
- [Higher-order functions](../functional_python/higher_order_functions.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
