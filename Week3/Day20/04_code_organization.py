"""
Day 20 - Code Organization Best Practices
==========================================
Learn: Project structure, modules, packages, clean code

Key Concepts:
- Organizing Python projects effectively
- Using modules and packages
- Writing maintainable code
- Following Python conventions
"""

import os
from typing import List, Dict, Any, Optional, Protocol
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

# ========== PROJECT STRUCTURE ==========
print("=" * 60)
print("PROJECT STRUCTURE BEST PRACTICES")
print("=" * 60)

"""
Recommended Python Project Structure:

my_project/
├── src/                      # Source code
│   └── my_project/
│       ├── __init__.py       # Package marker
│       ├── main.py           # Entry point
│       ├── config.py         # Configuration
│       ├── models/           # Data models
│       │   ├── __init__.py
│       │   └── user.py
│       ├── services/         # Business logic
│       │   ├── __init__.py
│       │   └── user_service.py
│       ├── repositories/     # Data access
│       │   ├── __init__.py
│       │   └── user_repo.py
│       ├── api/              # API endpoints
│       │   ├── __init__.py
│       │   └── routes.py
│       └── utils/            # Utilities
│           ├── __init__.py
│           └── helpers.py
├── tests/                    # Test files
│   ├── __init__.py
│   ├── conftest.py           # Shared fixtures
│   ├── unit/
│   │   └── test_services.py
│   └── integration/
│       └── test_api.py
├── docs/                     # Documentation
│   └── api.md
├── scripts/                  # Utility scripts
│   └── setup_db.py
├── .env.example              # Environment template
├── .gitignore
├── pyproject.toml            # Project config
├── requirements.txt          # Dependencies
├── README.md
└── Makefile                  # Common commands
"""


# ========== SEPARATION OF CONCERNS ==========
print("\n" + "=" * 60)
print("SEPARATION OF CONCERNS")
print("=" * 60)

"""
Layered Architecture:
1. Presentation Layer (API/UI)
2. Business Logic Layer (Services)
3. Data Access Layer (Repositories)
4. Data Layer (Models/Entities)

Benefits:
- Easier to test each layer
- Changes in one layer don't affect others
- Clear responsibilities
"""


# Example: Layered Architecture

# Layer 1: Models (Data structures)
@dataclass
class User:
    """User entity - represents data structure."""
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    password_hash: str = ""
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)


