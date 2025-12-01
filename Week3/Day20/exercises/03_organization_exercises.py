"""
EXERCISES: Code Organization & Error Handling
=============================================
Complete all 5 exercises below
"""

import pytest
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


# ========== EXERCISE 1: CREATE CUSTOM EXCEPTIONS ==========
print("Exercise 1: Create Custom Exceptions")
print("-" * 40)

# TODO: Create a hierarchy of custom exceptions for a library system
# 1. LibraryError (base exception)
# 2. BookNotFoundError
# 3. BookNotAvailableError
# 4. MemberNotFoundError
# 5. MaxBooksExceededError

# Your custom exceptions here:



# ========== EXERCISE 2: IMPLEMENT ERROR HANDLING ==========
print("\n\nExercise 2: Implement Error Handling")
print("-" * 40)

# TODO: Add proper error handling to this class using your custom exceptions

@dataclass
class Book:
    id: int
    title: str
    author: str
    available: bool = True


@dataclass
class Member:
    id: int
    name: str
    borrowed_books: List[int] = None
    
    def __post_init__(self):
        if self.borrowed_books is None:
            self.borrowed_books = []


class Library:
    """Library management system."""
    
    MAX_BOOKS_PER_MEMBER = 3
    
    def __init__(self):
        self._books: Dict[int, Book] = {}
        self._members: Dict[int, Member] = {}
    
    def add_book(self, book_id: int, title: str, author: str):
        """Add a book to the library."""
        # TODO: Add validation and error handling
        pass
    
    def register_member(self, member_id: int, name: str):
        """Register a new member."""
        # TODO: Add validation and error handling
        pass
    
    def borrow_book(self, member_id: int, book_id: int):
        """Borrow a book."""
        # TODO: Implement with proper error handling
        # - Check member exists
        # - Check book exists
        # - Check book is available
        # - Check member hasn't exceeded limit
        pass
    
    def return_book(self, member_id: int, book_id: int):
        """Return a borrowed book."""
        # TODO: Implement with proper error handling
        pass


# Write tests for your implementation:



# ========== EXERCISE 3: REFACTOR TO FOLLOW BEST PRACTICES ==========
print("\n\nExercise 3: Refactor Code")
print("-" * 40)

# TODO: Refactor this poorly organized code following best practices

# BAD CODE - Refactor this
class BadOrderSystem:
    """This class does too many things - refactor it!"""
    
    def __init__(self):
        self.products = {}
        self.orders = []
        self.users = {}
        self.email_config = {"host": "smtp.example.com"}
    
    def process(self, user_id, product_id, qty, credit_card):
        # Check user
        if user_id not in self.users:
            print("User not found")
            return None
        
        # Check product
        if product_id not in self.products:
            print("Product not found")
            return None
        
        product = self.products[product_id]
        
        # Check stock
        if product["stock"] < qty:
            print("Not enough stock")
            return None
        
        # Calculate price
        price = product["price"] * qty
        tax = price * 0.1
        total = price + tax
        
        # Process payment (simplified)
        if len(credit_card) != 16:
            print("Invalid card")
            return None
        
        # Update stock
        product["stock"] -= qty
        
        # Create order
        order = {
            "id": len(self.orders) + 1,
            "user_id": user_id,
            "product_id": product_id,
            "quantity": qty,
            "total": total
        }
        self.orders.append(order)
        
        # Send email (simplified)
        print(f"Email sent to {self.users[user_id]['email']}")
        
        return order


# TODO: Refactor into:
# 1. UserService - handles user operations
# 2. ProductService - handles product operations
# 3. PaymentService - handles payment processing
# 4. EmailService - handles notifications
# 5. OrderService - orchestrates the order process
# 6. Use proper exceptions

# Your refactored code here:



# ========== EXERCISE 4: IMPLEMENT RESULT PATTERN ==========
print("\n\nExercise 4: Implement Result Pattern")
print("-" * 40)

# TODO: Implement a Result type and use it for error handling

# Implement this Result class:
class Result:
    """Result type for operations that can fail."""
    pass


# Then use it in this function:
def parse_config(config_string: str):
    """
    Parse configuration string in format: key1=value1;key2=value2
    Returns Result with dict on success, error message on failure.
    """
    # TODO: Implement using Result pattern
    pass


# Write tests for your implementation:



# ========== EXERCISE 5: LOGGING EXERCISE ==========
print("\n\nExercise 5: Implement Proper Logging")
print("-" * 40)

# TODO: Add proper logging to this service

import logging

class DataProcessor:
    """Process data with proper logging."""
    
    def __init__(self):
        # TODO: Set up logging properly
        pass
    
    def process_batch(self, data: List[Dict]) -> List[Dict]:
        """
        Process a batch of records.
        Should log:
        - INFO: When starting and completing batch
        - DEBUG: Each record being processed
        - WARNING: Skipped invalid records
        - ERROR: Processing failures
        """
        results = []
        
        # TODO: Implement with proper logging
        for record in data:
            # Process each record
            # Log appropriate messages
            pass
        
        return results
    
    def validate_record(self, record: Dict) -> bool:
        """Validate a record."""
        # TODO: Implement with logging
        pass


# Write tests that verify logging behavior:



"""
Run your tests with: pytest 03_organization_exercises.py -v
"""
