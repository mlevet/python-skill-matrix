---
topic: Lambdas
domain: functional_python
confidence: 0
last_reviewed: never
interview_freq: high
---

# Lambdas

## Summary

A lambda is an anonymous function defined as a single expression. It is syntactic sugar for a `def` — both create a function object. The main differences are: lambdas can only contain one expression (no statements), and their `__name__` is `"<lambda>"`.

---

## Key concepts

- Syntax: `lambda [args]: expression`
- Returns the result of the expression implicitly — no `return` keyword.
- Can take default arguments, `*args`, and `**kwargs`.
- Subject to the same late-binding closure rules as regular functions.
- `__name__` is `"<lambda>"` — use `@wraps` or named functions for better debugging.

---

## Code examples

### Basic forms

```python
square = lambda x: x ** 2
add = lambda x, y: x + y
constant = lambda: 42
with_default = lambda x, n=10: x + n

print(square(4))         # 16
print(add(3, 4))         # 7
print(with_default(5))   # 15
```

### As argument to higher-order functions

```python
nums = [3, -1, 4, -1, 5]

sorted(nums, key=lambda x: abs(x))        # sort by absolute value
list(filter(lambda x: x > 0, nums))       # [3, 4, 5]
list(map(lambda x: x ** 2, nums))         # [9, 1, 16, 1, 25]
```

### Conditional expression (not `if` statement)

```python
abs_val = lambda x: x if x >= 0 else -x
print(abs_val(-5))   # 5
```

### Lambdas in a dispatch table

```python
ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}
print(ops['*'](3, 4))   # 12
```

### Returning a lambda (currying-like pattern)

```python
make_adder = lambda n: lambda x: x + n
add5 = make_adder(5)
print(add5(10))   # 15
```

---

## Common traps

- **Late binding in loops:** `[lambda: i for i in range(5)]` creates 5 lambdas all returning 4. Fix: `lambda i=i: i`.
- **Statements are forbidden:** `lambda x: x = x + 1` is a `SyntaxError`. Use `def` if you need assignments, loops, or multiple statements.
- **`__name__` is `"<lambda>"`:** stack traces and debugging are harder. Prefer `def` for anything non-trivial.
- **Not `functools.partial`:** a lambda with a default arg captures eagerly; a raw closure does not.

---

## Interview angle

- "What does this output?" → lambda in a loop with the late-binding trap
- "What's the difference between `lambda` and `def`?" → syntactic only (one expression), `__name__`, can't contain statements
- "Why should you avoid lambdas in some cases?" → debugging (`__name__`), readability, no docstring

Key things to say:
- "Lambda is just anonymous `def`. They produce the same type of object."
- "Lambda forces a single expression — the moment you need a statement, use `def`."

---

## Linked drill

`drills/lambdas.py` — all exercises

---

## Linked code-reading puzzles

- `code_reading/easy.md` — implicit (E1 uses a lambda concept)
- `code_reading/medium.md` — Puzzle M1 (late binding)

---

## Review notes

