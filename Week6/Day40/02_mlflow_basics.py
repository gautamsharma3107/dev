"""
Day 40 - MLflow Basics
======================
Learn: Experiment tracking with MLflow

Key Concepts:
- MLflow is an open-source platform for ML lifecycle management
- Key components: Tracking, Projects, Models, Registry
- Essential for reproducibility and collaboration
"""

# ========== WHAT IS MLFLOW? ==========
print("=" * 60)
print("WHAT IS MLFLOW?")
print("=" * 60)

MLFLOW_OVERVIEW = """
MLflow is an open-source platform for managing the ML lifecycle:

📊 MLFLOW COMPONENTS:

1. TRACKING
   - Log parameters, metrics, and artifacts
   - Compare experiments
   - Visualize results

2. PROJECTS
   - Package code in reusable format
   - Reproducible runs
   - Dependency management

3. MODELS
   - Standard format for packaging models
   - Deploy to various platforms
   - Multiple flavors (sklearn, tensorflow, etc.)

4. REGISTRY
   - Central model store
   - Model versioning
   - Stage transitions (Staging → Production)
"""

print(MLFLOW_OVERVIEW)

# ========== MLFLOW TRACKING BASICS ==========
print("\n" + "=" * 60)
print("MLFLOW TRACKING BASICS")
print("=" * 60)

# Note: This is demonstration code. In real use, install mlflow:
# pip install mlflow

TRACKING_CODE = '''
import mlflow
from mlflow.tracking import MlflowClient

# Set tracking URI (local or remote)
mlflow.set_tracking_uri("http://localhost:5000")

# Create or set experiment
mlflow.set_experiment("my_classification_experiment")

# Start a run
with mlflow.start_run(run_name="random_forest_v1"):
    # Log parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("random_state", 42)
    
    # Train model (example)
    # model = RandomForestClassifier(n_estimators=100, max_depth=10)
    # model.fit(X_train, y_train)
    
    # Log metrics
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("precision", 0.94)
    mlflow.log_metric("recall", 0.93)
    mlflow.log_metric("f1_score", 0.935)
    
    # Log metrics over epochs
    for epoch in range(10):
        mlflow.log_metric("loss", 1.0 - epoch * 0.1, step=epoch)
    
    # Log artifacts (files)
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.log_artifact("feature_importance.csv")
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Log custom tags
    mlflow.set_tag("model_type", "random_forest")
    mlflow.set_tag("dataset", "customer_churn")

print("Run logged successfully!")
'''

print("MLflow Tracking Example Code:")
print(TRACKING_CODE)


# ========== SIMULATED MLFLOW TRACKING ==========
print("\n" + "=" * 60)
print("SIMULATED MLFLOW TRACKING")
print("=" * 60)


