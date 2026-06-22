# Code Reading — Hard

Deep internals, metaclasses, descriptor protocol, and compound traps.
If you can answer these cold, your Python internals knowledge is solid.

---

## Puzzle H1 — Descriptor protocol

**Topic:** oop / descriptors  
**Trap:** data descriptors define `__set__` and take priority over
instance `__dict__`

```python
class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be non-negative")
        obj.__dict__[self.name] = value

class Temperature:
    celsius = Validator()

t = Temperature()
t.celsius = 25
t.__dict__['celsius'] = -100  # bypassing the descriptor?
print(t.celsius)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
-100
```

`Validator` defines `__set__`, making it a data descriptor. Data
descriptors take priority over instance `__dict__` when accessed via
the attribute protocol (`t.celsius`). However, directly writing to
`obj.__dict__` bypasses the descriptor's `__set__`. When `__get__` is
called, it looks in `obj.__dict__` directly and reads the bypassed
value.

The lesson: direct `__dict__` writes can circumvent data descriptors
if the `__get__` implementation reads `__dict__` itself.

</details>

---

## Puzzle H2 — Metaclass `__call__`

**Topic:** oop / metaclasses  
**Trap:** `type.__call__` triggers `__new__` and `__init__` — overriding
it changes instance creation

```python
class Meta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Meta.__call__ for {cls.__name__}")
        instance = cls.__new__(cls, *args, **kwargs)
        if isinstance(instance, cls):
            instance.__init__(*args, **kwargs)
        return instance

class MyClass(metaclass=Meta):
    def __init__(self, x):
        self.x = x
        print(f"__init__ x={x}")

obj = MyClass(42)
print(obj.x)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
Meta.__call__ for MyClass
__init__ x=42
42
```

`MyClass(42)` is a call on the *class* — which is an instance of
`Meta`. So `Meta.__call__` is triggered first. Inside it, we manually
call `__new__` then `__init__`.

</details>

---

## Puzzle H3 — Class variable vs instance variable shadowing

**Topic:** oop / dunder_methods  
**Trap:** assigning to `self.x` creates an instance variable that
shadows the class variable

```python
class Counter:
    count = 0

    def increment(self):
        self.count += 1

a = Counter()
b = Counter()

a.increment()
a.increment()
b.increment()

print(Counter.count)
print(a.count)
print(b.count)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
0
2
1
```

`self.count += 1` expands to `self.count = self.count + 1`. The right
side reads `Counter.count` (0), then the assignment creates an instance
variable `self.count = 1`, shadowing the class variable. The class
variable `Counter.count` is never modified.

</details>

---

## Puzzle H4 — `__slots__` and inheritance

**Topic:** oop / slots  
**Trap:** `__slots__` only prevents `__dict__` in the class that defines
it — subclasses get `__dict__` back unless they also define `__slots__`

```python
class Base:
    __slots__ = ('x',)

class Child(Base):
    pass

c = Child()
c.x = 1
c.y = 2  # will this work?
print(hasattr(c, '__dict__'))
print(c.y)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
True
2
```

`Child` doesn't define `__slots__`, so it inherits normally and gets
`__dict__`. The `__slots__ = ('x',)` from `Base` still creates a slot
for `x`, but `Child` can also have arbitrary attributes via its own
`__dict__`.

</details>

---

## Puzzle H5 — Generator `send()` and `yield` expression

**Topic:** advanced_syntax / generators  
**Trap:** `yield` is an expression; the value sent via `.send()` becomes
the result of that expression

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)          # prime the generator
print(gen.send(10))
print(gen.send(20))
print(gen.send(5))
```

**What does this print?**

<details>
<summary>Answer</summary>

```
10
30
35
```

`next(gen)` runs until the first `yield total` (yields `0`, which we
discard). Each `send(v)` resumes the generator with `value = v`, adds
to total, loops back, and yields the new total.

</details>

---

## Puzzle H6 — `__init_subclass__`

**Topic:** oop / metaclasses  
**Trap:** `__init_subclass__` fires on the *parent* when a *child* is
defined — runs at class definition time, not instantiation time

```python
class Plugin:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry.append(cls.__name__)

class Alpha(Plugin):
    pass

class Beta(Plugin):
    pass

print(Plugin.registry)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
['Alpha', 'Beta']
```

`__init_subclass__` is a hook that fires on `Plugin` whenever a
subclass is defined. It's a clean way to implement auto-registration
without metaclasses.

</details>

---

## Puzzle H7 — Compound closure + mutable default

**Topic:** functional_python / closures  
**Trap:** two traps compounding — mutable default + late binding

```python
def make_adders(n, cache=[]):
    for i in range(n):
        cache.append(lambda x: x + i)
    return cache

adders1 = make_adders(3)
adders2 = make_adders(2)

print(len(adders1))
print(adders1[0](10))
print(adders2[0](10))
```

**What does this print?**

<details>
<summary>Answer</summary>

```
5
11
11
```

First trap: `cache=[]` is shared across all calls (mutable default).
After two calls, `cache` has 5 lambdas (3 + 2).

Second trap: all lambdas close over `i`. After `make_adders(2)`,
`i == 1`. Every lambda — including those from the first call — now
returns `x + 1`.

`adders1[0](10)` → `10 + 1 = 11`. `adders2[0](10)` → same.

</details>

---

## Puzzle H8 — `__getattr__` vs `__getattribute__`

**Topic:** oop / dunder_methods, python_internals / data_model  
**Trap:** `__getattribute__` intercepts *every* attribute access;
`__getattr__` is only called when normal lookup fails

```python
class Tricky:
    def __init__(self):
        self.x = 10

    def __getattr__(self, name):
        return f"missing: {name}"

    def __getattribute__(self, name):
        if name == 'x':
            return 99
        return super().__getattribute__(name)

t = Tricky()
print(t.x)
print(t.y)
print(t.z)
```

**What does this print?**

<details>
<summary>Answer</summary>

```
99
missing: y
missing: z
```

`t.x` triggers `__getattribute__`, which intercepts and returns `99`
(ignoring `self.__dict__['x'] = 10`). `t.y` and `t.z` go through
`__getattribute__` → falls through to `super()` → not found →
`__getattr__` is called.

</details>
