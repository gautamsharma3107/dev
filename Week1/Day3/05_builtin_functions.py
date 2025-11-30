"""
Day 3 - Built-in Functions (map, filter, zip, etc.)
====================================================
Learn: Common functional programming tools

Key Concepts:
- map() - apply function to each item
- filter() - filter items by condition
- zip() - combine iterables
- reduce() - reduce to single value
- enumerate() - add index to iteration
- sorted() - sort iterables
"""

# ========== MAP FUNCTION ==========
print("=" * 50)
print("MAP FUNCTION")
print("=" * 50)

# map(function, iterable) - apply function to each item

# Example 1: Square numbers
numbers = [1, 2, 3, 4, 5]

# Using map with regular function
def square(x):
    return x ** 2

squared = list(map(square, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Using map with lambda
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Example 2: Convert strings to integers
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(f"\nStrings: {str_numbers}")
print(f"Integers: {int_numbers}")

# Example 3: Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"\nList1: {list1}")
print(f"List2: {list2}")
print(f"Sums: {sums}")

# Example 4: Uppercase strings
names = ["alice", "bob", "charlie"]
upper_names = list(map(str.upper, names))
print(f"\nNames: {names}")
print(f"Uppercase: {upper_names}")

# ========== FILTER FUNCTION ==========
print("\n" + "=" * 50)
print("FILTER FUNCTION")
print("=" * 50)

# filter(function, iterable) - keep items where function returns True

# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))
print(f"Original: {numbers}")
print(f"Evens: {evens}")

# Using lambda
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odds: {odds}")

# Example 2: Filter by length
words = ["apple", "cat", "banana", "dog", "elephant", "ant"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(f"\nWords: {words}")
print(f"Words longer than 3: {long_words}")

# Example 3: Filter None values
mixed = [1, None, 2, None, 3, None, 4]
non_none = list(filter(None, mixed))  # None as function removes falsy
print(f"\nMixed: {mixed}")
print(f"Non-None: {non_none}")

# Example 4: Filter dictionaries
products = [
    {"name": "Laptop", "price": 999, "in_stock": True},
    {"name": "Phone", "price": 699, "in_stock": False},
    {"name": "Tablet", "price": 399, "in_stock": True},
    {"name": "Watch", "price": 299, "in_stock": False}
]

in_stock = list(filter(lambda p: p["in_stock"], products))
print("\nProducts in stock:")
for p in in_stock:
    print(f"  {p['name']}: ${p['price']}")

# ========== ZIP FUNCTION ==========
print("\n" + "=" * 50)
print("ZIP FUNCTION")
print("=" * 50)

# zip(iter1, iter2, ...) - combine iterables element-wise

# Example 1: Basic zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

combined = list(zip(names, ages))
print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Zipped: {combined}")

# Example 2: Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Gautam", 25, "Delhi"]

person = dict(zip(keys, values))
print(f"\nDictionary from zip: {person}")

# Example 3: Zip three lists
names = ["Alice", "Bob"]
ages = [25, 30]
cities = ["NYC", "LA"]

combined = list(zip(names, ages, cities))
print(f"\nThree lists zipped: {combined}")

# Example 4: Unzip
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)  # * unpacks the list
print(f"\nPairs: {pairs}")
print(f"Letters: {letters}")
print(f"Numbers: {numbers}")

# Example 5: Zip with different lengths (stops at shortest)
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c"]

result = list(zip(list1, list2))
print(f"\nList1: {list1}")
print(f"List2: {list2}")
print(f"Zipped (stops at shortest): {result}")

# ========== ENUMERATE FUNCTION ==========
print("\n" + "=" * 50)
print("ENUMERATE FUNCTION")
print("=" * 50)

# enumerate(iterable, start=0) - add counter to iteration

# Example 1: Basic enumerate
fruits = ["apple", "banana", "cherry"]

print("Without enumerate:")
for fruit in fruits:
    print(f"  {fruit}")

print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\nWith enumerate (start=1):")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# Example 2: Find index of item
def find_index(lst, target):
    for index, item in enumerate(lst):
        if item == target:
            return index
    return -1

numbers = [10, 20, 30, 40, 50]
print(f"\nIndex of 30: {find_index(numbers, 30)}")
print(f"Index of 100: {find_index(numbers, 100)}")

# Example 3: Create numbered dict
items = ["apple", "banana", "cherry"]
numbered = {i: item for i, item in enumerate(items, start=1)}
print(f"\nNumbered dict: {numbered}")

# ========== SORTED FUNCTION ==========
print("\n" + "=" * 50)
print("SORTED FUNCTION")
print("=" * 50)

# sorted(iterable, key=None, reverse=False)

# Example 1: Basic sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
print(f"Sorted: {sorted(numbers)}")
print(f"Reverse sorted: {sorted(numbers, reverse=True)}")

# Example 2: Sort strings
names = ["charlie", "Alice", "bob", "David"]
print(f"\nNames: {names}")
print(f"Sorted: {sorted(names)}")
print(f"Sorted (case insensitive): {sorted(names, key=str.lower)}")

# Example 3: Sort by custom key
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 78}
]

