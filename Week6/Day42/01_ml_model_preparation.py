"""
Day 42 - ML Model Preparation for Production
==============================================
Learn: Saving, loading, and preparing ML models for deployment

Key Concepts:
- Model serialization with pickle and joblib
- Model versioning
- Input validation and preprocessing
- Creating prediction pipelines
"""

# ========== SETUP ==========
print("=" * 60)
print("ML MODEL PREPARATION FOR PRODUCTION")
print("=" * 60)

# Required imports
import pickle
import json
import numpy as np
from datetime import datetime

# Note: In production, you would use scikit-learn
# For demonstration, we'll create a simple model class

# ========== SIMPLE MODEL SIMULATION ==========
print("\n" + "=" * 60)
print("1. CREATING A SIMPLE MODEL")
print("=" * 60)


class SimpleLinearModel:
    """
    A simple linear regression model for demonstration.
    In production, you would use sklearn.linear_model.LinearRegression
    """
    
    def __init__(self):
        self.weights = None
        self.bias = None
        self.is_fitted = False
        self.version = "1.0.0"
        self.created_at = None
    
    def fit(self, X, y):
        """Train the model using simple least squares"""
        X = np.array(X)
        y = np.array(y)
        
        # Add bias term
        n_samples = X.shape[0]
        X_with_bias = np.c_[np.ones(n_samples), X]
        
        # Solve using normal equation
        theta = np.linalg.lstsq(X_with_bias, y, rcond=None)[0]
        self.bias = theta[0]
        self.weights = theta[1:]
        self.is_fitted = True
        self.created_at = datetime.now().isoformat()
        
        print(f"Model trained successfully!")
        print(f"Weights: {self.weights}")
        print(f"Bias: {self.bias}")
        return self
    
    def predict(self, X):
        """Make predictions"""
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")
        X = np.array(X)
        return np.dot(X, self.weights) + self.bias
    
    def get_metadata(self):
        """Get model metadata"""
        return {
            "version": self.version,
            "created_at": self.created_at,
            "is_fitted": self.is_fitted,
            "n_features": len(self.weights) if self.weights is not None else 0
        }


# Create and train a simple model
print("\nTraining a simple linear model...")
X_train = [[1], [2], [3], [4], [5]]
y_train = [2, 4, 6, 8, 10]  # y = 2x

model = SimpleLinearModel()
model.fit(X_train, y_train)

# Test prediction
print(f"\nPrediction for X=6: {model.predict([[6]])[0]:.2f} (expected: 12)")
print(f"Prediction for X=10: {model.predict([[10]])[0]:.2f} (expected: 20)")

# ========== SAVING MODELS WITH PICKLE ==========
print("\n" + "=" * 60)
print("2. SAVING MODELS WITH PICKLE")
print("=" * 60)


def save_model_pickle(model, filepath):
    """Save model using pickle"""
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to: {filepath}")


def load_model_pickle(filepath):
    """Load model using pickle"""
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    print(f"Model loaded from: {filepath}")
    return model


# Save the model
save_model_pickle(model, '/tmp/model.pkl')

# Load and test
loaded_model = load_model_pickle('/tmp/model.pkl')
print(f"Loaded model prediction for X=6: {loaded_model.predict([[6]])[0]:.2f}")

# ========== SAVING MODEL METADATA ==========
print("\n" + "=" * 60)
print("3. SAVING MODEL METADATA")
print("=" * 60)


def save_model_with_metadata(model, model_path, metadata_path):
    """Save model along with its metadata"""
    # Save model
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    # Save metadata
    metadata = model.get_metadata()
    metadata['model_path'] = model_path
    metadata['saved_at'] = datetime.now().isoformat()
    
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Model saved to: {model_path}")
    print(f"Metadata saved to: {metadata_path}")
    print(f"Metadata: {json.dumps(metadata, indent=2)}")


save_model_with_metadata(
    model,
    '/tmp/production_model.pkl',
    '/tmp/model_metadata.json'
)

# ========== MODEL WRAPPER FOR PRODUCTION ==========
print("\n" + "=" * 60)
print("4. PRODUCTION MODEL WRAPPER")
print("=" * 60)


class ProductionModel:
    """
    Wrapper class for production ML models.
    Handles loading, validation, and prediction.
    """
    
    def __init__(self, model_path, metadata_path=None):
        self.model_path = model_path
        self.metadata_path = metadata_path
        self.model = None
        self.metadata = None
        self._load()
    
    def _load(self):
        """Load model and metadata"""
        # Load model
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
        print(f"Model loaded: {self.model_path}")
        
        # Load metadata if available
        if self.metadata_path:
            with open(self.metadata_path, 'r') as f:
                self.metadata = json.load(f)
            print(f"Metadata loaded: {self.metadata_path}")
    
    def validate_input(self, X):
        """Validate input data"""
        if not isinstance(X, (list, np.ndarray)):
            raise ValueError("Input must be a list or numpy array")
        
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        
        expected_features = self.metadata.get('n_features', 1) if self.metadata else 1
        if X.shape[1] != expected_features:
            raise ValueError(
                f"Expected {expected_features} features, got {X.shape[1]}"
            )
        
        return X
    
    def predict(self, X):
        """Make validated prediction"""
        X = self.validate_input(X)
        predictions = self.model.predict(X)
        return {
            'predictions': predictions.tolist(),
            'model_version': self.metadata.get('version', 'unknown'),
            'timestamp': datetime.now().isoformat()
        }
    
    def get_info(self):
        """Get model information"""
        return {
            'model_path': self.model_path,
            'metadata': self.metadata,
            'is_loaded': self.model is not None
        }


