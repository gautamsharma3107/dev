"""
Day 40 - Production ML Best Practices
======================================
Learn: Best practices for deploying and maintaining ML in production

Key Concepts:
- Production ML requires more than just a good model
- Reliability, scalability, and maintainability are crucial
- Following best practices prevents common pitfalls
"""

# ========== PRODUCTION ML CHALLENGES ==========
print("=" * 60)
print("PRODUCTION ML CHALLENGES")
print("=" * 60)

CHALLENGES = """
🎯 CHALLENGES OF PRODUCTION ML:

1. MODEL DEGRADATION
   - Performance drops over time
   - Data distribution changes
   - Need continuous monitoring

2. REPRODUCIBILITY
   - Recreate experiments
   - Debug production issues
   - Audit requirements

3. SCALABILITY
   - Handle varying load
   - Low latency requirements
   - Cost optimization

4. RELIABILITY
   - High availability
   - Graceful degradation
   - Error handling

5. SECURITY
   - Model protection
   - Data privacy
   - Access control

6. TEAM COORDINATION
   - Multiple stakeholders
   - Clear handoffs
   - Documentation
"""

print(CHALLENGES)

# ========== MODEL SERVING PATTERNS ==========
print("\n" + "=" * 60)
print("MODEL SERVING PATTERNS")
print("=" * 60)


class ModelServer:
    """
    Example model server demonstrating best practices.
    """

    def __init__(self, model_path, version="1.0.0"):
        self.model = None
        self.model_path = model_path
        self.version = version
        self.is_ready = False
        self.prediction_count = 0

    def load_model(self):
        """Load model with error handling"""
        try:
            # In production: self.model = joblib.load(self.model_path)
            self.model = "MockModel"  # Simulated
            self.is_ready = True
            print(f"✅ Model loaded: {self.model_path} (v{self.version})")
            return True
        except Exception as e:
            print(f"❌ Failed to load model: {e}")
            self.is_ready = False
            return False

    def health_check(self):
        """Health check endpoint"""
        return {"status": "healthy", "version": self.version}

    def readiness_check(self):
        """Readiness check endpoint"""
        if self.is_ready and self.model is not None:
            return {"status": "ready", "version": self.version}
        return {"status": "not_ready", "reason": "Model not loaded"}

    def predict(self, features, request_id=None):
        """
        Make prediction with proper error handling and logging.
        """
        # Validate readiness
        if not self.is_ready:
            return {"error": "Model not ready", "request_id": request_id}

        # Validate input
        if not self._validate_input(features):
            return {"error": "Invalid input", "request_id": request_id}

        try:
            # Make prediction
            # In production: prediction = self.model.predict(features)
            prediction = "ClassA"  # Simulated
            confidence = 0.95

            self.prediction_count += 1

            return {
                "prediction": prediction,
                "confidence": confidence,
                "model_version": self.version,
                "request_id": request_id,
            }

        except Exception as e:
            return {"error": str(e), "request_id": request_id}

    def _validate_input(self, features):
        """Validate input data"""
        if features is None:
            return False
        if not isinstance(features, dict):
            return False
        return True


# Demo
print("\n--- Demo: Model Server ---\n")
server = ModelServer("models/classifier.pkl", version="2.1.0")
server.load_model()

print("\nHealth check:", server.health_check())
print("Readiness check:", server.readiness_check())
print("Prediction:", server.predict({"feature1": 1.0}, request_id="req-001"))

# ========== CONFIGURATION MANAGEMENT ==========
print("\n" + "=" * 60)
print("CONFIGURATION MANAGEMENT")
print("=" * 60)

import os


class Config:
    """
    Configuration management for ML applications.
    Uses environment variables with sensible defaults.
    """

    # Model settings
    MODEL_PATH = os.getenv("MODEL_PATH", "models/default.pkl")
    MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0.0")

    # Server settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    WORKERS = int(os.getenv("WORKERS", "4"))

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = os.getenv(
        "LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Monitoring
    ENABLE_METRICS = os.getenv("ENABLE_METRICS", "true").lower() == "true"
    METRICS_PORT = int(os.getenv("METRICS_PORT", "9090"))

    # Feature flags
    ENABLE_CACHING = os.getenv("ENABLE_CACHING", "true").lower() == "true"
    CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))

    @classmethod
    def display(cls):
        """Display current configuration"""
        print("\n📋 Current Configuration:")
        print(f"   MODEL_PATH: {cls.MODEL_PATH}")
        print(f"   MODEL_VERSION: {cls.MODEL_VERSION}")
        print(f"   HOST: {cls.HOST}")
        print(f"   PORT: {cls.PORT}")
        print(f"   WORKERS: {cls.WORKERS}")
        print(f"   LOG_LEVEL: {cls.LOG_LEVEL}")
        print(f"   ENABLE_METRICS: {cls.ENABLE_METRICS}")
        print(f"   ENABLE_CACHING: {cls.ENABLE_CACHING}")


