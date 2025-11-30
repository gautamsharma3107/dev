"""
Day 6 - Sorting Exercises
==========================
Practice problems for sorting algorithms.
Try to solve each problem before looking at the solution.
"""

# ========== EXERCISE 1 ==========
print("=" * 50)
print("EXERCISE 1: Implement Merge Sort")
print("=" * 50)
print("""
Implement merge sort algorithm.

Example:
Input: [38, 27, 43, 3, 9, 82, 10]
Output: [3, 9, 10, 27, 38, 43, 82]
""")

def merge_sort(arr):
    """
    Sort array using merge sort.
    
    Args:
        arr: List of integers
    Returns:
        Sorted list
    """
    # YOUR CODE HERE
    pass

def merge(left, right):
    """
    Merge two sorted arrays.
    
    Args:
        left: First sorted array
        right: Second sorted array
    Returns:
        Merged sorted array
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [38, 27, 43, 3, 9, 82, 10]
# print(f"Sorted: {merge_sort(arr)}")

# ========== EXERCISE 2 ==========
print("\n" + "=" * 50)
print("EXERCISE 2: Implement Quick Sort (In-Place)")
print("=" * 50)
print("""
Implement quick sort algorithm in-place.

Example:
Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
""")

def quick_sort(arr, low=None, high=None):
    """
    Sort array using quick sort (in-place).
    
    Args:
        arr: List of integers (modified in place)
        low: Starting index
        high: Ending index
    Returns:
        Sorted array
    """
    # YOUR CODE HERE
    pass

def partition(arr, low, high):
    """
    Partition array around pivot.
    
    Args:
        arr: List of integers
        low: Starting index
        high: Ending index (pivot position)
    Returns:
        Final position of pivot
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [10, 7, 8, 9, 1, 5]
# quick_sort(arr)
# print(f"Sorted: {arr}")

# ========== EXERCISE 3 ==========
print("\n" + "=" * 50)
print("EXERCISE 3: Find Kth Largest Element")
print("=" * 50)
print("""
Find kth largest element using Quick Select.

Example:
Input: arr = [3, 2, 1, 5, 6, 4], k = 2
Output: 5 (2nd largest)
""")

def find_kth_largest(arr, k):
    """
    Find kth largest element.
    
    Args:
        arr: List of integers
        k: Position from largest (1-indexed)
    Returns:
        Kth largest element
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [3, 2, 1, 5, 6, 4]
# print(f"2nd largest: {find_kth_largest(arr, 2)}")
# print(f"4th largest: {find_kth_largest(arr, 4)}")

# ========== EXERCISE 4 ==========
print("\n" + "=" * 50)
print("EXERCISE 4: Merge Two Sorted Arrays")
print("=" * 50)
print("""
Merge sorted array nums2 into sorted array nums1.
nums1 has extra space at end.

Example:
Input: nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
Output: nums1 = [1,2,2,3,5,6]
""")

def merge_arrays(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 (in-place).
    
    Args:
        nums1: First sorted array with extra space
        m: Number of elements in nums1
        nums2: Second sorted array
        n: Number of elements in nums2
    Returns:
        Modified nums1
    """
    # YOUR CODE HERE
    pass

# Test
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# merge_arrays(nums1, 3, nums2, 3)
# print(f"Merged: {nums1}")

# ========== EXERCISE 5 ==========
print("\n" + "=" * 50)
print("EXERCISE 5: Sort by Custom Key")
print("=" * 50)
print("""
Sort objects by custom key using any sorting method.

Example:
Input: students = [("Alice", 85), ("Bob", 90), ("Charlie", 75)]
Sort by grade descending.
Output: [("Bob", 90), ("Alice", 85), ("Charlie", 75)]
""")

def sort_by_grade(students):
    """
    Sort students by grade in descending order.
    Implement using merge sort or quick sort.
    
    Args:
        students: List of (name, grade) tuples
    Returns:
        Sorted list by grade descending
    """
    # YOUR CODE HERE
    pass

# Test
# students = [("Alice", 85), ("Bob", 90), ("Charlie", 75), ("David", 95)]
# sorted_students = sort_by_grade(students)
# print(f"Sorted by grade: {sorted_students}")

# ========== SOLUTIONS ==========
print("\n" + "=" * 50)
print("SOLUTIONS (scroll down after attempting)")
print("=" * 50)
print("""


















""")

# Solution 1
def merge_solution(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_solution(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_solution(arr[:mid])
    right = merge_sort_solution(arr[mid:])
    return merge_solution(left, right)

# Solution 2
def partition_solution(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_solution(arr, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition_solution(arr, low, high)
        quick_sort_solution(arr, low, pi - 1)
        quick_sort_solution(arr, pi + 1, high)
    return arr

# Solution 3
def find_kth_largest_solution(arr, k):
    def quick_select(nums, k):
        if len(nums) == 1:
            return nums[0]
        
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x > pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        if k <= len(left):
            return quick_select(left, k)
        elif k <= len(left) + len(middle):
            return pivot
        else:
            return quick_select(right, k - len(left) - len(middle))
    
    return quick_select(arr, k)

# Solution 4
def merge_arrays_solution(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    return nums1

# Solution 5
def sort_by_grade_solution(students):
    def merge_by_grade(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][1] >= right[j][1]:  # Sort descending
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort_students(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_students(arr[:mid])
        right = merge_sort_students(arr[mid:])
        return merge_by_grade(left, right)
    
    return merge_sort_students(students)

# Verify solutions
print("Verifying solutions:")
print("-" * 30)

arr = [38, 27, 43, 3, 9, 82, 10]
print(f"Merge sort: {merge_sort_solution(arr)}")

arr = [10, 7, 8, 9, 1, 5]
quick_sort_solution(arr)
print(f"Quick sort: {arr}")

arr = [3, 2, 1, 5, 6, 4]
print(f"2nd largest: {find_kth_largest_solution(arr, 2)}")
print(f"4th largest: {find_kth_largest_solution(arr, 4)}")

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge_arrays_solution(nums1, 3, nums2, 3)
print(f"Merged arrays: {nums1}")

students = [("Alice", 85), ("Bob", 90), ("Charlie", 75), ("David", 95)]
sorted_students = sort_by_grade_solution(students)
print(f"Sorted by grade: {sorted_students}")

print("\n" + "=" * 50)
print("✅ Sorting Exercises - Complete!")
print("=" * 50)
