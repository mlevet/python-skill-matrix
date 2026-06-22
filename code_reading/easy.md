# Code Reading — Easy

Puzzles that test basic but tricky Python behavior. Aim to answer each before revealing the spoiler.

---

## Puzzle E1 — Mutable default argument

**Topic:** basics / functions  
**Trap:** mutable default arguments are evaluated once at function definition time

```python
def append_to(element, target=[]):
    target.append(element)
    return target

print(append_to(1))
print(append_to(2))
print(append_to(3))
```

**What does this print?**

<details>
<summary>Answer</summary>

```
[1]
[1, 2]
[1, 2, 3]
```

The default `target=[]` is created **once** when the function is defined. Every call that omits `target` shares the same list object.

**Fix:** use `None` as the default and initialize inside the function.

```python
def append_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
```

</details>

---

## Puzzle E2 — `is` vs `==`

**Topic:** basics / is_vs_eq  
**Trap:** `is` checks identity (same object), `==` checks equality (same value)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
True
False
True
```

`a` and `b` are equal in value but are two different list objects. `c` is the same object as `a`.

</details>

---

## Puzzle E3 — String interning surprise

**Topic:** basics / is_vs_eq  
**Trap:** CPython interns small integers and some strings — `is` may return `True` unexpectedly

```python
x = 256
y = 256
print(x is y)

a = 257
b = 257
print(a is b)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
True
False
```

CPython caches integers from -5 to 256. `256` reuses the same object; `257` creates new ones. This is an implementation detail — never use `is` to compare values.

</details>

---

## Puzzle E4 — `for` loop variable leaks

**Topic:** basics / scoping  
**Trap:** loop variable stays in scope after the loop ends

```python
for i in range(5):
    pass

print(i)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
4
```

In Python, `for` loop variables leak into the enclosing scope. `i` is `4` after the loop completes.

</details>

---

## Puzzle E5 — Tuple with mutable element

**Topic:** data_structures / tuple  
**Trap:** tuples are immutable containers, but the objects they hold can still be mutable

```python
t = ([1, 2], [3, 4])
t[0].append(99)
print(t)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
([1, 2, 99], [3, 4])
```

The tuple itself didn't change (you can't reassign `t[0]`), but the list object that `t[0]` points to was mutated.

</details>

---

## Puzzle E6 — `==` on empty containers

**Topic:** basics / types  
**Trap:** empty containers of different types compare equal to each other... or do they?

```python
print([] == ())
print({} == set())
print([] == False)
print(0 == False)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
False
False
False
True
```

`[]` and `()` are different types — not equal. `{}` is a dict, `set()` is a set — not equal. `[]` is falsy but not equal to `False`. `0 == False` is `True` because `bool` is a subclass of `int` and `False == 0`.

</details>

---

## Puzzle E7 — `not in` vs `!= None`

**Topic:** basics / operators  
**Trap:** operator precedence in boolean expressions

```python
x = None
print(x is not None)
print(x != None)

y = float('nan')
print(y == y)
print(y != y)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
False
False
False
True
```

`float('nan')` is the only Python value that is not equal to itself — this follows the IEEE 754 standard. `nan != nan` is `True`.

</details>

---

## Puzzle E8 — `*` in assignment

**Topic:** advanced_syntax / unpacking  
**Trap:** starred assignment captures a list, not a tuple

```python
first, *rest = [1, 2, 3, 4, 5]
print(type(rest))
print(rest)

*init, last = [1, 2, 3, 4, 5]
print(init)
print(last)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
<class 'list'>
[2, 3, 4, 5]
[1, 2, 3, 4]
5
```

The starred variable always gets a `list`, even if the source is a tuple.

</details>

---

## Puzzle E9 — List multiplication with nested lists

**Topic:** data_structures / list  
**Trap:** `[[]] * n` creates `n` references to the same inner list — not `n` independent lists

```python
matrix = [[0] * 3] * 3
matrix[0][1] = 99
print(matrix)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
[[0, 99, 0], [0, 99, 0], [0, 99, 0]]
```

`[[0] * 3] * 3` creates one inner list and three references to it. Mutating through any reference mutates all three.

**Fix:**
```python
matrix = [[0] * 3 for _ in range(3)]
matrix[0][1] = 99
print(matrix)  # [[0, 99, 0], [0, 0, 0], [0, 0, 0]]
```

The comprehension creates three distinct inner lists.

</details>

---

## Puzzle E10 — Function assignment

**Topic:** functional_python / functions_as_objects  
**Trap:** assigning a function to a variable creates a second reference — the original name still works independently

```python
def say(msg):
    return msg.upper()

shout = say
say = lambda msg: msg.lower()

print(shout("hello"))
print(say("hello"))
print(shout is say)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
HELLO
hello
False
```

`shout` still holds the original function object. Reassigning `say` to a lambda doesn't affect `shout` — they were pointing to the same object, but rebinding `say` only changes what `say` points to.

</details>

---

## Puzzle E11 — `+=` vs `+` on lists

**Topic:** data_structures / list  
**Trap:** `+=` mutates in place; `+` creates a new object

```python
a = [1, 2, 3]
b = a
a += [4, 5]
print(b)

x = [1, 2, 3]
y = x
x = x + [4, 5]
print(y)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
[1, 2, 3, 4, 5]
[1, 2, 3]
```

`a += [4, 5]` calls `a.__iadd__([4, 5])` — mutates the list in place. `b` still points to the same list, so it sees the change. `x = x + [4, 5]` creates a new list and rebinds `x` to it. `y` still points to the original unchanged list.

</details>
