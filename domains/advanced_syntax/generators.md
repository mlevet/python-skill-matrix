---
topic: Generators & yield
domain: advanced_syntax
confidence: 0
last_reviewed: never
interview_freq: high
---

# Generators & `yield`

## Summary

A generator is a function that uses `yield` to produce values lazily — one at a time, on demand. Unlike a list comprehension, a generator expression doesn't compute all values upfront. Generators implement the iterator protocol automatically.

---

## Key concepts

- A function with `yield` returns a generator object when called — it does not execute the body immediately.
- `next(gen)` resumes execution until the next `yield`, then suspends again.
- `StopIteration` is raised when the function returns (or falls off the end).
- `yield from iterable` delegates to another iterable — equivalent to `for x in iterable: yield x` but more efficient.
- `gen.send(value)` resumes the generator and sets the result of the `yield` expression to `value`. Requires the generator to be primed with `next()` first.
- `gen.throw(ExcType)` injects an exception at the suspension point.
- Generators are single-pass — once exhausted, they return `[]` (or nothing) forever.

---

## Code examples

### Basic generator

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))   # 3
print(next(gen))   # 2
print(next(gen))   # 1
# next(gen) would raise StopIteration
```

### Generator expression

```python
squares = (x ** 2 for x in range(10))   # generator — lazy
squares_list = [x ** 2 for x in range(10)]  # list — eager

import sys
print(sys.getsizeof(squares))       # ~200 bytes
print(sys.getsizeof(squares_list))  # much larger
```

### `yield from`

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], 5])))   # [1, 2, 3, 4, 5]
```

### Two-way communication with `.send()`

```python
def accumulator():
    total = 0
    while True:
        value = yield total   # sends total out, receives value in
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)           # prime the generator (run to first yield)
print(gen.send(10)) # 10
print(gen.send(5))  # 15
```

### Generators are exhaustible

```python
gen = (x for x in range(3))
print(list(gen))   # [0, 1, 2]
print(list(gen))   # []  ← already exhausted
```

---

## Common traps

- **Not priming before `.send()`:** the first call must be `next(gen)` (or `gen.send(None)`) to advance to the first `yield`. Calling `gen.send(value)` before priming raises `TypeError`.
- **Generator exhaustion:** iterating a generator twice only works the first time. If you need to iterate multiple times, either use a list or recreate the generator.
- **`yield` vs `return`:** in a generator, `return value` sets the value of `StopIteration` — not a `yield`. In `yield from`, the return value is accessible via `StopIteration.value`.
- **Execution is deferred:** the function body doesn't run at all until `next()` is called. Side effects (like `print()`) don't happen at generator creation.

---

## Interview angle

- "What is a generator and when would you use one?" → lazy evaluation, large datasets, infinite sequences
- "What does `yield from` do?" → delegates to an inner iterable, more efficient than a loop
- "What is the difference between a generator function and a generator expression?"
- "What does `.send()` do?" → resumes the generator and injects a value as the result of `yield`

---

## Linked drill

`drills/iterators_generators.py` — all exercises

---

## Linked code-reading puzzles

- `code_reading/medium.md` — Puzzle M6 (exhausted generator)
- `code_reading/hard.md` — Puzzle H5 (`.send()`)

---

## Review notes

