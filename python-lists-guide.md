# Python Lists: Complete Guide

---

## Table of Contents
1. [Introduction to Lists](#introduction-to-lists)
2. [Creating and Accessing Lists](#creating-and-accessing-lists)
3. [List Indexing](#list-indexing)
4. [List Slicing](#list-slicing)
5. [List Methods](#list-methods)
6. [List Comprehensions](#list-comprehensions)
7. [Nested Lists](#nested-lists)
8. [Common List Operations](#common-list-operations)
9. [Practice Exercises](#practice-exercises)

---

## Introduction to Lists

### What is a List?
- **Ordered collection** of elements
- **Mutable** - can be changed after creation (unlike strings)
- **Heterogeneous** - can contain different data types
- **Zero-indexed** - first element at index 0
- **Dynamic** - size can grow or shrink

### Comparison with Other Languages

| Language | Equivalent |
|----------|-----------|
| Python   | list      |
| Java     | ArrayList |
| C++      | vector    |
| C#       | List<T>   |

### List vs Other Collections

```python
# List - mutable, ordered, allows duplicates
my_list = [1, 2, 2, 3]

# Tuple - immutable, ordered
my_tuple = (1, 2, 3)

# Set - mutable, unordered, unique elements only
my_set = {1, 2, 3}

# Dictionary - mutable, key-value pairs
my_dict = {"a": 1, "b": 2}
```

---

## Creating and Accessing Lists

### Creating Lists

#### Empty List
```python
empty_list = []
another_empty = list()

print(len(empty_list))  # Output: 0
```

#### List with Initial Values
```python
# Different data types
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]

# Using list() constructor
converted = list("hello")  # ['h', 'e', 'l', 'l', 'o']
range_list = list(range(5))  # [0, 1, 2, 3, 4]
```

#### List with Repeated Elements
```python
zeros = [0] * 5         # [0, 0, 0, 0, 0]
names = ["John"] * 3    # ['John', 'John', 'John']
```

### Accessing List Elements

#### Positive Indexing
```python
fruits = ["apple", "banana", "orange", "mango"]
#          0        1          2         3

first = fruits[0]       # "apple"
second = fruits[1]      # "banana"
last_item = fruits[3]   # "mango"

print(first)            # Output: apple
```

#### Negative Indexing
```python
fruits = ["apple", "banana", "orange", "mango"]
#          -4       -3         -2        -1

last = fruits[-1]       # "mango" (last element)
second_last = fruits[-2] # "orange"
first = fruits[-4]      # "apple"

print(last)             # Output: mango
```

#### Index Out of Range Error
```python
numbers = [1, 2, 3]

# This will raise IndexError
# print(numbers[5])  # IndexError: list index out of range

# Safe way - use len()
if len(numbers) > 5:
    print(numbers[5])
else:
    print("Index not available")
```

#### Checking if Element Exists
```python
fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("Banana is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")
```

### Finding Index of Element

```python
fruits = ["apple", "banana", "orange", "banana"]

# index() returns first occurrence
pos = fruits.index("banana")
print(pos)              # Output: 1

# Using count() to find frequency
count = fruits.count("banana")
print(count)            # Output: 2

# Error if element doesn't exist
# print(fruits.index("grape"))  # ValueError

# Safe way
try:
    pos = fruits.index("grape")
except ValueError:
    print("Element not found")
```

---

## List Indexing

### Understanding Indexing

```python
word = "PYTHON"
lst = [10, 20, 30, 40, 50, 60]
#       0   1   2   3   4   5   (positive)
#      -6  -5  -4  -3  -2  -1   (negative)

# Access by positive index
print(lst[0])       # 10
print(lst[3])       # 40

# Access by negative index
print(lst[-1])      # 60
print(lst[-3])      # 40
```

### Modifying Elements by Index

```python
colors = ["red", "green", "blue"]

# Change single element
colors[0] = "yellow"
colors[-1] = "purple"

print(colors)       # Output: ['yellow', 'green', 'purple']

# Change multiple elements
colors[0:2] = ["orange", "pink"]
print(colors)       # Output: ['orange', 'pink', 'purple']
```

---

## List Slicing

### Basic Slicing Syntax
**Format:** `list[start:stop:step]`

- `start` - begin index (inclusive, default: 0)
- `stop` - end index (exclusive, default: end of list)
- `step` - increment/decrement (default: 1)

### Slicing Examples

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
first_three = numbers[0:3]      # [0, 1, 2]
middle = numbers[3:7]           # [3, 4, 5, 6]

# Using defaults
from_start = numbers[:5]        # [0, 1, 2, 3, 4]
from_middle = numbers[5:]       # [5, 6, 7, 8, 9]
all_elements = numbers[:]       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Slicing with Step

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

every_second = numbers[::2]     # [0, 2, 4, 6, 8]
every_third = numbers[::3]      # [0, 3, 6, 9]

# Step with start and stop
specific = numbers[1:8:2]       # [1, 3, 5, 7]
```

### Reverse Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reverse entire list
reversed_list = numbers[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Reverse from index 7 to 2 (backwards)
partial_reverse = numbers[7:2:-1]  # [7, 6, 5, 4, 3]
```

### Slice Assignment

```python
numbers = [1, 2, 3, 4, 5]

# Replace slice
numbers[1:4] = [20, 30, 40]
print(numbers)              # [1, 20, 30, 40, 5]

# Insert elements using slice
items = [1, 2, 3]
items[1:1] = [1.5]          # Insert without replacing
print(items)                # [1, 1.5, 2, 3]

# Delete slice
numbers = [1, 2, 3, 4, 5]
del numbers[1:4]
print(numbers)              # [1, 5]
```

---

## List Methods

### append(element)
Adds single element to end of list.

```python
fruits = ["apple", "banana"]

fruits.append("orange")
print(fruits)               # ['apple', 'banana', 'orange']

# Add different types
numbers = [1, 2, 3]
numbers.append([4, 5])      # Adds list as element!
print(numbers)              # [1, 2, 3, [4, 5]]
```

### extend(iterable)
Adds all elements from iterable to list.

```python
fruits = ["apple", "banana"]
more_fruits = ["orange", "mango"]

fruits.extend(more_fruits)
print(fruits)               # ['apple', 'banana', 'orange', 'mango']

# Different from append
numbers1 = [1, 2, 3]
numbers1.extend([4, 5])
print(numbers1)             # [1, 2, 3, 4, 5]

# Extend can take any iterable
str_list = ["a", "b"]
str_list.extend("cd")       # Extends with individual characters
print(str_list)             # ['a', 'b', 'c', 'd']
```

### insert(index, element)
Inserts element at specific position.

```python
colors = ["red", "green", "blue"]

# Insert at index 1
colors.insert(1, "yellow")
print(colors)               # ['red', 'yellow', 'green', 'blue']

# Insert at beginning
colors.insert(0, "white")
print(colors)               # ['white', 'red', 'yellow', 'green', 'blue']

# Insert at end
colors.insert(len(colors), "black")
print(colors)               # ['white', 'red', 'yellow', 'green', 'blue', 'black']

# Negative index
numbers = [1, 2, 3]
numbers.insert(-1, 2.5)     # Insert before last element
print(numbers)              # [1, 2, 2.5, 3]
```

### remove(element)
Removes first occurrence of element.

```python
fruits = ["apple", "banana", "orange", "banana"]

fruits.remove("banana")
print(fruits)               # ['apple', 'orange', 'banana']

# Error if element doesn't exist
# fruits.remove("grape")    # ValueError: list.remove(x): x not in list

# Safe removal
if "grape" in fruits:
    fruits.remove("grape")
else:
    print("Grape not found")
```

### pop(index)
Removes and returns element at index (default: last).

```python
numbers = [1, 2, 3, 4, 5]

# Remove last element
last = numbers.pop()
print(last)                 # 5
print(numbers)              # [1, 2, 3, 4]

# Remove at specific index
second = numbers.pop(1)
print(second)               # 2
print(numbers)              # [1, 3, 4]

# Pop with error handling
items = [10, 20]
while len(items) > 0:
    item = items.pop()
    print(item)
```

### sort(reverse=False)
Sorts list in place.

```python
# Sort numbers in ascending order
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)              # [1, 2, 5, 8, 9]

# Sort in descending order
numbers.sort(reverse=True)
print(numbers)              # [9, 8, 5, 2, 1]

# Sort strings
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)                # ['Alice', 'Bob', 'Charlie']

# Sort with key function
words = ["banana", "pie", "Washington", "book"]
words.sort(key=len)         # Sort by length
print(words)                # ['pie', 'book', 'banana', 'Washington']

# Sort case-insensitive
words = ["Apple", "banana", "Cherry"]
words.sort(key=str.lower)
print(words)                # ['Apple', 'banana', 'Cherry']
```

### sorted(iterable)
Returns new sorted list (doesn't modify original).

```python
numbers = [5, 2, 8, 1, 9]

# Original unchanged
sorted_nums = sorted(numbers)
print(numbers)              # [5, 2, 8, 1, 9]
print(sorted_nums)          # [1, 2, 5, 8, 9]

# With reverse
descending = sorted(numbers, reverse=True)
print(descending)           # [9, 8, 5, 2, 1]
```

### reverse()
Reverses list in place.

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)              # [5, 4, 3, 2, 1]

# Vs slicing (doesn't modify)
numbers = [1, 2, 3]
reversed_copy = numbers[::-1]
print(numbers)              # [1, 2, 3] (unchanged)
print(reversed_copy)        # [3, 2, 1]
```

### clear()
Removes all elements.

```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)              # []
print(len(numbers))         # 0
```

### copy()
Creates shallow copy of list.

```python
original = [1, 2, 3]

# Shallow copy - creates new list
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# Modify copy
copy1.append(4)
print(original)             # [1, 2, 3] (unchanged)
print(copy1)                # [1, 2, 3, 4]

# Note: shallow copy for nested lists
nested = [[1, 2], [3, 4]]
copy = nested.copy()
copy[0][0] = 99             # Modifies original!
print(nested)               # [[99, 2], [3, 4]]
```

### count(element)
Returns number of occurrences.

```python
numbers = [1, 2, 2, 3, 2, 4]

count = numbers.count(2)
print(count)                # 3

# Check if element exists
if numbers.count(5) > 0:
    print("5 exists")
else:
    print("5 does not exist")
```

---

## List Comprehensions

### Basic List Comprehension
**Syntax:** `[expression for item in iterable]`

```python
# Traditional approach
squares_traditional = []
for i in range(5):
    squares_traditional.append(i ** 2)

# List comprehension (cleaner)
squares = [i ** 2 for i in range(5)]
print(squares)              # [0, 1, 4, 9, 16]
```

### With Conditions
**Syntax:** `[expression for item in iterable if condition]`

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)                # [2, 4, 6, 8, 10]

# Convert to uppercase if length > 3
names = ["alice", "bob", "charlie", "diana"]
long_names_upper = [name.upper() for name in names if len(name) > 3]
print(long_names_upper)     # ['CHARLIE', 'DIANA']
```

### Nested List Comprehensions

```python
# Create multiplication table
multiplication_table = [
    [i * j for j in range(1, 4)]
    for i in range(1, 4)
]
print(multiplication_table)
# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in nested for x in row]
print(flattened)            # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Using if-else in List Comprehension

```python
# Conditional expression
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(result)
# Output: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# Replace values
values = [10, 20, 30, 40, 50]
adjusted = [x + 10 if x > 25 else x for x in values]
print(adjusted)             # [10, 20, 40, 50, 60]
```

### Common Patterns

```python
# Extract specific values
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
scores = [s["score"] for s in students]
print(scores)               # [85, 92, 78]

# String operations
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)              # [5, 5, 6]

# Remove duplicates (preserve order)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = []
unique_ordered = [x for x in numbers if x not in unique and not unique.append(x)]
# Better approach:
unique = list(dict.fromkeys(numbers))
print(unique)               # [1, 2, 3, 4]
```

---

## Nested Lists

### Creating Nested Lists

```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0])            # [1, 2, 3] (first row)
print(matrix[0][0])         # 1 (first element of first row)
print(matrix[2][1])         # 8 (second element of third row)
```

### Modifying Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Modify element
matrix[1][2] = 60
print(matrix)               # [[1, 2, 3], [4, 5, 60], [7, 8, 9]]

# Modify entire row
matrix[0] = [10, 20, 30]
print(matrix)               # [[10, 20, 30], [4, 5, 60], [7, 8, 9]]
```

### Iterating Over Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print each row
for row in matrix:
    print(row)

# Print each element
for row in matrix:
    for element in row:
        print(element, end=" ")
print()                     # Newline

# Using enumerate
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"matrix[{i}][{j}] = {element}")
```

### 3D Lists

```python
# 3D list (cube)
cube = [
    [[1, 2], [3, 4]],       # First plane
    [[5, 6], [7, 8]]        # Second plane
]

print(cube[0][0][0])        # 1
print(cube[1][1][1])        # 8

# Modifying
cube[0][1][0] = 33
print(cube)
```

### Common Nested List Operations

```python
# Sum all elements in nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = sum(sum(row) for row in matrix)
print(total)                # 45

# Find maximum
max_val = max(max(row) for row in matrix)
print(max_val)              # 9

# Transpose matrix
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transposed)
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Flatten list
flat = [x for row in matrix for x in row]
print(flat)                 # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Common List Operations

### Combining Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Method 1: Concatenation
combined = list1 + list2
print(combined)             # [1, 2, 3, 4, 5, 6]

# Method 2: extend()
list1.extend(list2)
print(list1)                # [1, 2, 3, 4, 5, 6]

# Method 3: Unpacking (Python 3.5+)
combined = [*list1, *list2]
print(combined)
```

### Finding Minimum and Maximum

```python
numbers = [5, 2, 9, 1, 8, 3]

minimum = min(numbers)
maximum = max(numbers)

print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9
```

### Sum and Average

```python
scores = [85, 90, 78, 92, 88]

total = sum(scores)
average = sum(scores) / len(scores)

print(f"Total: {total}, Average: {average}")
```

### Check Membership

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)        # True
print("grape" in fruits)        # False
print("grape" not in fruits)    # True
```

### List Iteration Methods

```python
numbers = [1, 2, 3, 4, 5]

# Using for loop
for num in numbers:
    print(num)

# Using enumerate
for index, num in enumerate(numbers):
    print(f"Index {index}: {num}")

# Using while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

### Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Method 1: Using set (loses order)
unique1 = list(set(numbers))
print(unique1)              # [1, 2, 3, 4] (order may vary)

# Method 2: Preserving order
unique2 = list(dict.fromkeys(numbers))
print(unique2)              # [1, 2, 3, 4]

# Method 3: Manual approach
unique3 = []
for num in numbers:
    if num not in unique3:
        unique3.append(num)
print(unique3)              # [1, 2, 3, 4]
```

---

## Practice Exercises

### 1. Basic Operations
- Create a list of 5 numbers and print each element using a loop
- Add elements to a list using append() and extend()
- Remove specific elements using remove() and pop()

### 2. Indexing and Slicing
- Create a list and access elements using positive and negative indices
- Slice a list to get every second element
- Reverse a list using slicing

### 3. List Methods
- Sort a list of strings in alphabetical order
- Find the count and index of elements
- Copy a list and modify the copy without changing original

### 4. List Comprehensions
- Create a list of squares for numbers 1-10 using comprehension
- Filter odd numbers from a list using comprehension
- Create a list of string lengths using comprehension

### 5. Nested Lists
- Create a 3x3 matrix and print all elements
- Transpose a matrix
- Calculate the sum of all elements in a nested list

### 6. Real-World Scenarios
- Maintain a to-do list with add, remove, and display functionality
- Process student data (list of dictionaries) to find scores above a threshold
- Create a frequency counter for words in a sentence

---

# End of Notes
