# Properties

## Metadata

| Field | Value |
|---|---|
| Domain | OOP |
| Mastery | 0/10 |
| Freshness | Stale |
| Interview Frequency | Medium |
| Last Reviewed | Never |
| Next Review | TBD |
| Priority | TBD |

---

## 30-second explanation

`@property` turns a method into a read-only attribute. `@attr.setter` adds a setter. Together they let you add validation or computation behind what looks like a plain attribute access — without breaking the API.

---

## Mental model

`@property` is a built-in descriptor. It intercepts `obj.attr` and routes it through a function. From the caller's perspective it looks like a field; internally it can be computed or validated.

---

## Why interviewers ask this

Properties appear in "how would you add validation to this class?" questions. They also test understanding of descriptors, since `property` is a descriptor class itself.

---

## Common traps

- **`@property` alone is read-only** — assigning raises `AttributeError` without a `@setter`.
- **`@setter` name must match** — the setter decorator is `@<property_name>.setter`, not `@setter`.
- **Properties live on the class** — they're class-level descriptors, not instance attributes.
- **Can't use `self._x = x` in `__init__` if `_x` is behind a property** without a `_` prefix convention.

---

## Code-reading examples

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(0)
print(t.fahrenheit)
t.celsius = 100
print(t.fahrenheit)
```

**Question:** What does this output?

**Prediction:** write your answer before checking.

**Answer:**
```
32.0
212.0
```

**Why:** `fahrenheit` is a computed property. Updating `celsius` via the setter updates `_celsius`, which `fahrenheit` reads.

---

## Coding drills

- Add a `kelvin` property to `Temperature` that converts from Celsius
- Add validation to reject temperatures below absolute zero
- Attempt to set `t.fahrenheit = 100` and explain the error

---

## Related topics

- [Descriptors](descriptors.md)
- [Dunder methods](dunder_methods.md)

---

## My mistakes

---

## Review history

| Date | Result | Notes |
|---|---|---|
| TBD | TBD | TBD |
