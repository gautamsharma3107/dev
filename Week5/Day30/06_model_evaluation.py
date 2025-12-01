"""
Day 30 - Model Evaluation and Prediction
==========================================
Learn: Evaluating models and making predictions

Key Concepts:
- Evaluating model performance
- Making predictions on new data
- Saving and loading models
- Using models in production
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Set seeds
tf.random.set_seed(42)
np.random.seed(42)

# ========== PREPARE DATA ==========
print("=" * 60)
print("PREPARING DATA FOR EVALUATION")
print("=" * 60)

# Create dataset
X, y = make_classification(
    n_samples=2000,
    n_features=20,
    n_informative=15,
    n_classes=2,
    random_state=42
)

# Split data: train, validation, test
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

print(f"Training samples: {len(X_train)}")
print(f"Validation samples: {len(X_val)}")
print(f"Test samples: {len(X_test)}")

# Build and train model
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("\nTraining model...")
history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=32,
    validation_data=(X_val, y_val),
    verbose=0
)
print("✅ Training complete!")

# ========== MODEL EVALUATION ==========
print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print("""
model.evaluate() returns loss and metrics on given data.
Always evaluate on TEST data (never seen during training).
""")

# Evaluate on test data
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

print(f"\nTest Set Evaluation:")
print(f"  Loss: {test_loss:.4f}")
print(f"  Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

# Compare with training and validation
print(f"\nComparison:")
print(f"  Training Accuracy: {history.history['accuracy'][-1]:.4f}")
print(f"  Validation Accuracy: {history.history['val_accuracy'][-1]:.4f}")
print(f"  Test Accuracy: {test_accuracy:.4f}")

# ========== MAKING PREDICTIONS ==========
print("\n" + "=" * 60)
print("MAKING PREDICTIONS")
print("=" * 60)

# Predict probabilities
y_pred_prob = model.predict(X_test, verbose=0)

print("Prediction output (probabilities):")
print(f"  Shape: {y_pred_prob.shape}")
print(f"  First 5 predictions: {y_pred_prob[:5].flatten()}")

# Convert probabilities to classes (threshold = 0.5)
y_pred_classes = (y_pred_prob > 0.5).astype(int).flatten()

print(f"\nConverted to classes (threshold=0.5):")
print(f"  First 5 predictions: {y_pred_classes[:5]}")
print(f"  First 5 actual: {y_test[:5]}")

# ========== DETAILED METRICS ==========
print("\n" + "=" * 60)
print("DETAILED CLASSIFICATION METRICS")
print("=" * 60)

print("""
Beyond accuracy, evaluate models with:
- Precision: Of predicted positives, how many are correct?
- Recall: Of actual positives, how many did we find?
- F1-Score: Balance between precision and recall
- Confusion Matrix: True/False Positives/Negatives
""")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_classes, target_names=['Class 0', 'Class 1']))

# Confusion matrix
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred_classes)
print(cm)
print("""
    Predicted
    0      1
Actual 0  [TN     FP]
       1  [FN     TP]

TN (True Negative): Correctly predicted negative
FP (False Positive): Incorrectly predicted positive
FN (False Negative): Incorrectly predicted negative
TP (True Positive): Correctly predicted positive
""")

# ========== PREDICTION ON SINGLE SAMPLES ==========
print("=" * 60)
print("PREDICTING ON SINGLE SAMPLES")
print("=" * 60)

# Single sample prediction
single_sample = X_test[0:1]  # Keep 2D shape (1, 20)
single_prediction = model.predict(single_sample, verbose=0)

print(f"Single sample shape: {single_sample.shape}")
print(f"Prediction probability: {single_prediction[0][0]:.4f}")
print(f"Predicted class: {1 if single_prediction[0][0] > 0.5 else 0}")
print(f"Actual class: {y_test[0]}")

# Multiple samples
batch_samples = X_test[:10]
batch_predictions = model.predict(batch_samples, verbose=0)

print(f"\nBatch prediction (10 samples):")
print(f"  Predicted: {(batch_predictions > 0.5).astype(int).flatten()}")
print(f"  Actual:    {y_test[:10]}")

# ========== CUSTOM THRESHOLD ==========
print("\n" + "=" * 60)
print("CUSTOM DECISION THRESHOLD")
print("=" * 60)

print("""
Default threshold is 0.5, but you can adjust it:
- Higher threshold (0.7): More confident predictions, fewer positives
- Lower threshold (0.3): More sensitive, catches more positives

