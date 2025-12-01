"""
Day 34 - Error Handling for ML APIs
===================================
Learn: Production-ready error handling

Key Concepts:
- Error response formats
- Exception handling
- Logging
- Input validation
- Graceful degradation
"""

import json
import logging
import traceback
from datetime import datetime
from functools import wraps

# ========== WHY ERROR HANDLING MATTERS ==========
print("=" * 60)
print("WHY ERROR HANDLING MATTERS")
print("=" * 60)

print("""
In production ML APIs, errors WILL happen:
- Invalid input data
- Model loading failures
- Preprocessing errors
- Memory issues
- Timeout errors

Good error handling:
1. Informs users what went wrong
2. Doesn't expose sensitive info
3. Logs details for debugging
4. Allows graceful recovery
5. Returns appropriate status codes
""")

# ========== SETTING UP LOGGING ==========
print("\n" + "=" * 60)
print("SETTING UP LOGGING")
print("=" * 60)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('ml_api')

print("""
Logging setup example:

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ml_api')

Log levels:
- DEBUG   - Detailed debugging info
- INFO    - General operational info
- WARNING - Something unexpected
- ERROR   - Error occurred, but app continues
- CRITICAL - Serious error, app may not continue
""")

# Demo logging
logger.info("API started")
logger.warning("Model loaded with old version")
logger.error("Prediction failed for request abc123")

# ========== ERROR RESPONSE FORMAT ==========
print("\n" + "=" * 60)
print("STANDARDIZED ERROR RESPONSES")
print("=" * 60)

class APIError(Exception):
    """Base class for API errors."""
    
    def __init__(self, message, code=None, status_code=500, details=None):
        self.message = message
        self.code = code or "INTERNAL_ERROR"
        self.status_code = status_code
        self.details = details
        super().__init__(message)
    
    def to_dict(self):
        """Convert error to dictionary for JSON response."""
        return {
            "success": False,
            "error": {
                "message": self.message,
                "code": self.code,
                "details": self.details
            }
        }


class ValidationError(APIError):
    """Raised when input validation fails."""
    
    def __init__(self, message, field=None):
        super().__init__(
            message=message,
            code="VALIDATION_ERROR",
            status_code=400,
            details={"field": field} if field else None
        )


class ModelNotLoadedError(APIError):
    """Raised when model is not available."""
    
    def __init__(self):
        super().__init__(
            message="Model not loaded",
            code="MODEL_NOT_LOADED",
            status_code=503
        )


class PredictionError(APIError):
    """Raised when prediction fails."""
    
    def __init__(self, message, original_error=None):
        super().__init__(
            message=message,
            code="PREDICTION_ERROR",
            status_code=500,
            details={"original_error": str(original_error)} if original_error else None
        )


# Demo error classes
print("\nCustom error classes:")
print("-" * 40)

errors = [
    ValidationError("Invalid feature count", field="features"),
    ModelNotLoadedError(),
    PredictionError("Feature shape mismatch", ValueError("Expected 4 features"))
]

for error in errors:
    print(f"\n{error.__class__.__name__}:")
    print(f"  Status: {error.status_code}")
    print(f"  Response: {json.dumps(error.to_dict(), indent=4)}")

# ========== ERROR HANDLING DECORATOR ==========
print("\n" + "=" * 60)
print("ERROR HANDLING DECORATOR")
print("=" * 60)

def handle_errors(f):
    """
    Decorator for consistent error handling.
    Catches exceptions and returns proper JSON responses.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        
        except APIError as e:
            # Log the error
            logger.error(f"API Error: {e.code} - {e.message}")
            return e.to_dict(), e.status_code
        
        except ValueError as e:
            # Handle value errors (often from invalid input)
            logger.error(f"ValueError: {str(e)}")
            error = ValidationError(str(e))
            return error.to_dict(), error.status_code
        
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Unexpected error: {str(e)}")
            logger.error(traceback.format_exc())
            
            # Don't expose internal errors in production
            error = APIError("An unexpected error occurred")
            return error.to_dict(), error.status_code
    
    return decorated_function


# Demo decorator usage
print("""
Error handling decorator usage:

@app.route('/predict', methods=['POST'])
@handle_errors
def predict():
    # Validation error
    if not features:
        raise ValidationError("Missing features", field="features")
    
    # Model error
    if model is None:
        raise ModelNotLoadedError()
    
    # Prediction error
    try:
        prediction = model.predict(features)
    except Exception as e:
        raise PredictionError("Prediction failed", e)
    
    return jsonify({"prediction": prediction})
