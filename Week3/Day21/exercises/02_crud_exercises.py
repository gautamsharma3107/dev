"""
EXERCISES: CRUD Operations
==========================
Complete all 5 exercises below
"""

# Exercise 1: Create Schema with Validation
# TODO: Create Pydantic schemas for a Book resource:
# - BookCreate: title (min 1 char), author (min 1 char), isbn (exactly 13 chars), price (> 0)
# - BookResponse: includes id and all BookCreate fields

print("Exercise 1: Create Schema with Validation")
print("-" * 40)
# Your code here:




# Exercise 2: Implement CREATE endpoint
# TODO: Create a POST /books/ endpoint that:
# - Accepts a BookCreate model
# - Adds the book to an in-memory dictionary
# - Returns BookResponse with status 201

print("\n\nExercise 2: CREATE Endpoint")
print("-" * 40)
# Your code here:




# Exercise 3: Implement READ endpoints
# TODO: Create two GET endpoints:
# - GET /books/ - Returns all books with pagination (skip, limit)
# - GET /books/{book_id} - Returns a single book or 404

print("\n\nExercise 3: READ Endpoints")
print("-" * 40)
# Your code here:




# Exercise 4: Implement UPDATE endpoint
# TODO: Create a PUT /books/{book_id} endpoint that:
# - Accepts BookCreate model
# - Updates all fields of the book
# - Returns 404 if book not found

print("\n\nExercise 4: UPDATE Endpoint")
print("-" * 40)
# Your code here:




# Exercise 5: Implement DELETE endpoint
# TODO: Create a DELETE /books/{book_id} endpoint that:
# - Deletes the book from the dictionary
# - Returns 204 No Content on success
# - Returns 404 if book not found

print("\n\nExercise 5: DELETE Endpoint")
print("-" * 40)
# Your code here:
