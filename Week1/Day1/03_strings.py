"""
Day 1 - Strings
===============
Learn: String creation, operations, methods, formatting

Key Concepts:
- Strings are sequences of characters
- Immutable (cannot be changed after creation)
- Rich set of methods for manipulation
- Multiple ways to format strings
"""

# ========== STRING CREATION ==========
print("=" * 50)
print("STRING CREATION")
print("=" * 50)

# Single quotes
name = 'Gautam'
print(f"Single quotes: {name}")

# Double quotes
greeting = "Hello, World!"
print(f"Double quotes: {greeting}")

# Triple quotes (multiline)
message = """This is a
multiline string.
It preserves line breaks."""
print(f"Triple quotes:\n{message}")

# ========== STRING INDEXING & SLICING ==========
print("\n" + "=" * 50)
print("STRING INDEXING & SLICING")
print("=" * 50)

text = "Python"
print(f"String: {text}")
print(f"Length: {len(text)}")

# Indexing
print(f"\nFirst character [0]: {text[0]}")
print(f"Last character [-1]: {text[-1]}")
print(f"Third character [2]: {text[2]}")

# Slicing [start:end:step]
print(f"\nFirst 3 characters [0:3]: {text[0:3]}")
print(f"Last 3 characters [-3:]: {text[-3:]}")
print(f"Every other character [::2]: {text[::2]}")
print(f"Reverse string [::-1]: {text[::-1]}")

# ========== STRING CONCATENATION ==========
print("\n" + "=" * 50)
print("STRING CONCATENATION")
print("=" * 50)

first_name = "Gautam"
last_name = "Sharma"

# Using +
full_name = first_name + " " + last_name
print(f"Using +: {full_name}")

# Using join()
parts = [first_name, last_name]
full_name2 = " ".join(parts)
print(f"Using join(): {full_name2}")

# Repetition
print(f"Repeat 3 times: {'Ha' * 3}")

# ========== STRING METHODS ==========
print("\n" + "=" * 50)
print("STRING METHODS")
print("=" * 50)

sample = "  Hello, Python World!  "
print(f"Original: '{sample}'")

# Case conversion
print(f"upper(): {sample.upper()}")
print(f"lower(): {sample.lower()}")
print(f"title(): {sample.title()}")
print(f"capitalize(): {sample.capitalize()}")

# Whitespace removal
print(f"strip(): '{sample.strip()}'")
print(f"lstrip(): '{sample.lstrip()}'")
print(f"rstrip(): '{sample.rstrip()}'")

# Replace
new_text = sample.replace("Python", "Programming")
print(f"replace(): {new_text}")

# Split and Join
words = sample.strip().split()
print(f"split(): {words}")

joined = "-".join(words)
print(f"join(): {joined}")

# ========== STRING CHECKING METHODS ==========
print("\n" + "=" * 50)
print("STRING CHECKING METHODS")
print("=" * 50)

text1 = "hello"
text2 = "HELLO"
text3 = "12345"
text4 = "hello123"

print(f"'{text1}' is lowercase: {text1.islower()}")
print(f"'{text2}' is uppercase: {text2.isupper()}")
print(f"'{text3}' is digit: {text3.isdigit()}")
print(f"'{text4}' is alphanumeric: {text4.isalnum()}")

# Find and Count
sentence = "Python is awesome. Python is powerful."
print(f"\nSentence: {sentence}")
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Find 'awesome': {sentence.find('awesome')}")
print(f"Find 'java' (not found): {sentence.find('java')}")  # Returns -1

# Starts with / Ends with
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'powerful.': {sentence.endswith('powerful.')}")

# ========== STRING FORMATTING ==========
print("\n" + "=" * 50)
print("STRING FORMATTING")
print("=" * 50)

name = "Gautam"
age = 25
height = 5.9

# 1. f-strings (Python 3.6+) - RECOMMENDED
print(f"1. f-string: My name is {name}, I am {age} years old.")

# 2. format() method
print("2. format(): My name is {}, I am {} years old.".format(name, age))
print("3. format() with names: My name is {n}, I am {a} years old.".format(n=name, a=age))

# 4. % formatting (old style)
print("4. %% formatting: My name is %s, I am %d years old." % (name, age))

# Advanced formatting
pi = 3.14159265359
print(f"\nPi with 2 decimals: {pi:.2f}")
print(f"Pi with 4 decimals: {pi:.4f}")

number = 1234567
print(f"Number with commas: {number:,}")

# ========== ESCAPE CHARACTERS ==========
print("\n" + "=" * 50)
print("ESCAPE CHARACTERS")
print("=" * 50)

print("New line: Hello\\nWorld")
print("Hello\nWorld")

print("\nTab: Hello\\tWorld")
print("Hello\tWorld")

print("\nBackslash: C:\\\\Users\\\\Documents")
print("C:\\Users\\Documents")

print("\nQuote in string: He said \"Hello\"")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Email validation (simple)
email = "gautam@example.com"
is_valid = "@" in email and "." in email
print(f"Email: {email}")
print(f"Is valid (simple check): {is_valid}")

# Create username from full name
full_name = "Gautam Sharma"
username = full_name.lower().replace(" ", "_")
print(f"\nFull name: {full_name}")
print(f"Username: {username}")

# Password masking
password = "secretpass123"
masked = "*" * len(password)
print(f"\nPassword: {masked}")

# Text centering
title = "Welcome"
print(f"\n{title.center(50, '=')}")

print("\n" + "=" * 50)
print("✅ Strings - Complete!")
print("=" * 50)
