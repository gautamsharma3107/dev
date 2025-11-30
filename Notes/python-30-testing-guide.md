# Testing in Python: Complete Guide

---

## Table of Contents
1. [Introduction to Testing](#introduction-to-testing)
2. [unittest Module](#unittest-module)
3. [pytest Framework](#pytest-framework)
4. [Mocking](#mocking)
5. [Test Coverage](#test-coverage)
6. [Testing Types](#testing-types)
7. [Test-Driven Development](#test-driven-development)
8. [Practical Examples](#practical-examples)
9. [Best Practices](#best-practices)
10. [Practice Exercises](#practice-exercises)

---

## Introduction to Testing

### Why Testing?

```
Benefits:
✓ Catch bugs early
✓ Ensure code quality
✓ Refactor confidently
✓ Document expected behavior
✓ Reduce debugging time
✓ Save money (fix bugs early)

Types of Testing:
├── Unit Testing - Individual functions
├── Integration Testing - Multiple components
├── End-to-End Testing - Full workflows
├── API Testing - HTTP endpoints
└── Performance Testing - Speed/load

Testing Pyramid:
       /\
      /  \  E2E
     /____\
    /      \  Integration
   /________\
  /          \  Unit
 /____________\
```

### Testing Tools

```
unittest:
- Built-in Python
- Class-based
- Traditional
- xUnit style

pytest:
- Simpler syntax
- Fixtures
- Plugins
- Better parametrization
- More Pythonic

Coverage:
- Measure code coverage
- Identify untested code
- Reports

Mocking:
- unittest.mock
- Replace real objects
- Control behavior
```

---

## unittest Module

### Test Cases

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        """Test that 2 + 2 equals 4"""
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)
    
    def test_multiplication(self):
        result = 3 * 4
        self.assertEqual(result, 12)
    
    def test_division(self):
        result = 10 / 2
        self.assertEqual(result, 5.0)

# Run tests
if __name__ == '__main__':
    unittest.main()

# Run from command line
# python -m unittest test_calculator.py
# python -m unittest test_calculator.TestCalculator.test_addition
```

### Assertions

```python
import unittest

class TestAssertions(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(2 + 2, 4)          # ==
        self.assertNotEqual(2 + 2, 5)       # !=
    
    def test_truth(self):
        self.assertTrue(True)               # is True
        self.assertFalse(False)             # is False
    
    def test_identity(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)                 # is
        self.assertIsNot(a, [1, 2, 3])      # is not
    
    def test_membership(self):
        self.assertIn(1, [1, 2, 3])         # in
        self.assertNotIn(4, [1, 2, 3])      # not in
    
    def test_types(self):
        self.assertIsInstance(5, int)       # isinstance
        self.assertNotIsInstance(5, str)    # not isinstance
    
    def test_none(self):
        self.assertIsNone(None)             # is None
        self.assertIsNotNone(5)             # is not None
    
    def test_collections(self):
        self.assertListEqual([1, 2], [1, 2])
        self.assertDictEqual({'a': 1}, {'a': 1})
        self.assertSetEqual({1, 2}, {1, 2})
    
    def test_exceptions(self):
        with self.assertRaises(ValueError):
            int('not a number')
        
        with self.assertRaises(KeyError):
            d = {}
            d['missing_key']
    
    def test_regex(self):
        self.assertRegex('hello123', r'\d+')
        self.assertNotRegex('hello', r'\d+')
    
    def test_approximate(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
```

### setUp and tearDown

```python
import unittest

class TestWithSetupTeardown(unittest.TestCase):
    def setUp(self):
        """Run before each test"""
        print("setUp")
        self.items = []
        self.db_connection = "connected"
    
    def tearDown(self):
        """Run after each test"""
        print("tearDown")
        self.items = []
        self.db_connection = None
    
    def test_add_item(self):
        self.items.append(1)
        self.assertEqual(len(self.items), 1)
    
    def test_database_connected(self):
        self.assertEqual(self.db_connection, "connected")

# Module-level setup/teardown
def setUpModule():
    print("Module setup")

def tearDownModule():
    print("Module teardown")

# Class-level setup/teardown
class TestClassSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Class setup - runs once")
        cls.shared_resource = "resource"
    
    @classmethod
    def tearDownClass(cls):
        print("Class teardown - runs once")
        cls.shared_resource = None
    
    def test_something(self):
        self.assertEqual(self.shared_resource, "resource")
```

### Test Suites

```python
import unittest

class TestSuite1(unittest.TestCase):
    def test_a(self):
        self.assertTrue(True)
    
    def test_b(self):
        self.assertTrue(True)

class TestSuite2(unittest.TestCase):
    def test_c(self):
        self.assertTrue(True)
    
    def test_d(self):
        self.assertTrue(True)

# Create suite
suite = unittest.TestSuite()
suite.addTest(TestSuite1('test_a'))
suite.addTest(TestSuite2('test_c'))

# Run suite
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# Or load all tests from module
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(__import__(__name__))
runner = unittest.TextTestRunner()
runner.run(suite)
```

---

## pytest Framework

### Installation and Basic Usage

```bash
pip install pytest
```

```python
# test_simple.py
def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

def test_string():
    assert "hello" == "hello"

# Run tests
# pytest test_simple.py
# pytest                          # Run all tests
# pytest -v                       # Verbose
# pytest -s                       # Show print statements
# pytest test_simple.py::test_addition  # Specific test
```

### Fixtures

```python
import pytest

# Simple fixture
@pytest.fixture
def sample_list():
    return [1, 2, 3]

def test_with_fixture(sample_list):
    assert len(sample_list) == 3
    assert sample_list[0] == 1

# Fixture with setup and teardown
@pytest.fixture
def database_connection():
    # Setup
    db = {"connected": True}
    yield db  # Provide to test
    # Teardown
    db["connected"] = False

def test_database(database_connection):
    assert database_connection["connected"]

# Fixture with scope
@pytest.fixture(scope="session")
def expensive_resource():
    # Created once per session
    print("Setting up expensive resource")
    return {"data": "expensive"}

@pytest.fixture(scope="function")
def fresh_item():
    # Created for each test function
    return {"id": 1}

def test_with_session_fixture(expensive_resource):
    assert expensive_resource["data"] == "expensive"

# Parametrized fixtures
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_with_numbers(number):
    assert number > 0
```

### Parametrized Tests

```python
import pytest

# Simple parametrization
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input ** 2 == expected

# Multiple parameters
@pytest.mark.parametrize("x,y,expected", [
    (2, 3, 5),
    (1, 4, 5),
    (0, 5, 5),
])
def test_add(x, y, expected):
    assert x + y == expected

# Parametrize with IDs
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
], ids=["two", "three", "four"])
def test_square_with_ids(input, expected):
    assert input ** 2 == expected

# Nested parametrization
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_combined(x, y):
    assert x + y > 0
```

### Markers

```python
import pytest

# Built-in markers
@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    pass

@pytest.mark.skipif(True, reason="Skip if condition")
def test_skipped():
    pass

@pytest.mark.xfail
def test_expected_to_fail():
    assert False

@pytest.mark.xfail(strict=True)
def test_strict_expected_fail():
    assert False

# Custom markers
@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(10)

@pytest.mark.integration
def test_with_database():
    pass

# Run specific markers
# pytest -m slow
# pytest -m "not slow"
# pytest -m integration
```

### Plugins

```bash
# Install plugins
pip install pytest-cov
pip install pytest-mock
pip install pytest-asyncio
pip install pytest-timeout
```

```python
# pytest-cov for coverage
# pytest --cov=myapp test_myapp.py
# pytest --cov=myapp --cov-report=html

# pytest-mock for mocking
def test_with_mock(mocker):
    mock_func = mocker.patch('mymodule.external_function')
    mock_func.return_value = "mocked"
    
    result = mymodule.my_function()
    assert result == "mocked"
    mock_func.assert_called_once()

# pytest-asyncio for async tests
@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected

# pytest-timeout to prevent hanging tests
@pytest.mark.timeout(5)
def test_with_timeout():
    # Test must complete in 5 seconds
    pass
```

---

## Mocking

### unittest.mock

```python
from unittest import mock
from unittest.mock import Mock, MagicMock, patch

# Create mock object
mock_obj = Mock()
mock_obj.method.return_value = "value"
result = mock_obj.method()
print(result)  # "value"

# Access call information
mock_obj.method.assert_called()
mock_obj.method.assert_called_once()
mock_obj.method.assert_called_with()

# Configure mock
mock_obj = Mock(return_value=5)
print(mock_obj())  # 5

# Side effects
mock_obj = Mock(side_effect=[1, 2, 3])
print(mock_obj())  # 1
print(mock_obj())  # 2
print(mock_obj())  # 3

# MagicMock (supports magic methods)
magic_mock = MagicMock()
result = magic_mock + 5
print(result)  # MagicMock
```

### Patching

```python
from unittest.mock import patch
import requests

# Patch context manager
def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"id": 1}
        
        # Your code using requests.get
        response = requests.get('http://api.example.com/users')
        
        # Assertions
        assert response.json()["id"] == 1
        mock_get.assert_called_once_with('http://api.example.com/users')

# Patch decorator
@patch('requests.get')
def test_with_decorator(mock_get):
    mock_get.return_value.json.return_value = {"name": "Alice"}
    
    response = requests.get('http://api.example.com/users/1')
    assert response.json()["name"] == "Alice"

# Patch multiple objects
@patch('module.ClassB')
@patch('module.ClassA')
def test_multiple_patches(MockA, MockB):
    MockA.return_value.method.return_value = "A"
    MockB.return_value.method.return_value = "B"
    
    # Test code
    pass

# Patch object attributes
with patch.object(obj, 'attribute', 'new_value'):
    assert obj.attribute == 'new_value'
```

### MagicMock

```python
from unittest.mock import MagicMock

# MagicMock with special methods
mock_list = MagicMock()

# Supports magic methods
mock_list.__len__.return_value = 3
print(len(mock_list))  # 3

# Supports iteration
mock_list.__iter__.return_value = iter([1, 2, 3])
for item in mock_list:
    print(item)  # 1, 2, 3

# Supports item access
mock_dict = MagicMock()
mock_dict.__getitem__.return_value = "value"
print(mock_dict["key"])  # "value"

# Spec - restrict to specific class
class MyClass:
    def my_method(self):
        pass

mock = MagicMock(spec=MyClass)
mock.my_method()
# mock.unknown_method()  # Would raise AttributeError
```

---

## Test Coverage

### coverage.py

```bash
pip install coverage
```

```python
# Measure coverage
# coverage run -m pytest test_myapp.py
# coverage report
# coverage html  # Generate HTML report

# Command line
# coverage run --source=myapp -m pytest
# coverage report --precision=2
```

### Coverage Reports

```bash
# Terminal report
coverage report

# Detailed report
coverage report -m  # Show missing lines

# HTML report
coverage html
# Open htmlcov/index.html

# XML report (for CI/CD)
coverage xml

# JSON report
coverage json

# Configuration in .coveragerc
[run]
source = myapp
omit = 
    */tests/*
    */test_*.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
```

### Measuring Coverage

```python
# pytest-cov plugin
# pytest --cov=myapp
# pytest --cov=myapp --cov-report=html
# pytest --cov=myapp --cov-report=term-missing
# pytest --cov=myapp --cov-fail-under=80  # Fail if < 80%
```

---

## Testing Types

### Unit Testing

```python
# Test individual functions
def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Test classes
class Calculator:
    def multiply(self, x, y):
        return x * y

def test_calculator():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0
```

### Integration Testing

```python
# Test multiple components together
import pytest
from myapp import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_user_registration_flow(client):
    # Register user
    response = client.post('/register', json={
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    
    # Login
    response = client.post('/login', json={
        'username': 'alice',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in response.json
    
    # Access protected resource
    token = response.json['token']
    response = client.get('/profile', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
```

### End-to-End Testing

```python
# Test complete workflows
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_complete_workflow(browser):
    # Navigate to site
    browser.get('http://localhost:8000')
    
    # Fill form
    username_input = browser.find_element('id', 'username')
    username_input.send_keys('alice')
    
    password_input = browser.find_element('id', 'password')
    password_input.send_keys('password')
    
    submit_button = browser.find_element('id', 'submit')
    submit_button.click()
    
    # Assert result
    assert 'Dashboard' in browser.page_source
```

### API Testing

```python
import pytest
import requests
from myapp import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users_endpoint(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_user_endpoint(client):
    user_data = {
        'name': 'Alice',
        'email': 'alice@example.com'
    }
    response = client.post('/api/users', json=user_data)
    assert response.status_code == 201
    assert response.json['name'] == 'Alice'

def test_get_user_by_id(client):
    response = client.get('/api/users/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_update_user(client):
    response = client.put('/api/users/1', json={
        'name': 'Alice Updated'
    })
    assert response.status_code == 200
    assert response.json['name'] == 'Alice Updated'

def test_delete_user(client):
    response = client.delete('/api/users/1')
    assert response.status_code == 204
```

---

## Test-Driven Development (TDD)

### Red-Green-Refactor Cycle

```
1. RED: Write failing test
   - Test doesn't pass
   - Code doesn't exist

2. GREEN: Write minimal code to pass
   - Just enough to pass test
   - May not be perfect

3. REFACTOR: Improve code
   - Clean up
   - Optimize
   - Keep tests passing
```

### Writing Tests First

```python
# Step 1: Write failing test (RED)
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

# Step 2: Write minimal code (GREEN)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Step 3: Refactor (REFACTOR)
def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Verify tests still pass
# pytest test_fibonacci.py
```

### TDD Example

```python
# Test file (write first)
def test_user_creation():
    user = User(name='Alice', email='alice@example.com')
    assert user.name == 'Alice'
    assert user.email == 'alice@example.com'

def test_user_validation():
    with pytest.raises(ValueError):
        User(name='', email='alice@example.com')
    
    with pytest.raises(ValueError):
        User(name='Alice', email='invalid-email')

def test_user_save():
    user = User(name='Alice', email='alice@example.com')
    user_id = user.save()
    assert user_id is not None
    
    loaded = User.load(user_id)
    assert loaded.name == 'Alice'

# Implementation (write to pass tests)
class User:
    def __init__(self, name, email):
        if not name:
            raise ValueError("Name required")
        if '@' not in email:
            raise ValueError("Invalid email")
        self.name = name
        self.email = email
    
    def save(self):
        # Save to database
        return 1
    
    @staticmethod
    def load(user_id):
        # Load from database
        return User("Alice", "alice@example.com")
```

---

## Practical Examples

### Complete Test Suite

```python
# src/calculator.py
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# tests/test_calculator.py
import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

class TestCalculator:
    def test_add(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
    
    def test_subtract(self, calc):
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(0, 5) == -5
    
    def test_multiply(self, calc):
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(0, 5) == 0
    
    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5
        assert calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError):
            calc.divide(10, 0)

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (1, 1, 2),
    (0, 0, 0),
])
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected
```

### API Testing Example

```python
# tests/test_api.py
import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

class TestUserAPI:
    def test_create_user(self, client):
        response = client.post('/api/users', json={
            'name': 'Alice',
            'email': 'alice@example.com'
        })
        assert response.status_code == 201
        assert response.json['name'] == 'Alice'
    
    def test_get_users(self, client):
        # Create some users first
        client.post('/api/users', json={'name': 'Alice', 'email': 'alice@example.com'})
        client.post('/api/users', json={'name': 'Bob', 'email': 'bob@example.com'})
        
        response = client.get('/api/users')
        assert response.status_code == 200
        assert len(response.json) == 2
    
    def test_get_user_by_id(self, client):
        # Create user
        create_response = client.post('/api/users', json={
            'name': 'Alice',
            'email': 'alice@example.com'
        })
        user_id = create_response.json['id']
        
        # Get user
        response = client.get(f'/api/users/{user_id}')
        assert response.status_code == 200
        assert response.json['name'] == 'Alice'
    
    def test_update_user(self, client):
        # Create user
        create_response = client.post('/api/users', json={
            'name': 'Alice',
            'email': 'alice@example.com'
        })
        user_id = create_response.json['id']
        
        # Update user
        response = client.put(f'/api/users/{user_id}', json={
            'name': 'Alice Updated'
        })
        assert response.status_code == 200
        assert response.json['name'] == 'Alice Updated'
    
    def test_delete_user(self, client):
        # Create user
        create_response = client.post('/api/users', json={
            'name': 'Alice',
            'email': 'alice@example.com'
        })
        user_id = create_response.json['id']
        
        # Delete user
        response = client.delete(f'/api/users/{user_id}')
        assert response.status_code == 204
        
        # Verify deleted
        response = client.get(f'/api/users/{user_id}')
        assert response.status_code == 404
```

---

## Best Practices

### Testing

```
✓ Write tests first (TDD)
✓ Test edge cases
✓ Use descriptive names
✓ One assertion per test (ideally)
✓ Don't test implementation details
✓ Mock external dependencies
✓ Aim for high coverage
✓ Keep tests simple
✓ Run tests frequently
✓ Use fixtures for setup
```

### Coverage

```
✓ Aim for 80%+ coverage
✓ Focus on critical paths
✓ Don't aim for 100% blindly
✓ Monitor coverage trends
✓ Exclude generated code
✓ Test edge cases
```

### Mocking

```
✓ Mock external dependencies
✓ Don't over-mock
✓ Keep mocks simple
✓ Use patch correctly
✓ Verify mock calls
✓ Test real behavior with integration tests
```

---

## Practice Exercises

### 1. Unit Testing
- Write unit tests for functions
- Test edge cases
- Use assertions

### 2. pytest
- Convert unittest to pytest
- Use fixtures
- Parametrize tests

### 3. Mocking
- Mock external services
- Mock database
- Verify calls

### 4. Coverage
- Measure code coverage
- Generate reports
- Improve coverage

### 5. API Testing
- Test endpoints
- Test error cases
- Integration tests

### 6. TDD
- Write tests first
- Implement to pass
- Refactor

---

# End of Notes
