# Lambda Functions

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

A lambda is an anonymous function defined as a single expression: `lambda args: expression`. It is syntactic sugar for `def` — both produce a function object. Key limitations: one expression only, no statements, `__name__` is `"<lambda>"`. Subject to the same late-binding closure rules as regular functions.

---

## Mental model

Think of `lambda x: x * 2` as a one-liner `def` with the return implicit. The only real differences are: no name, no statements, and it fits inline as an argument.

---

## Why interviewers ask this

Lambdas appear in almost every "what does this print?" Python question involving `sorted`, `map`, `filter`, or a loop. Interviewers use them to probe for the late-binding trap, understanding of first-class functions, and whether you know when NOT to use a lambda (when `def` is clearer).

---

## Common traps

- **Late binding in loops:** `[lambda: i for i in range(5)]` — all return `4`. The lambda captures the variable `i`, not its value.
- **Default argument fix:** `lambda i=i: i` forces eager capture at definition time.
- **No statements:** `lambda x: x = x + 1` is a `SyntaxError`. You cannot assign inside a lambda.
- **`__name__` is `"<lambda>"`:** stack traces become unreadable for complex lambdas — use `def` instead.

---

## Code-reading examples

```python
funcs = [lambda: i for i in range(4)]
print([f() for f in funcs])

funcs2 = [lambda i=i: i for i in range(4)]
print([f() for f in funcs2])
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
[3, 3, 3, 3]
[0, 1, 2, 3]
```

**Why:** The first list captures the variable `i` (late binding) — all lambdas see `i == 3` after the loop. The second uses a default argument to capture the value at creation time.

---

## Coding drills

- Write a lambda that returns `True` if a number is even
- Use `sorted()` with a lambda to sort strings by their last character
- Rewrite `lambda x: x if x > 0 else -x` as a named `def` — when is each appropriate?

---

## Related topics

- [Closures](closures.md)
- [Late binding](late_binding.md)
- [Higher-order functions](higher_order_functions.md)
- [Functions as objects](functions_as_objects.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
