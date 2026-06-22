# Code Reading — Medium

Puzzles involving closures, late binding, decorators, and OOP traps.
Aim to predict the output before revealing the answer.

---

## Puzzle M1 — Classic late binding closure

**Topic:** functional_python / closures  
**Trap:** closures capture the *variable*, not its value at creation time

```python
functions = []
for i in range(5):
    functions.append(lambda: i)

print([f() for f in functions])
```

**What does this print?**

<details>
<summary>Answer</summary>

```
[4, 4, 4, 4, 4]
```

All lambdas close over the variable `i`, not the value of `i` at
creation time. By the time they are called, the loop has finished
and `i == 4`.

**Fix — capture by default argument:**
```python
functions = [lambda i=i: i for i in range(5)]
print([f() for f in functions])  # [0, 1, 2, 3, 4]
```

</details>

---

## Puzzle M2 — Late binding with `functools.partial`

**Topic:** functional_python / closures, functools  
**Trap:** contrast with the late-binding trap above

```python
from functools import partial

def multiply(x, y):
    return x * y

functions = [partial(multiply, i) for i in range(5)]
print([f(2) for f in functions])
```

**What does this print?**

<details>
<summary>Answer</summary>

```
[0, 2, 4, 6, 8]
```

`partial` *binds the value at creation time*, not the variable. This
is why `partial` avoids the late binding trap that raw lambdas fall
into.

</details>

---

## Puzzle M3 — Decorator execution order

**Topic:** functional_python / decorators  
**Trap:** decorators are applied bottom-up but execute top-down

```python
def decorator_a(func):
    print("applying A")
    def wrapper(*args, **kwargs):
        print("A before")
        result = func(*args, **kwargs)
        print("A after")
        return result
    return wrapper

def decorator_b(func):
    print("applying B")
    def wrapper(*args, **kwargs):
        print("B before")
        result = func(*args, **kwargs)
        print("B after")
        return result
    return wrapper

@decorator_a
@decorator_b
def greet():
    print("hello")

greet()
```

**What does this print?**

<details>
<summary>Answer</summary>

```
applying B
applying A
B before
A before
hello
A after
B after
```

Wait — re-read that. `@decorator_a` is on top, so it is applied *last*
(outermost). `@decorator_b` is applied first (innermost). Application
order: B then A. Call order: A's wrapper runs first and calls B's
wrapper, which calls `greet`.

</details>

---

## Puzzle M4 — `__init__` vs `__new__`

**Topic:** oop / dunder_methods  
**Trap:** `__new__` creates the instance; `__init__` initializes it

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)
print(id(a) == id(b))
```

**What does this print?**

<details>
<summary>Answer</summary>

```
True
True
```

`__new__` returns the existing instance on subsequent calls, so `a`
and `b` are the same object.

</details>

---

## Puzzle M5 — MRO and `super()`

**Topic:** oop / inheritance_mro  
**Trap:** `super()` follows MRO, not the class where `super()` is written

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        super().method()
        print("B")

class C(A):
    def method(self):
        super().method()
        print("C")

class D(B, C):
    def method(self):
        super().method()
        print("D")

D().method()
```

**What does this print?**

<details>
<summary>Answer</summary>

```
A
C
B
D
```

MRO for D is: D → B → C → A. Each `super()` call goes to the next
in MRO, not the parent of the class where `super()` is written.

</details>

---

## Puzzle M6 — Generator vs list

**Topic:** advanced_syntax / generators  
**Trap:** generators are lazy and can only be iterated once

```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(list(g))
print(list(g))
```

**What does this print?**

<details>
<summary>Answer</summary>

```
[1, 2, 3]
[]
```

Once a generator is exhausted, subsequent calls to `list()` on it
return `[]`. The generator is not reset.

</details>

---

## Puzzle M7 — `__class__` in `super()`

**Topic:** oop / dunder_methods  
**Trap:** unbound `super()` uses `__class__` cell variable

```python
class Base:
    def greet(self):
        return "base"

class Child(Base):
    def greet(self):
        return "child: " + super().greet()

obj = Child()
print(obj.greet())
print(Child.greet(obj))
```

**What does this print?**

<details>
<summary>Answer</summary>

```
child: base
child: base
```

Both work the same. `super()` with no arguments uses `__class__` (a
compiler cell variable) and the first argument of the method.

</details>

---

## Puzzle M8 — Walrus in comprehension scope

**Topic:** advanced_syntax / walrus  
**Trap:** walrus operator leaks into enclosing scope; loop variable does not

```python
results = [y := x * 2 for x in range(5)]
print(results)
print(y)
try:
    print(x)
except NameError:
    print("x not defined")
```

**What does this print?**

<details>
<summary>Answer</summary>

```
[0, 2, 4, 6, 8]
8
x not defined
```

The walrus `:=` leaks the variable into the enclosing scope
(`y == 8` after the comprehension). The loop variable `x` does not
leak — comprehensions have their own scope for loop variables since
Python 3.

</details>

---

## Puzzle M9 — `functools.wraps` and `__name__`

**Topic:** functional_python / decorators  
**Trap:** without `@wraps`, the wrapper hides the original function's metadata

```python
from functools import wraps

def log_without_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def log_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@log_without_wraps
def foo():
    pass

@log_with_wraps
def bar():
    pass

print(foo.__name__)
print(bar.__name__)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
wrapper
bar
```

Without `@wraps`, `foo.__name__` is `"wrapper"` — the original name
is lost. `@wraps` copies `__name__`, `__doc__`, and other attributes
from the wrapped function.

</details>

---

## Puzzle M10 — Iterator protocol and exhaustion

**Topic:** advanced_syntax / generators  
**Trap:** an iterator is not the same as an iterable — calling `iter()`
on an iterator returns itself, and it can only be traversed once

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))
print(next(it))

for n in it:
    print(n)

for n in it:
    print("again:", n)

print("done")
```

**What does this print?**

<details>
<summary>Answer</summary>

```
1
2
3
done
```

The first `next()` calls consume `1` and `2`. The `for` loop resumes
the iterator and consumes `3`. The second `for` loop gets nothing —
the iterator is exhausted. `"again:"` never prints.

</details>

---

## Puzzle M11 — `__call__` on class instances

**Topic:** oop / callable_objects  
**Trap:** instances are not callable by default — only when `__call__`
is defined on the class

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n

add5 = Adder(5)
ops = [Adder(1), Adder(2), add5]

print(callable(add5))
print([op(10) for op in ops])
print(add5.__class__.__name__)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
True
[11, 12, 15]
Adder
```

`callable(add5)` is `True` because `Adder` defines `__call__`. Each
`op(10)` calls `Adder.__call__(op, 10)`. `__class__.__name__` is
`"Adder"`.

</details>
