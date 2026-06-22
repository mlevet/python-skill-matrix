# OOP Internals Assessment

---

## Classes Are Objects

**Self-rating:** __ / 5

**Interview question:**
"In Python, what is a class? What is `type` and what is its
relationship to classes?"

Key points: a class is an instance of `type`; `type` is the default
metaclass; `type(MyClass)` returns `<class 'type'>`; classes are
created at class definition time, not at instantiation; class body
is executed immediately.

**Code reading:**

```python
class Animal:
    species = "unknown"

Dog = type("Dog", (Animal,), {"species": "Canis lupus"})

print(Dog.species)
print(isinstance(Dog, type))
print(issubclass(Dog, Animal))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
Canis lupus
True
True
```

`Dog` is created dynamically with `type(name, bases, dict)`.
`isinstance(Dog, type)` is `True` because every class is an instance
of `type`. `issubclass(Dog, Animal)` is `True` because `(Animal,)`
was passed as the bases tuple.

</details>

**Assessment:** Strong / Medium / Weak

---

## Inheritance

**Self-rating:** __ / 5

**Interview question:**
"What is the difference between a class variable and an instance
variable? What happens when you do `self.x += 1` inside a method
when `x` is a class variable?"

Key points: `self.x += 1` expands to `self.x = self.x + 1`; the
right side reads the class variable; the assignment creates an
instance variable that shadows it; the class variable is unmodified.

**Code reading:**

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

Predicted output: ___

<details>
<summary>Answer</summary>

```
0
2
1
```

Each call to `increment` creates an instance variable `self.count`
that shadows the class variable. `Counter.count` is never modified.

</details>

**Assessment:** Strong / Medium / Weak

---

## MRO

**Self-rating:** __ / 5

**Interview question:**
"What is the MRO? How does Python's C3 linearization work with
diamond inheritance?"

Key points: Method Resolution Order — the order Python searches
classes for a method; C3 ensures each class appears after all its
subclasses and preserves declaration order; `super()` follows MRO,
not the direct parent; `ClassName.__mro__` shows the full order.

**Code reading:**

```python
class A:
    def go(self): return "A"

class B(A):
    def go(self): return "B" + super().go()

class C(A):
    def go(self): return "C" + super().go()

class D(B, C):
    pass

print(D().go())
print([c.__name__ for c in D.__mro__])
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
BCA
['D', 'B', 'C', 'A', 'object']
```

MRO: D → B → C → A. `D().go()` calls `B.go()`, which calls
`super().go()` → `C.go()`, which calls `super().go()` → `A.go()`.
Results concatenate from deepest to shallowest.

</details>

**Assessment:** Strong / Medium / Weak

---

## `__call__`

**Self-rating:** __ / 5

**Interview question:**
"What is `__call__`? Give a use case where a callable instance is
preferable to a plain function."

Key points: allows an instance to be called like a function;
`callable(obj)` is `True` if the class defines `__call__`; use
cases: stateful callbacks (counters, memoizers), decorators
implemented as classes, configurable callables.

**Code reading:**

```python
class Power:
    def __init__(self, exp):
        self.exp = exp

    def __call__(self, base):
        return base ** self.exp

square = Power(2)
cube = Power(3)

print(square(4))
print(cube(3))
print(callable(square))
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
16
27
True
```

`Power(2)` creates an instance with `exp=2`. Calling `square(4)`
invokes `__call__` with `base=4`. `callable` returns `True` because
the class defines `__call__`.

</details>

**Assessment:** Strong / Medium / Weak

---

## Properties

**Self-rating:** __ / 5

**Interview question:**
"What does `@property` do? When would you use it instead of a plain
attribute?"

Key points: creates a computed attribute accessed via dot notation;
avoids breaking the public interface when adding validation or
computation later; `@prop.setter` enables assignment interception;
without a setter, assignment raises `AttributeError`.

**Code reading:**

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

t = Temperature(0)
print(t.fahrenheit)
t._celsius = 100
print(t.fahrenheit)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
32.0
212.0
```

`fahrenheit` is computed on access. Modifying `_celsius` directly
updates the underlying value; the property reflects the change on
the next access.

</details>

**Assessment:** Strong / Medium / Weak

---

## Descriptors

**Self-rating:** __ / 5

**Interview question:**
"What is a descriptor? What is the difference between a data
descriptor and a non-data descriptor?"

Key points: any object that defines `__get__`, `__set__`, or
`__delete__`; data descriptor defines `__set__` (takes priority over
instance `__dict__`); non-data descriptor only defines `__get__`
(instance `__dict__` takes priority); `@property` is a data
descriptor.

**Code reading:**

```python
class Descriptor:
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get("_val", 0)

    def __set__(self, obj, value):
        obj.__dict__["_val"] = value * 10

class MyClass:
    x = Descriptor()

m = MyClass()
m.x = 5
print(m.x)
print(m.__dict__)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
50
{'_val': 50}
```

Setting `m.x = 5` calls `Descriptor.__set__`, which stores `5 * 10 = 50`
in `m.__dict__["_val"]`. Getting `m.x` calls `Descriptor.__get__`,
which reads `_val` from `m.__dict__`.

</details>

**Assessment:** Strong / Medium / Weak

---

## `__new__` vs `__init__`

**Self-rating:** __ / 5

**Interview question:**
"What is the difference between `__new__` and `__init__`? When
would you override `__new__`?"

Key points: `__new__` creates and returns the instance (called
first); `__init__` initializes it (called on the returned object);
override `__new__` for Singleton, immutable types (subclassing
`int`/`str`), or controlling instance creation; `__init__` is not
called if `__new__` doesn't return an instance of `cls`.

**Code reading:**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = getattr(self, "value", 0) + 1

a = Singleton()
b = Singleton()
print(a is b)
print(a.value)
print(b.value)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
True
2
2
```

`a` and `b` are the same object. `__init__` runs twice on the same
instance, incrementing `value` each time (0+1=1, then 1+1=2). Both
`a.value` and `b.value` read the same attribute.

</details>

**Assessment:** Strong / Medium / Weak

---

## Metaclasses

**Self-rating:** __ / 5

**Interview question:**
"What is a metaclass? What is the difference between using a
metaclass and using `__init_subclass__`?"

Key points: a metaclass is the class of a class (`type` by default);
controls class creation; `__init_subclass__` is simpler — it fires
on the parent when a child is defined, without needing a metaclass;
metaclasses are more powerful but harder to reason about.

**Code reading:**

```python
class PluginBase:
    _registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase._registry.append(cls.__name__)

class Alpha(PluginBase): pass
class Beta(PluginBase): pass

print(PluginBase._registry)
```

Predicted output: ___

<details>
<summary>Answer</summary>

```
['Alpha', 'Beta']
```

`__init_subclass__` fires on `PluginBase` each time a subclass is
defined — at class definition time, not at instantiation. No
metaclass needed for this pattern.

</details>

**Assessment:** Strong / Medium / Weak
