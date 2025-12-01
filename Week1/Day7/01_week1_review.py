"""
Day 7 - Week 1 Review
====================
Quick review of all concepts from Week 1

Topics:
- Variables, data types, operators (Day 1)
- Collections: lists, dicts, tuples, sets (Day 2)
- Functions and lambda (Day 3)
- File handling and exceptions (Day 4)
- Basic DSA: Big O, binary search, stacks, queues (Day 5)
- DSA patterns: two pointers, sliding window (Day 6)
"""

# ========== DAY 1 REVIEW: Variables & Basics ==========
print("=" * 60)
print("DAY 1 REVIEW: Variables, Data Types, Operators")
print("=" * 60)

# Variables and types
name = "Python"
version = 3.12
is_popular = True

print(f"Language: {name}, Version: {version}, Popular: {is_popular}")
print(f"Types: {type(name)}, {type(version)}, {type(is_popular)}")

# Type conversion
num_str = "42"
num_int = int(num_str)
print(f"String '{num_str}' to int: {num_int}")

# Operators
a, b = 10, 3
print(f"\nArithmetic: {a}+{b}={a+b}, {a}-{b}={a-b}, {a}*{b}={a*b}")
print(f"Division: {a}/{b}={a/b:.2f}, {a}//{b}={a//b}, {a}%{b}={a%b}")
print(f"Power: {a}**{b}={a**b}")

# Conditional
x = 15
size = "large" if x > 10 else "small"
print(f"\n{x} is {size}")

# ========== DAY 2 REVIEW: Collections ==========
print("\n" + "=" * 60)
print("DAY 2 REVIEW: Lists, Dictionaries, Sets, Tuples")
print("=" * 60)

# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(f"Fruits: {fruits}")
print(f"First: {fruits[0]}, Last: {fruits[-1]}, Slice: {fruits[1:3]}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]
print(f"\nSquares: {squares}")
print(f"Evens: {evens}")

# Dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"\nPerson: {person}")
print(f"Name: {person['name']}, Age: {person.get('age', 0)}")

# Iterate dict
for key, value in person.items():
    print(f"  {key}: {value}")

# Sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f"\nUnion: {set1 | set2}")
print(f"Intersection: {set1 & set2}")

# Tuple
coords = (10, 20)
x, y = coords
print(f"\nCoords: ({x}, {y})")

# ========== DAY 3 REVIEW: Functions ==========
print("\n" + "=" * 60)
print("DAY 3 REVIEW: Functions and Lambda")
print("=" * 60)

# Basic function
def greet(name, greeting="Hello"):
    """Return a greeting message"""
    return f"{greeting}, {name}!"

print(greet("World"))
print(greet("Python", "Welcome"))

# *args and **kwargs
def summarize(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

summarize(1, 2, 3, name="test", value=100)

# Lambda
square = lambda x: x ** 2
print(f"\nLambda square(5): {square(5)}")

# Built-in functions
numbers = [1, 2, 3, 4, 5]
print(f"\nNumbers: {numbers}")
print(f"Doubled: {list(map(lambda x: x*2, numbers))}")
print(f"Evens: {list(filter(lambda x: x%2==0, numbers))}")

# Enumerate
print("\nEnumerate:")
for i, num in enumerate(numbers, start=1):
    print(f"  {i}. {num}")

# Zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"  {name}: {age}")

# ========== DAY 4 REVIEW: File Handling & Exceptions ==========
print("\n" + "=" * 60)
print("DAY 4 REVIEW: File Handling & Exceptions")
print("=" * 60)

import json
import os

# Exception handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types"

print(f"10/2 = {safe_divide(10, 2)}")
print(f"10/0 = {safe_divide(10, 0)}")

# File handling with JSON
sample_data = {
    "tasks": [
        {"id": 1, "title": "Learn Python", "completed": True},
        {"id": 2, "title": "Build project", "completed": False}
    ]
}

# Write JSON
with open("sample_review.json", "w") as f:
    json.dump(sample_data, f, indent=2)
print("\n✅ Wrote sample_review.json")

# Read JSON
with open("sample_review.json", "r") as f:
    loaded_data = json.load(f)
print(f"Loaded: {loaded_data}")

# Cleanup
os.remove("sample_review.json")
print("✅ Cleaned up file")

# ========== DAY 5 REVIEW: Basic DSA ==========
print("\n" + "=" * 60)
print("DAY 5 REVIEW: Basic Data Structures & Algorithms")
print("=" * 60)

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Array: {sorted_nums}")
print(f"Binary search for 7: index {binary_search(sorted_nums, 7)}")
print(f"Binary search for 6: index {binary_search(sorted_nums, 6)}")

# Stack (LIFO)
print("\nStack operations:")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"  After pushes: {stack}")
print(f"  Pop: {stack.pop()}")
print(f"  After pop: {stack}")

# Queue (FIFO)
from collections import deque
print("\nQueue operations:")
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(f"  After enqueues: {list(queue)}")
print(f"  Dequeue: {queue.popleft()}")
print(f"  After dequeue: {list(queue)}")

# Hash Map (O(1) lookup)
print("\nHash Map (Dictionary):")
word_count = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"  Word counts: {word_count}")

# ========== DAY 6 REVIEW: DSA Patterns ==========
print("\n" + "=" * 60)
print("DAY 6 REVIEW: Two Pointers, Sliding Window")
print("=" * 60)

# Two Pointers - Two Sum (sorted array)
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []

sorted_arr = [1, 2, 4, 6, 8, 10]
print(f"Two Sum in {sorted_arr}, target=10: {two_sum_sorted(sorted_arr, 10)}")

# Sliding Window - Max sum of k elements
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

nums = [2, 1, 5, 1, 3, 2]
print(f"\nMax sum of 3 consecutive in {nums}: {max_sum_subarray(nums, 3)}")

# Linked List basics
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
    
    def display(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals)

ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)
print(f"\nLinked List: {ll.display()}")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("WEEK 1 REVIEW COMPLETE!")
print("=" * 60)
print("""
✅ Day 1: Variables, types, operators, conditionals, loops
✅ Day 2: Lists, dictionaries, sets, tuples, comprehensions
✅ Day 3: Functions, lambda, map, filter, zip, enumerate
✅ Day 4: File handling, JSON, CSV, exceptions
✅ Day 5: Big O, binary search, stacks, queues, hash maps
✅ Day 6: Two pointers, sliding window, linked lists

Now you're ready to build the Task Manager project!
""")
