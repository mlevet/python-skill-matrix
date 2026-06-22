# Functions as Objects

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 7/10 |
| Freshness | Medium |
| Interview Frequency | High |
| Last Reviewed | TBD |
| Next Review | TBD |

## 30-second explanation

In Python, functions are first-class objects. They can be assigned to variables, stored in data structures, passed as arguments, and returned from other functions. `type(f)` returns `<class 'function'>`. This is the foundation of decorators, callbacks, and functional programming patterns.

## Mental model

A function is just an object that happens to be callable. The `def` statement creates a function object and binds it to a name — exactly like `x = 42` creates an int and binds it. After that, the name is just a reference.

```python
def greet(name):
    return f"hello {name}"

say_hello = greet   # two names, one object
```

`say_hello` and `greet` point to the same function. Deleting or reassigning one doesn't affect the other.

## Why interviewers ask this

They are testing whether you understand that functions are not special syntax — they're objects with attributes (`__name__`, `__doc__`, `__code__`). This underpins decorators, callbacks, and any pattern where behavior is passed around as data.

## Common traps

- Assigning `f = greet` creates a second reference, not a copy. `f is greet` is `True`.
- Reassigning `greet = None` does not affect `f` — `f` still holds the original object.
- `__name__` is an attribute of the object, not the variable. It reflects the name at definition, not the current variable name.
- `callable(x)` is the correct check, not `type(x) is function` — classes and instances with `__call__` are also callable.

## Code-reading example

```python
def greet(name):
    return f"hello {name}"

say = greet
greet = None

print(say("Alice"))
print(say.__name__)
print(say is greet)
```

### Answer

```
hello Alice
greet
False
```

### Explanation

`say` still holds the original function object. Setting `greet = None` only rebinds the name `greet` — it doesn't touch the object. `say.__name__` is `"greet"` because `__name__` is fixed at definition time, not updated when you reassign the variable. `say is greet` is `False` because `greet` now points to `None`.

## Related topics

- Lambda functions
- Closures
- Higher-order functions
- Decorators
