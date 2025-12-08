"""
Day 34 - Flask API Basics for ML Models
========================================
Learn: Building REST APIs with Flask for model serving

Key Concepts:
- Flask application setup
- Creating API endpoints
- Handling JSON requests
- Returning JSON responses
"""

# ========== FLASK INTRODUCTION ==========
print("=" * 60)
print("FLASK INTRODUCTION")
print("=" * 60)

print("""
Flask is a lightweight Python web framework.
Perfect for ML deployment because:
- Simple and easy to learn
- Minimal boilerplate
- Built-in development server
- Great for microservices

Install: pip install flask
""")

# Import Flask (with fallback for demo)
try:
    from flask import Flask, request, jsonify
    FLASK_AVAILABLE = True
except ImportError:
    print("Note: Flask not installed. Run: pip install flask")
    FLASK_AVAILABLE = False

# ========== BASIC FLASK APP ==========
print("\n" + "=" * 60)
print("BASIC FLASK APP STRUCTURE")
print("=" * 60)

basic_app_code = '''
from flask import Flask, request, jsonify

# Create Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hello, ML World!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
'''

print("Basic Flask app:")
print(basic_app_code)

print("""
Key concepts:
- Flask(__name__) creates the app
- @app.route() decorator defines URL endpoints
- Functions return the response
- app.run() starts the server
""")

# ========== HTTP METHODS ==========
print("\n" + "=" * 60)
print("HTTP METHODS FOR ML APIS")
print("=" * 60)

print("""
Common HTTP methods for ML APIs:

GET     - Retrieve information (model info, health check)
POST    - Send data for prediction
PUT     - Update model or settings
DELETE  - Remove cached predictions

For ML predictions, we mainly use:
- GET:  /health, /model/info
- POST: /predict (send features, get prediction)
""")

# ========== CREATING API ENDPOINTS ==========
print("\n" + "=" * 60)
print("CREATING API ENDPOINTS")
print("=" * 60)

api_endpoints_code = '''
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint - Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "message": "API is running"
    })

# GET endpoint - Model info
@app.route('/model/info', methods=['GET'])
def model_info():
    return jsonify({
        "model": "RandomForestClassifier",
        "version": "1.0.0",
        "features": ["sepal_length", "sepal_width", 
                     "petal_length", "petal_width"]
    })

# POST endpoint - Prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json()
    
    # Extract features
    features = data.get('features', [])
    
    # Make prediction (placeholder)
    prediction = {"class": "setosa", "confidence": 0.95}
    
    return jsonify({
        "success": True,
        "prediction": prediction
    })
'''

print("API endpoints example:")
print(api_endpoints_code)

# ========== HANDLING JSON REQUESTS ==========
print("\n" + "=" * 60)
print("HANDLING JSON REQUESTS")
print("=" * 60)

json_handling_code = '''
@app.route('/predict', methods=['POST'])
def predict():
    # Method 1: Get JSON data
    data = request.get_json()
    
    # Method 2: Get JSON with force=True (ignores content-type)
    data = request.get_json(force=True)
    
    # Access data fields
    features = data.get('features', [])
    model_name = data.get('model', 'default')
    
    # Validate input
    if not features:
        return jsonify({
            "error": "No features provided"
        }), 400  # Bad Request
    
    # Process and return
    return jsonify({
        "received_features": features,
        "model_used": model_name
    })
'''

print("Handling JSON requests:")
print(json_handling_code)

print("""
Client sends JSON like:
{
    "features": [5.1, 3.5, 1.4, 0.2],
    "model": "iris_classifier"
}

Key functions:
- request.get_json() - Parse JSON body
- request.args.get() - Get query parameters
- request.headers - Access headers
""")

# ========== RETURNING JSON RESPONSES ==========
print("\n" + "=" * 60)
print("RETURNING JSON RESPONSES")
print("=" * 60)

response_patterns_code = '''
from flask import jsonify

# Success response
@app.route('/success')
def success_response():
    return jsonify({
        "success": True,
        "data": {"result": "value"}
    }), 200  # OK

# Error response
@app.route('/error')
def error_response():
    return jsonify({
        "success": False,
        "error": "Something went wrong",
        "code": "PREDICTION_FAILED"
    }), 500  # Internal Server Error

# Standard ML prediction response
@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({
        "success": True,
        "prediction": {
            "class": "setosa",
            "class_id": 0,
            "confidence": 0.95,
            "probabilities": [0.95, 0.03, 0.02]
        },
        "model_version": "1.0.0",
        "processing_time_ms": 15
    })
'''

