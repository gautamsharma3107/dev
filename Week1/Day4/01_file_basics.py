"""
Day 4 - File Basics
===================
Learn: Opening, closing, and basic file operations

Key Concepts:
- Files are external data storage
- Must open before use, close after
- Different modes: read, write, append
- 'with' statement auto-closes files
"""

import os

# ========== FILE MODES ==========
print("=" * 50)
print("FILE MODES")
print("=" * 50)

print("""
Mode | Description                  | File Must Exist?
-----|------------------------------|------------------
'r'  | Read only (default)          | Yes
'w'  | Write (overwrites)           | No (creates)
'a'  | Append                       | No (creates)
'x'  | Create (exclusive)           | No (fails if exists)
'r+' | Read and Write               | Yes
'w+' | Write and Read               | No (creates/overwrites)
'a+' | Append and Read              | No (creates)

Add 'b' for binary mode:
'rb' | Read binary
'wb' | Write binary
""")

# ========== BASIC FILE OPERATIONS ==========
print("=" * 50)
print("BASIC FILE OPERATIONS")
print("=" * 50)

# Method 1: Traditional way (NOT recommended)
print("\n1. Traditional method (must close manually):")
print("   file = open('filename.txt', 'r')")
print("   content = file.read()")
print("   file.close()  # MUST close!")

# Method 2: Using 'with' statement (RECOMMENDED)
print("\n2. Using 'with' statement (auto-closes):")
print("   with open('filename.txt', 'r') as file:")
print("       content = file.read()")
print("   # File automatically closed here")

# ========== CREATING A SAMPLE FILE ==========
print("\n" + "=" * 50)
print("CREATING A SAMPLE FILE")
print("=" * 50)

sample_content = """Hello, Python!
This is a sample file.
It has multiple lines.
We will use it to practice.
Line 5: The End."""

# Write to file using 'with'
with open("sample.txt", "w") as file:
    file.write(sample_content)
print("✅ Created 'sample.txt'")

# ========== READING FILES ==========
print("\n" + "=" * 50)
print("READING FILES")
print("=" * 50)

# Method 1: read() - entire file as string
print("\n1. read() - Entire file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Method 2: read(n) - first n characters
print("\n2. read(20) - First 20 characters:")
with open("sample.txt", "r") as file:
    content = file.read(20)
    print(f"'{content}'")

# Method 3: readline() - one line at a time
print("\n3. readline() - One line:")
with open("sample.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# Method 4: readlines() - all lines as list
print("\n4. readlines() - All lines as list:")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Method 5: Iterate line by line (BEST for large files)
print("\n5. Iterate line by line:")
with open("sample.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"   {i}: {line.strip()}")

# ========== WRITING FILES ==========
print("\n" + "=" * 50)
print("WRITING FILES")
print("=" * 50)

# write() - single string
print("\n1. write() - Write string:")
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line.\n")
print("✅ Created 'output.txt'")

# writelines() - list of strings
print("\n2. writelines() - Write list:")
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("output2.txt", "w") as file:
    file.writelines(lines)
print("✅ Created 'output2.txt'")

# Verify
with open("output.txt", "r") as file:
    print(f"\noutput.txt contents:\n{file.read()}")

# ========== APPENDING TO FILES ==========
print("=" * 50)
print("APPENDING TO FILES")
print("=" * 50)

# Append mode adds to end
with open("output.txt", "a") as file:
    file.write("This was appended!\n")
print("✅ Appended to 'output.txt'")

with open("output.txt", "r") as file:
    print(f"After append:\n{file.read()}")

# ========== FILE POINTER POSITION ==========
print("=" * 50)
print("FILE POINTER POSITION")
print("=" * 50)

with open("sample.txt", "r") as file:
    print(f"Initial position: {file.tell()}")
    
    file.read(10)
    print(f"After reading 10 chars: {file.tell()}")
    
    file.seek(0)  # Go back to start
    print(f"After seek(0): {file.tell()}")
    
    file.seek(20)  # Go to position 20
    rest = file.read()
    print(f"Content from position 20:\n{rest}")

# ========== FILE PROPERTIES ==========
print("\n" + "=" * 50)
print("FILE PROPERTIES")
print("=" * 50)

with open("sample.txt", "r") as file:
    print(f"File name: {file.name}")
    print(f"File mode: {file.mode}")
    print(f"Is closed (inside with)? {file.closed}")

print(f"Is closed (outside with)? {file.closed}")

# ========== CHECK IF FILE EXISTS ==========
print("\n" + "=" * 50)
print("CHECK IF FILE EXISTS")
print("=" * 50)

filename = "sample.txt"
if os.path.exists(filename):
    print(f"✅ '{filename}' exists")
    print(f"   Size: {os.path.getsize(filename)} bytes")
    print(f"   Is file? {os.path.isfile(filename)}")
else:
    print(f"❌ '{filename}' does not exist")

# Check non-existent
if os.path.exists("nonexistent.txt"):
    print("File exists")
else:
    print("❌ 'nonexistent.txt' does not exist")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: Simple Logger")
print("=" * 50)

from datetime import datetime

def log(message, filename="app.log"):
    """Log a timestamped message"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# Create log entries
log("Application started")
log("User logged in")
log("Processing data...")
log("Application closed")

print("Log file contents:")
with open("app.log", "r") as file:
    print(file.read())

# Cleanup
for f in ["sample.txt", "output.txt", "output2.txt", "app.log"]:
    if os.path.exists(f):
        os.remove(f)
print("✅ Cleaned up files")

print("\n" + "=" * 50)
print("✅ File Basics - Complete!")
print("=" * 50)
