"""
Day 6 - Sliding Window Exercises
================================
Practice problems for sliding window technique.
Try to solve each problem before looking at the solution.
"""

# ========== EXERCISE 1 ==========
print("=" * 50)
print("EXERCISE 1: Maximum Sum Subarray of Size K")
print("=" * 50)
print("""
Find the maximum sum of any contiguous subarray of size k.

Example:
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (subarray [5, 1, 3])
""")

def max_sum_subarray_k(arr, k):
    """
    Find maximum sum of k consecutive elements.
    
    Args:
        arr: List of integers
        k: Window size
    Returns:
        Maximum sum of k consecutive elements
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [2, 1, 5, 1, 3, 2]
# print(f"Max sum (k=3): {max_sum_subarray_k(arr, 3)}")

# ========== EXERCISE 2 ==========
print("\n" + "=" * 50)
print("EXERCISE 2: Smallest Subarray with Sum >= S")
print("=" * 50)
print("""
Find the smallest subarray with sum >= target.
Return the length.

Example:
Input: arr = [2, 1, 5, 2, 3, 2], target = 7
Output: 2 (subarray [5, 2])
""")

def smallest_subarray_sum(arr, target):
    """
    Find length of smallest subarray with sum >= target.
    
    Args:
        arr: List of positive integers
        target: Target sum
    Returns:
        Length of smallest such subarray, or 0 if none exists
    """
    # YOUR CODE HERE
    pass

# Test
# arr = [2, 1, 5, 2, 3, 2]
# print(f"Smallest subarray length: {smallest_subarray_sum(arr, 7)}")

# ========== EXERCISE 3 ==========
print("\n" + "=" * 50)
print("EXERCISE 3: Longest Substring with K Distinct")
print("=" * 50)
print("""
Find length of longest substring with at most k distinct characters.

Example:
Input: s = "araaci", k = 2
Output: 4 ("araa")
""")

def longest_k_distinct(s, k):
    """
    Find longest substring with at most k distinct chars.
    
    Args:
        s: Input string
        k: Maximum distinct characters allowed
    Returns:
        Length of longest valid substring
    """
    # YOUR CODE HERE
    pass

# Test
# print(f"Longest (k=2): {longest_k_distinct('araaci', 2)}")
# print(f"Longest (k=1): {longest_k_distinct('araaci', 1)}")

# ========== EXERCISE 4 ==========
print("\n" + "=" * 50)
print("EXERCISE 4: Fruits Into Baskets")
print("=" * 50)
print("""
Given array of fruit types, find max fruits collectable 
with only 2 baskets (2 types allowed).

Example:
Input: [1, 2, 1, 2, 2, 3, 1]
Output: 4 (collecting [1, 2, 1, 2] or [2, 1, 2, 2])
""")

def max_fruits(fruits):
    """
    Find max fruits collectable with 2 baskets.
    
    Args:
        fruits: List of fruit types (integers)
    Returns:
        Maximum number of fruits
    """
    # YOUR CODE HERE
    pass

# Test
# fruits = [1, 2, 1, 2, 2, 3, 1]
# print(f"Max fruits: {max_fruits(fruits)}")

# ========== EXERCISE 5 ==========
print("\n" + "=" * 50)
print("EXERCISE 5: Longest Substring Without Repeating")
print("=" * 50)
print("""
Find length of longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3 ("abc")
""")

def longest_no_repeat(s):
    """
    Find longest substring without repeating characters.
    
    Args:
        s: Input string
    Returns:
        Length of longest substring without repeating chars
    """
    # YOUR CODE HERE
    pass

# Test
# print(f"'abcabcbb': {longest_no_repeat('abcabcbb')}")
# print(f"'bbbbb': {longest_no_repeat('bbbbb')}")
# print(f"'pwwkew': {longest_no_repeat('pwwkew')}")

# ========== SOLUTIONS ==========
print("\n" + "=" * 50)
print("SOLUTIONS (scroll down after attempting)")
print("=" * 50)
print("""


















""")

# Solution 1
def max_sum_subarray_k_solution(arr, k):
    if len(arr) < k:
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Solution 2
def smallest_subarray_sum_solution(arr, target):
    min_len = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# Solution 3
def longest_k_distinct_solution(s, k):
    if k == 0 or not s:
        return 0
    
    char_count = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Solution 4
def max_fruits_solution(fruits):
    basket = {}
    max_count = 0
    left = 0
    
    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1
        
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        
        max_count = max(max_count, right - left + 1)
    
    return max_count

# Solution 5
def longest_no_repeat_solution(s):
    char_index = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Verify solutions
print("Verifying solutions:")
print("-" * 30)

arr = [2, 1, 5, 1, 3, 2]
print(f"Max sum (k=3): {max_sum_subarray_k_solution(arr, 3)}")

arr = [2, 1, 5, 2, 3, 2]
print(f"Smallest subarray sum>=7: {smallest_subarray_sum_solution(arr, 7)}")

print(f"Longest k=2 distinct 'araaci': {longest_k_distinct_solution('araaci', 2)}")
print(f"Longest k=1 distinct 'araaci': {longest_k_distinct_solution('araaci', 1)}")

fruits = [1, 2, 1, 2, 2, 3, 1]
print(f"Max fruits: {max_fruits_solution(fruits)}")

print(f"'abcabcbb' no repeat: {longest_no_repeat_solution('abcabcbb')}")
print(f"'bbbbb' no repeat: {longest_no_repeat_solution('bbbbb')}")
print(f"'pwwkew' no repeat: {longest_no_repeat_solution('pwwkew')}")

print("\n" + "=" * 50)
print("✅ Sliding Window Exercises - Complete!")
print("=" * 50)
