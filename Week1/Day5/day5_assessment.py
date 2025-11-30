"""
DAY 5 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 5 ASSESSMENT - Essential DSA")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What is the time complexity of binary search?
a) O(n)
b) O(log n)
c) O(n²)
d) O(1)

Your answer: """)

print("""
Q2. Which data structure uses LIFO (Last In, First Out)?
a) Queue
b) Array
c) Stack
d) Hash Map

Your answer: """)

print("""
Q3. What is the average time complexity for dictionary lookup in Python?
a) O(n)
b) O(log n)
c) O(1)
d) O(n²)

Your answer: """)

print("""
Q4. Which data structure is best for BFS (Breadth-First Search)?
a) Stack
b) Queue
c) Array
d) Binary Tree

Your answer: """)

print("""
Q5. What happens when you use list.pop(0) in Python?
a) O(1) - removes first element instantly
b) O(n) - shifts all remaining elements
c) O(log n) - uses binary search
d) Raises an error

Your answer: """)

print("""
Q6. What is the time complexity of this code?
    for i in range(n):
        for j in range(n):
            print(i, j)

a) O(n)
b) O(log n)
c) O(n²)
d) O(2n)

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Implement a function to check if parentheses
    are balanced. Use a stack.
    
    Input: "([{}])"  → True
    Input: "([)]"    → False
""")

# Write your code here:
def is_balanced(s):
    pass  # Your implementation




print("""
Q8. (2 points) Implement binary search to find a target
    in a sorted array. Return index or -1 if not found.
    
    Input: arr=[1,3,5,7,9], target=5 → 2
    Input: arr=[1,3,5,7,9], target=6 → -1
""")

# Write your code here:
def binary_search(arr, target):
    pass  # Your implementation




print("""
Q9. (2 points) Find two numbers in an array that add up to 
    the target. Return their indices using a hash map.
    Use O(n) time complexity.
    
    Input: nums=[2,7,11,15], target=9 → [0, 1]
""")

# Write your code here:
def two_sum(nums, target):
    pass  # Your implementation




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain when you would use:
     a) A Stack vs a Queue
     b) Give one real-world example of each

Your answer:
""")

# Write your explanation here as comments:
#




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) O(log n)
Q2: c) Stack
Q3: c) O(1)
Q4: b) Queue
Q5: b) O(n) - shifts all remaining elements
Q6: c) O(n²)

Section B:
Q7:
def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

Q8:
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

Q9:
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

Section C:
Q10:
a) Stack (LIFO) vs Queue (FIFO):
   - Use Stack when you need to process in reverse order,
     or when the most recent item should be handled first.
   - Use Queue when you need first-come-first-served order,
     or when items should be processed in the order received.

b) Real-world examples:
   - Stack: Browser back button (most recent page first),
     Undo feature in text editors
   - Queue: Print queue (first document sent prints first),
     Customer service line, task scheduling
"""
