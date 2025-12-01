"""
Day 5 - Arrays and Lists
=========================
Learn: Core operations and patterns for arrays/lists

Key Concepts:
- Arrays are contiguous memory blocks
- Python lists are dynamic arrays
- Index-based access is O(1)
- Search is O(n) unless sorted
"""

# ========== ARRAY VS LIST BASICS ==========
print("=" * 50)
print("ARRAYS AND LISTS IN PYTHON")
print("=" * 50)

print("""
Python List Facts:
✅ Dynamic sizing (grows automatically)
✅ Can hold mixed types
✅ Implemented as dynamic arrays
✅ O(1) index access
✅ O(1) append (amortized)
❌ O(n) insert/delete at beginning

For typed arrays, use: from array import array
""")

# ========== LIST CREATION ==========
print("\n" + "=" * 50)
print("LIST CREATION")
print("=" * 50)

# Different ways to create lists
list1 = [1, 2, 3, 4, 5]
list2 = list(range(5))
list3 = [0] * 5
list4 = [i**2 for i in range(5)]
list5 = []

print(f"Literal:       {list1}")
print(f"From range:    {list2}")
print(f"Repeated:      {list3}")
print(f"Comprehension: {list4}")
print(f"Empty:         {list5}")

# ========== TIME COMPLEXITY OF OPERATIONS ==========
print("\n" + "=" * 50)
print("LIST OPERATIONS TIME COMPLEXITY")
print("=" * 50)

print("""
Operation              | Complexity | Example
-----------------------|------------|------------------
Access by index        | O(1)       | arr[i]
Assign by index        | O(1)       | arr[i] = x
Append                 | O(1)*      | arr.append(x)
Pop last               | O(1)       | arr.pop()
Pop at index           | O(n)       | arr.pop(i)
Insert at beginning    | O(n)       | arr.insert(0, x)
Insert at index        | O(n)       | arr.insert(i, x)
Delete by index        | O(n)       | del arr[i]
Check membership       | O(n)       | x in arr
Find index             | O(n)       | arr.index(x)
Length                 | O(1)       | len(arr)
Slice                  | O(k)       | arr[i:j]
Copy                   | O(n)       | arr.copy()
Sort                   | O(n log n) | arr.sort()

* amortized - occasional O(n) for resizing
""")

# ========== COMMON LIST OPERATIONS ==========
print("\n" + "=" * 50)
print("COMMON LIST OPERATIONS")
print("=" * 50)

arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {arr}")

# Access
print(f"\n-- Access --")
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")
print(f"Slice [2:5]: {arr[2:5]}")
print(f"Every other: {arr[::2]}")
print(f"Reversed: {arr[::-1]}")

# Modify
print(f"\n-- Modify --")
arr_copy = arr.copy()
arr_copy[0] = 100
print(f"After arr[0] = 100: {arr_copy}")

arr_copy.append(7)
print(f"After append(7): {arr_copy}")

arr_copy.insert(0, 0)
print(f"After insert(0, 0): {arr_copy}")

arr_copy.pop()
print(f"After pop(): {arr_copy}")

arr_copy.pop(0)
print(f"After pop(0): {arr_copy}")

# Search
print(f"\n-- Search --")
print(f"5 in arr: {5 in arr}")
print(f"Index of 5: {arr.index(5)}")
print(f"Count of 1: {arr.count(1)}")

# Sort
print(f"\n-- Sort --")
arr_copy = arr.copy()
arr_copy.sort()
print(f"Sorted: {arr_copy}")
arr_copy.sort(reverse=True)
print(f"Reverse sorted: {arr_copy}")

# ========== TWO-POINTER TECHNIQUE ==========
print("\n" + "=" * 50)
print("TWO-POINTER TECHNIQUE")
print("=" * 50)

print("""
Two pointers: Use two indices to traverse array
- One from start, one from end
- Both from start at different speeds
- Reduces O(n²) to O(n) for many problems
""")

# Example 1: Reverse array in-place
def reverse_array(arr):
    """Reverse array using two pointers - O(n) time, O(1) space"""
    arr = arr.copy()
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

arr = [1, 2, 3, 4, 5]
print(f"\nReverse {arr}: {reverse_array(arr)}")

