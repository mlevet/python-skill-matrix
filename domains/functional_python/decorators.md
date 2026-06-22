---
topic: Decorators
domain: functional_python
confidence: 0
last_reviewed: never
interview_freq: high
---

# Decorators

## Summary

A decorator is a callable that takes a function (or class) and returns a replacement. `@deco` above a `def` is syntactic sugar for `func = deco(func)`. Understanding decorators requires understanding closures and first-class functions.

---

## Key concepts

- `@deco` is exactly `func = deco(func)` — no magic.
- Stacking decorators applies them bottom-up: `@A @B def f` → `f = A(B(f))`.
- Always use `@functools.wraps(func)` inside the wrapper to preserve `__name__`, `__doc__`, `__wrapped__`.
- Decorators with arguments require a third layer: `@repeat(3)` → `repeat(3)` returns a decorator, which is then applied.
- Class-based decorators implement `__call__`.

---

## Code examples

### Minimal decorator

```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done {func.__name__}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(1, 2)
# Calling add
# Done add
```

### Decorator with arguments (factory pattern)

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)

say("hi")   # prints "hi" three times
```

### Stacking order

```python
@A   # applied second (outermost)
@B   # applied first (innermost)
def f(): ...

# equivalent to:
f = A(B(f))

# Call order: A's wrapper → B's wrapper → f
```

### Class-based decorator

```python
from functools import wraps

class CallCounter:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

@CallCounter
def add(x, y):
    return x + y

add(1, 2)
add(3, 4)
print(add.calls)   # 2
```

### Why `@wraps` matters

```python
def bad(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad
def original():
    """My docstring."""
    pass

print(original.__name__)   # wrapper  ← wrong!
print(original.__doc__)    # None     ← lost!
```

---

## Common traps

- **Forgetting `@wraps`:** the wrapper's name and docstring replace the original's, breaking `help()`, logging, and introspection.
- **Decorator order:** applied bottom-up, executed outside-in. Confuses people when logging decorators seem out of order.
- **Decorators with args:** need three levels of nesting (`decorator_factory → decorator → wrapper`). A common mistake is using only two.
- **Decoration happens at definition time:** side effects in the decorator body run when the module is imported, not when the function is called.

---

## Interview angle

- "What does `@decorator` do?" → exactly `func = decorator(func)`
- "What order do stacked decorators run in?" → bottom-up application, outermost first at call time
- "Why use `@functools.wraps`?" → preserves `__name__`, `__doc__`, `__wrapped__` for debugging/introspection
- "How do you write a decorator that accepts arguments?" → three-level nesting

---

## Linked drill

`drills/decorators.py` — all exercises

---

## Linked code-reading puzzles

- `code_reading/medium.md` — Puzzle M3 (decorator execution order)
- `code_reading/medium.md` — Puzzle M9 (functools.wraps)

---

## Review notes

