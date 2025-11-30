"""
Day 46 - Time Series Exercises
==============================
Practice: Time series fundamentals and data preparation

Complete each exercise to reinforce your understanding.
Solutions are at the bottom of the file.
"""

import numpy as np
import pandas as pd

# ============================================================
# EXERCISE 1: Create Time Series Data
# ============================================================
print("=" * 60)
print("EXERCISE 1: Create Time Series Data")
print("=" * 60)

print("""
Task: Create a pandas DataFrame with:
- 'date': 365 days starting from '2024-01-01'
- 'value': Numbers that include trend (increasing) and 
           seasonality (use sine wave with period 30)

Hints:
- Use pd.date_range() for dates
- Combine np.linspace() for trend
- Use np.sin() for seasonality
""")

# Your code here:




# ============================================================
# EXERCISE 2: Check Stationarity
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 2: Check Stationarity")
print("=" * 60)

print("""
Task: Write a function that checks if a series is likely 
stationary by comparing rolling mean at different windows.

Function: check_stationarity(series, window=30)
Return: True if variance of rolling mean < threshold

Hints:
- Calculate rolling mean
- Check if it varies significantly over time
""")

# Your code here:




# ============================================================
# EXERCISE 3: Create Lag Features
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 3: Create Lag Features")
print("=" * 60)

print("""
Task: Write a function that adds lag features to a DataFrame.

Function: add_lag_features(df, column, lags)
- df: DataFrame with time series
- column: Column name to create lags for
- lags: List of lag values [1, 7, 14]

Return: DataFrame with new columns like 'value_lag_1', 'value_lag_7'
""")

# Your code here:




# ============================================================
# EXERCISE 4: Rolling Statistics
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 4: Rolling Statistics")
print("=" * 60)

print("""
Task: Write a function that adds rolling statistics to a DataFrame.

Function: add_rolling_features(df, column, windows)
- df: DataFrame with time series
- column: Column name
- windows: List of window sizes [7, 14, 30]

Add for each window:
- Rolling mean
- Rolling std
- Rolling min
- Rolling max

Return: DataFrame with new columns
""")

# Your code here:




# ============================================================
# EXERCISE 5: Train-Test Split
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 5: Time-Based Train-Test Split")
print("=" * 60)

print("""
Task: Write a function that splits time series data properly.

Function: time_split(df, train_ratio=0.8)
- df: DataFrame with datetime index
- train_ratio: Proportion for training

Return: train_df, test_df (in chronological order)

Important: Do NOT shuffle the data!
""")

# Your code here:




# ============================================================
# EXERCISE 6: Autocorrelation
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 6: Calculate Autocorrelation")
print("=" * 60)

print("""
Task: Write a function to calculate autocorrelation at a given lag.

Function: autocorrelation(series, lag)
- series: Time series data (array or Series)
- lag: The lag at which to calculate autocorrelation

Return: Autocorrelation value (float between -1 and 1)

Formula: corr(Y_t, Y_{t-lag})
""")

# Your code here:




# ============================================================
# SOLUTIONS
# ============================================================

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# Solution 1
print("\n--- Solution 1: Create Time Series Data ---")
dates = pd.date_range(start='2024-01-01', periods=365, freq='D')
trend = np.linspace(100, 150, 365)
seasonality = 10 * np.sin(2 * np.pi * np.arange(365) / 30)
noise = np.random.normal(0, 3, 365)

ts_df = pd.DataFrame({
    'date': dates,
    'value': trend + seasonality + noise
})
ts_df.set_index('date', inplace=True)

print(ts_df.head())
print(f"Total records: {len(ts_df)}")

# Solution 2
print("\n--- Solution 2: Check Stationarity ---")
def check_stationarity(series, window=30, threshold=0.1):
    """Check if series is likely stationary"""
    rolling_mean = series.rolling(window=window).mean()
    
    # Divide into segments and compare means
    n_segments = 4
    segment_size = len(rolling_mean) // n_segments
    segment_means = []
    
    for i in range(n_segments):
        start = i * segment_size
        end = start + segment_size
        segment_means.append(rolling_mean.iloc[start:end].mean())
    
    # Check variation in segment means
    mean_std = np.std(segment_means)
    overall_std = series.std()
    
    ratio = mean_std / overall_std if overall_std > 0 else 0
    
    return ratio < threshold

# Test
print(f"Original series is stationary: {check_stationarity(ts_df['value'])}")

# Solution 3
print("\n--- Solution 3: Create Lag Features ---")
def add_lag_features(df, column, lags):
    """Add lag features to DataFrame"""
    result = df.copy()
    for lag in lags:
        result[f'{column}_lag_{lag}'] = result[column].shift(lag)
    return result

# Test
ts_with_lags = add_lag_features(ts_df, 'value', [1, 7, 14])
print(ts_with_lags.dropna().head())

# Solution 4
print("\n--- Solution 4: Rolling Statistics ---")
def add_rolling_features(df, column, windows):
    """Add rolling statistics to DataFrame"""
    result = df.copy()
    for window in windows:
        result[f'{column}_rolling_mean_{window}'] = result[column].rolling(window).mean()
        result[f'{column}_rolling_std_{window}'] = result[column].rolling(window).std()
        result[f'{column}_rolling_min_{window}'] = result[column].rolling(window).min()
        result[f'{column}_rolling_max_{window}'] = result[column].rolling(window).max()
    return result

# Test
ts_with_rolling = add_rolling_features(ts_df, 'value', [7, 14])
print(ts_with_rolling.dropna().head())

# Solution 5
print("\n--- Solution 5: Time-Based Train-Test Split ---")
def time_split(df, train_ratio=0.8):
    """Split time series data chronologically"""
    n = len(df)
    train_size = int(n * train_ratio)
    
    train_df = df.iloc[:train_size]
    test_df = df.iloc[train_size:]
    
    return train_df, test_df

# Test
train, test = time_split(ts_df)
print(f"Train size: {len(train)}")
print(f"Test size: {len(test)}")
print(f"Train period: {train.index[0].date()} to {train.index[-1].date()}")
print(f"Test period: {test.index[0].date()} to {test.index[-1].date()}")

# Solution 6
print("\n--- Solution 6: Calculate Autocorrelation ---")
def autocorrelation(series, lag):
    """Calculate autocorrelation at given lag"""
    series = np.array(series)
    n = len(series)
    
    if lag >= n:
        raise ValueError(f"Lag {lag} too large for series of length {n}")
    
    # Remove mean
    series_mean = np.mean(series)
    series_centered = series - series_mean
    
    # Calculate autocorrelation
    numerator = np.sum(series_centered[:n-lag] * series_centered[lag:])
    denominator = np.sum(series_centered ** 2)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

# Test
for lag in [1, 7, 14, 30]:
    acf = autocorrelation(ts_df['value'], lag)
    print(f"Autocorrelation at lag {lag}: {acf:.4f}")

print("\n✅ All solutions complete!")
