"""
Day 1 - Operators
=================
Learn: Arithmetic, Comparison, Logical, Assignment, Bitwise, and Identity operators

Key Concepts:
- Operators perform operations on variables and values
- Different types for different purposes
- Understanding operator precedence is important
"""

# ========== ARITHMETIC OPERATORS ==========
print("=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")  # Rounds down
print(f"Modulus (a % b): {a % b}")  # Remainder
print(f"Exponent (a ** b): {a ** b}")  # Power

# ========== COMPARISON OPERATORS ==========
print("\n" + "=" * 50)
print("COMPARISON OPERATORS (Returns True/False)")
print("=" * 50)

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"Equal (x == y): {x == y}")
print(f"Not Equal (x != y): {x != y}")
print(f"Greater than (x > y): {x > y}")
print(f"Less than (x < y): {x < y}")
print(f"Greater or Equal (x >= y): {x >= y}")
print(f"Less or Equal (x <= y): {x <= y}")

# ========== LOGICAL OPERATORS ==========
print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"AND (p and q): {p and q}")  # Both must be True
print(f"OR (p or q): {p or q}")     # At least one must be True
print(f"NOT (!p): {not p}")         # Inverts the value

# Practical example
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"\nAge: {age}, Has License: {has_license}")
print(f"Can drive? {can_drive}")

# ========== ASSIGNMENT OPERATORS ==========
print("\n" + "=" * 50)
print("ASSIGNMENT OPERATORS")
print("=" * 50)

num = 10
print(f"Initial value: {num}")

num += 5  # num = num + 5
print(f"After += 5: {num}")

num -= 3  # num = num - 3
print(f"After -= 3: {num}")

num *= 2  # num = num * 2
print(f"After *= 2: {num}")

num /= 4  # num = num / 4
print(f"After /= 4: {num}")

num **= 2  # num = num ** 2
print(f"After **= 2: {num}")

# ========== IDENTITY OPERATORS ==========
print("\n" + "=" * 50)
print("IDENTITY OPERATORS")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

print(f"\nlist1 == list2: {list1 == list2}")  # Same values
print(f"list1 is list2: {list1 is list2}")    # Different objects
print(f"list1 is list3: {list1 is list3}")    # Same object

print(f"\nlist1 is not list2: {list1 is not list2}")

# ========== MEMBERSHIP OPERATORS ==========
print("\n" + "=" * 50)
print("MEMBERSHIP OPERATORS")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}")

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# ========== OPERATOR PRECEDENCE ==========
print("\n" + "=" * 50)
print("OPERATOR PRECEDENCE")
print("=" * 50)

result1 = 10 + 5 * 2  # Multiplication first
print(f"10 + 5 * 2 = {result1}")

result2 = (10 + 5) * 2  # Parentheses first
print(f"(10 + 5) * 2 = {result2}")

result3 = 10 ** 2 + 3 * 5  # Exponent, then multiplication, then addition
print(f"10 ** 2 + 3 * 5 = {result3}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Check if number is even or odd
number = 17
is_even = number % 2 == 0
print(f"Is {number} even? {is_even}")

# Calculate discount
price = 100
discount = 0.20
final_price = price - (price * discount)
print(f"\nOriginal Price: ${price}")
print(f"Discount: {discount * 100}%")
print(f"Final Price: ${final_price}")

# Check eligibility for voting
age = 16
is_citizen = True
can_vote = age >= 18 and is_citizen
print(f"\nAge: {age}, Citizen: {is_citizen}")
print(f"Can vote? {can_vote}")

print("\n" + "=" * 50)
print("✅ Operators - Complete!")
print("=" * 50)
