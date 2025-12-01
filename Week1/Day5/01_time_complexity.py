"""
Day 5 - Time Complexity Basics (Big O)
======================================
Learn: How to analyze algorithm efficiency

Key Concepts:
- Big O notation measures worst-case time
- Helps compare algorithm efficiency
- Focus on how time grows with input size
- Drop constants and lower-order terms
"""

# ========== WHAT IS BIG O? ==========
print("=" * 50)
print("WHAT IS BIG O NOTATION?")
print("=" * 50)

print("""
Big O notation describes how the runtime of an algorithm
scales with the size of input (n).

We care about:
✅ How it grows as n → infinity
✅ Worst-case scenario
❌ NOT the exact time in seconds

Why it matters:
- n = 10: Most algorithms feel fast
- n = 1,000,000: Bad algorithms crash
""")

# ========== COMMON TIME COMPLEXITIES ==========
print("\n" + "=" * 50)
print("COMMON TIME COMPLEXITIES")
print("=" * 50)

print("""
Complexity | Name          | Example             | n=10   | n=1000
-----------|---------------|---------------------|--------|--------
O(1)       | Constant      | Array index access  | 1      | 1
O(log n)   | Logarithmic   | Binary search       | 3      | 10
O(n)       | Linear        | Simple loop         | 10     | 1000
O(n log n) | Linearithmic  | Merge sort          | 33     | 10000
O(n²)      | Quadratic     | Nested loops        | 100    | 1000000
O(2ⁿ)      | Exponential   | All subsets         | 1024   | ∞
O(n!)      | Factorial     | All permutations    | 3.6M   | ∞

RULE OF THUMB:
- O(1) to O(n log n) = Good 👍
- O(n²) = Acceptable for small n 🤔
- O(2ⁿ) or worse = Avoid! ❌
""")

# ========== O(1) - CONSTANT TIME ==========
print("\n" + "=" * 50)
print("O(1) - CONSTANT TIME")
print("=" * 50)

print("\nConstant time: Same time regardless of input size")

# Example 1: Array access by index
def get_first(arr):
    """O(1) - Always one operation"""
    return arr[0] if arr else None

# Example 2: Dictionary lookup
def get_value(d, key):
    """O(1) - Direct hash lookup"""
    return d.get(key)

# Example 3: Check even/odd
def is_even(n):
    """O(1) - Single calculation"""
    return n % 2 == 0

# Demonstrate
arr = list(range(1000000))
print(f"Array size: {len(arr)}")
print(f"First element (O(1)): {get_first(arr)}")
print(f"Is 42 even? (O(1)): {is_even(42)}")

# ========== O(n) - LINEAR TIME ==========
print("\n" + "=" * 50)
print("O(n) - LINEAR TIME")
print("=" * 50)

print("\nLinear time: Time grows proportionally with input")

# Example 1: Find maximum
def find_max(arr):
    """O(n) - Must check every element"""
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Example 2: Sum all elements
def sum_array(arr):
    """O(n) - Single pass through array"""
    total = 0
    for num in arr:  # n iterations
        total += num
    return total

# Example 3: Linear search
def linear_search(arr, target):
    """O(n) - Worst case: check all elements"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Demonstrate
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Array: {arr}")
print(f"Max (O(n)): {find_max(arr)}")
print(f"Sum (O(n)): {sum_array(arr)}")
print(f"Find 5 (O(n)): index {linear_search(arr, 5)}")

# ========== O(log n) - LOGARITHMIC TIME ==========
print("\n" + "=" * 50)
print("O(log n) - LOGARITHMIC TIME")
print("=" * 50)

print("\nLogarithmic: Halves the problem each step")
print("log₂(1000000) ≈ 20 steps (very efficient!)")

# Example: Binary search (covered in detail later)
def binary_search(arr, target):
    """O(log n) - Halve search space each iteration"""
    left, right = 0, len(arr) - 1
    steps = 0
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"   Found in {steps} steps!")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print(f"   Not found after {steps} steps")
    return -1

# Demonstrate
arr = list(range(0, 1000, 10))  # 100 elements
print(f"\nSearching in sorted array of {len(arr)} elements:")
print(f"Binary search for 500: index {binary_search(arr, 500)}")

# ========== O(n²) - QUADRATIC TIME ==========
print("\n" + "=" * 50)
print("O(n²) - QUADRATIC TIME")
print("=" * 50)

print("\nQuadratic: Nested loops over input")
print("WARNING: Gets slow fast! 1000² = 1,000,000 operations")

# Example 1: Find all pairs
def print_pairs(arr):
    """O(n²) - Nested loops"""
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            count += 1
            # print(arr[i], arr[j])
    return count

# Example 2: Bubble sort (naive)
def bubble_sort(arr):
    """O(n²) - Compare adjacent pairs repeatedly"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example 3: Check duplicates (naive)
