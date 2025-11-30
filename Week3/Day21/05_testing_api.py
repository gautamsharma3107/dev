"""
Day 21 - API Testing
====================
Learn: Testing FastAPI applications with pytest

Key Concepts:
- Unit testing with pytest
- Testing FastAPI with TestClient
- Testing authentication
- Test fixtures and setup
- Coverage reports
"""

# ========== TESTING OVERVIEW ==========
print("=" * 60)
print("API TESTING")
print("=" * 60)

testing_overview = """
Why Test APIs?
- Ensure endpoints work correctly
- Catch bugs early
- Document expected behavior
- Enable confident refactoring
- Prevent regressions

Testing Tools:
- pytest: Testing framework
- TestClient: FastAPI testing client
- pytest-cov: Coverage reports
- httpx: Async testing
"""
print(testing_overview)

# ========== SETUP ==========
print("\n1. TESTING SETUP")
print("-" * 40)

setup_code = '''
# Install testing dependencies
# pip install pytest httpx pytest-cov

# Project structure for tests:
# my_api/
# ├── main.py
# ├── tests/
# │   ├── __init__.py
# │   ├── conftest.py        # Shared fixtures
# │   ├── test_main.py       # General tests
# │   ├── test_users.py      # User endpoint tests
# │   └── test_items.py      # Item endpoint tests
# └── requirements.txt

# conftest.py - Shared fixtures
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db
from database import Base

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    """Create test database for each test"""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(db):
    """Create test client with test database"""
    def override_get_db():
        yield db
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
'''
print(setup_code)

# ========== BASIC TESTS ==========
print("\n2. BASIC ENDPOINT TESTS")
print("-" * 40)

basic_tests = '''
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the API"

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
'''
print(basic_tests)

# ========== CRUD TESTS ==========
print("\n3. CRUD OPERATION TESTS")
print("-" * 40)

crud_tests = '''
# test_items.py
import pytest
from fastapi.testclient import TestClient

# Test CREATE
def test_create_item(client):
    """Test creating a new item"""
    response = client.post(
        "/items/",
        json={"name": "Test Item", "price": 10.99, "description": "A test item"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 10.99
    assert "id" in data

def test_create_item_invalid(client):
    """Test creating item with invalid data"""
    response = client.post(
        "/items/",
        json={"name": "", "price": -5}  # Invalid: empty name, negative price
    )
    assert response.status_code == 422  # Validation error

# Test READ
def test_get_items(client):
    """Test getting all items"""
    # Create some items first
    client.post("/items/", json={"name": "Item 1", "price": 10.0})
    client.post("/items/", json={"name": "Item 2", "price": 20.0})
    
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2

def test_get_item(client):
    """Test getting a single item"""
    # Create item
    create_response = client.post(
        "/items/",
        json={"name": "Test Item", "price": 15.0}
    )
    item_id = create_response.json()["id"]
    
    # Get item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_get_item_not_found(client):
    """Test getting non-existent item"""
    response = client.get("/items/99999")
    assert response.status_code == 404

# Test UPDATE
def test_update_item(client):
    """Test updating an item"""
    # Create item
    create_response = client.post(
        "/items/",
        json={"name": "Original", "price": 10.0}
    )
    item_id = create_response.json()["id"]
    
    # Update item
    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated", "price": 20.0}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"
    assert response.json()["price"] == 20.0

def test_patch_item(client):
    """Test partial update"""
    # Create item
    create_response = client.post(
        "/items/",
        json={"name": "Original", "price": 10.0}
    )
    item_id = create_response.json()["id"]
    
    # Patch item (only update price)
    response = client.patch(
        f"/items/{item_id}",
        json={"price": 25.0}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Original"  # Unchanged
    assert response.json()["price"] == 25.0  # Updated

# Test DELETE
def test_delete_item(client):
    """Test deleting an item"""
    # Create item
    create_response = client.post(
        "/items/",
        json={"name": "To Delete", "price": 10.0}
    )
    item_id = create_response.json()["id"]
    
    # Delete item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204
    
    # Verify deleted
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404
'''
print(crud_tests)

# ========== AUTHENTICATION TESTS ==========
print("\n4. AUTHENTICATION TESTS")
print("-" * 40)

auth_tests = '''
# test_auth.py
import pytest
from fastapi.testclient import TestClient

def test_register(client):
    """Test user registration"""
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepassword123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert "password" not in data  # Password should not be returned

def test_register_duplicate_email(client):
    """Test registration with existing email"""
    # First registration
    client.post(
        "/auth/register",
        json={
            "username": "user1",
            "email": "same@example.com",
            "password": "password123"
        }
    )
    
    # Second registration with same email
    response = client.post(
        "/auth/register",
        json={
            "username": "user2",
            "email": "same@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"]

def test_login(client):
    """Test user login"""
    # Register user
    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "password123"
        }
    )
    
    # Login
    response = client.post(
        "/auth/login",
        data={"username": "login@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client):
    """Test login with wrong password"""
    response = client.post(
        "/auth/login",
        data={"username": "wrong@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_protected_route(client):
    """Test accessing protected route with token"""
    # Register and login
    client.post(
        "/auth/register",
        json={
            "username": "protecteduser",
            "email": "protected@example.com",
            "password": "password123"
        }
    )
    login_response = client.post(
        "/auth/login",
        data={"username": "protected@example.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    
    # Access protected route
    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "protected@example.com"

def test_protected_route_no_token(client):
    """Test accessing protected route without token"""
    response = client.get("/auth/me")
    assert response.status_code == 401
'''
print(auth_tests)

