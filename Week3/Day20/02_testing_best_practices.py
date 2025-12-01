"""
Day 20 - Testing Best Practices
===============================
Learn: Writing effective tests, TDD, test organization

Key Concepts:
- Write tests that are maintainable and meaningful
- Follow TDD (Test-Driven Development) principles
- Organize tests for scalability
"""

import pytest
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

# ========== TEST-DRIVEN DEVELOPMENT (TDD) ==========
print("=" * 60)
print("TEST-DRIVEN DEVELOPMENT (TDD)")
print("=" * 60)

"""
TDD Cycle (Red-Green-Refactor):
1. RED: Write a failing test first
2. GREEN: Write minimal code to pass the test
3. REFACTOR: Improve the code while keeping tests green

Benefits:
- Forces you to think about requirements first
- Results in testable code
- Better code design
- Living documentation
"""


# ========== EXAMPLE: TDD PASSWORD VALIDATOR ==========
print("\n" + "=" * 60)
print("TDD EXAMPLE: PASSWORD VALIDATOR")
print("=" * 60)


# Step 1: Write tests first (RED)
class TestPasswordValidator:
    """Tests for password validation."""
    
    def test_password_too_short(self):
        """Password must be at least 8 characters."""
        assert validate_password("short") == False
    
    def test_password_minimum_length(self):
        """Password with exactly 8 characters should pass length check."""
        result = validate_password("Abcd123!")
        assert result == True
    
    def test_password_needs_uppercase(self):
        """Password must contain uppercase letter."""
        assert validate_password("abcd1234!") == False
    
    def test_password_needs_lowercase(self):
        """Password must contain lowercase letter."""
        assert validate_password("ABCD1234!") == False
    
    def test_password_needs_digit(self):
        """Password must contain a digit."""
        assert validate_password("Abcdefgh!") == False
    
    def test_password_needs_special_char(self):
        """Password must contain special character."""
        assert validate_password("Abcd12345") == False
    
    def test_valid_password(self):
        """Valid password passes all checks."""
        assert validate_password("SecurePass123!") == True


# Step 2: Implement the function (GREEN)
def validate_password(password: str) -> bool:
    """
    Validate password strength.
    
    Requirements:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in password)
    
    return has_upper and has_lower and has_digit and has_special


# ========== THE AAA PATTERN ==========
print("\n" + "=" * 60)
print("THE AAA PATTERN (ARRANGE-ACT-ASSERT)")
print("=" * 60)

"""
Every test should follow the AAA pattern:
- ARRANGE: Set up test data and conditions
- ACT: Perform the action being tested
- ASSERT: Verify the results
"""


@dataclass
class User:
    """User model for testing examples."""
    id: int
    username: str
    email: str
    is_active: bool = True
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()


class UserService:
    """Service class for user operations."""
    
    def __init__(self):
        self.users: List[User] = []
    
    def create_user(self, username: str, email: str) -> User:
        """Create a new user."""
        if not username or not email:
            raise ValueError("Username and email are required")
        if "@" not in email:
            raise ValueError("Invalid email format")
        if any(u.email == email for u in self.users):
            raise ValueError("Email already exists")
        
        user = User(
            id=len(self.users) + 1,
            username=username,
            email=email
        )
        self.users.append(user)
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def deactivate_user(self, user_id: int) -> bool:
        """Deactivate a user."""
        user = self.get_user(user_id)
        if user:
            user.is_active = False
            return True
        return False
    
    def get_active_users(self) -> List[User]:
        """Get all active users."""
        return [u for u in self.users if u.is_active]


# Well-structured tests using AAA pattern
class TestUserService:
    """Tests for UserService following best practices."""
    
    @pytest.fixture
    def service(self):
        """Provide a fresh UserService instance."""
        return UserService()
    
    @pytest.fixture
    def service_with_users(self, service):
        """Provide a service with some existing users."""
        service.create_user("john", "john@example.com")
        service.create_user("jane", "jane@example.com")
        return service
    
    def test_create_user_successfully(self, service):
        """Test creating a new user with valid data."""
        # ARRANGE
        username = "testuser"
        email = "test@example.com"
        
        # ACT
        user = service.create_user(username, email)
        
        # ASSERT
        assert user.id == 1
        assert user.username == username
        assert user.email == email
        assert user.is_active == True
    
    def test_create_user_without_username_fails(self, service):
        """Test that creating user without username raises error."""
        # ARRANGE
        username = ""
        email = "test@example.com"
        
        # ACT & ASSERT
        with pytest.raises(ValueError) as excinfo:
            service.create_user(username, email)
        assert "required" in str(excinfo.value)
    
    def test_create_user_with_invalid_email_fails(self, service):
        """Test that invalid email format raises error."""
        # ARRANGE
        username = "testuser"
        email = "invalid-email"
        
        # ACT & ASSERT
        with pytest.raises(ValueError) as excinfo:
            service.create_user(username, email)
        assert "Invalid email" in str(excinfo.value)
    
    def test_create_user_with_duplicate_email_fails(self, service_with_users):
        """Test that duplicate email raises error."""
        # ARRANGE (user already exists via fixture)
        
        # ACT & ASSERT
        with pytest.raises(ValueError) as excinfo:
            service_with_users.create_user("newuser", "john@example.com")
        assert "already exists" in str(excinfo.value)
    
    def test_get_existing_user(self, service_with_users):
        """Test getting an existing user by ID."""
        # ARRANGE (users created via fixture)
        
        # ACT
        user = service_with_users.get_user(1)
        
        # ASSERT
        assert user is not None
        assert user.username == "john"
    
    def test_get_nonexistent_user_returns_none(self, service):
        """Test getting a user that doesn't exist."""
        # ARRANGE (empty service)
        
        # ACT
        user = service.get_user(999)
        
        # ASSERT
        assert user is None
    
    def test_deactivate_user(self, service_with_users):
        """Test deactivating a user."""
        # ARRANGE (users created via fixture)
        
        # ACT
        result = service_with_users.deactivate_user(1)
        
        # ASSERT
        assert result == True
        user = service_with_users.get_user(1)
        assert user.is_active == False
    
    def test_get_active_users(self, service_with_users):
        """Test getting only active users."""
        # ARRANGE
        service_with_users.deactivate_user(1)
        
        # ACT
        active_users = service_with_users.get_active_users()
        
        # ASSERT
        assert len(active_users) == 1
        assert active_users[0].username == "jane"


