"""
Day 46 - Time Series Concepts
=============================
Learn: Fundamentals of time series data and analysis

Key Concepts:
- What is time series data
- Components of time series
- Stationarity and tests
- Autocorrelation and partial autocorrelation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ========== WHAT IS TIME SERIES DATA? ==========
print("=" * 60)
print("WHAT IS TIME SERIES DATA?")
print("=" * 60)

print("""
Time Series: A sequence of data points collected at regular
time intervals over a period of time.

Examples:
- Stock prices (daily closing prices)
- Temperature readings (hourly)
- Sales data (monthly)
- Website traffic (minute by minute)
- Heart rate monitoring (seconds)

Key Properties:
1. Data is ordered by time
2. Each observation depends on previous observations
3. Time intervals are usually uniform
""")

# ========== CREATING TIME SERIES DATA ==========
print("\n" + "=" * 60)
print("CREATING TIME SERIES DATA")
print("=" * 60)

# Method 1: Create datetime index
dates = pd.date_range(start='2024-01-01', periods=365, freq='D')
print(f"Created {len(dates)} daily dates")
print(f"First: {dates[0]}, Last: {dates[-1]}")

# Method 2: Create sample time series with trend and seasonality
np.random.seed(42)

# Components of our synthetic time series:
# 1. Trend (upward)
trend = np.linspace(100, 150, 365)

# 2. Seasonality (yearly pattern)
seasonal = 10 * np.sin(2 * np.pi * np.arange(365) / 365)

# 3. Random noise
noise = np.random.normal(0, 5, 365)

# Combine all components
values = trend + seasonal + noise

# Create DataFrame
ts_data = pd.DataFrame({
    'date': dates,
    'value': values
})
ts_data.set_index('date', inplace=True)

print("\nSample Time Series (first 10 rows):")
print(ts_data.head(10))

# ========== TIME SERIES COMPONENTS ==========
print("\n" + "=" * 60)
print("TIME SERIES COMPONENTS")
print("=" * 60)

print("""
A time series can be decomposed into:

1. TREND (T): Long-term direction
   - Upward, downward, or flat
   - Example: Stock market growing over decades

2. SEASONALITY (S): Regular patterns at fixed intervals
   - Daily, weekly, monthly, yearly patterns
   - Example: Ice cream sales high in summer

3. CYCLICAL (C): Patterns without fixed period
   - Business cycles, economic cycles
   - Longer than seasonal patterns

4. RESIDUAL/NOISE (R): Random fluctuations
   - Unexplained variations
   - Should be white noise ideally

Two Models:
- Additive: Y = T + S + C + R
- Multiplicative: Y = T × S × C × R
""")

# Simple decomposition visualization
print("\nVisualization of Components:")
print("(Close plot window to continue)")

fig, axes = plt.subplots(4, 1, figsize=(12, 10))

# Original
axes[0].plot(ts_data.index, ts_data['value'], 'b-')
axes[0].set_title('Original Time Series')
axes[0].set_ylabel('Value')

# Trend
axes[1].plot(ts_data.index, trend, 'g-')
axes[1].set_title('Trend Component')
axes[1].set_ylabel('Value')

# Seasonality
axes[2].plot(ts_data.index, seasonal, 'r-')
axes[2].set_title('Seasonal Component')
axes[2].set_ylabel('Value')

# Noise
axes[3].plot(ts_data.index, noise, 'gray')
axes[3].set_title('Noise/Residual Component')
axes[3].set_ylabel('Value')

plt.tight_layout()
plt.savefig('time_series_components.png', dpi=100, bbox_inches='tight')
plt.close()
print("✅ Saved 'time_series_components.png'")

# ========== STATIONARITY ==========
print("\n" + "=" * 60)
print("STATIONARITY")
print("=" * 60)

print("""
A STATIONARY time series has:
1. Constant mean over time
2. Constant variance over time
3. No seasonality

Why is stationarity important?
- Most forecasting models assume stationarity
- Statistical properties don't change over time
- Easier to model and predict

NON-STATIONARY examples:
- Stock prices (trend)
- Population growth (increasing mean)
- Seasonal sales (varying patterns)

