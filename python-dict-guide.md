# Python Dictionaries: Complete Guide

---

## Table of Contents
1. [Introduction to Dictionaries](#introduction-to-dictionaries)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing Dictionary Elements](#accessing-dictionary-elements)
4. [Modifying Dictionaries](#modifying-dictionaries)
5. [Dictionary Methods](#dictionary-methods)
6. [Dictionary Comprehensions](#dictionary-comprehensions)
7. [Nested Dictionaries](#nested-dictionaries)
8. [Dictionary vs Other Collections](#dictionary-vs-other-collections)
9. [Common Dictionary Use Cases](#common-dictionary-use-cases)
10. [Practice Exercises](#practice-exercises)

---

## Introduction to Dictionaries

### What is a Dictionary?
- **Key-value pairs** - data stored as mappings
- **Mutable** - can be changed after creation
- **Ordered** - maintains insertion order (Python 3.7+)
- **Unindexed** - accessed by keys, not by position
- **Unique keys** - no duplicate keys allowed
- **Fast lookup** - O(1) average time to access values
- **Flexible keys** - keys can be any immutable type (str, int, tuple, etc.)
- **Flexible values** - values can be any type

### Why Use Dictionaries?

1. **Fast Lookup** - Access values instantly by key
2. **Structured Data** - Organize related data together
3. **Named Access** - More readable than index-based (like in Java HashMap)
4. **Flexible** - Keys and values can be any type
5. **Real-World Mapping** - Perfect for database records, configuration, etc.

### Comparison with Other Collections

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Ordered | Yes | Yes | No | Yes (3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Unique | No | No | Yes | Keys unique |
| Indexed | Yes | Yes | No | Via keys |
| Key-value | No | No | No | Yes |
| Lookup Speed | O(n) | O(n) | O(1) | O(1) |

### Comparison with Other Languages

| Language | Equivalent |
|----------|-----------|
| Python   | dict      |
| Java     | HashMap   |
| C++      | std::map  |
| C#       | Dictionary<K,V> |
| JavaScript | Object or Map |

---

## Creating Dictionaries

### Empty Dictionary

```python
# Using curly braces
empty_dict1 = {}
print(type(empty_dict1))    # Output: <class 'dict'>

# Using dict() constructor
empty_dict2 = dict()
print(type(empty_dict2))    # Output: <class 'dict'>

print(len(empty_dict1))     # Output: 0
```

### Dictionary with Initial Key-Value Pairs

```python
# Basic dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Mixed value types
mixed_dict = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "nested_dict": {"key": "value"}
}
print(mixed_dict)
```

### Creating Dictionaries from Other Data

```python
# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print(dict_from_pairs)      # Output: {'a': 1, 'b': 2, 'c': 3}

# From two lists (using zip)
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))
print(dict_from_lists)      # Output: {'a': 1, 'b': 2, 'c': 3}

# With default values
dict_with_defaults = dict.fromkeys(["x", "y", "z"], 0)
print(dict_with_defaults)   # Output: {'x': 0, 'y': 0, 'z': 0}

# Different default types
dict_lists = dict.fromkeys(["a", "b"], [])
print(dict_lists)           # Output: {'a': [], 'b': []}
```

### Dictionary with Keyword Arguments

```python
# Using dict() with keyword arguments
settings = dict(
    theme="dark",
    language="en",
    notifications=True
)
print(settings)
# Output: {'theme': 'dark', 'language': 'en', 'notifications': True}
```

---

## Accessing Dictionary Elements

### Accessing by Key

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Direct access using square brackets
name = person["name"]
print(name)                 # Output: Alice

age = person["age"]
print(age)                  # Output: 25

# ERROR - KeyError if key doesn't exist
# print(person["email"])    # KeyError: 'email'
```

### Checking if Key Exists

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using 'in' operator
if "name" in person:
    print("Name exists")    # This prints

if "email" not in person:
    print("Email doesn't exist")  # This prints
```

### Safe Access with get()

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# get() returns None if key doesn't exist (no error)
name = person.get("name")
print(name)                 # Output: Alice

email = person.get("email")
print(email)                # Output: None

# Provide default value
email = person.get("email", "No email provided")
print(email)                # Output: No email provided

# Practical use
city = person.get("city", "Unknown")
print(city)                 # Output: New York
```

### Getting Dictionary Length

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(len(person))          # Output: 3
```

---

## Modifying Dictionaries

### Adding New Key-Value Pairs

```python
person = {"name": "Alice"}

# Add single key-value pair
person["age"] = 25
person["city"] = "New York"

print(person)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

### Updating Existing Values

```python
person = {
    "name": "Alice",
    "age": 25
}

# Update existing value
person["age"] = 26
person["name"] = "Alicia"

print(person)
# Output: {'name': 'Alicia', 'age': 26}
```

### Deleting Key-Value Pairs

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Delete specific key
del person["city"]
print(person)               # Output: {'name': 'Alice', 'age': 25}

# ERROR - KeyError if key doesn't exist
# del person["email"]       # KeyError: 'email'

# Delete all items
person.clear()
print(person)               # Output: {}
```

### Getting and Removing (pop)

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# pop() removes and returns value
city = person.pop("city")
print(city)                 # Output: New York
print(person)               # Output: {'name': 'Alice', 'age': 25}

# pop() with default
country = person.pop("country", "USA")
print(country)              # Output: USA (default used)
```

---

## Dictionary Methods

### keys()

Returns all keys in dictionary:

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

keys = person.keys()
print(keys)                 # Output: dict_keys(['name', 'age', 'city'])
print(list(keys))           # Output: ['name', 'age', 'city']

# Iterate over keys
for key in person.keys():
    print(key)

# Check if key exists
if "name" in person.keys():
    print("Name key exists")
```

### values()

Returns all values in dictionary:

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

values = person.values()
print(values)               # Output: dict_values(['Alice', 25, 'New York'])
print(list(values))         # Output: ['Alice', 25, 'New York']

# Iterate over values
for value in person.values():
    print(value)

# Check if value exists
if "Alice" in person.values():
    print("Alice is in values")
```

### items()

Returns all key-value pairs as tuples:

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

items = person.items()
print(items)
# Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

print(list(items))
# Output: [('name', 'Alice'), ('age', 25), ('city', 'New York')]

# Iterate and unpack
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 25
# city: New York
```

### get(key, default=None)

Returns value for key with optional default:

```python
person = {
    "name": "Alice",
    "age": 25
}

# Existing key
name = person.get("name")
print(name)                 # Output: Alice

# Non-existing key (returns None)
email = person.get("email")
print(email)                # Output: None

# Non-existing key with default
email = person.get("email", "not@provided.com")
print(email)                # Output: not@provided.com

# Practical use
age = person.get("age", 0)
print(age)                  # Output: 25
```

### update(other_dict)

Merges another dictionary into current:

```python
person1 = {
    "name": "Alice",
    "age": 25
}

person2 = {
    "age": 26,
    "city": "New York"
}

# Update with another dictionary
person1.update(person2)
print(person1)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Update with list of tuples
person1.update([("email", "alice@example.com"), ("age", 27)])
print(person1)
# Output: {'name': 'Alice', 'age': 27, 'city': 'New York', 'email': 'alice@example.com'}

# Update with keyword arguments
person1.update(phone="123-456-7890", city="Boston")
print(person1)
```

### pop(key, default=None)

Removes and returns value:

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Remove existing key
city = person.pop("city")
print(city)                 # Output: New York
print(person)               # Output: {'name': 'Alice', 'age': 25}

# Remove non-existing key with default
country = person.pop("country", "USA")
print(country)              # Output: USA

# ERROR - KeyError without default
# person.pop("email")       # KeyError: 'email'
```

### popitem()

Removes and returns last inserted key-value pair:

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Remove last item
last_item = person.popitem()
print(last_item)            # Output: ('city', 'New York')
print(person)               # Output: {'name': 'Alice', 'age': 25}

# Keep removing items
while person:
    key, value = person.popitem()
    print(f"Removed: {key} = {value}")
```

### setdefault(key, default=None)

Returns value if key exists; otherwise sets and returns default:

```python
person = {"name": "Alice"}

# Key exists - returns value
age = person.setdefault("name", 25)
print(age)                  # Output: Alice
print(person)               # Output: {'name': 'Alice'}

# Key doesn't exist - sets and returns default
email = person.setdefault("email", "unknown@example.com")
print(email)                # Output: unknown@example.com
print(person)
# Output: {'name': 'Alice', 'email': 'unknown@example.com'}

# No default provided - uses None
phone = person.setdefault("phone")
print(phone)                # Output: None
print(person)
# Output: {'name': 'Alice', 'email': 'unknown@example.com', 'phone': None}
```

### copy()

Creates shallow copy:

```python
original = {"name": "Alice", "age": 25}

copy_dict = original.copy()

# Modify copy
copy_dict["age"] = 26

print(original)             # Output: {'name': 'Alice', 'age': 25} (unchanged)
print(copy_dict)            # Output: {'name': 'Alice', 'age': 26}
```

### clear()

Removes all items:

```python
person = {"name": "Alice", "age": 25}

person.clear()
print(person)               # Output: {}
print(len(person))          # Output: 0
```

---

## Dictionary Comprehensions

### Basic Dictionary Comprehension

**Syntax:** `{key_expression: value_expression for item in iterable}`

```python
# Create dictionary from range
squares = {x: x**2 for x in range(5)}
print(squares)              # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Convert list to dictionary
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)         # Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

### Dictionary Comprehension with Conditions

```python
# Only even numbers
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)         # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Filter strings by length
words = ["apple", "bat", "cherry", "dog", "elephant"]
long_words = {word: len(word) for word in words if len(word) > 3}
print(long_words)           # Output: {'apple': 5, 'cherry': 6, 'elephant': 8}
```

### Dictionary Comprehension with if-else

```python
# Categorize numbers
numbers = range(1, 11)
categorized = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print(categorized)
# Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}
```

### Dictionary Comprehension from Two Lists

```python
# Combine two lists into dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(combined)             # Output: {'a': 1, 'b': 2, 'c': 3}

# Create with index
items = ["apple", "banana", "cherry"]
indexed = {i: item for i, item in enumerate(items)}
print(indexed)              # Output: {0: 'apple', 1: 'banana', 2: 'cherry'}
```

### Dictionary Comprehension from Dictionary

```python
# Transform values
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v*2 for k, v in original.items()}
print(doubled)              # Output: {'a': 2, 'b': 4, 'c': 6}

# Filter and transform
filtered = {k: v**2 for k, v in original.items() if v > 1}
print(filtered)             # Output: {'b': 4, 'c': 9}

# Swap keys and values
swapped = {v: k for k, v in original.items()}
print(swapped)              # Output: {1: 'a', 2: 'b', 3: 'c'}
```

### Nested Dictionary Comprehension

```python
# Create matrix as nested dictionary
matrix = {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
print(matrix)
# Output: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}

# Flatten nested dictionary
flat = {f"{k1}_{k2}": v for k1, v1 in matrix.items() for k2, v in v1.items()}
print(flat)
# Output: {'1_1': 1, '1_2': 2, '1_3': 3, '2_1': 2, '2_2': 4, '2_3': 6, '3_1': 3, '3_2': 6, '3_3': 9}
```

---

## Nested Dictionaries

### Creating Nested Dictionaries

```python
# Employee database
employees = {
    "emp001": {
        "name": "Alice",
        "department": "Engineering",
        "salary": 80000
    },
    "emp002": {
        "name": "Bob",
        "department": "HR",
        "salary": 60000
    },
    "emp003": {
        "name": "Charlie",
        "department": "Sales",
        "salary": 70000
    }
}

print(employees)
```

### Accessing Nested Dictionary Values

```python
employees = {
    "emp001": {
        "name": "Alice",
        "department": "Engineering",
        "salary": 80000
    },
    "emp002": {
        "name": "Bob",
        "department": "HR",
        "salary": 60000
    }
}

# Access nested value
alice_name = employees["emp001"]["name"]
print(alice_name)           # Output: Alice

alice_dept = employees["emp001"]["department"]
print(alice_dept)           # Output: Engineering

bob_salary = employees["emp002"]["salary"]
print(bob_salary)           # Output: 60000
```

### Modifying Nested Dictionary Values

```python
employees = {
    "emp001": {
        "name": "Alice",
        "salary": 80000
    }
}

# Modify nested value
employees["emp001"]["salary"] = 85000
print(employees["emp001"])  # Output: {'name': 'Alice', 'salary': 85000}

# Add new nested key
employees["emp001"]["promotion"] = "Senior Engineer"
print(employees["emp001"])
# Output: {'name': 'Alice', 'salary': 85000, 'promotion': 'Senior Engineer'}

# Add entire new employee
employees["emp002"] = {
    "name": "Bob",
    "salary": 60000
}
print(employees["emp002"])  # Output: {'name': 'Bob', 'salary': 60000}
```

### Iterating Over Nested Dictionaries

```python
employees = {
    "emp001": {"name": "Alice", "salary": 80000},
    "emp002": {"name": "Bob", "salary": 60000},
    "emp003": {"name": "Charlie", "salary": 70000}
}

# Iterate and display
for emp_id, emp_data in employees.items():
    print(f"{emp_id}: {emp_data['name']} - ${emp_data['salary']}")

# Output:
# emp001: Alice - $80000
# emp002: Bob - $60000
# emp003: Charlie - $70000
```

### Safe Access to Nested Dictionaries

```python
employees = {
    "emp001": {"name": "Alice", "salary": 80000}
}

# Unsafe - KeyError if keys don't exist
# print(employees["emp002"]["name"])  # KeyError

# Safe - using get()
employee_data = employees.get("emp002")
if employee_data:
    name = employee_data.get("name")
else:
    print("Employee not found")

# Chained get() (careful, returns None at first missing key)
emp_name = employees.get("emp002", {}).get("name")
print(emp_name)             # Output: None

# Better approach
emp_name = employees.get("emp001", {}).get("name", "Unknown")
print(emp_name)             # Output: Alice
```

### Complex Nested Structures

```python
# Company structure
company = {
    "name": "Tech Corp",
    "departments": {
        "engineering": {
            "team_lead": "Alice",
            "members": ["Bob", "Charlie", "Diana"],
            "projects": {
                "project_a": {"status": "active", "budget": 50000},
                "project_b": {"status": "planned", "budget": 30000}
            }
        },
        "sales": {
            "team_lead": "Eve",
            "members": ["Frank", "Grace"]
        }
    }
}

# Access deeply nested value
project_a_status = company["departments"]["engineering"]["projects"]["project_a"]["status"]
print(project_a_status)     # Output: active

# Iterate over nested structure
for dept_name, dept_info in company["departments"].items():
    print(f"\nDepartment: {dept_name}")
    print(f"Team Lead: {dept_info['team_lead']}")
    print(f"Members: {', '.join(dept_info['members'])}")
```

---

## Dictionary vs Other Collections

### Comprehensive Comparison

```python
# List - indexed, ordered, mutable
list_data = ["Alice", 25, "New York"]
print(list_data[0])         # Access by index

# Tuple - indexed, ordered, immutable
tuple_data = ("Alice", 25, "New York")
print(tuple_data[0])        # Access by index

# Set - unordered, unique, mutable
set_data = {"Alice", 25, "New York"}
# Cannot access by index or key

# Dictionary - key-value, ordered (3.7+), mutable
dict_data = {"name": "Alice", "age": 25, "city": "New York"}
print(dict_data["name"])    # Access by key

# Speed comparison
import timeit

dict_time = timeit.timeit('d = {"a": 1}; v = d["a"]', number=1000000)
list_time = timeit.timeit('l = ["a", 1]; v = l[0]', number=1000000)
print(f"Dict lookup: {dict_time:.4f}s, List access: {list_time:.4f}s")
# Dict is typically faster for lookups
```

### When to Use Each

| Use Case | Best Choice |
|----------|------------|
| Ordered data | List or Tuple |
| Key-value data | Dictionary |
| Changing data | List or Dictionary |
| Fixed data | Tuple |
| Unique elements | Set |
| Fast lookup by key | Dictionary |
| Named access | Dictionary or namedtuple |
| Database records | Dictionary or namedtuple |

---

## Common Dictionary Use Cases

### Configuration Settings

```python
# Application configuration
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin"
    },
    "app": {
        "debug": True,
        "version": "1.0.0",
        "max_connections": 100
    }
}

# Access settings
db_host = config["database"]["host"]
debug_mode = config["app"]["debug"]
```

### Counting Occurrences

```python
# Count word frequency
text = "hello world hello python python python"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)           # Output: {'hello': 2, 'world': 1, 'python': 3}

# Using dictionary comprehension
word_count2 = {word: words.count(word) for word in set(words)}
print(word_count2)
```

### Grouping Data

```python
# Group students by grade
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "B"},
    {"name": "Eve", "grade": "A"}
]

grouped = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped:
        grouped[grade] = []
    grouped[grade].append(student["name"])

print(grouped)
# Output: {'A': ['Alice', 'Charlie', 'Eve'], 'B': ['Bob', 'Diana']}
```

### Default Values with setdefault()

```python
# Counting with setdefault
text = "programming"
char_count = {}

for char in text:
    char_count.setdefault(char, 0)
    char_count[char] += 1

print(char_count)
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
```

### Transforming Data

```python
# Convert list of tuples to dictionary
data = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
scores = {name: score for name, score in data}
print(scores)               # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# Find max score
max_name = max(scores, key=scores.get)
print(max_name)             # Output: Bob

# Invert keys and values
inverted = {v: k for k, v in scores.items()}
print(inverted)             # Output: {85: 'Alice', 90: 'Bob', 78: 'Charlie'}
```

### Merging Dictionaries

```python
# Merge multiple dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged1 = {**dict1, **dict2}
print(merged1)              # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Merge with precedence
dict3 = {"b": 99, "e": 5}
merged2 = {**dict1, **dict3}  # dict3 overwrites dict1
print(merged2)              # Output: {'a': 1, 'b': 99, 'e': 5}

# Using update()
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(dict1_copy)           # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### JSON-like Data

```python
# Working with API responses (JSON-like structure)
user_data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "profile": {
        "avatar": "avatar.jpg",
        "bio": "Software Developer",
        "social": {
            "twitter": "@alice",
            "github": "alice-github"
        }
    }
}

# Access nested data
twitter = user_data["profile"]["social"]["twitter"]
print(twitter)              # Output: @alice

# Safe access
bio = user_data.get("profile", {}).get("bio", "No bio")
print(bio)                  # Output: Software Developer
```

---

## Practice Exercises

### 1. Basic Dictionary Operations
- Create a dictionary with 5 key-value pairs
- Access values using both direct access and get()
- Add, modify, and delete dictionary items

### 2. Dictionary Methods
- Use keys(), values(), items() to iterate
- Use update() to merge dictionaries
- Use pop() and setdefault() methods

### 3. Dictionary Comprehensions
- Create dictionary from range with squares
- Filter dictionary using comprehension
- Create dictionary from two lists using zip

### 4. Nested Dictionaries
- Create employee or student database structure
- Access deeply nested values safely
- Iterate and display nested data

### 5. Real-World Scenarios
- Count word frequency in text
- Group data by category
- Transform and invert dictionaries
- Merge multiple dictionaries

### 6. Complex Operations
- Find maximum/minimum values in dictionary
- Create inverted dictionaries
- Handle missing keys gracefully
- Work with JSON-like nested structures

---

# End of Notes
