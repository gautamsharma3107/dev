"""
EXERCISES: Exception Handling
=============================
Complete all exercises below
"""

# Exercise 1: Safe Division
# TODO: Create a function that safely divides two numbers
# Handle: ZeroDivisionError, TypeError
# Return None on error with printed message

print("Exercise 1: Safe Division")
print("-" * 40)

def safe_divide(a, b):
    """Safely divide a by b"""
    pass  # Your code here

# Test cases:
# safe_divide(10, 2)   -> 5.0
# safe_divide(10, 0)   -> None (prints error)
# safe_divide("10", 2) -> None (prints error)


# Exercise 2: Safe List Access
# TODO: Create a function that safely gets an item from list
# Handle: IndexError, TypeError
# Return default value on error

print("\n\nExercise 2: Safe List Access")
print("-" * 40)

def safe_get(lst, index, default=None):
    """Safely get item from list"""
    pass  # Your code here


# Exercise 3: Input Validation
# TODO: Create a function that gets a valid integer from user
# Keep asking until valid input received
# Handle: ValueError

print("\n\nExercise 3: Validated Input")
print("-" * 40)

def get_valid_integer(prompt, min_val=None, max_val=None):
    """Get valid integer input from user"""
    pass  # Your code here


# Exercise 4: Custom Exception
# TODO: Create a custom PasswordTooWeakError exception
# Create validate_password function that raises it
# Requirements: min 8 chars, has digit, has uppercase

print("\n\nExercise 4: Custom Password Exception")
print("-" * 40)

class PasswordTooWeakError(Exception):
    pass  # Your code here

def validate_password(password):
    """Validate password strength"""
    pass  # Your code here


# Exercise 5: Exception Logger
# TODO: Create a decorator that logs exceptions
# Should print exception type and message
# Then re-raise the exception

print("\n\nExercise 5: Exception Logger Decorator")
print("-" * 40)

def log_exceptions(func):
    """Decorator that logs exceptions"""
    pass  # Your code here
