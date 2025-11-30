"""
DAY 7 COMPREHENSIVE ASSESSMENT
==============================
Week 1 Final Test

Total: 50 points
Pass: 35+ points (70%)
Time: 30 minutes

Topics Covered:
- Variables, data types, operators
- Collections (lists, dicts, sets, tuples)
- Functions and lambda
- File handling
- Exception handling
- Basic DSA (Big O, binary search, stacks, queues)
- DSA Patterns (two pointers, sliding window)
"""

print("=" * 70)
print("              WEEK 1 COMPREHENSIVE ASSESSMENT")
print("=" * 70)
print("Total Points: 50 | Passing Score: 35 (70%) | Time: 30 minutes")
print("=" * 70)

# ============================================================
# SECTION A: Multiple Choice Questions (15 points)
# 1 point each - 15 questions
# ============================================================

print("\n" + "=" * 70)
print("SECTION A: Multiple Choice (15 points)")
print("=" * 70)

print("""
Q1. What is the output of: print(type([1, 2, 3]))
    a) <class 'tuple'>
    b) <class 'list'>
    c) <class 'array'>
    d) <class 'set'>
""")

print("""
Q2. Which of the following creates a dictionary?
    a) {1, 2, 3}
    b) [1, 2, 3]
    c) {"a": 1, "b": 2}
    d) (1, 2, 3)
""")

print("""
Q3. What is the time complexity of searching in a Python dictionary?
    a) O(n)
    b) O(log n)
    c) O(1) average
    d) O(n²)
""")

print("""
Q4. Which method removes and returns the last element of a list?
    a) remove()
    b) delete()
    c) pop()
    d) discard()
""")

print("""
Q5. What does this list comprehension produce: [x**2 for x in range(4)]
    a) [1, 4, 9, 16]
    b) [0, 1, 4, 9]
    c) [0, 2, 4, 6]
    d) [1, 2, 3, 4]
""")

print("""
Q6. Which file mode opens for writing and creates if doesn't exist?
    a) 'r'
    b) 'w'
    c) 'r+'
    d) 'x'
""")

print("""
Q7. What is the output of: lambda x: x * 2)(5)
    a) 10
    b) 25
    c) 52
    d) Error
""")

print("""
Q8. Which block always executes in try-except-finally?
    a) try
    b) except
    c) else
    d) finally
""")

print("""
Q9. What is the time complexity of binary search?
    a) O(n)
    b) O(log n)
    c) O(n log n)
    d) O(1)
""")

print("""
Q10. What data structure follows LIFO (Last In First Out)?
    a) Queue
    b) Stack
    c) Linked List
    d) Hash Map
""")

print("""
Q11. What does json.dump() do?
    a) Converts JSON string to Python object
    b) Writes Python object to JSON file
    c) Reads JSON file into Python object
    d) Validates JSON syntax
""")

print("""
Q12. Which is NOT a valid Python data type?
    a) int
    b) float
    c) char
    d) bool
""")

print("""
Q13. What pattern does this represent: left, right = 0, len(arr)-1
    a) Sliding window
    b) Two pointers
    c) Binary search
    d) Both b and c
""")

print("""
Q14. What is the output of: set([1, 2, 2, 3, 3, 3])
    a) [1, 2, 2, 3, 3, 3]
    b) {1, 2, 3}
    c) {1, 2, 2, 3, 3, 3}
    d) Error
""")

print("""
Q15. Which function is used to iterate with index in Python?
    a) zip()
    b) map()
    c) enumerate()
    d) filter()
""")

# ============================================================
# SECTION B: True/False Questions (5 points)
# 1 point each
# ============================================================

print("\n" + "=" * 70)
print("SECTION B: True/False (5 points)")
print("=" * 70)

print("""
Q16. Tuples are mutable in Python.
    True / False
""")

print("""
Q17. The 'with' statement automatically closes files.
    True / False
""")

print("""
Q18. Dictionary keys must be immutable.
    True / False
""")

print("""
Q19. A deque is more efficient than a list for queue operations.
    True / False
""")

print("""
Q20. Exception handling with try-except makes code slower.
    True / False
""")

# ============================================================
# SECTION C: Short Coding Challenges (20 points)
# 4 points each - 5 questions
# ============================================================

print("\n" + "=" * 70)
print("SECTION C: Short Coding Challenges (20 points)")
print("=" * 70)

