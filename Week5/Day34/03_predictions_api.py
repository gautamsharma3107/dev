"""
Day 34 - Handling Predictions via API
=====================================
Learn: Building robust prediction endpoints

Key Concepts:
- Input validation
- Feature preprocessing
- Prediction response formatting
- Batch predictions
"""

import json
import time
from datetime import datetime

# ========== PREDICTION ENDPOINT DESIGN ==========
print("=" * 60)
print("PREDICTION ENDPOINT DESIGN")
print("=" * 60)

print("""
A good prediction endpoint should:
1. Validate input data
2. Preprocess features if needed
3. Make prediction efficiently
4. Format response consistently
5. Handle errors gracefully
6. Log predictions for monitoring
""")

# ========== INPUT VALIDATION ==========
print("\n" + "=" * 60)
print("INPUT VALIDATION")
print("=" * 60)

def validate_prediction_input(data, expected_features=4):
    """
    Validate prediction input data.
    
    Args:
        data: Input JSON data
        expected_features: Number of expected features
        
    Returns:
        (is_valid, error_message, validated_data)
    """
    # Check if data exists
    if data is None:
        return False, "No JSON data provided", None
    
    # Check if features key exists
    if 'features' not in data:
        return False, "Missing 'features' field", None
    
    features = data['features']
    
    # Check if features is a list
    if not isinstance(features, list):
        return False, "'features' must be a list", None
    
    # Check feature count
    if len(features) != expected_features:
        return False, f"Expected {expected_features} features, got {len(features)}", None
    
    # Check if all features are numeric
    for i, f in enumerate(features):
        if not isinstance(f, (int, float)):
            return False, f"Feature at index {i} must be numeric", None
    
    return True, None, features


# Demo validation
print("\nValidation examples:")
print("-" * 40)

test_cases = [
    (None, "No data"),
    ({}, "Empty dict"),
    ({"features": "not a list"}, "Features not a list"),
    ({"features": [1, 2]}, "Wrong feature count"),
    ({"features": [1, 2, "three", 4]}, "Non-numeric feature"),
    ({"features": [5.1, 3.5, 1.4, 0.2]}, "Valid input"),
]

for data, description in test_cases:
    is_valid, error, features = validate_prediction_input(data)
    status = "✅ Valid" if is_valid else f"❌ Invalid: {error}"
    print(f"{description:25} -> {status}")

# ========== PREDICTION RESPONSE FORMAT ==========
print("\n" + "=" * 60)
print("PREDICTION RESPONSE FORMAT")
print("=" * 60)

def format_prediction_response(
    prediction,
    probabilities=None,
    class_names=None,
    model_version="1.0.0",
    request_id=None,
    processing_time=None
):
    """
    Format prediction response consistently.
    
    Args:
        prediction: Model prediction (class index or value)
        probabilities: List of class probabilities (optional)
        class_names: List of class names for mapping
        model_version: Version of the model used
        request_id: Unique request identifier
        processing_time: Time taken for prediction
        
    Returns:
        Formatted response dictionary
    """
    response = {
        "success": True,
        "prediction": {
            "class_id": int(prediction) if hasattr(prediction, '__int__') else prediction
        },
        "metadata": {
            "model_version": model_version,
            "timestamp": datetime.now().isoformat()
        }
    }
    
    # Add class name if available
    if class_names and isinstance(prediction, int) and prediction < len(class_names):
        response["prediction"]["class_name"] = class_names[prediction]
    
    # Add probabilities if available
    if probabilities is not None:
        response["prediction"]["probabilities"] = [round(p, 4) for p in probabilities]
        response["prediction"]["confidence"] = round(max(probabilities), 4)
    
    # Add request ID if provided
    if request_id:
        response["metadata"]["request_id"] = request_id
    
    # Add processing time if provided
    if processing_time:
        response["metadata"]["processing_time_ms"] = round(processing_time * 1000, 2)
    
    return response


# Demo response formatting
print("\nFormatted prediction response:")
print("-" * 40)

