# Lambda Functions

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

A lambda is an anonymous function expression. It creates a function object without using `def`. Lambdas are limited to a single expression and are often used for short callbacks, sorting keys, or functional-style operations.

## Mental model

A lambda is still a function object.

```python
square = lambda x: x * x
```

is similar to:

```python
def square(x):
    return x * x
```

The only real differences: no name, no statements, `__name__` is `"<lambda>"`.

## Why interviewers ask this

They are often testing whether I understand that functions are first-class objects and whether I understand closures, late binding, and variable capture.

## Common traps

- Lambdas are not magic; they are function objects.
- Lambdas capture variables by name, not by value.
- Lambdas in loops often produce late-binding surprises.
- Lambdas can only contain expressions, not statements.

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

The lambda captures the name `i`, not its value at each iteration. After the loop ends, `i` is `2`, so every lambda reads the same final value.

### Fix

```python
funcs = []

for i in range(3):
    funcs.append(lambda i=i: i)
```

Using a default argument forces the value of `i` to be captured at the time the lambda is created.

## Related topics

- Closures
- Late binding
- Functions as objects
- Decorators
