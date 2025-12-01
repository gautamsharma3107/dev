"""
Day 20 - Unit Testing with pytest
=================================
Learn: pytest basics, writing tests, assertions, fixtures

Key Concepts:
- pytest is Python's most popular testing framework
- Tests help catch bugs early and ensure code quality
- Good tests are fast, isolated, and reliable
"""

# ========== WHAT IS TESTING? ==========
print("=" * 60)
print("INTRODUCTION TO TESTING")
print("=" * 60)

"""
Why Testing is Important:
1. Catches bugs before production
2. Documents expected behavior
3. Makes refactoring safer
4. Improves code design
5. Saves time in the long run
"""

# ========== BASIC TEST STRUCTURE ==========
print("\n" + "=" * 60)
print("BASIC TEST STRUCTURE")
print("=" * 60)

# First, let's write a simple function to test
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Now let's write tests for these functions
# In pytest, test functions must start with 'test_'

def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0


def test_add_zeros():
    """Test adding zeros."""
    assert add(0, 0) == 0
    assert add(5, 0) == 5


def test_subtract():
    """Test subtraction."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


def test_multiply():
    """Test multiplication."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


# ========== TESTING EXCEPTIONS ==========
print("\n" + "=" * 60)
print("TESTING EXCEPTIONS")
print("=" * 60)

# pytest provides a clean way to test exceptions
import pytest


def test_divide_by_zero():
    """Test that dividing by zero raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)


def test_divide_normal():
    """Test normal division."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


# ========== ASSERTIONS IN PYTEST ==========
print("\n" + "=" * 60)
print("COMMON ASSERTIONS")
print("=" * 60)

"""
Pytest uses plain Python assert statements:

assert x == y          # Equality
assert x != y          # Inequality
assert x               # Truthiness
assert not x           # Falsiness
assert x in collection # Membership
assert x is y          # Identity
assert x is None       # None check
"""


def test_various_assertions():
    """Demonstrate various assertion types."""
    # Equality
    assert 1 + 1 == 2
    
    # Inequality
    assert "hello" != "world"
    
    # Truthiness
    assert [1, 2, 3]  # Non-empty list is truthy
    
    # Falsiness
    assert not []  # Empty list is falsy
    
    # Membership
    assert 3 in [1, 2, 3]
    assert "a" in "abc"
    
    # Type checking
    assert isinstance([1, 2], list)
    
    # None check
    assert None is None


# ========== FIXTURES ==========
print("\n" + "=" * 60)
print("FIXTURES - SETUP AND TEARDOWN")
print("=" * 60)

"""
Fixtures provide a way to:
1. Set up test data
2. Create test objects
3. Handle setup/teardown
4. Share resources across tests
"""


