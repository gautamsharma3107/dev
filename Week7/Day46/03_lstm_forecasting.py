"""
Day 46 - LSTM for Forecasting
=============================
Learn: Using LSTM neural networks for time series prediction

Key Concepts:
- Sequence data preparation
- LSTM architecture for time series
- Building forecasting models
- Predictions and evaluation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ========== WHY LSTM FOR TIME SERIES? ==========
print("=" * 60)
print("WHY LSTM FOR TIME SERIES?")
print("=" * 60)

print("""
LSTM (Long Short-Term Memory) advantages:

✅ Captures long-term dependencies
   - Can "remember" patterns from far back
   - Better than traditional RNNs

✅ Handles non-linear patterns
   - Complex relationships
   - Feature interactions

✅ No stationarity requirement
   - Can learn from raw data
   - Less preprocessing needed

✅ Multi-step forecasting
   - Predict multiple future values
   - Seq-to-seq architecture

When to use LSTM:
- Complex non-linear patterns
- Long-range dependencies
- Multiple input features
- Enough data (1000+ samples)

When ARIMA might be better:
- Simple linear patterns
- Small datasets
- Interpretability needed
- Quick prototyping
""")

# ========== LSTM ARCHITECTURE ==========
print("\n" + "=" * 60)
print("LSTM ARCHITECTURE")
print("=" * 60)

print("""
LSTM Cell Components:

┌──────────────────────────────────────────────┐
│                                              │
│   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐    │
│   │  σ  │   │  σ  │   │ tanh│   │  σ  │    │
│   └──┬──┘   └──┬──┘   └──┬──┘   └──┬──┘    │
│      │         │         │         │        │
│   Forget    Input    Candidate   Output     │
│    Gate      Gate      Cell       Gate      │
│                                              │
└──────────────────────────────────────────────┘

1. FORGET GATE: What to discard from memory
2. INPUT GATE: What new information to store
3. CANDIDATE: New candidate values
4. OUTPUT GATE: What to output

This allows LSTM to:
- Remember important patterns
- Forget irrelevant information
- Control information flow
""")

# ========== DATA PREPARATION ==========
print("\n" + "=" * 60)
print("DATA PREPARATION FOR LSTM")
print("=" * 60)

print("""
LSTM input shape: (samples, timesteps, features)

Example: Predict next day using last 10 days
- samples: Number of training examples
- timesteps: 10 (look-back window)
- features: 1 (univariate) or more (multivariate)

Steps:
1. Scale data (usually 0-1 with MinMaxScaler)
2. Create sequences (sliding window)
3. Split into train/test (time-based!)
4. Reshape for LSTM
""")

# Create sample data
np.random.seed(42)
n_samples = 500

# Create synthetic data with pattern
t = np.arange(n_samples)
data = 50 + 20 * np.sin(2 * np.pi * t / 50) + np.random.normal(0, 3, n_samples)

print(f"\nGenerated {n_samples} data points")
print(f"Data range: [{data.min():.2f}, {data.max():.2f}]")

# ========== SCALING ==========
print("\n" + "=" * 60)
print("SCALING DATA")
print("=" * 60)

print("""
Scaling is CRITICAL for neural networks!

MinMaxScaler: Scale to [0, 1]
  X_scaled = (X - X_min) / (X_max - X_min)

StandardScaler: Scale to mean=0, std=1
  X_scaled = (X - mean) / std

Important: Fit scaler on TRAINING data only!
""")

# Simple MinMax scaling
def min_max_scale(data, min_val=None, max_val=None):
    """Scale data to [0, 1] range"""
    if min_val is None:
        min_val = data.min()
    if max_val is None:
        max_val = data.max()
    return (data - min_val) / (max_val - min_val), min_val, max_val

def inverse_scale(scaled_data, min_val, max_val):
    """Reverse the scaling"""
    return scaled_data * (max_val - min_val) + min_val

# Split first, then scale
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

# Scale using training data statistics
train_scaled, data_min, data_max = min_max_scale(train_data)
test_scaled = (test_data - data_min) / (data_max - data_min)

print(f"\nTraining data: {len(train_data)} samples")
print(f"Test data: {len(test_data)} samples")
print(f"Scale parameters: min={data_min:.2f}, max={data_max:.2f}")
print(f"Scaled range: [{train_scaled.min():.4f}, {train_scaled.max():.4f}]")

# ========== CREATING SEQUENCES ==========
print("\n" + "=" * 60)
print("CREATING SEQUENCES")
print("=" * 60)

print("""
Sliding window approach:

Data: [a, b, c, d, e, f, g, h]
Window size: 3

Sequences (X) → Target (y):
[a, b, c] → d
[b, c, d] → e
[c, d, e] → f
[d, e, f] → g
[e, f, g] → h
""")

def create_sequences(data, window_size):
    """Create sequences for LSTM"""
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:(i + window_size)])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)

# Create sequences
window_size = 10
X_train, y_train = create_sequences(train_scaled, window_size)
X_test, y_test = create_sequences(test_scaled, window_size)

print(f"\nWindow size: {window_size}")
print(f"Training sequences: {X_train.shape[0]}")
print(f"Test sequences: {X_test.shape[0]}")

# Reshape for LSTM: (samples, timesteps, features)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

print(f"\nReshaped X_train: {X_train.shape}")
print(f"Reshaped X_test: {X_test.shape}")

# ========== BUILDING LSTM MODEL ==========
print("\n" + "=" * 60)
print("BUILDING LSTM MODEL (TensorFlow/Keras)")
print("=" * 60)

print("""
Basic LSTM Model Architecture:

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

