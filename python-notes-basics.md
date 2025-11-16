# Python Programming: Fundamental Notes

---

## 1. Variables and Data Types

### What are Variables?
- **Variables** store data that can change during program execution.
- No need to declare type in Python; it's inferred from the assignment.
- Example:
    ```python
    x = 10        # Integer
    pi = 3.14     # Float
    name = "Alice"  # String
    is_valid = True # Boolean
    ```

### Data Types Overview

| Type      | Example          | Description                      |
|-----------|------------------|----------------------------------|
| int       | `x = 5`          | Whole numbers                    |
| float     | `y = 3.14`       | Decimal numbers                  |
| str       | `name = "Alice"` | Textual data (strings)           |
| bool      | `flag = True`    | True/False (Boolean values)      |

#### Integer (`int`)
```python
count = 42
negative = -7
```

#### Float (`float`)
```python
height = 175.5
```

#### String (`str`)
```python
msg = "Hello, World!"
```

#### Boolean (`bool`)
```python
completed = False
```

---

## 2. Type Conversion and Type Checking

### Implicit Type Conversion (Automatic)
Sometimes Python converts types automatically:
```python
a = 5      # int
b = 2.0    # float
result = a + b  # result is a float (7.0)
```

### Explicit Type Conversion (Casting)
Use built-in functions to convert between types:
- `int()`, `float()`, `str()`, `bool()`
```python
age = int("24")         # from string to int
price = float("49.99")  # from string to float
is_active = bool(1)     # from int to bool (True)
text = str(3000)        # from int to string
```

#### Error Handling Example:
```python
val = "ten"
# int(val)  # Raises ValueError
```

### Type Checking

#### The `type()` Function:
```python
x = 10
print(type(x))  # <class 'int'>
```

#### The `isinstance()` Function:
```python
num = 3.14
print(isinstance(num, float))  # True
print(isinstance(num, (int, float)))  # True
```

---

## 3. Input/Output Operations

### Output: `print()`
```python
print("Hello, World!")
name = "Alice"
print("Hello,", name)
```

### Input: `input()`
```python
user_input = input("Enter something: ")
print("You entered:", user_input)
```
*Note:* `input()` always returns string. Convert as needed:
```python
age = int(input("How old are you? "))
```

---

## 4. String Manipulation and Formatting

### Basic String Operations
- Concatenation: `greeting + " " + name`
- Repetition: `"hello" * 3` → `'hellohellohello'`
- Slicing: `msg[0:5]` gets first 5 characters

### Common String Methods
```python
txt = "Python is Awesome"
print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.strip())      # Removes whitespace
print(txt.replace("Awesome", "great"))
print("abc123".isalnum())  # True
```

### String Formatting

#### f-Strings (Python 3.6+)
```python
name = "Alice"
score = 97
print(f"{name}'s score is {score}.")
```

#### `.format()` Method
```python
template = "{} scored {} marks."
msg = template.format("Bob", 88)
print(msg)
```

#### Old Style `%` Operator
```python
text = "Value: %d" % 42
```

---

## 5. Operators

### Arithmetic Operators

| Operator | Description | Example      | Result |
|----------|-------------|--------------|--------|
| +        | Addition    | `x + y`      | sum    |
| -        | Subtraction | `x - y`      | diff   |
| *        | Multiplication|`x * y`     | prod   |
| /        | Division    | `x / y`      | quotient (float) |
| //       | Floor Division| `x // y`  | int division |
| %        | Modulus     | `x % y`      | remainder |
| **       | Power       | `x ** y`     | x^y    |

### Comparison Operators

| Operator | Description           | Example    |
|----------|-----------------------|------------|
| ==       | Equal to              | `x == y`   |
| !=       | Not equal to          | `x != y`   |
| >        | Greater than          | `x > y`    |
| <        | Less than             | `x < y`    |
| >=       | Greater or equal      | `x >= y`   |
| <=       | Less or equal         | `x <= y`   |

### Logical Operators

| Operator | Description                   | Example        |
|----------|-------------------------------|----------------|
| and      | True if both are true         | `x > 1 and y < 10` |
| or       | True if at least one is true  | `x < 1 or y > 10`  |
| not      | True if operand is false      | `not x`            |

### Bitwise Operators

| Operator | Description     | Example     |
|----------|-----------------|------------|
| &        | AND             | `x & y`    |
| |        | OR              | `x | y`    |
| ^        | XOR             | `x ^ y`    |
| ~        | NOT             | `~x`       |
| <<       | Left Shift      | `x << y`   |
| >>       | Right Shift     | `x >> y`   |

---

## 6. Operator Precedence

Python follows operator precedence (order of operations):

1. Parentheses: `()`
2. Exponents: `**`
3. Unary plus/minus: `+x`, `-x`
4. Multiplication/Division/Floor/Modulus: `* / // %`
5. Addition/Subtraction: `+ -`
6. Bitwise shifts: `<< >>`
7. Bitwise AND: `&`
8. Bitwise XOR/OR: `^ |`
9. Comparison: `< > <= >= == !=`
10. Logical NOT: `not`
11. Logical AND: `and`
12. Logical OR: `or`

**Example:**
```python
result = 5 + 2 * 3      # 5 + (2*3) = 11
result2 = (5 + 2) * 3   # (5+2)*3 = 21
```

---

# End of Notes
