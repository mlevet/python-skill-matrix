---
topic: Inheritance & MRO (C3 linearization)
domain: oop
confidence: 0
last_reviewed: never
interview_freq: high
---

# Inheritance & MRO (C3 Linearization)

## Summary

Python uses the C3 linearization algorithm to determine Method Resolution Order (MRO) — the order in which classes are searched when resolving an attribute or method. `super()` follows MRO, not the literal class hierarchy, which enables cooperative multiple inheritance.

---

## Key concepts

- `ClassName.__mro__` shows the resolution order as a tuple.
- `super()` calls the next class in MRO, not necessarily the direct parent.
- Cooperative multiple inheritance requires all classes in the hierarchy to call `super()`.
- Diamond problem: Python solves it cleanly via C3 — `Base` appears only once, at the end.
- C3 rule (simplified): a class always appears after its parents, and parents appear in the order listed.

---

## Code examples

### Basic MRO

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### Method resolution

```python
class A:
    def who(self): return "A"

class B(A):
    def who(self): return "B"

class C(A):
    def who(self): return "C"

class D(B, C): pass

print(D().who())   # B  ← first match in MRO: D → B → C → A
```

### Cooperative super()

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("Woof")
        super().speak()

class Robot(Animal):
    def speak(self):
        print("Beep")
        super().speak()

class RobotDog(Dog, Robot):
    def speak(self):
        print("RobotDog")
        super().speak()

RobotDog().speak()
# RobotDog
# Woof
# Beep
# ...
# MRO: RobotDog → Dog → Robot → Animal
```

### Calling super with explicit args (Python 2 style — avoid in Python 3)

```python
# Python 3: super() is enough
# Python 2: super(ClassName, self).method()
```

### Getting MRO programmatically

```python
print([c.__name__ for c in D.__mro__])   # ['D', 'B', 'C', 'A', 'object']
```

---

## Common traps

- **`super()` in non-cooperative hierarchy:** if `C(A)` doesn't call `super()`, then in a diamond `D(B, C)`, `B`'s `super()` call goes to `C` (per MRO), but `C` swallows the chain — `A` is never called.
- **Linearization failure:** Python raises `TypeError` if no consistent MRO can be computed (e.g., `class X(A, B)` where `B` is a subclass of `A` but `A` is listed first — breaks C3).
- **`super()` returns a proxy, not a class:** `super().method()` doesn't mean "call A.method" — it means "call the method from the next class in MRO of the actual instance's type."

---

## Interview angle

- "What is MRO and why does Python use it?" → C3 solves the diamond problem deterministically
- "What does `super()` actually call?" → next class in MRO of the runtime type
- "What order do these methods print in?" → trace MRO manually

Steps to trace MRO manually:
1. List the class and its bases in definition order.
2. Merge by taking the first element of each list that doesn't appear in the tail of any other list.

---

## Linked drill

`drills/oop_internals.py` — Exercises 2, 3

---

## Linked code-reading puzzles

- `code_reading/medium.md` — Puzzle M5 (MRO and super)

---

## Review notes