# ========== TEST FIXTURES ==========
print("\n5. ADVANCED TEST FIXTURES")
print("-" * 40)

fixtures_code = '''
# conftest.py - Advanced fixtures
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def auth_headers(client):
    """Fixture to get auth headers for authenticated requests"""
    # Register user
    client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
    )
    
    # Login and get token
    response = client.post(
        "/auth/login",
        data={"username": "test@example.com", "password": "password123"}
    )
    token = response.json()["access_token"]
    
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def sample_items(client, auth_headers):
    """Fixture to create sample items"""
    items = []
    for i in range(5):
        response = client.post(
            "/items/",
            json={"name": f"Item {i}", "price": 10.0 * (i + 1)},
            headers=auth_headers
        )
        items.append(response.json())
    return items

# Using fixtures in tests
def test_get_my_items(client, auth_headers, sample_items):
    """Test getting user's items"""
    response = client.get("/items/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == len(sample_items)
'''
print(fixtures_code)

# ========== RUNNING TESTS ==========
print("\n6. RUNNING TESTS")
print("-" * 40)

run_tests = """
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_items.py

# Run specific test function
pytest tests/test_items.py::test_create_item

# Run tests matching pattern
pytest -k "create"

# Run with coverage report
pytest --cov=. --cov-report=html

# Run with coverage and show missing lines
pytest --cov=. --cov-report=term-missing

# Run tests in parallel (requires pytest-xdist)
pytest -n auto

# Stop on first failure
pytest -x
"""
print(run_tests)

# ========== COMPLETE TEST FILE ==========
print("\n" + "=" * 60)
print("COMPLETE TEST FILE EXAMPLE")
print("=" * 60)

complete_tests = '''
# test_api.py - Complete test file

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ==================== FIXTURE ====================
@pytest.fixture
def test_user():
    """Create a test user and return credentials"""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123"
    }
    client.post("/auth/register", json=user_data)
    return user_data

@pytest.fixture
def auth_token(test_user):
    """Login and return auth token"""
    response = client.post(
        "/auth/login",
        data={"username": test_user["email"], "password": test_user["password"]}
    )
    return response.json()["access_token"]

@pytest.fixture
def auth_headers(auth_token):
    """Return authorization headers"""
    return {"Authorization": f"Bearer {auth_token}"}

# ==================== ROOT TESTS ====================
def test_root():
    response = client.get("/")
    assert response.status_code == 200

# ==================== AUTH TESTS ====================
class TestAuth:
    def test_register_success(self):
        response = client.post(
            "/auth/register",
            json={
                "username": "newuser",
                "email": "new@example.com",
                "password": "password123"
            }
        )
        assert response.status_code == 201
    
    def test_login_success(self, test_user):
        response = client.post(
            "/auth/login",
            data={"username": test_user["email"], "password": test_user["password"]}
        )
        assert response.status_code == 200
        assert "access_token" in response.json()
    
    def test_get_me(self, auth_headers):
        response = client.get("/auth/me", headers=auth_headers)
        assert response.status_code == 200

# ==================== ITEM TESTS ====================
class TestItems:
    def test_create_item(self, auth_headers):
        response = client.post(
            "/items/",
            json={"name": "Test Item", "price": 10.99},
            headers=auth_headers
        )
        assert response.status_code == 201
        assert response.json()["name"] == "Test Item"
    
    def test_get_items(self, auth_headers):
        response = client.get("/items/", headers=auth_headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_update_item(self, auth_headers):
        # Create
        create_res = client.post(
            "/items/",
            json={"name": "Original", "price": 10.0},
            headers=auth_headers
        )
        item_id = create_res.json()["id"]
        
        # Update
        response = client.put(
            f"/items/{item_id}",
            json={"name": "Updated", "price": 20.0},
            headers=auth_headers
        )
        assert response.status_code == 200
        assert response.json()["name"] == "Updated"
    
    def test_delete_item(self, auth_headers):
        # Create
        create_res = client.post(
            "/items/",
            json={"name": "To Delete", "price": 10.0},
            headers=auth_headers
        )
        item_id = create_res.json()["id"]
        
        # Delete
        response = client.delete(f"/items/{item_id}", headers=auth_headers)
        assert response.status_code == 204
'''
print(complete_tests)

print("\n" + "=" * 60)
print("✅ API Testing - Complete!")
print("=" * 60)
print("\nNow complete the Day 21 assessment!")