# ========== TESTING BEST PRACTICES ==========
print("\n" + "=" * 60)
print("TESTING BEST PRACTICES")
print("=" * 60)

"""
1. ONE ASSERTION PER TEST (when practical)
   - Makes failures easier to diagnose
   - Exception: Related assertions can be grouped

2. DESCRIPTIVE TEST NAMES
   - test_<what_is_being_tested>_<expected_behavior>
   - Use snake_case
   - Be specific

3. TEST ISOLATION
   - Tests should not depend on each other
   - Use fixtures for setup
   - Clean up after tests

4. TEST ONLY PUBLIC INTERFACE
   - Don't test private methods directly
   - Test behavior, not implementation

5. USE MEANINGFUL ASSERTIONS
   - Use specific assertions over generic ones
   - Include helpful error messages

6. AVOID MAGIC NUMBERS
   - Use constants or variables with clear names
   - Makes tests more readable
"""


# Example: Good vs Bad Test Names
class TestNamingConventions:
    """Examples of good test naming."""
    
    # BAD: test_user (what about user?)
    # GOOD:
    def test_create_user_with_valid_data_succeeds(self):
        """Clear name describes scenario and expectation."""
        pass
    
    # BAD: test_error (what error? when?)
    # GOOD:
    def test_create_user_with_empty_email_raises_validation_error(self):
        """Name tells us exactly what we're testing."""
        pass


# ========== ORGANIZING TEST FILES ==========
print("\n" + "=" * 60)
print("ORGANIZING TEST FILES")
print("=" * 60)

"""
Project Structure Example:

my_project/
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_models/
│   │   │   └── test_user.py
│   │   └── test_services/
│   │       └── test_user_service.py
│   └── integration/
│       ├── __init__.py
│       └── test_api.py
├── requirements.txt
├── pytest.ini
└── README.md

conftest.py - Contains shared fixtures:

import pytest

@pytest.fixture
def db_connection():
    '''Create test database connection.'''
    conn = create_connection("test_db")
    yield conn
    conn.rollback()
    conn.close()
"""


# ========== USING CONFTEST.PY ==========
print("\n" + "=" * 60)
print("SHARED FIXTURES (conftest.py)")
print("=" * 60)

"""
conftest.py is special:
- Automatically discovered by pytest
- Fixtures defined here are available to all test files
- Can have multiple conftest.py at different levels
"""

