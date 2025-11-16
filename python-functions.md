# Python Functions: Complete Guide

---

## Table of Contents
1. [Introduction to Functions](#introduction-to-functions)
2. [Defining and Calling Functions](#defining-and-calling-functions)
3. [Parameters and Arguments](#parameters-and-arguments)
4. [Special Parameters](#special-parameters)
5. [Return Values](#return-values)
6. [Scope and Lifetime](#scope-and-lifetime)
7. [Lambda Functions](#lambda-functions)
8. [Built-in Functions](#built-in-functions)
9. [Recursion](#recursion)
10. [Closures](#closures)
11. [Decorators](#decorators)
12. [Function Annotations](#function-annotations)
13. [Practice Exercises](#practice-exercises)

---

## Introduction to Functions

### What are Functions?

Functions are reusable blocks of code that perform specific tasks.

### Why Use Functions?

1. **Code Organization** - Group related code
2. **Reusability** - Use same code multiple times
3. **Modularity** - Break large problems into smaller parts
4. **Maintainability** - Easier to update and debug
5. **Encapsulation** - Hide complex operations

### Function Basics

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

---

## Defining and Calling Functions

### Basic Function

```python
# Defining a function
def say_hello():
    print("Hello, World!")

# Calling a function
say_hello()  # Output: Hello, World!
```

### Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### Multiple Parameters

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8
```

---

## Parameters and Arguments

### Positional Parameters

```python
def describe_person(name, age):
    print(f"{name} is {age} years old.")

# Order matters
describe_person("Alice", 25)  # Output: Alice is 25 years old.

# Wrong order
# describe_person(25, "Alice")  # Wrong!
```

### Keyword Arguments

```python
# Specify parameters by name
describe_person(age=30, name="Bob")  # Order doesn't matter!
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Charlie")  # Output: Hello, Charlie!
greet("Charlie", "Hi")  # Output: Hi, Charlie!
```

---

## Special Parameters

### *args (Variable Arguments)

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

### **kwargs (Keyword Arguments)

```python
def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

---

## Return Values

### Single Return

```python
def square(x):
    return x ** 2

result = square(5)
print(result)  # Output: 25
```

### Multiple Returns

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

mn, mx, sm = get_stats([1, 2, 3, 4, 5])
print(f"Min: {mn}, Max: {mx}, Sum: {sm}")
# Output: Min: 1, Max: 5, Sum: 15
```

---

## Scope and Lifetime

### LEGB Rule

```python
# Local, Enclosing, Global, Built-in
x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope
    
    def inner():
        x = "local"  # Local scope
        print(x)
    
    inner()
    print(x)

outer()
print(x)
# Output:
# local
# enclosing
# global
```

### Global Keyword

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```

---

## Lambda Functions

### What is Lambda?

Anonymous functions defined with `lambda` keyword.

```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))  # Output: 25
print(square_lambda(5))  # Output: 25
```

### Uses with map, filter, reduce

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# filter
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]

# reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15
```

---

## Built-in Functions

### map()

```python
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = map(double, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]
```

### filter()

```python
def is_positive(x):
    return x > 0

numbers = [-2, -1, 0, 1, 2]
positives = filter(is_positive, numbers)
print(list(positives))  # Output: [1, 2]
```

### reduce()

```python
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)
print(product)  # Output: 24
```

### zip()

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NY", "LA", "SF"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
# Output:
# Alice is 25 years old and lives in NY
# Bob is 30 years old and lives in LA
# Charlie is 35 years old and lives in SF
```

### enumerate()

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry
```

---

## Recursion

### Basic Recursion

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Fibonacci Sequence

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(6)])
# Output: [0, 1, 1, 2, 3, 5]
```

---

## Closures

### What is Closure?

Functions that remember variables from their enclosing scope.

```python
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2

counter2 = counter()
print(counter2())  # Output: 1
```

---

## Practice Exercises

### 1. Function Basics
- Create a function to calculate area of rectangle
- Write a function with keyword arguments
- Implement a function with default parameters

### 2. Parameters and Arguments
- Create a function using *args
- Implement a function using **kwargs
- Write a function mixing positional, *args, and **kwargs

### 3. Recursion
- Implement factorial using recursion
- Write a recursive function for sum of digits
- Create a recursive function for list flattening

### 4. Closures and Decorators
- Write a function that creates counters
- Implement a simple decorator
- Create a decorator with arguments

### 5. Built-in Functions
- Use map() to transform data
- Use filter() to extract specific elements
- Combine map() and filter() for complex operations

### 6. Real-world Applications
- Create a calculator with functions
- Implement a grade calculator
- Build a temperature converter
- Design a word frequency analyzer

---

# End of Notes
