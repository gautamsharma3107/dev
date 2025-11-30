# Python Functional Programming: Complete Guide

---

## Table of Contents
1. [Introduction to Functional Programming](#introduction-to-functional-programming)
2. [First-Class Functions](#first-class-functions)
3. [Higher-Order Functions](#higher-order-functions)
4. [Pure Functions](#pure-functions)
5. [Map, Filter, Reduce](#map-filter-reduce)
6. [functools Module](#functools-module)
7. [Partial Functions](#partial-functions)
8. [Immutability Concepts](#immutability-concepts)
9. [Practical Examples](#practical-examples)
10. [Functional vs Object-Oriented](#functional-vs-object-oriented)
11. [Best Practices](#best-practices)
12. [Practice Exercises](#practice-exercises)

---

## Introduction to Functional Programming

### What is Functional Programming?

Functional programming (FP) is a paradigm that treats computation as the evaluation of mathematical functions.

### Key Principles

1. **Immutability** - Data doesn't change after creation
2. **Pure Functions** - Functions produce consistent output for same input
3. **First-Class Functions** - Functions can be values
4. **Higher-Order Functions** - Functions that operate on functions
5. **Composition** - Combining functions together

### Why Functional Programming?

1. **Predictability** - Pure functions are easier to reason about
2. **Testability** - No side effects make testing easier
3. **Parallelization** - Immutable data enables parallel processing
4. **Debugging** - Easier to trace execution
5. **Code Reuse** - Functions compose well

### FP vs Imperative

```python
# Imperative - HOW to do it
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)

# Functional - WHAT to do
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Both output: [1, 4, 9, 16, 25]
```

---

## First-Class Functions

### Functions as Values

```python
# Functions are objects
def greet(name):
    return f"Hello, {name}!"

# Assign to variable
my_func = greet
print(my_func("Alice"))  # Output: Hello, Alice!

# Pass as argument
def apply_twice(func, value):
    return func(func(value))

def add_one(x):
    return x + 1

result = apply_twice(add_one, 5)
print(result)  # Output: 7
```

### Returning Functions

```python
# Function that returns function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_three = create_multiplier(3)
print(times_three(5))    # Output: 15
print(times_three(10))   # Output: 30

times_five = create_multiplier(5)
print(times_five(4))     # Output: 20
```

### Functions in Data Structures

```python
# Store functions in list
operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]

value = 5
for op in operations:
    value = op(value)
    print(value)
# Output: 6, 12, 144

# Store in dictionary
funcs = {
    "add": lambda x, y: x + y,
    "multiply": lambda x, y: x * y,
    "subtract": lambda x, y: x - y
}

print(funcs["add"](5, 3))      # Output: 8
print(funcs["multiply"](5, 3)) # Output: 15
```

---

## Higher-Order Functions

### Functions That Take Functions

```python
# Higher-order function
def apply_operation(func, a, b):
    return func(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print(apply_operation(add, 5, 3))      # Output: 8
print(apply_operation(multiply, 5, 3)) # Output: 15

# With lambdas
print(apply_operation(lambda x, y: x - y, 5, 3))  # Output: 2
```

### Decorator (Higher-Order Function)

```python
# Decorator is a higher-order function
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()
```

### Composing Functions

```python
# Function composition
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

def double(x):
    return x * 2

def add_one(x):
    return x + 1

# (double then add_one)
double_then_add = compose(add_one, double)
print(double_then_add(5))  # Output: 11 (5*2=10, 10+1=11)

# Pipe functions (left to right)
def pipe(*functions):
    def piped(value):
        for func in functions:
            value = func(value)
        return value
    return piped

add_five = lambda x: x + 5
multiply_two = lambda x: x * 2
divide_ten = lambda x: x / 10

pipeline = pipe(add_five, multiply_two, divide_ten)
print(pipeline(5))  # Output: 2.0 ((5+5)*2/10)
```

---

## Pure Functions

### What is a Pure Function?

A pure function:
1. Returns the same output for same input (deterministic)
2. Has no side effects (doesn't modify external state)

```python
# Pure function
def add(a, b):
    return a + b

print(add(5, 3))  # Always 8
print(add(5, 3))  # Always 8

# Not pure - has side effects
count = 0
def increment():
    global count
    count += 1  # Modifies external state
    return count

print(increment())  # 1
print(increment())  # 2 (different output)

# Not pure - non-deterministic
import random
def random_add(a, b):
    return a + b + random.random()

print(random_add(5, 3))  # 8.xxx
print(random_add(5, 3))  # 8.yyy (different)
```

### Benefits of Pure Functions

```python
# Pure functions are easy to test
def multiply(x, y):
    return x * y

assert multiply(3, 4) == 12
assert multiply(0, 100) == 0
assert multiply(-5, -2) == 10

# Pure functions can be cached
from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_computation(n):
    # Only computed once per unique input
    return n ** n

print(expensive_computation(5))  # Computed
print(expensive_computation(5))  # Cached
```

### Avoiding Side Effects

```python
# BAD - modifies original list
def sort_list_bad(items):
    items.sort()
    return items

# GOOD - returns new sorted list
def sort_list_good(items):
    return sorted(items)

original = [3, 1, 2]
result = sort_list_good(original)
print(original)  # [3, 1, 2] (unchanged)
print(result)    # [1, 2, 3]

# BAD - modifies dictionary
def update_dict_bad(data, key, value):
    data[key] = value
    return data

# GOOD - returns new dictionary
def update_dict_good(data, key, value):
    new_data = data.copy()
    new_data[key] = value
    return new_data

original = {"a": 1}
result = update_dict_good(original, "b", 2)
print(original)  # {"a": 1} (unchanged)
print(result)    # {"a": 1, "b": 2}
```

---

## Map, Filter, Reduce

### map()

```python
# Apply function to each element
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# With custom function
def uppercase(word):
    return word.upper()

words = ["hello", "world", "python"]
result = map(uppercase, words)
print(list(result))  # ['HELLO', 'WORLD', 'PYTHON']

# Multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
sums = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sums))  # [11, 22, 33]
```

### filter()

```python
# Keep only elements where function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6, 8, 10]

# Filter with custom function
def is_positive(x):
    return x > 0

numbers = [-2, -1, 0, 1, 2]
positives = filter(is_positive, numbers)
print(list(positives))  # [1, 2]

# Remove None values
data = [1, None, 2, None, 3, 4]
filtered = filter(None, data)
print(list(filtered))  # [1, 2, 3, 4]
```

### reduce()

```python
from functools import reduce

# Accumulate function result
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)

# With initial value
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers, 100)
print(total)  # 115 (100+1+2+3+4+5)

# Finding max
numbers = [5, 3, 9, 1, 7]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 9

# Concatenate strings
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Hello World Python
```

### Combining map, filter, reduce

```python
from functools import reduce

# Get sum of squares of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
print(result)  # 220 (4+16+36+64+100)

# Better with list comprehension
result2 = sum(x**2 for x in numbers if x % 2 == 0)
print(result2)  # 220 (same result)
```

---

## functools Module

### reduce()

```python
from functools import reduce

# Already covered above
```

### lru_cache

```python
from functools import lru_cache

# Cache function results
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Fast due to caching

# Clear cache
fibonacci.cache_clear()

# Cache info
print(fibonacci.cache_info())
# CacheInfo(hits=..., misses=..., maxsize=128, currsize=...)
```

### wraps

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

print(add.__name__)  # add (preserved)
print(add.__doc__)   # Add two numbers (preserved)
```

### cmp_to_key

```python
from functools import cmp_to_key

# Convert comparison function to key function
def compare(x, y):
    return (x > y) - (x < y)

numbers = [5, 2, 8, 1, 9]
sorted_nums = sorted(numbers, key=cmp_to_key(compare))
print(sorted_nums)  # [1, 2, 5, 8, 9]
```

---

## Partial Functions

### Creating Partial Functions

```python
from functools import partial

# Original function
def multiply(x, y):
    return x * y

# Create partial function with x=10
times_ten = partial(multiply, 10)
print(times_ten(5))   # Output: 50
print(times_ten(3))   # Output: 30

# With multiple arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))      # Output: 25
print(square(10))     # Output: 100

cube = partial(power, exponent=3)
print(cube(2))        # Output: 8
```

### Practical Applications

```python
from functools import partial

# Create specialized functions
def convert_temperature(value, formula):
    if formula == "c_to_f":
        return value * 9/5 + 32
    elif formula == "f_to_c":
        return (value - 32) * 5/9

celsius_to_fahrenheit = partial(convert_temperature, formula="c_to_f")
fahrenheit_to_celsius = partial(convert_temperature, formula="f_to_c")

print(celsius_to_fahrenheit(0))     # 32.0
print(fahrenheit_to_celsius(32))    # 0.0

# With map
temperatures_c = [0, 10, 20, 30]
temperatures_f = list(map(celsius_to_fahrenheit, temperatures_c))
print(temperatures_f)  # [32.0, 50.0, 68.0, 86.0]
```

---

## Immutability Concepts

### Understanding Immutability

```python
# Immutable types
immutable_int = 5
immutable_str = "hello"
immutable_tuple = (1, 2, 3)

# Cannot modify immutable types
# immutable_str[0] = "H"  # TypeError
# immutable_tuple[0] = 10  # TypeError

# Mutable types
mutable_list = [1, 2, 3]
mutable_dict = {"a": 1}

# Can modify mutable types
mutable_list[0] = 10
mutable_dict["a"] = 99
```

### Benefits of Immutability

```python
# Thread-safe (no race conditions)
import threading

immutable = (1, 2, 3)
mutable = [1, 2, 3]

# Multiple threads can safely read immutable data
# But need locks for mutable data

# Hashable (can use as dictionary key)
immutable_tuple = (1, 2, 3)
my_dict = {immutable_tuple: "value"}

# mutable_list = [1, 2, 3]
# my_dict[mutable_list] = "value"  # TypeError

# Predictable (no unexpected changes)
def process(data):
    data = data + (4, 5)  # Creates new tuple
    return data

original = (1, 2, 3)
result = process(original)
print(original)  # (1, 2, 3) - unchanged
print(result)    # (1, 2, 3, 4, 5)
```

### Making Copies for Immutability

```python
# Shallow copy
original = {"a": [1, 2], "b": 3}
shallow = original.copy()

shallow["b"] = 99
print(original["b"])  # 3 (changed)

shallow["a"].append(3)
print(original["a"])  # [1, 2, 3] (changed! nested list shared)

# Deep copy
from copy import deepcopy
original = {"a": [1, 2], "b": 3}
deep = deepcopy(original)

deep["a"].append(3)
print(original["a"])  # [1, 2] (unchanged)
```

### Immutable Data Structures

```python
from collections import namedtuple
from types import MappingProxyType

# Immutable named tuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x)  # 1
# p.x = 3   # AttributeError

# Make dictionary immutable
original = {"a": 1, "b": 2}
immutable_dict = MappingProxyType(original)
print(immutable_dict["a"])  # 1
# immutable_dict["a"] = 99  # TypeError

# But can modify original through proxy
original["a"] = 99
print(immutable_dict["a"])  # 99 (reflects change)
```

---

## Practical Examples

### Data Transformation Pipeline

```python
from functools import reduce

# Transform data through pipeline
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers, square them, sum them
result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2, 
        filter(lambda x: x % 2 == 0, data))
)
print(result)  # 220

# More readable with intermediate steps
evens = filter(lambda x: x % 2 == 0, data)
squared = map(lambda x: x**2, evens)
total = reduce(lambda acc, x: acc + x, squared)
print(total)  # 220
```

### Function Composition Utilities

```python
from functools import reduce

def compose(*functions):
    """Compose functions right to left: compose(f, g)(x) = f(g(x))"""
    def composed(value):
        return reduce(lambda v, f: f(v), reversed(functions), value)
    return composed

def add_five(x):
    return x + 5

def multiply_two(x):
    return x * 2

def square(x):
    return x ** 2

# Compose functions
add_then_multiply = compose(multiply_two, add_five)
print(add_then_multiply(3))  # (3+5)*2 = 16

add_then_multiply_then_square = compose(square, multiply_two, add_five)
print(add_then_multiply_then_square(3))  # ((3+5)*2)^2 = 256
```

### Currying

```python
# Currying - convert function with multiple arguments
# into sequence of functions with single argument

def curry(func):
    """Convert function to curried version"""
    from functools import wraps
    @wraps(func)
    def curried(*args):
        if len(args) == func.__code__.co_argcount:
            return func(*args)
        return lambda *more: curried(*args, *more)
    return curried

@curry
def add(a, b, c):
    return a + b + c

print(add(1)(2)(3))     # 6
print(add(1, 2)(3))     # 6
print(add(1)(2, 3))     # 6
print(add(1, 2, 3))     # 6
```

---

## Functional vs Object-Oriented

### Comparison

```python
# Object-Oriented
class Calculator:
    def __init__(self, value=0):
        self.value = value
    
    def add(self, x):
        self.value += x
        return self
    
    def multiply(self, x):
        self.value *= x
        return self
    
    def result(self):
        return self.value

calc = Calculator()
result = calc.add(5).multiply(2).add(3).result()
print(result)  # 13

# Functional
def add(x):
    return lambda value: value + x

def multiply(x):
    return lambda value: value * x

from functools import reduce

operations = [add(5), multiply(2), add(3)]
result = reduce(lambda val, op: op(val), operations, 0)
print(result)  # 13 (same result)
```

---

## Best Practices

### When to Use Functional Programming

```python
# Good - transforming data
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, data)))

# Good - creating specialized functions
from functools import partial
convert_to_celsius = partial(convert_temperature, formula="f_to_c")

# Avoid - deeply nested functions
# result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))
# Better - use list comprehension
result = [x**2 for x in data if x % 2 == 0]
```

### Readability Balance

```python
# Functional but hard to read
result = reduce(lambda acc, x: acc + [x**2] if x % 2 == 0 else acc, [1,2,3,4,5], [])

# Readable
result = [x**2 for x in [1,2,3,4,5] if x % 2 == 0]

# Both output: [4, 16]
```

---

## Practice Exercises

### 1. First-Class Functions
- Pass functions as arguments
- Return functions from functions
- Store functions in data structures

### 2. Higher-Order Functions
- Create function decorators
- Implement function composition
- Build pipelines

### 3. Pure Functions
- Write pure functions
- Test pure functions
- Avoid side effects

### 4. Map, Filter, Reduce
- Transform data with map
- Filter data with conditions
- Accumulate with reduce

### 5. functools
- Use lru_cache for memoization
- Create partial functions
- Apply wraps decorator

### 6. Immutability
- Use immutable data structures
- Make deep copies
- Thread-safe operations

### 7. Real-World Projects
- Build data processing pipeline
- Create API with FP principles
- Implement caching system

---

# End of Notes
