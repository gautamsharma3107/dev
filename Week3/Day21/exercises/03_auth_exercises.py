"""
EXERCISES: Authentication
=========================
Complete all 5 exercises below
"""

# Exercise 1: Password Hashing
# TODO: Using passlib with bcrypt:
# - Write a function to hash a password
# - Write a function to verify a password
# - Test both functions

print("Exercise 1: Password Hashing")
print("-" * 40)
# Your code here:




# Exercise 2: JWT Token Creation
# TODO: Using python-jose:
# - Write a function to create a JWT token
# - The token should include: sub (subject), exp (expiration)
# - Set expiration to 30 minutes from now

print("\n\nExercise 2: JWT Token Creation")
print("-" * 40)
# Your code here:




# Exercise 3: Token Validation
# TODO: Write a function to decode and validate a JWT token:
# - Return the payload if valid
# - Return None if invalid or expired

print("\n\nExercise 3: Token Validation")
print("-" * 40)
# Your code here:




# Exercise 4: User Registration Endpoint
# TODO: Create a POST /register endpoint that:
# - Accepts username, email, password
# - Hashes the password before storing
# - Returns user data (without password)

print("\n\nExercise 4: User Registration")
print("-" * 40)
# Your code here:




# Exercise 5: Protected Route
# TODO: Create a GET /protected endpoint that:
# - Requires a valid JWT token
# - Uses OAuth2PasswordBearer
# - Returns user info from the token

print("\n\nExercise 5: Protected Route")
print("-" * 40)
# Your code here:
