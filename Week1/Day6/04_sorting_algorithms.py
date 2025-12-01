"""
Day 6 - Sorting Algorithms
==========================
Learn: Merge Sort and Quick Sort implementations

Key Concepts:
- Divide and Conquer approach
- Time complexity analysis
- When to use which algorithm
"""

# ========== INTRODUCTION ==========
print("=" * 50)
print("SORTING ALGORITHMS")
print("=" * 50)

print("""
Why Learn Sorting?
- Fundamental algorithms in computer science
- Basis for many other algorithms
- Common interview questions
- Helps understand divide and conquer

Algorithms Covered:
1. Merge Sort - O(n log n), stable, extra space
2. Quick Sort - O(n log n) average, in-place

Comparison:
| Property      | Merge Sort | Quick Sort |
|---------------|------------|------------|
| Best Case     | O(n log n) | O(n log n) |
| Average Case  | O(n log n) | O(n log n) |
| Worst Case    | O(n log n) | O(n²)      |
| Space         | O(n)       | O(log n)   |
| Stable        | Yes        | No         |
| In-place      | No         | Yes        |
""")

# ========== MERGE SORT ==========
print("\n" + "=" * 50)
print("MERGE SORT")
print("=" * 50)

print("""
Merge Sort Algorithm:
1. Divide array into two halves
2. Recursively sort each half
3. Merge the two sorted halves

Key Properties:
- Divide and Conquer
- Stable (preserves order of equal elements)
- Not in-place (requires extra space)
- Consistent O(n log n) time
""")

def merge_sort(arr):
    """
    Merge Sort implementation.
    Time: O(n log n), Space: O(n)
    
    Returns a new sorted array.
    """
    # Base case: array of 0 or 1 element is sorted
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Conquer (recursively sort)
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combine (merge sorted halves)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    """
    result = []
    i = j = 0
    
    # Compare and add smaller element
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Demo
print("\nMerge Sort Demo:")
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted:   {sorted_arr}")

# Step by step visualization
print("\nStep-by-Step Visualization:")

def merge_sort_visual(arr, depth=0):
    """Visual merge sort with step printing."""
    indent = "  " * depth
    print(f"{indent}Sorting: {arr}")
    
    if len(arr) <= 1:
        print(f"{indent}Return: {arr}")
        return arr
    
    mid = len(arr) // 2
    print(f"{indent}Split at index {mid}")
    
    left = merge_sort_visual(arr[:mid], depth + 1)
    right = merge_sort_visual(arr[mid:], depth + 1)
    
    merged = merge(left, right)
    print(f"{indent}Merged {left} + {right} = {merged}")
    return merged

small_arr = [38, 27, 43, 3]
print(f"\nSorting: {small_arr}")
print("-" * 40)
result = merge_sort_visual(small_arr)
print("-" * 40)
print(f"Final: {result}")

# ========== QUICK SORT ==========
print("\n" + "=" * 50)
print("QUICK SORT")
print("=" * 50)

print("""
Quick Sort Algorithm:
1. Choose a pivot element
2. Partition: move smaller elements left, larger right
3. Recursively sort partitions

Key Properties:
- Divide and Conquer
- Not stable
- In-place (no extra array needed)
- O(n log n) average, O(n²) worst case
- Pivot selection affects performance
""")

def quick_sort(arr):
    """
    Quick Sort implementation (creates new array).
    Time: O(n log n) average, O(n²) worst
    Space: O(n) for this implementation
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    
    # Partition into three lists
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Demo
print("\nQuick Sort Demo (Simple Version):")
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
sorted_arr = quick_sort(arr)
print(f"Sorted:   {sorted_arr}")

# In-place Quick Sort
print("\nIn-Place Quick Sort:")

def quick_sort_inplace(arr, low=None, high=None):
    """
    In-place Quick Sort implementation.
    Time: O(n log n) average, Space: O(log n) stack
    """
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index
        pivot_idx = partition(arr, low, high)
        
        # Recursively sort partitions
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)
    
    return arr

