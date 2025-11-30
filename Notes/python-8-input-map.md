# Python Input and Map: Complete Guide

---

## Table of Contents
1. [Introduction](#introduction)
2. [Input Function](#input-function)
3. [Processing Input](#processing-input)
4. [Map Function](#map-function)
5. [Map with Built-in Functions](#map-with-built-in-functions)
6. [Map with Lambda Functions](#map-with-lambda-functions)
7. [Map vs List Comprehension](#map-vs-list-comprehension)
8. [Other Higher-Order Functions](#other-higher-order-functions)
9. [Practical Examples](#practical-examples)
10. [Practice Exercises](#practice-exercises)

---

## Introduction

### Input and Map Overview

**input()** - Get user input from console
**map()** - Apply function to each element in iterable

Both are essential for interactive programs and data transformation.

---

## Input Function

### Basic Input

```python
# Get user input (always returns string)
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Output example:
# Enter your name: Alice
# Hello, Alice!
```

### Important: input() Returns String

```python
# input() always returns a string
user_input = input("Enter a number: ")
print(type(user_input))     # Output: <class 'str'>

# Even if user enters a number
age_str = input("Enter your age: ")
print(age_str)              # "25" (string, not int)
print(type(age_str))        # Output: <class 'str'>
```

### Converting Input to Numbers

```python
# Convert to integer
age = int(input("Enter your age: "))
print(age + 10)             # Can perform arithmetic

# Convert to float
height = float(input("Enter your height (m): "))
print(height * 100)         # Can perform calculations

# Error if input cannot be converted
# int(input("Enter number: "))  # If user enters "abc" -> ValueError
```

### Safe Input Conversion (Error Handling)

```python
# Try-except for safe conversion
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")

# Output example:
# Enter your age: abc
# Please enter a valid number
```

### Getting Multiple Inputs

```python
# One by one
name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")

print(f"{name}, {age}, {city}")

# Multiple inputs at once
# Note: Limited to single line
inputs = input("Enter name, age, city (comma-separated): ")
name, age, city = inputs.split(",")
print(f"{name.strip()}, {age.strip()}, {city.strip()}")
```

### Input with Default Values

```python
# Ask for optional input
name = input("Enter your name (or press Enter for 'Guest'): ")
if name == "":
    name = "Guest"
print(f"Welcome, {name}!")

# More concise
name = input("Enter name: ") or "Guest"
print(name)
```

### Looping for Input

```python
# Keep asking until valid input
while True:
    try:
        age = int(input("Enter your age (1-150): "))
        if 1 <= age <= 150:
            break
        else:
            print("Please enter age between 1 and 150")
    except ValueError:
        print("Please enter a valid number")

print(f"Your age is {age}")
```

### Multi-line Input

```python
# Using sys.stdin
import sys

# Read multiple lines until EOF
lines = sys.stdin.readlines()
for line in lines:
    print(line.strip())

# Alternative: Read all at once
all_input = sys.stdin.read()
print(all_input)
```

### Input vs Raw Input (Python 2 vs 3)

```python
# Python 3 - input() returns string
name = input("Enter name: ")  # Returns string

# Python 2 had:
# raw_input() -> returns string
# input() -> evaluates expression (dangerous!)

# In Python 3, there's only input() which behaves like raw_input()
```

---

## Processing Input

### Type Conversion Examples

```python
# Single value
number = int(input("Enter number: "))

# Multiple values from one line
x, y = map(int, input("Enter two numbers: ").split())
print(f"Sum: {x + y}")

# Output example:
# Enter two numbers: 5 10
# Sum: 15
```

### Validating Input

```python
def get_valid_email():
    while True:
        email = input("Enter email: ")
        if "@" in email and "." in email:
            return email
        else:
            print("Invalid email format")

email = get_valid_email()
print(f"Valid email: {email}")
```

### Case-Insensitive Input

```python
# Make input case-insensitive
choice = input("Enter (yes/no): ").lower()

if choice == "yes":
    print("You chose yes")
elif choice == "no":
    print("You chose no")
else:
    print("Invalid choice")
```

### Stripping Whitespace

```python
# Remove leading/trailing spaces
name = input("Enter name: ").strip()
print(f"Hello, {name}!")

# Output if user enters "  Alice  ":
# Hello, Alice!
```

---

## Map Function

### Basic Map Usage

**Syntax:** `map(function, iterable)`

Returns iterator applying function to each element.

```python
# Simple mapping - square each number
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)

print(list(squared))        # Output: [1, 4, 9, 16, 25]

# map() returns iterator (not list)
squared_iter = map(lambda x: x**2, numbers)
print(squared_iter)         # Output: <map object at 0x...>

# Convert to list for viewing
squared_list = list(squared_iter)
print(squared_list)         # Output: [1, 4, 9, 16, 25]
```

### Map with Built-in Functions

```python
# Convert strings to integers
string_numbers = ["1", "2", "3", "4", "5"]
int_numbers = map(int, string_numbers)
print(list(int_numbers))    # Output: [1, 2, 3, 4, 5]

# Convert to strings
numbers = [1, 2, 3, 4, 5]
string_numbers = map(str, numbers)
print(list(string_numbers)) # Output: ['1', '2', '3', '4', '5']

# Convert to float
string_floats = ["1.5", "2.7", "3.2"]
floats = map(float, string_floats)
print(list(floats))         # Output: [1.5, 2.7, 3.2]

# Get absolute values
numbers = [-1, -2, 3, -4, 5]
abs_values = map(abs, numbers)
print(list(abs_values))     # Output: [1, 2, 3, 4, 5]

# Round numbers
floats = [1.234, 2.567, 3.891]
rounded = map(round, floats)
print(list(rounded))        # Output: [1, 3, 4]

# Specify precision for rounding
rounded_2 = map(lambda x: round(x, 1), floats)
print(list(rounded_2))      # Output: [1.2, 2.6, 3.9]
```

### Map with Custom Functions

```python
# Define custom function
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))        # Output: [1, 4, 9, 16, 25]

# More complex function
def calculate_discount(price):
    return price * 0.9  # 10% discount

prices = [100, 200, 300]
discounted = map(calculate_discount, prices)
print(list(discounted))     # Output: [90.0, 180.0, 270.0]

# Function checking element type
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5]
evens = map(is_even, numbers)
print(list(evens))          # Output: [False, True, False, True, False]
```

---

## Map with Built-in Functions

### int, str, float with Map

```python
# Convert user input to integers
print("Enter numbers (space-separated): ")
user_input = input()
numbers = map(int, user_input.split())
print(list(numbers))

# Output example:
# Enter numbers (space-separated):
# 1 2 3 4 5
# [1, 2, 3, 4, 5]

# Convert to strings
numbers = [1, 2, 3, 4, 5]
strings = map(str, numbers)
print(list(strings))        # Output: ['1', '2', '3', '4', '5']

# Convert to float
strings = ["1.5", "2.7", "3.2"]
floats = map(float, strings)
print(list(floats))         # Output: [1.5, 2.7, 3.2]

# Convert to bool
values = [0, 1, "", "hello", [], [1, 2]]
bools = map(bool, values)
print(list(bools))
# Output: [False, True, False, True, False, True]
```

### len() with Map

```python
# Get length of each string
words = ["apple", "banana", "cherry"]
lengths = map(len, words)
print(list(lengths))        # Output: [5, 6, 6]

# Get length of each list
lists = [[1, 2], [1, 2, 3], [1]]
sizes = map(len, lists)
print(list(sizes))          # Output: [2, 3, 1]
```

### String Methods with Map

```python
# Convert to uppercase
words = ["apple", "banana", "cherry"]
upper = map(str.upper, words)
print(list(upper))          # Output: ['APPLE', 'BANANA', 'CHERRY']

# Convert to lowercase
words = ["Apple", "BANANA", "Cherry"]
lower = map(str.lower, words)
print(list(lower))          # Output: ['apple', 'banana', 'cherry']

# Strip whitespace
words = ["  apple  ", " banana ", "cherry"]
stripped = map(str.strip, words)
print(list(stripped))       # Output: ['apple', 'banana', 'cherry']
```

---

## Map with Lambda Functions

### Lambda Basics

**Syntax:** `lambda arguments: expression`

Anonymous function for quick operations.

```python
# Simple lambda - add 10
add_ten = lambda x: x + 10
print(add_ten(5))           # Output: 15

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(5, 3))            # Output: 8

# Lambda with map
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))        # Output: [2, 4, 6, 8, 10]
```

### Common Lambda with Map

```python
# Square each number
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))        # Output: [1, 4, 9, 16, 25]

# Multiply each number by 2.5
numbers = [10, 20, 30]
scaled = map(lambda x: x * 2.5, numbers)
print(list(scaled))         # Output: [25.0, 50.0, 75.0]

# Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))     # Output: [32.0, 50.0, 68.0, 86.0]

# Extract specific part of data
data = ["Alice:25", "Bob:30", "Charlie:28"]
names = map(lambda x: x.split(":")[0], data)
print(list(names))          # Output: ['Alice', 'Bob', 'Charlie']
```

### Lambda with Conditions

```python
# Conditional lambda
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: "even" if x % 2 == 0 else "odd", numbers)
print(list(result))
# Output: ['odd', 'even', 'odd', 'even', 'odd']

# Absolute value (conditional)
numbers = [-5, -3, 0, 3, 5]
abs_values = map(lambda x: x if x >= 0 else -x, numbers)
print(list(abs_values))     # Output: [5, 3, 0, 3, 5]

# Grade based on score
scores = [45, 60, 75, 90, 95]
grades = map(lambda s: "A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F", scores)
print(list(grades))
# Output: ['F', 'D', 'C', 'A', 'A']
```

---

## Map vs List Comprehension

### Comparison

```python
# Using map()
numbers = [1, 2, 3, 4, 5]
squared_map = list(map(lambda x: x**2, numbers))

# Using list comprehension
squared_comp = [x**2 for x in numbers]

print(squared_map)          # Output: [1, 4, 9, 16, 25]
print(squared_comp)         # Output: [1, 4, 9, 16, 25]

# With conditions
# Map with filter
even_squared_map = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# List comprehension (cleaner)
even_squared_comp = [x**2 for x in numbers if x % 2 == 0]

print(even_squared_map)     # Output: [4, 16]
print(even_squared_comp)    # Output: [4, 16]
```

### When to Use Each

| Use Case | Better Choice |
|----------|---------------|
| Simple transformation | Both, but comprehension is more readable |
| With condition | List comprehension |
| Complex logic | List comprehension |
| Lazy evaluation needed | Map (returns iterator) |
| Quick throwaway | Map might be slightly shorter |
| Nested operations | List comprehension |
| Converting types | Map (e.g., `map(int, ...)`) |

### Readability Comparison

```python
# Map version - less readable
result = list(map(lambda x: x * 2 if x % 2 == 0 else x, range(10)))

# List comprehension - more readable
result = [x * 2 if x % 2 == 0 else x for x in range(10)]

# Both output: [0, 1, 4, 3, 8, 5, 12, 7, 16, 9]
```

---

## Other Higher-Order Functions

### Filter Function

**Syntax:** `filter(function, iterable)`

Returns iterator with elements where function returns True.

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))          # Output: [2, 4, 6, 8, 10]

# Filter strings starting with 'a'
words = ["apple", "banana", "apricot", "cherry"]
a_words = filter(lambda w: w.startswith("a"), words)
print(list(a_words))        # Output: ['apple', 'apricot']

# Filter non-empty strings
strings = ["hello", "", "world", "  ", "python"]
non_empty = filter(lambda s: s.strip(), strings)
print(list(non_empty))      # Output: ['hello', 'world', 'python']
```

### Reduce Function

**Note:** Requires `from functools import reduce`

Applies function cumulatively.

```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)                # Output: 15

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)              # Output: 120

# Find maximum
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)              # Output: 9

# Concatenate strings
words = ["Hello", " ", "World"]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)             # Output: Hello World
```

### Combining map, filter, reduce

```python
from functools import reduce

# Get even numbers, square them, sum them
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
print(result)               # Output: 120 (4 + 16 + 36 + 64)

# Better with list comprehension
result2 = sum(x**2 for x in numbers if x % 2 == 0)
print(result2)              # Output: 120
```

---

## Practical Examples

### Getting and Processing User Input

```python
# Read numbers from user and square them
print("Enter numbers (space-separated): ")
user_input = input()
numbers = map(int, user_input.split())
squared = map(lambda x: x**2, numbers)
print("Squared:", list(squared))

# Output example:
# Enter numbers (space-separated):
# 1 2 3 4 5
# Squared: [1, 4, 9, 16, 25]
```

### Processing Student Grades

```python
# Convert letter grades to points
grades = ["A", "B", "A", "C", "B"]
points_map = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

points = map(lambda g: points_map[g], grades)
gpa = sum(points) / len(grades)
print(f"GPA: {gpa:.2f}")    # Output: GPA: 3.40
```

### Converting Temperature List

```python
# Convert Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 100]
fahrenheit_temps = map(lambda c: (c * 9/5) + 32, celsius_temps)
print(list(fahrenheit_temps))
# Output: [32.0, 50.0, 68.0, 86.0, 212.0]

# Find temperatures above 70°F
hot_temps = filter(lambda f: f > 70, fahrenheit_temps)
```

### Processing CSV Data

```python
# Parse CSV-like input
csv_line = "Alice,85,90,78"
parts = csv_line.split(",")
name = parts[0]
scores = list(map(int, parts[1:]))
average = sum(scores) / len(scores)
print(f"{name}: Average = {average:.2f}")
# Output: Alice: Average = 84.33
```

### Multiple Input Transformations

```python
# Read student records
print("Enter student name and three scores (comma-separated): ")
student_input = input()
parts = student_input.split(",")

name = parts[0].strip()
scores = list(map(int, map(str.strip, parts[1:])))
average = sum(scores) / len(scores)
grade = "A" if average >= 90 else "B" if average >= 80 else "C" if average >= 70 else "D" if average >= 60 else "F"

print(f"{name}: Average = {average:.2f}, Grade = {grade}")

# Output example:
# Enter student name and three scores (comma-separated):
# Alice, 85, 90, 88
# Alice: Average = 87.67, Grade = B
```

### Processing URLs

```python
# Extract domain from URLs
urls = [
    "https://www.google.com/search",
    "https://www.github.com/user/repo",
    "https://stackoverflow.com/questions"
]

domains = map(lambda url: url.split("/")[2].replace("www.", ""), urls)
print(list(domains))
# Output: ['google.com', 'github.com', 'stackoverflow.com']
```

---

## Practice Exercises

### 1. Basic Input
- Get user's name and age, display formatted message
- Convert string input to integer and perform arithmetic
- Get multiple inputs on one line using split()

### 2. Input Validation
- Keep asking for input until valid number entered
- Validate email format from user input
- Get yes/no response with case-insensitive handling

### 3. Map with Built-in Functions
- Convert list of strings to integers
- Apply len() to list of strings
- Convert between number types using map()

### 4. Map with Lambda
- Square/cube numbers using lambda in map()
- Convert temperatures between Celsius and Fahrenheit
- Extract specific data from strings using lambda

### 5. Combining Functions
- Use map() and filter() together
- Process user input with multiple transformations
- Calculate statistics on mapped data

### 6. Real-World Scenarios
- Parse CSV input and calculate averages
- Convert multiple temperature values
- Process student grades and calculate GPA
- Extract information from structured text input

---

# End of Notes
