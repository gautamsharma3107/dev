"""
Day 4 - Custom Exceptions
=========================
Learn: Creating your own exception classes

Key Concepts:
- Inherit from Exception class
- Add custom attributes
- Create exception hierarchies
- Use for domain-specific errors
"""

# ========== WHY CUSTOM EXCEPTIONS? ==========
print("=" * 50)
print("WHY CUSTOM EXCEPTIONS?")
print("=" * 50)

print("""
Benefits of custom exceptions:
1. More descriptive error types
2. Domain-specific error handling
3. Add custom data to exceptions
4. Better code organization
5. Clearer error hierarchies
""")

# ========== BASIC CUSTOM EXCEPTION ==========
print("=" * 50)
print("BASIC CUSTOM EXCEPTION")
print("=" * 50)

# Simple custom exception
class ValidationError(Exception):
    """Raised when validation fails"""
    pass

def validate_username(username):
    if len(username) < 3:
        raise ValidationError("Username too short (min 3 chars)")
    if len(username) > 20:
        raise ValidationError("Username too long (max 20 chars)")
    if not username.isalnum():
        raise ValidationError("Username must be alphanumeric")
    return True

print("Testing validate_username():")
try:
    validate_username("ab")
except ValidationError as e:
    print(f"   ValidationError: {e}")

try:
    validate_username("valid_user123")
    print("   ✅ Username valid!")
except ValidationError as e:
    print(f"   ValidationError: {e}")

# ========== EXCEPTION WITH ATTRIBUTES ==========
print("\n" + "=" * 50)
print("EXCEPTION WITH CUSTOM ATTRIBUTES")
print("=" * 50)

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    
    def __init__(self, balance, amount, message="Insufficient funds"):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: Balance ${self.balance}, Requested ${self.amount}, Short ${self.deficit}"

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Test it
account = BankAccount(100)
print(f"Account balance: ${account.balance}")

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"   Current balance: ${e.balance}")
    print(f"   Requested: ${e.amount}")
    print(f"   Deficit: ${e.deficit}")

# ========== EXCEPTION HIERARCHY ==========
print("\n" + "=" * 50)
print("EXCEPTION HIERARCHY")
print("=" * 50)

# Base exception for our application
class AppError(Exception):
    """Base exception for application errors"""
    pass

# Specific exceptions
class DatabaseError(AppError):
    """Database-related errors"""
    pass

class ConnectionError(DatabaseError):
    """Database connection errors"""
    pass

class QueryError(DatabaseError):
    """Database query errors"""
    pass

class AuthenticationError(AppError):
    """Authentication-related errors"""
    pass

class InvalidCredentialsError(AuthenticationError):
    """Invalid username or password"""
    pass

class SessionExpiredError(AuthenticationError):
    """User session has expired"""
    pass

# Using the hierarchy
def simulate_login(username, password):
    if username != "admin":
        raise InvalidCredentialsError("User not found")
    if password != "secret":
        raise InvalidCredentialsError("Wrong password")
    return "Logged in!"

def simulate_db_query(query):
    if "DROP" in query.upper():
        raise QueryError("Dangerous query blocked")
    return "Query executed"

print("Testing exception hierarchy:")

# Catch specific exception
try:
    simulate_login("user", "pass")
except InvalidCredentialsError as e:
    print(f"   InvalidCredentialsError: {e}")

# Catch parent exception
try:
    simulate_login("admin", "wrong")
except AuthenticationError as e:
    print(f"   AuthenticationError: {e}")

# Catch base exception
try:
    simulate_db_query("DROP TABLE users")
except AppError as e:
    print(f"   AppError: {e}")

# ========== EXCEPTION WITH ERROR CODES ==========
print("\n" + "=" * 50)
print("EXCEPTION WITH ERROR CODES")
print("=" * 50)

class APIError(Exception):
    """API-related errors with codes"""
    
    def __init__(self, code, message, details=None):
        self.code = code
        self.message = message
        self.details = details or {}
        super().__init__(self.message)
    
    def to_dict(self):
        return {
            "error_code": self.code,
            "message": self.message,
            "details": self.details
        }

# Error code constants
class ErrorCodes:
    INVALID_INPUT = 1001
    NOT_FOUND = 1002
    UNAUTHORIZED = 1003
    RATE_LIMITED = 1004

def api_get_user(user_id):
    if user_id < 0:
        raise APIError(
            ErrorCodes.INVALID_INPUT,
            "Invalid user ID",
            {"user_id": user_id, "expected": "positive integer"}
        )
    if user_id > 1000:
        raise APIError(
            ErrorCodes.NOT_FOUND,
            "User not found",
            {"user_id": user_id}
        )
    return {"id": user_id, "name": "John"}

print("Testing API errors:")
try:
    api_get_user(-1)
except APIError as e:
    print(f"   Code: {e.code}")
    print(f"   Message: {e.message}")
    print(f"   Details: {e.details}")
    print(f"   As dict: {e.to_dict()}")

# ========== PRACTICAL: USER VALIDATION ==========
print("\n" + "=" * 50)
print("PRACTICAL: User Registration System")
print("=" * 50)

class RegistrationError(Exception):
    """Base exception for registration errors"""
    pass

class UsernameError(RegistrationError):
    pass

class EmailError(RegistrationError):
    pass

class PasswordError(RegistrationError):
    pass

def validate_registration(username, email, password):
    errors = []
    
    # Username validation
    if len(username) < 3:
        errors.append(UsernameError("Username must be at least 3 characters"))
    if not username[0].isalpha():
        errors.append(UsernameError("Username must start with a letter"))
    
    # Email validation
    if "@" not in email:
        errors.append(EmailError("Email must contain @"))
    if "." not in email.split("@")[-1]:
        errors.append(EmailError("Email domain must contain ."))
    
    # Password validation
    if len(password) < 8:
        errors.append(PasswordError("Password must be at least 8 characters"))
    if not any(c.isupper() for c in password):
        errors.append(PasswordError("Password must contain uppercase letter"))
    if not any(c.isdigit() for c in password):
        errors.append(PasswordError("Password must contain a digit"))
    
    if errors:
        raise RegistrationError(errors)
    
    return True

print("Testing registration:")

# Test with invalid data
try:
    validate_registration("ab", "invalid", "weak")
except RegistrationError as e:
    print("   Validation errors:")
    for error in e.args[0]:
        print(f"     - {type(error).__name__}: {error}")

# Test with valid data
try:
    validate_registration("johndoe", "john@example.com", "SecurePass123")
    print("   ✅ Registration valid!")
except RegistrationError as e:
    for error in e.args[0]:
        print(f"   - {error}")

print("\n" + "=" * 50)
print("✅ Custom Exceptions - Complete!")
print("=" * 50)