class UserStatus(Enum):
    """User status enumeration."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


# Layer 2: Repository (Data access)
class UserRepositoryInterface(Protocol):
    """Interface for user repository."""
    
    def get_by_id(self, user_id: int) -> Optional[User]: ...
    def get_by_email(self, email: str) -> Optional[User]: ...
    def save(self, user: User) -> User: ...
    def delete(self, user_id: int) -> bool: ...
    def list_all(self) -> List[User]: ...


class InMemoryUserRepository:
    """In-memory implementation of user repository."""
    
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._next_id = 1
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return self._users.get(user_id)
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    def save(self, user: User) -> User:
        """Save or update user."""
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        self._users[user.id] = user
        return user
    
    def delete(self, user_id: int) -> bool:
        """Delete user."""
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False
    
    def list_all(self) -> List[User]:
        """List all users."""
        return list(self._users.values())


# Layer 3: Services (Business logic)
class UserService:
    """User service - contains business logic."""
    
    def __init__(self, repository: InMemoryUserRepository):
        self._repository = repository
    
    def create_user(self, username: str, email: str, password: str) -> User:
        """Create a new user with validation."""
        # Validate input
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not email or "@" not in email:
            raise ValueError("Invalid email format")
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        # Check for existing user
        existing = self._repository.get_by_email(email)
        if existing:
            raise ValueError("Email already registered")
        
        # Create user
        user = User(
            username=username,
            email=email,
            password_hash=self._hash_password(password)
        )
        
        return self._repository.save(user)
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return self._repository.get_by_id(user_id)
    
    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        """Update user details."""
        user = self._repository.get_by_id(user_id)
        if not user:
            return None
        
        # Update allowed fields
        allowed_fields = {'username', 'email'}
        for key, value in kwargs.items():
            if key in allowed_fields and value:
                setattr(user, key, value)
        
        return self._repository.save(user)
    
    def deactivate_user(self, user_id: int) -> bool:
        """Deactivate user account."""
        user = self._repository.get_by_id(user_id)
        if user:
            user.is_active = False
            self._repository.save(user)
            return True
        return False
    
    def _hash_password(self, password: str) -> str:
        """Hash password (simplified - use bcrypt in production)."""
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()


# ========== DEPENDENCY INJECTION ==========
print("\n" + "=" * 60)
print("DEPENDENCY INJECTION")
print("=" * 60)

"""
Dependency Injection (DI):
- Pass dependencies instead of creating them
- Makes code testable
- Allows swapping implementations
"""


# Without DI (BAD)
class BadUserService:
    def __init__(self):
        self._repository = InMemoryUserRepository()  # Tightly coupled


# With DI (GOOD)
class GoodUserService:
    def __init__(self, repository: InMemoryUserRepository):
        self._repository = repository  # Loosely coupled


# Factory pattern for creating services
class ServiceFactory:
    """Factory for creating services with dependencies."""
    
    @staticmethod
    def create_user_service(use_mock: bool = False) -> UserService:
        """Create UserService with appropriate repository."""
        if use_mock:
            repository = InMemoryUserRepository()
        else:
            # In production, would use real database repository
            repository = InMemoryUserRepository()
        return UserService(repository)


# ========== CONFIGURATION MANAGEMENT ==========
print("\n" + "=" * 60)
print("CONFIGURATION MANAGEMENT")
print("=" * 60)


@dataclass
class DatabaseConfig:
    """Database configuration."""
    host: str = "localhost"
    port: int = 5432
    name: str = "mydb"
    user: str = "postgres"
    password: str = ""


@dataclass
class AppConfig:
    """Application configuration."""
    debug: bool = False
    log_level: str = "INFO"
    secret_key: str = ""
    database: DatabaseConfig = field(default_factory=DatabaseConfig)


class ConfigLoader:
    """Load configuration from environment."""
    
    @staticmethod
    def load() -> AppConfig:
        """Load configuration from environment variables."""
        return AppConfig(
            debug=os.getenv("DEBUG", "false").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            secret_key=os.getenv("SECRET_KEY", "dev-secret"),
            database=DatabaseConfig(
                host=os.getenv("DB_HOST", "localhost"),
                port=int(os.getenv("DB_PORT", "5432")),
                name=os.getenv("DB_NAME", "mydb"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", "")
            )
        )


# ========== SINGLE RESPONSIBILITY PRINCIPLE ==========
print("\n" + "=" * 60)
print("SINGLE RESPONSIBILITY PRINCIPLE")
print("=" * 60)

"""
Each class/function should have ONE responsibility.
If a class does multiple things, split it.
"""


# BAD: Class does too many things
class BadOrderProcessor:
    def process_order(self, order):
        # Validates order
        # Calculates total
        # Processes payment
        # Sends email
        # Updates inventory
        pass  # Too many responsibilities!


# GOOD: Split into focused classes
class OrderValidator:
    """Validates orders."""
    def validate(self, order: Dict) -> bool:
        return bool(order.get("items")) and order.get("total", 0) > 0


class PriceCalculator:
    """Calculates order prices."""
    def calculate_total(self, items: List[Dict]) -> float:
        return sum(item["price"] * item["quantity"] for item in items)


class PaymentProcessor:
    """Processes payments."""
    def process(self, amount: float, payment_info: Dict) -> bool:
        # Process payment logic
        return True


class EmailNotifier:
    """Sends email notifications."""
    def send_order_confirmation(self, email: str, order_id: str):
        # Send email logic
        pass


class InventoryManager:
    """Manages inventory."""
    def update_stock(self, items: List[Dict]):
        # Update inventory logic
        pass


class OrderService:
    """Orchestrates order processing using single-responsibility classes."""
    
    def __init__(
        self,
        validator: OrderValidator,
        calculator: PriceCalculator,
        payment: PaymentProcessor,
        notifier: EmailNotifier,
        inventory: InventoryManager
    ):
        self._validator = validator
        self._calculator = calculator
        self._payment = payment
        self._notifier = notifier
        self._inventory = inventory
    
    def process_order(self, order: Dict) -> bool:
        """Process an order using all services."""
        # Each step has single responsibility
        if not self._validator.validate(order):
            return False
        
        total = self._calculator.calculate_total(order["items"])
        
        if not self._payment.process(total, order["payment"]):
            return False
        
        self._inventory.update_stock(order["items"])
        self._notifier.send_order_confirmation(order["email"], order["id"])
        
        return True


# ========== NAMING CONVENTIONS ==========
print("\n" + "=" * 60)
print("NAMING CONVENTIONS (PEP 8)")
print("=" * 60)

"""
Python Naming Conventions:

1. Variables: lowercase_with_underscores
   user_name, total_count, is_valid

2. Functions: lowercase_with_underscores
   get_user(), calculate_total(), validate_input()

3. Classes: PascalCase
   UserService, DatabaseConnection, OrderProcessor

4. Constants: UPPERCASE_WITH_UNDERSCORES
   MAX_RETRIES, DATABASE_URL, API_KEY

5. Private: prefix with underscore
   _private_method(), _internal_variable

6. Protected: prefix with underscore
   _protected_method()

7. Modules: lowercase_with_underscores
   user_service.py, database_utils.py

8. Packages: lowercase (no underscores)
   mypackage, userservice
