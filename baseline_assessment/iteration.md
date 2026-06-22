# Iteration Assessment

---

## Iterable

**Self-rating:** __ / 5

**Interview question:**
"What is the difference between an iterable and an iterator?"

Key points: iterable implements `__iter__` (returns an iterator);
iterator implements `__iter__` and `__next__`; calling `iter()` on
an iterable gives a fresh iterator each time; calling `iter()` on an
iterator returns itself.

**Code reading:**

```python
nums = [1, 2, 3]

iter1 = iter(nums)
iter2 = iter(nums)

print(next(iter1))
print(next(iter1))
print(next(iter2))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
1
2
1
```

`iter(nums)` creates a new, independent iterator each time. `iter1`
and `iter2` have separate positions. Advancing `iter1` does not
affect `iter2`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Iterator

**Self-rating:** __ / 5

**Interview question:**
"What protocol does an iterator implement? What happens when you
call `iter()` on an already-exhausted iterator?"

Key points: must implement `__iter__` (returns self) and `__next__`
(raises `StopIteration` when done); `for` loops call both; once
exhausted, calling `iter()` on it returns the same exhausted object;
the second `for` loop produces nothing.

**Code reading:**

```python
it = iter([10, 20, 30])

print(next(it))
for val in it:
    print(val)
for val in it:
    print("again:", val)
print("done")
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
10
20
30
done
```

`next(it)` consumes `10`. The first `for` loop consumes `20` and
`30`. The second `for` loop gets nothing — the iterator is exhausted.
`"again:"` never prints.

</details>

**Assessment:** Strong / Medium / Weak

---

## next() with default

**Self-rating:** __ / 5

**Interview question:**
"What does `next(iterator, default)` do? When would you use it?"

Key points: returns `default` instead of raising `StopIteration`
when the iterator is exhausted; avoids try/except for single-item
consumption; common in parsing and streaming.

**Code reading:**

```python
it = iter([1, 2])

print(next(it))
print(next(it))
print(next(it, "end"))
print(next(it, "end"))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
1
2
end
end
```

After consuming `1` and `2`, the iterator is exhausted. Subsequent
`next()` calls with a default return `"end"` without raising.

</details>

**Assessment:** Strong / Medium / Weak

---

## Generator

**Self-rating:** __ / 5

**Interview question:**
"What is a generator function? How is calling it different from
calling a regular function?"

Key points: a function with `yield`; calling it returns a generator
object without executing the body; the body runs lazily, suspending
at each `yield`; generators implement the iterator protocol;
exhausted after one pass.

**Code reading:**

```python
def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen()
print("created")
print(next(g))
print(next(g))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
created
start
1
middle
2
```

`gen()` returns the generator object without running any code.
`"created"` prints first. Each `next()` resumes execution until the
next `yield`, printing the intermediate messages along the way.

</details>

**Assessment:** Strong / Medium / Weak

---

## yield

**Self-rating:** __ / 5

**Interview question:**
"What is `yield` and how does it differ from `return`?"

Key points: `yield` suspends the function and emits a value; the
function can resume from where it left off; `return` in a generator
raises `StopIteration`; `yield` is also an expression — `.send(val)`
makes `yield` evaluate to `val`.

**Code reading:**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(3):
    print(val)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
3
2
1
```

Each `yield n` suspends and emits the current value. The `for` loop
resumes the generator after each yield. When `n` reaches `0`, the
while loop ends and `StopIteration` is raised, stopping the loop.

</details>

**Assessment:** Strong / Medium / Weak

---

## yield from

**Self-rating:** __ / 5

**Interview question:**
"What does `yield from` do? Why is it better than looping with
`yield`?"

Key points: delegates to a sub-generator or iterable; transparently
forwards values, `send()`, `throw()`, and `StopIteration.value`;
avoids the boilerplate `for x in sub: yield x`; essential for
composing generators.

**Code reading:**

```python
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2], [3, 4], [5]))
print(result)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
[1, 2, 3, 4, 5]
```

`yield from it` yields every item from `it` in order. `chain` works
on any iterable, not just lists.

</details>

**Assessment:** Strong / Medium / Weak
