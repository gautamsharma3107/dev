"""
Day 20 - Error Handling Patterns
================================
Learn: Exception handling, custom exceptions, graceful error handling

Key Concepts:
- Writing robust error handling code
- Creating custom exceptions
- Logging errors appropriately
- Designing fail-safe systems
"""

import logging
import time
from typing import Dict, Any, Optional, List, TypeVar, Generic
from dataclasses import dataclass
from enum import Enum
from functools import wraps
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ========== ERROR HANDLING BASICS ==========
print("=" * 60)
print("ERROR HANDLING BASICS")
print("=" * 60)

"""
Exception Handling Best Practices:
1. Be specific - catch specific exceptions, not all
2. Don't suppress exceptions silently
3. Log errors with context
4. Use custom exceptions for domain errors
5. Clean up resources properly
"""


# BAD: Catching all exceptions
def bad_file_reader(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:  # BAD: Catches everything, including KeyboardInterrupt
        pass  # BAD: Silent suppression


# GOOD: Specific exception handling
def good_file_reader(filename: str) -> Optional[str]:
    """Read file contents with proper error handling."""
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        logger.warning(f"File not found: {filename}")
        return None
    except PermissionError:
        logger.error(f"Permission denied: {filename}")
        raise
    except IOError as e:
        logger.error(f"IO error reading {filename}: {e}")
        return None


# ========== CUSTOM EXCEPTIONS ==========
print("\n" + "=" * 60)
print("CUSTOM EXCEPTIONS")
print("=" * 60)

"""
Custom exceptions help:
1. Make error types explicit
2. Carry additional error information
3. Enable specific handling
4. Document possible errors
"""


# Base exception for application
class AppError(Exception):
    """Base exception for application errors."""
    
    def __init__(self, message: str, code: str = "APP_ERROR", details: Dict = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for API responses."""
        return {
            "error": self.code,
            "message": self.message,
            "details": self.details
        }


# Specific exceptions
class ValidationError(AppError):
    """Raised when validation fails."""
    
    def __init__(self, message: str, field: str = None, details: Dict = None):
        super().__init__(message, "VALIDATION_ERROR", details)
        self.field = field


class NotFoundError(AppError):
    """Raised when a resource is not found."""
    
    def __init__(self, resource: str, identifier: Any):
        message = f"{resource} with id '{identifier}' not found"
        super().__init__(message, "NOT_FOUND", {"resource": resource, "id": identifier})


class AuthenticationError(AppError):
    """Raised when authentication fails."""
    
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, "AUTH_ERROR")


class AuthorizationError(AppError):
    """Raised when user lacks permission."""
    
    def __init__(self, action: str, resource: str):
        message = f"Not authorized to {action} {resource}"
        super().__init__(message, "FORBIDDEN", {"action": action, "resource": resource})


class RateLimitError(AppError):
    """Raised when rate limit is exceeded."""
    
    def __init__(self, retry_after: int = 60):
        message = f"Rate limit exceeded. Retry after {retry_after} seconds"
        super().__init__(message, "RATE_LIMIT", {"retry_after": retry_after})


class ExternalServiceError(AppError):
    """Raised when external service fails."""
    
    def __init__(self, service: str, message: str):
        super().__init__(
            f"External service error ({service}): {message}",
            "EXTERNAL_ERROR",
            {"service": service}
        )


# ========== USING CUSTOM EXCEPTIONS ==========
print("\n" + "=" * 60)
print("USING CUSTOM EXCEPTIONS")
print("=" * 60)


@dataclass
class User:
    """User model."""
    id: int
    username: str
    email: str
    role: str = "user"


class UserRepository:
    """User repository with error handling."""
    
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._next_id = 1
    
    def get_by_id(self, user_id: int) -> User:
        """Get user by ID, raising NotFoundError if not found."""
        user = self._users.get(user_id)
        if not user:
            raise NotFoundError("User", user_id)
        return user
    
    def save(self, user: User) -> User:
        """Save user to repository."""
        if user.id is None:
            user.id = self._next_id
            self._next_id += 1
        self._users[user.id] = user
        return user


class UserService:
    """User service with comprehensive error handling."""
    
    def __init__(self, repository: UserRepository):
        self._repository = repository
    
    def create_user(self, username: str, email: str) -> User:
        """Create a new user with validation."""
        # Validate username
        if not username:
            raise ValidationError("Username is required", field="username")
        if len(username) < 3:
            raise ValidationError(
                "Username must be at least 3 characters",
                field="username"
            )
        
        # Validate email
        if not email:
            raise ValidationError("Email is required", field="email")
        if "@" not in email:
            raise ValidationError("Invalid email format", field="email")
        
        # Create and save user
        user = User(id=None, username=username, email=email)
        return self._repository.save(user)
    
    def get_user(self, user_id: int) -> User:
        """Get user by ID."""
        if user_id < 0:
            raise ValidationError("User ID must be positive", field="user_id")
        return self._repository.get_by_id(user_id)
    
    def delete_user(self, user_id: int, requester: User) -> bool:
        """Delete user with authorization check."""
        # Check authorization
        if requester.role != "admin":
            raise AuthorizationError("delete", "user")
        
        # Get user to delete
        user = self._repository.get_by_id(user_id)
        # Delete logic here...
        return True


# ========== ERROR HANDLING PATTERNS ==========
print("\n" + "=" * 60)
print("ERROR HANDLING PATTERNS")
print("=" * 60)


# Pattern 1: Result Type (Either pattern)
T = TypeVar('T')


@dataclass
class Result(Generic[T]):
    """Result type for operations that can fail."""
    success: bool
    value: Optional[T] = None
    error: Optional[str] = None
    
    @classmethod
    def ok(cls, value: T) -> 'Result[T]':
        """Create successful result."""
        return cls(success=True, value=value)
    
    @classmethod
    def fail(cls, error: str) -> 'Result[T]':
        """Create failed result."""
        return cls(success=False, error=error)


def divide_safe(a: float, b: float) -> Result[float]:
    """Divide with Result type."""
    if b == 0:
        return Result.fail("Division by zero")
    return Result.ok(a / b)


# Usage
result = divide_safe(10, 2)
if result.success:
    print(f"Result: {result.value}")
else:
    print(f"Error: {result.error}")


# Pattern 2: Error handling decorator
def handle_exceptions(logger_instance=None):
    """Decorator for handling exceptions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValidationError as e:
                if logger_instance:
                    logger_instance.warning(f"Validation error: {e.message}")
                raise
            except NotFoundError as e:
                if logger_instance:
                    logger_instance.warning(f"Not found: {e.message}")
                raise
            except AppError as e:
                if logger_instance:
                    logger_instance.error(f"Application error: {e.message}")
                raise
            except Exception as e:
                if logger_instance:
                    logger_instance.exception(f"Unexpected error in {func.__name__}")
                raise AppError(f"Unexpected error: {str(e)}")
        return wrapper
    return decorator


# Usage
@handle_exceptions(logger)
def process_user_request(user_id: int):
    """Process user request with automatic error handling."""
    if user_id < 0:
        raise ValidationError("Invalid user ID")
    return {"user_id": user_id, "status": "processed"}


# Pattern 3: Retry with backoff


def retry_with_backoff(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (Exception,)
):
    """Decorator for retrying operations with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            last_exception = None
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        logger.warning(
                            f"Attempt {attempt + 1} failed: {e}. "
                            f"Retrying in {delay}s..."
                        )
                        time.sleep(delay)
                        delay *= backoff_factor
            
            logger.error(f"All {max_retries} attempts failed")
            raise last_exception
        return wrapper
    return decorator


# Usage example (simulated)
# @retry_with_backoff(max_retries=3, exceptions=(ConnectionError,))
# def fetch_from_api():
#     """Fetch data from API with automatic retry."""
#     response = requests.get("https://api.example.com/data")
#     response.raise_for_status()
#     return response.json()


# Pattern 4: Context manager for resource cleanup
class DatabaseTransaction:
    """Context manager for database transactions."""
    
    def __init__(self, connection):
        self.connection = connection
        self._savepoint = None
    
    def __enter__(self):
        self._savepoint = "savepoint_1"  # Simulated
        logger.info("Transaction started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logger.error(f"Transaction failed: {exc_val}")
            # Rollback logic here
            logger.info("Transaction rolled back")
            return False  # Re-raise the exception
        
        # Commit logic here
        logger.info("Transaction committed")
        return True


# ========== API ERROR RESPONSES ==========
print("\n" + "=" * 60)
print("API ERROR RESPONSE PATTERN")
print("=" * 60)


class ErrorCode(Enum):
    """Standard error codes."""
    VALIDATION = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    CONFLICT = "CONFLICT"
    INTERNAL = "INTERNAL_ERROR"


@dataclass
class APIResponse:
    """Standardized API response."""
    success: bool
    data: Optional[Any] = None
    error: Optional[Dict] = None
    status_code: int = 200
    
    @classmethod
    def success_response(cls, data: Any, status_code: int = 200) -> 'APIResponse':
        """Create success response."""
        return cls(success=True, data=data, status_code=status_code)
    
    @classmethod
    def error_response(
        cls,
        code: ErrorCode,
        message: str,
        status_code: int,
        details: Dict = None
    ) -> 'APIResponse':
        """Create error response."""
        return cls(
            success=False,
            error={
                "code": code.value,
                "message": message,
                "details": details or {}
            },
            status_code=status_code
        )
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        if self.success:
            return {"success": True, "data": self.data}
        return {"success": False, "error": self.error}


class APIController:
    """API controller with error handling."""
    
    def __init__(self, user_service: UserService):
        self._user_service = user_service
    
    def create_user(self, request_data: Dict) -> APIResponse:
        """Handle user creation request."""
        try:
            user = self._user_service.create_user(
                username=request_data.get("username", ""),
                email=request_data.get("email", "")
            )
            return APIResponse.success_response(
                {"id": user.id, "username": user.username},
                status_code=201
            )
        except ValidationError as e:
            return APIResponse.error_response(
                ErrorCode.VALIDATION,
                e.message,
                status_code=400,
                details={"field": e.field} if e.field else None
            )
        except NotFoundError as e:
            return APIResponse.error_response(
                ErrorCode.NOT_FOUND,
                e.message,
                status_code=404
            )
        except AuthorizationError as e:
            return APIResponse.error_response(
                ErrorCode.FORBIDDEN,
                e.message,
                status_code=403
            )
        except Exception as e:
            logger.exception("Unexpected error in create_user")
            return APIResponse.error_response(
                ErrorCode.INTERNAL,
                "An unexpected error occurred",
                status_code=500
            )


# ========== LOGGING BEST PRACTICES ==========
print("\n" + "=" * 60)
print("LOGGING BEST PRACTICES")
print("=" * 60)

"""
Logging Levels:
- DEBUG: Detailed info for debugging
- INFO: General operational info
- WARNING: Something unexpected but recoverable
- ERROR: Error occurred but app can continue
- CRITICAL: Severe error, app may not continue

Best Practices:
1. Log at appropriate levels
2. Include context (IDs, user info)
3. Don't log sensitive data
4. Use structured logging for production
"""


class LoggingService:
    """Service demonstrating logging best practices."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def process_order(self, order_id: str, user_id: str, amount: float):
        """Process order with proper logging."""
        self.logger.info(
            f"Processing order",
            extra={
                "order_id": order_id,
                "user_id": user_id,
                "amount": amount
            }
        )
        
        try:
            # Validate
            if amount <= 0:
                self.logger.warning(
                    f"Invalid order amount",
                    extra={"order_id": order_id, "amount": amount}
                )
                raise ValidationError("Amount must be positive")
            
            # Process (simulated)
            self.logger.debug(f"Order {order_id}: Starting payment processing")
            # payment_result = process_payment(amount)
            
            self.logger.info(
                f"Order completed successfully",
                extra={"order_id": order_id}
            )
            
        except ValidationError:
            self.logger.warning(
                f"Order validation failed",
                extra={"order_id": order_id}
            )
            raise
        except Exception as e:
            self.logger.exception(
                f"Order processing failed",
                extra={"order_id": order_id, "error": str(e)}
            )
            raise


# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: ROBUST SERVICE")
print("=" * 60)


class PaymentError(AppError):
    """Payment-related error."""
    
    def __init__(self, message: str, transaction_id: str = None):
        super().__init__(message, "PAYMENT_ERROR")
        self.transaction_id = transaction_id


class InsufficientFundsError(PaymentError):
    """Insufficient funds error."""
    
    def __init__(self, required: float, available: float):
        message = f"Insufficient funds. Required: ${required}, Available: ${available}"
        super().__init__(message)
        self.required = required
        self.available = available


class PaymentService:
    """Payment service with comprehensive error handling."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._accounts: Dict[str, float] = {}
    
    def create_account(self, account_id: str, initial_balance: float = 0):
        """Create a new account."""
        if account_id in self._accounts:
            raise ValidationError(f"Account {account_id} already exists")
        if initial_balance < 0:
            raise ValidationError("Initial balance cannot be negative")
        
        self._accounts[account_id] = initial_balance
        self.logger.info(f"Account created", extra={"account_id": account_id})
    
    def process_payment(
        self,
        from_account: str,
        to_account: str,
        amount: float
    ) -> Dict[str, Any]:
        """Process payment between accounts."""
        transaction_id = f"TXN-{len(self._accounts)}"
        
        self.logger.info(
            "Processing payment",
            extra={
                "transaction_id": transaction_id,
                "from": from_account,
                "to": to_account,
                "amount": amount
            }
        )
        
        try:
            # Validate accounts
            self._validate_account(from_account)
            self._validate_account(to_account)
            
            # Validate amount
            if amount <= 0:
                raise ValidationError("Payment amount must be positive")
            
            # Check balance
            balance = self._accounts[from_account]
            if balance < amount:
                raise InsufficientFundsError(
                    required=amount,
                    available=balance
                )
            
            # Process transfer
            self._accounts[from_account] -= amount
            self._accounts[to_account] += amount
            
            self.logger.info(
                "Payment completed",
                extra={"transaction_id": transaction_id}
            )
            
            return {
                "transaction_id": transaction_id,
                "status": "completed",
                "amount": amount
            }
            
        except InsufficientFundsError:
            self.logger.warning(
                "Payment failed - insufficient funds",
                extra={"transaction_id": transaction_id}
            )
            raise
        except ValidationError:
            self.logger.warning(
                "Payment failed - validation error",
                extra={"transaction_id": transaction_id}
            )
            raise
        except Exception as e:
            self.logger.exception(
                "Payment failed - unexpected error",
                extra={"transaction_id": transaction_id}
            )
            raise PaymentError(f"Payment processing failed: {str(e)}", transaction_id)
    
    def _validate_account(self, account_id: str):
        """Validate account exists."""
        if account_id not in self._accounts:
            raise NotFoundError("Account", account_id)


# Test the payment service
def demo_error_handling():
    """Demonstrate error handling in action."""
    service = PaymentService()
    
    # Create accounts
    service.create_account("acc1", 100)
    service.create_account("acc2", 50)
    
    print("\n--- Successful Payment ---")
    try:
        result = service.process_payment("acc1", "acc2", 30)
        print(f"Success: {result}")
    except AppError as e:
        print(f"Error: {e.to_dict()}")
    
    print("\n--- Insufficient Funds ---")
    try:
        result = service.process_payment("acc1", "acc2", 100)
        print(f"Success: {result}")
    except InsufficientFundsError as e:
        print(f"Error: {e.to_dict()}")
    
    print("\n--- Account Not Found ---")
    try:
        result = service.process_payment("invalid", "acc2", 10)
        print(f"Success: {result}")
    except NotFoundError as e:
        print(f"Error: {e.to_dict()}")


# Run demo
demo_error_handling()


print("\n" + "=" * 60)
print("✅ Error Handling Patterns - Complete!")
print("=" * 60)
print("\nKey Takeaways:")
print("1. Use specific exceptions, not catch-all")
print("2. Create custom exceptions for domain errors")
print("3. Log errors with context")
print("4. Use patterns like Result type for operations that can fail")
print("5. Clean up resources with context managers")
