"""
DAY 20 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 20 ASSESSMENT TEST - Testing & Best Practices")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What naming convention should pytest test files follow?
a) They must start with "test_" or end with "_test.py"
b) They must be named "unittest.py"
c) Any Python file can be a test file
d) They must be in a folder named "tests"

Your answer: """)

print("""
Q2. What does the pytest fixture decorator do?
a) Marks a function as a test case
b) Skips a test under certain conditions
c) Provides reusable setup code for tests
d) Makes a test run faster

Your answer: """)

print("""
Q3. Which of the following is the correct way to test for an exception in pytest?
a) assert raises(ValueError)
b) pytest.raises(ValueError)
c) with pytest.raises(ValueError):
d) @pytest.exception(ValueError)

Your answer: """)

print("""
Q4. What is the AAA pattern in testing?
a) Assert, Act, Arrange
b) Arrange, Act, Assert
c) Assert, Arrange, Act
d) Act, Assert, Arrange

Your answer: """)

print("""
Q5. What is the purpose of mocking in tests?
a) To make tests run slower
b) To replace dependencies with controlled fake objects
c) To skip certain tests
d) To generate random test data

Your answer: """)

print("""
Q6. Which principle states that each class should have only one responsibility?
a) DRY (Don't Repeat Yourself)
b) KISS (Keep It Simple, Stupid)
c) SRP (Single Responsibility Principle)
d) YAGNI (You Aren't Gonna Need It)

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a pytest test function that tests if a divide function
raises a ZeroDivisionError when dividing by zero.
""")

# Given function:
def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Write your test here:
# def test_divide_by_zero():
#     # Your code here
#     pass



print("""
Q8. (2 points) Write a parametrized test that tests a function is_even(n)
with the following test cases: (2, True), (3, False), (0, True), (-2, True)
""")

def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

# Write your parametrized test here:
# @pytest.mark.parametrize(...)
# def test_is_even(...):
#     # Your code here
#     pass



print("""
Q9. (2 points) Create a custom exception called InsufficientFundsError
that inherits from Exception and stores the required amount and available amount.
Include a meaningful error message.
""")

# Write your custom exception here:
# class InsufficientFundsError(Exception):
#     # Your code here
#     pass



# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between unit tests and integration tests.
Give an example of each in the context of a web application.

Your answer:
""")

# Write your explanation here as comments:
#
# Unit Tests:
# 
# 
# Integration Tests:
#
#


# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: a) They must start with "test_" or end with "_test.py"
Q2: c) Provides reusable setup code for tests
Q3: c) with pytest.raises(ValueError):
Q4: b) Arrange, Act, Assert
Q5: b) To replace dependencies with controlled fake objects
Q6: c) SRP (Single Responsibility Principle)

Section B (Coding):

Q7: Testing exceptions
```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)
```

Q8: Parametrized test
```python
import pytest

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
])
def test_is_even(number, expected):
    assert is_even(number) == expected
```

Q9: Custom exception
```python
class InsufficientFundsError(Exception):
    def __init__(self, required: float, available: float):
        self.required = required
        self.available = available
        message = f"Insufficient funds. Required: ${required}, Available: ${available}"
        super().__init__(message)
```

Section C:
Q10: Unit vs Integration Tests

Unit Tests:
- Test individual components in isolation
- Fast to run
- Mock external dependencies
- Example: Testing a function that validates email format

Integration Tests:
- Test how multiple components work together
- Slower to run
- Use real (or test) databases/services
- Example: Testing an API endpoint that creates a user,
  which involves the route handler, service layer, and database

Scoring:
- MCQ: 6 points (1 each)
- Coding: 6 points (2 each)
- Conceptual: 2 points
- Total: 14 points
- Pass: 10+ points (70%)
"""
