"""
Drill: Closures
Domain: functional_python
Linked topic: domains/functional_python/closures.md

A closure is a function that captures variables from its enclosing scope.
The captured variable is a REFERENCE, not a copy — this is the source of most traps.
"""

# =============================================================================
# EXERCISE 1 — Basic closure
# =============================================================================

def outer():
    x = 10
    def inner():
        return x   # 'x' is a free variable — captured from outer's scope
    return inner

f = outer()
print(f())         # ?
print(f.__closure__)   # ?
print(f.__closure__[0].cell_contents)  # ?

# Expected:
# 10
# (<cell at 0x...>,)  ← one cell per free variable
# 10


# =============================================================================
# EXERCISE 2 — Closure captures the variable, not the value
# =============================================================================

def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c1 = make_counter()
c2 = make_counter()

print(c1())   # ?
print(c1())   # ?
print(c2())   # ?
print(c1())   # ?

# Expected: 1 / 2 / 1 / 3
# c1 and c2 have independent closures over their own `count` variables


# =============================================================================
# EXERCISE 3 — The classic late-binding trap
# =============================================================================

# Broken:
funcs_broken = []
for i in range(5):
    funcs_broken.append(lambda: i)

print([f() for f in funcs_broken])   # ?

# Fixed — capture by default argument:
funcs_fixed = []
for i in range(5):
    funcs_fixed.append(lambda i=i: i)

print([f() for f in funcs_fixed])    # ?

# Fixed — use a factory function:
def make_func(val):
    return lambda: val

funcs_factory = [make_func(i) for i in range(5)]
print([f() for f in funcs_factory])  # ?

# Expected:
# [4, 4, 4, 4, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]


# =============================================================================
# EXERCISE 4 — `nonlocal` keyword
# =============================================================================

def make_adder(start):
    total = start
    def add(x):
        nonlocal total
        total += x
        return total
    return add

add_from_10 = make_adder(10)
print(add_from_10(5))   # ?
print(add_from_10(3))   # ?
print(add_from_10(2))   # ?

# Expected: 15 / 18 / 20


# =============================================================================
# EXERCISE 5 — Without `nonlocal`: what happens?
# =============================================================================

def make_broken_adder(start):
    total = start
    def add(x):
        # total += x   ← UnboundLocalError without nonlocal!
        return total + x   # read-only is fine
    return add

broken = make_broken_adder(10)
print(broken(5))   # ?
print(broken(3))   # note: total is NOT updated

# Expected: 15 / 13 (total stays 10)


# =============================================================================
# EXERCISE 6 — Closure over loop: the mutable variable version
# =============================================================================

def make_powers():
    results = []
    for exp in range(1, 5):
        results.append(lambda x, e=exp: x ** e)  # fixed with default arg
    return results

powers = make_powers()
print([p(2) for p in powers])   # ?

# Expected: [2, 4, 8, 16]


# =============================================================================
# EXERCISE 7 — Inspect closures
# =============================================================================

def outer(x, y):
    def inner():
        return x + y
    return inner

f = outer(3, 4)
print(f.__code__.co_freevars)      # names of free variables
print(len(f.__closure__))          # number of cells
print([c.cell_contents for c in f.__closure__])

# Expected:
# ('x', 'y')
# 2
# [3, 4]


# =============================================================================
# EXERCISE 8 — Closure in a class method (common OOP pattern)
# =============================================================================

class Button:
    def __init__(self, label, action):
        self.label = label
        self._action = action

    def click(self):
        return self._action()

message = "Clicked!"
btn = Button("OK", lambda: message)

print(btn.click())   # ?

message = "Changed!"
print(btn.click())   # ?  ← does it reflect the change?

# Expected:
# Clicked!
# Changed!   ← yes, the lambda captures the variable `message`, not its value


if __name__ == "__main__":
    print("\nAll closure drills complete.")
