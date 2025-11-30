# Day 4 Quick Reference Cheat Sheet

## File Opening Modes
```python
'r'   # Read (default) - must exist
'w'   # Write - creates/overwrites
'a'   # Append - creates if needed
'x'   # Create - fails if exists
'r+'  # Read/Write - must exist
'w+'  # Write/Read - creates/overwrites
'a+'  # Append/Read - creates if needed
'rb'  # Read binary
'wb'  # Write binary
```

## Reading Files
```python
# Best practice: use 'with'
with open("file.txt", "r") as f:
    content = f.read()      # Entire file as string
    line = f.readline()     # One line
    lines = f.readlines()   # All lines as list
    
    # Line by line (memory efficient)
    for line in f:
        print(line.strip())
```

## Writing Files
```python
with open("file.txt", "w") as f:
    f.write("Hello\n")           # Write string
    f.writelines(["a\n", "b\n"]) # Write list

# Append mode
with open("file.txt", "a") as f:
    f.write("Appended line\n")
```

## CSV Files
```python
import csv

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row is a list

# Read as dict
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])

# Write CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerows([["Alice", 25], ["Bob", 30]])
```

## JSON Files
```python
import json

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# String conversion
json_str = json.dumps(data)
data = json.loads(json_str)
```

## Exception Handling
```python
try:
    risky_code()
except ValueError:
    print("Value error!")
except (TypeError, KeyError) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Other error: {e}")
else:
    print("No error occurred")
finally:
    print("Always runs")
```

## Common Exceptions
```python
ValueError      # Wrong value
TypeError       # Wrong type
KeyError        # Dict key not found
IndexError      # List index out of range
FileNotFoundError  # File doesn't exist
ZeroDivisionError  # Division by zero
AttributeError  # Missing attribute
ImportError     # Import fails
```

## Raising Exceptions
```python
# Raise exception
raise ValueError("Invalid input")

# Re-raise current exception
except Exception:
    print("Logging error...")
    raise
```

## Custom Exceptions
```python
class MyError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(message)

raise MyError("Failed", 500)
```

## Context Managers
```python
# Using with statement
with open("file.txt") as f:
    content = f.read()
# File auto-closed

# Custom context manager
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Setup")
    yield
    print("Cleanup")
```

## Quick Patterns
```python
# Check file exists
import os
if os.path.exists("file.txt"):
    # do something

# Safe file read
def read_file(path, default=""):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return default

# Safe type conversion
def safe_int(val, default=0):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default
```

---
**Keep this handy for Day 4 topics!** 🚀