model = Sequential([
    LSTM(50, activation='relu', input_shape=(window_size, 1)),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

Layers explained:
- LSTM(50): 50 LSTM units
- Dropout(0.2): 20% dropout for regularization
- Dense(1): Output layer for single prediction
""")

# Simple model demonstration (without TensorFlow)
print("\nSimple Neural Network Demonstration:")
print("(Using basic numpy implementation for concept)")

class SimpleLSTMDemo:
    """Simplified demo - not a real LSTM"""
    
    def __init__(self, hidden_size=20):
        self.hidden_size = hidden_size
        np.random.seed(42)
        # Simple weights (not actual LSTM)
        self.w = np.random.randn(hidden_size) * 0.1
        self.b = 0
        
    def predict(self, X):
        """Simple linear prediction for demo"""
        # Average of sequence * learned weight
        seq_mean = X.mean(axis=1).flatten()
        return seq_mean * self.w.mean() + self.b
    
    def fit(self, X, y, epochs=100, lr=0.01):
        """Simple gradient descent"""
        for epoch in range(epochs):
            # Predictions
            pred = self.predict(X)
            
            # Loss (MSE)
            loss = np.mean((pred - y) ** 2)
            
            # Simple gradient
            grad_b = np.mean(2 * (pred - y))
            
            # Update
            self.b -= lr * grad_b
            
            if (epoch + 1) % 20 == 0:
                print(f"  Epoch {epoch+1}/{epochs}, Loss: {loss:.6f}")
        
        return self

# Demo training
demo_model = SimpleLSTMDemo()
print("\nTraining demo model...")
demo_model.fit(X_train.reshape(X_train.shape[0], -1), y_train)

# Demo predictions
demo_pred = demo_model.predict(X_test.reshape(X_test.shape[0], -1))

# ========== ACTUAL KERAS MODEL CODE ==========
print("\n" + "=" * 60)
print("COMPLETE KERAS MODEL CODE")
print("=" * 60)

keras_code = """
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# 1. Prepare data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data.reshape(-1, 1))

# 2. Create sequences
def create_sequences(data, window_size):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:(i + window_size)])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)

window_size = 20
X, y = create_sequences(scaled_data, window_size)