@pytest.fixture
def sample_list():
    """Fixture that provides a sample list for testing."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_dict():
    """Fixture that provides a sample dictionary."""
    return {"name": "John", "age": 30, "city": "NYC"}


def test_list_operations(sample_list):
    """Test list operations using fixture."""
    assert len(sample_list) == 5
    assert sum(sample_list) == 15
    assert 3 in sample_list


def test_dict_operations(sample_dict):
    """Test dictionary operations using fixture."""
    assert sample_dict["name"] == "John"
    assert "age" in sample_dict
    assert len(sample_dict) == 3


# Fixture with setup and teardown
@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Hello, World!")
    yield file_path
    # Cleanup happens automatically with tmp_path


def test_read_file(temp_file):
    """Test reading from temporary file."""
    content = temp_file.read_text()
    assert content == "Hello, World!"


# ========== PARAMETRIZED TESTS ==========
print("\n" + "=" * 60)
print("PARAMETRIZED TESTS")
print("=" * 60)

"""
Parametrized tests run the same test with different inputs.
This reduces code duplication and improves test coverage.
"""


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    """Test add function with multiple inputs."""
    assert add(a, b) == expected


@pytest.mark.parametrize("input_list,expected_sum", [
    ([1, 2, 3], 6),
    ([], 0),
    ([10], 10),
    ([-1, 1], 0),
])
def test_sum_parametrized(input_list, expected_sum):
    """Test sum function with multiple inputs."""
    assert sum(input_list) == expected_sum


# ========== TEST MARKERS ==========
print("\n" + "=" * 60)
print("TEST MARKERS")
print("=" * 60)

"""
Markers allow you to categorize and filter tests:
- skip: Skip a test
- skipif: Skip conditionally
- xfail: Expected to fail
- Custom markers for categorization
"""

import sys


@pytest.mark.skip(reason="Feature not implemented yet")
def test_unimplemented_feature():
    """This test will be skipped."""
    pass


@pytest.mark.skipif(sys.platform == "win32", reason="Unix only")
def test_unix_specific():
    """This test runs only on Unix systems."""
    assert True


@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug():
    """This test is expected to fail."""
    assert 1 == 2  # Known issue


# Custom marker (requires pytest.ini configuration)
@pytest.mark.slow
def test_slow_operation():
    """Mark test as slow for filtering."""
    import time
    time.sleep(0.1)
    assert True


# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: SHOPPING CART")
print("=" * 60)


class ShoppingCart:
    """A simple shopping cart class to demonstrate testing."""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name: str, price: float, quantity: int = 1):
        """Add an item to the cart."""
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
    
    def remove_item(self, name: str):
        """Remove an item from the cart."""
        self.items = [item for item in self.items if item["name"] != name]
    
    def get_total(self) -> float:
        """Calculate total price of all items."""
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def get_item_count(self) -> int:
        """Get total number of items."""
        return sum(item["quantity"] for item in self.items)
    
    def clear(self):
        """Remove all items from the cart."""
        self.items = []


# Fixture for ShoppingCart
@pytest.fixture
def cart():
    """Provide a fresh shopping cart for each test."""
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    """Provide a cart with some items already added."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, 3)
    cart.add_item("Banana", 0.75, 5)
    return cart


# Tests for ShoppingCart
class TestShoppingCart:
    """Group related tests in a class."""
    
    def test_empty_cart(self, cart):
        """Test that new cart is empty."""
        assert cart.get_item_count() == 0
        assert cart.get_total() == 0
    
    def test_add_single_item(self, cart):
        """Test adding a single item."""
        cart.add_item("Apple", 1.50)
        assert cart.get_item_count() == 1
        assert cart.get_total() == 1.50
    
    def test_add_multiple_items(self, cart):
        """Test adding multiple items."""
        cart.add_item("Apple", 1.50, 2)
        cart.add_item("Banana", 0.75, 3)
        assert cart.get_item_count() == 5
        assert cart.get_total() == pytest.approx(5.25)
    
    def test_remove_item(self, cart_with_items):
        """Test removing an item."""
        cart_with_items.remove_item("Apple")
        assert cart_with_items.get_total() == pytest.approx(3.75)
    
    def test_clear_cart(self, cart_with_items):
        """Test clearing the cart."""
        cart_with_items.clear()
        assert cart_with_items.get_item_count() == 0
    
    def test_negative_price_raises_error(self, cart):
        """Test that negative price raises ValueError."""
        with pytest.raises(ValueError) as excinfo:
            cart.add_item("Invalid", -5.00)
        assert "Price cannot be negative" in str(excinfo.value)
    
    def test_zero_quantity_raises_error(self, cart):
        """Test that zero quantity raises ValueError."""
        with pytest.raises(ValueError) as excinfo:
            cart.add_item("Invalid", 5.00, 0)
        assert "Quantity must be at least 1" in str(excinfo.value)


# ========== RUNNING TESTS ==========
print("\n" + "=" * 60)
print("RUNNING TESTS")
print("=" * 60)

"""
To run these tests, save this file and use these commands:

# Run all tests in this file
pytest 01_pytest_basics.py -v

# Run specific test class
pytest 01_pytest_basics.py::TestShoppingCart -v

# Run specific test
pytest 01_pytest_basics.py::test_add_positive_numbers -v

# Run with coverage
pytest 01_pytest_basics.py --cov=. --cov-report=term-missing

# Run only slow tests
pytest 01_pytest_basics.py -m slow

# Run excluding slow tests
pytest 01_pytest_basics.py -m "not slow"
"""

print("\n" + "=" * 60)
print("✅ pytest Basics - Complete!")
print("=" * 60)
print("\nRun: pytest 01_pytest_basics.py -v")
