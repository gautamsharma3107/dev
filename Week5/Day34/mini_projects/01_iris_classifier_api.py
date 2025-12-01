"""
MINI PROJECT 1: Iris Classifier API
====================================
A complete Flask API for Iris flower classification

Features:
1. Train and save a model
2. Load model at startup
3. /predict endpoint
4. /health and /info endpoints
5. Error handling throughout

Run: python 01_iris_classifier_api.py
Test: curl http://localhost:5000/predict -X POST \
      -H "Content-Type: application/json" \
      -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
"""

import os
import json
import time
import pickle
from datetime import datetime

# Check for required packages
try:
    from flask import Flask, request, jsonify
    FLASK_AVAILABLE = True
except ImportError:
    print("Flask not installed. Run: pip install flask")
    FLASK_AVAILABLE = False

try:
    from sklearn.datasets import load_iris
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    import joblib
    SKLEARN_AVAILABLE = True
except ImportError:
    print("scikit-learn not installed. Run: pip install scikit-learn")
    SKLEARN_AVAILABLE = False

# ========== CONFIGURATION ==========
MODEL_PATH = "iris_model.joblib"
CLASS_NAMES = ["setosa", "versicolor", "virginica"]
FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

# ========== MODEL TRAINING ==========
def train_and_save_model():
    """Train model if it doesn't exist."""
    if not SKLEARN_AVAILABLE:
        print("Cannot train model without scikit-learn")
        return None
    
    print("Training new model...")
    
    # Load data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    
    # Train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy:.4f}")
    
    # Save
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    
    # Save metadata
    metadata = {
        "model_type": "RandomForestClassifier",
        "accuracy": float(accuracy),
        "n_estimators": 100,
        "features": FEATURE_NAMES,
        "classes": CLASS_NAMES,
        "created_at": datetime.now().isoformat()
    }
    with open(MODEL_PATH.replace('.joblib', '_meta.json'), 'w') as f:
        json.dump(metadata, f, indent=4)
    
    return model

# ========== LOAD MODEL ==========
def load_model():
    """Load model from file or train new one."""
    global model
    
    if os.path.exists(MODEL_PATH) and SKLEARN_AVAILABLE:
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")
    elif SKLEARN_AVAILABLE:
        model = train_and_save_model()
    else:
        model = None
        print("Model not available")
    
    return model

# ========== VALIDATION ==========
def validate_features(data):
    """Validate input features."""
    if data is None:
        return False, "No JSON data provided", None
    
    if 'features' not in data:
        return False, "Missing 'features' field", None
    
    features = data['features']
    
    if not isinstance(features, list):
        return False, "'features' must be a list", None
    
    if len(features) != 4:
        return False, f"Expected 4 features, got {len(features)}", None
    
    for i, val in enumerate(features):
        if not isinstance(val, (int, float)):
            return False, f"Feature {FEATURE_NAMES[i]} must be numeric", None
    
    return True, None, features

