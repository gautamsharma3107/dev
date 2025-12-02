# Lists in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Lists](#introduction-to-lists)
2. [Creating Lists](#creating-lists)
3. [Accessing List Elements](#accessing-list-elements)
4. [Modifying Lists](#modifying-lists)
5. [List Methods](#list-methods)
6. [List Operations](#list-operations)
7. [List Comprehensions](#list-comprehensions)
8. [2D Lists and Nested Lists](#2d-lists-and-nested-lists)
9. [List Best Practices](#list-best-practices)
10. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Create and manipulate lists effectively
- ✅ Use indexing and slicing to access elements
- ✅ Master 25+ list methods
- ✅ Understand list mutability
- ✅ Work with nested and 2D lists
- ✅ Use lists as stacks and queues
- ✅ Write efficient list comprehensions
- ✅ Apply best practices for list usage

---

## Introduction to Lists

### What are Lists?

**Lists** are ordered, mutable collections that can store multiple items. They're one of the most versatile and commonly used data structures in Python.

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "orange"]

# Mixed types (allowed!)
mixed = [1, "hello", 3.14, True]
```

**Real-World Analogy** 🌍

Think of a list like a shopping list or to-do list:
- Items are in order
- You can add new items
- You can cross off (remove) items
- You can check specific items
- You can reorganize items

###Key Characteristics

1. **Ordered** - Items maintain their position
2. **Mutable** - Can be changed after creation
3. **Allow duplicates** - Same value can appear multiple times
4. **Indexed** - Access items by position (0-based)
5. **Heterogeneous** - Can contain different types

```python
# Ordered
numbers = [3, 1, 4, 1, 5]
# Stays in this exact order

# Mutable  
fruits = ["apple", "banana"]
fruits.append("orange")  # Can modify!

# Duplicates allowed
numbers = [1, 1, 2, 2, 3]

# Indexed (0-based)
fruits = ["apple", "banana", "orange"]
#         0        1         2

# Mixed types
mixed = [42, "hello", 3.14, True, [1, 2, 3]]
```

---

## Creating Lists

### Empty List

```python
# Method 1: Square brackets
empty = []

# Method 2: list() constructor
also_empty = list()

print(len(empty))  # 0
```

### List with Initial Values

```python
# Numbers
numbers = [1, 2, 3, 4, 5]

# Strings
fruits = ["apple", "banana", "orange"]

# Mixed types
mixed = [1, "hello", 3.14, True]

# Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Using list() Constructor

```python
# From string (splits into characters)
chars = list("Python")
# ['P', 'y', 't', 'h', 'o', 'n']

# From range
numbers = list(range(5))
# [0, 1, 2, 3, 4]

numbers = list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# From tuple
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
# [1, 2, 3]
```

### Using List Comprehension

```python
# Squares of numbers 0-9
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### Repetition

```python
# Create list with repeated values
zeros = [0] * 5
# [0, 0, 0, 0, 0]

pattern = [1, 2] * 3
# [1, 2, 1, 2, 1, 2]
```

---

## Accessing List Elements

### Indexing

```python
fruits = ["apple", "banana", "orange", "grape", "mango"]
#         0        1         2         3        4      (positive index)
#        -5       -4        -3        -2       -1      (negative index)

# Positive indexing (from start)
print(fruits[0])   # "apple" (first)
print(fruits[1])   # "banana"
print(fruits[4])   # "mango" (last)

# Negative indexing (from end)
print(fruits[-1])  # "mango" (last)
print(fruits[-2])  # "grape" (second to last)
print(fruits[-5])  # "apple" (first)
```

### Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:stop]
print(numbers[2:5])    # [2, 3, 4] (indices 2, 3, 4)
print(numbers[0:3])    # [0, 1, 2]

# Omitting start/stop
print(numbers[:5])     # [0, 1, 2, 3, 4] (from beginning)
print(numbers[5:])     # [5, 6, 7, 8, 9] (to end)
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (entire list)

# Step parameter [start:stop:step]
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (every 2nd, starting from 1)
print(numbers[::3])    # [0, 3, 6, 9] (every 3rd)

# Negative step (reverse)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
print(numbers[8:2:-1]) # [8, 7, 6, 5, 4, 3] (backward from 8 to 3)

# Negative indices in slicing
print(numbers[-5:])    # [5, 6, 7, 8, 9] (last 5)
print(numbers[:-3])    # [0, 1, 2, 3, 4, 5, 6] (all but last 3)
print(numbers[-8:-3])  # [2, 3, 4, 5, 6]
```

### Checking if Item Exists

```python
fruits = ["apple", "banana", "orange"]

# Using 'in'
if "apple" in fruits:
    print("We have apples!")  # This executes

if "grape" in fruits:
    print("We have grapes")   # This doesn't execute

# Using 'not in'
if "grape" not in fruits:
    print("No grapes available")  # This executes
```

---

## Modifying Lists

### Changing Elements

```python
fruits = ["apple", "banana", "orange"]

# Change single element
fruits[1] = "grape"
print(fruits)  # ['apple', 'grape', 'orange']

# Change multiple elements via slicing
numbers = [0, 1, 2, 3, 4]
numbers[1:4] = [10, 20, 30]
print(numbers)  # [0, 10, 20, 30, 4]
```

### Adding Elements

```python
# append() - add to end
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# insert() - add at specific position
fruits.insert(1, "grape")  # Insert at index 1
print(fruits)  # ['apple', 'grape', 'banana', 'orange']

# extend() - add multiple items
fruits.extend(["mango", "kiwi"])
print(fruits)  # ['apple', 'grape', 'banana', 'orange', 'mango', 'kiwi']

# Using + operator
more_fruits = fruits + ["pear", "peach"]
print(more_fruits)

# Using += operator
fruits += ["cherry"]
print(fruits)
```

### Removing Elements

```python
fruits = ["apple", "banana", "orange", "grape", "mango"]

# remove() - remove first occurrence by value
fruits.remove("banana")
print(fruits)  # ['apple', 'orange', 'grape', 'mango']

# pop() - remove and return by index
last = fruits.pop()  # Removes and returns last item
print(last)    # 'mango'
print(fruits)  # ['apple', 'orange', 'grape']

second = fruits.pop(1)  # Remove and return index 1
print(second)  # 'orange'
print(fruits)  # ['apple', 'grape']

# del statement - remove by index or slice
numbers = [0, 1, 2, 3, 4, 5]
del numbers[0]
print(numbers)  # [1, 2, 3, 4, 5]

del numbers[1:3]
print(numbers)  # [1, 4, 5]

# clear() - remove all elements
fruits.clear()
print(fruits)  # []
```

---

## List Methods

### append(item)

Add item to end of list:

```python
fruits = ["apple", "banana"]
fruits.append("orange")
# ['apple', 'banana', 'orange']

# Note: append adds the item as a single element
fruits.append(["grape", "mango"])  # Adds list as single item
# ['apple', 'banana', 'orange', ['grape', 'mango']]
```

### extend(iterable)

Add all items from iterable:

```python
fruits = ["apple", "banana"]
fruits.extend(["orange", "grape"])
# ['apple', 'banana', 'orange', 'grape']

# Extend with string (adds each character!)
fruits.extend("hi")
# ['apple', 'banana', 'orange', 'grape', 'h', 'i']
```

### insert(index, item)

Insert item at specified index:

```python
fruits = ["apple", "banana", "orange"]
fruits.insert(1, "grape")  # Insert at index 1
# ['apple', 'grape', 'banana', 'orange']

fruits.insert(0, "mango")  # Insert at beginning
# ['mango', 'apple', 'grape', 'banana', 'orange']

fruits.insert(100, "kiwi")  # Index too large, adds to end
# ['mango', 'apple', 'grape', 'banana', 'orange', 'kiwi']
```

### remove(item)

Remove first occurrence of item:

```python
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)  # Removes first 2
# [1, 3, 2, 4]

# ValueError if item not in list
# numbers.remove(10)  # ValueError!

# Safe removal
if 10 in numbers:
    numbers.remove(10)
```

### pop([index])

Remove and return item at index (default: last):

```python
fruits = ["apple", "banana", "orange"]

last = fruits.pop()  # Remove and return last
print(last)    # 'orange'
print(fruits)  # ['apple', 'banana']

first = fruits.pop(0)  # Remove and return first
print(first)   # 'apple'
print(fruits)  # ['banana']
```

### clear()

Remove all elements:

```python
fruits = ["apple", "banana", "orange"]
fruits.clear()
print(fruits)  # []
```

### index(item[, start[, end]])

Return index of first occurrence:

```python
fruits = ["apple", "banana", "orange", "banana"]

print(fruits.index("banana"))  # 1 (first occurrence)

# Starting from index 2
print(fruits.index("banana", 2))  # 3

# ValueError if not found
# fruits.index("grape")  # ValueError!

# Safe search
if "grape" in fruits:
    idx = fruits.index("grape")
else:
    idx = -1
```

### count(item)

Count occurrences of item:

```python
numbers = [1, 2, 3, 2, 4, 2, 5]
print(numbers.count(2))  # 3
print(numbers.count(10)) # 0 (not found)

# Check for duplicates
if numbers.count(2) > 1:
    print("2 appears multiple times")
```

### sort([key][, reverse])

Sort list in-place:

```python
# Ascending order (default)
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# Sort strings
fruits = ["orange", "apple", "banana"]
fruits.sort()
print(fruits)  # ['apple', 'banana', 'orange']

# Sort by length
words = ["python", "is", "awesome", "!"]
words.sort(key=len)
print(words)  # ['!', 'is', 'python', 'awesome']

# Case-insensitive sort
words = ["Banana", "apple", "Cherry"]
words.sort(key=str.lower)
print(words)  # ['apple', 'Banana', 'Cherry']
```

### reverse()

Reverse list in-place:

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# Alternative: slicing (creates new list)
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]  # New list
print(reversed_numbers)  # [5, 4, 3, 2, 1]
print(numbers)           # [1, 2, 3, 4, 5] (original unchanged)
```

### copy()

Create shallow copy:

```python
original = [1, 2, 3]
copy = original.copy()

copy.append(4)
print(original)  # [1, 2, 3] (unchanged)
print(copy)      # [1, 2, 3, 4]

# Alternative methods
copy2 = original[:]  # Slicing
copy3 = list(original)  # list() constructor
```

---

## List Operations

### Concatenation (+)

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
# [1, 2, 3, 4, 5, 6]

# Multiple concatenations
result = [1] + [2, 3] + [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
```

### Repetition (*)

```python
zeros = [0] * 5
# [0, 0, 0, 0, 0]

pattern = [1, 2, 3] * 3
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Length

```python
fruits = ["apple", "banana", "orange"]
print(len(fruits))  # 3

empty = []
print(len(empty))  # 0
```

### Min, Max, Sum

```python
numbers = [5, 2, 8, 1, 9]

print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 25

# With strings (lexicographic)
words = ["zebra", "apple", "mango"]
print(min(words))  # 'apple'
print(max(words))  # 'zebra'
```

### Membership Testing

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True
```

### Iteration

```python
fruits = ["apple", "banana", "orange"]

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
# 1. apple
# 2. banana
# 3. orange
```

---

## List Comprehensions

### Basic Syntax

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (one line!)
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With Condition

```python
# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Squares of even numbers
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Filter list
numbers = [1, -2, 3, -4, 5, -6]
positives = [x for x in numbers if x > 0]
# [1, 3, 5]
```

### With If-Else

```python
# Categorize numbers
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']

# Absolute values
numbers = [1, -2, 3, -4, 5]
abs_values = [x if x >= 0 else -x for x in numbers]
# [1, 2, 3, 4, 5]
```

### Nested Comprehensions

```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create multiplication table
table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]
```

---

## 2D Lists and Nested Lists

### Creating 2D Lists

```python
# Method 1: Literal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Method 2: List comprehension
rows, cols = 3, 4
matrix = [[0 for j in range(cols)] for i in range(rows)]
# [[0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]]

# ⚠️ WRONG way (creates references to same list!)
wrong = [[0] * cols] * rows  # Don't do this!
```

### Accessing 2D List Elements

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access by [row][column]
print(matrix[0][0])  # 1 (first row, first column)
print(matrix[1][2])  # 6 (second row, third column)
print(matrix[2][1])  # 8 (third row, second column)

# Modify element
matrix[1][1] = 50
# [[1, 2, 3],
#  [4, 50, 6],
#  [7, 8, 9]]
```

### Iterating 2D Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate all elements
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row
# 1 2 3
# 4 5 6
# 7 8 9

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}] = {matrix[i][j]}")
```

---

## List Best Practices

### 1. Use List Comprehensions for Simple Transformations

```python
# ❌ Verbose
squares = []
for x in range(10):
    squares.append(x**2)

# ✅ Concise
squares = [x**2 for x in range(10)]
```

### 2. Don't Modify List While Iterating

```python
# ❌ BAD - can skip elements!
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# ✅ GOOD - iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # Slice creates copy
    if num % 2 == 0:
        numbers.remove(num)

# ✅ BETTER - create new list
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
```

### 3. Use enumerate() for Index and Value

```python
# ❌ BAD
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# ✅ GOOD
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### 4. Use sorted() for Sorted Copy

```python
numbers = [3, 1, 4, 1, 5]

# numbers.sort() modifies original
sorted_numbers = sorted(numbers)  # Creates new sorted list
print(numbers)         # [3, 1, 4, 1, 5] (unchanged)
print(sorted_numbers)  # [1, 1, 3, 4, 5]
```

### 5. Use extend() for Adding Multiple Items

```python
# ❌ SLOW
numbers = [1, 2, 3]
for x in [4, 5, 6]:
    numbers.append(x)

# ✅ FAST
numbers.extend([4, 5, 6])

# ✅ ALSO GOOD
numbers += [4, 5, 6]
```

---

## Practice Exercises

### Beginner

**Exercise 1**: Create a list of numbers 1 to 10

**Exercise 2**: Get the 3rd element from a list

**Exercise 3**: Add "grape" to end of fruits list

**Exercise 4**: Remove "banana" from fruits list

**Exercise 5**: Find length of a list

### Intermediate

**Exercise 6**: Reverse a list

**Exercise 7**: Find sum of all numbers in a list

**Exercise 8**: Remove all duplicates from a list

**Exercise 9**: Find second largest number in a list

**Exercise 10**: Merge two sorted lists into one sorted list

### Advanced

**Exercise 11**: Rotate list to right by k positions

**Exercise 12**: Find all pairs that sum to target value

**Exercise 13**: Flatten nested list of any depth

**Exercise 14**: Transpose a 2D matrix

**Exercise 15**: Implement binary search on sorted list

---

## 🎯 Key Takeaways

✅ Lists are **ordered, mutable** collections  
✅ Access elements by index (0-based) or slice [start:stop:step]  
✅ **25+ methods**: append, extend, insert, remove, pop, sort, reverse, etc.  
✅ List comprehensions provide concise syntax: [expr for item in iterable if condition]  
✅ Use copy() or [:] for shallow copy  
✅ **Don't modify list while iterating** - use copy or comprehension  
✅ enumerate() provides index and value together  
✅ sorted() returns new list, sort() modifies in-place  

---

## 📚 Quick Reference

```python
# Creation
lst = [1, 2, 3]
lst = list(range(5))
lst = [x**2 for x in range(10)]

# Access
lst[0]      # First element
lst[-1]     # Last element
lst[1:4]    # Slice
lst[::-1]   # Reverse

# Modify
lst.append(x)
lst.extend([a, b])
lst.insert(i, x)
lst.remove(x)
lst.pop()
lst.sort()
lst.reverse()

# Operations
len(lst)
min(lst)
max(lst)
sum(lst)
x in lst
```

---

**End of Lists Notes** 📝

Continue to `Dictionaries_Notes.md` for key-value pair operations!

## Advanced List Techniques

### List Aliasing and Copying

```python
# Aliasing (both reference same list)
original = [1, 2, 3]
alias = original
alias.append(4)
print(original)  # [1, 2, 3, 4] - both changed!

# Shallow copy (creates new list)
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)
copy1.append(4)
print(original)  # [1, 2, 3] - unchanged!
print(copy1)     # [1, 2, 3, 4]

# Deep copy (for nested lists)
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0].append(99)
print(original)  # [[1, 2, 99], [3, 4]] - affected!
print(shallow)   # [[1, 2, 99], [3, 4]]
print(deep)      # [[1, 2], [3, 4]] - unchanged!
```

### List Memory and Performance

```python
import sys

# Lists grow dynamically
small_list = [1, 2, 3]
print(sys.getsizeof(small_list))  # ~80 bytes

large_list = list(range(1000))
print(sys.getsizeof(large_list))  # ~9000+ bytes

# Pre-allocating can be faster
# Instead of:
result = []
for i in range(1000):
    result.append(i * 2)

# Use list comprehension:
result = [i * 2 for i in range(1000)]  # Faster!
```

### List as Stack (LIFO)

```python
# Stack operations: Last In, First Out
stack = []

# Push (add to top)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# Pop (remove from top)
top = stack.pop()
print(top)    # 3
print(stack)  # [1, 2]

# Peek (view top without removing)
if stack:
    top = stack[-1]
    print(f"Top: {top}")  # Top: 2
```

### List as Queue (FIFO)

```python
from collections import deque

# Use deque for efficient queue operations
queue = deque()

# Enqueue (add to back)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

# Dequeue (remove from front)
first = queue.popleft()
print(first)  # 1
print(queue)  # deque([2, 3])

# Regular list is slow for queue (pop(0) is O(n))
# ❌ BAD for large lists
slow_queue = [1, 2, 3]
slow_queue.pop(0)  # Slow! Shifts all elements

# ✅ GOOD: Use deque
fast_queue = deque([1, 2, 3])
fast_queue.popleft()  # Fast! O(1)
```

---

## List Patterns and Idioms

### Pattern 1: Removing Elements While Iterating

```python
# ❌ WRONG: Don't modify list while iterating
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Skips elements!

# ✅ CORRECT: List comprehension
numbers = [1, 2, 3, 4, 5, 6]
numbers = [num for num in numbers if num % 2 != 0]

# ✅ CORRECT: Iterate backwards
numbers = [1, 2, 3, 4, 5, 6]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
```

### Pattern 2: Flattening Nested Lists

```python
# Flatten 2D list
nested = [[1, 2], [3, 4], [5, 6]]

# Method 1: List comprehension
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# Method 2: Using sum()
flat = sum(nested, [])
print(flat)  # [1, 2, 3, 4, 5, 6]

# Method 3: itertools.chain
from itertools import chain
flat = list(chain.from_iterable(nested))
print(flat)  # [1, 2, 3, 4, 5, 6]

# Flatten deeply nested (recursive)
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

deep = [1, [2, [3, [4, 5]]]]
print(flatten(deep))  # [1, 2, 3, 4, 5]
```

### Pattern 3: Splitting Lists

```python
# Split list into chunks
def chunk_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunks = chunk_list(numbers, 3)
print(chunks)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Split at condition
def split_at(lst, condition):
    result = []
    current = []
    for item in lst:
        if condition(item):
            if current:
                result.append(current)
            current = []
        else:
            current.append(item)
    if current:
        result.append(current)
    return result

numbers = [1, 2, 0, 3, 4, 0, 5, 6]
parts = split_at(numbers, lambda x: x == 0)
print(parts)  # [[1, 2], [3, 4], [5, 6]]
```

---

## Real-World List Applications

### Application 1: Shopping Cart

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]
    
    def get_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def  show_cart(self):
        for item in self.items:
            print(f"{item['name']}: ${item['price']} x {item['quantity']}")
        print(f"Total: ${self.get_total():.2f}")

# Usage
cart = ShoppingCart()
cart.add_item("Apple", 0.99, 5)
cart.add_item("Banana", 0.59, 3)
cart.add_item("Orange", 1.29, 2)
cart.show_cart()
```

### Application 2: Task Priority Queue

```python
class TaskQueue:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task, priority):
        """Add task with priority (1=highest)"""
        self.tasks.append({'task': task, 'priority': priority})
        # Sort by priority
        self.tasks.sort(key=lambda x: x['priority'])
    
    def get_next_task(self):
        """Get highest priority task"""
        if self.tasks:
            return self.tasks.pop(0)
        return None
    
    def show_tasks(self):
        for i, item in enumerate(self.tasks, 1):
            print(f"{i}. [{item['priority']}] {item['task']}")

# Usage
queue = TaskQueue()
queue.add_task("Write report", 2)
queue.add_task("Fix critical bug", 1)
queue.add_task("Reply to email", 3)
queue.show_tasks()
next_task = queue.get_next_task()
print(f"\nNext: {next_task['task']}")
```

---

## List Performance Tips

### Tip 1: Use List Comprehension Over Loops

```python
import time

# ❌ SLOW
start = time.time()
result = []
for i in range(100000):
    result.append(i * 2)
slow_time = time.time() - start

# ✅ FAST
start = time.time()
result = [i * 2 for i in range(100000)]
fast_time = time.time() - start

print(f"Loop: {slow_time:.4f}s")
print(f"Comprehension: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")
```

### Tip 2: Use extend() Instead of += in Loops

```
python
# ❌ SLOW (creates new list each time)
result = []
for i in range(1000):
    result = result + [i]

# ✅ FAST (modifies in place)
result = []
for i in range(1000):
    result.append(i)

# ✅ EVEN BETTER (for multiple items)
result = []
for chunk in chunks:
    result.extend(chunk)  # Better than +=
```

### Tip 3: Check Membership in Sets, Not Lists

```python
# ❌ SLOW for large lists
large_list = list(range(10000))
if 9999 in large_list:  # O(n) - slow!
    print("Found")

# ✅ FAST with set
large_set = set(range(10000))
if 9999 in large_set:  # O(1) - fast!
    print("Found")
```

---

## Common List Mistakes

### Mistake 1: Default Mutable Arguments

```python
# ❌ WRONG
def add_item(item, items=[]):
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [1, 2] - unexpected!

# ✅ CORRECT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [2] - correct!
```

### Mistake 2: Infinite List Copying

```python
# ❌ WRONG
list1 = [1, 2, 3]
list2 = list1  # Not a copy!
list2.append(4)
print(list1)  # [1, 2, 3, 4] - modified!

# ✅ CORRECT
list1 = [1, 2, 3]
list2 = list1.copy()  # Real copy
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged
```

---

**End of Lists Notes** ���

Master Python lists for powerful data manipulation!