How to make data stationary:
1. Differencing: Y_t - Y_{t-1}
2. Log transformation
3. Seasonal differencing
4. Detrending
""")

# Example: Differencing
print("\nDifferencing Example:")
original = ts_data['value'].copy()
differenced = original.diff().dropna()

print(f"Original Mean: {original.mean():.2f}")
print(f"Differenced Mean: {differenced.mean():.2f}")
print(f"\nOriginal Std: {original.std():.2f}")
print(f"Differenced Std: {differenced.std():.2f}")

# ========== TESTING FOR STATIONARITY ==========
print("\n" + "=" * 60)
print("TESTING FOR STATIONARITY")
print("=" * 60)

print("""
Augmented Dickey-Fuller (ADF) Test:
- Null Hypothesis: Time series has unit root (non-stationary)
- If p-value < 0.05: Reject null → Data IS stationary
- If p-value >= 0.05: Fail to reject → Data IS NOT stationary

from statsmodels.tsa.stattools import adfuller

result = adfuller(time_series)
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
""")

# Simple stationarity check function
def check_stationarity(series, name="Series"):
    """Simple stationarity check using rolling statistics"""
    window = min(30, len(series) // 4)
    rolling_mean = series.rolling(window=window).mean()
    rolling_std = series.rolling(window=window).std()
    
    # Calculate variance of rolling mean and std
    mean_var = rolling_mean.var()
    std_var = rolling_std.var()
    
    print(f"\n{name}:")
    print(f"  Overall Mean: {series.mean():.2f}")
    print(f"  Rolling Mean Variance: {mean_var:.4f}")
    print(f"  (Lower = more stationary)")

check_stationarity(original, "Original Series")
check_stationarity(differenced, "Differenced Series")

# ========== AUTOCORRELATION ==========
print("\n" + "=" * 60)
print("AUTOCORRELATION")
print("=" * 60)

print("""
AUTOCORRELATION (ACF):
- Correlation between observations at different time lags
- Shows how much Y_t is related to Y_{t-k}
- Useful for identifying seasonality and MA order

PARTIAL AUTOCORRELATION (PACF):
- Correlation between Y_t and Y_{t-k} after removing
  effects of intermediate lags
- Useful for identifying AR order

Interpreting ACF/PACF:
- ACF decays slowly → Non-stationary or AR process
- ACF cuts off → MA process
- PACF cuts off → AR process
- Both decay → ARMA process
""")

# Simple autocorrelation calculation
def simple_autocorr(series, lags=10):
    """Calculate autocorrelation for given lags"""
    result = []
    series = series.values if hasattr(series, 'values') else series
    n = len(series)
    mean = np.mean(series)
    var = np.var(series)
    
    for k in range(lags + 1):
        if var == 0:
            result.append(0)
        else:
            corr = np.sum((series[:n-k] - mean) * (series[k:] - mean)) / (n * var)
            result.append(corr)
    return result

acf_values = simple_autocorr(differenced, 10)
print("\nAutocorrelation values (first 10 lags):")
for i, val in enumerate(acf_values):
    bar = "█" * int(abs(val) * 20)
    sign = "+" if val >= 0 else "-"
    print(f"Lag {i:2d}: {val:6.3f} {sign}{bar}")

# ========== RESAMPLING TIME SERIES ==========
print("\n" + "=" * 60)
print("RESAMPLING TIME SERIES")
print("=" * 60)

print("""
Change the frequency of time series data:

Downsampling (lower frequency):
- 'D' → 'W': Daily to Weekly
- 'D' → 'M': Daily to Monthly
- 'D' → 'Q': Daily to Quarterly

Upsampling (higher frequency):
- 'D' → 'H': Daily to Hourly (needs interpolation)

Common aggregation methods:
- mean(), sum(), first(), last()
- min(), max(), median()
""")

# Resample examples
print("\nOriginal (Daily) - First 7 days:")
print(ts_data.head(7))

weekly = ts_data.resample('W').mean()
print("\nResampled to Weekly (mean):")
print(weekly.head(7))

monthly = ts_data.resample('ME').agg({'value': ['mean', 'min', 'max']})
print("\nResampled to Monthly with multiple aggregations:")
print(monthly.head())

# ========== ROLLING WINDOWS ==========
print("\n" + "=" * 60)
print("ROLLING WINDOWS")
print("=" * 60)

print("""
Rolling/Moving calculations over a sliding window:

Common uses:
- Smoothing noisy data
- Calculating moving averages
- Identifying trends

