# Python Sets: Complete Guide

---

## Table of Contents
1. [Introduction to Sets](#introduction-to-sets)
2. [Creating Sets](#creating-sets)
3. [Accessing Set Elements](#accessing-set-elements)
4. [Set Methods](#set-methods)
5. [Set Operations](#set-operations)
6. [Mathematical Set Operations](#mathematical-set-operations)
7. [Frozen Sets](#frozen-sets)
8. [Sets vs Other Collections](#sets-vs-other-collections)
9. [Common Set Use Cases](#common-set-use-cases)
10. [Practice Exercises](#practice-exercises)

---

## Introduction to Sets

### What is a Set?
- **Unordered collection** of elements (unlike lists and tuples)
- **Mutable** - can be changed after creation
- **Unique elements only** - duplicates automatically removed
- **Unindexed** - cannot access by index
- **Unhashable** - cannot be used as dictionary keys (but frozenset can)
- **Fast membership testing** - O(1) average time
- **No duplicates** - automatically eliminates duplicates

### Why Use Sets?

1. **Remove Duplicates** - Automatically keeps unique elements
2. **Membership Testing** - Fast checking if element exists
3. **Mathematical Operations** - Union, intersection, difference, etc.
4. **Eliminate Redundancy** - Perfect for unique data
5. **Set Theory** - Perform set operations like in mathematics

### Comparison with Other Collections

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Ordered | Yes | Yes | No | No (Python 3.7+ ordered) |
| Mutable | Yes | No | Yes | Yes |
| Unique | No | No | Yes | No (keys unique) |
| Indexed | Yes | Yes | No | Via keys |
| Dictionary Key | No | Yes | No | Via keys |
| Duplicates | Allowed | Allowed | Not allowed | N/A |

### Comparison with Other Languages

| Language | Equivalent |
|----------|-----------|
| Python   | set       |
| Java     | HashSet   |
| C++      | std::set  |
| C#       | HashSet<T> |

---

## Creating Sets

### Empty Set (Important!)

```python
# WRONG - this creates an empty dictionary, not a set!
wrong_empty = {}
print(type(wrong_empty))    # Output: <class 'dict'>

# CORRECT - use set() function
correct_empty = set()
print(type(correct_empty))  # Output: <class 'set'>
print(len(correct_empty))   # Output: 0
```

### Set with Elements

```python
# Using curly braces
numbers = {1, 2, 3, 4, 5}
print(numbers)              # Output: {1, 2, 3, 4, 5}

# Mixed data types
mixed = {1, "hello", 3.14, True}
print(mixed)                # Output: {1, 'hello', 3.14}

# Note: True equals 1, so only one appears
mixed2 = {1, True}
print(mixed2)               # Output: {1}
```

### Creating Sets from Iterables

```python
# From list (removes duplicates)
list_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
set_from_list = set(list_data)
print(set_from_list)        # Output: {1, 2, 3, 4}

# From string
string_data = "hello"
set_from_string = set(string_data)
print(set_from_string)      # Output: {'h', 'e', 'l', 'o'}

# From tuple
tuple_data = (1, 1, 2, 2, 3, 3)
set_from_tuple = set(tuple_data)
print(set_from_tuple)       # Output: {1, 2, 3}

# From range
set_from_range = set(range(5))
print(set_from_range)       # Output: {0, 1, 2, 3, 4}

# From dictionary (keys only)
dict_data = {"a": 1, "b": 2, "c": 3}
set_from_dict = set(dict_data)
print(set_from_dict)        # Output: {'a', 'b', 'c'}
```

### Sets Automatically Remove Duplicates

```python
# Duplicates are automatically removed
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)              # Output: {1, 2, 3}
print(len(numbers))         # Output: 3

# Practical use: remove duplicates from list
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = list(set(numbers_with_duplicates))
print(unique_numbers)       # Output: [1, 2, 3, 4] (order may vary)
```

---

## Accessing Set Elements

### Sets are Unindexed

```python
colors = {"red", "green", "blue"}

# ERROR - cannot access by index
# print(colors[0])  # TypeError: 'set' object is not subscriptable

# You must iterate to access elements
for color in colors:
    print(color)
```

### Checking Membership

```python
fruits = {"apple", "banana", "orange"}

# Check if element exists
if "banana" in fruits:
    print("Banana is in the set")

if "grape" not in fruits:
    print("Grape is not in the set")

# Get all elements
print(fruits)               # Output: {'apple', 'banana', 'orange'}
```

### Iterating Over Sets

```python
numbers = {1, 2, 3, 4, 5}

# Simple iteration
for num in numbers:
    print(num)

# With enumerate (index not meaningful)
for index, num in enumerate(numbers):
    print(f"{index}: {num}")
```

### Finding Set Length

```python
numbers = {1, 2, 3, 4, 5}
print(len(numbers))         # Output: 5

empty_set = set()
print(len(empty_set))       # Output: 0
```

---

## Set Methods

### add(element)

Adds single element to set:

```python
colors = {"red", "green"}

colors.add("blue")
print(colors)               # Output: {'red', 'green', 'blue'}

# Adding duplicate (no effect)
colors.add("red")
print(colors)               # Output: {'red', 'green', 'blue'} (no change)

# Adding different types
mixed = {1, "hello"}
mixed.add(3.14)
mixed.add(True)             # True equals 1, so might not add
print(mixed)                # Output: {1, 'hello', 3.14}
```

### update(iterable) or |=

Adds multiple elements from iterable:

```python
numbers = {1, 2, 3}

# Using update()
numbers.update([4, 5, 6])
print(numbers)              # Output: {1, 2, 3, 4, 5, 6}

# Update with another set
numbers.update({7, 8})
print(numbers)              # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Update with string (adds individual characters)
letters = {"a", "b"}
letters.update("cd")
print(letters)              # Output: {'a', 'b', 'c', 'd'}

# Using |= operator
set1 = {1, 2}
set1 |= {3, 4}
print(set1)                 # Output: {1, 2, 3, 4}
```

### remove(element)

Removes element; raises KeyError if not found:

```python
fruits = {"apple", "banana", "orange"}

fruits.remove("banana")
print(fruits)               # Output: {'apple', 'orange'}

# ERROR - KeyError if element doesn't exist
# fruits.remove("grape")    # KeyError: 'grape'
```

### discard(element)

Removes element; does nothing if not found:

```python
fruits = {"apple", "banana", "orange"}

fruits.discard("banana")
print(fruits)               # Output: {'apple', 'orange'}

# No error - silently does nothing
fruits.discard("grape")
print(fruits)               # Output: {'apple', 'orange'} (no change)
```

### pop()

Removes and returns arbitrary element:

```python
numbers = {1, 2, 3, 4, 5}

removed = numbers.pop()
print(removed)              # Output: one of the numbers (unpredictable)
print(numbers)              # Output: set with 4 elements

# On empty set, raises KeyError
empty = set()
# empty.pop()               # KeyError: 'pop from an empty set'
```

### clear()

Removes all elements:

```python
numbers = {1, 2, 3, 4, 5}

numbers.clear()
print(numbers)              # Output: set()
print(len(numbers))         # Output: 0
```

### copy()

Creates shallow copy:

```python
original = {1, 2, 3}
copy_set = original.copy()

copy_set.add(4)
print(original)             # Output: {1, 2, 3} (unchanged)
print(copy_set)             # Output: {1, 2, 3, 4}
```

---

## Set Operations

### Union (|)

Combines all elements from both sets (no duplicates):

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using | operator
union1 = set1 | set2
print(union1)               # Output: {1, 2, 3, 4, 5}

# Using union() method
union2 = set1.union(set2)
print(union2)               # Output: {1, 2, 3, 4, 5}

# Using |= operator (in-place)
set1_copy = set1.copy()
set1_copy |= set2
print(set1_copy)            # Output: {1, 2, 3, 4, 5}

# Multiple sets
set3 = {5, 6, 7}
union3 = set1 | set2 | set3
print(union3)               # Output: {1, 2, 3, 4, 5, 6, 7}
```

### Intersection (&)

Elements present in both sets:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using & operator
intersection1 = set1 & set2
print(intersection1)        # Output: {3, 4}

# Using intersection() method
intersection2 = set1.intersection(set2)
print(intersection2)        # Output: {3, 4}

# Using &= operator (in-place)
set1_copy = set1.copy()
set1_copy &= set2
print(set1_copy)            # Output: {3, 4}

# No common elements
set3 = {7, 8, 9}
intersection3 = set1 & set3
print(intersection3)        # Output: set()
```

### Difference (-)

Elements in first set but not in second:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using - operator
difference1 = set1 - set2
print(difference1)          # Output: {1, 2}

# Using difference() method
difference2 = set1.difference(set2)
print(difference2)          # Output: {1, 2}

# Using -= operator (in-place)
set1_copy = set1.copy()
set1_copy -= set2
print(set1_copy)            # Output: {1, 2}

# Order matters!
difference3 = set2 - set1
print(difference3)          # Output: {5, 6}
```

### Symmetric Difference (^)

Elements in either set but not in both:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using ^ operator
sym_diff1 = set1 ^ set2
print(sym_diff1)            # Output: {1, 2, 5, 6}

# Using symmetric_difference() method
sym_diff2 = set1.symmetric_difference(set2)
print(sym_diff2)            # Output: {1, 2, 5, 6}

# Using ^= operator (in-place)
set1_copy = set1.copy()
set1_copy ^= set2
print(set1_copy)            # Output: {1, 2, 5, 6}
```

---

## Mathematical Set Operations

### Subset (<= or <)

Check if set1 is subset of set2:

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# Using <= operator (subset, including equal)
print(set1 <= set2)         # Output: True
print(set1 <= set3)         # Output: True

# Using < operator (proper subset, must be smaller)
print(set1 < set2)          # Output: True
print(set1 < set3)          # Output: False

# Using issubset() method
print(set1.issubset(set2))  # Output: True
```

### Superset (>= or >)

Check if set1 is superset of set2:

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
set3 = {1, 2, 3, 4, 5}

# Using >= operator (superset, including equal)
print(set1 >= set2)         # Output: True
print(set1 >= set3)         # Output: True

# Using > operator (proper superset, must be larger)
print(set1 > set2)          # Output: True
print(set1 > set3)          # Output: False

# Using issuperset() method
print(set1.issuperset(set2))  # Output: True
```

### Disjoint (isdisjoint())

Check if sets have no common elements:

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

# Using isdisjoint() method
print(set1.isdisjoint(set2))  # Output: True (no common elements)
print(set1.isdisjoint(set3))  # Output: False (3 is common)

# Practical use
if set1.isdisjoint(set2):
    print("Sets have no overlap")
```

### Equality (==)

Check if sets are equal:

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {3, 1, 2}  # Order doesn't matter
set4 = {1, 2, 3, 4}

print(set1 == set2)         # Output: True
print(set1 == set3)         # Output: True (order irrelevant)
print(set1 == set4)         # Output: False
```

---

## Frozen Sets

### What are Frozen Sets?

- **Immutable** version of set
- **Cannot be modified** after creation
- **Hashable** - can be used as dictionary keys
- **Can contain in other sets**

### Creating Frozen Sets

```python
# From literal (not possible, use frozenset())
# frozen = {1, 2, 3} doesn't work for frozenset

# Using frozenset() function
frozen1 = frozenset([1, 2, 3])
print(frozen1)              # Output: frozenset({1, 2, 3})
print(type(frozen1))        # Output: <class 'frozenset'>

# From other iterables
frozen2 = frozenset("hello")
print(frozen2)              # Output: frozenset({'h', 'e', 'l', 'o'})

# Empty frozenset
frozen_empty = frozenset()
print(frozen_empty)         # Output: frozenset()
```

### Frozenset Immutability

```python
frozen = frozenset({1, 2, 3})

# ERROR - cannot modify
# frozen.add(4)             # AttributeError
# frozen.remove(1)          # AttributeError
# frozen.discard(1)         # AttributeError
# frozen.clear()            # AttributeError

print(frozen)               # Output: frozenset({1, 2, 3}) (unchanged)
```

### Frozenset as Dictionary Key

```python
# Regular set cannot be dictionary key
# ERROR: dict1 = {set({1, 2}): "value"}  # TypeError

# But frozenset can!
dict_with_frozen = {
    frozenset({1, 2}): "pair 1-2",
    frozenset({3, 4}): "pair 3-4",
    frozenset({5}): "single"
}

print(dict_with_frozen[frozenset({1, 2})])  # Output: pair 1-2
```

### Frozenset in Sets

```python
# Cannot have regular sets in sets
# ERROR: nested = {{1, 2}, {3, 4}}  # TypeError

# But can have frozensets in sets
nested = {frozenset({1, 2}), frozenset({3, 4}), frozenset({5})}
print(nested)
# Output: {frozenset({1, 2}), frozenset({3, 4}), frozenset({5})}

for fset in nested:
    print(fset)
```

### Frozenset Operations

```python
frozen1 = frozenset({1, 2, 3})
frozen2 = frozenset({3, 4, 5})

# All read-only operations work
union = frozen1 | frozen2
print(union)                # Output: frozenset({1, 2, 3, 4, 5})

intersection = frozen1 & frozen2
print(intersection)         # Output: frozenset({3})

difference = frozen1 - frozen2
print(difference)           # Output: frozenset({1, 2})

sym_diff = frozen1 ^ frozen2
print(sym_diff)             # Output: frozenset({1, 2, 4, 5})

# Result is frozenset (immutable)
print(type(union))          # Output: <class 'frozenset'>
```

### Frozenset Comparison

```python
frozen1 = frozenset({1, 2})
frozen2 = frozenset({1, 2})
frozen3 = frozenset({1, 2, 3})

print(frozen1 == frozen2)       # Output: True
print(frozen1 <= frozen3)       # Output: True (subset)
print(frozen3 > frozen1)        # Output: True (superset)
```

---

## Sets vs Other Collections

### Comprehensive Comparison

```python
# List - ordered, mutable, allows duplicates
list_data = [1, 2, 2, 3]

# Tuple - ordered, immutable, allows duplicates
tuple_data = (1, 2, 2, 3)

# Set - unordered, mutable, no duplicates
set_data = {1, 2, 3}

# Dictionary - key-value pairs, ordered (Python 3.7+), mutable
dict_data = {1: "a", 2: "b", 3: "c"}

# Frozenset - unordered, immutable, no duplicates
frozenset_data = frozenset({1, 2, 3})

# Accessing
print(list_data[0])         # Works
print(tuple_data[0])        # Works
# print(set_data[0])        # ERROR - no indexing
# print(frozenset_data[0])  # ERROR - no indexing

# Modifying
list_data[0] = 99           # Works
# tuple_data[0] = 99        # ERROR
set_data.add(4)             # Works
# frozenset_data.add(4)     # ERROR

# Using as key
dict1 = {tuple_data: "value"}   # Works
# dict2 = {list_data: "value"}  # ERROR
# dict3 = {set_data: "value"}   # ERROR
dict4 = {frozenset_data: "value"}  # Works
```

### When to Use Each

| Use Case | Best Choice |
|----------|------------|
| Ordered data | List or Tuple |
| Changing data | List |
| Fixed data | Tuple |
| Unique elements | Set |
| Dictionary key | Tuple or Frozenset |
| Key-value pairs | Dictionary |
| Thread-safe immutable | Tuple or Frozenset |
| Fast membership testing | Set or Frozenset |

---

## Common Set Use Cases

### Remove Duplicates from List

```python
numbers_with_dups = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Method 1: Convert to set (loses order)
unique1 = list(set(numbers_with_dups))
print(unique1)              # Order varies

# Method 2: Preserve order (with set for tracking)
unique2 = []
seen = set()
for num in numbers_with_dups:
    if num not in seen:
        unique2.append(num)
        seen.add(num)
print(unique2)              # Output: [1, 2, 3, 4] (ordered)
```

### Finding Common Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Convert to sets
set1 = set(list1)
set2 = set(list2)

# Find common elements
common = set1 & set2
print(common)               # Output: {3, 4, 5}
```

### Finding Unique Elements

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

# Elements in list1 only
unique_in_list1 = set1 - set2
print(unique_in_list1)      # Output: {1, 2}

# Elements in either but not both
all_unique = set1 ^ set2
print(all_unique)           # Output: {1, 2, 6, 7}
```

### Checking Subset/Superset Relationships

```python
required_skills = {"Python", "Java", "SQL"}
candidate1_skills = {"Python", "Java", "SQL", "C++"}
candidate2_skills = {"Python", "Java"}

# Check if candidate has all required skills
if required_skills <= candidate1_skills:
    print("Candidate 1 qualifies")  # This prints

if required_skills <= candidate2_skills:
    print("Candidate 2 qualifies")  # This doesn't print
```

### Finding Differences Between Collections

```python
original_ids = {1, 2, 3, 4, 5}
processed_ids = {2, 4, 6}

# IDs not yet processed
remaining = original_ids - processed_ids
print(remaining)            # Output: {1, 3, 5}

# New IDs that appeared
new_ids = processed_ids - original_ids
print(new_ids)              # Output: {6}
```

### Filtering with Sets

```python
# Fast filtering with set
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
vowels = set("aeiou")

# Count words starting with vowel
vowel_words = [w for w in words if w[0] in vowels]
print(vowel_words)          # Output: ['apple', 'apple']

# Check if word contains specific letters
word = "hello"
letter_set = set(word)
print(letter_set)           # Output: {'h', 'e', 'l', 'o'}
```

### Venn Diagram Logic

```python
# Students in different activities
math_club = {"Alice", "Bob", "Charlie", "Diana"}
chess_club = {"Bob", "Diana", "Eve", "Frank"}
coding_club = {"Alice", "Eve", "Grace"}

# Only in math
only_math = math_club - chess_club - coding_club
print(only_math)            # Output: {'Charlie'}

# In all three
in_all = math_club & chess_club & coding_club
print(in_all)               # Output: set() (empty)

# In math and chess but not coding
math_and_chess = (math_club & chess_club) - coding_club
print(math_and_chess)       # Output: {'Bob', 'Diana'}

# In at least one
in_any = math_club | chess_club | coding_club
print(in_any)
# Output: {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'}
```

---

## Practice Exercises

### 1. Basic Set Creation
- Create a set of numbers and add/remove elements
- Create set from list with duplicates
- Create empty set correctly (avoid dictionary)

### 2. Set Methods
- Use add(), update(), remove(), discard(), pop()
- Understand the difference between remove() and discard()
- Clear a set and verify it's empty

### 3. Set Operations
- Perform union, intersection, difference operations
- Use both operators (|, &, -, ^) and methods
- Combine more than two sets

### 4. Mathematical Operations
- Check subset and superset relationships
- Verify if sets are disjoint
- Use comparison operators (<, >, <=, >=)

### 5. Frozen Sets
- Create frozenset and verify immutability
- Use frozenset as dictionary key
- Create set of frozensets

### 6. Real-World Scenarios
- Remove duplicates from a list of names
- Find common interests between two people
- Track processed IDs and find remaining ones
- Analyze Venn diagram relationships between groups
- Filter data based on set membership

---

# End of Notes
