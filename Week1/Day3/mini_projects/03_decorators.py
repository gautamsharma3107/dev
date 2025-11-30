"""
MINI PROJECT 3: Function Decorators
====================================
Create useful decorators

Requirements:
1. @timer - measure execution time
2. @logger - log function calls
3. @retry - retry on failure
4. @validate - validate arguments
5. @cache - cache results (memoization)
"""

print("=" * 50)
print("FUNCTION DECORATORS")
print("=" * 50)

import time
from functools import wraps

# TODO: Implement these decorators:

# 1. Timer decorator
def timer(func):
    """Measure and print execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Your implementation
        pass
    return wrapper


# 2. Logger decorator
def logger(func):
    """Log function calls with arguments and return value."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Your implementation
        pass
    return wrapper


# 3. Retry decorator
def retry(max_attempts=3, delay=1):
    """Retry function on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Your implementation
            pass
        return wrapper
    return decorator


# 4. Validate decorator
def validate_positive(func):
    """Ensure all numeric arguments are positive."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Your implementation
        pass
    return wrapper


# 5. Cache decorator
def cache(func):
    """Cache function results."""
    cached_results = {}
    @wraps(func)
    def wrapper(*args):
        # Your implementation
        pass
    return wrapper


# TEST YOUR DECORATORS
# --------------------