print("""
Q21. (4 points) Write a function that takes a list of numbers and 
returns a dictionary with the count of even and odd numbers.

Example:
    Input: [1, 2, 3, 4, 5, 6]
    Output: {"even": 3, "odd": 3}
""")

# Write your code here:




print("""
Q22. (4 points) Write a function that finds two numbers in a SORTED 
array that add up to a target. Return their indices or [-1, -1].

Example:
    Input: arr=[1, 2, 4, 6, 10], target=8
    Output: [1, 3] (because 2 + 6 = 8)
""")

# Write your code here:




print("""
Q23. (4 points) Write a function that safely reads a JSON file and 
returns its content. If the file doesn't exist or is invalid, 
return an empty dictionary.

Example:
    safe_read_json("config.json") -> {"setting": "value"} or {}
""")

# Write your code here:




print("""
Q24. (4 points) Write a function using a sliding window to find 
the maximum sum of any 'k' consecutive elements in an array.

Example:
    Input: arr=[1, 4, 2, 10, 2, 3, 1, 0, 20], k=4
    Output: 24 (elements: 2, 10, 2, 10)
""")

# Write your code here:




print("""
Q25. (4 points) Write a function that checks if a string has 
balanced brackets using a stack. Support: (), [], {}

Example:
    Input: "([{}])"
    Output: True
    
    Input: "([)]"
    Output: False
""")

# Write your code here:




# ============================================================
# SECTION D: Application Question (10 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION D: Application Question (10 points)")
print("=" * 70)

print("""
Q26. (10 points) Design and implement a simple Note Manager that:

1. Stores notes with: id, title, content, created_at (2 points)
2. Add new note (2 points)
3. List all notes (2 points)
4. Save notes to JSON file (2 points)
5. Load notes from JSON file (2 points)

Include proper error handling and input validation.
""")

# Write your code here:




print("\n" + "=" * 70)
print("                    ASSESSMENT COMPLETE!")
print("=" * 70)

"""
============================================================
                        ANSWER KEY
============================================================

SECTION A: Multiple Choice (15 points)
--------------------------------------
Q1:  b) <class 'list'>
Q2:  c) {"a": 1, "b": 2}
Q3:  c) O(1) average
Q4:  c) pop()
Q5:  b) [0, 1, 4, 9]
Q6:  b) 'w'
Q7:  a) 10
Q8:  d) finally
Q9:  b) O(log n)
Q10: b) Stack
Q11: b) Writes Python object to JSON file
Q12: c) char
Q13: d) Both b and c
Q14: b) {1, 2, 3}
Q15: c) enumerate()

SECTION B: True/False (5 points)
--------------------------------
Q16: False (Tuples are immutable)
Q17: True
Q18: True
Q19: True (deque has O(1) for both ends)
Q20: False (negligible overhead in modern Python)

SECTION C: Coding Challenges (20 points)
----------------------------------------

Q21: Even/Odd Counter
def count_even_odd(numbers):
    result = {"even": 0, "odd": 0}
    for num in numbers:
        if num % 2 == 0:
            result["even"] += 1
        else:
            result["odd"] += 1
    return result

Q22: Two Sum (Sorted)
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
    return [-1, -1]

Q23: Safe JSON Read
import json

def safe_read_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

Q24: Max Sum Sliding Window
def max_sum_k(arr, k):
    if len(arr) < k:
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

Q25: Balanced Brackets
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

SECTION D: Application Question (10 points)
-------------------------------------------

import json
from datetime import datetime

class NoteManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = []
        self._id_counter = 0
        self.load()
    
    def add(self, title, content):
        if not title:
            raise ValueError("Title required")
        
        self._id_counter += 1
        note = {
            "id": self._id_counter,
            "title": title,
            "content": content,
            "created_at": datetime.now().isoformat()
        }
        self.notes.append(note)
        return note
    
    def list_all(self):
        return self.notes
    
    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.notes, f, indent=2)
            return True
        except IOError:
            return False
    
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.notes = json.load(f)
                if self.notes:
                    self._id_counter = max(n["id"] for n in self.notes)
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = []

============================================================
                     SCORING GUIDE
============================================================

Section A: 15 points (1 point each)
Section B: 5 points (1 point each)
Section C: 20 points (4 points each)
Section D: 10 points

Total: 50 points
Passing Score: 35 points (70%)

Grading:
- 45-50: Excellent! Ready for Week 2
- 35-44: Good! Review weak areas
- 25-34: Needs Improvement - Review and retest
- Below 25: Review entire week

============================================================
"""
