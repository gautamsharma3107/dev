"""
Day 5 - Binary Search
=====================
Learn: Efficient searching in sorted arrays

Key Concepts:
- Only works on SORTED arrays
- O(log n) time complexity
- Halves search space each step
- Much faster than linear search for large arrays
"""

# ========== WHAT IS BINARY SEARCH? ==========
print("=" * 50)
print("WHAT IS BINARY SEARCH?")
print("=" * 50)

print("""
Binary Search: Find element in SORTED array

Algorithm:
1. Look at middle element
2. If target == middle: Found!
3. If target < middle: Search left half
4. If target > middle: Search right half
5. Repeat until found or no elements left

Why O(log n)?
- Each step eliminates HALF the remaining elements
- n=1000 → only ~10 steps!
- n=1,000,000 → only ~20 steps!

Comparison:
- Linear search: n = 1000 → up to 1000 comparisons
- Binary search: n = 1000 → up to 10 comparisons
""")

# ========== VISUAL EXAMPLE ==========
print("\n" + "=" * 50)
print("VISUAL EXAMPLE")
print("=" * 50)

print("""
Find 7 in [1, 3, 5, 7, 9, 11, 13]

Step 1: [1, 3, 5, 7, 9, 11, 13]
                 ↑
        middle = 7, target = 7
        Found! Return index 3

Find 3 in [1, 3, 5, 7, 9, 11, 13]

Step 1: [1, 3, 5, 7, 9, 11, 13]
                 ↑
        middle = 7, target = 3
        3 < 7, search left half

Step 2: [1, 3, 5]
            ↑
        middle = 3, target = 3
        Found! Return index 1
""")

# ========== BASIC BINARY SEARCH ==========
print("\n" + "=" * 50)
print("BASIC BINARY SEARCH IMPLEMENTATION")
print("=" * 50)

def binary_search(arr, target):
    """
    Basic binary search - O(log n)
    Returns index of target, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # or mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

# Test
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Array: {arr}")

targets = [7, 1, 19, 8, 20]
for target in targets:
    idx = binary_search(arr, target)
    if idx != -1:
        print(f"  Found {target} at index {idx}")
    else:
        print(f"  {target} not found")

# ========== RECURSIVE BINARY SEARCH ==========
print("\n" + "=" * 50)
print("RECURSIVE BINARY SEARCH")
print("=" * 50)

def binary_search_recursive(arr, target, left, right):
    """Recursive version of binary search"""
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Helper function
def binary_search_rec(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# Test
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
print(f"Array: {arr}")
print(f"Find {target} (recursive): index {binary_search_rec(arr, target)}")

# ========== PYTHON'S BISECT MODULE ==========
print("\n" + "=" * 50)
print("PYTHON'S BISECT MODULE")
print("=" * 50)

import bisect

arr = [1, 3, 5, 7, 9, 11]
print(f"Array: {arr}")

# bisect_left: Find leftmost position to insert
pos = bisect.bisect_left(arr, 5)
print(f"bisect_left(5): {pos}")  # Position where 5 is or would be

# bisect_right: Find rightmost position to insert
pos = bisect.bisect_right(arr, 5)
print(f"bisect_right(5): {pos}")  # Position after last 5

# Check if element exists
def binary_search_bisect(arr, target):
    """Binary search using bisect"""
    pos = bisect.bisect_left(arr, target)
    if pos < len(arr) and arr[pos] == target:
        return pos
    return -1

print(f"Find 7 using bisect: index {binary_search_bisect(arr, 7)}")
print(f"Find 6 using bisect: index {binary_search_bisect(arr, 6)}")

# ========== FIND FIRST AND LAST OCCURRENCE ==========
print("\n" + "=" * 50)
print("FIND FIRST AND LAST OCCURRENCE")
print("=" * 50)

def find_first(arr, target):
    """Find first occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_last(arr, target):
    """Find last occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Test
arr = [1, 2, 2, 2, 2, 3, 4, 4, 5]
target = 2
print(f"Array: {arr}")
print(f"First occurrence of {target}: index {find_first(arr, target)}")
print(f"Last occurrence of {target}: index {find_last(arr, target)}")

# Count occurrences
first = find_first(arr, target)
last = find_last(arr, target)
count = last - first + 1 if first != -1 else 0
print(f"Count of {target}: {count}")

# ========== SEARCH INSERT POSITION ==========
print("\n" + "=" * 50)
print("SEARCH INSERT POSITION")
print("=" * 50)

def search_insert(arr, target):
    """
    Find index where target would be inserted
    to keep array sorted - O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # Insert position

arr = [1, 3, 5, 6]
print(f"Array: {arr}")
print(f"Insert position for 5: {search_insert(arr, 5)}")
print(f"Insert position for 2: {search_insert(arr, 2)}")
print(f"Insert position for 7: {search_insert(arr, 7)}")
print(f"Insert position for 0: {search_insert(arr, 0)}")

# ========== FIND PEAK ELEMENT ==========
print("\n" + "=" * 50)
print("FIND PEAK ELEMENT")
print("=" * 50)

