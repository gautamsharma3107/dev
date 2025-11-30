"""
Day 4 - Context Managers
========================
Learn: The 'with' statement and resource management

Key Concepts:
- Context managers handle setup/cleanup
- 'with' statement auto-manages resources
- __enter__ and __exit__ methods
- contextlib for easy creation
"""

import os

# ========== WHAT ARE CONTEXT MANAGERS? ==========
print("=" * 50)
print("WHAT ARE CONTEXT MANAGERS?")
print("=" * 50)

print("""
Context Manager = Object that manages resources

Without context manager:
    file = open('file.txt')
    try:
        content = file.read()
    finally:
        file.close()  # Must remember!

With context manager:
    with open('file.txt') as file:
        content = file.read()
    # Auto-closed!

Benefits:
- Automatic cleanup
- Cleaner code
- Exception-safe
""")

# ========== FILE CONTEXT MANAGER ==========
print("=" * 50)
print("FILE CONTEXT MANAGER")
print("=" * 50)

# Files are the most common use case
print("1. File handling with 'with':")

with open("test.txt", "w") as f:
    f.write("Hello, World!")
    print(f"   Inside with: file closed? {f.closed}")

print(f"   Outside with: file closed? {f.closed}")

# Read back
with open("test.txt", "r") as f:
    print(f"   Content: {f.read()}")

os.remove("test.txt")

# ========== MULTIPLE CONTEXT MANAGERS ==========
print("\n" + "=" * 50)
print("MULTIPLE CONTEXT MANAGERS")
print("=" * 50)

# Create test files
with open("input.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3")

# Multiple files at once
print("Copy file using two context managers:")

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
    print("   Files processed!")

with open("output.txt", "r") as f:
    print(f"   Output: {f.read()}")

os.remove("input.txt")
os.remove("output.txt")

# ========== CREATING CONTEXT MANAGERS (CLASS) ==========
print("\n" + "=" * 50)
print("CREATING CONTEXT MANAGERS (Class-based)")
print("=" * 50)

class Timer:
    """Context manager to time code execution"""
    
    def __init__(self, name="Timer"):
        self.name = name
    
    def __enter__(self):
        import time
        self.start = time.time()
        print(f"   [{self.name}] Started...")
        return self  # Can return anything
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"   [{self.name}] Finished in {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

# Using our Timer
print("Testing Timer context manager:")
with Timer("Sum operation"):
    total = sum(range(1000000))

# ========== EXCEPTION HANDLING IN CONTEXT MANAGERS ==========
print("\n" + "=" * 50)
print("HANDLING EXCEPTIONS IN CONTEXT MANAGERS")
print("=" * 50)

class SafeOperation:
    """Context manager that handles exceptions"""
    
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"   Starting: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"   Error in {self.name}: {exc_val}")
            return True  # Suppress the exception
        print(f"   Completed: {self.name}")
        return False

print("Test without error:")
with SafeOperation("Task 1"):
    print("   Doing work...")

print("\nTest with error (suppressed):")
with SafeOperation("Task 2"):
    print("   Doing work...")
    raise ValueError("Something went wrong!")
print("   Code continues after suppressed error!")

# ========== CONTEXTLIB MODULE ==========
print("\n" + "=" * 50)
print("CONTEXTLIB - Easy Context Managers")
print("=" * 50)

from contextlib import contextmanager

# Using @contextmanager decorator
@contextmanager
def working_directory(path):
    """Temporarily change working directory"""
    original = os.getcwd()
    try:
        os.makedirs(path, exist_ok=True)
        os.chdir(path)
        print(f"   Changed to: {path}")
        yield path  # This is where 'with' block runs
    finally:
        os.chdir(original)
        print(f"   Restored to: {original}")

print("Testing working_directory:")
print(f"   Current: {os.getcwd()}")

# Use it (cleanup after)
temp_dir = os.path.join(os.getcwd(), "temp_test")
with working_directory(temp_dir):
    print(f"   Inside: {os.getcwd()}")

print(f"   After: {os.getcwd()}")
os.rmdir(temp_dir)

# ========== SUPPRESS CONTEXT MANAGER ==========
print("\n" + "=" * 50)
print("SUPPRESS - Ignore Specific Exceptions")
print("=" * 50)

from contextlib import suppress

print("Without suppress:")
print("   Would crash on FileNotFoundError")

print("\nWith suppress:")
with suppress(FileNotFoundError):
    os.remove("nonexistent_file.txt")
    print("   This won't print if error occurs")
print("   Code continues safely!")

# ========== REDIRECT OUTPUT ==========
print("\n" + "=" * 50)
print("REDIRECT OUTPUT")
print("=" * 50)

from contextlib import redirect_stdout
from io import StringIO

# Capture print output
output = StringIO()
with redirect_stdout(output):
    print("This goes to StringIO")
    print("So does this")

captured = output.getvalue()
print(f"Captured output:\n{captured}")

# ========== PRACTICAL: DATABASE CONNECTION ==========
print("=" * 50)
print("PRACTICAL: Database Connection Simulator")
print("=" * 50)

class DatabaseConnection:
    """Simulated database connection manager"""
    
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connected = False
    
    def __enter__(self):
        print(f"   Connecting to {self.database}@{self.host}...")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"   Closing connection to {self.database}...")
        self.connected = False
        if exc_type:
            print(f"   Error occurred: {exc_val}")
        return False
    
    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected!")
        print(f"   Executing: {sql}")
        return [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

print("Using DatabaseConnection:")
with DatabaseConnection("localhost", "mydb") as db:
    results = db.query("SELECT * FROM users")
    print(f"   Results: {results}")

print("   Connection closed automatically!")

# ========== PRACTICAL: FILE TRANSACTION ==========
print("\n" + "=" * 50)
print("PRACTICAL: Safe File Writer")
print("=" * 50)

@contextmanager
def safe_file_write(filename):
    """Write to temp file, rename on success"""
    temp_file = filename + ".tmp"
    try:
        f = open(temp_file, "w")
        yield f
        f.close()
        # Only rename if successful
        if os.path.exists(filename):
            os.remove(filename)
        os.rename(temp_file, filename)
        print(f"   ✅ Safely wrote to {filename}")
    except Exception as e:
        f.close()
        os.remove(temp_file)
        print(f"   ❌ Failed, temp file removed: {e}")
        raise

print("Safe file write:")
with safe_file_write("data.txt") as f:
    f.write("Important data\n")
    f.write("More data\n")

with open("data.txt", "r") as f:
    print(f"   Content: {f.read()}")

os.remove("data.txt")

print("\n" + "=" * 50)
print("✅ Context Managers - Complete!")
print("=" * 50)
