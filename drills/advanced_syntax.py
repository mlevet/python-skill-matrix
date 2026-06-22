"""
Drill: Advanced Syntax
Domain: advanced_syntax
Linked topics: advanced_syntax/walrus.md, advanced_syntax/unpacking.md,
               advanced_syntax/generators.md, advanced_syntax/context_managers.md

Covers: walrus operator, extended unpacking, context managers, f-strings, type hints.
"""

# =============================================================================
# EXERCISE 1 — Walrus operator (:=)
# =============================================================================

# Basic: assign and test in one expression
import re

text = "Hello, my number is 42!"
if m := re.search(r'\d+', text):
    print(f"Found number: {m.group()}")   # ?

# In a while loop:
data = iter([1, 2, 3, None, 4])
while (val := next(data, None)) is not None:
    print(val, end=" ")
print()

# Scope leakage in comprehension:
results = [y := x * 2 for x in range(4)]
print(results)   # ?
print(y)         # ?  ← leaks into enclosing scope

# Expected:
# Found number: 42
# 1 2 3
# [0, 2, 4, 6]
# 6


# =============================================================================
# EXERCISE 2 — Extended unpacking
# =============================================================================

first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]
print(type(rest))  # list (always a list, even if source is tuple)

*init, last = (10, 20, 30, 40)
print(init)    # [10, 20, 30]
print(last)    # 40

a, *middle, b = range(6)
print(a)       # 0
print(middle)  # [1, 2, 3, 4]
print(b)       # 5

# Nested unpacking:
(x, y), z = (1, 2), 3
print(x, y, z)   # 1 2 3

# Swap (classic Python idiom):
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1


# =============================================================================
# EXERCISE 3 — `*` and `**` in function calls
# =============================================================================

def f(a, b, c):
    return a + b + c

args = [1, 2, 3]
kwargs = {'a': 10, 'b': 20, 'c': 30}

print(f(*args))     # ?  6
print(f(**kwargs))  # ?  60

# Merge dicts (Python 3.9+):
d1 = {'x': 1, 'y': 2}
d2 = {'y': 99, 'z': 3}
merged = {**d1, **d2}
print(merged)   # ?  {'x': 1, 'y': 99, 'z': 3}  ← d2 wins on conflict


# =============================================================================
# EXERCISE 4 — Context managers
# =============================================================================

# Using contextlib.contextmanager to create one with a generator:
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")

with managed_resource("DB connection") as res:
    print(f"Using {res}")

# Expected:
# Acquiring DB connection
# Using DB connection
# Releasing DB connection

# Class-based context manager:
class Timer:
    import time as _time

    def __enter__(self):
        self._start = self._time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = self._time.perf_counter() - self._start
        return False   # don't suppress exceptions

with Timer() as t:
    sum(range(100_000))

print(f"Elapsed: {t.elapsed:.6f}s")


# =============================================================================
# EXERCISE 5 — Advanced f-strings
# =============================================================================

x = 3.14159
name = "world"

print(f"{x:.2f}")         # 3.14
print(f"{x!r}")           # 3.14159
print(f"{name!r}")        # 'world'
print(f"{name!s}")        # world  (same as str())
print(f"{name!a}")        # 'world' (ascii repr)

# Debug format (Python 3.8+):
value = 42
print(f"{value=}")        # value=42

# Expressions inside:
print(f"{2 ** 10}")       # 1024
print(f"{'hello'.upper()}")  # HELLO

# Alignment:
print(f"{'left':<10}|")    # 'left      |'
print(f"{'right':>10}|")   # '     right|'
print(f"{'center':^10}|")  # '  center  |'


# =============================================================================
# EXERCISE 6 — Type hints (runtime behavior)
# =============================================================================

from typing import Optional, Union, List, Callable

def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

print(greet("Alice"))
print(greet("Bob", 3))

# Type hints are not enforced at runtime:
print(greet(123))   # works fine — no error at runtime!

# Inspect annotations:
print(greet.__annotations__)

# Expected:
# Hello, Alice!
# Hello, Bob! Hello, Bob! Hello, Bob!
# Hello, 123!
# {'name': <class 'str'>, 'times': <class 'int'>, 'return': <class 'str'>}


# =============================================================================
# EXERCISE 7 — Generator expressions: lazy pipelines
# =============================================================================

# This processes 1M numbers without storing them:
result = sum(x ** 2 for x in range(1_000_000) if x % 2 == 0)
print(result)   # sum of squares of even numbers 0..999998


# =============================================================================
# EXERCISE 8 — `__enter__` / `__exit__` exception handling
# =============================================================================

class SuppressZeroDivision:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print("Caught ZeroDivisionError — suppressed")
            return True   # suppress the exception
        return False   # re-raise anything else

with SuppressZeroDivision():
    result = 1 / 0      # would normally crash
    print("This line is not reached")

print("Execution continues here")   # ?

# Expected:
# Caught ZeroDivisionError — suppressed
# Execution continues here


if __name__ == "__main__":
    print("\nAll advanced syntax drills complete.")
