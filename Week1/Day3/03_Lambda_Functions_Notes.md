# Lambda Functions in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Lambda Functions](#introduction-to-lambda-functions)
2. [Lambda Syntax](#lambda-syntax)
3. [Lambda with map(), filter(), reduce()](#lambda-with-map-filter-reduce)
4. [Lambda vs Regular Functions](#lambda-vs-regular-functions)
5. [When to Use Lambda](#when-to-use-lambda)
6. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

- ✅ Write lambda functions
- ✅ Use lambda with map(), filter(), reduce()
- ✅ Know when to use lambda vs regular functions
- ✅ Apply best practices for lambda usage

---

## Introduction to Lambda Functions

### What are Lambda Functions?

**Lambda functions** are small anonymous functions defined with `lambda` keyword. They can have any number of parameters but only ONE expression.

```python
# Regular function
def add(x, y):
    return x + y

# Lambda function (equivalent)
add = lambda x, y: x + y

print(add(5, 3))  # 8
```

### Syntax

```python
lambda parameters: expression

# Examples
lambda x: x**2           # Square
lambda x, y: x + y       # Add two numbers
lambda x: x % 2 == 0     # Check if even
```

---

## Lambda Syntax

### Basic Lambda

```python
# Lambda with one parameter
square = lambda x: x**2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 7))  # 10

# Multiple parameters
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24
```

### Lambda with Conditionals

```python
# Simple if-else (ternary)
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # 20

# Check even/odd
is_even = lambda x: "even" if x % 2 == 0 else "odd"
print(is_even(5))   # "odd"
print(is_even(10))  # "even"
```

### Immediate Invocation

```python
# Call lambda immediately
result = (lambda x: x**2)(5)
print(result)  # 25

# Useful for one-time calculations
total = (lambda price, tax: price * (1 + tax))(100, 0.08)
print(total)  # 108.0
```

---

## Lambda with map(), filter(), reduce()

### map()

Apply function to all items:

```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Convert to uppercase
words = ['hello', 'world']
upper = list(map(lambda s: s.upper(), words))
# ['HELLO', 'WORLD']

# Multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, nums1, nums2))
# [5, 7, 9]
```

### filter()

Filter items based on condition:

```python
# Get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8]

# Get positive numbers
numbers = [1, -2, 3, -4, 5, -6]
positives = list(filter(lambda x: x > 0, numbers))
# [1, 3, 5]

# Long words
words = ['hi', 'hello', 'hey', 'goodbye']
long_words = list(filter(lambda w: len(w) > 3, words))
# ['hello', 'goodbye']
```

### reduce()

Reduce sequence to single value:

```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
# 15 (1+2=3, 3+3=6, 6+4=10, 10+5=15)

# Find maximum
numbers = [5, 2, 8, 1, 9]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
# 9

# Product of all numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
# 24
```

---

## Lambda vs Regular Functions

### When Lambda is Good

```python
# ✅ GOOD - Simple, one-time use
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# ✅ GOOD - Sorting key
words = ['Python', 'is', 'awesome']
sorted_words = sorted(words, key=lambda w: len(w))
# ['is', 'Python', 'awesome']

# ✅ GOOD - Event handlers (GUI)
button.config(command=lambda: print("Clicked!"))
```

### When Regular Function is Better

```python
# ❌ BAD - Complex logic
result = list(map(lambda x: x**2 if x > 0 else x**3 if x < 0 else 0, numbers))

# ✅ BETTER - Regular function
def transform(x):
    if x > 0:
        return x**2
    elif x < 0:
        return x**3
    return 0

result = list(map(transform, numbers))

# ❌ BAD - Named lambda (defeats purpose)
square = lambda x: x**2

# ✅ BETTER - Regular function
def square(x):
    return x**2
```

---

## When to Use Lambda

### ✅ Good Use Cases

```python
# 1. Sorting with custom key
students = [('Alice', 85), ('Bob', 72), ('Charlie', 95)]
sorted_by_grade = sorted(students, key=lambda s: s[1])

# 2. One-time transformations
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))

# 3. Simple callbacks
from tkinter import Button
btn = Button(text="Click", command=lambda: print("Hello"))

# 4. Filter with simple condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

### ❌ Bad Use Cases

```python
# 1. Complex logic
# Use regular function instead

# 2. Multiple statements
# Lambda can only have ONE expression

# 3. Named and reused
# If you name it and use multiple times, use def

# 4. Needs documentation
# Lambda can't have docstrings
```

---

## Practice Exercises

**Exercise 1**: Lambda to square a number

**Exercise 2**: Use map() with lambda to uppercase strings

**Exercise 3**: Use filter() to get numbers > 10

**Exercise 4**: Use reduce() to find product

**Exercise 5**: Sort list of tuples by second element

---

## 🎯 Key Takeaways

✅ **Lambda**: `lambda params: expression`  
✅ Only **ONE expression** (no statements)  
✅ **Anonymous** (no name required)  
✅ Use with **map(), filter(), reduce()**  
✅ Good for **simple, one-time** operations  
✅ Use **regular functions** for complex logic  
✅ **Don't name** lambdas if reusing  

---

## 📚 Quick Reference

```python
# Syntax
lambda x: x**2
lambda x, y: x + y

# With map()
list(map(lambda x: x*2, [1,2,3]))

# With filter()
list(filter(lambda x: x>0, numbers))

# With reduce()
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3])

# Sorting
sorted(items, key=lambda x: x[1])
```

---

**End of Lambda Functions Notes** 📝

## Advanced Lambda Patterns

### Lambda with Multiple Arguments

```python
# Two arguments
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Three arguments
calculate = lambda a, b, c: (a + b) * c
print(calculate(2, 3, 4))  # 20

# Variable number of arguments
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))  # 15