def find_peak(arr):
    """
    Find any peak element (greater than neighbors)
    O(log n) using binary search
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            # Peak is on the right
            left = mid + 1
        else:
            # Peak is on the left (or at mid)
            right = mid
    
    return left

arr = [1, 2, 3, 1]
print(f"Array: {arr}")
print(f"Peak at index: {find_peak(arr)}, value: {arr[find_peak(arr)]}")

arr = [1, 2, 1, 3, 5, 6, 4]
print(f"Array: {arr}")
print(f"Peak at index: {find_peak(arr)}, value: {arr[find_peak(arr)]}")

# ========== SEARCH IN ROTATED SORTED ARRAY ==========
print("\n" + "=" * 50)
print("SEARCH IN ROTATED SORTED ARRAY")
print("=" * 50)

print("""
Rotated array: [4, 5, 6, 7, 0, 1, 2]
Original:      [0, 1, 2, 4, 5, 6, 7]
""")

def search_rotated(arr, target):
    """
    Search in rotated sorted array - O(log n)
    One half is always sorted!
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
print(f"Rotated array: {arr}")
print(f"Find 0: index {search_rotated(arr, 0)}")
print(f"Find 5: index {search_rotated(arr, 5)}")
print(f"Find 3: index {search_rotated(arr, 3)}")

# ========== FIND MINIMUM IN ROTATED ARRAY ==========
print("\n" + "=" * 50)
print("FIND MINIMUM IN ROTATED ARRAY")
print("=" * 50)

def find_min_rotated(arr):
    """Find minimum in rotated sorted array - O(log n)"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (or at mid)
            right = mid
    
    return arr[left]

arr = [4, 5, 6, 7, 0, 1, 2]
print(f"Rotated array: {arr}")
print(f"Minimum: {find_min_rotated(arr)}")

arr = [3, 4, 5, 1, 2]
print(f"Rotated array: {arr}")
print(f"Minimum: {find_min_rotated(arr)}")

# ========== BINARY SEARCH ON ANSWER ==========
print("\n" + "=" * 50)
print("BINARY SEARCH ON ANSWER")
print("=" * 50)

print("""
Binary search can find answers, not just array elements!

Example: Find square root of n (integer part)
- Search range: 0 to n
- Condition: mid * mid <= n
""")

def sqrt_int(n):
    """Find integer square root using binary search"""
    if n < 2:
        return n
    
    left, right = 1, n // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == n:
            return mid
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Largest integer where square <= n

print("Integer square roots:")
for n in [4, 8, 16, 25, 100]:
    print(f"  sqrt({n}) = {sqrt_int(n)}")

# ========== KOKO EATING BANANAS (CLASSIC) ==========
print("\n" + "=" * 50)
print("EXAMPLE: KOKO EATING BANANAS")
print("=" * 50)

print("""
Koko has piles of bananas. She can eat k bananas/hour.
Find minimum k to eat all bananas in h hours.

piles = [3, 6, 7, 11], h = 8
Each hour she picks a pile and eats k bananas.
""")

def min_eating_speed(piles, h):
    """Find minimum eating speed"""
    import math
    
    def can_finish(k):
        """Check if Koko can finish with speed k"""
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours <= h
    
    # Binary search on answer (speed k)
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

piles = [3, 6, 7, 11]
h = 8
print(f"Piles: {piles}, Hours: {h}")
print(f"Minimum eating speed: {min_eating_speed(piles, h)} bananas/hour")

# ========== BINARY SEARCH PATTERNS ==========
print("\n" + "=" * 50)
print("BINARY SEARCH PATTERNS")
print("=" * 50)

print("""
PATTERN 1: Find exact value
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1

PATTERN 2: Find leftmost/first valid
while left < right:
    mid = (left + right) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
return left

PATTERN 3: Find rightmost/last valid
while left < right:
    mid = (left + right + 1) // 2  # Round up!
    if condition(mid):
        left = mid
    else:
        right = mid - 1
return left
""")

# ========== WHEN TO USE BINARY SEARCH ==========
print("\n" + "=" * 50)
print("WHEN TO USE BINARY SEARCH")
print("=" * 50)

print("""
Use Binary Search when:
✅ Array is sorted
✅ Need O(log n) search
✅ Finding boundary/threshold
✅ Minimizing/maximizing answer
✅ Array has monotonic property

Signs you need binary search:
- "Sorted array" in problem
- "Find minimum/maximum that satisfies..."
- "Find first/last occurrence"
- Time complexity must be O(log n)

Common mistakes:
❌ Using on unsorted array
❌ Wrong boundary updates (off by one)
❌ Infinite loop (left >= right condition)
""")

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 50)
print("QUICK REFERENCE")
print("=" * 50)

print("""
| Problem Type               | Key Insight                |
|---------------------------|----------------------------|
| Find element              | Basic binary search        |
| First occurrence          | Keep searching left        |
| Last occurrence           | Keep searching right       |
| Insert position           | Return left when not found |
| Peak element              | Compare with neighbors     |
| Rotated array             | One half is always sorted  |
| Find answer               | Binary search on range     |
""")

print("\n" + "=" * 50)
print("✅ Binary Search - Complete!")
print("=" * 50)
print("\nYou've completed Day 5 DSA topics! 🎉")
print("Now try the exercises and mini projects!")
