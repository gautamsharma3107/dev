# Tuples in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Tuples](#introduction-to-tuples)
2. [Creating Tuples](#creating-tuples)
3. [Accessing Tuple Elements](#accessing-tuple-elements)
4. [Tuple Operations](#tuple-operations)
5. [Tuple Methods](#tuple-methods)
6. [Tuple Packing and Unpacking](#tuple-packing-and-unpacking)
7. [Named Tuples](#named-tuples)
8. [Tuples vs Lists](#tuples-vs-lists)
9. [Tuple Use Cases](#tuple-use-cases)
10. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Create and use tuples effectively
- ✅ Understand tuple immutability
- ✅ Pack and unpack tuples
- ✅ Use tuple methods
- ✅ Work with named tuples
- ✅ Know when to use tuples vs lists
- ✅ Apply tuples in practical scenarios

---

## Introduction to Tuples

### What are Tuples?

**Tuples** are immutable, ordered sequences. Like lists, but once created, they cannot be changed.

```python
# Tuple - immutable
point = (3, 5)
person = ("Alice", 25, "NYC")

# Can access elements
print(point[0])  # 3

# ❌ Cannot modify!
# point[0] = 4  # TypeError: 'tuple' object does not support item assignment
```

**Real-World Analogy** 🌍

Think of a tuple like:
- **An coordinates on a map** - Fixed position (latitude, longitude)
- **RGB color value** - (255, 128, 0) never changes
- **Date** - (2024, 12, 1) is immutable

### Key Characteristics

1. **Ordered** - Elements maintain their position
2. **Immutable** - Cannot change after creation
3. **Allow duplicates** - Same value can appear multiple times
4. **Indexed** - Access by position (0-based)
5. **Heterogeneous** - Can contain different types
6. **Hashable** - Can be used as dict keys or set elements

```python
# Ordered
numbers = (3, 1, 4, 1, 5)
# Stays in this exact order

# Immutable
point = (10, 20)
# point[0] = 5  # Error!

# Duplicates allowed
numbers = (1, 1, 2, 2, 3)

# Indexed
coords = (10, 20, 30)
#         0   1   2

# Mixed types
mixed = (42, "hello", 3.14, True, [1, 2, 3])

# Hashable (can be dict key!)
locations = {
    (0, 0): "origin",
    (1, 0): "east"
}
```

---

## Creating Tuples

### Using Parentheses

```python
# With parentheses
coords = (10, 20)
person = ("Alice", 25, "NYC")

# Without parentheses (still a tuple!)
point = 10, 20
print(type(point))  # <class 'tuple'>

# Empty tuple
empty = ()
print(len(empty))  # 0
```

### Single Element Tuple (IMPORTANT!)

```python
# ❌ WRONG - This is NOT a tuple!
not_tuple = (42)
print(type(not_tuple))  # <class 'int'>

# ✅ CORRECT - Need trailing comma!
single = (42,)
print(type(single))  # <class 'tuple'>

# Without parens (still works)
single = 42,
print(type(single))  # <class 'tuple'>

# Why? The comma makes it a tuple, not parentheses!
```

### Using tuple() Constructor

```python
# From list
tuple_from_list = tuple([1, 2, 3])
print(tuple_from_list)  # (1, 2, 3)

# From string
tuple_from_str = tuple("Python")
print(tuple_from_str)  # ('P', 'y', 't', 'h', 'o', 'n')

# From range
tuple_from_range = tuple(range(5))
print(tuple_from_range)  # (0, 1, 2, 3, 4)

# From set (random order)
tuple_from_set = tuple({3, 1, 2})
print(tuple_from_set)  # (1, 2, 3) - sorted by set
```

### Nested Tuples

```python
# Tuple of tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Access nested elements
print(matrix[0])     # (1, 2, 3)
print(matrix[0][1])  # 2

# Mixed nesting
mixed = (1, (2, 3), [4, 5], "hello")
```

---

## Accessing Tuple Elements

### Indexing

```python
fruits = ("apple", "banana", "orange", "grape", "mango")
#          0        1         2         3        4      (positive)
#         -5       -4        -3        -2       -1      (negative)

# Positive indexing
print(fruits[0])   # "apple"
print(fruits[2])   # "orange"
print(fruits[4])   # "mango"

# Negative indexing
print(fruits[-1])  # "mango" (last)
print(fruits[-2])  # "grape" (second to last)
print(fruits[-5])  # "apple" (first)
```

### Slicing

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing [start:stop]
print(numbers[2:5])    # (2, 3, 4)
print(numbers[0:3])    # (0, 1, 2)

# Omitting start/stop
print(numbers[:5])     # (0, 1, 2, 3, 4)
print(numbers[5:])     # (5, 6, 7, 8, 9)
print(numbers[:])      # Entire tuple (creates copy)

# Step parameter [start:stop:step]
print(numbers[::2])    # (0, 2, 4, 6, 8)
print(numbers[1::2])   # (1, 3, 5, 7, 9)
print(numbers[::3])    # (0, 3, 6, 9)

# Reverse
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# Negative indices
print(numbers[-5:])    # (5, 6, 7, 8, 9)
print(numbers[:-3])    # (0, 1, 2, 3, 4, 5, 6)
```

---

## Tuple Operations

### Concatenation (+)

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combine tuples
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# Multiple concatenation
result = (1,) + (2, 3) + (4, 5, 6)
print(result)  # (1, 2, 3, 4, 5, 6)

# Original tuples unchanged (immutable!)
print(tuple1)  # (1, 2, 3)
```

### Repetition (*)

```python
# Repeat tuple
pattern = (1, 2) * 3
print(pattern)  # (1, 2, 1, 2, 1, 2)

# Single element repeated
zeros = (0,) * 5
print(zeros)  # (0, 0, 0, 0, 0)

# Empty tuple repeated (still empty!)
empty = () * 100
print(empty)  # ()
```

### Membership Testing

```python
fruits = ("apple", "banana", "orange")

# Check if element exists
print("apple" in fruits)   # True
print("grape" in fruits)   # False

# Check for non-existence
print("grape" not in fruits)  # True

# With numbers
numbers = (1, 2, 3, 4, 5)
print(3 in numbers)  # True
print(10 in numbers)  # False
```

### Length

```python
# Get number of elements
numbers = (1, 2, 3, 4, 5)
print(len(numbers))  # 5

# Empty tuple
empty = ()
print(len(empty))  # 0

# Nested tuple
nested = ((1, 2), (3, 4), (5, 6))
print(len(nested))  # 3 (counts inner tuples as single elements)
```

### Min, Max, Sum

```python
numbers = (5, 2, 8, 1, 9, 3)

print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 28

# With strings (lexicographic order)
words = ("zebra", "apple", "mango")
print(min(words))  # "apple"
print(max(words))  # "zebra"
```

### Iteration

```python
fruits = ("apple", "banana", "orange")

# Simple iteration
for fruit in fruits:
    print(fruit)

# With index (enumerate)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# Start index from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

---

## Tuple Methods

Tuples have only 2 methods (because they're immutable):

### count() Method

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# Count occurrences
print(numbers.count(2))  # 3
print(numbers.count(5))  # 1
print(numbers.count(10)) # 0

# Practical use
votes = ("Alice", "Bob", "Alice", "Charlie", "Alice", "Bob")
print(f"Alice got {votes.count('Alice')} votes")  # 3
```

### index() Method

```python
fruits = ("apple", "banana", "orange", "banana", "grape")

# Find first occurrence
print(fruits.index("banana"))  # 1

# Starting from specific index
print(fruits.index("banana", 2))  # 3 (finds second "banana")

# Within range
print(fruits.index("orange", 1, 4))  # 2

# ValueError if not found
# fruits.index("mango")  # ValueError!

# Safe search
if "mango" in fruits:
    idx = fruits.index("mango")
else:
    idx = -1
    print("Not found")
```

---

## Tuple Packing and Unpacking

### Packing

```python
# Automatic packing
point = 3, 5  # Creates tuple (3, 5)
person = "Alice", 25, "NYC"  # Creates tuple

# Explicit packing
coords = (10, 20, 30)
```

### Unpacking

```python
# Basic unpacking
point = (3, 5)
x, y = point
print(f"x={x}, y={y}")  # x=3, y=5

# Multiple values
person = ("Alice", 25, "NYC")
name, age, city = person
print(f"{name} is {age} years old")

# Must match number of elements!
# name, age = person  # ValueError!
```

### Extended Unpacking (*)

```python
# Unpack first and rest
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5] (becomes list!)

# Unpack last and rest
*rest, last = numbers
print(rest)  # [1, 2, 3, 4]
print(last)  # 5

# Unpack first, middle, last
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Skip elements
first, _, third, *_ = numbers
print(first, third)  # 1 3
```

### Swapping Variables

```python
# Perfect use case for tuple unpacking!
a = 10
b = 20
print(f"Before: a={a}, b={b}")

# Swap without temporary variable
a, b = b, a
print(f"After: a={a}, b={b}")  # a=20, b=10

# Multiple swaps
x, y, z = 1, 2, 3
x, y, z = z, y, x  # Reverse
print(x, y, z)  # 3 2 1
```

### Unpacking in Loops

```python
# List of tuples
points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f"Point: ({x}, {y})")

# Dictionary items
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")
```

### Multiple Return Values

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)  # Returns tuple

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")

# Can also capture as tuple
result = get_min_max([1, 5, 3, 9, 2])
print(result)  # (1, 9)
```

---

## Named Tuples

### Creating Named Tuples

```python
from collections import namedtuple

# Define named tuple type
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(3, 5)
p2 = Point(x=10, y=20)

# Access by name (like attributes)
print(p1.x)  # 3
print(p1.y)  # 5

# Still works like regular tuple
print(p1[0])  # 3
print(p1[1])  # 5
```

### Named Tuple Examples

```python
from collections import namedtuple

# Person
Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person("Alice", 25, "NYC")
print(f"{alice.name} is {alice.age} years old")

# RGB Color
Color = namedtuple('Color', ['red', 'green', 'blue'])
purple = Color(128, 0, 128)
print(f"R:{purple.red}, G:{purple.green}, B:{purple.blue}")

# Date
Date = namedtuple('Date', ['year', 'month', 'day'])
today = Date(2024, 12, 1)
print(f"{today.year}/{today.month:02d}/{today.day:02d}")
```

### Named Tuple Methods

```python
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 5)

# _asdict() - convert to dictionary
print(p._asdict())  # {'x': 3, 'y': 5}

# _replace() - create new instance with changes
p2 = p._replace(x=10)
print(p2)  # Point(x=10, y=5)

# _fields - get field names
print(Point._fields)  # ('x', 'y')

# _make() - create from iterable
p3 = Point._make([7, 9])
print(p3)  # Point(x=7, y=9)
```

---

## Tuples vs Lists

### Immutability

```python
# List - mutable
list_data = [1, 2, 3]
list_data[0] = 10  # ✅ Works
list_data.append(4)  # ✅ Works

# Tuple - immutable
tuple_data = (1, 2, 3)
# tuple_data[0] = 10  # ❌ TypeError!
# tuple_data.append(4)  # ❌ AttributeError!
```

### When to Use Tuples

✅ **Use Tuples When:**
- Data shouldn't change (immutable)
- Need to use as dictionary key
- Need to use as set element
- Returning multiple values from function
- Fixed position has meaning (e.g., coordinates)

```python
# Dictionary keys (tuples OK, lists NOT OK)
locations = {
    (0, 0): "origin",
    (1, 0): "east"
}

# Set elements (tuples OK, lists NOT OK)
points = {(0, 0), (1, 0), (0, 1)}

# Function returns
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)
```

### When to Use Lists

✅ **Use Lists When:**
- Need to modify data
- Order matters but data changes
- Need methods like append, remove, etc.

```python
# Shopping cart (changes frequently)
cart = ["apple", "banana"]
cart.append("orange")
cart.remove("banana")

# User list (dynamic)
users = []
users.append("Alice")
users.append("Bob")
```

### Performance

```python
import sys

# Tuples use less memory
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_data)}")   # Larger
print(f"Tuple size: {sys.getsizeof(tuple_data)}") # Smaller

# Tuples are faster to create
import timeit

list_time = timeit.timeit('[1, 2, 3, 4, 5]', number=1000000)
tuple_time = timeit.timeit('(1, 2, 3, 4, 5)', number=1000000)

print(f"List: {list_time}")
print(f"Tuple: {tuple_time}")  # Faster!
```

---

## Tuple Use Cases

### 1. Multiple Return Values

```python
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns tuple

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")
```

### 2. Coordinates and Points

```python
# 2D point
point = (3, 5)
x, y = point

# 3D point
point_3d = (10, 20, 30)
x, y, z = point_3d

# GPS coordinates
location = (40.7128, -74.0060)  # NYC
latitude, longitude = location
```

### 3. RGB Colors

```python
# Colors as tuples
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Use in functions
def blend_colors(color1, color2):
    r = (color1[0] + color2[0]) // 2
    g = (color1[1] + color2[1]) // 2
    b = (color1[2] + color2[2]) // 2
    return (r, g, b)

purple = blend_colors(red, blue)
print(purple)  # (127, 0, 127)
```

### 4. Database Records

```python
# Student records
alice = ("Alice", 25, "CS", 3.8)
bob = ("Bob", 23, "Math", 3.5)

# Unpack
name, age, major, gpa = alice
print(f"{name}, {major}, GPA: {gpa}")
```

### 5. Configuration Data

```python
# Database config (shouldn't change)
DB_CONFIG = ("localhost", 5432, "mydb", "user")
host, port, database, user = DB_CONFIG

# Window size (fixed)
WINDOW_SIZE = (800, 600)
width, height = WINDOW_SIZE
```

---

## Practice Exercises

### Beginner

**Exercise 1**: Create a tuple with 5 elements
```python
# Create tuple: (1, 2, 3, 4, 5)
```

**Exercise 2**: Access tuple elements
```python
fruits = ("apple", "banana", "orange")
# Get second element
```

**Exercise 3**: Create single-element tuple
```python
# Create tuple with just number 42
```

**Exercise 4**: Concatenate tuples
```python
t1 = (1, 2)
t2 = (3, 4)
# Combine them
```

**Exercise 5**: Unpack tuple
```python
point = (10, 20)
# Unpack to x and y variables
```

### Intermediate

**Exercise 6**: Swap variables using tuple
```python
a = 5
b = 10
# Swap values
```

**Exercise 7**: Find element in tuple
```python
numbers = (1, 5, 3, 9, 2)
# Find index of 9
```

**Exercise 8**: Slice tuple
```python
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# Get elements from index 2 to 7
```

**Exercise 9**: Use tuple as dictionary key
```python
# Create dict mapping coordinate tuples to names
# (0, 0) -> "Origin"
# (1, 0) -> "East"
```

**Exercise 10**: Extended unpacking
```python
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Unpack first, last, and rest
```

### Advanced

**Exercise 11**: Named tuple for student
```python
# Create Student named tuple with name, id, major
# Create instance for "Alice", 12345, "CS"
```

**Exercise 12**: Function returning multiple values
```python
# Write function that returns min, max, and average of a list
def get_stats(numbers):
    # Your code here
    pass
```

**Exercise 13**: Convert list of tuples to dict
```python
pairs = [("a", 1), ("b", 2), ("c", 3)]
# Convert to dictionary
```

**Exercise 14**: Sort list of tuples
```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# Sort by score (second element)
```

**Exercise 15**: Nested tuple operations
```python
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# Get element at row 1, column 2
# Extract diagonal elements
```

---

## 🎯 Key Takeaways

✅ Tuples are **ordered** and **immutable**  
✅ Created with **()** or just commas  
✅ **Single element** needs comma: `(42,)`  
✅ Only 2 methods: **count()** and **index()**  
✅ **Packing**: `t = 1, 2, 3`  
✅ **Unpacking**: `a, b, c = t`  
✅ **Extended unpacking**: `first, *rest = t`  
✅ Perfect for **multiple returns** from functions  
✅ Can be **dict keys** and **set elements**  
✅ **Faster** and **lighter** than lists  

---

## 📚 Quick Reference

```python
# Creation
t = (1, 2, 3)
t = 1, 2, 3         # Packing
single = (42,)      # Single element
empty = ()

# Access
t[0]                # First
t[-1]               # Last
t[1:3]              # Slice

# Methods
t.count(value)
t.index(value)

# Operations
t1 + t2             # Concatenate
t * 3               # Repeat
len(t)
value in t

# Unpacking
a, b, c = t
first, *rest = t
*rest, last = t
first, *middle, last = t

# Swap
a, b = b, a

# Named tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 5)
print(p.x, p.y)
```

---

**End of Tuples Notes** 📝

Master tuples for efficient, immutable data handling!

## Tuple Performance Benefits

### Memory Efficiency

```python
import sys

# Tuples use less memory than lists
my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]

print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")
print(f"List size: {sys.getsizeof(my_list)} bytes")
# Tuple is smaller!
```

### Speed Comparison

```python
import timeit

# Tuples are faster to create
tuple_time = timeit.timeit('(1, 2, 3, 4, 5)', number=1000000)
list_time = timeit.timeit('[1, 2, 3, 4, 5]', number=1000000)

print(f"Tuple creation: {tuple_time:.4f} seconds")
print(f"List creation: {list_time:.4f} seconds")
# Tuple is faster!
```

---

## Advanced Tuple Techniques

### Tuple as Return Type Hint

```python
from typing import Tuple

def get_coordinates() -> Tuple[int, int]:
    """Return x, y coordinates"""
    return (10, 20)

def get_rgb() -> Tuple[int, int, int]:
    """Return RGB color values"""
    return (255, 128, 0)
```

### Nested Tuple Unpacking

```python
# Complex nested structures
data = ((1, 2), (3, 4), (5, 6))

# Unpack nested tuples
for (x, y) in data:
    print(f"Point: ({x}, {y})")

# Deeper nesting
nested = (1, (2, 3, (4, 5)))
a, (b, c, (d, e)) = nested
print(a, b, c, d, e)  # 1 2 3 4 5
```

### Tuple Concatenation Patterns

```python
# Combine multiple tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

# Chaining
combined = t1 + t2 + t3  # (1, 2, 3, 4, 5, 6)

# Using sum with start value
tuples = [(1, 2), (3, 4), (5, 6)]
result = sum(tuples, ())  # (1, 2, 3, 4, 5, 6)
```

---

## Tuple Best Practices

### DO's ✅

1. **Use for immutable data**
   ```python
   COORDINATES = (40.7128, -74.0060)  # NYC location
   RGB_RED = (255, 0, 0)
   ```

2. **Use as dictionary keys**
   ```python
   grid = {
       (0, 0): 'origin',
       (1, 0): 'right',
       (0, 1): 'up'
   }
   ```

3. **Return multiple values from functions**
   ```python
   def get_user_data():
       return ("Alice", 25, "alice@example.com")
   
   name, age, email = get_user_data()
   ```

4. **Use for sequence packing/unpacking**
   ```python
   # Swap values elegantly
   a, b = b, a
   
   # Multiple assignment
   x, y, z = 1, 2, 3
   ```

### DON'Ts ❌

1. **Don't use when data needs to change**
   ```python
   # ❌ BAD
   shopping_cart = ("apple", "banana")
   # Can't add items!
   
   # ✅ GOOD - use list instead
   shopping_cart = ["apple", "banana"]
   shopping_cart.append("orange")
   ```

2. **Don't forget the comma for single elements**
   ```python
   # ❌ WRONG
   single = (42)  # This is just an int!
   
   # ✅ CORRECT
   single = (42,)  # This is a tuple
   ```

---

## Common Patterns

### Pattern 1: Configuration Data

```python
# Database configuration
DB_CONFIG = (
    "localhost",  # host
    5432,         # port
    "mydb",       # database
    "user",       # username
    "pass"        # password
)

host, port, db, user, password = DB_CONFIG
```

### Pattern 2: Return Success and Value

```python
def divide(a, b):
    """Return (success, result) tuple"""
    if b == 0:
        return (False, None)
    return (True, a / b)

success, result = divide(10, 2)
if success:
    print(f"Result: {result}")
else:
    print("Division by zero!")
```

### Pattern 3: Enumerate with Tuples

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(f"{index}: {name}")
# enumerate returns tuples: (0, 'Alice'), (1, 'Bob'), ...
```

---

## Real-World Applications

### Application 1: Geographic Coordinates

```python
# Store locations as tuples
locations = {
    "home": (40.7128, -74.0060),
    "work": (40.7589, -73.9851),
    "gym": (40.7484, -73.9857)
}

def distance(coord1, coord2):
    """Calculate distance between coordinates"""
    import math
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat2-lat1)**2 + (lon2-lon1)**2)

dist = distance(locations['home'], locations['work'])
print(f"Distance: {dist:.4f}")
```

### Application 2: Color Management

```python
# RGB colors as tuples
COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

def blend_colors(color1, color2, ratio=0.5):
    """Blend two RGB colors"""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    
    r = int(r1 * (1-ratio) + r2 * ratio)
    g = int(g1 * (1-ratio) + g2 * ratio)
    b = int(b1 * (1-ratio) + b2 * ratio)
    
    return (r, g, b)

purple = blend_colors(COLORS['red'], COLORS['blue'])
print(f"Purple: {purple}")  # (127, 0, 127)
```

---

**End of Tuples Notes** ���

You've mastered Python tuples! Use them for immutable, structured data in your programs.