# Keyword arguments
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))  # "Hello, Alice!"
print(greet("Bob", greeting="Hi"))  # "Hi, Bob!"
```

### Lambda with Conditionals

```python
# Ternary operator in lambda
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # 20

# Multiple conditions
classify = lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'zero'
print(classify(5))   # 'positive'
print(classify(-3))  # 'negative'
print(classify(0))   # 'zero'

# Complex condition
check_range = lambda x: "low" if x < 10 else "medium" if x < 50 else "high"
print(check_range(5))   # "low"
print(check_range(25))  # "medium"
print(check_range(75))  # "high"
```

### Lambda with map()

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to strings
strings = list(map(lambda x: str(x), numbers))
print(strings)  # ['1', '2', '3', '4', '5']

# Multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [11, 22, 33]

# Dictionary transformation
users = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
names = list(map(lambda u: u['name'], users))
print(names)  # ['Alice', 'Bob']
```

### Lambda with filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)  # [6, 7, 8, 9, 10]

# Filter strings by length
words = ['python', 'is', 'awesome', 'and', 'powerful']
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)  # ['python', 'awesome', 'powerful']

# Filter non-empty strings
items = ['apple', '', 'banana', '', 'orange']
non_empty = list(filter(lambda x: x, items))
print(non_empty)  # ['apple', 'banana', 'orange']
```

### Lambda with reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5

# Concatenate strings
words = ['Python', 'is', 'awesome']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)  # "Python is awesome"
```

---

## Lambda with sorted()

### Sorting with Key Functions

```python
# Sort list of tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Sort by grade (second element)
by_grade = sorted(students, key=lambda x: x[1])
print(by_grade)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort descending
by_grade_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(by_grade_desc)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Sort dictionary list
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]

by_age = sorted(users, key=lambda u: u['age'])
print(by_age)  # Sorted by age

# Sort by multiple keys
data = [('Alice', 25, 85), ('Bob', 30, 92), ('Alice', 30, 78)]
sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
print(sorted_data)  # First by name, then by age
```

### Sorting Strings

