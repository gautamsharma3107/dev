# Day 3 Quick Reference Cheat Sheet

## Function Basics
```python
# Define function
def greet(name):
    """Docstring: explains function."""
    return f"Hello, {name}!"

# Call function
result = greet("Gautam")
```

## Parameters
```python
# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Keyword arguments
greet(name="Alice", greeting="Hi")

# *args - variable positional
def sum_all(*numbers):
    return sum(numbers)

# **kwargs - variable keyword
def create_user(**details):
    return details
```

## Return Values
```python
# Single return
def square(x):
    return x ** 2

# Multiple returns (tuple)
def min_max(nums):
    return min(nums), max(nums)

# Unpack returns
minimum, maximum = min_max([1, 2, 3])
```

## Lambda Functions
```python
# Syntax: lambda arguments: expression
square = lambda x: x ** 2
add = lambda a, b: a + b
is_even = lambda x: x % 2 == 0

# With conditional
sign = lambda x: "pos" if x > 0 else "neg"
```

## Built-in Functions
```python
# map - apply function to each item
squared = list(map(lambda x: x**2, [1,2,3]))

# filter - keep items where function returns True
evens = list(filter(lambda x: x%2==0, [1,2,3,4]))

# zip - combine iterables
pairs = list(zip([1,2], ['a','b']))  # [(1,'a'), (2,'b')]

# enumerate - add index
for i, item in enumerate(items):
    print(i, item)

# sorted - sort with key
sorted(students, key=lambda s: s['score'])

# reduce - reduce to single value
from functools import reduce
total = reduce(lambda a,b: a+b, [1,2,3,4])
```

## Scope
```python
# Global variable
global_var = "global"

def func():
    global global_var  # Use global
    local_var = "local"  # Only in function
```

## Closures
```python
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
double(5)  # 10
```

## Simple Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

## Common Patterns
```python
# Chain map and filter
result = list(map(lambda x: x**2, 
              filter(lambda x: x%2==0, nums)))

# Sort dict by value
sorted(d.items(), key=lambda x: x[1])

# Find max in dict
max(d, key=d.get)

# Create dict from two lists
dict(zip(keys, values))
```

---
**Keep this handy for Day 3 topics!** 🚀
