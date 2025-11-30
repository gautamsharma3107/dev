"""
Day 36 - Two Pointers Technique
================================
Learn: Two pointer patterns for efficient array/string manipulation

Key Concepts:
- Opposite direction pointers (start and end)
- Same direction pointers (fast and slow)
- When to use two pointers vs other techniques
"""

# ========== INTRODUCTION ==========
print("=" * 60)
print("TWO POINTERS TECHNIQUE")
print("=" * 60)

print("""
The Two Pointers technique uses two pointers to traverse data
structure, reducing time complexity from O(n²) to O(n).

Two main variations:
1. Opposite Direction: Start from both ends, move toward middle
2. Same Direction: Fast/slow pointers, both move in same direction

Best for:
- Sorted arrays
- Finding pairs with certain sum
- Palindrome problems
- Removing duplicates
- Linked list cycle detection
""")


# ========== OPPOSITE DIRECTION POINTERS ==========
print("=" * 60)
print("OPPOSITE DIRECTION POINTERS")
print("=" * 60)


# Example 1: Two Sum in Sorted Array
def two_sum_sorted(arr, target):
    """Find two numbers that add up to target in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return [-1, -1]


arr = [2, 7, 11, 15]
target = 9
print(f"\nArray: {arr}, Target: {target}")
result = two_sum_sorted(arr, target)
print(f"Two Sum indices: {result}")
print(f"Values: {arr[result[0]]} + {arr[result[1]]} = {target}")


# Example 2: Container With Most Water
def max_area(height):
    """Find two lines that form container with most water"""
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Water is limited by shorter line
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        
        # Move pointer of shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"\nHeights: {heights}")
print(f"Maximum water container area: {max_area(heights)}")


# Example 3: Valid Palindrome
def is_palindrome(s):
    """Check if string is palindrome (ignoring non-alphanumeric)"""
    left, right = 0, len(s) - 1
    
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


test_strings = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat I saw"]
print(f"\nPalindrome check:")
for s in test_strings:
    print(f"  '{s}' → {is_palindrome(s)}")


# Example 4: Reverse String
def reverse_string(s):
    """Reverse string in-place using two pointers"""
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)


print(f"\nReverse 'hello': '{reverse_string('hello')}'")


# Example 5: Three Sum
def three_sum(nums):
    """Find all unique triplets that sum to zero"""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result


nums = [-1, 0, 1, 2, -1, -4]
print(f"\nArray: {nums}")
print(f"Three Sum (sum to 0): {three_sum(nums)}")


# ========== SAME DIRECTION POINTERS (FAST/SLOW) ==========
print("\n" + "=" * 60)
print("SAME DIRECTION POINTERS (FAST/SLOW)")
print("=" * 60)


# Example 6: Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    """Remove duplicates in-place, return new length"""
    if not nums:
        return 0
    
    slow = 0  # Points to last unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(f"\nOriginal array: {nums}")
new_length = remove_duplicates(nums)
print(f"After removing duplicates: {nums[:new_length]}")
print(f"New length: {new_length}")


# Example 7: Move Zeroes
def move_zeroes(nums):
    """Move all zeroes to end, maintaining order of non-zero elements"""
    slow = 0  # Position to place next non-zero element
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    
    return nums


nums = [0, 1, 0, 3, 12]
print(f"\nOriginal: {nums}")
print(f"After moving zeroes: {move_zeroes(nums.copy())}")


# Example 8: Remove Element
def remove_element(nums, val):
    """Remove all occurrences of val in-place"""
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


nums = [3, 2, 2, 3]
val = 3
print(f"\nArray: {nums}, Remove: {val}")
new_len = remove_element(nums.copy(), val)
print(f"New length: {new_len}")


# Example 9: Squares of Sorted Array
def sorted_squares(nums):
    """Return sorted array of squares"""
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # Fill from end (largest values)
    
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    
    return result


nums = [-4, -1, 0, 3, 10]
print(f"\nSorted array: {nums}")
print(f"Sorted squares: {sorted_squares(nums)}")


# ========== LINKED LIST CYCLE DETECTION ==========
print("\n" + "=" * 60)
print("LINKED LIST - FAST/SLOW POINTERS")
print("=" * 60)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    """Detect cycle in linked list using Floyd's algorithm"""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def find_cycle_start(head):
    """Find the node where cycle begins"""
    slow = fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


def find_middle(head):
    """Find middle node of linked list"""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(f"\nLinked list: 1 -> 2 -> 3 -> 4 -> 5")
print(f"Has cycle: {has_cycle(head)}")
print(f"Middle node value: {find_middle(head).val}")

# Create cycle for testing
head.next.next.next.next.next = head.next.next  # 5 -> 3 (cycle)
print(f"\nAfter creating cycle (5 -> 3):")
print(f"Has cycle: {has_cycle(head)}")
print(f"Cycle starts at node: {find_cycle_start(head).val}")


# ========== TWO POINTERS TEMPLATE ==========
print("\n" + "=" * 60)
print("TWO POINTERS TEMPLATES")
print("=" * 60)

print("""
1. OPPOSITE DIRECTION (Sorted Array):
   def solve(arr, target):
       left, right = 0, len(arr) - 1
       
       while left < right:
           if condition_met:
               return result
           elif need_larger:
               left += 1
           else:
               right -= 1
       
       return default

2. SAME DIRECTION (Fast/Slow):
   def solve(arr):
       slow = 0
       
       for fast in range(len(arr)):
           if condition:
               arr[slow] = arr[fast]
               slow += 1
       
       return slow

3. LINKED LIST CYCLE:
   def solve(head):
       slow = fast = head
       
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
           
           if slow == fast:
               # Cycle detected
               break
""")


# ========== WHEN TO USE TWO POINTERS ==========
print("=" * 60)
print("WHEN TO USE TWO POINTERS")
print("=" * 60)

print("""
Use two pointers when:

1. Array is SORTED and need to find pairs/triplets
2. Need to compare elements from both ends
3. Need to remove duplicates or specific elements
4. Linked list problems (cycle, middle, nth from end)
5. Need to partition array in-place

Signs to look for:
- "In-place" modification
- "Sorted array"
- "Pair/triplet with sum"
- "Palindrome"
- "Remove/move elements"

Time Complexity: Usually O(n)
Space Complexity: Usually O(1)
""")


# ========== PRACTICE PROBLEMS ==========
print("\n" + "=" * 60)
print("PRACTICE PROBLEMS")
print("=" * 60)

print("""
Try these LeetCode problems:

Easy:
1. LC 167 - Two Sum II (Sorted Array)
2. LC 344 - Reverse String
3. LC 283 - Move Zeroes
4. LC 26 - Remove Duplicates from Sorted Array
5. LC 125 - Valid Palindrome

Medium:
6. LC 11 - Container With Most Water
7. LC 15 - Three Sum
8. LC 16 - Three Sum Closest
9. LC 75 - Sort Colors (Dutch National Flag)
10. LC 142 - Linked List Cycle II

Hard:
11. LC 42 - Trapping Rain Water
12. LC 287 - Find the Duplicate Number
""")


print("\n" + "=" * 60)
print("✅ Two Pointers Technique - Complete!")
print("=" * 60)
