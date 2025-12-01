"""
EXERCISES: API Testing
======================
Complete all 5 exercises below
"""

import pytest
from unittest.mock import Mock, patch
from typing import Dict, List, Optional
from dataclasses import dataclass


# ========== EXERCISE 1: TEST A REST API CLIENT ==========
print("Exercise 1: Test a REST API Client")
print("-" * 40)

# Here's an API client that fetches user data
class UserAPIClient:
    """Client for user API."""
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
    
    def get_user(self, user_id: int) -> Dict:
        """Get user by ID."""
        import requests
        response = requests.get(
            f"{self.base_url}/users/{user_id}",
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        if response.status_code == 404:
            raise ValueError(f"User {user_id} not found")
        if response.status_code != 200:
            raise RuntimeError("API error")
        return response.json()
    
    def create_user(self, username: str, email: str) -> Dict:
        """Create a new user."""
        import requests
        response = requests.post(
            f"{self.base_url}/users",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"username": username, "email": email}
        )
        if response.status_code == 400:
            raise ValueError("Invalid user data")
        if response.status_code != 201:
            raise RuntimeError("API error")
        return response.json()


# TODO: Write tests using mocking
# 1. Test get_user success - mock the response
# 2. Test get_user not found (404)
# 3. Test create_user success
# 4. Test create_user validation error (400)

# Your tests here:



# ========== EXERCISE 2: TEST CRUD OPERATIONS ==========
print("\n\nExercise 2: Test CRUD Operations")
print("-" * 40)


@dataclass
class Product:
    id: Optional[int]
    name: str
    price: float
    stock: int


class ProductStore:
    """In-memory product store."""
    
    def __init__(self):
        self._products: Dict[int, Product] = {}
        self._next_id = 1
    
    def create(self, name: str, price: float, stock: int) -> Product:
        if not name:
            raise ValueError("Name is required")
        if price < 0:
            raise ValueError("Price must be positive")
        
        product = Product(
            id=self._next_id,
            name=name,
            price=price,
            stock=stock
        )
        self._products[self._next_id] = product
        self._next_id += 1
        return product
    
    def read(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)
    
    def update(self, product_id: int, **kwargs) -> Optional[Product]:
        product = self._products.get(product_id)
        if not product:
            return None
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        return product
    
    def delete(self, product_id: int) -> bool:
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False
    
    def list_all(self) -> List[Product]:
        return list(self._products.values())


# TODO: Write comprehensive CRUD tests
# 1. Test create - valid and invalid inputs
# 2. Test read - existing and non-existing
# 3. Test update - update fields, non-existing product
# 4. Test delete - existing and non-existing
# 5. Test list_all - empty and with products

# Your tests here:



# ========== EXERCISE 3: TEST AUTHENTICATION FLOW ==========
print("\n\nExercise 3: Test Authentication Flow")
print("-" * 40)


class AuthService:
    """Authentication service."""
    
    def __init__(self):
        self._users = {
            "admin": {"password": "admin123", "role": "admin"},
            "user": {"password": "user123", "role": "user"}
        }
        self._tokens = {}
    
    def login(self, username: str, password: str) -> str:
        """Login and return token."""
        if username not in self._users:
            raise ValueError("Invalid username")
        if self._users[username]["password"] != password:
            raise ValueError("Invalid password")
        
        token = f"token_{username}_123"
        self._tokens[token] = {
            "username": username,
            "role": self._users[username]["role"]
        }
        return token
    
    def verify_token(self, token: str) -> Dict:
        """Verify token and return user info."""
        if token not in self._tokens:
            raise ValueError("Invalid token")
        return self._tokens[token]
    
    def logout(self, token: str) -> bool:
        """Invalidate token."""
        if token in self._tokens:
            del self._tokens[token]
            return True
        return False
    
    def check_permission(self, token: str, required_role: str) -> bool:
        """Check if user has required role."""
        user_info = self.verify_token(token)
        return user_info["role"] == required_role


# TODO: Write tests for the auth flow
# 1. Test successful login
# 2. Test login with invalid username
# 3. Test login with invalid password
# 4. Test token verification
# 5. Test logout
# 6. Test permission checking

# Your tests here:



# ========== EXERCISE 4: TEST ERROR HANDLING ==========
print("\n\nExercise 4: Test Error Handling")
print("-" * 40)


class OrderService:
    """Order service with error handling."""
    
    def __init__(self, product_store: ProductStore):
        self._store = product_store
        self._orders = []
    
    def create_order(self, product_id: int, quantity: int) -> Dict:
        """Create an order."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        
        product = self._store.read(product_id)
        if not product:
            raise ValueError(f"Product {product_id} not found")
        
        if product.stock < quantity:
            raise ValueError("Insufficient stock")
        
        # Update stock
        self._store.update(product_id, stock=product.stock - quantity)
        
        order = {
            "id": len(self._orders) + 1,
            "product_id": product_id,
            "quantity": quantity,
            "total": product.price * quantity
        }
        self._orders.append(order)
        return order


# TODO: Write tests for all error scenarios
# 1. Successful order creation
# 2. Invalid quantity (0 or negative)
# 3. Product not found
# 4. Insufficient stock
# 5. Verify stock is updated after order

# Your tests here:



# ========== EXERCISE 5: INTEGRATION TEST ==========
print("\n\nExercise 5: Integration Test")
print("-" * 40)

# TODO: Write an integration test that tests the full flow:
# 1. Create products
# 2. List products
# 3. Create orders
# 4. Verify stock updates
# 5. Handle errors gracefully

# Your integration test here:



"""
Run your tests with: pytest 02_api_testing_exercises.py -v
"""
