# Lambda Functions

---
**Path:** [Functional Python](../../roadmaps/functional_python_path.md) — Step 2 of 8  
**Prev:** [Functions as Objects](functions_as_objects.md) · **Next:** [Closures](closures.md)  
**Drill:** [drills/lambdas.py](../../drills/lambdas.py)  
**Code Reading:** [M1 — Late binding closure](../../code_reading/medium.md)  
**Hall of Pain:** [Late binding in loops](../../hall_of_pain.md)

---

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 6/10 |
| Freshness | Medium |
| Interview Frequency | High |
| Last Reviewed | TBD |
| Next Review | TBD |

## 30-second explanation

A lambda is an anonymous function expression. It creates a function
object without `def`. Lambdas are limited to a single expression and
are often used as sort keys, callbacks, or arguments to `map`/`filter`.
They are not special — they are function objects like any other.

## Mental model

A lambda is syntactic sugar for a single-expression `def`.

```python
square = lambda x: x * x
```

is equivalent to:

```python
def square(x):
    return x * x
```

The only differences: no name is given at definition time (`__name__`
is `"<lambda>"`), and only a single expression is allowed — no
statements, no assignments, no `return` keyword.

## Why interviewers ask this

Interviewers use lambdas to probe closures, late binding, and first-
class functions all at once. "What does this loop produce?" with a
lambda is one of the most common code-reading traps in Python interviews.
A strong answer explains that lambdas are not magic — just function
objects subject to the same scoping rules as `def`.

## Common traps

- Lambdas capture variables by name, not by value. A lambda in a loop
  closes over the loop variable, not its current value.
- Lambdas cannot contain statements. `lambda x: x = 1` is a syntax
  error. Use `def` when you need assignments, `if` statements, or
  multiple expressions.
- `__name__` is `"<lambda>"`, which breaks logging and stack traces.
  Prefer `def` for anything that will appear in error messages.
- A lambda used as a sort key captures the variable it references at
  call time. `sorted(items, key=lambda x: x.attr)` is fine, but
  beware of capturing a loop variable as the key.
- Immediately-invoked lambdas are valid Python but a code smell:
  `(lambda x: x * 2)(5)` works but is harder to read than a `def`.

## Code-reading example

```python
funcs = []

for i in range(3):
    funcs.append(lambda: i)

print(funcs[0]())
print(funcs[1]())
print(funcs[2]())
```

### Answer

```
2
2
2
```

### Explanation

The lambda captures the name `i`, not its value at each iteration.
After the loop ends, `i` is `2`, so every lambda reads the same final
value when called.

### Fix

```python
funcs = []

for i in range(3):
    funcs.append(lambda i=i: i)
```

Using `i=i` as a default argument forces the current value of `i` to
be captured at creation time. The default argument is evaluated
immediately — it is not a closure over the name.

## Related topics

- Closures
- Late binding
- Functions as objects
- Decorators