def has_duplicate_naive(arr):
    """O(n²) - Compare every pair"""
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False

# Demonstrate
arr = [5, 2, 8, 1, 9]
print(f"\nArray: {arr}")
print(f"Pair count for n={len(arr)}: {print_pairs(arr)}")
print(f"Bubble sort (O(n²)): {bubble_sort(arr)}")
print(f"Has duplicates (naive): {has_duplicate_naive(arr)}")

# ========== COMPARING COMPLEXITIES ==========
print("\n" + "=" * 50)
print("COMPARING COMPLEXITIES")
print("=" * 50)

import time

def measure_time(func, *args):
    """Measure function execution time"""
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

# Compare O(n) vs O(n²) for duplicate checking
def has_duplicate_linear(arr):
    """O(n) - Using hash set"""
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test with increasing sizes
print("\nComparing O(n) vs O(n²) for duplicate checking:")
for size in [100, 1000, 5000]:
    arr = list(range(size))  # No duplicates
    
    time_linear, _ = measure_time(has_duplicate_linear, arr)
    time_quad, _ = measure_time(has_duplicate_naive, arr)
    
    print(f"n={size:5d}: O(n)={time_linear:.6f}s, O(n²)={time_quad:.6f}s, "
          f"Ratio: {time_quad/max(time_linear, 0.000001):.1f}x slower")

# ========== ANALYZING YOUR CODE ==========
print("\n" + "=" * 50)
print("HOW TO ANALYZE YOUR CODE")
print("=" * 50)

print("""
RULES FOR FINDING BIG O:

1. Count the loops:
   - One loop over n → O(n)
   - Nested loops → O(n²)
   - Loop that halves → O(log n)

2. Drop constants:
   - O(2n) → O(n)
   - O(n + 100) → O(n)

3. Keep dominant term:
   - O(n² + n) → O(n²)
   - O(n + log n) → O(n)

4. Multiple inputs:
   - Loop over n, then m → O(n + m)
   - Nested loop over n and m → O(n × m)
""")

# Examples of analysis
print("\nEXAMPLES:")

def example1(arr):
    """What's the complexity?"""
    total = 0
    for x in arr:      # n iterations
        total += x
    return total

print("Example 1: Single loop → O(n)")

def example2(arr):
    """What's the complexity?"""
    for i in range(len(arr)):        # n iterations
        for j in range(len(arr)):    # n iterations each
            pass

print("Example 2: Nested loops → O(n²)")

def example3(arr):
    """What's the complexity?"""
    for i in range(len(arr)):        # n iterations
        for j in range(10):          # 10 iterations (constant!)
            pass

print("Example 3: Loop × constant → O(10n) → O(n)")

def example4(n):
    """What's the complexity?"""
    i = n
    while i > 1:
        i = i // 2

print("Example 4: Halving each time → O(log n)")

# ========== SPACE COMPLEXITY ==========
print("\n" + "=" * 50)
print("SPACE COMPLEXITY (BONUS)")
print("=" * 50)

print("""
Space complexity = Extra memory used by algorithm

O(1) Space - Constant:
    def sum_array(arr):
        total = 0  # Just one variable
        for x in arr:
            total += x
        return total

O(n) Space - Linear:
    def duplicate_array(arr):
        return arr.copy()  # New array of size n

TRADE-OFFS:
- Sometimes use more space for better time
- Hash set for O(1) lookup uses O(n) space
""")

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 50)
print("QUICK REFERENCE")
print("=" * 50)

print("""
| Operation                    | Time       | Example
|------------------------------|------------|------------------
| Variable assignment          | O(1)       | x = 5
| Array index access           | O(1)       | arr[0]
| Dict/Set lookup              | O(1)       | d['key']
| Array append (amortized)     | O(1)       | arr.append(x)
| Array search (unsorted)      | O(n)       | x in arr
| Array sort                   | O(n log n) | arr.sort()
| Nested loops                 | O(n²)      | for i: for j:
| Binary search (sorted)       | O(log n)   | binary_search()
""")

print("\n" + "=" * 50)
print("✅ Time Complexity Basics - Complete!")
print("=" * 50)
print("\nNow you can analyze algorithm efficiency!")
print("Next: Let's apply this to data structures! 🚀")
