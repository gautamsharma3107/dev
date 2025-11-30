# Python Standard Library: Complete Guide

---

## Table of Contents
1. [Introduction](#introduction)
2. [datetime Module](#datetime-module)
3. [math Module](#math-module)
4. [random Module](#random-module)
5. [re Module (Regular Expressions)](#re-module-regular-expressions)
6. [os and sys Modules](#os-and-sys-modules)
7. [argparse Module](#argparse-module)
8. [logging Module](#logging-module)
9. [json Module](#json-module)
10. [pickle Module](#pickle-module)
11. [Practical Examples](#practical-examples)
12. [Practice Exercises](#practice-exercises)

---

## Introduction

### Standard Library Overview

Python's standard library provides ready-made modules for common tasks.

### Why Use Standard Library?

1. **Pre-tested** - Thoroughly tested and reliable
2. **Performance** - Optimized implementations
3. **Consistency** - Follow Python conventions
4. **No Installation** - Built-in with Python

---

## datetime Module

### Working with Dates

```python
from datetime import date, datetime, timedelta

# Get today's date
today = date.today()
print(today)  # Output: 2025-11-04

# Create specific date
specific_date = date(2025, 12, 25)
print(specific_date)  # Output: 2025-12-25

# Date components
print(today.year)   # 2025
print(today.month)  # 11
print(today.day)    # 4

# Day of week (0=Monday, 6=Sunday)
print(today.weekday())     # 1 (Tuesday)
print(today.isoweekday())  # 2 (Tuesday, ISO)
```

### Working with Times

```python
from datetime import time, datetime

# Create time object
morning = time(8, 30, 0)
print(morning)  # Output: 08:30:00

# Time components
print(morning.hour)    # 8
print(morning.minute)  # 30
print(morning.second)  # 0

# Current datetime
now = datetime.now()
print(now)  # Output: 2025-11-04 12:14:32.123456

# Specific datetime
event = datetime(2025, 12, 25, 10, 30, 0)
print(event)  # Output: 2025-12-25 10:30:00

# Components
print(now.year, now.month, now.day)      # 2025 11 4
print(now.hour, now.minute, now.second)  # 12 14 32
```

### Timedeltas

```python
from datetime import datetime, timedelta

now = datetime.now()

# Create timedeltas
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
one_hour = timedelta(hours=1)
thirty_minutes = timedelta(minutes=30)

# Arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
last_month = now - timedelta(days=30)

print(f"Tomorrow: {tomorrow.date()}")
print(f"Next week: {next_week.date()}")
print(f"Last month: {last_month.date()}")

# Calculate difference
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 12, 31)
diff = date2 - date1
print(f"Days between: {diff.days}")  # 364
print(f"Total seconds: {diff.total_seconds()}")
```

### Formatting Dates

```python
from datetime import datetime

now = datetime.now()

# strftime - format datetime to string
print(now.strftime("%Y-%m-%d"))           # 2025-11-04
print(now.strftime("%d/%m/%Y"))           # 04/11/2025
print(now.strftime("%H:%M:%S"))           # 12:14:32
print(now.strftime("%A, %B %d, %Y"))      # Tuesday, November 04, 2025
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 2025-11-04 12:14:32

# Common format codes
# %Y - Year (4 digits)
# %m - Month (01-12)
# %d - Day (01-31)
# %H - Hour (00-23)
# %M - Minute (00-59)
# %S - Second (00-59)
# %A - Weekday name
# %B - Month name
```

### Parsing Dates

```python
from datetime import datetime

# strptime - parse string to datetime
date_str = "2025-12-25 10:30:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # Output: 2025-12-25 10:30:00

# Different formats
date_str2 = "25/12/2025"
parsed2 = datetime.strptime(date_str2, "%d/%m/%Y")
print(parsed2)  # Output: 2025-12-25 00:00:00

# With weekday
date_str3 = "Tuesday, December 25, 2025"
parsed3 = datetime.strptime(date_str3, "%A, %B %d, %Y")
print(parsed3)
```

---

## math Module

### Mathematical Functions

```python
import math

# Basic functions
print(math.ceil(3.2))      # 4 (round up)
print(math.floor(3.8))     # 3 (round down)
print(math.sqrt(16))       # 4.0 (square root)
print(math.pow(2, 3))      # 8.0 (power)
print(math.fabs(-5))       # 5.0 (absolute value)

# Trigonometric (in radians)
print(math.sin(math.pi/2)) # 1.0
print(math.cos(0))         # 1.0
print(math.tan(math.pi/4)) # 1.0

# Logarithms
print(math.log(10))        # 2.302... (natural log)
print(math.log10(100))     # 2.0 (log base 10)
print(math.log2(8))        # 3.0 (log base 2)

# Exponential
print(math.exp(1))         # 2.718... (e^1)

# GCD and LCM
print(math.gcd(48, 18))    # 6
print(math.lcm(12, 18))    # 36 (Python 3.9+)

# Factorial
print(math.factorial(5))   # 120
```

### Math Constants

```python
import math

print(math.pi)      # 3.14159...
print(math.e)       # 2.71828...
print(math.tau)     # 6.28318... (2*pi)
print(math.inf)     # infinity
print(math.nan)     # Not a number

# Infinity checking
print(math.isinf(math.inf))      # True
print(math.isnan(math.nan))      # True
print(math.isfinite(42))         # True
```

---

## random Module

### Random Numbers

```python
import random

# Random float [0.0, 1.0)
print(random.random())      # 0.371...

# Random integer in range
print(random.randint(1, 10))      # 1-10 inclusive
print(random.randrange(0, 10))    # 0-9 (like range)
print(random.randrange(0, 100, 5))  # 0, 5, 10, 15... (with step)

# Random float in range
print(random.uniform(1.0, 10.0))  # 1.0-10.0

# Normal distribution
print(random.gauss(0, 1))   # Mean=0, StdDev=1
```

### Random Choices

```python
import random

# Choose single element
colors = ["red", "green", "blue"]
print(random.choice(colors))  # Random color

# Choose multiple (without replacement)
print(random.sample(colors, 2))  # 2 unique colors

# Choose multiple (with replacement)
print(random.choices(colors, k=5))  # 5 elements (may repeat)

# Weighted choices
weights = [10, 1, 1]  # red is 10x more likely
print(random.choices(colors, weights=weights, k=100))
```

### Shuffling

```python
import random

# Shuffle list in-place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Shuffled order

# Without modifying original
original = [1, 2, 3, 4, 5]
shuffled = original.copy()
random.shuffle(shuffled)
```

---

## re Module (Regular Expressions)

### Pattern Matching Basics

```python
import re

# Simple pattern
pattern = r"hello"
text = "hello world"
if re.search(pattern, text):
    print("Found!")  # Output: Found!

# Case-insensitive
pattern = r"HELLO"
if re.search(pattern, text, re.IGNORECASE):
    print("Found!")  # Output: Found!
```

### Search and Match

```python
import re

text = "The year is 2025"

# search() - finds anywhere in string
match = re.search(r"\d+", text)
if match:
    print(match.group())  # Output: 2025
    print(match.start())  # 12
    print(match.end())    # 16

# match() - matches at beginning
match = re.match(r"The", text)
if match:
    print("Starts with 'The'")

# findall() - find all matches
numbers = re.findall(r"\d+", "I have 2 apples and 3 oranges")
print(numbers)  # ['2', '3']
```

### Groups and Capturing

```python
import re

# Capturing groups
text = "John is 30 years old"
pattern = r"(\w+) is (\d+)"
match = re.search(pattern, text)

if match:
    print(match.group(0))  # John is 30 (entire match)
    print(match.group(1))  # John (first group)
    print(match.group(2))  # 30 (second group)

# Named groups
pattern = r"(?P<name>\w+) is (?P<age>\d+)"
match = re.search(pattern, text)
print(match.group("name"))  # John
print(match.group("age"))   # 30
```

### Substitution

```python
import re

# Simple substitution
text = "The year is 2024"
new_text = re.sub(r"\d+", "2025", text)
print(new_text)  # The year is 2025

# Substitution with limit
text = "a a a a a"
new_text = re.sub(r"a", "b", text, count=2)
print(new_text)  # b b a a a

# Substitution with function
def double_number(match):
    num = int(match.group())
    return str(num * 2)

text = "I have 2 apples and 3 oranges"
new_text = re.sub(r"\d+", double_number, text)
print(new_text)  # I have 4 apples and 6 oranges
```

### Common Regex Patterns

```python
import re

# Email pattern
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email = "user@example.com"
print(re.match(email_pattern, email))  # Match object

# Phone number (US format)
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone = "123-456-7890"
print(re.match(phone_pattern, phone))

# URL pattern
url_pattern = r"https?://[^\s]+"
url = "https://example.com"
print(re.search(url_pattern, url))

# Common patterns
\d      # digit
\w      # word character (letter, digit, _)
\s      # whitespace
[a-z]   # character range
^       # start of string
$       # end of string
*       # 0 or more
+       # 1 or more
?       # 0 or 1
{n}     # exactly n
```

---

## os and sys Modules

### File System Operations

```python
import os
from pathlib import Path

# Current directory
cwd = os.getcwd()
print(cwd)

# List files
files = os.listdir(".")
print(files)

# Path operations
path = os.path.join("folder", "subfolder", "file.txt")
print(path)

# Check existence
print(os.path.exists("file.txt"))
print(os.path.isfile("file.txt"))
print(os.path.isdir("folder"))

# File operations
os.rename("old.txt", "new.txt")
os.remove("file.txt")
os.mkdir("new_folder")
os.makedirs("path/to/folder", exist_ok=True)

# Get file info
size = os.path.getsize("file.txt")
time = os.path.getmtime("file.txt")
```

### Environment Variables

```python
import os

# Get environment variable
home = os.environ.get("HOME")
user = os.environ.get("USER")

# Check if exists
if "PATH" in os.environ:
    print("PATH exists")

# Set environment variable
os.environ["MY_VAR"] = "value"
print(os.environ["MY_VAR"])
```

### System Information

```python
import sys
import os

# Python version
print(sys.version)
print(sys.version_info)

# Platform
print(sys.platform)  # linux, win32, darwin

# Executable
print(sys.executable)

# Path
print(sys.path)

# Arguments passed to script
print(sys.argv)
```

---

## argparse Module

### Command-line Argument Parsing

```python
import argparse

# Create parser
parser = argparse.ArgumentParser(description="My CLI tool")

# Add arguments
parser.add_argument("name", help="Your name")
parser.add_argument("-a", "--age", type=int, help="Your age")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

# Parse arguments
args = parser.parse_args()

# Access arguments
print(args.name)
print(args.age)
print(args.verbose)
```

### Creating CLI Tools

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="File processor")
    
    # Positional argument
    parser.add_argument("filename", help="File to process")
    
    # Optional arguments
    parser.add_argument("-o", "--output", default="output.txt",
                       help="Output file (default: output.txt)")
    parser.add_argument("-f", "--format", choices=["csv", "json", "xml"],
                       default="csv", help="Output format")
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="Enable verbose output")
    
    args = parser.parse_args()
    
    # Use arguments
    if args.verbose:
        print(f"Processing {args.filename}")
        print(f"Output: {args.output}")
        print(f"Format: {args.format}")
    
    # Process file...

if __name__ == "__main__":
    main()
```

---

## logging Module

### Log Levels

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Log messages
logging.debug("Debug message")      # Lowest priority
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message") # Highest priority
```

### Configuring Logging

```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log"
)

# Log to console and file
logger = logging.getLogger(__name__)
logger.info("Application started")
```

### Handlers and Formatters

```python
import logging

# Create logger
logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log messages
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
```

---

## json Module

### Serialization and Deserialization

```python
import json

# Python object to JSON string (serialization)
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"]
}

json_string = json.dumps(data)
print(json_string)

# JSON string to Python object (deserialization)
json_string = '{"name": "Bob", "age": 30}'
data = json.loads(json_string)
print(data)
print(data["name"])
```

### Working with JSON Files

```python
import json

# Write to file
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
```

### JSON Types

```python
import json

# Python to JSON conversion
data = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "null": None,
    "list": [1, 2, 3],
    "dict": {"nested": "value"}
}

json_string = json.dumps(data)
print(json_string)

# JSON types:
# string -> str
# number -> int/float
# true/false -> bool
# null -> None
# array -> list
# object -> dict
```

---

## pickle Module

### Object Serialization

```python
import pickle

# Serialize object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)

# Save to file
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

# Load from file
with open("person.pkl", "rb") as f:
    loaded_person = pickle.load(f)
    print(loaded_person.name)
    print(loaded_person.age)
```

### Pickle vs JSON

```python
import pickle
import json

# Pickle - any Python object
data = {"func": lambda x: x**2}
pickled = pickle.dumps(data)  # Works

# JSON - only basic types
data = {"name": "Alice"}
json_str = json.dumps(data)  # Works
# json.dumps({"func": lambda x: x**2})  # Error

# Best practice:
# Use JSON for data exchange, config files
# Use Pickle for Python-to-Python serialization
```

---

## Practical Examples

### Date Calculator

```python
from datetime import datetime, timedelta

def days_until(target_date_str):
    target = datetime.strptime(target_date_str, "%Y-%m-%d")
    today = datetime.now()
    diff = target - today
    return diff.days

days = days_until("2025-12-25")
print(f"Days until Christmas: {days}")
```

### Log File Analyzer

```python
import re
from collections import Counter

def analyze_logs(filename):
    pattern = r"\[(.*?)\].*?(\w+)$"
    levels = []
    
    with open(filename, "r") as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                timestamp, level = match.groups()
                levels.append(level)
    
    # Count log levels
    counts = Counter(levels)
    for level, count in counts.most_common():
        print(f"{level}: {count}")
```

### Configuration Parser

```python
import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default="config.json")
    args = parser.parse_args()
    
    with open(args.config) as f:
        config = json.load(f)
    
    print(f"Database: {config['database']}")
    print(f"Debug: {config['debug']}")

if __name__ == "__main__":
    main()
```

---

## Practice Exercises

### 1. datetime
- Calculate age from birthdate
- Find next occurrence of a date
- Format dates for display

### 2. math
- Calculate geometric shapes
- Implement trigonometric functions
- Work with complex numbers

### 3. random
- Generate random data
- Simulate probability scenarios
- Create random samples

### 4. re
- Extract data with regex
- Validate email/phone
- Parse log files

### 5. argparse
- Create CLI tool with arguments
- Add subcommands
- Implement help system

### 6. logging
- Configure logging system
- Log to file and console
- Use different log levels

### 7. JSON
- Parse JSON data
- Create JSON files
- Handle nested structures

### 8. Real-World Projects
- Build data analyzer
- Create backup tool
- Implement logger system

---

# End of Notes