Config.display()

# ========== ERROR HANDLING ==========
print("\n" + "=" * 60)
print("ERROR HANDLING")
print("=" * 60)


class PredictionError(Exception):
    """Custom exception for prediction errors"""

    pass


class ModelNotLoadedError(Exception):
    """Exception when model is not loaded"""

    pass


class InputValidationError(Exception):
    """Exception for invalid input"""

    pass


def safe_predict(model, features, fallback_value=None):
    """
    Make prediction with comprehensive error handling.
    """
    try:
        # Validate input
        if features is None:
            raise InputValidationError("Features cannot be None")

        # Check model
        if model is None:
            raise ModelNotLoadedError("Model is not loaded")

        # Make prediction
        # prediction = model.predict(features)
        prediction = "ClassA"  # Simulated

        return {"success": True, "prediction": prediction}

    except InputValidationError as e:
        return {"success": False, "error": "validation_error", "message": str(e)}

    except ModelNotLoadedError as e:
        return {"success": False, "error": "model_error", "message": str(e)}

    except Exception as e:
        # Log unexpected errors
        print(f"Unexpected error: {e}")

        # Return fallback if available
        if fallback_value is not None:
            return {
                "success": True,
                "prediction": fallback_value,
                "fallback_used": True,
            }

        return {"success": False, "error": "unknown_error", "message": str(e)}


# Demo
print("\n--- Demo: Error Handling ---")
print(safe_predict("model", {"x": 1}))  # Success
print(safe_predict("model", None))  # Validation error
print(safe_predict(None, {"x": 1}))  # Model error

# ========== LOGGING BEST PRACTICES ==========
print("\n" + "=" * 60)
print("LOGGING BEST PRACTICES")
print("=" * 60)

import logging


def setup_logging(level=logging.INFO):
    """Configure logging for ML application"""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            # In production: logging.FileHandler('app.log'),
        ],
    )
    return logging.getLogger(__name__)


logger = setup_logging()

LOGGING_PATTERNS = """
📝 LOGGING BEST PRACTICES:

1. LOG LEVELS
   - DEBUG: Detailed info for debugging
   - INFO: General operational info
   - WARNING: Something unexpected
   - ERROR: Something failed
   - CRITICAL: Application cannot continue

2. WHAT TO LOG
   - Request/response info
   - Prediction inputs/outputs
   - Model loading events
   - Errors with context
   - Performance metrics

3. STRUCTURED LOGGING
   - Use JSON format for easy parsing
   - Include timestamps
   - Add request IDs for tracing
   - Include model version

4. SENSITIVE DATA
   - Never log PII
   - Mask sensitive features
   - Be careful with input data
"""

print(LOGGING_PATTERNS)


# Example structured logging
def log_prediction(request_id, input_features, prediction, latency_ms):
    """Log prediction with structured data"""
    log_data = {
        "event": "prediction",
        "request_id": request_id,
        "feature_count": len(input_features) if input_features else 0,
        "prediction": prediction,
        "latency_ms": latency_ms,
    }
    logger.info(f"Prediction: {log_data}")


print("\n--- Demo: Structured Logging ---")
log_prediction("req-123", {"a": 1, "b": 2}, "ClassA", 15)

# ========== TESTING ML SYSTEMS ==========
print("\n" + "=" * 60)
print("TESTING ML SYSTEMS")
print("=" * 60)

TESTING_STRATEGIES = """
🧪 TESTING ML SYSTEMS:

1. UNIT TESTS
   - Test individual functions
   - Data preprocessing
   - Feature engineering
   - Utility functions

2. INTEGRATION TESTS
   - Test data pipeline end-to-end
   - Model loading and prediction
   - API endpoints

3. MODEL TESTS
   - Test model on known examples
   - Check output format
   - Verify predictions are within bounds
   - Test edge cases

4. DATA VALIDATION TESTS
   - Schema validation
   - Value range checks
   - Missing value handling
   - Type checking

5. PERFORMANCE TESTS
   - Latency benchmarks
   - Throughput testing
   - Memory usage
   - Load testing

6. INVARIANT TESTS
   - Test model properties that should always hold
   - e.g., probabilities sum to 1
   - Output shape is correct
"""