def partition(arr, low, high):
    """
    Partition array around pivot (last element).
    Returns index of pivot in sorted position.
    """
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
quick_sort_inplace(arr)
print(f"Sorted:   {arr}")

# Step by step visualization
print("\nStep-by-Step Visualization:")

def partition_visual(arr, low, high, depth=0):
    """Visual partition with step printing."""
    indent = "  " * depth
    pivot = arr[high]
    print(f"{indent}Partition [{low}:{high}]: {arr[low:high+1]}, pivot={pivot}")
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"{indent}After partition: {arr[low:high+1]}, pivot at index {i+1}")
    return i + 1

def quick_sort_visual(arr, low, high, depth=0):
    """Visual quick sort with step printing."""
    if low < high:
        pivot_idx = partition_visual(arr, low, high, depth)
        quick_sort_visual(arr, low, pivot_idx - 1, depth + 1)
        quick_sort_visual(arr, pivot_idx + 1, high, depth + 1)

small_arr = [10, 7, 8, 9, 1, 5]
print(f"\nSorting: {small_arr}")
print("-" * 40)
quick_sort_visual(small_arr, 0, len(small_arr) - 1)
print("-" * 40)
print(f"Final: {small_arr}")

# ========== PIVOT SELECTION STRATEGIES ==========
print("\n" + "=" * 50)
print("PIVOT SELECTION STRATEGIES")
print("=" * 50)

print("""
Pivot Selection affects performance:

1. Last Element (implemented above)
   - Simple but poor for sorted arrays
   - Worst case: O(n²) on sorted input

2. First Element
   - Same issues as last element

3. Middle Element
   - Better average performance
   - Avoids worst case on sorted arrays

4. Random Element
   - Good average case guarantee
   - Randomizes worst case

5. Median of Three
   - Choose median of first, middle, last
   - Best practical choice
""")

def quick_sort_median3(arr, low=None, high=None):
    """
    Quick Sort with median-of-three pivot selection.
    """
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Median of three pivot selection
        mid = (low + high) // 2
        
        # Sort low, mid, high
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        
        # Use middle as pivot (move to high-1)
        arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
        pivot = arr[high - 1]
        
        # Partition
        i = low
        j = high - 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        
        arr[i], arr[high - 1] = arr[high - 1], arr[i]
        
        quick_sort_median3(arr, low, i - 1)
        quick_sort_median3(arr, i + 1, high)
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90, 45, 67, 33]
print(f"\nMedian-of-Three Quick Sort:")
print(f"Original: {arr}")
quick_sort_median3(arr)
print(f"Sorted:   {arr}")

# ========== COMPARISON AND ANALYSIS ==========
print("\n" + "=" * 50)
print("COMPARISON AND ANALYSIS")
print("=" * 50)

import time
import random

def measure_time(sort_func, arr):
    """Measure sorting time."""
    arr_copy = arr.copy()
    start = time.time()
    sort_func(arr_copy)
    return time.time() - start

# Generate test arrays
sizes = [100, 500, 1000]
print("\nPerformance Comparison (seconds):")
print("-" * 50)
print(f"{'Size':<10} {'Merge Sort':<15} {'Quick Sort':<15}")
print("-" * 50)

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    
    merge_time = measure_time(merge_sort, arr)
    quick_time = measure_time(quick_sort_inplace, arr)
    
    print(f"{size:<10} {merge_time:.6f}        {quick_time:.6f}")

# Worst case for Quick Sort
print("\nQuick Sort Worst Case (sorted input):")
sorted_arr = list(range(100))
print(f"Sorted array of 100 elements:")
quick_time = measure_time(quick_sort_inplace, sorted_arr)
print(f"Quick Sort time: {quick_time:.6f}s")

# ========== STABILITY DEMONSTRATION ==========
print("\n" + "=" * 50)
print("STABILITY DEMONSTRATION")
print("=" * 50)

print("""
Stability: Equal elements maintain their relative order.

Example: Sorting by grade, students with same grade
         should keep their original order.
""")

students = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 85),
    ("David", 90),
    ("Eve", 85)
]

