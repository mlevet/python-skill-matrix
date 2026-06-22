# Runtime Behavior Assessment

---

## References

**Self-rating:** __ / 5

**Interview question:**
"In Python, what is the difference between a variable and an object?
What does assignment actually do?"

Key points: assignment binds a name to an object, not a copy; the
object exists independently; multiple names can point to the same
object; reassigning a name doesn't affect other names pointing to
the same object; mutation does affect all names.

**Code reading:**

```python
a = [1, 2, 3]
b = a

a.append(4)
print(b)

a = [99, 100]
print(b)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
[1, 2, 3, 4]
[1, 2, 3, 4]
```

`b = a` makes `b` point to the same list. `a.append(4)` mutates the
shared list, so `b` sees the change. Reassigning `a = [99, 100]`
rebinds `a` to a new list but does not affect `b`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Identity vs Equality

**Self-rating:** __ / 5

**Interview question:**
"What is the difference between `is` and `==`? When is `is` the
right choice?"

Key points: `is` checks identity (same object in memory); `==` calls
`__eq__` (same value); only use `is` for `None`, `True`, `False`;
CPython caches small integers (-5 to 256) and interned strings —
don't rely on this; `is not None` is idiomatic, `!= None` is not.

**Code reading:**

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)
print(x is y)
print(x is z)
print(x == z)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
True
False
True
True
```

`x` and `y` have equal values but are different objects.
`z = x` makes `z` an alias for `x` — same object, same value.

</details>

**Assessment:** Strong / Medium / Weak

---

## Mutability

**Self-rating:** __ / 5

**Interview question:**
"What types are mutable in Python, and what types are immutable?
Why does mutability matter for function arguments?"

Key points: mutable: list, dict, set, most custom objects; immutable:
int, float, str, tuple, frozenset, bytes; function arguments pass
references; mutating a mutable argument inside the function affects
the caller's object; reassigning the parameter doesn't.

**Code reading:**

```python
def process(items, flag):
    items.append(99)
    flag = True

my_list = [1, 2, 3]
my_flag = False

process(my_list, my_flag)
print(my_list)
print(my_flag)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
[1, 2, 3, 99]
False
```

`items.append(99)` mutates the shared list object — the caller sees
the change. `flag = True` only rebinds the local parameter; `my_flag`
in the caller is unaffected.

</details>

**Assessment:** Strong / Medium / Weak

---

## Mutable Defaults

**Self-rating:** __ / 5

**Interview question:**
"What is the mutable default argument trap? Why does it happen and
how do you fix it?"

Key points: default argument values are evaluated once at function
definition, not at each call; a mutable default (like `[]`) is shared
across all calls; fix: use `None` as the default and initialize
inside the function.

**Code reading:**

```python
def append_to(val, lst=[]):
    lst.append(val)
    return lst

print(append_to(1))
print(append_to(2))
print(append_to(3, []))
print(append_to(4))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
[1]
[1, 2]
[3]
[1, 2, 4]
```

`append_to(3, [])` uses a fresh list, so it returns `[3]`. But the
default list still has `[1, 2]` from before, and the next call
without an explicit list adds to it.

</details>

**Assessment:** Strong / Medium / Weak

---

## copy vs deepcopy

**Self-rating:** __ / 5

**Interview question:**
"What is the difference between `copy.copy()` and `copy.deepcopy()`?"

Key points: `copy.copy()` creates a shallow copy — the outer
container is new but inner objects are still shared; `copy.deepcopy()`
recursively copies all nested objects; `deepcopy` is slower and
uses more memory but fully independent.

**Code reading:**

```python
import copy

original = [[1, 2], [3, 4]]
shallow  = copy.copy(original)
deep     = copy.deepcopy(original)

original[0].append(99)

print(shallow[0])
print(deep[0])
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
[1, 2, 99]
[1, 2]
```

The shallow copy shares the inner lists with `original`. Mutating
`original[0]` is visible in `shallow[0]`. The deep copy has its own
independent inner lists.

</details>

**Assessment:** Strong / Medium / Weak

---

## Garbage Collection

**Self-rating:** __ / 5

**Interview question:**
"How does Python's garbage collection work? What is reference
counting, and when is the cyclic GC needed?"

Key points: primary mechanism is reference counting — each object
tracks how many names point to it; when count reaches 0, the object
is immediately freed; cyclic GC (`gc` module) handles reference
cycles (A → B → A) which refcounting can't free; `__del__` is called
when an object is garbage collected.

**Code reading:**

```python
import sys

a = [1, 2, 3]
b = a
c = a

print(sys.getrefcount(a))

del b
print(sys.getrefcount(a))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
4
3
```

`getrefcount` temporarily adds one reference (the argument itself).
`a`, `b`, `c`, and the `getrefcount` call: 4 total. After `del b`:
`a`, `c`, and the argument: 3.

</details>

**Assessment:** Strong / Medium / Weak

---

## GIL

**Self-rating:** __ / 5

**Interview question:**
"What is the GIL? How does it affect CPU-bound vs I/O-bound
multithreading?"

Key points: Global Interpreter Lock — a mutex that prevents multiple
threads from executing Python bytecode simultaneously; I/O-bound
threads release the GIL while waiting, so threading works well for
I/O; CPU-bound work is serialized — use `multiprocessing` instead;
GIL is CPython-specific.

**Code reading:**

```python
# No code reading for GIL — conceptual question only.
# Answer verbally: "If I have a CPU-bound task like image processing,
# should I use threading or multiprocessing, and why?"
```

Good answer: multiprocessing, because each process has its own
interpreter and GIL. Threading won't parallelize CPU-bound work.

**Assessment:** Strong / Medium / Weak