Useful when false positives/negatives have different costs.
""")

# Test different thresholds
thresholds = [0.3, 0.5, 0.7]

for threshold in thresholds:
    y_pred_custom = (y_pred_prob > threshold).astype(int).flatten()
    accuracy = np.mean(y_pred_custom == y_test)
    positives = np.sum(y_pred_custom)
    print(f"Threshold {threshold}: Accuracy={accuracy:.4f}, Predicted Positives={positives}")

# ========== SAVING MODELS ==========
print("\n" + "=" * 60)
print("SAVING AND LOADING MODELS")
print("=" * 60)

print("""
Save models to use later without retraining!

Methods:
1. model.save(): Save entire model (architecture + weights + optimizer)
2. model.save_weights(): Save only weights
3. model.to_json(): Save only architecture
""")

# Save entire model (recommended)
model.save('/tmp/my_first_model.keras')
print("✅ Model saved to '/tmp/my_first_model.keras'")

# Save weights only
model.save_weights('/tmp/model_weights.weights.h5')
print("✅ Weights saved to '/tmp/model_weights.weights.h5'")

# ========== LOADING MODELS ==========
print("\n" + "=" * 60)
print("LOADING SAVED MODELS")
print("=" * 60)

# Load entire model
loaded_model = load_model('/tmp/my_first_model.keras')
print("✅ Model loaded from file")

# Verify loaded model works
loaded_predictions = loaded_model.predict(X_test[:5], verbose=0)
print(f"\nPredictions from loaded model:")
print(f"  {loaded_predictions.flatten()}")

# Verify same as original
original_predictions = model.predict(X_test[:5], verbose=0)
print(f"\nPredictions from original model:")
print(f"  {original_predictions.flatten()}")

print(f"\nPredictions match: {np.allclose(loaded_predictions, original_predictions)}")

# ========== USING MODEL IN PRODUCTION ==========
print("\n" + "=" * 60)
print("USING MODEL IN PRODUCTION")
print("=" * 60)

print("""
Production workflow:

1. Train and evaluate model
2. Save the trained model
3. Save the scaler (important!)
4. In production:
   - Load model and scaler
   - Scale new data with saved scaler
   - Make predictions
   - Return results
""")

# Example production code
def predict_new_data(model, scaler, new_data):
    """Make predictions on new data."""
    # Scale the data using the SAME scaler
    scaled_data = scaler.transform(new_data)
    
    # Get predictions
    probabilities = model.predict(scaled_data, verbose=0)
    
    # Convert to classes
    predictions = (probabilities > 0.5).astype(int).flatten()
    
    return predictions, probabilities.flatten()

# Simulate new data (3 samples, 20 features)
new_data = np.random.randn(3, 20)

# Get predictions
predictions, probabilities = predict_new_data(loaded_model, scaler, new_data)

print("\nPredictions on new data:")
for i in range(len(predictions)):
    print(f"  Sample {i+1}: Class={predictions[i]}, Probability={probabilities[i]:.4f}")

# Save scaler (using pickle)
import pickle
with open('/tmp/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print("\n✅ Scaler saved for production use")

# ========== MODEL SUMMARY ==========
print("\n" + "=" * 60)
print("MODEL SUMMARY")
print("=" * 60)

print(f"""
Final Model Performance:
  Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)
  Test Loss: {test_loss:.4f}

Files Saved:
  Model: /tmp/my_first_model.keras
  Weights: /tmp/model_weights.weights.h5
  Scaler: /tmp/scaler.pkl

The model is ready for deployment!
""")

print("\n" + "=" * 60)
print("✅ Model Evaluation - Complete!")
print("=" * 60)
print("\nCongratulations! You've completed Day 30!")
print("Now try the exercises and mini-project to practice!")
