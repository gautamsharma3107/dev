"""
Day 6 - Sliding Window Pattern
==============================
Learn: Efficient algorithms using sliding window technique

Key Concepts:
- Window slides over array/string
- Avoids recalculating entire window contents
- Fixed-size vs variable-size windows
"""

# ========== INTRODUCTION ==========
print("=" * 50)
print("SLIDING WINDOW PATTERN")
print("=" * 50)

print("""
Sliding Window Technique:
- Maintains a "window" of elements
- Window slides from left to right
- Only updates elements entering/leaving window

Types:
1. Fixed Window: Window size stays constant
2. Variable Window: Window expands/shrinks based on condition

When to Use:
- Subarray/substring problems
- Finding max/min in contiguous elements
- Problems involving consecutive elements
- Optimization over brute force O(n*k) to O(n)
""")

# ========== FIXED-SIZE WINDOW ==========
print("\n" + "=" * 50)
print("FIXED-SIZE WINDOW")
print("=" * 50)

# Example 1: Maximum Sum of K Consecutive Elements
def max_sum_subarray(arr, k):
    """
    Find maximum sum of k consecutive elements.
    
    Brute Force: O(n*k) - recalculate sum for each window
    Sliding Window: O(n) - subtract left, add right
    """
    if len(arr) < k:
        return None
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window: remove leftmost, add rightmost
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print("\n1. Maximum Sum of K Consecutive Elements:")
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(f"Array: {arr}")
print(f"Window size (k): {k}")
print(f"Maximum sum of {k} consecutive: {max_sum_subarray(arr, k)}")

# Step by step visualization
print("\nVisualization:")
for i in range(len(arr) - k + 1):
    window = arr[i:i + k]
    print(f"Window {i + 1}: {window} -> sum = {sum(window)}")

# Example 2: Average of K Elements
def find_averages(arr, k):
    """
    Find average of each k-element window.
    Time: O(n), Space: O(n-k+1)
    """
    if len(arr) < k:
        return []
    
    averages = []
    window_sum = sum(arr[:k])
    averages.append(window_sum / k)
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        averages.append(window_sum / k)
    
    return averages

print("\n2. Average of K Elements:")
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(f"Array: {arr}")
print(f"Window size (k): {k}")
print(f"Averages: {[round(x, 2) for x in find_averages(arr, k)]}")

# Example 3: Maximum in Each Window
def max_in_windows(arr, k):
    """
    Find maximum element in each window of size k.
    Simple approach: O(n*k)
    Note: Can be optimized to O(n) using deque
    """
    if len(arr) < k:
        return []
    
    result = []
    for i in range(len(arr) - k + 1):
        result.append(max(arr[i:i + k]))
    
    return result

print("\n3. Maximum in Each Window:")
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(f"Array: {arr}")
print(f"Window size (k): {k}")
print(f"Max in each window: {max_in_windows(arr, k)}")

# Example 4: Count Occurrences of Anagrams
def count_anagrams(text, pattern):
    """
    Count number of pattern anagrams in text.
    Time: O(n), Space: O(k) where k is pattern length
    """
    from collections import Counter
    
    pattern_count = Counter(pattern)
    window_count = Counter()
    k = len(pattern)
    count = 0
    
    for i in range(len(text)):
        # Add new character to window
        window_count[text[i]] += 1
        
        # Remove character leaving window
        if i >= k:
            left_char = text[i - k]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        # Check if window is anagram
        if window_count == pattern_count:
            count += 1
    
    return count

print("\n4. Count Anagrams:")
text = "fororfrogforgrfor"
pattern = "for"
print(f"Text: '{text}'")
print(f"Pattern: '{pattern}'")
print(f"Anagram count: {count_anagrams(text, pattern)}")

# ========== VARIABLE-SIZE WINDOW ==========
print("\n" + "=" * 50)
print("VARIABLE-SIZE WINDOW")
print("=" * 50)

