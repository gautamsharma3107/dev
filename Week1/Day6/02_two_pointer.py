"""
Day 6 - Two-Pointer Technique
==============================
Learn: Efficient algorithms using two pointers

Key Concepts:
- Two pointers reduce time complexity (often O(n²) to O(n))
- Common patterns: opposite direction, same direction
- Used for: sorted arrays, linked lists, strings
"""

# ========== INTRODUCTION ==========
print("=" * 50)
print("TWO-POINTER TECHNIQUE")
print("=" * 50)

print("""
Two-Pointer Technique:
- Use two pointers to traverse data structure
- Reduces nested loops (O(n²)) to single pass (O(n))

Common Patterns:
1. Opposite Direction: Start from both ends
2. Same Direction: Both pointers start together (slow/fast)
3. Different Arrays: Pointer in each array

When to Use:
- Sorted arrays
- Finding pairs with conditions
- Linked list problems
- String manipulation
""")

# ========== PATTERN 1: OPPOSITE DIRECTION ==========
print("\n" + "=" * 50)
print("PATTERN 1: OPPOSITE DIRECTION")
print("=" * 50)

# Example 1: Two Sum (Sorted Array)
def two_sum_sorted(arr, target):
    """
    Find two numbers that sum to target.
    Array must be sorted.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # No pair found

print("\n1. Two Sum (Sorted Array):")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = two_sum_sorted(arr, target)
print(f"Array: {arr}")
print(f"Target: {target}")
print(f"Indices: {result}")
if result:
    print(f"Values: {arr[result[0]]} + {arr[result[1]]} = {target}")

# Example 2: Reverse Array
def reverse_array(arr):
    """
    Reverse array in place using two pointers.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

print("\n2. Reverse Array:")
arr = [1, 2, 3, 4, 5]
print(f"Original: {arr.copy()}")
reverse_array(arr)
print(f"Reversed: {arr}")

# Example 3: Valid Palindrome
def is_palindrome(s):
    """
    Check if string is palindrome (ignore non-alphanumeric).
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

print("\n3. Valid Palindrome:")
test_strings = ["racecar", "A man, a plan, a canal: Panama", "hello"]
for s in test_strings:
    print(f"'{s}' -> {is_palindrome(s)}")

# Example 4: Container With Most Water
def max_area(heights):
    """
    Find maximum water container can hold.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(heights) - 1
    max_water = 0
    
    while left < right:
        # Width between pointers
        width = right - left
        # Height is limited by shorter line
        height = min(heights[left], heights[right])
        # Calculate area
        area = width * height
        max_water = max(max_water, area)
        
        # Move pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

print("\n4. Container With Most Water:")
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"Heights: {heights}")
print(f"Max water: {max_area(heights)}")

# ========== PATTERN 2: SAME DIRECTION (SLOW/FAST) ==========
print("\n" + "=" * 50)
print("PATTERN 2: SAME DIRECTION (SLOW/FAST)")
print("=" * 50)

# Example 1: Remove Duplicates (Sorted Array)
def remove_duplicates(arr):
    """
    Remove duplicates in place from sorted array.
    Returns new length.
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0
    
    slow = 0  # Position for next unique element
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

print("\n1. Remove Duplicates (Sorted Array):")
arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print(f"Original: {arr}")
new_length = remove_duplicates(arr)
print(f"After removal: {arr[:new_length]}")
print(f"New length: {new_length}")

# Example 2: Move Zeros
def move_zeros(arr):
    """
    Move all zeros to end while maintaining order.
    Time: O(n), Space: O(1)
    """
    slow = 0  # Position for next non-zero
    
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    
    return arr

print("\n2. Move Zeros:")
arr = [0, 1, 0, 3, 12, 0, 5]
print(f"Original: {arr}")
move_zeros(arr)
print(f"After moving zeros: {arr}")

# Example 3: Remove Element
def remove_element(arr, val):
    """
    Remove all occurrences of val in place.
    Returns new length.
    Time: O(n), Space: O(1)
    """
    slow = 0
    
    for fast in range(len(arr)):
        if arr[fast] != val:
            arr[slow] = arr[fast]
            slow += 1
    
    return slow

print("\n3. Remove Element:")
arr = [3, 2, 2, 3, 4, 2, 5]
val = 2
print(f"Original: {arr}")
print(f"Remove value: {val}")
new_length = remove_element(arr, val)
print(f"After removal: {arr[:new_length]}")

# Example 4: Find Middle of Linked List (concept with array)
def find_middle(arr):
    """
    Find middle element using slow/fast pointers.
    Time: O(n), Space: O(1)
    """
    slow = 0
    fast = 0
    
    while fast < len(arr) - 1 and fast + 1 < len(arr):
        slow += 1
        fast += 2
    
    return arr[slow] if arr else None

print("\n4. Find Middle Element:")
arr = [1, 2, 3, 4, 5]
print(f"Array: {arr}")
print(f"Middle: {find_middle(arr)}")

arr = [1, 2, 3, 4, 5, 6]
print(f"Array: {arr}")
print(f"Middle: {find_middle(arr)}")

# ========== PATTERN 3: LINKED LIST PROBLEMS ==========
print("\n" + "=" * 50)
print("PATTERN 3: LINKED LIST PROBLEMS")
print("=" * 50)

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def create_linked_list(arr):
    """Helper to create linked list from array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Helper to convert linked list to array"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example 1: Detect Cycle
