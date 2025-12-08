"""
Day 36 - Sliding Window Pattern
================================
Learn: Fixed and variable size sliding windows for subarray/substring problems

Key Concepts:
- Sliding window optimizes brute force O(n²) to O(n)
- Fixed size: Window size remains constant
- Variable size: Window expands/shrinks based on condition
- Common use cases: Subarrays, substrings, max/min in window
"""

from typing import List
from collections import defaultdict, Counter

# ========== SLIDING WINDOW BASICS ==========
print("=" * 60)
print("SLIDING WINDOW PATTERN")
print("=" * 60)

print("""
The sliding window technique is used to perform operations on a 
specific window size of an array or string.

Types:
1. Fixed Size Window - Window size is constant (e.g., find max sum of k elements)
2. Variable Size Window - Window size changes based on condition

Why use it?
- Reduces O(n²) brute force to O(n)
- Eliminates redundant calculations
- Perfect for contiguous subarray/substring problems

Visual:
Array: [1, 2, 3, 4, 5, 6] with window size k=3

Step 1: [1, 2, 3] | 4, 5, 6  -> sum = 6
Step 2: 1, [2, 3, 4] | 5, 6  -> sum = 9  (add 4, remove 1)
Step 3: 1, 2, [3, 4, 5] | 6  -> sum = 12 (add 5, remove 2)
Step 4: 1, 2, 3, [4, 5, 6]   -> sum = 15 (add 6, remove 3)
""")


# ========== FIXED SIZE WINDOW ==========
print("\n" + "=" * 60)
print("FIXED SIZE SLIDING WINDOW")
print("=" * 60)


# Problem 1: Maximum Sum Subarray of Size K
def max_sum_subarray(arr: List[int], k: int) -> int:
    """
    Find maximum sum of any contiguous subarray of size k
    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add new element, remove old
        max_sum = max(max_sum, window_sum)
    
    return max_sum


print("\n--- Problem 1: Maximum Sum Subarray of Size K ---")
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Array: {arr}, k = {k}")
print(f"Maximum sum of subarray of size {k}: {max_sum_subarray(arr, k)}")


# Problem 2: Average of Subarrays of Size K
def average_of_subarrays(arr: List[int], k: int) -> List[float]:
    """
    Find averages of all contiguous subarrays of size k
    Time: O(n), Space: O(n-k+1)
    """
    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum / k)
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        result.append(window_sum / k)
    
    return result


print("\n--- Problem 2: Average of Subarrays of Size K ---")
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(f"Array: {arr}, k = {k}")
print(f"Averages: {average_of_subarrays(arr, k)}")


# Problem 3: Maximum of Each Subarray of Size K
def max_of_subarrays(arr: List[int], k: int) -> List[int]:
    """
    Find maximum element in each subarray of size k
    Time: O(n), Space: O(k) using deque
    """
    from collections import deque
    
    result = []
    dq = deque()  # Store indices, not values
    
    for i, num in enumerate(arr):
        # Remove elements outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements (they won't be max)
        while dq and arr[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result once we have a full window
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result


print("\n--- Problem 3: Maximum of Each Subarray of Size K ---")
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(f"Array: {arr}, k = {k}")
print(f"Maximums: {max_of_subarrays(arr, k)}")


# ========== VARIABLE SIZE WINDOW ==========
print("\n" + "=" * 60)
print("VARIABLE SIZE SLIDING WINDOW")
print("=" * 60)


# Problem 4: Smallest Subarray with Sum >= Target
def min_subarray_sum(arr: List[int], target: int) -> int:
    """
    Find the smallest subarray with sum >= target
    Time: O(n), Space: O(1)
    """
    min_length = float('inf')
    window_sum = 0
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        # Shrink window while sum >= target
        while window_sum >= target:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    return min_length if min_length != float('inf') else 0


print("\n--- Problem 4: Smallest Subarray with Sum >= Target ---")
arr = [2, 1, 5, 2, 3, 2]
target = 7
print(f"Array: {arr}, target = {target}")
print(f"Smallest subarray length: {min_subarray_sum(arr, target)}")


# Problem 5: Longest Substring with K Distinct Characters
def longest_k_distinct(s: str, k: int) -> int:
    """
    Find longest substring with at most k distinct characters
    Time: O(n), Space: O(k)
    """
    char_count = defaultdict(int)
    max_length = 0
    window_start = 0
    
    for window_end in range(len(s)):
        char_count[s[window_end]] += 1
        
        # Shrink window while we have more than k distinct chars
        while len(char_count) > k:
            char_count[s[window_start]] -= 1
            if char_count[s[window_start]] == 0:
                del char_count[s[window_start]]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


print("\n--- Problem 5: Longest Substring with K Distinct Characters ---")
s = "araaci"
k = 2
print(f"String: '{s}', k = {k}")
print(f"Longest substring length: {longest_k_distinct(s, k)}")


# Problem 6: Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    """
    Find longest substring without repeating characters
    Time: O(n), Space: O(min(n, alphabet_size))
    """
    char_index = {}
    max_length = 0
    window_start = 0
    
    for window_end in range(len(s)):
        current_char = s[window_end]
        
        # If character is seen and is in current window
        if current_char in char_index and char_index[current_char] >= window_start:
            window_start = char_index[current_char] + 1
        
        char_index[current_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


print("\n--- Problem 6: Longest Substring Without Repeating Characters ---")
s = "abcabcbb"
print(f"String: '{s}'")
print(f"Longest substring length: {length_of_longest_substring(s)}")


# ========== STRING PATTERN PROBLEMS ==========
print("\n" + "=" * 60)
print("STRING PATTERN PROBLEMS")
print("=" * 60)


# Problem 7: Find All Anagrams in a String
def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all starting indices of p's anagrams in s
    Time: O(n), Space: O(1) - only 26 letters
    """
    result = []
    if len(p) > len(s):
        return result
    
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    
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


