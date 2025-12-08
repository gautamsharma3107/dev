"""
EXERCISES: Sliding Window Pattern
==================================
Complete all exercises below
"""

# ============================================================
# Exercise 1: Maximum Sum of K Consecutive Elements
# ============================================================
print("Exercise 1: Maximum Sum of K Consecutive Elements")
print("-" * 50)

# TODO: Find the maximum sum of any k consecutive elements in the array
# Use the sliding window technique for O(n) time complexity

def max_sum_of_k_elements(arr, k):
    """Return maximum sum of k consecutive elements"""
    # Your code here
    pass


# Test:
# arr = [2, 1, 5, 1, 3, 2], k = 3
# Expected output: 9 (subarray [5, 1, 3])


# ============================================================
# Exercise 2: Minimum Size Subarray Sum
# ============================================================
print("\n\nExercise 2: Minimum Size Subarray Sum")
print("-" * 50)

# TODO: Find the minimal length of a contiguous subarray of which 
# the sum is greater than or equal to target
# Return 0 if no such subarray exists

def min_subarray_len(target, nums):
    """Return minimum length subarray with sum >= target"""
    # Your code here
    pass


# Test:
# target = 7, nums = [2, 3, 1, 2, 4, 3]
# Expected output: 2 (subarray [4, 3])


# ============================================================
# Exercise 3: Longest Substring Without Repeating Characters
# ============================================================
print("\n\nExercise 3: Longest Substring Without Repeating Characters")
print("-" * 50)

# TODO: Find the length of the longest substring without repeating characters
# Use sliding window with a set or dictionary

def length_of_longest_substring(s):
    """Return length of longest substring without repeating chars"""
    # Your code here
    pass


# Test cases:
# "abcabcbb" → 3 ("abc")
# "bbbbb" → 1 ("b")
# "pwwkew" → 3 ("wke")
# "" → 0


# ============================================================
# Exercise 4: Maximum Average Subarray
# ============================================================
print("\n\nExercise 4: Maximum Average Subarray")
print("-" * 50)

# TODO: Find a contiguous subarray of length k with maximum average value
# Return the maximum average value

def find_max_average(nums, k):
    """Return maximum average of k consecutive elements"""
    # Your code here
    pass


# Test:
# nums = [1, 12, -5, -6, 50, 3], k = 4
# Expected output: 12.75 (subarray [12, -5, -6, 50] has sum 51)


# ============================================================
# Exercise 5: Longest Substring with At Most K Distinct Characters
# ============================================================
print("\n\nExercise 5: Longest Substring with At Most K Distinct Characters")
print("-" * 50)

# TODO: Find the length of the longest substring with at most k distinct characters
# Use sliding window with a dictionary to count characters

def longest_substring_k_distinct(s, k):
    """Return length of longest substring with at most k distinct chars"""
    # Your code here
    pass


# Test:
# s = "eceba", k = 2 → 3 ("ece")
# s = "aa", k = 1 → 2 ("aa")


# ============================================================
# Exercise 6: Find All Anagrams in a String
# ============================================================
print("\n\nExercise 6: Find All Anagrams in a String")
print("-" * 50)

# TODO: Find all starting indices of p's anagrams in s
# Use fixed-size sliding window equal to length of p

def find_anagrams(s, p):
    """Return list of starting indices where anagrams of p exist in s"""
    # Your code here
    pass


# Test:
# s = "cbaebabacd", p = "abc"
# Expected output: [0, 6]
# "cba" at index 0 and "bac" at index 6 are anagrams of "abc"


# ============================================================
# Exercise 7: Fruit Into Baskets (Max Fruits with 2 Types)
# ============================================================
print("\n\nExercise 7: Fruit Into Baskets")
print("-" * 50)

# TODO: You have two baskets. Each basket can only hold one type of fruit.
# Find the maximum number of fruits you can collect from a row of trees.
# (This is essentially longest subarray with at most 2 distinct elements)

def total_fruit(fruits):
    """Return maximum fruits collectible with 2 baskets"""
    # Your code here
    pass


# Test:
# fruits = [1, 2, 1] → 3 (can collect all)
# fruits = [0, 1, 2, 2] → 3 ([1, 2, 2])
# fruits = [1, 2, 3, 2, 2] → 4 ([2, 3, 2, 2])


# ============================================================
# SOLUTIONS (Don't look until you've tried!)
# ============================================================

"""
SOLUTIONS:

Exercise 1 - Maximum Sum of K Elements:
def max_sum_of_k_elements(arr, k):
    if len(arr) < k:
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

Exercise 2 - Minimum Size Subarray Sum:
def min_subarray_len(target, nums):
    min_length = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

Exercise 3 - Longest Substring Without Repeating:
def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

Exercise 4 - Maximum Average Subarray:
def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k

Exercise 5 - Longest Substring K Distinct:
def longest_substring_k_distinct(s, k):
    char_count = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

Exercise 6 - Find All Anagrams:
def find_anagrams(s, p):
    from collections import Counter
    
    if len(s) < len(p):
        return []
    
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    result = []
    
    if s_count == p_count:
        result.append(0)
    
    for i in range(len(p), len(s)):
        # Add new character
        s_count[s[i]] += 1
        
        # Remove old character
        old_char = s[i - len(p)]
        s_count[old_char] -= 1
        if s_count[old_char] == 0:
            del s_count[old_char]
        
        if s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

Exercise 7 - Fruit Into Baskets:
def total_fruit(fruits):
    basket = {}
    max_fruits = 0
    left = 0
    
    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1
        
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits
"""