```python
words = ['Python', 'is', 'AWESOME', 'and', 'Powerful']

# Sort case-insensitive
sorted_words = sorted(words, key=lambda w: w.lower())
print(sorted_words)  # ['and', 'AWESOME', 'is', 'Powerful', 'Python']

# Sort by length
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['is', 'and', 'Python', 'AWESOME', 'Powerful']

# Sort by last character
by_last_char = sorted(words, key=lambda w: w[-1])
print(by_last_char)
```

---

## Lambda in Real-World Scenarios

### Data Processing

```python
# Process employee data
employees = [
    {'name': 'Alice', 'salary': 50000, 'dept': 'IT'},
    {'name': 'Bob', 'salary': 60000, 'dept': 'HR'},
    {'name': 'Charlie', 'salary': 55000, 'dept': 'IT'},
    {'name': 'David', 'salary': 45000, 'dept': 'HR'}
]

# Filter IT employees
it_employees = list(filter(lambda e: e['dept'] == 'IT', employees))
print(f"IT Employees: {len(it_employees)}")

# Get high earners (>50k)
high_earners = list(filter(lambda e: e['salary'] > 50000, employees))
print(f"High earners: {[e['name'] for e in high_earners]}")

# Calculate total IT salaries
it_salaries = map(lambda e: e['salary'], 
                  filter(lambda e: e['dept'] == 'IT', employees))
total_it_salary = reduce(lambda x, y: x + y, it_salaries)
print(f"Total IT salary: ${total_it_salary}")
```

### Event Handlers

```python
# Simulated button click handlers
def create_button_handler(action):
    """Create click handler using lambda"""
    handlers = {
        'save': lambda: print("Saving data..."),
        'cancel': lambda: print("Cancelled"),
        'delete': lambda: print("Deleting..."),
        'refresh': lambda: print("Refreshing...")
    }
    return handlers.get(action, lambda: print("Unknown action"))

# Usage
save_btn = create_button_handler('save')
cancel_btn = create_button_handler('cancel')

save_btn()    # "Saving data..."
cancel_btn()  # "Cancelled"
```

### Data Validation

```python
# Validation rules using lambdas
validators = {
    'email': lambda x: '@' in x and '.' in x,
    'age': lambda x: 0 < x < 150,
    'username': lambda x: len(x) >= 3,
    'password': lambda x: len(x) >= 8
}

def validate_user(user_data):
    """Validate user data"""
    errors = []
    
    for field, validator in validators.items():
        if field in user_data:
            if not validator(user_data[field]):
                errors.append(f"Invalid {field}")
    
    return len(errors) == 0, errors

# Test
user = {
    'email': 'alice@example.com',
    'age': 25,
    'username': 'ali',
    'password': 'short'
}

valid, errors = validate_user(user)
if not valid:
    for error in errors:
        print(error)
```

---

## Lambda Best Practices

### When to Use Lambda

✅ **Use Lambda When:**
```python
# 1. Simple one-liner functions
squared = map(lambda x: x**2, numbers)

# 2. Sort key functions
sorted_items = sorted(items, key=lambda x: x[1])

# 3. Filter conditions
evens = filter(lambda x: x % 2 == 0, numbers)

# 4. Simple callbacks
button.on_click(lambda: print("Clicked!"))
```

❌ **Avoid Lambda When:**
```python
# 1. Complex logic (use def instead)
# ❌ BAD
process = lambda x: x**2 if x > 0 else -x**2 if x < 0 else 0

# ✅ GOOD
def process(x):
    if x > 0:
        return x**2
    elif x < 0:
        return -x**2
    else:
        return 0

# 2. Need docstrings or type hints
# ❌ BAD: Lambda can't have docstrings
calc = lambda x, y: x + y

# ✅ GOOD
def calc(x: int, y: int) -> int:
    """Add two numbers"""
    return x + y

# 3. Multiple statements needed
# ❌ BAD: Can't do multiple statements
# process = lambda x: (print(x), x**2)  # Ugly!

# ✅ GOOD
def process(x):
    print(x)
    return x**2
```

