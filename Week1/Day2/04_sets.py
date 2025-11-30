"""
Day 2 - Sets
============
Learn: Set creation, operations, use cases

Key Concepts:
- Sets are unordered collections of unique elements
- No duplicates allowed
- Very fast membership testing
- Support mathematical set operations
"""

# ========== SET CREATION ==========
print("=" * 50)
print("SET CREATION")
print("=" * 50)

# Empty set (NOT {} which creates dict)
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with values
fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")

# Duplicates automatically removed
numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"Numbers (duplicates removed): {numbers}")

# From list
list_with_dups = [1, 2, 2, 3, 3, 3, 4]
unique = set(list_with_dups)
print(f"Unique from list: {unique}")

# From string
chars = set("hello")
print(f"Unique chars from 'hello': {chars}")

# ========== SET OPERATIONS (Basic) ==========
print("\n" + "=" * 50)
print("SET BASIC OPERATIONS")
print("=" * 50)

colors = {"red", "green", "blue"}
print(f"Colors: {colors}")

# Add element
colors.add("yellow")
print(f"After add: {colors}")

# Add existing element (no change)
colors.add("red")
print(f"After adding existing: {colors}")

# Remove element (error if not found)
colors.remove("yellow")
print(f"After remove: {colors}")

# Discard element (no error if not found)
colors.discard("purple")  # No error
print(f"After discard (not found): {colors}")

# Pop random element
popped = colors.pop()
print(f"Popped: {popped}")
print(f"After pop: {colors}")

# Add elements back for next examples
colors.update(["red", "green", "blue", "yellow"])
print(f"After update: {colors}")

# ========== SET MATHEMATICAL OPERATIONS ==========
print("\n" + "=" * 50)
print("SET MATHEMATICAL OPERATIONS")
print("=" * 50)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union (all elements from both sets)
union = set_a | set_b  # or set_a.union(set_b)
print(f"\nUnion (A | B): {union}")

# Intersection (common elements)
intersection = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection}")

# Difference (elements in A but not in B)
diff_a = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A - B): {diff_a}")

diff_b = set_b - set_a
print(f"Difference (B - A): {diff_b}")

# Symmetric difference (elements in either, but not both)
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (A ^ B): {sym_diff}")

# ========== SET COMPARISONS ==========
print("\n" + "=" * 50)
print("SET COMPARISONS")
print("=" * 50)

small = {1, 2, 3}
large = {1, 2, 3, 4, 5}

print(f"Small: {small}")
print(f"Large: {large}")

# Subset check
print(f"\nIs small subset of large? {small.issubset(large)}")
print(f"Using <=: {small <= large}")

# Superset check
print(f"\nIs large superset of small? {large.issuperset(small)}")
print(f"Using >=: {large >= small}")

# Disjoint (no common elements)
set_x = {1, 2, 3}
set_y = {4, 5, 6}
print(f"\nSet X: {set_x}")
print(f"Set Y: {set_y}")
print(f"Are X and Y disjoint? {set_x.isdisjoint(set_y)}")

# ========== SET MEMBERSHIP ==========
print("\n" + "=" * 50)
print("SET MEMBERSHIP (Very Fast!)")
print("=" * 50)

languages = {"Python", "Java", "JavaScript", "C++", "Ruby"}
print(f"Languages: {languages}")

print(f"\n'Python' in languages: {'Python' in languages}")
print(f"'Go' in languages: {'Go' in languages}")
print(f"'Go' not in languages: {'Go' not in languages}")

# ========== FROZEN SETS ==========
print("\n" + "=" * 50)
print("FROZEN SETS (Immutable Sets)")
print("=" * 50)

# Regular set - mutable
normal_set = {1, 2, 3}
normal_set.add(4)
print(f"Normal set (mutable): {normal_set}")

# Frozen set - immutable
frozen = frozenset([1, 2, 3])
print(f"Frozen set: {frozen}")

# frozen.add(4)  # This would cause an error

# Frozen sets can be dictionary keys or set elements
dict_with_frozen = {frozenset([1, 2]): "value"}
print(f"Dict with frozen key: {dict_with_frozen}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Remove duplicates from list
print("1. Remove duplicates:")
original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(original))
print(f"   Original: {original}")
print(f"   Unique: {unique}")

# Example 2: Find common elements
print("\n2. Find common friends:")
alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "Eve"}

common = alice_friends & bob_friends
print(f"   Alice's friends: {alice_friends}")
print(f"   Bob's friends: {bob_friends}")
print(f"   Common friends: {common}")

# Example 3: Find unique elements
print("\n3. Find who Alice knows but Bob doesn't:")
unique_to_alice = alice_friends - bob_friends
print(f"   Unique to Alice: {unique_to_alice}")

# Example 4: Tag system
print("\n4. Blog tag system:")
post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "data-science", "machine-learning"}
post3_tags = {"javascript", "web", "programming"}

# All unique tags
all_tags = post1_tags | post2_tags | post3_tags
print(f"   All tags: {all_tags}")

# Posts with 'python' tag
python_posts = [i+1 for i, tags in enumerate([post1_tags, post2_tags, post3_tags]) if "python" in tags]
print(f"   Posts with 'python' tag: {python_posts}")

# Example 5: Checking for anagrams
print("\n5. Anagram checker:")
def are_anagrams(word1, word2):
    return set(word1.lower()) == set(word2.lower()) and len(word1) == len(word2)

print(f"   'listen' and 'silent': {are_anagrams('listen', 'silent')}")
print(f"   'hello' and 'world': {are_anagrams('hello', 'world')}")

# Example 6: Count unique items
print("\n6. Unique visitors:")
visitors = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David", "Alice"]
unique_visitors = len(set(visitors))
print(f"   All visits: {visitors}")
print(f"   Unique visitors: {unique_visitors}")

print("\n" + "=" * 50)
print("✅ Sets - Complete!")
print("=" * 50)
