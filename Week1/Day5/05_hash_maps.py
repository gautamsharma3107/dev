"""
Day 5 - Hash Maps / Dictionaries
=================================
Learn: Hash tables for O(1) average lookups

Key Concepts:
- Hash function maps keys to indices
- O(1) average for insert, lookup, delete
- Handles collisions with chaining or probing
- Python dict is a hash table implementation
"""

# ========== WHAT IS A HASH MAP? ==========
print("=" * 50)
print("WHAT IS A HASH MAP?")
print("=" * 50)

print("""
Hash Map (Hash Table / Dictionary)
- Stores key-value pairs
- O(1) average time for operations
- Uses hash function to compute index

How it works:
1. key → hash(key) → index
2. Store value at that index
3. Retrieve by computing same index

Example:
key "name" → hash("name") → index 5
store: table[5] = "Alice"
get: return table[5]

Why so fast?
- Direct access via computed index
- No searching needed!
""")

# ========== PYTHON DICTIONARY ==========
print("\n" + "=" * 50)
print("PYTHON DICTIONARY (Built-in Hash Map)")
print("=" * 50)

# Creation
d1 = {'name': 'Alice', 'age': 25}
d2 = dict(name='Bob', age=30)
d3 = {}

print(f"Dict literal: {d1}")
print(f"Dict constructor: {d2}")
print(f"Empty dict: {d3}")

# ========== TIME COMPLEXITY ==========
print("\n" + "=" * 50)
print("DICT OPERATIONS - TIME COMPLEXITY")
print("=" * 50)

print("""
Operation           | Average | Worst Case
--------------------|---------|----------
Get d[key]          | O(1)    | O(n)*
Set d[key] = value  | O(1)    | O(n)*
Delete del d[key]   | O(1)    | O(n)*
Check key in d      | O(1)    | O(n)*
Get keys/values     | O(n)    | O(n)
Iterate             | O(n)    | O(n)

* Worst case happens with hash collisions
  (rare with good hash function)
""")

# ========== BASIC OPERATIONS ==========
print("\n" + "=" * 50)
print("BASIC DICTIONARY OPERATIONS")
print("=" * 50)

# Create
student = {'name': 'Charlie', 'age': 20, 'grade': 'A'}
print(f"Original: {student}")

# Get value - O(1)
print(f"\nGet 'name': {student['name']}")
print(f"Get with default: {student.get('email', 'N/A')}")

# Set value - O(1)
student['age'] = 21
student['email'] = 'charlie@example.com'
print(f"After updates: {student}")

# Check key exists - O(1)
print(f"\n'name' in dict: {'name' in student}")
print(f"'phone' in dict: {'phone' in student}")

# Delete - O(1)
del student['grade']
print(f"After delete 'grade': {student}")

# Pop with default
removed = student.pop('email', None)
print(f"Popped 'email': {removed}")

# ========== USE CASE 1: COUNTING FREQUENCY ==========
print("\n" + "=" * 50)
print("USE CASE 1: COUNTING FREQUENCY")
print("=" * 50)

def count_frequency(arr):
    """
    Count element occurrences - O(n)
    Classic hash map pattern!
    """
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Alternative using setdefault
def count_frequency_v2(arr):
    freq = {}
    for item in arr:
        freq.setdefault(item, 0)
        freq[item] += 1
    return freq

# Using Counter (built-in)
from collections import Counter

arr = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
print(f"Array: {arr}")
print(f"Frequency: {count_frequency(arr)}")

# With Counter (most Pythonic)
print(f"Using Counter: {dict(Counter(arr))}")

# ========== USE CASE 2: TWO SUM ==========
print("\n" + "=" * 50)
print("USE CASE 2: TWO SUM")
print("=" * 50)

print("""
Find two numbers that add up to target.
Return indices of the two numbers.

Brute force: O(n²) - check all pairs
With hash map: O(n) - single pass!
""")

