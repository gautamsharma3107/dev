# Python Collections Module: Complete Guide

---

## Table of Contents
1. [Introduction to Collections](#introduction-to-collections)
2. [Counter](#counter)
3. [defaultdict](#defaultdict)
4. [OrderedDict](#ordereddict)
5. [deque](#deque)
6. [namedtuple](#namedtuple)
7. [ChainMap](#chainmap)
8. [Practical Examples](#practical-examples)
9. [Comparison and Use Cases](#comparison-and-use-cases)
10. [Practice Exercises](#practice-exercises)

---

## Introduction to Collections

### What is the Collections Module?

The `collections` module provides specialized container data types beyond the basic built-in containers (list, tuple, dict, set).

### Why Use Collections?

1. **Performance** - Optimized for specific operations
2. **Convenience** - Built-in methods for common tasks
3. **Readability** - More expressive code
4. **Efficiency** - Less code needed for common patterns

### Importing from Collections

```python
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap

# Or individual imports
from collections import Counter
from collections import defaultdict
# etc.
```

---

## Counter

### What is Counter?

A dictionary subclass for counting hashable objects.

```python
from collections import Counter

# Create from list
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(fruits)
print(counter)
# Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Create from string
text = "hello"
counter = Counter(text)
print(counter)
# Output: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Create from dictionary
data = {"a": 1, "b": 2, "a": 3}
counter = Counter(data)
print(counter)
# Output: Counter({'a': 3, 'b': 2})
```

### Counter Methods

#### most_common()

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
counter = Counter(words)

# Get all elements sorted by count
print(counter.most_common())
# Output: [('apple', 3), ('banana', 2), ('cherry', 1), ('date', 1)]

# Get top N elements
print(counter.most_common(2))
# Output: [('apple', 3), ('banana', 2)]

# Get least common (reverse)
print(counter.most_common()[::-1])
# Output: [('date', 1), ('cherry', 1), ('banana', 2), ('apple', 3)]
```

#### elements()

```python
from collections import Counter

counter = Counter({'a': 3, 'b': 2, 'c': 1})

# Get iterator of elements (repeated by count)
elements = list(counter.elements())
print(elements)
# Output: ['a', 'a', 'a', 'b', 'b', 'c']

# Useful for reconstructing original data
print(''.join(counter.elements()))
# Output: aaabbc
```

#### update() and subtract()

```python
from collections import Counter

# Create counters
counter1 = Counter(['a', 'b', 'c'])
counter2 = Counter(['a', 'b', 'd'])

# update() - add counts
counter1.update(counter2)
print(counter1)
# Output: Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})

# subtract() - subtract counts
counter3 = Counter(['a', 'b', 'c'])
counter4 = Counter(['a', 'b'])
counter3.subtract(counter4)
print(counter3)
# Output: Counter({'c': 1, 'a': 0, 'b': 0})
```

### Counter Arithmetic Operations

```python
from collections import Counter

counter1 = Counter({'a': 3, 'b': 1})
counter2 = Counter({'a': 1, 'b': 2})

# Addition - combine counts
print(counter1 + counter2)
# Output: Counter({'a': 4, 'b': 3})

# Subtraction - keep only positive counts
print(counter1 - counter2)
# Output: Counter({'a': 2})

# Intersection - take minimum counts
print(counter1 & counter2)
# Output: Counter({'a': 1, 'b': 1})

# Union - take maximum counts
print(counter1 | counter2)
# Output: Counter({'a': 3, 'b': 2})
```

### Practical Counter Examples

```python
from collections import Counter

# Find most common character in text
text = "programming"
char_counter = Counter(text)
most_common_char = char_counter.most_common(1)[0][0]
print(f"Most common: {most_common_char}")
# Output: Most common: g

# Verify anagrams
word1 = "listen"
word2 = "silent"
print(Counter(word1) == Counter(word2))
# Output: True

# Find missing elements
original = "abcdef"
subset = "ace"
missing = Counter(original) - Counter(subset)
print(''.join(missing.elements()))
# Output: bdf
```

---

## defaultdict

### What is defaultdict?

A dictionary subclass that provides default values for missing keys.

```python
from collections import defaultdict

# Regular dictionary - KeyError for missing key
regular_dict = {}
# print(regular_dict["missing"])  # KeyError

# defaultdict - provides default value
default_dict = defaultdict(list)
print(default_dict["missing"])  # Output: []
print(default_dict)
# Output: defaultdict(<class 'list'>, {'missing': []})
```

### Common Default Factory Functions

```python
from collections import defaultdict

# Using list as default
dict_list = defaultdict(list)
dict_list["a"].append(1)
dict_list["a"].append(2)
print(dict_list)
# Output: defaultdict(<class 'list'>, {'a': [1, 2]})

# Using int as default (returns 0)
dict_int = defaultdict(int)
dict_int["count"] += 1
dict_int["count"] += 1
print(dict_int)
# Output: defaultdict(<class 'int'>, {'count': 2})

# Using set as default
dict_set = defaultdict(set)
dict_set["colors"].add("red")
dict_set["colors"].add("blue")
print(dict_set)
# Output: defaultdict(<class 'set'>, {'colors': {'red', 'blue'}})

# Using str as default (empty string)
dict_str = defaultdict(str)
print(dict_str["missing"])
# Output: (empty string)
```

### Custom Default Factory

```python
from collections import defaultdict

# Using lambda for custom default
dict_custom = defaultdict(lambda: "N/A")
print(dict_custom["missing"])
# Output: N/A

# Using lambda to return complex values
dict_complex = defaultdict(lambda: {"status": "pending", "count": 0})
print(dict_complex["item1"])
# Output: {'status': 'pending', 'count': 0}

# Incrementing counter
dict_counter = defaultdict(lambda: 0)
dict_counter["a"] += 1
dict_counter["a"] += 1
dict_counter["b"] += 1
print(dict(dict_counter))
# Output: {'a': 2, 'b': 1}
```

### Practical defaultdict Examples

```python
from collections import defaultdict

# Group words by first letter
words = ["apple", "apricot", "banana", "berry", "cherry"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
# Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'berry'], 'c': ['cherry']}

# Count word frequency
text = "hello world hello python"
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1

print(dict(word_count))
# Output: {'hello': 2, 'world': 1, 'python': 1}

# Build adjacency list for graph
edges = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd')]
graph = defaultdict(list)
for source, target in edges:
    graph[source].append(target)

print(dict(graph))
# Output: {'a': ['b', 'c'], 'b': ['c', 'd']}
```

---

## OrderedDict

### What is OrderedDict?

Dictionary that remembers insertion order (but Python 3.7+ dicts do this by default).

```python
from collections import OrderedDict

# Create OrderedDict
ordered = OrderedDict()
ordered['first'] = 1
ordered['second'] = 2
ordered['third'] = 3

print(ordered)
# Output: OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Convert to list of tuples
print(list(ordered.items()))
# Output: [('first', 1), ('second', 2), ('third', 3)]
```

### OrderedDict Methods

```python
from collections import OrderedDict

# move_to_end()
ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move to end (default)
ordered.move_to_end('a')
print(list(ordered.keys()))
# Output: ['b', 'c', 'a']

# Move to beginning
ordered.move_to_end('c', last=False)
print(list(ordered.keys()))
# Output: ['c', 'b', 'a']

# popitem() - remove items in LIFO order
ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordered.popitem())  # Remove last
# Output: ('c', 3)

# Pop first with last=False
print(ordered.popitem(last=False))  # Remove first
# Output: ('a', 1)
```

### Comparison with Regular Dict

```python
from collections import OrderedDict

# Python 3.7+ - regular dicts maintain insertion order
regular_dict = {}
regular_dict['z'] = 26
regular_dict['a'] = 1
regular_dict['m'] = 13

# Both maintain insertion order
ordered_dict = OrderedDict()
ordered_dict['z'] = 26
ordered_dict['a'] = 1
ordered_dict['m'] = 13

print(list(regular_dict.keys()))
# Output: ['z', 'a', 'm']

print(list(ordered_dict.keys()))
# Output: ['z', 'a', 'm']

# Equality comparison - order matters for OrderedDict
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)
# Output: False (different order)
```

### Practical OrderedDict Examples

```python
from collections import OrderedDict

# Maintain configuration order
config = OrderedDict()
config['host'] = 'localhost'
config['port'] = 5432
config['database'] = 'mydb'
config['user'] = 'admin'

# Print in specific order
for key, value in config.items():
    print(f"{key}: {value}")

# Reorder configuration
config.move_to_end('database', last=False)  # Move to front
for key, value in config.items():
    print(f"{key}: {value}")
```

---

## deque

### What is deque?

Double-ended queue - optimized for adding/removing from both ends.

```python
from collections import deque

# Create empty deque
queue = deque()

# Create with initial items
queue = deque([1, 2, 3, 4, 5])
print(queue)
# Output: deque([1, 2, 3, 4, 5])

# With max length
bounded_queue = deque([1, 2, 3], maxlen=3)
print(bounded_queue)
# Output: deque([1, 2, 3], maxlen=3)
```

### deque Methods

#### append() and appendleft()

```python
from collections import deque

queue = deque([2, 3])

# Add to right
queue.append(4)
print(queue)
# Output: deque([2, 3, 4])

# Add to left
queue.appendleft(1)
print(queue)
# Output: deque([1, 2, 3, 4])
```

#### pop() and popleft()

```python
from collections import deque

queue = deque([1, 2, 3, 4, 5])

# Remove from right
right_val = queue.pop()
print(right_val)
# Output: 5
print(queue)
# Output: deque([1, 2, 3, 4])

# Remove from left
left_val = queue.popleft()
print(left_val)
# Output: 1
print(queue)
# Output: deque([2, 3, 4])
```

#### extend() and extendleft()

```python
from collections import deque

queue = deque([1, 2, 3])

# Extend right
queue.extend([4, 5, 6])
print(queue)
# Output: deque([1, 2, 3, 4, 5, 6])

# Extend left (adds in reverse order)
queue2 = deque([1, 2, 3])
queue2.extendleft([0, -1, -2])
print(queue2)
# Output: deque([-2, -1, 0, 1, 2, 3])
```

#### rotate()

```python
from collections import deque

queue = deque([1, 2, 3, 4, 5])

# Rotate right
queue.rotate(2)
print(queue)
# Output: deque([4, 5, 1, 2, 3])

# Rotate left (negative)
queue.rotate(-2)
print(queue)
# Output: deque([1, 2, 3, 4, 5])
```

### Practical deque Examples

```python
from collections import deque

# Implement queue (FIFO)
task_queue = deque()
task_queue.append("task1")
task_queue.append("task2")
task_queue.append("task3")

while task_queue:
    task = task_queue.popleft()
    print(f"Processing: {task}")

# Output:
# Processing: task1
# Processing: task2
# Processing: task3

# Implement stack (LIFO)
stack = deque()
stack.append("page1")
stack.append("page2")
stack.append("page3")

while stack:
    page = stack.pop()
    print(f"Back to: {page}")

# Output:
# Back to: page3
# Back to: page2
# Back to: page1

# Sliding window
numbers = [1, 2, 3, 4, 5]
window = deque(maxlen=3)
for num in numbers:
    window.append(num)
    print(f"Window: {list(window)}")

# Output:
# Window: [1]
# Window: [1, 2]
# Window: [1, 2, 3]
# Window: [2, 3, 4]
# Window: [3, 4, 5]
```

---

## namedtuple

### What is namedtuple?

Factory function for creating tuple subclasses with named fields.

```python
from collections import namedtuple

# Define namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create instance
p = Point(10, 20)
print(p)
# Output: Point(x=10, y=20)

# Access by name
print(p.x)
# Output: 10
print(p.y)
# Output: 20

# Access by index (tuple-like)
print(p[0])
# Output: 10
print(p[1])
# Output: 20
```

### Creating namedtuples

```python
from collections import namedtuple

# Method 1: Space/comma separated string
Person1 = namedtuple('Person1', 'name age email')

# Method 2: List
Person2 = namedtuple('Person2', ['name', 'age', 'email'])

# Method 3: Space-separated string
Person3 = namedtuple('Person3', 'name age email')

# All create same structure
p1 = Person1("Alice", 25, "alice@example.com")
p2 = Person2("Alice", 25, "alice@example.com")
p3 = Person3("Alice", 25, "alice@example.com")

print(p1)
# Output: Person(name='Alice', age=25, email='alice@example.com')
```

### namedtuple Methods

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# _fields - get field names
print(Point._fields)
# Output: ('x', 'y')

# _asdict() - convert to dictionary
print(p._asdict())
# Output: OrderedDict([('x', 10), ('y', 20)])

# _replace() - create new with changed fields
p2 = p._replace(x=30)
print(p2)
# Output: Point(x=30, y=20)
print(p)  # Original unchanged
# Output: Point(x=10, y=20)

# _make() - create from iterable
values = [5, 15]
p3 = Point._make(values)
print(p3)
# Output: Point(x=5, y=15)
```

### Practical namedtuple Examples

```python
from collections import namedtuple

# Employee records
Employee = namedtuple('Employee', ['name', 'department', 'salary'])

employees = [
    Employee("Alice", "Engineering", 80000),
    Employee("Bob", "HR", 60000),
    Employee("Charlie", "Sales", 70000)
]

# Display employees
for emp in employees:
    print(f"{emp.name} - {emp.department}: ${emp.salary}")

# Find highest paid
highest_paid = max(employees, key=lambda e: e.salary)
print(f"Highest paid: {highest_paid.name} (${highest_paid.salary})")

# Get all names
names = [emp.name for emp in employees]
print(f"Team: {', '.join(names)}")
```

---

## ChainMap

### What is ChainMap?

Groups multiple dictionaries into a single view.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

# Create ChainMap
chain = ChainMap(dict1, dict2, dict3)
print(chain)
# Output: ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5})

# Access like normal dictionary
print(chain['a'])
# Output: 1
print(chain['c'])
# Output: 3
print(chain['e'])
# Output: 5
```

### ChainMap Methods

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 3}

chain = ChainMap(dict1, dict2)

# Search order - first occurrence wins
print(chain['b'])
# Output: 2 (from dict1, not dict2)

# keys() - all keys from all dicts
print(list(chain.keys()))
# Output: ['a', 'b', 'c']

# values() - all values in search order
print(list(chain.values()))
# Output: [1, 2, 3]

# items() - all items
print(list(chain.items()))
# Output: [('a', 1), ('b', 2), ('c', 3)]

# maps - access individual dictionaries
print(chain.maps)
# Output: [{'a': 1, 'b': 2}, {'b': 20, 'c': 3}]
```

#### new_child()

```python
from collections import ChainMap

defaults = {'color': 'red', 'size': 10}
user_settings = {'color': 'blue'}

chain = ChainMap(user_settings, defaults)
print(dict(chain))
# Output: {'color': 'blue', 'size': 10}

# Create new level
new_chain = chain.new_child({'size': 20})
print(dict(new_chain))
# Output: {'size': 20, 'color': 'blue'}

# Original unchanged
print(dict(chain))
# Output: {'color': 'blue', 'size': 10}
```

### Practical ChainMap Examples

```python
from collections import ChainMap
import os

# Configuration hierarchy
defaults = {'host': 'localhost', 'port': 8000, 'debug': False}
env_config = {'debug': True}  # From environment
user_config = {'port': 9000}  # From user input

config = ChainMap(user_config, env_config, defaults)

print(f"Host: {config['host']}")     # localhost (from defaults)
print(f"Port: {config['port']}")     # 9000 (from user_config)
print(f"Debug: {config['debug']}")   # True (from env_config)

# Scope chain
global_scope = {'x': 1, 'y': 2}
local_scope = {'x': 10}  # Shadows global x

scope = ChainMap(local_scope, global_scope)
print(scope['x'])  # 10 (local shadows global)
print(scope['y'])  # 2 (from global)
```

---

## Practical Examples

### Word Frequency Counter

```python
from collections import Counter

text = """
Python is great. Python is powerful.
I love Python programming. Python is amazing.
"""

words = text.lower().split()
word_counter = Counter(words)

print("Top 5 words:")
for word, count in word_counter.most_common(5):
    print(f"{word}: {count}")

# Clean punctuation and recount
import string
words_clean = [w.strip(string.punctuation) for w in words]
word_counter_clean = Counter(words_clean)
print("\nTop 5 words (cleaned):")
for word, count in word_counter_clean.most_common(5):
    print(f"{word}: {count}")
```

### Student Grades Manager

```python
from collections import defaultdict, namedtuple

# Define Grade namedtuple
Grade = namedtuple('Grade', ['subject', 'score'])

# Group grades by student
student_grades = defaultdict(list)
student_grades['Alice'].append(Grade('Math', 85))
student_grades['Alice'].append(Grade('English', 90))
student_grades['Bob'].append(Grade('Math', 92))
student_grades['Bob'].append(Grade('English', 88))

# Calculate average per student
for student, grades in student_grades.items():
    avg = sum(g.score for g in grades) / len(grades)
    print(f"{student}: Average = {avg:.2f}")
```

### Task Queue System

```python
from collections import deque

class TaskQueue:
    def __init__(self):
        self.high_priority = deque()
        self.normal_priority = deque()
    
    def add_task(self, task, priority='normal'):
        if priority == 'high':
            self.high_priority.append(task)
        else:
            self.normal_priority.append(task)
    
    def process_next(self):
        if self.high_priority:
            return self.high_priority.popleft()
        elif self.normal_priority:
            return self.normal_priority.popleft()
        return None

# Usage
queue = TaskQueue()
queue.add_task("Send email", priority='high')
queue.add_task("Write report")
queue.add_task("Fix bug", priority='high')
queue.add_task("Update docs")

while True:
    task = queue.process_next()
    if not task:
        break
    print(f"Processing: {task}")

# Output:
# Processing: Send email
# Processing: Fix bug
# Processing: Write report
# Processing: Update docs
```

---

## Comparison and Use Cases

### When to Use Each

| Collection | Best For | Key Feature |
|-----------|----------|------------|
| Counter | Counting elements | Most common() |
| defaultdict | Missing key handling | Automatic defaults |
| OrderedDict | Preserve order (legacy) | move_to_end() |
| deque | Queue/Stack operations | Efficient both ends |
| namedtuple | Structured data | Named access |
| ChainMap | Multiple dicts as one | Priority lookup |

### Performance Comparison

```python
import timeit
from collections import deque, defaultdict

# deque vs list for popleft
deque_time = timeit.timeit(
    'd = deque(range(1000)); d.popleft()',
    'from collections import deque',
    number=10000
)

list_time = timeit.timeit(
    'l = list(range(1000)); l.pop(0)',
    number=10000
)

print(f"deque.popleft(): {deque_time:.4f}s")
print(f"list.pop(0): {list_time:.4f}s")
# deque is much faster for popleft
```

---

## Practice Exercises

### 1. Counter
- Count character frequency in a string
- Find most common and least common elements
- Verify if two words are anagrams
- Perform arithmetic operations on counters

### 2. defaultdict
- Group words by first letter
- Count word frequencies
- Build graph adjacency list
- Create nested structures

### 3. OrderedDict
- Maintain configuration order
- Track insertion order (compare with regular dict)
- Use move_to_end() for reordering

### 4. deque
- Implement a queue (FIFO)
- Implement a stack (LIFO)
- Create sliding window
- Rotate elements

### 5. namedtuple
- Create employee records
- Access by name and index
- Use _asdict() and _replace()
- Work with collections of namedtuples

### 6. ChainMap
- Create configuration hierarchy
- Implement scope chain
- Merge multiple dictionaries

### 7. Real-World Scenarios
- Build word frequency analyzer
- Create task priority queue
- Implement student grade manager
- Design configuration system
- Build LRU cache (using OrderedDict and defaultdict)

---

# End of Notes
