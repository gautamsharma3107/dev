# Python File Handling: Complete Guide

---

## Table of Contents
1. [Introduction to File Handling](#introduction-to-file-handling)
2. [Opening and Closing Files](#opening-and-closing-files)
3. [File Modes](#file-modes)
4. [Reading Files](#reading-files)
5. [Writing Files](#writing-files)
6. [Context Managers (with statement)](#context-managers-with-statement)
7. [Binary Files](#binary-files)
8. [File Paths and os Module](#file-paths-and-os-module)
9. [pathlib Module](#pathlib-module)
10. [CSV File Handling](#csv-file-handling)
11. [JSON File Handling](#json-file-handling)
12. [Practical Examples](#practical-examples)
13. [Practice Exercises](#practice-exercises)

---

## Introduction to File Handling

### Why File Handling?

1. **Data Persistence** - Save data beyond program execution
2. **Data Exchange** - Read/write data from external sources
3. **Configuration** - Load settings from files
4. **Logging** - Record program execution
5. **Batch Processing** - Handle large amounts of data

### File I/O Flow

```python
# Three main steps:
# 1. Open file
# 2. Read/Write data
# 3. Close file

file = open("data.txt", "r")
content = file.read()
file.close()
```

---

## Opening and Closing Files

### Basic File Opening

```python
# Open a file
file = open("data.txt", "r")  # r = read mode

# Close the file
file.close()
```

### File Object Methods

```python
# After opening file
file = open("data.txt", "r")

# Check if file is closed
print(file.closed)  # Output: False

# Get filename
print(file.name)    # Output: data.txt

# Get file mode
print(file.mode)    # Output: r

# Get current position (in bytes)
print(file.tell())  # Output: 0

file.close()
print(file.closed)  # Output: True
```

### Importance of Closing Files

```python
# BAD - file not closed
file = open("data.txt", "w")
file.write("Hello")
# File might not be written until close()

# GOOD - use context manager (better approach, see next section)
with open("data.txt", "w") as file:
    file.write("Hello")
# File automatically closed
```

---

## File Modes

### Common File Modes

| Mode | Description |
|------|------------|
| `'r'` | Read (default) - file must exist |
| `'w'` | Write - creates/overwrites file |
| `'a'` | Append - adds to end of file |
| `'r+'` | Read and write - file must exist |
| `'w+'` | Write and read - creates/overwrites |
| `'a+'` | Append and read - creates if not exists |

### Text vs Binary

```python
# Text mode (default)
file = open("data.txt", "r")        # Text mode

# Binary mode
file = open("data.bin", "rb")       # Binary read
file = open("data.bin", "wb")       # Binary write
```

### Mode Examples

```python
# Read mode - file must exist
with open("existing.txt", "r") as file:
    content = file.read()

# Write mode - creates/overwrites
with open("new.txt", "w") as file:
    file.write("New content")  # Previous content lost!

# Append mode - adds to end
with open("new.txt", "a") as file:
    file.write("\nAdded line")  # Previous content preserved
```

---

## Reading Files

### read() - Read Entire File

```python
# Read entire file content
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# read() with size parameter
with open("data.txt", "r") as file:
    chunk = file.read(10)  # Read first 10 characters
    print(chunk)
```

### readline() - Read One Line

```python
# Read one line at a time
with open("data.txt", "r") as file:
    line1 = file.readline()  # First line (with \n)
    line2 = file.readline()  # Second line (with \n)
    print(line1.strip())     # Remove \n
    print(line2.strip())
```

### readlines() - Read All Lines

```python
# Read all lines as list
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Remove \n
```

### Iterate Over File

```python
# Most efficient for large files
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# Equivalent to readlines() but more memory efficient
```

### Reading with Encoding

```python
# Specify encoding (important for special characters)
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Other common encodings
with open("data.txt", "r", encoding="latin-1") as file:
    content = file.read()
```

### Practical Reading Examples

```python
# Count lines in file
with open("data.txt", "r") as file:
    line_count = sum(1 for line in file)
    print(f"Total lines: {line_count}")

# Find specific lines
with open("data.txt", "r") as file:
    for line in file:
        if "keyword" in line:
            print(line.strip())

# Read specific number of lines
with open("data.txt", "r") as file:
    for i, line in enumerate(file):
        if i < 10:  # First 10 lines
            print(line.strip())
        else:
            break
```

---

## Writing Files

### write() - Write String

```python
# Write single string
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Write overwrites previous content!
# To append, use "a" mode instead

# Write multiple times
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
```

### writelines() - Write Multiple Lines

```python
# Write list of strings
lines = ["First line\n", "Second line\n", "Third line\n"]

with open("output.txt", "w") as file:
    file.writelines(lines)

# Note: writelines() does NOT add newlines automatically
# You must include \n in each string
```

### Append Mode

```python
# Append to existing file
with open("data.txt", "a") as file:
    file.write("\nNew line appended")

# File content preserved
```

### Writing with Formatting

```python
# Using formatted strings
with open("output.txt", "w") as file:
    name = "Alice"
    age = 25
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
```

---

## Context Managers (with statement)

### Why Use Context Managers?

Automatically closes files even if errors occur.

```python
# BAD - file not closed if error
file = open("data.txt", "r")
try:
    content = file.read()
except:
    print("Error reading file")
finally:
    file.close()

# GOOD - context manager
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed
```

### with Statement

```python
# Opens file, assigns to variable, ensures close()
with open("data.txt", "r") as file:
    content = file.read()

# File automatically closed here

# Multiple files
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content)
```

### Exception Safety

```python
# If error occurs, file still closes
with open("data.txt", "r") as file:
    lines = file.readlines()
    # Even if exception happens below, file closes
    for line in lines:
        if line.startswith("ERROR"):
            raise ValueError("Found error!")
```

---

## Binary Files

### Reading Binary Files

```python
# Read binary file
with open("image.png", "rb") as file:
    binary_data = file.read()
    print(type(binary_data))  # <class 'bytes'>

# Read specific number of bytes
with open("data.bin", "rb") as file:
    first_100_bytes = file.read(100)
```

### Writing Binary Files

```python
# Write binary data
data = b"Hello Binary"
with open("output.bin", "wb") as file:
    file.write(data)

# Copy binary file
with open("source.bin", "rb") as infile:
    with open("copy.bin", "wb") as outfile:
        outfile.write(infile.read())
```

### Working with Binary Data

```python
# Convert string to binary and write
text = "Hello, World!"
binary = text.encode("utf-8")  # Convert to bytes

with open("text.bin", "wb") as file:
    file.write(binary)

# Read binary and convert back to string
with open("text.bin", "rb") as file:
    binary_data = file.read()
    text = binary_data.decode("utf-8")
    print(text)  # Output: Hello, World!
```

---

## File Paths and os Module

### os Module Basics

```python
import os

# Get current working directory
current_dir = os.getcwd()
print(current_dir)

# Change directory
os.chdir("/path/to/directory")

# List files in directory
files = os.listdir(".")
print(files)

# Check if path exists
exists = os.path.exists("data.txt")
print(exists)

# Check if it's a file or directory
is_file = os.path.isfile("data.txt")
is_dir = os.path.isdir("data")
print(is_file, is_dir)
```

### Working with Paths

```python
import os

# Join paths (platform-independent)
path = os.path.join("folder", "subfolder", "file.txt")
print(path)

# Get file name
filename = os.path.basename("/home/user/data.txt")
print(filename)  # Output: data.txt

# Get directory
dirname = os.path.dirname("/home/user/data.txt")
print(dirname)  # Output: /home/user

# Split path
dir_path, file_name = os.path.split("/home/user/data.txt")
print(dir_path, file_name)

# Get absolute path
abs_path = os.path.abspath("data.txt")
print(abs_path)
```

### File Operations

```python
import os

# Rename file
os.rename("old_name.txt", "new_name.txt")

# Delete file
os.remove("file.txt")

# Create directory
os.mkdir("new_folder")

# Create nested directories
os.makedirs("path/to/nested/folder")

# Delete directory
os.rmdir("folder")  # Must be empty

# Get file size
size = os.path.getsize("data.txt")
print(f"Size: {size} bytes")
```

### Walking Through Directories

```python
import os

# Walk through all directories and files
for root, dirs, files in os.walk("/path/to/start"):
    print(f"Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    # Process each file
    for file in files:
        filepath = os.path.join(root, file)
        print(f"Processing: {filepath}")
```

---

## pathlib Module

### Path Objects

```python
from pathlib import Path

# Create Path object
p = Path("data.txt")
print(p)  # Output: data.txt

# Current directory
current = Path(".")
print(current)

# Home directory
home = Path.home()
print(home)

# Working directory
cwd = Path.cwd()
print(cwd)
```

### Path Operations

```python
from pathlib import Path

# Joining paths (cleaner than os.path.join)
p = Path("folder") / "subfolder" / "file.txt"
print(p)

# Get parts
print(p.parts)      # ('folder', 'subfolder', 'file.txt')
print(p.parent)     # folder/subfolder
print(p.name)       # file.txt
print(p.stem)       # file (without extension)
print(p.suffix)     # .txt

# Absolute path
abs_p = p.absolute()
print(abs_p)
```

### Path Methods

```python
from pathlib import Path

p = Path("data.txt")

# Check existence and type
print(p.exists())    # True/False
print(p.is_file())   # True/False
print(p.is_dir())    # True/False

# Create directory
p_dir = Path("new_folder")
p_dir.mkdir(exist_ok=True)  # exist_ok prevents error if exists

# Create nested directories
p_nested = Path("path/to/nested")
p_nested.mkdir(parents=True, exist_ok=True)

# Get file size
size = p.stat().st_size
print(f"Size: {size} bytes")
```

### Reading/Writing with pathlib

```python
from pathlib import Path

# Read file
p = Path("data.txt")
content = p.read_text()

# Write file
p.write_text("New content")

# Read binary
binary = p.read_bytes()

# Write binary
p.write_bytes(b"Binary content")

# Append (pathlib doesn't have built-in append)
p.write_text(p.read_text() + "\nAppended line")
```

### Iterating Paths

```python
from pathlib import Path

# Get all files in directory
folder = Path(".")
for file in folder.iterdir():
    print(file)

# Get all text files recursively
for file in folder.glob("**/*.txt"):
    print(file)

# Get files matching pattern
for file in folder.glob("*.py"):
    print(file)
```

---

## CSV File Handling

### Reading CSV Files

```python
import csv

# Read CSV as dictionaries
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary
        # Access columns by name
        print(f"Name: {row['name']}, Age: {row['age']}")

# Read CSV as lists
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
        print(f"Column 1: {row[0]}, Column 2: {row[1]}")
```

### Writing CSV Files

```python
import csv

# Write CSV from dictionaries
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Write CSV from lists
rows = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

### CSV with Different Delimiters

```python
import csv

# Tab-separated
with open("data.tsv", "r") as file:
    reader = csv.DictReader(file, delimiter="\t")
    for row in reader:
        print(row)

# Semicolon-separated
with open("data.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        print(row)

# Custom delimiter
with open("data.txt", "r") as file:
    reader = csv.DictReader(file, delimiter="|")
    for row in reader:
        print(row)
```

---

## JSON File Handling

### Reading JSON Files

```python
import json

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # Python dictionary or list

# Parse JSON string
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
print(data)  # {'name': 'Alice', 'age': 25}
```

### Writing JSON Files

```python
import json

# Write JSON from dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "gaming"]
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=2)  # indent for pretty printing

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
```

### Pretty Printing JSON

```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"]
}

# Pretty print
pretty_json = json.dumps(data, indent=2, sort_keys=True)
print(pretty_json)

# Output:
# {
#   "age": 25,
#   "hobbies": [
#     "reading",
#     "coding"
#   ],
#   "name": "Alice"
# }
```

### Complex JSON Handling

```python
import json

# Nested JSON
data = {
    "users": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ],
    "count": 2
}

# Write
with open("users.json", "w") as file:
    json.dump(data, file, indent=2)

# Read and process
with open("users.json", "r") as file:
    data = json.load(file)
    for user in data["users"]:
        print(f"{user['name']}: {user['age']}")
```

---

## Practical Examples

### Counting Lines in Large File

```python
def count_lines(filename):
    with open(filename, "r") as file:
        return sum(1 for line in file)

lines = count_lines("large_file.txt")
print(f"Total lines: {lines}")
```

### Copying File

```python
def copy_file(source, destination):
    with open(source, "r") as infile:
        with open(destination, "w") as outfile:
            outfile.write(infile.read())

copy_file("source.txt", "destination.txt")
```

### Merging Multiple Files

```python
def merge_files(file_list, output_file):
    with open(output_file, "w") as outfile:
        for filename in file_list:
            with open(filename, "r") as infile:
                outfile.write(infile.read())
                outfile.write("\n---\n")  # Separator

merge_files(["file1.txt", "file2.txt", "file3.txt"], "merged.txt")
```

### Reading Large CSV File

```python
import csv

def process_large_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Process each row (memory efficient)
            print(f"Processing: {row['name']}")

process_large_csv("large_data.csv")
```

### JSON Configuration File

```python
import json
from pathlib import Path

# Read configuration
config_path = Path("config.json")
config = json.loads(config_path.read_text())

print(f"Host: {config['host']}")
print(f"Port: {config['port']}")
```

---

## Practice Exercises

### 1. File Reading
- Read entire file content
- Read specific number of lines
- Count words/lines in a file

### 2. File Writing
- Write text to file
- Append to existing file
- Copy file contents

### 3. File Modes
- Practice different file modes (r, w, a)
- Understanding file mode behavior

### 4. Path Handling
- Use os module to navigate directories
- Use pathlib for modern path operations
- List files in directory

### 5. CSV Handling
- Read CSV file
- Write CSV file
- Filter CSV data
- Transform CSV data

### 6. JSON Handling
- Read JSON file
- Write JSON file
- Parse JSON string
- Modify and save JSON

### 7. Real-World Projects
- Build log file analyzer
- Create data backup script
- Implement configuration system
- Build data import/export tool

---

# End of Notes
