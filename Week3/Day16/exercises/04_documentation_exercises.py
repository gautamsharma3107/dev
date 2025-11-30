"""
EXERCISES: API Documentation
=============================
Complete all exercises below
"""

# Exercise 1: DRF-Spectacular Setup
# TODO: Write the settings.py configuration for drf-spectacular
# Include: SPECTACULAR_SETTINGS with title, description, version

print("Exercise 1: DRF-Spectacular Settings")
print("-" * 40)
# Your code here


# Exercise 2: Documentation URLs
# TODO: Write the URL configuration for:
# - /api/schema/ - Raw schema
# - /api/docs/ - Swagger UI
# - /api/redoc/ - ReDoc

print("\n\nExercise 2: Documentation URLs")
print("-" * 40)
# Your code here


# Exercise 3: Documenting a ViewSet
# TODO: Use @extend_schema_view to document a BookViewSet with:
# - list: summary and tags
# - create: summary, description, and tags
# - retrieve: summary and tags
# - destroy: summary, description (mention admin only)

print("\n\nExercise 3: Documenting ViewSet")
print("-" * 40)
# Your code here


# Exercise 4: Query Parameters Documentation
# TODO: Document the following query parameters for a list view:
# - title (string, optional) - Filter by title
# - min_price (number, optional) - Minimum price
# - category (string, optional, enum: ['fiction', 'non-fiction', 'science'])
# - page (integer, optional) - Page number

print("\n\nExercise 4: Query Parameters")
print("-" * 40)
# Your code here


# Exercise 5: Request/Response Examples
# TODO: Add OpenApiExample for a create endpoint:
# - Request example with book title, author, price
# - Success response example (201)
# - Error response example (400)

print("\n\nExercise 5: Request/Response Examples")
print("-" * 40)
# Your code here


# Exercise 6: Security Documentation
# TODO: Configure SPECTACULAR_SETTINGS to document:
# - Token authentication (Authorization: Token xxx)
# - Mark certain endpoints as requiring authentication

print("\n\nExercise 6: Security Documentation")
print("-" * 40)
# Your code here
