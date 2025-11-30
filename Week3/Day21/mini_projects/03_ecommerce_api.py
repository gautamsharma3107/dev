"""
MINI PROJECT: E-commerce API
============================
Build a complete REST API for an e-commerce platform

Features to implement:
1. User registration and authentication
2. Products (CRUD)
3. Categories (CRUD)
4. Shopping Cart
5. Orders

Requirements:
- FastAPI or Django REST Framework
- SQLAlchemy for database
- JWT authentication
- At least 5 unit tests
"""

# ============================================================
# PROJECT STRUCTURE
# ============================================================

project_structure = """
ecommerce_api/
├── main.py                 # Application entry point
├── config.py               # Configuration
├── database.py             # Database setup
├── models/
│   ├── __init__.py
│   ├── user.py            # User model
│   ├── product.py         # Product model
│   ├── category.py        # Category model
│   ├── cart.py            # Cart model
│   └── order.py           # Order model
├── schemas/
│   ├── __init__.py
│   ├── user.py            # User schemas
│   ├── product.py         # Product schemas
│   ├── category.py        # Category schemas
│   ├── cart.py            # Cart schemas
│   └── order.py           # Order schemas
├── routers/
│   ├── __init__.py
│   ├── auth.py            # Auth routes
│   ├── products.py        # Product routes
│   ├── categories.py      # Category routes
│   ├── cart.py            # Cart routes
│   └── orders.py          # Order routes
├── services/
│   ├── __init__.py
│   ├── auth.py            # Auth service
│   └── cart.py            # Cart service
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_products.py
│   └── test_orders.py
└── requirements.txt
"""
print(project_structure)

# ============================================================
# STARTER CODE
# ============================================================

print("=" * 60)
print("STARTER CODE")
print("=" * 60)

# Database models
models_code = '''
# models/user.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    # Relationships
    cart = relationship("Cart", back_populates="user", uselist=False)
    orders = relationship("Order", back_populates="user")

# models/category.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    
    # Relationships
    products = relationship("Product", back_populates="category")

# models/product.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    
    # Relationships
    category = relationship("Category", back_populates="products")

# models/cart.py
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Association table for Cart and Products
# Note: For columns with extra data like quantity, consider using an Association Object pattern
cart_items = Table(
    "cart_items",
    Base.metadata,
    Column("cart_id", Integer, ForeignKey("carts.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("quantity", Integer, nullable=False)  # Set quantity when inserting
)

class Cart(Base):
    __tablename__ = "carts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Relationships
    user = relationship("User", back_populates="cart")
    items = relationship("Product", secondary=cart_items)

# models/order.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Enum, Table
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

class OrderStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

order_items = Table(
    "order_items",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("quantity", Integer),
    Column("price", Float)
)

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Float)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="orders")
    items = relationship("Product", secondary=order_items)
'''
print(models_code)

# API Endpoints to implement
print("\n" + "=" * 60)
print("ENDPOINTS TO IMPLEMENT")
print("=" * 60)

endpoints = """
Authentication:
- POST /auth/register    - Register new user
- POST /auth/login       - Login and get token
- GET  /auth/me          - Get current user

Products:
- GET    /products/              - List all products (public)
- GET    /products/{id}          - Get product details
- POST   /products/              - Create product (admin only)
- PUT    /products/{id}          - Update product (admin only)
- DELETE /products/{id}          - Delete product (admin only)
- GET    /products/search?q=...  - Search products

Categories:
- GET    /categories/            - List all categories
- GET    /categories/{id}        - Get category with products
- POST   /categories/            - Create category (admin only)

Cart:
- GET    /cart/                  - Get user's cart
- POST   /cart/items             - Add item to cart
- PUT    /cart/items/{id}        - Update item quantity
- DELETE /cart/items/{id}        - Remove item from cart
- DELETE /cart/                  - Clear cart

Orders:
- POST   /orders/                - Create order from cart
- GET    /orders/                - Get user's orders
- GET    /orders/{id}            - Get order details
- PATCH  /orders/{id}/status     - Update order status (admin only)
"""
print(endpoints)

# Tests to write
print("\n" + "=" * 60)
print("TESTS TO WRITE")
print("=" * 60)

tests = """
Required Tests (minimum 5):
1. test_list_products - Test listing products
2. test_add_to_cart - Test adding product to cart
3. test_create_order - Test creating order from cart
4. test_admin_create_product - Test admin creating product
5. test_search_products - Test product search

Bonus Tests:
- test_update_cart_quantity
- test_remove_from_cart
- test_order_status_flow
- test_category_products
- test_stock_management
"""
print(tests)

# Grading rubric
print("\n" + "=" * 60)
print("GRADING RUBRIC")
print("=" * 60)

rubric = """
Functionality (40 points):
- User auth working (8)
- Products CRUD working (10)
- Categories working (5)
- Cart operations working (10)
- Orders working (7)

Code Quality (20 points):
- Clean code structure (10)
- Proper use of Pydantic (5)
- Proper use of SQLAlchemy (5)

Best Practices (20 points):
- Separation of concerns (5)
- Input validation (5)
- Proper HTTP status codes (5)
- Security best practices (5)

Testing (10 points):
- At least 5 tests (5)
- Tests cover main flows (5)

Documentation (10 points):
- API docs accessible (5)
- README with setup instructions (5)

Total: 100 points
Pass: 70 points
"""
print(rubric)

print("\n" + "=" * 60)
print("Good luck building your E-commerce API! 🚀")
print("=" * 60)
