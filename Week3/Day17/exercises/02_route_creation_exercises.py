"""
EXERCISES: Route Creation
=========================
Complete all 5 exercises below
"""

# Exercise 1: Path Parameters
# TODO: Create endpoints with different path parameters:
# - GET "/users/{user_id}" - user_id should be an integer
# - GET "/posts/{post_slug}" - post_slug should be a string
# - GET "/files/{file_path:path}" - file_path can include slashes

print("Exercise 1: Path Parameters")
print("-" * 40)
# Your code here




# Exercise 2: Query Parameters
# TODO: Create an endpoint GET "/search" that accepts:
# - q: required string query parameter
# - skip: optional integer (default 0)
# - limit: optional integer (default 10)
# Return all parameters in the response

print("\n\nExercise 2: Query Parameters")
print("-" * 40)
# Your code here




# Exercise 3: Path Parameter Validation
# TODO: Create an endpoint GET "/products/{product_id}" where:
# - product_id must be greater than 0
# - product_id must be less than or equal to 10000
# - Use Path() for validation with a description

print("\n\nExercise 3: Path Parameter Validation")
print("-" * 40)
# Your code here




# Exercise 4: Query Parameter Validation
# TODO: Create an endpoint GET "/items" with:
# - category: optional string (min 2 chars, max 50 chars)
# - min_price: optional float (must be >= 0)
# - max_price: optional float (must be >= 0)
# - in_stock: optional boolean (default None)

print("\n\nExercise 4: Query Parameter Validation")
print("-" * 40)
# Your code here




# Exercise 5: Combined Path and Query
# TODO: Create an endpoint GET "/categories/{category_id}/products" that:
# - Takes category_id as path parameter (int, > 0)
# - Takes page as query parameter (int, default 1, >= 1)
# - Takes per_page as query parameter (int, default 20, between 1-100)
# - Takes sort_by as optional query parameter (string)

print("\n\nExercise 5: Combined Path and Query")
print("-" * 40)
# Your code here



