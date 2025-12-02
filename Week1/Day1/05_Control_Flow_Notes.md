# Control Flow (If-Else Statements) - Complete Guide

## 📚 Table of Contents
1. [Introduction to Control Flow](#introduction-to-control-flow)
2. [If Statements](#if-statements)
3. [If-Else Statements](#if-else-statements)
4. [If-Elif-Else Statements](#if-elif-else-statements)
5. [Nested Conditionals](#nested-conditionals)
6. [Conditional Expressions (Ternary Operator)](#conditional-expressions-ternary-operator)
7. [Match-Case Statements](#match-case-statements)
8. [Best Practices](#best-practices)
9. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

By the end of this guide, you will:
- ✅ Use if, else, and elif for decision making
- ✅ Write complex conditional expressions
- ✅ Nest conditionals appropriately
- ✅ Use the ternary operator for simple conditions
- ✅ Understand Python 3.10+ match-case statements
- ✅ Apply best practices for readable conditionals

---

## Introduction to Control Flow

### What is Control Flow?

**Control flow** determines which code blocks execute based on conditions. It's like a decision tree - your program chooses different paths based on circumstances.

**Real-World Analogy** 🌍

Think of a traffic light:
- If RED → Stop
- If YELLOW → Slow down
- If GREEN → Go

Your code does the same - makes decisions based on conditions.

```python
# Simple control flow
age = 18

if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote")
```

---

## If Statements

### Basic If Statement

Execute code only if condition is True:

```python
age = 20

if age >= 18:
    print("You are an adult")
# Output: You are an adult

age = 15

if age >= 18:
    print("You are an adult")
# No output (condition is False)
```

### Multiple Statements in If Block

```python
score = 95

if score >= 90:
    print("Excellent!")
    print("You got an A!")
    grade = "A"
# All three statements execute if condition is True
```

### Indentation is Critical!

Python uses indentation to define code blocks:

```python
# ✅ CORRECT
if condition:
    print("This is indented")
    print("Part of if block")
print("This is not indented - always runs")

# ❌ WRONG
if condition:
print("Error! Not indented")  # IndentationError
```

### Conditions with Comparison Operators

```python
temperature = 75

if temperature > 80:
    print("It's hot!")

if temperature == 75:
    print("Perfect temperature!")

if temperature < 32:
    print("It's freezing!")
```

### Conditions with Logical Operators  

```python
age = 25
has_license = True

# AND - both must be True
if age >= 18 and has_license:
    print("You can drive!")

# OR - at least one must be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")

# NOT - inverts condition
is_raining = False

if not is_raining:
    print("Let's go outside!")
```

### Truthy and Falsy in If Statements

```python
# Empty string is falsy
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")  # This executes

# Non-empty string is truthy
name = "Alice"
if name:
    print(f"Hello, {name}")  # This executes

# Zero is falsy, non-zero is truthy
count = 0
if count:
    print("Has items")
else:
    print("Empty")  # This executes

# Empty list is falsy
items = []
if items:
    print("List has items")
else:
    print("List is empty")  # This executes
```

---

## If-Else Statements

### Basic If-Else

Execute one block if True, another if False:

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")
# Output: Too young to vote
```

### Multiple Statements in Each Block

```python
score = 75

if score >= 60:
    print("You passed!")
    grade = "Pass"
    can_advance = True
else:
    print("You failed")
    grade = "Fail"
    can_advance = False
```

### Practical Examples

```python
# Login system
password = input("Enter password: ")

if password == "secret123":
    print("Access granted!")
    print("Welcome back!")
else:
    print("Access denied")
    print("Try again")

# Even or odd
number = 17

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Positive or negative
value = -5

if value >= 0:
    print("Positive number")
else:
    print("Negative number")
```

---

## If-Elif-Else Statements

### Multiple Conditions

Check multiple conditions in sequence:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
# Output: Your grade is: B
```

**How it works:**
1. Checks first condition (score >= 90) - False, skip
2. Checks second condition (score >= 80) - True, execute and STOP
3. Remaining conditions are not checked!

### Order Matters!

```python
# ❌ WRONG - will never give "A"
score = 95

if score >= 60:
    grade = "D"  # This executes first!
elif score >= 70:
    grade = "C"  # Never checked
elif score >= 80:
    grade = "B"  # Never checked
elif score >= 90:
    grade = "A"  # Never checked
else:
    grade = "F"

# ✅ CORRECT - most restrictive first
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

### Multiple Elif Clauses

```python
day = "Monday"

if day == "Monday":
    print("Start of work week")
elif day == "Tuesday":
    print("Second day")
elif day == "Wednesday":
    print("Midweek")
elif day == "Thursday":
    print("Almost Friday")
elif day == "Friday":
    print("End of work week!")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Invalid day")
```

### Practical Examples

```python
# Temperature advice
temp = 68

if temp > 85:
    print("It's hot! Stay hydrated")
elif temp > 70:
    print("Nice weather!")
elif temp > 50:
    print("A bit cool, maybe a jacket")
elif temp > 32:
    print("Cold! Wear a coat")
else:
    print("Freezing! Stay indoors")

# BMI calculator
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f} - {category}")

# Ticket pricing
age = 25

if age < 3:
    price = 0
    print("Free admission")
elif age < 12:
    price = 10
    print("Child ticket: $10")
elif age < 65:
    price = 20
    print("Adult ticket: $20")
else:
    price = 15
    print("Senior ticket: $15")
```

---

## Nested Conditionals

### Basic Nesting

If statement inside another if:

```python
age = 25
has_license = True

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive!")
    else:
        print("You need a license to drive")
else:
    print("Too young to drive")
```

### Multiple Levels of Nesting

```python
username = "admin"
password = "secret"
is_active = True

if username == "admin":
    if password == "secret":
        if is_active:
            print("Login successful!")
        else:
            print("Account inactive")
    else:
        print("Wrong password")
else:
    print("User not found")
```

### Avoid Deep Nesting

```python
# ❌ BAD - hard to read
if condition1:
    if condition2:
        if condition3:
            if condition4:
                print("Too deep!")

# ✅ BETTER - use 'and'
if condition1 and condition2 and condition3 and condition4:
    print("Much clearer!")

# ✅ BETTER - early returns (in functions)
def check_access(user, password):
    if user != "admin":
        return "User not found"
    if password != "secret":
        return "Wrong password"
    if not is_active:
        return "Account inactive"
    return "Login successful!"
```

### Practical Nested Examples

```python
# Grade with extra credit
score = 88
extra_credit = 5

if score >= 60:
    if extra_credit > 0:
        final_score = score + extra_credit
        print(f"With extra credit: {final_score}")
    else:
        final_score = score
    
    if final_score >= 90:
        grade = "A"
    elif final_score >= 80:
        grade = "B"
    else:
        grade = "C"
    print(f"Grade: {grade}")
else:
    print("Failed")
```

---

## Conditional Expressions (Ternary Operator)

### Basic Syntax

```python
# Standard if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator (one line!)
status = "adult" if age >= 18 else "minor"

# Format: value_if_true if condition else value_if_false
```

### Practical Examples

```python
# Absolute value
x = -5
abs_x = x if x >= 0 else -x

# Min/max
a, b = 10, 20
minimum = a if a < b else b
maximum = a if a > b else b

# Even/odd
number = 7
parity = "even" if number % 2 == 0 else "odd"

# Discount
price = 100
has_coupon = True
final_price = price * 0.9 if has_coupon else price

# Sign of number
num = -5
sign = "positive" if num > 0 else ("negative" if num < 0 else "zero")
```

### When to Use

```python
# ✅ GOOD - simple condition
message = "Pass" if score >= 60 else "Fail"

# ✅ GOOD - inline value selection
print("Even" if num % 2 == 0 else "Odd")

# ❌ BAD - too complex, use regular if-else
result = value1 if cond1 else (value2 if cond2 else (value3 if cond3 else value4))

# ✅ BETTER
if cond1:
    result = value1
elif cond2:
    result = value2
elif cond3:
    result = value3
else:
    result = value4
```

---

## Match-Case Statements

*Python 3.10+ only*

### Basic Match-Case

Similar to switch-case in other languages:

```python
# Python 3.10+
day = "Monday"

match day:
    case "Monday":
        print("Start of week")
    case "Tuesday":
        print("Second day")
    case "Wednesday":
        print("Midweek")
    case "Thursday":
        print("Almost Friday")
    case "Friday":
        print("TGIF!")
    case "Saturday" | "Sunday":  # Multiple patterns
        print("Weekend!")
    case _:  # Default case
        print("Invalid day")
```

### Matching Values

```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status")
```

### Matching with Guards

```python
age = 25

match age:
    case age if age < 13:
        category = "Child"
    case age if age < 20:
        category = "Teenager"
    case age if age < 65:
        category = "Adult"
    case _:
        category = "Senior"
```

### Pattern Matching (Advanced)

```python
# Matching sequences
point = (0, 0)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at y={y}")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# Matching dictionaries
user = {"name": "Alice", "role": "admin"}

match user:
    case {"role": "admin"}:
        print("Admin access granted")
    case {"role": "user"}:
        print("User access granted")
    case _:
        print("No access")
```

---

## Best Practices

### 1. Use Descriptive Conditions

```python
# ❌ BAD
if x > 18:
    ...

# ✅ GOOD
MIN_AGE = 18
if age > MIN_AGE:
    ...

# Even better with descriptive variable
is_adult = age >= 18
if is_adult:
    ...
```

### 2. Keep Conditions Simple

```python
# ❌ BAD
if (user.is_authenticated and user.has_permission("edit") and 
    not user.is_banned and user.email_verified and 
    user.account_active):
    ...

# ✅ BETTER
can_edit = (user.is_authenticated and 
            user.has_permission("edit") and
            not user.is_banned and
            user.email_verified and
            user.account_active)
            
if can_edit:
    ...
```

### 3. Avoid Comparing to True/False

```python
# ❌ BAD
if is_valid == True:
    ...

if has_items == False:
    ...

# ✅ GOOD
if is_valid:
    ...

if not has_items:
    ...
```

### 4. Use 'in' for Multiple Comparisons

```python
# ❌ BAD
if day == "Saturday" or day == "Sunday":
    ...

# ✅ GOOD
if day in ["Saturday", "Sunday"]:
    ...

if day in ("Saturday", "Sunday"):  # Tuple is more efficient
    ...
```

### 5. Avoid Redundant Else

```python
# ❌ REDUNDANT
def is_positive(num):
    if num > 0:
        return True
    else:
        return False

# ✅ SIMPLE
def is_positive(num):
    return num > 0
```

### 6. Use Early Returns

```python
# ❌ NESTED
def process(data):
    if data is not None:
        if len(data) > 0:
            if data.is_valid():
                return data.process()
            else:
                return "Invalid"
        else:
            return "Empty"
    else:
        return "None"

# ✅ EARLY RETURNS
def process(data):
    if data is None:
        return "None"
    if len(data) == 0:
        return "Empty"
    if not data.is_valid():
        return "Invalid"
    return data.process()
```

---

## Practice Exercises

### Beginner Exercises

**Exercise 1: Age Category**
```python
# Classify age into: baby (<2), child (2-12), teen (13-19), adult (20+)
age = 15
```

**Exercise 2: Pass/Fail**
```python
# Print "Pass" if score >= 60, else "Fail"
score = 75
```

**Exercise 3: Positive/Negative/Zero**
```python
# Check if number is positive, negative, or zero
number = -5
```

**Exercise 4: Even or Odd**
```python
# Determine if number is even or odd
number = 42
```

**Exercise 5: Maximum of Two**
```python
# Find and print the larger of two numbers
a = 10
b = 20
```

### Intermediate Exercises

**Exercise 6: Letter Grade**
```python
# Assign letter grade: A (90-100), B (80-89), C (70-79), D (60-69), F (<60)
score = 85
```

**Exercise 7: Leap Year**
```python
# Check if year is a leap year
# Leap if: divisible by 4 AND (not divisible by 100 OR divisible by 400)
year = 2024
```

**Exercise 8: Triangle Type**
```python
# Determine triangle type: equilateral, isosceles, or scalene
side1, side2, side3 = 5, 5, 8
```

**Exercise 9: Ticket Price**
```python
# Calculate ticket price:
# Age < 3: Free
# Age 3-12: $10
# Age 13-64: $20
# Age 65+: $15
age = 25
```

**Exercise 10: Login System**
```python
# Check username AND password
# username: "admin", password: "secret123"
username = input("Username: ")
password = input("Password: ")
```

### Advanced Exercises

**Exercise 11: Calculator**
```python
# Implement basic calculator (+, -, *, /)
num1 = 10
num2 = 5
operation = "+"
```

**Exercise 12: Date Validator**
```python
# Check if date is valid (consider month lengths)
day = 31
month = 2
year = 2024
```

**Exercise 13: Grade with Curves**
```python
# Apply curve: +5 points if avg < 70
# Then assign grade
score = 68
class_average = 65
```

**Exercise 14: Quadrant Finder**
```python
# Determine which quadrant a point (x,y) is in
# Or on axis, or origin
x = 5
y = -3
```

**Exercise 15: Rock Paper Scissors**
```python
# Determine winner
player1 = "rock"
player2 = "scissors"
# Who wins?
```

---

## 🎯 Key Takeaways

✅ **if** executes code when condition is True  
✅ **if-else** chooses between two paths  
✅ **if-elif-else** handles multiple conditions  
✅ Conditions are checked **in order** - first match wins  
✅ **Indentation** defines code blocks  
✅ Use **and**, **or**, **not** for complex conditions  
✅ **Ternary operator**: `value_if_true if condition else value_if_false`  
✅ **match-case** (Python 3.10+) is like switch-case  
✅ Avoid deep nesting - use early returns or combine conditions  

---

## 📚 Quick Reference

```python
# If
if condition:
    # code

# If-Else
if condition:
    # code
else:
    # code

# If-Elif-Else
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code

# Ternary
value = true_val if condition else false_val

# Match-Case (Python 3.10+)
match variable:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default
```

---

**End of Control Flow Notes** 📝

**Next:** Practice with loops and conditionals together!

## Advanced Control Flow Patterns

### Pattern 1: Guard Clauses

Early returns to reduce nesting:

```python
def process_user(user):
    # ❌ BAD: Deep nesting
    if user is not None:
        if user.is_active:
            if user.has_permission("edit"):
                return "Processing..."
            else:
                return "No permission"
        else:
            return "User inactive"
    else:
        return "User not found"
    
    # ✅ GOOD: Guard clauses
    if user is None:
        return "User not found"
    
    if not user.is_active:
        return "User inactive"
    
    if not user.has_permission("edit"):
        return "No permission"
    
    return "Processing..."
```

### Pattern 2: Dictionary Dispatch

Replace long if-elif chains:

```python
# ❌ VERBOSE
def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b

# ✅ CLEANER
def calculate(operation, a, b):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y
    }
    return operations[operation](a, b)
```

### Pattern 3: Validation Chains

```python
def validate_user_input(data):
    """Multiple validation checks"""
    errors = []
    
    if not data.get('username'):
        errors.append("Username required")
    elif len(data['username']) < 3:
        errors.append("Username too short")
    
    if not data.get('email'):
        errors.append("Email required")
    elif '@' not in data['email']:
        errors.append("Invalid email")
    
    if not data.get('age'):
        errors.append("Age required")
    elif data['age'] < 18:
        errors.append("Must be 18+")
    
    if errors:
        return False, errors
    return True, []

# Usage
data = {"username": "ab", "email": "invalid", "age": 15}
valid, errors = validate_user_input(data)
if not valid:
    for error in errors:
        print(f"Error: {error}")
```

---

## Match-Case Advanced Examples (Python 3.10+)

### Pattern Matching with Guards

```python
def classify_number(num):
    match num:
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"
        case n if n < 10:
            return "Small positive"
        case n if n < 100:
            return "Medium positive"
        case _:
            return "Large positive"

print(classify_number(-5))   # "Negative"
print(classify_number(5))    # "Small positive"
print(classify_number(50))   # "Medium positive"
print(classify_number(500))  # "Large positive"
```

### Matching Data Structures

```python
def process_command(command):
    match command:
        case ["quit"] | ["exit"]:
            return "Exiting..."
        
        case ["help"]:
            return "Available commands: quit, help, echo <msg>"
        
        case ["echo", *message]:
            return " ".join(message)
        
        case ["add", x, y]:
            return int(x) + int(y)
        
        case _:
            return "Unknown command"

print(process_command(["echo", "Hello", "World"]))  # "Hello World"
print(process_command(["add", "5", "3"]))           # 8
```

---

## Error Handling in Control Flow

### Try-Except with Else and Finally

```python
def read_config(filename):
    """Read configuration with proper error handling"""
    try:
        file = open(filename, 'r')
        data = file.read()
    except FileNotFoundError:
        print(f"Config file {filename} not found")
        return None
    except PermissionError:
        print(f"No permission to read {filename}")
        return None
    else:
        # Runs only if no exception
        print("Config loaded successfully")
        return data
    finally:
        # Always runs
        try:
            file.close()
        except:
            pass
```

### Custom Error Handling Flow

```python
class ValidationError(Exception):
    pass

def process_data(data):
    try:
        # Validate
        if not data:
            raise ValidationError("Data cannot be empty")
        
        if not isinstance(data, dict):
            raise ValidationError("Data must be a dictionary")
        
        # Process
        result = data.get('value', 0) * 2
        return result
    
    except ValidationError as e:
        print(f"Validation failed: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

---

## Real-World Control Flow Examples

### Example 1: State Machine

```python
class TrafficLight:
    def __init__(self):
        self.state = "RED"
    
    def next_state(self):
        if self.state == "RED":
            self.state = "YELLOW"
            action = "Prepare to go"
        elif self.state == "YELLOW":
            self.state = "GREEN"
            action = "Go!"
        elif self.state == "GREEN":
            self.state = "RED"
            action = "Stop!"
        else:
            self.state = "RED"
            action = "Reset to stop"
        
        return action

# Usage
light = TrafficLight()
for _ in range(6):
    action = light.next_state()
    print(f"Light: {light.state}, Action: {action}")
```

### Example 2: Menu System

```python
def show_menu():
    print("\n=== Main Menu ===")
    print("1. View Profile")
    print("2. Edit Settings")
    print("3. Logout")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("Viewing profile...")
        elif choice == "2":
            print("Editing settings...")
        elif choice == "3":
            print("Logging out...")
            continue
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            continue
        
        # Ask if user wants to continue
        again = input("Return to menu? (y/n): ")
        if again.lower() != 'y':
            break

# main()  # Uncomment to run
```

### Example 3: Input Validation Loop

```python
def get_valid_age():
    """Keep asking until valid age is entered"""
    while True:
        try:
            age_str = input("Enter your age (18-120): ")
            age = int(age_str)
            
            if age < 18:
                print("Must be 18 or older")
                continue
            
            if age > 120:
                print("Please enter a realistic age")
                continue
            
            return age
        
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nCancelled")
            return None

# age = get_valid_age()
# print(f"Your age: {age}")
```

---

## Control Flow Best Practices

### DO's ✅

1. **Use guard clauses** to reduce nesting
2. **Keep conditions simple** and readable
3. **Use meaningful variable names** in conditions
4. **Handle edge cases** early
5. **Use elif** to avoid redundant checks

### DON'Ts ❌

1. **Don't nest too deeply** (max 3-4 levels)
2. **Don't use complex boolean expressions** without parentheses
3. **Don't forget the else case** when needed
4. **Don't use magic numbers** in conditions

---

## Performance Considerations

### Short-Circuit Evaluation

```python
# Python stops evaluating as soon as result is known

# OR: stops at first True
result = True or expensive_function()
# expensive_function() never runs!

# AND: stops at first False
result = False and expensive_function()
# expensive_function() never runs!

# Use this for safety
if user and user.is_active:
    # user.is_active only checked if user exists
    process_user(user)
```

---

**End of Control Flow Notes** ���

Master control flow for writing clean, efficient Python programs!
