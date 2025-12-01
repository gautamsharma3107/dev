"""
MINI PROJECT 3: Complete Model Server
=====================================
A production-ready model server with multiple models,
versioning, and comprehensive API

Features:
1. Multiple model support
2. Model versioning
3. Batch predictions
4. Request logging
5. Health monitoring
6. API documentation

This is a complete example combining all Day 34 concepts.

Run: python 03_model_server.py
"""

import os
import json
import time
import logging
from datetime import datetime
from functools import wraps

try:
    from flask import Flask, request, jsonify
    FLASK_AVAILABLE = True
except ImportError:
    print("Flask not installed. Run: pip install flask")
    FLASK_AVAILABLE = False

try:
    import joblib
    JOBLIB_AVAILABLE = True
except ImportError:
    JOBLIB_AVAILABLE = False

# ========== LOGGING SETUP ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('model_server')

# ========== CUSTOM ERRORS ==========
class APIError(Exception):
    """Base API error."""
    def __init__(self, message, code="ERROR", status_code=500):
        self.message = message
        self.code = code
        self.status_code = status_code

class ValidationError(APIError):
    def __init__(self, message, field=None):
        super().__init__(message, "VALIDATION_ERROR", 400)
        self.field = field

class ModelNotFoundError(APIError):
    def __init__(self, model_name):
        super().__init__(f"Model '{model_name}' not found", "MODEL_NOT_FOUND", 404)

class PredictionError(APIError):
    def __init__(self, message):
        super().__init__(message, "PREDICTION_ERROR", 500)

# ========== MODEL REGISTRY ==========
class ModelRegistry:
    """
    Registry for managing multiple models.
    """
    
    def __init__(self, models_dir="models"):
        self.models_dir = models_dir
        self._models = {}
        self._metadata = {}
        os.makedirs(models_dir, exist_ok=True)
    
    def register(self, name, model, metadata=None):
        """Register a model."""
        self._models[name] = model
        self._metadata[name] = metadata or {}
        self._metadata[name]["registered_at"] = datetime.now().isoformat()
        logger.info(f"Registered model: {name}")
    
    def get(self, name):
        """Get a model by name."""
        if name not in self._models:
            raise ModelNotFoundError(name)
        return self._models[name]
    
    def get_metadata(self, name):
        """Get model metadata."""
        if name not in self._metadata:
            raise ModelNotFoundError(name)
        return self._metadata[name]
    
    def list_models(self):
        """List all registered models."""
        return list(self._models.keys())
    
    def load_from_file(self, name, filepath, metadata=None):
        """Load model from file and register."""
        if not JOBLIB_AVAILABLE:
            logger.warning("joblib not available, cannot load model")
            return None
        
        try:
            model = joblib.load(filepath)
            self.register(name, model, metadata)
            return model
        except Exception as e:
            logger.error(f"Failed to load model from {filepath}: {e}")
            raise
    
    def is_loaded(self, name):
        """Check if model is loaded."""
        return name in self._models

# ========== REQUEST TRACKER ==========
class RequestTracker:
    """Track API requests for monitoring."""
    
    def __init__(self):
        self.requests = []
        self.max_history = 1000
    
    def log_request(self, endpoint, model_name, success, latency_ms):
        """Log a request."""
        self.requests.append({
            "timestamp": datetime.now().isoformat(),
            "endpoint": endpoint,
            "model": model_name,
            "success": success,
            "latency_ms": latency_ms
        })
        
        # Keep only recent history
        if len(self.requests) > self.max_history:
            self.requests = self.requests[-self.max_history:]
    
    def get_stats(self, minutes=5):
        """Get recent request statistics."""
        cutoff = datetime.now().timestamp() - (minutes * 60)
        recent = [r for r in self.requests 
                  if datetime.fromisoformat(r["timestamp"]).timestamp() > cutoff]
        
        if not recent:
            return {
                "total_requests": 0,
                "success_rate": 0,
                "avg_latency_ms": 0
            }
        
        successes = sum(1 for r in recent if r["success"])
        latencies = [r["latency_ms"] for r in recent]
        
        return {
            "total_requests": len(recent),
            "success_rate": round(successes / len(recent), 4),
            "avg_latency_ms": round(sum(latencies) / len(latencies), 2),
            "period_minutes": minutes
        }

