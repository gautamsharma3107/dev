"""
Day 1 - Variables and Data Types
=================================
Learn: Variables, data types, type conversion

Key Concepts:
- Variables are containers for storing data
- Python has dynamic typing (no need to declare type)
- Main data types: int, float, str, bool, list, tuple, dict, set
"""

# ========== VARIABLES ==========
print("=" * 50)
print("VARIABLES")
print("=" * 50)

# Variable assignment
name = "Gautam"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Multiple assignment
x, y, z = 10, 20, 30
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# Same value to multiple variables
a = b = c = 100
print(f"Same value: a={a}, b={b}, c={c}")

# ========== DATA TYPES ==========
print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)

# Numeric types
integer_num = 42
float_num = 3.14159
complex_num = 3 + 4j

print(f"Integer: {integer_num}")
print(f"Float: {float_num}")
print(f"Complex: {complex_num}")

# String type
greeting = "Hello, World!"
multiline = """This is a
multiline
string"""

print(f"\nString: {greeting}")
print(f"Multiline:\n{multiline}")

# Boolean type
is_python_fun = True
is_boring = False

print(f"\nBoolean True: {is_python_fun}")
print(f"Boolean False: {is_boring}")

# ========== TYPE CONVERSION ==========
print("\n" + "=" * 50)
print("TYPE CONVERSION")
print("=" * 50)

# String to int
str_num = "123"
converted_int = int(str_num)
print(f"String '{str_num}' to int: {converted_int}, Type: {type(converted_int)}")

# Int to string
num = 456
converted_str = str(num)
print(f"Int {num} to string: '{converted_str}', Type: {type(converted_str)}")

# String to float
str_float = "3.14"
converted_float = float(str_float)
print(f"String '{str_float}' to float: {converted_float}, Type: {type(converted_float)}")

# Float to int (loses decimal)
float_val = 9.99
converted_int = int(float_val)
print(f"Float {float_val} to int: {converted_int} (decimal lost)")

# Int to bool
print(f"\nint(0) to bool: {bool(0)}")  # False
print(f"int(1) to bool: {bool(1)}")    # True
print(f"int(-5) to bool: {bool(-5)}")  # True (any non-zero is True)

# ========== CHECKING TYPES ==========
print("\n" + "=" * 50)
print("CHECKING TYPES")
print("=" * 50)

value = 42
print(f"Value: {value}")
print(f"Type: {type(value)}")
print(f"Is int? {isinstance(value, int)}")
print(f"Is str? {isinstance(value, str)}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE")
print("=" * 50)

# Calculate age in days
age_years = 25
days_per_year = 365
age_in_days = age_years * days_per_year

print(f"If you are {age_years} years old,")
print(f"you have lived approximately {age_in_days} days!")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

print("\n" + "=" * 50)
print("✅ Variables and Data Types - Complete!")
print("=" * 50)
