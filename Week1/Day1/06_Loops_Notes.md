# Loops in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Loops](#introduction-to-loops)
2. [For Loops](#for-loops)
3. [While Loops](#while-loops)
4. [Loop Control Statements](#loop-control-statements)
5. [Nested Loops](#nested-loops)
6. [Loop Patterns](#loop-patterns)
7. [Loop Best Practices](#loop-best-practices)
8. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Understand when to use for vs while loops
- ✅ Master the range() function
- ✅ Use break, continue, and else with loops
- ✅ Create nested loops for complex patterns
- ✅ Iterate over different data structures
- ✅ Write efficient and Pythonic loops
- ✅ Apply common loop patterns

---

## Introduction to Loops

### What are Loops?

**Loops** allow you to execute a block of code repeatedly. Instead of writing the same code multiple times, you write it once and loop through it.

**Real-World Analogy** 🌍

Think of a washing machine cycle - it repeats the same washing action multiple times until the clothes are clean. Similarly, loops repeat code until a condition is met.

### Types of Loops in Python

1. **for loop** - Iterate over a sequence (list, string, range, etc.)
2. **while loop** - Repeat while a condition is True

```python
# for loop - "for each item in sequence"
for i in range(5):
    print(i)

# while loop - "while condition is true"
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## For Loops

### Basic For Loop

```python
# Loop through numbers 0-4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Loop with custom message
for i in range(3):
    print(f"Iteration {i + 1}")
# Output:
# Iteration 1
# Iteration 2
# Iteration 3
```

### The range() Function

`range()` generates a sequence of numbers:

```python
# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - from start to stop-1
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step) - with custom increment
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Counting backwards
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1

# Negative range
for i in range(-5, 0):
    print(i)  # -5, -4, -3, -2, -1
```

**Common Patterns:**
```python
# Print 1 to 10
for i in range(1, 11):
    print(i)

# Print even numbers 0-10
for i in range(0, 11, 2):
    print(i)

# Print odd numbers 1-10
for i in range(1, 11, 2):
    print(i)

# Countdown
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```

### Looping Through Lists

```python
fruits = ["apple", "banana", "orange"]

# Method 1: Direct iteration (Pythonic!)
for fruit in fruits:
    print(fruit)

# Method 2: Using index
for i in range(len(fruits)):
    print(fruits[i])

# Method 3: With index and value (Best!)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: orange
```

### Looping Through Strings

```python
text = "Python"

# Each character
for char in text:
    print(char)
# P
# y
# t
# h
# o
# n

# With index
for i, char in enumerate(text):
    print(f"Index {i}: {char}")
```

### Looping Through Dictionaries

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Loop through keys
for key in person:
    print(key)
# name, age, city

# Loop through values
for value in person.values():
    print(value)
# Alice, 25, New York

# Loop through key-value pairs (Best!)
for key, value in person.items():
    print(f"{key}: {value}")
# name: Alice
# age: 25
# city: New York
```

### Looping Through Multiple Lists (zip)

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# Combine lists with zip()
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
# Alice is 25 years old and lives in NYC
# Bob is 30 years old and lives in LA
# Charlie is 35 years old and lives in Chicago
```

---

## While Loops

### Basic While Loop

```python
# Count to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# Output: 1, 2, 3, 4, 5

# Important: Must update the condition variable!
# Otherwise infinite loop!
```

### While with User Input

```python
# Keep asking until correct password
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Better with attempt limit
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"{attempts} attempts remaining")
```

### While True (Infinite Loop with Break)

```python
# Menu system
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Exit")
    choice = input("Choose option: ")
    
    if choice == "3":
        break
    elif choice == "1":
        print("Adding...")
    elif choice == "2":
        print("Subtracting...")
    else:
        print("Invalid choice!")
```

### For vs While - When to Use

**Use for** when:
- You know how many iterations needed
- Iterating over a sequence
- Working with ranges

```python
# Perfect for 'for' loop
for i in range(10):
    print(i)

for fruit in fruits:
    print(fruit)
```

**Use while** when:
- Number of iterations unknown
- Condition-based termination
- User input loops

```python
# Perfect for 'while' loop
while temperature > 100:
    cool_down()

while not valid_input:
    get_user_input()
```

---

## Loop Control Statements

### Break - Exit Loop Early

Immediately exits the loop:

```python
# Stop when found
numbers = [1, 3, 5, 7, 2, 9]
for num in numbers:
    print(num)
    if num % 2 == 0:  # Found even number
        print("Found even number!")
        break
# Output: 1, 3, 5, 7, 2, Found even number!

# Search example
names = ["Alice", "Bob", "Charlie", "Dave"]
search = "Charlie"
for name in names:
    if name == search:
        print(f"Found {search}!")
        break
else:  # This runs if break was NOT called
    print(f"{search} not found")
```

### Continue - Skip Current Iteration

Skips rest of current iteration, continues with next:

```python
# Skip odd numbers
for i in range(10):
    if i % 2 != 0:  # If odd
        continue    # Skip to next iteration
    print(i)
# Output: 0, 2, 4, 6, 8

# Skip specific values
numbers = [1, 2, -3, 4, -5, 6]
for num in numbers:
    if num < 0:
        continue  # Skip negatives
    print(num)
# Output: 1, 2, 4, 6
```

### Else Clause with Loops

The `else` block runs if loop completes WITHOUT break:

```python
# Search with else
numbers = [1, 3, 5, 7, 9]
search = 4

for num in numbers:
    if num == search:
        print(f"Found {search}!")
        break
else:  # Runs if break was NOT called
    print(f"{search} not found")
# Output: 4 not found

# Check if all pass
scores = [85, 92, 78, 95]
passing_grade = 60

for score in scores:
    if score < passing_grade:
        print("At least one failing score")
        break
else:  # All scores passed!
    print("All scores passed!")
```

### Pass - Do Nothing

Placeholder for empty loop body:

```python
# Coming soon...
for i in range(5):
    pass  # TODO: implement later

# Commonly used in development
while condition:
    pass  # Placeholder
```

---

## Nested Loops

### Basic Nested Loop

Loop inside another loop:

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # Blank line after each row

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
#
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ...
```

### 2D List (Matrix) Iteration

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print each element
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}] = {matrix[i][j]}")
```

### Pattern Printing

```python
# Right triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# Output:
# *
# **
# ***
# ****
# *****

# Square
size = 5
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Number pyramid
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
```

---

## Loop Patterns

### Accumulator Pattern

```python
# Sum of numbers
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55

# Product
product = 1
for i in range(1, 6):
    product *= i
print(product)  # 120 (factorial of 5)

# Count matches
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(even_count)  # 5
```

### Filter Pattern

```python
# Filter positive numbers
numbers = [1, -2, 3, -4, 5, -6]
positive = []
for num in numbers:
    if num > 0:
        positive.append(num)
print(positive)  # [1, 3, 5]

# Better with list comprehension
positive = [num for num in numbers if num > 0]
```

### Transform Pattern

```python
# Square each number
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # [1, 4, 9, 16, 25]

# Better with list comprehension
squared = [num ** 2 for num in numbers]
```

### Search Pattern

```python
# Linear search
numbers = [10, 20, 30, 40, 50]
target = 30
found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print(f"{target} found!")
else:
    print(f"{target} not found")

# Better with 'in'
if target in numbers:
    print(f"{target} found!")
```

### Min/Max Pattern

```python
# Find maximum
numbers = [23, 45, 12, 67, 34]
max_val = numbers[0]  # Start with first

for num in numbers:
    if num > max_val:
        max_val = num
print(max_val)  # 67

# Better with built-in
max_val = max(numbers)

# Find minimum
min_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num
print(min_val)  # 12
```

---

## Loop Best Practices

### 1. Use Meaningful Variable Names

```python
# ❌ BAD
for i in items:
    print(i)

# ✅ GOOD
for item in items:
    print(item)

# ❌ BAD
for x in students:
    print(x)

# ✅ GOOD
for student in students:
    print(student)
```

### 2. Use enumerate() for Index + Value

```python
#❌ BAD
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# ✅ GOOD
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start index from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
```

### 3. Use zip() for Multiple Lists

```python
# ❌ BAD
names = ["Alice", "Bob"]
ages = [25, 30]
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]}")

