# Day 34 Quick Reference Cheat Sheet

## Saving Models

### Pickle
```python
import pickle

# Save
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Load
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
```

### Joblib (Recommended for ML)
```python
import joblib

# Save
joblib.dump(model, "model.joblib")

# Save compressed
joblib.dump(model, "model.joblib", compress=3)

# Load
model = joblib.load("model.joblib")
```

### Save with Metadata
```python
import json
from datetime import datetime

# Save metadata alongside model
metadata = {
    "model_name": "iris_classifier",
    "version": "1.0.0",
    "created_at": datetime.now().isoformat(),
    "accuracy": 0.95
}

with open("model_meta.json", "w") as f:
    json.dump(metadata, f, indent=4)
```

## Flask API Basics

### Minimal App
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features')
    # prediction = model.predict([features])
    return jsonify({"prediction": 0})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Request Handling
```python
# Get JSON body
data = request.get_json()

# Get query params
value = request.args.get('param', 'default')

# Get headers
auth = request.headers.get('Authorization')
```

### Response Patterns
```python
# Success
return jsonify({"success": True, "data": result}), 200

# Client Error
return jsonify({"error": "Invalid input"}), 400

# Server Error
return jsonify({"error": "Server error"}), 500
```

## Prediction Endpoint

### Standard Format
```python
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Validate
    if not data or 'features' not in data:
        return jsonify({"error": "Missing features"}), 400
    
    # Predict
    features = data['features']
    prediction = model.predict([features])[0]
    proba = model.predict_proba([features])[0]
    
    # Response
    return jsonify({
        "success": True,
        "prediction": {
            "class_id": int(prediction),
            "confidence": float(max(proba))
        }
    })
```

### Batch Predictions
```python
@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    instances = request.get_json().get('instances', [])
    predictions = []
    
    for instance in instances:
        pred = model.predict([instance['features']])[0]
        predictions.append({"class_id": int(pred)})
    
    return jsonify({"predictions": predictions})
```

## Input Validation

```python
def validate_features(features, expected_count=4):
    if not isinstance(features, list):
        return False, "Features must be a list"
    
    if len(features) != expected_count:
        return False, f"Expected {expected_count} features"
    
    for i, f in enumerate(features):
        if not isinstance(f, (int, float)):
            return False, f"Feature {i} must be numeric"
    
    return True, None
```

## Error Handling

### Custom Errors
```python
class ValidationError(Exception):
    def __init__(self, message, field=None):
        self.message = message
        self.field = field

class ModelNotLoadedError(Exception):
    pass
```

### Error Handler
```python
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal error"}), 500
```

### Try-Except Pattern
```python
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        prediction = model.predict([data['features']])
        return jsonify({"prediction": int(prediction[0])})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Prediction failed"}), 500
```

## HTTP Status Codes

```
200 OK           - Success
201 Created      - Resource created
400 Bad Request  - Invalid input
401 Unauthorized - Auth required
404 Not Found    - Endpoint missing
422 Unprocessable- Invalid data
429 Rate Limited - Too many requests
500 Server Error - Internal error
503 Unavailable  - Model not ready
```

## Testing with curl

```bash
# Health check
curl http://localhost:5000/health

# POST prediction
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# Batch prediction
curl -X POST http://localhost:5000/predict/batch \
     -H "Content-Type: application/json" \
     -d '{"instances": [{"features": [5.1, 3.5, 1.4, 0.2]}]}'
```

## Testing with Python

```python
import requests

# Health check
r = requests.get("http://localhost:5000/health")
print(r.json())

# Prediction
r = requests.post(
    "http://localhost:5000/predict",
    json={"features": [5.1, 3.5, 1.4, 0.2]}
)
print(r.json())
```

## Model Loading Pattern

```python
model = None

def load_model():
    global model
    model = joblib.load("model.joblib")
    print("Model loaded!")

# Load at startup
if __name__ == '__main__':
    load_model()
    app.run()
```

## Quick Response Template

```python
{
    "success": True/False,
    "prediction": {
        "class_id": 0,
        "class_name": "setosa",
        "confidence": 0.95,
        "probabilities": [0.95, 0.03, 0.02]
    },
    "metadata": {
        "model_version": "1.0.0",
        "processing_time_ms": 15
    },
    "error": {  # Only on failure
        "message": "Error description",
        "code": "ERROR_CODE"
    }
}
```

---
**Keep this handy for Day 34 topics!** 🚀
