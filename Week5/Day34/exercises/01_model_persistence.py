"""
EXERCISES: Model Persistence
============================
Complete all exercises below
"""

print("=" * 60)
print("EXERCISES: Model Persistence")
print("=" * 60)

# Exercise 1: Basic Model Saving
# TODO: Train a simple model and save it with both pickle and joblib
# Compare file sizes

print("\n" + "=" * 60)
print("Exercise 1: Save Model Two Ways")
print("=" * 60)

def exercise_1():
    """
    1. Load the iris dataset
    2. Train a RandomForestClassifier
    3. Save the model using pickle
    4. Save the model using joblib
    5. Save with joblib compression
    6. Print file sizes for comparison
    """
    # Your code here:
    pass


# Exercise 2: Save Model with Metadata
# TODO: Create a function that saves model along with metadata

print("\n" + "=" * 60)
print("Exercise 2: Model with Metadata")
print("=" * 60)

def save_model_with_info(model, filepath, model_name, version, metrics):
    """
    Save model and create a metadata file with:
    - model_name
    - version
    - creation timestamp
    - metrics (accuracy, etc.)
    - model filepath
    
    Metadata should be saved as {filepath}_meta.json
    """
    # Your code here:
    pass

# Test your function:
# save_model_with_info(model, "my_model.joblib", "iris_clf", "1.0", {"accuracy": 0.95})


# Exercise 3: Model Loader Class
# TODO: Implement a singleton model loader

print("\n" + "=" * 60)
print("Exercise 3: Singleton Model Loader")
print("=" * 60)

class ModelManager:
    """
    Implement a model manager that:
    1. Uses singleton pattern (only one instance)
    2. Can load multiple models by name
    3. Caches loaded models
    4. Can reload a specific model
    5. Can list all loaded models
    """
    
    _instance = None
    
    def __new__(cls):
        # Implement singleton
        pass
    
    def __init__(self):
        self._models = {}
    
    def load_model(self, name, filepath):
        """Load model and cache it by name."""
        pass
    
    def get_model(self, name):
        """Get a loaded model by name."""
        pass
    
    def reload_model(self, name, filepath):
        """Force reload a model."""
        pass
    
    def list_models(self):
        """Return list of loaded model names."""
        pass

# Test:
# manager = ModelManager()
# manager.load_model("iris", "iris_model.joblib")
# model = manager.get_model("iris")


# Exercise 4: Model Version Manager
# TODO: Create a system for managing model versions

print("\n" + "=" * 60)
print("Exercise 4: Version Manager")
print("=" * 60)

class ModelVersionManager:
    """
    Manage multiple versions of models:
    1. Save new versions with auto-incrementing version numbers
    2. Load specific versions
    3. Load latest version
    4. List all versions
    5. Compare two versions (just metadata)
    """
    
    def __init__(self, base_dir="models"):
        self.base_dir = base_dir
    
    def save_version(self, model, model_name, metrics):
        """Save model as new version, return version number."""
        pass
    
    def load_version(self, model_name, version):
        """Load specific version of a model."""
        pass
    
    def load_latest(self, model_name):
        """Load the latest version of a model."""
        pass
    
    def list_versions(self, model_name):
        """List all versions of a model."""
        pass
    
    def compare_versions(self, model_name, v1, v2):
        """Compare metadata of two versions."""
        pass


# Exercise 5: Preprocessor + Model Bundle
# TODO: Save and load model with its preprocessor

print("\n" + "=" * 60)
print("Exercise 5: Model + Preprocessor Bundle")
print("=" * 60)

class ModelBundle:
    """
    Bundle a model with its preprocessor for deployment.
    
    Usage:
        bundle = ModelBundle(model, scaler, label_encoder)
        bundle.save("my_bundle.joblib")
        
        loaded = ModelBundle.load("my_bundle.joblib")
        prediction = loaded.predict(raw_features)
    """
    
    def __init__(self, model, scaler=None, label_encoder=None):
        self.model = model
        self.scaler = scaler
        self.label_encoder = label_encoder
    
    def preprocess(self, features):
        """Apply preprocessing to features."""
        pass
    
    def predict(self, features):
        """Preprocess and predict."""
        pass
    
    def predict_proba(self, features):
        """Preprocess and predict probabilities."""
        pass
    
    def save(self, filepath):
        """Save the entire bundle."""
        pass
    
    @classmethod
    def load(cls, filepath):
        """Load a bundle from file."""
        pass


print("\n" + "=" * 60)
print("Complete all exercises and test your implementations!")
print("=" * 60)

