# Python Advanced Data Structures & Concepts: Complete Guide

---

## Table of Contents
1. [Introduction](#introduction)
2. [Advanced Comprehensions](#advanced-comprehensions)
3. [Iterators and Iterables](#iterators-and-iterables)
4. [Generators](#generators)
5. [Decorators](#decorators)
6. [Context Managers](#context-managers)
7. [Practical Examples](#practical-examples)
8. [Performance Comparisons](#performance-comparisons)
9. [Best Practices](#best-practices)
10. [Practice Exercises](#practice-exercises)

---

## Introduction

### Why Advanced Concepts?

1. **Performance** - Write efficient code
2. **Readability** - Express intent clearly
3. **Flexibility** - Powerful abstractions
4. **Pythonic** - Follow Python conventions

---

## Advanced Comprehensions

### Nested List Comprehensions

```python
# Creating nested lists
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flattening nested lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in nested for x in row]
print(flat)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiple levels of nesting
triple_nested = [[[x for x in range(2)] for _ in range(2)] for _ in range(2)]
print(triple_nested)
# Output: [[[0, 1], [0, 1]], [[0, 1], [0, 1]]]
```

### Dictionary Comprehensions

```python
# Create dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)
# Output: {'a': 1, 'b': 2, 'c': 3}

# Transform dictionary values
prices = {"apple": 1.50, "banana": 0.75, "orange": 2.00}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)
# Output: {'apple': 1.35, 'banana': 0.675, 'orange': 1.8}

# Invert dictionary
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print(inverted)
# Output: {1: 'a', 2: 'b', 3: 'c'}

# Conditional dictionary comprehension
numbers = range(10)
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### Set Comprehensions

```python
# Create set from list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
print(unique)
# Output: {1, 2, 3, 4}

# Get unique lengths
words = ["apple", "ant", "banana", "bat", "cherry"]
lengths = {len(word) for word in words}
print(lengths)
# Output: {3, 4, 6}

# Conditional set comprehension
numbers = range(20)
evens = {x for x in numbers if x % 2 == 0}
print(evens)
# Output: {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

### Conditional Comprehensions

```python
# If-else in list comprehension
numbers = range(10)
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(result)
# Output: ['even', 'odd', 'even', 'odd', ...]

# Multiple conditions
numbers = range(20)
result = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(result)
# Output: [0, 6, 12, 18]

# Nested if-else
numbers = range(10)
result = [x**2 if x % 2 == 0 else x**3 for x in numbers]
print(result)
# Output: [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]
```

---

## Iterators and Iterables

### Understanding Iteration Protocol

```python
# Iterable - has __iter__()
my_list = [1, 2, 3]
print(hasattr(my_list, '__iter__'))  # True

# Iterator - has __iter__() and __next__()
iterator = iter(my_list)
print(hasattr(iterator, '__iter__'))  # True
print(hasattr(iterator, '__next__'))  # True

# Get next items
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator)       # StopIteration
```

### Creating Custom Iterators

```python
class CountUp:
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

# Using custom iterator
counter = CountUp(3)
for num in counter:
    print(num)
# Output: 1 2 3

# Manual iteration
counter2 = CountUp(3)
while True:
    try:
        print(next(counter2))
    except StopIteration:
        break
# Output: 1 2 3
```

### iter() and next() Functions

```python
# iter() creates iterator
my_list = [10, 20, 30]
it = iter(my_list)

# next() gets next item
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

# With default value
my_list = [1, 2, 3]
it = iter(my_list)
print(next(it, "done"))  # 1
print(next(it, "done"))  # 2
print(next(it, "done"))  # 3
print(next(it, "done"))  # "done" (default)

# Reading file line by line
with open("data.txt") as f:
    line_iterator = iter(f)
    first_line = next(line_iterator)
    second_line = next(line_iterator)
```

---

## Generators

### Generator Functions

```python
def count_up(max):
    current = 0
    while current < max:
        current += 1
        yield current

# Using generator
for num in count_up(3):
    print(num)
# Output: 1 2 3

# Get all values
numbers = list(count_up(5))
print(numbers)  # [1, 2, 3, 4, 5]
```

### Yield Keyword

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate Fibonacci sequence
fib_list = list(fibonacci(7))
print(fib_list)
# Output: [0, 1, 1, 2, 3, 5, 8]

# Memory efficient - lazy evaluation
for fib in fibonacci(3):
    print(fib)
# Output: 0 1 1
```

### Generator Expressions

```python
# Like list comprehension but returns generator
gen = (x**2 for x in range(5))
print(gen)  # <generator object>

# Convert to list
squares = list(gen)
print(squares)  # [0, 1, 4, 9, 16]

# Generator expression uses less memory than list comprehension
import sys
list_comp = [x**2 for x in range(1000)]
gen_exp = (x**2 for x in range(1000))
print(sys.getsizeof(list_comp))  # ~9000 bytes
print(sys.getsizeof(gen_exp))    # ~128 bytes

# Use with functions
total = sum(x**2 for x in range(5))
print(total)  # 30

any_even = any(x % 2 == 0 for x in [1, 3, 5, 7, 8])
print(any_even)  # True
```

### send() Method

```python
def echo():
    value = None
    while True:
        value = yield value
        if value is not None:
            value = f"Echoing: {value}"

# Using send()
gen = echo()
next(gen)  # Prime generator
print(gen.send("hello"))     # Output: Echoing: hello
print(gen.send("world"))     # Output: Echoing: world
```

### Advantages of Generators

```python
# 1. Memory efficiency - lazy evaluation
def large_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Only generates values when needed
for num in large_range(1000000):
    if num > 10:
        break
# Only generated first 11 values, not 1 million

# 2. Chaining generators
def multiply(gen, factor):
    for x in gen:
        yield x * factor

def add(gen, value):
    for x in gen:
        yield x + value

# Chain operations
nums = range(5)
result = add(multiply(nums, 2), 10)
print(list(result))  # [10, 12, 14, 16, 18]

# 3. Infinite sequences
def infinite_count():
    num = 0
    while True:
        yield num
        num += 1

# Take only what you need
counter = infinite_count()
for i in range(5):
    print(next(counter))
# Output: 0 1 2 3 4
```

---

## Decorators

### Function Decorators

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### Decorators with Arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(5, 3))
# Output:
# Calling add
# Finished add
# 8
```

### Decorators with Parameters

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
# Output: ["Hello, Alice!", "Hello, Alice!", "Hello, Alice!"]
```

### functools.wraps

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Add two numbers"""
    return a + b

# Without @wraps - loses original function info
# print(add.__name__)  # Output: wrapper
# print(add.__doc__)   # Output: None

# With @wraps - preserves original function info
print(add.__name__)  # Output: add
print(add.__doc__)   # Output: Add two numbers
```

### Class Decorators

```python
def add_greeting(cls):
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        print(f"Creating {cls.__name__} instance")
        original_init(self, *args, **kwargs)
    
    cls.__init__ = new_init
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
# Output: Creating Person instance
```

### Common Built-in Decorators

```python
class MyClass:
    @staticmethod
    def static_method():
        return "Static"
    
    @classmethod
    def class_method(cls):
        return f"Class method of {cls.__name__}"
    
    @property
    def my_property(self):
        return "Property value"

obj = MyClass()
print(obj.static_method())      # Static
print(obj.class_method())       # Class method of MyClass
print(obj.my_property)          # Property value

# @property setter
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature too low")
        self._celsius = value

temp = Temperature()
temp.celsius = 25
print(temp.celsius)  # 25
```

### Chaining Decorators

```python
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 - Before")
        result = func(*args, **kwargs)
        print("Decorator 1 - After")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 - Before")
        result = func(*args, **kwargs)
        print("Decorator 2 - After")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Decorator 1 - Before
# Decorator 2 - Before
# Hello!
# Decorator 2 - After
# Decorator 1 - After

# Order: decorator1(decorator2(say_hello))
```

---

## Context Managers

### Creating Context Managers

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Using context manager
with FileManager("data.txt", "w") as f:
    f.write("Hello, World!")
# Output:
# Opening data.txt
# Closing data.txt
```

### contextlib Module

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    try:
        yield "Resource"
    finally:
        print("Exiting context")

with my_context() as resource:
    print(f"Using {resource}")
# Output:
# Entering context
# Using Resource
# Exiting context
```

### @contextmanager Decorator

```python
from contextlib import contextmanager

@contextmanager
def temporary_list():
    temp_list = []
    print("Created temporary list")
    try:
        yield temp_list
    finally:
        temp_list.clear()
        print("Cleaned up temporary list")

with temporary_list() as lst:
    lst.append(1)
    lst.append(2)
    print(f"List: {lst}")

# Output:
# Created temporary list
# List: [1, 2]
# Cleaned up temporary list
```

### Suppressing Exceptions

```python
from contextlib import suppress

# Without suppress - exception printed
with suppress(FileNotFoundError):
    open("nonexistent.txt")

# Does nothing, no exception raised
print("Continued after error")
```

---

## Practical Examples

### Timing Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()
# Output: slow_function took 1.0001 seconds
```

### Database Connection Context Manager

```python
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    connection = None
    try:
        print(f"Connecting to {db_name}")
        connection = f"Connection to {db_name}"  # Simulate connection
        yield connection
    except Exception as e:
        print(f"Error: {e}")
        raise
    finally:
        if connection:
            print(f"Disconnecting from {db_name}")

# Using it
with database_connection("users.db") as conn:
    print(f"Using {conn}")
# Output:
# Connecting to users.db
# Using Connection to users.db
# Disconnecting from users.db
```

### Caching Decorator

```python
from functools import wraps

def cache(func):
    cached = {}
    
    @wraps(func)
    def wrapper(n):
        if n not in cached:
            cached[n] = func(n)
        return cached[n]
    
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Much faster with caching
```

---

## Performance Comparisons

### List Comprehension vs Generator

```python
import sys
import timeit

# Memory usage
list_comp = [x**2 for x in range(10000)]
gen_exp = (x**2 for x in range(10000))

print(f"List: {sys.getsizeof(list_comp)} bytes")
print(f"Generator: {sys.getsizeof(gen_exp)} bytes")

# Time comparison
time_list = timeit.timeit("[x**2 for x in range(1000)]", number=10000)
time_gen = timeit.timeit("list(x**2 for x in range(1000))", number=10000)

print(f"List comprehension: {time_list:.4f}s")
print(f"Generator expression: {time_gen:.4f}s")
```

---

## Best Practices

### Use Comprehensions When

```python
# Good - simple transformations
squares = [x**2 for x in range(10)]

# Good - filtering
evens = [x for x in range(10) if x % 2 == 0]

# Avoid - too complex
result = [
    x**2 if x % 2 == 0 else x**3
    for x in range(100)
    if x > 50
    if x % 3 == 0
]
# Better as a function
```

### Use Generators When

```python
# Good - large datasets
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()

# Good - infinite sequences
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1
```

### Use Decorators For

```python
# Good - cross-cutting concerns
@timer
@cache
def expensive_function():
    pass

# Good - framework integration
@app.route("/users")
def get_users():
    pass
```

---

## Practice Exercises

### 1. Comprehensions
- Create nested list comprehensions
- Build dictionaries with comprehensions
- Use conditional comprehensions

### 2. Iterators
- Create custom iterators
- Use iter() and next()
- Understand iteration protocol

### 3. Generators
- Write generator functions
- Use generator expressions
- Compare with list comprehensions

### 4. Decorators
- Create function decorators
- Write decorators with parameters
- Chain multiple decorators

### 5. Context Managers
- Create context managers
- Use @contextmanager
- Implement resource cleanup

### 6. Real-World Projects
- Implement file processing with generators
- Build logging decorator
- Create database connection manager

---

# End of Notes