# 3. Split data
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# 4. Build model
model = Sequential([
    LSTM(64, activation='relu', return_sequences=True,
         input_shape=(window_size, 1)),
    Dropout(0.2),
    LSTM(32, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 5. Train with early stopping
early_stop = EarlyStopping(monitor='val_loss', patience=10,
                           restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.1,
    callbacks=[early_stop],
    verbose=1
)

# 6. Evaluate
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f'Test MAE: {test_mae:.4f}')

# 7. Make predictions
predictions = model.predict(X_test)

# 8. Inverse transform to original scale
predictions_original = scaler.inverse_transform(predictions)
y_test_original = scaler.inverse_transform(y_test)
"""

print(keras_code)

# ========== MODEL VARIATIONS ==========
print("\n" + "=" * 60)
print("MODEL VARIATIONS")
print("=" * 60)

print("""
1. STACKED LSTM (deeper networks)
   LSTM(64, return_sequences=True)
   LSTM(32, return_sequences=True)
   LSTM(16)
   Dense(1)

2. BIDIRECTIONAL LSTM
   from tensorflow.keras.layers import Bidirectional
   Bidirectional(LSTM(50))

3. SEQUENCE-TO-SEQUENCE (multi-step)
   # Encoder
   LSTM(64, return_sequences=True)
   LSTM(32)
   
   # Decoder
   RepeatVector(output_steps)
   LSTM(32, return_sequences=True)
   TimeDistributed(Dense(1))

4. MULTIVARIATE (multiple features)
   input_shape=(window_size, n_features)
   # Include: price, volume, indicators, etc.

5. CNN-LSTM HYBRID
   Conv1D(32, kernel_size=3)
   MaxPooling1D()
   LSTM(50)
   Dense(1)
""")

# ========== MULTI-STEP FORECASTING ==========
print("\n" + "=" * 60)
print("MULTI-STEP FORECASTING")
print("=" * 60)

print("""
Methods for predicting multiple future steps:

1. RECURSIVE (Iterative)
   - Predict t+1
   - Use prediction to predict t+2
   - Continue...
   ⚠️ Errors accumulate

2. DIRECT (Multiple Models)
   - Train separate model for each step
   - Model 1 predicts t+1
   - Model 2 predicts t+2
   ⚠️ Ignores dependencies

3. MULTIPLE OUTPUT (Single Model)
   - One model, multiple outputs
   Dense(n_steps)
   ✅ Learns dependencies

4. SEQ2SEQ (Encoder-Decoder)
   - Encode entire input sequence
   - Decode to output sequence
   ✅ Best for long sequences
""")

# Recursive forecasting demo
def recursive_forecast(model_predict, last_sequence, n_steps):
    """Recursive multi-step forecasting"""
    forecasts = []
    current_seq = last_sequence.copy()
    
    for _ in range(n_steps):
        # Predict next step
        next_pred = model_predict(current_seq.reshape(1, -1))
        forecasts.append(next_pred[0])
        
        # Update sequence (remove oldest, add prediction)
        current_seq = np.append(current_seq[1:], next_pred)
    
    return np.array(forecasts)

# Demo
last_seq = X_test[-1].flatten()
multi_step = recursive_forecast(demo_model.predict, last_seq, 10)

print("\nRecursive Forecast (10 steps):")
for i, val in enumerate(multi_step, 1):
    original_val = inverse_scale(val, data_min, data_max)
    print(f"  t+{i}: {original_val:.2f}")

# ========== HYPERPARAMETER TUNING ==========
print("\n" + "=" * 60)
print("HYPERPARAMETER TUNING")
print("=" * 60)

print("""
Key hyperparameters to tune:

1. ARCHITECTURE
   - Number of LSTM layers (1-3)
   - Units per layer (32, 64, 128, 256)
   - Dropout rate (0.1-0.5)

2. TRAINING
   - Learning rate (0.001, 0.0001)
   - Batch size (16, 32, 64)
   - Epochs (with early stopping)

3. SEQUENCE
   - Window size (10, 20, 30, 50)
   - Depends on data patterns

4. OPTIMIZER
   - Adam (recommended start)
   - RMSprop (alternative)

Grid Search Example:
param_grid = {
    'units': [32, 64, 128],
    'dropout': [0.1, 0.2, 0.3],
    'window': [10, 20, 30]
}

Use KerasTuner for automated search.
""")

# ========== EVALUATION METRICS ==========
print("\n" + "=" * 60)
print("EVALUATION METRICS")
print("=" * 60)

def evaluate_forecast(actual, predicted):
    """Calculate forecast metrics"""
    mae = np.mean(np.abs(actual - predicted))
    mse = np.mean((actual - predicted) ** 2)
    rmse = np.sqrt(mse)
    
    # MAPE (avoid division by zero)
    non_zero = actual != 0
    mape = np.mean(np.abs((actual[non_zero] - predicted[non_zero]) / actual[non_zero])) * 100
    
    return {'MAE': mae, 'MSE': mse, 'RMSE': rmse, 'MAPE': mape}

# Demo evaluation
y_actual = inverse_scale(y_test, data_min, data_max)
y_predicted = inverse_scale(demo_pred, data_min, data_max)

metrics = evaluate_forecast(y_actual, y_predicted)

print("\nDemo Model Metrics:")
for name, value in metrics.items():
    print(f"  {name}: {value:.4f}")

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("""
1. DATA PREPARATION
   ✅ Always scale your data
   ✅ Use time-based splits (no shuffling!)
   ✅ Handle missing values before modeling
   ✅ Consider differencing for trends

2. MODEL BUILDING
   ✅ Start simple, add complexity
   ✅ Use dropout to prevent overfitting
   ✅ Try different window sizes
   ✅ Use early stopping

3. TRAINING
   ✅ Use validation data
   ✅ Monitor both train and val loss
   ✅ Use callbacks (EarlyStopping, ReduceLROnPlateau)
   ✅ Save best model

4. EVALUATION
   ✅ Evaluate on unseen future data
   ✅ Use multiple metrics
   ✅ Compare with baselines (naive, ARIMA)
   ✅ Check residuals

5. COMMON MISTAKES
   ❌ Data leakage (future info in features)
   ❌ Random train/test split
   ❌ Over-complex models for simple patterns
   ❌ Ignoring baseline comparisons
""")

# ========== COMPARISON: LSTM vs ARIMA ==========
print("\n" + "=" * 60)
print("COMPARISON: LSTM vs ARIMA")
print("=" * 60)

print("""
┌─────────────────┬────────────────┬────────────────┐
│     Aspect      │     LSTM       │     ARIMA      │
├─────────────────┼────────────────┼────────────────┤
│ Complexity      │ High           │ Low            │
│ Data Required   │ Large (1000+)  │ Small (100+)   │
│ Training Time   │ Minutes-Hours  │ Seconds        │
│ Interpretability│ Black box      │ Clear          │
│ Non-linearity   │ Yes            │ No             │
│ Multi-feature   │ Natural        │ Limited        │
│ Stationarity    │ Not required   │ Required       │
│ Accuracy*       │ Often higher   │ Good for simple│
└─────────────────┴────────────────┴────────────────┘

*Accuracy depends on data complexity and size

Recommendation:
- Start with ARIMA for quick baseline
- Use LSTM when:
  • You have lots of data
  • Patterns are complex/non-linear
  • Multiple features available
  • ARIMA isn't accurate enough
""")

print("\n" + "=" * 60)
print("✅ LSTM for Forecasting - Complete!")
print("=" * 60)
