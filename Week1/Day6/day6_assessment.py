"""
DAY 6 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Topics Covered:
- Linked Lists
- Two-Pointer Technique
- Sliding Window Pattern
- Sorting Algorithms (Merge Sort, Quick Sort)
"""

print("=" * 60)
print("DAY 6 ASSESSMENT - Essential DSA Part 2")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What is the time complexity of inserting at the head of a singly linked list?
a) O(n)
b) O(1)
c) O(log n)
d) O(n²)

Your answer: """)

print("""
Q2. In the two-pointer technique for finding a pair sum in a sorted array,
    if current_sum < target, what should you do?
a) Move left pointer left
b) Move right pointer right
c) Move left pointer right
d) Move both pointers

Your answer: """)

print("""
Q3. What is the key characteristic of the sliding window pattern?
a) Uses recursion
b) Avoids recalculating entire window contents
c) Requires sorted input
d) Uses extra data structures

Your answer: """)

print("""
Q4. What is the worst-case time complexity of Quick Sort?
a) O(n)
b) O(n log n)
c) O(n²)
d) O(log n)

Your answer: """)

print("""
Q5. Which sorting algorithm is stable and guarantees O(n log n)?
a) Quick Sort
b) Merge Sort
c) Both
d) Neither

Your answer: """)

print("""
Q6. In Floyd's Cycle Detection algorithm, how do the pointers move?
a) Both move one step
b) Both move two steps
c) Slow moves one, fast moves two
d) Fast moves one, slow moves two

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a function to reverse a linked list.
    Return the new head.
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
""")

# Write your code here:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    """Reverse the linked list and return new head."""
    # YOUR CODE HERE
    pass




print("""
Q8. (2 points) Write a function to find the maximum sum of k consecutive
    elements using sliding window technique.
    
    Example: arr = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9 (subarray [5, 1, 3])
""")

# Write your code here:
def max_sum_k_elements(arr, k):
    """Find maximum sum of k consecutive elements."""
    # YOUR CODE HERE
    pass




print("""
Q9. (2 points) Complete the partition function for Quick Sort.
    Use the last element as pivot.
    
    def partition(arr, low, high):
        # Return the final pivot position
""")

# Write your code here:
def partition(arr, low, high):
    """Partition array and return pivot position."""
    # YOUR CODE HERE
    pass




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Compare Merge Sort and Quick Sort:
     - When would you choose Merge Sort over Quick Sort?
     - When would you choose Quick Sort over Merge Sort?
     
     Provide at least 2 reasons for each.

Your answer:
""")

# Write your explanation here as comments:
# 




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) O(1) - Just update head pointer
Q2: c) Move left pointer right - Need larger sum
Q3: b) Avoids recalculating entire window contents
Q4: c) O(n²) - Worst case with poor pivot selection
Q5: b) Merge Sort - Stable and always O(n log n)
Q6: c) Slow moves one, fast moves two

Section B:

Q7: Reverse Linked List
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

Q8: Maximum Sum of K Elements
def max_sum_k_elements(arr, k):
    if len(arr) < k:
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

Q9: Partition Function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

Section C:
Q10: Merge Sort vs Quick Sort

Choose Merge Sort when:
1. Stability is required (preserving order of equal elements)
2. Consistent O(n log n) time is needed (no worst case)
3. Working with linked lists (no random access needed)
4. External sorting (large files that don't fit in memory)
5. Parallel processing is possible (easy to parallelize)

Choose Quick Sort when:
1. Memory is limited (in-place sorting)
2. Average case performance is acceptable
3. Working with arrays (better cache locality)
4. Simple implementation is preferred
5. The input is unlikely to be sorted (avoiding worst case)

SCORING:
========
Section A: 6 points (1 point each)
Section B: 6 points (2 points each)
Section C: 2 points

Total: 14 points
Passing: 10 points (70%)
"""
