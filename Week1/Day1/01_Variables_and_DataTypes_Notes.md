# Variables and Data Types in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Variables](#introduction-to-variables)
2. [Variable Naming Rules and Conventions](#variable-naming-rules-and-conventions)
3. [Python's Dynamic Typing](#pythons-dynamic-typing)
4. [Integer Data Type](#integer-data-type)
5. [Float Data Type](#float-data-type)
6. [String Data Type (Preview)](#string-data-type-preview)
7. [Boolean Data Type](#boolean-data-type)
8. [None Type](#none-type)
9. [Type Conversion](#type-conversion)
10. [Memory and Variables](#memory-and-variables)
11. [Best Practices](#best-practices)
12. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Understand what variables are and how to create them
- ✅ Follow Python naming conventions and rules
- ✅ Work with all basic data types (int, float, bool, str, None)
- ✅ Convert between different data types
- ✅ Understand Python's dynamic typing system
- ✅ Apply best practices for variable usage

---

## Introduction to Variables

### What is a Variable?

A **variable** is like a labeled container that stores data in your program. Think of it as a name tag you put on a piece of information so you can find and use it later.

```python
# Creating variables
name = "Alice"
age = 25
height = 5.8
is_student = True
```

**Real-World Analogy** 🌍

Imagine you're organizing a kitchen:
- **Variable name** = Label on the jar ("Sugar", "Salt", "Coffee")
- **Variable value** = What's inside the jar
- **Assignment (=)** = Putting the contents into the labeled jar

When you write `temperature = 72`, you're saying: "Put the value 72 into a container labeled 'temperature'".

### How Variables Work

```python
x = 10  # Create a variable named x and assign it the value 10
```

What Python does behind the scenes:
1. **Allocates memory** - Reserves space in RAM
2. **Stores the value** - Puts 10 in that memory location
3. **Creates a reference** - Links the name 'x' to that memory address

### Variable Assignment

The `=` sign is the **assignment operator** (not "equals"!):

```python
score = 100      # Assign 100 to score
score = 200      # Reassign - score now equals 200
score = score + 50  # Use current value to calculate new value
print(score)     # 250
```

### Multiple Assignment

Python allows elegant multiple assignments:

```python
# Assign same value to multiple variables
x = y = z = 0
print(x, y, z)  # 0 0 0

# Assign different values in one line
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30

# Swap variables (Python magic!)
a, b = b, a
print(a, b)  # 20 10
```

### Variables vs Constants

Python doesn't have true constants, but by **convention**, we use ALL_CAPS for values that shouldn't change:

```python
# Constants (by convention only)
PI = 3.14159
MAX_USERS = 1000
DATABASE_URL = "localhost:5432"

# Regular variables
radius = 5
area = PI * radius ** 2
```

---

## Variable Naming Rules and Conventions

### Mandatory Rules ⚠️

Breaking these rules causes **SyntaxError**!

#### Rule 1: Must start with letter (a-z, A-Z) or underscore (_)

```python
# ✅ VALID
name = "John"
_private = "secret"
user1 = "Alice"
User = "Bob"

# ❌ INVALID
1user = "Bob"      # SyntaxError
@name = "Charlie"  # SyntaxError
```

#### Rule 2: Can only contain letters, numbers, and underscores

```python
# ✅ VALID
user_name = "Alice"
userName = "Bob"
user123 = "Charlie"
_internal = 42

# ❌ INVALID
user-name = "Dave"   # Hyphen not allowed
user.name = "Eve"    # Dot not allowed
user name = "Frank"  # Space not allowed
```

#### Rule 3: Case-sensitive

```python
age = 25
Age = 30
AGE = 35

print(age)  # 25
print(Age)  # 30
print(AGE)  # 35
# These are three different variables!
```

#### Rule 4: Cannot use Python keywords

Reserved words can't be variable names:

```python
# ❌ INVALID - These are Python keywords
class = "Math"     # SyntaxError
for = 10          # SyntaxError
if = True         # SyntaxError
def = "function"  # SyntaxError
```

**Python 3.11 Keywords:**
```
False    None     True     and      as       assert   async    await
break    class    continue def      del      elif     else     except
finally  for      from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise    return   try
while    with     yield
```

### Naming Conventions (PEP 8)

Follow these for readable, Pythonic code:

#### snake_case for variables and functions

```python
# ✅ GOOD - Python convention
first_name = "John"
user_account_balance = 1000
total_score = 95

# ⚠️ WORKS but not Pythonic
firstName = "John"        # camelCase (JavaScript style)
UserAccountBalance = 1000 # PascalCase (for classes)
```

#### Use descriptive names

```python
# ✅ GOOD - Self-explanatory
student_average_grade = 85
max_connection_attempts = 3
is_logged_in = True

# ❌ BAD - Too cryptic
x = 85
n = 3
flag = True
```

#### Avoid single-letter names (except in specific contexts)

```python
# ✅ ACCEPTABLE for loop counters
for i in range(10):
    print(i)

# ✅ ACCEPTABLE in math
a = 5
b = 10
c = a + b  # Clear mathematical context

# ❌ BAD for business logic
u = "Alice"  # Use 'username' instead
p = 12.99    # Use 'price' instead
```

#### ALL_CAPS for constants

```python
# ✅ GOOD
MAX_RETRIES = 5
DEFAULT_TIMEOUT = 30
PI = 3.14159
DATABASE_URL = "localhost:5432"
```

#### Prefix with _ for "internal" use

```python
# Convention for "private" or internal variables
_internal_counter = 0
_cache = {}
_temp_data = []
```

### Naming Patterns

**Boolean variables - use is_, has_, can_:**
```python
is_active = True
has_permission = False
can_edit = True
is_valid_email = False
should_retry = True
```

**Collections - use plural:**
```python
users = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
user_ids = [101, 102, 103]
product_names = ["Laptop", "Mouse", "Keyboard"]
```

**Temporary variables:**
```python
temp = calculate_something()
tmp_result = process_data()
```

### Self-Documenting Code

Variable names should make code read like English:

```python
# ❌ BAD - Unclear
t = 3600
d = t / 60
print(d)

# ✅ GOOD - Reads naturally
total_seconds = 3600
minutes = total_seconds / 60
print(minutes)  # Converting seconds to minutes
```

---

## Python's Dynamic Typing

### What is Dynamic Typing?

Python automatically figures out variable types - you **don't declare them**:

```python
# Python automatically knows the types
name = "Alice"        # str
age = 25              # int
height = 5.8          # float
is_student = True     # bool
```

Compare to statically-typed languages like Java:
```java
// Java requires type declarations
String name = "Alice";
int age = 25;
double height = 5.8;
boolean isStudent = true;
```

### Dynamic = Can Change Type

The same variable can hold different types over time:

```python
x = 42              # x is an integer
print(type(x))      # <class 'int'>

x = "Hello"         # Now x is a string
print(type(x))      # <class 'str'>

x = [1, 2, 3]       # Now x is a list
print(type(x))      # <class 'list'>

x = 3.14            # Now x is a float
print(type(x))      # <class 'float'>
```

### Checking Types

Use `type()` and `isinstance()`:

```python
age = 25
print(type(age))           # <class 'int'>
print(isinstance(age, int)) # True
print(isinstance(age, str)) # False

name = "Alice"
print(type(name))          # <class 'str'>
print(isinstance(name, str)) # True
```

### Benefits of Dynamic Typing

**1. Less code to write:**
```python
# Python
count = 0
total = 0.0

# Java
int count = 0;
double total = 0.0;
```

**2. More flexible:**
```python
def process(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return data * 2
    elif isinstance(data, list):
        return len(data)

print(process("hello"))  # HELLO
print(process(5))        # 10
print(process([1,2,3]))  # 3
```

### Potential Pitfalls

Type changes can cause errors:

```python
age = "25"          # String
age = age + 1       # TypeError: can only concatenate str to str

# Fix: Convert types
age = "25"
age = int(age) + 1  # Now it works!
print(age)          # 26
```

---

## Integer Data Type

### What are Integers?

Integers are **whole numbers** (no decimals):

```python
positive = 42
negative = -17
zero = 0
large_number = 1000000
```

### Creating Integers

```python
# Direct assignment
age = 25
score = 100

# From calculations
total = 50 + 75        # 125
difference = 100 - 30  # 70

# Type conversion
from_string = int("42")      # 42
from_float = int(3.99)       # 3 (truncates!)
from_bool = int(True)        # 1
```

### Integer Operations

```python
a = 10
b = 3

# Basic arithmetic
addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30

# Division (returns float!)
division = a / b        # 3.3333...

# Floor division (returns int)
floor_div = a // b      # 3

# Modulus (remainder)
remainder = a % b       # 1

# Exponentiation (power)
power = a ** b          # 1000
```

### Understanding Division Types

```python
# Regular division ALWAYS returns float
print(10 / 2)    # 5.0 (float, even for whole result)
print(10 / 3)    # 3.3333333333333335

# Floor division returns integer (rounds down)
print(10 // 2)   # 5 (int)
print(10 // 3)   # 3 (rounds down)
print(-10 // 3)  # -4 (rounds toward negative infinity!)
```

### Modulus Operator (%)

Returns the **remainder** after division:

```python
print(10 % 3)    # 1  (10 = 3*3 + 1)
print(17 % 5)    # 2  (17 = 5*3 + 2)
print(20 % 4)    # 0  (20 = 4*5 + 0)
```

**Use Case 1: Check Even/Odd**
```python
number = 42
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Use Case 2: Get Last Digit**
```python
number = 12345
last_digit = number % 10
print(last_digit)  # 5
```

**Use Case 3: Cycling/Wrapping**
```python
# 7-day week cycle
for day in range(20):
    day_of_week = day % 7
    print(f"Day {day} -> Weekday {day_of_week}")
# 0,1,2,3,4,5,6,0,1,2,3,4,5,6,0,1,2,3,4,5...
```

### Unlimited Integer Size

Python 3 handles **arbitrarily large** integers:

```python
# In C/Java, this would overflow
huge = 123456789012345678901234567890
bigger = huge ** 10
print(bigger)  # Works perfectly!

# Factorial of 100
import math
result = math.factorial(100)
print(result)  # Massive number, Python handles it!
```

### Integer Methods

```python
num = 42

# Convert to other types
float(num)       # 42.0
str(num)         # "42"
bool(num)        # True (non-zero is True)

# Number system conversions
bin(num)         # "0b101010" (binary)
oct(num)         # "0o52" (octal)
hex(num)         # "0x2a" (hexadecimal)

# Absolute value
abs(-42)         # 42

# Power
pow(2, 8)        # 256
pow(2, 8, 10)    # 6 ((2^8) % 10)
```

### Augmented Assignment

Shortcuts for common operations:

```python
count = 10

count += 5   # count = count + 5    → 15
count -= 3   # count = count - 3    → 12
count *= 2   # count = count * 2    → 24
count //= 4  # count = count // 4   → 6
count **= 2  # count = count ** 2   → 36
count %= 7   # count = count % 7    → 1
```

### Comparison Operators

```python
x = 10
y = 20

x == y  # False (equal to)
x != y  # True  (not equal)
x < y   # True  (less than)
x > y   # False (greater than)
x <= y  # True  (less than or equal)
x >= y  # False (greater than or equal)

# Chained comparisons (Pythonic!)
z = 15
print(10 < z < 20)      # True
print(10 <= z <= 20)    # True
```

### Underscores in Large Numbers

For readability (Python 3.6+):

```python
# Hard to read
population = 1000000000

# Easy to read
population = 1_000_000_000

# Works anywhere
price = 1_234_567.89
binary = 0b_1010_1010
hex_val = 0x_FF_FF
```

---

## Float Data Type

### What are Floats?

Floats are numbers **with decimal points**:

```python
price = 19.99
temperature = -3.5
pi = 3.14159
very_small = 1.5e-10  # Scientific notation: 0.00000000015
very_large = 3.2e8    # 320,000,000
```

### Creating Floats

```python
# Direct assignment
height = 5.9
price = 12.50

# From calculations
average = 100 / 4     # 25.0

# Type conversion
float(42)             # 42.0
float("3.14")         # 3.14
float(True)           # 1.0
```

### Float Precision Issues ⚠️

Computers use **binary** to store floats, causing precision issues:

```python
# Surprising!
print(0.1 + 0.2)  # 0.30000000000000004

# Why? Binary can't exactly represent some decimals
# Like how 1/3 = 0.333... in decimal
```

**Never use == for floats!**

```python
# ❌ WRONG
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False!

# ✅ CORRECT - Check if close enough
import math
print(math.isclose(a, b))  # True

# Or use tolerance
tolerance = 0.00001
print(abs(a - b) < tolerance)  # True
```

### Float Operations

```python
a = 10.5
b = 3.2

sum_val = a + b      # 13.7
diff = a - b         # 7.3
product = a * b      # 33.6
division = a / b     # 3.28125
power = a ** 2       # 110.25
floor = a // b       # 3.0 (still float!)
mod = a % b          # 0.9 (with precision issues)
```

### Rounding

```python
number = 3.14159

round(number, 2)  # 3.14
round(number, 3)  # 3.142
round(number)     # 3

# Banker's rounding (rounds to nearest even)
round(2.5)  # 2
round(3.5)  # 4
```

### Scientific Notation

```python
# Very large
light_speed = 3e8       # 300,000,000

# Very small
planck = 6.62607015e-34  # 0.000...000662607015

# In calculations
distance = light_speed * 1.5  # 450,000,000.0
```

### Special Float Values

```python
# Infinity
inf = float('inf')
neg_inf = float('-inf')

print(inf > 1000000)      # True
print(1 / inf)            # 0.0
print(inf + inf)          # inf

# Not a Number
nan = float('nan')
print(nan == nan)         # False (NaN never equals anything!)

# Checking special values
import math
math.isinf(inf)           # True
math.isnan(nan)           # True
math.isfinite(3.14)       # True
```

### Financial Calculations - Use Decimal

For money, use `decimal` module:

```python
from decimal import Decimal

# Exact arithmetic
price1 = Decimal('10.50')
price2 = Decimal('20.30')
total = price1 + price2
print(total)  # 30.80 (exact!)

# Regular floats are imprecise
total_float = 10.50 + 20.30
print(total_float)  # 30.799999999999997
```

---

## String Data Type (Preview)

*Note: Strings are covered in detail in the Strings_Notes.md file*

### Quick Overview

Strings are **text data** enclosed in quotes:

```python
name = "Alice"
message = 'Hello, World!'
multiline = """This is
a multiline
string"""
```

### Basic String Operations

```python
# Concatenation
first = "Hello"
last = "World"
full = first + " " + last  # "Hello World"

# Repetition
laugh = "ha" * 3  # "hahaha"

# Length
text = "Python"
length = len(text)  # 6

# Indexing
first_char = text[0]  # "P"
last_char = text[-1]  # "n"
```

### String to Number Conversion

```python
# String to int
age = int("25")       # 25

# String to float
price = float("19.99")  # 19.99

# Number to string
num_str = str(42)     # "42"
```

**More in Strings_Notes.md!**

---

## Boolean Data Type

### What are Booleans?

Booleans represent **True or False**:

```python
is_active = True
is_complete = False
has_permission = True
```

### Creating Booleans

```python
# Direct assignment
enabled = True
disabled = False

# From comparisons
age = 18
is_adult = age >= 18      # True
is_child = age < 13       # False

x = 10
y = 20
are_equal = x == y        # False
```

### Boolean Operations

```python
# AND - both must be True
True and True    # True
True and False   # False
False and False  # False

# OR - at least one must be True
True or False    # True
False or False   # False
True or True     # True

# NOT - inverts the value
not True         # False
not False        # True
```

**Real Example:**
```python
age = 25
has_license = True
has_insurance = True

can_drive = age >= 18 and has_license and has_insurance
print(can_drive)  # True
```

### Truthy and Falsy Values

**Everything in Python has a truth value!**

**Falsy** (evaluate to False):
```python
bool(False)      # False
bool(None)       # False
bool(0)          # False
bool(0.0)        # False
bool("")         # False (empty string)
bool([])         # False (empty list)
bool({})         # False (empty dict)
bool(())         # False (empty tuple)
bool(set())      # False (empty set)
```

**Truthy** (evaluate to True):
```python
bool(True)       # True
bool(1)          # True
bool(-1)         # True
bool(3.14)       # True
bool("hello")    # True
bool(" ")        # True (single space!)
bool([1, 2])     # True
bool({"a": 1})   # True
```

**Practical Usage:**
```python
name = input("Enter name: ")

# Pythonic way
if name:
    print(f"Hello, {name}!")
else:
    print("No name provided")

# Less Pythonic
if len(name) > 0:
    print(f"Hello, {name}!")
```

### Short-Circuit Evaluation

Python stops evaluating as soon as the result is determined:

```python
# AND stops at first False
result = False and expensive_function()
# expensive_function() never runs!

# OR stops at first True
result = True or expensive_function()
# expensive_function() never runs!

# Practical use - avoid errors
x = 10
y = 0
if y != 0 and x / y > 5:  # Safe! Division never happens if y is 0
    print("Greater than 5")
```

### Chained Comparisons

```python
x = 15

# Elegant Pythonic way
if 10 < x < 20:
    print("In range")

# Instead of
if x > 10 and x < 20:
    print("In range")

# Multiple chains
score = 85
if 0 <= score <= 100:
    print("Valid score")
```

---

## None Type

### What is None?

`None` represents **"no value"** or **"nothing"**:

```python
result = None
user = None
data = None
```

### When to Use None

**1. Default parameters:**
```python
def greet(name=None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")

greet()         # Hello, stranger!
greet("Alice")  # Hello, Alice!
```

**2. Function returns nothing:**
```python
def find_user(user_id):
    if user_id == 1:
        return "Alice"
    else:
        return None  # Not found

user = find_user(99)
if user is None:
    print("User not found")
```

**3. Initialize before assignment:**
```python
max_value = None
for num in [5, 12, 3, 18, 7]:
    if max_value is None or num > max_value:
        max_value = num
print(max_value)  # 18
```

### Checking for None

**Always use `is` or `is not`:**

```python
value = None

# ✅ CORRECT
if value is None:
    print("It's None!")

if value is not None:
    print("It has a value")

# ❌ WRONG (works but not recommended)
if value == None:
    print("It's None")
```

### None vs Empty Values

```python
none_val = None      # No value
empty_str = ""       # Empty but exists
zero = 0             # Actual value (zero)
empty_list = []      # Empty but exists

# Only None is None
print(none_val is None)     # True
print(empty_str is None)    # False
print(zero is None)         # False

# But all are falsy
print(bool(none_val))    # False
print(bool(empty_str))   # False
print(bool(zero))        # False
```

---

## Type Conversion

### Implicit Conversion (Automatic)

Python auto-converts in some cases:

```python
# Int + Float = Float
result = 5 + 2.5
print(result)       # 7.5
print(type(result)) # <class 'float'>

# Boolean + Int = Int
result = True + 5
print(result)       # 6 (True = 1)
```

### Explicit Conversion (Manual)

#### To Integer

```python
int(3.99)        # 3 (truncates, doesn't round!)
int("42")        # 42
int(True)        # 1
int(False)       # 0
# int("3.14")    # ValueError!
```

#### To Float

```python
float(42)        # 42.0
float("3.14")    # 3.14
float(True)      # 1.0
```

#### To String

```python
str(42)          # "42"
str(3.14)        # "3.14"
str(True)        # "True"
str([1, 2, 3])   # "[1, 2, 3]"
```

#### To Boolean

```python
bool(1)          # True
bool(0)          # False
bool(-5)         # True
bool("")         # False
bool("hello")    # True
bool([])         # False
bool([1])        # True
```

### Common Patterns

**User Input (always strings):**
```python
age = int(input("Enter age: "))
price = float(input("Enter price: "))
```

**Safe Conversion:**
```python
text = "123"
if text.isdigit():
    number = int(text)
else:
    print("Not a valid number")

# With error handling
try:
    number = int(text)
except ValueError:
    print("Invalid number!")
```

---

## Memory and Variables

### How Variables are Stored

```python
x = 42
```

Python does:
1. Creates an integer object with value 42
2. Stores it in memory
3. Creates a reference 'x' pointing to it

### Multiple References

```python
a = [1, 2, 3]
b = a  # b references the same list!

b.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
# They're the same object!
```

### Immutable vs Mutable

**Immutable** (can't be changed):
- int, float, str, tuple, bool, None

```python
x = 10
x = 20  # Creates new object, doesn't modify 10
```

**Mutable** (can be changed):
- list, dict, set

```python
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the same object
```

### Identity Checking

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)   # True (same values)
print(x is y)   # False (different objects)
print(x is z)   # True (same object)

# Use 'is' only for None, True, False
if value is None:    # ✅ Good
    pass
if value is True:    # ✅ Good (but usually just 'if value:')
    pass
```

---

## Best Practices

### 1. Use Descriptive Names

```python
# ❌ BAD
x = 85
d = 30

# ✅ GOOD
student_grade = 85
days_until_deadline = 30
```

### 2. Follow Naming Conventions

```python
# Variables and functions: snake_case
user_name = "Alice"
total_count = 100

# Constants: ALL_CAPS
MAX_RETRIES = 5
PI = 3.14159

# Classes: PascalCase (covered later)
class UserAccount:
    pass
```

### 3. Initialize Variables

```python
# ❌ Might cause errors
if some_condition:
    result = calculate()
print(result)  # NameError if condition is False!

# ✅ Better
result = None
if some_condition:
    result = calculate()
if result is not None:
    print(result)
```

### 4. Use Type Hints (Python 3.5+)

```python
# Helps with code clarity and tools
age: int = 25
name: str = "Alice"
price: float = 19.99
is_active: bool = True

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### 5. Avoid Global Variables

```python
# ❌ BAD - Global variable
count = 0

def increment():
    global count
    count += 1

# ✅ BETTER - Pass as parameter
def increment(count):
    return count + 1

count = 0
count = increment(count)
```

---

## Practice Exercises

### Beginner Exercises

**Exercise 1: Create Variables**
```python
# Create variables for:
# - Your name (string)
# - Your age (integer)
# - Your height in meters (float)
# - Whether you're a student (boolean)
```

**Exercise 2: Type Checking**
```python
# Create three variables and check their types
var1 = 42
var2 = "Hello"
var3 = 3.14

# Print the type of each
```

**Exercise 3: Basic Arithmetic**
```python
# Given a = 15 and b = 4
# Calculate and print: sum, difference, product, division,
# floor division, remainder, power
```

**Exercise 4: Temperature Converter**
```python
# Convert 25°C to Fahrenheit
# Formula: F = (C × 9/5) + 32
celsius = 25
```

**Exercise 5: Even or Odd**
```python
# Check if a number is even or odd using modulus
number = 17
```

### Intermediate Exercises

**Exercise 6: Swap Variables**
```python
# Swap two variables without using a temporary variable
a = 100
b = 200
```

**Exercise 7: Type Conversion Chain**
```python
# Start with "42"
# Convert to int, multiply by 2, convert to float,
# divide by 3, convert back to string
value = "42"
```

**Exercise 8: Truthy/Falsy**
```python
# Check if these are truthy or falsy:
# 0, "", [], None, False, "0", [0]
```

**Exercise 9: Safe Division**
```python
# Write code to divide two numbers safely
# Return None if dividing by zero
a = 10
b = 0
```

**Exercise 10: BMI Calculator**
```python
# Calculate BMI = weight(kg) / height(m)²
weight = 70
height = 1.75
```

### Advanced Exercises

**Exercise 11: Digit Extraction**
```python
# Extract each digit from 1234
# Expected output: 1, 2, 3, 4
number = 1234
```

**Exercise 12: Time Converter**
```python
# Convert 3665 seconds to hours, minutes, seconds
# Expected: 1h 1m 5s
total_seconds = 3665
```

**Exercise 13: Compound Interest**
```python
# Calculate compound interest
# A = P(1 + r/n)^(nt)
# P=1000, r=0.05, n=4, t=3
```

**Exercise 14: Distance Between Points**
```python
# Calculate distance between two 2D points
# Distance = √((x2-x1)² + (y2-y1)²)
x1, y1 = 0, 0
x2, y2 = 3, 4
```

**Exercise 15: Float Precision**
```python
# Add 0.1 ten times and check if equals 1.0
# Use math.isclose() for proper comparison
```

---

## 🎯 Key Takeaways

✅ Variables are labeled containers for data  
✅ Follow Python naming rules and PEP 8 conventions  
✅ Python uses dynamic typing - types are determined automatically  
✅ Basic types: int, float, str, bool, None  
✅ Use explicit type conversion when needed  
✅ Be careful with float precision  
✅ Use `is` for None/True/False, `==` for values  
✅ Everything in Python has a truth value (truthy/falsy)  
✅ Write descriptive, self-documenting variable names  

---

## 📚 Quick Reference Card

```python
# Variable creation
variable_name = value

# Multiple assignment
x = y = z = 0
a, b, c = 1, 2, 3

# Type checking
type(variable)
isinstance(variable, type)

# Type conversion
int(), float(), str(), bool()

# Integer operations
+  -  *  /  //  %  **

# Augmented assignment
+=  -=  *=  /=  //=  **=  %=

# Comparison
==  !=  <  >  <=  >=

# Boolean operators
and  or  not

# None checking
is None  /  is not None
```

---

**End of Variables and Data Types Notes** 📝

For more on specific topics:
- **Strings**: See `Strings_Notes.md`
- **Operators**: See `Operators_Notes.md`
- **Numbers**: See `Numbers_and_Booleans_Notes.md`