print(f"Original: {students}")

# Stable sort (maintains order for equal grades)
stable_sorted = sorted(students, key=lambda x: x[1])
print(f"Stable sort (by grade): {stable_sorted}")
print("Notice: Alice, Charlie, Eve (all 85) maintain order")

# ========== PRACTICAL APPLICATIONS ==========
print("\n" + "=" * 50)
print("PRACTICAL APPLICATIONS")
print("=" * 50)

# Application 1: Finding Kth Largest Element
def find_kth_largest(arr, k):
    """
    Find kth largest element using modified Quick Sort.
    Average: O(n), Worst: O(n²)
    """
    def quick_select(arr, k):
        if len(arr) == 1:
            return arr[0]
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
        
        if k <= len(left):
            return quick_select(left, k)
        elif k <= len(left) + len(middle):
            return pivot
        else:
            return quick_select(right, k - len(left) - len(middle))
    
    return quick_select(arr, k)

print("\n1. Finding Kth Largest Element:")
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(f"Array: {arr}")
print(f"2nd largest: {find_kth_largest(arr, 2)}")
print(f"4th largest: {find_kth_largest(arr, 4)}")

# Application 2: Merge K Sorted Arrays
def merge_k_sorted(arrays):
    """
    Merge k sorted arrays into one sorted array.
    Uses divide and conquer approach.
    """
    if not arrays:
        return []
    if len(arrays) == 1:
        return arrays[0]
    
    mid = len(arrays) // 2
    left = merge_k_sorted(arrays[:mid])
    right = merge_k_sorted(arrays[mid:])
    
    return merge(left, right)

print("\n2. Merge K Sorted Arrays:")
arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(f"Arrays: {arrays}")
print(f"Merged: {merge_k_sorted(arrays)}")

# Application 3: Sort by Custom Key
def sort_by_key(arr, key_func):
    """
    Sort using merge sort with custom key function.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = sort_by_key(arr[:mid], key_func)
    right = sort_by_key(arr[mid:], key_func)
    
    # Merge with custom comparison
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("\n3. Sort by Custom Key:")
words = ["apple", "pie", "banana", "kiwi", "cherry"]
print(f"Words: {words}")
sorted_words = sort_by_key(words, len)
print(f"Sorted by length: {sorted_words}")

# ========== WHEN TO USE WHICH ==========
print("\n" + "=" * 50)
print("WHEN TO USE WHICH")
print("=" * 50)

print("""
USE MERGE SORT WHEN:
✓ Stability is required
✓ Consistent O(n log n) is needed
✓ Working with linked lists
✓ External sorting (large files)
✓ Parallel processing possible

USE QUICK SORT WHEN:
✓ In-place sorting preferred (memory constrained)
✓ Average case performance matters most
✓ Arrays fit in cache (better locality)
✓ Working with primitive types

USE BUILT-IN sort() WHEN:
✓ Production code (Timsort - hybrid of merge + insertion)
✓ You don't need to implement from scratch
✓ Best of both worlds

INTERVIEW TIPS:
- Know both implementations by heart
- Understand time/space complexity
- Know stability implications
- Be ready to modify for variations
""")

# ========== SUMMARY ==========
print("\n" + "=" * 50)
print("SORTING ALGORITHMS SUMMARY")
print("=" * 50)

print("""
MERGE SORT:
- Divide array in half, sort each, merge
- Time: O(n log n) always
- Space: O(n)
- Stable: Yes
- Use when: stability needed, consistent time

QUICK SORT:
- Choose pivot, partition around it, recurse
- Time: O(n log n) average, O(n²) worst
- Space: O(log n)
- Stable: No
- Use when: in-place needed, average case OK

KEY TAKEAWAYS:
1. Both use divide and conquer
2. Merge Sort divides, then merges sorted halves
3. Quick Sort partitions, then recurses on parts
4. Pivot selection crucial for Quick Sort
5. Python's sort() uses Timsort (hybrid)
""")

print("\n" + "=" * 50)
print("✅ Sorting Algorithms - Complete!")
print("=" * 50)
