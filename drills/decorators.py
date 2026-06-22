"""
Drill: Decorators
Domain: functional_python
Linked topic: domains/functional_python/decorators.md

A decorator is a function that takes a function and returns a replacement function.
`@deco` is syntactic sugar for `func = deco(func)`.
"""

from functools import wraps
import time

# =============================================================================
# EXERCISE 1 — Manual decorator (no sugar)
# =============================================================================

def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def greet(name):
    return f"hello {name}"

# Apply manually:
greet = shout(greet)
print(greet("alice"))   # ?

# Expected: HELLO ALICE


# =============================================================================
# EXERCISE 2 — Decorator with @syntax
# =============================================================================

def shout_v2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout_v2
def greet_v2(name):
    """Greets someone."""
    return f"hello {name}"

print(greet_v2("bob"))         # ?
print(greet_v2.__name__)       # ?   ← wraps preserves this
print(greet_v2.__doc__)        # ?   ← and this

# Expected: HELLO BOB / greet_v2 / Greets someone.


# =============================================================================
# EXERCISE 3 — Decorator execution order (stacking)
# =============================================================================

def deco_a(func):
    print("Applying A")
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("A: before")
        r = func(*args, **kwargs)
        print("A: after")
        return r
    return wrapper

def deco_b(func):
    print("Applying B")
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("B: before")
        r = func(*args, **kwargs)
        print("B: after")
        return r
    return wrapper

@deco_a
@deco_b
def target():
    print("target")

# What does the entire block above print, including decoration?
print("--- calling target ---")
target()

# Expected (including decoration at import time):
# Applying B
# Applying A
# --- calling target ---
# A: before
# B: before
# target
# B: after
# A: after


# =============================================================================
# EXERCISE 4 — Decorator with arguments (factory pattern)
# =============================================================================

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

say("hi")   # expected: prints "hi" 3 times


# =============================================================================
# EXERCISE 5 — Timer decorator
# =============================================================================

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

result = slow_sum(1_000_000)
print(f"Result: {result}")


# =============================================================================
# EXERCISE 6 — Class-based decorator
# =============================================================================

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

print(add(1, 2))     # 3
print(add(3, 4))     # 7
print(add.calls)     # 2


# =============================================================================
# EXERCISE 7 — Preserve function identity: why @wraps matters
# =============================================================================

def bad_deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def good_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_deco
def original_bad():
    """Original docstring."""
    pass

@good_deco
def original_good():
    """Original docstring."""
    pass

print(original_bad.__name__)    # ?  wrapper
print(original_bad.__doc__)     # ?  None
print(original_good.__name__)   # ?  original_good
print(original_good.__doc__)    # ?  Original docstring.


# =============================================================================
# EXERCISE 8 — Property as a descriptor-based decorator
# =============================================================================

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)   # 5
print(round(c.area, 2))  # 78.54

c.radius = 10
print(c.radius)   # 10

try:
    c.radius = -1
except ValueError as e:
    print(e)   # Radius cannot be negative


if __name__ == "__main__":
    print("\nAll decorator drills complete.")
