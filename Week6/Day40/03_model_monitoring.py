"""
Day 40 - Model Monitoring
=========================
Learn: Monitoring ML models in production

Key Concepts:
- Model performance can degrade over time
- Data drift and concept drift are common issues
- Monitoring is essential for maintaining model quality
"""

import random
from datetime import datetime, timedelta

# ========== WHY MODEL MONITORING? ==========
print("=" * 60)
print("WHY MODEL MONITORING?")
print("=" * 60)

MONITORING_IMPORTANCE = """
ML models can fail silently in production!

📉 REASONS FOR MODEL DEGRADATION:

1. DATA DRIFT
   - Input data distribution changes
   - Example: Customer behavior changes seasonally
   
2. CONCEPT DRIFT
   - Relationship between features and target changes
   - Example: What defines spam email evolves
   
3. FEATURE DRIFT
   - Individual feature distributions change
   - Example: Average transaction amount increases
   
4. LABEL SHIFT
   - Distribution of target variable changes
   - Example: More fraud cases than before
   
5. UPSTREAM DATA ISSUES
   - Data pipeline problems
   - Missing features
   - Schema changes

Without monitoring, you won't know your model is failing!
"""

print(MONITORING_IMPORTANCE)

# ========== TYPES OF MODEL MONITORING ==========
print("\n" + "=" * 60)
print("TYPES OF MODEL MONITORING")
print("=" * 60)

MONITORING_TYPES = """
🔍 PERFORMANCE MONITORING
   - Track prediction accuracy over time
   - Compare against baseline metrics
   - Alert when metrics drop

📊 DATA MONITORING
   - Monitor input data quality
   - Detect missing values, outliers
   - Track feature distributions

⚡ OPERATIONAL MONITORING
   - Latency and throughput
   - Error rates
   - Resource usage

📈 BUSINESS MONITORING
   - Business KPIs
   - Revenue impact
   - User engagement
"""

print(MONITORING_TYPES)

# ========== DATA DRIFT DETECTION ==========
print("\n" + "=" * 60)
print("DATA DRIFT DETECTION")
print("=" * 60)


class DataDriftDetector:
    """
    Detect data drift using statistical tests.
    """

    def __init__(self, reference_data, threshold=0.05):
        """
        Initialize with reference (training) data.
        
        Args:
            reference_data: Dictionary of feature_name -> values
            threshold: P-value threshold for drift detection
        """
        self.reference_data = reference_data
        self.threshold = threshold

    def _calculate_stats(self, data):
        """Calculate basic statistics"""
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std = variance**0.5
        return {"mean": mean, "std": std, "min": min(data), "max": max(data)}

    def _ks_test_approximation(self, ref_data, curr_data):
        """
        Simplified Kolmogorov-Smirnov test approximation.
        In production, use scipy.stats.ks_2samp
        """
        ref_sorted = sorted(ref_data)
        curr_sorted = sorted(curr_data)

        # Calculate maximum difference in CDFs (simplified)
        ref_mean, ref_std = sum(ref_data) / len(ref_data), (
            sum((x - sum(ref_data) / len(ref_data)) ** 2 for x in ref_data)
            / len(ref_data)
        ) ** 0.5
        curr_mean, curr_std = sum(curr_data) / len(curr_data), (
            sum((x - sum(curr_data) / len(curr_data)) ** 2 for x in curr_data)
            / len(curr_data)
        ) ** 0.5

        # Use normalized difference as proxy for p-value
        if ref_std > 0:
            z_score = abs(ref_mean - curr_mean) / ref_std
            # Approximate p-value (simplified)
            p_value = max(0, 1 - z_score / 3)
        else:
            p_value = 1.0 if ref_mean == curr_mean else 0.0

        return p_value

    def detect_drift(self, current_data):
        """
        Detect drift for all features.
        
        Args:
            current_data: Dictionary of feature_name -> values
            
        Returns:
            Dictionary with drift detection results
        """
        results = {}

        for feature in self.reference_data:
            if feature not in current_data:
                results[feature] = {
                    "drift_detected": True,
                    "reason": "Feature missing in current data",
                }
                continue

            ref = self.reference_data[feature]
            curr = current_data[feature]

            p_value = self._ks_test_approximation(ref, curr)
            drift_detected = p_value < self.threshold

            ref_stats = self._calculate_stats(ref)
            curr_stats = self._calculate_stats(curr)

            results[feature] = {
                "drift_detected": drift_detected,
                "p_value": round(p_value, 4),
                "reference_stats": ref_stats,
                "current_stats": curr_stats,
                "mean_shift": round(curr_stats["mean"] - ref_stats["mean"], 4),
            }

        return results

    def report(self, current_data):
        """Generate a drift report"""
        results = self.detect_drift(current_data)

        print("\n📊 DATA DRIFT REPORT")
        print("=" * 50)

        drifted_features = []
        for feature, info in results.items():
            status = "🔴 DRIFT" if info["drift_detected"] else "🟢 OK"
            print(f"\n{feature}: {status}")

            if "p_value" in info:
                print(f"   P-value: {info['p_value']}")
                print(f"   Mean shift: {info['mean_shift']}")

            if info["drift_detected"]:
                drifted_features.append(feature)

        print("\n" + "=" * 50)
        print(f"Summary: {len(drifted_features)}/{len(results)} features drifted")

        return results


