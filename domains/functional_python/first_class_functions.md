---
topic: Functions as First-Class Objects
domain: functional_python
confidence: 0
last_reviewed: never
interview_freq: high
---

# Functions as First-Class Objects

## Summary

In Python, functions are objects of type `function`. They can be assigned to variables, stored in data structures, passed as arguments, and returned from other functions. This is the foundation of closures, decorators, and functional programming patterns.

---

## Key concepts

- `type(f)` → `<class 'function'>` for any function `f`.
- Functions have attributes: `__name__`, `__doc__`, `__annotations__`, `__defaults__`, `__code__`, `__closure__`.
- A function assigned to another variable: both names point to the same object.
- `callable(x)` returns `True` for functions, methods, lambdas, and objects with `__call__`.

---

## Code examples

### Functions are objects

```python
def greet(name):
    return f"Hello, {name}"

say_hello = greet          # same object, different name
print(say_hello is greet)  # True
print(greet.__name__)      # greet
print(say_hello.__name__)  # greet  ← __name__ doesn't change
```

### Functions in data structures

```python
ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}
result = ops['+'](3, 4)   # 7

pipeline = [str.strip, str.lower, str.title]
text = "  hello world  "
for fn in pipeline:
    text = fn(text)
print(text)   # Hello World
```

### Functions as arguments (higher-order functions)

```python
def apply(func, value):
    return func(value)

print(apply(str.upper, "hello"))   # HELLO
print(apply(len, [1, 2, 3]))       # 3
```

### Functions as return values

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))   # 10
```

### `callable()` and `__call__`

```python
class Greeter:
    def __call__(self, name):
        return f"Hello, {name}"

g = Greeter()
print(callable(g))     # True
print(g("Alice"))      # Hello, Alice
```

---

## Common traps

- **`is` vs variable identity:** `say_hello = greet` makes them the same object (`is` is True). But after `greet = something_else`, `say_hello` still points to the original function.
- **Function attributes persist:** you can set `f.custom = "data"` on any function — it persists for the lifetime of the object.
- **`callable()` vs `type(...) is function`:** classes are callable (they call `__init__`), and so are instances with `__call__`. Don't check `type(x) is function` to test callability — use `callable(x)`.

---

## Interview angle

- "What does it mean for a function to be a first-class object?" → can be stored, passed, returned
- "What is a higher-order function?" → takes function(s) as argument or returns one
- "Is a class callable?" → yes, calling `MyClass()` calls `MyClass.__call__` → `type.__call__` → `MyClass.__new__` + `MyClass.__init__`

---

## Linked drill

`drills/functions_as_objects.py` — all exercises

---

## Linked code-reading puzzles

- `code_reading/easy.md` — general functional patterns

---

## Review notes