# ✅ GOOD
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### 4. Avoid Modifying List While Iterating

```python
# ❌ BAD - Can cause issues
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# ✅ GOOD - Create new list
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]

# ✅ GOOD - Iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # Slice creates copy
    if num % 2 == 0:
        numbers.remove(num)
```

### 5. Use List Comprehensions When Appropriate

```python
# ❌ Verbose
squares = []
for i in range(10):
    squares.append(i ** 2)

# ✅ Concise
squares = [i ** 2 for i in range(10)]

# But keep loops for complex logic
# ✅ GOOD - Complex logic stays readable
results = []
for item in data:
    if condition1:
        processed = process(item)
        if condition2:
            results.append(processed)
```

### 6. Avoid Infinite Loops

```python
# ❌ BAD - Infinite loop!
while True:
    print("Help!")
    # No break statement!

# ✅ GOOD - Clear exit condition
MAX_ATTEMPTS = 5
attempts = 0
while attempts < MAX_ATTEMPTS:
    if check_condition():
        break
    attempts += 1
```

---

## Practice Exercises

### Beginner Exercises

**Exercise 1: Print 1 to 10**
```python
# Use a for loop to print numbers 1 to 10
```

**Exercise 2: Sum of Numbers**
```python
# Calculate sum of numbers from 1 to 100
```