window.rolling(window_size).function()
""")

# Calculate rolling statistics
ts_data['MA_7'] = ts_data['value'].rolling(window=7).mean()
ts_data['MA_30'] = ts_data['value'].rolling(window=30).mean()
ts_data['Rolling_Std'] = ts_data['value'].rolling(window=30).std()

print("\nTime Series with Rolling Statistics:")
print(ts_data[['value', 'MA_7', 'MA_30', 'Rolling_Std']].dropna().head(10))

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(ts_data.index, ts_data['value'], 'b-', alpha=0.5, label='Original')
plt.plot(ts_data.index, ts_data['MA_7'], 'r-', label='7-day MA')
plt.plot(ts_data.index, ts_data['MA_30'], 'g-', linewidth=2, label='30-day MA')
plt.title('Time Series with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('moving_averages.png', dpi=100, bbox_inches='tight')
plt.close()
print("\n✅ Saved 'moving_averages.png'")

# ========== LAG FEATURES ==========
print("\n" + "=" * 60)
print("LAG FEATURES")
print("=" * 60)

print("""
Create features from past values (lags):
- Useful for ML models
- Captures temporal dependencies

df['lag_1'] = df['value'].shift(1)  # Previous day
df['lag_7'] = df['value'].shift(7)  # 1 week ago
""")

# Create lag features
ts_data['lag_1'] = ts_data['value'].shift(1)
ts_data['lag_7'] = ts_data['value'].shift(7)
ts_data['diff_1'] = ts_data['value'].diff(1)

print("\nTime Series with Lag Features:")
print(ts_data[['value', 'lag_1', 'lag_7', 'diff_1']].dropna().head(10))

# ========== TRAIN-TEST SPLIT FOR TIME SERIES ==========
print("\n" + "=" * 60)
print("TRAIN-TEST SPLIT FOR TIME SERIES")
print("=" * 60)

print("""
⚠️ IMPORTANT: Never use random split for time series!
   - Data must remain in chronological order
   - Train on past, test on future

Common approaches:
1. Simple split: first 80% train, last 20% test
2. Rolling window validation
3. Expanding window validation
""")

# Simple time-based split
train_size = int(len(ts_data) * 0.8)
train = ts_data[:train_size]
test = ts_data[train_size:]

print(f"\nDataset size: {len(ts_data)}")
print(f"Training set: {len(train)} ({len(train)/len(ts_data)*100:.1f}%)")
print(f"  From: {train.index[0].date()} to {train.index[-1].date()}")
print(f"Test set: {len(test)} ({len(test)/len(ts_data)*100:.1f}%)")
print(f"  From: {test.index[0].date()} to {test.index[-1].date()}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Analyzing Stock Data")
print("=" * 60)

# Create synthetic stock data
np.random.seed(123)
n_days = 252  # Trading days in a year

# Random walk with drift (simulating stock)
returns = np.random.normal(0.0005, 0.02, n_days)  # Daily returns
stock_prices = 100 * np.exp(np.cumsum(returns))

stock_dates = pd.bdate_range(start='2024-01-01', periods=n_days)
stock_df = pd.DataFrame({
    'close': stock_prices,
    'volume': np.random.randint(1000000, 5000000, n_days)
}, index=stock_dates)

print("Synthetic Stock Data:")
print(stock_df.head(10))

# Calculate common stock indicators
stock_df['returns'] = stock_df['close'].pct_change()
stock_df['log_returns'] = np.log(stock_df['close']).diff()
stock_df['MA_20'] = stock_df['close'].rolling(20).mean()
stock_df['MA_50'] = stock_df['close'].rolling(50).mean()
stock_df['volatility_20'] = stock_df['returns'].rolling(20).std() * np.sqrt(252)

print("\nWith Technical Indicators:")
print(stock_df[['close', 'returns', 'MA_20', 'MA_50', 'volatility_20']].dropna().head(10))

# Summary statistics
print("\nSummary Statistics:")
print(f"Starting Price: ${stock_df['close'].iloc[0]:.2f}")
print(f"Ending Price: ${stock_df['close'].iloc[-1]:.2f}")
print(f"Total Return: {(stock_df['close'].iloc[-1]/stock_df['close'].iloc[0]-1)*100:.2f}%")
print(f"Average Daily Return: {stock_df['returns'].mean()*100:.4f}%")
print(f"Volatility (annualized): {stock_df['returns'].std()*np.sqrt(252)*100:.2f}%")

# Cleanup
import os
for f in ['time_series_components.png', 'moving_averages.png']:
    if os.path.exists(f):
        os.remove(f)
print("\n✅ Cleaned up generated files")

print("\n" + "=" * 60)
print("✅ Time Series Concepts - Complete!")
print("=" * 60)