# Demo
print("\n--- Demo: Data Drift Detection ---\n")

# Reference data (from training time)
reference_data = {
    "age": [25 + random.randint(-5, 5) for _ in range(1000)],
    "income": [50000 + random.randint(-10000, 10000) for _ in range(1000)],
    "score": [0.5 + random.random() * 0.3 for _ in range(1000)],
}

# Current data (no drift)
current_data_no_drift = {
    "age": [25 + random.randint(-5, 5) for _ in range(100)],
    "income": [50000 + random.randint(-10000, 10000) for _ in range(100)],
    "score": [0.5 + random.random() * 0.3 for _ in range(100)],
}

# Current data (with drift)
current_data_with_drift = {
    "age": [35 + random.randint(-5, 5) for _ in range(100)],  # Age shifted up
    "income": [70000 + random.randint(-10000, 10000) for _ in range(100)],  # Income increased
    "score": [0.5 + random.random() * 0.3 for _ in range(100)],  # No drift
}

detector = DataDriftDetector(reference_data)

print("Testing with NO drift:")
detector.report(current_data_no_drift)

print("\n\nTesting with DRIFT:")
detector.report(current_data_with_drift)

# ========== PERFORMANCE MONITORING ==========
print("\n" + "=" * 60)
print("PERFORMANCE MONITORING")
print("=" * 60)


class ModelPerformanceMonitor:
    """Monitor model performance over time"""

    def __init__(self, baseline_metrics, alert_threshold=0.1):
        """
        Initialize monitor.
        
        Args:
            baseline_metrics: Dict of metric_name -> baseline_value
            alert_threshold: Relative drop that triggers alert
        """
        self.baseline = baseline_metrics
        self.threshold = alert_threshold
        self.history = []

    def log_metrics(self, metrics, timestamp=None):
        """Log current metrics"""
        timestamp = timestamp or datetime.now()
        entry = {"timestamp": timestamp, "metrics": metrics, "alerts": []}

        # Check for alerts
        for metric, value in metrics.items():
            if metric in self.baseline:
                baseline_value = self.baseline[metric]
                relative_change = (baseline_value - value) / baseline_value

                if relative_change > self.threshold:
                    entry["alerts"].append(
                        {
                            "metric": metric,
                            "baseline": baseline_value,
                            "current": value,
                            "drop": f"{relative_change*100:.1f}%",
                        }
                    )

        self.history.append(entry)

        if entry["alerts"]:
            print(f"⚠️  ALERT at {timestamp}:")
            for alert in entry["alerts"]:
                print(f"   {alert['metric']}: dropped {alert['drop']} ", end="")
                print(f"(baseline: {alert['baseline']:.3f}, current: {alert['current']:.3f})")
        else:
            print(f"✅ Metrics OK at {timestamp}")

        return entry

    def get_trend(self, metric):
        """Get trend for a specific metric"""
        values = [
            (h["timestamp"], h["metrics"].get(metric))
            for h in self.history
            if metric in h["metrics"]
        ]
        return values

    def summary_report(self):
        """Generate summary report"""
        print("\n📈 PERFORMANCE MONITORING SUMMARY")
        print("=" * 50)

        total_alerts = sum(len(h["alerts"]) for h in self.history)
        print(f"Total data points: {len(self.history)}")
        print(f"Total alerts: {total_alerts}")

        if self.history:
            latest = self.history[-1]
            print("\nLatest metrics:")
            for metric, value in latest["metrics"].items():
                baseline = self.baseline.get(metric, "N/A")
                print(f"   {metric}: {value:.3f} (baseline: {baseline})")


# Demo
print("\n--- Demo: Performance Monitoring ---\n")

monitor = ModelPerformanceMonitor(
    baseline_metrics={"accuracy": 0.95, "precision": 0.93, "recall": 0.91},
    alert_threshold=0.05,
)

# Simulate metrics over time
base_time = datetime.now()
simulated_metrics = [
    {"accuracy": 0.94, "precision": 0.92, "recall": 0.90},  # Slight drop, OK
    {"accuracy": 0.93, "precision": 0.91, "recall": 0.89},  # More drop, still OK
    {"accuracy": 0.88, "precision": 0.87, "recall": 0.85},  # Significant drop - ALERT
    {"accuracy": 0.92, "precision": 0.90, "recall": 0.88},  # Recovery
]

for i, metrics in enumerate(simulated_metrics):
    timestamp = base_time + timedelta(hours=i)
    monitor.log_metrics(metrics, timestamp)

monitor.summary_report()

