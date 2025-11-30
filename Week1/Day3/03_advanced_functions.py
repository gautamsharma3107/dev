"""
Day 3 - Advanced Functions
===========================
Learn: Scope, closures, decorators, recursion

Key Concepts:
- Variable scope (local, global, nonlocal)
- Closures (functions that remember their environment)
- Decorators (functions that modify functions)
- Recursion (functions that call themselves)
"""

# ========== VARIABLE SCOPE ==========
print("=" * 50)
print("VARIABLE SCOPE")
print("=" * 50)

# Global vs Local scope
global_var = "I'm global"

def show_scope():
    local_var = "I'm local"
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")

show_scope()
print(f"Outside function - global_var: {global_var}")
# print(local_var)  # Error! local_var not accessible

# Modifying global variable
counter = 0

def increment():
    global counter  # Declare we want to use global
    counter += 1

print(f"\nCounter before: {counter}")
increment()
increment()
increment()
print(f"Counter after 3 increments: {counter}")

# ========== NESTED FUNCTIONS ==========
print("\n" + "=" * 50)
print("NESTED FUNCTIONS")
print("=" * 50)

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function(10)

result = outer_function(5)
print(f"outer_function(5) with inner adding 10: {result}")

# Inner functions for organization
def process_data(data):
    """Process data using helper functions."""
    
    def validate(item):
        return item is not None and item != ""
    
    def transform(item):
        return str(item).upper()
    
    # Use inner functions
    valid_data = [item for item in data if validate(item)]
    transformed = [transform(item) for item in valid_data]
    return transformed

data = ["hello", None, "world", "", "python"]
result = process_data(data)
print(f"\nOriginal: {data}")
print(f"Processed: {result}")

# ========== CLOSURES ==========
print("\n" + "=" * 50)
print("CLOSURES")
print("=" * 50)

def multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(number):
        return number * factor
    return multiply

# Create closures
double = multiplier(2)
triple = multiplier(3)
times_ten = multiplier(10)

print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")
print(f"times_ten(5): {times_ten(5)}")

# Counter closure
def make_counter(start=0):
    """Create a counter function."""
    count = start
    
    def counter():
        nonlocal count  # Access outer variable
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter(100)

print(f"\nCounter 1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter 2: {counter2()}, {counter2()}, {counter2()}")

# ========== DECORATORS (Basic) ==========
print("\n" + "=" * 50)
print("DECORATORS (Basic)")
print("=" * 50)

# A decorator is a function that takes a function and returns a modified function

def my_decorator(func):
    """A simple decorator."""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

print("Calling say_hello():")
say_hello()

# Decorator with arguments
def log_calls(func):
    """Log function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name):
    return f"Hello, {name}!"

print("\nDecorated add:")
add(5, 3)

print("\nDecorated greet:")
greet("Gautam")

# Practical decorator: Timer
import time

def timer(func):
    """Measure execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function(n):
    """A deliberately slow function."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

print("\nTimed function:")
slow_function(1000000)

# ========== RECURSION ==========
print("\n" + "=" * 50)
print("RECURSION")
print("=" * 50)

# Factorial using recursion
def factorial_recursive(n):
    """Calculate factorial recursively."""
    if n <= 1:  # Base case
        return 1
    return n * factorial_recursive(n - 1)  # Recursive case

print(f"5! = {factorial_recursive(5)}")
print(f"10! = {factorial_recursive(10)}")

# Fibonacci sequence
def fibonacci(n):
    """Get nth Fibonacci number."""
    if n <= 1:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFirst 10 Fibonacci numbers:")
fib_sequence = [fibonacci(i) for i in range(10)]
print(fib_sequence)

# Sum of list using recursion
def sum_recursive(numbers):
    """Sum a list recursively."""
    if not numbers:  # Base case: empty list
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

print(f"\nSum of [1,2,3,4,5]: {sum_recursive([1, 2, 3, 4, 5])}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Memoization decorator (caching)
def memoize(func):
    """Cache function results."""
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci_fast(n):
    """Fibonacci with memoization - much faster!"""
    if n <= 1:
        return n
    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)

print("Fibonacci with memoization:")
print(f"fibonacci_fast(30): {fibonacci_fast(30)}")
print(f"fibonacci_fast(40): {fibonacci_fast(40)}")

# Example 2: Validate decorator
def validate_positive(func):
    """Ensure all arguments are positive."""
    def wrapper(*args):
        for arg in args:
            if arg < 0:
                raise ValueError(f"All arguments must be positive. Got {arg}")
        return func(*args)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print(f"\nArea of 5x3: {calculate_area(5, 3)}")
# calculate_area(-5, 3)  # Would raise ValueError

# Example 3: Retry decorator
def retry(max_attempts=3):
    """Retry a function if it fails."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
            raise Exception(f"Failed after {max_attempts} attempts")
        return wrapper
    return decorator

import random

@retry(max_attempts=5)
def unstable_function():
    """A function that randomly fails."""
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("Random failure!")
    return "Success!"

print("\nTrying unstable function:")
try:
    result = unstable_function()
    print(f"Result: {result}")
except Exception as e:
    print(f"Final failure: {e}")

print("\n" + "=" * 50)
print("✅ Advanced Functions - Complete!")
print("=" * 50)