response = format_prediction_response(
    prediction=0,
    probabilities=[0.95, 0.03, 0.02],
    class_names=["setosa", "versicolor", "virginica"],
    model_version="1.0.0",
    request_id="req_12345",
    processing_time=0.015
)

print(json.dumps(response, indent=2))

# ========== COMPLETE PREDICTION ENDPOINT ==========
print("\n" + "=" * 60)
print("COMPLETE PREDICTION ENDPOINT")
print("=" * 60)

prediction_endpoint_code = '''
from flask import Flask, request, jsonify
import time
import uuid

app = Flask(__name__)

# Class names for iris dataset
IRIS_CLASSES = ["setosa", "versicolor", "virginica"]

@app.route('/predict', methods=['POST'])
def predict():
    """
    Make prediction from input features.
    
    Request body:
    {
        "features": [5.1, 3.5, 1.4, 0.2]
    }
    
    Response:
    {
        "success": true,
        "prediction": {
            "class_id": 0,
            "class_name": "setosa",
            "confidence": 0.95,
            "probabilities": [0.95, 0.03, 0.02]
        },
        "metadata": {...}
    }
    """
    request_id = str(uuid.uuid4())[:8]
    start_time = time.time()
    
    # Get JSON data
    data = request.get_json()
    
    # Validate input
    is_valid, error, features = validate_prediction_input(data)
    if not is_valid:
        return jsonify({
            "success": False,
            "error": error,
            "request_id": request_id
        }), 400
    
    try:
        # Make prediction (placeholder - replace with actual model)
        # prediction = model.predict([features])[0]
        # probabilities = model.predict_proba([features])[0]
        
        prediction = 0  # Demo
        probabilities = [0.95, 0.03, 0.02]  # Demo
        
        # Format response
        processing_time = time.time() - start_time
        response = format_prediction_response(
            prediction=prediction,
            probabilities=probabilities,
            class_names=IRIS_CLASSES,
            request_id=request_id,
            processing_time=processing_time
        )
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Prediction failed: {str(e)}",
            "request_id": request_id
        }), 500
'''

print("Complete prediction endpoint:")
print(prediction_endpoint_code)

# ========== BATCH PREDICTIONS ==========
print("\n" + "=" * 60)
print("BATCH PREDICTIONS")
print("=" * 60)

print("""
For efficiency, support batch predictions:
- Accept list of feature arrays
- Return list of predictions
- Process in parallel if possible
""")

batch_endpoint_code = '''
@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    """
    Make batch predictions.
    
    Request body:
    {
        "instances": [
            {"features": [5.1, 3.5, 1.4, 0.2]},
            {"features": [6.2, 3.4, 5.4, 2.3]}
        ]
    }
    """
    data = request.get_json()
    
    if not data or 'instances' not in data:
        return jsonify({
            "error": "Missing 'instances' field"
        }), 400
    
    instances = data['instances']
    
    if not isinstance(instances, list):
        return jsonify({
            "error": "'instances' must be a list"
        }), 400
    
    if len(instances) > 100:  # Limit batch size
        return jsonify({
            "error": "Maximum batch size is 100"
        }), 400
    
    predictions = []
    errors = []
    
    for i, instance in enumerate(instances):
        is_valid, error, features = validate_prediction_input(instance)
        
        if not is_valid:
            errors.append({"index": i, "error": error})
            predictions.append(None)
            continue
        
        try:
            # Make prediction
            # pred = model.predict([features])[0]
            pred = 0  # Demo
            predictions.append({
                "class_id": pred,
                "class_name": IRIS_CLASSES[pred]
            })
        except Exception as e:
            errors.append({"index": i, "error": str(e)})
            predictions.append(None)
    
    return jsonify({
        "success": len(errors) == 0,
        "predictions": predictions,
        "errors": errors if errors else None,
        "total": len(instances),
        "successful": len(instances) - len(errors)
    })
'''

print("Batch prediction endpoint:")
print(batch_endpoint_code)

