# Closures

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

A closure is a function that retains access to variables from its enclosing scope, even after that scope has finished executing. The variables are captured by reference — not by value. This distinction is the source of the late-binding trap.

---

## Mental model

Think of a closure as a function bundled with a backpack. The backpack contains cell objects — live references to variables from the outer scope. When the function runs, it reaches into the backpack to find the current value of those variables.

---

## Why interviewers ask this

Closures are a Python fundamental that most developers get partially wrong. Interviewers use them to test whether you understand reference semantics, `nonlocal`, and the late-binding trap. Getting both "what is a closure" and "what is the trap" right is the mark of fluency.

---

## Common traps

- **Capture by reference, not value:** the closure holds a live reference — if the variable changes after the closure is created, the closure sees the new value.
- **Late binding in loops:** all closures in a loop share the same variable (see [late_binding.md](late_binding.md)).
- **`nonlocal` required to write:** you can read an enclosing variable freely, but assigning to it requires `nonlocal` or Python treats it as a new local.
- **`UnboundLocalError`:** any assignment to a name inside a function makes it local for the entire function body — even lines before the assignment.

---

## Code-reading examples

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c1 = make_counter()
c2 = make_counter()
print(c1())
print(c1())
print(c2())
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
1
2
1
```

**Why:** `c1` and `c2` are separate closures over separate `count` variables — each call to `make_counter()` creates a new scope. `c1` has its own counter; `c2` starts fresh.

---

## Coding drills

- Implement `make_counter()` with `reset()` and `increment()` methods via closures
- Write the late-binding bug, then both fixes (default arg and factory function)
- Inspect `__closure__` and `__code__.co_freevars` on a closure you create

---

## Related topics

- [Late binding](late_binding.md)
- [Lambda functions](lambda_functions.md)
- [Decorators](decorators.md)
- [LEGB scoping](../python_internals/scoping_legb.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
