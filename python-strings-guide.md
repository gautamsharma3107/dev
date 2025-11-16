# Python Strings: Complete Guide

---

## Table of Contents
1. [Introduction to Strings](#introduction-to-strings)
2. [Strings as Sequences](#strings-as-sequences)
3. [String Indexing and Slicing](#string-indexing-and-slicing)
4. [String Methods](#string-methods)
5. [String Formatting](#string-formatting)
6. [String Operations](#string-operations)
7. [Raw Strings and Special Characters](#raw-strings-and-special-characters)
8. [String Immutability](#string-immutability)
9. [Common String Use Cases](#common-string-use-cases)
10. [Practice Exercises](#practice-exercises)

---

## Introduction to Strings

### What is a String?
- **Sequence of characters** enclosed in quotes
- **Immutable** - cannot be changed after creation
- **Ordered** - characters have specific positions
- **Zero-indexed** - first character at index 0
- **Iterable** - can loop through characters
- **Comparable** - can compare strings lexicographically
- **Created with quotes** - single, double, or triple quotes

### Creating Strings

```python
# Single quotes
str1 = 'Hello'

# Double quotes
str2 = "World"

# No difference between single and double
print(str1 == "Hello")      # Output: True
print(str2 == 'World')      # Output: True

# String with quotes inside
mixed1 = "He said 'Hello'"
mixed2 = 'She said "Goodbye"'

# Escape quotes
escaped = "He said \"Hello\""
escaped2 = 'She said \'Goodbye\''

print(mixed1)               # Output: He said 'Hello'
print(escaped)              # Output: He said "Hello"
```

### Multi-line Strings

```python
# Triple quotes - preserve newlines
multiline = """
This is a
multiline string
spanning several lines
"""
print(multiline)

# Also with single quotes
multiline2 = '''
Line 1
Line 2
Line 3
'''

# For docstrings (in functions/classes)
def my_function():
    """
    This is a docstring
    It describes the function
    """
    pass
```

### Empty String

```python
empty = ""
print(len(empty))           # Output: 0
print(bool(empty))          # Output: False
```

### String Length

```python
text = "Python"
print(len(text))            # Output: 6

empty = ""
print(len(empty))           # Output: 0

# Length of string with spaces
with_spaces = "Hello World"
print(len(with_spaces))     # Output: 11 (includes space)
```

---

## Strings as Sequences

### Understanding String Sequences

Strings are sequences of characters, similar to lists:

```python
# String is a sequence
text = "Python"

# Iterate over characters
for char in text:
    print(char)

# Output:
# P
# y
# t
# h
# o
# n

# Get each character
print(text[0])              # Output: P
print(text[1])              # Output: y
print(text[5])              # Output: n
```

### Membership Testing

```python
text = "Hello World"

# Check if character exists
print("H" in text)          # Output: True
print("h" in text)          # Output: False (case-sensitive)
print("World" in text)      # Output: True (substring)
print("xyz" in text)        # Output: False

# Negative check
print("Z" not in text)      # Output: True
```

### Iterating Over Strings

```python
# Simple iteration
word = "cat"
for char in word:
    print(char)

# Output:
# c
# a
# t

# With enumerate (index and character)
for index, char in enumerate(word):
    print(f"Index {index}: {char}")

# Output:
# Index 0: c
# Index 1: a
# Index 2: t
```

### String Comparisons

```python
# Lexicographic comparison (alphabetical order)
print("apple" < "banana")   # Output: True
print("zebra" > "apple")    # Output: True
print("cat" == "cat")       # Output: True
print("dog" != "dog")       # Output: False

# Case-sensitive
print("Apple" < "apple")    # Output: True (uppercase < lowercase)

# Compare strings
names = ["Charlie", "Alice", "Bob"]
names_sorted = sorted(names)
print(names_sorted)         # Output: ['Alice', 'Bob', 'Charlie']
```

---

## String Indexing and Slicing

### Positive Indexing

```python
text = "Python Programming"
#       0123456789...

# Access by positive index
print(text[0])              # Output: P
print(text[1])              # Output: y
print(text[7])              # Output: (space)
print(text[8])              # Output: P

# Out of range - IndexError
# print(text[100])          # IndexError: string index out of range
```

### Negative Indexing

```python
text = "Python"
#       -6 -5 -4 -3 -2 -1

# Access from end
print(text[-1])             # Output: n (last character)
print(text[-2])             # Output: o
print(text[-6])             # Output: P (first character)
```

### Basic Slicing

**Syntax:** `string[start:end:step]`

```python
text = "Python Programming"

# Get substring
print(text[0:6])            # Output: Python
print(text[7:18])           # Output: Programming

# Default start (beginning)
print(text[:6])             # Output: Python

# Default end (to end)
print(text[7:])             # Output: Programming

# Entire string
print(text[:])              # Output: Python Programming
```

### Slicing with Step

```python
text = "Python"

# Every 2nd character
print(text[::2])            # Output: Pto

# Every 3rd character
print(text[::3])            # Output: Po

# Specific range with step
print(text[1:5:2])          # Output: yh

# Negative step (reverse)
print(text[::-1])           # Output: nohtyP
```

### Reverse Slicing

```python
text = "Hello"

# Reverse entire string
reversed_text = text[::-1]
print(reversed_text)        # Output: olleH

# Reverse specific portion
print(text[4:1:-1])         # Output: oll (from index 4 to 2)
```

---

## String Methods

### Case Conversion Methods

```python
text = "Hello World"

# uppercase() - all uppercase
print(text.upper())         # Output: HELLO WORLD

# lower() - all lowercase
print(text.lower())         # Output: hello world

# title() - capitalize each word
print(text.title())         # Output: Hello World

# capitalize() - capitalize first character only
print(text.capitalize())    # Output: Hello world

# swapcase() - swap upper and lower
print(text.swapcase())      # Output: hELLO wORLD
```

### Whitespace Methods

```python
text = "  Hello World  \n"

# strip() - remove whitespace from both ends
print(f"|{text.strip()}|")   # Output: |Hello World|

# lstrip() - remove from left
print(f"|{text.lstrip()}|")  # Output: |Hello World  \n|

# rstrip() - remove from right
print(f"|{text.rstrip()}|")  # Output: |  Hello World|

# removeprefix() - Python 3.9+
url = "https://example.com"
print(url.removeprefix("https://"))  # Output: example.com

# removesuffix() - Python 3.9+
print(url.removesuffix(".com"))      # Output: https://example
```

### Finding and Replacing

```python
text = "Hello World, Hello Python"

# find() - index of first occurrence
pos = text.find("Hello")
print(pos)                  # Output: 0

pos2 = text.find("World")
print(pos2)                 # Output: 6

pos3 = text.find("xyz")
print(pos3)                 # Output: -1 (not found)

# index() - like find() but raises error if not found
try:
    pos = text.index("xyz")
except ValueError:
    print("Not found")

# count() - count occurrences
count = text.count("Hello")
print(count)                # Output: 2

# replace() - replace all occurrences
replaced = text.replace("Hello", "Hi")
print(replaced)             # Output: Hi World, Hi Python

# Replace limited occurrences
replaced2 = text.replace("Hello", "Hi", 1)  # Only first
print(replaced2)            # Output: Hi World, Hello Python
```

### Splitting and Joining

```python
# split() - split by delimiter
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)               # Output: ['apple', 'banana', 'orange']

# Split by space (default)
sentence = "Hello World Python"
words = sentence.split()
print(words)                # Output: ['Hello', 'World', 'Python']

# Split with limit
text2 = "a-b-c-d-e"
parts = text2.split("-", 2)  # Only first 2 splits
print(parts)                # Output: ['a', 'b', 'c-d-e']

# splitlines() - split by newlines
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.splitlines()
print(lines)                # Output: ['Line 1', 'Line 2', 'Line 3']

# join() - combine list into string
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)             # Output: Hello World Python

# Join with different delimiter
result = "-".join(words)
print(result)               # Output: Hello-World-Python
```

### String Testing Methods

```python
# isdigit() - all digits?
print("12345".isdigit())    # Output: True
print("123a5".isdigit())    # Output: False

# isalpha() - all alphabetic?
print("hello".isalpha())    # Output: True
print("hello123".isalpha()) # Output: False

# isalnum() - all alphanumeric?
print("hello123".isalnum()) # Output: True
print("hello 123".isalnum())# Output: False

# isspace() - all whitespace?
print("   ".isspace())      # Output: True
print(" a ".isspace())      # Output: False

# islower() - all lowercase?
print("hello".islower())    # Output: True
print("Hello".islower())    # Output: False

# isupper() - all uppercase?
print("HELLO".isupper())    # Output: True
print("Hello".isupper())    # Output: False

# isidentifier() - valid variable name?
print("my_var".isidentifier())      # Output: True
print("123var".isidentifier())      # Output: False

# startswith() - starts with?
text = "Hello World"
print(text.startswith("Hello"))     # Output: True
print(text.startswith("World"))     # Output: False

# endswith() - ends with?
print(text.endswith("World"))       # Output: True
print(text.endswith("Hello"))       # Output: False
```

### Other Useful Methods

```python
# center() - center string
text = "Hello"
print(f"|{text.center(15)}|")       # Output: |     Hello     |

# ljust() - left justify
print(f"|{text.ljust(15)}|")        # Output: |Hello          |

# rjust() - right justify
print(f"|{text.rjust(15)}|")        # Output: |          Hello|

# zfill() - pad with zeros
number = "42"
print(number.zfill(5))              # Output: 00042

# count() - count occurrences
text = "abracadabra"
print(text.count("a"))              # Output: 5
print(text.count("ab"))             # Output: 2
```

---

## String Formatting

### f-Strings (Python 3.6+) - RECOMMENDED

```python
# Basic f-string
name = "Alice"
age = 25
print(f"My name is {name} and I am {age}")
# Output: My name is Alice and I am 25

# Expressions in f-strings
x = 10
y = 20
print(f"Sum: {x + y}, Product: {x * y}")
# Output: Sum: 30, Product: 200

# Formatting numbers
pi = 3.14159
print(f"Pi = {pi:.2f}")             # 2 decimal places
print(f"Pi = {pi:.4f}")             # 4 decimal places

# Percentage formatting
percentage = 0.85
print(f"Score: {percentage:.1%}")   # Output: Score: 85.0%

# Padding and alignment
name = "Bob"
print(f"|{name:10}|")               # Left-aligned, width 10
print(f"|{name:>10}|")              # Right-aligned
print(f"|{name:^10}|")              # Center-aligned
print(f"|{name:*^10}|")             # Center with * padding
```

### .format() Method

```python
# Basic format
text = "My name is {} and I am {}".format("Alice", 25)
print(text)
# Output: My name is Alice and I am 25

# Named placeholders
text = "My name is {name} and I am {age}".format(name="Bob", age=30)
print(text)
# Output: My name is Bob and I am 30

# Formatting numbers
pi = 3.14159
print("Pi = {:.2f}".format(pi))     # Output: Pi = 3.14

# Positional arguments
text = "{1} {0}".format("World", "Hello")
print(text)                         # Output: Hello World

# Padding
print("|{:10}|".format("test"))     # Output: |test      |
print("|{:>10}|".format("test"))    # Output: |      test|
print("|{:^10}|".format("test"))    # Output: |   test   |
```

### % Operator (Old Style)

```python
# String formatting
name = "Charlie"
text = "Hello, %s" % name
print(text)                         # Output: Hello, Charlie

# Multiple values
name = "Alice"
age = 25
text = "%s is %d years old" % (name, age)
print(text)
# Output: Alice is 25 years old

# Float formatting
pi = 3.14159
text = "Pi = %.2f" % pi
print(text)                         # Output: Pi = 3.14
```

### String Formatting Specifiers

```python
# Width and alignment
value = "test"
print(f"{value:10}")                # Left-aligned width 10
print(f"{value:>10}")               # Right-aligned
print(f"{value:^10}")               # Center-aligned
print(f"{value:*^10}")              # Center with padding

# Numbers
num = 42
print(f"{num:05d}")                 # Zero-padded integer
print(f"{num:x}")                   # Hexadecimal
print(f"{num:o}")                   # Octal
print(f"{num:b}")                   # Binary

# Floats
pi = 3.14159
print(f"{pi:.2f}")                  # 2 decimal places
print(f"{pi:.4f}")                  # 4 decimal places
print(f"{pi:10.2f}")                # Width 10, 2 decimals

# Scientific notation
large = 1234567
print(f"{large:e}")                 # Scientific notation
print(f"{large:.2e}")               # 2 decimals in scientific
```

### Complex Formatting Examples

```python
# Table formatting
data = [("Alice", 25, 85.5), ("Bob", 22, 92.3), ("Charlie", 23, 78.9)]

print(f"{'Name':<15} {'Age':>5} {'Score':>8}")
print("-" * 30)
for name, age, score in data:
    print(f"{name:<15} {age:>5} {score:>8.1f}")

# Output:
# Name               Age    Score
# ------------------------------
# Alice              25     85.5
# Bob                22     92.3
# Charlie            23     78.9

# Currency formatting
price = 1234.5678
print(f"Price: ${price:,.2f}")      # Output: Price: $1,234.57
```

---

## String Operations

### Concatenation

```python
# Using + operator
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)                       # Output: Hello World

# String repetition
word = "Ha"
print(word * 3)                     # Output: HaHaHa

# Concatenation in loop
words = ["Python", "is", "awesome"]
sentence = ""
for word in words:
    sentence += word + " "
print(sentence)                     # Output: Python is awesome

# Better: use join()
sentence = " ".join(words)
print(sentence)                     # Output: Python is awesome
```

### String Comparison

```python
# Lexicographic comparison
print("apple" < "banana")           # Output: True
print("apple" == "apple")           # Output: True
print("apple" != "Apple")           # Output: True (case-sensitive)

# String in list
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)            # Output: True
print("grape" in fruits)            # Output: False
```

### Converting to/from Other Types

```python
# String to list (characters)
text = "hello"
char_list = list(text)
print(char_list)                    # Output: ['h', 'e', 'l', 'l', 'o']

# List to string
words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)                     # Output: Hello World

# String to number
num_str = "42"
num_int = int(num_str)
print(num_int + 10)                 # Output: 52

num_float_str = "3.14"
num_float = float(num_float_str)
print(num_float + 0.86)             # Output: 4.0

# Number to string
num = 100
text = str(num)
print("Value: " + text)             # Output: Value: 100
```

---

## Raw Strings and Special Characters

### Raw Strings (r prefix)

```python
# Normal string - backslash interpreted
normal = "C:\new\folder"
print(normal)                       # Output: C:
#                                   #         ew\folder

# Raw string - backslash treated literally
raw = r"C:\new\folder"
print(raw)                          # Output: C:\new\folder

# Regex patterns
import re
pattern = r"\d+"                    # Match digits
text = "I have 42 apples"
matches = re.findall(pattern, text)
print(matches)                      # Output: ['42']
```

### Special Characters

```python
# Newline
text = "Line 1\nLine 2\nLine 3"
print(text)
# Output:
# Line 1
# Line 2
# Line 3

# Tab
text = "Name\tAge\tCity"
print(text)                         # Output: Name    Age    City

# Backslash
text = "Path: C:\\Users\\Alice"
print(text)                         # Output: Path: C:\Users\Alice

# Quote inside string
text1 = "He said \"Hello\""
text2 = 'She said \'Hi\''
print(text1)                        # Output: He said "Hello"
print(text2)                        # Output: She said 'Hi'
```

---

## String Immutability

### Understanding Immutability

```python
text = "Hello"

# ERROR - cannot modify
# text[0] = "J"             # TypeError: 'str' object does not support item assignment

# Create new string instead
text = "J" + text[1:]
print(text)                         # Output: Jello

# Replace creates new string
text = "Hello".replace("H", "J")
print(text)                         # Output: Jello

# Original unchanged
original = "Hello"
modified = original.upper()
print(original)                     # Output: Hello
print(modified)                     # Output: HELLO
```

### Why Immutability Matters

```python
# Strings can be used as dictionary keys (because immutable)
person = {
    "name": "Alice",
    "email": "alice@example.com"
}

print(person["name"])               # Works fine

# Mutable types cannot be dictionary keys
# ERROR: bad_dict = {["a", "b"]: "value"}  # TypeError

# Immutable types work
good_dict = {("a", "b"): "value"}   # Works with tuple
print(good_dict[("a", "b")])        # Output: value
```

---

## Common String Use Cases

### Text Processing

```python
# Count word frequency
text = "hello world hello python python python"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# Output: {'hello': 2, 'world': 1, 'python': 3}

# Remove punctuation
import string
text = "Hello, World! How are you?"
cleaned = text.translate(str.maketrans('', '', string.punctuation))
print(cleaned)                      # Output: Hello World How are you
```

### Email Validation

```python
# Simple email check
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

print(is_valid_email("alice@example.com"))      # True
print(is_valid_email("invalid.email"))          # False
```

### Path Manipulation

```python
# Extract file info
filepath = "/home/user/documents/file.txt"

# Get filename
filename = filepath.split("/")[-1]
print(filename)                     # Output: file.txt

# Get extension
extension = filename.split(".")[-1]
print(extension)                    # Output: txt

# Get directory
directory = filepath.rsplit("/", 1)[0]
print(directory)                    # Output: /home/user/documents
```

### String Parsing

```python
# Parse CSV-like data
csv_line = "Alice,25,Engineer,80000"
name, age, role, salary = csv_line.split(",")

print(f"{name} works as {role}")     # Output: Alice works as Engineer

# Parse key-value pairs
config = "host=localhost,port=5432,user=admin"
settings = {}
for pair in config.split(","):
    key, value = pair.split("=")
    settings[key] = value

print(settings)
# Output: {'host': 'localhost', 'port': '5432', 'user': 'admin'}
```

### String Validation

```python
# Check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Too short"
    if not any(c.isdigit() for c in password):
        return "No digits"
    if not any(c.isupper() for c in password):
        return "No uppercase"
    return "Strong"

print(check_password_strength("weak"))           # Too short
print(check_password_strength("Weak1234"))       # Strong
```

---

## Practice Exercises

### 1. String Basics
- Create strings using different quote styles
- Get string length and iterate through characters
- Use indexing and slicing

### 2. String Methods
- Convert case (upper, lower, title)
- Find and replace text
- Split and join strings
- Test string properties (isdigit, isalpha, etc.)

### 3. String Slicing
- Extract substrings using positive/negative indices
- Reverse strings using slicing
- Use step parameter for extracting patterns

### 4. String Formatting
- Use f-strings with expressions
- Format numbers with specific decimal places
- Create aligned tables
- Format currency values

### 5. Text Processing
- Count word frequency
- Remove punctuation
- Parse CSV-like data
- Validate email addresses

### 6. Real-World Scenarios
- Parse file paths
- Extract information from structured text
- Validate user input
- Create formatted reports

---

# End of Notes
