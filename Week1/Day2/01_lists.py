"""
Day 2 - Lists
=============
Learn: List creation, operations, methods, slicing

Key Concepts:
- Lists are ordered, mutable collections
- Can contain mixed data types
- Support indexing, slicing, and iteration
- Rich set of built-in methods
"""

# ========== LIST CREATION ==========
print("=" * 50)
print("LIST CREATION")
print("=" * 50)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with values
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# Mixed data types
mixed = [1, "hello", 3.14, True, None]
print(f"Mixed types: {mixed}")

# List from range
numbers = list(range(1, 6))
print(f"Numbers from range: {numbers}")

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")

# ========== LIST INDEXING ==========
print("\n" + "=" * 50)
print("LIST INDEXING")
print("=" * 50)

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")

# Positive indexing
print(f"\nFirst element [0]: {colors[0]}")
print(f"Third element [2]: {colors[2]}")

# Negative indexing
print(f"\nLast element [-1]: {colors[-1]}")
print(f"Second last [-2]: {colors[-2]}")

# ========== LIST SLICING ==========
print("\n" + "=" * 50)
print("LIST SLICING [start:end:step]")
print("=" * 50)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Numbers: {nums}")

print(f"\nFirst 5 [0:5]: {nums[0:5]}")
print(f"Last 3 [-3:]: {nums[-3:]}")
print(f"Middle [3:7]: {nums[3:7]}")
print(f"Every 2nd [::2]: {nums[::2]}")
print(f"Reverse [::-1]: {nums[::-1]}")
print(f"Odd indices [1::2]: {nums[1::2]}")

# ========== LIST MODIFICATION ==========
print("\n" + "=" * 50)
print("LIST MODIFICATION")
print("=" * 50)

animals = ["cat", "dog", "bird"]
print(f"Original: {animals}")

# Change element
animals[1] = "fish"
print(f"After change [1]: {animals}")

# Add element - append
animals.append("rabbit")
print(f"After append: {animals}")

# Add element - insert at position
animals.insert(1, "hamster")
print(f"After insert at [1]: {animals}")

# Add multiple elements
animals.extend(["lion", "tiger"])
print(f"After extend: {animals}")

# Remove by value
animals.remove("cat")
print(f"After remove 'cat': {animals}")

# Remove by index
removed = animals.pop(2)
print(f"Popped element: {removed}")
print(f"After pop [2]: {animals}")

# Remove last element
last = animals.pop()
print(f"Popped last: {last}")
print(f"After pop(): {animals}")

# Clear list
copy_animals = animals.copy()
copy_animals.clear()
print(f"After clear: {copy_animals}")

# ========== LIST METHODS ==========
print("\n" + "=" * 50)
print("LIST METHODS")
print("=" * 50)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Numbers: {numbers}")

# Count occurrences
print(f"\nCount of 5: {numbers.count(5)}")
print(f"Count of 1: {numbers.count(1)}")

# Find index
print(f"Index of 9: {numbers.index(9)}")

# Sort (modifies original)
numbers.sort()
print(f"After sort: {numbers}")

# Sort descending
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Reverse
numbers.reverse()
print(f"After reverse: {numbers}")

# ========== LIST FUNCTIONS ==========
print("\n" + "=" * 50)
print("BUILT-IN FUNCTIONS WITH LISTS")
print("=" * 50)

nums = [10, 25, 5, 30, 15]
print(f"Numbers: {nums}")

print(f"\nlen(nums): {len(nums)}")
print(f"max(nums): {max(nums)}")
print(f"min(nums): {min(nums)}")
print(f"sum(nums): {sum(nums)}")
print(f"Average: {sum(nums)/len(nums)}")

# Sorted (returns new list)
print(f"\nsorted(nums): {sorted(nums)}")
print(f"Original unchanged: {nums}")

# ========== LIST COPYING ==========
print("\n" + "=" * 50)
print("LIST COPYING")
print("=" * 50)

original = [1, 2, 3, 4, 5]

# Wrong way (reference copy)
wrong_copy = original
wrong_copy[0] = 999
print(f"Original after reference change: {original}")

# Reset
original = [1, 2, 3, 4, 5]

# Correct ways to copy
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

copy1[0] = 111
print(f"\nOriginal after copy change: {original}")
print(f"Modified copy: {copy1}")

# ========== LIST ITERATION ==========
print("\n" + "=" * 50)
print("LIST ITERATION")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]

# Simple iteration
print("Simple loop:")
for fruit in fruits:
    print(f"  - {fruit}")

# With index using enumerate
print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# With enumerate starting at 1
print("\nEnumerate from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# ========== LIST MEMBERSHIP ==========
print("\n" + "=" * 50)
print("LIST MEMBERSHIP")
print("=" * 50)

languages = ["Python", "Java", "JavaScript", "C++"]
print(f"Languages: {languages}")

print(f"\n'Python' in languages: {'Python' in languages}")
print(f"'Ruby' in languages: {'Ruby' in languages}")
print(f"'Ruby' not in languages: {'Ruby' not in languages}")

# ========== NESTED LISTS ==========
print("\n" + "=" * 50)
print("NESTED LISTS (2D Lists)")
print("=" * 50)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Access elements
print(f"\nElement at [0][0]: {matrix[0][0]}")
print(f"Element at [1][2]: {matrix[1][2]}")
print(f"Middle row: {matrix[1]}")

# Iterate with indices
print("\nAll elements:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"  [{i}][{j}] = {matrix[i][j]}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Shopping cart
cart = []
cart.append({"item": "Apple", "price": 1.50, "qty": 4})
cart.append({"item": "Milk", "price": 3.00, "qty": 2})
cart.append({"item": "Bread", "price": 2.50, "qty": 1})

print("Shopping Cart:")
total = 0
for item in cart:
    subtotal = item["price"] * item["qty"]
    total += subtotal
    print(f"  {item['item']}: ${item['price']} x {item['qty']} = ${subtotal:.2f}")
print(f"Total: ${total:.2f}")

# Example 2: Find duplicates
numbers = [1, 2, 3, 2, 4, 3, 5, 1]
seen = []
duplicates = []

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.append(num)

print(f"\nNumbers: {numbers}")
print(f"Duplicates: {duplicates}")

# Example 3: Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)

print(f"\nNested: {nested}")
print(f"Flattened: {flat}")

print("\n" + "=" * 50)
print("✅ Lists - Complete!")
print("=" * 50)
