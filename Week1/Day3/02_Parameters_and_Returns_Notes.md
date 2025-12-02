# Parameters and Returns in Python - Complete Guide

This guide is a deep dive into function parameters and return values. For basic function concepts, see `Functions_Basics_Notes.md`.

## 📚 Table of Contents
1. [Positional Parameters](#positional-parameters)
2. [Keyword Parameters](#keyword-parameters)
3. [Default Parameters](#default-parameters)
4. [Variable-Length Arguments (*args)](#variable-length-arguments-args)
5. [Variable-Length Keyword Arguments (**kwargs)](#variable-length-keyword-arguments-kwargs)
6. [Parameter Order Rules](#parameter-order-rules)
7. [Return Values](#return-values)
8. [Advanced Return Patterns](#advanced-return-patterns)
9. [Practice Exercises](#practice-exercises)

---

## 🎯 Learning Objectives

- ✅ Master all parameter types
- ✅ Use *args and **kwargs effectively
- ✅ Understand parameter order rules
- ✅ Return multiple values
- ✅ Use early returns and guard clauses
- ✅ Apply best practices for parameters and returns

---

## Positional Parameters

### Basic Positional Parameters

```python
def greet(first, last):
    print(f"Hello, {first} {last}!")

# Order matters!
greet("John", "Doe")  # Hello, John Doe!
greet("Doe", "John")  # Hello, Doe John! (wrong!)
```

### Multiple Positional Parameters

```python
def calculate_total(price, quantity, tax_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

total = calculate_total(10.99, 3, 0.08)
print(f"${total:.2f}")  # $35.60
```

---

## Keyword Parameters

### Basic Keyword Arguments

```python
def greet(first, last):
    print(f"Hello, {first} {last}!")

# Specify parameters by name - order doesn't matter
greet(first="John", last="Doe")
greet(last="Doe", first="John")  # Same result!
```

### Mixing Positional and Keyword

```python
def create_user(username, email, age, city):
    return {
        "username": username,
        "email": email,
        "age": age,
        "city": city
    }

# Mix positional and keyword
user = create_user("alice", email="alice@email.com", age=25, city="NYC")

# Positional must come before keyword!
# user = create_user(username="alice", "alice@email.com")  # SyntaxError!
```

---

## Default Parameters

### Basic Defaults

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", greeting="Hey")  # Hey, Charlie!
```

### Multiple Defaults

```python
def create_user(username, active=True, role="user", verified=False):
    return {
        "username": username,
        "active": active,
        "role": role,
        "verified": verified
    }

# Use all defaults
user1 = create_user("alice")
# {'username': 'alice', 'active': True, 'role': 'user', 'verified': False}

# Override specific defaults
user2 = create_user("bob", role="admin")
# {'username': 'bob', 'active': True, 'role': 'admin', 'verified': False}

user3 = create_user("charlie", verified=True, active=False)
# {'username': 'charlie', 'active': False, 'role': 'user', 'verified': True}
```

### ⚠️ Mutable Default Arguments (Gotcha!)

```python
# ❌ WRONG - Dangerous!
def add_item(item, items=[]):
    items.append(item)
    return items

list1 = add_item("apple")   # ['apple']
list2 = add_item("banana")  # ['apple', 'banana'] - WTF?!
# Same list is reused!

# ✅ CORRECT - Use None
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item("apple")   # ['apple']
list2 = add_item("banana")  # ['banana'] - Correct!
```

---

## Variable-Length Arguments (*args)

### Basic *args

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(1, 2, 3, 4, 5))     # 15
print(sum_all(10))                 # 10
print(sum_all())                   # 0
```

### *args Creates a Tuple

```python
def print_args(*args):
    print(f"Type: {type(args)}")  # <class 'tuple'>
    print(f"Args: {args}")
    print(f"Length: {len(args)}")

print_args(1, 2, 3)
# Type: <class 'tuple'>
# Args: (1, 2, 3)
# Length: 3
```

### Combining Regular Parameters with *args

```python
def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Unpacking with *

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks list into arguments
print(result)  # 6

# Same as: add(1, 2, 3)
```

---

## Variable-Length Keyword Arguments (**kwargs)

### Basic **kwargs

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC
```

### **kwargs Creates a Dictionary

```python
def print_kwargs(**kwargs):
    print(f"Type: {type(kwargs)}")  # <class 'dict'>
    print(f"kwargs: {kwargs}")

print_kwargs(a=1, b=2, c=3)
# Type: <class 'dict'>
# kwargs: {'a': 1, 'b': 2, 'c': 3}
```

### Combining Parameters with **kwargs

```python
def create_user(username, **details):
    user = {"username": username}
    user.update(details)
    return user

user = create_user("alice", age=25, city="NYC", role="admin")
# {'username': 'alice', 'age': 25, 'city': 'NYC', 'role': 'admin'}
```

### Unpacking with **

```python
def greet(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

person = {"name": "Alice", "age": 25, "city": "NYC"}
greet(**person)  # Unpacks dict into keyword arguments
# Alice is 25 years old and lives in NYC
```

---

## Parameter Order Rules

### Correct Parameter Order

```python
def function(
    positional_only, /,       # Positional-only (Python 3.8+)
    positional_or_keyword,     # Standard
    *args,                     # Variable positional
    keyword_only, *,           # Keyword-only
    **kwargs                   # Variable keyword
):
    pass

# Example
def example(a, b, /, c, d, *args, e, f, **kwargs):
    print(f"a={a}, b={b}")           # Positional-only
    print(f"c={c}, d={d}")           # Positional or keyword
    print(f"args={args}")             # Extra positional
    print(f"e={e}, f={f}")           # Keyword-only
    print(f"kwargs={kwargs}")         # Extra keyword

example(1, 2, 3, 4, 5, 6, e=7, f=8, g=9, h=10)
```

### Common Parameter Patterns

```python
# Pattern 1: Regular + defaults
def func(required, optional="default"):
    pass

# Pattern 2: Regular + *args
def func(first, *rest):
    pass

# Pattern 3: Regular + **kwargs
def func(required, **options):
    pass

# Pattern 4: All three
def func(required, *args, **kwargs):
    pass

# Pattern 5: Defaults + *args + **kwargs
def func(a, b=10, *args, **kwargs):
    pass
```

---

## Return Values

### Single Return Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

### Multiple Return Values (Tuple)

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Can also return as tuple
result = get_min_max([1, 5, 3, 9, 2])
print(result)  # (1, 9)
```

### Return Dictionary

```python
def get_stats(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": sum(numbers) / len(numbers)
    }

stats = get_stats([1, 2, 3, 4, 5])
print(stats["min"])  # 1
print(stats["avg"])  # 3.0
```

### Return List

```python
def get_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

result = get_even_numbers([1, 2, 3, 4, 5, 6])
print(result)  # [2, 4, 6]
```

---

## Advanced Return Patterns

### Early Return (Guard Clauses)

```python
# ❌ Deeply nested
def calculate_discount(price, customer_type):
    if customer_type == "premium":
        if price > 100:
            return price * 0.8
        else:
            return price * 0.9
    else:
        if price > 100:
            return price * 0.95
        else:
            return price

# ✅ Early returns
def calculate_discount(price, customer_type):
    if customer_type == "premium" and price > 100:
        return price * 0.8
    if customer_type == "premium":
        return price * 0.9
    if price > 100:
        return price * 0.95
    return price
```

### Return None for Errors

```python
def safe_divide(a, b):
    if b == 0:
        return None  # Indicate error
    return a / b

result = safe_divide(10, 2)
if result is not None:
    print(f"Result: {result}")
else:
    print("Error: Division by zero")
```

### Return Boolean for Success/Failure

```python
def save_user(user_data):
    try:
        # Save logic here
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if save_user(data):
    print("User saved successfully")
else:
    print("Failed to save user")
```

---

## Practice Exercises

### Beginner

**Exercise 1**: Function with 2 positional parameters

**Exercise 2**: Function with default parameter

**Exercise 3**: Function returning multiple values

**Exercise 4**: Function with keyword parameters

**Exercise 5**: Function using *args to sum numbers

### Intermediate

**Exercise 6**: Function with mixed parameters (positional, default, *args)

**Exercise 7**: Function using **kwargs to create dict

**Exercise 8**: Function with early return for error handling

**Exercise 9**: Function that unpacks list with *

**Exercise 10**: Function that unpacks dict with **

### Advanced

**Exercise 11**: Create flexible API wrapper using *args and **kwargs

**Exercise 12**: Decorator function (uses parameters and returns)

**Exercise 13**: Function with all parameter types in correct order

**Exercise 14**: Currying function (returns function)

**Exercise 15**: Memoization decorator

---

## 🎯 Key Takeaways

✅ **Positional** parameters: order matters  
✅ **Keyword** parameters: specify by name  
✅ **Default** parameters: provide fallback values  
✅ ***args**: variable positional arguments (tuple)  
✅ ****kwargs**: variable keyword arguments (dict)  
✅ **Parameter order**: positional, *args, keyword-only, **kwargs  
✅ **Multiple returns**: use tuple unpacking  
✅ **Early returns**: cleaner than nested if-else  

---

## 📚 Quick Reference

```python
# Parameters
def func(a, b):              # Positional
def func(a, b=10):           # Default
def func(a, b, *args):       # Variable positional
def func(a, b, **kwargs):    # Variable keyword
def func(a, *args, **kwargs): # All three

# Calling
func(1, 2)                   # Positional
func(a=1, b=2)               # Keyword
func(*[1, 2])                # Unpack list
func(**{"a": 1, "b": 2})     # Unpack dict

# Returns
return value                 # Single
return a, b, c               # Multiple (tuple)
return {"key": "value"}      # Dict
return [1, 2, 3]             # List
return None                  # No value/error
```

---

**End of Parameters and Returns Notes** 📝

Continue exploring advanced function topics!

## Advanced Parameter Patterns

### Variadic Functions with Mixed Parameters

```python
def create_user(name, email, *hobbies, role="user", **metadata):
    """Complex parameter combination"""
    user = {
        'name': name,
        'email': email,
        'role': role,
        'hobbies': list(hobbies),
        'metadata': metadata
    }
    return user

# Usage
user = create_user(
    "Alice", 
    "alice@example.com",
    "reading", "coding", "gaming",
    role="admin",
    age=25,
    city="NYC"
)
print(user)
# {'name': 'Alice', 'email': 'alice@example.com', 
#  'role': 'admin', 'hobbies': ['reading', 'coding', 'gaming'],
#  'metadata': {'age': 25, 'city': 'NYC'}}
```

### Parameter Validation Decorator

```python
def validate_params(**validators):
    """Decorator to validate function parameters"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get function parameter names
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            
            # Validate each parameter
            for param_name, validator in validators.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not validator(value):
                        raise ValueError(f"Invalid {param_name}: {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage
@validate_params(
    age=lambda x: 0 < x < 150,
    email=lambda x: '@' in x
)
def register_user(name, age, email):
    return f"Registered {name}, {age}, {email}"

# Valid
print(register_user("Alice", 25, "alice@example.com"))

# Invalid - raises ValueError
# register_user("Bob", -5, "invalid")
```

###Unpacking in Function Calls

```python
def calculate_total(price, quantity, tax_rate, discount=0):
    """Calculate total with all parameters"""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax - discount
    return total

# Unpack dictionary as keyword arguments
params = {
    'price': 10.99,
    'quantity': 3,
    'tax_rate': 0.08,
    'discount': 5.00
}

total = calculate_total(**params)
print(f"Total: ${total:.2f}")

# Unpack list/tuple as positional arguments
args = [10.99, 3, 0.08]
total = calculate_total(*args)
print(f"Total: ${total:.2f}")
```

---

## Return Value Patterns

### Multiple Return Values (Named Tuple)

```python
from collections import namedtuple

def analyze_text(text):
    """Analyze text and return structured results"""
    Result = namedtuple('Result', ['word_count', 'char_count', 'line_count'])
    
    words = len(text.split())
    chars = len(text)
    lines = text.count('\n') + 1
    
    return Result(words, chars, lines)

# Usage
result = analyze_text("Hello\nWorld\nPython")
print(f"Words: {result.word_count}")
print(f"Characters: {result.char_count}")
print(f"Lines: {result.line_count}")
```

### Returning Functions (Factory Pattern)

```python
def make_multiplier(factor):
    """Return a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Create specific multipliers
double = make_multiplier(2)
triple = make_multiplier(3)
times_10 = make_multiplier(10)

print(double(5))    # 10
print(triple(5))    # 15
print(times_10(5))  # 50
```

### Context-Based Returns

```python
def divide(a, b, return_remainder=False):
    """Return quotient or both quotient and remainder"""
    quotient = a // b
    
    if return_remainder:
        remainder = a % b
        return quotient, remainder
    
    return quotient

# Different return types based on parameter
result = divide(17, 5)
print(result)  # 3

result = divide(17, 5, return_remainder=True)
print(result)  # (3, 2)
```

---

## Real-World Applications

### Application 1: API Request Handler

```python
def api_request(endpoint, method="GET", **params):
    """Simulate API request with flexible parameters"""
    request = {
        'endpoint': endpoint,
        'method': method,
        'params': params
    }
    
    # Simulate processing
    print(f"Making {method} request to {endpoint}")
    for key, value in params.items():
        print(f"  {key}: {value}")
    
    return {'status': 'success', 'data': request}

# Usage
response = api_request(
    "/users",
    method="POST",
    name="Alice",
    email="alice@example.com",
    age=25
)
```

### Application 2: Configuration Builder

```python
def build_config(app_name, *required_modules, debug=False, **settings):
    """Build application configuration"""
    config = {
        'app_name': app_name,
        'modules': list(required_modules),
        'debug': debug,
        'settings': settings
    }
    
    # Validate required modules
    if not required_modules:
        raise ValueError("At least one module required")
    
    return config

# Usage
config = build_config(
    "MyApp",
    "database",
    "cache",
    "auth",
    debug=True,
    db_host="localhost",
    cache_ttl=3600
)
print(config)
```

---

## Parameter Best Practices

### DO's ✅

1. **Use descriptive parameter names**
2. **Provide sensible defaults**
3. **Use type hints**
4. **Document parameters in docstrings**
5. **Validate input parameters**

```python
def calculate_discount(
    price: float,
    discount_percent: float = 10.0,
    apply_tax: bool = True
) -> float:
    """
    Calculate final price after discount and tax.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (default 10%)
        apply_tax: Whether to apply tax (default True)
    
    Returns:
        Final price after discount and tax
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be positive")
    
    discounted = price * (1 - discount_percent / 100)
    
    if apply_tax:
        discounted *= 1.08  # 8% tax
    
    return round(discounted, 2)
```

### DON'Ts ❌

1. **Don't use mutable defaults**
2. **Don't have too many parameters (max 5-7)**
3. **Don't modify mutable arguments**
4. **Don't use unclear abbreviations**

```python
# ❌ BAD
def process(d, l=[]):  # Mutable default!
    l.append(d)
    return l

# ✅ GOOD
def process(data, items=None):
    if items is None:
        items = []
    items.append(data)
    return items
```

---

## Common Patterns

### Pattern 1: Builder Pattern with Kwargs

```python
class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self.conditions = []
        self.order = None
        self.limit_value = None
    
    def where(self, **conditions):
        for key, value in conditions.items():
            self.conditions.append(f"{key} = {value}")
        return self
    
    def order_by(self, field):
        self.order = field
        return self
    
    def limit(self, n):
        self.limit_value = n
        return self
    
    def build(self):
        query = f"SELECT * FROM {self.table}"
        
        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)
        
        if self.order:
            query += f" ORDER BY {self.order}"
        
        if self.limit_value:
            query += f" LIMIT {self.limit_value}"
        
        return query

# Usage
query = (QueryBuilder("users")
         .where(age=25, city="NYC")
         .order_by("name")
         .limit(10)
         .build())

print(query)
# SELECT * FROM users WHERE age = 25 AND city = NYC ORDER BY name LIMIT 10
```

### Pattern 2: Pipeline Functions

```python
def pipeline(*functions):
    """Create a pipeline of functions"""
    def process(value):
        result = value
        for func in functions:
            result = func(result)
        return result
    return process

# Individual functions
def double(x):
    return x * 2

def add_10(x):
    return x + 10

def square(x):
    return x ** 2

# Create pipeline
process = pipeline(double, add_10, square)
result = process(5)  # ((5 * 2) + 10) ** 2 = 400
print(result)
```

---

**End of Parameters and Returns Notes** ���

Master parameter handling for flexible, powerful Python functions!

## Advanced Return Patterns

### Generator Functions

```python
def generate_fibonacci(n):
    """Generate Fibonacci sequence using yield"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
for num in generate_fibonacci(10):
    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34

# Create list from generator
fib_list = list(generate_fibonacci(10))
print(fib_list)
```

### Return Type Annotations

```python
from typing import List, Dict, Tuple, Optional, Union

def get_user_data(user_id: int) -> Dict[str, Union[str, int]]:
    """Return user data with type hints"""
    return {
        'id': user_id,
        'name': 'Alice',
        'age': 25,
        'email': 'alice@example.com'
    }

def find_user(name: str) -> Optional[Dict[str, any]]:
    """Return user or None if not found"""
    # Search database...
    if name == "Alice":
        return {'name': 'Alice', 'age': 25}
    return None

def process_items(items: List[str]) -> Tuple[int, List[str]]:
    """Return count and processed items"""
    processed = [item.upper() for item in items]
    return len(processed), processed
```

### Context Managers (Advanced Returns)

```python
class FileManager:
    """Context manager example"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

---

## Parameter Validation Patterns

### Type Checking

```python
def calculate_age(birth_year: int, current_year: int = 2024) -> int:
    """Calculate age with type validation"""
    if not isinstance(birth_year, int):
        raise TypeError(f"birth_year must be int, got {type(birth_year)}")
    
    if not isinstance(current_year, int):
        raise TypeError(f"current_year must be int, got {type(current_year)}")
    
    if birth_year > current_year:
        raise ValueError("birth_year cannot be in the future")
    
    if birth_year < 1900:
        raise ValueError("birth_year seems unrealistic")
    
    return current_year - birth_year

# Usage
age = calculate_age(1995)
print(f"Age: {age}")  # 29
```

### Range Validation

```python
def set_volume(level: int) -> None:
    """Set volume with range validation"""
    if not 0 <= level <= 100:
        raise ValueError(f"Volume must be 0-100, got {level}")
    
    print(f"Volume set to {level}")

def create_password(length: int = 12) -> str:
    """Generate password with length validation"""
    if not 8 <= length <= 128:
        raise ValueError("Password length must be 8-128 characters")
    
    import random
    import string
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
```

---

## Practical Examples

### Example 1: Database Query Builder

```python
def query_users(
    *fields,
    where: dict = None,
    order_by: str = None,
    limit: int = None,
    **options
):
    """Build SQL query for users table"""
    # Default fields
    if not fields:
        fields = ('*',)
    
    # Build query
    query = f"SELECT {', '.join(fields)} FROM users"
    
    # WHERE clause
    if where:
        conditions = [f"{k} = '{v}'" for k, v in where.items()]
        query += f" WHERE {' AND '.join(conditions)}"
    
    # ORDER BY
    if order_by:
        query += f" ORDER BY {order_by}"
    
    # LIMIT
    if limit:
        query += f" LIMIT {limit}"
    
    # Additional options
    if options.get('distinct'):
        query = query.replace('SELECT', 'SELECT DISTINCT')
    
    return query

# Usage examples
q1 = query_users('name', 'email')
# SELECT name, email FROM users

q2 = query_users('*', where={'age': 25, 'city': 'NYC'})
# SELECT * FROM users WHERE age = '25' AND city = 'NYC'

q3 = query_users('name', order_by='age DESC', limit=10)
# SELECT name FROM users ORDER BY age DESC LIMIT 10
```

### Example 2: API Response Builder

```python
def api_response(
    data=None,
    error=None,
    status_code: int = 200,
    **metadata
):
    """Build standardized API response"""
    response = {
        'status_code': status_code,
        'success': error is None,
        'timestamp': '2024-12-02T10:00:00Z'
    }
    
    if data is not None:
        response['data'] = data
    
    if error is not None:
        response['error'] = error
        response['success'] = False
    
    # Add metadata
    if metadata:
        response['metadata'] = metadata
    
    return response

# Usage
success_response = api_response(
    data={'users': [{'name': 'Alice'}]},
    status_code=200,
    page=1,
    total=100
)

error_response = api_response(
    error='User not found',
    status_code=404
)
```

### Example 3: Logging Decorator

```python
def log_calls(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"Calling {func.__name__}({all_args})")
        
        result = func(*args, **kwargs)
        
        print(f"{func.__name__} returned {result!r}")
        
        return result
    
    return wrapper

@log_calls
def calculate(x, y, operation='add'):
    """Calculate with logging"""
    if operation == 'add':
        return x + y
    elif operation == 'multiply':
        return x * y

# Usage
result = calculate(5, 3)
# Calling calculate(5, 3, operation='add')
# calculate returned 8

result = calculate(5, 3, operation='multiply')
# Calling calculate(5, 3, operation='multiply')
# calculate returned 15
```

---

## Common Pitfalls and Solutions

### Pitfall 1: Mutable Default Arguments

```python
# ❌ WRONG
def add_item(item, items=[]):
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [1, 2] - UNEXPECTED!
list3 = add_item(3)  # [1, 2, 3] - UNEXPECTED!

# ✅ CORRECT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [2] - CORRECT
list3 = add_item(3)  # [3] - CORRECT
```

### Pitfall 2: Modifying Mutable Arguments

```python
# ❌ RISKY
def sort_list(numbers):
    numbers.sort()  # Modifies original!
    return numbers

my_list = [3, 1, 2]
sorted_list = sort_list(my_list)
print(my_list)  # [1, 2, 3] - Original modified!

# ✅ BETTER
def sort_list(numbers):
    return sorted(numbers)  # Returns new list

my_list = [3, 1, 2]
sorted_list = sort_list(my_list)
print(my_list)  # [3, 1, 2] - Original unchanged
```

### Pitfall 3: Too Many Parameters

```python
# ❌ BAD: Too many parameters
def create_user(name, email, age, city, country, phone, address, zip_code):
    pass

# ✅ BETTER: Use dictionary or class
def create_user(user_data: dict):
    required = ['name', 'email', 'age']
    if not all(k in user_data for k in required):
        raise ValueError("Missing required fields")
    
    return user_data

# Or even better: Use dataclass
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
    city: str = ""
    country: str = ""
    phone: str = ""
```

---

## Performance Considerations

### Early Returns

```python
def process_user(user):
    """Use early returns for efficiency"""
    # Validate early, exit fast
    if not user:
        return None
    
    if not user.get('active'):
        return None
    
    if user.get('age', 0) < 18:
        return None
    
    # Only process if all validations pass
    return {
        'name': user['name'],
        'processed': True
    }
```

### Lazy Evaluation with Generators

```python
def process_large_data(data):
    """Use generator for memory efficiency"""
    for item in data:
        # Process one item at a time
        yield process_item(item)

# Instead of loading everything into memory
def process_item(item):
    return item * 2

# Usage
for result in process_large_data(range(1000000)):
    # Process results one at a time
    if result > 100:
        break  # Can stop early
```

---

**End of Parameters and Returns Notes** ���

Complete mastery of function parameters and return values for flexible Python programming!
