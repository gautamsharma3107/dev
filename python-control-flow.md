# Python Control Flow: Conditional Statements and Loops

---

## Table of Contents
1. [Conditional Statements](#conditional-statements)
2. [Ternary Operators](#ternary-operators)
3. [Loops](#loops)
4. [Break, Continue, Pass Statements](#break-continue-pass-statements)
5. [Loop Else Clause](#loop-else-clause)
6. [Nested Loops and Conditions](#nested-loops-and-conditions)
7. [Match-Case Statements](#match-case-statements)

---

## Conditional Statements

### if Statement
The most basic conditional. Executes code only if condition is True.

```python
age = 18

if age >= 18:
    print("You are an adult")
```

**Output:** `You are an adult`

### if-else Statement
Executes one block if condition is True, another if False.

```python
score = 45

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

**Output:** `Fail`

### if-elif-else Statement
Multiple conditions. Checks each condition in order until one is True.

```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Output:** `Grade: C`

**Important Notes:**
- Only ONE block executes (the first True condition)
- `elif` can be chained multiple times
- `else` is optional and executes if all conditions are False

### Comparison with Java/C++

**Python:**
```python
if x > 10:
    print("x is greater than 10")
```

**Java:**
```java
if (x > 10) {
    System.out.println("x is greater than 10");
}
```

**Key Differences:**
- Python uses indentation (no braces `{}`)
- Python uses `:` to mark start of block
- Python doesn't need parentheses around condition (though allowed)

### Compound Conditions with Logical Operators

```python
age = 25
income = 50000

# AND operator - both must be True
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# OR operator - at least one must be True
if age < 18 or income < 10000:
    print("Not eligible")

# NOT operator
if not (age < 18):
    print("Age is 18 or above")
```

### Nested If Statements

```python
username = "john"
password = "secure123"

if username == "john":
    print("Username found")
    if password == "secure123":
        print("Password correct - Login successful")
    else:
        print("Wrong password")
else:
    print("Username not found")
```

---

## Ternary Operators

### Single Line if-else
Compact way to assign values based on condition.

**Syntax:** `value_if_true if condition else value_if_false`

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Comparison
marks = 45
result = "Pass" if marks >= 50 else "Fail"
print(result)  # Output: Fail
```

### Nested Ternary (Multiple Conditions)
```python
score = 75

grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(grade)  # Output: C
```

**Note:** Nested ternary can reduce readability. Use if-elif-else for clarity when more than 2 conditions.

### Practical Examples

```python
# Getting minimum value
x, y = 10, 20
min_val = x if x < y else y
print(min_val)  # Output: 10

# Checking even/odd
num = 7
parity = "Even" if num % 2 == 0 else "Odd"
print(parity)  # Output: Odd

# Default value assignment
user_name = ""
display_name = user_name if user_name else "Guest"
print(display_name)  # Output: Guest
```

---

## Loops

### for Loop
Iterates over a sequence (list, tuple, string, range, etc.).

#### Basic for Loop with range()
```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

#### range() Function Details
- `range(stop)` - 0 to stop-1
- `range(start, stop)` - start to stop-1
- `range(start, stop, step)` - with increment/decrement

```python
# 0 to 9
for i in range(10):
    print(i, end=" ")  # Output: 0 1 2 3 4 5 6 7 8 9

# 5 to 9
for i in range(5, 10):
    print(i, end=" ")  # Output: 5 6 7 8 9

# 0 to 10 with step 2
for i in range(0, 11, 2):
    print(i, end=" ")  # Output: 0 2 4 6 8 10

# Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i, end=" ")  # Output: 10 9 8 7 6 5 4 3 2 1
```

#### for Loop with Lists
```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(f"I like {fruit}")
```

**Output:**
```
I like apple
I like banana
I like orange
```

#### for Loop with enumerate()
Get both index and value:

```python
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**Output:**
```
0: apple
1: banana
2: orange
```

#### for Loop with zip()
Iterate over multiple sequences:

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

**Output:**
```
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
```

---

### while Loop
Executes as long as condition is True.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

**Output:**
```
0
1
2
3
4
```

#### while with User Input
```python
password = ""

while password != "secret":
    password = input("Enter password: ")

print("Access granted!")
```

#### Infinite Loop (Use with Caution!)
```python
# This runs forever
# while True:
#     print("This is an infinite loop")

# Better approach - exit with break
count = 0
while True:
    print(count)
    count += 1
    if count > 4:
        break
```

---

## Break, Continue, Pass Statements

### break Statement
Exits the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Output:**
```
0
1
2
3
4
```

**Use Case:** Finding a value in a list:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")
```

### continue Statement
Skips current iteration and moves to next.

```python
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)
```

**Output:**
```
1
3
5
7
9
```

**Use Case:** Filtering data:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num < 3 or num > 8:
        continue
    print(num)  # Output: 3 4 5 6 7 8
```

### pass Statement
Placeholder - does nothing. Used when a statement is required syntactically.

```python
# Code structure planned but not implemented yet
for i in range(5):
    pass  # TODO: Add logic here

# Using in if block
age = 20
if age >= 18:
    pass  # Will implement later
else:
    print("Too young")
```

**Use Cases:**
- Empty function/class definitions
- Placeholder for future implementation
- Avoid syntax errors

```python
def my_function():
    pass  # Empty function

class MyClass:
    pass  # Empty class
```

---

## Loop Else Clause

### else with for Loop
The `else` block executes when loop completes normally (without `break`).

```python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")
```

**Output:**
```
0
1
2
3
4
Loop completed successfully
```

#### With break (else doesn't execute)
```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed successfully")
```

**Output:**
```
0
1
2
```

**Note:** The `else` clause did NOT execute because of `break`.

#### Practical Use: Searching

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 15

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list")
```

**Output:** `15 not found in the list`

### else with while Loop

```python
count = 0

while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed")
```

**Output:**
```
0
1
2
While loop completed
```

#### With break
```python
count = 0

while count < 10:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("While loop completed")
```

**Output:**
```
0
1
2
```

---

## Nested Loops and Conditions

### Nested for Loops
Loop inside another loop.

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
```

**Output:**
```
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
```

### Pattern Printing with Nested Loops

```python
# Triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

**Output:**
```
*
**
***
****
*****
```

### Nested while Loops

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1
```

**Output:**
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

### Nested Conditions Inside Loops

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 45},
    {"name": "Charlie", "score": 92},
    {"name": "Diana", "score": 38}
]

for student in students:
    name = student["name"]
    score = student["score"]
    
    if score >= 80:
        if score >= 90:
            print(f"{name}: Grade A")
        else:
            print(f"{name}: Grade B")
    elif score >= 50:
        print(f"{name}: Grade C")
    else:
        print(f"{name}: Grade F")
```

**Output:**
```
Alice: Grade B
Bob: Grade C
Charlie: Grade A
Diana: Grade F
```

### Using break in Nested Loops

```python
# Find a pair that sums to 10
for i in range(1, 6):
    for j in range(1, 6):
        if i + j == 10:
            print(f"Found: {i} + {j} = 10")
            break
    else:
        continue
    break  # Exit outer loop if found
```

**Output:** `Found: 4 + 6 = 10`

---

## Match-Case Statements

### Introduction (Python 3.10+)
Structural pattern matching - similar to switch in other languages but more powerful.

**Syntax:**
```python
match value:
    case pattern1:
        # Code for pattern1
    case pattern2:
        # Code for pattern2
    case _:
        # Default case
```

### Basic Match-Case

```python
day = "Monday"

match day:
    case "Monday":
        print("Start of work week")
    case "Friday":
        print("Almost weekend")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Unknown day")
```

**Output:** `Start of work week`

### Multiple Values (using |)

```python
status = "inactive"

match status:
    case "active" | "online":
        print("User is available")
    case "inactive" | "offline":
        print("User is not available")
    case "busy":
        print("User is busy")
    case _:
        print("Unknown status")
```

**Output:** `User is not available`

### Pattern Matching with Types

```python
def describe_value(val):
    match val:
        case int():
            print(f"{val} is an integer")
        case float():
            print(f"{val} is a float")
        case str():
            print(f"{val} is a string")
        case bool():
            print(f"{val} is a boolean")
        case _:
            print(f"Unknown type")

describe_value(42)       # Output: 42 is an integer
describe_value(3.14)     # Output: 3.14 is a float
describe_value("hello")  # Output: hello is a string
```

### Pattern Matching with Sequences

```python
def process_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"On Y-axis at {y}")
        case (x, 0):
            print(f"On X-axis at {x}")
        case (x, y):
            print(f"Point at ({x}, {y})")

process_point((0, 0))    # Output: Origin
process_point((0, 5))    # Output: On Y-axis at 5
process_point((3, 4))    # Output: Point at (3, 4)
```

### Pattern Matching with Dictionaries

```python
def process_request(request):
    match request:
        case {"method": "GET", "path": path}:
            print(f"Getting data from {path}")
        case {"method": "POST", "path": path, "data": data}:
            print(f"Posting data to {path}: {data}")
        case {"method": "DELETE", "path": path}:
            print(f"Deleting {path}")
        case _:
            print("Unknown request")

process_request({"method": "GET", "path": "/users"})
# Output: Getting data from /users

process_request({"method": "POST", "path": "/users", "data": {"name": "Alice"}})
# Output: Posting data to /users: {'name': 'Alice'}
```

### Pattern Matching with Guards

Guard conditions add extra logic:

```python
def check_number(num):
    match num:
        case int() if num < 0:
            print("Negative number")
        case int() if num == 0:
            print("Zero")
        case int() if num > 0:
            print("Positive number")
        case _:
            print("Not an integer")

check_number(-5)   # Output: Negative number
check_number(0)    # Output: Zero
check_number(10)   # Output: Positive number
```

### Class Pattern Matching

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def analyze_point(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=x, y=0):
            print(f"On X-axis at {x}")
        case Point(x=0, y=y):
            print(f"On Y-axis at {y}")
        case Point(x=x, y=y):
            print(f"Point at ({x}, {y})")

analyze_point(Point(0, 0))    # Output: Origin
analyze_point(Point(5, 0))    # Output: On X-axis at 5
analyze_point(Point(3, 4))    # Output: Point at (3, 4)
```

### Comparison: Match-Case vs if-elif-else

**Using if-elif-else:**
```python
status = "active"

if status == "active":
    print("User is online")
elif status == "inactive":
    print("User is offline")
elif status == "busy":
    print("User is busy")
else:
    print("Unknown status")
```

**Using match-case:**
```python
status = "active"

match status:
    case "active":
        print("User is online")
    case "inactive":
        print("User is offline")
    case "busy":
        print("User is busy")
    case _:
        print("Unknown status")
```

---

## Practice Exercises

### 1. Conditional Statements
- Write a program to check if a number is positive, negative, or zero.
- Create a grade calculator that assigns grades A-F based on marks.

### 2. Ternary Operators
- Use ternary to find the maximum of two numbers.
- Assign a discount based on purchase amount using ternary.

### 3. Loops
- Print multiplication table for a given number using loops.
- Create a pattern of stars using nested for loops.

### 4. Break and Continue
- Write a loop to find the first occurrence of a number in a list.
- Print all odd numbers from 1-20, skipping 10-15.

### 5. Loop Else
- Search for an element in a list using for-else.
- Validate a password (retry until correct) using while-else.

### 6. Nested Structures
- Create a 2D grid and access elements using nested loops.
- Find duplicate pairs in a nested list structure.

### 7. Match-Case
- Create a simple calculator using match-case for operators.
- Process different types of user commands using match-case.

---

# End of Notes
