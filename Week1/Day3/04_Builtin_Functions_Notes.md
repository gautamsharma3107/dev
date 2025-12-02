# Python Built-in Functions - Complete Guide

## 📚 Table of Contents
1. [Essential Built-in Functions](#essential-built-in-functions)
2. [Type Conversion Functions](#type-conversion-functions)
3. [Mathematical Functions](#mathematical-functions)
4. [Sequence Functions](#sequence-functions)
5. [Iterator Functions](#iterator-functions)
6. [I/O Functions](#io-functions)
7. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

- ✅ Use essential built-in functions
- ✅ Convert between data types
- ✅ Work with mathematical functions
- ✅ Process sequences efficiently
- ✅ Use iterator functions effectively

---

## Essential Built-in Functions

### print()

```python
print("Hello, World!")
print("Name:", "Alice", "Age:", 25)  # Multiple args
print("Python", "JavaScript", sep=" | ")  # Custom separator
print("No newline", end="")  # Custom ending
```

### len()

```python
print(len("Python"))      # 6
print(len([1, 2, 3]))     # 3
print(len({" a": 1, "b": 2}))  # 2
```

### type()

```python
print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type([1, 2]))      # <class 'list'>
```

### input()

```python
name = input("Enter name: ")
age = int(input("Enter age: "))  # Convert to int
```

### help()

```python
help(str.upper)  # Show documentation
help(list)       # Show list documentation
```

---

## Type Conversion Functions

### int(), float(), str()

```python
# To integer
int("42")        # 42
int(3.9)        # 3 (truncates)
int(True)        # 1

# To float
float("3.14")    # 3.14
float(42)        # 42.0

# To string
str(42)          # "42"
str(3.14)        # "3.14"
str([1, 2])      # "[1, 2]"
```

### list(), tuple(), set(), dict()

```python
# To list
list("abc")          # ['a', 'b', 'c']
list((1, 2, 3))      # [1, 2, 3]
list(range(5))       # [0, 1, 2, 3, 4]

# To tuple
tuple([1, 2, 3])     # (1, 2, 3)

# To set
set([1, 1, 2, 2, 3]) # {1, 2, 3} (removes duplicates)

# To dict
dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}
```

---

## Mathematical Functions

### abs()

```python
abs(-5)      # 5
abs(3.14)    # 3.14
abs(-10.5)   # 10.5
```

### round()

```python
round(3.14159, 2)  # 3.14
round(3.5)         # 4 (banker's rounding)
```

### pow()

```python
pow(2, 3)       # 8 (2³)
pow(2, 3, 5)    # 3 ((2³) % 5)
```

### min(), max()

```python
min(1, 5, 3)             # 1
max([1, 5, 3, 9, 2])     # 9

# With key function
words = ['python', 'is', 'awesome']
min(words, key=len)      # 'is'
```

### sum()

```python
sum([1, 2, 3, 4, 5])     # 15
sum(range(10))           # 45
sum([1, 2, 3], 10)       # 16 (start value 10)
```

---

## Sequence Functions

### range()

```python
list(range(5))           # [0, 1, 2, 3, 4]
list(range(2, 10))       # [2, 3, 4, 5, 6, 7, 8, 9]
list(range(0, 10, 2))    # [0, 2, 4, 6, 8]
```

### enumerate()

```python
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# Start from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### zip()

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
# Alice is 25
# Bob is 30
# Charlie is 35

# Create dict
dict(zip(names, ages))
# {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

### sorted()

```python
# Returns NEW sorted list
sorted([3, 1, 4, 1, 5])  # [1, 1, 3, 4, 5]

# Reverse
sorted([3, 1, 4], reverse=True)  # [4, 3, 1]

# Custom key
sorted(['python', 'is', 'awesome'], key=len)
# ['is', 'python', 'awesome']
```

### reversed()

```python
numbers = [1, 2, 3, 4, 5]
list(reversed(numbers))  # [5, 4, 3, 2, 1]

# Works with strings
list(reversed("Python"))  # ['n', 'o', 'h', 't', 'y', 'P']
```

---

## Iterator Functions

### map()

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Multiple iterables
list(map(lambda x, y: x + y, [1, 2], [3, 4]))
# [4, 6]
```

### filter()

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

### all()

```python
all([True, True, True])   # True
all([True, False, True])  # False
all([1, 2, 3])            # True (all truthy)
all([1, 0, 3])            # False (0 is falsy)

# Check if all positive
numbers = [1, 2, 3, 4]
all(x > 0 for x in numbers)  # True
```

### any()

```python
any([False, False, True])  # True
any([False, False])        # False
any([0, 0, 1])             # True

# Check if any negative
numbers = [1, 2, -3, 4]
any(x < 0 for x in numbers)  # True
```

---

## I/O Functions

### open()

```python
# Read file
with open('file.txt', 'r') as f:
    content = f.read()

# Write file
with open('file.txt', 'w') as f:
    f.write("Hello, World!")
```

---

## Practice Exercises

**Exercise 1**: Use len() to find string length

**Exercise 2**: Convert list to set to remove duplicates

**Exercise 3**: Use enumerate() to print indexed list

**Exercise 4**: Use zip() to combine two lists

**Exercise 5**: Use map() to square all numbers

**Exercise 6**: Use filter() to get positive numbers

**Exercise 7**: Use sorted() with custom key

**Exercise 8**: Use all() to check if all numbers > 0

**Exercise 9**: Use any() to check if any string starts with 'A'

**Exercise 10**: Use sum() to calculate total

---

## 🎯 Key Takeaways

✅ **print()**: Output to console  
✅ **len()**: Get length  
✅ **type()**: Check type  
✅ **int(), float(), str()**: Type conversion  
✅ **abs(), round(), pow()**: Math operations  
✅ **min(), max(), sum()**: Aggregate functions  
✅ **range()**: Generate sequences  
✅ **enumerate()**: Index + value  
✅ **zip()**: Combine iterables  
✅ **sorted(), reversed()**: Sequence operations  
✅ **map(), filter()**: Transform/filter sequences  
✅ **all(), any()**: Boolean aggregation  

---

## 📚 Quick Reference

```python
# Essential
print(), len(), type(), input()

# Conversion
int(), float(), str(), list(), tuple(), set(), dict()

# Math
abs(), round(), pow(), min(), max(), sum()

# Sequences
range(), enumerate(), zip(), sorted(), reversed()

# Iterators
map(), filter(), all(), any()

# I/O
open(), print()
```

---

**End of Builtin Functions Notes** 📝

## Advanced Built-in Functions

### all() and any() Deep Dive

```python
# all() - True if ALL elements are truthy
numbers = [1, 2, 3, 4, 5]
print(all(n > 0 for n in numbers))  # True (all positive)
print(all(n > 3 for n in numbers))  # False (not all > 3)

# any() - True if ANY element is truthy
print(any(n > 4 for n in numbers))  # True (5 is > 4)
print(any(n > 10 for n in numbers)) # False (none > 10)

# Practical use: Validation
def validate_user(user):
    required_fields = ['name', 'email', 'age']
    return all(field in user for field in required_fields)

user1 = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
user2 = {'name': 'Bob', 'email': 'bob@example.com'}

print(validate_user(user1))  # True
print(validate_user(user2))  # False (missing 'age')
```

### filter() and map() Advanced

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() - Keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# map() - Transform each element
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25, ...]

# Combine filter and map
even_squares = list(map(lambda x: x**2, 
                        filter(lambda x: x % 2 == 0, numbers)))
print(even_squares)  # [4, 16, 36, 64, 100]

# Multiple iterables with map
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [11, 22, 33]
```

### zip() and enumerate() Advanced

```python
# zip() - Combine multiple iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# Unzip data
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

# enumerate() with custom start
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. orange
```

### sorted() and reversed() Deep Dive

```python
# sorted() with key function
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade
by_grade = sorted(students, key=lambda s: s['grade'])
print(by_grade)

# Sort by grade (descending)
by_grade_desc = sorted(students, key=lambda s: s['grade'], reverse=True)
print(by_grade_desc)

# Sort by multiple keys
data = [('Alice', 25), ('Bob', 30), ('Alice', 30)]
sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
print(sorted_data)  # [('Alice', 25), ('Alice', 30), ('Bob', 30)]

# reversed() - Returns iterator
numbers = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(numbers))
print(reversed_nums)  # [5, 4, 3, 2, 1]
```

---

## Type Conversion Functions

### int(), float(), str() Advanced

```python
# int() with base
binary_str = "1010"
decimal = int(binary_str, 2)  # Convert from binary
print(decimal)  # 10

hex_str = "FF"
decimal = int(hex_str, 16)  # Convert from hex
print(decimal)  # 255

# float() handling
print(float("3.14"))      # 3.14
print(float("inf"))       # inf
print(float("-inf"))      # -inf
print(float("1e6"))       # 1000000.0

# str() with custom class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(str(p))   # Alice (25)
print(repr(p))  # Person('Alice', 25)
```

### list(), tuple(), set(), dict() Conversions

```python
# Conversion between types
my_list = [1, 2, 3, 2, 1]
my_tuple = tuple(my_list)    # [1, 2, 3, 2, 1] → (1, 2, 3, 2, 1)
my_set = set(my_list)        # [1, 2, 3, 2, 1] → {1, 2, 3}
back_to_list = list(my_set)  # {1, 2, 3} → [1, 2, 3]

# dict() from pairs
pairs = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(pairs)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

# dict() from keywords
my_dict = dict(name='Alice', age=25, city='NYC')
print(my_dict)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

---

## Mathematical Functions

### abs(), round(), pow()

```python
# abs() - Absolute value
print(abs(-5))      # 5
print(abs(3.14))    # 3.14
print(abs(-2.5))    # 2.5

# Works with complex numbers
print(abs(3 + 4j))  # 5.0 (magnitude)

# round() - Round to n decimals
print(round(3.14159))      # 3
print(round(3.14159, 2))   # 3.14
print(round(3.14159, 4))   # 3.1416

# Banker's rounding (round half to even)
print(round(2.5))  # 2
print(round(3.5))  # 4

# pow() - Power operation
print(pow(2, 3))      # 8  (same as 2**3)
print(pow(2, 3, 5))   # 3  (2**3 % 5)
```

### min(), max(), sum()

```python
numbers = [5, 2, 8, 1, 9, 3]

print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 28

# With key function
words = ['python', 'is', 'awesome']
longest = max(words, key=len)
print(longest)  # 'awesome'

# min/max with default
empty_list = []
result = min(empty_list, default=0)
print(result)  # 0

# sum() with start value
print(sum(numbers, start=10))  # 38 (28 + 10)
```

---

## Sequence Functions

### len(), range(), slice()

```python
# len() works on sequences
print(len([1, 2, 3]))      # 3
print(len("Python"))       # 6
print(len({1, 2, 3}))      # 3
print(len({'a': 1, 'b': 2}))  # 2

# range() advanced usage
# range(stop)
for i in range(5):
    print(i, end=' ')  # 0 1 2 3 4

# range(start, stop)
for i in range(2, 7):
    print(i, end=' ')  # 2 3 4 5 6

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=' ')  # 0 2 4 6 8

# Backwards range
for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1

# slice() object
my_slice = slice(1, 5, 2)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[my_slice])  # [1, 3] (same as numbers[1:5:2])
```

---

## Object Inspection Functions

### type(), isinstance(), hasattr()

```python
# type() - Get object type
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>

# isinstance() - Check type
print(isinstance(42, int))        # True
print(isinstance(3.14, float))    # True
print(isinstance("hi", str))      # True

# Check multiple types
print(isinstance(42, (int, float)))  # True
print(isinstance(3.14, (int, float)))  # True

# hasattr(), getattr(), setattr()
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")

print(hasattr(p, 'name'))   # True
print(hasattr(p, 'age'))    # False

# getattr with default
age = getattr(p, 'age', 25)
print(age)  # 25 (default)

# setattr
setattr(p, 'age', 30)
print(p.age)  # 30
```

### dir(), vars(), id()

```python
# dir() - List object attributes
class MyClass:
    def __init__(self):
        self.x = 10
    
    def my_method(self):
        pass

obj = MyClass()
print(dir(obj))  # Lists all attributes and methods

# vars() - Get __dict__
print(vars(obj))  # {'x': 10}

# id() - Get object memory address
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))  # Memory address
print(id(b))  # Different address (different object)
print(id(c))  # Same as 'a' (same object)
```

---

## Input/Output Functions

### input(), print() Advanced

```python
# input() with validation
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number")

age = get_integer("Enter your age: ")

# print() advanced
# Multiple items
print("Name:", "Alice", "Age:", 25)

# Custom separator
print(1, 2, 3, 4, 5, sep=" | ")  # 1 | 2 | 3 | 4 | 5

# Custom end
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# Print to file
with open("output.txt", "w") as f:
    print("Hello, File!", file=f)

# Flush immediately
import time
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(0.5)
```

---

## Functional Programming

### map(), filter(), reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() - Transform
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# filter() - Select
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce() - Accumulate
total = reduce(lambda x, y: x + y, numbers)
print(total)  #15

# reduce with initial value
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# Practical example: Find maximum
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # 5
```

---

## Real-World Applications

### Application 1: Data Processing Pipeline

```python
# Process list of user data
users = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 17, 'score': 92},
    {'name': 'Charlie', 'age': 30, 'score': 78},
    {'name': 'David', 'age': 22, 'score': 95}
]

# Filter adults, map to scores, get average
adult_scores = list(
    map(lambda u: u['score'],
        filter(lambda u: u['age'] >= 18, users))
)

average = sum(adult_scores) / len(adult_scores)
print(f"Average adult score: {average:.1f}")  # 85.0
```

### Application 2: Text Analysis

```python
text = "Python is awesome. Python is powerful. Python is fun."

# Process text
words = text.lower().replace('.', '').split()

# Count unique words
unique_words = set(words)
print(f"Unique words: {len(unique_words)}")

# Find longest word
longest = max(words, key=len)
print(f"Longest word: {longest}")

# Word frequency
from collections import Counter
freq = Counter(words)
print(f"Most common: {freq.most_common(3)}")
```

---

## Built-in Functions Reference

### Complete List

| Function | Description | Example |
|----------|-------------|---------|
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `all(iterable)` | True if all are true | `all([True, True])` → `True` |
| `any(iterable)` | True if any is true | `any([False, True])` → `True` |
| `bin(x)` | Binary string | `bin(10)` → `'0b1010'` |
| `bool(x)` | Convert to boolean | `bool(1)` → `True` |
| `chr(i)` | Character from code | `chr(65)` → `'A'` |
| `dict()` | Create dictionary | `dict(a=1)` → `{'a': 1}` |
| `enumerate()` | Index, value pairs | `list(enumerate(['a']))` → `[(0, 'a')]` |
| `filter()` | Filter elements | `list(filter(lambda x: x>0, [-1,1]))` → `[1]` |
| `float(x)` | Convert to float | `float("3.14")` → `3.14` |
| `format()` | Format value | `format(0.5, '%')` → `'50%'` |
| `hex(x)` | Hex string | `hex(255)` → `'0xff'` |
| `int(x)` | Convert to int | `int("42")` → `42` |
| `len(s)` | Length | `len([1,2,3])` → `3` |
| `list()` | Create list | `list((1,2))` → `[1, 2]` |
| `map()` | Transform elements | `list(map(str, [1,2]))` → `['1', '2']` |
| `max()` | Maximum value | `max([1,5,3])` → `5` |
| `min()` | Minimum value | `min([1,5,3])` → `1` |
| `oct(x)` | Octal string | `oct(8)` → `'0o10'` |
| `ord(c)` | Code from char | `ord('A')` → `65` |
| `pow(x, y)` | Power | `pow(2, 3)` → `8` |
| `print()` | Print output | `print("Hi")` |
| `range()` | Number sequence | `list(range(3))` → `[0, 1, 2]` |
| `reversed()` | Reversed iterator | `list(reversed([1,2]))` → `[2, 1]` |
| `round(x, n)` | Round number | `round(3.14, 1)` → `3.1` |
| `set()` | Create set | `set([1,1,2])` → `{1, 2}` |
| `sorted()` | Sorted list | `sorted([3,1,2])` → `[1, 2, 3]` |
| `str(x)` | Convert to string | `str(42)` → `'42'` |
| `sum()` | Sum values | `sum([1,2,3])` → `6` |
| `tuple()` | Create tuple | `tuple([1,2])` → `(1, 2)` |
| `type(x)` | Get type | `type(42)` → `<class 'int'>` |
| `zip()` | Combine iterables | `list(zip([1], ['a']))` → `[(1, 'a')]` |

---

**End of Builtin Functions Notes** ���

Master built-in functions for efficient Python programming!

## String Functions

### chr() and ord()

```python
# chr() - Get character from Unicode code point
print(chr(65))    # 'A'
print(chr(97))    # 'a'
print(chr(8364))  # '€'
print(chr(128512))  # '���'

# ord() - Get Unicode code point from character
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('€'))   # 8364
print(ord('���'))  # 128512

# Practical use: Caesar cipher
def caesar_encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

encrypted = caesar_encrypt("Hello World", 3)
print(encrypted)  # "Khoor Zruog"
```

### format() and ascii()

```python
# format() - Format values
print(format(42, 'b'))      # '101010' (binary)
print(format(42, 'o'))      # '52' (octal)
print(format(42, 'x'))      # '2a' (hex)
print(format(42, 'X'))      # '2A' (HEX)

print(format(3.14159, '.2f'))  # '3.14'
print(format(0.5, '%'))        # '50.000000%'
print(format(1000000, ','))    # '1,000,000'

# ascii() - ASCII representation
print(ascii("Hello"))          # "'Hello'"
print(ascii("Café"))           # "'Caf\\xe9'"
print(ascii(['a', 'é', '���']))  # "['a', '\\xe9', '\\U0001f600']"
```

---

## Iteration Functions

### iter() and next()

```python
# iter() - Create iterator
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

# next() - Get next item
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# next() with default
print(next(iterator, 'Done'))  # 4
print(next(iterator, 'Done'))  # 5
print(next(iterator, 'Done'))  # 'Done' (no StopIteration)

# Custom iterator
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in Countdown(5):
    print(num, end=' ')  # 5 4 3 2 1
```

### enumerate() Advanced

```python
# Basic enumerate
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start from custom index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Enumerate with conditional
for i, fruit in enumerate(fruits):
    if fruit.startswith('a'):
        print(f"Found '{fruit}' at index {i}")

# Multiple lists with enumerate and zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for i, (name, age) in enumerate(zip(names, ages), 1):
    print(f"{i}. {name} is {age} years old")
```

---

## Comparison and Hashing

### hash() and id()

```python
# hash() - Get hash value
print(hash("Python"))    # Consistent hash
print(hash(42))          # Integer hash
print(hash((1, 2, 3)))   # Tuple hash

# Mutable objects can't be hashed
# print(hash([1, 2, 3]))  # TypeError

# Custom hash for objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(hash(p1) == hash(p2))  # True

# id() - Object identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))  # Unique ID
print(id(b))  # Different ID (different object)
print(id(c))  # Same as 'a' (same object)
print(id(a) == id(c))  # True
```

---

## Advanced Functional Programming

### Combining map, filter, reduce

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Complex pipeline
result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
print(result)  # 220 (2²+4²+6²+8²+10² = 4+16+36+64+100)

# More readable version
evens = filter(lambda x: x % 2 == 0, numbers)
squared = map(lambda x: x ** 2, evens)
total = reduce(lambda x, y: x + y, squared)
print(total)  # 220
```

### Custom Reduction Functions

```python
from functools import reduce

# Find maximum
numbers = [3, 7, 2, 9, 1, 5]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 9

# Concatenate strings
words = ['Python', 'is', 'awesome']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)  # "Python is awesome"

# Nested list flattening
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda x, y: x + y, nested)
print(flat)  # [1, 2, 3, 4, 5, 6]

# Product of all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120
```

---

## Memory and Performance

### sys.getsizeof() for Built-ins

```python
import sys

# Compare sizes
print(f"int(42): {sys.getsizeof(42)} bytes")
print(f"float(3.14): {sys.getsizeof(3.14)} bytes")
print(f"str('hello'): {sys.getsizeof('hello')} bytes")
print(f"list[1,2,3]: {sys.getsizeof([1,2,3])} bytes")
print(f"tuple(1,2,3): {sys.getsizeof((1,2,3))} bytes")
print(f"dict{a:1}: {sys.getsizeof({'a':1})} bytes")
print(f"set{1,2,3}: {sys.getsizeof({1,2,3})} bytes")
```

### Generator vs List Performance

```python
import sys

# List comprehension (loads all into memory)
list_comp = [x**2 for x in range(10000)]
print(f"List size: {sys.getsizeof(list_comp)} bytes")

# Generator expression (generates on demand)
gen_exp = (x**2 for x in range(10000))
print(f"Generator size: {sys.getsizeof(gen_exp)} bytes")

# Generator is much smaller!
# Use when you only need to iterate once
```

---

## Practical Built-in Combinations

### Data Cleaning Pipeline

```python
# Clean and process text data
def clean_data(text_list):
    """Clean text data using built-ins"""
    # Remove empty strings
    filtered = filter(None, text_list)
    
    # Strip whitespace
    stripped = map(str.strip, filtered)
    
    # Convert to lowercase
    lowercased = map(str.lower, stripped)
    
    # Remove duplicates and sort
    unique = sorted(set(lowercased))
    
    return unique

data = ["  Python  ", "python", "", "  JAVA  ", "Java", "C++"]
cleaned = clean_data(data)
print(cleaned)  # ['c++', 'java', 'python']
```

### Data Transformation

```python
# Transform nested data
users = [
    {'name': 'Alice', 'scores': [85, 90, 88]},
    {'name': 'Bob', 'scores': [75, 80, 78]},
    {'name': 'Charlie', 'scores': [95, 92, 98]}
]

# Calculate average scores
def calculate_averages(users):
    return [
        {
            'name': user['name'],
            'average': round(sum(user['scores']) / len(user['scores']), 2)
        }
        for user in users
    ]

averages = calculate_averages(users)
print(averages)
# [{'name': 'Alice', 'average': 87.67}, ...]

# Find top performer
top_performer = max(averages, key=lambda x: x['average'])
print(f"Top performer: {top_performer['name']}")
```

---

## Built-in Exceptions

### Common Exception Types

```python
# ValueError
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError
try:
    "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# KeyError
try:
    d = {'a': 1}
    value = d['b']
except KeyError as e:
    print(f"KeyError: {e}")

# IndexError
try:
    lst = [1, 2, 3]
    value = lst[10]
except IndexError as e:
    print(f"IndexError: {e}")

# AttributeError
try:
    value = "hello".nonexistent_method()
except AttributeError as e:
    print(f"AttributeError: {e}")
```

### Exception Hierarchy

```python
# Catching multiple exceptions
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types for division"
    except Exception as e:
        return f"Unexpected error: {e}"

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # "Cannot divide by zero"
print(safe_divide(10, "a"))  # "Invalid types for division"
```

---

## Quick Reference Card

### Most Used Built-ins

```python
# Type conversions
int(), float(), str(), bool(), list(), tuple(), set(), dict()

# Math
abs(), round(), pow(), min(), max(), sum()

# Sequences
len(), range(), sorted(), reversed(), enumerate(), zip()

# Functional
map(), filter(), all(), any()

# I/O
print(), input(), open()

# Object inspection
type(), isinstance(), hasattr(), getattr(), setattr(), dir()

# Iteration
iter(), next()

# String
chr(), ord(), format(), ascii()

# Other
help(), id(), hash()
```

---

## Built-in Tips and Tricks

### Tip 1: Use any() for existence checks

```python
# ❌ VERBOSE
found = False
for item in items:
    if condition(item):
        found = True
        break

# ✅ CONCISE
found = any(condition(item) for item in items)
```

### Tip 2: Use all() for validation

```python
# ❌ VERBOSE
valid = True
for value in values:
    if not is_valid(value):
        valid = False
        break

# ✅ CONCISE
valid = all(is_valid(value) for value in values)
```

### Tip 3: Use zip() for parallel iteration

```python
# ❌ VERBOSE
for i in range(len(names)):
    print(f"{names[i]}: {ages[i]}")

# ✅ BETTER
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### Tip 4: Use enumerate() instead of range(len())

```python
# ❌ VERBOSE
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# ✅ BETTER
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

---

**End of Builtin Functions Notes** ���

Complete mastery of Python's powerful built-in functions!
