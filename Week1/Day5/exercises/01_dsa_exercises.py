"""
EXERCISES: Data Structures & Algorithms
========================================
Complete all 3 exercises below
These are classic DSA problems!
"""

# ============================================================
# Exercise 1: Valid Parentheses (Easy)
# ============================================================
print("=" * 60)
print("Exercise 1: Valid Parentheses")
print("=" * 60)

print("""
Given a string containing just '(', ')', '{', '}', '[', ']',
determine if the input string has valid (balanced) brackets.

Examples:
- "()" → True
- "()[]{}" → True
- "(]" → False
- "([)]" → False
- "{[]}" → True

Hint: Use a stack!
""")

def is_valid(s):
    """
    Check if brackets are valid/balanced
    
    Args:
        s: String containing only brackets
    
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement using a stack
    pass


# Test cases
test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("((()))", True),
    ("((()", False),
]

print("\nTest your solution:")
for s, expected in test_cases:
    result = is_valid(s)
    status = "✅" if result == expected else "❌"
    print(f"  {status} is_valid('{s}') = {result} (expected {expected})")


# ============================================================
# Exercise 2: Two Sum (Easy-Medium)
# ============================================================
print("\n" + "=" * 60)
print("Exercise 2: Two Sum")
print("=" * 60)

print("""
Given an array of integers and a target, return indices of 
two numbers that add up to the target.

Assume exactly one solution exists. Don't use same element twice.

Examples:
- nums = [2,7,11,15], target = 9 → [0, 1] (2 + 7 = 9)
- nums = [3,2,4], target = 6 → [1, 2] (2 + 4 = 6)
- nums = [3,3], target = 6 → [0, 1] (3 + 3 = 6)

Requirements:
- O(n) time complexity using hash map
- O(n) space complexity

Hint: For each number, check if (target - number) was seen before.
""")

def two_sum(nums, target):
    """
    Find two numbers that add up to target
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices
    """
    # TODO: Implement using a hash map for O(n) solution
    pass


# Test cases
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 2, 3, 4, 5], 9, [3, 4]),
]

print("\nTest your solution:")
for nums, target, expected in test_cases:
    result = two_sum(nums, target)
    # Check if result is valid (order might differ)
    is_correct = result is not None and sorted(result) == sorted(expected)
    status = "✅" if is_correct else "❌"
    print(f"  {status} two_sum({nums}, {target}) = {result} (expected {expected})")


# ============================================================
# Exercise 3: Binary Search Variants (Medium)
# ============================================================
print("\n" + "=" * 60)
print("Exercise 3: Binary Search Variants")
print("=" * 60)

print("""
Implement these binary search variants:

Part A: Find the first occurrence of target
Part B: Find the last occurrence of target  
Part C: Count occurrences of target

All should be O(log n) time!

Example array: [1, 2, 2, 2, 3, 4, 4, 5]
- First occurrence of 2: index 1
- Last occurrence of 2: index 3
- Count of 2: 3
""")

def find_first_occurrence(arr, target):
    """
    Find the first (leftmost) occurrence of target
    
    Args:
        arr: Sorted list of integers
        target: Value to find
    
    Returns:
        Index of first occurrence, or -1 if not found
    """
    # TODO: Implement binary search to find FIRST occurrence
    pass


def find_last_occurrence(arr, target):
    """
    Find the last (rightmost) occurrence of target
    
    Args:
        arr: Sorted list of integers
        target: Value to find
    
    Returns:
        Index of last occurrence, or -1 if not found
    """
    # TODO: Implement binary search to find LAST occurrence
    pass


def count_occurrences(arr, target):
    """
    Count how many times target appears in sorted array
    
    Args:
        arr: Sorted list of integers
        target: Value to count
    
    Returns:
        Count of occurrences
    """
    # TODO: Use find_first and find_last to count
    # Hint: count = last - first + 1 (if found)
    pass


# Test cases
arr = [1, 2, 2, 2, 3, 4, 4, 5]
print(f"\nTest array: {arr}")

print("\nPart A - First occurrence:")
tests_first = [(2, 1), (4, 5), (5, 7), (6, -1)]
for target, expected in tests_first:
    result = find_first_occurrence(arr, target)
    status = "✅" if result == expected else "❌"
    print(f"  {status} find_first({target}) = {result} (expected {expected})")

print("\nPart B - Last occurrence:")
tests_last = [(2, 3), (4, 6), (5, 7), (6, -1)]
for target, expected in tests_last:
    result = find_last_occurrence(arr, target)
    status = "✅" if result == expected else "❌"
    print(f"  {status} find_last({target}) = {result} (expected {expected})")

print("\nPart C - Count occurrences:")
tests_count = [(2, 3), (4, 2), (5, 1), (6, 0)]
for target, expected in tests_count:
    result = count_occurrences(arr, target)
    status = "✅" if result == expected else "❌"
    print(f"  {status} count({target}) = {result} (expected {expected})")


# ============================================================
# BONUS: Next Greater Element
# ============================================================
print("\n" + "=" * 60)
print("BONUS Exercise: Next Greater Element")
print("=" * 60)

print("""
For each element, find the next greater element to its right.
If no greater element exists, use -1.

Example:
- Input:  [4, 5, 2, 10, 8]
- Output: [5, 10, 10, -1, -1]

Explanation:
- 4 → 5 (next greater)
- 5 → 10 (next greater)
- 2 → 10 (next greater)
- 10 → -1 (no greater element to right)
- 8 → -1 (no greater element to right)

Challenge: Solve in O(n) using a stack!
""")

def next_greater_element(arr):
    """
    Find next greater element for each position
    
    Args:
        arr: List of integers
    
    Returns:
        List where result[i] is the next greater element for arr[i]
    """
    # TODO: Implement using a stack for O(n) solution
    pass


# Test cases
test_cases = [
    ([4, 5, 2, 10, 8], [5, 10, 10, -1, -1]),
    ([1, 2, 3, 4], [2, 3, 4, -1]),
    ([4, 3, 2, 1], [-1, -1, -1, -1]),
    ([1], [-1]),
]

print("\nTest your solution:")
for arr, expected in test_cases:
    result = next_greater_element(arr)
    status = "✅" if result == expected else "❌"
    print(f"  {status} next_greater({arr}) = {result}")
    if result != expected:
        print(f"      Expected: {expected}")


print("\n" + "=" * 60)
print("Exercises Complete! Check your solutions above.")
print("=" * 60)
