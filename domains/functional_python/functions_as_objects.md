# Functions as Objects

---
**Path:** [Functional Python](../../roadmaps/functional_python_path.md) — Step 1 of 8  
**Next:** [Lambda Functions](lambda_functions.md)  
**Drill:** [drills/functions_as_objects.py](../../drills/functions_as_objects.py)  
**Code Reading:** [E10 — Function assignment](../../code_reading/easy.md)

---

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

In Python, functions are first-class objects. They can be assigned to
variables, stored in data structures, passed as arguments, and returned
from other functions. `type(f)` returns `<class 'function'>`. This is
the foundation of decorators, callbacks, and higher-order functions.

## Mental model

A function is an object that happens to be callable. The `def` statement
creates a function object and binds it to a name — exactly like
`x = 42` creates an int and binds it. After that, the name is just a
reference; the object exists independently.

```python
def greet(name):
    return f"hello {name}"

say_hello = greet   # two names, one object
print(say_hello is greet)  # True
```

Deleting or reassigning one name doesn't affect the other. The object
survives as long as at least one reference to it exists.

## Why interviewers ask this

They are testing whether you understand that functions are not special
syntax — they are objects with attributes (`__name__`, `__doc__`,
`__code__`, `__defaults__`). This is the conceptual foundation for
decorators, closures, and any pattern where behavior is passed as data.
A candidate who says "functions are objects" and can show it is
signalling real Python fluency.

## Common traps

- Assigning `f = greet` creates a second reference, not a copy.
  `f is greet` is `True` immediately after the assignment.
- Reassigning `greet = None` does not affect `f`. The function object
  is still alive; only the name `greet` now points elsewhere.
- `__name__` reflects the name at definition time, not the current
  variable name. If you alias a function, `__name__` doesn't update.
- `callable(x)` is the right check for "can I call this?", not
  `type(x) is function`. Classes, instances with `__call__`, and
  built-ins all pass `callable()` but fail a type check.
- Functions have mutable `__dict__`. You can attach arbitrary
  attributes: `greet.call_count = 0`. This is occasionally used in
  decorators to store state without a closure.

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

`say` holds the original function object. Setting `greet = None` only
rebinds the name `greet` — it does not touch the object. `say.__name__`
is `"greet"` because `__name__` is set at definition time and never
updated automatically. `say is greet` is `False` because `greet` now
points to `None`.

## Related topics

- Lambda functions
- Closures
- Higher-order functions
- Decorators
