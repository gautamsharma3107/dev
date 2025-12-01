"""
EXERCISES: API Development
==========================
Complete all exercises below
"""

print("=" * 60)
print("EXERCISES: API Development")
print("=" * 60)

# Exercise 1: Basic Flask API
# TODO: Create a basic Flask API with health and info endpoints

print("\n" + "=" * 60)
print("Exercise 1: Basic Flask API")
print("=" * 60)

def exercise_1():
    """
    Create a Flask app with:
    1. GET / - Return welcome message
    2. GET /health - Return health status
    3. GET /info - Return API version and available endpoints
    
    Run and test with curl or browser.
    """
    # Your code here:
    pass

# Exercise 2: Input Validation
# TODO: Create comprehensive input validation

print("\n" + "=" * 60)
print("Exercise 2: Input Validation")
print("=" * 60)

def validate_prediction_request(data, feature_specs):
    """
    Validate prediction request with feature specifications.
    
    Args:
        data: Request JSON data
        feature_specs: List of dicts with feature info:
            [
                {"name": "sepal_length", "min": 4.0, "max": 8.0},
                {"name": "sepal_width", "min": 2.0, "max": 4.5},
                ...
            ]
    
    Returns:
        (is_valid, error_message, validated_features)
    
    Validate:
    - 'features' key exists
    - features is a list
    - correct number of features
    - all features are numeric
    - all features within range
    """
    # Your code here:
    pass


# Exercise 3: Prediction Endpoint
# TODO: Create a full prediction endpoint

print("\n" + "=" * 60)
print("Exercise 3: Complete Prediction Endpoint")
print("=" * 60)

def exercise_3():
    """
    Create a /predict endpoint that:
    1. Accepts POST with JSON body
    2. Validates input
    3. Returns prediction with:
        - class_id
        - class_name
        - confidence
        - probabilities
        - processing_time_ms
    4. Returns proper error responses (400, 500)
    """
    # Your code here:
    pass


# Exercise 4: Batch Predictions
# TODO: Create batch prediction endpoint

print("\n" + "=" * 60)
print("Exercise 4: Batch Predictions")
print("=" * 60)

def exercise_4():
    """
    Create a /predict/batch endpoint that:
    1. Accepts list of instances
    2. Validates each instance
    3. Returns list of predictions
    4. Handles partial failures (some invalid, some valid)
    5. Returns summary (total, successful, failed)
    6. Limits batch size to 100
    """
    # Your code here:
    pass


# Exercise 5: Error Handler Decorator
# TODO: Create a decorator for consistent error handling

print("\n" + "=" * 60)
print("Exercise 5: Error Handler Decorator")
print("=" * 60)

def handle_api_errors(f):
    """
    Create a decorator that:
    1. Catches ValidationError -> 400
    2. Catches ModelNotLoadedError -> 503
    3. Catches PredictionError -> 500
    4. Catches all other exceptions -> 500
    5. Logs errors
    6. Returns consistent JSON error format
    """
    # Your code here:
    pass


# Exercise 6: API Testing
# TODO: Write tests for your API

print("\n" + "=" * 60)
print("Exercise 6: API Tests")
print("=" * 60)

def test_api():
    """
    Write tests using Flask test client:
    1. Test GET /health returns 200
    2. Test POST /predict with valid data returns 200
    3. Test POST /predict with missing features returns 400
    4. Test POST /predict with wrong feature count returns 400
    5. Test POST /predict with non-numeric features returns 400
    """
    # Your code here:
    pass


print("\n" + "=" * 60)
print("Complete all exercises and test your implementations!")
print("=" * 60)