# Use production model wrapper
print("\nCreating production model wrapper...")
prod_model = ProductionModel(
    '/tmp/production_model.pkl',
    '/tmp/model_metadata.json'
)

print(f"\nModel info: {json.dumps(prod_model.get_info(), indent=2, default=str)}")

# Make prediction
result = prod_model.predict([[7]])
print(f"\nPrediction result: {json.dumps(result, indent=2)}")

# ========== INPUT PREPROCESSING ==========
print("\n" + "=" * 60)
print("5. INPUT PREPROCESSING")
print("=" * 60)


class DataPreprocessor:
    """
    Preprocessor for ML model inputs.
    Handles scaling, encoding, and validation.
    """
    
    def __init__(self):
        self.fitted = False
        self.mean = None
        self.std = None
    
    def fit(self, X):
        """Fit preprocessor on training data"""
        X = np.array(X)
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        self.std[self.std == 0] = 1  # Avoid division by zero
        self.fitted = True
        print(f"Preprocessor fitted. Mean: {self.mean}, Std: {self.std}")
        return self
    
    def transform(self, X):
        """Transform input data"""
        if not self.fitted:
            raise ValueError("Preprocessor not fitted. Call fit() first.")
        X = np.array(X)
        return (X - self.mean) / self.std
    
    def fit_transform(self, X):
        """Fit and transform in one step"""
        return self.fit(X).transform(X)
    
    def inverse_transform(self, X):
        """Reverse the transformation"""
        X = np.array(X)
        return X * self.std + self.mean


# Example usage
print("\nDemonstrating preprocessing...")
raw_data = [[100], [200], [300], [400], [500]]

preprocessor = DataPreprocessor()
preprocessor.fit(raw_data)

transformed = preprocessor.transform([[150]])
print(f"Original: 150 -> Transformed: {transformed[0][0]:.4f}")

reversed_val = preprocessor.inverse_transform(transformed)
print(f"Reversed back: {reversed_val[0][0]:.2f}")

# ========== COMPLETE PREDICTION PIPELINE ==========
print("\n" + "=" * 60)
print("6. COMPLETE PREDICTION PIPELINE")
print("=" * 60)


class PredictionPipeline:
    """
    Complete prediction pipeline for production.
    Includes preprocessing, prediction, and postprocessing.
    """
    
    def __init__(self, model, preprocessor=None):
        self.model = model
        self.preprocessor = preprocessor
        self.request_count = 0
    
    def preprocess(self, X):
        """Preprocess input"""
        if self.preprocessor:
            return self.preprocessor.transform(X)
        return np.array(X)
    
    def postprocess(self, predictions):
        """Postprocess predictions"""
        # Example: clip predictions to reasonable range
        predictions = np.clip(predictions, 0, 1000)
        return predictions
    
    def predict(self, X):
        """Run complete prediction pipeline"""
        self.request_count += 1
        
        # Preprocess
        X_processed = self.preprocess(X)
        
        # Predict
        raw_predictions = self.model.predict(X_processed)
        
        # Postprocess
        final_predictions = self.postprocess(raw_predictions)
        
        return {
            'predictions': final_predictions.tolist(),
            'request_id': self.request_count,
            'timestamp': datetime.now().isoformat()
        }


# Create pipeline (without preprocessor for simplicity)
print("\nCreating prediction pipeline...")
pipeline = PredictionPipeline(model)

# Make predictions
print("\nPipeline predictions:")
for x in [[5], [7], [10]]:
    result = pipeline.predict(x)
    print(f"Input: {x} -> Prediction: {result['predictions'][0]:.2f}")

# ========== PRACTICAL EXERCISE ==========
print("\n" + "=" * 60)
print("7. PRACTICAL EXERCISE")
print("=" * 60)

print("""
EXERCISE: Create a production-ready model setup

Task 1: Create a multi-feature model
- Train a model with multiple features
- Save model and metadata
- Load and make predictions

Task 2: Add input validation
- Validate feature count
- Handle missing values
- Validate data types

Task 3: Create prediction logging
- Log all predictions
- Track prediction latency
- Store request metadata

SOLUTION STRUCTURE:
```python
class ProductionMLService:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
        self.logger = self.setup_logging()
    
    def load_model(self, path):
        # Load model with error handling
        pass
    
    def validate_input(self, data):
        # Validate and preprocess input
        pass
    
    def predict(self, data):
        # Make prediction with logging
        pass
    
    def log_prediction(self, input_data, prediction):
        # Log prediction for monitoring
        pass
```
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
1. Model Serialization
   - Use pickle or joblib for saving models
   - Always save metadata alongside models
   - Include version information

2. Production Wrappers
   - Create wrapper classes for models
   - Handle loading, validation, prediction
   - Make models easy to use in APIs

3. Input Validation
   - Always validate input data
   - Check feature count and types
   - Handle edge cases gracefully

4. Preprocessing Pipelines
   - Save preprocessors with models
   - Apply consistent transformations
   - Consider inverse transforms for outputs

5. Best Practices
   - Version your models
   - Log all predictions
   - Monitor model performance
   - Handle errors gracefully
""")

print("\n" + "=" * 60)
print("✅ ML Model Preparation - Complete!")
print("=" * 60)