by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print("\nStudents by score (highest first):")
for s in by_score:
    print(f"  {s['name']}: {s['score']}")

# ========== REDUCE FUNCTION ==========
print("\n" + "=" * 50)
print("REDUCE FUNCTION")
print("=" * 50)

from functools import reduce

# reduce(function, iterable, initial) - reduce to single value

# Example 1: Sum
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(f"Numbers: {numbers}")
print(f"Sum using reduce: {total}")

# Example 2: Product
product = reduce(lambda a, b: a * b, numbers)
print(f"Product: {product}")

# Example 3: Maximum
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"Maximum: {maximum}")

# Example 4: Flatten list
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
print(f"\nNested: {nested}")
print(f"Flattened: {flat}")

# ========== ANY AND ALL ==========
print("\n" + "=" * 50)
print("ANY AND ALL")
print("=" * 50)

# any(iterable) - True if any element is True
# all(iterable) - True if all elements are True

numbers = [1, 2, 3, 4, 5]

# Any even?
any_even = any(n % 2 == 0 for n in numbers)
print(f"Numbers: {numbers}")
print(f"Any even? {any_even}")

# All positive?
all_positive = all(n > 0 for n in numbers)
print(f"All positive? {all_positive}")

# Mixed list
mixed = [True, True, False, True]
print(f"\nMixed: {mixed}")
print(f"any(mixed): {any(mixed)}")
print(f"all(mixed): {all(mixed)}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Process sales data
sales = [
    {"product": "Laptop", "quantity": 5, "price": 999},
    {"product": "Phone", "quantity": 10, "price": 699},
    {"product": "Tablet", "quantity": 8, "price": 399},
    {"product": "Watch", "quantity": 15, "price": 299}
]

# Calculate total revenue per product
revenues = list(map(lambda s: {
    "product": s["product"],
    "revenue": s["quantity"] * s["price"]
}, sales))

print("Sales revenue:")
for r in revenues:
    print(f"  {r['product']}: ${r['revenue']:,}")

# Total revenue
total_revenue = reduce(lambda a, b: a + b["quantity"] * b["price"], sales, 0)
print(f"\nTotal revenue: ${total_revenue:,}")

# Example 2: Data pipeline
data = ["  Alice  ", "BOB", "  charlie  ", "DAVID  "]

# Clean, normalize, and filter
processed = list(filter(
    lambda x: len(x) > 3,
    map(lambda x: x.strip().title(), data)
))

print(f"\nOriginal: {data}")
print(f"Processed: {processed}")

# Example 3: Parallel processing with zip
temperatures_c = [0, 20, 37, 100]
temperatures_f = list(map(lambda c: (c * 9/5) + 32, temperatures_c))

print("\nTemperature conversion:")
for c, f in zip(temperatures_c, temperatures_f):
    print(f"  {c}°C = {f}°F")

# Example 4: Grade report
students = ["Alice", "Bob", "Charlie"]
math_scores = [85, 92, 78]
science_scores = [88, 95, 82]

# Calculate averages
averages = list(map(lambda m, s: (m + s) / 2, math_scores, science_scores))

# Create report
print("\nGrade Report:")
for name, math, science, avg in zip(students, math_scores, science_scores, averages):
    print(f"  {name}: Math={math}, Science={science}, Average={avg:.1f}")

print("\n" + "=" * 50)
print("✅ Built-in Functions - Complete!")
print("=" * 50)
