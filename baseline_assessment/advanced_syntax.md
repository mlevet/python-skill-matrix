# Advanced Syntax Assessment

---

## Positional-Only Arguments

**Self-rating:** __ / 5

**Interview question:**
"What does `/` in a function signature mean? Why would you make
an argument positional-only?"

Key points: `/` in the parameter list separates positional-only
parameters (to the left) from the rest; callers cannot pass them
as keyword arguments; useful for API design when the parameter
name is an implementation detail or when matching C extension
signatures.

**Code reading:**

```python
def greet(name, /, greeting="hello"):
    return f"{greeting}, {name}"

print(greet("Alice"))
print(greet("Bob", greeting="hi"))
try:
    print(greet(name="Carol"))
except TypeError as e:
    print(f"Error: {e}")
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
hello, Alice
hi, Bob
Error: greet() got some positional-only arguments passed as keyword arguments: 'name'
```

`name` is positional-only (left of `/`). `greeting` can be passed
positionally or as a keyword. Passing `name="Carol"` as a keyword
argument raises `TypeError`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Keyword-Only Arguments

**Self-rating:** __ / 5

**Interview question:**
"What does `*` in a function signature mean? When would you make
an argument keyword-only?"

Key points: `*` forces all arguments after it to be keyword-only;
keyword-only arguments improve call-site readability; they prevent
accidental positional misuse; common in public APIs (`sorted(key=...)`,
`print(end=...)`).

**Code reading:**

```python
def create_user(name, *, role="user", active=True):
    return {"name": name, "role": role, "active": active}

print(create_user("Alice"))
print(create_user("Bob", role="admin"))
try:
    print(create_user("Carol", "admin"))
except TypeError as e:
    print(f"Error: {e}")
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
{'name': 'Alice', 'role': 'user', 'active': True}
{'name': 'Bob', 'role': 'admin', 'active': True}
Error: create_user() takes 1 positional argument but 2 were given
```

`role` and `active` are keyword-only (after `*`). Passing `"admin"`
as a positional argument raises `TypeError`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Walrus Operator

**Self-rating:** __ / 5

**Interview question:**
"What does the walrus operator `:=` do? What scoping behavior
makes it different from regular assignment?"

Key points: assigns and returns a value in a single expression;
useful in `while` loops and comprehension filters; unlike regular
assignment in a comprehension, walrus leaks the variable into the
enclosing scope; loop variable in comprehensions does not leak.

**Code reading:**

```python
data = [1, 3, 7, 2, 8, 4]

filtered = [y for x in data if (y := x * 2) > 6]
print(filtered)
print(y)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
[14, 16, 8]
8
```

For each `x` in `[1, 3, 7, 2, 8, 4]`, `y = x * 2`:
- x=1: y=2, 2>6 False, skip
- x=3: y=6, 6>6 False, skip
- x=7: y=14, 14>6 True, include
- x=2: y=4, 4>6 False, skip
- x=8: y=16, 16>6 True, include
- x=4: y=8, 8>6 True, include

`y` leaks into the enclosing scope. Its final value is `8` (last
walrus assignment, regardless of the filter result).

</details>

**Assessment:** Strong / Medium / Weak

---

## Star Unpacking

**Self-rating:** __ / 5

**Interview question:**
"What does `*` do in an assignment? What type does the starred
variable always produce?"

Key points: collects zero or more items into a list (always a list,
even if the source is a tuple); can appear at the beginning, middle,
or end; only one starred variable per assignment; also used in
function calls to unpack iterables.

**Code reading:**

```python
first, *middle, last = range(6)

print(first)
print(middle)
print(last)
print(type(middle))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
0
[1, 2, 3, 4]
5
<class 'list'>
```

`range(6)` produces `0, 1, 2, 3, 4, 5`. `first=0`, `last=5`, and
`middle` collects everything in between as a list.

</details>

**Assessment:** Strong / Medium / Weak

---

## Generator Expressions

**Self-rating:** __ / 5

**Interview question:**
"What is the difference between a list comprehension and a generator
expression? When would you choose one over the other?"

Key points: list comprehension: `[...]` — computes all values
immediately, stores them in memory; generator expression: `(...)` —
lazy, yields one value at a time; generators are better for large
sequences when you only need to iterate once; lists are better when
you need random access or multiple iterations.

**Code reading:**

```python
gen = (x ** 2 for x in range(5))

print(type(gen))
print(next(gen))
print(sum(gen))
print(sum(gen))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
<class 'generator'>
0
30
0
```

`next(gen)` consumes `0² = 0`. `sum(gen)` consumes the rest:
`1 + 4 + 9 + 16 = 30`. The second `sum(gen)` gets an exhausted
generator and returns `0`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Pattern Matching

**Self-rating:** __ / 5

**Interview question:**
"What is `match/case`? How is it different from a chain of
`if/elif`?"

Key points: structural pattern matching (Python 3.10+); matches
against patterns, not just values; can destructure sequences, dicts,
class instances; `case _` is the wildcard (default); can use guards
(`if condition`); does not fall through like C's `switch`.

**Code reading:**

```python
def describe(val):
    match val:
        case []:
            return "empty list"
        case [x]:
            return f"one item: {x}"
        case [x, y]:
            return f"two items: {x}, {y}"
        case list():
            return "longer list"
        case _:
            return "not a list"

print(describe([]))
print(describe([1]))
print(describe([1, 2]))
print(describe([1, 2, 3]))
print(describe("hello"))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
empty list
one item: 1
two items: 1, 2
longer list
not a list
```

Each `case` is tried in order. `[x]` matches any one-element list
and binds `x`. `list()` matches any list (longer than already
matched). `_` is the fallback for anything that didn't match.

</details>

**Assessment:** Strong / Medium / Weak