print("Response patterns:")
print(response_patterns_code)

# ========== STATUS CODES ==========
print("\n" + "=" * 60)
print("HTTP STATUS CODES")
print("=" * 60)

print("""
Common status codes for ML APIs:

2xx Success:
  200 OK           - Request successful
  201 Created      - Resource created

4xx Client Errors:
  400 Bad Request  - Invalid input data
  401 Unauthorized - Authentication required
  404 Not Found    - Endpoint doesn't exist
  422 Unprocessable - Invalid data format

5xx Server Errors:
  500 Internal Error - Server/model error
  503 Unavailable    - Model not loaded

Usage: return jsonify(data), status_code
""")

# ========== COMPLETE MINIMAL API ==========
print("\n" + "=" * 60)
print("COMPLETE MINIMAL ML API")
print("=" * 60)

complete_api_code = '''
"""
Minimal ML API with Flask
Run: python app.py
Test: curl http://localhost:5000/health
"""

from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Global model variable
model = None

def load_model():
    """Load model at startup."""
    global model
    model_path = "model.pkl"
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        print("Model loaded successfully!")
    else:
        print("Warning: No model file found")

@app.route('/')
def home():
    return jsonify({
        "name": "ML Model API",
        "version": "1.0.0",
        "endpoints": ["/health", "/predict"]
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({
            "error": "Model not loaded"
        }), 503
    
    data = request.get_json()
    if not data or 'features' not in data:
        return jsonify({
            "error": "Missing 'features' in request"
        }), 400
    
    try:
        features = data['features']
        prediction = model.predict([features])
        
        return jsonify({
            "success": True,
            "prediction": int(prediction[0])
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == '__main__':
    load_model()
    app.run(debug=True, port=5000)
'''

print("Complete minimal ML API:")
print(complete_api_code)

# ========== TESTING THE API ==========
print("\n" + "=" * 60)
print("TESTING THE API")
print("=" * 60)

print("""
Testing with curl:
------------------

# Health check
curl http://localhost:5000/health

# Make prediction
curl -X POST http://localhost:5000/predict \\
     -H "Content-Type: application/json" \\
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

Testing with Python requests:
-----------------------------

import requests

# Health check
response = requests.get("http://localhost:5000/health")
print(response.json())

# Make prediction
response = requests.post(
    "http://localhost:5000/predict",
    json={"features": [5.1, 3.5, 1.4, 0.2]}
)
print(response.json())
""")

# ========== PRACTICAL: CREATE A RUNNABLE API ==========
print("\n" + "=" * 60)
print("PRACTICAL: DEMO API (If Flask installed)")
print("=" * 60)

if FLASK_AVAILABLE:
    print("""
To run the demo API:
1. Copy the complete API code above to a file (e.g., app.py)
2. Create a model file or use the prediction endpoint stub
3. Run: python app.py
4. Visit: http://localhost:5000/

Or run the provided mini_projects/01_iris_classifier_api.py
""")
    
    # Create a demo that doesn't start a server
    app = Flask(__name__)
    
    @app.route('/')
    def demo_home():
        return jsonify({"message": "Demo API"})
    
    @app.route('/health')
    def demo_health():
        return jsonify({"status": "healthy"})
    
    # Test with Flask test client
    print("\nDemo using Flask test client:")
    with app.test_client() as client:
        response = client.get('/')
        print(f"GET /: {response.get_json()}")
        
        response = client.get('/health')
        print(f"GET /health: {response.get_json()}")

else:
    print("Install Flask to run demo: pip install flask")

print("\n" + "=" * 60)
print("✅ Flask API Basics - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Flask is perfect for ML microservices
2. Use @app.route() to define endpoints
3. Use request.get_json() for input
4. Use jsonify() for JSON responses
5. Return appropriate status codes
6. Load model at startup, not per request

Next: Building Prediction APIs →
""")
