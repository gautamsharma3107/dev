"""
Day 3 - Functions Basics
========================
Learn: Function definition, calling, basic parameters

Key Concepts:
- Functions are reusable blocks of code
- Use 'def' keyword to define
- Functions help organize and DRY (Don't Repeat Yourself)
- Can take inputs (parameters) and return outputs
"""

# ========== WHY FUNCTIONS? ==========
print("=" * 50)
print("WHY FUNCTIONS?")
print("=" * 50)

# Without functions (repetitive code)
print("Hello, Alice!")
print("Hello, Bob!")
print("Hello, Charlie!")

# With functions (reusable)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

# ========== BASIC FUNCTION DEFINITION ==========
print("\n" + "=" * 50)
print("BASIC FUNCTION DEFINITION")
print("=" * 50)

# Simple function (no parameters, no return)
def say_hello():
    print("Hello, World!")

# Call the function
say_hello()

# Function with parameter
def greet_person(name):
    print(f"Hello, {name}! Nice to meet you.")

greet_person("Gautam")

# Function with multiple parameters
def introduce(name, age, city):
    print(f"I'm {name}, {age} years old, from {city}.")

introduce("Alice", 25, "New York")

# ========== RETURN VALUES ==========
print("\n" + "=" * 50)
print("RETURN VALUES")
print("=" * 50)

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Return can be used in expressions
total = add(10, 20) + add(30, 40)
print(f"(10+20) + (30+40) = {total}")

# Multiple return values (returns tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

nums = [5, 2, 8, 1, 9]
minimum, maximum, total = get_stats(nums)
print(f"\nNumbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}, Sum: {total}")

# ========== DOCSTRINGS ==========
print("\n" + "=" * 50)
print("DOCSTRINGS (Documentation)")
print("=" * 50)

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Access docstring
print(f"Function: calculate_area")
print(f"Docstring: {calculate_area.__doc__}")

area = calculate_area(5, 3)
print(f"Area of 5x3 rectangle: {area}")

# ========== DEFAULT PARAMETERS ==========
print("\n" + "=" * 50)
print("DEFAULT PARAMETERS")
print("=" * 50)

def greet_with_message(name, message="Hello"):
    print(f"{message}, {name}!")

greet_with_message("Alice")  # Uses default
greet_with_message("Bob", "Good morning")  # Custom message
greet_with_message("Charlie", "Welcome")

# Multiple default parameters
def create_profile(name, age=0, city="Unknown", active=True):
    return {
        "name": name,
        "age": age,
        "city": city,
        "active": active
    }

profile1 = create_profile("Alice")
profile2 = create_profile("Bob", 25)
profile3 = create_profile("Charlie", 30, "London")

print(f"\nProfile 1: {profile1}")
print(f"Profile 2: {profile2}")
print(f"Profile 3: {profile3}")

# ========== KEYWORD ARGUMENTS ==========
print("\n" + "=" * 50)
print("KEYWORD ARGUMENTS")
print("=" * 50)

def describe_pet(animal, name, age):
    print(f"{name} is a {age}-year-old {animal}.")

# Positional arguments (order matters)
describe_pet("dog", "Buddy", 3)

# Keyword arguments (order doesn't matter)
describe_pet(name="Whiskers", age=5, animal="cat")
describe_pet(age=2, animal="bird", name="Tweety")

# Mixed (positional must come first)
describe_pet("rabbit", name="Fluffy", age=1)

# ========== FUNCTION EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL FUNCTION EXAMPLES")
print("=" * 50)

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

# Example 2: Check even/odd
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

print(f"\n10 is even: {is_even(10)}")
print(f"7 is even: {is_even(7)}")

# Example 3: Calculate factorial
def factorial(n):
    """Calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"\n5! = {factorial(5)}")
print(f"10! = {factorial(10)}")

# Example 4: Check prime
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"\n17 is prime: {is_prime(17)}")
print(f"20 is prime: {is_prime(20)}")

# Example 5: Reverse string
def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

print(f"\nReverse 'Python': {reverse_string('Python')}")

# Example 6: Count vowels
def count_vowels(text):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")

# ========== FUNCTION AS FIRST-CLASS OBJECTS ==========
print("\n" + "=" * 50)
print("FUNCTIONS AS OBJECTS")
print("=" * 50)

# Functions can be assigned to variables
def square(x):
    return x ** 2

# Assign function to variable
sq = square
print(f"square(5) = {square(5)}")
print(f"sq(5) = {sq(5)}")

# Functions can be passed as arguments
def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2

def triple(x):
    return x * 3

print(f"\nApply double to 5: {apply_operation(double, 5)}")
print(f"Apply triple to 5: {apply_operation(triple, 5)}")
print(f"Apply square to 5: {apply_operation(square, 5)}")

# Functions can be stored in data structures
operations = {
    "square": square,
    "double": double,
    "triple": triple
}

for name, func in operations.items():
    print(f"{name}(4) = {func(4)}")

print("\n" + "=" * 50)
print("✅ Functions Basics - Complete!")
print("=" * 50)
