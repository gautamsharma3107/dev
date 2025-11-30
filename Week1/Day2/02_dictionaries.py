"""
Day 2 - Dictionaries
====================
Learn: Dictionary creation, operations, methods

Key Concepts:
- Dictionaries store key-value pairs
- Keys must be unique and immutable
- Values can be any type
- Very fast lookups by key
"""

# ========== DICTIONARY CREATION ==========
print("=" * 50)
print("DICTIONARY CREATION")
print("=" * 50)

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Dictionary with values
person = {
    "name": "Gautam",
    "age": 25,
    "city": "Delhi"
}
print(f"Person: {person}")

# Using dict() constructor
student = dict(name="Alice", grade="A", score=95)
print(f"Student: {student}")

# From list of tuples
items = [("apple", 1.50), ("banana", 0.75), ("orange", 2.00)]
prices = dict(items)
print(f"Prices: {prices}")

# ========== ACCESSING VALUES ==========
print("\n" + "=" * 50)
print("ACCESSING VALUES")
print("=" * 50)

user = {
    "username": "gautam123",
    "email": "gautam@example.com",
    "age": 25
}
print(f"User: {user}")

# Using square brackets
print(f"\nUsername: {user['username']}")
print(f"Email: {user['email']}")

# Using get() - safer, returns None if key missing
print(f"Age: {user.get('age')}")
print(f"Phone (missing): {user.get('phone')}")
print(f"Phone (with default): {user.get('phone', 'Not provided')}")

# ========== MODIFYING DICTIONARIES ==========
print("\n" + "=" * 50)
print("MODIFYING DICTIONARIES")
print("=" * 50)

profile = {"name": "John", "age": 30}
print(f"Original: {profile}")

# Add/Update using square brackets
profile["city"] = "New York"  # Add new key
print(f"After adding city: {profile}")

profile["age"] = 31  # Update existing
print(f"After updating age: {profile}")

# Update multiple values
profile.update({"country": "USA", "age": 32})
print(f"After update(): {profile}")

# Remove items
removed = profile.pop("city")
print(f"\nRemoved city: {removed}")
print(f"After pop: {profile}")

# Remove and return last item (Python 3.7+)
last = profile.popitem()
print(f"Popped last: {last}")
print(f"After popitem: {profile}")

# Delete using del
del profile["age"]
print(f"After del age: {profile}")

# Clear all
copy_profile = {"a": 1, "b": 2}
copy_profile.clear()
print(f"After clear: {copy_profile}")

# ========== DICTIONARY METHODS ==========
print("\n" + "=" * 50)
print("DICTIONARY METHODS")
print("=" * 50)

student = {
    "name": "Alice",
    "subjects": ["Math", "Science"],
    "grade": "A",
    "score": 95
}
print(f"Student: {student}")

# Get all keys
print(f"\nKeys: {list(student.keys())}")

# Get all values
print(f"Values: {list(student.values())}")

# Get all key-value pairs
print(f"Items: {list(student.items())}")

# Check if key exists
print(f"\n'name' in student: {'name' in student}")
print(f"'age' in student: {'age' in student}")

# setdefault - get value or set default if missing
phone = student.setdefault("phone", "N/A")
print(f"\nsetdefault phone: {phone}")
print(f"Student after setdefault: {student}")

# ========== ITERATING DICTIONARIES ==========
print("\n" + "=" * 50)
print("ITERATING DICTIONARIES")
print("=" * 50)

scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(f"Scores: {scores}")

# Iterate keys
print("\nIterating keys:")
for name in scores:
    print(f"  {name}")

# Iterate values
print("\nIterating values:")
for score in scores.values():
    print(f"  {score}")

# Iterate key-value pairs
print("\nIterating items:")
for name, score in scores.items():
    print(f"  {name}: {score}")

# ========== NESTED DICTIONARIES ==========
print("\n" + "=" * 50)
print("NESTED DICTIONARIES")
print("=" * 50)

school = {
    "class_10": {
        "Alice": {"math": 95, "science": 88},
        "Bob": {"math": 78, "science": 92}
    },
    "class_11": {
        "Charlie": {"math": 88, "science": 85},
        "David": {"math": 91, "science": 94}
    }
}

# Access nested values
print(f"Alice's math score: {school['class_10']['Alice']['math']}")

# Iterate nested dictionary
print("\nAll students and scores:")
for class_name, students in school.items():
    print(f"\n  {class_name}:")
    for student, scores in students.items():
        print(f"    {student}: Math={scores['math']}, Science={scores['science']}")

# ========== DICTIONARY COMPREHENSION ==========
print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION")
print("=" * 50)

# Create dictionary from range
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Filter dictionary
scores = {"Alice": 95, "Bob": 65, "Charlie": 88, "David": 55}
passed = {name: score for name, score in scores.items() if score >= 70}
print(f"\nAll scores: {scores}")
print(f"Passed students: {passed}")

# Transform values
doubled = {name: score * 2 for name, score in scores.items()}
print(f"Doubled scores: {doubled}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Word counter
text = "hello world hello python world python python"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word count:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

# Example 2: Phonebook
print("\n--- Phonebook ---")
phonebook = {}

def add_contact(name, phone):
    phonebook[name] = phone
    print(f"Added: {name} -> {phone}")

def lookup(name):
    return phonebook.get(name, "Contact not found")

add_contact("Alice", "123-456-7890")
add_contact("Bob", "098-765-4321")
print(f"Alice's number: {lookup('Alice')}")
print(f"Charlie's number: {lookup('Charlie')}")

# Example 3: Inventory system
print("\n--- Inventory ---")
inventory = {
    "apple": {"price": 1.50, "stock": 100},
    "banana": {"price": 0.75, "stock": 150},
    "orange": {"price": 2.00, "stock": 75}
}

def check_stock(item):
    if item in inventory:
        return inventory[item]["stock"]
    return 0

def update_stock(item, quantity):
    if item in inventory:
        inventory[item]["stock"] += quantity
        print(f"Updated {item}: new stock = {inventory[item]['stock']}")

print(f"Apple stock: {check_stock('apple')}")
update_stock("apple", -20)  # Sold 20 apples

# Example 4: Group by category
print("\n--- Group by Category ---")
products = [
    {"name": "iPhone", "category": "Electronics"},
    {"name": "T-Shirt", "category": "Clothing"},
    {"name": "MacBook", "category": "Electronics"},
    {"name": "Jeans", "category": "Clothing"},
    {"name": "Headphones", "category": "Electronics"}
]

grouped = {}
for product in products:
    category = product["category"]
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(product["name"])

for category, items in grouped.items():
    print(f"  {category}: {items}")

print("\n" + "=" * 50)
print("✅ Dictionaries - Complete!")
print("=" * 50)