"""
SOLUTIONS (Don't look until you've tried!)
==========================================

Exercise 1:
-----------
import pickle
import joblib
import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def exercise_1():
    # Load and train
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save with pickle
    with open("model_pickle.pkl", "wb") as f:
        pickle.dump(model, f)
    
    # Save with joblib
    joblib.dump(model, "model_joblib.joblib")
    
    # Save compressed
    joblib.dump(model, "model_compressed.joblib", compress=3)
    
    # Compare sizes
    print(f"Pickle: {os.path.getsize('model_pickle.pkl'):,} bytes")
    print(f"Joblib: {os.path.getsize('model_joblib.joblib'):,} bytes")
    print(f"Compressed: {os.path.getsize('model_compressed.joblib'):,} bytes")


Exercise 2:
-----------
import json
import joblib
from datetime import datetime

def save_model_with_info(model, filepath, model_name, version, metrics):
    # Save model
    joblib.dump(model, filepath)
    
    # Create metadata
    metadata = {
        "model_name": model_name,
        "version": version,
        "created_at": datetime.now().isoformat(),
        "metrics": metrics,
        "model_file": filepath
    }
    
    # Save metadata
    meta_path = filepath.replace('.joblib', '_meta.json').replace('.pkl', '_meta.json')
    with open(meta_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    
    return metadata


Exercise 3:
-----------
class ModelManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._models = {}
        return cls._instance
    
    def load_model(self, name, filepath):
        self._models[name] = joblib.load(filepath)
        return self._models[name]
    
    def get_model(self, name):
        if name not in self._models:
            raise KeyError(f"Model '{name}' not loaded")
        return self._models[name]
    
    def reload_model(self, name, filepath):
        self._models[name] = joblib.load(filepath)
        return self._models[name]
    
    def list_models(self):
        return list(self._models.keys())


Exercise 4:
-----------
import os
import json
import joblib
from datetime import datetime

class ModelVersionManager:
    def __init__(self, base_dir="models"):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)
    
    def _get_next_version(self, model_name):
        versions = self.list_versions(model_name)
        if not versions:
            return 1
        return max(versions) + 1
    
    def save_version(self, model, model_name, metrics):
        version = self._get_next_version(model_name)
        
        model_dir = os.path.join(self.base_dir, model_name)
        os.makedirs(model_dir, exist_ok=True)
        
        # Save model
        model_path = os.path.join(model_dir, f"v{version}.joblib")
        joblib.dump(model, model_path)
        
        # Save metadata
        meta = {
            "version": version,
            "created_at": datetime.now().isoformat(),
            "metrics": metrics
        }
        meta_path = os.path.join(model_dir, f"v{version}_meta.json")
        with open(meta_path, 'w') as f:
            json.dump(meta, f, indent=4)
        
        return version
    
    def load_version(self, model_name, version):
        path = os.path.join(self.base_dir, model_name, f"v{version}.joblib")
        return joblib.load(path)
    
    def load_latest(self, model_name):
        versions = self.list_versions(model_name)
        if not versions:
            raise FileNotFoundError(f"No versions found for {model_name}")
        return self.load_version(model_name, max(versions))
    
    def list_versions(self, model_name):
        model_dir = os.path.join(self.base_dir, model_name)
        if not os.path.exists(model_dir):
            return []
        
        versions = []
        for f in os.listdir(model_dir):
            if f.startswith('v') and f.endswith('.joblib'):
                try:
                    v = int(f[1:].replace('.joblib', ''))
                    versions.append(v)
                except ValueError:
                    pass
        return sorted(versions)


Exercise 5:
-----------
import joblib
import numpy as np

class ModelBundle:
    def __init__(self, model, scaler=None, label_encoder=None):
        self.model = model
        self.scaler = scaler
        self.label_encoder = label_encoder
    
    def preprocess(self, features):
        features = np.array(features)
        if features.ndim == 1:
            features = features.reshape(1, -1)
        if self.scaler:
            features = self.scaler.transform(features)
        return features
    
    def predict(self, features):
        processed = self.preprocess(features)
        predictions = self.model.predict(processed)
        if self.label_encoder:
            return self.label_encoder.inverse_transform(predictions)
        return predictions
    
    def predict_proba(self, features):
        processed = self.preprocess(features)
        return self.model.predict_proba(processed)
    
    def save(self, filepath):
        bundle = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoder': self.label_encoder
        }
        joblib.dump(bundle, filepath)
    
    @classmethod
    def load(cls, filepath):
        bundle = joblib.load(filepath)
        return cls(
            model=bundle['model'],
            scaler=bundle['scaler'],
            label_encoder=bundle['label_encoder']
        )
"""
