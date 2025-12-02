# Input and Output in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to I/O](#introduction-to-io)
2. [Input Function](#input-function)
3. [Print Function](#print-function)
4. [String Formatting](#string-formatting)
5. [File I/O Basics](#file-io-basics)
6. [Reading Files](#reading-files)
7. [Writing Files](#writing-files)
8. [Working with CSV Files](#working-with-csv-files)
9. [Working with JSON Files](#working-with-json-files)
10. [Error Handling in I/O](#error-handling-in-io)
11. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Get user input with input() function
- ✅ Master print() function and all its parameters
- ✅ Format output using f-strings, format(), and %
- ✅ Read from and write to files
- ✅ Handle different file formats (text, CSV, JSON)
- ✅ Implement proper error handling for I/O
- ✅ Validate user input effectively

---

## Introduction to I/O

### What is Input/Output?

**Input/Output (I/O)** refers to communication between a program and the outside world:
- **Input**: Getting data into the program (keyboard, files, network)
- **Output**: Sending data out of the program (screen, files, network)

```python
# Input - getting data
name = input("Enter your name: ")

# Output - displaying data
print(f"Hello, {name}!")
```

---

## Input Function

### Basic Input

```python
# Get user input (always returns string!)
name = input("What is your name? ")
print(f"Hello, {name}!")

# Input without prompt
data = input()

# Multiple inputs
first = input("First name: ")
last = input("Last name: ")
print(f"Full name: {first} {last}")
```

### Type Conversion

```python
# input() always returns string!
age_str = input("Enter your age: ")
print(type(age_str))  # <class 'str'>

# Convert to integer
age = int(input("Enter your age: "))
print(type(age))  # <class 'int'>

# Convert to float
price = float(input("Enter price: "))
print(type(price))  # <class 'float'>

# Multiple conversions
x = int(input("Enter x: "))
y = int(input("Enter y: "))
sum = x + y
print(f"{x} + {y} = {sum}")
```

### Input Validation

```python
# Validate numeric input
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0 and age < 150:
            break
        else:
            print("Please enter a valid age (1-149)")
    except ValueError:
        print("Please enter a number!")

print(f"Your age is {age}")

# Validate string input
while True:
    answer = input("Do you agree? (yes/no): ").lower()
    if answer in ['yes', 'no']:
        break
    print("Please enter 'yes' or 'no'")

# Validate email
while True:
    email = input("Enter email: ")
    if "@" in email and "." in email:
        break
    print("Please enter a valid email address")

# Validate non-empty input
while True:
    name = input("Enter your name: ").strip()
    if name:
        break
    print("Name cannot be empty!")
```

### Multiple Inputs on One Line

```python
# Split input
numbers = input("Enter numbers separated by space: ").split()
print(numbers)  # ['10', '20', '30']

# Convert to integers
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)  # [10, 20, 30]

# Unpack values
x, y = input("Enter x and y: ").split()
x, y = int(x), int(y)

# Or in one line
x, y = map(int, input("Enter x and y: ").split())
```

### Input with Default Values

```python
# Provide default if empty
name = input("Enter name (or press Enter for 'Guest'): ") or "Guest"
print(f"Hello, {name}!")

# Default with conversion
age_input = input("Enter age (default 18): ")
age = int(age_input) if age_input else 18
```

---

## Print Function

### Basic Printing

```python
# Simple print
print("Hello, World!")

# Multiple arguments
print("Python", "is", "awesome")  # Python is awesome

# Variables
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Numbers
print(42)
print(3.14)
print(True)
```

### Print Parameters

#### sep Parameter

```python
# Default separator is space
print("A", "B", "C")  # A B C

# Custom separator
print("A", "B", "C", sep=", ")  # A, B, C
print("A", "B", "C", sep=" | ")  # A | B | C
print("A", "B", "C", sep="-")  # A-B-C
print("A", "B", "C", sep="")  # ABC

# Practical use: CSV output
name, age, city = "Alice", 25, "NYC"
print(name, age, city, sep=",")  # Alice,25,NYC

# Multiple separators for different prints
print("2024", "12", "01", sep="-")  # 2024-12-01
```

#### end Parameter

```python
# Default end is newline (\n)
print("Hello")
print("World")
# Hello
# World

# Custom end
print("Hello", end=" ")
print("World")
# Hello World

# No newline
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".")
# Loading...

# Progress indicator
for i in range(5):
    print("#", end="")
print()  # New line at end
# #####
```

#### file Parameter

```python
# Print to file
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)
    print("This goes to file", file=f)

# Print to stderr
import sys
print("Error message", file=sys.stderr)

# Print to string (using StringIO)
from io import StringIO
output = StringIO()
print("Captured output", file=output)
result = output.getvalue()
print(result)  # "Captured output\n"
```

#### flush Parameter

```python
import time

# Without flush (buffered)
print("Loading", end="")
time.sleep(2)
print("Done!")

# With flush (immediate output)
print("Loading", end="", flush=True)
time.sleep(2)
print("Done!")

# Progress bar example
for i in range(10):
    print("#", end="", flush=True)
    time.sleep(0.5)
print()
```

### Combining Parameters

```python
# All parameters together
with open("log.txt", "w") as f:
    print("Status", "OK", sep=": ", end="\n", file=f, flush=True)

# Multiple values with custom formatting
values = [1, 2, 3, 4, 5]
print(*values, sep=" | ", end=" <-- Values\n")
# 1 | 2 | 3 | 4 | 5 <-- Values
```

### Printing Special Characters

```python
# Newline
print("Line 1\nLine 2")

# Tab
print("Name:\tAlice")
print("Age:\t25")

# Backslash
print("C:\\Users\\Documents")

# Quotes
print("She said, \"Hello!\"")
print('It\'s a nice day')

# Raw strings (no escaping)
print(r"C:\Users\Documents")  # C:\Users\Documents
```

---

## String Formatting

### F-Strings (Python 3.6+) ⭐ RECOMMENDED

```python
# Basic f-string
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")

# Expressions
print(f"Next year I'll be {age + 1}")
print(f"My name in uppercase: {name.upper()}")

# Calling functions
def square(x):
    return x ** 2

n = 5
print(f"Square of {n} is {square(n)}")

# Multiple lines
message = f"""
Name: {name}
Age: {age}
Status: Active
"""
print(message)
```

### F-String Formatting

```python
# Decimal places
pi = 3.14159
print(f"Pi: {pi:.2f}")  # Pi: 3.14
print(f"Pi: {pi:.4f}")  # Pi: 3.1416

# Width and alignment
text = "Python"
print(f"|{text:>10}|")  # |    Python| (right align, width 10)
print(f"|{text:<10}|")  # |Python    | (left align)
print(f"|{text:^10}|")  # |  Python  | (center align)

# Padding with custom character
print(f"|{text:*>10}|")  # |****Python|
print(f"|{text:->10}|")  # |----Python|

# Numbers with width
num = 42
print(f"|{num:5}|")      # |   42|
print(f"|{num:05}|")     # |00042| (zero-padded)

# Thousands separator
large = 1000000
print(f"{large:,}")      # 1,000,000
print(f"{large:_}")      # 1_000_000

# Percentage
ratio = 0.856
print(f"{ratio:.2%}")    # 85.60%

# Scientific notation
big = 1234567890
print(f"{big:e}")        # 1.234568e+09
print(f"{big:.2e}")      # 1.23e+09
```

### F-String Advanced Features

```python
# Debugging (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}")  # x=10, y=20

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")

# Dictionary access
person = {"name": "Alice", "age": 25}
print(f"Name: {person['name']}, Age: {person['age']}")

# Nested f-strings
value = 42
print(f"The answer is: {f'{value:>5}'}")
```

### format() Method

```python
# Positional arguments
print("My name is {} and I'm {} years old".format("Alice", 25))

# With indices
print("I'm {1} and my name is {0}".format("Alice", 25))

# Named arguments
print("My name is {name} and I'm {age}".format(name="Alice", age=25))

# Mixed
print("{0}, {1}, {other}".format("A", "B", other="C"))

# Formatting
pi = 3.14159
print("Pi: {:.2f}".format(pi))  # Pi: 3.14
print("Pi: {:10.2f}".format(pi))  # Pi:       3.14
```

### % Formatting (Old Style)

```python
# String
name = "Alice"
print("Hello, %s!" % name)

# Integer
age = 25
print("Age: %d" % age)

# Float
pi = 3.14159
print("Pi: %.2f" % pi)

# Multiple values
print("%s is %d years old" % ("Alice", 25))

## Named placeholders
print("%(name)s is %(age)d" % {"name": "Alice", "age": 25})
```

---

## File I/O Basics

### Opening Files

```python
# Open file for reading
file = open("data.txt", "r")
# ... use file ...
file.close()

# Better: Use with statement (auto-closes)
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed here
```

### File Modes

```python
# 'r' - Read (default)
# 'w' - Write (overwrites existing file)
# 'a' - Append (adds to end of file)
# 'x' - Exclusive creation (fails if file exists)
# 'b' - Binary mode
# 't' - Text mode (default)
# '+' - Read and write

# Examples
open("file.txt", "r")   # Read text
open("file.txt", "w")   # Write text (overwrite)
open("file.txt", "a")   # Append text
open("file.txt", "r+")  # Read and write
open("file.bin", "rb")  # Read binary
open("file.bin", "wb")  # Write binary
```

---

## Reading Files

### read() - Read Entire File

```python
# Read entire file as string
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read specific number of characters
with open("data.txt", "r") as file:
    first_100 = file.read(100)
    print(first_100)
```

### readline() - Read One Line

```python
# Read single line
with open("data.txt", "r") as file:
    line = file.readline()
    print(line)

# Read multiple lines
with open("data.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1, line2)
```

### readlines() - Read All Lines into List

```python
# Read all lines into list
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n', ...]

# Strip newlines
with open("data.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
```

### Iterating Over File

```python
# Best way to read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# Process each line
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        number = int(line.strip())
        total += number
    print(f"Total: {total}")
```

### Reading with Error Handling

```python
# Handle file not found
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist!")
except PermissionError:
    print("No permission to read file!")
except Exception as e:
    print(f"Error: {e}")
```

---

## Writing Files

### write() - Write String to File

```python
# Write to file (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")

# Returns number of characters written
with open("output.txt", "w") as file:
    chars_written = file.write("Hello!")
    print(f"Wrote {chars_written} characters")
```

### writelines() - Write List of Strings

```python
# Write list of lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Generate and write lines
with open("numbers.txt", "w") as file:
    lines = [f"{i}\n" for i in range(1, 11)]
    file.writelines(lines)
```

### Appending to Files

```python
# Append mode
with open("log.txt", "a") as file:
    file.write("New log entry\n")

# Append multiple times
with open("log.txt", "a") as file:
    file.write("Entry 1\n")
    file.write("Entry 2\n")
    file.write("Entry 3\n")
```

### Writing with Error Handling

```python
try:
    with open("output.txt", "w") as file:
        file.write("Data")
except PermissionError:
    print("No permission to write to file!")
except IOError as e:
    print(f"I/O error: {e}")
```

---

## Working with CSV Files

### Reading CSV Files

```python
import csv

# Read CSV with csv.reader
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['col1', 'col2', 'col3']

# Read CSV as dictionaries
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])

# Skip header
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        print(row)
```

### Writing CSV Files

```python
import csv

# Write CSV with csv.writer
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Write CSV as dictionaries
data = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

---

## Working with JSON Files

### Reading JSON Files

```python
import json

# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

# Parse JSON string
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
print(data["name"])
```

### Writing JSON Files

```python
import json

# Write JSON file
data = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)

# Pretty print
print(json.dumps(data, indent=4, sort_keys=True))
```

---

## Error Handling in I/O

### Common Exceptions

```python
# FileNotFoundError
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# PermissionError
try:
    with open("/etc/passwd", "w") as file:
        file.write("data")
except PermissionError:
    print("No permission!")

# IOError
try:
    with open("file.txt", "r") as file:
        content = file.read()
except IOError as e:
    print(f"I/O error: {e}")
```

### Comprehensive Error Handling

```python
def safe_read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

content = safe_read_file("data.txt")
if content:
    print(content)
```

---

## Practice Exercises

### Beginner

**Exercise 1**: Get user's name and age, print greeting

**Exercise 2**: Calculate rectangle area from user input

**Exercise 3**: Create a simple calculator (get two numbers and operation)

**Exercise 4**: Write user input to a file

**Exercise 5**: Read file and print line count

### Intermediate

**Exercise 6**: Read CSV file and calculate average of a column

**Exercise 7**: Create contact list program (save/load from file)

**Exercise 8**: Print formatted table of data

**Exercise 9**: Copy file line by line

**Exercise 10**: Count word frequency in text file

### Advanced

**Exercise 11**: Create a simple database using JSON

**Exercise 12**: Implement file search tool

**Exercise 13**: Create log file analyzer

**Exercise 14**: Build CSV to JSON converter

**Exercise 15**: Create configuration file reader

---

## 🎯 Key Takeaways

✅ **input()** always returns string - convert as needed  
✅ **print()** has sep, end, file, flush parameters  
✅ **F-strings** are the best formatting method  
✅ **with statement** automatically closes files  
✅ File modes: 'r' read, 'w' write, 'a' append  
✅ **csv module** for CSV files  
✅ **json module** for JSON files  
✅ Always handle **exceptions** in file I/O  

---

## 📚 Quick Reference

```python
# Input
name = input("Prompt: ")
age = int(input("Age: "))

# Print
print(a, b, sep=", ", end="\n")

# F-string formatting
f"{value}"           # Basic
f"{value:.2f}"       # 2 decimals
f"{value:>10}"       # Right align, width 10
f"{value:,}"         # Thousands separator

# File reading
with open("file.txt", "r") as f:
    content = f.read()
    lines = f.readlines()
    for line in f:
        print(line)

# File writing
with open("file.txt", "w") as f:
    f.write("text\n")
    f.writelines(["line1\n", "line2\n"])

# CSV
import csv
with open("file.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# JSON
import json
with open("file.json", "r") as f:
    data = json.load(f)
```

---

**End of Input/Output Notes** 📝

Master these I/O concepts for effective Python programming!

## Real-World Examples

### Example 1: User Registration System

```python
def register_user():
    """Simple user registration system with file storage"""
    print("=== User Registration ===")
    
    # Get user input
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    age = int(input("Enter age: "))
    
    # Validate input
    if not username or not email:
        print("Error: Username and email cannot be empty!")
        return
    
    if age < 18:
        print("Error: Must be 18 or older!")
        return
    
    # Save to file
    with open("users.txt", "a") as f:
        f.write(f"{username},{email},{age}\n")
    
    print(f"✓ User {username} registered successfully!")

# Usage
register_user()
```

### Example 2: Contact Book with JSON

```python
import json

def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    contacts = load_contacts()
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✓ Added {name}!")
```

---

## Command-Line Arguments

### Using sys.argv

```python
import sys

# python script.py arg1 arg2
print(f"Script: {sys.argv[0]}")
print(f"Args: {sys.argv[1:]}")

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
```

---

## Common Mistakes

### 1. Forgetting to Convert input()
```python
# ❌ WRONG
age = input("Age: ")
next_year = age + 1  # TypeError!

# ✅ CORRECT
age = int(input("Age: "))
next_year = age + 1
```

### 2. Not Using with Statement
```python
# ❌ BAD
f = open("file.txt", "r")
content = f.read()
f.close()  # Might not execute!

# ✅ GOOD
with open("file.txt", "r") as f:
    content = f.read()
```

---

## Further Learning

### Next Steps
1. Binary file I/O (`rb`, `wb` modes)
2. Regular expressions for text processing
3. Building complete CLI applications

---

**Continue practicing with real-world I/O projects!**

## Additional Tips

### Tip 1: Always Validate User Input
```python
while True:
    try:
        age = int(input("Age: "))
        if 0 < age < 150:
            break
        print("Please enter a valid age")
    except ValueError:
        print("Please enter a number")
```

### Tip 2: Use Descriptive Prompts
```python
# ❌ BAD
x = input("? ")

# ✅ GOOD
width = float(input("Enter rectangle width (in cm): "))
```

### Tip 3: Handle File Paths Properly
```python
import os

# Check if file exists before reading
if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        content = f.read()
else:
    print("File not found!")
```

---

**��� You've completed the Input/Output guide!**

Master these concepts through practice and real-world projects.
