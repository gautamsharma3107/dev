# Strings in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Strings](#introduction-to-strings)
2. [Creating Strings](#creating-strings)
3. [String Indexing and Slicing](#string-indexing-and-slicing)
4. [String Methods](#string-methods)
5. [String Formatting](#string-formatting)
6. [String Operations](#string-operations)
7. [Escape Sequences](#escape-sequences)
8. [String Immutability](#string-immutability)
9. [Advanced String Topics](#advanced-string-topics)
10. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Create and manipulate strings effectively
- ✅ Use string indexing and slicing
- ✅ Master essential string methods
- ✅ Format strings using f-strings, format(), and %
- ✅ Understand string immutability
- ✅ Work with escape sequences and special characters
- ✅ Perform common string operations

---

## Introduction to Strings

### What are Strings?

**Strings** are sequences of characters used to represent text. In Python, strings are one of the most commonly used data types.

```python
name = "Alice"
message = "Hello, World!"
address = "123 Main Street"
```

**Real-World Analogy** 🌍

Think of a string like a sentence in a book - it's a sequence of characters (letters, numbers, symbols) that convey meaning. Just like you can read the first letter of a sentence, the last word, or extract part of it, Python lets you do the same with strings.

### Strings are Sequences

Strings are ordered collections of characters:

```python
text = "Python"
# P  y  t  h  o  n
# 0  1  2  3  4  5  (index positions)
```

---

## Creating Strings

### Single Quotes

```python
message = 'Hello, World!'
name = 'Alice'
single = '123'
```

### Double Quotes

```python
message = "Hello, World!"
name = "Alice"
double = "456"
```

**Single vs Double**: No difference in Python! Use whichever you prefer (or mix to avoid escaping):

```python
# Easy to include apostrophes with double quotes
text = "It's a beautiful day"

# Easy to include quotes with single quotes
speech = 'She said, "Hello"'
```

### Triple Quotes (Multiline Strings)

Use triple quotes (`"""` or `'''`) for multiline strings:

```python
# Triple double quotes
paragraph = """This is a long paragraph
that spans multiple lines.
You can write as much as you want!"""

# Triple single quotes
poem = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''

print(paragraph)
print(poem)
```

**Use Case: Docstrings**
```python
def greet(name):
    """
    This function greets the person with the given name.
    
    Parameters:
        name (str): The name of the person
    
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"
```

### Empty String

```python
empty = ""
also_empty = ''
print(len(empty))  # 0
```

### String with Numbers

```python
# These are strings, not numbers!
age_str = "25"
price_str = "19.99"

# Can't do math directly
# result = age_str + 5  # TypeError!

# Need to convert first
age_num = int(age_str)
result = age_num + 5  # 30
```

---

## String Indexing and Slicing

### String Indexing

Access individual characters using index (position):

```python
text = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5  (positive indexing)
#      -6 -5 -4 -3 -2 -1  (negative indexing)

# Positive indexing (from left)
print(text[0])   # 'P' (first character)
print(text[1])   # 'y'
print(text[5])   # 'n' (last character)

# Negative indexing (from right)
print(text[-1])  # 'n' (last character)
print(text[-2])  # 'o' (second to last)
print(text[-6])  # 'P' (first character)
```

**Index Out of Range:**
```python
text = "Python"
# print(text[10])  # IndexError: string index out of range
```

### String Slicing

Extract substring using `[start:stop:step]`:

```python
text = "Python Programming"
#       0123456789...

# Basic slicing [start:stop]
print(text[0:6])     # "Python" (index 0 to 5)
print(text[7:18])    # "Programming"
print(text[7:])      # "Programming" (from 7 to end)
print(text[:6])      # "Python" (from start to 5)
print(text[:])       # "Python Programming" (entire string)

# Negative indices
print(text[-11:])    # "Programming"
print(text[:-12])    # "Python"

# Step parameter [start:stop:step]
print(text[::2])     # "Pto rgamn" (every 2nd char)
print(text[::3])     # "Ph orm" (every 3rd char)

# Reverse string
print(text[::-1])    # "gnimmargorP nohtyP" (reversed!)
```

**Slicing Rules:**
- `start` is inclusive
- `stop` is exclusive
- Default `start` is 0
- Default `stop` is length
- Default `step` is 1

**Practical Examples:**
```python
# Get first 3 characters
text = "Python"
first_three = text[:3]  # "Pyt"

# Get last 3 characters
last_three = text[-3:]  # "hon"

# Remove first and last character
middle = text[1:-1]  # "ytho"

# Get every other character
every_other = text[::2]  # "Pto"

# Reverse a string
reversed_text = text[::-1]  # "nohtyP"
```

---

## String Methods

Python provides 40+ built-in string methods. Here are the most important ones:

### Case Methods

```python
text = "Hello World"

# Convert to uppercase  
print(text.upper())      # "HELLO WORLD"

# Convert to lowercase
print(text.lower())      # "hello world"

# Capitalize first letter only
print(text.capitalize()) # "Hello world"

# Title case (capitalize each word)
print(text.title())      # "Hello World"

# Swap case
print(text.swapcase())   # "hELLO wORLD"

# Case-insensitive comparison
print(text.lower() == "hello world")  # True
```

### Search and Check Methods

```python
text = "Python Programming"

# Check if starts with
print(text.startswith("Python"))  # True
print(text.startswith("Java"))    # False

# Check if ends with
print(text.endswith("ming"))      # True
print(text.endswith("ing"))       # True

# Find substring (returns index or -1)
print(text.find("Pro"))           # 7
print(text.find("Java"))          # -1 (not found)

# Index (like find but raises error if not found)
print(text.index("Pro"))          # 7
# print(text.index("Java"))       # ValueError!

# Count occurrences
print(text.count("m"))            # 2
print(text.count("Pro"))          # 1

# Check if contains (better way)
print("Python" in text)           # True
print("Java" in text)             # False
```

### Validation Methods

```python
# Is alphabetic only?
print("Hello".isalpha())     # True
print("Hello123".isalpha())  # False

# Is digit only?
print("12345".isdigit())     # True
print("123abc".isdigit())    # False

# Is alphanumeric?
print("Hello123".isalnum())  # True
print("Hello 123".isalnum()) # False (space!)

# Is all lowercase?
print("hello".islower())     # True
print("Hello".islower())     # False

# Is all uppercase?
print("HELLO".isupper())     # True
print("Hello".isupper())     # False

# Is whitespace only?
print("   ".isspace())       # True
print(" a ".isspace())       # False
```

**Practical Use:**
```python
# Validate password
password = input("Enter password: ")

if len(password) < 8:
    print("Too short!")
elif not any(c.isdigit() for c in password):
    print("Must contain a number!")
elif not any(c.isupper() for c in password):
    print("Must contain an uppercase letter!")
else:
    print("Password accepted!")
```

### Trim and Strip Methods

```python
text = "   Hello World   "

# Remove whitespace from both ends
print(text.strip())       # "Hello World"

# Remove from left only
print(text.lstrip())      # "Hello World   "

# Remove from right only
print(text.rstrip())      # "   Hello World"

# Strip specific characters
text2 = "###Hello###"
print(text2.strip("#"))   # "Hello"
```

### Split and Join Methods

```python
# Split string into list
sentence = "Python is awesome"
words = sentence.split()  # ["Python", "is", "awesome"]
print(words)

# Split by specific delimiter
data = "apple,banana,orange"
fruits = data.split(",")  # ["apple", "banana", "orange"]
print(fruits)

# Split with max splits
text = "a-b-c-d-e"
parts = text.split("-", 2)  # ["a", "b", "c-d-e"]
print(parts)

# Join list into string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)  # "Python is awesome"
print(sentence)

# Join with different separator
sentence = "-".join(words)  # "Python-is-awesome"
print(sentence)
```

**Practical Examples:**
```python
# Parse CSV data
csv_line = "John,25,Engineer"
name, age, job = csv_line.split(",")
print(f"{name} is {age} years old and works as {job}")

# Create filename
words = ["my", "file", "name"]
filename = "_".join(words) + ".txt"  # "my_file_name.txt"

# Split lines
text = """Line 1
Line 2
Line 3"""
lines = text.split("\n")  # ["Line 1", "Line 2", "Line 3"]
```

### Replace Method

```python
text = "Hello World"

# Replace substring
new_text = text.replace("World", "Python")
print(new_text)  # "Hello Python"

# Replace with max count
text2 = "a b a b a b"
result = text2.replace("a", "x", 2)  # Replace first 2
print(result)  # "x b x b a b"

# Remove by replacing with empty string
text3 = "Hello World"
no_spaces = text3.replace(" ", "")
print(no_spaces)  # "HelloWorld"
```

### Alignment Methods

```python
text = "Python"

# Center align
print(text.center(20, "-"))  # "-------Python-------"

# Left align
print(text.ljust(20, "-"))   # "Python--------------"

# Right align
print(text.rjust(20, "-"))   # "--------------Python"

# Zero-fill (useful for numbers)
num = "42"
print(num.zfill(5))          # "00042"
```

---

## String Formatting

### F-Strings (Python 3.6+) ⭐ RECOMMENDED

Most modern and readable way:

```python
name = "Alice"
age = 25

# Basic f-string
message = f"My name is {name} and I am {age} years old"
print(message)

# Expressions inside {}
print(f"{name.upper()} is {age + 5} years old in 5 years")

# Calling functions
def discount(price):
    return price * 0.9
    
price = 100
print(f"Price after discount: ${discount(price)}")

# Formatting numbers
pi = 3.14159
price = 19.99

print(f"Pi: {pi:.2f}")            # "Pi: 3.14" (2 decimals)
print(f"Price: ${price:.2f}")     # "Price: $19.99"

# Width and alignment
name = "Bob"
print(f"|{name:>10}|")  # "|       Bob|" (right align)
print(f"|{name:<10}|")  # "|Bob       |" (left align)
print(f"|{name:^10}|")  # "|   Bob    |" (center)

# Numbers with thousands separator
large = 1000000
print(f"{large:,}")     # "1,000,000"

# Percentage
ratio = 0.75
print(f"{ratio:.2%}")   # "75.00%"
```

### format() Method

```python
name = "Alice"
age = 25

# Positional arguments
message = "My name is {} and I am {} years old".format(name, age)
print(message)

# Named arguments
message = "My name is {n} and I am {a} years old".format(n=name, a=age)
print(message)

# Index-based
message = "I am {1} years old and my name is {0}".format(name, age)
print(message)

# Formatting numbers
pi = 3.14159
print("Pi: {:.2f}".format(pi))  # "Pi: 3.14"

# Width and alignment
print("|{:>10}|".format("Bob"))  # "|       Bob|"
```

### % Formatting (Old Style)

```python
name = "Alice"
age = 25

# %s for string, %d for integer, %f for float
message = "My name is %s and I am %d years old" % (name, age)
print(message)

# Formatting numbers
pi = 3.14159
print("Pi: %.2f" % pi)  # "Pi: 3.14"

# Multiple values
print("%s is %d years old" % (name, age))
```

**Recommendation:** Use **f-strings** for modern Python!

---

## String Operations

### Concatenation (+)

```python
first = "Hello"
last = "World"

# Using +
result = first + " " + last  # "Hello World"

# Multiple concatenations
full = "Python" + " " + "is" + " " + "awesome"  # "Python is awesome"

# With variables
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"  # "Hello, Alice!"
```

### Repetition (*)

```python
# Repeat string
print("Ha" * 3)          # "HaHaHa"
print("-" * 20)          # "--------------------"
print("=" * 10)          # "=========="

# Create separator
separator = "=" * 50
print(separator)
print("Title")
print(separator)
```

### Membership (in, not in)

```python
text = "Python Programming"

# Check if substring exists
print("Python" in text)      # True
print("Java" in text)        # False
print("python" in text)      # False (case-sensitive!)

# Not in
print("Ruby" not in text)    # True

# Case-insensitive check
print("python" in text.lower())  # True
```

### Length

```python
text = "Python"
print(len(text))  # 6

# Empty string
empty = ""
print(len(empty))  # 0

# With spaces
sentence = "Hello World"
print(len(sentence))  # 11 (space counts!)
```

### Iteration

```python
text = "Python"

# Loop through each character
for char in text:
    print(char)
# P
# y
# t
# h
# o
# n

# With index
for i, char in enumerate(text):
    print(f"Index {i}: {char}")
```

---

## Escape Sequences

Special characters that start with backslash (`\`):

```python
# Newline \n
print("Hello\nWorld")
# Hello
# World

# Tab \t
print("Name:\tAlice")
# Name:    Alice

# Backslash \\
print("C:\\Users\\Documents")  # C:\Users\Documents

# Single quote \'
print('It\'s a nice day')  # It's a nice day

# Double quote \"
print("She said, \"Hello\"")  # She said, "Hello"

# Carriage return \r
print("Hello\rWorld")  # World (overwrites Hello in terminal)

# Unicode character \u
print("\u2665")  # ♥ (heart symbol)
print("\u03B1")  # α (alpha)
```

### Raw Strings

Prefix with `r` to treat backslash literally:

```python
# Regular string
path = "C:\\Users\\Documents"

# Raw string (no escaping needed)
path = r"C:\Users\Documents"

# Useful for regex patterns
import re
pattern = r"\d+"  # Match digits (\ is literal)
```

---

## String Immutability

Strings cannot be changed after creation (immutable):

```python
text = "Hello"

# This doesn't work!
# text[0] = 'h'  # TypeError: 'str' object doesn't support item assignment

# Instead, create a new string
text = "h" + text[1:]  # "hello"

# Or use methods (which return new strings)
text = text.replace("H", "h")  # "hello"
```

**Why Immutability Matters:**

```python
# Each modification creates a new string
original = "Python"
modified = original.replace("P", "J")

print(original)  # "Python" (unchanged!)
print(modified)  # "Jython" (new string)

# Multiple references
a = "Hello"
b = a
b = b + " World"

print(a)  # "Hello" (unchanged)
print(b)  # "Hello World" (new string)
```

---

## Advanced String Topics

### String Comparison

```python
# Lexicographic (alphabetical) comparison
print("apple" < "banana")   # True
print("zebra" > "apple")    # True
print("Apple" < "apple")    # True (uppercase comes first)

# Case-insensitive comparison
str1 = "Hello"
str2 = "hello"
print(str1.lower() == str2.lower())  # True

# Comparing lengths
if len(str1) == len(str2):
    print("Same length")
```

### Multi-line String Tricks

```python
# Continue on next line with \
long_text = "This is a very long string that " \
            "spans multiple lines in code but " \
            "is a single line when printed"

# Automatic concatenation
message = ("Hello "
           "World")  # "Hello World"
```

### String Constants

```python
import string

# All ASCII letters
print(string.ascii_letters)  # abcdefg...XYZ

# Lowercase only
print(string.ascii_lowercase)  # abcdefg...xyz

# Uppercase only
print(string.ascii_uppercase)  # ABCDEFG...XYZ

# Digits
print(string.digits)  # 0123456789

# Punctuation
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Whitespace
print(string.whitespace)  # ' \t\n\r\v\f'
```

---

## Practice Exercises

### Beginner Exercises

**Exercise 1: String Creation**
```python
# Create variables with your:
# - Full name
# - favorite_color
# - A sentence about yourself
```

**Exercise 2: String Slicing**
```python
text = "Python Programming"
# Extract: "Python", "Programming", "gram", reverse it
```

**Exercise 3: String Methods**
```python
# Convert "hello world" to:
# - All uppercase
# - Title case
# - First letter capitalized only
```

**Exercise 4: Check Email**
```python
email = "user@example.com"
# Check if it contains "@" and "."
```

**Exercise 5: Clean Input**
```python
user_input = "  Hello World  "
# Remove leading/trailing spaces and convert to lowercase
```

### Intermediate Exercises

**Exercise 6: Reverse Words**
```python
sentence = "Python is awesome"
# Output: "awesome is Python"
```

**Exercise 7: Count Vowels**
```python
text = "Hello World"
# Count how many vowels (a, e, i, o, u)
```

**Exercise 8: Palindrome Checker**
```python
word = "racecar"
# Check if it's a palindrome (reads same forwards and backwards)
```

**Exercise 9: Password Validator**
```python
password = "MyPass123"
# Check if:
# - At least 8 characters
# - Has uppercase letter
# - Has lowercase letter
# - Has a digit
```

**Exercise 10: Extract Domain**
```python
email = "user@example.com"
# Extract "example.com"
```

### Advanced Exercises

**Exercise 11: Titlecase Sentence**
```python
sentence = "the quick brown fox"
# Output: "The Quick Brown Fox"
# Don't capitalize: a, an, the, of, in, on (unless first word)
```

**Exercise 12: Remove Duplicates**
```python
text = "programming"
# Output: "progamin" (keep first occurrence only)
```

**Exercise 13: Caesar Cipher**
```python
text = "ABC"
shift = 3
# Output: "DEF" (shift each letter by 3)
```

**Exercise 14: Format Phone Number**
```python
phone = "1234567890"
# Output: "(123) 456-7890"
```

**Exercise 15: Word Frequency**
```python
text = "the quick brown fox jumps over the lazy dog"
# Count frequency of each word
```

---

## 🎯 Key Takeaways

✅ Strings are **immutable** sequences of characters  
✅ Use **f-strings** for modern, readable formatting  
✅ **Slicing** syntax: `[start:stop:step]`  
✅ Many built-in methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, etc.  
✅ **Indexing**: Positive from left (0, 1, 2...), negative from right (-1, -2, -3...)  
✅ Use `in` to check if substring exists  
✅ Escape sequences: `\n` (newline), `\t` (tab), `\\` (backslash)  
✅ Strings can't be modified in place - methods return new strings  

---

## 📚 Quick Reference

```python
# Creation
single = 'text'
double = "text"
multi = """text"""

# Indexing/Slicing
text[0]      # First char
text[-1]     # Last char
text[2:5]    # Substring
text[::-1]   # Reverse

# Common Methods
.upper()     .lower()     .capitalize()  .title()
.strip()     .lstrip()    .rstrip()
.startswith() .endswith() .find()        .count()
.split()     .join()      .replace()
.isalpha()   .isdigit()   .isalnum()

# Formatting
f"{name} is {age}"                    # f-string
"{} is {}".format(name, age)          # format()
"%s is %d" % (name, age)              # % formatting

# Operations
+    # Concatenation
*    # Repetition
in   # Membership
len() # Length
```

---

**End of Strings Notes** 📝

**Next Topics:** `Numbers_and_Booleans_Notes.md`, `Input_Output_Notes.md`

## Additional String Techniques

### String Multiplication for Patterns

```python
# Create decorative borders
print("=" * 50)
print("Title".center(50))
print("=" * 50)

# ASCII art patterns
print("*" * 20)
for i in range(5):
    print("*" + " " * 18 + "*")
print("*" * 20)

# Progress bars
def show_progress(percent):
    bar_length = 50
    filled = int(bar_length * percent / 100)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"[{bar}] {percent}%")

show_progress(75)  # [█████████████████████████████████████---------] 75%
```

### String Encoding and Decoding

```python
# Encode to bytes
text = "Hello, World!"
encoded = text.encode('utf-8')
print(encoded)  # b'Hello, World!'

# Decode from bytes
decoded = encoded.decode('utf-8')
print(decoded)  # "Hello, World!"

# Different encodings
text = "Café"
print(text.encode('utf-8'))    # b'Caf\xc3\xa9'
print(text.encode('ascii', errors='ignore'))  # b'Caf'
```

### String Translation

```python
# Create translation table
table = str.maketrans('aeiou', '12345')
text = "hello world"
translated = text.translate(table)
print(translated)  # "h2ll4 w4rld"

# Remove characters
remove_vowels = str.maketrans('', '', 'aeiou')
text = "hello world"
no_vowels = text.translate(remove_vowels)
print(no_vowels)  # "hll wrld"
```

---

## String Performance Tips

### Tip 1: Use join() Instead of += for Many Concatenations

```python
# ❌ SLOW (creates new string each time)
result = ""
for i in range(1000):
    result += str(i)

# ✅ FAST (builds list then joins once)
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)

# ✅ EVEN BETTER (list comprehension)
result = "".join(str(i) for i in range(1000))
```

### Tip 2: Use String Formatting Instead of Concatenation

```python
name = "Alice"
age = 25

# ❌ LESS EFFICIENT
message = "Name: " + name + ", Age: " + str(age)

# ✅ MORE EFFICIENT
message = f"Name: {name}, Age: {age}"
```

---

## Real-World String Applications

### Application 1: Text Cleaning

```python
def clean_text(text):
    """Clean and normalize text"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespace
    text = " ".join(text.split())
    
    # Remove punctuation
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text

dirty = "  Hello,  World!  How   are YOU?  "
clean = clean_text(dirty)
print(clean)  # "hello world how are you"
```

### Application 2: Password Validation

```python
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Too short (min 8 chars)"
    
    if not any(c.isupper() for c in password):
        return False, "Must contain uppercase"
    
    if not any(c.islower() for c in password):
        return False, "Must contain lowercase"
    
    if not any(c.isdigit() for c in password):
        return False, "Must contain digit"
    
    special = "!@#$%^&*"
    if not any(c in special for c in password):
        return False, "Must contain special character"
    
    return True, "Strong password!"

# Test
valid, message = validate_password("Weak")
print(message)  # "Too short (min 8 chars)"

valid, message = validate_password("Strong123!")
print(message)  # "Strong password!"
```

---

**End of Strings Notes** ���

Master these string techniques for powerful text processing in Python!
