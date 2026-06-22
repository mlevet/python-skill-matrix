# Late Binding

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 5/10 |
| Freshness | Stale |
| Interview Frequency | High |
| Last Reviewed | TBD |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

Late binding means closures look up variables at call time, not at definition time. When a lambda or inner function closes over a loop variable, all copies share the same variable — and they all see its final value when called.

---

## Mental model

The closure holds a reference to the variable, like a pointer. It doesn't copy the value. When you call the function, it follows the pointer to find the current value — which may have changed since the function was created.

---

## Why interviewers ask this

This is one of the most common Python "what does this print?" traps. It tests whether you understand the difference between closing over a name vs capturing a value, and whether you know the two standard fixes.

---

## Common traps

- **The trap:** `[lambda: i for i in range(5)]` — all five lambdas return `4` because `i` is the same variable and holds `4` after the loop.
- **Fix 1 — default argument:** `lambda i=i: i` evaluates `i` at definition time and stores it as a default.
- **Fix 2 — factory function:** wrapping in `def make(i): return lambda: i` creates a new scope per iteration.
- **`functools.partial` avoids it:** `partial(f, i)` binds the value eagerly, not the variable.

---

## Code-reading examples

```python
functions = []
for i in range(3):
    functions.append(lambda: i * 2)

print([f() for f in functions])
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
[4, 4, 4]
```

**Why:** All three lambdas close over the same `i`. After the loop, `i == 2`. Each lambda returns `2 * 2 == 4`.

---

## Coding drills

- Write the broken version and the two fixed versions of a late-binding loop
- Predict the output: `fs = [lambda x, i=i: x + i for i in range(3)]` — then call `fs[0](10)`, `fs[1](10)`, `fs[2](10)`
- Demonstrate that `functools.partial` does not have the late-binding problem

---

## Related topics

- [Closures](closures.md)
- [Lambda functions](lambda_functions.md)
- [functools.partial](partial.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
