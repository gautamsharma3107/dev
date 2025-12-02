# List Comprehensions in Python - Complete Guide

## 📚 Table of Contents
1. [Introduction to List Comprehensions](#introduction-to-list-comprehensions)
2. [Basic List Comprehensions](#basic-list-comprehensions)
3. [Comprehensions with Conditions](#comprehensions-with-conditions)
4. [Nested Comprehensions](#nested-comprehensions)
5. [Dict and Set Comprehensions](#dict-and-set-comprehensions)
6. [Generator Expressions](#generator-expressions)
7. [When NOT to Use Comprehensions](#when-not-to-use-comprehensions)
8. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

- ✅ Write list comprehensions for transformations
- ✅ Add conditions to comprehensions
- ✅ Create nested comprehensions
- ✅ Use dict and set comprehensions
- ✅ Understand generator expressions
- ✅ Know when comprehensions are appropriate

---

## Introduction to List Comprehensions

### What are List Comprehensions?

**List comprehensions** provide a concise way to create lists. They're more readable and often faster than traditional loops.

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (one line!)
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Syntax

```python
[expression for item in iterable]

# Examples
[x**2 for x in range(5)]           # [0, 1, 4, 9, 16]
[x.upper() for x in ['a', 'b']]    # ['A', 'B']
[len(word) for word in ['hi', 'hello']]  # [2, 5]
```

---

## Basic List Comprehensions

### Simple Transformations

```python
# Square numbers
squares = [x**2 for x in range(10)]

# Convert to uppercase
words = ['hello', 'world']
upper_words = [word.upper() for word in words]
# ['HELLO', 'WORLD']

# String lengths
words = ['python', 'is', 'awesome']
lengths = [len(word) for word in words]
# [6, 2, 7]

# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
# [2,4, 6, 8, 10]
```

### Working with Ranges

```python
# First 10 even numbers
evens = [x for x in range(0, 20, 2)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Or with transformation
evens = [x * 2 for x in range(10)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Powers  of 2
powers = [2**x for x in range(10)]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

---

## Comprehensions with Conditions

### Filtering with if

```python
# Even numbers only
numbers = range(20)
evens = [x for x in numbers if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Positive numbers only
numbers = [1, -2, 3, -4, 5, -6]
positives = [x for x in numbers if x > 0]
# [1, 3, 5]

# Long words (length > 5)
words = ['python', 'is', 'awesome', 'code']
long_words = [word for word in words if len(word) > 5]
# ['python', 'awesome']
```

### if-else (Ternary Operator)

```python
# Categorize numbers
numbers = [1, 2, 3, 4, 5]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']

# Absolute values
numbers = [1, -2, 3, -4, 5]
abs_values = [x if x >= 0 else -x for x in numbers]
# [1, 2, 3, 4, 5]

# Cap values at 100
values = [50, 150, 75, 200, 25]
capped = [x if x <= 100 else 100 for x in values]
# [50, 100, 75, 100, 25]
```

---

## Nested Comprehensions

### Flatten 2D List

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reading: "for each row in matrix, for each num in that row"
```

### Create 2D List

```python
# 3x4 matrix of zeros
matrix = [[0 for j in range(4)] for i in range(3)]
# [[0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]]

# Multiplication table
table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]
```

---

## Dict and Set Comprehensions

### Dictionary Comprehensions

```python
# Squares dictionary
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Invert dictionary
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
scores = {'Alice': 85, 'Bob': 72, 'Charlie': 95}
passing = {name: score for name, score in scores.items() if score >= 80}
# {'Alice': 85, 'Charlie': 95}
```

### Set Comprehensions

```python
# Unique squares
squares = {x**2 for x in [-2, -1, 0, 1, 2]}
# {0, 1, 4}

# Unique lengths
words = ['hello', 'world', 'hi', 'bye']
lengths = {len(word) for word in words}
# {2, 3, 5}
```

---

## Generator Expressions

### Generator vs List

```python
# List comprehension - creates entire list in memory
list_comp = [x**2 for x in range(1000000)]

# Generator expression - creates values on demand
gen_exp = (x**2 for x in range(1000000))

# Use generator with for loop
for square in gen_exp:
    print(square)
    if square > 100:
        break  # Can stop early, saving computation
```

---

## When NOT to Use Comprehensions

### Too Complex

```python
# ❌ BAD - hard to read
result = [x*2 if x > 0 else x**2 if x < 0 else 0 for x in numbers if x != 5]

# ✅ BETTER - use regular loop
result = []
for x in numbers:
    if x == 5:
        continue
    if x > 0:
        result.append(x * 2)
    elif x < 0:
        result.append(x ** 2)
    else:
        result.append(0)
```

---

## Practice Exercises

**Exercise 1**: List of squares 1-10

**Exercise 2**: Extract even numbers from list

**Exercise 3**: Flatten nested list

**Exercise 4**: Create dict mapping numbers to squares

**Exercise 5**: Remove duplicates using set comprehension

---

## 🎯 Key Takeaways

✅ **List comp**: `[expr for item in iterable]`  
✅ **With filter**: `[expr for item in iterable if condition]`  
✅ **With if-else**: `[expr1 if cond else expr2 for item in iterable]`  
✅ **Dict comp**: `{k: v for item in iterable}`  
✅ **Set comp**: `{expr for item in iterable}`  
✅ **Generator**: `(expr for item in iterable)`  
✅ Keep comprehensions **simple and readable**  

---

**End of List Comprehensions Notes** 📝

## Advanced List Comprehension Patterns

### Nested List Comprehensions

```python
# 2D matrix creation
matrix = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print(matrix)
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]

# Flatten 2D list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create pairs
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)  # [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), ...]

# Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = [f"{color}-{size}" for color in colors for size in sizes]
print(products)  # ['red-S', 'red-M', 'red-L', 'blue-S', 'blue-M', 'blue-L']
```

### Conditional Comprehensions

```python
numbers = range(1, 11)

# Filter with if
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Transform with if-else
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', ...]

# Multiple conditions (AND)
divisible_by_2_and_3 = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(divisible_by_2_and_3)  # [6]

# Multiple conditions (OR) using conditional expression
div_2_or_3 = [x for x in numbers if x % 2 == 0 or x % 3 == 0]
print(div_2_or_3)  # [2, 3, 4, 6, 8, 9, 10]

# Complex filtering
words = ['python', 'is', 'awesome', 'and', 'powerful']
long_words_upper = [w.upper() for w in words if len(w) > 3]
print(long_words_upper)  # ['PYTHON', 'AWESOME', 'POWERFUL']
```

### Multiple Iteration Variables

```python
# Enumerate with comprehension
items = ['apple', 'banana', 'orange']
indexed = [(i, item) for i, item in enumerate(items)]
print(indexed)  # [(0, 'apple'), (1, 'banana'), (2, 'orange')]

# Zip with comprehension
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = [{'name': n, 'age': a} for n, a in zip(names, ages)]
print(people)
# [{'name': 'Alice', 'age': 25}, ...]

# Dictionary items
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
high_scorers = [name for name, score in scores.items() if score >= 80]
print(high_scorers)  # ['Alice', 'Bob']
```

---

## Dictionary Comprehensions

### Basic Dictionary Comprehensions

```python
# Create dictionary from lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Square numbers
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From string
char_codes = {char: ord(char) for char in 'Python'}
print(char_codes)  # {'P': 80, 'y': 121, 't': 116, ...}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

### Conditional Dictionary Comprehensions

```python
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Filter by value
evens = {k: v for k, v in numbers.items() if v % 2 == 0}
print(evens)  # {'b': 2, 'd': 4}

# Filter by key
vowels = {k: v for k, v in numbers.items() if k in 'aeiou'}
print(vowels)  # {'a': 1, 'e': 5}

# Transform values
doubled = {k: v*2 for k, v in numbers.items()}
print(doubled)  # {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

# Conditional transformation
transformed = {k: v**2 if v % 2 == 0 else v for k, v in numbers.items()}
print(transformed)  # {'a': 1, 'b': 4, 'c': 3, 'd': 16, 'e': 5}
```

### Nested Dictionary Comprehensions

```python
# Create nested dictionary
matrix_dict = {
    i: {j: i*j for j in range(1, 4)}
    for i in range(1, 4)
}
print(matrix_dict)
# {1: {1: 1, 2: 2, 3: 3},
#  2: {1: 2, 2: 4, 3: 6},
#  3: {1: 3, 2: 6, 3: 9}}

# Group items by property
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
    {'name': 'David', 'grade': 'C'}
]

by_grade = {
    grade: [s['name'] for s in students if s['grade'] == grade]
    for grade in set(s['grade'] for s in students)
}
print(by_grade)
# {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}
```

---

## Set Comprehensions

### Basic Set Comprehensions

```python
# Create set of squares
squares = {x**2 for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}

# Get unique values
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = {x for x in numbers}
print(unique)  # {1, 2, 3, 4, 5}

# Extract unique characters
text = "hello world"
unique_chars = {char for char in text if char != ' '}
print(unique_chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Get unique lengths
words = ['python', 'is', 'awesome', 'and', 'fun']
lengths = {len(word) for word in words}
print(lengths)  # {2, 3, 6, 7}
```

### Conditional Set Comprehensions

```python
# Filter vowels
text = "python programming"
vowels = {char for char in text if char in 'aeiou'}
print(vowels)  # {'a', 'i', 'o'}

# Get even numbers
numbers = range(1, 11)
evens = {x for x in numbers if x % 2 == 0}
print(evens)  # {2, 4, 6, 8, 10}

# Unique word starts
words = ['apple', 'apricot', 'banana', 'berry', 'cherry']
starts = {word[0] for word in words}
print(starts)  # {'a', 'b', 'c'}
```

---

## Generator Expressions

### Basics

```python
# Generator (lazy evaluation)
gen = (x**2 for x in range(1, 6))
print(gen)  # <generator object>

# Consume generator
for value in gen:
    print(value, end=' ')  # 1 4 9 16 25

# Convert to list
gen = (x**2 for x in range(1, 6))
squares = list(gen)
print(squares)  # [1, 4, 9, 16, 25]

# Sum generator
total = sum(x**2 for x in range(1, 11))
print(total)  # 385
```

### Memory Efficiency

```python
import sys

# List comprehension (stores all in memory)
list_comp = [x**2 for x in range(10000)]
print(f"List: {sys.getsizeof(list_comp)} bytes")

# Generator (generates on demand)
gen_exp = (x**2 for x in range(10000))
print(f"Generator: {sys.getsizeof(gen_exp)} bytes")

# Generator is MUCH smaller!

# Use generator for large datasets
def process_large_file():
    # Good: Memory efficient
    lines = (line.strip() for line in open('large_file.txt'))
    return sum(1 for line in lines if 'error' in line.lower())
```

---

## Real-World Applications

### Application 1: Data Processing

```python
# Process user data
users = [
    {'name': 'Alice', 'age': 25, 'active': True, 'score': 85},
    {'name': 'Bob', 'age': 17, 'active': False, 'score': 92},
    {'name': 'Charlie', 'age': 30, 'active': True, 'score': 78},
    {'name': 'David', 'age': 22, 'active': True, 'score': 95}
]

# Get active adult users
active_adults = [
    u['name'] for u in users
    if u['age'] >= 18 and u['active']
]
print(active_adults)  # ['Alice', 'Charlie', 'David']

# Calculate statistics
high_scores = {
    u['name']: u['score']
    for u in users
    if u['score'] >= 80
}
print(high_scores)  # {'Alice': 85, 'Bob': 92, 'David': 95}

# Group by age category
age_groups = {
    'teen': [u['name'] for u in users if u['age'] < 20],
    'adult': [u['name'] for u in users if 20 <= u['age'] < 30],
    'senior': [u['name'] for u in users if u['age'] >= 30]
}
print(age_groups)
```

### Application 2: Text Analysis

```python
text = "Python is awesome. Python is powerful. Python is fun."

# Get unique words
words = text.lower().replace('.', '').split()
unique_words = {word for word in words}
print(f"Unique words: {len(unique_words)}")

# Word frequency
from collections import Counter
word_freq = {
    word: words.count(word)
    for word in unique_words
}
print(word_freq)

# Long words
long_words = [word for word in unique_words if len(word) > 5]
print(f"Long words: {long_words}")

# Words starting with vowels
vowel_words = [word for word in unique_words if word[0] in 'aeiou']
print(f"Vowel words: {vowel_words}")
```

### Application 3: Matrix Operations

```python
# Create matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Transpose matrix
transposed = [[row[i] for row in matrix_a] for i in range(len(matrix_a[0]))]
print("Transposed:")
for row in transposed:
    print(row)

# Add matrices
sum_matrix = [
    [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
    for i in range(len(matrix_a))
]
print("Sum:")
for row in sum_matrix:
    print(row)

# Get diagonal
diagonal = [matrix_a[i][i] for i in range(len(matrix_a))]
print(f"Diagonal: {diagonal}")
```

---

## Performance Considerations

### Comprehension vs Loop

```python
import timeit

# List comprehension
def with_comprehension():
    return [x**2 for x in range(1000)]

# Regular loop  
def with_loop():
    result = []
    for x in range(1000):
        result.append(x**2)
    return result

comp_time = timeit.timeit(with_comprehension, number=10000)
loop_time = timeit.timeit(with_loop, number=10000)

print(f"Comprehension: {comp_time:.4f}s")
print(f"Loop: {loop_time:.4f}s")
print(f"Comprehension is {loop_time/comp_time:.1f}x faster")
```

### When to Use What

```python
# ✅ Use list comprehension for simple transformations
squares = [x**2 for x in numbers]

# ✅ Use generator for large datasets
large_data = (process(x) for x in huge_dataset)

# ✅ Use dict comprehension for mapping
lookup = {item['id']: item for item in items}

# ❌ Avoid for complex logic
# BAD:
result = [
    complex_transform(x) if condition1(x) else
    other_transform(x) if condition2(x) else
    default_value for x in items if filter_condition(x)
]

# BETTER: Use regular loop
result = []
for x in items:
    if filter_condition(x):
        if condition1(x):
            result.append(complex_transform(x))
        elif condition2(x):
            result.append(other_transform(x))
        else:
            result.append(default_value)
```

---

## Common Patterns

### Pattern 1: Filtering and Transforming

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get squares of even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Get uppercase of long words
words = ['hi', 'python', 'is', 'awesome']
long_upper = [w.upper() for w in words if len(w) > 3]
print(long_upper)  # ['PYTHON', 'AWESOME']
```

### Pattern 2: Conditional Transformation

```python
numbers = [1, 2, 3, 4, 5]

# Different transformation based on condition
transformed = [x**2 if x % 2 == 0 else x**3 for x in numbers]
print(transformed)  # [1, 4, 27, 16, 125]

# Clamp values
values = [-5, -2, 0, 3, 8, 12]
clamped = [max(0, min(10, x)) for x in values]
print(clamped)  # [0, 0, 0, 3, 8, 10]
```

### Pattern 3: Flattening

```python
# Flatten list of lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# Flatten with condition
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_evens = [
    item for sublist in nested
    for item in sublist
    if item % 2 == 0
]
print(flat_evens)  # [2, 4, 6, 8]
```

---

## Best Practices

### DO's ✅

```python
# 1. Use for simple, readable transformations
squares = [x**2 for x in range(10)]

# 2. Filter with if
evens = [x for x in numbers if x % 2 == 0]

# 3. Use generator for large data
total = sum(x**2 for x in range(1000000))

# 4. Keep it readable (max 2 levels)
pairs = [(x, y) for x in range(3) for y in range(3)]
```

### DON'Ts ❌

```python
# 1. Don't use for complex logic
# BAD: Too complex
result = [f(x, y) if cond1(x) else g(x, y) if cond2(x) 
          else h(x, y) for x in items for y in other 
          if x > 0 if y < 10]

# 2. Don't nest too deeply
# BAD: 3+ levels
result = [[[x+y+z for z in c] for y in b] for x in a]

# 3. Don't sacrifice readability
# BAD: Hard to read
x = [i for i in [j for j in [k for k in range(10)]]]
```

---

**End of List Comprehensions Notes** ���

Master comprehensions for concise, Pythonic code!
