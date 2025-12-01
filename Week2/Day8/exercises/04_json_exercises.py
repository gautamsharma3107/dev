"""
Day 8 - Exercise 4: JSON Exercises
==================================
Practice working with JSON data
"""

print("=" * 60)
print("Exercise 4: JSON Format")
print("=" * 60)

import json

# ============================================================
# Exercise 4.1: JSON Parsing
# ============================================================

print("\n📝 Exercise 4.1: Parse JSON Data")
print("-" * 50)
print("""
Given the following JSON string representing an API response,
parse it and extract specific information.
""")

api_response = '''
{
    "status": "success",
    "data": {
        "user": {
            "id": 12345,
            "username": "john_doe",
            "email": "john@example.com",
            "profile": {
                "full_name": "John Doe",
                "bio": "Software Developer",
                "location": "New York"
            },
            "settings": {
                "notifications": true,
                "theme": "dark"
            }
        },
        "posts": [
            {"id": 1, "title": "First Post", "likes": 42},
            {"id": 2, "title": "Second Post", "likes": 15},
            {"id": 3, "title": "Third Post", "likes": 88}
        ]
    },
    "meta": {
        "request_id": "abc-123",
        "timestamp": "2024-01-15T10:30:00Z"
    }
}
'''

# TODO: Parse the JSON and extract:
# 1. The user's full name
# 2. The user's email
# 3. The theme setting
# 4. Total number of posts
# 5. The title of the most liked post
# 6. Total likes across all posts

# Your code here:




# ============================================================
# Exercise 4.2: Create JSON Structure
# ============================================================

print("\n📝 Exercise 4.2: Create JSON Structure")
print("-" * 50)
print("""
Create a Python dictionary that represents an e-commerce order,
then convert it to a formatted JSON string.

Required fields:
- order_id: "ORD-2024-001"
- customer: name, email, shipping_address (street, city, country, zip)
- items: list of 3 products (each with id, name, quantity, price)
- totals: subtotal, tax, shipping, total
- status: "pending"
- created_at: "2024-01-15T10:30:00Z"
""")

# TODO: Create the order dictionary and convert to JSON
order = {
    # Your code here
}

# Convert to formatted JSON string:
# json_order = json.dumps(order, indent=4)
# print(json_order)

# ============================================================
# Exercise 4.3: JSON Transformation
# ============================================================

print("\n📝 Exercise 4.3: Transform JSON Data")
print("-" * 50)
print("""
Given a list of users in one format, transform it to another format.

Input format:
[
    {"firstName": "John", "lastName": "Doe", "emailAddress": "john@test.com", "isActive": true},
    {"firstName": "Jane", "lastName": "Smith", "emailAddress": "jane@test.com", "isActive": false}
]

Output format:
[
    {"name": "John Doe", "email": "john@test.com", "status": "active"},
    {"name": "Jane Smith", "email": "jane@test.com", "status": "inactive"}
]
""")

input_users = [
    {"firstName": "John", "lastName": "Doe", "emailAddress": "john@test.com", "isActive": True},
    {"firstName": "Jane", "lastName": "Smith", "emailAddress": "jane@test.com", "isActive": False},
    {"firstName": "Bob", "lastName": "Wilson", "emailAddress": "bob@test.com", "isActive": True}
]

def transform_users(users):
    """Transform user data to new format"""
    # TODO: Implement transformation
    pass

# Test:
# transformed = transform_users(input_users)
# print(json.dumps(transformed, indent=2))

# ============================================================
# Exercise 4.4: JSON Validation
# ============================================================

print("\n📝 Exercise 4.4: Validate JSON Data")
print("-" * 50)
print("""
Create a function that validates if a user object has all required fields
and the correct data types.

Required fields:
- name (string, required)
- email (string, required, must contain @)
- age (number, optional, must be positive if present)
- is_active (boolean, required)
- roles (array of strings, optional)
""")

def validate_user(user_data):
    """
    Validate user data structure.
    
    Returns:
        tuple: (is_valid: bool, errors: list of error messages)
    """
    errors = []
    
    # TODO: Implement validation
    # Check for required fields
    # Check data types
    # Check email format
    # Check age is positive if present
    
    return (len(errors) == 0, errors)

# Test cases:
test_users = [
    {"name": "John", "email": "john@test.com", "is_active": True},  # Valid
    {"name": "Jane", "email": "invalid-email", "is_active": True},  # Invalid email
    {"email": "bob@test.com", "is_active": True},  # Missing name
    {"name": "Alice", "email": "alice@test.com", "age": -5, "is_active": True},  # Negative age
    {"name": "Eve", "email": "eve@test.com", "is_active": "yes"},  # Wrong type for is_active
]

# for user in test_users:
#     is_valid, errors = validate_user(user)
#     print(f"Valid: {is_valid}, Errors: {errors}")

# ============================================================
# Exercise 4.5: JSON File Operations
# ============================================================

print("\n📝 Exercise 4.5: JSON File Operations")
print("-" * 50)
print("""
Create functions to work with JSON files:
1. save_data(filename, data) - Save data to JSON file
2. load_data(filename) - Load data from JSON file
3. update_field(filename, key, value) - Update a specific field
4. merge_files(file1, file2, output_file) - Merge two JSON files
""")

