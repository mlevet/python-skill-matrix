# Class Variables vs Instance Variables

## Metadata

| Field | Value |
|---|---|
| Domain | OOP |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | High |
| Last Reviewed | Never |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

Class variables are shared across all instances and live in `MyClass.__dict__`. Instance variables are per-instance and live in `instance.__dict__`. Reading `self.x` checks `instance.__dict__` first, then `MyClass.__dict__`. Writing `self.x = value` always writes to the instance — it never modifies the class variable, it shadows it.

---

## Mental model

Think of the class as a shared whiteboard and each instance as a personal notebook. Reading looks in your notebook first; if not found, checks the whiteboard. Writing always goes into your notebook — never onto the whiteboard (unless you write to `MyClass.x` explicitly).

---

## Why interviewers ask this

This is one of the most common Python "what does this print?" traps. `self.x += 1` silently shadows the class variable rather than incrementing it. Every Python developer has been burned by this.

---

## Common traps

- **`self.count += 1` creates an instance variable:** `self.count = self.count + 1` reads the class variable (right side), then writes an instance variable (left side) — the class variable is unchanged.
- **Mutable class variables are shared:** `class Foo: items = []` — all instances share the same list. Appending via one instance mutates it for all.
- **Deletion reveals class variable:** `del instance.x` removes the shadowing instance variable, making the class variable visible again via `instance.x`.

---

## Code-reading examples

```python
class Counter:
    count = 0

    def increment(self):
        self.count += 1

a = Counter()
b = Counter()
a.increment()
a.increment()
b.increment()

print(Counter.count)
print(a.count)
print(b.count)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
0
2
1
```

**Why:** `self.count += 1` is `self.count = self.count + 1`. The right side reads `Counter.count` (0), the left side creates an instance variable `self.count = 1`. The class variable stays at 0.

---

## Coding drills

- Write a class where `count` actually counts all instances using a class variable correctly
- Show the mutable class variable trap with a shared list
- Use `del instance.x` and observe the class variable reappear

---

## Related topics

- [Dunder methods](dunder_methods.md)
- [Descriptors](descriptors.md)
- [Classes are objects](classes_are_objects.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