# ========== PREDICTION LOGGING ==========
print("\n" + "=" * 60)
print("PREDICTION LOGGING")
print("=" * 60)


class PredictionLogger:
    """Log predictions for monitoring and debugging"""

    def __init__(self, log_path="predictions.log"):
        self.log_path = log_path
        self.predictions = []

    def log(self, input_features, prediction, confidence, actual=None, metadata=None):
        """Log a prediction"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "input_features": input_features,
            "prediction": prediction,
            "confidence": confidence,
            "actual": actual,
            "metadata": metadata or {},
        }
        self.predictions.append(entry)
        return entry

    def get_accuracy(self, window_size=None):
        """Calculate accuracy from logged predictions with actuals"""
        preds_with_actuals = [p for p in self.predictions if p["actual"] is not None]

        if window_size:
            preds_with_actuals = preds_with_actuals[-window_size:]

        if not preds_with_actuals:
            return None

        correct = sum(1 for p in preds_with_actuals if p["prediction"] == p["actual"])
        return correct / len(preds_with_actuals)

    def get_low_confidence_predictions(self, threshold=0.5):
        """Get predictions with low confidence"""
        return [p for p in self.predictions if p["confidence"] < threshold]


# Demo
print("\n--- Demo: Prediction Logging ---\n")
logger = PredictionLogger()

# Simulate some predictions
sample_predictions = [
    ({"feature1": 1.0, "feature2": 2.0}, "ClassA", 0.95, "ClassA"),
    ({"feature1": 1.5, "feature2": 2.5}, "ClassB", 0.88, "ClassB"),
    ({"feature1": 2.0, "feature2": 1.0}, "ClassA", 0.45, "ClassB"),  # Wrong, low confidence
    ({"feature1": 1.2, "feature2": 2.2}, "ClassB", 0.92, "ClassB"),
    ({"feature1": 1.8, "feature2": 1.8}, "ClassA", 0.78, "ClassA"),
]

for features, pred, conf, actual in sample_predictions:
    logger.log(features, pred, conf, actual)

print(f"Logged {len(logger.predictions)} predictions")
print(f"Accuracy: {logger.get_accuracy():.2%}")
print(f"Low confidence predictions: {len(logger.get_low_confidence_predictions(0.5))}")

# ========== ALERTING STRATEGIES ==========
print("\n" + "=" * 60)
print("ALERTING STRATEGIES")
print("=" * 60)

ALERTING_STRATEGIES = """
🚨 ALERTING BEST PRACTICES:

1. SET APPROPRIATE THRESHOLDS
   - Too sensitive = alert fatigue
   - Too lenient = miss real issues
   - Use historical data to calibrate

2. USE MULTIPLE METRICS
   - Don't rely on single metric
   - Combine accuracy, latency, errors
   - Business metrics too

3. IMPLEMENT ALERT LEVELS
   - INFO: For logging, no action needed
   - WARNING: Investigate when convenient
   - CRITICAL: Immediate action required

4. AVOID ALERT FATIGUE
   - Group related alerts
   - Implement cooldown periods
   - Only alert on actionable issues

5. SET UP ESCALATION
   - Start with team notification
   - Escalate if not acknowledged
   - Include runbooks for common issues
"""

print(ALERTING_STRATEGIES)


class AlertManager:
    """Simple alert manager"""

    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

    def __init__(self):
        self.alerts = []

    def alert(self, level, message, metadata=None):
        """Create an alert"""
        alert = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message,
            "metadata": metadata or {},
        }
        self.alerts.append(alert)

        icon = {"INFO": "ℹ️", "WARNING": "⚠️", "CRITICAL": "🚨"}.get(level, "")
        print(f"{icon} [{level}] {message}")

        return alert


# Demo
print("\n--- Demo: Alert Manager ---")
alerts = AlertManager()
alerts.alert(AlertManager.INFO, "Model version 2.0 deployed")
alerts.alert(AlertManager.WARNING, "Accuracy dropped to 0.88 (threshold: 0.90)")
alerts.alert(AlertManager.CRITICAL, "Model latency exceeds 5s")

# ========== MONITORING DASHBOARD METRICS ==========
print("\n" + "=" * 60)
print("KEY MONITORING METRICS")
print("=" * 60)

KEY_METRICS = """
📊 ESSENTIAL METRICS TO TRACK:

MODEL PERFORMANCE:
- Accuracy, Precision, Recall, F1
- AUC-ROC, AUC-PR
- Mean Squared Error (regression)
- Custom business metrics

DATA QUALITY:
- Missing value rate
- Feature distribution statistics
- Outlier percentage
- Data freshness

OPERATIONAL:
- Prediction latency (p50, p95, p99)
- Throughput (predictions/second)
- Error rate
- Model load time

INFRASTRUCTURE:
- CPU/Memory usage
- Disk space
- Network latency
- Container health
"""

print(KEY_METRICS)

print("\n" + "=" * 60)
print("✅ Model Monitoring - Complete!")
print("=" * 60)
