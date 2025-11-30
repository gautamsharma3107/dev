"""
Day 36 - Sliding Window Pattern
================================
Learn: Fixed and variable sliding window techniques for array/string problems

Key Concepts:
- Fixed-size window: Window size is constant
- Variable-size window: Window expands/shrinks based on conditions
- Optimizes brute force O(n²) to O(n)
"""

# ========== INTRODUCTION ==========
print("=" * 60)
print("SLIDING WINDOW PATTERN")
print("=" * 60)

print("""
The Sliding Window pattern is used to perform operations on a 
specific window of elements in an array or string.

Two types:
1. Fixed Window: Window size is predetermined (k elements)
2. Variable Window: Window size changes based on conditions

Key insight: Instead of recalculating everything for each window,
we "slide" by removing old element and adding new element.
""")


# ========== FIXED SIZE WINDOW ==========
print("=" * 60)
print("FIXED SIZE WINDOW")
print("=" * 60)


# Example 1: Maximum sum of k consecutive elements
def max_sum_subarray_brute(arr, k):
    """Brute force: O(n*k) time complexity"""
    n = len(arr)
    if n < k:
        return -1
    
    max_sum = float('-inf')
    for i in range(n - k + 1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_sum_subarray(arr, k):
    """Sliding window: O(n) time complexity"""
    n = len(arr)
    if n < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(n - k):
        # Remove first element of previous window
        # Add last element of new window
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"\nArray: {arr}, Window size k={k}")
print(f"Maximum sum of {k} consecutive elements:")
print(f"  Brute force: {max_sum_subarray_brute(arr, k)}")
print(f"  Sliding window: {max_sum_subarray(arr, k)}")


# Example 2: Find all averages of contiguous subarrays of size k
def find_averages(arr, k):
    """Find averages of all k-sized windows"""
    result = []
    window_sum = 0
    start = 0
    
    for end in range(len(arr)):
        window_sum += arr[end]
        
        # Window is complete
        if end >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[start]
            start += 1
    
    return result


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(f"\nArray: {arr}, k={k}")
print(f"Averages: {find_averages(arr, k)}")


# Example 3: Maximum of each subarray of size k
def max_of_subarrays(arr, k):
    """Find maximum in each window (using deque for O(n) solution)"""
    from collections import deque
    
    if not arr or k <= 0:
        return []
    
    result = []
    dq = deque()  # Store indices
    
    for i in range(len(arr)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements (they won't be maximum)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result once window is complete
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(f"\nArray: {arr}, k={k}")
print(f"Maximum of each window: {max_of_subarrays(arr, k)}")


# ========== VARIABLE SIZE WINDOW ==========
print("\n" + "=" * 60)
print("VARIABLE SIZE WINDOW")
print("=" * 60)


# Example 4: Smallest subarray with sum >= target
def min_subarray_len(arr, target):
    """Find minimum length subarray with sum >= target"""
    min_length = float('inf')
    window_sum = 0
    start = 0
    
    for end in range(len(arr)):
        window_sum += arr[end]
        
        # Shrink window while condition is met
        while window_sum >= target:
            min_length = min(min_length, end - start + 1)
            window_sum -= arr[start]
            start += 1
    
    return min_length if min_length != float('inf') else 0


arr = [2, 1, 5, 2, 3, 2]
target = 7
print(f"\nArray: {arr}, Target sum: {target}")
print(f"Minimum subarray length with sum >= {target}: {min_subarray_len(arr, target)}")


# Example 5: Longest substring with at most k distinct characters
def longest_substring_k_distinct(s, k):
    """Find longest substring with at most k distinct characters"""
    char_count = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        # Add character to window
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        
        # Shrink window if too many distinct characters
        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length


s = "araaci"
k = 2
print(f"\nString: '{s}', k={k}")
print(f"Longest substring with at most {k} distinct chars: {longest_substring_k_distinct(s, k)}")


# Example 6: Longest substring without repeating characters
def length_of_longest_substring(s):
    """Classic LeetCode problem - sliding window approach"""
    char_index = {}  # Store last index of each character
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        # If character seen before and within current window
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


test_strings = ["abcabcbb", "bbbbb", "pwwkew", ""]
print(f"\nLongest substring without repeating characters:")
for s in test_strings:
    print(f"  '{s}' → {length_of_longest_substring(s)}")


# Example 7: Minimum window substring
def min_window_substring(s, t):
    """Find minimum window in s containing all characters of t"""
    if not s or not t:
        return ""
    
    from collections import Counter
    
    # Count characters needed
    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0
    
    # Result: (window_length, left, right)
    result = float('inf'), None, None
    left = 0
    
    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1
        
        # Check if current character satisfies need
        if char in need and have[char] == need[char]:
            formed += 1
        
        # Contract window while valid
        while formed == required:
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            # Remove leftmost character
            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1
    
    return "" if result[0] == float('inf') else s[result[1]:result[2]+1]


s = "ADOBECODEBANC"
t = "ABC"
print(f"\nString s: '{s}', t: '{t}'")
print(f"Minimum window containing all chars of t: '{min_window_substring(s, t)}'")


# ========== SLIDING WINDOW TEMPLATE ==========
print("\n" + "=" * 60)
print("SLIDING WINDOW TEMPLATE")
print("=" * 60)

print("""
General template for sliding window problems:

def sliding_window(s):
    left = 0
    result = 0
    window = {}  # or other data structure for tracking
    
    for right in range(len(s)):
        # 1. Add s[right] to window
        # Update window state
        
        # 2. Shrink window if needed
        while (condition to shrink):
            # Remove s[left] from window
            # Update window state
            left += 1
        
        # 3. Update result
        result = max(result, right - left + 1)
    
    return result


Key points:
- Use two pointers (left, right) to define window
- Expand by moving right pointer
- Shrink by moving left pointer
- Use hashmap/set to track window contents
""")


# ========== WHEN TO USE SLIDING WINDOW ==========
print("=" * 60)
print("WHEN TO USE SLIDING WINDOW")
print("=" * 60)

print("""
Use sliding window when:

1. Problem involves contiguous subarray/substring
2. Need to find max/min/count of something in window
3. Need to optimize O(n²) brute force to O(n)

Common patterns:
- "Maximum sum of k elements"
- "Longest/shortest substring with condition"
- "Find all anagrams in string"
- "Minimum window containing all characters"

NOT sliding window:
- Non-contiguous elements
- Need to consider all subsets
- Need multiple passes
""")


# ========== PRACTICE PROBLEMS ==========
print("\n" + "=" * 60)
print("PRACTICE PROBLEMS")
print("=" * 60)

print("""
Try these LeetCode problems:

Easy:
1. LC 643 - Maximum Average Subarray I
2. LC 219 - Contains Duplicate II

Medium:
3. LC 3 - Longest Substring Without Repeating Characters
4. LC 424 - Longest Repeating Character Replacement
5. LC 567 - Permutation in String
6. LC 438 - Find All Anagrams in a String
7. LC 76 - Minimum Window Substring

Hard:
8. LC 239 - Sliding Window Maximum
9. LC 480 - Sliding Window Median
""")


print("\n" + "=" * 60)
print("✅ Sliding Window Pattern - Complete!")
print("=" * 60)