# Example 2: Two sum (sorted array)
def two_sum_sorted(arr, target):
    """Find two numbers that add up to target - O(n)"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

arr = [1, 2, 3, 4, 6, 8, 9]
target = 10
result = two_sum_sorted(arr, target)
print(f"Two sum in {arr}, target={target}: indices {result}")
if result:
    print(f"  Values: {arr[result[0]]} + {arr[result[1]]} = {target}")

# Example 3: Remove duplicates from sorted array
def remove_duplicates(arr):
    """Remove duplicates in-place, return new length - O(n)"""
    if not arr:
        return 0
    
    arr = arr.copy()
    write_pointer = 1
    
    for read_pointer in range(1, len(arr)):
        if arr[read_pointer] != arr[read_pointer - 1]:
            arr[write_pointer] = arr[read_pointer]
            write_pointer += 1
    
    return write_pointer, arr[:write_pointer]

arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length, unique = remove_duplicates(arr)
print(f"\nRemove duplicates from {arr}")
print(f"  Unique elements: {unique}, length: {length}")

# ========== SLIDING WINDOW ==========
print("\n" + "=" * 50)
print("SLIDING WINDOW TECHNIQUE")
print("=" * 50)

print("""
Sliding window: Fixed or variable size window over array
- Useful for subarray problems
- O(n) instead of O(n²)
""")

# Example 1: Maximum sum of k consecutive elements
def max_sum_subarray(arr, k):
    """Find max sum of k consecutive elements - O(n)"""
    if len(arr) < k:
        return None
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]  # Remove left, add right
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"\nMax sum of {k} consecutive in {arr}: {max_sum_subarray(arr, k)}")

# Example 2: Find all averages of contiguous subarrays
def find_averages(arr, k):
    """Find average of all k-size windows - O(n)"""
    result = []
    window_sum = 0
    
    for i in range(len(arr)):
        window_sum += arr[i]
        
        if i >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[i - k + 1]
    
    return result

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(f"Averages of {k}-size windows in {arr}:")
print(f"  {find_averages(arr, k)}")

# ========== COMMON PATTERNS ==========
print("\n" + "=" * 50)
print("COMMON ARRAY PATTERNS")
print("=" * 50)

# Pattern 1: Find minimum/maximum
def find_min_max(arr):
    """Find min and max in single pass - O(n)"""
    if not arr:
        return None, None
    min_val = max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

arr = [3, 1, 4, 1, 5, 9, 2, 6]
min_v, max_v = find_min_max(arr)
print(f"\nFind min/max in {arr}: min={min_v}, max={max_v}")

# Pattern 2: Frequency count
def count_frequency(arr):
    """Count element frequencies - O(n)"""
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Frequency in {arr}: {count_frequency(arr)}")

# Pattern 3: Prefix sum
def prefix_sum(arr):
    """Calculate prefix sums - O(n)"""
    result = [0]
    for num in arr:
        result.append(result[-1] + num)
    return result

arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
print(f"\nPrefix sum of {arr}: {prefix}")
print(f"  Sum of indices 1-3: {prefix[4] - prefix[1]}")  # 2+3+4 = 9

# Pattern 4: Find missing number
def find_missing(arr, n):
    """Find missing number from 1 to n - O(n)"""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [1, 2, 4, 5, 6]  # Missing 3
n = 6
print(f"\nMissing number in {arr} (1 to {n}): {find_missing(arr, n)}")

# ========== MULTIDIMENSIONAL ARRAYS ==========
print("\n" + "=" * 50)
print("2D ARRAYS (MATRICES)")
print("=" * 50)

# Create 2D array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Access elements
print(f"\nElement at [1][2]: {matrix[1][2]}")  # 6

# Traverse row by row
print("\nRow-major traversal:")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
print()

# Traverse column by column
print("\nColumn-major traversal:")
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=" ")
print()

# Create n x m matrix filled with zeros
def create_matrix(rows, cols, val=0):
    """Create matrix filled with value"""
    return [[val for _ in range(cols)] for _ in range(rows)]

print(f"\n3x4 matrix of zeros:")
zero_matrix = create_matrix(3, 4)
for row in zero_matrix:
    print(f"  {row}")

# ========== PRACTICE PROBLEMS ==========
print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

print("""
Try these classic array problems:

1. Rotate Array: Rotate array by k positions
   [1,2,3,4,5], k=2 → [4,5,1,2,3]

2. Move Zeros: Move all zeros to end
   [0,1,0,3,12] → [1,3,12,0,0]

3. Find Duplicate: Find the duplicate in array
   [1,3,4,2,2] → 2

4. Maximum Subarray: Find contiguous subarray with max sum
   [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])
""")

print("\n" + "=" * 50)
print("✅ Arrays and Lists - Complete!")
print("=" * 50)
print("\nNext: Let's learn about Stacks! 🚀")
