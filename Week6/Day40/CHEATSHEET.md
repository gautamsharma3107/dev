# Day 40 Quick Reference Cheat Sheet

## MLflow Essentials
```python
import mlflow
from mlflow.tracking import MlflowClient

# Start MLflow server (terminal)
# mlflow ui --port 5000

# Set tracking URI
mlflow.set_tracking_uri("http://localhost:5000")

# Create/set experiment
mlflow.set_experiment("my_experiment")

# Start a run
with mlflow.start_run(run_name="my_run"):
    # Log parameters
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 100)
    
    # Log metrics
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("loss", 0.05)
    
    # Log artifacts (files)
    mlflow.log_artifact("model.pkl")
    
    # Log model
    mlflow.sklearn.log_model(model, "model")

# Search runs
runs = mlflow.search_runs(experiment_ids=["1"])

# Load model
model = mlflow.sklearn.load_model("runs:/run_id/model")
```

## Model Registry
```python
# Register model
mlflow.register_model(
    "runs:/run_id/model",
    "my_model"
)

# Model stages: None -> Staging -> Production -> Archived
client = MlflowClient()

# Transition model stage
client.transition_model_version_stage(
    name="my_model",
    version=1,
    stage="Production"
)

# Load production model
model = mlflow.pyfunc.load_model(
    "models:/my_model/Production"
)
```

## DVC (Data Version Control)
```bash
# Initialize DVC
dvc init

# Track data file
dvc add data/dataset.csv

# Commit DVC files to git
git add data/dataset.csv.dvc data/.gitignore
git commit -m "Add dataset tracking"

# Push data to remote
dvc remote add -d myremote s3://mybucket/path
dvc push

# Pull data
dvc pull

# Create pipeline
dvc run -n preprocess \
    -d data/raw.csv \
    -o data/processed.csv \
    python preprocess.py

# Reproduce pipeline
dvc repro
```

## Model Monitoring
```python
# Data Drift Detection
from scipy.stats import ks_2samp

def detect_drift(reference_data, current_data, threshold=0.05):
    """Detect drift using Kolmogorov-Smirnov test"""
    statistic, p_value = ks_2samp(reference_data, current_data)
    return p_value < threshold  # True = drift detected

# Performance Monitoring
def monitor_model_performance(predictions, actuals):
    """Track model performance metrics"""
    from sklearn.metrics import accuracy_score, f1_score
    return {
        'accuracy': accuracy_score(actuals, predictions),
        'f1_score': f1_score(actuals, predictions, average='weighted')
    }

# Logging predictions
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_prediction(input_data, prediction, confidence):
    logger.info(f"Input: {input_data}, Prediction: {prediction}, Confidence: {confidence}")
```

## Model Versioning Best Practices
```python
import joblib
import json
from datetime import datetime

# Save model with metadata
def save_model_with_version(model, model_name, version, metrics):
    metadata = {
        'model_name': model_name,
        'version': version,
        'timestamp': datetime.now().isoformat(),
        'metrics': metrics
    }
    
    # Save model
    joblib.dump(model, f'{model_name}_v{version}.joblib')
    
    # Save metadata
    with open(f'{model_name}_v{version}_metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)

# Load model with version check
def load_model_with_version(model_name, version):
    model = joblib.load(f'{model_name}_v{version}.joblib')
    with open(f'{model_name}_v{version}_metadata.json', 'r') as f:
        metadata = json.load(f)
    return model, metadata
```

## Production Configuration
```python
# Environment-based config
import os

class Config:
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI', 'http://localhost:5000')
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', '32'))
    
# Feature flags
FEATURE_FLAGS = {
    'use_new_model': os.getenv('USE_NEW_MODEL', 'false').lower() == 'true',
    'enable_monitoring': os.getenv('ENABLE_MONITORING', 'true').lower() == 'true',
}
```

## Health Checks
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/ready")
def readiness_check():
    # Check model is loaded
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ready"}
```

## Common Commands
```bash
# MLflow
mlflow ui                           # Start UI
mlflow experiments list             # List experiments
mlflow runs list --experiment-id 0  # List runs

# DVC
dvc status                          # Check status
dvc diff                            # Show changes
dvc metrics show                    # Show metrics
dvc plots show                      # Show plots

# Docker for ML
docker build -t my-ml-model .
docker run -p 8000:8000 my-ml-model
```

## Key Metrics to Track
```python
METRICS_TO_LOG = {
    'model_metrics': ['accuracy', 'precision', 'recall', 'f1', 'auc'],
    'data_metrics': ['num_samples', 'feature_count', 'missing_values'],
    'system_metrics': ['latency_ms', 'throughput', 'memory_mb'],
    'business_metrics': ['conversion_rate', 'revenue_impact']
}
```

---
**Keep this handy for quick MLOps reference!** 🚀
