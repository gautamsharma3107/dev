"""
Day 3 - Parameters and Return Values
=====================================
Learn: Different parameter types, return patterns

Key Concepts:
- Positional vs keyword arguments
- Default parameter values
- *args for variable positional arguments
- **kwargs for variable keyword arguments
- Multiple return values
"""

# ========== POSITIONAL ARGUMENTS ==========
print("=" * 50)
print("POSITIONAL ARGUMENTS")
print("=" * 50)

def divide(dividend, divisor):
    """Order matters for positional arguments."""
    return dividend / divisor

# Order matters!
print(f"divide(10, 2) = {divide(10, 2)}")  # 10 / 2 = 5
print(f"divide(2, 10) = {divide(2, 10)}")  # 2 / 10 = 0.2

# ========== KEYWORD ARGUMENTS ==========
print("\n" + "=" * 50)
print("KEYWORD ARGUMENTS")
print("=" * 50)

def create_email(to, subject, body, cc=None, bcc=None):
    """Create an email with various fields."""
    email = {
        "to": to,
        "subject": subject,
        "body": body
    }
    if cc:
        email["cc"] = cc
    if bcc:
        email["bcc"] = bcc
    return email

# Using keyword arguments for clarity
email1 = create_email(
    to="alice@example.com",
    subject="Meeting",
    body="Let's meet tomorrow."
)

email2 = create_email(
    body="Important update",
    to="bob@example.com",
    subject="Update",
    cc="manager@example.com"
)

print(f"Email 1: {email1}")
print(f"Email 2: {email2}")

# ========== *args (Variable Positional Arguments) ==========
print("\n" + "=" * 50)
print("*args (Variable Positional Arguments)")
print("=" * 50)

def sum_all(*numbers):
    """Sum any number of arguments."""
    print(f"Received: {numbers}, Type: {type(numbers)}")
    return sum(numbers)

print(f"sum_all(1, 2): {sum_all(1, 2)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10): {sum_all(10)}")

# *args with regular parameters
def greet_all(greeting, *names):
    """Greet multiple people with the same greeting."""
    for name in names:
        print(f"{greeting}, {name}!")

print("\nGreeting multiple people:")
greet_all("Hello", "Alice", "Bob", "Charlie")

# Practical example: calculate average
def average(*numbers):
    """Calculate average of any number of values."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(f"\nAverage of 10, 20, 30: {average(10, 20, 30)}")
print(f"Average of 5, 10, 15, 20, 25: {average(5, 10, 15, 20, 25)}")

# ========== **kwargs (Variable Keyword Arguments) ==========
print("\n" + "=" * 50)
print("**kwargs (Variable Keyword Arguments)")
print("=" * 50)

def print_info(**kwargs):
    """Print any keyword arguments passed."""
    print(f"Received: {kwargs}, Type: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Calling print_info:")
print_info(name="Gautam", age=25, city="Delhi")

print("\nAnother call:")
print_info(language="Python", level="Advanced", years=5)

# Practical example: create user profile
def create_user(username, password, **details):
    """Create user with required and optional fields."""
    user = {
        "username": username,
        "password": "***" + password[-2:],  # Masked
        **details
    }
    return user

user1 = create_user("gautam", "secret123", email="g@example.com", age=25)
user2 = create_user("alice", "pass456", email="a@example.com", city="NYC", active=True)

print(f"\nUser 1: {user1}")
print(f"User 2: {user2}")

# ========== COMBINING *args and **kwargs ==========
print("\n" + "=" * 50)
print("COMBINING *args AND **kwargs")
print("=" * 50)

def super_function(required, *args, default="value", **kwargs):
    """Function with all parameter types."""
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

print("Calling super_function:")
super_function("must_have", 1, 2, 3, default="custom", x=10, y=20)

# ========== UNPACKING ARGUMENTS ==========
print("\n" + "=" * 50)
print("UNPACKING ARGUMENTS")
print("=" * 50)

def add_three(a, b, c):
    return a + b + c

# Unpack list/tuple with *
numbers = [1, 2, 3]
print(f"add_three(*[1, 2, 3]) = {add_three(*numbers)}")

# Unpack dict with **
params = {"a": 10, "b": 20, "c": 30}
print(f"add_three(**dict) = {add_three(**params)}")

# ========== MULTIPLE RETURN VALUES ==========
print("\n" + "=" * 50)
print("MULTIPLE RETURN VALUES")
print("=" * 50)

def analyze_numbers(numbers):
    """Return multiple statistics about a list."""
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

nums = [5, 2, 8, 1, 9, 3, 7]
stats = analyze_numbers(nums)
print(f"Numbers: {nums}")
print(f"Statistics: {stats}")

# Return as tuple and unpack
def divide_with_remainder(dividend, divisor):
    """Return quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder  # Returns tuple

q, r = divide_with_remainder(17, 5)
print(f"\n17 ÷ 5 = {q} remainder {r}")

# ========== NONE AS RETURN ==========
print("\n" + "=" * 50)
print("NONE AS RETURN")
print("=" * 50)

def process_data(data):
    """Process data and return result or None."""
    if not data:
        return None  # Early return for empty data
    return [x * 2 for x in data]

result1 = process_data([1, 2, 3])
result2 = process_data([])

print(f"process_data([1, 2, 3]): {result1}")
print(f"process_data([]): {result2}")

# Check for None before using
if result2 is None:
    print("No data to process!")

# ========== EARLY RETURNS ==========
print("\n" + "=" * 50)
print("EARLY RETURNS (Guard Clauses)")
print("=" * 50)

# Without early return (nested)
def get_grade_nested(score):
    if score >= 0 and score <= 100:
        if score >= 90:
            return "A"
        else:
            if score >= 80:
                return "B"
            else:
                if score >= 70:
                    return "C"
                else:
                    return "F"
    else:
        return "Invalid"

# With early returns (cleaner)
def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"

print(f"Grade for 85: {get_grade(85)}")
print(f"Grade for 65: {get_grade(65)}")
print(f"Grade for -5: {get_grade(-5)}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Flexible logger
def log(message, *tags, level="INFO", **metadata):
    """Flexible logging function."""
    tag_str = ", ".join(tags) if tags else "general"
    print(f"[{level}] [{tag_str}] {message}")
    if metadata:
        print(f"  Metadata: {metadata}")

log("Server started", "system", "startup")
log("User login", "auth", "user", level="DEBUG", user_id=123)
log("Error occurred", level="ERROR", error_code=500, path="/api")

# Example 2: Build query parameters
def build_url(base_url, **params):
    """Build URL with query parameters."""
    if not params:
        return base_url
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base_url}?{query}"

url1 = build_url("https://api.example.com/search", q="python", limit=10)
url2 = build_url("https://api.example.com/users", id=123, format="json")

print(f"\nURL 1: {url1}")
print(f"URL 2: {url2}")

# Example 3: Merge configs
def merge_configs(default, *overrides, **kwargs):
    """Merge multiple configuration dictionaries."""
    result = default.copy()
    for override in overrides:
        result.update(override)
    result.update(kwargs)
    return result

default_config = {"debug": False, "port": 8080, "host": "localhost"}
dev_config = {"debug": True, "port": 3000}
final = merge_configs(default_config, dev_config, host="0.0.0.0")

print(f"\nDefault config: {default_config}")
print(f"Dev config: {dev_config}")
print(f"Final config: {final}")

print("\n" + "=" * 50)
print("✅ Parameters and Returns - Complete!")
print("=" * 50)
