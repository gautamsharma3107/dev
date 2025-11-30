"""
Day 4 - Try/Except/Finally
==========================
Learn: Handling exceptions properly

Key Concepts:
- try: code that might fail
- except: handle specific errors
- else: runs if no error
- finally: always runs
"""

# ========== BASIC TRY/EXCEPT ==========
print("=" * 50)
print("BASIC TRY/EXCEPT")
print("=" * 50)

# Without handling (commented - would crash)
# result = 10 / 0

# With handling
print("1. Basic try/except:")
try:
    result = 10 / 0
except:
    print("   An error occurred!")

# ========== CATCHING SPECIFIC EXCEPTIONS ==========
print("\n" + "=" * 50)
print("CATCHING SPECIFIC EXCEPTIONS")
print("=" * 50)

print("1. Catch specific type:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("   Cannot divide by zero!")

print("\n2. Access exception object:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   Error: {e}")

# ========== MULTIPLE EXCEPT BLOCKS ==========
print("\n" + "=" * 50)
print("MULTIPLE EXCEPT BLOCKS")
print("=" * 50)

def process_input(value):
    try:
        number = int(value)
        result = 100 / number
        return result
    except ValueError:
        return "Not a valid number!"
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except Exception as e:
        return f"Unexpected error: {e}"

print(f"process_input('5'): {process_input('5')}")
print(f"process_input('abc'): {process_input('abc')}")
print(f"process_input('0'): {process_input('0')}")

# ========== CATCHING MULTIPLE TYPES ==========
print("\n" + "=" * 50)
print("CATCHING MULTIPLE EXCEPTION TYPES")
print("=" * 50)

def get_item(data, key):
    try:
        return data[key]
    except (KeyError, IndexError, TypeError) as e:
        return f"Access error: {type(e).__name__}"

print(f"Dict access: {get_item({'a': 1}, 'b')}")
print(f"List access: {get_item([1,2,3], 10)}")
print(f"None access: {get_item(None, 0)}")

# ========== TRY/EXCEPT/ELSE ==========
print("\n" + "=" * 50)
print("TRY/EXCEPT/ELSE")
print("=" * 50)

print("""
else block runs ONLY if no exception occurred
""")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("   Error: Division by zero!")
        return None
    else:
        print("   Success! No errors.")
        return result

print("divide(10, 2):")
print(f"   Result: {divide(10, 2)}")

print("\ndivide(10, 0):")
divide(10, 0)

# ========== TRY/EXCEPT/FINALLY ==========
print("\n" + "=" * 50)
print("TRY/EXCEPT/FINALLY")
print("=" * 50)

print("""
finally block ALWAYS runs, even if:
- Exception occurs
- Return statement executed
- Exception re-raised
""")

def read_file_demo(filename):
    file = None
    try:
        print(f"   Opening {filename}...")
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print("   Error: File not found!")
        return None
    finally:
        print("   Finally: Cleaning up...")
        if file:
            file.close()
            print("   File closed.")

print("Reading existing file concept:")
read_file_demo("nonexistent.txt")

# ========== COMPLETE STRUCTURE ==========
print("\n" + "=" * 50)
print("COMPLETE TRY STRUCTURE")
print("=" * 50)

def complete_example(x, y):
    try:
        print(f"   Trying: {x} / {y}")
        result = x / y
    except ZeroDivisionError:
        print("   Except: Can't divide by zero!")
        result = None
    except TypeError:
        print("   Except: Invalid types!")
        result = None
    else:
        print(f"   Else: Success! Result = {result}")
    finally:
        print("   Finally: This always runs!")
    
    return result

print("\nTest 1: complete_example(10, 2)")
complete_example(10, 2)

print("\nTest 2: complete_example(10, 0)")
complete_example(10, 0)

print("\nTest 3: complete_example('10', 2)")
complete_example("10", 2)

# ========== RAISING EXCEPTIONS ==========
print("\n" + "=" * 50)
print("RAISING EXCEPTIONS")
print("=" * 50)

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age {age} is valid"

print("Testing validate_age():")
try:
    print(f"   {validate_age(25)}")
    print(f"   {validate_age(-5)}")
except ValueError as e:
    print(f"   ValueError: {e}")

try:
    print(f"   {validate_age('twenty')}")
except TypeError as e:
    print(f"   TypeError: {e}")

# ========== RE-RAISING EXCEPTIONS ==========
print("\n" + "=" * 50)
print("RE-RAISING EXCEPTIONS")
print("=" * 50)

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print("   Logging error...")
        raise  # Re-raise the same exception

print("Re-raising after logging:")
try:
    process_data("abc")
except ValueError as e:
    print(f"   Caught re-raised error: {e}")

# ========== EXCEPTION CHAINING ==========
print("\n" + "=" * 50)
print("EXCEPTION CHAINING")
print("=" * 50)

def fetch_data():
    try:
        # Simulate failed operation
        raise ConnectionError("Network unavailable")
    except ConnectionError as e:
        raise RuntimeError("Failed to fetch data") from e

try:
    fetch_data()
except RuntimeError as e:
    print(f"   Error: {e}")
    print(f"   Caused by: {e.__cause__}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: Safe Calculator")
print("=" * 50)

def safe_calculate(expression):
    """Safely evaluate a math expression"""
    try:
        # Only allow safe operations
        allowed = set("0123456789+-*/.(). ")
        if not all(c in allowed for c in expression):
            raise ValueError("Invalid characters in expression")
        
        result = eval(expression)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except SyntaxError:
        return "Error: Invalid expression!"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"

print(f"   '10 + 5': {safe_calculate('10 + 5')}")
print(f"   '100 / 4': {safe_calculate('100 / 4')}")
print(f"   '10 / 0': {safe_calculate('10 / 0')}")
print(f"   '10 +': {safe_calculate('10 +')}")

print("\n" + "=" * 50)
print("✅ Try/Except/Finally - Complete!")
print("=" * 50)
