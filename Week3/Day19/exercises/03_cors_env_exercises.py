"""
EXERCISES: CORS, Security, and Environment Variables
=====================================================
Complete all exercises below
"""

# Exercise 1: CORS Configuration
# TODO: Write FastAPI CORS configuration that:
# - Allows origins from localhost:3000, localhost:5000, and myapp.com
# - Allows credentials
# - Only allows GET, POST, PUT methods
# - Only allows Content-Type and Authorization headers
# - Sets max_age to 600 seconds

print("Exercise 1: CORS Configuration")
print("-" * 40)
# Your code here




# Exercise 2: Security Headers Middleware
# TODO: Create a middleware that adds these security headers:
# - X-Content-Type-Options: nosniff
# - X-Frame-Options: SAMEORIGIN (not DENY)
# - Referrer-Policy: strict-origin-when-cross-origin
# - X-XSS-Protection: 1; mode=block

print("\n\nExercise 2: Security Headers Middleware")
print("-" * 40)
# Your code here




# Exercise 3: Environment Variables
# TODO: Create a Settings class using Pydantic that has:
# - app_name (str, default "MyApp")
# - environment (str, must be "development", "staging", or "production")
# - database_url (str, required)
# - secret_key (str, required)
# - debug (bool, default False)
# - allowed_hosts (List[str], parse from comma-separated string)
# - max_connections (int, between 1 and 100, default 10)

print("\n\nExercise 3: Environment Variables")
print("-" * 40)
# Your code here




# Exercise 4: Rate Limiting
# TODO: Write a simple rate limiting middleware/decorator
# that limits requests to 100 per minute per IP address
# Return 429 status if limit exceeded

print("\n\nExercise 4: Rate Limiting")
print("-" * 40)
# Your code here




# Exercise 5: Complete Secure API Setup
# TODO: Create a FastAPI app with:
# - CORS middleware (for localhost:3000)
# - Security headers middleware
# - Rate limiting (60 requests/minute)
# - Settings loaded from environment
# - One protected endpoint that requires an API key

print("\n\nExercise 5: Complete Secure API Setup")
print("-" * 40)
# Your code here
