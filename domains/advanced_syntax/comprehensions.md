# Comprehensions

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

Comprehensions are concise one-liner constructs for building lists, dicts, sets, or generators: `[expr for x in iterable if condition]`. In Python 3, all comprehension types (list, dict, set) have their own scope — loop variables do not leak.

---

## Mental model

A comprehension is a `for` loop turned inside out. The expression comes first, the loop follows, the filter is optional. Each type uses different brackets: `[]` list, `{}` set or dict, `()` generator.

---

## Why interviewers ask this

Comprehensions are ubiquitous in Python code. Interviewers test: scope (does the variable leak?), nesting (how do you flatten?), and performance (list vs generator expression). The walrus operator leak is a frequent trick question.

---

## Common traps

- **Loop variable scope:** in Python 3, loop variables in list/dict/set comprehensions do NOT leak into the enclosing scope. Generator expressions never did.
- **Walrus operator leaks:** `[y := f(x) for x in items]` — `y` is visible after the comprehension.
- **Nested comprehensions:** `[[j for j in row] for row in matrix]` — outer loop is last in the expression, which reads left-to-right differently from a nested `for`.
- **Dict comprehension vs set:** `{k: v for ...}` is a dict; `{x for ...}` is a set; `{}` alone is an empty dict.

---

## Code-reading examples

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

**Why:** The nested comprehension reads as "for each row, for each x in row" — equivalent to two nested `for` loops. The dict comprehension maps even numbers to their squares.

---

## Coding drills

- Flatten a 2D list using a comprehension
- Create a dict that inverts a given dict (values become keys)
- Show that `{x for x in range(3)}` is a set, not a dict

---

## Related topics

- [Generator expressions](generator_expressions.md)
- [Walrus operator](walrus_operator.md)
- [LEGB scoping](../python_internals/scoping_legb.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
