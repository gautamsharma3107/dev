# Dictionaries in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to Dictionaries](#introduction-to-dictionaries)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing Dictionary Elements](#accessing-dictionary-elements)
4. [Modifying Dictionaries](#modifying-dictionaries)
5. [Dictionary Methods](#dictionary-methods)
6. [Dictionary Operations](#dictionary-operations)
7. [Nested Dictionaries](#nested-dictionaries)
8. [Dictionary Comprehensions](#dictionary-comprehensions)
9. [Advanced Dictionary Topics](#advanced-dictionary-topics)
10. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Create and manipulate dictionaries
- ✅ Access, add, modify, and remove key-value pairs
- ✅ Master 15+ dictionary methods
- ✅ Work with nested dictionaries
- ✅ Use dictionary comprehensions
- ✅ Understand dictionary use cases and patterns
- ✅ Apply best practices for dictionary usage

---

## Introduction to Dictionaries

### What are Dictionaries?

**Dictionaries** are unordered collections of key-value pairs. They store data as mappings where each unique key maps to a value.

```python
# Simple dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access value by key
print(person["name"])  # "Alice"
```

**Real-World Analogy** 🌍

Think of a dictionary like a real dictionary or phone book:
- **Key** = Word (or name)
- **Value** = Definition (or phone number)
- You look up information using the key

### Key Characteristics

1. **Key-Value Pairs** - Data stored as pairs
2. **Unordered** (Python 3.7+ maintains insertion order)
3. **Mutable** - Can be changed after creation
4. **Keys must be unique** - No duplicate keys
5. **Keys must be immutable** - Strings, numbers, tuples (not lists)

```python
# Valid keys
valid = {
    "string_key": "value1",
    42: "value2",
    (1, 2): "value3"
}

# Invalid key
# invalid = {[1, 2]: "value"}  # TypeError! Lists are mutable
```

---

## Creating Dictionaries

### Empty Dictionary

```python
# Method 1: Curly braces
empty = {}

# Method 2: dict() constructor
also_empty = dict()

print(len(empty))  # 0
```

### Dictionary with Initial Values

```python
# Basic dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Mixed value types
data = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "nested_dict": {"a": 1, "b": 2}
}

# Keys can be different types (but usually same type)
mixed_keys = {
    "text": "value1",
    42: "value2",
    (1, 2): "value3"
}
```

### Using dict() Constructor

```python
# From keyword arguments
person = dict(name="Alice", age=25, city="New York")

# From list of tuples
pairs = [("name", "Bob"), ("age", 30)]
person = dict(pairs)

# From two lists (zip)
keys = ["name", "age", "city"]
values = ["Charlie", 35, "LA"]
person = dict(zip(keys, values))
```

### fromkeys() Method

```python
# Create dict with same value for all keys
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
# {'a': 0, 'b': 0, 'c': 0}

# Without value argument (defaults to None)
keys_dict = dict.fromkeys(["x", "y", "z"])
# {'x': None, 'y': None, 'z': None}
```

---

## Accessing Dictionary Elements

### Using Square Brackets []

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Access value
print(person["name"])  # "Alice"
print(person["age"])   # 25

# KeyError if key doesn't exist
# print(person["email"])  # KeyError!
```

### Using get() Method

```python
person = {"name": "Alice", "age": 25}

# get(key) - returns None if key doesn't exist
print(person.get("name"))   # "Alice"
print(person.get("email"))  # None (no error!)

# get(key, default) - returns default if key doesn't exist
print(person.get("email", "Not provided"))  # "Not provided"
```

### Checking if Key Exists

```python
person = {"name": "Alice", "age": 25}

# Using 'in' operator
if "email" in person:
    print(person["email"])
else:
    print("Email not found")

# Check for non-existence
if "phone" not in person:
    print("Phone number not provided")
```

---

## Modifying Dictionaries

### Adding/Updating Items

```python
person = {"name": "Alice", "age": 25}

# Add new key-value pair
person["email"] = "alice@email.com"
# {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'}

# Update existing value
person["age"] = 26
# {'name': 'Alice', 'age': 26, 'email': 'alice@email.com'}

# Multiple updates using update()
person.update({"city": "NYC", "country": "USA"})
# Adds both new pairs
```

### Removing Items

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# pop(key) - remove and return value
age = person.pop("age")
print(age)     # 25
print(person)  # {'name': 'Alice', 'city': 'NYC'}

# pop with default (no error if key missing)
email = person.pop("email", "Not found")
print(email)  # "Not found"

# popitem() - remove and return last inserted pair (Python 3.7+)
item = person.popitem()
print(item)    # ('city', 'NYC')
print(person)  # {'name': 'Alice'}

# del statement - remove by key
person = {"name": "Alice", "age": 25, "city": "NYC"}
del person["age"]
print(person)  # {'name': 'Alice', 'city': 'NYC'}

# clear() - remove all items
person.clear()
print(person)  # {}
```

---

## Dictionary Methods

### keys(), values(), items()

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# keys() - get all keys
keys = person.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])
print(list(keys))  # ['name', 'age', 'city']

# values() - get all values
values = person.values()
print(list(values))  # ['Alice', 25, 'NYC']

# items() - get all key-value pairs as tuples
items = person.items()
print(list(items))  
# [('name', 'Alice'), ('age', 25), ('city', 'NYC')]

# Iterate using items()
for key, value in person.items():
    print(f"{key}: {value}")
# name: Alice
# age: 25
# city: NYC
```

### get(key[, default])

```python
person = {"name": "Alice", "age": 25}

# Basic usage
print(person.get("name"))  # "Alice"
print(person.get("email")) # None

# With default value
email = person.get("email", "not@provided.com")
print(email)  # "not@provided.com"

# Useful in calculations
count = person.get("login_count", 0) + 1
print(count)  # 1 (0 + 1)
```

### setdefault(key[, default])

```python
person = {"name": "Alice"}

# Get value, set default if key doesn't exist
age = person.setdefault("age", 0)
print(age)     # 0
print(person)  # {'name': 'Alice', 'age': 0}

# If key exists, returns existing value
name = person.setdefault("name", "Unknown")
print(name)    # "Alice" (not changed)
```

### update(other)

```python
person = {"name": "Alice", "age": 25}

# Update from another dict
person.update({"city": "NYC", "country": "USA"})
print(person)
# {'name': 'Alice', 'age': 25, 'city': 'NYC', 'country': 'USA'}

# Update existing + add new
person.update({"age": 26, "email": "alice@email.com"})
print(person)
# age updated to 26, email added

# Update from keyword arguments
person.update(phone="555-1234", zip_code="10001")
```

### copy()

```python
original = {"a": 1, "b": 2}
copy = original.copy()

copy["c"] = 3
print(original)  # {'a': 1, 'b': 2} (unchanged)
print(copy)      # {'a': 1, 'b': 2, 'c': 3}

# Shallow copy warning!
original = {"data": [1, 2, 3]}
copy = original.copy()
copy["data"].append(4)
print(original)  # {'data': [1, 2, 3, 4]} (modified!)
# The list is shared!
```

---

## Dictionary Operations

### Iteration

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Iterate keys (default)
for key in person:
    print(key)
# name
# age
# city

# Iterate values
for value in person.values():
    print(value)
# Alice
# 25
# NYC

# Iterate key-value pairs (best for most cases)
for key, value in person.items():
    print(f"{key} = {value}")
# name = Alice
# age = 25  
# city = NYC
```

### Membership Testing

```python
person = {"name": "Alice", "age": 25}

# Check keys (default)
print("name" in person)     # True
print("email" in person)    # False

# Check values (need to use values())
print("Alice" in person.values())  # True
print(25 in person.values())       # True
```

### Length

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}
print(len(person))  # 3

empty = {}
print(len(empty))  # 0
```

### Merging Dictionaries

```python
# Using update()
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using ** operator (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using | operator (Python 3.9+)
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

## Nested Dictionaries

### Creating Nested Dictionaries

```python
# Students with grades
students = {
    "Alice": {
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Physics"]
    },
    "Bob": {
        "age": 21,
        "grade": "B",
        "subjects": ["Chemistry", "Biology"]
    }
}
```

### Accessing Nested Values

```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"}
}

# Access nested value
print(students["Alice"]["age"])    # 20
print(students["Bob"]["grade"])    # "B"

# Safe access with get()
age = students.get("Alice", {}).get("age", 0)
print(age)  # 20

# If student doesn't exist
age = students.get("Charlie", {}).get("age", 0)
print(age)  # 0 (default)
```

### Modifying Nested Dictionaries

```python
students = {
    "Alice": {"age": 20, "grade": "A"}
}

# Modify nested value
students["Alice"]["age"] = 21

# Add new nested key
students["Alice"]["email"] = "alice@email.com"

# Add new student
students["Bob"] = {"age": 22, "grade": "B"}
```

### Iterating Nested Dictionaries

```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"}
}

# Iterate outer dictionary
for name, info in students.items():
    print(f"Student: {name}")
    for key, value in info.items():
        print(f"  {key}: {value}")

# Output:
# Student: Alice
#   age: 20
#   grade: A
# Student: Bob
#   age: 21
#   grade: B
```

---

## Dictionary Comprehensions

### Basic Syntax

```python
# Traditional way
squares = {}
for x in range(5):
    squares[x] = x**2

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### With Condition

```python
# Even numbers only
evens = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Filter dict based on values
scores = {"Alice": 85, "Bob": 72, "Charlie": 95, "Dave": 68}
passing = {name: score for name, score in scores.items() if score >= 70}
# {'Alice': 85, 'Bob': 72, 'Charlie': 95}
```

### Transform Values

```python
# Convert to uppercase
names = {"first": "alice", "last": "smith"}
upper_names = {k: v.upper() for k, v in names.items()}
# {'first': 'ALICE', 'last': 'SMITH'}

# Double all values
numbers = {"a": 1, "b": 2, "c": 3}
doubled = {k: v*2 for k, v in numbers.items()}
# {'a': 2, 'b': 4, 'c': 6}
```

### Swap Keys and Values

```python
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

---

## Advanced Dictionary Topics

### defaultdict

```python
from collections import defaultdict

# Regular dict - KeyError if key doesn't exist
regular = {}
# regular["a"] += 1  # KeyError!

# defaultdict - provides default value
counter = defaultdict(int)  # default value: 0
counter["a"] += 1
print(counter)  # defaultdict(<class 'int'>, {'a': 1})

# Default list
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("banana")
print(groups)  
# defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})
```

### Counter

```python
from collections import Counter

# Count occurrences
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(words)
print(counter)  
# Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Most common
print(counter.most_common(2))  
# [('apple', 3), ('banana', 2)]

# Count characters
text = "hello world"
char_count = Counter(text)
print(char_count)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

### OrderedDict

```python
from collections import OrderedDict

# Python 3.7+ regular dicts maintain insertion order
# OrderedDict needed for older versions or specific ordering operations

ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

print(ordered)
# OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Move to end
ordered.move_to_end("first")
# OrderedDict([('second', 2), ('third', 3), ('first', 1)])
```

---

## Practice Exercises

### Beginner

**Exercise 1**: Create dictionary for person with name, age, city

**Exercise 2**: Access value by key

**Exercise 3**: Add new key-value pair

**Exercise 4**: Update existing value

**Exercise 5**: Check if key exists

### Intermediate

**Exercise 6**: Count word frequency in a sentence

**Exercise 7**: Merge two dictionaries

**Exercise 8**: Get all keys with values > 50

**Exercise 9**: Create dict from two lists (keys and values)

**Exercise 10**: Invert dictionary (swap keys and values)

### Advanced

**Exercise 11**: Group list of dicts by a key

**Exercise 12**: Flatten nested dictionary

**Exercise 13**: Find common keys in two dicts

**Exercise 14**: Sort dictionary by values

**Exercise 15**: Deep copy nested dictionary

---

## 🎯 Key Takeaways

✅ Dictionaries store **key-value pairs**  
✅ Keys must be **unique** and **immutable**  
✅ Access values using **[key]** or **.get(key)**  
✅ **15+ methods**: get, keys, values, items, update, pop, setdefault  
✅ **Dictionary comprehensions**: `{k: v for k, v in items}`  
✅ Use **defaultdict** for automatic default values  
✅ Use **Counter** for counting occurrences  
✅ Python 3.7+ dicts maintain **insertion order**  

---

## 📚 Quick Reference

```python
# Creation
d = {"key": "value"}
d = dict(key="value")

# Access
d["key"]
d.get("key", default)

# Modify
d["key"] = "new_value"
d.update({"k": "v"})
del d["key"]
d.pop("key")
d.clear()

# Iterate
for key in d:
for value in d.values():
for key, value in d.items():

# Methods
d.keys()
d.values()
d.items()
d.get(key, default)
d.setdefault(key, default)

# Comprehension
{k: v for k, v in items}
```

---

**End of Dictionaries Notes** 📝

Continue to `Functions_Basics_Notes.md` for Day 3 topics!

## Advanced Dictionary Techniques

### Dictionary Comprehensions Advanced

```python
# Conditional comprehension
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36}

# Transform keys and values
names = ['alice', 'bob', 'charlie']
name_lengths = {name.upper(): len(name) for name in names}
print(name_lengths)  # {'ALICE': 5, 'BOB': 3, 'CHARLIE': 7}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(combined)  # {'a': 1, 'b': 2, 'c': 3}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

### Merging Dictionaries

```python
# Python 3.9+ Union operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 3, 'c': 4} - dict2 wins

# Update operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1 |= dict2
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}

# **unpacking (all Python versions)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}
```

### Nested Dictionary Operations

```python
# Deep access with get() chain
data = {
    'user': {
        'name': 'Alice',
        'address': {
            'city': 'NYC',
            'zip': '10001'
        }
    }
}

# Safe access
city = data.get('user', {}).get('address', {}).get('city')
print(city)  # 'NYC'

# Update nested value
data['user']['address']['zip'] = '10002'

# Add nested key safely
if 'user' not in data:
    data['user'] = {}
if 'phone' not in data['user']:
    data['user']['phone'] = '555-1234'
```

### Dictionary as Switch Statement

```python
# Instead of long if-elif chains
def get_day_type(day):
    day_types = {
        'Monday': 'Workday',
        'Tuesday': 'Workday',
        'Wednesday': 'Workday',
        'Thursday': 'Workday',
        'Friday': 'Workday',
        'Saturday': 'Weekend',
        'Sunday': 'Weekend'
    }
    return day_types.get(day, 'Invalid day')

print(get_day_type('Saturday'))  # 'Weekend'
print(get_day_type('Tuesday'))   # 'Workday'

# With functions as values
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply
}

result = operations['+'](5, 3)  # 8
```

---

## Performance and Memory

### Dictionary Copy Performance

```python
import copy

original = {str(i): i for i in range(1000)}

# Shallow copy (fast)
shallow = original.copy()
shallow2 = dict(original)

# Deep copy (slower, for nested structures)
nested = {'a': {'b': [1, 2, 3]}}
deep = copy.deepcopy(nested)

# Modify deep copy
deep['a']['b'].append(4)
print(nested)  # {'a': {'b': [1, 2, 3]}} - unchanged
print(deep)    # {'a': {'b': [1, 2, 3, 4]}} - modified
```

### Memory-Efficient Alternatives

```python
# For counting - use Counter
from collections import Counter

items = ['a', 'b', 'c', 'a', 'b', 'a']

# Regular dict
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

# Counter (more efficient)
counts = Counter(items)
print(counts)  # Counter({'a': 3, 'b': 2, 'c': 1})

# For ordered data - use OrderedDict (Python <3.7) or regular dict (Python 3.7+)
# For default values - use defaultdict
```

---

## Real-World Dictionary Applications

### Application 1: Configuration Management

```python
class Config:
    """Application configuration using dict"""
    def __init__(self):
        self._config = {
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'mydb'
            },
            'api': {
                'url': 'https://api.example.com',
                'timeout': 30
            },
            'features': {
                'debug': False,
                'logging': True
            }
        }
    
    def get(self, key, default=None):
        """Get config value using dot notation"""
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """Set config value using dot notation"""
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value

# Usage
config = Config()
print(config.get('database.host'))  # 'localhost'
config.set('database.port', 3306)
print(config.get('database.port'))  # 3306
```

### Application 2: In-Memory Cache

```python
class SimpleCache:
    """Simple in-memory cache using dict"""
    def __init__(self, max_size=100):
        self._cache = {}
        self._max_size = max_size
    
    def get(self, key):
        """Get value from cache"""
        return self._cache.get(key)
    
    def set(self, key, value):
        """Set value in cache"""
        if len(self._cache) >= self._max_size:
            # Remove oldest (first) item
            first_key = next(iter(self._cache))
            del self._cache[first_key]
        
        self._cache[key] = value
    
    def clear(self):
        """Clear cache"""
        self._cache.clear()
    
    def size(self):
        """Get cache size"""
        return len(self._cache)

# Usage
cache = SimpleCache(max_size=3)
cache.set('user:1', {'name': 'Alice'})
cache.set('user:2', {'name': 'Bob'})
print(cache.get('user:1'))  # {'name': 'Alice'}
print(cache.size())  # 2
```

### Application 3: Word Frequency Counter

```python
def count_words(text):
    """Count word frequency in text"""
    # Clean and split text
    words = text.lower().split()
    
    # Count frequencies
    frequency = {}
    for word in words:
        # Remove punctuation
        word = word.strip('.,!?;:')
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    
    # Sort by frequency
    sorted_words = sorted(frequency.items(), 
                         key=lambda x: x[1], 
                         reverse=True)
    
    return dict(sorted_words)

text = "hello world hello python python python"
frequencies = count_words(text)
print(frequencies)  # {'python': 3, 'hello': 2, 'world': 1}

# Get top N words
def get_top_words(text, n=5):
    frequencies = count_words(text)
    return list(frequencies.items())[:n]
```

---

## Dictionary Patterns and Idioms

### Pattern 1: Group By

```python
def group_by(items, key_func):
    """Group items by key function"""
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# Example: Group students by grade
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
    {'name': 'David', 'grade': 'C'},
    {'name': 'Eve', 'grade': 'B'}
]

by_grade = group_by(students, lambda s: s['grade'])
print(by_grade)
# {'A': [{'name': 'Alice', ...}, {'name': 'Charlie', ...}],
#  'B': [{'name': 'Bob', ...}, {'name': 'Eve', ...}],
#  'C': [{'name': 'David', ...}]}
```

### Pattern 2: Dictionary Filtering

```python
# Filter by value
scores = {'Alice': 95, 'Bob': 67, 'Charlie': 88, 'David': 72}

# Get scores above 80
high_scores = {k: v for k, v in scores.items() if v >= 80}
print(high_scores)  # {'Alice': 95, 'Charlie': 88}

# Filter by key
# Get names starting with 'A'
a_names = {k: v for k, v in scores.items() if k.startswith('A')}
print(a_names)  # {'Alice': 95}

# Filter by both key and value
filtered = {k: v for k, v in scores.items() 
            if k.startswith('C') and v >= 80}
print(filtered)  # {'Charlie': 88}
```

### Pattern 3: Dictionary Transformation

```python
prices = {'apple': 1.20, 'banana': 0.50, 'orange': 0.80}

# Apply discount to all prices
discounted = {k: v * 0.9 for k, v in prices.items()}
print(discounted)  # {'apple': 1.08, 'banana': 0.45, 'orange': 0.72}

# Round all values
rounded = {k: round(v, 2) for k, v in discounted.items()}

# Convert values to strings with formatting
formatted = {k: f"${v:.2f}" for k, v in prices.items()}
print(formatted)  # {'apple': '$1.20', 'banana': '$0.50', 'orange': '$0.80'}
```

---

## Dictionary Common Mistakes

### Mistake 1: Modifying Dict During Iteration

```python
# ❌ WRONG
scores = {'Alice': 95, 'Bob': 67, 'Charlie': 88}
for name in scores:
    if scores[name] < 70:
        del scores[name]  # RuntimeError!

# ✅ CORRECT
scores = {'Alice': 95, 'Bob': 67, 'Charlie': 88}
scores = {k: v for k, v in scores.items() if v >= 70}

# Or use list() to avoid runtime error
scores = {'Alice': 95, 'Bob': 67, 'Charlie': 88}
for name in list(scores.keys()):
    if scores[name] < 70:
        del scores[name]
```

### Mistake 2: Not Checking Key Existence

```python
# ❌ RISKY
user = {'name': 'Alice'}
age = user['age']  # KeyError!

# ✅ SAFE
age = user.get('age', 25)  # Default value

# Or check first
if 'age' in user:
    age = user['age']
else:
    age = 25
```

---

## Dictionary Best Practices Summary

### DO's ✅

1. **Use get()** for safe access with defaults
2. **Use dict comprehensions** for filtering/transforming
3. **Use defaultdict** when all keys should have default value
4. **Use Counter** for counting occurrences
5. **Document complex nested structures**

### DON'Ts ❌

1. **Don't modify dict while iterating**
2. **Don't use mutable objects as keys**
3. **Don't access keys without checking existence**
4. **Don't nest too deeply** (max 2-3 levels)
5. **Don't use dicts when other data structures are better**

---

**End of Dictionaries Notes** ���

Master Python dictionaries for efficient key-value data management!
