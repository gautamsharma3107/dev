# Python Object-Oriented Programming (OOP): Complete Guide

---

## Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [Classes and Objects](#classes-and-objects)
3. [Attributes and Methods](#attributes-and-methods)
4. [Constructors](#constructors)
5. [Inheritance](#inheritance)
6. [Encapsulation](#encapsulation)
7. [Polymorphism](#polymorphism)
8. [Abstraction](#abstraction)
9. [Magic/Dunder Methods](#magicdunder-methods)
10. [Practical Examples](#practical-examples)
11. [Practice Exercises](#practice-exercises)

---

## Introduction to OOP

### What is OOP?

Object-Oriented Programming is a programming paradigm based on objects and classes.

### Four Pillars of OOP

1. **Encapsulation** - Bundle data and methods together
2. **Inheritance** - Reuse code through parent-child relationships
3. **Polymorphism** - Objects can take multiple forms
4. **Abstraction** - Hide complex implementation details

### Benefits of OOP

1. **Modularity** - Code organized into logical units
2. **Reusability** - Code can be reused and extended
3. **Maintainability** - Easier to understand and modify
4. **Scalability** - Handles large codebases well

---

## Classes and Objects

### Defining a Class

```python
# Class definition
class Dog:
    pass  # Empty class

# Create object (instance)
my_dog = Dog()
print(type(my_dog))  # Output: <class '__main__.Dog'>
```

### Class with Methods

```python
class Dog:
    def bark(self):
        print("Woof! Woof!")
    
    def greet(self, name):
        print(f"Hi {name}, I'm a dog!")

# Create and use object
my_dog = Dog()
my_dog.bark()  # Output: Woof! Woof!
my_dog.greet("Alice")  # Output: Hi Alice, I'm a dog!
```

### The self Parameter

```python
class Person:
    def greet(self):
        print("Hello, I'm a person")

# self refers to the instance
p = Person()
p.greet()  # self = p inside the method

# Explicit equivalent
Person.greet(p)  # Calling method directly on class
```

---

## Attributes and Methods

### Instance Attributes

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute
        self.age = 0  # Instance attribute

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Max

# Each instance has separate attributes
dog1.age = 5
dog2.age = 3
print(dog1.age, dog2.age)  # Output: 5 3
```

### Class Attributes

```python
class Dog:
    species = "Canis familiaris"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Access class attribute
print(dog1.species)  # Output: Canis familiaris
print(Dog.species)   # Output: Canis familiaris

# Shared across all instances
print(dog1.species == dog2.species)  # Output: True
```

### Instance Methods

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())  # Output: 15
print(rect.perimeter())  # Output: 16
```

### Class Methods (@classmethod)

```python
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.get_count())  # Output: 3
```

### Static Methods (@staticmethod)

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Call without creating instance
print(Math.add(5, 3))  # Output: 8
print(Math.multiply(5, 3))  # Output: 15

# Can also call on instance
m = Math()
print(m.add(5, 3))  # Output: 8
```

---

## Constructors

### __init__ Method

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        print(f"{self.year} {self.brand} {self.model}")

car = Car("Toyota", "Camry", 2020)
car.info()  # Output: 2020 Toyota Camry
```

### __new__ Method

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True (same instance)
```

### Constructor with Default Values

```python
class Person:
    def __init__(self, name, age=0, city="Unknown"):
        self.name = name
        self.age = age
        self.city = city

p1 = Person("Alice", 25, "New York")
p2 = Person("Bob", 30)
p3 = Person("Charlie")

print(p1.city)  # Output: New York
print(p2.city)  # Output: Unknown
print(p3.age)   # Output: 0
```

---

## Inheritance

### Single Inheritance

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks: Woof!")

dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks: Woof!
```

### Multiple Inheritance

```python
class Flying:
    def fly(self):
        print("Flying...")

class Swimming:
    def swim(self):
        print("Swimming...")

class Duck(Flying, Swimming):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()    # Output: Flying...
duck.swim()   # Output: Swimming...
duck.quack()  # Output: Quack!
```

### Multi-level Inheritance

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Puppy(Dog):
    def speak(self):
        print("Puppy yaps")

puppy = Puppy()
puppy.speak()  # Output: Puppy yaps
```

### Method Resolution Order (MRO)

```python
class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")

class C(A):
    def method(self):
        print("C's method")

class D(B, C):
    pass

d = D()
d.method()  # Output: B's method

# Check MRO
print(D.__mro__)
# Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### super() Function

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed
    
    def speak(self):
        super().speak()  # Call parent speak()
        print(f"{self.name} barks!")

dog = Dog("Buddy", "Labrador")
dog.speak()
# Output:
# Buddy makes a sound
# Buddy barks!
```

---

## Encapsulation

### Public Attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute

p = Person("Alice", 25)
print(p.name)  # Output: Alice
p.name = "Bob"  # Can modify freely
print(p.name)  # Output: Bob
```

### Protected Attributes (_variable)

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected (convention)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Can access but shouldn't (convention)
print(account._balance)  # Output: 1500
```

### Private Attributes (__variable)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Cannot access directly
# print(account.__balance)  # AttributeError
```

### Name Mangling

```python
class MyClass:
    def __init__(self):
        self.__private = "secret"

obj = MyClass()

# Name mangling: __private becomes _MyClass__private
print(obj._MyClass__private)  # Output: secret
```

### @property Decorator

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age must be positive")

p = Person("Alice", 25)
print(p.name)  # Output: Alice
print(p.age)   # Output: 25

p.age = 26
print(p.age)   # Output: 26

p.age = -5     # Output: Age must be positive
```

---

## Polymorphism

### Method Overriding

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()
# Output:
# Dog barks
# Cat meows
# Animal speaks
```

### Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)  # Output: (4, 6)

v4 = v1 * 2
print(v4)  # Output: (2, 4)
```

### Duck Typing

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(obj):
    obj.quack()

duck = Duck()
person = Person()

make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm quacking like a duck!

# If it quacks like a duck, it's a duck (duck typing)
```

---

## Abstraction

### Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Cannot instantiate abstract class
# shape = Shape()  # TypeError

# Can instantiate concrete class
circle = Circle(5)
print(circle.area())  # Output: 78.5
```

### Abstract Methods

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def honk(self):
        print("Honk!")

class Car(Vehicle):
    def start(self):
        print("Car engine starts")
    
    def stop(self):
        print("Car engine stops")

car = Car()
car.start()   # Output: Car engine starts
car.honk()    # Output: Honk!
```

---

## Magic/Dunder Methods

### __str__ and __repr__

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(str(p))   # Output: Alice is 25 years old
print(repr(p))  # Output: Person('Alice', 25)
```

### __len__ and __getitem__

```python
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value

ml = MyList([1, 2, 3, 4, 5])
print(len(ml))  # Output: 5
print(ml[0])    # Output: 1
ml[0] = 10
print(ml[0])    # Output: 10
```

### __iter__ and __next__

```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)
# Output:
# 1
# 2
# 3
```

### __call__

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

times3 = Multiplier(3)
print(times3(5))  # Output: 15
print(times3(10))  # Output: 30
```

### __enter__ and __exit__

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileManager("data.txt", "w") as f:
    f.write("Hello, World!")
# File automatically closed
```

### Comparison Operators

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __ge__(self, other):
        return self.age >= other.age
    
    def __ne__(self, other):
        return self.age != other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1 == p2)  # Output: False
print(p1 < p2)   # Output: True
print(p1 > p2)   # Output: False
```

### Arithmetic Operators

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, scalar):
        return Complex(self.real * scalar, self.imag * scalar)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(3, 4)
c2 = Complex(1, 2)

c3 = c1 + c2
print(c3)  # Output: 4 + 6i

c4 = c1 * 2
print(c4)  # Output: 6 + 8i
```

---

## Practical Examples

### Bank Account System

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid or insufficient funds")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")
```

### Employee Management System

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
    
    def __str__(self):
        return f"{self.name}: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def __str__(self):
        return f"{self.name}: ${self.salary} (manages {self.team_size})"

emp = Employee("Alice", 50000)
mgr = Manager("Bob", 60000, 5)

print(emp)  # Output: Alice: $50000
print(mgr)  # Output: Bob: $60000 (manages 5)
```

---

## Practice Exercises

### 1. Classes and Objects
- Create a Student class with attributes and methods
- Create multiple instances with different data
- Practice accessing attributes and calling methods

### 2. Inheritance
- Create parent and child classes
- Override parent methods in child
- Use super() to call parent methods

### 3. Encapsulation
- Practice public, protected, and private attributes
- Use @property decorator for getters/setters
- Implement validation in setters

### 4. Polymorphism
- Create multiple classes with same method names
- Demonstrate method overriding
- Overload operators for custom classes

### 5. Abstraction
- Create abstract base classes
- Implement abstract methods in subclasses
- Practice with ABC module

### 6. Magic Methods
- Implement __str__ and __repr__
- Overload arithmetic operators
- Create custom iteration with __iter__

### 7. Real-World Projects
- Build library management system
- Create game character hierarchy
- Design e-commerce product system
- Implement todo list application

---

# End of Notes
