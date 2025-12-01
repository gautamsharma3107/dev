# Day 6 Quick Reference Cheat Sheet

## Linked List Node
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Linked List Operations
```python
# Create linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at beginning - O(1)
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert at end - O(n)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    # Delete node - O(n)
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != data:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
    
    # Search - O(n)
    def search(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    # Traverse - O(n)
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
```

## Two-Pointer Patterns
```python
# Pattern 1: Opposite Direction (sorted array)
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Pattern 2: Same Direction (slow/fast pointers)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Pattern 3: Remove duplicates
def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

## Sliding Window Patterns
```python
# Fixed Window Size
def max_sum_fixed_window(arr, k):
    if len(arr) < k:
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Variable Window Size
def min_subarray_sum(arr, target):
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

# Substring with K distinct chars
def longest_substring_k_distinct(s, k):
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
```

## Sorting Algorithms
```python
# Merge Sort - O(n log n), stable
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
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

# Quick Sort - O(n log n) average, in-place
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

## Time Complexity Quick Reference
```
| Operation          | Array | Linked List |
|--------------------|-------|-------------|
| Access by index    | O(1)  | O(n)        |
| Search             | O(n)  | O(n)        |
| Insert at head     | O(n)  | O(1)        |
| Insert at tail     | O(1)* | O(n)        |
| Delete             | O(n)  | O(n)        |

* O(1) if array has space, O(n) if needs resize

| Algorithm    | Best    | Average   | Worst     | Space |
|-------------|---------|-----------|-----------|-------|
| Merge Sort  | O(nlogn)| O(nlogn)  | O(nlogn)  | O(n)  |
| Quick Sort  | O(nlogn)| O(nlogn)  | O(n²)     | O(logn)|
```

## Common Patterns Summary
```python
# Two Pointers for:
# - Pair sum problems
# - Removing duplicates
# - Reversing arrays
# - Linked list cycle detection
# - Finding middle element

# Sliding Window for:
# - Subarray sum problems
# - Substring problems
# - Maximum/minimum in window
# - Anagram finding
# - Character frequency

# When to use:
# - Sorted array → Two pointers (opposite direction)
# - Unsorted + consecutive elements → Sliding window
# - Linked list → Two pointers (slow/fast)
```

---
**Keep this handy for Day 6 topics!** 🚀
