# Positional-Only Arguments

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

Parameters before `/` in a function signature are positional-only — they cannot be passed as keyword arguments. Introduced in Python 3.8 (PEP 570). Used extensively in built-in functions and C extensions.

---

## Mental model

The `/` marker draws a line: everything to the left is positional-only, everything to the right is normal. Add `*` for keyword-only on the right side.

```
def f(pos_only, /, normal, *, kw_only):
```

---

## Why interviewers ask this

Tests knowledge of modern Python syntax. Appears in "what does this signature mean?" or "why does `range(stop=10)` raise a TypeError?" questions. Also tests reading stdlib signatures like `pow(x, y, z=None, /)`.

---

## Common traps

- **Built-ins use `/` silently:** `len(obj=x)` raises `TypeError: len() takes no keyword arguments`.
- **Can't be passed by name:** `f(pos=1)` fails if `pos` is before `/`.
- **Allows reusing parameter names** in `**kwargs` without conflict — a use case for library authors.

---

## Code-reading examples

```python
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Alice"))
print(greet("Bob", greeting="Hi"))
print(greet(name="Charlie"))
```

**Question:** What does this output/raise?

**Prediction:** write your answer before checking.

**Answer:**
```
Hello, Alice
Hi, Bob
TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'
```

**Why:** `name` is before `/`, so it must be passed positionally. `greeting` is after `/` and can be passed either way.

---

## Coding drills

- Write a function with positional-only, normal, and keyword-only parameters
- Try calling `len(obj=[1,2,3])` and explain the error
- Check the signature of `pow` and explain why `pow(base=2, exp=3)` fails

---

## Related topics

- [Keyword-only arguments](keyword_only_arguments.md)
- [Star unpacking](star_unpacking.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