# Example conftest.py content (usually in separate file)
"""
# tests/conftest.py

import pytest
from myapp import create_app, db

@pytest.fixture(scope="session")
def app():
    '''Create application for testing.'''
    app = create_app("testing")
    return app

@pytest.fixture(scope="function")
def client(app):
    '''Create test client.'''
    return app.test_client()

@pytest.fixture(scope="function")
def database(app):
    '''Set up test database.'''
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()
"""


# ========== TEST COVERAGE ==========
print("\n" + "=" * 60)
print("TEST COVERAGE")
print("=" * 60)

"""
Coverage measures how much of your code is tested.

Commands:
- pytest --cov=src                    # Basic coverage
- pytest --cov=src --cov-report=html  # HTML report
- pytest --cov=src --cov-fail-under=80  # Fail if < 80%

Coverage Targets:
- 80%+ is a good goal for most projects
- 100% is often impractical
- Focus on critical paths first
"""


# ========== WHAT NOT TO TEST ==========
print("\n" + "=" * 60)
print("WHAT NOT TO TEST")
print("=" * 60)

"""
Skip testing:
1. Third-party libraries (they have their own tests)
2. Language features (Python itself is tested)
3. Simple getters/setters with no logic
4. Generated code
5. Configuration constants

Focus on:
1. Business logic
2. Edge cases
3. Error handling
4. Integration points
5. Complex algorithms
"""


# ========== COMMON MISTAKES ==========
print("\n" + "=" * 60)
print("COMMON TESTING MISTAKES")
print("=" * 60)

"""
1. Testing implementation instead of behavior
   BAD: Testing that a specific method was called
   GOOD: Testing that the result is correct

2. Not testing edge cases
   BAD: Only testing happy path
   GOOD: Testing empty inputs, None, boundaries

3. Fragile tests
   BAD: Tests that break with minor changes
   GOOD: Tests that focus on behavior

4. Slow tests
   BAD: Tests that take minutes
   GOOD: Fast unit tests, separate slow integration tests

5. Not cleaning up
   BAD: Tests leave data behind
   GOOD: Use fixtures with proper teardown
"""


# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE EXAMPLE: CALCULATOR WITH TDD")
print("=" * 60)


class Calculator:
    """Calculator class developed with TDD."""
    
    def __init__(self):
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self._record_operation(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self._record_operation(f"{a} / {b} = {result}")
        return result
    
    def _record_operation(self, operation: str):
        """Record operation in history."""
        self.history.append(operation)
    
    def get_history(self) -> List[str]:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()


class TestCalculator:
    """Comprehensive tests for Calculator."""
    
    @pytest.fixture
    def calc(self):
        """Provide a fresh calculator instance."""
        return Calculator()
    
    # Addition tests
    def test_add_positive_numbers(self, calc):
        assert calc.add(2, 3) == 5
    
    def test_add_negative_numbers(self, calc):
        assert calc.add(-1, -1) == -2
    
    def test_add_floats(self, calc):
        assert calc.add(1.5, 2.5) == pytest.approx(4.0)
    
    # Subtraction tests
    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(5, 3) == 2
    
    def test_subtract_resulting_negative(self, calc):
        assert calc.subtract(3, 5) == -2
    
    # Multiplication tests
    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(3, 4) == 12
    
    def test_multiply_by_zero(self, calc):
        assert calc.multiply(100, 0) == 0
    
    # Division tests
    def test_divide_positive_numbers(self, calc):
        assert calc.divide(10, 2) == 5
    
    def test_divide_with_float_result(self, calc):
        assert calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero_raises_error(self, calc):
        with pytest.raises(ZeroDivisionError) as excinfo:
            calc.divide(10, 0)
        assert "Cannot divide by zero" in str(excinfo.value)
    
    # History tests
    def test_history_is_empty_initially(self, calc):
        assert calc.get_history() == []
    
    def test_operations_are_recorded(self, calc):
        calc.add(2, 3)
        calc.multiply(4, 5)
        history = calc.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history[0]
    
    def test_clear_history(self, calc):
        calc.add(1, 1)
        calc.clear_history()
        assert calc.get_history() == []


print("\n" + "=" * 60)
print("✅ Testing Best Practices - Complete!")
print("=" * 60)
print("\nRun: pytest 02_testing_best_practices.py -v")
