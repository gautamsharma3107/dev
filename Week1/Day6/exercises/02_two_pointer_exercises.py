"""
Day 6 - Two-Pointer Exercises
==============================
Practice problems for two-pointer technique.
Try to solve each problem before looking at the solution.
"""

# ========== EXERCISE 1 ==========
print("=" * 50)
print("EXERCISE 1: Pair with Target Sum")
print("=" * 50)
print("""
Given a sorted array, find a pair that sums to target.
Return indices of the pair.

Example:
Input: arr = [1, 2, 3, 4, 6], target = 6
Output: [1, 3] (arr[1] + arr[3] = 2 + 4 = 6)
""")

def pair_with_sum(arr, target):
    """
    Find indices of pair that sum to target.
    Array is sorted.
    
    Args:
        arr: Sorted list of integers
        target: Target sum
    Returns:
        List of two indices, or empty list if not found
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [1, 2, 3, 4, 6]
# print(f"Pair indices: {pair_with_sum(arr, 6)}")  # Expected: [1, 3]

# ========== EXERCISE 2 ==========
print("\n" + "=" * 50)
print("EXERCISE 2: Remove Duplicates from Sorted Array")
print("=" * 50)
print("""
Remove duplicates in-place from sorted array.
Return new length.

Example:
Input: [1, 1, 2, 2, 2, 3, 4, 4]
Output: 4 (array becomes [1, 2, 3, 4, ...])
""")

def remove_duplicates(arr):
    """
    Remove duplicates from sorted array in place.
    
    Args:
        arr: Sorted list (will be modified)
    Returns:
        New length after removing duplicates
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [1, 1, 2, 2, 2, 3, 4, 4]
# length = remove_duplicates(arr)
# print(f"New length: {length}, Array: {arr[:length]}")

# ========== EXERCISE 3 ==========
print("\n" + "=" * 50)
print("EXERCISE 3: Triplet Sum to Zero")
print("=" * 50)
print("""
Find all unique triplets that sum to zero.

Example:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
""")

def triplet_sum_zero(arr):
    """
    Find all unique triplets summing to zero.
    
    Args:
        arr: List of integers
    Returns:
        List of triplets [a, b, c] where a + b + c = 0
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [-3, 0, 1, 2, -1, 1, -2]
# print(f"Triplets: {triplet_sum_zero(arr)}")

# ========== EXERCISE 4 ==========
print("\n" + "=" * 50)
print("EXERCISE 4: Squaring a Sorted Array")
print("=" * 50)
print("""
Given sorted array with negatives, return squares in sorted order.

Example:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
""")

def sorted_squares(arr):
    """
    Return sorted squares of sorted array.
    
    Args:
        arr: Sorted list of integers (may have negatives)
    Returns:
        List of squares in sorted order
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [-2, -1, 0, 2, 3]
# print(f"Sorted squares: {sorted_squares(arr)}")

# ========== EXERCISE 5 ==========
print("\n" + "=" * 50)
print("EXERCISE 5: Dutch National Flag (Sort Colors)")
print("=" * 50)
print("""
Sort array with only 0s, 1s, and 2s in place.
Use three pointers.

Example:
Input: [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
""")

def sort_colors(arr):
    """
    Sort array containing 0s, 1s, and 2s in place.
    
    Args:
        arr: List containing only 0, 1, 2
    Returns:
        Sorted array (modified in place)
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [2, 0, 2, 1, 1, 0]
# sort_colors(arr)
# print(f"Sorted colors: {arr}")

# ========== SOLUTIONS ==========
print("\n" + "=" * 50)
print("SOLUTIONS (scroll down after attempting)")
print("=" * 50)
print("""


















""")

# Solution 1
def pair_with_sum_solution(arr, target):
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

# Solution 2
def remove_duplicates_solution(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1

# Solution 3
def triplet_sum_zero_solution(arr):
    arr.sort()
    triplets = []
    
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        left, right = i + 1, len(arr) - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return triplets

# Solution 4
def sorted_squares_solution(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    position = n - 1
    
    while left <= right:
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2
        if left_sq > right_sq:
            result[position] = left_sq
            left += 1
        else:
            result[position] = right_sq
            right -= 1
        position -= 1
    
    return result

# Solution 5
def sort_colors_solution(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# Verify solutions
print("Verifying solutions:")
print("-" * 30)

arr = [1, 2, 3, 4, 6]
print(f"Pair indices: {pair_with_sum_solution(arr, 6)}")

arr = [1, 1, 2, 2, 2, 3, 4, 4]
length = remove_duplicates_solution(arr)
print(f"Remove dups - Length: {length}, Array: {arr[:length]}")

arr = [-3, 0, 1, 2, -1, 1, -2]
print(f"Triplets summing to 0: {triplet_sum_zero_solution(arr)}")

arr = [-2, -1, 0, 2, 3]
print(f"Sorted squares: {sorted_squares_solution(arr)}")

arr = [2, 0, 2, 1, 1, 0]
sort_colors_solution(arr)
print(f"Sorted colors: {arr}")

print("\n" + "=" * 50)
print("✅ Two-Pointer Exercises - Complete!")
print("=" * 50)
