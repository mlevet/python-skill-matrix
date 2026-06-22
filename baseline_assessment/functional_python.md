# Functional Python Assessment

Rate yourself before answering. Answer the interview question aloud
(30 seconds). Predict the code output, then reveal the answer.

---

## Functions as Objects

**Self-rating:** __ / 5

**Interview question:**
"What does it mean for functions to be first-class objects in Python?"

Key points a good answer covers: can be assigned to variables, stored
in data structures, passed as arguments, returned from functions;
`type(f)` is `function`; they have attributes like `__name__` and
`__code__`.

**Code reading:**

```python
def greet(name):
    return f"hi {name}"

say = greet
greet = None

print(say("Alice"))
print(greet)
print(say is greet)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
hi Alice
None
False
```

`say` holds the original function object. Setting `greet = None`
only rebinds the name. `say is greet` is `False` because `greet`
now points to `None`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Lambda Functions

**Self-rating:** __ / 5

**Interview question:**
"What is a lambda, and what can't it do?"

Key points: anonymous function expression; single expression only;
no statements, no assignments; `__name__` is `"<lambda>"`; same
object type as `def`.

**Code reading:**

```python
ops = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
value = 3
for fn in ops:
    print(fn(value))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
4
6
9
```

Each lambda is called in turn with `value = 3`. No late-binding
trap here — `value` doesn't change inside the loop.

</details>

**Assessment:** Strong / Medium / Weak

---

## Higher-Order Functions

**Self-rating:** __ / 5

**Interview question:**
"What is a higher-order function? Give two examples from the standard
library."

Key points: a function that takes a function as argument or returns
one; examples: `map`, `filter`, `sorted`, `functools.reduce`.
`map`/`filter` return lazy iterators in Python 3.

**Code reading:**

```python
result = list(filter(None, [0, 1, False, 2, "", "hi", None, []]))
print(result)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
[1, 2, 'hi']
```

`filter(None, iterable)` removes falsy values. `0`, `False`, `""`,
`None`, and `[]` are all falsy.

</details>

**Assessment:** Strong / Medium / Weak

---

## Closures

**Self-rating:** __ / 5

**Interview question:**
"What is a closure? How does Python store the captured variable?"

Key points: function that retains access to variables from enclosing
scope; captured as cell objects in `__closure__`; captured by
reference, not by value; `nonlocal` required to assign.

**Code reading:**

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
print(double.__closure__[0].cell_contents)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
10
15
2
```

Each call to `make_multiplier` creates an independent scope with its
own `n`. The cell object stores `2` for `double` and `3` for `triple`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Late Binding

**Self-rating:** __ / 5

**Interview question:**
"What is late binding, and why does it catch people off guard in
loops?"

Key points: closures look up variable values at call time, not
definition time; loop variable is one variable that gets reassigned;
fix with default argument `i=i` or factory function; `partial` also
avoids it.

**Code reading:**

```python
ops = {}
for name in ["a", "b", "c"]:
    ops[name] = lambda: name

print(ops["a"]())
print(ops["b"]())
print(ops["c"]())
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
c
c
c
```

All three lambdas close over the same variable `name`. After the
loop, `name` is `"c"`. Every lambda reads `"c"` when called.

</details>

**Assessment:** Strong / Medium / Weak

---

## Decorators

**Self-rating:** __ / 5

**Interview question:**
"How does `@decorator` work? What does `@wraps(func)` do and why
does it matter?"

Key points: `@deco` is syntactic sugar for `func = deco(func)`;
happens at import time; decorator returns a wrapper (usually a
closure); without `@wraps` the wrapper replaces `__name__`, `__doc__`,
`__annotations__`.

**Code reading:**

```python
from functools import wraps

def loud(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@loud
def add(x, y):
    return x + y

result = add(3, 4)
print(result)
print(add.__name__)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
calling add
7
wrapper
```

`add.__name__` is `"wrapper"` because `@loud` didn't use `@wraps`.
Had it used `@wraps(func)`, the last line would print `"add"`.

</details>

**Assessment:** Strong / Medium / Weak

---

## functools.partial

**Self-rating:** __ / 5

**Interview question:**
"What does `functools.partial` do, and how does it differ from a
lambda closure in a loop?"

Key points: pre-fills arguments at creation time (eager binding);
unlike a closure, it does not look up the variable later; cleaner
than `lambda i=i: f(i)`; `__name__` from original function is
preserved.

**Code reading:**

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)

print(square(4))
print(cube(3))
print(square.__name__)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
16
27
power
```

`partial` freezes `exp=2` and `exp=3` at creation. `__name__` is
inherited from the original `power` function.

</details>

**Assessment:** Strong / Medium / Weak

---

## functools.lru_cache

**Self-rating:** __ / 5

**Interview question:**
"What does `@lru_cache` do? What type of arguments can it cache, and
why?"

Key points: memoization — caches return values keyed by arguments;
arguments must be hashable (no lists or dicts); `maxsize=None` is
unbounded; decorated function gains `cache_info()` and
`cache_clear()`.

**Code reading:**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))
info = fib.cache_info()
print(info.misses)
print(info.hits)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
8
7
4
```

`fib(6)` = 8. Computing it requires 7 unique values (0–6), so
misses = 7. The remaining calls (e.g. `fib(4)` is used twice) hit
the cache: hits = 4.

</details>

**Assessment:** Strong / Medium / Weak
