# Day 20 Quick Reference Cheat Sheet

## pytest Basics
```python
# Install pytest
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest test_file.py

# Run specific test function
pytest test_file.py::test_function

# Run with verbose output
pytest -v

# Run and show print statements
pytest -s
```

## Test File Naming
```python
# Test files must start with test_ or end with _test.py
test_calculator.py  # ✅
calculator_test.py  # ✅
calculator.py       # ❌ (won't be discovered)

# Test functions must start with test_
def test_addition():  # ✅
def addition_test():  # ❌
```

## Basic Test Structure
```python
import pytest

def add(a, b):
    return a + b

# Simple test
def test_add_positive_numbers():
    assert add(2, 3) == 5

# Test with multiple assertions
def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0

# Test for exceptions
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## Fixtures
```python
import pytest

# Simple fixture
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list_length(sample_list):
    assert len(sample_list) == 5

# Fixture with setup and teardown
@pytest.fixture
def database_connection():
    # Setup
    conn = create_connection()
    yield conn
    # Teardown
    conn.close()

# Shared fixtures (conftest.py)
# Place fixtures in conftest.py for sharing across test files
```

## Parametrized Tests
```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Markers
```python
import pytest

# Skip a test
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

# Skip conditionally
@pytest.mark.skipif(sys.platform == "win32", reason="Not for Windows")
def test_unix_only():
    pass

# Mark as expected to fail
@pytest.mark.xfail
def test_known_bug():
    assert 1 == 2

# Custom markers
@pytest.mark.slow
def test_slow_operation():
    pass

# Run only slow tests: pytest -m slow
```

## Mocking
```python
from unittest.mock import Mock, patch, MagicMock

# Simple mock
mock_obj = Mock()
mock_obj.method.return_value = 42
assert mock_obj.method() == 42

# Patch a function
@patch('module.function')
def test_with_patch(mock_func):
    mock_func.return_value = "mocked"
    result = module.function()
    assert result == "mocked"

# Patch as context manager
def test_with_context_patch():
    with patch('module.function') as mock_func:
        mock_func.return_value = "mocked"
        result = module.function()
        assert result == "mocked"
```

## API Testing
```python
import pytest
import requests

# Testing API endpoints
def test_get_users():
    response = requests.get("https://api.example.com/users")
    assert response.status_code == 200
    assert "users" in response.json()

# Using fixtures for API client
@pytest.fixture
def api_client():
    return requests.Session()

def test_authenticated_request(api_client):
    api_client.headers["Authorization"] = "Bearer token"
    response = api_client.get("https://api.example.com/protected")
    assert response.status_code == 200
```

## FastAPI Testing
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post("/items/", json={"name": "Test"})
    assert response.status_code == 201
```

## Code Organization
```python
# Project structure
my_project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models/
│   └── test_services/
├── requirements.txt
└── pytest.ini
```

## Error Handling Patterns
```python
# Custom exceptions
class ValidationError(Exception):
    """Raised when validation fails"""
    pass

class NotFoundError(Exception):
    """Raised when resource not found"""
    pass

# Function with proper error handling
def get_user(user_id: int):
    if user_id < 0:
        raise ValidationError("User ID must be positive")
    user = database.get(user_id)
    if not user:
        raise NotFoundError(f"User {user_id} not found")
    return user

# Testing exceptions
def test_invalid_user_id():
    with pytest.raises(ValidationError):
        get_user(-1)
```

## Test Coverage Commands
```bash
# Run with coverage
pytest --cov=src

# Generate HTML report
pytest --cov=src --cov-report=html

# Show missing lines
pytest --cov=src --cov-report=term-missing

# Fail if coverage below threshold
pytest --cov=src --cov-fail-under=80
```

## Common Assertions
```python
# Equality
assert result == expected
assert result != unexpected

# Boolean
assert condition
assert not condition

# Membership
assert item in collection
assert item not in collection

# Type checking
assert isinstance(result, list)

# Approximate (for floats)
assert result == pytest.approx(expected, rel=1e-3)

# None checks
assert result is None
assert result is not None
```

## pytest.ini Configuration
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
```

---
**Keep this handy for quick reference!** 🚀
