# Walrus Operator (`:=`)

## Metadata

| Field | Value |
|---|---|
| Domain | Advanced Syntax |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | Medium |
| Last Reviewed | Never |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

The walrus operator `:=` assigns and returns a value in a single expression. Useful in `while` conditions and `if` checks where you want to both test and keep the result. Introduced in Python 3.8 (PEP 572).

---

## Mental model

`:=` is "assign and yield". `if x := f()` means "call `f()`, store the result in `x`, and evaluate the truthiness of that result" — all in one line.

---

## Why interviewers ask this

Tests knowledge of modern Python. Tricky because of scope: `:=` inside a comprehension leaks into the enclosing scope, while the comprehension loop variable does not.

---

## Common traps

- **Scope leakage from comprehensions:** `[y := f(x) for x in items]` — `y` is accessible after the comprehension; `x` is not.
- **`x` the loop variable does NOT leak** from comprehensions in Python 3 — only `:=` does.
- **Cannot use `:=` at the top level of an expression statement** alone — `(x := 5)` is valid; `x := 5` without parentheses is a `SyntaxError` in most contexts.

---

## Code-reading examples

```python
data = [1, -2, 3, -4, 5]
result = [y for x in data if (y := x * 2) > 0]
print(result)
print(y)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
[2, 6, 10]
10
```

**Why:** `:=` assigns `x * 2` to `y` and the `if` tests whether `y > 0`. Negative values (`-4`, `-8`) fail the filter. `y` leaks into the enclosing scope and holds the last assigned value: `5 * 2 = 10`.

---

## Coding drills

- Rewrite a `while True` / `break` loop as a `while val := next(...)` pattern
- Show scope leakage: access the walrus variable after a comprehension
- Show that the loop variable does NOT leak; compare with walrus

---

## Related topics

- [Comprehensions](comprehensions.md)
- [Generator expressions](generator_expressions.md)
- [LEGB scoping](../python_internals/scoping_legb.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
