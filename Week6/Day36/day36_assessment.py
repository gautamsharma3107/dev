"""
DAY 36 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 36 ASSESSMENT TEST - Advanced DSA for Interviews")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What is the time complexity of DFS traversal on a binary tree with n nodes?
a) O(log n)
b) O(n)
c) O(n²)
d) O(2^n)

Your answer: """)

print("""
Q2. In which traversal order does In-order DFS visit nodes?
a) Root → Left → Right
b) Left → Root → Right
c) Left → Right → Root
d) Right → Root → Left

Your answer: """)

print("""
Q3. What data structure is typically used for BFS traversal?
a) Stack
b) Queue
c) Heap
d) Hash Table

Your answer: """)

print("""
Q4. When should you use the Sliding Window technique?
a) When elements are sorted
b) When finding contiguous subarrays/substrings
c) When detecting cycles
d) When finding shortest path

Your answer: """)

print("""
Q5. What are the two main approaches to Dynamic Programming?
a) Recursion and Iteration
b) Memoization and Tabulation
c) Greedy and Divide-Conquer
d) BFS and DFS

Your answer: """)

print("""
Q6. In the Two Pointers technique for a sorted array, if the current sum is less 
than the target, what should you do?
a) Move left pointer right
b) Move right pointer left
c) Move both pointers
d) Return -1

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a function to perform level-order (BFS) traversal of a binary tree.
Return a flat list of node values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    # Your code here
    pass
""")

# Write your code here:
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    # Your code here
    pass


# Test your solution:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# Expected output: [1, 2, 3, 4, 5]

print("""
Q8. (2 points) Write a function to find the maximum sum of any contiguous subarray
using Kadane's algorithm (Dynamic Programming approach).

def max_subarray_sum(nums):
    # Your code here
    pass

# Test with: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Expected output: 6 (subarray [4, -1, 2, 1])
""")

# Write your code here:
def max_subarray_sum(nums):
    # Your code here
    pass


print("""
Q9. (2 points) Write a function that uses two pointers to find if there are 
two numbers in a SORTED array that add up to a target.
Return the indices of the two numbers.

def two_sum_sorted(arr, target):
    # Your code here
    pass

# Test with: arr = [2, 7, 11, 15], target = 9
# Expected output: [0, 1] (indices of 2 and 7)
""")

# Write your code here:
def two_sum_sorted(arr, target):
    # Your code here
    pass


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between Memoization (Top-Down) and 
Tabulation (Bottom-Up) approaches in Dynamic Programming.
When would you prefer one over the other?

Your answer:
""")

# Write your explanation here as comments:
# 



# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Understand WHY each answer is correct

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) O(n) - We visit each node exactly once
Q2: b) Left → Root → Right - In-order visits left subtree, then root, then right
Q3: b) Queue - BFS uses FIFO (First In First Out) queue
Q4: b) When finding contiguous subarrays/substrings
Q5: b) Memoization and Tabulation
Q6: a) Move left pointer right - To increase the sum

Section B (Coding):

Q7: Level Order Traversal
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

Q8: Maximum Subarray Sum (Kadane's Algorithm)
def max_subarray_sum(nums):
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

Q9: Two Sum Sorted
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

Section C:
Q10: Memoization vs Tabulation

MEMOIZATION (Top-Down):
- Uses recursion with caching
- Starts from the main problem and recursively solves subproblems
- Only computes subproblems that are actually needed
- Easier to implement if recursive solution is intuitive
- May have stack overflow for very deep recursion

TABULATION (Bottom-Up):
- Uses iteration
- Starts from smallest subproblems and builds up to the main problem
- Computes all subproblems (even ones not needed)
- More efficient (no recursion overhead)
- Easier to optimize space

When to use:
- Memoization: When not all subproblems are needed, or recursive solution is clearer
- Tabulation: When all subproblems will be needed, or to avoid recursion depth issues

SCORING:
- Section A: 6 points (1 each)
- Section B: 6 points (2 each)
- Section C: 2 points
- Total: 14 points
- Pass: 10+ points (70%)
"""
