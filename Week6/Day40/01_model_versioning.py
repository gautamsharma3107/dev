"""
Day 40 - Model Versioning
=========================
Learn: Why model versioning matters and how to implement it

Key Concepts:
- Model versioning tracks different iterations of ML models
- Essential for reproducibility, rollback, and collaboration
- Multiple approaches: file-based, Git-based, dedicated tools
"""

import json
import hashlib
from datetime import datetime

# ========== WHY MODEL VERSIONING? ==========
print("=" * 60)
print("WHY MODEL VERSIONING?")
print("=" * 60)

"""
Model versioning is critical because:

1. REPRODUCIBILITY
   - Recreate exact results from any point in time
   - Debug issues by comparing model versions
   
2. COLLABORATION
   - Team members can work on different experiments
   - Clear history of who changed what and when
   
3. ROLLBACK CAPABILITY
   - Quickly revert to previous working version
   - A/B testing between model versions
   
4. AUDIT TRAIL
   - Track model lineage for compliance
   - Document model evolution over time
   
5. DEPLOYMENT MANAGEMENT
   - Manage staging vs production models
   - Gradual rollout of new models
"""

# ========== SIMPLE FILE-BASED VERSIONING ==========
print("\n" + "=" * 60)
print("SIMPLE FILE-BASED VERSIONING")
print("=" * 60)


class SimpleModelVersioner:
    """Basic model versioning using files and metadata"""

    def __init__(self, base_path="models"):
        self.base_path = base_path
        self.version_history = []

    def _generate_version_id(self, model_params):
        """Generate unique version ID based on params and timestamp"""
        timestamp = datetime.now().isoformat()
        content = json.dumps(model_params) + timestamp
        return hashlib.md5(content.encode()).hexdigest()[:8]

    def save_model(self, model, model_name, params, metrics):
        """Save model with version metadata"""
        version_id = self._generate_version_id(params)
        version_info = {
            "version_id": version_id,
            "model_name": model_name,
            "timestamp": datetime.now().isoformat(),
            "parameters": params,
            "metrics": metrics,
            "file_path": f"{self.base_path}/{model_name}_v{version_id}.pkl",
        }

        self.version_history.append(version_info)

        print(f"✅ Model saved: {model_name}")
        print(f"   Version ID: {version_id}")
        print(f"   Parameters: {params}")
        print(f"   Metrics: {metrics}")

        return version_info

    def list_versions(self, model_name=None):
        """List all versions or filter by model name"""
        versions = self.version_history
        if model_name:
            versions = [v for v in versions if v["model_name"] == model_name]

        print(f"\n📋 Model Versions ({len(versions)} found):")
        for v in versions:
            print(f"   - {v['version_id']}: {v['model_name']} ({v['timestamp'][:10]})")
            print(f"     Metrics: {v['metrics']}")

        return versions

    def get_best_version(self, model_name, metric="accuracy"):
        """Get the best version based on a metric"""
        versions = [v for v in self.version_history if v["model_name"] == model_name]
        if not versions:
            return None

        best = max(versions, key=lambda x: x["metrics"].get(metric, 0))
        print(f"\n🏆 Best version for {model_name} (by {metric}):")
        print(f"   Version: {best['version_id']}")
        print(f"   {metric}: {best['metrics'][metric]}")

        return best


# Demo
print("\n--- Demo: Simple Model Versioning ---\n")
versioner = SimpleModelVersioner()

# Simulate saving different model versions
versioner.save_model(
    model=None,  # In real scenario, this would be actual model
    model_name="classifier",
    params={"learning_rate": 0.01, "epochs": 100},
    metrics={"accuracy": 0.85, "f1_score": 0.82},
)

versioner.save_model(
    model=None,
    model_name="classifier",
    params={"learning_rate": 0.001, "epochs": 200},
    metrics={"accuracy": 0.92, "f1_score": 0.89},
)

