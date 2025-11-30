"""
Day 2 - Tuples
==============
Learn: Tuple creation, operations, use cases

Key Concepts:
- Tuples are ordered, immutable collections
- Cannot be changed after creation
- Faster than lists
- Used for fixed data that shouldn't change
"""

# ========== TUPLE CREATION ==========
print("=" * 50)
print("TUPLE CREATION")
print("=" * 50)

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# Tuple with values
fruits = ("apple", "banana", "cherry")
print(f"Fruits: {fruits}")

# Single element tuple (need comma!)
single = (42,)  # Note the comma
not_tuple = (42)  # This is just an integer
print(f"Single element tuple: {single}, Type: {type(single)}")
print(f"Not a tuple: {not_tuple}, Type: {type(not_tuple)}")

# Tuple without parentheses
coordinates = 10, 20, 30
print(f"Without parentheses: {coordinates}")

# Mixed types
mixed = (1, "hello", 3.14, True)
print(f"Mixed types: {mixed}")

# From list
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(f"From list: {tuple_data}")

# ========== TUPLE INDEXING & SLICING ==========
print("\n" + "=" * 50)
print("TUPLE INDEXING & SLICING")
print("=" * 50)

colors = ("red", "green", "blue", "yellow", "purple")
print(f"Colors: {colors}")

# Indexing
print(f"\nFirst [0]: {colors[0]}")
print(f"Last [-1]: {colors[-1]}")

# Slicing
print(f"First 3 [0:3]: {colors[0:3]}")
print(f"Last 2 [-2:]: {colors[-2:]}")
print(f"Reverse [::-1]: {colors[::-1]}")

# ========== TUPLE IMMUTABILITY ==========
print("\n" + "=" * 50)
print("TUPLE IMMUTABILITY")
print("=" * 50)

point = (10, 20)
print(f"Point: {point}")

# This will cause an error:
# point[0] = 15  # TypeError: 'tuple' object does not support item assignment

# But you can create a new tuple
new_point = (15,) + point[1:]
print(f"New point: {new_point}")

# Convert to list, modify, convert back
temp_list = list(point)
temp_list[0] = 15
modified_point = tuple(temp_list)
print(f"Modified point: {modified_point}")

# ========== TUPLE METHODS ==========
print("\n" + "=" * 50)
print("TUPLE METHODS")
print("=" * 50)

numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers: {numbers}")

# Count occurrences
print(f"Count of 2: {numbers.count(2)}")

# Find index
print(f"Index of 4: {numbers.index(4)}")

# ========== TUPLE UNPACKING ==========
print("\n" + "=" * 50)
print("TUPLE UNPACKING")
print("=" * 50)

# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Coordinates: {coordinates}")
print(f"x={x}, y={y}, z={z}")

# Swap variables
a, b = 5, 10
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(f"\nfirst={first}, middle={middle}, last={last}")

# Ignore values
name, _, age = ("Alice", "ignored", 25)
print(f"name={name}, age={age}")

# ========== TUPLE VS LIST ==========
print("\n" + "=" * 50)
print("TUPLE VS LIST")
print("=" * 50)

import sys

# Memory comparison
list_ex = [1, 2, 3, 4, 5]
tuple_ex = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_ex)} bytes")
print(f"Tuple size: {sys.getsizeof(tuple_ex)} bytes")

print("""
Key Differences:
┌─────────────┬──────────────────────┬──────────────────────┐
│ Feature     │ List                 │ Tuple                │
├─────────────┼──────────────────────┼──────────────────────┤
│ Mutable     │ Yes                  │ No                   │
│ Syntax      │ [1, 2, 3]            │ (1, 2, 3)            │
│ Speed       │ Slower               │ Faster               │
│ Memory      │ More                 │ Less                 │
│ Use case    │ Dynamic data         │ Fixed data           │
└─────────────┴──────────────────────┴──────────────────────┘
""")

# ========== NAMED TUPLES ==========
print("\n" + "=" * 50)
print("NAMED TUPLES (Bonus)")
print("=" * 50)

from collections import namedtuple

# Create a named tuple class
Person = namedtuple("Person", ["name", "age", "city"])

# Create instances
person1 = Person("Alice", 30, "New York")
person2 = Person(name="Bob", age=25, city="London")

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")

# Access by name or index
print(f"\nPerson 1 name: {person1.name}")
print(f"Person 1 age: {person1[1]}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Return multiple values from function
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [5, 2, 8, 1, 9, 3]
minimum, maximum = get_min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

# Example 2: Coordinates and distance
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

p1 = (0, 0)
p2 = (3, 4)
distance = calculate_distance(p1, p2)
print(f"\nDistance from {p1} to {p2}: {distance}")

# Example 3: Dictionary with tuple keys
locations = {
    (0, 0): "Origin",
    (1, 0): "East",
    (0, 1): "North",
    (-1, 0): "West",
    (0, -1): "South"
}

print("\nLocation lookup:")
for coord, name in locations.items():
    print(f"  {coord}: {name}")

# Example 4: RGB colors (immutable makes sense)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

print(f"\nRGB Colors:")
print(f"  RED: {RED}")
print(f"  GREEN: {GREEN}")
print(f"  BLUE: {BLUE}")

print("\n" + "=" * 50)
print("✅ Tuples - Complete!")
print("=" * 50)
