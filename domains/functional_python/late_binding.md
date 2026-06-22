# Late Binding

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

Late binding means that closures look up the value of a variable at call time, not at the time the function was defined. When multiple closures are created in a loop over the same variable, they all share that single variable and will all read its final value when called.

## Mental model

The closure stores a pointer to the variable, not a snapshot of its value. When you call the function, it follows the pointer and reads whatever the variable holds at that moment.

```python
# The closure holds a pointer to 'i'
# When called, it reads i's current value
funcs = [lambda: i for i in range(5)]
```

By the time any of these lambdas is called, the loop has finished and `i` is `4`. All five functions follow the same pointer and see the same value.

## Why interviewers ask this

This is one of the most common "what does this print?" traps in Python interviews. It appears in questions involving lambdas in loops, list comprehensions with closures, and dictionary-based dispatch. Knowing the fix signals real-world Python experience.

## Common traps

- Closures capture the name, not the current value. The lookup happens at call time.
- The loop variable is a single shared variable, not a new variable per iteration.
- The fix using `i=i` looks like a default argument but is actually forcing eager evaluation.
- `functools.partial` also avoids late binding because it binds argument values at creation time.

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

All three lambdas close over the same variable `i`. By the time they are called, the loop has ended and `i == 2`. Each lambda computes `2 * 2 = 4`.

### Fix

```python
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i * 2)

print([f() for f in funcs])  # [0, 2, 4]
```

The default argument `i=i` is evaluated immediately when the lambda is created, capturing the current value of `i` rather than a reference to the variable.

## Related topics

- Closures
- Lambda functions
- functools.partial
