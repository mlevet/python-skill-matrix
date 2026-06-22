# Pattern Matching (`match` / `case`)

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

`match`/`case` (Python 3.10+, PEP 634) is structural pattern matching. Unlike a `switch`, it matches against the *structure* of data — tuples, dicts, class instances — and can destructure and bind names in one step.

---

## Mental model

Pattern matching is like `isinstance` + `if`/`elif` + destructuring, all in one block. Each `case` pattern both checks the shape and unpacks matching parts into variables.

---

## Why interviewers ask this

Appears in "what does this do?" questions using newer syntax, or "how would you replace this if/elif chain?". Tests awareness of Python 3.10+ features and structural programming.

---

## Common traps

- **Bare names in patterns are capture variables, not comparisons** — `case x` captures any value into `x`. To match a constant, use a dotted name (`case Status.OK`) or a guard (`case x if x == 0`).
- **`case _` is the wildcard** — it matches anything and doesn't bind.
- **Patterns are checked top to bottom** — first match wins, like `if/elif`.

---

## Code-reading examples

```python
def classify(point):
    match point:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"x-axis at {x}"
        case (0, y):
            return f"y-axis at {y}"
        case (x, y):
            return f"point ({x}, {y})"

print(classify((0, 0)))
print(classify((3, 0)))
print(classify((0, 5)))
print(classify((2, 4)))
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
origin
x-axis at 3
y-axis at 5
point (2, 4)
```

**Why:** Each tuple is matched in order. `(x, 0)` captures `x` when the second element is `0`. `(x, y)` is the catch-all.

---

## Coding drills

- Write a `match` block to handle HTTP status codes (200, 404, 500, else)
- Use class patterns: `case Point(x=0, y=y)` to match dataclass fields
- Show the "bare name is a capture" trap: `STATUS = "ok"; case STATUS:` — does it match the constant?

---

## Related topics

- [Comprehensions](comprehensions.md)
- [Star unpacking](star_unpacking.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
