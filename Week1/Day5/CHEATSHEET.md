# Day 5 Quick Reference Cheat Sheet

## Big O Notation

```
O(1)       Constant      arr[i], dict[key]
O(log n)   Logarithmic   Binary search
O(n)       Linear        Single loop
O(n log n) Linearithmic  Sorting (merge, quick)
O(n²)      Quadratic     Nested loops
O(2ⁿ)      Exponential   All subsets
```

## Arrays/Lists

```python
# Create
arr = [1, 2, 3]
arr = list(range(5))
arr = [0] * n

# Access - O(1)
first = arr[0]
last = arr[-1]

# Modify
arr.append(x)     # O(1) - add to end
arr.pop()         # O(1) - remove from end
arr.insert(i, x)  # O(n) - insert at index
arr.pop(i)        # O(n) - remove at index

# Search - O(n)
x in arr          # membership
arr.index(x)      # find index
```

## Two Pointers

```python
# Opposite ends
left, right = 0, len(arr) - 1
while left < right:
    # process arr[left], arr[right]
    left += 1
    right -= 1

# Same direction (fast/slow)
slow = fast = 0
while fast < len(arr):
    if condition:
        arr[slow] = arr[fast]
        slow += 1
    fast += 1
```

## Stack (LIFO)

```python
stack = []
stack.append(x)   # push - O(1)
stack.pop()       # pop - O(1)
stack[-1]         # peek - O(1)
len(stack) == 0   # is_empty

# Use cases:
# - Balanced parentheses
# - Undo functionality
# - DFS traversal
```

## Queue (FIFO)

```python
from collections import deque
queue = deque()
queue.append(x)   # enqueue - O(1)
queue.popleft()   # dequeue - O(1)
queue[0]          # peek - O(1)

# Use cases:
# - BFS traversal
# - Task scheduling
# - Level order traversal
```

## Hash Map / Dict

```python
d = {}
d[key] = value    # set - O(1)
d[key]            # get - O(1)
key in d          # check - O(1)
del d[key]        # delete - O(1)
d.get(key, default)

# Counting pattern
for item in arr:
    d[item] = d.get(item, 0) + 1

# Two Sum pattern
seen = {}
for i, num in enumerate(arr):
    if target - num in seen:
        return [seen[target - num], i]
    seen[num] = i
```

## Hash Set

```python
s = set()
s.add(x)          # add - O(1)
s.remove(x)       # remove - O(1)
x in s            # check - O(1)

# Set operations
a | b             # union
a & b             # intersection
a - b             # difference
```

## Binary Search

```python
# Find exact value
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Using bisect
import bisect
bisect.bisect_left(arr, x)   # leftmost position
bisect.bisect_right(arr, x)  # rightmost position
```

## Common Patterns

### Frequency Count
```python
from collections import Counter
freq = Counter(arr)
```

### Sliding Window
```python
# Fixed size k
window_sum = sum(arr[:k])
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
```

### Prefix Sum
```python
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)
# Sum of arr[i:j] = prefix[j] - prefix[i]
```

## Time Complexity Summary

| Data Structure | Access | Search | Insert | Delete |
|---------------|--------|--------|--------|--------|
| Array         | O(1)   | O(n)   | O(n)   | O(n)   |
| Stack         | O(n)   | O(n)   | O(1)   | O(1)   |
| Queue         | O(n)   | O(n)   | O(1)   | O(1)   |
| Hash Table    | N/A    | O(1)   | O(1)   | O(1)   |
| Binary Search | -      | O(log n)| -     | -      |

---
**Keep this handy for Day 5 topics!** 🚀
