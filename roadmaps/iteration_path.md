# Iteration Learning Path

Covers generators, iterators, and the iteration protocol — a cluster
that appears in nearly every senior Python interview.

**Estimated total time:** 3–4 sessions of 30 minutes each.

---

## The Path

```
Generators & yield
       ↓
yield from
       ↓
Generator Expressions
       ↓
Iterables vs Iterators
       ↓
Comprehensions
```

---

## Step 1 — Generators & `yield`

Lazy evaluation, generator objects, and `next()`.

→ [Topic](../domains/advanced_syntax/generators.md)  
→ [Drill](../drills/iterators_generators.py)  
→ [Code Reading M6](../code_reading/medium.md)  
→ [Code Reading M10](../code_reading/medium.md)

**You're ready for Step 2 when:** you can explain why
`list(g); list(g)` prints `[1, 2, 3]` then `[]`.

---

## Step 2 — Generator Expressions

The lazy alternative to list comprehensions.

→ [Topic](../domains/advanced_syntax/generator_expressions.md)  
→ [Drill](../drills/iterators_generators.py)

**You're ready for Step 3 when:** you can explain the memory
difference between `[x*2 for x in range(1000)]` and
`(x*2 for x in range(1000))`.

---

## Step 3 — Comprehensions

List, dict, set comprehensions and their scope rules.

→ [Topic](../domains/advanced_syntax/comprehensions.md)  
→ [Code Reading M8](../code_reading/medium.md)

**You're ready for Step 4 when:** you can explain why the walrus
operator leaks out of a comprehension but the loop variable doesn't.

---

## After this path

→ [Functional Python Path](functional_python_path.md)  
→ [OOP Internals Path](oop_internals_path.md)