print(TESTING_STRATEGIES)


# Example test functions
def test_model_loads():
    """Test that model loads successfully"""
    server = ModelServer("models/test.pkl")
    assert server.load_model() is True
    print("✅ test_model_loads passed")


def test_prediction_format():
    """Test prediction returns expected format"""
    server = ModelServer("models/test.pkl")
    server.load_model()
    result = server.predict({"x": 1}, request_id="test-001")

    assert "prediction" in result
    assert "confidence" in result
    assert "model_version" in result
    print("✅ test_prediction_format passed")


def test_invalid_input():
    """Test handling of invalid input"""
    server = ModelServer("models/test.pkl")
    server.load_model()
    result = server.predict(None)

    assert "error" in result
    print("✅ test_invalid_input passed")


print("\n--- Demo: Running Tests ---")
test_model_loads()
test_prediction_format()
test_invalid_input()

# ========== DEPLOYMENT CHECKLIST ==========
print("\n" + "=" * 60)
print("DEPLOYMENT CHECKLIST")
print("=" * 60)

CHECKLIST = """
✅ PRODUCTION DEPLOYMENT CHECKLIST:

PRE-DEPLOYMENT:
[ ] Model validated on test set
[ ] Model versioned and tagged
[ ] Dependencies documented
[ ] Configuration externalized
[ ] Secrets secured
[ ] Logging configured
[ ] Health endpoints added
[ ] Tests passing
[ ] Documentation updated

DEPLOYMENT:
[ ] Use container (Docker)
[ ] Set resource limits
[ ] Configure auto-scaling
[ ] Set up load balancing
[ ] Enable HTTPS
[ ] Configure timeouts
[ ] Set up rollback plan

POST-DEPLOYMENT:
[ ] Verify health endpoints
[ ] Check logs for errors
[ ] Monitor metrics
[ ] Test with real traffic
[ ] Set up alerts
[ ] Document runbooks
"""

print(CHECKLIST)

# ========== MONITORING IN PRODUCTION ==========
print("\n" + "=" * 60)
print("MONITORING IN PRODUCTION")
print("=" * 60)


class ProductionMetrics:
    """Track production metrics"""

    def __init__(self):
        self.predictions = 0
        self.errors = 0
        self.total_latency = 0

    def record_prediction(self, latency_ms, error=False):
        """Record a prediction event"""
        self.predictions += 1
        self.total_latency += latency_ms
        if error:
            self.errors += 1

    def get_metrics(self):
        """Get current metrics"""
        avg_latency = (
            self.total_latency / self.predictions if self.predictions > 0 else 0
        )
        error_rate = self.errors / self.predictions if self.predictions > 0 else 0

        return {
            "total_predictions": self.predictions,
            "total_errors": self.errors,
            "error_rate": f"{error_rate:.2%}",
            "avg_latency_ms": round(avg_latency, 2),
        }


# Demo
print("\n--- Demo: Production Metrics ---")
metrics = ProductionMetrics()

# Simulate some predictions
for i in range(100):
    latency = 10 + (i % 5)
    error = i % 20 == 0  # 5% error rate
    metrics.record_prediction(latency, error)

print(metrics.get_metrics())

# ========== BEST PRACTICES SUMMARY ==========
print("\n" + "=" * 60)
print("PRODUCTION ML BEST PRACTICES SUMMARY")
print("=" * 60)

BEST_PRACTICES = """
🏆 KEY BEST PRACTICES:

1. VERSION EVERYTHING
   - Models, data, code, configs
   - Use semantic versioning
   - Tag releases

2. AUTOMATE EVERYTHING
   - CI/CD pipelines
   - Testing
   - Deployment
   - Monitoring

3. MONITOR CONTINUOUSLY
   - Model performance
   - Data quality
   - System health
   - Business metrics

4. DESIGN FOR FAILURE
   - Handle errors gracefully
   - Implement fallbacks
   - Plan for rollback

5. KEEP IT SIMPLE
   - Start simple, add complexity
   - Avoid premature optimization
   - Document decisions

6. SECURITY FIRST
   - Protect models
   - Secure data
   - Manage access

7. ITERATE QUICKLY
   - Small, frequent updates
   - A/B testing
   - Fast feedback loops

8. COLLABORATE EFFECTIVELY
   - Clear ownership
   - Documentation
   - Knowledge sharing
"""

print(BEST_PRACTICES)

print("\n" + "=" * 60)
print("✅ Production ML Best Practices - Complete!")
print("=" * 60)
