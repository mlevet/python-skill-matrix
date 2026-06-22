# Closures

---
**Path:** [Functional Python](../../roadmaps/functional_python_path.md) — Step 4 of 8  
**Prev:** [Higher-Order Functions](higher_order_functions.md) · **Next:** [Late Binding](late_binding.md)  
**Drill:** [drills/closures.py](../../drills/closures.py)  
**Code Reading:** [M1 — Late binding](../../code_reading/medium.md) · [H7 — Compound trap](../../code_reading/hard.md)  
**Hall of Pain:** [Late binding surprise](../../hall_of_pain.md)

---

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 5/10 |
| Freshness | Stale |
| Interview Frequency | High |
| Last Reviewed | TBD |
| Next Review | TBD |

## 30-second explanation

A closure is a function that retains access to variables from its
enclosing scope, even after that scope has finished executing. The
captured variables are called free variables. They are stored as cell
objects inside `__closure__` and are accessed by reference, not by
value.

## Mental model

Think of a closure as a function bundled with a backpack. The backpack
holds live references — called cell objects — to variables in the outer
scope. When the function runs, it reaches into the backpack to read the
current value of each captured variable.

```python
def make_multiplier(n):
    def multiply(x):
        return x * n   # n lives in the backpack
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
```

`double.__closure__[0].cell_contents` is `2`. `triple`'s cell holds
`3`. The two closures are independent — each call to `make_multiplier`
creates a new scope and a new cell.

## Why interviewers ask this

Closures are where most intermediate Python developers have gaps. The
interviewer is testing whether you know the difference between capturing
a name and capturing a value, when `nonlocal` is required, and whether
two closures over the same variable share state. Getting this right
signals you understand how Python scoping actually works.

## Common traps

- Closures capture the variable, not the value. If the variable changes
  after the closure is created, the closure sees the new value.
- `nonlocal` is required to assign to an enclosing variable. Without
  it, Python creates a new local of the same name and raises
  `UnboundLocalError` when you try to read it before assignment.
- Two closures created inside the same scope can share state through a
  mutable variable. This is surprising when it happens by accident.
- Each call to the outer function creates a completely independent scope
  and a completely independent set of cell objects.
- `__closure__` is `None` for functions with no free variables.
  Inspecting it is a useful debugging technique.

## Code-reading example

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

### Answer

```
1
2
1
```

### Explanation

Each call to `make_counter()` creates a fresh scope with its own `count`
variable. `c1` and `c2` have independent cell objects — incrementing
`c1` has no effect on `c2`. Within `c1`, `nonlocal count` allows
`increment` to write back to the `count` in its enclosing scope.
Without `nonlocal`, the line `count += 1` would try to read `count`
as a local before assigning to it, raising `UnboundLocalError`.

## Related topics

- Late binding
- Lambda functions
- Decorators
- LEGB scoping
