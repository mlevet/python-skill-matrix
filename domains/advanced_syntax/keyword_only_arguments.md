# Keyword-Only Arguments

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

Parameters after a bare `*` (or after `*args`) in a function signature are keyword-only — they must be passed by name, never by position. Used to enforce explicit, self-documenting call sites.

---

## Mental model

The bare `*` "absorbs" the positional argument slot without capturing anything, forcing everything after it to be named. `*args` does the same but also collects extra positional arguments.

---

## Why interviewers ask this

Tests whether you can read and write modern Python function signatures. Common in "what does this signature do?" or "why does this call fail?" questions. Also tests practical API design instincts.

---

## Common traps

- **Bare `*` vs `*args`:** bare `*` forces keyword-only without collecting args; `*args` collects any positional args AND forces keyword-only for what follows.
- **Keyword-only can still have defaults** — they become optional keyword arguments.
- **Keyword-only without default is required** — must be passed every call.

---

## Code-reading examples

```python
def create_user(name, *, admin=False, active=True):
    return {"name": name, "admin": admin, "active": active}

print(create_user("Alice"))
print(create_user("Bob", admin=True))
print(create_user("Charlie", True))
```

**Question:** What does this output/raise?

**Prediction:** write your answer before checking.

**Answer:**
```
{'name': 'Alice', 'admin': False, 'active': True}
{'name': 'Bob', 'admin': True, 'active': True}
TypeError: create_user() takes 1 positional argument but 2 were given
```

**Why:** `admin` and `active` are keyword-only (after `*`). Passing `True` positionally fails.

---

## Coding drills

- Rewrite `sorted(iterable, key, reverse)` to enforce `key` and `reverse` as keyword-only
- Write a function that accepts any number of positional args and two keyword-only flags
- Combine `/` and `*` in one signature and write 3 valid and 3 invalid calls

---

## Related topics

- [Positional-only arguments](positional_only_arguments.md)
- [Star unpacking](star_unpacking.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