def save_data(filename, data):
    """Save data to JSON file"""
    # TODO: Implement
    pass

def load_data(filename):
    """Load data from JSON file, return None if file doesn't exist"""
    # TODO: Implement
    pass

def update_field(filename, key, value):
    """Update a specific field in JSON file"""
    # TODO: Implement
    pass

def merge_files(file1, file2, output_file):
    """Merge two JSON files into one"""
    # TODO: Implement
    pass

# ============================================================
# Exercise 4.6: Working with API Response
# ============================================================

print("\n📝 Exercise 4.6: Process Paginated API Response")
print("-" * 50)
print("""
Given paginated API responses, create a function that processes them
and returns a combined result.

Each page response looks like:
{
    "data": [...items...],
    "pagination": {
        "page": 1,
        "per_page": 10,
        "total": 25,
        "total_pages": 3
    }
}
""")

page1 = {
    "data": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}],
    "pagination": {"page": 1, "per_page": 2, "total": 5, "total_pages": 3}
}

page2 = {
    "data": [{"id": 3, "name": "Item 3"}, {"id": 4, "name": "Item 4"}],
    "pagination": {"page": 2, "per_page": 2, "total": 5, "total_pages": 3}
}

page3 = {
    "data": [{"id": 5, "name": "Item 5"}],
    "pagination": {"page": 3, "per_page": 2, "total": 5, "total_pages": 3}
}

def combine_paginated_responses(responses):
    """
    Combine multiple paginated responses into a single result.
    
    Returns:
        dict with 'data' (all items) and 'total' (item count)
    """
    # TODO: Implement
    pass

# Test:
# result = combine_paginated_responses([page1, page2, page3])
# print(json.dumps(result, indent=2))

print("\n" + "=" * 60)
print("✅ Complete the exercises above!")
print("=" * 60)

"""
SOLUTIONS:

Exercise 4.1:
data = json.loads(api_response)
print(f"1. Full name: {data['data']['user']['profile']['full_name']}")
print(f"2. Email: {data['data']['user']['email']}")
print(f"3. Theme: {data['data']['user']['settings']['theme']}")
print(f"4. Posts count: {len(data['data']['posts'])}")
most_liked = max(data['data']['posts'], key=lambda x: x['likes'])
print(f"5. Most liked: {most_liked['title']}")
total_likes = sum(post['likes'] for post in data['data']['posts'])
print(f"6. Total likes: {total_likes}")

Exercise 4.2:
order = {
    "order_id": "ORD-2024-001",
    "customer": {
        "name": "John Doe",
        "email": "john@example.com",
        "shipping_address": {
            "street": "123 Main St",
            "city": "New York",
            "country": "USA",
            "zip": "10001"
        }
    },
    "items": [
        {"id": "PROD-001", "name": "Widget", "quantity": 2, "price": 29.99},
        {"id": "PROD-002", "name": "Gadget", "quantity": 1, "price": 49.99},
        {"id": "PROD-003", "name": "Gizmo", "quantity": 3, "price": 9.99}
    ],
    "totals": {
        "subtotal": 139.94,
        "tax": 12.59,
        "shipping": 5.99,
        "total": 158.52
    },
    "status": "pending",
    "created_at": "2024-01-15T10:30:00Z"
}

Exercise 4.3:
def transform_users(users):
    return [
        {
            "name": f"{u['firstName']} {u['lastName']}",
            "email": u["emailAddress"],
            "status": "active" if u["isActive"] else "inactive"
        }
        for u in users
    ]

Exercise 4.4:
def validate_user(user_data):
    errors = []
    
    # Check required fields
    if "name" not in user_data:
        errors.append("Missing required field: name")
    elif not isinstance(user_data["name"], str):
        errors.append("name must be a string")
    
    if "email" not in user_data:
        errors.append("Missing required field: email")
    elif not isinstance(user_data["email"], str):
        errors.append("email must be a string")
    elif "@" not in user_data["email"]:
        errors.append("email must contain @")
    
    if "is_active" not in user_data:
        errors.append("Missing required field: is_active")
    elif not isinstance(user_data["is_active"], bool):
        errors.append("is_active must be a boolean")
    
    if "age" in user_data:
        if not isinstance(user_data["age"], (int, float)):
            errors.append("age must be a number")
        elif user_data["age"] < 0:
            errors.append("age must be positive")
    
    return (len(errors) == 0, errors)

Exercise 4.5:
def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def update_field(filename, key, value):
    data = load_data(filename) or {}
    data[key] = value
    save_data(filename, data)

def merge_files(file1, file2, output_file):
    data1 = load_data(file1) or {}
    data2 = load_data(file2) or {}
    merged = {**data1, **data2}
    save_data(output_file, merged)

Exercise 4.6:
def combine_paginated_responses(responses):
    all_items = []
    for response in responses:
        all_items.extend(response['data'])
    return {
        'data': all_items,
        'total': len(all_items)
    }
"""
