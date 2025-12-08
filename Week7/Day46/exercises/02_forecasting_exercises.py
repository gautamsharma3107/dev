"""
Day 46 - Forecasting Exercises
==============================
Practice: ARIMA, LSTM preparation, and Prophet setup

Complete each exercise to reinforce your understanding.
Solutions are at the bottom of the file.
"""

import numpy as np
import pandas as pd

# ============================================================
# EXERCISE 1: ARIMA Parameter Selection
# ============================================================
print("=" * 60)
print("EXERCISE 1: ARIMA Parameter Selection")
print("=" * 60)

print("""
Task: Given ACF and PACF patterns, determine the ARIMA(p,d,q) order.

Scenario A:
- ACF: Gradual decay
- PACF: Cuts off sharply after lag 2
What order? p=?, d=?, q=?

Scenario B:
- ACF: Cuts off after lag 1
- PACF: Gradual decay
What order? p=?, d=?, q=?

Scenario C:
- Both ACF and PACF show gradual decay
What order? p=?, d=?, q=?

Write your answers as comments below.
""")

# Your answers here:
# Scenario A: p=?, d=?, q=?
# Scenario B: p=?, d=?, q=?
# Scenario C: p=?, d=?, q=?




# ============================================================
# EXERCISE 2: Differencing
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 2: Differencing")
print("=" * 60)

print("""
Task: Write functions for first and second-order differencing.

Function 1: first_difference(series)
- Return: Y_t - Y_{t-1}

Function 2: second_difference(series)
- Return: (Y_t - Y_{t-1}) - (Y_{t-1} - Y_{t-2})

Both should drop NaN values.
""")

# Your code here:




# ============================================================
# EXERCISE 3: LSTM Sequence Creation
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 3: LSTM Sequence Creation")
print("=" * 60)

print("""
Task: Write a function to create sequences for LSTM.

Function: create_lstm_data(data, window_size, forecast_horizon=1)
- data: Array of values
- window_size: Number of past observations to use
- forecast_horizon: Number of steps to predict (default 1)

Return: X, y where
- X shape: (samples, window_size, 1)
- y shape: (samples, forecast_horizon)

For multi-step: if forecast_horizon=3, y should have next 3 values
""")

# Your code here:




# ============================================================
# EXERCISE 4: Model Evaluation Metrics
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 4: Model Evaluation Metrics")
print("=" * 60)

print("""
Task: Write a function that calculates all common forecast metrics.

Function: evaluate_forecast(actual, predicted)

Return dictionary with:
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- sMAPE (Symmetric MAPE)

Handle edge cases (division by zero, empty arrays).
""")

# Your code here:




# ============================================================
# EXERCISE 5: Prophet Data Preparation
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 5: Prophet Data Preparation")
print("=" * 60)

print("""
Task: Write a function to convert any DataFrame to Prophet format.

Function: to_prophet_format(df, date_col, value_col)
- df: Original DataFrame
- date_col: Name of date column
- value_col: Name of value column

Return: DataFrame with columns 'ds' and 'y'
- 'ds' should be datetime type
- Handle missing values (interpolate or drop)
""")

# Your code here:




# ============================================================
# EXERCISE 6: Cross-Validation for Time Series
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 6: Time Series Cross-Validation")
print("=" * 60)

print("""
Task: Write a function for time series cross-validation.

Function: time_series_cv(data, n_splits, train_size, test_size)
- data: Array or Series
- n_splits: Number of CV splits
- train_size: Minimum training samples
- test_size: Test samples per fold

Return: List of (train_idx, test_idx) tuples

Use expanding window approach:
- Fold 1: train[0:train_size], test[train_size:train_size+test_size]
- Fold 2: train[0:train_size+test_size], test[...]
- etc.
""")

# Your code here:




# ============================================================
# SOLUTIONS
# ============================================================

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# Solution 1
print("\n--- Solution 1: ARIMA Parameter Selection ---")
print("""
Scenario A:
- ACF: Gradual decay → Suggests AR process
- PACF: Cuts off at lag 2 → p = 2
Answer: ARIMA(2, 0, 0) or ARIMA(2, 1, 0) if non-stationary

Scenario B:
- ACF: Cuts off at lag 1 → q = 1
- PACF: Gradual decay → Suggests MA process
Answer: ARIMA(0, 0, 1) or ARIMA(0, 1, 1) if non-stationary

Scenario C:
- Both gradual decay → Mixed ARMA
Answer: ARIMA(1, 0, 1) or similar (try different combinations)
""")

# Solution 2
print("\n--- Solution 2: Differencing ---")
def first_difference(series):
    """First-order differencing"""
    return series.diff().dropna()

