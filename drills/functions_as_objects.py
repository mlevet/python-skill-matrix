"""
Drill: Functions as First-Class Objects
Domain: functional_python
Linked topic: domains/functional_python/functions_as_objects.md

Core idea: in Python, functions are objects. They can be stored in variables,
passed as arguments, returned from other functions, and stored in data structures.
"""

# =============================================================================
# EXERCISE 1 — Predict the output
# =============================================================================

def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Alice"))          # ?
print(greet is say_hello)          # ?
print(type(greet))                 # ?
print(greet.__name__)              # ?
print(say_hello.__name__)          # ?

# Expected:
# Hello, Alice
# True
# <class 'function'>
# greet
# greet   ← same name, because say_hello is just another reference to the same object


# =============================================================================
# EXERCISE 2 — Functions stored in a dict (dispatch table)
# =============================================================================

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

ops = {
    '+': add,
    '-': sub,
    '*': mul,
}

# What does this print?
for symbol, fn in ops.items():
    print(f"3 {symbol} 2 = {fn(3, 2)}")

# Expected:
# 3 + 2 = 5
# 3 - 2 = 1
# 3 * 2 = 6


# =============================================================================
# EXERCISE 3 — Higher-order function: function as argument
# =============================================================================

def apply(func, value):
    return func(value)

# Predict:
print(apply(str.upper, "hello"))   # ?
print(apply(len, [1, 2, 3]))       # ?
print(apply(lambda x: x ** 2, 5)) # ?

# Expected: HELLO / 3 / 25


# =============================================================================
# EXERCISE 4 — Function as return value
# =============================================================================

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # ?
print(triple(5))   # ?
print(double is triple)  # ?

# Expected: 10 / 15 / False


# =============================================================================
# EXERCISE 5 — Sorting with a function key
# =============================================================================

words = ["banana", "fig", "apple", "cherry", "date"]

# Sort by length, then alphabetically for ties
sorted_words = sorted(words, key=lambda w: (len(w), w))
print(sorted_words)

# Expected: ['fig', 'date', 'apple', 'banana', 'cherry']


# =============================================================================
# EXERCISE 6 — Callable check
# =============================================================================

class MyClass:
    def __call__(self, x):
        return x * 2

obj = MyClass()
print(callable(obj))           # ?
print(callable(42))            # ?
print(callable(print))         # ?
print(obj(5))                  # ?

# Expected: True / False / True / 10


# =============================================================================
# EXERCISE 7 — Functions have attributes
# =============================================================================

def documented_function():
    """This is the docstring."""
    pass

documented_function.custom_attr = "metadata"

print(documented_function.__doc__)
print(documented_function.custom_attr)
print(dir(documented_function))  # shows all attributes


# =============================================================================
# RUN ALL (no asserts — exercises are predict-the-output style)
# =============================================================================

if __name__ == "__main__":
    print("\nAll exercises run. Check predictions above.")
