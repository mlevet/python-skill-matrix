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

## 30-second explanation

A closure is a function that retains access to variables from its enclosing scope, even after that scope has finished executing. The variables are captured by reference — not by value. This distinction is the source of the late-binding trap.

## Mental model

A closure is a function bundled with a backpack. The backpack holds live references — called cell objects — to variables from the outer scope. When the function runs, it reaches into the backpack to find the current value of each variable.

```python
def make_multiplier(n):
    def multiply(x):
        return x * n   # n is in the backpack
    return multiply

double = make_multiplier(2)
```

`double.__closure__[0].cell_contents` is `2` — the captured value of `n`.

## Why interviewers ask this

Closures are a core Python concept that most developers understand incompletely. Interviewers use them to test whether you know the difference between capturing a name and capturing a value, how `nonlocal` works, and how to diagnose and fix the late-binding trap.

## Common traps

- Closures capture the variable, not the value. If the variable changes later, the closure sees the new value.
- `nonlocal` is required to assign to an enclosing variable. Without it, Python treats the name as a new local, causing `UnboundLocalError`.
- Two closures over the same variable share state — incrementing through one affects what the other sees.
- Each call to the outer function creates a new, independent scope and a new closure.

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

Each call to `make_counter()` creates a fresh scope with its own `count` variable. `c1` and `c2` are independent closures — incrementing `c1` does not affect `c2`. Within `c1`, `nonlocal count` lets `increment` assign back to the `count` in its enclosing scope.

## Related topics

- Late binding
- Lambda functions
- Decorators
- LEGB scoping
