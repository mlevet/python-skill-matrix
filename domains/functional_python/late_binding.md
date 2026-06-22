# Late Binding

---
**Path:** [Functional Python](../../roadmaps/functional_python_path.md) — Step 5 of 8  
**Prev:** [Closures](closures.md) · **Next:** [Decorators](decorators.md)  
**Drill:** [drills/closures.py](../../drills/closures.py)  
**Code Reading:** [M1 — Classic trap](../../code_reading/medium.md) · [M2 — partial fix](../../code_reading/medium.md)  
**Hall of Pain:** [Lambda late binding](../../hall_of_pain.md)

---

## Metadata

| Field | Value |
|---|---|
| Domain | Functional Python |
| Mastery | 5/10 |
| Freshness | Stale |
| Interview Frequency | High |
| Last Reviewed | TBD |
| Next Review | TBD |

## 30-second explanation

Late binding means closures look up the value of a captured variable at
call time, not at definition time. When multiple closures close over the
same loop variable, they all see its final value when called — because
they all hold a reference to the same variable, not separate snapshots.

## Mental model

The closure stores a pointer to the variable, not a copy of its value.
Calling the function follows the pointer and reads whatever the variable
holds at that moment.

```python
# All three lambdas point to the same 'i'
funcs = [lambda: i for i in range(3)]
# After the loop: i == 2
# Every lambda follows its pointer → reads 2
```

The fix forces eager evaluation by making the current value a default
argument, which is evaluated at definition time:

```python
funcs = [lambda i=i: i for i in range(3)]
# Each lambda gets its own default, frozen at creation
```

## Why interviewers ask this

Late binding is one of the most commonly asked Python gotchas. It
appears in any context where functions are created in a loop: lambdas,
`def` inside a loop, dictionary-based dispatch, and callbacks. Knowing
both the `i=i` fix and the `functools.partial` alternative — and being
able to explain why they work — is a strong signal.

## Common traps

- The trap is not specific to lambdas. A `def` inside a loop has
  exactly the same late-binding behavior.
- The loop variable is a single variable that gets reassigned each
  iteration. It is not a new variable per iteration.
- The `i=i` fix looks like it's doing nothing, but the left-hand `i`
  creates a new local variable (the default) while the right-hand `i`
  reads the current value of the outer variable.
- `functools.partial` avoids late binding because it binds argument
  values immediately at creation time — it does not create a closure
  over a name.
- Late binding also bites in class bodies and comprehensions that
  reference variables from an outer scope.

## Code-reading example

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i * 2)

print([f() for f in funcs])
```

### Answer

```
[4, 4, 4]
```

### Explanation

All three lambdas close over the same variable `i`. After the loop
ends, `i` is `2`. Each lambda computes `2 * 2 = 4` when called. The
value `i` had during earlier iterations is irrelevant — the closure
follows the pointer to whatever `i` holds now.

### Fix

```python
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i * 2)

print([f() for f in funcs])  # [0, 2, 4]
```

The default argument `i=i` captures the current value of `i` at the
moment the lambda is created. After the loop, each lambda has a
different default and no longer depends on the outer `i`.

## Related topics

- Closures
- Lambda functions
- functools.partial