"""


# Good naming examples
class UserAccountService:
    """Service for managing user accounts."""
    
    MAX_LOGIN_ATTEMPTS = 3
    DEFAULT_TIMEOUT = 30
    
    def __init__(self):
        self._login_attempts: Dict[str, int] = {}
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate user with username and password."""
        if self._is_locked_out(username):
            return False
        
        is_valid = self._verify_credentials(username, password)
        
        if not is_valid:
            self._record_failed_attempt(username)
        
        return is_valid
    
    def _is_locked_out(self, username: str) -> bool:
        """Check if user is locked out due to failed attempts."""
        attempts = self._login_attempts.get(username, 0)
        return attempts >= self.MAX_LOGIN_ATTEMPTS
    
    def _verify_credentials(self, username: str, password: str) -> bool:
        """Verify user credentials (simplified)."""
        return username == "admin" and password == "admin123"
    
    def _record_failed_attempt(self, username: str):
        """Record a failed login attempt."""
        self._login_attempts[username] = self._login_attempts.get(username, 0) + 1


# ========== DOCUMENTATION ==========
print("\n" + "=" * 60)
print("DOCUMENTATION BEST PRACTICES")
print("=" * 60)

"""
Good documentation includes:
1. Module docstrings
2. Class docstrings
3. Function docstrings
4. Type hints
5. Inline comments (when necessary)
"""


def calculate_compound_interest(
    principal: float,
    rate: float,
    time: int,
    compounds_per_year: int = 12
) -> float:
    """
    Calculate compound interest.
    
    Args:
        principal: The initial investment amount.
        rate: Annual interest rate as decimal (e.g., 0.05 for 5%).
        time: Investment period in years.
        compounds_per_year: Number of times interest compounds per year.
            Defaults to 12 (monthly).
    
    Returns:
        The total amount after compound interest.
    
    Raises:
        ValueError: If principal or rate is negative.
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 2)
        1104.9413355583269
    """
    if principal < 0:
        raise ValueError("Principal cannot be negative")
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    
    # A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    
    return amount


# ========== CODE SMELLS TO AVOID ==========
print("\n" + "=" * 60)
print("CODE SMELLS TO AVOID")
print("=" * 60)

"""
Common Code Smells:

1. Long Functions (>20 lines)
   - Split into smaller functions

2. Deep Nesting (>3 levels)
   - Use early returns
   - Extract methods

3. Magic Numbers
   - Use named constants

4. Duplicate Code
   - Extract to function/class

5. God Classes
   - Split into smaller classes

6. Feature Envy
   - Move logic to appropriate class

7. Comments explaining bad code
   - Rewrite the code instead
"""


# BAD: Deep nesting and magic numbers
def bad_process_order(order):
    if order:
        if order.get("items"):
            if len(order["items"]) > 0:
                if order.get("total", 0) > 0:
                    if order["total"] < 10000:  # Magic number!
                        return True
    return False


# GOOD: Early returns and constants
MAX_ORDER_TOTAL = 10000


def good_process_order(order: Optional[Dict]) -> bool:
    """Process order with clear validation."""
    if not order:
        return False
    
    items = order.get("items", [])
    if not items:
        return False
    
    total = order.get("total", 0)
    if total <= 0:
        return False
    
    if total >= MAX_ORDER_TOTAL:
        return False
    
    return True


# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: ORGANIZED PROJECT")
print("=" * 60)


# models/product.py
@dataclass
class Product:
    """Product entity."""
    id: Optional[int] = None
    name: str = ""
    price: float = 0.0
    stock: int = 0
    category: str = ""


# repositories/product_repository.py
class ProductRepository:
    """Repository for product data access."""
    
    def __init__(self):
        self._products: Dict[int, Product] = {}
        self._next_id = 1
    
    def find_by_id(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)
    
    def find_by_category(self, category: str) -> List[Product]:
        return [p for p in self._products.values() if p.category == category]
    
    def save(self, product: Product) -> Product:
        if product.id is None:
            product.id = self._next_id
            self._next_id += 1
        self._products[product.id] = product
        return product
    
    def delete(self, product_id: int) -> bool:
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False


# services/product_service.py
class ProductService:
    """Service for product business logic."""
    
    def __init__(self, repository: ProductRepository):
        self._repository = repository
    
    def create_product(
        self,
        name: str,
        price: float,
        stock: int,
        category: str
    ) -> Product:
        """Create a new product."""
        self._validate_product_data(name, price, stock)
        
        product = Product(
            name=name,
            price=price,
            stock=stock,
            category=category
        )
        
        return self._repository.save(product)
    
    def update_stock(self, product_id: int, quantity: int) -> Optional[Product]:
        """Update product stock."""
        product = self._repository.find_by_id(product_id)
        if not product:
            return None
        
        new_stock = product.stock + quantity
        if new_stock < 0:
            raise ValueError("Stock cannot be negative")
        
        product.stock = new_stock
        return self._repository.save(product)
    
    def _validate_product_data(self, name: str, price: float, stock: int):
        """Validate product data."""
        if not name or len(name) < 2:
            raise ValueError("Name must be at least 2 characters")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if stock < 0:
            raise ValueError("Stock cannot be negative")


print("\n" + "=" * 60)
print("✅ Code Organization Best Practices - Complete!")
print("=" * 60)
print("\nKey Takeaways:")
print("1. Organize code into layers (models, repositories, services)")
print("2. Use dependency injection for testability")
print("3. Follow naming conventions (PEP 8)")
print("4. Write clear documentation")
print("5. Avoid code smells")
