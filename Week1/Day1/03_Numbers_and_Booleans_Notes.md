# Numbers and Booleans in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Numbers](#introduction-to-numbers)
2. [Integer Data Type](#integer-data-type)
3. [Float Data Type](#float-data-type)
4. [Complex Numbers](#complex-numbers)
5. [Number Systems and Conversions](#number-systems-and-conversions)
6. [Mathematical Operations](#mathematical-operations)
7. [Boolean Data Type](#boolean-data-type)
8. [Boolean Logic](#boolean-logic)
9. [Truthy and Falsy Values](#truthy-and-falsy-values)
10. [Math Module](#math-module)
11. [Random Module](#random-module)
12. [Decimal and Fraction Modules](#decimal-and-fraction-modules)
13. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Master integer, float, and complex number operations
- ✅ Understand number systems (binary, octal, hexadecimal)
- ✅ Work with boolean logic effectively
- ✅ Handle floating-point precision issues
- ✅ Use the math module for advanced operations
- ✅ Apply truthy/falsy concepts in conditions
- ✅ Generate random numbers

---

## Introduction to Numbers

### What are Numbers in Python?

Python supports several numeric types to represent different kinds of numbers:

1. **int** - Integers (whole numbers)
2. **float** - Floating-point numbers (decimals)
3. **complex** - Complex numbers (with real and imaginary parts)

```python
# Integer
age = 25
population = 7800000000

# Float
price = 19.99
pi = 3.14159

# Complex
z = 3 + 4j
```

**Real-World Analogy** 🌍

Think of number types like measuring tools:
- **Integers** = Counting objects (whole items)
- **Floats** = Measuring with precision (weight, distance)
- **Complex** = Advanced calculations (engineering, physics)

---

## Integer Data Type

### Creating Integers

```python
# Direct assignment
x = 42
y = -17
zero = 0

# From other types
from_float = int(3.9)    # 3 (truncates)
from_string = int("100") # 100
from_bool = int(True)    # 1
```

### Integer Properties

Python 3 integers have **unlimited precision**:

```python
# Extremely large numbers
googol = 10 ** 100
print(googol)  # Prints a 101-digit number!

# Factorial of large number
import math
huge = math.factorial(100)
print(huge)  # Massive number, Python handles it!

# In many languages, this would overflow
# Python handles it seamlessly
```

### Integer Arithmetic Operations

```python
a = 17
b = 5

# Addition
print(a + b)   # 22

# Subtraction  
print(a - b)   # 12

# Multiplication
print(a * b)   # 85

# Division (always returns float!)
print(a / b)   # 3.4

# Floor Division (returns integer)
print(a // b)  # 3

# Modulus (remainder)
print(a % b)   # 2

# Exponentiation (power)
print(a ** b)  # 1419857 (17^5)
```

### Understanding Floor Division

Floor division rounds toward negative infinity:

```python
# Positive numbers
print(17 // 5)   # 3
print(20 // 6)   # 3

# Negative numbers (rounds toward negative infinity!)
print(-17 // 5)  # -4 (not -3!)
print(17 // -5)  # -4
print(-17 // -5) # 3

# With floats (result is still floored)
print(17.5 // 5) # 3.0
```

### Understanding Modulus

The modulus operator returns the remainder:

```python
# Basic modulus
print(17 % 5)   # 2 (17 = 5*3 + 2)
print(20 % 6)   # 2 (20 = 6*3 + 2)
print(25 % 5)   # 0 (divides evenly)

# Negative numbers
print(-17 % 5)  # 3
print(17 % -5)  # -3
```

**Use Cases:**

```python
# 1. Check if even/odd
number = 42
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Get last digit
number = 12345
last_digit = number % 10  # 5

# 3. Cycle through values
for day in range(20):
    day_of_week = day % 7
    weekday_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    print(f"Day {day}: {weekday_names[day_of_week]}")

# 4. Check divisibility
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
```

### Augmented Assignment Operators

```python
count = 10

# Addition assignment
count += 5    # count = count + 5 → 15

# Subtraction assignment
count -= 3    # count = count - 3 → 12

# Multiplication assignment
count *= 2    # count = count * 2 → 24

# Floor division assignment
count //= 4   # count = count // 4 → 6

# Exponentiation assignment
count **= 2   # count = count ** 2 → 36

# Modulus assignment
count %= 7    # count = count % 7 → 1
```

### Comparison Operators

```python
x = 10
y = 20

print(x == y)   # False (equal to)
print(x != y)   # True (not equal)
print(x < y)    # True (less than)
print(x > y)    # False (greater than)
print(x <= y)   # True (less than or equal)
print(x >= y)   # False (greater than or equal)

# Chained comparisons (Pythonic!)
z = 15
print(10 < z < 20)     # True
print(10 <= z <= 20)   # True
```

### Bitwise Operations

Work with individual bits of integers:

```python
a = 5   # 0101 in binary
b = 3   # 0011 in binary

# Bitwise AND
print(a & b)   # 1 (0001)

# Bitwise OR
print(a | b)   # 7 (0111)

# Bitwise XOR
print(a ^ b)   # 6 (0110)

# Bitwise NOT
print(~a)      # -6 (inverts all bits)

# Left shift (multiply by 2^n)
print(a << 1)  # 10 (shift left by 1 = multiply by 2)
print(a << 2)  # 20 (shift left by 2 = multiply by 4)

# Right shift (divide by 2^n)
print(a >> 1)  # 2 (shift right by 1 = divide by 2)
```

**Practical Bitwise Operations:**

```python
# Check if number is even (fast method)
n = 42
is_even = (n & 1) == 0  # Last bit is 0 for even
print(is_even)  # True

# Multiply by power of 2 (fast)
n = 5
print(n << 3)  # 40 (5 * 2^3 = 5 * 8)

# Divide by power of 2 (fast)
n = 40
print(n >> 3)  # 5 (40 / 2^3 = 40 / 8)

# Swap two numbers without temporary variable
a, b = 5, 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 10, 5
```

---

## Float Data Type

### Creating Floats

```python
# Direct assignment
pi = 3.14159
price = 19.99
negative = -273.15

# Scientific notation
speed_of_light = 3e8       # 3 × 10^8 = 300,000,000
planck_constant = 6.626e-34  # Very small number

# From other types
from_int = float(42)        # 42.0
from_string = float("3.14") # 3.14
from_bool = float(True)     # 1.0
```

### Float Operations

```python
a = 10.5
b = 3.2

print(a + b)   # 13.7
print(a - b)   # 7.3
print(a * b)   # 33.6
print(a / b)   # 3.28125
print(a // b)  # 3.0 (float result!)
print(a % b)   # 0.9
print(a ** 2)  # 110.25
```

### Floating-Point Precision Issues ⚠️

Computers use binary to represent floats, causing precision errors:

```python
# The famous 0.1 + 0.2 problem
print(0.1 + 0.2)  # 0.30000000000000004 (not 0.3!)

# Why? Binary can't exactly represent 0.1
# Like how 1/3 = 0.333... in decimal

# More examples
print(0.1 + 0.1 + 0.1)  # 0.30000000000000004
print(1.2 - 1.0)         # 0.19999999999999996

# This affects comparisons
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False! (unexpected)
```

**Solutions to Precision Issues:**

```python
# 1. Use math.isclose() for comparisons
import math

a = 0.1 + 0.2
b = 0.3
print(math.isclose(a, b))  # True

# 2. Use decimal module for exact decimal arithmetic
from decimal import Decimal

a = Decimal('0.1') + Decimal('0.2')
b = Decimal('0.3')
print(a == b)  # True

# 3. Round to desired precision
a = round(0.1 + 0.2, 10)
b = 0.3
print(a == b)  # True

# 4. Use tolerance comparison
tolerance = 1e-9
a = 0.1 + 0.2
b = 0.3
print(abs(a - b) < tolerance)  # True
```

### Rounding Functions

```python
number = 3.14159

# round() - round to n decimal places
print(round(number, 2))   # 3.14
print(round(number, 3))   # 3.142
print(round(number))      # 3 (rounds to integer)

# Banker's rounding (rounds to nearest even)
print(round(2.5))   # 2
print(round(3.5))   # 4
print(round(4.5))   # 4

# import math for more rounding
import math
print(math.ceil(3.2))   # 4 (round up)
print(math.floor(3.9))  # 3 (round down)
print(math.trunc(3.9))  # 3 (truncate decimals)
```

### Special Float Values

```python
# Positive infinity
inf = float('inf')
print(inf)                # inf
print(inf > 1000000)      # True
print(inf + 100)          # inf
print(1 / inf)            # 0.0

# Negative infinity
neg_inf = float('-inf')
print(neg_inf < -1000000) # True

# Not a Number (NaN)
nan = float('nan')
print(nan)               # nan
print(nan == nan)        # False (NaN is never equal to anything!)
print(nan is nan)        # True (same object)

# Checking special values
import math
print(math.isinf(inf))        # True
print(math.isnan(nan))        # True
print(math.isfinite(3.14))    # True
print(math.isfinite(inf))     # False
```

### Scientific Notation

```python
# Very large numbers
avogadro = 6.022e23  # 6.022 × 10^23
print(avogadro)

# Very small numbers
electron_mass = 9.109e-31  # kg
print(electron_mass)

# In calculations
distance = 3e8 * 2  # Speed of light × 2 seconds
print(distance)     # 600000000.0
```

---

## Complex Numbers

### Creating Complex Numbers

```python
# Using j or J for imaginary unit
z1 = 3 + 4j
z2 = 2 - 5j
z3 = 1j  # Pure imaginary

# Using complex() function
z4 = complex(3, 4)  # 3 + 4j
z5 = complex(2)     # 2 + 0j

print(z1)  # (3+4j)
```

### Accessing Real and Imaginary Parts

```python
z = 3 + 4j

print(z.real)  # 3.0
print(z.imag)  # 4.0

# Conjugate
print(z.conjugate())  # (3-4j)

# Magnitude (absolute value)
print(abs(z))  # 5.0 (√(3² + 4²))
```

### Complex Number Operations

```python
z1 = 3 + 4j
z2 = 1 + 2j

# Addition
print(z1 + z2)  # (4+6j)

# Subtraction
print(z1 - z2)  # (2+2j)

# Multiplication
print(z1 * z2)  # (-5+10j)

# Division
print(z1 / z2)  # (2.2-0.4j)

# Power
print(z1 ** 2)  # (-7+24j)
```

---

## Number Systems and Conversions

### Binary (Base 2)

```python
# Binary literals (prefix: 0b)
binary = 0b1010  # 10 in decimal
print(binary)    # 10

# Convert to binary
decimal = 10
print(bin(decimal))  # '0b1010'

# Binary arithmetic
a = 0b1010  # 10
b = 0b0101  # 5
print(a + b)     # 15
print(bin(a + b)) # '0b1111'

# Convert binary string to int
binary_str = '1010'
decimal = int(binary_str, 2)
print(decimal)  # 10
```

### Octal (Base 8)

```python
# Octal literals (prefix: 0o)
octal = 0o12  # 10 in decimal
print(octal)  # 10

# Convert to octal
decimal = 10
print(oct(decimal))  # '0o12'

# Convert octal string to int
octal_str = '12'
decimal = int(octal_str, 8)
print(decimal)  # 10
```

### Hexadecimal (Base 16)

```python
# Hexadecimal literals (prefix: 0x)
hexa = 0xA   # 10 in decimal
print(hexa)  # 10

# Hex uses 0-9, A-F
color = 0xFF  # 255 in decimal
print(color)  # 255

# Convert to hexadecimal
decimal = 255
print(hex(decimal))  # '0xff'

# Convert hex string to int
hex_str = 'FF'
decimal = int(hex_str, 16)
print(decimal)  # 255
```

### Number System Conversions

```python
number = 42

# To different bases
print(f"Decimal: {number}")          # 42
print(f"Binary: {bin(number)}")      # 0b101010
print(f"Octal: {oct(number)}")       # 0o52
print(f"Hexadecimal: {hex(number)}") # 0x2a

# From different bases to decimal
print(int('101010', 2))   # 42 (binary)
print(int('52', 8))       # 42 (octal)
print(int('2a', 16))      # 42 (hex)

# Format with different bases
print(f"{number:b}")   # 101010 (binary, no prefix)
print(f"{number:o}")   # 52 (octal, no prefix)
print(f"{number:x}")   # 2a (hex lowercase)
print(f"{number:X}")   # 2A (hex uppercase)
```

---

## Mathematical Operations

### Absolute Value

```python
print(abs(-5))        # 5
print(abs(3.14))      # 3.14
print(abs(-10.7))     # 10.7
print(abs(3 + 4j))    # 5.0 (magnitude)
```

### Power and Roots

```python
# pow() function
print(pow(2, 3))      # 8 (2³)
print(pow(2, 3, 5))   # 3 ((2³) % 5)

# ** operator
print(2 ** 3)         # 8

# Square root
import math
print(math.sqrt(16))  # 4.0
print(16 ** 0.5)      # 4.0 (alternative)

# Cube root
print(27 ** (1/3))    # 3.0

# nth root
n = 4
number = 16
print(number ** (1/n))  # 2.0 (4th root of 16)
```

### Min and Max

```python
# min() and max()
print(min(5, 2, 8, 1))  # 1
print(max(5, 2, 8, 1))  # 8

# With lists
numbers = [5, 2, 8, 1, 9]
print(min(numbers))  # 1
print(max(numbers))  # 9

# Multiple arguments
print(min(5, 2, 8, 1, 9))  # 1
```

### Sum

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15

# With start value
print(sum(numbers, 10))  # 25 (10 + sum of list)

# Sum of range
print(sum(range(1, 11)))  # 55 (1+2+...+10)
```

### Divmod

Get quotient and remainder together:

```python
quotient, remainder = divmod(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")
# 17 ÷ 5 = 3 remainder 2

# Useful for time conversion
total_seconds = 3725
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)
print(f"{hours}h {minutes}m {seconds}s")
# 1h 2m 5s
```

---

## Boolean Data Type

### Creating Booleans

```python
# Boolean literals
is_active = True
is_complete = False

# From comparisons
age = 25
is_adult = age >= 18  # True

# From bool() function
print(bool(1))        # True
print(bool(0))        # False
print(bool("text"))   # True
print(bool(""))       # False
```

### Boolean Values

```python
# Only two boolean values
print(True)   # True
print(False)  # False

# Type
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# Booleans are subclass of int
print(isinstance(True, int))   # True
print(isinstance(False, int))  # True

# Numeric values
print(int(True))   # 1
print(int(False))  # 0

# Arithmetic with booleans
print(True + True)    # 2
print(True * 5)       # 5
print(False * 100)    # 0
```

---

## Boolean Logic

### AND Operator

```python
# Truth table
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Practical example
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(can_drive)  # True
```

### OR Operator

```python
# Truth table
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Practical example
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True
```

### NOT Operator

```python
# Negation
print(not True)   # False
print(not False)  # True

# Practical example
is_raining = False
should_go_outside = not is_raining
print(should_go_outside)  # True
```

### Combined Logic

```python
# Complex conditions
age = 25
has_ticket = True
is_member = False

# (has ticket OR is member) AND age >= 18
can_enter = (has_ticket or is_member) and age >= 18
print(can_enter)  # True

# De Morgan's Laws
# not (A and B) == (not A) or (not B)
# not (A or B) == (not A) and (not B)
```

### Short-Circuit Evaluation

```python
# AND stops at first False
result = False and expensive_function()
# expensive_function() never runs!

# OR stops at first True
result = True or expensive_function()
# expensive_function() never runs!

# Practical use
x = 10
y = 0
if y != 0 and x / y > 5:
    print("Safe!")
# Division never happens because y != 0 is False
```

---

## Truthy and Falsy Values

### Falsy Values

These evaluate to False in boolean context:

```python
# Explicit False
bool(False)      # False

# None
bool(None)       # False

# Numeric zeros
bool(0)          # False
bool(0.0)        # False
bool(0j)         # False

# Empty sequences
bool("")         # False
bool([])         # False
bool(())         # False
bool({})         # False
bool(set())      # False
bool(range(0))   # False
```

### Truthy Values

Everything else evaluates to True:

```python
bool(True)       # True
bool(1)          # True
bool(-1)         # True
bool(0.1)        # True
bool("text")     # True
bool(" ")        # True (single space!)
bool([1])        # True
bool([0])        # True (list with zero is truthy!)
bool({"a": 0})   # True
```

### Practical Uses

```python
# Check if string is not empty
name = input("Enter name: ")
if name:  # Truthy if not empty
    print(f"Hello, {name}!")
else:
    print("No name provided")

# Check if list has items
items = []
if items:
    print(f"You have {len(items)} items")
else:
    print("Your cart is empty")

# Default values
user_input = ""
name = user_input or "Guest"  # "Guest" (because "" is falsy)
print(name)
```

---

## Math Module

### Importing Math Module

```python
import math

# Or import specific functions
from math import sqrt, pi, sin, cos
```

### Rounding Functions

```python
import math

# ceil() - round up
print(math.ceil(3.2))   # 4
print(math.ceil(3.9))   # 4
print(math.ceil(-3.2))  # -3

# floor() - round down
print(math.floor(3.2))  # 3
print(math.floor(3.9))  # 3
print(math.floor(-3.2)) # -4

# trunc() - truncate (remove decimals)
print(math.trunc(3.9))   # 3
print(math.trunc(-3.9))  # -3
```

### Power and Logarithm Functions

```python
import math

# sqrt() - square root
print(math.sqrt(16))    # 4.0
print(math.sqrt(2))     # 1.4142135623730951

# pow() - power
print(math.pow(2, 3))   # 8.0

# exp() - e^x
print(math.exp(1))      # 2.718281828459045 (e)

# log() - natural logarithm
print(math.log(math.e))  # 1.0

# log(x, base) - logarithm with custom base
print(math.log(100, 10))  # 2.0 (log₁₀(100))
print(math.log(8, 2))     # 3.0 (log₂(8))

# log10() - base 10 logarithm
print(math.log10(100))  # 2.0

# log2() - base 2 logarithm
print(math.log2(8))     # 3.0
```

### Trigonometric Functions

```python
import math

# sin, cos, tan (input in radians!)
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))             # 1.0
print(math.tan(math.pi / 4))   # 1.0

# Convert degrees to radians
degrees = 90
radians = math.radians(degrees)
print(math.sin(radians))  # 1.0

# Convert radians to degrees
print(math.degrees(math.pi))  # 180.0

# Inverse trig functions
print(math.asin(1))  # π/2
print(math.acos(1))  # 0
print(math.atan(1))  # π/4
```

### Constants

```python
import math

# π (pi)
print(math.pi)   # 3.141592653589793

# e (Euler's number)
print(math.e)    # 2.718281828459045

# τ (tau = 2π)
print(math.tau)  # 6.283185307179586

# inf (infinity)
print(math.inf)  # inf

# nan (not a number)
print(math.nan)  # nan
```

### Other Useful Functions

```python
import math

# factorial
print(math.factorial(5))  # 120 (5!)

# gcd - greatest common divisor
print(math.gcd(48, 18))  # 6

# hypot - hypotenuse (√(x² + y²))
print(math.hypot(3, 4))  # 5.0

# copysign - copy sign of number
print(math.copysign(5, -1))  # -5.0

# fabs - absolute value (float)
print(math.fabs(-3.14))  # 3.14

# fmod - floating-point remainder
print(math.fmod(10, 3))  # 1.0

# isclose() - check if two floats are close
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

---

## Random Module

### Generating Random Numbers

```python
import random

# Random float between 0.0 and 1.0
print(random.random())  # e.g., 0.7234...

# Random integer in range [a, b]
print(random.randint(1, 10))  # e.g., 7

# Random integer from range
print(random.randrange(1, 10))  # 1 to 9 (10 excluded)
print(random.randrange(0, 100, 5))  # 0, 5, 10, ..., 95

# Random float in range [a, b]
print(random.uniform(1.0, 10.0))  # e.g., 5.789...
```

### Random Choices

```python
import random

# Choose random element from list
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))  # e.g., 'banana'

# Choose k random elements (with replacement)
print(random.choices(fruits, k=2))  # e.g., ['apple', 'apple']

# Choose k random elements (without replacement)
print(random.sample(fruits, k=2))  # e.g., ['banana', 'orange']

# Shuffle list in-place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # e.g., [3, 1, 5, 2, 4]
```

### Setting Random Seed

```python
import random

# Set seed for reproducible results
random.seed(42)
print(random.random())  # Always same result with seed 42

random.seed(42)
print(random.random())  # Same as above

# Without seed, different each time
print(random.random())
```

---

## Decimal and Fraction Modules

### Decimal Module (Exact Decimal Arithmetic)

```python
from decimal import Decimal

# Exact decimal arithmetic
a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)  # 0.3 (exact!)

# Compared to float
print(0.1 + 0.2)  # 0.30000000000000004

# Financial calculations
price = Decimal('19.99')
quantity = Decimal('3')
total = price * quantity
print(total)  # 59.97 (exact)

# Set precision
from decimal import getcontext
getcontext().prec = 6  # 6 significant figures
print(Decimal(1) / Decimal(7))  # 0.142857
```

### Fraction Module

```python
from fractions import Fraction

# Create fractions
f1 = Fraction(1, 3)   # 1/3
f2 = Fraction(1, 6)   # 1/6

# Arithmetic
print(f1 + f2)  # 1/2
print(f1 * 2)   # 2/3

# From float
f3 = Fraction(0.25)
print(f3)  # 1/4

# From string
f4 = Fraction('3/4')
print(f4)  # 3/4

# Get numerator and denominator
print(f4.numerator)    # 3
print(f4.denominator)  # 4
```

---

## Practice Exercises

### Beginner Exercises

**Exercise 1**: Calculate Circle Area
```python
# Given radius = 5, calculate area (π × r²)
# Use math.pi
```

**Exercise 2**: Temperature Converter
```python
# Convert 25°C to Fahrenheit
# Formula: F = (C × 9/5) + 32
```

**Exercise 3**: Even or Odd
```python
# Check if number is even or odd using modulus
number = 17
```

**Exercise 4**: Absolute Value
```python
# Calculate absolute value without using abs()
number = -42
```

**Exercise 5**: Power Calculator
```python
# Calculate 2^10 using ** operator
```

### Intermediate Exercises

**Exercise 6**: Compound Interest
```python
# Calculate compound interest
# A = P(1 + r/n)^(nt)
# P = 1000, r = 0.05, n = 4, t = 3
```

**Exercise 7**: Distance Between Points
```python
# Calculate distance between two 2D points
# Distance = √((x2-x1)² + (y2-y1)²)
x1, y1 = 0, 0
x2, y2 = 3, 4
```

**Exercise 8**: Prime Number Check
```python
# Check if number is prime
number = 17
```

**Exercise 9**: Binary to Decimal
```python
# Convert binary string to decimal
binary_str = "1101"
# Expected: 13
```

**Exercise 10**: Random Dice Roll
```python
# Simulate rolling two 6-sided dice
# Print sum
```

### Advanced Exercises

**Exercise 11**: Fibonacci Sequence
```python
# Generate first 10 Fibonacci numbers
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

**Exercise 12**: Factorial Calculator
```python
# Calculate factorial without math.factorial()
n = 5
# Expected: 120
```

**Exercise 13**: GCD Calculator
```python
# Calculate GCD without math.gcd() using Euclidean algorithm
a, b = 48, 18
# Expected: 6
```

**Exercise 14**: Quadratic Formula
```python
# Solve ax² + bx + c = 0
# x = (-b ± √(b²-4ac)) / 2a
a, b, c = 1, -5, 6
# Find both roots
```

**Exercise 15**: Number Guessing Game
```python
# Computer picks random number 1-100
# Player guesses, computer says higher/lower
# Count number of guesses
```

---

## 🎯 Key Takeaways

✅ **Integers**: Unlimited precision in Python 3  
✅ **Floats**: Be careful with precision issues  
✅ **Complex**: Use j for imaginary part  
✅ **Bitwise**: Work with individual bits  
✅ **Number Systems**: Binary (0b), Octal (0o), Hex (0x)  
✅ **Booleans**: True, False, and/or/not  
✅ **Truthy/Falsy**: Everything has boolean value  
✅ **Math Module**: Advanced mathematical functions  
✅ **Random Module**: Generate random numbers  
✅ **Decimal/Fraction**: Exact arithmetic  

---

## 📚 Quick Reference

```python
# Integer operations
+  -  *  /  //  %  **

# Number conversions
int()  float()  complex()

# Number systems
bin()  oct()  hex()
int(str, base)

# Boolean operations
and  or  not

# Math module
import math
math.sqrt()  math.ceil()  math.floor()
math.sin()  math.cos()  math.log()
math.pi  math.e

# Random module
import random
random.random()  random.randint(a, b)
random.choice(seq)  random.shuffle(list)

# Decimal (exact)
from decimal import Decimal
Decimal('0.1') + Decimal('0.2')

# Fractions
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)
```

---

**End of Numbers and Booleans Notes** 📝

Continue to other topics for complete Python mastery!
