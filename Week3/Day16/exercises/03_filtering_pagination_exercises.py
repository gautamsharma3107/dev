"""
EXERCISES: Filtering and Pagination
====================================
Complete all exercises below
"""

# Exercise 1: Basic Filtering Setup
# TODO: Configure a ViewSet with:
# - DjangoFilterBackend
# - filterset_fields for: category, status, is_featured

print("Exercise 1: Basic Filtering")
print("-" * 40)
# Your code here


# Exercise 2: Custom FilterSet
# TODO: Create a FilterSet for a Product model with:
# - name (case-insensitive contains)
# - min_price and max_price (range filter)
# - category (exact match)
# - in_stock (boolean, items with stock > 0)

print("\n\nExercise 2: Custom FilterSet")
print("-" * 40)
# Your code here


# Exercise 3: Search and Ordering
# TODO: Configure a ViewSet with:
# - SearchFilter searching: title, description, author__username
# - OrderingFilter with fields: created_at, price, rating
# - Default ordering by -created_at

print("\n\nExercise 3: Search and Ordering")
print("-" * 40)
# Your code here


# Exercise 4: Custom Pagination
# TODO: Create a custom PageNumberPagination class that:
# - Has 20 items per page by default
# - Allows page_size query param (max 100)
# - Returns custom response format with: count, total_pages, current_page, results

print("\n\nExercise 4: Custom Pagination")
print("-" * 40)
# Your code here


# Exercise 5: Complete ViewSet
# TODO: Create a complete ViewSet that combines:
# - All three filter backends
# - Custom FilterSet
# - Search in multiple fields
# - Ordering by multiple fields
# - Custom pagination

print("\n\nExercise 5: Complete Filtering + Pagination")
print("-" * 40)
# Your code here


# Bonus Exercise: Conditional Pagination
# TODO: Create a ViewSet that:
# - Paginates by default
# - Returns all results when ?all=true is passed

print("\n\nBonus: Conditional Pagination")
print("-" * 40)
# Your code here
