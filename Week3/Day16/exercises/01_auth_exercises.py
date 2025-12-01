"""
EXERCISES: Token Authentication
================================
Complete all exercises below
"""

# Exercise 1: Basic Token Setup
# TODO: Write the settings.py configuration needed to enable 
# TokenAuthentication as the default authentication class

print("Exercise 1: Token Authentication Settings")
print("-" * 40)
# Your code here - Write the INSTALLED_APPS and REST_FRAMEWORK settings


# Exercise 2: Token Creation Signal
# TODO: Write a signal that automatically creates a token 
# when a new user is created

print("\n\nExercise 2: Auto Token Creation Signal")
print("-" * 40)
# Your code here


# Exercise 3: Custom Login View
# TODO: Create a login view that:
# - Accepts username and password
# - Returns token, user_id, and username
# - Handles invalid credentials with proper error messages

print("\n\nExercise 3: Custom Login View")
print("-" * 40)
# Your code here


# Exercise 4: Registration with Token
# TODO: Create a registration view that:
# - Creates a new user
# - Automatically creates a token
# - Returns the token with user info

print("\n\nExercise 4: Registration with Token")
print("-" * 40)
# Your code here


# Exercise 5: Protected Endpoint
# TODO: Create an API view that:
# - Requires authentication
# - Returns current user's profile information
# - Include username, email, and date joined

print("\n\nExercise 5: Protected Profile Endpoint")
print("-" * 40)
# Your code here
