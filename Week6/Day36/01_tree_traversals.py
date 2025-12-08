"""
Day 36 - Tree Traversals: DFS and BFS
======================================
Learn: Depth-First Search (DFS) and Breadth-First Search (BFS) traversals

Key Concepts:
- DFS: Pre-order, In-order, Post-order traversals
- BFS: Level-order traversal
- Both recursive and iterative implementations
- When to use each traversal type
"""

from collections import deque

# ========== TREE NODE DEFINITION ==========
print("=" * 60)
print("TREE NODE DEFINITION")
print("=" * 60)


class TreeNode:
    """Basic tree node class"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


# Create a sample binary tree for demonstration
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("""
Sample Tree Structure:
        1
       / \\
      2   3
     / \\   \\
    4   5   6
""")


# ========== DFS - PRE-ORDER TRAVERSAL ==========
print("=" * 60)
print("DFS - PRE-ORDER TRAVERSAL (Root → Left → Right)")
print("=" * 60)


def preorder_recursive(root):
    """Pre-order: Visit root first, then left subtree, then right subtree"""
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def preorder_iterative(root):
    """Iterative pre-order using stack"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


print(f"Pre-order (Recursive): {preorder_recursive(root)}")
print(f"Pre-order (Iterative): {preorder_iterative(root)}")
print("\nUse case: Copy a tree, serialize/deserialize, prefix expression")


# ========== DFS - IN-ORDER TRAVERSAL ==========
print("\n" + "=" * 60)
print("DFS - IN-ORDER TRAVERSAL (Left → Root → Right)")
print("=" * 60)


def inorder_recursive(root):
    """In-order: Visit left subtree, then root, then right subtree"""
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def inorder_iterative(root):
    """Iterative in-order using stack"""
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result


print(f"In-order (Recursive): {inorder_recursive(root)}")
print(f"In-order (Iterative): {inorder_iterative(root)}")
print("\nUse case: BST gives sorted order, validate BST")


# ========== DFS - POST-ORDER TRAVERSAL ==========
print("\n" + "=" * 60)
print("DFS - POST-ORDER TRAVERSAL (Left → Right → Root)")
print("=" * 60)


def postorder_recursive(root):
    """Post-order: Visit left subtree, then right subtree, then root"""
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def postorder_iterative(root):
    """Iterative post-order using two stacks"""
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node.val)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    return stack2[::-1]


print(f"Post-order (Recursive): {postorder_recursive(root)}")
print(f"Post-order (Iterative): {postorder_iterative(root)}")
print("\nUse case: Delete tree, evaluate expression tree, postfix expression")


# ========== BFS - LEVEL ORDER TRAVERSAL ==========
print("\n" + "=" * 60)
print("BFS - LEVEL ORDER TRAVERSAL")
print("=" * 60)


def level_order(root):
    """BFS: Visit nodes level by level from left to right"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


def level_order_flat(root):
    """BFS: Return flat list instead of levels"""
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


print(f"Level-order (by level): {level_order(root)}")
print(f"Level-order (flat): {level_order_flat(root)}")
print("\nUse case: Shortest path, find minimum depth, zigzag traversal")


# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)


# Example 1: Find maximum depth of tree
def max_depth(root):
    """Find the maximum depth of a binary tree using DFS"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


print(f"\n1. Maximum depth of tree: {max_depth(root)}")


# Example 2: Find minimum depth of tree
def min_depth(root):
    """Find the minimum depth using BFS (more efficient)"""
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        # First leaf node found = minimum depth
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0


print(f"2. Minimum depth of tree: {min_depth(root)}")


# Example 3: Check if tree is symmetric
def is_symmetric(root):
    """Check if tree is symmetric around its center"""
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    if not root:
        return True
    return is_mirror(root.left, root.right)


# Create symmetric tree for testing
#        1
#       / \
#      2   2
#     / \ / \
#    3  4 4  3
symmetric_root = TreeNode(1)
symmetric_root.left = TreeNode(2)
symmetric_root.right = TreeNode(2)
symmetric_root.left.left = TreeNode(3)
symmetric_root.left.right = TreeNode(4)
symmetric_root.right.left = TreeNode(4)
symmetric_root.right.right = TreeNode(3)

print(f"3. Is original tree symmetric? {is_symmetric(root)}")
print(f"   Is symmetric tree symmetric? {is_symmetric(symmetric_root)}")


# Example 4: Path sum
def has_path_sum(root, target_sum):
    """Check if there's a root-to-leaf path with given sum"""
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target_sum
    
    remaining = target_sum - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)


print(f"4. Has path sum 7 (1→2→4)? {has_path_sum(root, 7)}")
print(f"   Has path sum 10 (1→3→6)? {has_path_sum(root, 10)}")


# Example 5: Invert binary tree
def invert_tree(root):
    """Invert a binary tree (mirror image)"""
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


# Create a copy for inversion
import copy

def clone_tree(root):
    """Deep clone a binary tree"""
    if not root:
        return None
    new_node = TreeNode(root.val)
    new_node.left = clone_tree(root.left)
    new_node.right = clone_tree(root.right)
    return new_node


inverted = invert_tree(clone_tree(root))
print(f"5. Inverted tree level-order: {level_order(inverted)}")


# ========== DFS VS BFS COMPARISON ==========
print("\n" + "=" * 60)
print("DFS VS BFS COMPARISON")
print("=" * 60)

print("""
| Aspect          | DFS                    | BFS                    |
|-----------------|------------------------|------------------------|
| Data Structure  | Stack (recursion/iter) | Queue                  |
| Space           | O(h) - tree height     | O(w) - max width       |
| Best for        | Deep trees, all paths  | Shallow trees, shortest|
| Use cases       | Path finding, backtrack| Level problems, min    |
""")


# ========== TIME AND SPACE COMPLEXITY ==========
print("=" * 60)
print("TIME AND SPACE COMPLEXITY")
print("=" * 60)

print("""
All traversals visit each node once:
- Time Complexity: O(n) where n = number of nodes

Space Complexity:
- DFS (Recursive): O(h) for call stack, where h = height
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)
  
- DFS (Iterative): O(h) for explicit stack

- BFS: O(w) for queue, where w = max width
  - Best case: O(1)
  - Worst case (complete tree): O(n/2) ≈ O(n)
""")


print("\n" + "=" * 60)
print("✅ Tree Traversals - Complete!")
print("=" * 60)
