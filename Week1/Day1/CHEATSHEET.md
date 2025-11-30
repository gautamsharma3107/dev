# Day 1 Quick Reference Cheat Sheet

## Variables and Data Types
```python
# Variable assignment
name = "Gautam"
age = 25
height = 5.9
is_student = True

# Type conversion
int("123")      # String to integer
float("3.14")   # String to float
str(123)        # Integer to string
bool(1)         # To boolean
```

## Operators
```python
# Arithmetic
+ - * / // % **

# Comparison
== != > < >= <=

# Logical
and or not

# Assignment
= += -= *= /=
```

## Strings
```python
text = "Python"
text.upper()              # PYTHON
text.lower()              # python
text.replace("o", "0")    # Pyth0n
text.split()              # Split by space
len(text)                 # Length: 6

# Slicing
text[0]      # First: P
text[-1]     # Last: n
text[0:3]    # Pyt
text[::-1]   # Reverse: nohtyP

# Formatting
f"{name} is {age}"
```

## Numbers and Booleans
```python
import math

# Math operations
abs(-5)          # 5
round(3.14, 1)   # 3.1
max(1,2,3)       # 3
min(1,2,3)       # 1
sum([1,2,3])     # 6

math.sqrt(16)    # 4.0
math.pi          # 3.14159...
math.ceil(3.2)   # 4
math.floor(3.8)  # 3

# Boolean
True and False   # False
True or False    # True
not True         # False
```

## Input/Output
```python
# Input
name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))

# Multiple inputs
a, b, c = map(int, input().split())

# Output
print(f"{name} is {age} years old")
print("A", "B", sep="-")  # A-B
print("Loading", end="...")
```

## If-Else
```python
if condition:
    # code
elif condition:
    # code
else:
    # code

# Ternary
result = "yes" if x > 5 else "no"
```

## Loops
```python
# For loop
for i in range(5):      # 0 to 4
    print(i)

for i in range(1, 6):   # 1 to 5
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
break      # Exit loop
continue   # Skip to next iteration
```

## Common Patterns
```python
# Check even/odd
if num % 2 == 0:
    print("Even")

# Swap variables
a, b = b, a

# Sum of numbers
total = sum(range(1, 11))

# Factorial
factorial = 1
for i in range(1, n+1):
    factorial *= i

# Prime check
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
```

---
**Keep this handy for quick reference!** 🚀
