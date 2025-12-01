"""
EXERCISES: pytest Basics
========================
Complete all 5 exercises below
"""

import pytest

# ========== EXERCISE 1: BASIC TESTS ==========
print("Exercise 1: Write Basic Tests")
print("-" * 40)

# TODO: Write tests for this function
def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignoring case and spaces)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# Write at least 3 test cases:
# 1. Test with a simple palindrome like "radar"
# 2. Test with a sentence palindrome like "A man a plan a canal Panama"
# 3. Test with a non-palindrome

# Your tests here:



# ========== EXERCISE 2: TESTING EXCEPTIONS ==========
print("\n\nExercise 2: Testing Exceptions")
print("-" * 40)

# TODO: Write tests for this function that test exception handling
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# Write tests for:
# 1. Normal division
# 2. Division by zero should raise ZeroDivisionError
# 3. Verify the error message

# Your tests here:



# ========== EXERCISE 3: FIXTURES ==========
print("\n\nExercise 3: Using Fixtures")
print("-" * 40)

# TODO: Create a fixture and use it in tests
class BankAccount:
    """Simple bank account class."""
    
    def __init__(self, initial_balance: float = 0):
        self.balance = initial_balance
    
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


# Create a fixture that provides a BankAccount with $100
# Then write tests for:
# 1. Depositing money
# 2. Withdrawing money
# 3. Withdrawing more than balance (should raise error)

# Your fixture and tests here:



# ========== EXERCISE 4: PARAMETRIZED TESTS ==========
print("\n\nExercise 4: Parametrized Tests")
print("-" * 40)

# TODO: Write parametrized tests for this function
def grade_score(score: int) -> str:
    """Convert numeric score to letter grade."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


# Write parametrized tests to test:
# - Score 95 -> "A"
# - Score 85 -> "B"
# - Score 75 -> "C"
# - Score 65 -> "D"
# - Score 55 -> "F"
# - Boundary cases (90, 80, 70, 60)
# - Invalid scores (-1, 101)

# Your parametrized tests here:



# ========== EXERCISE 5: TEST CLASS ==========
print("\n\nExercise 5: Organize Tests in a Class")
print("-" * 40)

# TODO: Create a test class for this ShoppingCart
class ShoppingCart:
    """Shopping cart implementation."""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name: str, price: float, quantity: int = 1):
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
        self.items = [item for item in self.items if item["name"] != name]
    
    def get_total(self) -> float:
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def get_item_count(self) -> int:
        return sum(item["quantity"] for item in self.items)
    
    def clear(self):
        self.items = []


# Create a TestShoppingCart class with:
# 1. A fixture for an empty cart
# 2. A fixture for a cart with items
# 3. Tests for all methods
# 4. Edge case tests

# Your test class here:



"""
Run your tests with: pytest 01_pytest_exercises.py -v
"""