# Example 1: Minimum Size Subarray Sum
def min_subarray_len(target, arr):
    """
    Find minimum length subarray with sum >= target.
    Time: O(n), Space: O(1)
    
    Strategy:
    - Expand window (add right) until sum >= target
    - Shrink window (remove left) while maintaining condition
    """
    min_len = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(arr)):
        # Expand window
        window_sum += arr[right]
        
        # Shrink window while condition is met
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

print("\n1. Minimum Size Subarray Sum:")
arr = [2, 3, 1, 2, 4, 3]
target = 7
print(f"Array: {arr}")
print(f"Target: {target}")
print(f"Minimum length: {min_subarray_len(target, arr)}")

# Example 2: Longest Substring Without Repeating Characters
def longest_unique_substring(s):
    """
    Find length of longest substring without repeating chars.
    Time: O(n), Space: O(min(n, alphabet_size))
    """
    char_index = {}  # Last seen index of each character
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        # If char was seen and is in current window
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

print("\n2. Longest Substring Without Repeating Characters:")
test_strings = ["abcabcbb", "bbbbb", "pwwkew", ""]
for s in test_strings:
    print(f"'{s}' -> {longest_unique_substring(s)}")

# Example 3: Longest Substring with K Distinct Characters
def longest_k_distinct(s, k):
    """
    Find longest substring with at most k distinct characters.
    Time: O(n), Space: O(k)
    """
    if k == 0 or not s:
        return 0
    
    char_count = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        # Add character to window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window if more than k distinct
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

print("\n3. Longest Substring with K Distinct Characters:")
s = "araaci"
k = 2
print(f"String: '{s}', K: {k}")
print(f"Longest: {longest_k_distinct(s, k)}")

s = "cbbebi"
k = 3
print(f"String: '{s}', K: {k}")
print(f"Longest: {longest_k_distinct(s, k)}")

# Example 4: Fruit Into Baskets (max 2 types)
def total_fruit(fruits):
    """
    Maximum fruits you can collect with 2 baskets (types).
    Same as longest substring with 2 distinct characters.
    Time: O(n), Space: O(1)
    """
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

print("\n4. Fruit Into Baskets:")
fruits = [1, 2, 1, 2, 2, 3, 1]
print(f"Fruits: {fruits}")
print(f"Max fruits: {total_fruit(fruits)}")

# ========== STRING PATTERN MATCHING ==========
print("\n" + "=" * 50)
print("STRING PATTERN MATCHING")
print("=" * 50)

# Example 1: Permutation in String
def check_inclusion(s1, s2):
    """
    Check if s2 contains any permutation of s1.
    Time: O(n), Space: O(26) = O(1)
    """
    from collections import Counter
    
    if len(s1) > len(s2):
        return False
    
    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)])
    
    if s1_count == window_count:
        return True
    
    for i in range(len(s1), len(s2)):
        # Add new character
        window_count[s2[i]] += 1
        
        # Remove old character
        old_char = s2[i - len(s1)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]
        
        if s1_count == window_count:
            return True
    
    return False

print("\n1. Permutation in String:")
test_cases = [("ab", "eidbaooo"), ("ab", "eidboaoo"), ("adc", "dcda")]
for s1, s2 in test_cases:
    print(f"s1='{s1}', s2='{s2}' -> {check_inclusion(s1, s2)}")

# Example 2: Find All Anagrams
def find_anagrams(s, p):
    """
    Find all start indices of p's anagrams in s.
    Time: O(n), Space: O(26) = O(1)
    """
    from collections import Counter
    
    result = []
    if len(p) > len(s):
        return result
    
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])
    
    if p_count == window_count:
        result.append(0)
    
    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1
        
        # Remove old character
        old_char = s[i - len(p)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]
        
        if p_count == window_count:
            result.append(i - len(p) + 1)
    
    return result

