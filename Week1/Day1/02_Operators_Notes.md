# Python Operators - Complete Guide

## 📚 Table of Contents
1. [Introduction to Operators](#introduction-to-operators)
2. [Arithmetic Operators](#arithmetic-operators)
3. [Comparison Operators](#comparison-operators)
4. [Logical Operators](#logical-operators)
5. [Assignment Operators](#assignment-operators)
6. [Identity Operators](#identity-operators)
7. [Membership Operators](#membership-operators)
8. [Bitwise Operators](#bitwise-operators)
9. [Operator Precedence](#operator-precedence)
10. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Master all Python operator types
- ✅ Understand operator precedence and associativity
- ✅ Use arithmetic operators for calculations
- ✅ Apply comparison and logical operators in conditions
- ✅ Work with assignment operators efficiently
- ✅ Understand identity and membership testing
- ✅ Know when to use each operator type

---

## Introduction to Operators

### What are Operators?

**Operators** are special symbols that perform operations on values and variables. Think of them as the verbs of programming - they tell Python what action to perform.

```python
# Examples of operators in action
result = 5 + 3      # + is an operator
is_equal = x == y   # == is an operator
combined = a and b  # and is an operator
```

### Types of Operators

Python has 7 main categories:

1. **Arithmetic** - Math operations (+, -, *, /, etc.)
2. **Comparison** - Compare values (==, !=, <, >, etc.)
3. **Logical** - Combine conditions (and, or, not)
4. **Assignment** - Assign values (=, +=, -=, etc.)
5. **Identity** - Test object identity (is, is not)
6. **Membership** - Test membership (in, not in)
7. **Bitwise** - Manipulate bits (&, |, ^, etc.)

---

## Arithmetic Operators

Arithmetic operators perform mathematical calculations.

### Basic Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| + | Addition | 5 + 3 | 8 |
| - | Subtraction | 5 - 3 | 2 |
| * | Multiplication | 5 * 3 | 15 |
| / | Division | 5 / 2 | 2.5 |
| // | Floor Division | 5 // 2 | 2 |
| % | Modulus | 5 % 2 | 1 |
| ** | Exponentiation | 5 ** 2 | 25 |

### Addition (+)

Adds two numbers or concatenates strings:

```python
# Numbers
print(10 + 5)        # 15
print(3.5 + 2.1)     # 5.6
print(-5 + 10)       # 5

# Strings (concatenation)
print("Hello" + " " + "World")  # "Hello World"
print("Python" + "3")           # "Python3"

# Lists (concatenation)
print([1, 2] + [3, 4])  # [1, 2, 3, 4]
```

**Real-World Example:**
```python
# Shopping cart total
item1_price = 29.99
item2_price = 14.50
item3_price = 8.99

total = item1_price + item2_price + item3_price
print(f"Total: ${total:.2f}")  # Total: $53.48
```

### Subtraction (-)

Subtracts the second number from the first:

```python
print(10 - 3)        # 7
print(5.5 - 2.3)     # 3.2
print(0 - 5)         # -5 (negative result)
```

**Real-World Example:**
```python
# Calculate days remaining
total_days = 365
days_passed = 100
days_remaining = total_days - days_passed
print(f"Days left: {days_remaining}")  # Days left: 265
```

### Multiplication (*)

Multiplies two numbers or repeats sequences:

```python
# Numbers
print(5 * 3)         # 15
print(2.5 * 4)       # 10.0
print(-3 * 2)        # -6

# String repetition
print("Ha" * 3)      # "HaHaHa"
print("-" * 20)      # "--------------------"

# List repetition
print([0] * 5)       # [0, 0, 0, 0, 0]
print([1, 2] * 3)    # [1, 2, 1, 2, 1, 2]
```

**Real-World Example:**
```python
# Calculate rectangle area
length = 10
width = 5
area = length * width
print(f"Area: {area} square units")  # Area: 50 square units
```

### Division (/)

Divides first number by second, **always returns float**:

```python
print(10 / 2)        # 5.0 (float, not 5!)
print(7 / 2)         # 3.5
print(1 / 3)         # 0.3333333333333333
print(10 / 4)        # 2.5
```

**Important:** Even when result is a whole number, division returns float!

```python
result = 10 / 2
print(result)        # 5.0
print(type(result))  # <class 'float'>
```

**Real-World Example:**
```python
# Calculate average
total_score = 285
num_tests = 3
average = total_score / num_tests
print(f"Average: {average:.2f}")  # Average: 95.00
```

### Floor Division (//)

Divides and **rounds down** to nearest integer:

```python
print(10 // 3)       # 3 (not 3.333...)
print(15 // 4)       # 3 (not 3.75)
print(20 // 6)       # 3 (not 3.333...)
```

**With floats:**
```python
print(10.0 // 3)     # 3.0 (still floor division, but float result)
print(7.5 // 2)      # 3.0
```

**Negative numbers** (rounds toward negative infinity):
```python
print(10 // 3)       # 3
print(-10 // 3)      # -4 (not -3!)
print(10 // -3)      # -4
```

**Real-World Example:**
```python
# How many full boxes can we make?
total_items = 47
items_per_box = 12
full_boxes = total_items // items_per_box
print(f"Full boxes: {full_boxes}")  # Full boxes: 3
```

### Modulus (%)

Returns the **remainder** after division:

```python
print(10 % 3)        # 1 (10 = 3*3 + 1)
print(15 % 4)        # 3 (15 = 4*3 + 3)
print(20 % 5)        # 0 (divides evenly)
print(7 % 2)         # 1 (odd number)
print(8 % 2)         # 0 (even number)
```

**Use Case 1: Check Even/Odd**
```python
number = 17
if number % 2 == 0:
    print("Even")
else:
    print("Odd")  # Prints "Odd"
```

**Use Case 2: Get Last Digit**
```python
number = 12345
last_digit = number % 10
print(last_digit)  # 5
```

**Use Case 3: Wrap Around (Circular Array)**
```python
# Days of week (0-6)
for day in range(20):
    day_of_week = day % 7
    print(f"Day {day} -> Day of week {day_of_week}")
# Outputs: 0,1,2,3,4,5,6,0,1,2,3,4,5,6...
```

**Use Case 4: Get Leftover Items**
```python
total_items = 47
items_per_box = 12
leftover = total_items % items_per_box
print(f"Leftover items: {leftover}")  # Leftover items: 11
```

### Exponentiation (**)

Raises first number to the power of second:

```python
print(2 ** 3)        # 8 (2³)
print(5 ** 2)        # 25 (5²)
print(10 ** 0)       # 1 (anything⁰ = 1)
print(2 ** -1)       # 0.5 (negative exponent)
print(4 ** 0.5)      # 2.0 (square root!)
```

**Square and Cube:**
```python
number = 5
square = number ** 2      # 25
cube = number ** 3        # 125
```

**Square Root:**
```python
number = 16
square_root = number ** 0.5  # 4.0

# Or use math module
import math
square_root = math.sqrt(16)  # 4.0
```

**Real-World Example:**
```python
# Compound interest calculation
principal = 1000
rate = 0.05  # 5%
years = 3
amount = principal * (1 + rate) ** years
print(f"Amount after {years} years: ${amount:.2f}")
# Amount after 3 years: $1157.63
```

### Unary Operators

Operators that work with single operands:

```python
# Unary plus (doesn't change value)
x = 5
print(+x)    # 5

# Unary minus (negates value)
print(-x)    # -5

y = -10
print(-y)    # 10 (double negative)
```

### Mixed Type Arithmetic

When mixing types, Python converts to most general type:

```python
# int + float = float
result = 5 + 2.5
print(result)       # 7.5
print(type(result)) # <class 'float'>

# int + int = int
result = 5 + 3
print(result)       # 8
print(type(result)) # <class 'int'>

# float + float = float
result = 2.5 + 3.7
print(result)       # 6.2
print(type(result)) # <class 'float'>
```

---

## Comparison Operators

Comparison operators compare values and return **True** or **False**.

### All Comparison Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| == | Equal to | 5 == 5 | True |
| != | Not equal | 5 != 3 | True |
| < | Less than | 3 < 5 | True |
| > | Greater than | 5 > 3 | True |
| <= | Less than or equal | 3 <= 3 | True |
| >= | Greater than or equal | 5 >= 3 | True |

### Equal To (==)

Tests if two values are equal:

```python
print(5 == 5)        # True
print(5 == 3)        # False
print("hi" == "hi")  # True
print("Hi" == "hi")  # False (case-sensitive)

# Works with different types (compares values)
print(5 == 5.0)      # True
print(True == 1)     # True
print(False == 0)    # True
```

**Real-World Example:**
```python
password = input("Enter password: ")
if password == "secret123":
    print("Access granted!")
else:
    print("Access denied!")
```

### Not Equal To (!=)

Tests if two values are different:

```python
print(5 != 3)        # True
print(5 != 5)        # False
print("cat" != "dog") # True
```

**Real-World Example:**
```python
status = "inactive"
if status != "active":
    print("Please activate your account")
```

### Less Than (<)

Tests if left value is smaller:

```python
print(3 < 5)         # True
print(5 < 3)         # False
print(5 < 5)         # False (not less than, equal)

# Strings (alphabetical order)
print("apple" < "banana")  # True
print("z" < "a")           # False
```

### Greater Than (>)

Tests if left value is larger:

```python
print(5 > 3)         # True
print(3 > 5)         # False
print(5 > 5)         # False
```

### Less Than or Equal (<=)

```python
print(3 <= 5)        # True
print(5 <= 5)        # True (equal counts!)
print(7 <= 5)        # False
```

**Real-World Example:**
```python
age = 17
if age <= 17:
    print("You are a minor")
```

### Greater Than or Equal (>=)

```python
print(5 >= 3)        # True
print(5 >= 5)        # True
print(3 >= 5)        # False
```

**Real-World Example:**
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This executes
elif score >= 70:
    grade = "C"
print(grade)  # B
```

### Chained Comparisons

Python allows elegant chained comparisons:

```python
x = 15

# Instead of this:
if x > 10 and x < 20:
    print("In range")

# Write this (more Pythonic):
if 10 < x < 20:
    print("In range")

# Multiple chains
if 0 <= x <= 100:
    print("Valid percentage")

# Complex chains
if 10 < x < 20 < 30:
    print("All conditions true")
```

### Comparing Different Types

```python
# Numbers
print(5 == 5.0)      # True (values are equal)
print(5 is 5.0)      # False (different types/objects)

# Strings
print("10" == 10)    # False (string vs int)
print("10" < "9")    # True (string comparison, alphabetical)

# Comparisons with None
print(None == None)  # True
print(None == 0)     # False
print(None == "")    # False
```

---

## Logical Operators

Logical operators combine boolean expressions.

### The Three Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| and | True if both are True | True and False → False |
| or | True if at least one is True | True or False → True |
| not | Inverts the value | not True → False |

### AND Operator

Returns **True** only if **both** conditions are True:

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

**Truth Table for AND:**
```
A     | B     | A and B
------|-------|--------
True  | True  | True
True  | False | False
False | True  | False
False | False | False
```

**Real-World Example:**
```python
age = 25
has_license = True
has_insurance = True

# Can drive only if ALL conditions are True
can_drive = age >= 18 and has_license and has_insurance
if can_drive:
    print("You can drive!")  # This prints
```

### OR Operator

Returns **True** if **at least one** condition is True:

```python
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

**Truth Table for OR:**
```
A     | B     | A or B
------|-------|-------
True  | True  | True
True  | False | True
False | True  | True
False | False | False
```

**Real-World Example:**
```python
is_weekend = True
is_holiday = False

# Can sleep in if it's weekend OR holiday
can_sleep_in = is_weekend or is_holiday
if can_sleep_in:
    print("Sleep in!")  # This prints
```

### NOT Operator

**Inverts** the boolean value:

```python
print(not True)         # False
print(not False)        # True
print(not (5 > 3))      # False (because 5 > 3 is True)
```

**Real-World Example:**
```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")  # This prints
```

### Combining Logical Operators

```python
# Complex conditions
age = 25
has_ticket = True
is_member = False

# Can enter if: (has ticket OR is member) AND age >= 18
can_enter = (has_ticket or is_member) and age >= 18
print(can_enter)  # True

# Another example
score = 85
attended = True
passed = score >= 60 and attended
print(passed)  # True
```

### Short-Circuit Evaluation

Python stops evaluating as soon as result is determined:

```python
# AND: stops at first False
def expensive_check():
    print("Expensive operation!")
    return True

result = False and expensive_check()
# "Expensive operation!" never prints!
# False AND anything = False, so no need to check second part

# OR: stops at first True
result = True or expensive_check()
# Also doesn't print!
# True OR anything = True
```

**Practical Use:**
```python
# Avoid division by zero
x = 10
y = 0

if y != 0 and x / y > 5:  # Safe!
    print("Greater than 5")
# y != 0 is False, so x / y never executes
```

### De Morgan's Laws

Useful for simplifying logic:

```python
# These are equivalent:
not (A and B) == (not A) or (not B)
not (A or B) == (not A) and (not B)

# Example
not (True and False) == (not True) or (not False)
# not False == False or True
# True == True ✓
```

---

## Assignment Operators

Assignment operators assign values to variables.

### Basic Assignment (=)

```python
x = 10           # Assign 10 tothe variable x
name = "Alice"   # Assign string to name
values = [1, 2, 3]  # Assign list
```

### Augmented Assignment Operators

Shortcuts for common operations:

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| += | x += 5 | x = x + 5 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 2 | x = x * 2 |
| /= | x /= 4 | x = x / 4 |
| //= | x //= 4 | x = x // 4 |
| %= | x %= 3 | x = x % 3 |
| **= | x **= 2 | x = x ** 2 |

### Addition Assignment (+=)

```python
count = 10
count += 5  # Same as: count = count + 5
print(count)  # 15

# Also works with strings
message = "Hello"
message += " World"
print(message)  # "Hello World"

# And lists
numbers = [1, 2, 3]
numbers += [4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
```

### Subtraction Assignment (-=)

```python
balance = 1000
balance -= 250  # Deduct 250
print(balance)  # 750
```

### Multiplication Assignment (*=)

```python
price = 10
price *= 3  # Triple the price
print(price)  # 30
```

### Division Assignment (/=)

```python
total = 100
total /= 4  # Divide by 4
print(total)  # 25.0 (note: float!)
```

### Floor Division Assignment (//=)

```python
value = 17
value //= 5  # Floor divide by 5
print(value)  # 3
```

### Modulus Assignment (%=)

```python
number = 17
number %= 5  # Get remainder
print(number)  # 2
```

### Exponentiation Assignment (**=)

```python
base = 2
base **= 10  # 2 to the power of 10
print(base)  # 1024
```

### Multiple Assignment

```python
# Assign same value to multiple variables
x = y = z = 0
print(x, y, z)  # 0 0 0

# Assign different values
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap values
a, b = 10, 20
a, b = b, a  # Swap!
print(a, b)  # 20 10
```

---

## Identity Operators

Identity operators test if two variables refer to the **same object** in memory.

### Is Operator

Tests if two variables point to the same object:

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # False (different objects, same values)
print(x is z)  # True (same object)
print(x == y)  # True (same values)
```

**Visualizing:**
```
x → [1, 2, 3]  (Object A in memory)
y → [1, 2, 3]  (Object B in memory)
z → [1, 2, 3]  (Points to Object A)

x is y: False (different objects)
x is z: True (same object)
```

### Is Not Operator

Tests if two variables point to different objects:

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y)  # True (different objects)
```

### When to Use 'is'

Use `is` for:
1. **None** checks
2. **True/False** checks
3. Checking if objects are same instance

```python
# ✅ CORRECT - Use 'is' with None
value = None
if value is None:
    print("No value")

# ✅ CORRECT - Use 'is' with boolean literals
flag = True
if flag is True:
    print("Enabled")
# Though usually you'd just write: if flag:

# ❌ WRONG - Don't use 'is' for values
x = 5
y = 5
if x is y:  # Works but conceptually wrong
    print("Equal")
# Use: if x == y:
```

### Integer Interning

Python caches small integers (-5 to 256):

```python
a = 10
b = 10
print(a is b)  # True (same cached object)

a = 1000
b = 1000
print(a is b)  # False (different objects)
print(a == b)  # True (same value)
```

---

## Membership Operators

Membership operators test if a value exists in a sequence.

### In Operator

Tests if value exists in sequence:

```python
# Lists
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)     # True
print(10 in numbers)    # False

# Strings
text = "Hello World"
print("Hello" in text)  # True
print("hello" in text)  # False (case-sensitive)
print("x" in text)      # False

# Tuples
colors = ("red", "green", "blue")
print("red" in colors)  # True

# Dictionaries (checks keys, not values)
person = {"name": "Alice", "age": 25}
print("name" in person)   # True
print("Alice" in person)  # False (value, not key)
```

**Real-World Example:**
```python
# Check if user has permission
user_roles = ["admin", "editor", "viewer"]
required_role = "admin"

if required_role in user_roles:
    print("Access granted!")
else:
    print("Access denied!")
```

### Not In Operator

Tests if value does NOT exist in sequence:

```python
numbers = [1, 2, 3]
print(10 not in numbers)  # True
print(2 not in numbers)   # False

# Check for banned words
comment = "This is a nice post"
banned_words = ["spam", "scam", "fake"]

contains_banned = any(word in comment.lower() for word in banned_words)
if not contains_banned:
    print("Comment approved")
```

---

## Bitwise Operators

Bitwise operators work on binary representations of numbers.

### All Bitwise Operators

| Operator | Name | Example |
|----------|------|---------|
| & | AND | 5 & 3 → 1 |
| \| | OR | 5 \| 3 → 7 |
| ^ | XOR | 5 ^ 3 → 6 |
| ~ | NOT | ~5 → -6 |
| << | Left shift | 5 << 1 → 10 |
| >> | Right shift | 5 >> 1 → 2 |

### Understanding Binary

First, understand how numbers are represented in binary:

```python
# Decimal → Binary
5  → 0101
3  → 0011
10 → 1010
```

### Bitwise AND (&)

Returns 1 where both bits are 1:

```python
print(5 & 3)  # 1

# Binary representation:
#   0101 (5)
# & 0011 (3)
# ------
#   0001 (1)
```

### Bitwise OR (|)

Returns 1 where at least one bit is 1:

```python
print(5 | 3)  # 7

# Binary:
#   0101 (5)
# | 0011 (3)
# ------
#   0111 (7)
```

### Bitwise XOR (^)

Returns 1 where bits are different:

```python
print(5 ^ 3)  # 6

# Binary:
#   0101 (5)
# ^ 0011 (3)
# ------
#   0110 (6)
```

### Bitwise NOT (~)

Inverts all bits:

```python
print(~5)  # -6

# Binary (simplified):
# ~0101 → ...11111010 (two's complement)
```

### Left Shift (<<)

Shifts bits left (multiplies by 2^n):

```python
print(5 << 1)  # 10 (5 * 2)
print(5 << 2)  # 20 (5 * 4)

# Binary:
# 0101 << 1 → 1010 (10)
```

### Right Shift (>>)

Shifts bits right (divides by 2^n):

```python
print(10 >> 1)  # 5 (10 / 2)
print(10 >> 2)  # 2 (10 / 4)

# Binary:
# 1010 >> 1 → 0101 (5)
```

### Practical Uses

**Checking if number is even:**
```python
n = 42
is_even = (n & 1) == 0  # Last bit is 0 for even numbers
print(is_even)  # True
```

**Swap without temporary variable:**
```python
a, b = 5, 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 10 5
```

---

## Operator Precedence

When multiple operators appear in an expression, precedence determines the order of evaluation.

### Precedence Table (Highest to Lowest)

| Precedence | Operator | Description |
|------------|----------|-------------|
| 1 (Highest) | ** | Exponentiation |
| 2 | +x, -x, ~x | Unary plus, minus, NOT |
| 3 | *, /, //, % | Mult, Div, Floor Div, Mod |
| 4 | +, - | Addition, Subtraction |
| 5 | <<, >> | Bit Shifts |
| 6 | & | Bitwise AND |
| 7 | ^ | Bitwise XOR |
| 8 | \| | Bitwise OR |
| 9 | ==, !=, <, >, <=, >= | Comparisons |
| 10 | not | Logical NOT |
| 11 | and | Logical AND |
| 12 (Lowest) | or | Logical OR |

### Examples

```python
# Example 1: Multiplication before addition
result = 2 + 3 * 4
print(result)  # 14, not 20!
# Evaluated as: 2 + (3 * 4)

# Example 2: Exponentiation before multiplication
result = 2 * 3 ** 2
print(result)  # 18, not 36!
# Evaluated as: 2 * (3 ** 2)

# Example 3: Comparison before 'and'
result = 5 > 3 and 10 < 20
print(result)  # True
# Evaluated as: (5 > 3) and (10 < 20)
```

### Using Parentheses

When in doubt, use parentheses for clarity:

```python
# Without parentheses (relies on precedence)
result = 10 + 5 * 2  # 20

# With parentheses (explicit)
result = (10 + 5) * 2  # 30
result = 10 + (5 * 2)  # 20 (same as without)

# Complex expression
result = 2 ** 3 ** 2  # Right-associative: 2 ** (3 ** 2) = 512
result = (2 ** 3) ** 2  # Explicit: 8 ** 2 = 64
```

### Associativity

When operators have same precedence, associativity determines order:

```python
# Left-to-right (most operators)
result = 10 - 5 - 2  # (10 - 5) - 2 = 3

# Right-to-left (exponentiation)
result = 2 ** 3 ** 2  # 2 ** (3 ** 2) = 512
```

---

## Practice Exercises

### Arithmetic Operators

**Exercise 1: Basic Calculator**
```python
# Create a simple calculator
a = 15
b = 4
# Calculate and print: +, -, *, /, //, %, **
```

**Exercise 2: Circle Calculations**
```python
# Given radius = 7
# Calculate circumference (2πr) and area (πr²)
# Use 3.14159 for π
```

**Exercise 3: Temperature Converter**
```python
# Convert 32°F to Celsius
# Formula: C = (F - 32) * 5/9
```

**Exercise 4: Time Converter**
```python
# Convert 3665 seconds to hours, minutes, seconds
# Use //, %
```

**Exercise 5: Discount Calculator**
```python
# Original price: 250
# Discount: 15%
# Calculate final price
```

### Comparison Operators

**Exercise 6: Age Checker**
```python
# Check if age 17 qualifies for:
# - Child ticket (< 12)
# - Teen ticket (12-17)
# - Adult ticket (>= 18)
```

**Exercise 7: Grade Checker**
```python
# Score = 85
# A: >= 90, B: 80-89, C: 70-79, D: 60-69, F: < 60
```

**Exercise 8: Password Validator**
```python
# Check if password length is between 8 and 20
password = "mypassword123"
```

### Logical Operators

**Exercise 9: Login System**
```python
# User can log in if:
# - Username is "admin" AND password is "secret"
username = "admin"
password = "secret"
```

**Exercise 10: Eligibility Checker**
```python
# Can vote if:
# - Age >= 18 AND is_citizen is True
age = 20
is_citizen = True
```

**Exercise 11: Weekend Checker**
```python
# Is it weekend if day is "Saturday" OR "Sunday"?
day = "Saturday"
```

### Assignment Operators

**Exercise 12: Counter**
```python
# Start with count = 0
# Add 5, multiply by 2, subtract 3, divide by 7
```

**Exercise 13: Score Accumulator**
```python
# Total starts at 0
# Add the following scores: 10, 15, 20, 25, 30
```

### Identity and Membership

**Exercise 14: List Checker**
```python
# Check if 42 is in the list [10, 20, 30, 40, 50]
```

**Exercise 15: Permission Checker**
```python
# Check if "delete" is in permissions list
permissions = ["read", "write", "execute"]
```

### Combined Exercises

**Exercise 16: Leap Year**
```python
# Year is leap if:
# - Divisible by 4 AND (not divisible by 100 OR divisible by 400)
year = 2024
```

**Exercise 17: BMI Calculator with Categories**
```python
# Calculate BMI and categorize:
# Underweight: < 18.5
# Normal: 18.5-24.9
# Overweight: 25-29.9
# Obese: >= 30
weight = 70  # kg
height = 1.75  # meters
```

**Exercise 18: Quadratic Formula**
```python
# Solve ax² + bx + c = 0
# x = (-b ± √(b²-4ac)) / 2a
a, b, c = 1, -5, 6
# Find both roots
```

---

## 🎯 Key Takeaways

✅ **Arithmetic operators** perform math operations (+, -, *, /, //, %, **)  
✅ **Comparison operators** compare values and return True/False  
✅ **Logical operators** combine conditions (and, or, not)  
✅ **Assignment operators** assign values, with shortcuts (+=, -=, etc.)  
✅ **Identity operators** check if objects are the same (is, is not)  
✅ **Membership operators** check if value exists in sequence (in, not in)  
✅ **Bitwise operators** manipulate individual bits  
✅ **Precedence** determines evaluation order - use parentheses when unclear  

---

## 📚 Quick Reference

```python
# Arithmetic
+  -  *  /  //  %  **

# Comparison
==  !=  <  >  <=  >=

# Logical
and  or  not

# Assignment
=  +=  -=  *=  /=  //=  %=  **=

# Identity
is  is not

# Membership
in  not in

# Bitwise
&  |  ^  ~  <<  >>

# Precedence (remember PEMDAS-like):
# ** → Unary → * / // % → + - → Comparisons → Logical
```

---

**End of Operators Notes** 📝  

**Next Topic:** See `Strings_Notes.md` for comprehensive string operations!