# ========== DEMO MODEL ==========
class DemoModel:
    """Demo classifier for testing without sklearn."""
    
    def __init__(self, name="demo"):
        self.name = name
        self.classes = ["class_0", "class_1", "class_2"]
    
    def predict(self, X):
        """Simple demo prediction."""
        results = []
        for features in X:
            # Simple rule-based prediction
            if sum(features) < 10:
                results.append(0)
            elif sum(features) < 15:
                results.append(1)
            else:
                results.append(2)
        return results
    
    def predict_proba(self, X):
        """Return mock probabilities."""
        results = []
        for features in X:
            pred = self.predict([features])[0]
            probs = [0.1, 0.1, 0.1]
            probs[pred] = 0.8
            results.append(probs)
        return results

# ========== CREATE FLASK APP ==========
if FLASK_AVAILABLE:
    app = Flask(__name__)
    
    # Initialize components
    registry = ModelRegistry()
    tracker = RequestTracker()
    
    # Register demo model
    demo_model = DemoModel("demo_classifier")
    registry.register("demo", demo_model, {
        "type": "DemoModel",
        "features": 4,
        "classes": demo_model.classes,
        "version": "1.0.0"
    })
    
    # ========== DECORATORS ==========
    def handle_errors(f):
        """Error handling decorator."""
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except APIError as e:
                logger.warning(f"API Error: {e.code} - {e.message}")
                return jsonify({
                    "success": False,
                    "error": {"code": e.code, "message": e.message}
                }), e.status_code
            except Exception as e:
                logger.exception("Unexpected error")
                return jsonify({
                    "success": False,
                    "error": {"code": "INTERNAL_ERROR", "message": "An error occurred"}
                }), 500
        return decorated
    
    def track_request(endpoint):
        """Request tracking decorator."""
        def decorator(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                start = time.time()
                try:
                    result = f(*args, **kwargs)
                    latency = (time.time() - start) * 1000
                    
                    # Get model name from request if available
                    data = request.get_json() or {}
                    model_name = data.get('model', kwargs.get('model_name', 'unknown'))
                    
                    tracker.log_request(endpoint, model_name, True, latency)
                    return result
                except Exception as e:
                    latency = (time.time() - start) * 1000
                    tracker.log_request(endpoint, 'error', False, latency)
                    raise
            return decorated
        return decorator
    
    # ========== ROUTES ==========
    @app.route('/')
    def home():
        """API documentation."""
        return jsonify({
            "name": "Model Server API",
            "version": "1.0.0",
            "description": "Multi-model serving API",
            "endpoints": {
                "GET /": "API documentation",
                "GET /health": "Health check",
                "GET /stats": "Request statistics",
                "GET /models": "List models",
                "GET /models/<name>": "Model info",
                "POST /predict/<model_name>": "Single prediction",
                "POST /predict/<model_name>/batch": "Batch predictions"
            }
        })
    
    @app.route('/health')
    def health():
        """Health check."""
        models = registry.list_models()
        return jsonify({
            "status": "healthy",
            "models_loaded": len(models),
            "model_names": models,
            "timestamp": datetime.now().isoformat()
        })
    
    @app.route('/stats')
    def stats():
        """Request statistics."""
        return jsonify({
            "success": True,
            "stats": tracker.get_stats(5)
        })
    
    @app.route('/models')
    def list_models():
        """List all models."""
        models = []
        for name in registry.list_models():
            meta = registry.get_metadata(name)
            models.append({
                "name": name,
                "version": meta.get("version", "unknown"),
                "type": meta.get("type", "unknown")
            })
        
        return jsonify({
            "success": True,
            "models": models,
            "count": len(models)
        })
    
    @app.route('/models/<name>')
    @handle_errors
    def model_info(name):
        """Get model information."""
        registry.get(name)  # Check exists
        metadata = registry.get_metadata(name)
        
        return jsonify({
            "success": True,
            "model": {
                "name": name,
                **metadata
            }
        })
    
    @app.route('/predict/<model_name>', methods=['POST'])
    @handle_errors
    @track_request('/predict')
    def predict(model_name):
        """Make single prediction."""
        model = registry.get(model_name)
        data = request.get_json()
        
        if not data or 'features' not in data:
            raise ValidationError("Missing 'features' field", "features")
        
        features = data['features']
        
        if not isinstance(features, list):
            raise ValidationError("'features' must be a list", "features")
        
        start = time.time()
        
        try:
            prediction = model.predict([features])[0]
            probabilities = model.predict_proba([features])[0]
        except Exception as e:
            raise PredictionError(f"Model prediction failed: {str(e)}")
        
        latency = (time.time() - start) * 1000
        
        meta = registry.get_metadata(model_name)
        classes = meta.get("classes", [])
        
        result = {
            "class_id": int(prediction),
            "confidence": round(float(max(probabilities)), 4),
            "probabilities": [round(float(p), 4) for p in probabilities]
        }
        
        if classes and prediction < len(classes):
            result["class_name"] = classes[prediction]
        
        return jsonify({
            "success": True,
            "prediction": result,
            "metadata": {
                "model": model_name,
                "version": meta.get("version", "unknown"),
                "latency_ms": round(latency, 2)
            }
        })
    
    @app.route('/predict/<model_name>/batch', methods=['POST'])
    @handle_errors
    @track_request('/predict/batch')
    def predict_batch(model_name):
        """Make batch predictions."""
        model = registry.get(model_name)
        data = request.get_json()
        
        if not data or 'instances' not in data:
            raise ValidationError("Missing 'instances' field", "instances")
        
        instances = data['instances']
        
        if not isinstance(instances, list):
            raise ValidationError("'instances' must be a list", "instances")
        
        if len(instances) > 100:
            raise ValidationError("Maximum 100 instances per batch", "instances")
        
        meta = registry.get_metadata(model_name)
        classes = meta.get("classes", [])
        
        results = []
        errors = []
        
        start = time.time()
        
        for i, instance in enumerate(instances):
            try:
                if 'features' not in instance:
                    errors.append({"index": i, "error": "Missing features"})
                    results.append(None)
                    continue
                
                features = instance['features']
                prediction = model.predict([features])[0]
                proba = model.predict_proba([features])[0]
                
                result = {
                    "class_id": int(prediction),
                    "confidence": round(float(max(proba)), 4)
                }
                
                if classes and prediction < len(classes):
                    result["class_name"] = classes[prediction]
                
                results.append(result)
                
            except Exception as e:
                errors.append({"index": i, "error": str(e)})
                results.append(None)
        
        latency = (time.time() - start) * 1000
        
        return jsonify({
            "success": len(errors) == 0,
            "predictions": results,
            "errors": errors if errors else None,
            "summary": {
                "total": len(instances),
                "successful": len(instances) - len(errors),
                "failed": len(errors)
            },
            "metadata": {
                "model": model_name,
                "latency_ms": round(latency, 2)
            }
        })
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({
            "success": False,
            "error": {"code": "NOT_FOUND", "message": "Endpoint not found"}
        }), 404

# ========== MAIN ==========
if __name__ == '__main__':
    print("=" * 60)
    print("MODEL SERVER")
    print("=" * 60)
    
    if not FLASK_AVAILABLE:
        print("Flask is required. Install with: pip install flask")
        exit(1)
    
    print(f"\nModels loaded: {registry.list_models()}")
    print("\nEndpoints:")
    print("  GET  /                         - API docs")
    print("  GET  /health                   - Health check")
    print("  GET  /stats                    - Request stats")
    print("  GET  /models                   - List models")
    print("  GET  /models/<name>            - Model info")
    print("  POST /predict/<model>/         - Single prediction")
    print("  POST /predict/<model>/batch    - Batch predictions")
    print("\nTest with:")
    print('  curl http://localhost:5002/predict/demo -X POST \\')
    print('       -H "Content-Type: application/json" \\')
    print('       -d \'{"features": [5.1, 3.5, 1.4, 0.2]}\'')
    print("=" * 60)
    
    app.run(debug=True, port=5002, host='0.0.0.0')