def has_cycle(head):
    """
    Detect cycle in linked list using Floyd's algorithm.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

print("\n1. Detect Cycle in Linked List:")
# Create list without cycle
head = create_linked_list([1, 2, 3, 4, 5])
print(f"List: {linked_list_to_array(head)}")
print(f"Has cycle: {has_cycle(head)}")

# Create list with cycle (manually)
head = create_linked_list([1, 2, 3, 4, 5])
current = head
while current.next:
    current = current.next
current.next = head.next  # Create cycle: 5 -> 2
print(f"List with cycle (5->2): Has cycle: {has_cycle(head)}")

# Example 2: Find Middle of Linked List
def find_middle_linked_list(head):
    """
    Find middle node of linked list.
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

print("\n2. Find Middle of Linked List:")
head = create_linked_list([1, 2, 3, 4, 5])
print(f"List: {linked_list_to_array(head)}")
print(f"Middle: {find_middle_linked_list(head)}")

head = create_linked_list([1, 2, 3, 4, 5, 6])
print(f"List: {linked_list_to_array(head)}")
print(f"Middle: {find_middle_linked_list(head)}")

# Example 3: Remove Nth Node From End
def remove_nth_from_end(head, n):
    """
    Remove nth node from end using two pointers.
    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    
    fast = dummy
    slow = dummy
    
    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove nth node
    slow.next = slow.next.next
    
    return dummy.next

print("\n3. Remove Nth Node From End:")
head = create_linked_list([1, 2, 3, 4, 5])
print(f"Original: {linked_list_to_array(head)}")
head = remove_nth_from_end(head, 2)
print(f"After removing 2nd from end: {linked_list_to_array(head)}")

# ========== PATTERN 4: THREE POINTERS ==========
print("\n" + "=" * 50)
print("PATTERN 4: THREE POINTERS")
print("=" * 50)

# Example: 3Sum
def three_sum(nums, target=0):
    """
    Find all unique triplets that sum to target.
    Time: O(n²), Space: O(1) excluding output
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return result

print("\n1. Three Sum:")
nums = [-1, 0, 1, 2, -1, -4]
print(f"Array: {nums}")
print(f"Triplets summing to 0: {three_sum(nums)}")

# ========== PRACTICE PROBLEMS ==========
print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

# Problem 1: Sort Colors (Dutch National Flag)
def sort_colors(nums):
    """
    Sort array with 0s, 1s, and 2s in place.
    Time: O(n), Space: O(1)
    """
    low = 0           # Boundary for 0s
    mid = 0           # Current element
    high = len(nums) - 1  # Boundary for 2s
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums

print("\n1. Sort Colors (Dutch National Flag):")
nums = [2, 0, 2, 1, 1, 0]
print(f"Original: {nums}")
sort_colors(nums)
print(f"Sorted: {nums}")

# Problem 2: Squares of Sorted Array
def sorted_squares(nums):
    """
    Return squares of sorted array in sorted order.
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    position = n - 1
    
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        
        if left_sq > right_sq:
            result[position] = left_sq
            left += 1
        else:
            result[position] = right_sq
            right -= 1
        position -= 1
    
    return result

print("\n2. Squares of Sorted Array:")
nums = [-4, -1, 0, 3, 10]
print(f"Original: {nums}")
print(f"Sorted squares: {sorted_squares(nums)}")

# Problem 3: Merge Sorted Arrays
def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 (has space for n more elements).
    Time: O(m+n), Space: O(1)
    """
    # Start from end of both arrays
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    return nums1

print("\n3. Merge Sorted Arrays:")
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(f"nums1: {nums1[:m]}, nums2: {nums2}")
merge_sorted_arrays(nums1, m, nums2, n)
print(f"Merged: {nums1}")

# ========== SUMMARY ==========
print("\n" + "=" * 50)
print("TWO-POINTER TECHNIQUE SUMMARY")
print("=" * 50)

print("""
Pattern Recognition Guide:

1. OPPOSITE DIRECTION (left, right = 0, n-1)
   - Two Sum in sorted array
   - Container with most water
   - Valid palindrome
   - Reverse array/string

2. SAME DIRECTION (slow, fast)
   - Remove duplicates
   - Move zeros
   - Linked list cycle detection
   - Find middle element

3. THREE POINTERS
   - 3Sum problem
   - Sort colors (Dutch flag)
   - Merge two sorted arrays

Key Insight:
- Sorted array + pair problem → Two pointers
- In-place modification → Slow/fast pointers
- Linked list traversal → Fast/slow pointers
""")

print("\n" + "=" * 50)
print("✅ Two-Pointer Technique - Complete!")
print("=" * 50)
