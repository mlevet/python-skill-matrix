---
topic: LEGB Scoping Rules
domain: python_internals
confidence: 0
last_reviewed: never
interview_freq: high
---

# LEGB Scoping Rules

## Summary

Python resolves variable names by searching four nested scopes in order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in. Understanding this eliminates a whole class of `NameError` and `UnboundLocalError` surprises.

---

## Key concepts

- **Local:** inside the current function.
- **Enclosing:** in any enclosing function scopes (for closures). Searched inside-out.
- **Global:** module-level names (`global` keyword to write, not just read).
- **Built-in:** Python's built-ins (`len`, `print`, `True`, etc.).
- `global x` declares that `x` refers to the module-level variable.
- `nonlocal x` declares that `x` refers to the nearest enclosing non-global scope.

---

## Code examples

### The four scopes

```python
x = "global"           # Global

def outer():
    x = "enclosing"    # Enclosing (for inner)

    def inner():
        x = "local"    # Local
        print(x)       # local

    inner()
    print(x)           # enclosing

outer()
print(x)               # global
```

### Read vs write

```python
x = 10

def f():
    print(x)   # reads global — works

def g():
    print(x)   # UnboundLocalError! Python sees the assignment below
    x = 5      # assignment makes x LOCAL for the entire function scope
```

### `global` keyword

```python
count = 0

def increment():
    global count
    count += 1   # modifies the global

increment()
print(count)   # 1
```

### `nonlocal` keyword

```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)   # 1

outer()
```

### Comprehension scope (Python 3)

```python
x = 10
result = [x for x in range(5)]   # comprehension has its own scope
print(x)   # 10  ← not 4!  comprehension doesn't leak its loop variable

# Walrus DOES leak:
result = [y := x * 2 for x in range(3)]
print(y)   # 4  ← leaked
```

---

## Common traps

- **`UnboundLocalError`:** any assignment to a name inside a function makes it local for the *entire* function — even before the assignment. Reading it before assignment raises `UnboundLocalError`.
- **Comprehension scope:** in Python 3, list/dict/set comprehensions have their own scope (unlike Python 2 where they leaked). Generator expressions always had their own scope.
- **Shadowing builtins:** `list = [1,2,3]` shadows the built-in `list`. Dangerous.
- **Walrus leaks from comprehensions:** unlike regular comprehension loop variables, `:=` does leak into the enclosing scope.

---

## Interview angle

- "What is LEGB?" → Local, Enclosing, Global, Built-in — the name lookup order
- "Why does this raise `UnboundLocalError`?" → any assignment makes the variable local for the whole function
- "What does `nonlocal` do vs `global`?" → `nonlocal` targets the nearest enclosing non-global; `global` targets module level

---

## Linked drill

No dedicated drill yet — see `drills/closures.py` exercises 4 and 5 for `nonlocal`.

---

## Linked code-reading puzzles

- `code_reading/easy.md` — Puzzle E4 (loop variable scope)
- `code_reading/medium.md` — Puzzle M8 (walrus in comprehension)

---

## Review notes

