# Functional Python Learning Path

Master this cluster first. It covers 80% of advanced Python interview
questions on functions, closures, and decorators.

**Estimated total time:** 5–7 sessions of 30 minutes each.

---

## The Path

```
Functions as Objects
       ↓
Lambda Functions
       ↓
Higher-Order Functions
       ↓
Closures
       ↓
Late Binding
       ↓
Decorators
       ↓
functools.partial
       ↓
functools.lru_cache
```

---

## Step 1 — Functions as Objects

The foundation. Everything else builds on this.

→ [Topic](../domains/functional_python/functions_as_objects.md)  
→ [Drill](../drills/functions_as_objects.py)  
→ [Code Reading E10](../code_reading/easy.md)

**You're ready for Step 2 when:** you can explain why
`greet = None` doesn't affect a variable that already referenced
the function.

---

## Step 2 — Lambda Functions

Anonymous functions, limitations, and the loop trap.

→ [Topic](../domains/functional_python/lambda_functions.md)  
→ [Drill](../drills/lambdas.py)  
→ [Code Reading M1](../code_reading/medium.md)

**You're ready for Step 3 when:** you can predict the output of
`[lambda: i for i in range(3)]` and explain both fixes.

---

## Step 3 — Higher-Order Functions

`map`, `filter`, `reduce`, and composable behavior.

→ [Topic](../domains/functional_python/higher_order_functions.md)  
→ [Code Reading M2](../code_reading/medium.md)

**You're ready for Step 4 when:** you can explain when to prefer a
list comprehension over `map()` and why.

---

## Step 4 — Closures

Variable capture, cell objects, and `nonlocal`.

→ [Topic](../domains/functional_python/closures.md)  
→ [Drill](../drills/closures.py)  
→ [Code Reading M1](../code_reading/medium.md)  
→ [Code Reading H7](../code_reading/hard.md)

**You're ready for Step 5 when:** you can explain why `c1` and `c2`
from `make_counter()` have independent state.

---

## Step 5 — Late Binding

Why closures capture names, not values, and how to fix it.

→ [Topic](../domains/functional_python/late_binding.md)  
→ [Code Reading M1](../code_reading/medium.md)  
→ [Code Reading M2](../code_reading/medium.md)  
→ [Hall of Pain](../hall_of_pain.md)

**You're ready for Step 6 when:** you can describe three ways to
fix the late-binding trap and explain the mechanism behind each.

---

## Step 6 — Decorators

Wrapping functions with closures. The three-layer pattern.

→ [Topic](../domains/functional_python/decorators.md)  
→ [Drill](../drills/decorators.py)  
→ [Code Reading M3](../code_reading/medium.md)  
→ [Code Reading M9](../code_reading/medium.md)

**You're ready for Step 7 when:** you can implement `@timer` and
`@repeat(n)` from memory, using `@wraps`.

---

## Step 7 — functools.partial

Eager argument binding. The clean alternative to the `i=i` trick.

→ [Topic](../domains/functional_python/partial.md)  
→ [Code Reading M2](../code_reading/medium.md)

**You're ready for Step 8 when:** you can explain the difference
between `partial(f, i)` and `lambda: f(i)` in a loop.

---

## Step 8 — functools.lru_cache

Memoization, hashability, and the decorator mechanics.

→ [Topic](../domains/functional_python/lru_cache.md)  
→ [Drill](../drills/decorators.py)

**You've completed this path when:** you can implement a cached
Fibonacci and explain why lists can't be passed as arguments.

---

## After this path

→ [Iteration Path](iteration_path.md) — Generators & yield  
→ [OOP Internals Path](oop_internals_path.md) — `__call__`, MRO, Descriptors