**Exercise 3: Countdown**
```python
# Print countdown from 10 to 1, then "Blast off!"
```

**Exercise 4: Even Numbers**
```python
# Print all even numbers between 1 and 20
```

**Exercise 5: Multiplication Table**
```python
# Print the 5 times table (5 x 1 = 5, 5 x 2 = 10, ...)
```

### Intermediate Exercises

**Exercise 6: Factorial**
```python
# Calculate factorial of n
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
n = 5
```

**Exercise 7: Reverse a String**
```python
# Reverse "Python" to "nohtyP" using a loop
text = "Python"
```

**Exercise 8: Count Vowels**
```python
# Count vowels in a string
text = "Hello World"
```

**Exercise 9: Find Prime Numbers**
```python
# Find all prime numbers between 1 and 50
```

**Exercise 10: Fibonacci Sequence**
```python
# Generate first 10 Fibonacci numbers
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### Advanced Exercises

**Exercise 11: Pattern - Right Triangle**
```python
# Print:
# *
# **
# ***
# ****
# *****
```

**Exercise 12: Pattern - Pyramid**
```python
# Print:
#     *
#    ***
#   *****
#  *******
# *********
```

**Exercise 13: Number Guessing Game**
```python
# Computer picks random number 1-100
# Player guesses, computer says higher/lower
# Count number of guesses
import random
```

**Exercise 14: Prime Factorization**
```python
# Find prime factors of a number
# Example: 60 = 2 × 2 × 3 × 5
number = 60
```

**Exercise 15: Matrix Transpose**
```python
# Transpose a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Result should be:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
```

---

## 🎯 Key Takeaways

✅ **for loops** iterate over sequences (lists, strings, ranges)  
✅ **while loops** repeat while a condition is True  
✅ **range(start, stop, step)** generates number sequences  
✅ **break** exits loop, **continue** skips to next iteration  
✅ **else** clause runs if loop completes without break  
✅ **enumerate()** provides index and value  
✅ **zip()** combines multiple iterables  
✅ Avoid modifying lists while iterating over them  
✅ Use for loop when iterations known, while for condition-based  

---

## 📚 Quick Reference

```python
# For loop
for item in sequence:
    # code

# Range
range(5)           # 0,1,2,3,4
range(2, 7)        # 2,3,4,5,6
range(0, 10, 2)    # 0,2,4,6,8

# While loop
while condition:
    # code

# Loop control
break      # Exit loop
continue   # Skip to next iteration
pass       # Do nothing

# Enumerate
for i, item in enumerate(items):
    print(i, item)

# Zip
for x, y in zip(list1, list2):
    print(x, y)

# Else clause
for item in items:
    if condition:
        break
else:
    # Runs if no break
```

---

**End of Loops Notes** 📝

**Next:** `Control_Flow_Notes.md` for if-else statements and decision making!

## Advanced Loop Techniques

### Loop with enumerate() and Multiple Variables

```python
# Unpack tuples in enumerate
pairs = [('a', 1), ('b', 2), ('c', 3)]
for index, (letter, number) in enumerate(pairs):
    print(f"{index}: {letter} = {number}")
# 0: a = 1
# 1: b = 2
# 2: c = 3

