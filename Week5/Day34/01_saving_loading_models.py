"""
Day 34 - Saving and Loading ML Models
=====================================
Learn: Model persistence with pickle and joblib

Key Concepts:
- Serialize trained models for later use
- Save models to files
- Load models for predictions
- Model versioning basics
"""

import os
import pickle
import json
from datetime import datetime

# We'll use sklearn for demo models
try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    import joblib
    SKLEARN_AVAILABLE = True
except ImportError:
    print("Note: scikit-learn not installed. Run: pip install scikit-learn")
    SKLEARN_AVAILABLE = False

# ========== WHY SAVE MODELS? ==========
print("=" * 60)
print("WHY SAVE MODELS?")
print("=" * 60)

print("""
Without saving models, you'd need to retrain every time!

Benefits of saving models:
1. No need to retrain - use pre-trained model
2. Deploy to production servers
3. Share models with team members
4. Version control your models
5. A/B testing different model versions
6. Rollback to previous versions if needed
""")

# ========== PICKLE BASICS ==========
print("\n" + "=" * 60)
print("PICKLE BASICS")
print("=" * 60)

print("""
Pickle is Python's built-in serialization module.
- Converts Python objects to byte streams
- Can save almost any Python object
- Fast and simple to use

Common functions:
- pickle.dump(obj, file)  -> Save to file
- pickle.load(file)       -> Load from file
- pickle.dumps(obj)       -> Convert to bytes
- pickle.loads(bytes)     -> Load from bytes
""")

# Demo with simple Python object
data = {
    "name": "My Model",
    "accuracy": 0.95,
    "created": str(datetime.now()),
    "features": ["feature1", "feature2", "feature3"]
}

# Save with pickle
with open("model_info.pkl", "wb") as f:
    pickle.dump(data, f)
print("✅ Saved model info with pickle")

# Load with pickle
with open("model_info.pkl", "rb") as f:
    loaded_data = pickle.load(f)
print(f"✅ Loaded: {loaded_data['name']} with accuracy {loaded_data['accuracy']}")

# ========== SAVING ML MODELS WITH PICKLE ==========
print("\n" + "=" * 60)
print("SAVING ML MODELS WITH PICKLE")
print("=" * 60)

if SKLEARN_AVAILABLE:
    # Train a simple model
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    
    # Train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"Trained model accuracy: {accuracy:.4f}")
    
    # Save model with pickle
    with open("iris_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("✅ Model saved to 'iris_model.pkl'")
    
    # Load and verify
    with open("iris_model.pkl", "rb") as f:
        loaded_model = pickle.load(f)
    
    loaded_accuracy = loaded_model.score(X_test, y_test)
    print(f"✅ Loaded model accuracy: {loaded_accuracy:.4f}")
    print(f"   Accuracy match: {accuracy == loaded_accuracy}")

# ========== JOBLIB FOR ML MODELS ==========
print("\n" + "=" * 60)
print("JOBLIB FOR ML MODELS")
print("=" * 60)

print("""
Joblib is optimized for large numpy arrays (common in ML).
- Faster than pickle for large models
- Better compression
- Recommended by scikit-learn

Usage:
- joblib.dump(obj, filename)
- joblib.load(filename)
""")

if SKLEARN_AVAILABLE:
    # Save with joblib
    joblib.dump(model, "iris_model.joblib")
    print("✅ Model saved to 'iris_model.joblib'")
    
    # Load with joblib
    loaded_model_joblib = joblib.load("iris_model.joblib")
    joblib_accuracy = loaded_model_joblib.score(X_test, y_test)
    print(f"✅ Loaded model accuracy: {joblib_accuracy:.4f}")
    
    # Compressed save
    joblib.dump(model, "iris_model_compressed.joblib", compress=3)
    print("✅ Saved compressed model")
    
    # Compare file sizes
    pkl_size = os.path.getsize("iris_model.pkl")
    joblib_size = os.path.getsize("iris_model.joblib")
    compressed_size = os.path.getsize("iris_model_compressed.joblib")
    
    print(f"\nFile sizes comparison:")
    print(f"   Pickle:            {pkl_size:,} bytes")
    print(f"   Joblib:            {joblib_size:,} bytes")
    print(f"   Joblib compressed: {compressed_size:,} bytes")

# ========== MODEL VERSIONING ==========
print("\n" + "=" * 60)
print("MODEL VERSIONING")
print("=" * 60)

print("""
Best practices for versioning:
1. Include version in filename
2. Save metadata alongside model
3. Use timestamps
4. Track model performance metrics
""")

def save_model_with_metadata(model, model_name, version, metrics):
    """Save model with metadata for tracking."""
    # Create model directory
    model_dir = "models"
    os.makedirs(model_dir, exist_ok=True)
    
    # Create metadata
    metadata = {
        "model_name": model_name,
        "version": version,
        "created_at": datetime.now().isoformat(),
        "metrics": metrics,
        "model_file": f"{model_name}_v{version}.joblib"
    }
    
    # Save model
    model_path = os.path.join(model_dir, metadata["model_file"])
    if SKLEARN_AVAILABLE and model is not None:
        joblib.dump(model, model_path)
    else:
        # Demo: create empty file
        with open(model_path, "w") as f:
            f.write("demo model")
    
    # Save metadata
    meta_path = os.path.join(model_dir, f"{model_name}_v{version}_meta.json")
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=4)
    
    print(f"✅ Saved model: {model_path}")
    print(f"✅ Saved metadata: {meta_path}")
    return metadata