# ========== PREPROCESSING IN API ==========
print("\n" + "=" * 60)
print("PREPROCESSING IN API")
print("=" * 60)

print("""
If your model requires preprocessing, include it in the API.
Save preprocessor along with model!
""")

preprocessing_code = '''
import pickle
import numpy as np

# Load model and preprocessor at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict_with_preprocessing():
    data = request.get_json()
    features = data.get('features')
    
    # Preprocess features
    features_array = np.array([features])
    features_scaled = scaler.transform(features_array)
    
    # Make prediction
    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]
    
    return jsonify({
        "prediction": int(prediction),
        "confidence": float(max(probabilities))
    })
'''

print("Preprocessing in API:")
print(preprocessing_code)

# ========== FEATURE NAMES ENDPOINT ==========
print("\n" + "=" * 60)
print("FEATURE NAMES ENDPOINT")
print("=" * 60)

feature_endpoint_code = '''
@app.route('/features', methods=['GET'])
def get_features():
    """Return expected feature information."""
    return jsonify({
        "features": [
            {
                "name": "sepal_length",
                "type": "float",
                "description": "Sepal length in cm",
                "range": {"min": 4.0, "max": 8.0}
            },
            {
                "name": "sepal_width",
                "type": "float",
                "description": "Sepal width in cm",
                "range": {"min": 2.0, "max": 4.5}
            },
            {
                "name": "petal_length",
                "type": "float",
                "description": "Petal length in cm",
                "range": {"min": 1.0, "max": 7.0}
            },
            {
                "name": "petal_width",
                "type": "float",
                "description": "Petal width in cm",
                "range": {"min": 0.1, "max": 2.5}
            }
        ],
        "total_features": 4
    })
'''

print("Feature information endpoint:")
print(feature_endpoint_code)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL: SIMULATED PREDICTIONS")
print("=" * 60)

class DemoModel:
    """Demo model for testing."""
    
    def __init__(self):
        self.classes = ["setosa", "versicolor", "virginica"]
    
    def predict(self, features):
        """Simple rule-based prediction for demo."""
        # Use petal length (index 2) for simple classification
        petal_length = features[0][2] if isinstance(features[0], list) else features[2]
        
        if petal_length < 2.5:
            return [0]
        elif petal_length < 5.0:
            return [1]
        else:
            return [2]
    
    def predict_proba(self, features):
        """Return mock probabilities."""
        pred = self.predict(features)[0]
        probs = [0.05, 0.05, 0.05]
        probs[pred] = 0.90
        return [probs]


# Demo prediction flow
print("\nSimulated prediction flow:")
print("-" * 40)

demo_model = DemoModel()

# Simulate incoming requests
test_requests = [
    {"features": [5.1, 3.5, 1.4, 0.2]},  # setosa
    {"features": [6.0, 2.9, 4.5, 1.5]},  # versicolor
    {"features": [6.3, 3.3, 6.0, 2.5]},  # virginica
]

for i, req in enumerate(test_requests, 1):
    start = time.time()
    
    # Validate
    is_valid, error, features = validate_prediction_input(req)
    
    if is_valid:
        # Predict
        pred = demo_model.predict([features])[0]
        probs = demo_model.predict_proba([features])[0]
        
        # Format
        processing_time = time.time() - start
        response = format_prediction_response(
            prediction=pred,
            probabilities=probs,
            class_names=demo_model.classes,
            request_id=f"req_{i}",
            processing_time=processing_time
        )
        
        print(f"\nRequest {i}:")
        print(f"  Input: {features}")
        print(f"  Prediction: {response['prediction']['class_name']}")
        print(f"  Confidence: {response['prediction']['confidence']:.2%}")
    else:
        print(f"\nRequest {i}: Invalid - {error}")

print("\n" + "=" * 60)
print("✅ Handling Predictions via API - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Always validate input data
2. Format responses consistently
3. Include metadata (version, time, request ID)
4. Support batch predictions for efficiency
5. Save and use preprocessors with model
6. Document expected features

Next: Error Handling →
""")
