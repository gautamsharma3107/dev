"""
Day 6 - Linked List Exercises
============================
Practice problems for linked list implementation.
Try to solve each problem before looking at the solution.
"""

# ========== SETUP ==========
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def from_list(self, arr):
        for item in arr:
            self.append(item)

def create_list(arr):
    ll = LinkedList()
    ll.from_list(arr)
    return ll

# ========== EXERCISE 1 ==========
print("=" * 50)
print("EXERCISE 1: Get Length of Linked List")
print("=" * 50)
print("""
Write a function that returns the length of a linked list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> None
Output: 4
""")

def get_length(head):
    """
    Return the number of nodes in the linked list.
    
    Args:
        head: Head node of the linked list
    Returns:
        int: Number of nodes
    """
    # YOUR CODE HERE
    pass

# Test
ll = create_list([1, 2, 3, 4, 5])
# print(f"Length: {get_length(ll.head)}")  # Expected: 5

# ========== EXERCISE 2 ==========
print("\n" + "=" * 50)
print("EXERCISE 2: Find Nth Node from End")
print("=" * 50)
print("""
Write a function to find the nth node from the end.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> None, n=2
Output: 4 (2nd from end)
""")

def find_nth_from_end(head, n):
    """
    Find nth node from end using two-pointer technique.
    
    Args:
        head: Head node of the linked list
        n: Position from end (1-indexed)
    Returns:
        Data of nth node from end, or None if not found
    """
    # YOUR CODE HERE
    pass

# Test
ll = create_list([1, 2, 3, 4, 5])
# print(f"2nd from end: {find_nth_from_end(ll.head, 2)}")  # Expected: 4

# ========== EXERCISE 3 ==========
print("\n" + "=" * 50)
print("EXERCISE 3: Detect Loop in Linked List")
print("=" * 50)
print("""
Write a function to detect if a linked list has a loop.
Use Floyd's Cycle Detection (slow/fast pointers).

Example:
Input: 1 -> 2 -> 3 -> 4 -> 2 (loop)
Output: True
""")

def has_loop(head):
    """
    Detect if linked list has a loop.
    
    Args:
        head: Head node of the linked list
    Returns:
        bool: True if loop exists, False otherwise
    """
    # YOUR CODE HERE
    pass

# Test
ll = create_list([1, 2, 3, 4, 5])
# print(f"Has loop: {has_loop(ll.head)}")  # Expected: False

# ========== EXERCISE 4 ==========
print("\n" + "=" * 50)
print("EXERCISE 4: Reverse Linked List")
print("=" * 50)
print("""
Write a function to reverse a linked list in place.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
""")

def reverse_list(head):
    """
    Reverse linked list and return new head.
    
    Args:
        head: Head node of the linked list
    Returns:
        New head after reversal
    """
    # YOUR CODE HERE
    pass

# Test
ll = create_list([1, 2, 3, 4, 5])
# ll.head = reverse_list(ll.head)
# print(f"Reversed: {ll.to_list()}")  # Expected: [5, 4, 3, 2, 1]

# ========== EXERCISE 5 ==========
print("\n" + "=" * 50)
print("EXERCISE 5: Merge Two Sorted Lists")
print("=" * 50)
print("""
Write a function to merge two sorted linked lists.

Example:
Input: 1 -> 3 -> 5 and 2 -> 4 -> 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
""")

def merge_sorted_lists(head1, head2):
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        head1: Head of first sorted list
        head2: Head of second sorted list
    Returns:
        Head of merged sorted list
    """
    # YOUR CODE HERE
    pass

# Test
ll1 = create_list([1, 3, 5])
ll2 = create_list([2, 4, 6])
# merged_head = merge_sorted_lists(ll1.head, ll2.head)
# # Convert to list for printing
# result = []
# while merged_head:
#     result.append(merged_head.data)
#     merged_head = merged_head.next
# print(f"Merged: {result}")  # Expected: [1, 2, 3, 4, 5, 6]

# ========== SOLUTIONS ==========
print("\n" + "=" * 50)
print("SOLUTIONS (scroll down after attempting)")
print("=" * 50)
print("""


















""")

# Solution 1
def get_length_solution(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

# Solution 2
def find_nth_from_end_solution(head, n):
    fast = slow = head
    # Move fast n nodes ahead
    for _ in range(n):
        if not fast:
            return None
        fast = fast.next
    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.data if slow else None

# Solution 3
def has_loop_solution(head):
    if not head or not head.next:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Solution 4
def reverse_list_solution(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Solution 5
def merge_sorted_lists_solution(head1, head2):
    dummy = Node(0)
    current = dummy
    
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    
    current.next = head1 or head2
    return dummy.next

# Verify solutions
print("Verifying solutions:")
print("-" * 30)

ll = create_list([1, 2, 3, 4, 5])
print(f"Length: {get_length_solution(ll.head)}")

ll = create_list([1, 2, 3, 4, 5])
print(f"2nd from end: {find_nth_from_end_solution(ll.head, 2)}")

ll = create_list([1, 2, 3, 4, 5])
print(f"Has loop: {has_loop_solution(ll.head)}")

ll = create_list([1, 2, 3, 4, 5])
ll.head = reverse_list_solution(ll.head)
print(f"Reversed: {ll.to_list()}")

ll1 = create_list([1, 3, 5])
ll2 = create_list([2, 4, 6])
merged = merge_sorted_lists_solution(ll1.head, ll2.head)
result = []
while merged:
    result.append(merged.data)
    merged = merged.next
print(f"Merged: {result}")

print("\n" + "=" * 50)
print("✅ Linked List Exercises - Complete!")
print("=" * 50)