def two_sum_brute(nums, target):
    """O(n²) - nested loops"""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum(nums, target):
    """
    O(n) - using hash map
    Store: {number: index}
    For each num, check if (target - num) exists
    """
    seen = {}  # number -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Array: {nums}, Target: {target}")
print(f"Indices: {result}")
print(f"Values: {nums[result[0]]} + {nums[result[1]]} = {target}")

# ========== USE CASE 3: CHECK ANAGRAM ==========
print("\n" + "=" * 50)
print("USE CASE 3: CHECK ANAGRAM")
print("=" * 50)

def is_anagram(s1, s2):
    """
    Check if two strings are anagrams - O(n)
    Anagram: Same characters, different order
    """
    if len(s1) != len(s2):
        return False
    
    # Count characters in both strings
    count1 = {}
    count2 = {}
    
    for c in s1:
        count1[c] = count1.get(c, 0) + 1
    
    for c in s2:
        count2[c] = count2.get(c, 0) + 1
    
    return count1 == count2

# Shorter version using Counter
def is_anagram_short(s1, s2):
    return Counter(s1) == Counter(s2)

# Test cases
test_cases = [
    ("listen", "silent"),
    ("hello", "world"),
    ("race", "care"),
    ("python", "typhon"),
]

print("Anagram checker:")
for s1, s2 in test_cases:
    result = "✅ Yes" if is_anagram(s1, s2) else "❌ No"
    print(f"  '{s1}' and '{s2}': {result}")

# ========== USE CASE 4: FIND DUPLICATES ==========
print("\n" + "=" * 50)
print("USE CASE 4: FIND DUPLICATES")
print("=" * 50)

def find_duplicates(arr):
    """Find all duplicate elements - O(n)"""
    seen = set()  # Hash set
    duplicates = []
    
    for item in arr:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates

def has_duplicate(arr):
    """Check if any duplicate exists - O(n)"""
    return len(arr) != len(set(arr))

arr = [1, 2, 3, 2, 4, 5, 3, 6]
print(f"Array: {arr}")
print(f"Has duplicates: {has_duplicate(arr)}")
print(f"Duplicate values: {find_duplicates(arr)}")

# ========== USE CASE 5: GROUP ANAGRAMS ==========
print("\n" + "=" * 50)
print("USE CASE 5: GROUP ANAGRAMS")
print("=" * 50)

def group_anagrams(words):
    """
    Group words that are anagrams - O(n * k log k)
    where n = number of words, k = max word length
    """
    groups = {}  # sorted_word -> list of anagrams
    
    for word in words:
        # Use sorted characters as key
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(f"Words: {words}")
print(f"Grouped anagrams:")
for group in result:
    print(f"  {group}")

# ========== USE CASE 6: FIRST NON-REPEATING CHARACTER ==========
print("\n" + "=" * 50)
print("USE CASE 6: FIRST NON-REPEATING CHARACTER")
print("=" * 50)

def first_unique_char(s):
    """
    Find first non-repeating character - O(n)
    Return index, or -1 if none exists
    """
    # Count all characters
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    
    # Find first with count 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    
    return -1

test_strings = ["leetcode", "loveleetcode", "aabb"]
print("First non-repeating character:")
for s in test_strings:
    idx = first_unique_char(s)
    char = s[idx] if idx != -1 else "None"
    print(f"  '{s}': index {idx}, char '{char}'")

# ========== USE CASE 7: SUBARRAY SUM EQUALS K ==========
print("\n" + "=" * 50)
print("USE CASE 7: SUBARRAY SUM EQUALS K")
print("=" * 50)

def subarray_sum(nums, k):
    """
    Count subarrays with sum equal to k - O(n)
    Uses prefix sum + hash map
    """
    count = 0
    prefix_sum = 0
    prefix_counts = {0: 1}  # sum -> count of occurrences
    
    for num in nums:
        prefix_sum += num
        
        # If (prefix_sum - k) exists, we found a subarray
        if prefix_sum - k in prefix_counts:
            count += prefix_counts[prefix_sum - k]
        
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
    
    return count

