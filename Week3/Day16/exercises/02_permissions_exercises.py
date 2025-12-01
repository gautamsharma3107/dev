"""
EXERCISES: Permissions
=======================
Complete all exercises below
"""

# Exercise 1: Permission Classes Usage
# TODO: Which permission class would you use for each scenario?
# a) A view that only admins can access
# b) A view that anyone can read but only logged-in users can write
# c) A view that only the owner can access
# d) A public view that doesn't require authentication

print("Exercise 1: Permission Classes")
print("-" * 40)
# Write your answers as comments
# a) 
# b) 
# c) 
# d) 


# Exercise 2: Custom IsOwner Permission
# TODO: Create a custom permission class called IsOwner that:
# - Allows any authenticated user to list and create
# - Only allows the owner to retrieve, update, or delete

print("\n\nExercise 2: IsOwner Permission")
print("-" * 40)
# Your code here


# Exercise 3: IsOwnerOrAdmin Permission
# TODO: Create a permission that allows:
# - Admins to access anything
# - Owners to access their own objects
# - Read-only access for everyone else

print("\n\nExercise 3: IsOwnerOrAdmin Permission")
print("-" * 40)
# Your code here


# Exercise 4: Action-Level Permissions
# TODO: Write a get_permissions() method that:
# - list: AllowAny
# - create: IsAuthenticated
# - retrieve: AllowAny
# - update/partial_update: IsOwner
# - destroy: IsAdminUser

print("\n\nExercise 4: Action-Level Permissions")
print("-" * 40)
# Your code here


# Exercise 5: Premium User Permission
# TODO: Create a permission that:
# - Checks if user has a 'is_premium' attribute
# - Returns custom error message if not premium
# - Allows access only to premium users

print("\n\nExercise 5: Premium User Permission")
print("-" * 40)
# Your code here
