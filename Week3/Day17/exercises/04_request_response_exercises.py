"""
EXERCISES: Request/Response Handling
====================================
Complete all 5 exercises below
"""

# Exercise 1: Request Body with Model
# TODO: Create a POST endpoint "/orders/" that:
# - Accepts an Order model (product_id: int, quantity: int, notes: optional str)
# - Returns the order with a generated order_id and total_price (quantity * 10)

print("Exercise 1: Request Body with Model")
print("-" * 40)
# Your code here




# Exercise 2: Response Model
# TODO: Create:
# - UserInput model: name, email, password
# - UserOutput model: id, name, email (no password!)
# - POST endpoint "/users/" that uses response_model=UserOutput

print("\n\nExercise 2: Response Model")
print("-" * 40)
# Your code here




# Exercise 3: Error Handling
# TODO: Create a GET endpoint "/items/{item_id}" that:
# - Checks if item_id exists in a fake database (dict with ids 1, 2, 3)
# - Returns 404 with detail "Item not found" if not exists
# - Returns the item if it exists

print("\n\nExercise 3: Error Handling")
print("-" * 40)
# Your code here




# Exercise 4: Status Codes
# TODO: Create these endpoints with appropriate status codes:
# - POST "/tasks/" - 201 Created
# - GET "/tasks/{task_id}" - 200 OK (or 404)
# - PUT "/tasks/{task_id}" - 200 OK (or 404)
# - DELETE "/tasks/{task_id}" - 204 No Content (or 404)

print("\n\nExercise 4: Status Codes")
print("-" * 40)
# Your code here




# Exercise 5: Headers and Cookies
# TODO: Create:
# - GET "/headers/" that reads and returns "X-Custom-Header"
# - POST "/login/" that sets a cookie "session_token" with value "abc123"
# - POST "/logout/" that deletes the "session_token" cookie

print("\n\nExercise 5: Headers and Cookies")
print("-" * 40)
# Your code here



