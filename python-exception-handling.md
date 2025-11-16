# Python Exception Handling: Complete Guide

---

## Table of Contents
1. [Introduction to Exceptions](#introduction-to-exceptions)
2. [Understanding Exceptions](#understanding-exceptions)
3. [Try-Except Blocks](#try-except-blocks)
4. [Multiple Except Blocks](#multiple-except-blocks)
5. [Else Clause](#else-clause)
6. [Finally Clause](#finally-clause)
7. [Raising Exceptions](#raising-exceptions)
8. [Custom Exceptions](#custom-exceptions)
9. [Exception Hierarchy](#exception-hierarchy)
10. [Assertions](#assertions)
11. [Context Managers](#context-managers)
12. [Best Practices](#best-practices)
13. [Practical Examples](#practical-examples)
14. [Practice Exercises](#practice-exercises)

---

## Introduction to Exceptions

### What are Exceptions?

Exceptions are events that disrupt normal program execution flow.

### Why Handle Exceptions?

1. **Prevent Crashes** - Handle errors gracefully
2. **Provide Feedback** - Inform users of problems
3. **Log Issues** - Record errors for debugging
4. **Recover** - Continue execution after errors
5. **Cleanup** - Release resources properly

### Exception vs Error

```python
# Exceptions - can be caught and handled
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Errors - usually cannot be caught
# StackOverflowError, SystemError, etc.
```

---

## Understanding Exceptions

### Common Built-in Exceptions

| Exception | Cause |
|-----------|-------|
| `ZeroDivisionError` | Division by zero |
| `ValueError` | Invalid value |
| `TypeError` | Wrong type |
| `IndexError` | Index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File doesn't exist |
| `AttributeError` | Attribute doesn't exist |
| `NameError` | Variable not defined |
| `ImportError` | Cannot import module |
| `RuntimeError` | General runtime error |

### Examining Exception Information

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e)}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")
```

---

## Try-Except Blocks

### Basic Try-Except

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Catching Multiple Exception Types

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
```

### Accessing Exception Information

```python
try:
    files = ["file1.txt", "file2.txt"]
    print(files[10])
except IndexError as e:
    print(f"Error: {e}")
    print(f"Exception type: {type(e).__name__}")
```

### Exception as Base Class

```python
try:
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")

# Catches ANY exception (not recommended - too broad)
```

---

## Multiple Except Blocks

### Specific to General Order

```python
try:
    user_input = input("Enter a number: ")
    result = 10 / int(user_input)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print("An unexpected error occurred")
```

### Different Handling for Different Errors

```python
try:
    file = open("data.txt", "r")
    number = int(file.read())
    result = 100 / number
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("File contains non-numeric data")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    if 'file' in locals():
        file.close()
```

### Type-Specific Exception Handling

```python
def process_data(data):
    try:
        if isinstance(data, str):
            return int(data)
        elif isinstance(data, list):
            return sum(data)
        else:
            raise TypeError("Unsupported data type")
    except ValueError:
        print("Cannot convert to integer")
    except TypeError as e:
        print(f"Type error: {e}")

process_data("123")      # Works
process_data([1, 2, 3])  # Works
process_data({"a": 1})   # Raises TypeError
```

---

## Else Clause

### Using Else with Try-Except

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print(f"You entered: {x}")
    print(f"Square: {x ** 2}")
```

### Else Executes Only on Success

```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error reading file")
else:
    print(f"File contents: {data}")
    file.close()
```

### Practical Use Case

```python
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Both values must be numbers")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result

divide_numbers(10, 2)  # Output: Division successful: 10 / 2 = 5.0
divide_numbers(10, 0)  # Output: Cannot divide by zero
```

---

## Finally Clause

### Finally Always Executes

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error caught")
finally:
    print("This always executes")

# Output:
# Error caught
# This always executes
```

### Cleanup with Finally

```python
def read_file(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found")
    finally:
        if file:
            file.close()
            print("File closed")

read_file("nonexistent.txt")
# Output:
# File not found
# File closed
```

### Finally with Return

```python
def test_finally():
    try:
        return "Try block"
    finally:
        print("Finally block executes")

result = test_finally()
print(result)
# Output:
# Finally block executes
# Try block
```

### Complete Try-Except-Else-Finally

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Program completed")
```

---

## Raising Exceptions

### Raising Built-in Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    print(f"Age {age} is valid")

validate_age(25)   # Output: Age 25 is valid
validate_age(-5)   # Raises ValueError: Age cannot be negative
```

### Raising with Custom Message

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero. Divisor must be non-zero.")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

### Re-raising Exceptions

```python
def process_data(data):
    try:
        return int(data)
    except ValueError as e:
        print(f"Logging error: Invalid data: {data}")
        raise  # Re-raise the same exception

try:
    process_data("abc")
except ValueError:
    print("Caught re-raised exception")

# Output:
# Logging error: Invalid data: abc
# Caught re-raised exception
```

### Chaining Exceptions

```python
try:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid calculation") from e
except ValueError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")
```

---

## Custom Exceptions

### Creating Custom Exception Classes

```python
# Simple custom exception
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Age {age} is invalid")

try:
    validate_age(-5)
except InvalidAgeError as e:
    print(f"Caught custom error: {e}")
```

### Custom Exception with Details

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance {balance}, Requested {amount}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew ${amount}")

account = BankAccount(1000)
try:
    account.withdraw(500)
    account.withdraw(700)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    print(f"Current balance: ${e.balance}")
```

### Exception Inheritance

```python
# Custom exception hierarchy
class ValidationError(Exception):
    pass

class EmailError(ValidationError):
    pass

class PasswordError(ValidationError):
    pass

def validate_email(email):
    if "@" not in email:
        raise EmailError("Invalid email format")

def validate_password(password):
    if len(password) < 8:
        raise PasswordError("Password too short")

# Handle specific errors
try:
    validate_email("invalid")
except EmailError as e:
    print(f"Email error: {e}")
except ValidationError as e:
    print(f"Validation error: {e}")
```

---

## Exception Hierarchy

### Built-in Exception Tree

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── ...
    ├── RuntimeError
    ├── SyntaxError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    └── Warning
```

### Checking Exception Hierarchy

```python
# Check if exception is instance of type
try:
    x = 1 / 0
except Exception as e:
    print(isinstance(e, ZeroDivisionError))  # True
    print(isinstance(e, ArithmeticError))    # True (parent)
    print(isinstance(e, Exception))          # True (ancestor)
```

---

## Assertions

### Basic Assertions

```python
# Assert with no message
x = 5
assert x > 0

# Assert will fail silently if condition is True
# Assert raises AssertionError if condition is False
assert x > 10  # Raises: AssertionError
```

### Assertions with Messages

```python
def validate_scores(scores):
    assert len(scores) > 0, "Scores list cannot be empty"
    assert all(0 <= s <= 100 for s in scores), "All scores must be 0-100"
    return sum(scores) / len(scores)

try:
    avg = validate_scores([85, 90, 88])
    print(f"Average: {avg}")
except AssertionError as e:
    print(f"Assertion failed: {e}")
```

### Assertions in Development

```python
def process_data(data):
    # Development assertions
    assert data is not None, "Data cannot be None"
    assert isinstance(data, list), "Data must be a list"
    
    # Process data
    return sum(data)

# Assertions can be disabled with: python -O script.py
```

### Best Practices for Assertions

```python
# Good - assertions for sanity checks during development
def binary_search(arr, target):
    assert len(arr) > 0, "Array must not be empty"
    assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)), "Array must be sorted"
    # Implementation...

# Bad - don't use assertions for user input validation
# Use try-except instead
# assert int(user_input) > 0, "User must enter positive number"  # BAD

try:
    number = int(user_input)
    if number <= 0:
        raise ValueError("Must be positive")
except ValueError:
    print("Invalid input")  # GOOD
```

---

## Context Managers

### Using Context Managers

```python
# Context managers ensure cleanup
with open("data.txt", "r") as file:
    data = file.read()
# File automatically closed

# Without context manager
file = open("data.txt", "r")
try:
    data = file.read()
finally:
    file.close()
```

### Creating Custom Context Managers

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"Opened {self.filename}")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"Closed {self.filename}")
        return False

with FileManager("data.txt", "w") as f:
    f.write("Hello, World!")
```

### Using contextlib

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Setting up resource")
    try:
        yield "resource"
    finally:
        print("Cleaning up resource")

with managed_resource() as r:
    print(f"Using {r}")

# Output:
# Setting up resource
# Using resource
# Cleaning up resource
```

---

## Best Practices

### 1. Catch Specific Exceptions

```python
# BAD - too broad
try:
    dangerous_operation()
except Exception:
    pass

# GOOD - specific
try:
    dangerous_operation()
except FileNotFoundError:
    handle_file_error()
except ValueError:
    handle_value_error()
```

### 2. Don't Suppress All Exceptions

```python
# BAD
try:
    risky_code()
except:
    pass

# GOOD
try:
    risky_code()
except SpecificError as e:
    log_error(e)
    handle_error(e)
```

### 3. Use Finally for Cleanup

```python
# GOOD - resources always cleaned up
try:
    file = open("data.txt")
    data = file.read()
except IOError as e:
    print(f"Error: {e}")
finally:
    if file:
        file.close()
```

### 4. Use Context Managers

```python
# BETTER - automatic cleanup
with open("data.txt") as file:
    data = file.read()
# File automatically closed
```

### 5. Log Exceptions

```python
import logging

try:
    risky_operation()
except Exception as e:
    logging.error(f"Operation failed: {e}", exc_info=True)
```

### 6. Provide Context

```python
# BAD
except Exception:
    print("Error")

# GOOD
except Exception as e:
    print(f"Failed to process user {user_id}: {e}")
```

---

## Practical Examples

### Data Validation

```python
def validate_user_input(age, email):
    try:
        age = int(age)
        if age < 0 or age > 150:
            raise ValueError("Age must be 0-150")
        
        if "@" not in email:
            raise ValueError("Invalid email")
        
        return age, email
    except ValueError as e:
        print(f"Validation error: {e}")
        return None, None

age, email = validate_user_input("25", "user@example.com")
```

### File Processing

```python
def read_config_file(filename):
    try:
        with open(filename, "r") as file:
            config = {}
            for line in file:
                if line.startswith("#"):
                    continue
                key, value = line.strip().split("=")
                config[key] = value
            return config
    except FileNotFoundError:
        print(f"Config file {filename} not found")
    except ValueError:
        print("Invalid config format")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Config loading completed")
```

### Database Operations

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        try:
            # Simulate connection
            self.connection = f"Connected to {self.db_name}"
            print(self.connection)
            return self
        except Exception as e:
            print(f"Connection failed: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            print(f"Disconnected from {self.db_name}")
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False

with DatabaseConnection("users.db") as db:
    print("Performing database operations...")
```

---

## Practice Exercises

### 1. Exception Basics
- Create try-except blocks for common errors
- Practice handling multiple exception types
- Access and display exception information

### 2. Exception Control Flow
- Use else clause for success path
- Use finally clause for cleanup
- Combine try-except-else-finally

### 3. Raising Exceptions
- Raise built-in exceptions with messages
- Re-raise exceptions
- Chain exceptions with "from"

### 4. Custom Exceptions
- Create custom exception classes
- Create exception hierarchy
- Use custom exceptions in your code

### 5. Assertions
- Write assertions for preconditions
- Use assertions in development
- Understand assertion limitations

### 6. Context Managers
- Use with statement for resources
- Create custom context managers
- Use contextlib decorators

### 7. Real-World Scenarios
- Build error-handling for user input
- Create file processing with proper cleanup
- Implement database operations safely
- Build configuration file reader

---

# End of Notes
