"""
Day 3 - Lambda Functions
=========================
Learn: Anonymous functions, use cases

Key Concepts:
- Lambda functions are small anonymous functions
- Defined with 'lambda' keyword
- Can have any number of arguments but one expression
- Useful for short, throwaway functions
"""

# ========== BASIC LAMBDA ==========
print("=" * 50)
print("BASIC LAMBDA")
print("=" * 50)

# Regular function
def add_regular(a, b):
    return a + b

# Equivalent lambda
add_lambda = lambda a, b: a + b

print(f"Regular function: {add_regular(5, 3)}")
print(f"Lambda function: {add_lambda(5, 3)}")

# Syntax: lambda arguments: expression

# More examples
square = lambda x: x ** 2
double = lambda x: x * 2
is_even = lambda x: x % 2 == 0

print(f"\nsquare(5): {square(5)}")
print(f"double(5): {double(5)}")
print(f"is_even(4): {is_even(4)}")
print(f"is_even(5): {is_even(5)}")

# ========== LAMBDA WITH MULTIPLE ARGUMENTS ==========
print("\n" + "=" * 50)
print("LAMBDA WITH MULTIPLE ARGUMENTS")
print("=" * 50)

# Two arguments
multiply = lambda x, y: x * y
print(f"multiply(4, 5): {multiply(4, 5)}")

# Three arguments
calculate = lambda a, b, c: a + b * c
print(f"calculate(2, 3, 4): {calculate(2, 3, 4)}")

# With default argument
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(f"greet('Gautam'): {greet('Gautam')}")
print(f"greet('Alice', 'Hi'): {greet('Alice', 'Hi')}")

# ========== LAMBDA WITH CONDITIONALS ==========
print("\n" + "=" * 50)
print("LAMBDA WITH CONDITIONALS")
print("=" * 50)

# Ternary in lambda
max_of_two = lambda a, b: a if a > b else b
print(f"max_of_two(5, 3): {max_of_two(5, 3)}")
print(f"max_of_two(2, 8): {max_of_two(2, 8)}")

# Check positive/negative
sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
print(f"\nsign(5): {sign(5)}")
print(f"sign(-3): {sign(-3)}")
print(f"sign(0): {sign(0)}")

# Grade assignment
get_grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"\nget_grade(95): {get_grade(95)}")
print(f"get_grade(82): {get_grade(82)}")
print(f"get_grade(65): {get_grade(65)}")

# ========== LAMBDA WITH BUILT-IN FUNCTIONS ==========
print("\n" + "=" * 50)
print("LAMBDA WITH SORTING")
print("=" * 50)

# Sort with lambda key
students = [
    {"name": "Alice", "age": 25, "score": 88},
    {"name": "Bob", "age": 22, "score": 95},
    {"name": "Charlie", "age": 28, "score": 78}
]

# Sort by age
by_age = sorted(students, key=lambda s: s["age"])
print("Sorted by age:")
for s in by_age:
    print(f"  {s['name']}: {s['age']}")

# Sort by score (descending)
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print("\nSorted by score (highest first):")
for s in by_score:
    print(f"  {s['name']}: {s['score']}")

# Sort by name
by_name = sorted(students, key=lambda s: s["name"])
print("\nSorted by name:")
for s in by_name:
    print(f"  {s['name']}")

# Sort list of tuples
points = [(3, 4), (1, 2), (5, 0), (2, 3)]
by_x = sorted(points, key=lambda p: p[0])
by_y = sorted(points, key=lambda p: p[1])
by_sum = sorted(points, key=lambda p: p[0] + p[1])

print(f"\nPoints: {points}")
print(f"By x: {by_x}")
print(f"By y: {by_y}")
print(f"By sum: {by_sum}")

# ========== LAMBDA WITH MAP ==========
print("\n" + "=" * 50)
print("LAMBDA WITH MAP")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Convert to strings
strings = list(map(lambda x: str(x), numbers))
print(f"As strings: {strings}")

# ========== LAMBDA WITH FILTER ==========
print("\n" + "=" * 50)
print("LAMBDA WITH FILTER")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original: {numbers}")
print(f"Evens: {evens}")

# Filter numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")

# Filter words longer than 4 characters
words = ["apple", "cat", "banana", "dog", "elephant"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(f"\nWords: {words}")
print(f"Long words (>4): {long_words}")

# ========== LAMBDA WITH REDUCE ==========
print("\n" + "=" * 50)
print("LAMBDA WITH REDUCE")
print("=" * 50)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum using reduce
total = reduce(lambda a, b: a + b, numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Product using reduce
product = reduce(lambda a, b: a * b, numbers)
print(f"Product: {product}")

# Find maximum using reduce
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"Maximum: {maximum}")

# ========== IMMEDIATELY INVOKED LAMBDA ==========
print("\n" + "=" * 50)
print("IMMEDIATELY INVOKED LAMBDA")
print("=" * 50)

# Call lambda immediately
result = (lambda x, y: x + y)(5, 3)
print(f"Immediately invoked: {result}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Sort products by price
products = [
    {"name": "Laptop", "price": 999, "stock": 50},
    {"name": "Phone", "price": 699, "stock": 100},
    {"name": "Tablet", "price": 399, "stock": 75},
    {"name": "Watch", "price": 299, "stock": 200}
]

# Sort by price
by_price = sorted(products, key=lambda p: p["price"])
print("Products by price:")
for p in by_price:
    print(f"  {p['name']}: ${p['price']}")

# Filter in stock
in_stock = list(filter(lambda p: p["stock"] > 60, products))
print("\nProducts with stock > 60:")
for p in in_stock:
    print(f"  {p['name']}: {p['stock']} units")

# Example 2: Calculate discounts
prices = [100, 250, 50, 400, 150]
discount_rate = 0.20

# Apply 20% discount
discounted = list(map(lambda p: p * (1 - discount_rate), prices))
print(f"\nOriginal prices: {prices}")
print(f"After 20% discount: {discounted}")

# Example 3: Extract initials
names = ["John Doe", "Alice Smith", "Bob Johnson"]
initials = list(map(lambda name: "".join([n[0] for n in name.split()]), names))
print(f"\nNames: {names}")
print(f"Initials: {initials}")

# Example 4: Validate emails (simple)
emails = ["user@example.com", "invalid", "test@test.org", "bad@"]
valid_emails = list(filter(lambda e: "@" in e and "." in e.split("@")[-1], emails))
print(f"\nEmails: {emails}")
print(f"Valid: {valid_emails}")

# Example 5: Chain operations
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter evens, then square them
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"\nNumbers: {numbers}")
print(f"Even numbers squared: {result}")

print("\n" + "=" * 50)
print("✅ Lambda Functions - Complete!")
print("=" * 50)