# ========== CREATE FLASK APP ==========
if FLASK_AVAILABLE:
    app = Flask(__name__)
    model = None
    
    # ========== ROUTES ==========
    @app.route('/')
    def home():
        """Welcome endpoint."""
        return jsonify({
            "name": "Iris Classifier API",
            "version": "1.0.0",
            "description": "Classify Iris flowers based on sepal/petal measurements",
            "endpoints": {
                "GET /": "This info",
                "GET /health": "Health check",
                "GET /info": "Model info",
                "POST /predict": "Make prediction"
            }
        })
    
    @app.route('/health')
    def health():
        """Health check endpoint."""
        return jsonify({
            "status": "healthy" if model is not None else "degraded",
            "model_loaded": model is not None,
            "timestamp": datetime.now().isoformat()
        })
    
    @app.route('/info')
    def info():
        """Model information endpoint."""
        meta_path = MODEL_PATH.replace('.joblib', '_meta.json')
        metadata = {}
        
        if os.path.exists(meta_path):
            with open(meta_path, 'r') as f:
                metadata = json.load(f)
        
        return jsonify({
            "model_loaded": model is not None,
            "model_path": MODEL_PATH,
            "features": FEATURE_NAMES,
            "classes": CLASS_NAMES,
            "metadata": metadata
        })
    
    @app.route('/predict', methods=['POST'])
    def predict():
        """Prediction endpoint."""
        request_id = f"req_{int(time.time()*1000)}"
        start_time = time.time()
        
        # Check model
        if model is None:
            return jsonify({
                "success": False,
                "error": {
                    "code": "MODEL_NOT_LOADED",
                    "message": "Model is not available"
                },
                "request_id": request_id
            }), 503
        
        # Validate input
        data = request.get_json()
        is_valid, error, features = validate_features(data)
        
        if not is_valid:
            return jsonify({
                "success": False,
                "error": {
                    "code": "VALIDATION_ERROR",
                    "message": error
                },
                "request_id": request_id
            }), 400
        
        try:
            # Make prediction
            prediction = model.predict([features])[0]
            probabilities = model.predict_proba([features])[0]
            
            processing_time = time.time() - start_time
            
            return jsonify({
                "success": True,
                "prediction": {
                    "class_id": int(prediction),
                    "class_name": CLASS_NAMES[prediction],
                    "confidence": round(float(max(probabilities)), 4),
                    "probabilities": {
                        CLASS_NAMES[i]: round(float(p), 4)
                        for i, p in enumerate(probabilities)
                    }
                },
                "metadata": {
                    "request_id": request_id,
                    "processing_time_ms": round(processing_time * 1000, 2),
                    "model_version": "1.0.0"
                }
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {
                    "code": "PREDICTION_ERROR",
                    "message": f"Prediction failed: {str(e)}"
                },
                "request_id": request_id
            }), 500
    
    @app.route('/features')
    def features():
        """Feature information endpoint."""
        return jsonify({
            "features": [
                {
                    "name": "sepal_length",
                    "description": "Sepal length in cm",
                    "type": "float",
                    "range": {"min": 4.0, "max": 8.0}
                },
                {
                    "name": "sepal_width",
                    "description": "Sepal width in cm",
                    "type": "float",
                    "range": {"min": 2.0, "max": 4.5}
                },
                {
                    "name": "petal_length",
                    "description": "Petal length in cm",
                    "type": "float",
                    "range": {"min": 1.0, "max": 7.0}
                },
                {
                    "name": "petal_width",
                    "description": "Petal width in cm",
                    "type": "float",
                    "range": {"min": 0.1, "max": 2.5}
                }
            ],
            "classes": CLASS_NAMES
        })
    
    # ========== ERROR HANDLERS ==========
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "success": False,
            "error": {
                "code": "NOT_FOUND",
                "message": "Endpoint not found"
            }
        }), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            "success": False,
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Internal server error"
            }
        }), 500

# ========== MAIN ==========
if __name__ == '__main__':
    print("=" * 50)
    print("IRIS CLASSIFIER API")
    print("=" * 50)
    
    if not FLASK_AVAILABLE:
        print("Flask is required. Install with: pip install flask")
        exit(1)
    
    # Load or train model
    model = load_model()
    
    print("\nStarting server...")
    print("Endpoints:")
    print("  GET  /         - API info")
    print("  GET  /health   - Health check")
    print("  GET  /info     - Model info")
    print("  GET  /features - Feature info")
    print("  POST /predict  - Make prediction")
    print("\nTest with:")
    print('  curl http://localhost:5000/predict -X POST \\')
    print('       -H "Content-Type: application/json" \\')
    print('       -d \'{"features": [5.1, 3.5, 1.4, 0.2]}\'')
    print("=" * 50)
    
    # Run server
    app.run(debug=True, port=5000, host='0.0.0.0')