print("\n2. Find All Anagrams:")
s = "cbaebabacd"
p = "abc"
print(f"String: '{s}', Pattern: '{p}'")
print(f"Anagram indices: {find_anagrams(s, p)}")

# Example 3: Minimum Window Substring
def min_window(s, t):
    """
    Find minimum window in s containing all chars of t.
    Time: O(n), Space: O(m) where m is t length
    """
    from collections import Counter
    
    if not t or not s:
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_count = {}
    
    ans = (float('inf'), None, None)  # (length, left, right)
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Contract window
        while left <= right and formed == required:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            char = s[left]
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

print("\n3. Minimum Window Substring:")
s = "ADOBECODEBANC"
t = "ABC"
print(f"String: '{s}', Target: '{t}'")
print(f"Minimum window: '{min_window(s, t)}'")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Stock Buy/Sell - Max Profit
def max_profit_window(prices, window_size):
    """
    Find maximum profit with holding period constraint.
    Time: O(n), Space: O(1)
    """
    if len(prices) < 2:
        return 0
    
    max_profit = 0
    
    for i in range(len(prices) - 1):
        # Look ahead up to window_size days
        end = min(i + window_size, len(prices))
        for j in range(i + 1, end):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit

print("\n1. Stock Trading (Max Profit):")
prices = [7, 1, 5, 3, 6, 4]
print(f"Prices: {prices}")
print(f"Max profit (window=3): {max_profit_window(prices, 3)}")

# Example 2: Network Traffic Analysis
def detect_anomaly(traffic, threshold, window_size):
    """
    Detect periods where average traffic exceeds threshold.
    Returns list of (start_index, average) tuples.
    """
    if len(traffic) < window_size:
        return []
    
    anomalies = []
    window_sum = sum(traffic[:window_size])
    
    if window_sum / window_size > threshold:
        anomalies.append((0, window_sum / window_size))
    
    for i in range(window_size, len(traffic)):
        window_sum = window_sum - traffic[i - window_size] + traffic[i]
        avg = window_sum / window_size
        if avg > threshold:
            anomalies.append((i - window_size + 1, avg))
    
    return anomalies

print("\n2. Network Traffic Anomaly Detection:")
traffic = [100, 150, 200, 180, 160, 250, 300, 280, 200, 150]
threshold = 200
window = 3
print(f"Traffic: {traffic}")
print(f"Threshold: {threshold}, Window: {window}")
anomalies = detect_anomaly(traffic, threshold, window)
print(f"Anomalies: {[(f'index {a[0]}', f'avg {a[1]:.1f}') for a in anomalies]}")

# ========== SUMMARY ==========
print("\n" + "=" * 50)
print("SLIDING WINDOW SUMMARY")
print("=" * 50)

print("""
Pattern Recognition Guide:

1. FIXED-SIZE WINDOW
   Keywords: "k consecutive", "window of size k"
   - Max/min sum of k elements
   - Average of k elements
   - Count anagrams of size k
   
   Template:
   window = sum(arr[:k])
   for i in range(k, len(arr)):
       window = window - arr[i-k] + arr[i]

2. VARIABLE-SIZE WINDOW
   Keywords: "minimum length", "longest", "at most k"
   - Minimum subarray with sum >= target
   - Longest substring without repeating
   - At most k distinct characters
   
   Template:
   left = 0
   for right in range(len(arr)):
       # expand window
       while condition_broken:
           # shrink window
           left += 1
       # update result

3. STRING MATCHING
   Keywords: "permutation", "anagram", "contains"
   - Check permutation exists
   - Find all anagrams
   - Minimum window substring
   
   Use Counter/hashmap to track character frequencies

Time Complexity:
- Fixed window: O(n)
- Variable window: O(n) - each element visited at most twice
- Space: Usually O(1) or O(k) for character frequency
""")

print("\n" + "=" * 50)
print("✅ Sliding Window Pattern - Complete!")
print("=" * 50)