"""
SOLUTIONS (Don't look until you've tried!)
==========================================

Exercise 1:
-----------
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to ML API",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/info')
def info():
    return jsonify({
        "api_version": "1.0.0",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Welcome"},
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/info", "method": "GET", "description": "API info"},
            {"path": "/predict", "method": "POST", "description": "Make prediction"}
        ]
    })


Exercise 2:
-----------
def validate_prediction_request(data, feature_specs):
    # Check data exists
    if data is None:
        return False, "No JSON data provided", None
    
    # Check features key
    if 'features' not in data:
        return False, "Missing 'features' field", None
    
    features = data['features']
    
    # Check type
    if not isinstance(features, list):
        return False, "'features' must be a list", None
    
    # Check count
    expected = len(feature_specs)
    if len(features) != expected:
        return False, f"Expected {expected} features, got {len(features)}", None
    
    validated = []
    for i, (value, spec) in enumerate(zip(features, feature_specs)):
        # Check numeric
        if not isinstance(value, (int, float)):
            return False, f"Feature '{spec['name']}' must be numeric", None
        
        # Check range
        if value < spec['min'] or value > spec['max']:
            return False, f"Feature '{spec['name']}' out of range [{spec['min']}, {spec['max']}]", None
        
        validated.append(float(value))
    
    return True, None, validated


Exercise 3:
-----------
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
model = None  # Load at startup

CLASS_NAMES = ["setosa", "versicolor", "virginica"]

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    
    # Get data
    data = request.get_json()
    
    # Validate
    if not data or 'features' not in data:
        return jsonify({
            "success": False,
            "error": "Missing 'features' field"
        }), 400
    
    features = data['features']
    
    if not isinstance(features, list) or len(features) != 4:
        return jsonify({
            "success": False,
            "error": "Expected 4 numeric features"
        }), 400
    
    try:
        # Predict
        prediction = model.predict([features])[0]
        probabilities = model.predict_proba([features])[0]
        
        processing_time = (time.time() - start_time) * 1000
        
        return jsonify({
            "success": True,
            "prediction": {
                "class_id": int(prediction),
                "class_name": CLASS_NAMES[prediction],
                "confidence": float(max(probabilities)),
                "probabilities": [float(p) for p in probabilities]
            },
            "processing_time_ms": round(processing_time, 2)
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Prediction failed: {str(e)}"
        }), 500


Exercise 4:
-----------
@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    data = request.get_json()
    
    if not data or 'instances' not in data:
        return jsonify({"error": "Missing 'instances' field"}), 400
    
    instances = data['instances']
    
    if not isinstance(instances, list):
        return jsonify({"error": "'instances' must be a list"}), 400
    
    if len(instances) > 100:
        return jsonify({"error": "Max batch size is 100"}), 400
    
    predictions = []
    errors = []
    
    for i, instance in enumerate(instances):
        try:
            features = instance.get('features')
            
            if not features or len(features) != 4:
                errors.append({"index": i, "error": "Invalid features"})
                predictions.append(None)
                continue
            
            pred = model.predict([features])[0]
            proba = model.predict_proba([features])[0]
            
            predictions.append({
                "class_id": int(pred),
                "class_name": CLASS_NAMES[pred],
                "confidence": float(max(proba))
            })
            
        except Exception as e:
            errors.append({"index": i, "error": str(e)})
            predictions.append(None)
    
    return jsonify({
        "success": len(errors) == 0,
        "predictions": predictions,
        "errors": errors if errors else None,
        "summary": {
            "total": len(instances),
            "successful": len(instances) - len(errors),
            "failed": len(errors)
        }
    })


Exercise 5:
-----------
from functools import wraps
import logging

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    pass

class ModelNotLoadedError(Exception):
    pass

class PredictionError(Exception):
    pass

def handle_api_errors(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
            
        except ValidationError as e:
            logger.warning(f"Validation error: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"code": "VALIDATION_ERROR", "message": str(e)}
            }), 400
            
        except ModelNotLoadedError:
            logger.error("Model not loaded")
            return jsonify({
                "success": False,
                "error": {"code": "MODEL_NOT_LOADED", "message": "Model not available"}
            }), 503
            
        except PredictionError as e:
            logger.error(f"Prediction error: {str(e)}")
            return jsonify({
                "success": False,
                "error": {"code": "PREDICTION_ERROR", "message": str(e)}
            }), 500
            
        except Exception as e:
            logger.exception("Unexpected error")
            return jsonify({
                "success": False,
                "error": {"code": "INTERNAL_ERROR", "message": "An unexpected error occurred"}
            }), 500
    
    return decorated


Exercise 6:
-----------
def test_api():
    # Create test app
    app = Flask(__name__)
    
    # Add routes (copy from above)
    
    with app.test_client() as client:
        # Test health
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        print("✅ Health check passed")
        
        # Test valid prediction
        response = client.post('/predict',
            json={"features": [5.1, 3.5, 1.4, 0.2]},
            content_type='application/json'
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] == True
        print("✅ Valid prediction passed")
        
        # Test missing features
        response = client.post('/predict',
            json={},
            content_type='application/json'
        )
        assert response.status_code == 400
        print("✅ Missing features test passed")
        
        # Test wrong feature count
        response = client.post('/predict',
            json={"features": [1, 2]},
            content_type='application/json'
        )
        assert response.status_code == 400
        print("✅ Wrong feature count test passed")
        
        print("All tests passed! 🎉")
"""
