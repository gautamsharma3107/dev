"""
EXERCISES: API Concepts
=======================
Complete all 5 exercises below
"""

# Exercise 1: HTTP Methods
# TODO: Match each HTTP method with its purpose
# Fill in the blanks with: CREATE, READ, UPDATE (full), UPDATE (partial), DELETE

print("Exercise 1: HTTP Methods")
print("-" * 40)

http_methods = {
    "GET": "______",      # What operation?
    "POST": "______",     # What operation?
    "PUT": "______",      # What operation?
    "PATCH": "______",    # What operation?
    "DELETE": "______",   # What operation?
}

# Print your answers
for method, operation in http_methods.items():
    print(f"{method}: {operation}")


# Exercise 2: Status Codes
# TODO: What status code would you return for each scenario?
# Choose from: 200, 201, 204, 400, 401, 403, 404, 500

print("\n\nExercise 2: Status Codes")
print("-" * 40)

scenarios = {
    "Successfully retrieved a list of books": "___",
    "Successfully created a new book": "___",
    "Successfully deleted a book (no content returned)": "___",
    "Client sent invalid data": "___",
    "User is not logged in": "___",
    "User is logged in but doesn't have permission": "___",
    "The requested book doesn't exist": "___",
    "Server crashed while processing request": "___",
}

# Print your answers
for scenario, code in scenarios.items():
    print(f"{scenario}: {code}")


# Exercise 3: JSON Data Types
# TODO: Identify the JSON data type for each value

print("\n\nExercise 3: JSON Data Types")
print("-" * 40)

# What JSON type is each of these?
values = {
    '"Hello World"': "______",      # Type?
    '42': "______",                 # Type?
    '3.14': "______",               # Type?
    'true': "______",               # Type?
    'null': "______",               # Type?
    '[1, 2, 3]': "______",          # Type?
    '{"name": "John"}': "______",   # Type?
}

for value, json_type in values.items():
    print(f"{value}: {json_type}")


# Exercise 4: RESTful URL Design
# TODO: Design RESTful URLs for a "products" resource

print("\n\nExercise 4: RESTful URL Design")
print("-" * 40)

# Fill in the URL patterns for a products API
print("""
Design URLs for these operations:

1. Get all products: _______________
2. Create a new product: _______________
3. Get product with ID 5: _______________
4. Update product with ID 5: _______________
5. Delete product with ID 5: _______________
6. Get all products in category "electronics": _______________
7. Search products by name: _______________
""")


# Exercise 5: API Response Design
# TODO: Design a JSON response for a book API

print("\n\nExercise 5: API Response Design")
print("-" * 40)

# Design a JSON response for getting a single book
# Include: id, title, author (nested with name and email), price, 
# is_available, published_date, and a list of tags

print("""
Design a JSON response for GET /api/books/1/

Your response should include:
- id (integer)
- title (string)
- author (nested object with name and email)
- price (decimal)
- is_available (boolean)
- published_date (date string)
- tags (array of strings)

Write your JSON response here:

{
    
    
    
    
    
    
    
}
""")
