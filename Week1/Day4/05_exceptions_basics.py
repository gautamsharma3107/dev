"""
Day 4 - Exception Basics
========================
Learn: Understanding Python exceptions

Key Concepts:
- Exceptions = errors during runtime
- Different exception types
- Exception hierarchy
- Reading error messages
"""

# ========== WHAT ARE EXCEPTIONS? ==========
print("=" * 50)
print("WHAT ARE EXCEPTIONS?")
print("=" * 50)

print("""
Exception = Error that occurs during program execution

Without handling:
  - Program crashes immediately
  - User sees ugly error message
  - Data may be lost

With handling:
  - Program continues gracefully
  - User sees friendly message
  - Can recover or log errors
""")

# ========== COMMON EXCEPTIONS ==========
print("=" * 50)
print("COMMON EXCEPTION TYPES")
print("=" * 50)

print("""
Exception Type      | When It Occurs
--------------------|----------------------------------
SyntaxError         | Invalid Python syntax
TypeError           | Wrong type operation
ValueError          | Right type, wrong value
NameError           | Variable not defined
IndexError          | List index out of range
KeyError            | Dictionary key not found
FileNotFoundError   | File doesn't exist
ZeroDivisionError   | Division by zero
AttributeError      | Object has no attribute
ImportError         | Module import fails
""")

# ========== EXCEPTION EXAMPLES ==========
print("=" * 50)
print("EXCEPTION EXAMPLES")
print("=" * 50)

# 1. TypeError
print("\n1. TypeError:")
print("   Code: 'hello' + 5")
print("   Error: can only concatenate str (not 'int') to str")

# 2. ValueError
print("\n2. ValueError:")
print("   Code: int('hello')")
print("   Error: invalid literal for int() with base 10: 'hello'")

# 3. NameError
print("\n3. NameError:")
print("   Code: print(undefined_variable)")
print("   Error: name 'undefined_variable' is not defined")

# 4. IndexError
print("\n4. IndexError:")
print("   Code: [1,2,3][10]")
print("   Error: list index out of range")

# 5. KeyError
print("\n5. KeyError:")
print("   Code: {'a':1}['b']")
print("   Error: 'b'")

# 6. ZeroDivisionError
print("\n6. ZeroDivisionError:")
print("   Code: 10 / 0")
print("   Error: division by zero")

# 7. FileNotFoundError
print("\n7. FileNotFoundError:")
print("   Code: open('nonexistent.txt')")
print("   Error: No such file or directory: 'nonexistent.txt'")

# ========== EXCEPTION HIERARCHY ==========
print("\n" + "=" * 50)
print("EXCEPTION HIERARCHY")
print("=" * 50)

print("""
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   └── FileNotFoundError
    ├── TypeError
    ├── ValueError
    └── ... many more
""")

# ========== READING ERROR MESSAGES ==========
print("=" * 50)
print("READING ERROR MESSAGES")
print("=" * 50)

print("""
Example Error:
--------------
Traceback (most recent call last):
  File "script.py", line 5, in <module>
    result = divide(10, 0)
  File "script.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero

How to read:
1. Start from BOTTOM - see exception type
2. Error message after colon
3. Look UP the traceback for location
4. File name, line number, function name
5. The actual code that caused it
""")

# ========== DEMONSTRATING EXCEPTIONS ==========
print("=" * 50)
print("LIVE EXCEPTION DEMOS (handled)")
print("=" * 50)

# Safe demo function
def demo_exception(code_str):
    """Safely demonstrate an exception"""
    try:
        exec(code_str)
    except Exception as e:
        print(f"   {type(e).__name__}: {e}")

print("\n1. TypeError:")
print("   'hello' + 5")
demo_exception("'hello' + 5")

print("\n2. ValueError:")
print("   int('abc')")
demo_exception("int('abc')")

print("\n3. IndexError:")
print("   [1,2,3][10]")
demo_exception("[1,2,3][10]")

print("\n4. KeyError:")
print("   {'a':1}['b']")
demo_exception("{'a':1}['b']")

print("\n5. ZeroDivisionError:")
print("   10 / 0")
demo_exception("10 / 0")

# ========== ACCESSING EXCEPTION INFO ==========
print("\n" + "=" * 50)
print("ACCESSING EXCEPTION INFORMATION")
print("=" * 50)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")

# ========== WHY HANDLE EXCEPTIONS? ==========
print("\n" + "=" * 50)
print("WHY HANDLE EXCEPTIONS?")
print("=" * 50)

print("""
1. PREVENT CRASHES
   - Keep program running
   - Handle errors gracefully

2. USER EXPERIENCE
   - Show friendly messages
   - Guide users to fix issues

3. DATA PROTECTION
   - Save data before failure
   - Clean up resources

4. DEBUGGING
   - Log errors for analysis
   - Track issues in production

5. ROBUSTNESS
   - Handle unexpected inputs
   - Deal with external failures
""")

print("\n" + "=" * 50)
print("✅ Exception Basics - Complete!")
print("=" * 50)
