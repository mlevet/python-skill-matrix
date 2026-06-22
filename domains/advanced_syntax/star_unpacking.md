# Star Unpacking

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

`*` in assignment unpacks the "rest" of an iterable into a list. `**` unpacks dicts. In function calls, `*iterable` spreads positional args and `**dict` spreads keyword args. In function signatures, `*args` collects extra positionals and `**kwargs` collects extra keywords.

---

## Mental model

`*` means "collect the rest" or "spread these out", depending on context. In assignment: collect into a list. In a call: spread out of a container. In a signature: collect into a tuple/dict.

---

## Why interviewers ask this

Unpacking appears in sorting, merging dicts, variadic functions, and functional patterns. The common traps are: starred assignment always produces a `list`, and `**` merging has a specific precedence when keys clash.

---

## Common traps

- **Starred assignment always returns a `list`** — even when unpacking from a tuple.
- **`{**d1, **d2}` — right wins on key conflicts:** later dict's values overwrite earlier ones.
- **Can't use two starred expressions in one assignment** at the same level: `*a, *b = [1, 2, 3]` is a `SyntaxError`.
- **`*` in function call vs signature:** `f(*args)` spreads; `def f(*args)` collects.

---

## Code-reading examples

```python
a, *b, c = range(6)
print(a, b, c)
print(type(b))

d1 = {"x": 1, "y": 2}
d2 = {"y": 99, "z": 3}
merged = {**d1, **d2}
print(merged)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
0 [1, 2, 3, 4] 5
<class 'list'>
{'x': 1, 'y': 99, 'z': 3}
```

**Why:** `b` collects elements 1–4 as a `list`. In the merge, `d2["y"] = 99` overwrites `d1["y"] = 2` because `d2` comes later.

---

## Coding drills

- Swap two variables without a temp: `a, b = b, a`
- Unpack the first and last elements of a list, capturing the middle with `*`
- Merge three dicts where all have a common key — verify which value wins

---

## Related topics

- [Positional-only arguments](positional_only_arguments.md)
- [Keyword-only arguments](keyword_only_arguments.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