def second_difference(series):
    """Second-order differencing"""
    return series.diff().diff().dropna()

# Test
test_data = pd.Series([10, 15, 25, 40, 60, 85])
print(f"Original: {test_data.tolist()}")
print(f"First diff: {first_difference(test_data).tolist()}")
print(f"Second diff: {second_difference(test_data).tolist()}")

# Solution 3
print("\n--- Solution 3: LSTM Sequence Creation ---")
def create_lstm_data(data, window_size, forecast_horizon=1):
    """Create sequences for LSTM"""
    data = np.array(data)
    X, y = [], []
    
    for i in range(len(data) - window_size - forecast_horizon + 1):
        X.append(data[i:i + window_size])
        y.append(data[i + window_size:i + window_size + forecast_horizon])
    
    X = np.array(X)
    y = np.array(y)
    
    # Reshape X for LSTM: (samples, timesteps, features)
    X = X.reshape(X.shape[0], X.shape[1], 1)
    
    return X, y

# Test
test_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
X, y = create_lstm_data(test_data, window_size=3, forecast_horizon=2)
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"First X: {X[0].flatten()}, First y: {y[0]}")

# Solution 4
print("\n--- Solution 4: Model Evaluation Metrics ---")
def evaluate_forecast(actual, predicted):
    """Calculate forecast evaluation metrics"""
    actual = np.array(actual)
    predicted = np.array(predicted)
    
    if len(actual) == 0 or len(predicted) == 0:
        return {'error': 'Empty arrays'}
    
    # MAE
    mae = np.mean(np.abs(actual - predicted))
    
    # MSE
    mse = np.mean((actual - predicted) ** 2)
    
    # RMSE
    rmse = np.sqrt(mse)
    
    # MAPE (handle zeros)
    non_zero = actual != 0
    if np.any(non_zero):
        mape = np.mean(np.abs((actual[non_zero] - predicted[non_zero]) 
                              / actual[non_zero])) * 100
    else:
        mape = float('inf')
    
    # sMAPE (symmetric MAPE)
    denominator = np.abs(actual) + np.abs(predicted)
    non_zero_denom = denominator != 0
    if np.any(non_zero_denom):
        smape = np.mean(2 * np.abs(actual[non_zero_denom] - predicted[non_zero_denom]) 
                        / denominator[non_zero_denom]) * 100
    else:
        smape = float('inf')
    
    return {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'MAPE': mape,
        'sMAPE': smape
    }

# Test
actual = [100, 150, 200, 250]
predicted = [110, 140, 210, 260]
metrics = evaluate_forecast(actual, predicted)
for name, value in metrics.items():
    print(f"  {name}: {value:.4f}")

# Solution 5
print("\n--- Solution 5: Prophet Data Preparation ---")
def to_prophet_format(df, date_col, value_col, interpolate=True):
    """Convert DataFrame to Prophet format"""
    # Create copy with required columns
    prophet_df = pd.DataFrame({
        'ds': pd.to_datetime(df[date_col]),
        'y': df[value_col].astype(float)
    })
    
    # Handle missing values
    if interpolate:
        prophet_df['y'] = prophet_df['y'].interpolate(method='linear')
    else:
        prophet_df = prophet_df.dropna()
    
    # Sort by date
    prophet_df = prophet_df.sort_values('ds').reset_index(drop=True)
    
    return prophet_df

# Test
test_df = pd.DataFrame({
    'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'sales': [100, np.nan, 120, 130]
})
prophet_df = to_prophet_format(test_df, 'timestamp', 'sales')
print(prophet_df)

# Solution 6
print("\n--- Solution 6: Time Series Cross-Validation ---")
def time_series_cv(data, n_splits, train_size, test_size):
    """Time series cross-validation with expanding window"""
    n = len(data)
    folds = []
    
    for i in range(n_splits):
        # Training end index (expanding)
        train_end = train_size + i * test_size
        
        # Check if we have enough data
        if train_end + test_size > n:
            break
        
        train_idx = list(range(0, train_end))
        test_idx = list(range(train_end, train_end + test_size))
        
        folds.append((train_idx, test_idx))
    
    return folds

# Test
data = np.arange(100)
folds = time_series_cv(data, n_splits=5, train_size=60, test_size=10)
print(f"Number of folds: {len(folds)}")
for i, (train_idx, test_idx) in enumerate(folds):
    print(f"  Fold {i+1}: Train {len(train_idx)} samples [{train_idx[0]}-{train_idx[-1]}], "
          f"Test {len(test_idx)} samples [{test_idx[0]}-{test_idx[-1]}]")

print("\n✅ All solutions complete!")
