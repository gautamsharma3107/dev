# Functions in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Functions](#introduction-to-functions)
2. [Defining Functions](#defining-functions)
3. [Calling Functions](#calling-functions)
4. [Return Statements](#return-statements)
5. [Function Parameters](#function-parameters)
6. [Docstrings](#docstrings)
7. [Scope](#scope)
8. [Recursion](#recursion)
9. [Best Practices](#best-practices)
10. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Define and call functions
- ✅ Use parameters and return values effectively
- ✅ Write clear docstrings
- ✅ Understand scope (local vs global)
- ✅ Use recursion for appropriate problems
- ✅ Apply function best practices
- ✅ Organize code with functions

---

## Introduction to Functions

### What are Functions?

**Functions** are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs more readable.

```python
# Without functions - repetitive
print("Hello, Alice!")
print("Hello, Bob!")
print("Hello, Charlie!")

# With function - reusable
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")
```

**Real-World Analogy** 🌍

Think of a function like a recipe:
- **Function name** = Recipe name ("make_cake")
- **Parameters** = Ingredients (flour, sugar, eggs)
- **Function body** = Instructions (mix, bake, etc.)
- **Return value** = Final product (the cake)

### Why Use Functions?

1. **Reusability** - Write once, use many times
2. **Organization** - Break complex problems into smaller pieces
3. **Maintainability** - Fix bugs in one place
4. **Readability** - Self-documenting code
5. **Testing** - Easy to test individual pieces

```python
# Bad - repetitive code
total1 = item1_price * item1_quantity
total2 = item2_price * item2_quantity
total3 = item3_price * item3_quantity

# Good - function
def calculate_total(price, quantity):
    return price * quantity

total1 = calculate_total(item1_price, item1_quantity)
total2 = calculate_total(item2_price, item2_quantity)
total3 = calculate_total(item3_price, item3_quantity)
```

---

## Defining Functions

###Basic Function Syntax

```python
def function_name():
    # Function body (code to execute)
    statement1
    statement2
    ...

# Define function
def say_hello():
    print("Hello!")
    print("Welcome to Python!")

# Call function
say_hello()
# Output:
# Hello!
# Welcome to Python!
```

### Function Naming Conventions

```python
# ✅ GOOD - snake_case
def calculate_total():
    pass

def get_user_input():
    pass

def process_data():
    pass

# ❌ BAD - not Pythonic
def CalculateTotal():  # PascalCase (use for classes)
    pass

def getUserInput():    # camelCase (use in JavaScript)
    pass
```

### Functions with Parameters

```python
# Single parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!

# Multiple parameters
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)  # 5 + 3 = 8
```

---

## Calling Functions

### Basic Function Call

```python
def greet():
    print("Hello!")

# Call the function
greet()  # Hello!

# Call multiple times
greet()  # Hello!
greet()  # Hello!
```

### Passing Arguments

```python
def greet(name):
    print(f"Hello, {name}!")

# Positional argument
greet("Alice")  # Hello, Alice!

# Multiple arguments
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old")

introduce("Bob", 25)
# My name is Bob and I'm 25 years old
```

### Functions in Expressions

```python
def double(x):
    return x * 2

# Use in expression
result = double(5) + 10
print(result)  # 20 (double(5) returns 10, then 10 + 10)

# Use in if statement
if double(3) > 5:
    print("Greater than 5")

# Use in print
print(f"Double of 7 is {double(7)}")
#Double of 7 is 14
```

---

## Return Statements

### Basic Return

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Without return, function returns None
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")
print(result)  # None
```

### Multiple Return Values

```python
# Return tuple (unpacked automatically)
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(minimum)  # 1
print(maximum)  # 9

# Return dictionary
def get_person_info():
    return {"name": "Alice", "age": 25}

info = get_person_info()
print(info["name"])  # Alice
```

### Early Return

```python
def check_positive(num):
    if num <= 0:
        return False  # Early return
    # More processing for positive numbers
    return True

# Cleaner than nested if-else
def divide(a, b):
    if b == 0:
        return None  # Early return for error case
    return a / b
```

### No Return vs Return None

```python
# No return statement
def func1():
    print("Hello")

# Explicit return None
def func2():
    print("Hello")
    return None

# Both return None
result1 = func1()  # None
result2 = func2()  # None
```

---

## Function Parameters

### Positional Parameters

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Order matters!
greet("John", "Doe")  # Hello, John Doe!
greet("Doe", "John")  # Hello, Doe John! (wrong order)
```

### Keyword Parameters

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Specify parameters by name
greet(first_name="John", last_name="Doe")
greet(last_name="Doe", first_name="John")  # Order doesn't matter!

# Mix positional and keyword
greet("John", last_name="Doe")
# But positional must come first!
# greet(first_name="John", "Doe")  # SyntaxError!
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice! (uses default)
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", "Hey")     # Hey, Charlie!

# Multiple defaults
def create_user(username, active=True, role="user"):
    return {"username": username, "active": active, "role": role}

user1 = create_user("alice")
# {'username': 'alice', 'active': True, 'role': 'user'}

user2 = create_user("bob", role="admin")
# {'username': 'bob', 'active': True, 'role': 'admin'}
```

### Variable Arguments (*args)

```python
# Accept any number of positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(10))             # 10

# *args creates a tuple
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    print(args)

print_args(1, 2, 3)  # (1, 2, 3)
```

### Variable Keyword Arguments (**kwargs)

```python
# Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC

# **kwargs creates a dictionary
def print_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

print_kwargs(a=1, b=2, c=3)
# {'a': 1, 'b': 2, 'c': 3}
```

---

## Docstrings

### Basic Docstring

```python
def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")

# Access docstring
print(greet.__doc__)
# Print a greeting message.

# help() function
help(greet)
```

### Multi-line Docstring

```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)
```

### Google Style Docstring

```python
def divide(a, b):
    """
    Divide two numbers.
    
    Args:
        a (float): The dividend
        b (float): The divisor
        
    Returns:
        float: The quotient or None if b is zero
        
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(10, 0)
        None
    """
    if b == 0:
        return None
    return a / b
```

---

## Scope

### Local Scope

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # 10
# print(x)  # NameError! x doesn't exist outside function
```

### Global Scope

```python
x = 10  # Global variable

def my_function():
    print(x)  # Can read global variable

my_function()  # 10
print(x)       # 10

# But can't modify without 'global' keyword
def try_modify():
    x = 20  # Creates new local variable!
    print(x)

try_modify()  # 20 (local)
print(x)      # 10 (global unchanged)
```

### The global Keyword

```python
count = 0  # Global

def increment():
    global count  # Declare we're using global variable
    count += 1

increment()
print(count)  # 1

increment()
print(count)  # 2
```

### The nonlocal Keyword

```python
def outer():
    x = 10  # Enclosing scope
    
    def inner():
        nonlocal x  # Modify enclosing variable
        x = 20
    
    inner()
    print(x)  # 20 (modified by inner)

outer()
```

---

## Recursion

### Basic Recursive Function

```python
# Factorial: 5! = 5 × 4 × 3 × 2 × 1
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = 120
```

### Fibonacci Sequence

```python
def fibonacci(n):
    """Return nth Fibonacci number."""
    # Base cases
    if n <= 1:
        return n
    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)

# First 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13 21 34
```

### When to Use Recursion

```python
# ✅ GOOD - naturally recursive (tree traversal, etc.)
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
# 5, 4, 3, 2, 1, Done!

# ❌ BAD - iteration is better (factorial, fibonacci)
# Recursion causes stack overflow for large n
# Use loops or iteration instead
```

---

## Best Practices

### 1. Single Responsibility

```python
# ❌ BAD - does too many things
def process_user(name, email):
    validate_email(email)
    save_to_database(name, email)
    send_welcome_email(email)

# ✅ GOOD - separate functions
def validate_email(email):
    # Validation logic
    pass

def save_user(name, email):
    # Save logic
    pass

def send_welcome_email(email):
    # Email logic
    pass

# Then combine
def register_user(name, email):
    if validate_email(email):
        save_user(name, email)
       send_welcome_email(email)
```

### 2. Descriptive Names

```python
# ❌ BAD
def calc(a, b):
    return a + b

# ✅ GOOD
def calculate_total_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)
```

### 3. Keep Functions Small

```python
# ✅ GOOD - small, focused functions
def is_valid_email(email):
    return "@" in email and "." in email

def is_adult(age):
    return age >= 18

def can_register(email, age):
    return is_valid_email(email) and is_adult(age)
```

### 4. Avoid Side Effects

```python
# ❌ BAD - modifies global state
total = 0

def add_to_total(x):
    global total
    total += x

# ✅ GOOD - pure function
def add(a, b):
    return a + b

total = 0
total = add(total, 5)
```

### 5. Use Type Hints (Python 3.5+)

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def get_user(user_id: int) -> dict:
    return {"id": user_id, "name": "Alice"}
```

---

## Practice Exercises

### Beginner

**Exercise 1**: Write function to calculate area of rectangle

**Exercise 2**: Write function to check if number is even

**Exercise 3**: Write function to convert Celsius to Fahrenheit

**Exercise 4**: Write function to find maximum of two numbers

**Exercise 5**: Write function to count vowels in a string

### Intermediate

**Exercise 6**: Write function to reverse a string

**Exercise 7**: Write function to check if string is palindrome

**Exercise 8**: Write function to calculate average of a list

**Exercise 9**: Write function to find all prime numbers up to n

**Exercise 10**: Write function to merge two sorted lists

### Advanced

**Exercise 11**: Write recursive function to calculate power

**Exercise 12**: Write function to flatten nested list

**Exercise 13**: Write function for binary search

**Exercise 14**: Write function to generate all permutations

**Exercise 15**: Write memoized Fibonacci function

---

## 🎯 Key Takeaways

✅ Functions make code **reusable and organized**  
✅ Use `def` to define, call by name with ()  
✅ **return** sends values back to caller  
✅ **Parameters**: positional, keyword, default, *args, **kwargs  
✅ Write **docstrings** for documentation  
✅ **Scope**: local (inside function) vs global (outside)  
✅ **Recursion**: function calling itself (needs base case!)  
✅ Follow best practices: small, focused, pure functions  

---

## 📚 Quick Reference

```python
# Definition
def function_name(param1, param2):
    """Docstring"""
    # Function body
    return result

# Call
result = function_name(arg1, arg2)

# Default parameters
def func(a, b=10):
    return a + b

# Variable arguments
def func(*args, **kwargs):
    pass

# Scope
global variable_name
nonlocal variable_name

# Recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

---

**End of Functions Basics Notes** 📝

Continue to `Parameters_and_Returns_Notes.md` for advanced parameter handling!

## Advanced Function Concepts

### Function Objects

Functions are objects in Python - they can be assigned, passed, and returned:

```python
def greet(name):
    return f"Hello, {name}!"

# Assign function to variable
say_hello = greet
print(say_hello("Alice"))  # "Hello, Alice!"

# Store functions in data structures
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y
}

result = operations['add'](5, 3)  # 8
```

### Higher-Order Functions

Functions that take other functions as arguments or return functions:

```python
def apply_operation(func, x, y):
    """Higher-order function"""
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Pass functions as arguments
print(apply_operation(add, 5, 3))       # 8
print(apply_operation(multiply, 5, 3))  # 15

# Return functions
def make_multiplier(n):
    """Returns a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_5 = make_multiplier(5)

print(times_2(10))  # 20
print(times_5(10))  # 50
```

### Closures

Inner functions that remember variables from outer scope:

```python
def create_counter():
    """Closure example"""
    count = 0
    
    def increment():
        nonlocal count  # Access outer variable
        count += 1
        return count
    
    return increment

counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (separate counter)
print(counter1())  # 3
```

---

## Decorators Introduction

### Basic Decorator

```python
def timer_decorator(func):
    """Measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

slow_function()  # slow_function took 1.0001 seconds
```

### Decorator with Arguments

```python
def repeat(times):
    """Decorator that repeats function call"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

---

## Function Best Practices

### Practice 1: Single Responsibility

```python
# ❌ BAD: Function does too much
def process_user_data(data):
    # Validate
    if not data:
        return None
    # Parse
    user = parse_data(data)
    # Save to database
    save_to_db(user)
    # Send email
    send_email(user)
    # Log
    log_event(user)

# ✅ GOOD: Separate concerns
def validate_user_data(data):
    return data is not None

def process_user(data):
    if not validate_user_data(data):
        return None
    
    user = parse_data(data)
    save_user(user)
    notify_user(user)
    log_user_creation(user)
```

### Practice 2: Clear Function Names

```python
# ❌ BAD: Unclear names
def calc(x, y):
    return x + y

def proc(data):
    return data * 2

# ✅ GOOD: Descriptive names
def calculate_sum(a, b):
    return a + b

def double_value(number):
    return number * 2
```

### Practice 3: Use Type Hints

```python
def greet(name: str, age: int) -> str:
    """Greet user with name and age"""
    return f"Hello, {name}! You are {age} years old."

def calculate_average(numbers: list[float]) -> float:
    """Calculate average of numbers"""
    return sum(numbers) / len(numbers)
```

---

## Real-World Function Examples

### Example 1: Data Validator

```python
def validate_email(email: str) -> tuple[bool, str]:
    """Validate email address"""
    if not email:
        return False, "Email cannot be empty"
    
    if "@" not in email:
        return False, "Email must contain @"
    
    if "." not in email.split("@")[1]:
        return False, "Email domain must contain ."
    
    if len(email) < 5:
        return False, "Email too short"
    
    return True, "Valid email"

# Usage
valid, message = validate_email("user@example.com")
if valid:
    print("Email accepted!")
else:
    print(f"Error: {message}")
```

### Example 2: Text Processor

```python
def clean_text(text: str, lowercase: bool = True, 
               remove_punctuation: bool = True) -> str:
    """Clean and normalize text"""
    result = text.strip()
    
    if lowercase:
        result = result.lower()
    
    if remove_punctuation:
        import string
        result = result.translate(
            str.maketrans('', '', string.punctuation)
        )
    
    # Remove extra whitespace
    result = ' '.join(result.split())
    
    return result

dirty = "  Hello,  WORLD!  How   are YOU?  "
clean = clean_text(dirty)
print(clean)  # "hello world how are you"
```

### Example 3: Calculator Functions

```python
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(operation: str, a: float, b: float) -> float:
    """Main calculator function"""
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    
    return operations[operation](a, b)

# Usage
result = calculate('add', 10, 5)
print(result)  # 15
```

---

## Function Performance Tips

### Tip 1: Use Default Arguments Wisely

```python
# ❌ BAD: Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [1, 2] - unexpected!

# ✅ GOOD: Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [2] - correct!
```

### Tip 2: Avoid Global Variables

```python
# ❌ BAD: Using global variable
counter = 0

def increment():
    global counter
    counter += 1

# ✅ GOOD: Pass as parameter or use class
def increment(counter):
    return counter + 1

count = 0
count = increment(count)
```

---

## Error Handling in Functions

### Raising Exceptions

```python
def divide(a: float, b: float) -> float:
    """Divide with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    
    return a / b

# Usage with try-except
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

### Custom Exceptions

```python
class ValidationError(Exception):
    """Custom validation exception"""
    pass

def validate_age(age: int) -> None:
    """Validate age with custom exception"""
    if age < 0:
        raise ValidationError("Age cannot be negative")
    
    if age > 150:
        raise ValidationError("Age too large")
    
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer")

# Usage
try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation failed: {e}")
```

---

## Function Documentation

### Comprehensive Docstring

```python
def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    
    Raises:
        ValueError: If weight or height is non-positive
    
    Examples:
        >>> calculate_bmi(70, 1.75)
        22.86
        
        >>> calculate_bmi(80, 1.80)
        24.69
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")
    
    return weight / (height ** 2)

# Access docstring
print(calculate_bmi.__doc__)
```

---

**End of Functions Basics Notes** ���

Master functions for writing clean, modular Python code!