versioner.save_model(
    model=None,
    model_name="classifier",
    params={"learning_rate": 0.005, "epochs": 150},
    metrics={"accuracy": 0.88, "f1_score": 0.86},
)

versioner.list_versions("classifier")
versioner.get_best_version("classifier", "accuracy")

# ========== VERSION METADATA SCHEMA ==========
print("\n" + "=" * 60)
print("VERSION METADATA SCHEMA")
print("=" * 60)

MODEL_VERSION_SCHEMA = {
    "version_id": "Unique identifier for this version",
    "model_name": "Name of the model",
    "version_number": "Semantic version (e.g., 1.0.0)",
    "created_at": "Timestamp when version was created",
    "created_by": "User who created this version",
    "description": "Description of changes in this version",
    "parameters": {
        "hyperparameters": "Model hyperparameters used",
        "training_config": "Training configuration",
        "feature_config": "Feature engineering settings",
    },
    "metrics": {
        "training_metrics": "Metrics on training data",
        "validation_metrics": "Metrics on validation data",
        "test_metrics": "Metrics on test data",
    },
    "artifacts": {
        "model_file": "Path to serialized model",
        "preprocessing_pipeline": "Path to preprocessing artifacts",
        "feature_names": "List of feature names used",
    },
    "data_info": {
        "training_data_hash": "Hash of training dataset",
        "data_version": "Version of dataset used",
        "num_samples": "Number of training samples",
    },
    "environment": {
        "python_version": "Python version used",
        "dependencies": "List of package dependencies",
        "hardware": "Hardware specifications",
    },
    "status": "Current status (development/staging/production/archived)",
}

print("Model Version Metadata Schema:")
print(json.dumps(MODEL_VERSION_SCHEMA, indent=2))

# ========== SEMANTIC VERSIONING FOR MODELS ==========
print("\n" + "=" * 60)
print("SEMANTIC VERSIONING FOR MODELS")
print("=" * 60)


