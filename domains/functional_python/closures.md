---
topic: Closures & Late Binding
domain: functional_python
confidence: 0
last_reviewed: never
interview_freq: high
---

# Closures & Late Binding

## Summary

A closure is a function that remembers variables from its enclosing scope even after that scope has finished executing. The captured variables are references — not copies — which is the source of the late-binding trap.

---

## Key concepts

- A closure is created when a nested function refers to a variable from its enclosing scope.
- `__closure__` holds the cell objects; `cell.cell_contents` shows the captured value.
- `nonlocal` allows writing to the enclosing variable (not just reading).
- The captured variable is a live reference — changes to it are visible inside the closure.

---

## Code examples

### Basic closure

```python
def make_multiplier(n):
    def multiply(x):
        return x * n   # n is captured from make_multiplier's scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
```

### The late-binding trap

```python
# BROKEN: all lambdas share the same 'i' variable
funcs = [lambda: i for i in range(5)]
print([f() for f in funcs])   # [4, 4, 4, 4, 4]

# FIXED: capture value at definition time
funcs = [lambda i=i: i for i in range(5)]
print([f() for f in funcs])   # [0, 1, 2, 3, 4]
```

### `nonlocal` for mutation

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

### Inspecting closures

```python
def outer(x):
    def inner():
        return x
    return inner

f = outer(42)
print(f.__code__.co_freevars)    # ('x',)
print(f.__closure__[0].cell_contents)  # 42
```

---

## Common traps

- **Late binding:** closures over loop variables capture the variable, not its value. By the time the closure is called, the loop has ended and the variable holds its final value.
- **Read vs write:** you can read an enclosing variable without `nonlocal`. The moment you assign to it (including `+=`), Python treats it as a local, causing `UnboundLocalError` unless `nonlocal` is declared.
- **Shared state between calls:** closures share the same cell object — multiple closures over the same variable see the same state.

---

## Interview angle

- "What does this code output?" → classic late-binding loop with lambdas
- "What is a closure?" → function + captured environment (cell references)
- "How do you fix the late-binding trap?" → default argument, `functools.partial`, or factory function
- "What does `nonlocal` do?" → enables assignment to an enclosing (non-global) variable

Key things to say:
- "Closures capture the *variable*, not the *value* at creation time."
- "The fix is to force eager evaluation via a default argument (`lambda i=i: i`)."

---

## Linked drill

`drills/closures.py` — all exercises

---

## Linked code-reading puzzles

- `code_reading/medium.md` — Puzzle M1 (classic late binding)
- `code_reading/hard.md` — Puzzle H7 (compound trap)

---

## Review notes

<!-- Things you got wrong, tricky edge cases to remember -->
