"""
Drill: Lambdas
Domain: functional_python
Linked topic: domains/functional_python/lambdas.md

Lambda = anonymous function. Single expression. Often confused with closures.
Key traps: late binding, lambda in loops, lambda vs def.
"""

# =============================================================================
# EXERCISE 1 — Basic lambda syntax
# =============================================================================

square = lambda x: x ** 2
add = lambda x, y: x + y
identity = lambda x: x

print(square(4))      # ?
print(add(3, 4))      # ?
print(identity(99))   # ?
print(type(square))   # ?

# Expected: 16 / 7 / 99 / <class 'function'>


# =============================================================================
# EXERCISE 2 — Lambda as argument (sort, filter, map)
# =============================================================================

nums = [3, -1, 4, -1, 5, -9, 2, 6]

# Sort by absolute value
by_abs = sorted(nums, key=lambda x: abs(x))
print(by_abs)  # ?

# Filter positives
positives = list(filter(lambda x: x > 0, nums))
print(positives)  # ?

# Square all
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # ?

# Expected:
# [-1, -1, 2, 3, 4, 5, 6, -9]
# [3, 4, 5, 2, 6]
# [9, 1, 16, 1, 25, 81, 4, 36]


# =============================================================================
# EXERCISE 3 — The late binding trap in a loop
# =============================================================================

# BROKEN: all lambdas will return the same value
broken = [lambda: i for i in range(5)]
print([f() for f in broken])   # what does this print?

# FIXED: capture i's value at definition time
fixed = [lambda i=i: i for i in range(5)]
print([f() for f in fixed])    # what does this print?

# Expected:
# [4, 4, 4, 4, 4]
# [0, 1, 2, 3, 4]


# =============================================================================
# EXERCISE 4 — Lambda in a dict (dispatch)
# =============================================================================

ops = {
    'double': lambda x: x * 2,
    'square': lambda x: x ** 2,
    'negate': lambda x: -x,
}

for name, fn in ops.items():
    print(f"{name}(5) = {fn(5)}")

# Expected:
# double(5) = 10
# square(5) = 25
# negate(5) = -5


# =============================================================================
# EXERCISE 5 — Lambda returning a lambda
# =============================================================================

make_adder = lambda n: lambda x: x + n

add5 = make_adder(5)
add10 = make_adder(10)

print(add5(3))    # ?
print(add10(3))   # ?
print(make_adder(7)(3))  # ?

# Expected: 8 / 13 / 10


# =============================================================================
# EXERCISE 6 — Lambda limitations (what you cannot do)
# =============================================================================

# These are INVALID — uncomment to see SyntaxErrors:
# f = lambda x: if x > 0: return x else: return -x   # no if/else statement
# f = lambda x: x = x + 1                            # no assignment

# This IS valid (conditional expression):
abs_val = lambda x: x if x >= 0 else -x
print(abs_val(-5))   # 5
print(abs_val(3))    # 3


# =============================================================================
# EXERCISE 7 — `sorted` with multiple keys
# =============================================================================

people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 30),
    ("Dave", 25),
]

# Sort by age ascending, then name ascending
result = sorted(people, key=lambda p: (p[1], p[0]))
print(result)

# Expected:
# [('Bob', 25), ('Dave', 25), ('Alice', 30), ('Charlie', 30)]


# =============================================================================
# EXERCISE 8 — Lambda vs def: are they really the same?
# =============================================================================

def square_def(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(square_def(4) == square_lambda(4))   # True
print(square_def.__name__)                  # square_def
print(square_lambda.__name__)               # <lambda>  ← key difference for debugging


if __name__ == "__main__":
    print("\nAll lambda drills complete.")