class SemanticModelVersion:
    """
    Semantic versioning for ML models: MAJOR.MINOR.PATCH

    MAJOR: Breaking changes (new features, different input/output)
    MINOR: Performance improvements, new training data
    PATCH: Bug fixes, minor adjustments
    """

    def __init__(self, major=1, minor=0, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def bump_major(self, reason=""):
        """Breaking changes to model"""
        self.major += 1
        self.minor = 0
        self.patch = 0
        print(f"⬆️ Major bump to {self}: {reason}")

    def bump_minor(self, reason=""):
        """Backward compatible improvements"""
        self.minor += 1
        self.patch = 0
        print(f"⬆️ Minor bump to {self}: {reason}")

    def bump_patch(self, reason=""):
        """Bug fixes"""
        self.patch += 1
        print(f"⬆️ Patch bump to {self}: {reason}")


# Demo semantic versioning
print("\n--- Demo: Semantic Versioning ---\n")
version = SemanticModelVersion()
print(f"Initial version: {version}")

version.bump_patch("Fixed data preprocessing bug")
version.bump_minor("Retrained with more data, improved accuracy by 2%")
version.bump_minor("Added new features")
version.bump_major("Changed model architecture to transformer")

# ========== MODEL LIFECYCLE STAGES ==========
print("\n" + "=" * 60)
print("MODEL LIFECYCLE STAGES")
print("=" * 60)

MODEL_STAGES = {
    "Development": "Model is being developed and tested",
    "Staging": "Model is ready for pre-production testing",
    "Production": "Model is deployed and serving predictions",
    "Archived": "Model is retired but kept for reference",
}

print("\nModel Lifecycle Stages:")
for stage, description in MODEL_STAGES.items():
    print(f"  {stage}: {description}")

print(
    """
Typical Flow:
  Development → Staging → Production → Archived
       ↑          ↓
       └──────────┘ (if issues found)
"""
)

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("MODEL VERSIONING BEST PRACTICES")
print("=" * 60)

BEST_PRACTICES = """
1. VERSION EVERYTHING
   - Model weights/parameters
   - Training code
   - Preprocessing pipeline
   - Feature definitions
   - Training data

2. USE MEANINGFUL NAMES
   - Include date, experiment ID, or semantic version
   - Example: model_classifier_v2.1.0_20240101.pkl

3. STORE METADATA
   - Hyperparameters used
   - Training metrics
   - Data statistics
   - Environment info

4. AUTOMATE VERSIONING
   - Use tools like MLflow, DVC, or custom CI/CD
   - Don't rely on manual versioning

5. IMPLEMENT ROLLBACK STRATEGY
   - Always keep previous working version
   - Test rollback procedure regularly

6. TRACK DATA VERSIONS TOO
   - Model is only as good as its data
   - Use DVC or similar tools

7. DOCUMENT CHANGES
   - Maintain changelog
   - Record why changes were made
"""

print(BEST_PRACTICES)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Model Registry")
print("=" * 60)


class ModelRegistry:
    """Simple model registry implementation"""

    def __init__(self):
        self.models = {}  # model_name -> list of versions
        self.production_models = {}  # model_name -> version_id

    def register_model(self, model_name, version_id, metadata):
        """Register a new model version"""
        if model_name not in self.models:
            self.models[model_name] = []

        self.models[model_name].append(
            {"version_id": version_id, "metadata": metadata, "stage": "Development"}
        )
        print(f"✅ Registered: {model_name} v{version_id}")

    def promote_to_staging(self, model_name, version_id):
        """Promote model to staging"""
        for version in self.models.get(model_name, []):
            if version["version_id"] == version_id:
                version["stage"] = "Staging"
                print(f"📦 Promoted to Staging: {model_name} v{version_id}")
                return
        print(f"❌ Version not found: {model_name} v{version_id}")

    def promote_to_production(self, model_name, version_id):
        """Promote model to production"""
        for version in self.models.get(model_name, []):
            if version["version_id"] == version_id:
                # Archive current production model
                if model_name in self.production_models:
                    old_version = self.production_models[model_name]
                    for v in self.models[model_name]:
                        if v["version_id"] == old_version:
                            v["stage"] = "Archived"
                            print(f"📁 Archived: {model_name} v{old_version}")

                version["stage"] = "Production"
                self.production_models[model_name] = version_id
                print(f"🚀 Promoted to Production: {model_name} v{version_id}")
                return
        print(f"❌ Version not found: {model_name} v{version_id}")

    def get_production_model(self, model_name):
        """Get current production model"""
        version_id = self.production_models.get(model_name)
        if version_id:
            for version in self.models[model_name]:
                if version["version_id"] == version_id:
                    return version
        return None

    def list_all(self):
        """List all registered models"""
        print("\n📋 Model Registry:")
        for model_name, versions in self.models.items():
            print(f"\n  {model_name}:")
            for v in versions:
                stage_icon = {"Development": "🔧", "Staging": "📦", "Production": "🚀", "Archived": "📁"}
                icon = stage_icon.get(v["stage"], "")
                print(f"    {icon} v{v['version_id']} [{v['stage']}]")


# Demo
print("\n--- Demo: Model Registry ---\n")
registry = ModelRegistry()

registry.register_model(
    "fraud_detector", "1.0.0", {"accuracy": 0.90, "trained_on": "2024-01-01"}
)
registry.register_model(
    "fraud_detector", "1.1.0", {"accuracy": 0.93, "trained_on": "2024-02-01"}
)
registry.register_model(
    "fraud_detector", "2.0.0", {"accuracy": 0.95, "trained_on": "2024-03-01"}
)

registry.promote_to_staging("fraud_detector", "1.1.0")
registry.promote_to_production("fraud_detector", "1.1.0")
registry.promote_to_staging("fraud_detector", "2.0.0")
registry.promote_to_production("fraud_detector", "2.0.0")

registry.list_all()

print("\n" + "=" * 60)
print("✅ Model Versioning - Complete!")
print("=" * 60)
