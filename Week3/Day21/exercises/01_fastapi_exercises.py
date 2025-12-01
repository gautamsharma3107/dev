"""
EXERCISES: FastAPI Basics
=========================
Complete all 5 exercises below
"""

# Exercise 1: Create a basic FastAPI application
# TODO: Create a FastAPI app with a root endpoint that returns {"message": "Hello World"}

print("Exercise 1: Basic FastAPI App")
print("-" * 40)
# Your code here:




# Exercise 2: Path parameters
# TODO: Create an endpoint GET /users/{user_id} that returns the user_id in the response

print("\n\nExercise 2: Path Parameters")
print("-" * 40)
# Your code here:




# Exercise 3: Query parameters
# TODO: Create an endpoint GET /items/ that accepts optional query parameters:
# - skip: int (default 0)
# - limit: int (default 10)
# Return the skip and limit values in the response

print("\n\nExercise 3: Query Parameters")
print("-" * 40)
# Your code here:




# Exercise 4: Request body with Pydantic
# TODO: Create a Pydantic model for a Product (name: str, price: float, in_stock: bool)
# Create a POST /products/ endpoint that accepts this model and returns it

print("\n\nExercise 4: Request Body with Pydantic")
print("-" * 40)
# Your code here:




# Exercise 5: HTTP Status codes and exceptions
# TODO: Create a GET /items/{item_id} endpoint that:
# - Returns the item if found
# - Returns 404 if item_id doesn't exist
# Use HTTPException from FastAPI

print("\n\nExercise 5: HTTP Status Codes")
print("-" * 40)
# Your code here:
