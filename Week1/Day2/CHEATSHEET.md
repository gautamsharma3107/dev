# Day 2 Quick Reference Cheat Sheet

## Lists
```python
# Create
fruits = ["apple", "banana", "cherry"]
nums = list(range(1, 6))

# Access
fruits[0]      # First
fruits[-1]     # Last
fruits[1:3]    # Slice

# Modify
fruits.append("date")       # Add end
fruits.insert(1, "berry")   # Add at index
fruits.extend(["e", "f"])   # Add multiple
fruits.remove("apple")      # Remove by value
fruits.pop()                # Remove last
fruits.pop(0)               # Remove by index

# Methods
len(fruits)
sorted(fruits)
fruits.sort()
fruits.reverse()
fruits.count("apple")
fruits.index("banana")

# Iteration
for fruit in fruits:
for i, fruit in enumerate(fruits):
```

## Dictionaries
```python
# Create
person = {"name": "Gautam", "age": 25}
person = dict(name="Gautam", age=25)

# Access
person["name"]
person.get("name", "default")

# Modify
person["city"] = "Delhi"    # Add/Update
person.update({"a": 1})     # Update multiple
del person["age"]           # Delete
person.pop("name")          # Remove and return

# Methods
person.keys()
person.values()
person.items()
"name" in person            # Check key

# Iteration
for key in person:
for key, value in person.items():
```

## Tuples
```python
# Create
point = (10, 20)
single = (42,)              # Single element needs comma

# Unpacking
x, y = point
a, *rest, b = (1, 2, 3, 4, 5)

# Methods
point.count(10)
point.index(20)
```

## Sets
```python
# Create
nums = {1, 2, 3}
unique = set([1, 2, 2, 3])  # Remove duplicates

# Methods
nums.add(4)
nums.remove(1)              # Error if missing
nums.discard(1)             # No error

# Operations
a | b    # Union
a & b    # Intersection
a - b    # Difference
a ^ b    # Symmetric difference

# Check
a.issubset(b)
a.issuperset(b)
```

## List Comprehensions
```python
# Basic
[x**2 for x in range(5)]

# With condition
[x for x in range(10) if x % 2 == 0]

# With if-else
["even" if x%2==0 else "odd" for x in range(5)]

# Dictionary comprehension
{x: x**2 for x in range(5)}

# Set comprehension
{x**2 for x in range(-3, 4)}
```

## Common Patterns
```python
# Remove duplicates (preserve order)
list(dict.fromkeys(my_list))

# Find max in dict by value
max(my_dict, key=my_dict.get)

# Merge dictionaries
merged = {**dict1, **dict2}

# Flatten nested list
[x for sublist in nested for x in sublist]

# Word frequency
{word: text.count(word) for word in set(text.split())}
```

---
**Keep this handy for Day 2 topics!** 🚀
