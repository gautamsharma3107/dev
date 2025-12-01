"""
EXERCISES: Pydantic Models
==========================
Complete all 5 exercises below
"""

# Exercise 1: Basic Pydantic Model
# TODO: Create a Pydantic model called "Book" with:
# - title: required string
# - author: required string
# - year: required integer
# - isbn: optional string
# - price: float with default 9.99

print("Exercise 1: Basic Pydantic Model")
print("-" * 40)
# Your code here




# Exercise 2: Field Validation
# TODO: Create a Pydantic model called "User" with:
# - username: string (3-20 characters)
# - email: EmailStr
# - age: integer (must be >= 18 and <= 120)
# - password: string (minimum 8 characters)

print("\n\nExercise 2: Field Validation")
print("-" * 40)
# Your code here




# Exercise 3: Nested Models
# TODO: Create these nested models:
# - Address: street, city, country, postal_code
# - Person: name, email, address (Address model)
# - Company: name, employees (list of Person)

print("\n\nExercise 3: Nested Models")
print("-" * 40)
# Your code here




# Exercise 4: Custom Validators
# TODO: Create a Pydantic model "Comment" with:
# - content: string (validator: must not be empty after stripping whitespace)
# - author: string (validator: convert to title case)
# - tags: list of strings (validator: each tag should be lowercase, max 5 tags)

print("\n\nExercise 4: Custom Validators")
print("-" * 40)
# Your code here




# Exercise 5: Model Inheritance
# TODO: Create a model hierarchy for a blog:
# - PostBase: title, content (both required)
# - PostCreate: inherits PostBase (for creating posts)
# - PostUpdate: title and content both optional (for partial updates)
# - PostResponse: inherits PostBase, adds id, created_at, author_name

print("\n\nExercise 5: Model Inheritance")
print("-" * 40)
# Your code here