# Enumerate with custom start
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. orange
```

### Loop with zip() Advanced

```python
# Zip multiple lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# zip() stops at shortest list
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b']
for num, letter in zip(list1, list2):
    print(num, letter)
# Only 2 iterations: (1, 'a'), (2, 'b')

# Use itertools.zip_longest for all elements
from itertools import zip_longest
for num, letter in zip_longest(list1, list2, fillvalue='?'):
    print(num, letter)
# 5 iterations: (1, 'a'), (2, 'b'), (3, '?'), (4, '?'), (5, '?')
```

### Dictionary Iteration Patterns

```python
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}

# Iterate over keys (default)
for name in scores:
    print(name)

# Iterate over values
for score in scores.values():
    print(score)

# Iterate over key-value pairs
for name, score in scores.items():
    print(f"{name}: {score}")

# Iterate with index
for i, (name, score) in enumerate(scores.items(), 1):
    print(f"{i}. {name}: {score}")
```

---

## Loop Control Advanced Patterns

### Multiple Break Points

```python
def find_in_matrix(matrix, target):
    """Find element in 2D matrix"""
    found = False
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                print(f"Found {target} at ({i}, {j})")
                found = True
                break
        if found:
            break
    else:
        print(f"{target} not found")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
find_in_matrix(matrix, 5)  # Found 5 at (1, 1)
```

### Using Flags with Break

```python
# Search with early exit
def find_duplicate(items):
    """Find first duplicate"""
    seen = set()
    for item in items:
        if item in seen:
            return item  # Found duplicate, exit
        seen.add(item)
    return None  # No duplicate found

numbers = [1, 2, 3, 4, 2, 5]
dup = find_duplicate(numbers)
print(f"First duplicate: {dup}")  # First duplicate: 2
```

### Continue with Conditions

```python
# Skip processing based on multiple conditions
for number in range(1, 21):
    # Skip multiples of 2 but not multiples of 10
    if number % 2 == 0 and number % 10 != 0:
        continue
    
    # Skip numbers ending in 5
    if number % 10 == 5:
        continue
    
    print(number)
# Prints: 1, 3, 7, 9, 10, 11, 13, 17, 19
```

---

## Loop Performance Optimization

### List Comprehension vs Loop

```python
import time

# Timing function
def time_it(func):
    start = time.time()
    result = func()
    return time.time() - start, result

# Regular loop
def with_loop():
    result = []
    for i in range(100000):
        if i % 2 == 0:
            result.append(i * 2)
    return result

# List comprehension
def with_comprehension():
    return [i * 2 for i in range(100000) if i % 2 == 0]

loop_time, _ = time_it(with_loop)
comp_time, _ = time_it(with_comprehension)

print(f"Loop: {loop_time:.4f}s")
print(f"Comprehension: {comp_time:.4f}s")
print(f"Speedup: {loop_time/comp_time:.1f}x")
```

### Generator Expressions for Memory

```python
import sys

# List comprehension (stores all in memory)
squares_list = [x**2 for x in range(100000)]
print(f"List size: {sys.getsizeof(squares_list)} bytes")

# Generator expression (generates on demand)
squares_gen = (x**2 for x in range(100000))
print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")

# Generator is MUCH smaller!
# Use when you only need to iterate once
for square in squares_gen:
    if square > 1000:
        break  # Can stop early, saving computation
```

---

## Real-World Loop Applications

### Application 1: Processing CSV Data

```python
def process_csv(filename):
    """Process CSV file line by line"""
    with open(filename, 'r') as file:
        # Skip header
        next(file)
        
        total = 0
        count = 0
        
        for line in file:
            # Parse CSV line
            parts = line.strip().split(',')
            if len(parts) >= 3:
                name, age, salary = parts[0], int(parts[1]), float(parts[2])
                total += salary
                count += 1
                
                # Print employee info
                print(f"{name}: {age} years, ${salary:,.2f}")
        
        # Calculate average
        if count > 0:
            avg = total / count
            print(f"\nAverage salary: ${avg:,.2f}")

# Example usage (if file exists):
# process_csv('employees.csv')
```

### Application 2: Batch Processing with Progress

```python
def process_batch(items, batch_size=10):
    """Process items in batches with progress"""
    total = len(items)
    
    for i in range(0, total, batch_size):
        batch = items[i:i+batch_size]
        
        # Process batch
        for item in batch:
            # Simulate processing
            pass
        
        # Show progress
        progress = min(i + batch_size, total)
        percent = (progress / total) * 100
        print(f"Processed {progress}/{total} items ({percent:.1f}%)")

# Usage
items = list(range(100))
process_batch(items, batch_size=25)
```

### Application 3: Menu System Loop

```python
def menu_system():
    """Interactive menu with loop"""
    options = {
        '1': 'View Profile',
        '2': 'Edit Settings',
        '3': 'View Stats',
        '4': 'Help',
        '5': 'Exit'
    }
    
    while True:
        print("\n=== Main Menu ===")
        for key, value in options.items():
            print(f"{key}. {value}")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            print("Viewing profile...")
        elif choice == '2':
            print("Editing settings...")
        elif choice == '3':
            print("Viewing stats...")
        elif choice == '4':
            print("Help information...")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            continue
        
        # Ask to continue
        if input("\nPress Enter to return to menu (or 'q' to quit): ") == 'q':
            break

# menu_system()  # Uncomment to run
```

---

## Loop Patterns Collection

### Pattern 1: Running Average

```python
def running_average(numbers):
    """Calculate running average"""
    total = 0
    for i, num in enumerate(numbers, 1):
        total += num
        avg = total / i
        print(f"After {i} numbers: average = {avg:.2f}")

running_average([10, 20, 30, 40, 50])
# After 1 numbers: average = 10.00
# After 2 numbers: average = 15.00
# After 3 numbers: average = 20.00
# After 4 numbers: average = 25.00
# After 5 numbers: average = 30.00
```

### Pattern 2: Sliding Window

```python
def sliding_window(lst, window_size):
    """Process list elements in sliding window"""
    for i in range(len(lst) - window_size + 1):
        window = lst[i:i+window_size]
        print(f"Window {i}: {window}, sum = {sum(window)}")

numbers = [1, 2, 3, 4, 5, 6]
sliding_window(numbers, 3)
# Window 0: [1, 2, 3], sum = 6
# Window 1: [2, 3, 4], sum = 9
# Window 2: [3, 4, 5], sum = 12
# Window 3: [4, 5, 6], sum = 15
```

### Pattern 3: Pairwise Iteration

```python
def pairwise(lst):
    """Iterate over pairs of consecutive elements"""
    for i in range(len(lst) - 1):
        current = lst[i]
        next_item = lst[i + 1]
        print(f"Pair: ({current}, {next_item})")

pairwise([1, 2, 3, 4, 5])
# Pair: (1, 2)
# Pair: (2, 3)
# Pair: (3, 4)
# Pair: (4, 5)

# Or using zip
def pairwise_zip(lst):
    for a, b in zip(lst, lst[1:]):
        print(f"Pair: ({a}, {b})")
```

---

## Loop Best Practices

### DO's ✅

1. **Use list comprehensions** when possible
2. **Use enumerate()** instead of range(len())
3. **Use zip()** for parallel iteration
4. **Break early** when condition is met
5. **Use generator expressions** for large datasets

```python
# ✅ GOOD examples
squares = [x**2 for x in range(10)]
for i, item in enumerate(items):
    print(i, item)
for a, b in zip(list1, list2):
    if a == target:
        break
```

### DON'Ts ❌

1. **Don't modify list while iterating**
2. **Don't use range(len()) unnecessarily**
3. **Don't nest too deeply** (max 2-3 levels)
4. **Don't use while True without break**
5. **Don't ignore loop else clause**

```python
# ❌ BAD examples
for i in range(len(items)):  # Use enumerate instead
    print(items[i])

while True:  # No break condition!
    do_something()
```

---

##Common Loop Mistakes

### Mistake 1: Modifying List During Iteration

```python
# ❌ WRONG
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Skips elements!
print(numbers)  # [1, 3, 5] but missed 6!

# ✅ CORRECT
numbers = [1, 2, 3, 4, 5, 6]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]
```

### Mistake 2: Infinite Loop Without Exit

```python
# ❌ WRONG
while True:
    do_something()  # Never exits!

# ✅ CORRECT
max_iterations = 1000
iteration = 0
while True:
    do_something()
    iteration += 1
    if iteration >= max_iterations:
        break
```

---

**End of Loops Notes** ���

Master Python loops for efficient iteration and control flow!
