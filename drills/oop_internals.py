"""
Drill: OOP Internals
Domain: oop
Linked topics: oop/dunder_methods.md, oop/inheritance_mro.md, oop/descriptors.md

Covers: dunder methods, MRO, descriptors, classmethod/staticmethod, __slots__.
"""

# =============================================================================
# EXERCISE 1 — Core dunder methods
# =============================================================================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(repr(v1))       # ?
print(str(v1))        # ?
print(v1 + v2)        # ?
print(v1 * 3)         # ?
print(v1 == Vector(1, 2))  # ?
print(len(v1))        # ?
print(round(abs(v2), 2))   # ?

# Expected: Vector(1, 2) / (1, 2) / (4, 6) / (3, 6) / True / 2 / 5.0


# =============================================================================
# EXERCISE 2 — MRO and C3 linearization
# =============================================================================

class A:
    def who(self): return "A"

class B(A):
    def who(self): return "B"

class C(A):
    def who(self): return "C"

class D(B, C):
    pass

d = D()
print(d.who())         # ?
print(D.__mro__)       # ?

# Expected:
# B
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)


# =============================================================================
# EXERCISE 3 — Cooperative `super()` in diamond inheritance
# =============================================================================

class Base:
    def greet(self):
        print("Base.greet")

class Left(Base):
    def greet(self):
        print("Left.greet")
        super().greet()

class Right(Base):
    def greet(self):
        print("Right.greet")
        super().greet()

class Child(Left, Right):
    def greet(self):
        print("Child.greet")
        super().greet()

Child().greet()

# Expected:
# Child.greet
# Left.greet
# Right.greet
# Base.greet


# =============================================================================
# EXERCISE 4 — classmethod vs staticmethod vs instance method
# =============================================================================

class MyClass:
    class_var = "I am the class"

    def instance_method(self):
        return f"instance, class_var={self.class_var}"

    @classmethod
    def class_method(cls):
        return f"classmethod, cls={cls.__name__}, class_var={cls.class_var}"

    @staticmethod
    def static_method(x):
        return f"staticmethod, no access to class or instance, x={x}"

obj = MyClass()
print(obj.instance_method())   # ?
print(obj.class_method())      # ?
print(obj.static_method(42))   # ?
print(MyClass.class_method())  # ?
print(MyClass.static_method(99))  # ?

# What happens with:
# MyClass.instance_method()    ← TypeError: missing 'self'


# =============================================================================
# EXERCISE 5 — `__slots__` memory and attribute restriction
# =============================================================================

class WithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys

a = WithDict(1, 2)
b = WithSlots(1, 2)

print(sys.getsizeof(a))   # larger (has __dict__)
print(sys.getsizeof(b))   # smaller (no __dict__)
print(hasattr(a, '__dict__'))  # True
print(hasattr(b, '__dict__'))  # False

try:
    b.z = 3   # ?
except AttributeError as e:
    print(e)  # 'WithSlots' object has no attribute 'z'


# =============================================================================
# EXERCISE 6 — `__new__` vs `__init__`
# =============================================================================

class Tracked:
    _count = 0

    def __new__(cls, *args, **kwargs):
        cls._count += 1
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        self.name = name

a = Tracked("a")
b = Tracked("b")
c = Tracked("c")

print(Tracked._count)   # ?
print(a.name)           # ?

# Expected: 3 / a


# =============================================================================
# EXERCISE 7 — `__repr__` vs `__str__`
# =============================================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(str(p))     # uses __str__
print(repr(p))    # uses __repr__
print(f"{p}")     # uses __str__
print(f"{p!r}")   # forces __repr__
print([p])        # list repr uses __repr__ of elements

# Expected:
# (1, 2)
# Point(1, 2)
# (1, 2)
# Point(1, 2)
# [Point(1, 2)]


if __name__ == "__main__":
    print("\nAll OOP internals drills complete.")