# Example usage
if SKLEARN_AVAILABLE:
    save_model_with_metadata(
        model=model,
        model_name="iris_classifier",
        version="1.0.0",
        metrics={"accuracy": accuracy, "n_estimators": 100}
    )

# ========== LOADING MODELS IN PRODUCTION ==========
print("\n" + "=" * 60)
print("LOADING MODELS IN PRODUCTION")
print("=" * 60)

print("""
Production loading patterns:
1. Load once at startup
2. Cache the model in memory
3. Use singleton pattern
4. Handle loading errors gracefully
""")

class ModelLoader:
    """Singleton pattern for loading models."""
    
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def load_model(self, model_path):
        """Load model if not already loaded."""
        if self._model is None:
            try:
                if model_path.endswith('.pkl'):
                    with open(model_path, 'rb') as f:
                        self._model = pickle.load(f)
                else:
                    if SKLEARN_AVAILABLE:
                        self._model = joblib.load(model_path)
                print(f"✅ Model loaded from {model_path}")
            except FileNotFoundError:
                print(f"❌ Model file not found: {model_path}")
                raise
            except Exception as e:
                print(f"❌ Error loading model: {e}")
                raise
        return self._model
    
    def get_model(self):
        """Get the loaded model."""
        if self._model is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        return self._model
    
    def reload_model(self, model_path):
        """Force reload the model."""
        self._model = None
        return self.load_model(model_path)

# Usage example
print("\nModelLoader usage:")
if SKLEARN_AVAILABLE and os.path.exists("iris_model.joblib"):
    loader = ModelLoader()
    model = loader.load_model("iris_model.joblib")
    
    # Make prediction
    sample = [[5.1, 3.5, 1.4, 0.2]]  # Sample iris data
    prediction = model.predict(sample)
    print(f"Sample prediction: {prediction[0]} ({iris.target_names[prediction[0]]})")

# ========== PRACTICAL: MODEL SAVE/LOAD FUNCTIONS ==========
print("\n" + "=" * 60)
print("PRACTICAL: UTILITY FUNCTIONS")
print("=" * 60)

def save_model(model, filepath, metadata=None):
    """
    Save model to file with optional metadata.
    
    Args:
        model: The trained model to save
        filepath: Path to save the model
        metadata: Optional dict with model info
    """
    # Save model
    if filepath.endswith('.pkl'):
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
    elif SKLEARN_AVAILABLE:
        joblib.dump(model, filepath)
    
    # Save metadata if provided
    if metadata:
        meta_path = filepath.replace('.pkl', '_meta.json').replace('.joblib', '_meta.json')
        with open(meta_path, 'w') as f:
            json.dump(metadata, f, indent=4)
    
    print(f"✅ Model saved to {filepath}")
    return filepath


def load_model(filepath, with_metadata=False):
    """
    Load model from file.
    
    Args:
        filepath: Path to the model file
        with_metadata: Also load metadata if True
    
    Returns:
        model or (model, metadata) tuple
    """
    # Load model
    if filepath.endswith('.pkl'):
        with open(filepath, 'rb') as f:
            model = pickle.load(f)
    elif SKLEARN_AVAILABLE:
        model = joblib.load(filepath)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")
    
    if with_metadata:
        meta_path = filepath.replace('.pkl', '_meta.json').replace('.joblib', '_meta.json')
        try:
            with open(meta_path, 'r') as f:
                metadata = json.load(f)
            return model, metadata
        except FileNotFoundError:
            return model, None
    
    return model


# Demo the utility functions
if SKLEARN_AVAILABLE:
    print("\nUsing utility functions:")
    
    # Train a new model
    lr_model = LogisticRegression(max_iter=200)
    lr_model.fit(X_train, y_train)
    
    # Save with metadata
    save_model(
        lr_model,
        "logistic_model.joblib",
        metadata={
            "algorithm": "LogisticRegression",
            "accuracy": lr_model.score(X_test, y_test),
            "training_date": datetime.now().isoformat()
        }
    )
    
    # Load with metadata
    loaded, meta = load_model("logistic_model.joblib", with_metadata=True)
    print(f"✅ Loaded model with metadata: {meta}")

# ========== CLEANUP ==========
print("\n" + "=" * 60)
print("CLEANUP")
print("=" * 60)

# Clean up demo files
cleanup_files = [
    "model_info.pkl",
    "iris_model.pkl",
    "iris_model.joblib",
    "iris_model_compressed.joblib",
    "logistic_model.joblib",
    "logistic_model_meta.json"
]

for f in cleanup_files:
    if os.path.exists(f):
        os.remove(f)
        print(f"   Removed: {f}")

# Clean models directory
if os.path.exists("models"):
    import shutil
    shutil.rmtree("models")
    print("   Removed: models/")

print("\n✅ Cleanup complete!")

print("\n" + "=" * 60)
print("✅ Saving and Loading Models - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Use pickle for simple objects
2. Use joblib for ML models (faster, better compression)
3. Always version your models
4. Save metadata alongside models
5. Load models once and cache them
6. Handle loading errors gracefully

Next: Flask API for ML Models →
""")
