"""
Day 1 - Numbers and Booleans
=============================
Learn: Numeric types (int, float), mathematical operations, boolean logic

Key Concepts:
- Python supports integers, floating-point, and complex numbers
- Built-in math functions
- Boolean values: True and False
- Truthy and Falsy values
"""

# ========== INTEGERS ==========
print("=" * 50)
print("INTEGERS")
print("=" * 50)

# Integer basics
x = 10
y = -5
z = 0

print(f"Positive integer: {x}")
print(f"Negative integer: {y}")
print(f"Zero: {z}")

# Large integers (Python handles any size)
big_num = 123456789012345678901234567890
print(f"Large integer: {big_num}")

# Integer operations
print(f"\n10 + 5 = {10 + 5}")
print(f"10 - 5 = {10 - 5}")
print(f"10 * 5 = {10 * 5}")
print(f"10 / 5 = {10 / 5}")  # Returns float
print(f"10 // 3 = {10 // 3}")  # Floor division
print(f"10 % 3 = {10 % 3}")  # Modulus
print(f"2 ** 8 = {2 ** 8}")  # Exponentiation

# ========== FLOATING-POINT NUMBERS ==========
print("\n" + "=" * 50)
print("FLOATING-POINT NUMBERS")
print("=" * 50)

# Float basics
a = 3.14
b = -2.5
c = 0.0

print(f"Positive float: {a}")
print(f"Negative float: {b}")
print(f"Zero float: {c}")

# Scientific notation
sci_num = 1.5e3  # 1.5 * 10^3 = 1500
print(f"Scientific notation (1.5e3): {sci_num}")

# Float precision
result = 0.1 + 0.2
print(f"\n0.1 + 0.2 = {result}")  # Not exactly 0.3!
print(f"Rounded to 1 decimal: {round(result, 1)}")

# ========== BUILT-IN MATH FUNCTIONS ==========
print("\n" + "=" * 50)
print("BUILT-IN MATH FUNCTIONS")
print("=" * 50)

numbers = [10, -5, 3.14, -2.5, 0]
print(f"Numbers: {numbers}")

print(f"abs(-5): {abs(-5)}")  # Absolute value
print(f"round(3.14159, 2): {round(3.14159, 2)}")  # Round to 2 decimals
print(f"max(numbers): {max(numbers)}")  # Maximum
print(f"min(numbers): {min(numbers)}")  # Minimum
print(f"sum([1,2,3,4,5]): {sum([1,2,3,4,5])}")  # Sum

# Power and square root
print(f"\npow(2, 3): {pow(2, 3)}")  # 2^3
print(f"pow(16, 0.5): {pow(16, 0.5)}")  # Square root

# ========== MATH MODULE ==========
print("\n" + "=" * 50)
print("MATH MODULE")
print("=" * 50)

import math

print(f"math.pi: {math.pi}")
print(f"math.e: {math.e}")

print(f"\nmath.sqrt(16): {math.sqrt(16)}")
print(f"math.ceil(3.2): {math.ceil(3.2)}")  # Round up
print(f"math.floor(3.8): {math.floor(3.8)}")  # Round down

print(f"\nmath.sin(math.pi/2): {math.sin(math.pi/2)}")
print(f"math.cos(0): {math.cos(0)}")
print(f"math.log(10): {math.log(10)}")  # Natural log
print(f"math.log10(100): {math.log10(100)}")  # Base 10 log

# ========== BOOLEANS ==========
print("\n" + "=" * 50)
print("BOOLEANS")
print("=" * 50)

# Boolean basics
is_python_fun = True
is_difficult = False

print(f"Type of True: {type(True)}")
print(f"Type of False: {type(False)}")

# Boolean from comparisons
print(f"\n10 > 5: {10 > 5}")
print(f"10 == 10: {10 == 10}")
print(f"5 != 5: {5 != 5}")

# ========== TRUTHY AND FALSY VALUES ==========
print("\n" + "=" * 50)
print("TRUTHY AND FALSY VALUES")
print("=" * 50)

# Falsy values
print("Falsy values (evaluate to False):")
print(f"bool(0): {bool(0)}")
print(f"bool(0.0): {bool(0.0)}")
print(f"bool(''): {bool('')}")  # Empty string
print(f"bool([]): {bool([])}")  # Empty list
print(f"bool({{}}): {bool({})}")  # Empty dict
print(f"bool(None): {bool(None)}")

# Truthy values
print("\nTruthy values (evaluate to True):")
print(f"bool(1): {bool(1)}")
print(f"bool(-1): {bool(-1)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([1,2,3]): {bool([1,2,3])}")

# ========== BOOLEAN OPERATIONS ==========
print("\n" + "=" * 50)
print("BOOLEAN OPERATIONS")
print("=" * 50)

a = True
b = False

print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"not b: {not b}")

# Chaining comparisons
x = 5
print(f"\nx = {x}")
print(f"1 < x < 10: {1 < x < 10}")
print(f"10 < x < 20: {10 < x < 20}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Calculate area of a circle
radius = 5
area = math.pi * radius ** 2
print(f"Circle with radius {radius}")
print(f"Area: {area:.2f} square units")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"\n{celsius}°C = {fahrenheit}°F")

# Check if number is positive, negative, or zero
number = -10
is_positive = number > 0
is_negative = number < 0
is_zero = number == 0

print(f"\nNumber: {number}")
print(f"Is positive? {is_positive}")
print(f"Is negative? {is_negative}")
print(f"Is zero? {is_zero}")

# Calculate compound interest
principal = 1000
rate = 0.05  # 5%
time = 5  # years
amount = principal * (1 + rate) ** time
print(f"\nPrincipal: ${principal}")
print(f"Rate: {rate*100}%")
print(f"Time: {time} years")
print(f"Final Amount: ${amount:.2f}")
print(f"Interest Earned: ${amount - principal:.2f}")

# Check eligibility
age = 20
has_id = True
can_enter = age >= 18 and has_id
print(f"\nAge: {age}, Has ID: {has_id}")
print(f"Can enter: {can_enter}")

print("\n" + "=" * 50)
print("✅ Numbers and Booleans - Complete!")
print("=" * 50)