class MockMLflowTracker:
    """
    Simulated MLflow tracker for learning purposes.
    Demonstrates the MLflow API without requiring installation.
    """

    def __init__(self):
        self.experiments = {}
        self.current_experiment = None
        self.current_run = None
        self.runs = []

    def set_experiment(self, name):
        """Set or create an experiment"""
        if name not in self.experiments:
            self.experiments[name] = {"name": name, "runs": []}
        self.current_experiment = name
        print(f"📊 Experiment set: {name}")

    def start_run(self, run_name=None):
        """Start a new run"""
        run_id = f"run_{len(self.runs) + 1}"
        self.current_run = {
            "run_id": run_id,
            "run_name": run_name or run_id,
            "experiment": self.current_experiment,
            "params": {},
            "metrics": {},
            "artifacts": [],
            "tags": {},
        }
        print(f"🏃 Started run: {run_name or run_id}")
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_run()

    def end_run(self):
        """End the current run"""
        if self.current_run:
            self.runs.append(self.current_run)
            self.experiments[self.current_experiment]["runs"].append(self.current_run)
            print(f"✅ Run ended: {self.current_run['run_name']}")
            self.current_run = None

    def log_param(self, key, value):
        """Log a parameter"""
        self.current_run["params"][key] = value
        print(f"   📝 Param: {key} = {value}")

    def log_params(self, params):
        """Log multiple parameters"""
        for key, value in params.items():
            self.log_param(key, value)

    def log_metric(self, key, value, step=None):
        """Log a metric"""
        if key not in self.current_run["metrics"]:
            self.current_run["metrics"][key] = []
        self.current_run["metrics"][key].append({"value": value, "step": step})
        if step is not None:
            print(f"   📈 Metric: {key} = {value} (step {step})")
        else:
            print(f"   📈 Metric: {key} = {value}")

    def log_artifact(self, path):
        """Log an artifact"""
        self.current_run["artifacts"].append(path)
        print(f"   📁 Artifact: {path}")

    def set_tag(self, key, value):
        """Set a tag"""
        self.current_run["tags"][key] = value
        print(f"   🏷️ Tag: {key} = {value}")

    def search_runs(self, experiment_name=None):
        """Search runs in an experiment"""
        if experiment_name:
            return self.experiments.get(experiment_name, {}).get("runs", [])
        return self.runs

    def get_best_run(self, experiment_name, metric, maximize=True):
        """Get the best run based on a metric"""
        runs = self.search_runs(experiment_name)
        if not runs:
            return None

        def get_metric_value(run):
            metrics = run["metrics"].get(metric, [])
            if not metrics:
                return float("-inf") if maximize else float("inf")
            return metrics[-1]["value"]

        return max(runs, key=get_metric_value) if maximize else min(runs, key=get_metric_value)


# Demo
print("\n--- Demo: MLflow Tracking ---\n")
mlflow = MockMLflowTracker()
mlflow.set_experiment("iris_classification")

# Run 1: Random Forest
with mlflow.start_run(run_name="random_forest_baseline"):
    mlflow.log_params({"model_type": "RandomForest", "n_estimators": 100, "max_depth": 10})
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_metric("f1_score", 0.91)
    mlflow.set_tag("developer", "gautam")

# Run 2: Gradient Boosting
with mlflow.start_run(run_name="gradient_boosting"):
    mlflow.log_params(
        {"model_type": "GradientBoosting", "n_estimators": 200, "learning_rate": 0.1}
    )
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("f1_score", 0.94)
    mlflow.set_tag("developer", "gautam")

# Run 3: Neural Network
with mlflow.start_run(run_name="neural_network"):
    mlflow.log_params(
        {"model_type": "NeuralNetwork", "layers": [64, 32], "learning_rate": 0.001}
    )
    # Log metrics over epochs
    for epoch, (acc, loss) in enumerate(
        [(0.80, 0.5), (0.85, 0.3), (0.90, 0.2), (0.93, 0.15)]
    ):
        mlflow.log_metric("accuracy", acc, step=epoch)
        mlflow.log_metric("loss", loss, step=epoch)
    mlflow.set_tag("developer", "gautam")

# Find best run
print("\n--- Finding Best Run ---")
best = mlflow.get_best_run("iris_classification", "accuracy")
print(f"🏆 Best run: {best['run_name']}")
print(f"   Accuracy: {best['metrics']['accuracy'][-1]['value']}")
print(f"   Parameters: {best['params']}")

# ========== MLFLOW MODEL REGISTRY ==========
print("\n" + "=" * 60)
print("MLFLOW MODEL REGISTRY")
print("=" * 60)

REGISTRY_CODE = '''
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Register a model from a run
mlflow.register_model(
    "runs:/abc123/model",
    "iris_classifier"
)

# List registered models
for rm in client.search_registered_models():
    print(f"Model: {rm.name}")
    
# Get model versions
for mv in client.search_model_versions("name='iris_classifier'"):
    print(f"Version: {mv.version}, Stage: {mv.current_stage}")

# Transition model stage
client.transition_model_version_stage(
    name="iris_classifier",
    version=1,
    stage="Staging"  # or "Production", "Archived"
)

# Load model by stage
model = mlflow.pyfunc.load_model("models:/iris_classifier/Production")

# Make predictions
predictions = model.predict(X_test)
'''