print("\n--- Problem 7: Find All Anagrams in a String ---")
s = "cbaebabacd"
p = "abc"
print(f"String: '{s}', Pattern: '{p}'")
print(f"Anagram indices: {find_anagrams(s, p)}")


# Problem 8: Minimum Window Substring
def min_window_substring(s: str, t: str) -> str:
    """
    Find minimum window in s that contains all characters of t
    Time: O(n + m), Space: O(m)
    """
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    
    window_count = defaultdict(int)
    formed = 0
    
    left = 0
    min_len = float('inf')
    result = ""
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] += 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Try to shrink window
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1
    
    return result


print("\n--- Problem 8: Minimum Window Substring ---")
s = "ADOBECODEBANC"
t = "ABC"
print(f"String: '{s}', Pattern: '{t}'")
print(f"Minimum window: '{min_window_substring(s, t)}'")


# ========== SLIDING WINDOW TEMPLATE ==========
print("\n" + "=" * 60)
print("SLIDING WINDOW TEMPLATE")
print("=" * 60)

print("""
# Fixed Size Window Template:
def fixed_window(arr, k):
    # Initialize first window
    window_result = process(arr[:k])
    result = window_result
    
    for i in range(k, len(arr)):
        # Slide window: add arr[i], remove arr[i-k]
        window_result = update(window_result, arr[i], arr[i-k])
        result = combine(result, window_result)
    
    return result

# Variable Size Window Template:
def variable_window(arr, condition):
    left = 0
    result = initial_value
    state = initial_state
    
    for right in range(len(arr)):
        # Expand window: add arr[right]
        state = expand(state, arr[right])
        
        # Shrink window while condition not met
        while not valid(state, condition):
            state = shrink(state, arr[left])
            left += 1
        
        # Update result
        result = update(result, left, right)
    
    return result

Key Points:
1. Fixed window: Use when window size is constant
2. Variable window: Use when looking for optimal size
3. Track window state efficiently (sum, count, hash map)
4. Shrink from left, expand from right
""")


print("\n" + "=" * 60)
print("✅ Sliding Window Pattern - Complete!")
print("=" * 60)
