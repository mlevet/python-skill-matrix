"""
Drill: Iterators & Generators
Domain: advanced_syntax
Linked topic: domains/advanced_syntax/generators.md

Iterator protocol: __iter__ returns self, __next__ returns next value or raises StopIteration.
Generator: a function with yield. Lazy — values computed on demand.
"""

# =============================================================================
# EXERCISE 1 — Manual iterator protocol
# =============================================================================

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in Countdown(3):
    print(n)   # ?

# Expected: 3 / 2 / 1


# =============================================================================
# EXERCISE 2 — Generator function
# =============================================================================

def countdown(start):
    while start > 0:
        yield start
        start -= 1

gen = countdown(3)
print(next(gen))   # ?
print(next(gen))   # ?
print(next(gen))   # ?
# next(gen)        # would raise StopIteration

# Expected: 3 / 2 / 1


# =============================================================================
# EXERCISE 3 — Generator is lazy (and exhaustible)
# =============================================================================

def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = infinite_counter()
first_five = [next(counter) for _ in range(5)]
print(first_five)   # ?

# Generators can be exhausted:
gen = (x ** 2 for x in range(3))
print(list(gen))   # ?
print(list(gen))   # ?  ← second time

# Expected:
# [0, 1, 2, 3, 4]
# [0, 1, 4]
# []


# =============================================================================
# EXERCISE 4 — Generator expression vs list comprehension
# =============================================================================

import sys

list_comp = [x ** 2 for x in range(1000)]
gen_expr  = (x ** 2 for x in range(1000))

print(type(list_comp))   # list
print(type(gen_expr))    # generator
print(sys.getsizeof(list_comp))   # large
print(sys.getsizeof(gen_expr))    # tiny — lazy, not stored


# =============================================================================
# EXERCISE 5 — `yield from`
# =============================================================================

def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2], (3, 4), range(5, 7)))
print(result)   # ?

# Expected: [1, 2, 3, 4, 5, 6]


# =============================================================================
# EXERCISE 6 — Generator `.send()` — two-way communication
# =============================================================================

def accumulator():
    total = 0
    while True:
        value = yield total   # yield sends total out; receives value in
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)           # prime — run until first yield
print(gen.send(10)) # ?
print(gen.send(20)) # ?
print(gen.send(5))  # ?

# Expected: 10 / 30 / 35


# =============================================================================
# EXERCISE 7 — `itertools` essentials
# =============================================================================

import itertools

# chain: flatten
print(list(itertools.chain([1, 2], [3, 4], [5])))   # [1, 2, 3, 4, 5]

# islice: take first N from lazy sequence
gen = (x ** 2 for x in itertools.count(1))
print(list(itertools.islice(gen, 5)))   # [1, 4, 9, 16, 25]

# groupby: consecutive groups (input must be sorted first!)
data = sorted([("a", 1), ("b", 2), ("a", 3)], key=lambda t: t[0])
for key, group in itertools.groupby(data, key=lambda t: t[0]):
    print(key, list(group))

# zip_longest vs zip:
a = [1, 2, 3]
b = [4, 5]
print(list(zip(a, b)))                               # [(1,4),(2,5)]
print(list(itertools.zip_longest(a, b, fillvalue=0))) # [(1,4),(2,5),(3,0)]


# =============================================================================
# EXERCISE 8 — Identify the trap
# =============================================================================

# What does this print?
def gen_with_print():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen_with_print()   # does "start" print here?
print("before next")
print(next(g))
print("between nexts")
print(next(g))
print("after all")

# Expected:
# before next
# start
# 1
# between nexts
# middle
# 2
# after all
# (then "end" would print if we called next(g) again, which raises StopIteration)


if __name__ == "__main__":
    print("\nAll iterator/generator drills complete.")