---

## Lambda vs Regular Functions

### Comparison

```python
# Regular function
def add(x, y):
    """Add two numbers"""
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

# Both work the same
print(add(5, 3))         # 8
print(add_lambda(5, 3))  # 8

# But regular function has:
print(add.__name__)      # 'add'
print(add.__doc__)       # 'Add two numbers'

# Lambda has limitations:
print(add_lambda.__name__)  # '<lambda>'
print(add_lambda.__doc__)   # None
```

### Performance

```python
import timeit

# Regular function
def square(x):
    return x ** 2

# Lambda
square_lambda = lambda x: x ** 2

# Performance is nearly identical
time_def = timeit.timeit('square(5)', globals=globals(), number=1000000)
time_lambda = timeit.timeit('square_lambda(5)', globals=globals(), number=1000000)

print(f"def: {time_def:.4f}s")
print(f"lambda: {time_lambda:.4f}s")
# Nearly the same!
```

---

## Advanced Lambda Techniques

### Closures with Lambda

```python
def make_multiplier(n):
    """Return lambda that multiplies by n"""
    return lambda x: x * n

# Create specific multipliers
double = make_multiplier(2)
triple = make_multiplier(3)
times_10 = make_multiplier(10)

print(double(5))    # 10
print(triple(5))    # 15
print(times_10(5))  # 50

# Practical use: discount calculator
def make_discount_calculator(discount_percent):
    return lambda price: price * (1 - discount_percent / 100)

apply_10_percent = make_discount_calculator(10)
apply_20_percent = make_discount_calculator(20)

price = 100
print(f"10% off: ${apply_10_percent(price)}")  # $90.0
print(f"20% off: ${apply_20_percent(price)}")  # $80.0
```

### Lambda with List Comprehension

```python
# Combine lambda with comprehensions
numbers = [1, 2, 3, 4, 5]

# Apply function to filtered items
process = lambda x: x ** 2
result = [process(x) for x in numbers if x % 2 == 0]
print(result)  # [4, 16]

# Multiple transformations
transforms = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x ** 2
]

value = 5
results = [t(value) for t in transforms]
print(results)  # [15, 10, 25]
```

---

## Common Lambda Patterns

### Pattern 1: Default Value Handler

```python
# Handle missing values
get_value = lambda d, k, default=None: d.get(k, default)

data = {'a': 1, 'b': 2}
print(get_value(data, 'a'))    # 1
print(get_value(data, 'c', 0)) # 0
```

### Pattern 2: Type Checker

```python
# Check types quickly
is_string = lambda x: isinstance(x, str)
is_number = lambda x: isinstance(x, (int, float))
is_list = lambda x: isinstance(x, list)

print(is_string("hello"))  # True
print(is_number(42))       # True
print(is_list([1, 2, 3]))  # True
```

### Pattern 3: Range Checker

```python
# Check if value in range
in_range = lambda x, min_val, max_val: min_val <= x <= max_val

print(in_range(5, 0, 10))   # True
print(in_range(15, 0, 10))  # False

# Validate age
valid_age = lambda age: in_range(age, 0, 150)
print(valid_age(25))   # True
print(valid_age(200))  # False
```

---

## Lambda Quick Reference

```python
# Basic syntax
lambda arguments: expression

# Examples
square = lambda x: x**2
add = lambda x, y: x + y
greet = lambda name: f"Hello, {name}!"

# With map()
squared = map(lambda x: x**2, numbers)

# With filter()
evens = filter(lambda x: x % 2 == 0, numbers)

# With sorted()
sorted_items = sorted(items, key=lambda x: x[1])

# With reduce()
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)

# Multiple arguments
calc = lambda a, b, c: (a + b) * c

# Conditional
max_val = lambda a, b: a if a > b else b

# Default arguments
greet = lambda name, msg="Hello": f"{msg}, {name}!"
```

---

**End of Lambda Functions Notes** ���

Master lambda functions for concise, functional Python programming!
