"""
EXERCISES: Tree Traversals (DFS and BFS)
=========================================
Complete all exercises below
"""

from collections import deque

# Tree Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# Exercise 1: Pre-order Traversal (Recursive)
# ============================================================
print("Exercise 1: Pre-order Traversal (Recursive)")
print("-" * 50)

# TODO: Implement pre-order traversal recursively
# Pre-order: Root → Left → Right
# Return a list of node values

def preorder_recursive(root):
    """Return list of values in pre-order"""
    # Your code here
    pass


# Test:
# Build tree:     1
#               /   \
#              2     3
#             / \
#            4   5
# Expected output: [1, 2, 4, 5, 3]


# ============================================================
# Exercise 2: In-order Traversal (Iterative)
# ============================================================
print("\n\nExercise 2: In-order Traversal (Iterative)")
print("-" * 50)

# TODO: Implement in-order traversal iteratively using a stack
# In-order: Left → Root → Right
# Return a list of node values

def inorder_iterative(root):
    """Return list of values in in-order using iteration"""
    # Your code here
    pass


# Test:
# Build tree:     1
#               /   \
#              2     3
#             / \
#            4   5
# Expected output: [4, 2, 5, 1, 3]


# ============================================================
# Exercise 3: Level Order Traversal
# ============================================================
print("\n\nExercise 3: Level Order Traversal")
print("-" * 50)

# TODO: Implement BFS level order traversal
# Return a list of lists, where each inner list contains values at that level

def level_order(root):
    """Return list of lists of values at each level"""
    # Your code here
    pass


# Test:
# Build tree:     3
#               /   \
#              9    20
#                  /  \
#                 15   7
# Expected output: [[3], [9, 20], [15, 7]]


# ============================================================
# Exercise 4: Maximum Depth of Binary Tree
# ============================================================
print("\n\nExercise 4: Maximum Depth of Binary Tree")
print("-" * 50)

# TODO: Find the maximum depth (height) of a binary tree
# Use DFS approach

def max_depth(root):
    """Return the maximum depth of the tree"""
    # Your code here
    pass


# Test:
# Build tree:     3
#               /   \
#              9    20
#                  /  \
#                 15   7
# Expected output: 3


# ============================================================
# Exercise 5: Check if Binary Tree is Balanced
# ============================================================
print("\n\nExercise 5: Balanced Binary Tree")
print("-" * 50)

# TODO: Check if a binary tree is height-balanced
# A tree is balanced if the depths of two subtrees never differ by more than 1

def is_balanced(root):
    """Return True if tree is balanced, False otherwise"""
    # Your code here
    pass


# Test:
# Balanced tree:     3
#                  /   \
#                 9    20
#                     /  \
#                    15   7
# Expected output: True

# Unbalanced:     1
#                  \
#                   2
#                    \
#                     3
# Expected output: False


# ============================================================
# Exercise 6: Invert Binary Tree
# ============================================================
print("\n\nExercise 6: Invert Binary Tree")
print("-" * 50)

# TODO: Invert a binary tree (mirror it)
# Each node's left and right children should be swapped

def invert_tree(root):
    """Invert the tree and return the root"""
    # Your code here
    pass


# Test:
# Original:     4
#             /   \
#            2     7
#           / \   / \
#          1   3 6   9
# 
# Inverted:     4
#             /   \
#            7     2
#           / \   / \
#          9   6 3   1


# ============================================================
# Exercise 7: Path Sum
# ============================================================
print("\n\nExercise 7: Path Sum")
print("-" * 50)

# TODO: Given a binary tree and a target sum, determine if the tree has
# a root-to-leaf path such that adding up all values equals the target

def has_path_sum(root, target_sum):
    """Return True if root-to-leaf path with target sum exists"""
    # Your code here
    pass


# Test:
# Tree:       5
#            / \
#           4   8
#          /   / \
#         11  13  4
#        /  \      \
#       7    2      1
# Target: 22
# Expected output: True (path: 5 → 4 → 11 → 2 = 22)


# ============================================================
# SOLUTIONS (Don't look until you've tried!)
# ============================================================

"""
SOLUTIONS:

Exercise 1 - Pre-order Recursive:
def preorder_recursive(root):
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)

Exercise 2 - In-order Iterative:
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

Exercise 3 - Level Order:
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result

Exercise 4 - Maximum Depth:
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

Exercise 5 - Is Balanced:
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
    return check(root) != -1

Exercise 6 - Invert Tree:
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

Exercise 7 - Path Sum:
def has_path_sum(root, target_sum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    remaining = target_sum - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)
"""
