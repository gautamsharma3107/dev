"""
Day 36 - Tree Traversals: DFS and BFS
=====================================
Learn: Tree structures, DFS (Inorder, Preorder, Postorder), BFS (Level Order)

Key Concepts:
- Trees are hierarchical data structures
- DFS explores depth-first (uses stack/recursion)
- BFS explores level by level (uses queue)
- Time Complexity: O(n) for all traversals
- Space Complexity: O(h) for DFS, O(w) for BFS
  where h = height, w = max width of tree
"""

from collections import deque
from typing import List, Optional

# ========== TREE NODE DEFINITION ==========
print("=" * 60)
print("TREE NODE DEFINITION")
print("=" * 60)


class TreeNode:
    """Basic binary tree node structure"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


# Helper function to build tree from list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a list (level-order representation)"""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# ========== DEPTH FIRST SEARCH (DFS) ==========
print("\n" + "=" * 60)
print("DEPTH FIRST SEARCH (DFS)")
print("=" * 60)

print("""
DFS explores as deep as possible along each branch before backtracking.
Three types: Inorder (Left-Root-Right), Preorder (Root-Left-Right), Postorder (Left-Right-Root)

        1
       / \\
      2   3
     / \\   \\
    4   5   6

Inorder:   [4, 2, 5, 1, 3, 6]  - Left, Root, Right (gives sorted order for BST)
Preorder:  [1, 2, 4, 5, 3, 6]  - Root, Left, Right (useful for copying tree)
Postorder: [4, 5, 2, 6, 3, 1]  - Left, Right, Root (useful for deletion)
""")


# 1. Inorder Traversal (Left -> Root -> Right)
def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """Inorder traversal using recursion"""
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)      # Left
        result.append(node.val)  # Root
        dfs(node.right)     # Right
    
    dfs(root)
    return result


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Inorder traversal using iteration (stack)"""
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result


# 2. Preorder Traversal (Root -> Left -> Right)
def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """Preorder traversal using recursion"""
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)  # Root
        dfs(node.left)      # Left
        dfs(node.right)     # Right
    
    dfs(root)
    return result


def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Preorder traversal using iteration (stack)"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# 3. Postorder Traversal (Left -> Right -> Root)
def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """Postorder traversal using recursion"""
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)      # Left
        dfs(node.right)     # Right
        result.append(node.val)  # Root
    
    dfs(root)
    return result


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Postorder traversal using iteration (two stacks)"""
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while stack2:
        result.append(stack2.pop().val)
    
    return result


# ========== BREADTH FIRST SEARCH (BFS) ==========
print("\n" + "=" * 60)
print("BREADTH FIRST SEARCH (BFS)")
print("=" * 60)

print("""
BFS explores level by level, using a queue data structure.

        1           Level 0: [1]
       / \\
      2   3         Level 1: [2, 3]
     / \\   \\
    4   5   6       Level 2: [4, 5, 6]

Level Order: [[1], [2, 3], [4, 5, 6]]
Flat:        [1, 2, 3, 4, 5, 6]
""")


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """BFS - Level order traversal returning nodes by level"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


def level_order_flat(root: Optional[TreeNode]) -> List[int]:
    """BFS - Level order traversal returning flat list"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Build example tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
tree_values = [1, 2, 3, 4, 5, None, 6]
root = build_tree(tree_values)

print("\nTree Structure:")
print("      1")
print("     / \\")
print("    2   3")
print("   / \\   \\")
print("  4   5   6")

print("\n--- DFS Traversals ---")
print(f"Inorder (recursive):  {inorder_recursive(root)}")
print(f"Inorder (iterative):  {inorder_iterative(root)}")
print(f"Preorder (recursive): {preorder_recursive(root)}")
print(f"Preorder (iterative): {preorder_iterative(root)}")
print(f"Postorder (recursive): {postorder_recursive(root)}")
print(f"Postorder (iterative): {postorder_iterative(root)}")

print("\n--- BFS Traversals ---")
print(f"Level Order (by levels): {level_order(root)}")
print(f"Level Order (flat):      {level_order_flat(root)}")


# ========== COMMON INTERVIEW PROBLEMS ==========
print("\n" + "=" * 60)
print("COMMON INTERVIEW PROBLEMS")
print("=" * 60)


# Problem 1: Maximum Depth of Binary Tree
def max_depth(root: Optional[TreeNode]) -> int:
    """Find the maximum depth of a binary tree"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Problem 2: Check if Tree is Symmetric
def is_symmetric(root: Optional[TreeNode]) -> bool:
    """Check if a binary tree is symmetric (mirror of itself)"""
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return is_mirror(root, root) if root else True


# Problem 3: Path Sum
def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """Check if tree has a root-to-leaf path with given sum"""
    if not root:
        return False
    
    # Check if leaf node and sum matches
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Recursively check left and right subtrees
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or 
            has_path_sum(root.right, remaining))


# Problem 4: Invert Binary Tree
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree (mirror it)"""
    if not root:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


# Problem 5: Lowest Common Ancestor
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Find the lowest common ancestor of two nodes"""
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right


print("\n--- Testing Interview Problems ---")
print(f"Max Depth: {max_depth(root)}")

# Build symmetric tree for testing
symmetric_values = [1, 2, 2, 3, 4, 4, 3]
symmetric_root = build_tree(symmetric_values)
print(f"Is Symmetric (symmetric tree): {is_symmetric(symmetric_root)}")
print(f"Is Symmetric (original tree): {is_symmetric(root)}")

# Test path sum
print(f"Has Path Sum (target=7): {has_path_sum(root, 7)}")  # 1->2->4 = 7
print(f"Has Path Sum (target=10): {has_path_sum(root, 10)}")  # 1->3->6 = 10


# ========== TIME AND SPACE COMPLEXITY ==========
print("\n" + "=" * 60)
print("TIME AND SPACE COMPLEXITY")
print("=" * 60)

print("""
All traversal methods:
- Time: O(n) - visit each node once
- Space: 
  - Recursive: O(h) where h = height (call stack)
  - Iterative DFS: O(h) (explicit stack)
  - BFS: O(w) where w = max width of tree

For a balanced tree: h = log(n), w = n/2
For a skewed tree: h = n, w = 1

Choose based on:
- Use DFS for: Path problems, tree comparison, memory efficiency
- Use BFS for: Level-based problems, shortest path, finding nodes
""")


print("\n" + "=" * 60)
print("✅ Tree Traversals - Complete!")
print("=" * 60)