nums = [1, 1, 1]
k = 2
print(f"Array: {nums}, k={k}")
print(f"Subarrays with sum {k}: {subarray_sum(nums, k)}")

nums = [1, 2, 3]
k = 3
print(f"Array: {nums}, k={k}")
print(f"Subarrays with sum {k}: {subarray_sum(nums, k)}")

# ========== HASH SET (SET) ==========
print("\n" + "=" * 50)
print("HASH SET (Python set)")
print("=" * 50)

print("""
Set = Hash table with only keys (no values)
Same O(1) operations for add, remove, lookup
""")

# Create
s1 = {1, 2, 3}
s2 = set([1, 2, 2, 3])  # Duplicates removed
s3 = set()

print(f"Set literal: {s1}")
print(f"From list (deduped): {s2}")

# Operations
s = {1, 2, 3}
s.add(4)        # Add element - O(1)
s.remove(1)     # Remove element - O(1)
print(f"After add(4), remove(1): {s}")
print(f"3 in s: {3 in s}")  # Check membership - O(1)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"\nSet a: {a}")
print(f"Set b: {b}")
print(f"Union (a | b): {a | b}")
print(f"Intersection (a & b): {a & b}")
print(f"Difference (a - b): {a - b}")
print(f"Symmetric diff (a ^ b): {a ^ b}")

# ========== DEFAULT DICT ==========
print("\n" + "=" * 50)
print("DEFAULTDICT (Handy Tool)")
print("=" * 50)

from collections import defaultdict

# Without defaultdict
d = {}
# d['key'].append('value')  # KeyError!

# With defaultdict
d = defaultdict(list)
d['fruits'].append('apple')
d['fruits'].append('banana')
d['vegetables'].append('carrot')
print(f"defaultdict(list): {dict(d)}")

# For counting
d = defaultdict(int)
for char in "hello":
    d[char] += 1
print(f"defaultdict(int) for counting: {dict(d)}")

# ========== HASH MAP IMPLEMENTATION (CONCEPT) ==========
print("\n" + "=" * 50)
print("HOW HASH TABLES WORK (Concept)")
print("=" * 50)

print("""
Simple Hash Table Implementation:

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Chaining
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        # Check if key exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

Collision Handling:
1. Chaining: Each bucket is a list
2. Open Addressing: Find next empty slot
""")

# ========== WHEN TO USE HASH MAPS ==========
print("\n" + "=" * 50)
print("WHEN TO USE HASH MAPS")
print("=" * 50)

print("""
Use Hash Map / Dict when:
✅ Need O(1) lookup by key
✅ Counting frequencies
✅ Caching results
✅ Two-sum type problems
✅ Grouping items
✅ Deduplication
✅ Storing key-value associations

Don't use when:
❌ Need ordered data (use list)
❌ Need min/max efficiently (use heap)
❌ Keys not hashable (use id or convert)
""")

# ========== COMMON PATTERNS SUMMARY ==========
print("\n" + "=" * 50)
print("COMMON HASH MAP PATTERNS")
print("=" * 50)

print("""
1. COUNTING
   freq = {}
   for x in arr:
       freq[x] = freq.get(x, 0) + 1

2. LOOKUP TABLE
   seen = set()
   for x in arr:
       complement = target - x
       if complement in seen:
           return True
       seen.add(x)

3. GROUPING
   groups = {}
   for item in arr:
       key = get_key(item)
       groups.setdefault(key, []).append(item)

4. CACHING (Memoization)
   cache = {}
   def expensive(n):
       if n in cache:
           return cache[n]
       result = compute(n)
       cache[n] = result
       return result
""")

print("\n" + "=" * 50)
print("✅ Hash Maps - Complete!")
print("=" * 50)
print("\nNext: Let's learn Binary Search! 🚀")