print("MLflow Model Registry Code:")
print(REGISTRY_CODE)

# ========== MLFLOW UI ==========
print("\n" + "=" * 60)
print("MLFLOW UI")
print("=" * 60)

print(
    """
Starting MLflow UI:

1. Install MLflow:
   pip install mlflow

2. Start the UI server:
   mlflow ui --port 5000

3. Open browser:
   http://localhost:5000

UI Features:
- View all experiments and runs
- Compare runs side by side
- Visualize metrics over time
- Download artifacts
- Search and filter runs
- Model registry management
"""
)

# ========== MLFLOW PROJECT STRUCTURE ==========
print("\n" + "=" * 60)
print("MLFLOW PROJECT STRUCTURE")
print("=" * 60)

PROJECT_STRUCTURE = """
my_ml_project/
├── MLproject              # Project configuration
├── conda.yaml             # Conda environment
├── requirements.txt       # Pip requirements
├── train.py              # Training script
├── predict.py            # Prediction script
└── README.md

MLproject file example:
```yaml
name: my_ml_project

conda_env: conda.yaml

entry_points:
  main:
    parameters:
      learning_rate: {type: float, default: 0.01}
      epochs: {type: int, default: 100}
    command: "python train.py --lr {learning_rate} --epochs {epochs}"
  
  predict:
    parameters:
      model_path: path
    command: "python predict.py --model {model_path}"
```

Running a project:
```bash
mlflow run . -P learning_rate=0.001 -P epochs=200
mlflow run https://github.com/user/project
```
"""

print(PROJECT_STRUCTURE)

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("MLFLOW BEST PRACTICES")
print("=" * 60)

BEST_PRACTICES = """
1. ORGANIZE EXPERIMENTS
   - Use meaningful experiment names
   - Group related runs together
   - Use tags for categorization

2. LOG COMPREHENSIVELY
   - All hyperparameters
   - Training and validation metrics
   - Test metrics
   - Model artifacts
   - Environment info

3. USE CONSISTENT NAMING
   - Parameter names
   - Metric names
   - Run names

4. TRACK EVERYTHING
   - Source code version (git commit)
   - Dataset version
   - Random seeds
   - Hardware info

5. AUTOMATE TRACKING
   - Use autolog when available:
     mlflow.sklearn.autolog()
     mlflow.tensorflow.autolog()
     mlflow.pytorch.autolog()

6. SET UP REMOTE TRACKING
   - Use a shared tracking server
   - Configure artifact storage (S3, GCS, etc.)
   - Set up authentication

7. USE MODEL REGISTRY
   - Register promising models
   - Use stages (Staging, Production)
   - Document model changes
"""

print(BEST_PRACTICES)

# ========== AUTOLOGGING ==========
print("\n" + "=" * 60)
print("MLFLOW AUTOLOGGING")
print("=" * 60)

AUTOLOG_CODE = '''
import mlflow

# Enable autologging for scikit-learn
mlflow.sklearn.autolog()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Your training code - MLflow logs automatically!
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# MLflow automatically logs:
# - Parameters (n_estimators, max_depth, etc.)
# - Metrics (accuracy, precision, recall, f1)
# - Model artifact
# - Feature importance
# - Confusion matrix

# Supported frameworks:
# - mlflow.sklearn.autolog()
# - mlflow.tensorflow.autolog()
# - mlflow.pytorch.autolog()
# - mlflow.keras.autolog()
# - mlflow.xgboost.autolog()
# - mlflow.lightgbm.autolog()
# - mlflow.spark.autolog()
'''

print("MLflow Autologging:")
print(AUTOLOG_CODE)

print("\n" + "=" * 60)
print("✅ MLflow Basics - Complete!")
print("=" * 60)
