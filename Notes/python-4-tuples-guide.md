# Python Tuples: Complete Guide

---

## Table of Contents
1. [Introduction to Tuples](#introduction-to-tuples)
2. [Creating Tuples](#creating-tuples)
3. [Accessing Tuple Elements](#accessing-tuple-elements)
4. [Tuple Immutability](#tuple-immutability)
5. [Tuple Packing and Unpacking](#tuple-packing-and-unpacking)
6. [Tuple Methods](#tuple-methods)
7. [Named Tuples](#named-tuples)
8. [Tuples vs Lists](#tuples-vs-lists)
9. [Common Tuple Operations](#common-tuple-operations)
10. [Practice Exercises](#practice-exercises)

---

## Introduction to Tuples

### What is a Tuple?
- **Ordered collection** of elements (like lists)
- **Immutable** - cannot be changed after creation (key difference from lists)
- **Heterogeneous** - can contain different data types
- **Zero-indexed** - first element at index 0
- **Fixed size** - cannot grow or shrink after creation
- **Hashable** - can be used as dictionary keys (if contains hashable elements)

### Why Use Tuples?

1. **Performance** - Faster than lists for read-only operations
2. **Safety** - Prevents accidental modification
3. **Dictionary Keys** - Can use tuples as keys (lists cannot)
4. **Immutability** - Thread-safe in multi-threaded programs
5. **Function Returns** - Return multiple values easily

### Comparison with Lists

| Feature | List | Tuple |
|---------|------|-------|
| Mutable | Yes | No |
| Speed | Slower | Faster |
| Syntax | `[]` | `()` |
| Dictionary Key | No | Yes (if hashable) |
| Memory | More | Less |
| Use Case | Changing data | Fixed data |

### Comparison with Other Languages

| Language | Equivalent |
|----------|-----------|
| Python   | tuple     |
| Java     | immutable List |
| C++      | std::tuple |
| C#       | Tuple<T> |

---

## Creating Tuples

### Empty Tuple

```python
empty_tuple = ()
another_empty = tuple()

print(len(empty_tuple))     # Output: 0
print(type(empty_tuple))    # Output: <class 'tuple'>
```

### Tuple with Elements

```python
# Basic tuple
numbers = (1, 2, 3, 4, 5)
names = ("Alice", "Bob", "Charlie")
mixed = (1, "hello", 3.14, True, None)

print(numbers)              # Output: (1, 2, 3, 4, 5)
print(type(numbers))        # Output: <class 'tuple'>
```

### Single Element Tuple (Important!)

```python
# WRONG - this is not a tuple, it's just a number in parentheses
single_wrong = (5)
print(type(single_wrong))   # Output: <class 'int'>

# CORRECT - use comma to make it a tuple
single_correct = (5,)
print(type(single_correct)) # Output: <class 'tuple'>

# Another correct way
single_also = 5,
print(type(single_also))    # Output: <class 'tuple'>
```

### Creating Tuples from Other Iterables

```python
# From list
list_data = [1, 2, 3]
tuple_from_list = tuple(list_data)
print(tuple_from_list)      # Output: (1, 2, 3)

# From string
string_data = "hello"
tuple_from_string = tuple(string_data)
print(tuple_from_string)    # Output: ('h', 'e', 'l', 'l', 'o')

# From range
tuple_from_range = tuple(range(5))
print(tuple_from_range)     # Output: (0, 1, 2, 3, 4)

# From set
set_data = {3, 1, 2}
tuple_from_set = tuple(set_data)
print(tuple_from_set)       # Output: (1, 2, 3) or different order
```

### Tuple with Repeated Elements

```python
zeros = (0,) * 5            # (0, 0, 0, 0, 0)
names = ("John",) * 3       # ('John', 'John', 'John')

print(zeros)
print(names)
```

---

## Accessing Tuple Elements

### Positive Indexing

```python
fruits = ("apple", "banana", "orange", "mango")
#          0        1          2         3

first = fruits[0]           # "apple"
second = fruits[1]          # "banana"
last = fruits[3]            # "mango"

print(first)                # Output: apple
```

### Negative Indexing

```python
fruits = ("apple", "banana", "orange", "mango")
#          -4       -3         -2        -1

last = fruits[-1]           # "mango"
second_last = fruits[-2]    # "orange"
first = fruits[-4]          # "apple"

print(last)                 # Output: mango
```

### Slicing Tuples

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing
first_three = numbers[0:3]      # (0, 1, 2)
middle = numbers[3:7]           # (3, 4, 5, 6)

# Using defaults
from_start = numbers[:5]        # (0, 1, 2, 3, 4)
from_middle = numbers[5:]       # (5, 6, 7, 8, 9)
all_elements = numbers[:]       # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# With step
every_second = numbers[::2]     # (0, 2, 4, 6, 8)
reversed_tuple = numbers[::-1]  # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

### Checking Membership

```python
fruits = ("apple", "banana", "orange")

if "banana" in fruits:
    print("Banana is in the tuple")

if "grape" not in fruits:
    print("Grape is not in the tuple")
```

### Finding Index

```python
fruits = ("apple", "banana", "orange", "banana")

pos = fruits.index("banana")
print(pos)                  # Output: 1 (first occurrence)

# Count occurrences
count = fruits.count("banana")
print(count)                # Output: 2
```

---

## Tuple Immutability

### What is Immutability?

Tuples cannot be modified after creation. You **cannot**:
- Add elements
- Remove elements
- Modify existing elements

### Examples of Immutability

```python
numbers = (1, 2, 3, 4, 5)

# ERROR - cannot modify element
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

# ERROR - cannot append
# numbers.append(6)  # AttributeError: 'tuple' object has no attribute 'append'

# ERROR - cannot remove
# numbers.remove(3)  # AttributeError: 'tuple' object has no attribute 'remove'

# ERROR - cannot delete element
# del numbers[0]  # TypeError: 'tuple' object doesn't support item deletion
```

### Creating Modified Tuples

To "modify" a tuple, create a new one:

```python
original = (1, 2, 3)

# Change one element
modified = (original[0], 99, original[2])
print(modified)             # Output: (1, 99, 3)

# Add element
extended = original + (4, 5)
print(extended)             # Output: (1, 2, 3, 4, 5)

# Convert to list, modify, convert back
as_list = list(original)
as_list[0] = 99
modified_again = tuple(as_list)
print(modified_again)       # Output: (99, 2, 3)

# Remove element using slicing
without_middle = original[:1] + original[2:]
print(without_middle)       # Output: (1, 3)
```

### Nested Tuples - Mutable Contents

```python
# Tuple contains a list (mutable)
mixed = (1, 2, [3, 4, 5])

# Cannot change the reference
# mixed[2] = [6, 7, 8]  # ERROR

# But CAN modify contents of the list
mixed[2][0] = 99
print(mixed)                # Output: (1, 2, [99, 4, 5])

# Tuple with tuple (immutable all the way)
pure = (1, 2, (3, 4, 5))
# Cannot modify anything
# pure[2][0] = 99  # ERROR
```

### Immutability Benefits

```python
# Use tuple as dictionary key
coordinates = {
    (0, 0): "origin",
    (1, 2): "point A",
    (3, 4): "point B"
}

print(coordinates[(0, 0)])  # Output: origin

# Lists cannot be dictionary keys
# ERROR:
# bad_dict = {[1, 2]: "value"}  # TypeError
```

---

## Tuple Packing and Unpacking

### Tuple Packing

Combining values into a single tuple:

```python
# Explicit packing
name = "Alice"
age = 25
salary = 50000

employee = (name, age, salary)
print(employee)             # Output: ('Alice', 25, 50000)

# Implicit packing (no parentheses needed)
packed = name, age, salary
print(packed)               # Output: ('Alice', 25, 50000)
print(type(packed))         # Output: <class 'tuple'>
```

### Tuple Unpacking

Extracting values from a tuple into separate variables:

```python
employee = ("Alice", 25, 50000)

# Basic unpacking
name, age, salary = employee
print(f"{name} is {age} years old and earns ${salary}")
# Output: Alice is 25 years old and earns $50000

# Unpacking with underscore (ignore values)
name, _, salary = employee
print(f"{name} earns ${salary}")
# Output: Alice earns $50000
```

### Unpacking with Multiple Values

```python
# Unpacking with * (extended unpacking)
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers
print(f"First: {first}")        # Output: First: 1
print(f"Middle: {middle}")      # Output: Middle: [2, 3, 4]
print(f"Last: {last}")          # Output: Last: 5

# Collecting first few
head, *tail = (10, 20, 30, 40)
print(f"Head: {head}")          # Output: Head: 10
print(f"Tail: {tail}")          # Output: Tail: [20, 30, 40]

# Multiple values at start and end
first, *middle, second_last, last = (1, 2, 3, 4, 5)
print(f"Middle: {middle}")      # Output: Middle: [2, 3]
```

### Unpacking in Loops

```python
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 95)
]

# Unpacking in loop
for name, score in students:
    print(f"{name}: {score}")

# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana: 95
```

### Unpacking in Function Calls

```python
def greet(first_name, last_name, age):
    print(f"Hello {first_name} {last_name}, you are {age} years old")

# Unpacking tuple as arguments
person = ("John", "Doe", 30)
greet(*person)
# Output: Hello John Doe, you are 30 years old

# Multiple tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = (*tuple1, *tuple2)
print(combined)                 # Output: (1, 2, 3, 4)
```

### Swapping Variables

```python
a = 5
b = 10

# Traditional swap (requires temp variable in other languages)
a, b = b, a

print(f"a = {a}, b = {b}")  # Output: a = 10, b = 5

# Swap in list
values = [1, 2, 3]
values[0], values[2] = values[2], values[0]
print(values)               # Output: [3, 2, 1]
```

---

## Tuple Methods

Tuples have very few methods (because they're immutable):

### count(element)

Returns number of occurrences:

```python
numbers = (1, 2, 2, 3, 2, 4)

count = numbers.count(2)
print(count)                # Output: 3

# Check if element exists
if numbers.count(5) > 0:
    print("5 exists")
else:
    print("5 does not exist")
```

### index(element)

Returns index of first occurrence:

```python
fruits = ("apple", "banana", "orange", "banana")

pos = fruits.index("banana")
print(pos)                  # Output: 1

# With error handling
try:
    pos = fruits.index("grape")
except ValueError:
    print("Element not found")
```

### len()

Returns number of elements:

```python
numbers = (1, 2, 3, 4, 5)
print(len(numbers))         # Output: 5
```

### min() and max()

```python
numbers = (5, 2, 9, 1, 8)

print(min(numbers))         # Output: 1
print(max(numbers))         # Output: 9
```

### sum()

```python
numbers = (1, 2, 3, 4, 5)
total = sum(numbers)
print(total)                # Output: 15
```

---

## Named Tuples

### Introduction to Named Tuples

Standard tuples use positional indexing. Named tuples let you access elements by name:

```python
from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(x=10, y=20)
p2 = Point(10, 20)  # Also works with positional args

# Access by name (clearer)
print(p1.x)                 # Output: 10
print(p1.y)                 # Output: 20

# Also access by index (like regular tuple)
print(p1[0])                # Output: 10
print(p1[1])                # Output: 20
```

### Named Tuple Definition Styles

```python
from collections import namedtuple

# Method 1: String with space-separated names
Student1 = namedtuple('Student1', 'name age score')

# Method 2: String with comma-separated names
Student2 = namedtuple('Student2', 'name, age, score')

# Method 3: List of names
Student3 = namedtuple('Student3', ['name', 'age', 'score'])

# All work the same way
s1 = Student1("Alice", 20, 85)
print(s1)                   # Output: Student1(name='Alice', age=20, score=85)
print(s1.name)              # Output: Alice
```

### Practical Named Tuple Examples

```python
from collections import namedtuple

# Example 1: Employee
Employee = namedtuple('Employee', ['name', 'department', 'salary'])

emp1 = Employee("Alice", "Engineering", 80000)
emp2 = Employee("Bob", "HR", 60000)

print(f"{emp1.name} works in {emp1.department}")
# Output: Alice works in Engineering

# Example 2: Coordinate
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude', 'altitude'])

location = Coordinate(28.6139, 77.2090, 216)
print(f"Latitude: {location.latitude}")
# Output: Latitude: 28.6139

# Example 3: RGB Color
Color = namedtuple('Color', ['red', 'green', 'blue'])

red = Color(255, 0, 0)
green = Color(0, 255, 0)

print(f"Red: {red}")        # Output: Red: Color(red=255, green=0, blue=0)
```

### Named Tuple Methods

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# _fields - get field names
print(Point._fields)        # Output: ('x', 'y')

# _asdict() - convert to dictionary
p_dict = p._asdict()
print(p_dict)               # Output: {'x': 10, 'y': 20}

# _replace() - create new tuple with replaced fields
p2 = p._replace(x=30)
print(p2)                   # Output: Point(x=30, y=20)
print(p)                    # Output: Point(x=10, y=20) - original unchanged

# _make() - create from iterable
values = [5, 15]
p3 = Point._make(values)
print(p3)                   # Output: Point(x=5, y=15)
```

### Named Tuple with Default Values (Python 3.7+)

```python
from collections import namedtuple

# Define with defaults
Person = namedtuple('Person', ['name', 'age', 'city'], defaults=['Unknown', 0, 'N/A'])

# Using defaults
p1 = Person("Alice")
print(p1)                   # Output: Person(name='Alice', age=0, city='N/A')

# Override defaults
p2 = Person("Bob", 30, "New York")
print(p2)                   # Output: Person(name='Bob', age=30, city='New York')
```

### Named Tuple vs Regular Tuple

```python
# Regular tuple
regular = ("Alice", 25, "Engineer")
print(regular[0])           # Output: Alice

# Named tuple
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'job'])
named = Person("Alice", 25, "Engineer")
print(named.name)           # Output: Alice
print(named[0])             # Output: Alice (also works)

# Named tuple is more readable
print(named)                # Output: Person(name='Alice', age=25, job='Engineer')
```

---

## Tuples vs Lists

### Side-by-Side Comparison

```python
# Creating
tuple_data = (1, 2, 3)
list_data = [1, 2, 3]

# Accessing
print(tuple_data[0])        # Works
print(list_data[0])         # Works

# Modifying
list_data[0] = 99           # Works
# tuple_data[0] = 99        # ERROR

# Adding
list_data.append(4)         # Works
# tuple_data.append(4)      # ERROR

# Using as key
dict1 = {tuple_data: "value"}   # Works
# dict2 = {list_data: "value"}  # ERROR

# Speed comparison
import timeit

# Time for creating
tuple_time = timeit.timeit('x = (1, 2, 3)', number=1000000)
list_time = timeit.timeit('x = [1, 2, 3]', number=1000000)
print(f"Tuple: {tuple_time:.4f}s, List: {list_time:.4f}s")
# Tuples are typically faster
```

### When to Use Each

| Use Tuple | Use List |
|-----------|----------|
| Fixed data | Growing data |
| Dictionary keys | Need to modify |
| Function returns | Collection of items |
| Immutable requirement | Need flexibility |
| Performance critical | Variable size |

---

## Common Tuple Operations

### Concatenation

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2
print(combined)             # Output: (1, 2, 3, 4, 5, 6)

# Multiple concatenation
result = tuple1 + tuple2 + (7, 8)
print(result)               # Output: (1, 2, 3, 4, 5, 6, 7, 8)
```

### Repetition

```python
tuple1 = (1, 2)

repeated = tuple1 * 3
print(repeated)             # Output: (1, 2, 1, 2, 1, 2)
```

### Iteration

```python
colors = ("red", "green", "blue")

# Simple iteration
for color in colors:
    print(color)

# With enumerate
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# With range and len
for i in range(len(colors)):
    print(f"Color {i}: {colors[i]}")
```

### Finding Length

```python
numbers = (1, 2, 3, 4, 5)
print(len(numbers))         # Output: 5
```

### Checking Membership

```python
fruits = ("apple", "banana", "orange")

print("banana" in fruits)       # Output: True
print("grape" not in fruits)    # Output: True
```

### Nested Tuples

```python
# 2D structure
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[0])            # Output: (1, 2, 3)
print(matrix[1][2])         # Output: 6

# Flatten nested tuples
flat = tuple(x for row in matrix for x in row)
print(flat)                 # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
```

### Converting Between Types

```python
# Tuple to list
t = (1, 2, 3)
lst = list(t)
print(lst)                  # Output: [1, 2, 3]

# List to tuple
lst = [1, 2, 3]
t = tuple(lst)
print(t)                    # Output: (1, 2, 3)

# String to tuple
s = "hello"
t = tuple(s)
print(t)                    # Output: ('h', 'e', 'l', 'l', 'o')

# Dictionary items to tuple
d = {"a": 1, "b": 2}
items = tuple(d.items())
print(items)                # Output: (('a', 1), ('b', 2))
```

---

## Practice Exercises

### 1. Basic Tuple Creation and Access
- Create a tuple with 5 different data types
- Access elements using positive and negative indexing
- Slice a tuple to get alternating elements

### 2. Tuple Immutability
- Try to modify a tuple and handle the error
- Create a new tuple by concatenating two tuples
- Convert tuple to list, modify, then convert back

### 3. Packing and Unpacking
- Pack multiple variables into a tuple
- Unpack a tuple with different techniques
- Swap two variables using tuple unpacking
- Use extended unpacking with * operator

### 4. Named Tuples
- Define a named tuple for Person (name, age, email)
- Create instances and access fields by name
- Use _asdict() and _replace() methods
- Create a list of named tuples and iterate

### 5. Tuple Methods
- Find count and index of elements
- Use min(), max(), and sum() on tuples
- Apply functions to tuple elements

### 6. Real-World Scenarios
- Use tuple as dictionary key for coordinates
- Return multiple values from function using tuple
- Create a structure of related data using named tuples
- Work with CSV-like data using named tuples

---

# End of Notes
