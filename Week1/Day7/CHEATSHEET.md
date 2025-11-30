# Week 1 Complete Cheat Sheet

## Day 1: Variables, Data Types, Operators

### Variables
```python
name = "Python"         # str
age = 25               # int
height = 5.9           # float
is_student = True      # bool

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 100
```

### Type Conversion
```python
int("123")      # String to int
float("3.14")   # String to float
str(123)        # Int to string
bool(1)         # To boolean
```

### Operators
```python
# Arithmetic: + - * / // % **
# Comparison: == != > < >= <=
# Logical: and or not
# Assignment: = += -= *= /=
```

### Strings
```python
text = "Python"
text.upper()           # PYTHON
text.lower()           # python
text[0]                # P (first)
text[-1]               # n (last)
text[0:3]              # Pyt (slice)
len(text)              # 6
f"{name} is {age}"     # f-string
```

### If-Else
```python
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")

# Ternary
result = "yes" if x > 5 else "no"
```

### Loops
```python
for i in range(5):      # 0 to 4
    print(i)

for i in range(1, 6):   # 1 to 5
    print(i)

while count < 5:
    count += 1

# Control: break, continue
```

---

## Day 2: Collections

### Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")       # Add to end
fruits.insert(0, "apricot") # Insert at index
fruits.remove("banana")     # Remove by value
fruits.pop()                # Remove last
fruits.pop(0)               # Remove at index
len(fruits)                 # Length
fruits.sort()               # Sort in place
fruits.reverse()            # Reverse
```

### List Operations
```python
fruits[0]              # Access by index
fruits[1:3]            # Slice
"apple" in fruits      # Check membership
fruits + ["fig"]       # Concatenate
fruits * 2             # Repeat
```

### List Comprehensions
```python
squares = [x**2 for x in range(10)]
evens = [x for x in nums if x % 2 == 0]
```

### Dictionaries
```python
person = {"name": "Alice", "age": 25}
person["name"]              # Get value
person.get("age", 0)        # Get with default
person["city"] = "NYC"      # Add/update
del person["age"]           # Delete key
person.keys()               # All keys
person.values()             # All values
person.items()              # Key-value pairs
```

### Tuples (Immutable)
```python
coords = (10, 20)
x, y = coords          # Unpacking
```

### Sets (Unique, Unordered)
```python
nums = {1, 2, 3}
nums.add(4)
nums.remove(1)
nums.union({5, 6})
nums.intersection({2, 3})
```

---

## Day 3: Functions

### Basic Functions
```python
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def greet(name="World"):
    return f"Hello, {name}!"

# *args and **kwargs
def func(*args, **kwargs):
    print(args)    # Tuple
    print(kwargs)  # Dict
```

### Lambda Functions
```python
square = lambda x: x ** 2
add = lambda a, b: a + b
```

### Built-in Functions
```python
# map
squares = list(map(lambda x: x**2, nums))

# filter
evens = list(filter(lambda x: x%2==0, nums))

# zip
pairs = list(zip(names, ages))

# sorted
sorted_list = sorted(items, key=lambda x: x[1])

# enumerate
for i, item in enumerate(items):
    print(i, item)
```

---

## Day 4: File Handling & Exceptions

### File Modes
```python
'r'   # Read (default)
'w'   # Write (overwrites)
'a'   # Append
'x'   # Create (exclusive)
'r+'  # Read/Write
```

### Reading Files
```python
with open("file.txt", "r") as f:
    content = f.read()       # Entire file
    line = f.readline()      # One line
    lines = f.readlines()    # All lines as list
    
    for line in f:           # Line by line
        print(line.strip())
```

### Writing Files
```python
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.writelines(["a\n", "b\n"])
```

### JSON Files
```python
import json

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### CSV Files
```python
import csv

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])

# Write CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerows([["Alice", 25]])
```

### Exception Handling
```python
try:
    risky_code()
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Other: {e}")
else:
    print("Success!")
finally:
    print("Cleanup")

# Raise exception
raise ValueError("Invalid input")
```

### Common Exceptions
```python
ValueError       # Wrong value
TypeError        # Wrong type
KeyError         # Dict key not found
IndexError       # List index out of range
FileNotFoundError  # File doesn't exist
ZeroDivisionError  # Division by zero
```

---

## Day 5: Basic DSA

### Big O Notation
```python
O(1)      # Constant - dict lookup
O(log n)  # Logarithmic - binary search
O(n)      # Linear - single loop
O(n log n)# Log-linear - merge sort
O(n²)     # Quadratic - nested loops
```

### Binary Search
```python
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
```

### Stack (LIFO)
```python
stack = []
stack.append(item)   # Push
item = stack.pop()   # Pop
top = stack[-1]      # Peek
is_empty = len(stack) == 0
```

### Queue (FIFO)
```python
from collections import deque
queue = deque()
queue.append(item)      # Enqueue
item = queue.popleft()  # Dequeue
```

### Hash Map (Dictionary)
```python
# O(1) average lookup
cache = {}
cache[key] = value
value = cache.get(key, default)
```

---

## Day 6: DSA Patterns

### Two Pointers
```python
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
```

### Sliding Window
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### Linked List
```python
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
```

---

## Quick Patterns

### Check if palindrome
```python
def is_palindrome(s):
    return s == s[::-1]
```

### Factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

### Fibonacci
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### Find duplicates
```python
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
```

### Count frequency
```python
from collections import Counter
freq = Counter(items)
most_common = freq.most_common(3)
```

---

**Keep this handy for your Week 1 project and assessment!** 🚀
