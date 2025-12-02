# Sets in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Sets](#introduction-to-sets)
2. [Creating Sets](#creating-sets)
3. [Set Operations](#set-operations)
4. [Set Methods](#set-methods)
5. [Set Comprehensions](#set-comprehensions)
6. [Frozensets](#frozensets)
7. [Set Use Cases](#set-use-cases)
8. [Performance Considerations](#performance-considerations)
9. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Create and manipulate sets
- ✅ Perform mathematical set operations
- ✅ Use set methods effectively
- ✅ Understand set vs list vs tuple
- ✅ Work with frozensets
- ✅ Apply sets to solve practical problems
- ✅ Understand set performance characteristics

---

## Introduction to Sets

### What are Sets?

**Sets** are unordered collections of unique elements. They automatically remove duplicates and are optimized for membership testing.

```python
# Set automatically removes duplicates
numbers = {1, 2, 3, 2, 1, 3}
print(numbers)  # {1, 2, 3}

# Sets are unordered
# {1, 2, 3} and {3, 2, 1} are the same set
```

**Real-World Analogy** 🌍

Think of a set like:
- **A collection of unique items** - No duplicates allowed
- **A bag of marbles** - Order doesn't matter, each marble is unique
- **A membership list** - Each person appears only once

### Key Characteristics

1. **Unordered** - No index-based access
2. **Unique elements** - Automatically removes duplicates
3. **Mutable** - Can add/remove elements (frozenset is immutable)
4. **Fast membership testing** - O(1) average case
5. **Elements must be hashable** - No lists or dicts as elements

```python
# Valid set elements (hashable)
valid = {1, 2.5, "text", (1, 2), True, None}

# Invalid set elements (unhashable)
# invalid = {[1, 2]}  # TypeError! Lists are unhashable
# invalid = {{1: 2}}  # TypeError! Dicts are unhashable
```

---

## Creating Sets

### Empty Set

```python
# ❌ WRONG - This creates a dictionary!
wrong = {}
print(type(wrong))  # <class 'dict'>

# ✅ CORRECT - Use set() constructor
empty = set()
print(type(empty))  # <class 'set'>
print(empty)  # set()
```

### Set with Initial Elements

```python
# Curly braces
fruits = {"apple", "banana", "orange"}

# set() constructor from list
numbers = set([1, 2, 3, 4, 5])

# From string (splits into characters)
chars = set("hello")
print(chars)  # {'h', 'e', 'l', 'o'} - 'l' appears once!

# From tuple
numbers = set((1, 2, 3))

# From range
numbers = set(range(5))  # {0, 1, 2, 3, 4}
```

### Removing Duplicates with Sets

```python
# Remove duplicates from list
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers_with_dupes))
print(unique_numbers)  # [1, 2, 3, 4, 5] (order may vary)

# Remove duplicate words
text = "the quick brown fox jumps over the lazy dog"
unique_words = set(text.split())
print(unique_words)
# {'lazy', 'dog', 'the', 'over', 'quick', 'fox', 'brown', 'jumps'}

# Count unique elements
print(f"Unique words: {len(unique_words)}")
```

---

## Set Operations

### Mathematical Set Operations

Sets support mathematical operations from set theory:

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
```

### Union (|) - All Elements from Both Sets

```python
# Using | operator
print(a | b)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Using union() method
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7, 8}

# Multiple sets
c = {9, 10}
print(a | b | c)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(a.union(b, c))  # Same result

# Practical example: Combine user lists
monday_users = {"Alice", "Bob", "Charlie"}
tuesday_users = {"Bob", "David", "Eve"}
all_users = monday_users | tuesday_users
print(all_users)  # {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
```

### Intersection (&) - Common Elements

```python
# Using & operator
print(a & b)  # {4, 5}

# Using intersection() method
print(a.intersection(b))  # {4, 5}

# Multiple sets
c = {4, 9, 10}
print(a & b & c)  # {4}

# Practical example: Find mutual friends
alice_friends = {"Bob", "Charlie", "David"}
bob_friends = {"Alice", "Charlie", "Eve"}
mutual_friends = alice_friends & bob_friends
print(mutual_friends)  # {'Charlie'}
```

### Difference (-) - Elements in First but Not Second

```python
# Using - operator
print(a - b)  # {1, 2, 3}
print(b - a)  # {6, 7, 8}

# Using difference() method
print(a.difference(b))  # {1, 2, 3}

# Practical example: Find exclusive items
all_items = {"apple", "banana", "orange", "grape"}
sold_items = {"banana", "grape"}
remaining_items = all_items - sold_items
print(remaining_items)  # {'apple', 'orange'}
```

### Symmetric Difference (^) - Elements in Either but Not Both

```python
# Using ^ operator
print(a ^ b)  # {1, 2, 3, 6, 7, 8}

# Using symmetric_difference() method
print(a.symmetric_difference(b))  # {1, 2, 3, 6, 7, 8}

# Practical example: Find unique preferences
alice_likes = {"pizza", "pasta", "burger"}
bob_likes = {"pizza", "sushi", "burger"}
unique_preferences = alice_likes ^ bob_likes
print(unique_preferences)  # {'pasta', 'sushi'}
```

### Subset and Superset

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2}

# Subset (<=) - all elements in a are in b
print(a <= b)  # True (a is subset of b)
print(a.issubset(b))  # True

# Proper subset (<) - subset but not equal
print(a < b)  # True
print(a < a)  # False (not proper subset of itself)

# Superset (>=) - all elements in other set are in this set
print(b >= a)  # True (b is superset of a)
print(b.issuperset(a))  # True

# Proper superset (>)
print(b > a)  # True
print(b > b)  # False

# Practical example: Check permissions
required_permissions = {"read", "write"}
user_permissions = {"read", "write", "execute"}
has_all_permissions = required_permissions <= user_permissions
print(f"Has permissions: {has_all_permissions}")  # True
```

### Disjoint Sets

```python
# Sets with no common elements
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))  # True (no common elements)

c = {3, 4, 5}
print(a.isdisjoint(c))  # False (3 is common)

# Practical example: Check for conflicts
morning_class = {"Alice", "Bob"}
afternoon_class = {"Charlie", "David"}
has_conflicts = not morning_class.isdisjoint(afternoon_class)
print(f"Has conflicts: {has_conflicts}")  # False
```

---

## Set Methods

### Adding Elements

```python
fruits = {"apple", "banana"}

# add() - add single element
fruits.add("orange")
print(fruits)  # {'apple', 'banana', 'orange'}

# Adding duplicate (no effect)
fruits.add("apple")
print(fruits)  # Still {'apple', 'banana', 'orange'}

# update() - add multiple elements
fruits.update(["grape", "mango"])
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'mango'}

# Update with multiple iterables
fruits.update(["kiwi"], {"pear"}, ("peach",))

# Update using | operator (union update)
fruits |= {"cherry", "plum"}
```

### Removing Elements

```python
fruits = {"apple", "banana", "orange", "grape"}

# remove() - removes element, raises KeyError if not found
fruits.remove("banana")
print(fruits)  # {'apple', 'orange', 'grape'}

# Raises error if element doesn't exist
# fruits.remove("mango")  # KeyError!

# discard() - removes element, no error if not found
fruits.discard("orange")
print(fruits)  # {'apple', 'grape'}

fruits.discard("mango")  # No error, just does nothing

# pop() - removes and returns arbitrary element
fruit = fruits.pop()
print(f"Popped: {fruit}")
print(fruits)  # One element removed

# clear() - removes all elements
fruits.clear()
print(fruits)  # set()
```

### Copying Sets

```python
original = {1, 2, 3, 4, 5}

# copy() - shallow copy
copy = original.copy()
copy.add(6)
print(original)  # {1, 2, 3, 4, 5} (unchanged)
print(copy)      # {1, 2, 3, 4, 5, 6}

# Alternative: use set() constructor
copy2 = set(original)
```

### Set Comparison

```python
a = {1, 2, 3}
b = {1, 2, 3}
c = {3, 2, 1}  # Same elements, different order

# Equality (order doesn't matter!)
print(a == b)  # True
print(a == c)  # True

# Inequality
d = {1, 2, 4}
print(a != d)  # True
```

---

## Set Comprehensions

### Basic Set Comprehension

```python
# Squares of numbers 0-9
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Uppercase letters
text = "hello world"
uppercase = {ch.upper() for ch in text if ch.isalpha()}
print(uppercase)  # {'E', 'H', 'L', 'O', 'R', 'W', 'D'}

# Lengths of words
words = ["hello", "world", "hi", "goodbye"]
lengths = {len(word) for word in words}
print(lengths)  # {2, 5, 7}
```

### Set Comprehension with Condition

```python
# Even numbers
evens = {x for x in range(20) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# Vowels from text
text = "hello world"
vowels = {ch for ch in text if ch in 'aeiou'}
print(vowels)  # {'e', 'o'}

# Unique word lengths > 3
words = ["hi", "hello", "world", "hey", "goodbye"]
long_lengths = {len(w) for w in words if len(w) > 3}
print(long_lengths)  # {5, 7}
```

---

## Frozensets

### Creating Frozensets

```python
# Immutable set
frozen = frozenset([1, 2, 3, 4, 5])
print(frozen)  # frozenset({1, 2, 3, 4, 5})

# From set
regular_set = {1, 2, 3}
frozen = frozenset(regular_set)

# Can't modify frozenset!
# frozen.add(6)  # AttributeError!
# frozen.remove(1)  # AttributeError!
```

### Why Use Frozensets?

```python
# 1. As dictionary keys (sets can't be dict keys!)
locations = {
    frozenset([1, 2]): "Point A",
    frozenset([3, 4]): "Point B"
}
print(locations[frozenset([1, 2])])  # "Point A"

# 2. As set elements (sets can't contain sets!)
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}

# 3. When you need immutability guarantee
def process_ids(ids):
    # Convert to frozenset to ensure it won't be modified
    return frozenset(ids)
```

### Frozenset Operations

```python
# All set operations work on frozensets
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a | b)  # frozenset({1, 2, 3, 4, 5})
print(a & b)  # frozenset({3})
print(a - b)  # frozenset({1, 2})
```

---

## Set Use Cases

### 1. Remove Duplicates

```python
# From list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))

# From string (get unique characters)
text = "hello"
unique_chars = set(text)  # {'h', 'e', 'l', 'o'}

# Count unique items
count = len(set(numbers))
```

### 2. Membership Testing (Fast!)

```python
# Check if element exists (O(1) average case)
valid_users = {"alice", "bob", "charlie"}

username = "alice"
if username in valid_users:  # Very fast!
    print("Valid user")

# Compare to list (O(n))
valid_users_list = ["alice", "bob", "charlie"]
if username in valid_users_list:  # Slower for large lists
    print("Valid user")
```

### 3. Find Common Elements

```python
# Common interests
alice_interests = {"coding", "reading", "gaming"}
bob_interests = {"gaming", "sports", "reading"}
common = alice_interests & bob_interests
print(common)  # {'reading', 'gaming'}
```

### 4. Find Unique Elements

```python
# Items only Alice has
alice_only = alice_interests - bob_interests
print(alice_only)  # {'coding'}

# Items only one person has
unique_to_each = alice_interests ^ bob_interests
print(unique_to_each)  # {'coding', 'sports'}
```

### 5. Check for Duplicates

```python
# Check if list has duplicates
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
has_duplicates = len(numbers) != len(set(numbers))
print(f"Has duplicates: {has_duplicates}")  # False

numbers_with_dupes = [1, 2, 2, 3]
has_duplicates = len(numbers_with_dupes) != len(set(numbers_with_dupes))
print(f"Has duplicates: {has_duplicates}")  # True
```

### 6. Filter Data

```python
# Remove banned words
text = "hello world hello python"
banned_words = {"hello", "world"}
words = text.split()
filtered = [w for w in words if w not in banned_words]
print(filtered)  # ['python']
```

---

## Performance Considerations

### Time Complexity

```python
# O(1) - Average case
x in set_obj          # Membership test
set_obj.add(x)        # Add element
set_obj.remove(x)     # Remove element  
set_obj.discard(x)    # Discard element

# O(len(s)) - Linear in set size
set(iterable)         # Create set from iterable
set_obj.copy()        # Copy set

# O(len(s1) + len(s2))
s1 | s2              # Union
s1 & s2              # Intersection
s1 - s2              # Difference
s1 ^ s2              # Symmetric difference
```

### Set vs List Performance

```python
import time

# Create large collections
large_list = list(range(100000))
large_set = set(range(100000))

# Membership test - Set is MUCH faster
start = time.time()
99999 in large_list  # O(n) - slow
print(f"List: {time.time() - start}")

start = time.time()
99999 in large_set   # O(1) - fast!
print(f"Set: {time.time() - start}")
```

### When to Use Sets

✅ **Use Sets When:**
- Need unique elements
- Frequent membership testing
- Need set operations (union, intersection, etc.)
- Order doesn't matter

❌ **Don't Use Sets When:**
- Need to maintain order
- Need index-based access
- Need duplicate elements
- Elements aren't hashable

---

## Practice Exercises

### Beginner

**Exercise 1**: Create set from list and remove duplicates
```python
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# Create set to get unique numbers
```

**Exercise 2**: Check if element exists in set
```python
fruits = {"apple", "banana", "orange"}
# Check if "banana" is in set
```

**Exercise 3**: Add elements to set
```python
colors = {"red", "blue"}
# Add "green" and "yellow"
```

**Exercise 4**: Find union of two sets
```python
a = {1, 2, 3}
b = {3, 4, 5}
# Find union
```

**Exercise 5**: Find intersection of two sets
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Find common elements
```

### Intermediate

**Exercise 6**: Remove elements from set
```python
numbers = {1, 2, 3, 4, 5}
# Remove 3 using remove(), try removing 10 using discard()
```

**Exercise 7**: Check if one set is subset of another
```python
a = {1, 2}
b = {1, 2, 3, 4}
# Check if a is subset of b
```

**Exercise 8**: Find symmetric difference
```python
a = {1, 2, 3}
b = {3, 4, 5}
# Find elements in either set but not both
```

**Exercise 9**: Use set comprehension
```python
# Create set of squares of even numbers from 0 to 20
```

**Exercise 10**: Count unique words in sentence
```python
sentence = "the quick brown fox jumps over the lazy dog the fox"
# Count unique words
```

### Advanced

**Exercise 11**: Find common elements in three sets
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 5, 6, 7}
# Find elements common to all three
```

**Exercise 12**: Use frozenset as dictionary key
```python
# Create dictionary mapping frozensets to values
# frozenset([1, 2]) -> "Group A"
# frozenset([3, 4]) -> "Group B"
```

**Exercise 13**: Find students in all classes
```python
class1 = {"Alice", "Bob", "Charlie"}
class2 = {"Bob", "David"}
class3 = {"Bob", "Eve"}
# Find students common to all classes
```

**Exercise 14**: Check if lists have same elements (ignoring order)
```python
list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
# Check if they contain same elements
```

**Exercise 15**: Remove all vowels from string using sets
```python
text = "hello world"
vowels = set("aeiouAEIOU")
# Remove all vowels
```

---

## 🎯 Key Takeaways

✅ Sets are **unordered** collections of **unique** elements  
✅ Use **{}** or **set()** to create (not {} for empty!)  
✅ Sets **automatically remove duplicates**  
✅ **Fast membership testing** - O(1) average  
✅ Set operations: **| & - ^** (union, intersection, difference, symmetric difference)  
✅ **Frozenset** is immutable version  
✅ Elements must be **hashable** (no lists/dicts)  
✅ Use for: deduplication, fast lookups, set math  

---

## 📚 Quick Reference

```python
# Creation
s = {1, 2, 3}
s = set([1, 2, 3])
empty = set()

# Adding/Removing
s.add(x)
s.update([a, b])
s.remove(x)      # KeyError if not found
s.discard(x)     # No error
s.pop()          # Remove arbitrary
s.clear()        # Remove all

# Set Operations
a | b            # Union
a & b            # Intersection
a - b            # Difference
a ^ b            # Symmetric difference

# Tests
a <= b           # Subset
a >= b           # Superset
a.isdisjoint(b)  # No common elements

# Comprehension
{x**2 for x in range(10)}
{x for x in range(20) if x % 2 == 0}

# Frozenset
fs = frozenset([1, 2, 3])
```

---

**End of Sets Notes** 📝

Master sets for efficient Python programming!

## Advanced Set Patterns

### Pattern 1: Finding Unique Elements Across Lists

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]

# Elements in all three lists
common = set(list1) & set(list2) & set(list3)
print(f"Common: {common}")  # {5}

# Elements in at least one list
all_elements = set(list1) | set(list2) | set(list3)
print(f"All: {all_elements}")  # {1,2,3,4,5,6,7,8,9}

# Elements unique to each list
unique_to_list1 = set(list1) - set(list2) - set(list3)
print(f"Unique to list1: {unique_to_list1}")  # {1, 2, 3}
```

### Pattern 2: Set-Based Data Validation

```python
# Valid user roles
VALID_ROLES = {"admin", "editor", "viewer", "guest"}

def validate_user_roles(user_roles):
    """Check if all roles are valid"""
    user_set = set(user_roles)
    invalid = user_set - VALID_ROLES
    
    if invalid:
        print(f"Invalid roles: {invalid}")
        return False
    return True

# Test
user_roles = ["admin", "editor", "superuser"]
if validate_user_roles(user_roles):
    print("All roles valid!")
else:
    print("Some roles invalid!")
```

### Pattern 3: Efficient Duplicate Detection

```python
def has_duplicates(items):
    """Check if list has duplicates using set"""
    return len(items) != len(set(items))

def find_duplicates(items):
    """Find all duplicate items"""
    seen = set()
    duplicates = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return duplicates

numbers = [1, 2, 3, 2, 4, 5, 3]
print(f"Has duplicates: {has_duplicates(numbers)}")  # True
print(f"Duplicates: {find_duplicates(numbers)}")      # {2, 3}
```

---

## Set Performance Analysis

### Time Complexity

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| `x in s` | O(1) | O(n) |
| `s.add(x)` | O(1) | O(n) |
| `s.remove(x)` | O(1) | O(n) |
| `s & t` | O(min(len(s), len(t))) | O(len(s) * len(t)) |
| `s | t` | O(len(s) + len(t)) | - |

### When Sets Win

```python
import time

# Membership testing: Set vs List
large_list = list(range(100000))
large_set = set(range(100000))

# Test with list (slow!)
start = time.time()
99999 in large_list
list_time = time.time() - start

# Test with set (fast!)
start = time.time()
99999 in large_set
set_time = time.time() - start

print(f"List: {list_time:.6f}s")
print(f"Set: {set_time:.6f}s")
print(f"Set is {list_time/set_time:.0f}x faster!")
```

---

## Set Gotchas and Solutions

### Gotcha 1: Mutable Elements Not Allowed

```python
# ❌ Can't add lists to sets
# my_set = {[1, 2], [3, 4]}  # TypeError!

# ✅ Use tuples instead
my_set = {(1, 2), (3, 4)}  # Works!

# ❌ Can't add dicts to sets
# my_set = {{'a': 1}}  # TypeError!

# ✅ Use frozenset or tuple of items
my_set = {frozenset({'a': 1}.items())}  # Works!
```

### Gotcha 2: Set Order is Not Guaranteed

```python
# Don't rely on set order!
numbers = {3, 1, 4, 1, 5, 9, 2, 6}
print(numbers)  # Order may vary!

# If order matters, use list(set(...))
ordered = sorted(set(numbers))
print(ordered)  # [1, 2, 3, 4, 5, 6, 9]
```

### Gotcha 3: Empty Set Requires set()

```python
# ❌ This creates an empty dict!
empty = {}
print(type(empty))  # <class 'dict'>

# ✅ Use set() for empty set
empty = set()
print(type(empty))  # <class 'set'>
```

---

## Real-World Applications

### Application 1: Finding Common Friends

```python
# Social network: find mutual friends
alice_friends = {"Bob", "Charlie", "Dave", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "George"}

mutual_friends = alice_friends & bob_friends
print(f"Mutual friends: {mutual_friends}")  # {'Charlie'}

# Friend suggestions (friends of friends, not already friends)
suggestions = bob_friends - alice_friends - {"Bob"}
print(f"Suggestions for Alice: {suggestions}")  # {'Frank', 'George'}
```

### Application 2: Tag Management System

```python
class Article:
    def __init__(self, title, tags):
        self.title = title
        self.tags = set(tags)
    
    def add_tag(self, tag):
        self.tags.add(tag)
    
    def remove_tag(self, tag):
        self.tags.discard(tag)
    
    def has_tag(self, tag):
        return tag in self.tags
    
    def common_tags(self, other_article):
        return self.tags & other_article.tags

# Usage
article1 = Article("Python Basics", ["python", "programming", "tutorial"])
article2 = Article("Advanced Python", ["python", "advanced", "programming"])

common = article1.common_tags(article2)
print(f"Common tags: {common}")  # {'python', 'programming'}
```

### Application 3: Access Control

```python
class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = set(permissions)
    
    def has_permission(self, permission):
        return permission in self.permissions
    
    def grant_permission(self, permission):
        self.permissions.add(permission)
    
    def revoke_permission(self, permission):
        self.permissions.discard(permission)

# Usage
user = User("alice", ["read", "write"])
print(user.has_permission("read"))    # True
print(user.has_permission("delete"))  # False

user.grant_permission("delete")
print(user.has_permission("delete"))  # True
```

---

## Set vs FrozenSet Decision Guide

### Use Set When:
- ✅ Need to add/remove elements
- ✅ Data changes over time
- ✅ Don't need to use as dict key

```python
active_users = {"alice", "bob"}
active_users.add("charlie")  # Can modify
```

### Use Frozenset When:
- ✅ Need immutable set
- ✅ Want to use as dict key
- ✅ Want to add to another set

```python
# Use as dict key
permissions = {
    frozenset(["read", "write"]): "editor",
    frozenset(["read"]): "viewer"
}

# Add to set
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4])
}
```

---

## Set Comprehension Power

### Complex Filtering

```python
# Get unique word lengths from text
text = "the quick brown fox jumps over the lazy dog"
word_lengths = {len(word) for word in text.split()}
print(word_lengths)  # {3, 4, 5}

# Get all vowels in text
vowels = {char for char in text.lower() if char in 'aeiou'}
print(vowels)  # {'e', 'o', 'i', 'u', 'a'}

# Squares of even numbers
even_squares = {x**2 for x in range(20) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64, 100, ...}
```

---

## Best Practices Summary

### DO's ✅

1. **Use sets for membership testing**
2. **Use sets to remove duplicates**
3. **Use set operations for logic (union, intersection, etc.)**
4. **Use frozensets when immutability needed**
5. **Convert to list when order matters**

### DON'Ts ❌

1. **Don't use `{}` for empty set** (that's a dict!)
2. **Don't expect order to be preserved**
3. **Don't try to add mutable objects**
4. **Don't use when duplicates matter**
5. **Don't use when order matters**

---

**End of Sets Notes** ���

Master sets for efficient, unique element management in your Python programs!
