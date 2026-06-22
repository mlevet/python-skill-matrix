# Decorators

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

A decorator is a callable that takes a function and returns a
replacement. `@deco` above a `def` is syntactic sugar for
`func = deco(func)`, executed immediately after the function is defined.
Decorators are built on closures and first-class functions — you need
both to implement one from scratch.

## Mental model

`@deco` is just assignment with extra syntax. When Python sees:

```python
@timer
def fetch():
    ...
```

it executes `fetch = timer(fetch)` right after defining `fetch`. The
decorator replaces the original function with whatever `timer` returns —
usually a wrapper closure that calls the original.

Three-layer pattern for decorators that take arguments:

```python
def repeat(n):          # layer 1: receives the argument
    def decorator(func):  # layer 2: receives the function
        @wraps(func)
        def wrapper(*args, **kwargs):  # layer 3: the actual wrapper
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("hi")
```

`@repeat(3)` calls `repeat(3)` first, which returns `decorator`, which
then wraps `hello`.

## Why interviewers ask this

Decorators are the standard test for closures, first-class functions,
`*args/**kwargs`, and `functools.wraps` all in one question. "Implement
a timer decorator" or "implement `@retry(n)`" is a canonical coding
task. A strong answer uses `@wraps`, handles arbitrary signatures with
`*args, **kwargs`, and explains the three-layer pattern for arguments.

## Common traps

- Without `@wraps(func)`, the wrapper replaces `__name__`, `__doc__`,
  and `__annotations__` with its own. Logging, introspection, and
  frameworks that inspect function metadata all break silently.
- Stacking order is bottom-up: `@A @B def f` applies `B` first, then
  `A`. The resulting call order is top-down: `A`'s wrapper runs first
  and calls `B`'s wrapper.
- Decoration happens at import time, not at call time. Any code in the
  decorator body runs when the module loads, not when the function is
  called.
- A decorator that forgets to `return wrapper` returns `None`, silently
  replacing the function with `None`. The error only appears on the
  first call.
- Decorators with arguments need three layers. Forgetting the middle
  layer is the most common implementation mistake.

## Code-reading example

```python
from functools import wraps

def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

print(greet("world"))
print(greet.__name__)
```

### Answer

```
HELLO WORLD
greet
```

### Explanation

`@shout` replaces `greet` with `wrapper`. Calling `greet("world")`
now calls `wrapper("world")`, which calls the original `greet` and
uppercases the result. `greet.__name__` is `"greet"` — not `"wrapper"`
— because `@wraps(func)` copies the original function's metadata onto
the wrapper. Without `@wraps`, it would print `"wrapper"`.

## Related topics

- Closures
- Functions as objects
- functools.wraps
- Callable objects