""")

# ========== COMPREHENSIVE ERROR HANDLING ==========
print("\n" + "=" * 60)
print("COMPREHENSIVE ERROR HANDLING EXAMPLE")
print("=" * 60)

comprehensive_code = '''
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Error handlers
@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        "success": False,
        "error": {
            "message": "Bad request",
            "code": "BAD_REQUEST"
        }
    }), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "success": False,
        "error": {
            "message": "Endpoint not found",
            "code": "NOT_FOUND"
        }
    }), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "success": False,
        "error": {
            "message": "Internal server error",
            "code": "INTERNAL_ERROR"
        }
    }), 500

@app.errorhandler(APIError)
def handle_api_error(e):
    logger.error(f"APIError: {e.code} - {e.message}")
    return jsonify(e.to_dict()), e.status_code

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Validate input
        if not data:
            raise ValidationError("No JSON data provided")
        
        if 'features' not in data:
            raise ValidationError("Missing features", field="features")
        
        features = data['features']
        
        if not isinstance(features, list):
            raise ValidationError("Features must be a list", field="features")
        
        if len(features) != 4:
            raise ValidationError(
                f"Expected 4 features, got {len(features)}", 
                field="features"
            )
        
        # Check model
        if model is None:
            raise ModelNotLoadedError()
        
        # Make prediction
        try:
            prediction = model.predict([features])[0]
            probabilities = model.predict_proba([features])[0]
        except Exception as e:
            raise PredictionError("Model prediction failed", e)
        
        return jsonify({
            "success": True,
            "prediction": int(prediction),
            "confidence": float(max(probabilities))
        })
        
    except APIError:
        raise  # Re-raise API errors
    except Exception as e:
        logger.exception("Unexpected error in predict endpoint")
        raise APIError("Prediction failed unexpectedly")
'''

print("Comprehensive error handling:")
print(comprehensive_code)

# ========== INPUT VALIDATION HELPERS ==========
print("\n" + "=" * 60)
print("INPUT VALIDATION HELPERS")
print("=" * 60)

def validate_request_data(data, required_fields=None, optional_fields=None):
    """
    Validate request data comprehensively.
    
    Args:
        data: Request data dictionary
        required_fields: List of required field names
        optional_fields: Dict of optional fields with defaults
        
    Returns:
        Validated and cleaned data
        
    Raises:
        ValidationError if validation fails
    """
    if data is None:
        raise ValidationError("No data provided")
    
    if not isinstance(data, dict):
        raise ValidationError("Data must be a JSON object")
    
    validated = {}
    
    # Check required fields
    if required_fields:
        for field in required_fields:
            if field not in data:
                raise ValidationError(f"Missing required field: {field}", field=field)
            validated[field] = data[field]
    
    # Add optional fields with defaults
    if optional_fields:
        for field, default in optional_fields.items():
            validated[field] = data.get(field, default)
    
    return validated


def validate_features(features, expected_count, feature_ranges=None):
    """
    Validate feature array.
    
    Args:
        features: List of feature values
        expected_count: Expected number of features
        feature_ranges: Optional dict of {index: (min, max)} for range validation
        
    Returns:
        Validated feature list
        
    Raises:
        ValidationError if validation fails
    """
    if not isinstance(features, list):
        raise ValidationError("Features must be a list", field="features")
    
    if len(features) != expected_count:
        raise ValidationError(
            f"Expected {expected_count} features, got {len(features)}",
            field="features"
        )
    
    validated = []
    for i, value in enumerate(features):
        # Check type
        if not isinstance(value, (int, float)):
            raise ValidationError(
                f"Feature at index {i} must be numeric",
                field=f"features[{i}]"
            )
        
        # Check range if specified
        if feature_ranges and i in feature_ranges:
            min_val, max_val = feature_ranges[i]
            if not min_val <= value <= max_val:
                raise ValidationError(
                    f"Feature at index {i} out of range [{min_val}, {max_val}]",
                    field=f"features[{i}]"
                )
        
        validated.append(float(value))
    
    return validated


# Demo validation helpers
print("\nValidation helper examples:")
print("-" * 40)

# Test request validation
try:
    data = validate_request_data(
        {"features": [1, 2, 3, 4], "model": "iris"},
        required_fields=["features"],
        optional_fields={"model": "default", "version": "1.0"}
    )
    print(f"✅ Validated request: {data}")
except ValidationError as e:
    print(f"❌ {e.message}")

# Test feature validation
try:
    features = validate_features(
        [5.1, 3.5, 1.4, 0.2],
        expected_count=4,
        feature_ranges={0: (4.0, 8.0), 1: (2.0, 4.5)}
    )
    print(f"✅ Validated features: {features}")
except ValidationError as e:
    print(f"❌ {e.message}")

# Test with invalid data
print("\nInvalid data examples:")
invalid_cases = [
    ({"features": [1, 2]}, "Wrong feature count"),
    ({"features": [1, "two", 3, 4]}, "Non-numeric feature"),
    ({"features": [10.0, 3.5, 1.4, 0.2]}, "Out of range"),  # 10.0 > 8.0
]

for data, description in invalid_cases:
    try:
        validate_features(data['features'], 4, {0: (4.0, 8.0)})
    except ValidationError as e:
        print(f"  {description}: {e.message}")

# ========== GRACEFUL DEGRADATION ==========
print("\n" + "=" * 60)
print("GRACEFUL DEGRADATION")
print("=" * 60)

print("""
When errors occur, consider graceful fallbacks:
1. Use cached predictions
2. Fall back to simpler model
3. Return partial results
4. Queue request for later
""")

graceful_code = '''
@app.route('/predict', methods=['POST'])
def predict_with_fallback():
    try:
        # Try primary model
        prediction = primary_model.predict(features)
        return jsonify({"prediction": prediction, "model": "primary"})
        
    except Exception as e:
        logger.warning(f"Primary model failed: {e}")
        
        try:
            # Fall back to simpler model
            prediction = fallback_model.predict(features)
            return jsonify({
                "prediction": prediction,
                "model": "fallback",
                "warning": "Using fallback model"
            })
            
        except Exception as e2:
            logger.error(f"Fallback model also failed: {e2}")
            raise PredictionError("All models failed")
'''

print("Graceful degradation example:")
print(graceful_code)

# ========== RATE LIMITING AND TIMEOUTS ==========
print("\n" + "=" * 60)
print("RATE LIMITING AND TIMEOUTS")
print("=" * 60)

print("""
Protect your API from abuse:
1. Rate limiting - limit requests per user/IP
2. Timeouts - don't let requests hang forever
3. Request size limits - prevent large payloads
""")

protection_code = '''
from flask import Flask, request, jsonify
from functools import wraps
import time

# Simple rate limiter (use Redis for production)
request_counts = {}
RATE_LIMIT = 100  # requests per minute

def rate_limit(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        ip = request.remote_addr
        current_minute = int(time.time() / 60)
        
        key = f"{ip}:{current_minute}"
        request_counts[key] = request_counts.get(key, 0) + 1
        
        if request_counts[key] > RATE_LIMIT:
            return jsonify({
                "error": "Rate limit exceeded",
                "code": "RATE_LIMITED"
            }), 429
        
        return f(*args, **kwargs)
    return decorated

@app.route('/predict', methods=['POST'])
@rate_limit
def predict():
    # Handle prediction
    pass

# Timeout handling
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Prediction timeout")

def predict_with_timeout(model, features, timeout_seconds=30):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)
    
    try:
        result = model.predict(features)
        signal.alarm(0)  # Cancel alarm
        return result
    except TimeoutError:
        raise PredictionError("Prediction timed out")
'''

print("Rate limiting and timeout example:")
print(protection_code)

# ========== PRACTICAL: ERROR SIMULATION ==========
print("\n" + "=" * 60)
print("PRACTICAL: ERROR SIMULATION")
print("=" * 60)

def simulate_prediction_endpoint(data, model_loaded=True, model_fails=False):
    """Simulate prediction endpoint with various error scenarios."""
    
    try:
        # Step 1: Validate request
        validated = validate_request_data(data, required_fields=["features"])
        
        # Step 2: Validate features
        features = validate_features(
            validated["features"],
            expected_count=4,
            feature_ranges={0: (4.0, 8.0), 1: (2.0, 4.5), 2: (1.0, 7.0), 3: (0.1, 2.5)}
        )
        
        # Step 3: Check model
        if not model_loaded:
            raise ModelNotLoadedError()
        
        # Step 4: Make prediction
        if model_fails:
            raise PredictionError("Model inference failed", RuntimeError("Memory error"))
        
        # Success!
        return {
            "success": True,
            "prediction": {"class_id": 0, "class_name": "setosa"},
            "status_code": 200
        }
        
    except APIError as e:
        return {**e.to_dict(), "status_code": e.status_code}
    
    except Exception as e:
        return {
            "success": False,
            "error": {"message": str(e), "code": "UNKNOWN"},
            "status_code": 500
        }


# Test various scenarios
print("\nTesting error scenarios:")
print("-" * 40)

scenarios = [
    ({"features": [5.1, 3.5, 1.4, 0.2]}, True, False, "Valid request"),
    ({}, True, False, "Missing features"),
    ({"features": [1, 2]}, True, False, "Wrong feature count"),
    ({"features": [5.1, 3.5, 1.4, 0.2]}, False, False, "Model not loaded"),
    ({"features": [5.1, 3.5, 1.4, 0.2]}, True, True, "Model failure"),
]

for data, model_loaded, model_fails, description in scenarios:
    result = simulate_prediction_endpoint(data, model_loaded, model_fails)
    status = "✅" if result.get("success") else "❌"
    code = result.get("error", {}).get("code", "OK") if not result.get("success") else "OK"
    print(f"\n{description}:")
    print(f"  {status} Status: {result['status_code']}, Code: {code}")

print("\n" + "=" * 60)
print("✅ Error Handling for ML APIs - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Use custom error classes for different error types
2. Return consistent error response format
3. Use proper HTTP status codes
4. Log errors for debugging (not to users)
5. Validate input thoroughly
6. Implement graceful degradation
7. Protect with rate limiting and timeouts

Key error codes:
- 400: Bad Request (invalid input)
- 401: Unauthorized (auth required)
- 404: Not Found (bad endpoint)
- 422: Unprocessable (invalid data)
- 429: Too Many Requests (rate limited)
- 500: Internal Error (server issue)
- 503: Service Unavailable (model not ready)

Your ML API is now production-ready! 🚀
""")
